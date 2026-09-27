---
id: proposal-fi-l1-valuation-yields-term-structure
type: proposal
title: Fixed Income Level 1 - Valuation, Yield Measures, and Term Structure
target: "[[Fixed Income]]"
change_type: topic-expansion
status: merged
tags:
  - cfa/level-1
---

# Fixed Income Level 1 - Valuation, Yield Measures, and Term Structure

## Rationale

Extend the existing pricing and YTM pilot with the remaining valuation tools, quoting conventions, spread measures, floating-rate valuation, and spot-par-forward rate relationships.

## Proposed updates to trusted concepts

### `Bond Pricing`

Propose adding clean-versus-dirty price mechanics without editing the trusted note before approval:

$$
\text{Accrued interest}=\frac{t}{T}\times\text{Coupon payment}
$$

$$
P_{\text{clean}}=P_{\text{full}}-\text{Accrued interest}
$$

Government bonds commonly use actual/actual day count, while corporate bonds often use 30/360.[^fi-valuation-p41]

### `Yield to Maturity`

Propose adding the assumptions required for realized return to equal YTM: full and timely payment, holding to maturity, and reinvestment of coupons at the YTM.[^fi-valuation-p42]

### `Bond Pricing` and `Convexity`

Propose cross-linking the coupon, maturity, and convexity effects: lower coupons and generally longer maturities increase price sensitivity, while the price-yield relationship is nonlinear.[^fi-valuation-p43]

## Proposed canonical concepts

### `Matrix Pricing`

- Value a bond that does not trade actively using more frequently traded comparables with similar maturity, coupon, and credit quality; use linear interpolation when relevant maturities differ.[^fi-valuation-p44]
- Matrix pricing may also estimate the yield spread over a similar-maturity government benchmark.[^fi-valuation-p44]

Aliases to review: `Matrix Pricing Method`, `矩阵定价法`.

### `Annualized Yield Conventions`

- Separate the rate per period, stated annual yield or APR, and effective annual rate.[^fi-valuation-p45]

$$
r=\frac{R_s}{n}
$$

$$
EAR=(1+r)^n-1=\left(1+\frac{R_s}{n}\right)^n-1
$$

$$
\left(1+\frac{APR_m}{m}\right)^m=\left(1+\frac{APR_n}{n}\right)^n
$$

[^fi-valuation-p45]

Aliases to review: `APR and EAR`, `Yield Periodicity`, `年化收益率`.

### `Bond Yield Measures`

- Compare current yield, simple yield, street-convention yield, true yield, yield to call, and yield to worst. Current yield focuses only on coupon income; true yield reflects the actual calendar; yield to worst is the lowest among the relevant call yields and YTM.[^fi-valuation-p46]

Aliases to review: `Yield Measures`, `Yield to Call`, `Yield to Worst`, `债券收益率指标`.

### `Yield Spread Measures`

- Decompose YTM into a benchmark rate capturing broad macro conditions and a yield spread capturing credit, liquidity, and tax effects.[^fi-valuation-p47]
- Define G-spread relative to an actual or interpolated government bond, I-spread relative to the same-tenor swap rate, Z-spread as the constant spread over the government spot curve, and OAS as the spread after removing embedded-option value.[^fi-valuation-p47][^fi-valuation-p48]

$$
P_0=\sum_{t=1}^{N}\frac{CF_t}{(1+s_t+Z)^t}
$$

[^fi-valuation-p48]

> [!warning] Source convention to review
> Page 48 presents `OAS = Z-spread - option value (%)` as a study shortcut. The approved note should explain the callable-versus-putable direction carefully rather than treating option value as a directly subtractable percentage in every valuation model.[^fi-valuation-p48]

Aliases to review: `G-Spread`, `I-Spread`, `Z-Spread`, `OAS`, `收益率利差`.

### `Floating-Rate Note Valuation`

- A floating-rate note pays the market reference rate plus a quoted margin, while valuation discounts at the market reference rate plus a discount margin. The quoted margin is contractual; the discount margin changes with required compensation.[^fi-valuation-p49]

$$
\text{Coupon rate}=MRR+QM
$$

$$
\text{Discount rate}=MRR+DM
$$

[^fi-valuation-p49]

- At issuance, most FRNs are priced at par with `QM = DM`. If `DM > QM`, price is below par; if `DM < QM`, price is above par. When the margins match, price returns to par on reset dates, with between-date movements driven by the reference rate.[^fi-valuation-p50]

Aliases to review: `FRN Valuation`, `Floater Valuation`, `浮息债估值`.

### `Money Market Yield Measures`

- Discount rates quote return relative to face value and are commonly used for Treasury bills, commercial paper, and bankers' acceptances; add-on rates quote return relative to invested value and are common for certificates of deposit and repos.[^fi-valuation-p51]

$$
PV=FV\left(1-\frac{\text{days}}{\text{year}}DR\right)
$$

$$
DR=\frac{FV-PV}{FV}\times\frac{\text{year}}{\text{days}}
$$

