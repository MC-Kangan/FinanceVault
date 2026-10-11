---
id: concept-margin-call
type: concept
title: Margin Call
aliases: []
first_level: 1
topics:
- '[[Equity Investments]]'
- '[[Derivatives]]'
prerequisites: []
used_in: []
related:
- '[[Margin Buying]]'
- '[[Financial Leverage Ratio]]'
- '[[Maintenance Margin]]'
- '[[Variation Margin]]'
contrasts_with: []
source_notes:
- '[[Source - Equity Investments Level 1 Speed Review]]'
- '[[Source - Derivatives Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---
# Margin Call

> [!summary]
> Margin Call is a Level 1 link target within Financial Markets and Trading; keeping it atomic makes its definition, mechanics, and later-level extensions directly reusable.[^eq-l1-p14]

## Level 1 - Foundation

### Formula and mechanics

**Equity Investments — Financial Markets and Trading:** Margin buying uses a margin loan; buyer’s equity is the investor-funded portion. Leverage is position value divided by equity, and margin rate is its reciprocal. Visually verified margin-call price: $P_c=P_0(1-\text{initial margin})/(1-\text{maintenance margin})$.[^eq-l1-p14]

### Interpretation

Use Margin Call as a distinct exam concept when navigating [[Equity Investments]]; compare it with adjacent concepts from the same source section instead of treating the chapter as one undifferentiated note.[^eq-l1-p14]

### Common pitfalls

Do not merge Margin Call with an abbreviation, translation, or neighbouring category. Apply the exact definition, classification, and formula convention shown on the cited source page.[^eq-l1-p14]

### Corporate Issuers and Derivatives applications

<!-- merged:ci-der-applications -->

**Derivatives application:** Daily marking to market transfers gains and losses through margin accounts supported by initial, maintenance, and variation margin. Use [[Derivatives - Instruments and Markets]] for the surrounding chapter context.[^der-l1-p9]

<!-- enrichment:equity:start -->

### Equity slide enrichment

Margin leverage and the margin rate are reciprocals:[^eq-enrich-p14]

$$
Leverage=\frac{Position\ value}{Buyer's\ equity},\qquad Margin\ rate=\frac{1}{Leverage}
$$[^eq-enrich-p14]

Falling below maintenance margin triggers a margin call or liquidation. The slide's call-price relation is:[^eq-enrich-p14]

$$
P_c=P_0\left(\frac{1-Initial\ margin}{1-Maintenance\ margin}\right)
$$[^eq-enrich-p14]

[^eq-enrich-p14]

<!-- enrichment:equity:end -->

## Connections

Within the source sequence, this concept is directly adjacent to [[Margin Buying]], [[Financial Leverage Ratio]]. Use the topic map to move outward to the wider model or workflow.

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^eq-l1-p14]: [[equity-investments-level-1-speed-review.pdf#page=14|Equity Investments Level I Speed Review, PDF p. 14]]
[^der-l1-p9]: [[derivatives-level-1-speed-review.pdf#page=9|Derivatives Level I Speed Review, PDF p. 9]]

[^eq-enrich-p14]: [[equity-investments-level-1-speed-review.pdf#page=14|Equity Investments Level I Speed Review, PDF p. 14]]
