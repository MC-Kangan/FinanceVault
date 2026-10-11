---
id: proposal-fi-l1-valuation-yields-enrichment
type: proposal
title: Fixed Income - Valuation and Yields Enrichment
target: "[[Fixed Income]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Fixed Income - Valuation and Yields Enrichment

## Rationale

Valuation nodes need the deck's complete yield conventions, spread measures, floating-rate mechanics, and term-structure formulas. The merge will create `Fixed Income - Valuation and Yields` as a subtopic map.

## Exact proposed content

Retain and refine `Bond Pricing`, `Yield to Maturity`, and `Matrix Pricing`: bond value is the present value of promised cash flows; coupon versus market discount rate determines premium, par, or discount status, and constant-yield prices pull to par. Dirty price equals clean price plus accrued interest; government bonds commonly use actual/actual and corporate bonds 30/360. Matrix pricing estimates a thinly traded bond's yield from comparable bonds and may interpolate between maturities.[^fi-val-p40][^fi-val-p41][^fi-val-p42][^fi-val-p44]

Enrich `Annualized Yield Conventions`:

$$EAR=\left(1+\frac{R_s}{n}\right)^n-1$$

where $R_s$ is the stated annual rate and $n$ is compounding periods per year. Current yield equals annual coupon divided by flat price and ignores time value, accrued interest, and capital gain or loss. Simple yield adds straight-line annual amortization of discount or premium to annual coupon before dividing by flat price.[^fi-val-p45][^fi-val-p46]

Enrich `Yield to Call` and `Yield to Worst`: YTC is the IRR assuming exercise on a call date; yield to first call uses the first call date and yield to second call the second. YTW is the lowest among the relevant YTCs and YTM.[^fi-val-p46]

Enrich `Yield Spread Measures`: YTM can be separated into a benchmark rate and a spread over the benchmark. G-spread is over the actual or interpolated government yield; I-spread is over a same-tenor swap rate. Z-spread is the constant spread over every government spot rate that prices the bond. Option-adjusted spread removes embedded-option influence: $OAS=Z\ spread-option\ value$ under the deck's sign convention, so callable bonds have $OAS<Z$ and putable bonds have $OAS>Z$.[^fi-val-p47][^fi-val-p48]

Enrich `Floating-Rate Note Valuation`: coupon rate equals market reference rate plus quoted margin, while discount rate equals market reference rate plus discount margin. Quoted margin is usually fixed; discount margin changes with required compensation. When discount margin equals quoted margin the floater prices at par; a larger discount margin implies a discount, a smaller one a premium. At reset dates the floater returns to par when the required margin still equals quoted margin.[^fi-val-p49][^fi-val-p50]

Enrich `Money Market Yield Measures`:

$$PV=FV\left(1-\frac{days}{year}\times DR\right),\qquad DR=\frac{FV-PV}{FV}\times\frac{year}{days}$$

$$FV=PV\left(1+\frac{days}{year}\times AOR\right),\qquad AOR=\frac{FV-PV}{PV}\times\frac{year}{days}$$

Discount rates are common for commercial paper, Treasury bills, and bankers' acceptances; add-on rates are common for certificates of deposit and repos.[^fi-val-p51]

Enrich `Spot Rate`, `Par Rate`, `Forward Rate`, and `Term Structure of Interest Rates`: spot rates discount individual cash flows; the par rate is the coupon rate making a bond price equal par; forward rates are future-period rates implied by current spot rates.

$$V_0=\frac{C_1}{(1+s_1)}+\frac{C_2}{(1+s_2)^2}+\cdots+\frac{C_N+Par}{(1+s_N)^N}$$

$$Par=\frac{PR_N\times Par}{(1+s_1)}+\cdots+\frac{PR_N\times Par+Par}{(1+s_N)^N}$$

$$\left(1+s_A\right)^A\left(1+IFR_{A,B-A}\right)^{B-A}=\left(1+s_B\right)^B$$

The term structure may be represented by spot, par, or forward curves; the deck contrasts normal upward-sloping curves with non-normal flat or inverted shapes.[^fi-val-p52][^fi-val-p53][^fi-val-p54]

## Navigation changes on merge

Create `Fixed Income - Valuation and Yields`, link it from `[[Fixed Income]]`, and group pricing, yield measures, spread measures, floaters, money-market conventions, and term structure.

## Review checklist

- [x] PDF pages 40-54 were visually inspected.
- [x] All displayed formulas were visually checked.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^fi-val-p40]: [[fixed-income-level-1-speed-review.pdf#page=40|Fixed Income Level I Speed Review, PDF p. 40]]
[^fi-val-p41]: [[fixed-income-level-1-speed-review.pdf#page=41|Fixed Income Level I Speed Review, PDF p. 41]]
[^fi-val-p42]: [[fixed-income-level-1-speed-review.pdf#page=42|Fixed Income Level I Speed Review, PDF p. 42]]
[^fi-val-p44]: [[fixed-income-level-1-speed-review.pdf#page=44|Fixed Income Level I Speed Review, PDF p. 44]]
[^fi-val-p45]: [[fixed-income-level-1-speed-review.pdf#page=45|Fixed Income Level I Speed Review, PDF p. 45]]
[^fi-val-p46]: [[fixed-income-level-1-speed-review.pdf#page=46|Fixed Income Level I Speed Review, PDF p. 46]]
[^fi-val-p47]: [[fixed-income-level-1-speed-review.pdf#page=47|Fixed Income Level I Speed Review, PDF p. 47]]
[^fi-val-p48]: [[fixed-income-level-1-speed-review.pdf#page=48|Fixed Income Level I Speed Review, PDF p. 48]]
[^fi-val-p49]: [[fixed-income-level-1-speed-review.pdf#page=49|Fixed Income Level I Speed Review, PDF p. 49]]
[^fi-val-p50]: [[fixed-income-level-1-speed-review.pdf#page=50|Fixed Income Level I Speed Review, PDF p. 50]]
[^fi-val-p51]: [[fixed-income-level-1-speed-review.pdf#page=51|Fixed Income Level I Speed Review, PDF p. 51]]
[^fi-val-p52]: [[fixed-income-level-1-speed-review.pdf#page=52|Fixed Income Level I Speed Review, PDF p. 52]]
[^fi-val-p53]: [[fixed-income-level-1-speed-review.pdf#page=53|Fixed Income Level I Speed Review, PDF p. 53]]
[^fi-val-p54]: [[fixed-income-level-1-speed-review.pdf#page=54|Fixed Income Level I Speed Review, PDF p. 54]]
