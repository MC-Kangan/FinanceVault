---
id: concept-effective-duration
type: concept
title: Effective Duration
aliases:
- Option-Adjusted Duration
- Effective Interest Rate Duration
- 有效久期
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites: []
used_in: []
related:
- '[[Modified Duration]]'
- '[[Effective Convexity]]'
- '[[Callable Bond]]'
- '[[Putable Bond]]'
- '[[Key Rate Duration]]'
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Effective Duration

> [!summary]
> Effective duration measures first-order sensitivity to a parallel shift in a benchmark yield curve and is appropriate when cash flows change with rates, especially for bonds with embedded options.[^fi-risk-p69]

## Level 1 - Foundation

### Definition and mechanics

Effective duration measures first-order sensitivity to a parallel shift in a benchmark yield curve and is appropriate when cash flows change with rates, especially for bonds with embedded options.[^fi-risk-p69]

$$
D_{\text{eff}}\approx\frac{P_{-}-P_{+}}{2P_0\Delta y_{\text{curve}}}
$$
[^fi-risk-p69]

Callable bonds can exhibit reduced effective duration when rates are low; putable bonds can exhibit reduced effective duration when rates are high.[^fi-risk-p71]

### Exam focus

Identify the definition, direction of the principal relationships, and the financial-statement or valuation effect tested by this concept.[^fi-risk-p69]

### Slide-deck enrichment

<!-- merged:fi-enrichment -->

Effective measures revalue cash flows after benchmark-curve shifts and are appropriate when embedded options change cash flows. Callable bonds have lower effective duration and may have negative convexity at low rates; putable bonds have lower effective duration and often stronger positive convexity at high rates.[^fi-risk-p69][^fi-risk-p70][^fi-risk-p71]

## Connections

- [[Modified Duration]]
- [[Effective Convexity]]
- [[Callable Bond]]
- [[Putable Bond]]
- [[Key Rate Duration]]

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-risk-p69]: [[fixed-income-level-1-speed-review.pdf#page=69|Fixed Income Level I Speed Review, PDF p. 69]]
[^fi-risk-p71]: [[fixed-income-level-1-speed-review.pdf#page=71|Fixed Income Level I Speed Review, PDF p. 71]]
[^fi-risk-p70]: [[fixed-income-level-1-speed-review.pdf#page=70|Fixed Income Level I Speed Review, PDF p. 70]]
