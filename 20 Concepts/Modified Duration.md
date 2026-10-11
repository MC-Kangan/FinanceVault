---
id: concept-modified-duration
type: concept
title: Modified Duration
aliases:
- ModDur
- Modified Duration Measure
- 修正久期
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites:
- '[[Macaulay Duration]]'
- '[[Yield to Maturity]]'
used_in:
- '[[Bond Pricing]]'
related:
- '[[Convexity]]'
contrasts_with:
- '[[Macaulay Duration]]'
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Modified Duration

> [!summary]
> Modified duration approximates a bond's percentage full-price change for a small change in yield to maturity.[^fi-l1-p62]

## Level 1 - Foundation

### Conversion from Macaulay duration

For a yield quoted with $m$ compounding periods per year:[^fi-l1-p63]

$$
\mathrm{ModDur}=\frac{\mathrm{MacDur}}{1+\mathrm{YTM}/m}
$$
[^fi-l1-p63]

### Price sensitivity

$$
\frac{\Delta P^{\mathrm{full}}}{P^{\mathrm{full}}}\approx-\mathrm{ModDur}\times\Delta\mathrm{YTM}
$$
[^fi-l1-p62]

The negative sign belongs in the price-change equation because price and yield move in opposite directions. Modified duration itself is normally stated as a positive sensitivity measure.[^fi-l1-p62]

> [!warning] Source convention check
> PDF page 63 places a leading minus sign in the displayed Macaulay-to-modified-duration relationship. The standard positive-measure convention above is consistent with the separate price-change equation on PDF page 62; always inspect the sign convention used in a question.[^fi-l1-p62][^fi-l1-p63]

### Limitation

The approximation is linear and is most useful for small yield changes. Add [[Convexity]] when curvature materially affects the estimate.[^fi-l1-p66]

### Full-deck extension: Modified Duration

the standard positive magnitude relationship:[^fi-risk-p62]

$$
D_{\text{mod}}=\frac{D_{\text{Mac}}}{1+r_{\text{period}}}
$$
[^fi-risk-p62]

and the negative sign belongs in the price-change approximation:[^fi-risk-p62]

$$
\frac{\Delta P}{P}\approx-D_{\text{mod}}\Delta y
$$
[^fi-risk-p62][^fi-risk-p63]

> [!warning] Source inconsistency
> PDF page 63 prints a leading negative sign in the identity relating modified duration to Macaulay duration. Duration is stored as a positive sensitivity magnitude; the negative sign belongs in the price-change equation on page 62. This proposal flags the inconsistency and does not copy it into the trusted note.[^fi-risk-p62][^fi-risk-p63]

### Slide-deck enrichment

<!-- merged:fi-enrichment -->

Macaulay duration is the present-value-weighted time to cash flows; modified duration estimates percentage price sensitivity; money duration translates it into currency; PVBP measures the currency effect of one basis point.[^fi-risk-p61][^fi-risk-p62][^fi-risk-p64]

$$ModDur=\frac{MacDur}{1+r_{period}},\quad \frac{\Delta P}{P}\approx-ModDur\Delta y,\quad PVBP=MoneyDur\times0.0001$$
[^fi-risk-p62][^fi-risk-p64]

## Connections

- Derive the measure from [[Macaulay Duration]].
- Apply it to [[Bond Pricing]] and credit-spread changes.
- Combine it with [[Convexity]] for a second-order estimate.

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-l1-p62]: [[fixed-income-level-1-speed-review.pdf#page=62|Fixed Income Level I Speed Review, PDF p. 62]]
[^fi-l1-p63]: [[fixed-income-level-1-speed-review.pdf#page=63|Fixed Income Level I Speed Review, PDF p. 63]]
[^fi-l1-p66]: [[fixed-income-level-1-speed-review.pdf#page=66|Fixed Income Level I Speed Review, PDF p. 66]]
[^fi-risk-p62]: [[fixed-income-level-1-speed-review.pdf#page=62|Fixed Income Level I Speed Review, PDF p. 62]]
[^fi-risk-p63]: [[fixed-income-level-1-speed-review.pdf#page=63|Fixed Income Level I Speed Review, PDF p. 63]]
[^fi-risk-p61]: [[fixed-income-level-1-speed-review.pdf#page=61|Fixed Income Level I Speed Review, PDF p. 61]]
[^fi-risk-p64]: [[fixed-income-level-1-speed-review.pdf#page=64|Fixed Income Level I Speed Review, PDF p. 64]]
