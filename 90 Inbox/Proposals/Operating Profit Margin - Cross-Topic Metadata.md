---
id: proposal-operating-profit-margin-cross-topic-metadata
type: proposal
title: Operating Profit Margin - Cross-Topic Metadata
target: "[[Operating Profit Margin]]"
change_type: metadata-update
status: pending-review
tags:
  - cfa/level-1
---

# Proposed change

## Rationale

The FSA deck defines Operating Profit Margin as operating profits divided by revenue, while the Fixed Income corporate-credit slide uses the equivalent EBIT Margin measure as its profitability input. `EBIT Margin` is already an alias of the canonical `Operating Profit Margin` note, so this should be one dual-topic concept rather than a second node.[^fsa-l1-p46][^fi-l1-p87]

## Exact proposed metadata changes

In `[[Operating Profit Margin]]`:

- Add `[[Fixed Income]]` to `topics`.
- Add `[[Corporate Credit Analysis]]` to `used_in`.
- Add `[[Source - Fixed Income Level 1 Speed Review]]` to `source_notes`.

In `[[Corporate Credit Analysis]]`:

- Replace the supporting profitability link from `[[Net Profit Margin]]` to `[[Operating Profit Margin]]`, because the Fixed Income slide specifically uses EBIT Margin rather than net margin.[^fi-l1-p87]

## Graph effect

After approval and merge, `Operating Profit Margin` will become a purple dual-topic node. `Free Cash Flow` should remain an FSA topic concept with a direct application link into credit analysis; the Fixed Income slide's distinct formula should eventually be represented by an atomic `Retained Cash Flow to Net Debt` concept.[^fi-l1-p87]

## Evidence

[^fsa-l1-p46]: [[financial-statement-analysis-level-1-speed-review.pdf#page=46|Financial Statement Analysis Level I Speed Review, PDF p. 46]]
[^fi-l1-p87]: [[fixed-income-level-1-speed-review.pdf#page=87|Fixed Income Level I Speed Review, PDF p. 87]]

## Review checklist

- [x] Exact formulas visually verified against both source pages.
- [x] `EBIT Margin` already resolves to `Operating Profit Margin`; no alias collision is introduced.
- [x] No trusted concept note changed before approval.
- [x] Personal Notes will remain byte-for-byte unchanged during merge.
- [ ] User approves or rejects the metadata change.
