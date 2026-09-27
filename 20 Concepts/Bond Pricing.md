---
id: concept-bond-pricing
type: concept
title: Bond Pricing
aliases:
- Bond Valuation
- 债券定价
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites: []
used_in:
- '[[Yield to Maturity]]'
- '[[Macaulay Duration]]'
related:
- '[[Modified Duration]]'
- '[[Convexity]]'
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Bond Pricing

> [!summary]
> A bond's value is the present value of its promised cash flows, discounted at the market-required yield for comparable risk.[^fi-l1-p40]

## Level 1 - Foundation

### Present-value model

$$
P_0=\sum_{t=1}^{N}\frac{CF_t}{(1+r)^t}
$$
[^fi-l1-p40]

For a fixed-rate bond, the cash flows are coupon payments plus principal at maturity. A market discount rate above the coupon rate produces a discount bond; an equal rate produces a par bond; and a lower market rate produces a premium bond.[^fi-l1-p40]

### Price through time

If the required yield does not change, a discount bond's price rises toward par and a premium bond's price falls toward par as maturity approaches. This convergence is the pull-to-par effect.[^fi-l1-p40]

### Quoted and settlement price

The full or dirty price equals the flat or clean price plus accrued interest. The buyer pays the full price at settlement even when the market quote is the clean price.[^fi-l1-p41]

$$
\text{Full Price}=\text{Clean Price}+\text{Accrued Interest}
$$
[^fi-l1-p41]

> [!tip] 中文提示
> 债券报价常用净价，但实际结算支付全价；不要把两者混淆。[^fi-l1-p41]

### Full-deck extension: Bond Pricing

clean-versus-dirty price mechanics without editing the trusted note before approval:[^fi-valuation-p41]

$$
\text{Accrued interest}=\frac{t}{T}\times\text{Coupon payment}
$$
[^fi-valuation-p41]

$$
P_{\text{clean}}=P_{\text{full}}-\text{Accrued interest}
$$
[^fi-valuation-p41]

Government bonds commonly use actual/actual day count, while corporate bonds often use 30/360.[^fi-valuation-p41]

## Connections

- Solve the present-value equation for the discount rate in [[Yield to Maturity]].
- Use [[Macaulay Duration]], [[Modified Duration]], and [[Convexity]] to estimate how price reacts to yield changes.
- Return to [[Fixed Income]] for the valuation and risk sequence.

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-l1-p40]: [[fixed-income-level-1-speed-review.pdf#page=40|Fixed Income Level I Speed Review, PDF p. 40]]
[^fi-l1-p41]: [[fixed-income-level-1-speed-review.pdf#page=41|Fixed Income Level I Speed Review, PDF p. 41]]
[^fi-valuation-p41]: [[fixed-income-level-1-speed-review.pdf#page=41|Fixed Income Level I Speed Review, PDF p. 41]]
