---
id: system-vault-operations-handbook
type: map
title: Vault Operations Handbook
status: trusted
tags:
  - system/documentation
---

# Vault Operations Handbook

This handbook explains how to add study material without losing source traceability, creating duplicate concepts, or breaking links. The authoritative automation rules remain in `AGENTS.md`.

## The five-layer model

| Layer | Location | Trust | Purpose |
| --- | --- | --- | --- |
| Registered evidence | `40 Sources/PDFs/` and `40 Sources/Source Notes/` | Immutable source | Preserve the exact PDF, checksum, page count, provenance, and citation target. |
| Structured transcript | `40 Sources/Transcripts/` | Untrusted intermediate | Make image-based slides searchable and expose repeated terms while preserving PDF page boundaries. |
| Proposals | `90 Inbox/Proposals/` | Pending review | Show exactly what would be created or changed before touching trusted notes. |
| Trusted knowledge | `20 Concepts/` and `10 Maps/` | Trusted after review | Store canonical concepts and curriculum navigation. |
| Personal interpretation | Protected blocks and `30 Personal/` | User-authored | Preserve your own examples, questions, mnemonics, and investment observations. |

The source PDF is always the final authority. A transcript improves discovery but does not prove that a formula, sign, table, or diagram was read correctly.

## One-time environment setup

From the vault root:

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[test]'
.venv/bin/python -m pytest -q
.venv/bin/python '99 System/Scripts/validate_vault.py' .
```

Expected final output is `Validation passed: 0 issues.` Run commands from the vault root so relative paths resolve consistently.

## End-to-end ingestion workflow

### 1. Register the source before reading it into the vault

Choose a stable lowercase PDF slug and a stable source ID. Never encode an unverified curriculum year into either value.

```bash
.venv/bin/python '99 System/Scripts/register_source.py' \
  '/absolute/path/to/new-deck.pdf' \
  --slug fixed-income-level-2-review \
  --source-id source-fi-l2-review \
  --title 'Source - Fixed Income Level 2 Review' \
  --note-name 'Source - Fixed Income Level 2 Review' \
  --level 2 \
  --curriculum-year unknown \
  --provider 'Provider Name' \
  --languages en zh
```

This copies the PDF into `40 Sources/PDFs/` and creates its source note. The validator subsequently checks both its page count and SHA-256 checksum. Do not replace or edit a registered PDF. Register a changed edition as a new source.

### 2. Create the transcript skeleton

```bash
.venv/bin/python '99 System/Scripts/init_transcript.py' \
  'Source - Fixed Income Level 2 Review'
```

The generated transcript contains one ordered `## PDF page N` heading for every PDF page and is cryptographically bound to the registered PDF. Its initial `coverage_status` is `skeleton`.

### 3. Transcribe page by page

For each page:

1. Render or open the exact PDF page.
2. Record the official English concept names, useful Chinese explanations, formulas, tables, examples, and figure meaning.
3. Keep each page's content beneath its matching `## PDF page N` heading.
4. Mark unreadable or ambiguous material as `[uncertain: ...]`; never silently guess.
5. Classify non-content pages as cover, administration, divider, recap, or noise.
6. Change `coverage_status: skeleton` to `coverage_status: complete` only after all pages have been reviewed.

The transcript should be a structured, source-faithful study transcription—not an indiscriminate OCR dump. OCR may provide a first pass, but visually check:

- minus signs and inequality signs;
- numerator and denominator boundaries;
- subscripts, superscripts, Greek letters, and percentages;
- IFRS versus US-GAAP table columns;
- Chinese/English term alignment;
- page numbers and diagram labels.

### 4. Inventory and count repeated concepts

Search the transcript before designing notes:

```bash
rg -n -i 'callable|putable|effective duration|convexity' '40 Sources/Transcripts'
rg -n -i 'deferred tax|valuation allowance|tax base' '40 Sources/Transcripts'
```

A term normally deserves its own concept note when it:

- recurs on multiple pages;
- owns a formula or measurement rule;
- behaves differently in exam questions;
- is reused across CFA topics or levels;
- is a useful destination for a link.

