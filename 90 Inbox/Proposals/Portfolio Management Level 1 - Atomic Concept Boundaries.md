---
id: proposal-pm-l1-atomic-concept-boundaries
type: proposal
title: Portfolio Management Level 1 - Atomic Concept Boundaries
target: Portfolio Management
change_type: topic-expansion
status: pending-review
tags:
  - cfa/level-1
---

# Portfolio Management Level 1 - Atomic Concept Boundaries

## Rationale

The deck repeatedly uses named risk-return models, lines, performance measures, IPS components, behavioral biases, and risk tools. Each recurring or formula-owning item should be a canonical link target, while shared Equity and Fixed Income concepts remain single nodes.

## Modern Portfolio Theory and Asset Pricing

Proposed canonical notes:

- Holding Period Return, Expected Return, Variance, Standard Deviation, Risk Aversion, Utility Function, Indifference Curve.[^pm-atomic-p4][^pm-atomic-p5]
- Portfolio Expected Return, Portfolio Variance, Correlation, Diversification, Minimum-Variance Frontier, Efficient Frontier, Optimal Risky Portfolio.[^pm-atomic-p6][^pm-atomic-p7]
- Capital Allocation Line, Sharpe Ratio, Market Portfolio, Capital Market Line.[^pm-atomic-p8][^pm-atomic-p9]
- Systematic Risk, Unsystematic Risk, Beta, Portfolio Beta.[^pm-atomic-p10]
- Multifactor Model, Single-Index Model, Market Model, Security Characteristic Line.[^pm-atomic-p11]
- Capital Asset Pricing Model, Security Market Line, Jensen's Alpha, Treynor Ratio, M-Squared, M-Squared Alpha.[^pm-atomic-p12][^pm-atomic-p13][^pm-atomic-p14]

### Visually verified formulas

$$
U=E(R)-\frac{1}{2}A\sigma^2
$$

$$
E(R_p)=w_1R_1+w_2R_2
$$

$$
\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\sigma_1\sigma_2\rho_{12}
$$

[^pm-atomic-p5][^pm-atomic-p6]

$$
E(R_p)=r_f+\frac{R_A-r_f}{\sigma_A}\sigma_p
\qquad
E(R_p)=r_f+\frac{R_M-r_f}{\sigma_M}\sigma_p
$$

[^pm-atomic-p8][^pm-atomic-p9]

$$
\beta_i=\frac{\operatorname{Cov}(R_i,R_M)}{\sigma_M^2}
=\rho_{iM}\frac{\sigma_i}{\sigma_M},
\qquad
\beta_p=\sum_iw_i\beta_i
$$

$$
E(R_i)=r_f+\beta_i[E(R_M)-r_f]
$$

[^pm-atomic-p10][^pm-atomic-p12]

$$
\alpha_p=R_p-[r_f+\beta_p(E(R_M)-r_f)]
$$

$$
\text{Treynor}=\frac{R_p-r_f}{\beta_p},
\quad
\text{Sharpe}=\frac{R_p-r_f}{\sigma_p},
\quad
M^2=(R_p-r_f)\frac{\sigma_M}{\sigma_p}+r_f
$$

[^pm-atomic-p14]

## Portfolio Management Process and IPS

Proposed canonical notes:

- Portfolio Approach, Portfolio Management Process, Planning Step, Execution Step, Feedback Step.[^pm-atomic-p18]
- Defined Contribution Plan, Defined Benefit Plan, Endowment, Foundation, Bank Portfolio, Insurance Portfolio.[^pm-atomic-p19]
- Open-End Mutual Fund, Closed-End Fund, Exchange-Traded Fund, Net Asset Value, ETF Creation and Redemption.[^pm-atomic-p20]
- Active Management, Passive Management, Alternative Investment Management.[^pm-atomic-p21]
- Investment Policy Statement, Return Objective, Risk Objective, Time Horizon Constraint, Tax Constraint, Liquidity Constraint, Legal and Regulatory Constraint, Unique Circumstances.[^pm-atomic-p22]
- Strategic Asset Allocation, Tactical Asset Allocation, Portfolio Construction, Risk Budgeting.[^pm-atomic-p23]
- ESG Integration, Negative Screening, Positive Screening, Best-in-Class Investing, Thematic Investing, Impact Investing, Active Ownership.[^pm-atomic-p24]

