---
id: concept-effective-convexity
type: concept
title: Effective Convexity
aliases:
- Option-Adjusted Convexity
- Effective Interest Rate Convexity
- 有效凸度
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites: []
used_in: []
related:
- '[[Convexity]]'
- '[[Effective Duration]]'
- '[[Callable Bond]]'
- '[[Putable Bond]]'
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Effective Convexity

> [!summary]
> Effective convexity measures second-order sensitivity when cash flows can change with benchmark-curve shifts.[^fi-risk-p70]

## Level 1 - Foundation

### Definition and mechanics

Effective convexity measures second-order sensitivity when cash flows can change with benchmark-curve shifts.[^fi-risk-p70]

$$
C_{\text{eff}}\approx\frac{P_{-}+P_{+}-2P_0}{P_0(\Delta y_{\text{curve}})^2}
$$
[^fi-risk-p70]

Together, effective duration and effective convexity estimate the price effect of a curve shift.[^fi-risk-p69][^fi-risk-p70]

$$
\frac{\Delta P}{P}\approx-D_{\text{eff}}\Delta y_{\text{curve}}+\frac{1}{2}C_{\text{eff}}(\Delta y_{\text{curve}})^2
$$
[^fi-risk-p69]

Callable bonds can exhibit negative effective convexity when rates are low; putable bonds can exhibit stronger positive convexity when rates are high.[^fi-risk-p71]

### Exam focus

Identify the definition, direction of the principal relationships, and the financial-statement or valuation effect tested by this concept.[^fi-risk-p70]

### Slide-deck enrichment

<!-- merged:fi-enrichment -->

Effective measures revalue cash flows after benchmark-curve shifts and are appropriate when embedded options change cash flows. Callable bonds have lower effective duration and may have negative convexity at low rates; putable bonds have lower effective duration and often stronger positive convexity at high rates.[^fi-risk-p69][^fi-risk-p70][^fi-risk-p71]

## Connections

- [[Convexity]]
- [[Effective Duration]]
- [[Callable Bond]]
- [[Putable Bond]]

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-risk-p70]: [[fixed-income-level-1-speed-review.pdf#page=70|Fixed Income Level I Speed Review, PDF p. 70]]
[^fi-risk-p69]: [[fixed-income-level-1-speed-review.pdf#page=69|Fixed Income Level I Speed Review, PDF p. 69]]
[^fi-risk-p71]: [[fixed-income-level-1-speed-review.pdf#page=71|Fixed Income Level I Speed Review, PDF p. 71]]