$$
FV=PV\left(1+\frac{\text{days}}{\text{year}}AOR\right)
$$

$$
AOR=\frac{FV-PV}{PV}\times\frac{\text{year}}{\text{days}}
$$

[^fi-valuation-p51]

Aliases to review: `Discount Rate and Add-On Rate`, `Money Market Rates`, `货币市场收益率`.

### `Spot Rate`

- Define a spot or zero rate as the yield on a zero-coupon bond maturing at the date of the relevant cash flow, and use a different spot rate to discount each cash flow.[^fi-valuation-p52]

$$
V_0=\sum_{t=1}^{N}\frac{CF_t}{(1+s_t)^t}
$$

[^fi-valuation-p52]

Aliases to review: `Zero Rate`, `Zero-Coupon Rate`, `即期利率`.

### `Par Rate`

- Define the par rate for a maturity as the coupon rate that makes a bond's price equal par when its cash flows are discounted with the spot curve.[^fi-valuation-p52]

Aliases to review: `Par Yield`, `平价利率`.

### `Forward Rate`

- Define a forward rate and read `myny` as an n-year rate beginning m years from today. The implied forward rate is the reinvestment rate that makes two spot-rate investment paths break even.[^fi-valuation-p53]

$$
(1+s_A)^A\left(1+IFR_{A,B-A}\right)^{B-A}=(1+s_B)^B
$$

[^fi-valuation-p53]

Aliases to review: `Implied Forward Rate`, `远期利率`.

### `Term Structure of Interest Rates`

- Distinguish the spot, par, and forward curves. Under normal conditions the forward curve typically lies above the spot curve and the par curve below it; flat and inverted shapes can alter or eliminate that ordering.[^fi-valuation-p54]

![[source-fi-l1-speed-review-p054-yield-curves.png]]

Figure: The relative positions of spot, par, and forward curves depend on the shape of the term structure; the chart contrasts normal, flat, and inverted examples.[^fi-valuation-p54]

Aliases to review: `Yield Curve`, `Interest Rate Term Structure`, `利率期限结构`.

## Link and alias changes

- Link `Spot Rate`, `Par Rate`, and `Forward Rate` bidirectionally through `Term Structure of Interest Rates`.
- Connect `Yield Spread Measures` to existing `Credit Risk` and `Corporate Credit Analysis`.
- Connect `Floating-Rate Note Valuation` to proposed `Coupon Structures` and existing `Bond Pricing`.
- No trusted notes or aliases change until approval.

## Review checklist

- [x] Formulas were visually checked against pages 40-54.
- [x] Source-convention warning is explicit.
- [x] Proposed yield-curve figure is legible and page-addressable.
- [x] Trusted pilot notes remain unchanged.
- [ ] User approves concept boundaries and updates.

## Evidence

[^fi-valuation-p41]: [[fixed-income-level-1-speed-review.pdf#page=41|Fixed Income Level I Speed Review, PDF p. 41]]
[^fi-valuation-p42]: [[fixed-income-level-1-speed-review.pdf#page=42|Fixed Income Level I Speed Review, PDF p. 42]]
[^fi-valuation-p43]: [[fixed-income-level-1-speed-review.pdf#page=43|Fixed Income Level I Speed Review, PDF p. 43]]
[^fi-valuation-p44]: [[fixed-income-level-1-speed-review.pdf#page=44|Fixed Income Level I Speed Review, PDF p. 44]]
[^fi-valuation-p45]: [[fixed-income-level-1-speed-review.pdf#page=45|Fixed Income Level I Speed Review, PDF p. 45]]
[^fi-valuation-p46]: [[fixed-income-level-1-speed-review.pdf#page=46|Fixed Income Level I Speed Review, PDF p. 46]]
[^fi-valuation-p47]: [[fixed-income-level-1-speed-review.pdf#page=47|Fixed Income Level I Speed Review, PDF p. 47]]
[^fi-valuation-p48]: [[fixed-income-level-1-speed-review.pdf#page=48|Fixed Income Level I Speed Review, PDF p. 48]]
[^fi-valuation-p49]: [[fixed-income-level-1-speed-review.pdf#page=49|Fixed Income Level I Speed Review, PDF p. 49]]
[^fi-valuation-p50]: [[fixed-income-level-1-speed-review.pdf#page=50|Fixed Income Level I Speed Review, PDF p. 50]]
[^fi-valuation-p51]: [[fixed-income-level-1-speed-review.pdf#page=51|Fixed Income Level I Speed Review, PDF p. 51]]
[^fi-valuation-p52]: [[fixed-income-level-1-speed-review.pdf#page=52|Fixed Income Level I Speed Review, PDF p. 52]]
[^fi-valuation-p53]: [[fixed-income-level-1-speed-review.pdf#page=53|Fixed Income Level I Speed Review, PDF p. 53]]
[^fi-valuation-p54]: [[fixed-income-level-1-speed-review.pdf#page=54|Fixed Income Level I Speed Review, PDF p. 54]]
