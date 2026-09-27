from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pytest
from pypdf import PdfWriter


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "99 System" / "Scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from vault_core import (  # noqa: E402
    build_alias_registry,
    extract_personal_block,
    normalize_alias,
    preserve_personal_block,
    validate_vault,
)
from init_transcript import initialize_transcript  # noqa: E402


def write_pdf(path: Path, pages: int = 2) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=100, height=100)
    with path.open("wb") as stream:
        writer.write(stream)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_source(vault: Path, digest: str, pages: int = 2) -> None:
    path = vault / "40 Sources" / "Source Notes" / "Source - Test.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
id: source-test
type: source
title: Source - Test
source_kind: slides
cfa_level: 1
curriculum_year: unknown
provider: Test
languages: [en]
source_file: "[[test.pdf]]"
page_count: {pages}
sha256: {digest}
status: trusted
tags: [cfa/level-1, source/slides]
---
# Source - Test
""",
        encoding="utf-8",
    )


def concept_text(title: str = "Balance Sheet", alias: str = "BS", page: int = 1) -> str:
    slug = title.casefold().replace(" ", "-")
    return f"""---
id: concept-{slug}
type: concept
title: {title}
aliases: [{alias}]
first_level: 1
topics: []
prerequisites: []
used_in: []
related: []
contrasts_with: []
source_notes:
  - "[[Source - Test]]"
status: trusted
tags: [cfa/level-1]
---
# {title}

> [!summary]
> A cited summary.[^test-p{page}]

## Level 1 - Foundation

A managed fact.[^test-p{page}]

## Connections

## Personal Notes
<!-- personal:start -->
My text.
<!-- personal:end -->