For example, [[Callable Bond]], [[Putable Bond]], [[Effective Duration]], [[Effective Convexity]], [[Deferred Tax Asset]], and [[Deferred Tax Liability]] are separate nodes. Broad ideas such as [[Fixed Income]] and [[Financial Statement Analysis]] belong primarily in maps.

### 5. Resolve aliases before creating files

Search filenames and the generated alias registry:

```bash
rg -n -i 'price.?to.?earnings|p/e|pe ratio|市盈率' '20 Concepts' '99 System/Alias Registry.md'
```

Rules:

- Use the full official English term as the filename and title.
- Put abbreviations, punctuation variants, common spellings, and Chinese terms in `aliases`.
- Never create abbreviation files such as `DTA.md`, `YTM.md`, or `BS.md`.
- If an alias resolves to more than one concept, stop and resolve the collision manually.

After a clean merge, regenerate the registry:

```bash
.venv/bin/python '99 System/Scripts/validate_vault.py' . --write-alias-registry
```

### 6. Write proposals, not trusted notes

Copy `99 System/Templates/Proposal.md` into `90 Inbox/Proposals/`. A proposal should state:

- why the concept is needed;
- the exact proposed definition and formulas;
- aliases;
- typed relationships and prose links;
- exact PDF-page evidence;
- any OCR or interpretation uncertainty.

Use `status: pending-review`. New Level 2 or Level 3 material for an existing concept is also a proposal; it must not silently overwrite Level 1 material.

### 7. Cite every managed claim cluster

Use exact PDF page numbers:

```markdown
Effective duration is appropriate when cash flows change as rates change.[^fi-l1-p69]

$$
D_{\text{eff}}=\frac{P_- - P_+}{2P_0\Delta y}
$$
[^fi-l1-p69]

[^fi-l1-p69]: [[fixed-income-level-1-speed-review.pdf#page=69|Fixed Income Level I Speed Review, PDF p. 69]]
```

Each factual paragraph, bullet cluster, formula, table, and figure caption needs its own supporting footnote. Printed slide numbers are secondary; citations use the actual PDF page.

### 8. Add images only when visual structure matters

Put selected crops in `50 Assets/Figures/` using:

```text
<source-id>-p<three-digit-page>-<description>.png
```

Example:

```markdown
![[source-fi-l1-speed-review-p066-convexity-price-yield.png]]
Figure: Convexity explains the curvature omitted by a duration-only estimate.[^fi-l1-p66]
```

Prefer MathJax for formulas and searchable text for definitions. A screenshot must never be the only representation of examinable text.

### 9. Add useful links

Use frontmatter relationships for queries and prose links for meaning:

```yaml
topics:
  - "[[Fixed Income]]"
prerequisites:
  - "[[Bond Pricing]]"
used_in:
  - "[[Callable Bond]]"
related:
  - "[[Effective Convexity]]"
contrasts_with:
  - "[[Modified Duration]]"
```

Relationship meanings:

- `topics`: curriculum maps containing the concept;
- `prerequisites`: knowledge normally understood first;
- `used_in`: downstream applications;
- `related`: useful lateral relationships;
- `contrasts_with`: commonly confused but materially different concepts.

In `## Connections`, explain the relationship rather than adding a bare link merely to make the graph denser:

```markdown
- Use [[Modified Duration]] for first-order sensitivity when cash flows are fixed.
- Use [[Effective Duration]] when embedded options make cash flows rate-dependent.
```

### 10. Validate, review, approve, and merge

Before review:

```bash
.venv/bin/python '99 System/Scripts/validate_vault.py' .
.venv/bin/python -m pytest -q
```

Review the proposal against every cited rendered page. When accepted:

