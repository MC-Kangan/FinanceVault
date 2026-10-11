---
id: proposal-fi-l1-interest-rate-risk-enrichment
type: proposal
title: Fixed Income - Interest Rate Risk Enrichment
target: "[[Fixed Income]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Fixed Income - Interest Rate Risk Enrichment

## Rationale

The duration and convexity nodes contain core formulas but not the deck's full horizon logic, property comparisons, portfolio caveats, option behavior, key-rate interpretation, and empirical-versus-analytical distinction. The merge will create `Fixed Income - Interest Rate Risk` as a subtopic map.

## Exact proposed content

Enrich `Bond Return Components`, `Reinvestment Risk`, and `Market Price Risk`: fixed-rate returns come from coupon/principal cash flows, reinvestment income, and capital gain or loss. Coupon reinvestment risk matters more for long horizons; market price risk matters more for short horizons. Macaulay duration is the investment horizon at which the two effects offset for a one-time parallel yield-curve shift.[^fi-risk-p60][^fi-risk-p61]

Enrich `Macaulay Duration`, `Modified Duration`, `Money Duration`, and `Price Value of a Basis Point`:

$$MacDur=\sum_i\left(\frac{PV(CF_i)}{P_0}\right)t_i$$

$$ModDur=\frac{MacDur}{1+r_{period}},\qquad \frac{\Delta P}{P}\approx-ModDur\times\Delta y$$

$$MoneyDur=ModDur\times P_{full},\qquad PVBP=MoneyDur\times0.0001\approx\frac{P_{-}-P_{+}}{2}$$

For zero-coupon bonds, Macaulay duration equals maturity; for perpetual bonds the deck gives $MacDur=(1+r_{period})/r_{period}$; for floating-rate instruments it reflects time to next reset.[^fi-risk-p61][^fi-risk-p62][^fi-risk-p63][^fi-risk-p64]

Enrich duration properties: lower coupon, longer maturity, and lower yield generally increase duration and interest-rate risk. Lower timing dispersion of cash flows also increases duration. Constant-yield-to-maturity Macaulay duration declines smoothly and then jumps after a coupon is paid.[^fi-risk-p65]

Enrich `Convexity`, `Money Convexity`, and `Portfolio Convexity`:

$$Convexity\approx\frac{P_-+P_+-2P_0}{P_0(\Delta y)^2}$$

$$\frac{\Delta P}{P}\approx-ModDur\Delta y+\frac{1}{2}Convexity(\Delta y)^2$$

$$\Delta P\approx-MoneyDur\Delta y+\frac{1}{2}MoneyConvexity(\Delta y)^2$$

Greater convexity makes a bond gain more when yields fall and lose less when yields rise, all else equal. Longer maturity, lower coupon, lower yield, and greater cash-flow dispersion generally increase convexity. Portfolio duration and convexity may be computed as market-value weighted averages, subject to the deck's parallel-shift and flat-curve cautions.[^fi-risk-p66][^fi-risk-p67][^fi-risk-p68]

Enrich `Effective Duration` and `Effective Convexity` for cash flows that change with benchmark-curve shifts:

$$EffDur=\frac{P_--P_+}{2P_0\Delta curve},\qquad EffCon=\frac{P_-+P_+-2P_0}{P_0(\Delta curve)^2}$$

Use them for embedded-option bonds and potentially for option-free bonds when cash-flow valuation under shifted benchmark curves is preferable. Callable bonds have lower effective duration and may have negative convexity at low rates; putable bonds have lower effective duration and often higher positive convexity at high rates.[^fi-risk-p69][^fi-risk-p70][^fi-risk-p71]

Enrich `Key Rate Duration`: it measures sensitivity to a benchmark-curve change at a specific maturity segment, helps identify curve-shape risk, and the sum of key-rate durations equals effective duration under the deck's framework.[^fi-risk-p72]

Enrich `Analytical Duration` and `Empirical Duration`: analytical measures estimate price effects from mathematical models that commonly treat benchmark-yield changes and spreads as independent; empirical measures use historical/statistical relationships and can reflect yield-spread correlation and nonparallel benchmark moves. The deck notes empirical and analytical duration are approximately equal for government bonds, while empirical duration can be lower for corporate bonds.[^fi-risk-p73]

## Navigation changes on merge

Create `Fixed Income - Interest Rate Risk`, link it from `[[Fixed Income]]`, and organize return sources, duration family, convexity family, option-aware measures, key-rate duration, and analytical/empirical measures.

## Review checklist

- [x] PDF pages 60-73 were visually inspected.
- [x] Every duration and convexity formula and the option-behavior diagrams were visually checked.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^fi-risk-p60]: [[fixed-income-level-1-speed-review.pdf#page=60|Fixed Income Level I Speed Review, PDF p. 60]]
[^fi-risk-p61]: [[fixed-income-level-1-speed-review.pdf#page=61|Fixed Income Level I Speed Review, PDF p. 61]]
[^fi-risk-p62]: [[fixed-income-level-1-speed-review.pdf#page=62|Fixed Income Level I Speed Review, PDF p. 62]]
[^fi-risk-p63]: [[fixed-income-level-1-speed-review.pdf#page=63|Fixed Income Level I Speed Review, PDF p. 63]]
[^fi-risk-p64]: [[fixed-income-level-1-speed-review.pdf#page=64|Fixed Income Level I Speed Review, PDF p. 64]]
[^fi-risk-p65]: [[fixed-income-level-1-speed-review.pdf#page=65|Fixed Income Level I Speed Review, PDF p. 65]]
[^fi-risk-p66]: [[fixed-income-level-1-speed-review.pdf#page=66|Fixed Income Level I Speed Review, PDF p. 66]]
[^fi-risk-p67]: [[fixed-income-level-1-speed-review.pdf#page=67|Fixed Income Level I Speed Review, PDF p. 67]]
[^fi-risk-p68]: [[fixed-income-level-1-speed-review.pdf#page=68|Fixed Income Level I Speed Review, PDF p. 68]]
[^fi-risk-p69]: [[fixed-income-level-1-speed-review.pdf#page=69|Fixed Income Level I Speed Review, PDF p. 69]]
[^fi-risk-p70]: [[fixed-income-level-1-speed-review.pdf#page=70|Fixed Income Level I Speed Review, PDF p. 70]]
[^fi-risk-p71]: [[fixed-income-level-1-speed-review.pdf#page=71|Fixed Income Level I Speed Review, PDF p. 71]]
[^fi-risk-p72]: [[fixed-income-level-1-speed-review.pdf#page=72|Fixed Income Level I Speed Review, PDF p. 72]]
[^fi-risk-p73]: [[fixed-income-level-1-speed-review.pdf#page=73|Fixed Income Level I Speed Review, PDF p. 73]]
