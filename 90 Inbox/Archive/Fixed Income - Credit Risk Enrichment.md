---
id: proposal-fi-l1-credit-risk-enrichment
type: proposal
title: Fixed Income - Credit Risk Enrichment
target: "[[Fixed Income]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Fixed Income - Credit Risk Enrichment

## Rationale

Credit concepts need the complete expected-loss chain, ratings limitations, sovereign/municipal distinctions, and corporate ratio framework. The merge will create `Fixed Income - Credit Risk` and preserve the accounting-derived concepts as genuine cross-topic bridges.

## Exact proposed content

Enrich `Credit Risk`, `Expected Loss`, `Probability of Default`, `Loss Given Default`, `Exposure at Default`, and `Recovery Rate`:

$$Expected\ loss=PD\times LGD$$

$$LGD=EAD\times Loss\ severity=EAD\times(1-RR)$$

$$Expected\ loss\ rate=PD\times LGD\%$$

Credit risk is loss from failure to make full and timely interest or principal payments. The analytical framework combines qualitative capacity, capital, character, collateral, and covenants with quantitative evidence; unsecured investment-grade investors focus more on PD, while high-yield investors also emphasize LGD, collateral, and covenants.[^fi-credit-p80][^fi-credit-p81]

Enrich `Credit Ratings`: agencies use quantitative and qualitative analysis, rate on a forward-looking basis, and may notch issue ratings from issuer ratings according to seniority. Ratings can be sticky, lag market pricing, focus on credit rather than every risk, and may miss unforeseen changes.[^fi-credit-p82]

Enrich `Credit Spread Risk` and `Yield Spread Measures`: yield spread versus a comparable default-free bond includes credit spread plus liquidity premium. Macro conditions, market liquidity, and issuer performance affect spreads. Investment-grade spread differences tend to be narrower than high-yield differences, and spread-price sensitivity can be approximated with modified duration and convexity.[^fi-credit-p83]

Enrich `Sovereign Credit Analysis`: sovereign repayment capacity differs from corporate analysis because governments tax, issue currency, and fund public services. Qualitative factors include institutions/policy, fiscal flexibility, monetary effectiveness, economic flexibility, and external status. Quantitative factors include debt burden, affordability, real growth and volatility, economic size, currency reserves, and external debt, using the exact ratios presented on pages 85-86.[^fi-credit-p84][^fi-credit-p85][^fi-credit-p86]

Enrich `Municipal Credit Analysis`: general-obligation bonds are unsecured and supported by taxing authority; revenue bonds are supported by project financing such as toll roads, bridges, or airports and depend on a narrower revenue source.[^fi-credit-p86]

Enrich `Corporate Credit Analysis` with its slide-specific bridges. Qualitative analysis covers business model, industry and competition, corporate governance, and business risk. Quantitative analysis covers profitability, coverage, leverage, and cash flow:

$$EBIT\ margin=\frac{Operating\ income}{Revenue}$$

$$Interest\ coverage=\frac{Operating\ income}{Interest\ expense}$$

$$Debt/EBITDA=\frac{Debt}{EBITDA}$$

$$Free\ cash\ flow\ to\ debt=RCF-(Debt-Cash-Marketable\ securities)$$

Keep `Operating Profit Margin`, `Interest Coverage Ratio`, `Debt-to-EBITDA Ratio`, and `Free Cash Flow` tagged to both Financial Statement Analysis and Fixed Income so the graph reflects genuine source-supported crossover.[^fi-credit-p87]

Enrich `Debt Seniority` and `Recovery Rate`: creditors at the same seniority rank are treated as one class; recovery rates generally vary by priority. The slide orders secured debt above senior unsecured, senior subordinated, and junior subordinated claims, while warning that claim priority is not absolute.[^fi-credit-p88]

## Navigation changes on merge

Create `Fixed Income - Credit Risk`, link it from `[[Fixed Income]]`, and connect expected loss, ratings/spreads, sovereign/municipal analysis, corporate analysis, seniority, and the accounting-derived bridge concepts.

## Review checklist

- [x] PDF pages 80-88 were visually inspected.
- [x] Expected-loss and corporate-ratio formulas were visually checked.
- [x] Cross-topic links are limited to relationships explicitly supported by the slides.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^fi-credit-p80]: [[fixed-income-level-1-speed-review.pdf#page=80|Fixed Income Level I Speed Review, PDF p. 80]]
[^fi-credit-p81]: [[fixed-income-level-1-speed-review.pdf#page=81|Fixed Income Level I Speed Review, PDF p. 81]]
[^fi-credit-p82]: [[fixed-income-level-1-speed-review.pdf#page=82|Fixed Income Level I Speed Review, PDF p. 82]]
[^fi-credit-p83]: [[fixed-income-level-1-speed-review.pdf#page=83|Fixed Income Level I Speed Review, PDF p. 83]]
[^fi-credit-p84]: [[fixed-income-level-1-speed-review.pdf#page=84|Fixed Income Level I Speed Review, PDF p. 84]]
[^fi-credit-p85]: [[fixed-income-level-1-speed-review.pdf#page=85|Fixed Income Level I Speed Review, PDF p. 85]]
[^fi-credit-p86]: [[fixed-income-level-1-speed-review.pdf#page=86|Fixed Income Level I Speed Review, PDF p. 86]]
[^fi-credit-p87]: [[fixed-income-level-1-speed-review.pdf#page=87|Fixed Income Level I Speed Review, PDF p. 87]]
[^fi-credit-p88]: [[fixed-income-level-1-speed-review.pdf#page=88|Fixed Income Level I Speed Review, PDF p. 88]]
