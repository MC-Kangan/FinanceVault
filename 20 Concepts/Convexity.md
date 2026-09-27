---
id: concept-convexity
type: concept
title: Convexity
aliases:
- Bond Convexity
- 凸性
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites:
- '[[Modified Duration]]'
used_in:
- '[[Bond Pricing]]'
related:
- '[[Macaulay Duration]]'
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Convexity

> [!summary]
> Convexity captures the curvature of the bond price-yield relationship and improves the linear price estimate from modified duration.[^fi-l1-p66][^fi-l1-p67]

## Level 1 - Foundation

### Price-yield curvature

![[source-fi-l1-speed-review-p066-convexity-price-yield.png|900]][^fi-l1-p66]

The source diagram contrasts the curved price-yield relationship with a tangent-line duration estimate. The gap grows as the yield change moves farther from the starting point.[^fi-l1-p66]

### Convexity approximation

Using equal upward and downward yield shocks around the current full price:[^fi-l1-p68]

$$
\mathrm{Convexity}\approx
\frac{P_{-}+P_{+}-2P_0}{P_0(\Delta y)^2}
$$
[^fi-l1-p68]

### Duration-plus-convexity estimate

$$
\frac{\Delta P^{\mathrm{full}}}{P^{\mathrm{full}}}
\approx-\mathrm{ModDur}\,\Delta y
+\frac{1}{2}\mathrm{Convexity}(\Delta y)^2
$$
[^fi-l1-p67]

For a conventional option-free bond with positive convexity, the second-order term is positive for either sign of yield change, correcting part of the duration-only error.[^fi-l1-p67]

### Full-deck extension: Convexity

the second-order price estimate and money convexity while retaining the existing visually verified convexity diagram.[^fi-risk-p66][^fi-risk-p67]

$$
\frac{\Delta P}{P}\approx-D_{\text{mod}}\Delta y+\frac{1}{2}C(\Delta y)^2
$$
[^fi-risk-p67]

$$
\Delta P\approx-\text{Money duration}\times\Delta y+\frac{1}{2}\text{Money convexity}\times(\Delta y)^2
$$
[^fi-risk-p67]

## Connections

- Start with the first-order estimate in [[Modified Duration]].
- Apply both measures to [[Bond Pricing]].
- Credit-spread price effects use the same duration-and-convexity structure in [[Credit Risk]].

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-l1-p66]: [[fixed-income-level-1-speed-review.pdf#page=66|Fixed Income Level I Speed Review, PDF p. 66]]
[^fi-l1-p67]: [[fixed-income-level-1-speed-review.pdf#page=67|Fixed Income Level I Speed Review, PDF p. 67]]
[^fi-l1-p68]: [[fixed-income-level-1-speed-review.pdf#page=68|Fixed Income Level I Speed Review, PDF p. 68]]
[^fi-risk-p66]: [[fixed-income-level-1-speed-review.pdf#page=66|Fixed Income Level I Speed Review, PDF p. 66]]
[^fi-risk-p67]: [[fixed-income-level-1-speed-review.pdf#page=67|Fixed Income Level I Speed Review, PDF p. 67]]
