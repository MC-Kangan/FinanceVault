---
id: concept-credit-risk
type: concept
title: Credit Risk
aliases:
- Default Risk
- 信用风险
first_level: 1
topics:
- '[[Fixed Income]]'
- '[[Portfolio Management]]'
prerequisites: []
used_in:
- '[[Corporate Credit Analysis]]'
related:
- '[[Expected Loss]]'
- '[[Modified Duration]]'
- '[[Convexity]]'
- '[[Market Price Risk]]'
- '[[Liquidity Risk]]'
contrasts_with: []
source_notes:
- '[[Source - Fixed Income Level 1 Speed Review]]'
- '[[Source - Portfolio Management Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---
# Credit Risk

> [!summary]
> Credit risk is the risk of loss when a borrower fails to make full and timely interest or principal payments.[^fi-l1-p80]

## Level 1 - Foundation

### Analysis framework

![[source-fi-l1-speed-review-p081-credit-risk-framework.png|900]][^fi-l1-p81]

The framework combines top-down country, economic-condition, and currency factors with bottom-up capacity, capital, character, collateral, and covenant analysis.[^fi-l1-p81]

Probability of default is driven by the issuer's ability to service debt, assessed using qualitative and quantitative evidence such as profitability, coverage, and leverage.[^fi-l1-p81]

### Yield spread

A bond's yield spread is measured relative to a comparable default-free bond. It contains a credit spread and a liquidity premium, so the full yield spread is not a pure measure of expected credit loss.[^fi-l1-p83]

Macroeconomic conditions, market liquidity, and issuer-specific performance can change yield spreads. The price effect of a spread change can be approximated using [[Modified Duration]] and [[Convexity]].[^fi-l1-p83]

### Common pitfalls

Do not equate credit risk only with default probability: loss severity also matters through [[Expected Loss]], while market yield spreads additionally reflect liquidity.[^fi-l1-p80][^fi-l1-p83]

### Cross-topic applications

<!-- merged:eq-pm-applications -->

**Portfolio Management application:** Risk identification covers financial risks—market, credit, liquidity—and non-financial risks such as operational, model, settlement, legal, regulatory, political, and reputational risk.[^pm-l1-p34]

**Portfolio Management application:** Risk measurement can use probability, volatility, sensitivity, scenario/stress tests, value at risk, and conditional VaR/expected shortfall. Credit-risk measurement considers exposure, default likelihood, and loss severity.[^pm-l1-p35]

### Slide-deck enrichment

<!-- merged:fi-enrichment -->

Credit risk includes both default likelihood and loss severity. Unsecured investment-grade analysis emphasizes probability of default, while high-yield analysis also emphasizes collateral, covenants, and loss given default.[^fi-credit-p80][^fi-credit-p81]

$$Expected\ loss=PD\times LGD,\qquad LGD=EAD\times(1-RR)$$
[^fi-credit-p80]

## Connections

- Quantify the loss component with [[Expected Loss]].
- Evaluate issuer capacity in [[Corporate Credit Analysis]].
- Use [[Corporate Credit Analysis]] to connect accounting-derived coverage, leverage, profitability, and cash-flow measures to this risk assessment.

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fi-l1-p80]: [[fixed-income-level-1-speed-review.pdf#page=80|Fixed Income Level I Speed Review, PDF p. 80]]
[^fi-l1-p81]: [[fixed-income-level-1-speed-review.pdf#page=81|Fixed Income Level I Speed Review, PDF p. 81]]
[^fi-l1-p83]: [[fixed-income-level-1-speed-review.pdf#page=83|Fixed Income Level I Speed Review, PDF p. 83]]
[^pm-l1-p34]: [[portfolio-management-level-1-speed-review.pdf#page=34|Portfolio Management Level I Speed Review, PDF p. 34]]
[^pm-l1-p35]: [[portfolio-management-level-1-speed-review.pdf#page=35|Portfolio Management Level I Speed Review, PDF p. 35]]
[^fi-credit-p80]: [[fixed-income-level-1-speed-review.pdf#page=80|Fixed Income Level I Speed Review, PDF p. 80]]
[^fi-credit-p81]: [[fixed-income-level-1-speed-review.pdf#page=81|Fixed Income Level I Speed Review, PDF p. 81]]
