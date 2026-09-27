#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from vault_core import load_note


def _wikilink_target(value: object) -> str:
    if not isinstance(value, str) or not value.startswith("[[") or not value.endswith("]]" ):
        raise ValueError("source_file must be a simple [[registered-file.pdf]] wikilink")
    return value[2:-2]


def initialize_transcript(vault: Path, source_note_name: str) -> Path:
    vault = vault.resolve()
    source_note_path = vault / "40 Sources" / "Source Notes" / f"{source_note_name}.md"
    source = load_note(source_note_path)
    metadata = source.metadata
    if metadata.get("type") != "source":
        raise ValueError(f"{source_note_path} is not a source note")

    source_title = str(metadata["title"])
    display_title = source_title.removeprefix("Source - ")
    transcript_title = f"Transcript - {display_title}"
    output = vault / "40 Sources" / "Transcripts" / f"{transcript_title}.md"
    if output.exists():
        raise FileExistsError(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    page_count = int(metadata["page_count"])
    transcript_metadata = {
        "id": f"transcript-{str(metadata['id']).removeprefix('source-')}",
        "type": "transcript",
        "title": transcript_title,
        "source_note": f"[[{source_title}]]",
        "source_file": f"[[{_wikilink_target(metadata['source_file'])}]]",
        "source_sha256": metadata["sha256"],
        "page_count": page_count,
        "extraction_method": "visual-structured-transcription",
        "coverage_status": "skeleton",
        "languages": metadata["languages"],
        "status": "untrusted",
        "tags": [f"cfa/level-{metadata['cfa_level']}", "source/transcript"],
    }
    frontmatter = yaml.safe_dump(
        transcript_metadata,
        sort_keys=False,
        allow_unicode=True,
    ).strip()
    lines = [
        "---",
        frontmatter,
        "---",
        "",
        f"# {transcript_title}",
        "",
        "> [!warning] Untrusted intermediate",
        "> Use this text for search, recurrence detection, aliases, and candidate discovery. Verify every promoted claim, formula, table, and figure against the rendered PDF page.",
        "",
    ]
    for page in range(1, page_count + 1):
        lines.extend(
            [
                f"## PDF page {page}",
                "",
                f"<!-- Transcribe PDF page {page}. Preserve uncertainty explicitly; do not infer missing text. -->",
                "",
            ]
        )
    output.write_text("\n".join(lines), encoding="utf-8")
    return output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a page-separated transcript skeleton for a registered source"
    )
    parser.add_argument(
        "source_note_name",
        help="source note filename without .md, for example 'Source - Fixed Income Level 1 Speed Review'",
    )
    parser.add_argument("--vault", type=Path, default=Path.cwd())
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    transcript = initialize_transcript(args.vault, args.source_note_name)
    print(f"Created transcript skeleton: {transcript}")
