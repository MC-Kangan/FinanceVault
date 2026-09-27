---
id: proposal-fi-l1-interest-rate-risk-measures
type: proposal
title: Fixed Income Level 1 - Interest Rate Risk Measures
target: "[[Fixed Income]]"
change_type: topic-expansion
status: merged
tags:
  - cfa/level-1
---

# Fixed Income Level 1 - Interest Rate Risk Measures

## Rationale

Extend the duration and convexity pilot with the return decomposition, reinvestment and market-price risks, currency-value measures, portfolio aggregation, effective measures, curve-shape risk, and empirical estimation.

## Proposed canonical concepts

### `Bond Return Components`

- A fixed-rate bond's return comes from promised coupons and principal, reinvestment income on coupons, and any capital gain or loss when sold before maturity.[^fi-risk-p60]
- Interest-rate risk has two opposing components: coupon reinvestment risk matters more over long horizons, while market-price risk matters more over short horizons.[^fi-risk-p60]

Aliases to review: `Sources of Bond Return`, `Bond Investment Return`, `债券回报构成`.

### `Reinvestment Risk`

- Define uncertainty about the rate at which coupon cash flows can be reinvested. Rising rates improve reinvestment income but lower current bond prices; falling rates have the opposite effects.[^fi-risk-p60]
- Connect this concept to existing `Macaulay Duration`, where the duration horizon balances the reinvestment and price effects of a one-time parallel yield-curve shift.[^fi-risk-p61]

Aliases to review: `Coupon Reinvestment Risk`, `再投资风险`.

### `Money Duration`

Money duration converts modified duration into a currency price-change measure.[^fi-risk-p64]

$$
\text{Money duration}=\text{Modified duration}\times P_{\text{full}}
$$

[^fi-risk-p64]

Aliases to review: `Dollar Duration`, `Currency Duration`, `美元久期`.

### `Price Value of a Basis Point`

Price value of a basis point measures the currency change in full price for a one-basis-point yield move.[^fi-risk-p64]

$$
PVBP=\text{Money duration}\times0.0001
$$

$$
PVBP\approx\frac{P_{-}-P_{+}}{2}
$$

[^fi-risk-p64]

Aliases to review: `PVBP`, `PV01`, `DV01`, `BPV`, `Basis Point Value`, `基点价值`.

### `Portfolio Duration`

Aggregate-cash-flow duration is theoretically correct but difficult in practice. A weighted average of constituent durations is more practical and becomes more accurate when constituent yields are similar and the yield curve is flat. The weighted-average approach assumes a parallel yield-curve shift.[^fi-risk-p68]

Aliases to review: `Portfolio Modified Duration`, `组合久期`.

### `Portfolio Convexity`

Portfolio convexity can be approximated as a market-value-weighted average of constituent convexities under the same simplifying assumptions used for portfolio duration.[^fi-risk-p68]

Aliases to review: `Portfolio Interest Rate Convexity`, `组合凸度`.

### `Effective Duration`

Effective duration measures first-order sensitivity to a parallel shift in a benchmark yield curve and is appropriate when cash flows change with rates, especially for bonds with embedded options.[^fi-risk-p69]

$$
D_{\text{eff}}\approx\frac{P_{-}-P_{+}}{2P_0\Delta y_{\text{curve}}}
$$

[^fi-risk-p69]

Callable bonds can exhibit reduced effective duration when rates are low; putable bonds can exhibit reduced effective duration when rates are high.[^fi-risk-p71]

Aliases to review: `Option-Adjusted Duration`, `Effective Interest Rate Duration`, `有效久期`.

### `Effective Convexity`

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

Aliases to review: `Option-Adjusted Convexity`, `Effective Interest Rate Convexity`, `有效凸度`.

### `Key Rate Duration`

- Key rate duration measures sensitivity to a change at one maturity segment of a benchmark curve, making it useful for steepening, flattening, and twisting rather than only parallel shifts.[^fi-risk-p72]

$$
\frac{\Delta P}{P}\approx-KRD_k\Delta r_k
$$

$$
\sum_k KRD_k=D_{\text{eff}}
$$

[^fi-risk-p72]

Aliases to review: `Partial Duration`, `KRD`, `关键利率久期`.

### `Empirical Duration`

- Analytical duration uses formulas and typically treats government yields and spreads as independent. Empirical duration uses historical statistical relationships and can reflect correlation between benchmark-rate and spread changes.[^fi-risk-p73]
- Under stress, government-bond empirical duration may remain close to analytical duration, while corporate-bond empirical duration can be lower because spread widening offsets benchmark-yield declines.[^fi-risk-p73]

Aliases to review: `Empirical Convexity`, `Analytical Duration`, `实证久期`.

## Proposed updates to trusted concepts

### `Macaulay Duration`

Propose adding duration gap, special-instrument behavior, and the principal comparative statics: lower coupon and lower YTM increase duration; maturity generally increases it; zero-coupon duration equals maturity; a floating-rate instrument reflects time to the next reset.[^fi-risk-p61][^fi-risk-p63][^fi-risk-p65]

$$
\text{Duration gap}=D_{\text{Mac}}-\text{Investment horizon}
$$

[^fi-risk-p61]

### `Modified Duration`

The approved note should retain the standard positive magnitude relationship:

$$
D_{\text{mod}}=\frac{D_{\text{Mac}}}{1+r_{\text{period}}}
$$

and the negative sign belongs in the price-change approximation:

$$
\frac{\Delta P}{P}\approx-D_{\text{mod}}\Delta y
$$

[^fi-risk-p62][^fi-risk-p63]

> [!warning] Source inconsistency
> PDF page 63 prints a leading negative sign in the identity relating modified duration to Macaulay duration. Duration is stored as a positive sensitivity magnitude; the negative sign belongs in the price-change equation on page 62. This proposal flags the inconsistency and does not copy it into the trusted note.[^fi-risk-p62][^fi-risk-p63]

### `Convexity`

Propose adding the second-order price estimate and money convexity while retaining the existing visually verified convexity diagram.[^fi-risk-p66][^fi-risk-p67]

$$
\frac{\Delta P}{P}\approx-D_{\text{mod}}\Delta y+\frac{1}{2}C(\Delta y)^2
$$

$$
\Delta P\approx-\text{Money duration}\times\Delta y+\frac{1}{2}\text{Money convexity}\times(\Delta y)^2
$$

[^fi-risk-p67]

## Link and alias changes

- Connect `Money Duration`, `Price Value of a Basis Point`, `Effective Duration`, `Effective Convexity`, and `Key Rate Duration` to existing `Modified Duration`.
- Connect `Reinvestment Risk` to `Bond Return Components` and existing `Macaulay Duration`.
- Connect `Effective Duration` and `Effective Convexity` to proposed `Callable Bond` and `Putable Bond`.
- Aliases remain unregistered until approval and collision validation.

## Review checklist

- [x] Formulas were visually checked against pages 60-73.
- [x] Page 63 inconsistency is explicitly isolated.
- [x] Trusted pilot notes remain unchanged.
- [ ] User approves concept boundaries and updates.
- [ ] Approved concepts are created through the merge workflow.

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
