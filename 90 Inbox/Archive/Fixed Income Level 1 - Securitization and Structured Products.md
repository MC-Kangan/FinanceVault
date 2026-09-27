---
id: proposal-fi-l1-securitization-structured-products
type: proposal
title: Fixed Income Level 1 - Securitization and Structured Products
target: "[[Fixed Income]]"
change_type: topic-expansion
status: merged
tags:
  - cfa/level-1
---

# Fixed Income Level 1 - Securitization and Structured Products

## Rationale

Build the structured-products branch from the securitization process through credit enhancement, ABS and covered bonds, mortgage prepayment, MBS and CMO structures, and CMBS credit measures.

## Proposed canonical concepts

### `Securitization`

- Securitization transfers assets from an originator to a bankruptcy-remote special-purpose vehicle, which purchases the assets and issues securities repaid from the asset-pool cash flows.[^fi-structured-p92]
- Benefits include capital and profitability efficiency for originators, lower funding cost through disintermediation, tailored risk-return-maturity profiles for investors, and broader funding alternatives for markets.[^fi-structured-p92]

Aliases to review: `Asset Securitization`, `证券化`, `SPV`.

### `Credit Enhancement`

- External enhancement includes financial guarantees, letters of credit, and cash-collateral accounts.[^fi-structured-p93]
- Internal enhancement includes overcollateralization, excess spread, and subordination or credit tranching, which allocates losses differently among bond classes.[^fi-structured-p93]

Aliases to review: `Credit Enhancement Mechanisms`, `信用增强`.

### `Covered Bonds`

- Covered bonds are issued by a bank and collateralized by a ring-fenced cover pool that remains on the bank balance sheet, so they are not full securitizations through an independent SPV.[^fi-structured-p94]
- Investors have dual recourse to the cover pool and the issuer's unencumbered assets. Cover pools are monitored and usually overcollateralized; redemption regimes include hard bullet, soft bullet, and conditional pass-through.[^fi-structured-p95]

Aliases to review: `Covered Bond`, `担保债券`.

### `Asset-Backed Securities`

- Define ABS as securities backed by and repaid from a pool of assets, then use credit-card receivable ABS and solar ABS as examples of how collateral cash-flow structure affects the security.[^fi-structured-p92][^fi-structured-p96]
- Credit-card ABS has a revolving period during which principal receipts are reinvested, followed by repayment to investors; early-amortization triggers protect credit quality.[^fi-structured-p96]

Aliases to review: `ABS`, `Asset Backed Securities`, `资产支持证券`.

### `Collateralized Debt Obligation`

- A CDO is backed by a diversified debt pool; a collateral manager trades obligations for the portfolio. The structure commonly includes senior, mezzanine, and subordinated or equity tranches.[^fi-structured-p97]
- Senior and mezzanine tranches earn bond-like returns, while the equity tranche receives leveraged residual economics after funding costs.[^fi-structured-p97]

Aliases to review: `CDO`, `Collateralized Loan Obligation`, `CLO`, `债务抵押证券`.

### `Mortgage Prepayment Risk`

- A mortgage is secured by real property; foreclosure gives the lender a route to recover value after default. Underwriting measures include LTV and debt-to-income.[^fi-structured-p98]

$$
LTV=\frac{\text{Mortgage amount}}{\text{Property value}}
$$

$$
DTI=\frac{\text{Monthly debt payments}}{\text{Monthly pretax gross income}}
$$

[^fi-structured-p98]

- Prepayment risk is the uncertainty that actual cash flows differ from scheduled cash flows. Faster-than-expected principal creates contraction risk; slower-than-expected principal creates extension risk.[^fi-structured-p98]

Aliases to review: `Prepayment Risk`, `Contraction Risk`, `Extension Risk`, `提前还款风险`.

### `Mortgage-Backed Securities`

- Residential MBS are backed by residential mortgage pools. Agency RMBS receive federal-agency or GSE support, while non-agency RMBS rely more heavily on credit enhancement.[^fi-structured-p99]
- A mortgage pass-through gives investors proportional participation in pool cash flows. Store weighted average coupon, weighted average maturity, weighted average life, pass-through rate, and the waterfall concept as core mechanics.[^fi-structured-p99]

