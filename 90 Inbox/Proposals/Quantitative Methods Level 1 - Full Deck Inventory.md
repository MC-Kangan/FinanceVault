---
id: proposal-quant-l1-full-deck-inventory
type: proposal
title: Quantitative Methods Level 1 - Full Deck Inventory
target: Quantitative Methods
change_type: source-inventory
status: pending-review
tags:
  - cfa/level-1
---

# Quantitative Methods Level 1 - Full Deck Inventory

## Rationale

This inventory separates reusable concepts, formulas, comparisons, and workflows from dividers, recaps, administration, and promotional material. The full page-separated transcript is an untrusted search aid; the PDF remains authoritative.

## Page inventory

| PDF pages | Classification | Proposed handling |
| --- | --- | --- |
| 1–2 | cover / promotion | register source; exclude promotional material |
| 3 | divider | navigation only |
| 4–10 | concepts, formulas, applications, recap | Interest Rates and Investment Returns chapter |
| 11 | divider | navigation only |
| 12–21 | concepts, formulas, diagrams, recap | Descriptive Statistics chapter |
| 22 | divider | navigation only |
| 23–31 | concepts, formulas, distributions, recap | Probability Foundations chapter |
| 32 | cross-section roadmap | navigation and recurrence check only |
| 33 | divider | navigation only |
| 34–50 | concepts, formulas, comparisons, tests, recap | Sampling and Inference chapter |
| 51 | divider | navigation only |
| 52–60 | concepts, formulas, tables, recap | Simple Linear Regression chapter |
| 61 | divider | navigation only |
| 62–67 | concepts, classifications, recap | Big Data Analysis chapter |
| 68 | closing | exclude as noise |

The six content chapters jointly cover every reusable study page in the deck.[^quant-inventory-p4][^quant-inventory-p67]

## Proposed navigation

- Create the top-level topic map `Quantitative Methods` and add it to [[CFA Level 1]].
- Create six chapter maps: `Quant - Interest Rates and Investment Returns`, `Quant - Descriptive Statistics`, `Quant - Probability Foundations`, `Quant - Sampling and Inference`, `Quant - Simple Linear Regression`, and `Quant - Big Data Analysis`.
- Keep canonical concepts flat in `20 Concepts/`; chapter maps provide the visible clustering in graph view.
- Reuse existing concepts such as [[Holding Period Return]], [[Expected Return]], [[Variance]], [[Standard Deviation]], [[Correlation]], [[Portfolio Expected Return]], and [[Portfolio Variance]] rather than creating duplicates.
- After approval and merge, update `.obsidian/graph.json` so the new topic and chapter maps use the existing map colours and source/transcript nodes remain excluded from the graph.

## Review checklist

- [x] Immutable source hash and 68-page count registered.
- [x] Full page-separated transcript completed with OCR uncertainty markers.
- [x] Representative pages from all six chapters visually inspected.
- [x] Existing canonical filenames searched before proposing reusable nodes.
- [x] Trusted concept notes and maps remain unchanged.
- [ ] User approves page classification and chapter boundaries.
- [ ] Every formula-heavy source page is visually checked during merge.
- [ ] Final graph clustering is visually inspected after merge.

## Evidence

[^quant-inventory-p4]: [[quantitative-methods-level-1-speed-review.pdf#page=4|Quantitative Methods Level I Speed Review, PDF p. 4]]
[^quant-inventory-p67]: [[quantitative-methods-level-1-speed-review.pdf#page=67|Quantitative Methods Level I Speed Review, PDF p. 67]]
