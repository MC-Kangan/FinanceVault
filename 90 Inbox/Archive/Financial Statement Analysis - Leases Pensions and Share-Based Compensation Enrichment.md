---
id: proposal-fsa-l1-leases-pensions-share-compensation-enrichment
type: proposal
title: Financial Statement Analysis - Leases Pensions and Share-Based Compensation Enrichment
target: "[[Financial Statement Analysis]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Financial Statement Analysis - Leases Pensions and Share-Based Compensation Enrichment

## Rationale

The current notes establish the correct atomic concepts but do not consistently retain the source's classification criteria, cash-flow treatment, expense pattern, pension-risk allocation, or share-based-compensation remeasurement mechanics.

## Exact proposed content

### Lease classification

Enrich `Lease Classification`, `Finance Lease`, and `Operating Lease` with the five finance-lease indicators in the source: ownership transfers, a purchase option is reasonably certain to be exercised, the lease term covers a major part of the asset's economic life, the present value of lease payments represents substantially all of the asset's fair value, or the asset is sufficiently specialized that the lessor has no alternative use. Otherwise the lease is operating.[^fsa-lpsc-p62]

Retain the source's stated leasing advantages: less initial cash, potentially cheaper financing, reduced obsolescence risk for the lessee, fewer restrictive covenants, and possible tax advantages.[^fsa-lpsc-p62]

Enrich the classification map with the source framework: IFRS lessees use a single recognition model subject to short-term and low-value exemptions; US-GAAP lessees distinguish finance and operating leases; lessors distinguish finance and operating leases.[^fsa-lpsc-p63]

### Lessee accounting

Enrich `Right-of-Use Asset`, `Finance Lease`, and `Operating Lease` with the complete lessee comparison:

| Treatment | Initial balance sheet | Cash-flow classification | Expense pattern | Liability measurement |
| --- | --- | --- | --- | --- |
| IFRS / US finance lease | ROU asset and lease liability | Interest as CFO outflow and principal as CFF outflow in the source table | Interest plus straight-line ROU amortization; total expense declines | Effective-interest method |
| US operating lease | ROU asset and lease liability | Full payment as CFO outflow | Single lease expense equal to the periodic payment; level total expense | Effective-interest method, with the ROU asset adjusted to produce the level expense |
| Short-term or low-value exemption | No recognized ROU asset or lease liability | Payment as CFO outflow | Straight-line rental expense | Not applicable |

For finance leases, interest equals opening lease liability multiplied by the periodic rate.[^fsa-lpsc-p64]

### Lessor accounting

Enrich `Lessor Accounting` with:

| Treatment | Initial accounting | Cash receipt | Income pattern |
| --- | --- | --- | --- |
| Finance lease | Derecognize the leased asset and recognize a lease receivable | Interest plus recovery of the lease receivable, classified as CFO in the source | A single interest-income stream that declines as the receivable amortizes |
| Operating lease | Keep the underlying asset | Lease cash inflow | Lease income and depreciation remain separate; the source presents a level revenue/expense pattern |

Finance-lease interest income equals the opening lease receivable multiplied by the periodic rate, and the receivable follows the effective-interest method.[^fsa-lpsc-p65]

### Pension plans

Enrich `Defined Contribution Plan` with the source's risk allocation: the employer's contribution is pension expense and a CFO outflow, the employee owns the account, and the employee bears investment risk and receives the investment return.[^fsa-lpsc-p67]

Enrich `Defined Benefit Plan` and `Pension Funded Status` with: the projected benefit obligation depends on actuarial assumptions; the source uses a high-quality corporate bond yield for discounting; the employer bears the investment and actuarial risk; plan assets are held separately; and funded status appears as a net pension asset or liability.[^fsa-lpsc-p67]

Enrich `Defined Benefit Pension Expense` with the source comparison:

| Component | IFRS treatment shown | US-GAAP treatment shown |
| --- | --- | --- |
| Current service cost | Profit or loss | Profit or loss |
| Past service cost | Profit or loss | Initially OCI, with later amortization in the source framework |
| Interest / return component | Net interest on opening net pension asset or liability in profit or loss | Interest on beginning obligation less expected return on plan assets in profit or loss |
| Actuarial gains and losses | OCI without recycling | OCI, with the source showing later amortization |
| Difference between actual return and return embedded in net interest / expected return | OCI | OCI |

[^fsa-lpsc-p68]

### Share-based compensation

Enrich `Equity-Settled Share-Based Compensation` with the source's rationale and mechanics. Equity awards can align employees with shareholders and do not require a cash outflow, but may dilute existing shareholders and may encourage excessive risk-taking. Measure the award at grant-date fair value and recognize expense over the vesting or service period. Stock grants use the grant-date market price; stock options require an option-pricing model.[^fsa-lpsc-p69]

Enrich `Cash-Settled Share-Based Compensation` with stock-appreciation rights and phantom shares. Remeasure the liability to fair value at each balance-sheet date and recognize compensation expense over the service period.[^fsa-lpsc-p70]

## Navigation changes on merge

Create subtopic maps `FSA - Leases`, `FSA - Employee Compensation`, and link them from `Financial Statement Analysis`. The employee-compensation map should branch to defined-contribution plans, defined-benefit plans, funded status, pension expense, and equity- versus cash-settled compensation.

## Review checklist

- [x] Every proposed treatment is limited to what appears in the registered FSA source.
- [x] Classification criteria and comparison tables were visually checked against rendered pages.
- [x] Existing aliases and canonical filenames remain unchanged.
- [x] Trusted notes and Personal Notes remain unchanged at proposal stage.
- [x] User approves this enrichment bundle.
- [x] Merge preserves every Personal Notes block byte-for-byte.
- [x] Post-merge validation and graph inspection pass.

## Evidence

[^fsa-lpsc-p62]: [[financial-statement-analysis-level-1-speed-review.pdf#page=62|Financial Statement Analysis Level I Speed Review, PDF p. 62]]
[^fsa-lpsc-p63]: [[financial-statement-analysis-level-1-speed-review.pdf#page=63|Financial Statement Analysis Level I Speed Review, PDF p. 63]]
[^fsa-lpsc-p64]: [[financial-statement-analysis-level-1-speed-review.pdf#page=64|Financial Statement Analysis Level I Speed Review, PDF p. 64]]
[^fsa-lpsc-p65]: [[financial-statement-analysis-level-1-speed-review.pdf#page=65|Financial Statement Analysis Level I Speed Review, PDF p. 65]]
[^fsa-lpsc-p67]: [[financial-statement-analysis-level-1-speed-review.pdf#page=67|Financial Statement Analysis Level I Speed Review, PDF p. 67]]
[^fsa-lpsc-p68]: [[financial-statement-analysis-level-1-speed-review.pdf#page=68|Financial Statement Analysis Level I Speed Review, PDF p. 68]]
[^fsa-lpsc-p69]: [[financial-statement-analysis-level-1-speed-review.pdf#page=69|Financial Statement Analysis Level I Speed Review, PDF p. 69]]
[^fsa-lpsc-p70]: [[financial-statement-analysis-level-1-speed-review.pdf#page=70|Financial Statement Analysis Level I Speed Review, PDF p. 70]]
