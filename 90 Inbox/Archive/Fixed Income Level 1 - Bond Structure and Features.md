---
id: proposal-fi-l1-bond-structure-features
type: proposal
title: Fixed Income Level 1 - Bond Structure and Features
target: "[[Fixed Income]]"
change_type: topic-expansion
status: merged
tags:
  - cfa/level-1
---

# Fixed Income Level 1 - Bond Structure and Features

## Rationale

Create focused canonical notes for the contractual building blocks of a bond. The proposed boundaries keep reusable ideas such as covenants, repayment structures, and embedded options separate while avoiding one note for every slide term.

## Proposed canonical concepts

### `Bond Features`

- Define bonds as debt securities establishing a creditor-debtor relationship, distinguish public and private issuers, and capture maturity, par value, coupon, seniority, and current yield as core descriptors.[^fi-features-p4][^fi-features-p5]
- Explain that repayment support depends on issuer type: sovereign tax and monetary capacity, local-government taxing or project cash flows, corporate operating cash flow, collateral for secured debt, and asset-pool cash flow for ABS.[^fi-features-p6]

Formula to store as searchable MathJax:

$$
\text{Current yield}=\frac{\text{Annual coupon payment}}{\text{Bond price}}
$$

[^fi-features-p5]

Aliases to review: `Bond Characteristics`, `债券特征`.

### `Bond Covenants`

- Separate affirmative covenants, such as permitted use of proceeds, timely reporting, pari passu treatment, and cross-default provisions, from negative covenants that restrict issuer actions; include negative pledge as a key example.[^fi-features-p7]

Aliases to review: `Covenants`, `债券契约`.

### `Principal Repayment Structures`

- Compare bullet, fully amortizing, and partially amortizing structures; flag balloon-payment risk for partially amortized debt.[^fi-features-p8]
- Explain that a sinking fund reduces credit risk through scheduled retirement but can create reinvestment risk when bonds are retired early.[^fi-features-p8]

![[source-fi-l1-speed-review-p008-principal-repayment-structures.png]]

Figure: Cash-flow patterns distinguish bullet and amortizing principal structures; the image remains a proposed asset until the note is approved.[^fi-features-p8]

Aliases to review: `Amortization Structures`, `Principal Structures`, `本金偿还结构`.

### `Coupon Structures`

- Cover fixed-rate, deferred-coupon, zero-coupon, floating-rate, step-up, credit-linked, index-linked, inflation-linked, and payment-in-kind structures.[^fi-features-p9][^fi-features-p10]
- For a floating-rate note, store the coupon identity and explain that the reference rate resets while the quoted margin is usually fixed and coupon payment is typically in arrears.[^fi-features-p9]

$$
\text{Coupon rate}=\text{Reference rate}+\text{Quoted margin}
$$

[^fi-features-p9]

Aliases to review: `Coupon Types`, `票息结构`, `PIK Coupon`.

### `Callable Bond`

A callable bond gives the issuer the right to redeem early, caps investor price appreciation, increases reinvestment risk, and generally requires a higher yield than an otherwise equivalent straight bond.[^fi-features-p11]

$$
V_{\text{callable}}=V_{\text{straight}}-V_{\text{call option}}
$$

[^fi-features-p11]

Aliases to review: `Callable Note`, `Redeemable Bond`, `可赎回债券`.

### `Putable Bond`

A putable bond gives the investor the right to sell early, creates a price floor, and generally accepts a lower yield than an otherwise equivalent straight bond.[^fi-features-p12]

$$
V_{\text{putable}}=V_{\text{straight}}+V_{\text{put option}}
$$

[^fi-features-p12]

Aliases to review: `Put Bond`, `Puttable Bond`, `可回售债券`.

### `Make-Whole Call`

A make-whole call is a call structure designed to compensate investors using the present value of foregone cash flows. It links to but is not an alias of `Callable Bond`.[^fi-features-p11]

Aliases to review: `Make Whole Call`, `Make-Whole Provision`, `补偿性赎回`.

### `Convertible Bonds`

