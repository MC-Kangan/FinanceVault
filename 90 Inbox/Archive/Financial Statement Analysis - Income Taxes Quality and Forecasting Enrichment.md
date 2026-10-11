---
id: proposal-fsa-l1-income-taxes-quality-forecasting-enrichment
type: proposal
title: Financial Statement Analysis - Income Taxes Quality and Forecasting Enrichment
target: "[[Financial Statement Analysis]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Financial Statement Analysis - Income Taxes Quality and Forecasting Enrichment

## Rationale

The current tax, reporting-quality, and forecasting notes identify the concepts but do not consistently retain the source's reconciliation formulas, tax-base examples, recoverability treatment, quality spectrum, accounting-choice comparison, or forecast construction guidance.

## Exact proposed content

### Income tax accounting

Enrich `Taxable Income` and `Income Tax Expense` with the distinction between taxable income used to determine current tax payable and pretax accounting income reported in the financial statements. Retain the source reconciliation:

$$
Income\ tax\ expense=Current\ tax\ payable+\Delta DTL-\Delta DTA
$$

and link it to the net-income bridge.[^fsa-itqf-p73]

Enrich `Temporary Difference`, `Permanent Difference`, `Deferred Tax Asset`, and `Deferred Tax Liability`: timing differences that reverse are temporary, while differences that do not reverse are permanent. A taxable temporary difference creates a DTL; a deductible temporary difference creates a DTA.[^fsa-itqf-p74]

Enrich `Tax Base` with the source mechanics. For an asset, tax base is the amount deductible against future taxable economic benefits. Examples include depreciable assets, receivables, and capitalized or expensed R&D. For a liability, tax base is carrying value less amounts deductible for tax in future periods; the slide shows accounts payable and other payables with tax base equal to carrying value, while warranty liabilities and customer advances can have a zero tax base.[^fsa-itqf-p74][^fsa-itqf-p75]

Add the source matrix to the tax branch:

| Item | Carrying value versus tax base | Deferred-tax result |
| --- | --- | --- |
| Asset | Carrying value greater than tax base | DTL |
| Asset | Carrying value less than tax base | DTA |
| Liability | Carrying value greater than tax base | DTA |
| Liability | Carrying value less than tax base | DTL |

Enrich `Tax Loss Carryforward`: tax-loss carryforwards create a DTA subject to the recoverability assessment shown in the source.[^fsa-itqf-p75]

Enrich `Valuation Allowance` and `Deferred Tax Asset`: recognize a DTA only when realization is sufficiently supported and reassess it over time. The slide presents IFRS as reducing the DTA directly and US GAAP as recording a valuation allowance. Later improvement in expected recovery can reverse the reduction or allowance within the source framework.[^fsa-itqf-p76]

Enrich `Deferred Tax Liability` and the tax-analysis section with the source's analytical treatment: a DTL may be treated as equity if it is not expected to reverse and as a liability when reversal is expected. Preserve the slide's presentation convention that deferred-tax balances are not netted and that US GAAP and IFRS classification differ as shown.[^fsa-itqf-p77]

Retain the complete calculation set:

$$
Current\ tax\ payable=Taxable\ income\times Current\ tax\ rate
$$

$$
DTA\ or\ DTL=Temporary\ difference\times Expected\ future\ tax\ rate
$$

$$
Income\ tax\ expense=Current\ tax\ payable+\Delta DTL-\Delta DTA
$$

[^fsa-itqf-p78]

Enrich `Effective Tax Rate` and `Cash Tax Rate` with:

$$
Effective\ tax\ rate=\frac{Income\ tax\ expense}{Pretax\ income}
$$

$$
Cash\ tax\ rate=\frac{Cash\ taxes\ paid}{Pretax\ income}
$$

The source positions the effective rate as useful for earnings forecasts and the cash rate as useful for cash-flow forecasts.[^fsa-itqf-p79]

### Reporting and earnings quality

Enrich `Financial Reporting Quality` and `Earnings Quality` with the source distinction: reporting quality asks whether information faithfully represents economic reality and is decision-useful, while earnings quality asks whether reported earnings are sustainable and adequate. Preserve the source's quality spectrum rather than treating quality as a binary label.[^fsa-itqf-p82]

Enrich `Aggressive Accounting` and `Conservative Accounting` with the source comparison:

| Accounting choice | Aggressive presentation | Conservative presentation |
| --- | --- | --- |
| Expenditure | Capitalize | Expense |
| Useful life | Longer | Shorter |
| Salvage value | Higher | Lower |
| DTA valuation allowance | Smaller | Larger |

