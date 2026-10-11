---
id: proposal-fi-l1-securitization-enrichment
type: proposal
title: Fixed Income - Securitization Enrichment
target: "[[Fixed Income]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Fixed Income - Securitization Enrichment

## Rationale

Structured-product nodes need the deck's transaction mechanics, credit enhancement, mortgage ratios, prepayment behavior, and tranche distinctions. The merge will create `Fixed Income - Securitization` as a subtopic map.

## Exact proposed content

Enrich `Securitization` and `Asset-Backed Securities`: securitization transfers assets from the owner to a bankruptcy-remote special-purpose vehicle, which issues securities backed by asset cash flows. Benefits include capital efficiency for originators, disintermediation and lower funding cost for borrowers, tailored risk/return/maturity exposure for investors, and alternative funding for markets.[^fi-sec-p92]

Enrich `Credit Enhancement`: external enhancement includes financial guarantees, letters of credit, and cash collateral accounts. Internal enhancement includes overcollateralization, excess spread, and subordination/credit tranching.[^fi-sec-p93]

Enrich `Covered Bond`: the issuer identifies a ring-fenced cover pool but retains it on balance sheet; investors have dual recourse to the pool and issuer. The pool is dynamically monitored, typically overcollateralized, and often subject to loan-to-value standards. Distinguish hard-bullet, soft-bullet, and conditional pass-through repayment regimes.[^fi-sec-p94][^fi-sec-p95]

Enrich credit-card and solar ABS: credit-card receivables are non-amortizing, with periodic interest/fees and principal paid during a lockout or revolving period before amortization; early-amortization provisions protect credit quality. Solar ABS may be backed by solar loans or leases and may include a prefunding period.[^fi-sec-p96]

Enrich `Collateralized Debt Obligation`: a CDO is backed by a diversified debt pool, managed to buy and sell obligations, and commonly has senior, mezzanine, and subordinated/equity classes. Senior and mezzanine tranches earn bond-like returns, while the equity tranche earns residual/equity-like returns; an arbitrage CDO seeks a return above funding cost.[^fi-sec-p97]

Enrich mortgage concepts:

$$LTV=\frac{Mortgage\ amount}{Property\ value},\qquad Debt\text{-}to\text{-}income=\frac{Monthly\ debt\ payments}{Monthly\ pre\text{-}tax\ income}$$

Mortgage types include prime/subprime, recourse/non-recourse, and conforming/non-conforming. A prepayment option creates contraction risk when borrowers repay faster than scheduled and extension risk when they repay more slowly.[^fi-sec-p98]

Enrich `Mortgage-Backed Securities`: residential MBS may be agency or non-agency; the latter often needs credit enhancement. Mortgage pass-through holders receive proportional pool cash flows; retain weighted average coupon, weighted average maturity, weighted average life, and pass-through rate as core measures.[^fi-sec-p99]

Enrich `Collateralized Mortgage Obligation`, `Sequential-Pay Tranche`, `Planned Amortization Class Tranche`, `Support Tranche`, `Z-Tranche`, `Principal-Only Strip`, `Interest-Only Strip`, and `Inverse Floater`: sequential tranches retire in order; PAC tranches target a scheduled principal band and shift more prepayment risk to support tranches. Z-tranches accrue rather than pay current interest until earlier tranches retire; residual tranches receive remaining cash. PO and IO strips separate principal and interest cash flows, while floating-rate tranches can be paired with inverse floaters.[^fi-sec-p100][^fi-sec-p101]

Enrich `Commercial Mortgage-Backed Securities`: commercial mortgages carry concentration risk, are typically non-recourse and collateralized by income-producing property. Credit measures include:

$$LTV=\frac{Loan}{Current\ value},\qquad DSC=\frac{NOI}{Debt\ service}$$

Commercial mortgages may have balloon payments, creating balloon/extension risk if refinancing or sale cannot cover the payment.[^fi-sec-p102]

## Navigation changes on merge

Create `Fixed Income - Securitization`, link it from `[[Fixed Income]]`, and group securitization mechanics, enhancement, covered bonds, non-mortgage ABS/CDOs, residential MBS/CMOs, and CMBS.

## Review checklist

- [x] PDF pages 92-102 were visually inspected.
- [x] Mortgage-ratio formulas and tranche descriptions were visually checked.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^fi-sec-p92]: [[fixed-income-level-1-speed-review.pdf#page=92|Fixed Income Level I Speed Review, PDF p. 92]]
[^fi-sec-p93]: [[fixed-income-level-1-speed-review.pdf#page=93|Fixed Income Level I Speed Review, PDF p. 93]]
[^fi-sec-p94]: [[fixed-income-level-1-speed-review.pdf#page=94|Fixed Income Level I Speed Review, PDF p. 94]]
[^fi-sec-p95]: [[fixed-income-level-1-speed-review.pdf#page=95|Fixed Income Level I Speed Review, PDF p. 95]]
[^fi-sec-p96]: [[fixed-income-level-1-speed-review.pdf#page=96|Fixed Income Level I Speed Review, PDF p. 96]]
[^fi-sec-p97]: [[fixed-income-level-1-speed-review.pdf#page=97|Fixed Income Level I Speed Review, PDF p. 97]]
[^fi-sec-p98]: [[fixed-income-level-1-speed-review.pdf#page=98|Fixed Income Level I Speed Review, PDF p. 98]]
[^fi-sec-p99]: [[fixed-income-level-1-speed-review.pdf#page=99|Fixed Income Level I Speed Review, PDF p. 99]]
[^fi-sec-p100]: [[fixed-income-level-1-speed-review.pdf#page=100|Fixed Income Level I Speed Review, PDF p. 100]]
[^fi-sec-p101]: [[fixed-income-level-1-speed-review.pdf#page=101|Fixed Income Level I Speed Review, PDF p. 101]]
[^fi-sec-p102]: [[fixed-income-level-1-speed-review.pdf#page=102|Fixed Income Level I Speed Review, PDF p. 102]]
