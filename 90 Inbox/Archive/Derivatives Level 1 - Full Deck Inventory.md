---
id: proposal-derivatives-l1-full-deck-inventory
type: proposal
title: Derivatives Level 1 - Full Deck Inventory
target: Derivatives
change_type: source-inventory
status: merged
tags:
  - cfa/level-1
---

# Derivatives Level 1 - Full Deck Inventory

## Rationale

This inventory separates reusable instrument concepts, market mechanics, pricing principles, formulas, and payoff structures from dividers, recaps, promotion, and closing material. The page-separated OCR transcript is an untrusted discovery aid; the rendered PDF remains authoritative.

## Page inventory

| PDF pages | Classification | Proposed handling |
| --- | --- | --- |
| 1-2 | cover / promotion | register source; exclude promotional material |
| 3 | divider | navigation only |
| 4-15 | concepts, classifications, comparisons, payoff diagrams | Derivative Instruments and Markets chapter |
| 16 | recap | completeness and recurrence check only |
| 17 | divider | navigation only |
| 18-26 | pricing principles, formulas, worked example, valuation | Forward Commitments Pricing and Valuation chapter |
| 27 | recap | completeness check only |
| 28 | divider | navigation only |
| 29-36 | formulas, comparisons, option analogy, binomial examples | Option Value and Binomial Pricing chapter |
| 37 | recap | completeness check only |
| 38 | closing | exclude as noise |

The three content chapters cover every reusable study page in the deck.[^der-inventory-p4][^der-inventory-p36]

## Proposed navigation

- Create the top-level topic map `Derivatives` and add it to [[CFA Level 1]].
- Create three chapter maps: `Derivatives - Instruments and Markets`, `Derivatives - Forward Commitments Pricing and Valuation`, and `Derivatives - Option Value and Binomial Pricing`.
- Keep canonical concepts flat in `20 Concepts/`; chapter maps create visible graph clusters.
- Reuse and enrich existing concepts including [[Cost of Carry]], [[Convenience Yield]], [[Credit Risk]], and fixed-income concepts used in interest-rate derivative pricing where canonical equivalents exist.
- After approval and merge, add Derivatives to the top-level topic-map colour group, add a dedicated concept colour, regenerate the cross-topic query, and visually inspect the graph. Sources, transcripts, and proposals remain excluded.

## Review checklist

- [x] Immutable source hash and 38-page count registered.
- [x] Full page-separated OCR transcript completed with uncertainty markers.
- [x] Representative pages from all three chapters visually inspected.
- [x] Existing canonical filenames and likely aliases searched before proposing nodes.
- [x] Trusted concepts, maps, and graph settings remain unchanged.
- [x] User approved page classification and chapter boundaries.
- [x] Every promoted formula is visually reverified during merge.
- [x] Final graph configuration and chapter clustering are verified after merge.

## Evidence

[^der-inventory-p4]: [[derivatives-level-1-speed-review.pdf#page=4|Derivatives Level I Speed Review, PDF p. 4]]
[^der-inventory-p36]: [[derivatives-level-1-speed-review.pdf#page=36|Derivatives Level I Speed Review, PDF p. 36]]
