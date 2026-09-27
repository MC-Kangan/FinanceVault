---
id: proposal-fi-l1-full-deck-inventory
type: proposal
title: Fixed Income Level 1 - Full Deck Inventory
target: "[[Fixed Income]]"
change_type: source-inventory
status: merged
tags:
  - cfa/level-1
---

# Fixed Income Level 1 - Full Deck Inventory

## Rationale

This proposal records the page-level triage completed before concept creation. It separates reusable concepts and formulas from recap pages and administrative noise so later ingestion remains selective rather than copying the deck wholesale.

## Page inventory

| PDF pages | Classification | Proposed handling |
| --- | --- | --- |
| 1-2 | cover and administration | exclude as noise |
| 3, 20, 39, 59, 79, 91 | section dividers | exclude as navigation-only slides |
| 4-16 | concept, formula, comparison, diagram | Bond Structure and Features bundle |
| 17-19 | recap maps | use only as a completeness check |
| 21-34 | concept, formula, comparison, diagram | Markets, Issuance, and Funding bundle |
| 35-38 | recap maps | use only as a completeness check |
| 40-54 | concept, formula, comparison, diagram | Valuation, Yield Measures, and Term Structure bundle |
| 55-58 | recap maps | use only as a completeness check |
| 60-73 | concept, formula, comparison, diagram | Interest Rate Risk Measures bundle |
| 74-78 | recap maps | use only as a completeness check |
| 80-88 | concept, formula, comparison, diagram | Credit Analysis and Seniority bundle |
| 89-90 | recap maps | use only as a completeness check |
| 92-102 | concept, formula, comparison, diagram | Securitization and Structured Products bundle |
| 103-104 | recap maps | use only as a completeness check |
| 105 | closing slide | exclude as noise |

The six content bundles jointly cover the reusable study material on PDF pages 4-16, 21-34, 40-54, 60-73, 80-88, and 92-102. Recap slides remain source navigation aids and are not proposed as separate notes.[^fi-inventory-p4][^fi-inventory-p104]

## Review notes

- All content pages listed above were visually inspected from rendered PDF pages; OCR was not used as authoritative evidence.
- Existing trusted pilot notes remain unchanged. Any overlapping material is described as a proposed update rather than rewritten in place.
- Curriculum year remains `unknown`.

## Review checklist

- [x] Source hash and page count are already registered.
- [x] Every proposed content page was visually inspected.
- [x] Formula-heavy pages were compared directly with rendered slides.
- [x] Existing concepts were resolved before proposing new canonical titles.
- [ ] User approves the page classification and bundle boundaries.

## Evidence

[^fi-inventory-p4]: [[fixed-income-level-1-speed-review.pdf#page=4|Fixed Income Level I Speed Review, PDF p. 4]]
[^fi-inventory-p104]: [[fixed-income-level-1-speed-review.pdf#page=104|Fixed Income Level I Speed Review, PDF p. 104]]