Reuse/update existing [[Defined Contribution Plan]] and [[Defined Benefit Plan]] rather than duplicate them; add the Portfolio Management topic and investor-profile application only after approval.[^pm-atomic-p19]

## Behavioral Biases

Proposed canonical notes:

- Cognitive Error, Emotional Bias, Belief Perseverance Error, Information-Processing Error.[^pm-atomic-p27]
- Conservatism Bias, Confirmation Bias, Representativeness Bias, Illusion of Control Bias, Hindsight Bias, Anchoring and Adjustment Bias, Mental Accounting, Framing Bias, Availability Bias.[^pm-atomic-p28]
- Loss Aversion Bias, Overconfidence Bias, Self-Control Bias, Status Quo Bias, Endowment Bias, Regret Aversion Bias.[^pm-atomic-p29]
- Behavioral Market Effects and Limits to Arbitrage.[^pm-atomic-p30]

Reuse the same canonical Mental Accounting, Representativeness Bias, Overconfidence Bias, Conservatism Bias, and Limits to Arbitrage nodes proposed by Equity Investments; their topic lists should contain both maps.[^pm-atomic-p28][^pm-atomic-p29][^pm-atomic-p30]

## Risk Management

Proposed canonical notes:

- Risk Management Framework, Risk Governance, Risk Infrastructure, Risk Appetite, Risk Tolerance, Enterprise Risk Management.[^pm-atomic-p33]
- Financial Risk, Non-Financial Risk, Liquidity Risk, Operational Risk, Model Risk, Settlement Risk, Legal Risk, Regulatory Risk, Political Risk, Reputational Risk.[^pm-atomic-p34]
- Value at Risk, Conditional Value at Risk, Expected Shortfall, Stress Testing, Scenario Analysis, Risk Sensitivity.[^pm-atomic-p35]
- Risk Avoidance, Risk Acceptance, Risk Prevention, Risk Reduction, Risk Transfer, Risk Insurance, Risk Hedging.[^pm-atomic-p36]

Reuse/update existing [[Market Price Risk]] and [[Credit Risk]]. Link credit-risk measurement to existing [[Probability of Default]], [[Loss Given Default]], and [[Exposure at Default]] rather than restating those formulas.[^pm-atomic-p34][^pm-atomic-p35]

## Alias decisions

- MPT resolves to Modern Portfolio Theory as a map section, not a duplicate concept.
- CAL, CML, SML, SCL, CAPM, IPS, SAA, TAA, ETF, NAV, VaR, CVaR, ERM, and ESG resolve to their full canonical titles.
- M2 and Modigliani-Modigliani Measure resolve to M-Squared; Expected Shortfall resolves jointly with CVaR only if the approved note explains the convention.
- Cognitive and emotional bias names shared with Equity resolve to exactly one note.
- Final merge is blocked if the alias registry detects any collision.

## High-value visual candidates

- source-pm-l1-speed-review-p007-efficient-frontier.png — Modern Portfolio Theory → Efficient Frontier; crop the minimum-variance frontier, efficient frontier, and indifference-curve tangency from PDF p. 7.
- source-pm-l1-speed-review-p009-cml.png — Asset Pricing → Capital Market Line; crop the risk-free lending/borrowing and market-portfolio diagram from PDF p. 9.
- source-pm-l1-speed-review-p013-cml-vs-sml.png — Asset Pricing → Security Market Line; crop the CML/SML comparison table from PDF p. 13.
- source-pm-l1-speed-review-p014-performance-measures.png — Performance Evaluation; crop the Jensen/Treynor/M-squared/Sharpe relationship from PDF p. 14.

No crop is proposed for merge yet; searchable formula text remains mandatory.

## Review checklist

- [x] All named source concepts inventoried at review-deck granularity.
- [x] Cross-topic overlaps resolved to existing or shared proposed nodes.
- [x] Formula-heavy pages visually verified.
- [x] Aliases mapped to one canonical English title.
- [x] No trusted note changed.
- [ ] User approves concept boundaries, map creation, and updates.

## Evidence

