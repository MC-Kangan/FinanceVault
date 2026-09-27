---
id: proposal-fsa-l1-leases-pensions-share-compensation
type: proposal
title: Financial Statement Analysis Level 1 - Leases, Pensions, and Share-Based Compensation
target: "[[Financial Statement Analysis]]"
change_type: topic-expansion
status: merged
tags:
  - cfa/level-1
---

# Financial Statement Analysis Level 1 - Leases, Pensions, and Share-Based Compensation

## Rationale

The pilot omitted this entire chapter. Each accounting model below becomes a reusable canonical node because it has distinct recognition, cash-flow, ratio, or analytical consequences.

## Proposed canonical concepts

### `Lease Classification`

A lease conveys the right to use an identified asset for consideration. The finance-lease indicators include transfer of ownership, a purchase option reasonably certain to be exercised, a lease term covering a major part of useful life, present value of payments representing substantially all fair value, or a specialized asset with no alternative use. A lease not meeting those indicators is classified as operating in the source framework.[^fsa-lease-p62]

Aliases to review: `Finance Lease Criteria`, `Lease Accounting Classification`, `租赁分类`.

### `Finance Lease`

For a lessee, initial recognition includes a right-of-use asset and lease liability. Each payment is split between interest and principal; interest equals the opening lease liability times the periodic rate, and the liability follows the effective-interest method. The source classifies interest as CFO and principal as CFF, and presents total expense as front-loaded.[^fsa-lease-p64]

$$
\text{Interest expense}_t=\text{Opening lease liability}_t\times r
$$

[^fsa-lease-p64]

Aliases to review: `Finance Lease Accounting`, `融资租赁`.

### `Operating Lease`

The source's US-GAAP lessee model recognizes a right-of-use asset and lease liability but reports a single straight-line lease expense and operating cash outflow. The right-of-use asset is adjusted so total lease expense stays level.[^fsa-lease-p64]

Aliases to review: `Operating Lease Accounting`, `经营租赁`.

### `Right-of-Use Asset`

Create a separate node for the lessee asset because it links lease recognition to amortization, impairment, liabilities, cash-flow classification, and ratio analysis. Short-term and low-value exemptions remain a section of this note and `Lease Classification`.[^fsa-lease-p63][^fsa-lease-p64]

Aliases to review: `ROU Asset`, `Right of Use Asset`, `使用权资产`.

### `Lessor Accounting`

For a finance lease, the source derecognizes the leased asset and recognizes a lease receivable; receipts comprise interest and receivable recovery. For an operating lease, the lessor retains the asset and separately recognizes lease income and depreciation.[^fsa-lease-p65]

Aliases to review: `Lease Receivable`, `出租人会计`.

### `Defined Contribution Plan`

The employer's agreed contribution is pension expense and an operating cash outflow. The employee owns the plan balance and bears investment risk, so the employer has no obligation beyond the specified contribution.[^fsa-pension-p67]

Aliases to review: `DC Plan`, `Defined Contribution Pension`, `固定缴款计划`.

### `Defined Benefit Plan`

The employer promises a benefit based on financial and actuarial assumptions and bears actuarial and investment risk. The present value of the obligation uses a discount rate based on high-quality corporate bond yields in the source.[^fsa-pension-p67]

Aliases to review: `DB Plan`, `Defined Benefit Pension`, `固定收益养老金计划`.

### `Pension Funded Status`

Funded status compares plan assets with the present value of the defined benefit obligation. A surplus is a net pension asset and a deficit is a net pension liability.[^fsa-pension-p67]

$$
\text{Funded status}=\text{Fair value of plan assets}-\text{Present value of pension obligation}
$$

[^fsa-pension-p67]

Aliases to review: `Funded Status`, `Net Pension Asset`, `Net Pension Liability`, `养老金资金状况`.

### `Defined Benefit Pension Expense`

Under IFRS in the source, profit or loss contains service cost and net interest on the opening net pension liability or asset. Remeasurements—including actuarial gains and losses and actual plan return less the return included in net interest—go to OCI and are not subsequently amortized into profit or loss.[^fsa-pension-p68]

Under US GAAP in the source, profit or loss includes current service cost, interest on the beginning obligation, and expected return on plan assets; past service cost, actuarial gains and losses, and actual less expected return first enter OCI, with amortization mechanics shown separately.[^fsa-pension-p68]

Aliases to review: `Pension Expense`, `Periodic Pension Cost`, `养老金费用`.

### `Equity-Settled Share-Based Compensation`

Equity-settled awards include restricted shares and employee stock options. The grant-date fair value is recognized as compensation expense over the vesting period; stock grants use market price and option grants use an option-pricing model. The arrangement avoids current cash outflow but can dilute shareholders.[^fsa-share-p69]

Aliases to review: `Equity-Settled Share Compensation`, `Stock-Based Compensation`, `权益结算股份支付`.

### `Cash-Settled Share-Based Compensation`

Cash-settled awards include stock-appreciation rights and phantom shares. They avoid share dilution but create a cash obligation; fair value is remeasured at each balance-sheet date and expense is recognized over the service period.[^fsa-share-p70]

Aliases to review: `Cash-Settled Share Compensation`, `SAR`, `Phantom Shares`, `现金结算股份支付`.

## Link changes

- Connect both pension plan types to `Pension Funded Status`; connect funded status and pension expense to `Balance Sheet`, the Income Statement branch, cash flow, and `Corporate Credit Analysis`.
- Connect `Right-of-Use Asset` and lease liabilities to solvency ratios and credit analysis.
- Contrast the two share-based compensation settlement methods and link them to diluted EPS.

## Review checklist

- [x] Pages 62-70 were visually inspected.
- [x] Each recurring accounting model is a separate proposed node.
- [x] Trusted notes remain unchanged.
- [ ] User approves concepts and aliases.

## Evidence

[^fsa-lease-p62]: [[financial-statement-analysis-level-1-speed-review.pdf#page=62|Financial Statement Analysis Level I Speed Review, PDF p. 62]]
[^fsa-lease-p63]: [[financial-statement-analysis-level-1-speed-review.pdf#page=63|Financial Statement Analysis Level I Speed Review, PDF p. 63]]
[^fsa-lease-p64]: [[financial-statement-analysis-level-1-speed-review.pdf#page=64|Financial Statement Analysis Level I Speed Review, PDF p. 64]]
[^fsa-lease-p65]: [[financial-statement-analysis-level-1-speed-review.pdf#page=65|Financial Statement Analysis Level I Speed Review, PDF p. 65]]
[^fsa-pension-p67]: [[financial-statement-analysis-level-1-speed-review.pdf#page=67|Financial Statement Analysis Level I Speed Review, PDF p. 67]]
[^fsa-pension-p68]: [[financial-statement-analysis-level-1-speed-review.pdf#page=68|Financial Statement Analysis Level I Speed Review, PDF p. 68]]
[^fsa-share-p69]: [[financial-statement-analysis-level-1-speed-review.pdf#page=69|Financial Statement Analysis Level I Speed Review, PDF p. 69]]
[^fsa-share-p70]: [[financial-statement-analysis-level-1-speed-review.pdf#page=70|Financial Statement Analysis Level I Speed Review, PDF p. 70]]
