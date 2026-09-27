#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import yaml

from vault_core import pdf_page_count, sha256_file


def wikilink(value: str) -> str:
    return f"[[{value}]]"


def register_source(args: argparse.Namespace) -> tuple[Path, Path]:
    vault = args.vault.resolve()
    source = args.source.resolve()
    if not source.is_file():
        raise FileNotFoundError(source)

    pdf_directory = vault / "40 Sources" / "PDFs"
    note_directory = vault / "40 Sources" / "Source Notes"
    pdf_directory.mkdir(parents=True, exist_ok=True)
    note_directory.mkdir(parents=True, exist_ok=True)

    destination = pdf_directory / f"{args.slug}.pdf"
    if destination.exists():
        if sha256_file(destination) != sha256_file(source):
            raise FileExistsError(
                f"{destination} already exists with different content; registered PDFs are immutable"
            )
    else:
        shutil.copy2(source, destination)

    metadata = {
        "id": args.source_id,
        "type": "source",
        "title": args.title,
        "aliases": [source.name],
        "source_kind": "slides",
        "cfa_level": args.level,
        "curriculum_year": args.curriculum_year,
        "provider": args.provider,
        "languages": args.languages,
        "source_file": wikilink(destination.name),
        "original_filename": source.name,
        "page_count": pdf_page_count(destination),
        "sha256": sha256_file(destination),
        "status": "trusted",
        "tags": [f"cfa/level-{args.level}", "source/slides"],
    }
    note_path = note_directory / f"{args.note_name}.md"
    if note_path.exists():
        raise FileExistsError(note_path)
    frontmatter = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True).strip()
    body = (
        f"---\n{frontmatter}\n---\n\n"
        f"# {args.title}\n\n"
        "> [!summary]\n"
        "> Immutable registered source for page-addressable citations. Curriculum year remains unknown unless independently confirmed.\n\n"
        "## Source file\n\n"
        f"![[{destination.name}#page=1]]\n\n"
        "## Pilot coverage\n\n"
        "To be recorded after page inventory and visual review.\n"
    )
    note_path.write_text(body, encoding="utf-8")
    return destination, note_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Register an immutable PDF source in the CFA vault")
    parser.add_argument("source", type=Path)
    parser.add_argument("--vault", type=Path, default=Path.cwd())
    parser.add_argument("--slug", required=True)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--note-name", required=True)
    parser.add_argument("--level", type=int, choices=(1, 2, 3), required=True)
    parser.add_argument("--curriculum-year", default="unknown")
    parser.add_argument("--provider", required=True)
    parser.add_argument("--languages", nargs="+", default=["en", "zh"])
    return parser


if __name__ == "__main__":
    pdf_path, note_path = register_source(build_parser().parse_args())
    print(f"Registered PDF: {pdf_path}")
    print(f"Created source note: {note_path}")
