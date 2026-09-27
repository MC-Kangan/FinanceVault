from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml
from pypdf import PdfReader


FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
WIKILINK_RE = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
CITATION_DEFINITION_RE = re.compile(
    r"^\[\^(?P<key>[^\]]+)\]:\s*\[\[(?P<target>[^\]#|]+\.pdf)#page=(?P<page>\d+)\|(?P<label>[^\]]+)\]\]\s*$",
    re.MULTILINE | re.IGNORECASE,
)
CITATION_REF_RE = re.compile(r"\[\^([^\]]+)\]")
LEVEL_HEADING_RE = re.compile(r"^##\s+Level\s+([123])\b", re.MULTILINE)
FIGURE_NAME_RE = re.compile(r"^(?P<source_id>source-.+)-p(?P<page>\d{3})-[a-z0-9][a-z0-9-]*\.png$")
PERSONAL_BLOCK_RE = re.compile(
    r"<!-- personal:start -->(.*?)<!-- personal:end -->", re.DOTALL
)
TRANSCRIPT_PAGE_RE = re.compile(r"^## PDF page (?P<page>\d+)$", re.MULTILINE)


@dataclass(frozen=True)
class Note:
    path: Path
    metadata: dict[str, Any]
    body: str
    raw: str


@dataclass(frozen=True)
class Issue:
    code: str
    path: Path
    message: str

    def __str__(self) -> str:
        return f"{self.code}: {self.path}: {self.message}"


def split_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(raw)
    if not match:
        raise ValueError("missing YAML frontmatter")
    metadata = yaml.safe_load(match.group(1)) or {}
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    return metadata, raw[match.end() :]


def load_note(path: Path) -> Note:
    raw = path.read_text(encoding="utf-8")
    metadata, body = split_frontmatter(raw)
    return Note(path=path, metadata=metadata, body=body, raw=raw)


def iter_notes(vault: Path) -> Iterable[Path]:
    for path in sorted(vault.rglob("*.md")):
        relative = path.relative_to(vault)
        if relative == Path("AGENTS.md"):
            continue
        if relative.parts and relative.parts[0] in {".venv", "tmp"}:
            continue
        if relative.parts[:2] == ("99 System", "Templates"):
            continue
        if ".pytest_cache" in relative.parts or "__pycache__" in relative.parts:
            continue
        yield path


