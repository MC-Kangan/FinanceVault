---
id: concept-price-value-of-a-basis-point
type: concept
title: Price Value of a Basis Point
aliases:
- PVBP
- PV01
- DV01
- BPV
- Basis Point Value
- 基点价值
first_level: 1
topics:
- '[[Fixed Income]]'
- '[[Derivatives]]'
prerequisites: []
used_in: []
related:
- '[[Money Duration]]'
- '[[Modified Duration]]'
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
- '[[Source - Derivatives Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---
# Price Value of a Basis Point

> [!summary]
> Price value of a basis point measures the currency change in full price for a one-basis-point yield move.[^fi-risk-p64]

## Level 1 - Foundation

### Definition and mechanics

Price value of a basis point measures the currency change in full price for a one-basis-point yield move.[^fi-risk-p64]

$$
PVBP=\text{Money duration}\times0.0001
$$
[^fi-risk-p64]

$$
PVBP\approx\frac{P_{-}-P_{+}}{2}
$$
[^fi-risk-p64]

### Exam focus

Identify the definition, direction of the principal relationships, and the financial-statement or valuation effect tested by this concept.[^fi-risk-p64]

### Corporate Issuers and Derivatives applications

<!-- merged:price-value-of-a-basis-point-ci-der -->

Interest-rate futures settle daily using a basis-point value calculated from notional principal, one basis point, and the contract period. Use [[Derivatives - Forward Commitments Pricing and Valuation]] for the surrounding chapter context.[^der-l1-p24]

### Slide-deck enrichment

<!-- merged:fi-enrichment -->

Macaulay duration is the present-value-weighted time to cash flows; modified duration estimates percentage price sensitivity; money duration translates it into currency; PVBP measures the currency effect of one basis point.[^fi-risk-p61][^fi-risk-p62][^fi-risk-p64]

$$ModDur=\frac{MacDur}{1+r_{period}},\quad \frac{\Delta P}{P}\approx-ModDur\Delta y,\quad PVBP=MoneyDur\times0.0001$$
[^fi-risk-p62][^fi-risk-p64]

## Connections

- [[Money Duration]]
- [[Modified Duration]]

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-risk-p64]: [[fixed-income-level-1-speed-review.pdf#page=64|Fixed Income Level I Speed Review, PDF p. 64]]
[^der-l1-p24]: [[derivatives-level-1-speed-review.pdf#page=24|Derivatives Level I Speed Review, PDF p. 24]]
[^fi-risk-p61]: [[fixed-income-level-1-speed-review.pdf#page=61|Fixed Income Level I Speed Review, PDF p. 61]]
[^fi-risk-p62]: [[fixed-income-level-1-speed-review.pdf#page=62|Fixed Income Level I Speed Review, PDF p. 62]]