[^pm-atomic-p4]: [[portfolio-management-level-1-speed-review.pdf#page=4|Portfolio Management Level I Speed Review, PDF p. 4]]
[^pm-atomic-p5]: [[portfolio-management-level-1-speed-review.pdf#page=5|Portfolio Management Level I Speed Review, PDF p. 5]]
[^pm-atomic-p6]: [[portfolio-management-level-1-speed-review.pdf#page=6|Portfolio Management Level I Speed Review, PDF p. 6]]
[^pm-atomic-p7]: [[portfolio-management-level-1-speed-review.pdf#page=7|Portfolio Management Level I Speed Review, PDF p. 7]]
[^pm-atomic-p8]: [[portfolio-management-level-1-speed-review.pdf#page=8|Portfolio Management Level I Speed Review, PDF p. 8]]
[^pm-atomic-p9]: [[portfolio-management-level-1-speed-review.pdf#page=9|Portfolio Management Level I Speed Review, PDF p. 9]]
[^pm-atomic-p10]: [[portfolio-management-level-1-speed-review.pdf#page=10|Portfolio Management Level I Speed Review, PDF p. 10]]
[^pm-atomic-p11]: [[portfolio-management-level-1-speed-review.pdf#page=11|Portfolio Management Level I Speed Review, PDF p. 11]]
[^pm-atomic-p12]: [[portfolio-management-level-1-speed-review.pdf#page=12|Portfolio Management Level I Speed Review, PDF p. 12]]
[^pm-atomic-p13]: [[portfolio-management-level-1-speed-review.pdf#page=13|Portfolio Management Level I Speed Review, PDF p. 13]]
[^pm-atomic-p14]: [[portfolio-management-level-1-speed-review.pdf#page=14|Portfolio Management Level I Speed Review, PDF p. 14]]
[^pm-atomic-p18]: [[portfolio-management-level-1-speed-review.pdf#page=18|Portfolio Management Level I Speed Review, PDF p. 18]]
[^pm-atomic-p19]: [[portfolio-management-level-1-speed-review.pdf#page=19|Portfolio Management Level I Speed Review, PDF p. 19]]
[^pm-atomic-p20]: [[portfolio-management-level-1-speed-review.pdf#page=20|Portfolio Management Level I Speed Review, PDF p. 20]]
[^pm-atomic-p21]: [[portfolio-management-level-1-speed-review.pdf#page=21|Portfolio Management Level I Speed Review, PDF p. 21]]
[^pm-atomic-p22]: [[portfolio-management-level-1-speed-review.pdf#page=22|Portfolio Management Level I Speed Review, PDF p. 22]]
[^pm-atomic-p23]: [[portfolio-management-level-1-speed-review.pdf#page=23|Portfolio Management Level I Speed Review, PDF p. 23]]
[^pm-atomic-p24]: [[portfolio-management-level-1-speed-review.pdf#page=24|Portfolio Management Level I Speed Review, PDF p. 24]]
[^pm-atomic-p27]: [[portfolio-management-level-1-speed-review.pdf#page=27|Portfolio Management Level I Speed Review, PDF p. 27]]
[^pm-atomic-p28]: [[portfolio-management-level-1-speed-review.pdf#page=28|Portfolio Management Level I Speed Review, PDF p. 28]]
[^pm-atomic-p29]: [[portfolio-management-level-1-speed-review.pdf#page=29|Portfolio Management Level I Speed Review, PDF p. 29]]
[^pm-atomic-p30]: [[portfolio-management-level-1-speed-review.pdf#page=30|Portfolio Management Level I Speed Review, PDF p. 30]]
[^pm-atomic-p33]: [[portfolio-management-level-1-speed-review.pdf#page=33|Portfolio Management Level I Speed Review, PDF p. 33]]
[^pm-atomic-p34]: [[portfolio-management-level-1-speed-review.pdf#page=34|Portfolio Management Level I Speed Review, PDF p. 34]]
[^pm-atomic-p35]: [[portfolio-management-level-1-speed-review.pdf#page=35|Portfolio Management Level I Speed Review, PDF p. 35]]
[^pm-atomic-p36]: [[portfolio-management-level-1-speed-review.pdf#page=36|Portfolio Management Level I Speed Review, PDF p. 36]]