## Sources
[^test-p{page}]: [[test.pdf#page={page}|Test, PDF p. {page}]]
"""


def transcript_text(digest: str, pages: int = 2) -> str:
    headings = "\n\n".join(f"## PDF page {page}\n\nPage summary." for page in range(1, pages + 1))
    return f"""---
id: transcript-test
type: transcript
title: Transcript - Test
source_note: "[[Source - Test]]"
source_file: "[[test.pdf]]"
source_sha256: {digest}
page_count: {pages}
extraction_method: visual-structured-transcription
languages: [en]
status: untrusted
tags: [source/transcript]
---
# Transcript - Test

{headings}
"""


@pytest.fixture
def valid_vault(tmp_path: Path) -> Path:
    pdf = tmp_path / "40 Sources" / "PDFs" / "test.pdf"
    digest = write_pdf(pdf)
    write_source(tmp_path, digest)
    concept = tmp_path / "20 Concepts" / "Balance Sheet.md"
    concept.parent.mkdir(parents=True, exist_ok=True)
    concept.write_text(concept_text(), encoding="utf-8")
    return tmp_path


def issue_codes(vault: Path) -> set[str]:
    return {issue.code for issue in validate_vault(vault)}


def test_alias_normalization() -> None:
    assert normalize_alias("P/E Ratio") == normalize_alias("PE-ratio")
    assert normalize_alias("资产 负债表") == normalize_alias("资产负债表")


def test_valid_fixture_has_no_issues(valid_vault: Path) -> None:
    assert validate_vault(valid_vault) == []


def test_output_artifacts_are_outside_vault_validation(valid_vault: Path) -> None:
    artifact = valid_vault / "output" / "draft.md"
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_text("No vault frontmatter required here.\n", encoding="utf-8")
    assert validate_vault(valid_vault) == []


def test_duplicate_alias_is_rejected(valid_vault: Path) -> None:
    second = valid_vault / "20 Concepts" / "Bond Structure.md"
    second.write_text(concept_text("Bond Structure", "BS"), encoding="utf-8")
    assert "duplicate-alias" in issue_codes(valid_vault)


def test_alias_cannot_collide_with_another_concept_title(valid_vault: Path) -> None:
    second = valid_vault / "20 Concepts" / "BS.md"
    second.write_text(concept_text("BS", "Statement Alias"), encoding="utf-8")
    assert "duplicate-alias" in issue_codes(valid_vault)


def test_generated_alias_registry_resolves_bs(valid_vault: Path) -> None:
    registry = build_alias_registry(valid_vault)
    assert "| `bs` | BS | [[Balance Sheet]] |" in registry
    assert "Do not edit it manually" in registry


def test_broken_link_is_rejected(valid_vault: Path) -> None:
    path = valid_vault / "20 Concepts" / "Balance Sheet.md"
    path.write_text(path.read_text(encoding="utf-8").replace("## Connections", "## Connections\n\n[[Missing Note]]"), encoding="utf-8")
    assert "broken-link" in issue_codes(valid_vault)


def test_invalid_pdf_page_is_rejected(valid_vault: Path) -> None:
    path = valid_vault / "20 Concepts" / "Balance Sheet.md"
    path.write_text(concept_text(page=3), encoding="utf-8")
    assert "citation-page" in issue_codes(valid_vault)


def test_mismatched_level_tag_is_rejected(valid_vault: Path) -> None:
    path = valid_vault / "20 Concepts" / "Balance Sheet.md"
    path.write_text(path.read_text(encoding="utf-8").replace("cfa/level-1", "cfa/level-2"), encoding="utf-8")
    assert "level-tags" in issue_codes(valid_vault)


def test_uncited_managed_block_is_rejected(valid_vault: Path) -> None:
    path = valid_vault / "20 Concepts" / "Balance Sheet.md"
    path.write_text(path.read_text(encoding="utf-8").replace("A managed fact.[^test-p1]", "A managed fact."), encoding="utf-8")
    assert "uncited-claim" in issue_codes(valid_vault)


def test_modified_source_hash_is_rejected(valid_vault: Path) -> None:
    pdf = valid_vault / "40 Sources" / "PDFs" / "test.pdf"
    pdf.write_bytes(pdf.read_bytes() + b"changed")
    assert "source-hash" in issue_codes(valid_vault)


def test_valid_page_separated_transcript(valid_vault: Path) -> None:
    pdf = valid_vault / "40 Sources" / "PDFs" / "test.pdf"
    transcript = valid_vault / "40 Sources" / "Transcripts" / "Transcript - Test.md"
    transcript.parent.mkdir(parents=True, exist_ok=True)
    transcript.write_text(transcript_text(hashlib.sha256(pdf.read_bytes()).hexdigest()), encoding="utf-8")
    assert validate_vault(valid_vault) == []


def test_transcript_requires_complete_ordered_pages(valid_vault: Path) -> None:
    pdf = valid_vault / "40 Sources" / "PDFs" / "test.pdf"
    transcript = valid_vault / "40 Sources" / "Transcripts" / "Transcript - Test.md"
    transcript.parent.mkdir(parents=True, exist_ok=True)
    text = transcript_text(hashlib.sha256(pdf.read_bytes()).hexdigest()).replace("## PDF page 2", "## PDF page 3")
    transcript.write_text(text, encoding="utf-8")
    assert "transcript-pages" in issue_codes(valid_vault)


def test_initialize_transcript_from_registered_source(valid_vault: Path) -> None:
    transcript = initialize_transcript(valid_vault, "Source - Test")
    text = transcript.read_text(encoding="utf-8")
    assert "coverage_status: skeleton" in text
    assert "## PDF page 1" in text
    assert "## PDF page 2" in text
    assert validate_vault(valid_vault) == []


def test_personal_block_is_preserved_byte_for_byte() -> None:
    existing = "before\n<!-- personal:start -->\nMy private note.\n<!-- personal:end -->\nafter"
    replacement = "new\n<!-- personal:start -->\nAgent text.\n<!-- personal:end -->\nend"
    merged = preserve_personal_block(existing, replacement)
    assert extract_personal_block(merged) == extract_personal_block(existing)
    assert "Agent text" not in merged


def test_simulated_level_two_stays_in_proposal(valid_vault: Path) -> None:
    concept = valid_vault / "20 Concepts" / "Balance Sheet.md"
    original = concept.read_text(encoding="utf-8")
    proposal = valid_vault / "90 Inbox" / "Proposals" / "Balance Sheet - Level 2.md"
    proposal.parent.mkdir(parents=True, exist_ok=True)
    proposal.write_text(
        """---
id: proposal-balance-sheet-level-2
type: proposal
title: Balance Sheet - Level 2 Extension
target: "[[Balance Sheet]]"
change_type: level-extension
status: pending-review
tags: [cfa/level-2]
---
# Proposed Level 2 extension
""",
        encoding="utf-8",
    )
    assert concept.read_text(encoding="utf-8") == original
    assert proposal.exists()


def test_approved_level_two_merge_preserves_personal_notes(valid_vault: Path) -> None:
    concept = valid_vault / "20 Concepts" / "Balance Sheet.md"
    existing = concept.read_text(encoding="utf-8")
    proposed = existing.replace(
        "tags: [cfa/level-1]",
        "tags: [cfa/level-1, cfa/level-2]",
    ).replace(
        "## Connections",
        "## Level 2 - Extensions\n\nAn approved extension.[^test-p1]\n\n## Connections",
    ).replace("My text.", "Agent must not replace this.")
    merged = preserve_personal_block(existing, proposed)
    concept.write_text(merged, encoding="utf-8")

    assert "## Level 2 - Extensions" in merged
    assert "cfa/level-2" in merged
    assert extract_personal_block(merged) == extract_personal_block(existing)
    assert validate_vault(valid_vault) == []
