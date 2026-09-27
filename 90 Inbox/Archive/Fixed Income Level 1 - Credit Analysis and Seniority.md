---
id: proposal-fi-l1-credit-analysis-seniority
type: proposal
title: Fixed Income Level 1 - Credit Analysis and Seniority
target: "[[Fixed Income]]"
change_type: topic-expansion
status: merged
tags:
  - cfa/level-1
---

# Fixed Income Level 1 - Credit Analysis and Seniority

## Rationale

Extend the existing credit pilot with ratings, sovereign and municipal analysis, spread sensitivity, and debt seniority while preserving the accounting-to-credit bridge already established in the vault.

## Proposed updates to trusted concepts

### `Credit Risk` and `Expected Loss`

The current trusted notes already cover the core definition and expected-loss identity. Propose adding the distinction between expected loss expressed in currency and as a percentage of exposure, plus the compensation comparison between expected loss and credit spread.[^fi-credit-p80]

$$
EL=PD\times LGD
$$

$$
LGD_{\text{currency}}=EAD\times(1-RR)
$$

$$
LGD_{\%}=1-RR
$$

[^fi-credit-p80]

### `Corporate Credit Analysis`

Propose retaining qualitative assessment of business model, industry and competition, corporate governance, and business risk, then linking quantitative profitability, coverage, leverage, and retained-cash-flow measures to the accounting concepts that generate them.[^fi-credit-p87]

$$
\text{EBIT margin}=\frac{\text{Operating income}}{\text{Revenue}}
$$

$$
\text{EBIT to interest expense}=\frac{\text{Operating income}}{\text{Interest expense}}
$$

$$
\text{Debt to EBITDA}=\frac{\text{Debt}}{\text{EBITDA}}
$$

$$
\text{RCF to net debt}=\frac{\text{Retained cash flow}}{\text{Debt}-\text{Cash and marketable securities}}
$$

[^fi-credit-p87]

Existing `Interest Coverage Ratio` and `Debt-to-EBITDA Ratio` remain the canonical destinations for the coverage and leverage formulas.

## Proposed canonical concepts

### `Credit Ratings`

- Rating agencies independently assess issuer credit risk using forward-looking qualitative and quantitative analysis. Credit migration or downgrade risk can widen spreads and lower price.[^fi-credit-p82]
- Distinguish issuer and issue ratings, explain notching relative to senior unsecured debt, and caution that ratings can be sticky, lag market pricing, and miss difficult-to-model risks.[^fi-credit-p82]

Aliases to review: `Credit Rating`, `Rating Migration`, `信用评级`.

### `Credit Spread Risk`

- A bond's yield spread over a comparable default-free bond reflects credit spread plus liquidity premium and responds to macroeconomic, market, and issuer-specific factors.[^fi-credit-p83]
- High-yield spread levels and spread changes are generally larger than those within investment grade. The price effect of a spread change can be approximated with duration and convexity.[^fi-credit-p83]

$$
\frac{\Delta P}{P}\approx-D_{\text{mod}}\Delta s+\frac{1}{2}C(\Delta s)^2
$$

[^fi-credit-p83]

Aliases to review: `Spread Risk`, `Credit Spread`, `信用利差风险`.

### `Sovereign Credit Analysis`

- Government debt supports fiscal policy and public expenditure and is repaid primarily from tax and other government revenue. Analysis combines willingness and ability to pay.[^fi-credit-p84]
- Qualitative factors include institutions and policy, external status, fiscal flexibility, monetary effectiveness, and economic flexibility.[^fi-credit-p84]
- Quantitative factors include debt burden, debt affordability, growth and volatility, economic scale, foreign-exchange reserves, and external debt.[^fi-credit-p85][^fi-credit-p86]

Representative formulas:

$$
\text{Debt to GDP}=\frac{\text{General government debt}}{GDP}
$$

$$
\text{Interest to revenue}=\frac{\text{Government interest payments}}{\text{Government revenue}}
$$

$$
\text{Reserve ratio}=\frac{\text{FX reserves}}{\text{External debt}}
$$

[^fi-credit-p85][^fi-credit-p86]

Aliases to review: `Sovereign Risk Analysis`, `Government Credit Analysis`, `主权信用分析`.

### `Municipal Credit Analysis`

- General-obligation bonds are unsecured local-government debt supported by taxing authority. Revenue bonds finance specific projects and rely on a narrower revenue source, making project cash-flow analysis central.[^fi-credit-p86]

Aliases to review: `Local Government Credit Analysis`, `Municipal Bond Analysis`, `地方政府信用分析`.

### `Debt Seniority`

- Seniority ranks the priority of payment or claims. Creditors at the same level are treated as one class, and recovery rates vary with priority, although legal outcomes do not always follow an absolute ordering.[^fi-credit-p88]
- The proposed order runs from first-lien or mortgage and other secured claims through senior unsecured, senior subordinated, subordinated, and junior subordinated claims; secured debt generally has lower LGD because of direct collateral claims.[^fi-credit-p88]

![[source-fi-l1-speed-review-p088-seniority-ranking.png]]

Figure: The seniority ladder links claim priority and collateral support to expected recovery and LGD.[^fi-credit-p88]

Aliases to review: `Seniority Ranking`, `Priority of Claims`, `Capital Structure Priority`, `债务偿还顺序`.

## Link and alias changes

- Connect `Credit Spread Risk` to existing `Credit Risk`, `Modified Duration`, and `Convexity`.
- Connect `Debt Seniority` to existing `Expected Loss` through recovery rate and LGD.
- Connect `Sovereign Credit Analysis` and `Municipal Credit Analysis` to proposed `Sovereign and Non-Sovereign Bonds`.
- Preserve the existing route from `Corporate Credit Analysis` to `Interest Coverage Ratio`, `Debt-to-EBITDA Ratio`, and the FSA map.
- Proposed aliases remain unregistered until collision validation passes.

## Review checklist

- [x] Claims and formulas were visually checked against pages 80-88.
- [x] Existing credit and accounting bridge notes remain unchanged.
- [x] Proposed seniority figure is legible and page-addressable.
- [ ] User approves concept boundaries and aliases.
- [ ] Approved concepts are created through the merge workflow.

## Evidence

[^fi-credit-p80]: [[fixed-income-level-1-speed-review.pdf#page=80|Fixed Income Level I Speed Review, PDF p. 80]]
[^fi-credit-p82]: [[fixed-income-level-1-speed-review.pdf#page=82|Fixed Income Level I Speed Review, PDF p. 82]]
[^fi-credit-p83]: [[fixed-income-level-1-speed-review.pdf#page=83|Fixed Income Level I Speed Review, PDF p. 83]]
[^fi-credit-p84]: [[fixed-income-level-1-speed-review.pdf#page=84|Fixed Income Level I Speed Review, PDF p. 84]]
[^fi-credit-p85]: [[fixed-income-level-1-speed-review.pdf#page=85|Fixed Income Level I Speed Review, PDF p. 85]]
[^fi-credit-p86]: [[fixed-income-level-1-speed-review.pdf#page=86|Fixed Income Level I Speed Review, PDF p. 86]]
[^fi-credit-p87]: [[fixed-income-level-1-speed-review.pdf#page=87|Fixed Income Level I Speed Review, PDF p. 87]]
[^fi-credit-p88]: [[fixed-income-level-1-speed-review.pdf#page=88|Fixed Income Level I Speed Review, PDF p. 88]]