Aliases to review: `MBS`, `RMBS`, `Mortgage Pass-Through Security`, `住房抵押贷款支持证券`.

### `Collateralized Mortgage Obligation`

- A CMO reallocates pass-through cash flows among tranches to create different prepayment-risk exposures.[^fi-structured-p100]
- Sequential-pay tranches retire in order; PAC tranches gain cash-flow stability from support tranches within a specified prepayment band.[^fi-structured-p100]
- Z-tranches accrue rather than pay interest until a preset date; residual tranches receive remaining cash flow; PO and IO securities split principal and interest; floating-rate structures pair a floater with an inverse floater.[^fi-structured-p101]

Aliases to review: `CMO`, `PAC Tranche`, `Z-Tranche`, `PO and IO Strips`, `抵押担保证券`.

### `Commercial Mortgage-Backed Securities`

- CMBS pools contain a smaller number of income-producing commercial properties, creating concentration risk. Credit analysis uses LTV and debt-service coverage.[^fi-structured-p102]

$$
DSC=\frac{\text{Net operating income}}{\text{Debt service}}
$$

[^fi-structured-p102]

- CMBS generally has stronger call protection than RMBS and can behave more like corporate debt. Balloon-payment refinancing risk is a form of extension risk.[^fi-structured-p102]

Aliases to review: `CMBS`, `Commercial MBS`, `商业房地产贷款支持证券`.

## Link and alias changes

- Connect `Securitization` to `Asset-Backed Securities`, `Mortgage-Backed Securities`, and `Collateralized Debt Obligation`.
- Connect `Credit Enhancement` to existing `Credit Risk`, `Expected Loss`, and proposed `Debt Seniority`.
- Connect `Mortgage Prepayment Risk` to proposed `Callable Bond`, `Effective Duration`, `Effective Convexity`, and `Collateralized Mortgage Obligation`.
- Connect `Commercial Mortgage-Backed Securities` to proposed `Principal Repayment Structures` through balloon risk.
- Proposed aliases remain unregistered until collision validation passes.

## Review checklist

- [x] Claims and formulas were visually checked against pages 92-102.
- [x] Notes are proposed by reusable concept rather than by slide.
- [x] Existing trusted notes remain unchanged.
- [ ] User approves concept boundaries and aliases.
- [ ] Approved concepts are created through the merge workflow.

## Evidence

[^fi-structured-p92]: [[fixed-income-level-1-speed-review.pdf#page=92|Fixed Income Level I Speed Review, PDF p. 92]]
[^fi-structured-p93]: [[fixed-income-level-1-speed-review.pdf#page=93|Fixed Income Level I Speed Review, PDF p. 93]]
[^fi-structured-p94]: [[fixed-income-level-1-speed-review.pdf#page=94|Fixed Income Level I Speed Review, PDF p. 94]]
[^fi-structured-p95]: [[fixed-income-level-1-speed-review.pdf#page=95|Fixed Income Level I Speed Review, PDF p. 95]]
[^fi-structured-p96]: [[fixed-income-level-1-speed-review.pdf#page=96|Fixed Income Level I Speed Review, PDF p. 96]]
[^fi-structured-p97]: [[fixed-income-level-1-speed-review.pdf#page=97|Fixed Income Level I Speed Review, PDF p. 97]]
[^fi-structured-p98]: [[fixed-income-level-1-speed-review.pdf#page=98|Fixed Income Level I Speed Review, PDF p. 98]]
[^fi-structured-p99]: [[fixed-income-level-1-speed-review.pdf#page=99|Fixed Income Level I Speed Review, PDF p. 99]]
[^fi-structured-p100]: [[fixed-income-level-1-speed-review.pdf#page=100|Fixed Income Level I Speed Review, PDF p. 100]]
[^fi-structured-p101]: [[fixed-income-level-1-speed-review.pdf#page=101|Fixed Income Level I Speed Review, PDF p. 101]]
[^fi-structured-p102]: [[fixed-income-level-1-speed-review.pdf#page=102|Fixed Income Level I Speed Review, PDF p. 102]]