- Define a convertible bond as a debt-equity hybrid that gives the investor the right to exchange the bond for issuer shares. The conversion option raises value and generally permits a lower coupon or yield than straight debt.[^fi-features-p13]

$$
V_{\text{convertible}}=V_{\text{straight}}+V_{\text{call option on equity}}
$$

$$
\text{Conversion price}=\frac{\text{Par value}}{\text{Conversion ratio}}
$$

$$
\text{Conversion value}=\text{Share price}\times\text{Conversion ratio}
$$

[^fi-features-p13]

- Connect contingent convertibles, which convert when a trigger is reached, and warrants, which are detachable options rather than embedded conversion rights.[^fi-features-p14]

Aliases to review: `Convertible Bond`, `Convertibles`, `可转换债券`, `CoCo`.

### `International Bond Markets`

- Distinguish domestic bonds, foreign bonds, Eurobonds, and global bonds by market of issuance and currency; retain bearer-versus-registered form as a historical market distinction.[^fi-features-p15]

Aliases to review: `International Bonds`, `Eurobond Market`, `国际债券市场`.

### `Bond Taxation`

- Separate periodic interest income from capital gains and explain original issue discount as the difference between par and the original issue price, with tax treatment depending on whether OID accrual rules apply.[^fi-features-p16]

Aliases to review: `Original Issue Discount`, `OID`, `债券税务`.

## Link and alias changes

- `Callable Bond`, `Putable Bond`, and `Make-Whole Call` should connect to existing `Bond Pricing`, `Yield to Maturity`, and `Convexity` after approval.
- `Coupon Structures` should connect to proposed `Floating-Rate Note Valuation` and existing `Macaulay Duration`.
- `Principal Repayment Structures` should connect to proposed `Mortgage Prepayment Risk` and `Commercial Mortgage-Backed Securities`.
- No alias is promoted until collision validation passes.

## Review checklist

- [x] Claims and formulas were visually checked against pages 4-16.
- [x] Proposed figure is legible and has page provenance.
- [x] Existing canonical concepts were not edited.
- [ ] User approves concept boundaries and aliases.
- [ ] Approved concepts are created through the merge workflow.

## Evidence

[^fi-features-p4]: [[fixed-income-level-1-speed-review.pdf#page=4|Fixed Income Level I Speed Review, PDF p. 4]]
[^fi-features-p5]: [[fixed-income-level-1-speed-review.pdf#page=5|Fixed Income Level I Speed Review, PDF p. 5]]
[^fi-features-p6]: [[fixed-income-level-1-speed-review.pdf#page=6|Fixed Income Level I Speed Review, PDF p. 6]]
[^fi-features-p7]: [[fixed-income-level-1-speed-review.pdf#page=7|Fixed Income Level I Speed Review, PDF p. 7]]
[^fi-features-p8]: [[fixed-income-level-1-speed-review.pdf#page=8|Fixed Income Level I Speed Review, PDF p. 8]]
[^fi-features-p9]: [[fixed-income-level-1-speed-review.pdf#page=9|Fixed Income Level I Speed Review, PDF p. 9]]
[^fi-features-p10]: [[fixed-income-level-1-speed-review.pdf#page=10|Fixed Income Level I Speed Review, PDF p. 10]]
[^fi-features-p11]: [[fixed-income-level-1-speed-review.pdf#page=11|Fixed Income Level I Speed Review, PDF p. 11]]
[^fi-features-p12]: [[fixed-income-level-1-speed-review.pdf#page=12|Fixed Income Level I Speed Review, PDF p. 12]]
[^fi-features-p13]: [[fixed-income-level-1-speed-review.pdf#page=13|Fixed Income Level I Speed Review, PDF p. 13]]
[^fi-features-p14]: [[fixed-income-level-1-speed-review.pdf#page=14|Fixed Income Level I Speed Review, PDF p. 14]]
[^fi-features-p15]: [[fixed-income-level-1-speed-review.pdf#page=15|Fixed Income Level I Speed Review, PDF p. 15]]
[^fi-features-p16]: [[fixed-income-level-1-speed-review.pdf#page=16|Fixed Income Level I Speed Review, PDF p. 16]]
