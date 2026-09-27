---
id: concept-yield-spread-measures
type: concept
title: Yield Spread Measures
aliases:
- 收益率利差
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites: []
used_in: []
related: []
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Yield Spread Measures

> [!summary]
> Decompose YTM into a benchmark rate capturing broad macro conditions and a yield spread capturing credit, liquidity, and tax effects. - Define G-spread relative to an actual or interpolated government bond, I-spread relative to the same-tenor swap rate,…[^fi-valuation-p47]

## Level 1 - Foundation

### Definition and mechanics

- Decompose YTM into a benchmark rate capturing broad macro conditions and a yield spread capturing credit, liquidity, and tax effects.[^fi-valuation-p47]
- Define G-spread relative to an actual or interpolated government bond, I-spread relative to the same-tenor swap rate, Z-spread as the constant spread over the government spot curve, and OAS as the spread after removing embedded-option value.[^fi-valuation-p47][^fi-valuation-p48]

$$
P_0=\sum_{t=1}^{N}\frac{CF_t}{(1+s_t+Z)^t}
$$
[^fi-valuation-p48]

> [!warning] Source convention to review
> Page 48 presents `OAS = Z-spread - option value (%)` as a study shortcut. The approved note should explain the callable-versus-putable direction carefully rather than treating option value as a directly subtractable percentage in every valuation model.[^fi-valuation-p48]

### Exam focus

Identify the definition, direction of the principal relationships, and the financial-statement or valuation effect tested by this concept.[^fi-valuation-p47]

## Connections

- Use [[Fixed Income]] to navigate the surrounding curriculum and related concepts.

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-valuation-p47]: [[fixed-income-level-1-speed-review.pdf#page=47|Fixed Income Level I Speed Review, PDF p. 47]]
[^fi-valuation-p48]: [[fixed-income-level-1-speed-review.pdf#page=48|Fixed Income Level I Speed Review, PDF p. 48]]