Enrich `Fraud Triangle` with its three source elements and contextual explanation: incentive or pressure, opportunity, and rationalization.[^fsa-itqf-p83]

### Forecasting

Enrich `Financial Statement Forecasting` with the source construction sequence:

- Forecast revenue using a top-down year-over-year approach.
- Forecast COGS as $(1-Gross\ margin)\times Forecast\ revenue$.
- Separate variable and fixed SG&A behavior where the slide indicates.
- Forecast net interest from opening debt and the market rate, less interest income.
- Link balance-sheet items to forecast operating drivers when appropriate; PP&E and intangible assets require separate maintenance and growth capital-expenditure consideration.
- Check leverage ratios as part of forecast consistency.[^fsa-itqf-p84]

Enrich `Forecasting Bias` with the named biases shown in the slide, but keep each as a concise pitfall rather than creating unsupported stand-alone nodes. Link `Porter's Five Forces` as the industry-analysis framework used to challenge forecast assumptions.[^fsa-itqf-p85]

Enrich `Inflation and Financial Forecasts`: inflation can raise costs and revenue; whether margins are preserved depends on the ability to pass costs through without losing excessive volume or market share, which is influenced by price elasticity, industry conditions, and strategy.[^fsa-itqf-p86]

Enrich `Normalized Earnings` as mid-cycle earnings that remove unusual or temporary effects for forecasting and valuation use.[^fsa-itqf-p86]

## Navigation changes on merge

Create subtopic maps `FSA - Income Taxes`, `FSA - Financial Reporting Quality`, and `FSA - Forecasting`. Link them from `Financial Statement Analysis` and use them to replace the current flat concept dump while preserving every reachable concept.

## Review checklist

- [x] Every proposed claim and formula is drawn from the registered FSA source.
- [x] Formula signs, matrix directions, and accounting-choice comparisons were visually checked against rendered pages.
- [x] Existing aliases and canonical filenames remain unchanged.
- [x] Trusted notes and Personal Notes remain unchanged at proposal stage.
- [x] User approves this enrichment bundle.
- [x] Merge preserves every Personal Notes block byte-for-byte.
- [x] Post-merge validation and graph inspection pass.

## Evidence

[^fsa-itqf-p73]: [[financial-statement-analysis-level-1-speed-review.pdf#page=73|Financial Statement Analysis Level I Speed Review, PDF p. 73]]
[^fsa-itqf-p74]: [[financial-statement-analysis-level-1-speed-review.pdf#page=74|Financial Statement Analysis Level I Speed Review, PDF p. 74]]
[^fsa-itqf-p75]: [[financial-statement-analysis-level-1-speed-review.pdf#page=75|Financial Statement Analysis Level I Speed Review, PDF p. 75]]
[^fsa-itqf-p76]: [[financial-statement-analysis-level-1-speed-review.pdf#page=76|Financial Statement Analysis Level I Speed Review, PDF p. 76]]
[^fsa-itqf-p77]: [[financial-statement-analysis-level-1-speed-review.pdf#page=77|Financial Statement Analysis Level I Speed Review, PDF p. 77]]
[^fsa-itqf-p78]: [[financial-statement-analysis-level-1-speed-review.pdf#page=78|Financial Statement Analysis Level I Speed Review, PDF p. 78]]
[^fsa-itqf-p79]: [[financial-statement-analysis-level-1-speed-review.pdf#page=79|Financial Statement Analysis Level I Speed Review, PDF p. 79]]
[^fsa-itqf-p82]: [[financial-statement-analysis-level-1-speed-review.pdf#page=82|Financial Statement Analysis Level I Speed Review, PDF p. 82]]
[^fsa-itqf-p83]: [[financial-statement-analysis-level-1-speed-review.pdf#page=83|Financial Statement Analysis Level I Speed Review, PDF p. 83]]
[^fsa-itqf-p84]: [[financial-statement-analysis-level-1-speed-review.pdf#page=84|Financial Statement Analysis Level I Speed Review, PDF p. 84]]
[^fsa-itqf-p85]: [[financial-statement-analysis-level-1-speed-review.pdf#page=85|Financial Statement Analysis Level I Speed Review, PDF p. 85]]
[^fsa-itqf-p86]: [[financial-statement-analysis-level-1-speed-review.pdf#page=86|Financial Statement Analysis Level I Speed Review, PDF p. 86]]
