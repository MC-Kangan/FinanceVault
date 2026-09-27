---
id: concept-macaulay-duration
type: concept
title: Macaulay Duration
aliases:
- MacDur
- Macaulay Duration Measure
- 麦考利久期
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites:
- '[[Bond Pricing]]'
- '[[Yield to Maturity]]'
used_in:
- '[[Modified Duration]]'
related:
- '[[Convexity]]'
contrasts_with:
- '[[Modified Duration]]'
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Macaulay Duration

> [!summary]
> Macaulay duration is the present-value-weighted average time until a bond's cash flows are received, expressed in years.[^fi-l1-p61]

## Level 1 - Foundation

### Formula

$$
\mathrm{MacDur}=\sum_{t=1}^{N}t\left(\frac{PV(CF_t)}{P^{\mathrm{full}}}\right)
$$
[^fi-l1-p61]

Each time-to-cash-flow is weighted by that cash flow's share of the bond's full price. A zero-coupon bond therefore has Macaulay duration equal to its maturity.[^fi-l1-p61]

### Relationships

For otherwise similar bonds, Macaulay duration is generally higher with a longer maturity or lower coupon rate. For a given bond, duration generally declines as time passes, and lower yield tends to produce higher duration.[^fi-l1-p65]

### Common pitfalls

Macaulay duration is a timing measure. Use [[Modified Duration]]—not Macaulay duration directly—for the first-order percentage price response to a yield change.[^fi-l1-p62]

### Full-deck extension: Macaulay Duration

duration gap, special-instrument behavior, and the principal comparative statics: lower coupon and lower YTM increase duration; maturity generally increases it; zero-coupon duration equals maturity; a floating-rate instrument reflects time to the next reset.[^fi-risk-p61][^fi-risk-p63][^fi-risk-p65]

$$
\text{Duration gap}=D_{\text{Mac}}-\text{Investment horizon}
$$
[^fi-risk-p61]

## Connections

- Build the weights from [[Bond Pricing]].
- Convert the timing measure into price sensitivity with [[Modified Duration]].
- Add [[Convexity]] for curvature ignored by a duration-only estimate.

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-l1-p61]: [[fixed-income-level-1-speed-review.pdf#page=61|Fixed Income Level I Speed Review, PDF p. 61]]
[^fi-l1-p62]: [[fixed-income-level-1-speed-review.pdf#page=62|Fixed Income Level I Speed Review, PDF p. 62]]
[^fi-l1-p65]: [[fixed-income-level-1-speed-review.pdf#page=65|Fixed Income Level I Speed Review, PDF p. 65]]
[^fi-risk-p61]: [[fixed-income-level-1-speed-review.pdf#page=61|Fixed Income Level I Speed Review, PDF p. 61]]
[^fi-risk-p63]: [[fixed-income-level-1-speed-review.pdf#page=63|Fixed Income Level I Speed Review, PDF p. 63]]
[^fi-risk-p65]: [[fixed-income-level-1-speed-review.pdf#page=65|Fixed Income Level I Speed Review, PDF p. 65]]
