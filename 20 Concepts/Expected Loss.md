---
id: concept-expected-loss
type: concept
title: Expected Loss
aliases:
- EL
- Credit Expected Loss
- 预期损失
first_level: 1
topics:
- '[[Fixed Income]]'
prerequisites:
- '[[Credit Risk]]'
used_in:
- '[[Corporate Credit Analysis]]'
related:
- '[[Probability of Default]]'
- '[[Loss Given Default]]'
- '[[Exposure at Default]]'
- '[[Recovery Rate]]'
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---

# Expected Loss

> [!summary]
> Expected loss combines the probability of default with the loss given default and may be stated as a currency amount or as a percentage of exposure.[^fi-l1-p80]

## Level 1 - Foundation

### Core relationship

$$
EL=POD\times LGD
$$
[^fi-l1-p80]

The source uses **POD** for probability of default; **PD** is another common abbreviation for the same concept.[^fi-l1-p80]

### Currency and percentage forms

When loss given default is a currency amount:[^fi-l1-p80]

$$
LGD=EAD\times\text{Loss Severity}
$$
[^fi-l1-p80]

$$
EAD=\text{Face Value}+\text{Accrued Interest}-\text{Current Collateral Value}
$$
[^fi-l1-p80]

When expected loss is expressed as a percentage of exposure, loss given default is the loss-severity rate:[^fi-l1-p80]

$$
LGD=1-\text{Recovery Rate}
$$
[^fi-l1-p80]

### Interpretation

Investors compare expected loss with the credit spread to judge compensation, while remembering that observed yield spread also includes a liquidity premium.[^fi-l1-p80][^fi-l1-p83]

> [!tip] 中文提示
> 先确认 LGD 是金额还是比例；单位不同，公式中的敞口处理也不同。[^fi-l1-p80]

### Slide-deck enrichment

<!-- merged:fi-enrichment -->

Credit risk includes both default likelihood and loss severity. Unsecured investment-grade analysis emphasizes probability of default, while high-yield analysis also emphasizes collateral, covenants, and loss given default.[^fi-credit-p80][^fi-credit-p81]

$$Expected\ loss=PD\times LGD,\qquad LGD=EAD\times(1-RR)$$
[^fi-credit-p80]

## Connections

- [[Probability of Default]]
- [[Loss Given Default]]
- [[Exposure at Default]]
- [[Recovery Rate]]

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-l1-p80]: [[fixed-income-level-1-speed-review.pdf#page=80|Fixed Income Level I Speed Review, PDF p. 80]]
[^fi-l1-p83]: [[fixed-income-level-1-speed-review.pdf#page=83|Fixed Income Level I Speed Review, PDF p. 83]]
[^fi-credit-p80]: [[fixed-income-level-1-speed-review.pdf#page=80|Fixed Income Level I Speed Review, PDF p. 80]]
[^fi-credit-p81]: [[fixed-income-level-1-speed-review.pdf#page=81|Fixed Income Level I Speed Review, PDF p. 81]]
