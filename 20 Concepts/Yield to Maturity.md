---
id: concept-yield-to-maturity
type: concept
title: Yield to Maturity
aliases:
- YTM
- 到期收益率
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites:
- '[[Bond Pricing]]'
used_in:
- '[[Macaulay Duration]]'
- '[[Modified Duration]]'
related:
- '[[Bond Pricing]]'
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Yield to Maturity

> [!summary]
> Yield to maturity is the single discount rate that equates a bond's full price with the present value of all promised cash flows.[^fi-l1-p42]

## Level 1 - Foundation

### Pricing equation

$$
P_0=\sum_{t=1}^{N}\frac{PMT_t}{(1+\mathrm{YTM})^t}+\frac{FV}{(1+\mathrm{YTM})^N}
$$
[^fi-l1-p42]

YTM is an internal rate of return. Bond price and YTM move inversely when the promised cash flows are unchanged.[^fi-l1-p42]

### Interpretation assumptions

The quoted YTM is realized only if the investor holds the bond to maturity, the issuer makes all promised payments, and interim coupon cash flows can be reinvested at the same YTM.[^fi-l1-p42]

### Common pitfalls

YTM is not a guaranteed return. Default, sale before maturity, or reinvestment at a different rate causes realized return to differ from the quoted YTM.[^fi-l1-p42]

> [!tip] 中文提示
> YTM 是把价格与承诺现金流现值相等的内部收益率，不等于无条件实现的收益率。[^fi-l1-p42]

### Full-deck extension: Yield to Maturity

the assumptions required for realized return to equal YTM: full and timely payment, holding to maturity, and reinvestment of coupons at the YTM.[^fi-valuation-p42]

## Connections

- Start from the cash-flow present value in [[Bond Pricing]].
- Convert YTM into price sensitivity with [[Macaulay Duration]] and [[Modified Duration]].
- Return to [[Fixed Income]] for the topic sequence.

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-l1-p42]: [[fixed-income-level-1-speed-review.pdf#page=42|Fixed Income Level I Speed Review, PDF p. 42]]
[^fi-valuation-p42]: [[fixed-income-level-1-speed-review.pdf#page=42|Fixed Income Level I Speed Review, PDF p. 42]]
