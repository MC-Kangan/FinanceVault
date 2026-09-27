---
id: proposal-fsa-l1-income-taxes
type: proposal
title: Financial Statement Analysis Level 1 - Income Taxes
target: "[[Financial Statement Analysis]]"
change_type: topic-expansion
status: merged
tags:
  - cfa/level-1
---

# Financial Statement Analysis Level 1 - Income Taxes

## Rationale

The pilot omitted the complete income-tax chapter. Deferred tax assets and liabilities are distinct analytical nodes, not subsections of one generic tax note, because they arise from different temporary differences and can affect forecasts, valuation allowances, leverage interpretation, and earnings quality.

## Proposed canonical concepts

### `Taxable Income`

Taxable income is taxable revenue less deductible expense; tax payable is taxable income multiplied by the applicable tax rate and represents a current tax obligation and eventual cash outflow.[^fsa-tax-p73]

$$
\text{Taxable income}=\text{Taxable revenue}-\text{Deductible expense}
$$

$$
\text{Tax payable}=\text{Taxable income}\times\text{Tax rate}
$$

[^fsa-tax-p73]

Aliases to review: `Tax Return Income`, `应税收入`.

### `Income Tax Expense`

Income tax expense reconciles current tax payable with changes in deferred tax balances.[^fsa-tax-p73][^fsa-tax-p78]

$$
\text{Income tax expense}=\text{Current tax payable}+\Delta DTL-\Delta DTA
$$

$$
\text{Net income}=\text{Pretax accounting income}-\text{Income tax expense}
$$

[^fsa-tax-p73]

Aliases to review: `Tax Expense`, `Income Tax Provision`, `所得税费用`.

### `Tax Base`

An asset's tax base is the amount deductible against future taxable benefits. A liability's tax base is its carrying amount less amounts deductible for tax in future periods. The source applies these rules to depreciable assets, receivables, research and development costs, payables, warranties, and customer advances.[^fsa-tax-p74][^fsa-tax-p75]

Aliases to review: `Tax Basis`, `计税基础`.

### `Temporary Difference`

A temporary difference is the difference between an asset or liability's financial-statement carrying value and tax base that will reverse in a future period. A taxable temporary difference generally creates a deferred tax liability; a deductible temporary difference generally creates a deferred tax asset.[^fsa-tax-p74][^fsa-tax-p75]

Aliases to review: `Timing Difference`, `Temporary Tax Difference`, `暂时性差异`.

### `Permanent Difference`

A permanent difference affects accounting income or taxable income but does not reverse in later periods. It affects the effective tax rate but does not create a deferred tax balance.[^fsa-tax-p74]

Aliases to review: `Permanent Tax Difference`, `永久性差异`.

### `Deferred Tax Asset`

A deferred tax asset arises from deductible temporary differences and tax-loss carryforwards when future tax benefits are expected to be realizable. For assets, carrying value below tax base indicates a DTA; for liabilities, carrying value above tax base indicates a DTA.[^fsa-tax-p75]

$$
DTA=\text{Deductible temporary difference}\times\text{Expected future tax rate}
$$

[^fsa-tax-p78]

The source requires recoverability to be reassessed at each balance-sheet date. IFRS reduces the recognized DTA when recovery is not expected, whereas the source's US-GAAP presentation uses a valuation allowance.[^fsa-tax-p76]

Aliases to review: `DTA`, `Deferred Tax Asset`, `递延所得税资产`.

### `Deferred Tax Liability`

A deferred tax liability arises from taxable temporary differences. For assets, carrying value above tax base indicates a DTL; for liabilities, carrying value below tax base indicates a DTL.[^fsa-tax-p75]

$$
DTL=\text{Taxable temporary difference}\times\text{Expected future tax rate}
$$

[^fsa-tax-p78]

For analysis, the source suggests that a DTL unlikely to reverse may be treated more like equity, while a DTL expected to reverse remains a true liability.[^fsa-tax-p77]

Aliases to review: `DTL`, `Deferred Tax Liability`, `递延所得税负债`.

### `Tax Loss Carryforward`

A tax loss carryforward can create a deferred tax asset because future taxable income may be offset by the unused loss, subject to the expectation that the benefit will be realized.[^fsa-tax-p75][^fsa-tax-p76]

Aliases to review: `Net Operating Loss Carryforward`, `NOL Carryforward`, `Tax-Loss Carryforward`, `税务亏损结转`.

### `Valuation Allowance`

Under the source's US-GAAP presentation, a valuation allowance reduces a deferred tax asset when realization is not expected. A larger allowance is associated with more conservative reported net DTA, and the allowance can reverse when recovery becomes expected.[^fsa-tax-p76]

Aliases to review: `DTA Valuation Allowance`, `Deferred Tax Valuation Allowance`, `估值备抵`.

### `Effective Tax Rate`

The effective tax rate relates reported income tax expense to pretax accounting income and is useful for analyzing reported earnings.[^fsa-tax-p79]

$$
\text{Effective tax rate}=\frac{\text{Income tax expense}}{\text{Pretax accounting income}}
$$

[^fsa-tax-p79]

Aliases to review: `ETR`, `Effective Income Tax Rate`, `实际税率`.

### `Cash Tax Rate`

The cash tax rate relates cash taxes paid to pretax accounting income and is useful for cash-flow forecasting.[^fsa-tax-p79]

$$
\text{Cash tax rate}=\frac{\text{Cash taxes paid}}{\text{Pretax accounting income}}
$$

[^fsa-tax-p79]

Aliases to review: `Cash Taxes to Pretax Income`, `现金税率`.

## Link changes

- Link `Deferred Tax Asset` to `Valuation Allowance`, `Tax Loss Carryforward`, aggressive/conservative accounting, and income-statement forecasting.
- Link `Deferred Tax Liability` to solvency analysis, equity adjustments, and `Corporate Credit Analysis`.
- Contrast `Effective Tax Rate` with `Cash Tax Rate`; both link to `Income Tax Expense`, while the statutory tax rate is an input rather than a synonym.
- Link `Temporary Difference` and `Permanent Difference` as contrasts, not aliases.

## Review checklist

- [x] Pages 73-79 were visually inspected.
- [x] DTA and DTL are separate canonical concepts with directional rules.
- [x] Formulas were checked against the rendered pages.
- [x] Trusted notes remain unchanged.
- [ ] User approves concepts and aliases.

## Evidence

[^fsa-tax-p73]: [[financial-statement-analysis-level-1-speed-review.pdf#page=73|Financial Statement Analysis Level I Speed Review, PDF p. 73]]
[^fsa-tax-p74]: [[financial-statement-analysis-level-1-speed-review.pdf#page=74|Financial Statement Analysis Level I Speed Review, PDF p. 74]]
[^fsa-tax-p75]: [[financial-statement-analysis-level-1-speed-review.pdf#page=75|Financial Statement Analysis Level I Speed Review, PDF p. 75]]
[^fsa-tax-p76]: [[financial-statement-analysis-level-1-speed-review.pdf#page=76|Financial Statement Analysis Level I Speed Review, PDF p. 76]]
[^fsa-tax-p77]: [[financial-statement-analysis-level-1-speed-review.pdf#page=77|Financial Statement Analysis Level I Speed Review, PDF p. 77]]
[^fsa-tax-p78]: [[financial-statement-analysis-level-1-speed-review.pdf#page=78|Financial Statement Analysis Level I Speed Review, PDF p. 78]]
[^fsa-tax-p79]: [[financial-statement-analysis-level-1-speed-review.pdf#page=79|Financial Statement Analysis Level I Speed Review, PDF p. 79]]