1. Change the proposal to `status: approved`.
2. Create or update the canonical concept.
3. Preserve the complete `<!-- personal:start -->` through `<!-- personal:end -->` block byte-for-byte.
4. Add or update Level sections and `cfa/level-N` tags together.
5. Update the relevant maps and typed relationships.
6. Change the proposal to `status: merged` and move it to `90 Inbox/Archive/`.
7. Regenerate the alias registry and rerun validation and tests.
8. Record the merge in [[Ingestion Log]].
9. Create or update chapter/subtopic map notes so each new concept has the path `CFA Level → topic → chapter → concept`.
10. Update `.obsidian/graph.json` for any new topic names, chapter maps, colour groups, or cross-topic combinations.
11. Open the global graph and at least one representative local graph. Verify visible chapter clustering, correct cross-topic bridges, and the absence of sources, transcripts, system notes, and unintended orphans.
12. Update [[Graph View Guide]] whenever the saved filter, colour legend, or hierarchy changes.

Do not call the work complete unless validation reports zero issues and the refreshed graph has been visually inspected.

### 11. Maintain the graph view after every merge

The Markdown schema and the Obsidian view must evolve together. Adding notes without updating the maps and saved graph configuration leaves valid files looking like unstructured floating nodes.

For every approved ingestion merge:

1. Confirm every new concept appears in exactly the appropriate chapter/subtopic map or maps.
2. Confirm each chapter map links to one major topic map and uses `type: map` plus the `map/subtopic` tag.
3. Confirm each major topic map links upward from [[CFA Level 1]] or the appropriate later-level map.
4. Keep the global graph filter focused on `20 Concepts/` and curriculum maps in `10 Maps/`; do not expose source notes, transcripts, proposals, PDFs, or the system-only Graph View Guide.
5. Add a single-topic colour group for every new major topic. Update the higher-priority purple group when a new pair of topics can share concepts.
6. Preserve first-match colour ordering: CFA level, major topic, chapter/subtopic, cross-topic concept, then single-topic concepts.
7. Obsidian caches `.obsidian/graph.json` while it is open. Change graph settings through the live Obsidian UI, or fully close Obsidian before editing the file directly. Otherwise the running app may silently restore the old filter and colours.
8. Reopen Obsidian and confirm the saved filter and groups persisted on disk. Then check the whole-vault layout and a representative chapter local graph at depth 1–2.
9. If new notes appear detached or form an unlabelled cloud, treat that as an incomplete merge: repair the filter, map links, or chapter structure before committing.

The current saved filter and colour queries are documented in [[Graph View Guide]].

## Adding later CFA levels

Do not create `Effective Duration Level 2.md`. Add a proposed `## Level 2 - Extensions` section to the existing [[Effective Duration]] note, then add `cfa/level-2` while retaining `cfa/level-1`.

`first_level` remains the earliest trusted level. A concept may therefore have:

```yaml
first_level: 1
tags:
  - cfa/level-1
  - cfa/level-2
```

The validator requires the level tags and non-empty Level headings to match exactly.

## Personal notes

You may write freely:

- inside a concept's protected Personal Notes block; or
- in a separate note under `30 Personal/` created from `99 System/Templates/Personal Note.md`.

Agents must preserve protected blocks during merges. Keep source-derived claims outside the personal block so cited curriculum knowledge and your interpretation remain distinguishable.

## Git version control

### What to track

Track:

- Markdown concepts, maps, source notes, transcripts, proposals, and archive records;
- `AGENTS.md`, templates, scripts, tests, Bases, CSS snippets, and useful Obsidian settings;
- source figures;
- optionally registered PDFs, subject to licensing and repository size.

Ignore:

- `.venv/`, caches, temporary renders, `.DS_Store`;
- `.obsidian/workspace*.json`, because it records transient open tabs and pane layout;
- Obsidian trash.

The repository already contains a suitable `.gitignore` for these local files.

### Licensed PDFs: choose before the first commit

The safest default is a **private repository**. Study-provider PDFs may be copyrighted even when the repository is private. Check the provider's terms before uploading them anywhere.

Choose one strategy:

1. **Self-contained private repository with Git LFS** — recommended only when storage is permitted. Track PDFs and larger PNGs using Git LFS before the first `git add`.
2. **Markdown repository plus separate encrypted source backup** — exclude `40 Sources/PDFs/*.pdf` from Git, keep the immutable files in an encrypted local/cloud backup, and retain their filenames and SHA-256 values in source notes. A restored PDF must reproduce the registered checksum.