def normalize_alias(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return "".join(
        character
        for character in normalized
        if unicodedata.category(character)[0] in {"L", "N"}
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def extract_personal_block(raw: str) -> str:
    match = PERSONAL_BLOCK_RE.search(raw)
    if not match:
        raise ValueError("Personal Notes markers are missing")
    return match.group(0)


def preserve_personal_block(existing: str, replacement: str) -> str:
    """Return replacement content with the existing protected block restored byte-for-byte."""
    existing_block = extract_personal_block(existing)
    if not PERSONAL_BLOCK_RE.search(replacement):
        raise ValueError("replacement Personal Notes markers are missing")
    return PERSONAL_BLOCK_RE.sub(lambda _: existing_block, replacement, count=1)


def build_alias_registry(vault: Path) -> str:
    """Build a generated, human-readable index from canonical concept metadata."""
    rows: list[tuple[str, str, str]] = []
    for path in iter_notes(vault.resolve()):
        note = load_note(path)
        if note.metadata.get("type") != "concept":
            continue
        title = str(note.metadata["title"])
        names = [title, *_list_value(note.metadata, "aliases")]
        seen: set[str] = set()
        for name in names:
            if not isinstance(name, str):
                continue
            key = normalize_alias(name)
            if key in seen:
                continue
            seen.add(key)
            rows.append((key, name, title))

    rows.sort(key=lambda row: (row[0], row[2], row[1]))
    lines = [
        "---",
        "id: system-alias-registry",
        "type: map",
        "title: Alias Registry",
        "status: generated",
        "tags:",
        "  - system/generated",
        "---",
        "",
        "# Alias Registry",
        "",
        "> [!info] Generated file",
        "> This registry is generated from canonical concept frontmatter. Do not edit it manually.",
        "",
        "| Normalized key | Alias or title | Canonical concept |",
        "| --- | --- | --- |",
    ]
    for key, name, title in rows:
        safe_name = name.replace("|", "\\|")
        safe_title = title.replace("|", "\\|")
        lines.append(f"| `{key}` | {safe_name} | [[{safe_title}]] |")
    lines.append("")
    return "\n".join(lines)


def _list_value(metadata: dict[str, Any], key: str) -> list[Any]:
    value = metadata.get(key, [])
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def _link_target_from_property(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    match = WIKILINK_RE.fullmatch(value.strip())
    return match.group(1) if match else None


def _claim_blocks(body: str) -> list[str]:
    """Return summary and Level-section claim clusters that require citations."""
    lines = body.splitlines()
    blocks: list[str] = []
    current: list[str] = []
    in_managed = False
    in_sources = False
    in_code = False

    def flush() -> None:
        nonlocal current
        text = "\n".join(current).strip()
        current = []
        if not text:
            return
        meaningful = [
            line
            for line in text.splitlines()
            if line.strip()
            and not re.match(r"^\s*>?\s*\[![^\]]+\]", line)
            and not line.lstrip().startswith("<!--")
        ]
        if meaningful:
            blocks.append(text)

    for line in lines:
        if line.startswith("## Sources"):
            flush()
            in_sources = True
            in_managed = False
            continue
        if in_sources:
            continue
        if line.startswith("## "):
            flush()
            in_managed = bool(re.match(r"##\s+Level\s+[123]\b", line))
            continue
        if line.startswith("> [!summary]"):
            flush()
            in_managed = True
            current.append(line)
            continue
        if in_managed and line.startswith("# "):
            flush()
            in_managed = False
            continue
        if not in_managed:
            continue
        if line.strip().startswith("```"):
            in_code = not in_code
            current.append(line)
            continue
        if not in_code and line.startswith("### "):
            flush()
            continue
        if not in_code and not line.strip():
            flush()
            continue
        current.append(line)
    flush()
    return blocks


def validate_vault(vault: Path) -> list[Issue]:
    vault = vault.resolve()
    issues: list[Issue] = []
    notes: list[Note] = []

    for path in iter_notes(vault):
        try:
            notes.append(load_note(path))
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
            issues.append(Issue("frontmatter", path.relative_to(vault), str(error)))

    id_index: dict[str, Path] = {}
    note_targets: dict[str, Path] = {}
    alias_targets: dict[str, Path] = {}
    source_by_id: dict[str, tuple[Note, Path, int]] = {}

    for note in notes:
        relative = note.path.relative_to(vault)
        metadata = note.metadata
        note_type = metadata.get("type")
        note_id = metadata.get("id")
        title = metadata.get("title")

        if not isinstance(note_id, str) or not note_id:
            issues.append(Issue("schema", relative, "missing non-empty id"))
        elif note_id in id_index:
            issues.append(Issue("duplicate-id", relative, f"id also used by {id_index[note_id]}"))
        else:
            id_index[note_id] = relative

        if not isinstance(title, str) or not title:
            issues.append(Issue("schema", relative, "missing non-empty title"))
        else:
            note_targets[normalize_alias(title)] = relative
        note_targets[normalize_alias(note.path.stem)] = relative

        required: dict[str, set[str]] = {
            "concept": {
                "id", "type", "title", "aliases", "first_level", "topics",
                "prerequisites", "used_in", "related", "contrasts_with",
                "source_notes", "status", "tags",
            },
            "map": {"id", "type", "title", "status", "tags"},
            "source": {
                "id", "type", "title", "source_kind", "cfa_level",
                "curriculum_year", "provider", "languages", "source_file",
                "page_count", "sha256", "status", "tags",
            },
            "transcript": {
                "id", "type", "title", "source_note", "source_file",
                "source_sha256", "page_count", "extraction_method",
                "languages", "status", "tags",
            },
            "proposal": {
                "id", "type", "title", "target", "change_type", "status", "tags",
            },
            "personal": {"id", "type", "title", "status", "tags"},
        }
        if note_type not in required:
            issues.append(Issue("schema", relative, f"unsupported type {note_type!r}"))
        else:
            missing = sorted(required[note_type] - metadata.keys())
            if missing:
                issues.append(Issue("schema", relative, f"missing fields: {', '.join(missing)}"))

        if note_type == "concept":
            aliases = _list_value(metadata, "aliases")
            for alias in aliases:
                if not isinstance(alias, str) or not alias.strip():
                    issues.append(Issue("schema", relative, "aliases must be non-empty strings"))
            resolution_names = [
                value
                for value in [title, note.path.stem, *aliases]
                if isinstance(value, str) and value.strip()
            ]
            local_keys: set[str] = set()
            for name in resolution_names:
                key = normalize_alias(name)
                if key in local_keys:
                    continue
                local_keys.add(key)
                existing = alias_targets.get(key)
                if existing and existing != relative:
                    issues.append(Issue("duplicate-alias", relative, f"{name!r} also maps to {existing}"))
                else:
                    alias_targets[key] = relative
                    note_targets.setdefault(key, relative)

            tags = {str(tag) for tag in _list_value(metadata, "tags")}
            heading_levels = {int(level) for level in LEVEL_HEADING_RE.findall(note.body)}
            tagged_levels = {
                int(match.group(1))
                for tag in tags
                if (match := re.fullmatch(r"cfa/level-([123])", tag))
            }
            if heading_levels != tagged_levels:
                issues.append(
                    Issue(
                        "level-tags",
                        relative,
                        f"Level headings {sorted(heading_levels)} do not match tags {sorted(tagged_levels)}",
                    )
                )
            if heading_levels and metadata.get("first_level") != min(heading_levels):
                issues.append(Issue("first-level", relative, "first_level must equal earliest Level heading"))
            if len(PERSONAL_BLOCK_RE.findall(note.raw)) != 1:
                issues.append(Issue("personal-block", relative, "expected exactly one protected Personal Notes block"))
            for block in _claim_blocks(note.body):
                if not CITATION_REF_RE.search(block):
                    excerpt = re.sub(r"\s+", " ", block)[:100]
                    issues.append(Issue("uncited-claim", relative, f"managed claim lacks citation: {excerpt}"))

        if note_type == "proposal" and metadata.get("status") not in {
            "pending-review", "approved", "rejected", "merged"
        }:
            issues.append(Issue("proposal-status", relative, "invalid proposal status"))

        if note_type == "transcript":
            if metadata.get("status") != "untrusted":
                issues.append(Issue("transcript-status", relative, "transcripts must remain untrusted"))
            pages = [int(match.group("page")) for match in TRANSCRIPT_PAGE_RE.finditer(note.body)]
            declared_count = metadata.get("page_count")
            if isinstance(declared_count, int) and pages != list(range(1, declared_count + 1)):
                issues.append(
                    Issue(
                        "transcript-pages",
                        relative,
                        "page headings must be unique, ordered, and cover PDF pages 1 through page_count",
                    )
                )

    pdf_paths = {path.name: path for path in (vault / "40 Sources" / "PDFs").glob("*.pdf")}
    attachment_paths = {
        path.name: path
        for folder in (vault / "50 Assets").glob("*")
        if folder.is_dir()
        for path in folder.iterdir()
        if path.is_file()
    }

    for note in notes:
        if note.metadata.get("type") != "source":
            continue
        relative = note.path.relative_to(vault)
        target = _link_target_from_property(note.metadata.get("source_file"))
        filename = Path(target).name if target else ""
        pdf_path = pdf_paths.get(filename)
        if not pdf_path:
            issues.append(Issue("source-file", relative, f"PDF not found for source_file {target!r}"))
            continue
        actual_pages = pdf_page_count(pdf_path)
        actual_hash = sha256_file(pdf_path)
        if note.metadata.get("page_count") != actual_pages:
            issues.append(Issue("source-pages", relative, f"expected {actual_pages} pages"))
        if note.metadata.get("sha256") != actual_hash:
            issues.append(Issue("source-hash", relative, "source PDF hash differs from registered hash"))
        source_id = note.metadata.get("id")
        if isinstance(source_id, str):
            source_by_id[source_id] = (note, pdf_path, actual_pages)

    for note in notes:
        if note.metadata.get("type") != "transcript":
            continue
        relative = note.path.relative_to(vault)
        target = _link_target_from_property(note.metadata.get("source_file"))
        filename = Path(target).name if target else ""
        pdf_path = pdf_paths.get(filename)
        if not pdf_path:
            issues.append(Issue("transcript-source", relative, f"PDF not found for source_file {target!r}"))
            continue
        actual_pages = pdf_page_count(pdf_path)
        if note.metadata.get("page_count") != actual_pages:
            issues.append(Issue("transcript-pages", relative, f"expected {actual_pages} pages"))
        if note.metadata.get("source_sha256") != sha256_file(pdf_path):
            issues.append(Issue("transcript-hash", relative, "transcript is not bound to the current source PDF hash"))

    all_citation_keys: dict[Path, set[str]] = {}
    for note in notes:
        relative = note.path.relative_to(vault)
        definitions = {match.group("key"): match for match in CITATION_DEFINITION_RE.finditer(note.body)}
        refs = set(CITATION_REF_RE.findall(note.body))
        definition_keys = set(definitions)
        for key in sorted(refs - definition_keys):
            issues.append(Issue("citation-definition", relative, f"missing definition for [^{key}]"))
        for key in sorted(definition_keys - refs):
            issues.append(Issue("unused-citation", relative, f"unused citation definition [^{key}]"))
        for match in definitions.values():
            filename = Path(match.group("target")).name
            pdf_path = pdf_paths.get(filename)
            page = int(match.group("page"))
            if not pdf_path:
                issues.append(Issue("citation-target", relative, f"PDF {filename!r} not found"))
            elif page < 1 or page > pdf_page_count(pdf_path):
                issues.append(Issue("citation-page", relative, f"page {page} outside {filename}"))
        all_citation_keys[relative] = definition_keys

        for target in WIKILINK_RE.findall(note.raw):
            target = target.strip()
            if not target:
                continue
            filename = Path(target).name
            suffix = Path(filename).suffix.casefold()
            if suffix == ".pdf" and filename in pdf_paths:
                continue
            if suffix in {".png", ".jpg", ".jpeg", ".webp", ".svg"} and filename in attachment_paths:
                continue
            if suffix == ".base" and (vault / "99 System" / "Bases" / filename).exists():
                continue
            key = normalize_alias(Path(target).stem if suffix else target)
            if key not in note_targets:
                issues.append(Issue("broken-link", relative, f"unresolved wikilink [[{target}]]"))

    figures = list((vault / "50 Assets" / "Figures").glob("*.png"))
    combined_markdown = "\n".join(note.raw for note in notes)
    for figure in figures:
        match = FIGURE_NAME_RE.fullmatch(figure.name)
        relative = figure.relative_to(vault)
        if not match:
            issues.append(Issue("figure-name", relative, "figure filename lacks source/page provenance"))
            continue
        source_id = match.group("source_id")
        page = int(match.group("page"))
        source = source_by_id.get(source_id)
        if not source:
            issues.append(Issue("figure-source", relative, f"unknown source id {source_id}"))
        elif page < 1 or page > source[2]:
            issues.append(Issue("figure-page", relative, f"page {page} outside registered source"))
        embed = f"![[{figure.name}"
        position = combined_markdown.find(embed)
        if position < 0:
            issues.append(Issue("figure-unused", relative, "figure is not embedded in any note"))
        else:
            nearby = combined_markdown[position : position + 500]
            if not CITATION_REF_RE.search(nearby):
                issues.append(Issue("figure-citation", relative, "embedded figure lacks a nearby citation"))

    return issues