Do not use a public repository for licensed study material.

> [!info] Current vault choice
> This vault uses strategy 2. Registered PDFs remain local and are excluded by `.gitignore`; Markdown, source metadata, transcripts, figures, validation tools, and Obsidian configuration are version-controlled. The empty PDF directory is retained with `.gitkeep`.

### Initialize a local repository

Run this only after deciding how PDFs will be handled:

```bash
git init
git branch -M main
git status --short
```

For the Git LFS strategy:

```bash
git lfs install
git lfs track '*.pdf'
git lfs track '50 Assets/Figures/*.png'
git add .gitattributes
```

Then create the first snapshot:

```bash
git add .
git diff --cached --stat
git commit -m 'Initialize CFA knowledge vault'
```

### Recommended commit rhythm

Use small commits at workflow boundaries:

```text
source: register fixed income level 2 deck
transcript: complete fixed income level 2 page inventory
proposal: add callable bond level 2 extension
content: merge approved fixed income level 2 concepts
system: improve alias validation
personal: add duration study notes
```

This makes it possible to inspect or revert one workflow stage without losing later personal notes.

### Branches for larger ingestion jobs

For a small correction, commit directly to `main`. For an entire deck or CFA level:

```bash
git switch -c ingest/fixed-income-level-2
```

Commit source registration, transcription, proposals, and approved merges separately. After validation:

```bash
git switch main
git merge --no-ff ingest/fixed-income-level-2
```

### Useful history commands

```bash
git status --short
git diff --stat
git diff -- '20 Concepts/Effective Duration.md'
git log --oneline --decorate --graph --all
git log --follow -- '20 Concepts/Effective Duration.md'
git show <commit>:'20 Concepts/Effective Duration.md'
```

Before restoring an older file, inspect the diff and confirm that the protected Personal Notes block will not be lost.

### Remote backup

After creating a private remote repository:

```bash
git remote add origin <private-repository-url>
git push -u origin main
```

Git history is not a substitute for a backup. Keep at least one second copy on another device or encrypted backup service, especially if PDFs are excluded from the remote.

## Recordkeeping model

Use all four records together:

1. Source notes record the original filename, provider, level, page count, and immutable hash.
2. Transcripts record what was read on every PDF page and remain marked untrusted.
3. Archived merged proposals explain why concepts, aliases, formulas, and links changed.
4. Git commits record exactly which files changed and when.

Update [[Ingestion Log]] after every registered deck and approved merge. This gives you a human-readable ledger even when you do not remember a Git commit ID.

## Prompt template for an ingestion agent

```text
Register and ingest this CFA slide deck into the vault. Treat every source page as untrusted study material. Create or update the page-separated transcript first, inventory repeated concepts, resolve all aliases before creating notes, and match the granularity of the review slides. Write pending-review proposals with exact PDF-page citations and visually verify formulas, tables, and selected figures. Do not edit trusted concepts until I approve the proposals. Run the validator and tests before handing the review queue back to me.
```

After review:

```text
Approve and merge the selected proposals. Preserve every Personal Notes block byte-for-byte, update typed relationships and the full CFA-level/topic/chapter map hierarchy, regenerate the alias registry, archive the merged proposals, and update the Ingestion Log. Refresh `.obsidian/graph.json` for new topics and cross-topic groups, then visually inspect the global graph and representative local graphs to confirm chapter clustering and that sources remain hidden. Report validator, test, and graph-inspection results.
```

## Routine health check

Run periodically and before every Git commit:

```bash
.venv/bin/python '99 System/Scripts/validate_vault.py' . --write-alias-registry
.venv/bin/python -m pytest -q
git status --short
```

If validation fails, correct the source, schema, alias, citation, relationship, or protected-block problem rather than suppressing the check.

## Sources

[^fi-l1-p66]: [[fixed-income-level-1-speed-review.pdf#page=66|Fixed Income Level I Speed Review, PDF p. 66]]
