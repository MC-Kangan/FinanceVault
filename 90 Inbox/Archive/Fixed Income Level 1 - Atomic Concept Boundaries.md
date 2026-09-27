---
id: proposal-fi-l1-atomic-concept-boundaries
type: proposal
title: Fixed Income Level 1 - Atomic Concept Boundaries
target: "[[Fixed Income]]"
change_type: schema-granularity-revision
status: merged
tags:
  - cfa/level-1
---

# Fixed Income Level 1 - Atomic Concept Boundaries

## Rationale

The first full-deck pass grouped several slide-level concepts into broad notes. This revision supersedes those boundaries where a named concept recurs, has its own formula or exam behavior, or is a useful navigation target. The detailed claims and formulas remain in the thematic proposals; this proposal defines the canonical note split to use at merge.

## Required atomic splits

### Bond cash-flow structures

Create separate canonical nodes for `Bullet Bond`, `Fully Amortizing Bond`, `Partially Amortizing Bond`, `Balloon Payment`, and `Sinking Fund`. The repayment patterns and risks differ and later connect independently to prepayment, refinancing, and credit analysis.[^fi-granularity-p8]

Create separate nodes for `Fixed-Rate Bond`, `Floating-Rate Note`, `Deferred-Coupon Bond`, `Zero-Coupon Bond`, `Step-Up Coupon Bond`, `Credit-Linked Coupon Bond`, `Index-Linked Bond`, `Inflation-Linked Bond`, and `Payment-in-Kind Bond`. Keep `Coupon Structures` only as a map section, not as the single canonical destination.[^fi-granularity-p9][^fi-granularity-p10]

### Embedded options and equity-linked bonds

Create `Callable Bond`, `Putable Bond`, and `Make-Whole Call` as separate nodes. They must link to `Bond Pricing`, `Yield to Call`, `Effective Duration`, and `Effective Convexity`; callable and putable behavior must not be hidden inside `Embedded Bond Options`.[^fi-granularity-p11][^fi-granularity-p12][^fi-granularity-p71]

Create separate nodes for `Convertible Bond`, `Contingent Convertible Bond`, and `Warrant`. Conversion ratio, conversion price, and conversion value stay in `Convertible Bond`; automatic trigger behavior belongs to `Contingent Convertible Bond`.[^fi-granularity-p13][^fi-granularity-p14]

### Yield and spread measures

Create separate nodes for `Current Yield`, `Yield to Call`, `Yield to Worst`, `G-Spread`, `I-Spread`, `Z-Spread`, and `Option-Adjusted Spread`. Less reusable quotation variants may remain sections of a `Bond Yield Conventions` note, but every named measure that is used in valuation or credit links must be directly addressable.[^fi-granularity-p46][^fi-granularity-p47][^fi-granularity-p48]

### Interest-rate risk

Create separate nodes for `Reinvestment Risk`, `Market Price Risk`, `Money Duration`, `Price Value of a Basis Point`, `Portfolio Duration`, `Portfolio Convexity`, `Effective Duration`, `Effective Convexity`, `Key Rate Duration`, `Analytical Duration`, and `Empirical Duration`.[^fi-granularity-p60][^fi-granularity-p64][^fi-granularity-p68][^fi-granularity-p69][^fi-granularity-p70][^fi-granularity-p72][^fi-granularity-p73]

`PVBP`, `PV01`, `DV01`, and `BPV` are aliases of `Price Value of a Basis Point`, not separate nodes. `Effective Duration` and `Effective Convexity` are distinct canonical notes because their formulas, dimensions, and first- versus second-order roles differ.[^fi-granularity-p64][^fi-granularity-p69][^fi-granularity-p70]

### Credit and structured products

Create separate nodes for `Probability of Default`, `Loss Given Default`, `Exposure at Default`, and `Recovery Rate`, linked through existing `Expected Loss`.[^fi-granularity-p80]

Create separate nodes for `Contraction Risk` and `Extension Risk`; both link to `Mortgage Prepayment Risk`, while `Balloon Payment` also links to extension and refinancing risk.[^fi-granularity-p98][^fi-granularity-p102]

Create separate nodes for `Sequential-Pay Tranche`, `Planned Amortization Class Tranche`, `Support Tranche`, `Z-Tranche`, `Principal-Only Strip`, `Interest-Only Strip`, `Floater`, and `Inverse Floater`. `Collateralized Mortgage Obligation` remains the parent concept and map destination.[^fi-granularity-p100][^fi-granularity-p101]

## Repeat-driven links

- `Callable Bond` appears in contractual features and again in effective duration/convexity. The canonical note must contain both contexts and cite both page groups.[^fi-granularity-p11][^fi-granularity-p71]
- `Putable Bond` follows the same cross-context pattern.[^fi-granularity-p12][^fi-granularity-p71]
- `Floating-Rate Note` appears in coupon design and valuation; the note must connect the reset mechanism to quoted margin and discount margin.[^fi-granularity-p9][^fi-granularity-p49][^fi-granularity-p50]
- `Balloon Payment` appears in principal structure and CMBS refinancing risk.[^fi-granularity-p8][^fi-granularity-p102]
- `Credit Enhancement` appears in securitization, non-agency RMBS, and tranche subordination; its connections should expose each use rather than repeat definitions.[^fi-granularity-p93][^fi-granularity-p99]

## Review checklist

- [x] Existing trusted concepts remain unchanged.
- [x] Boundaries were tested against the page-separated transcript and rendered pages.
- [x] Alias-only variants are distinguished from true concepts.
- [ ] User approves this atomic split.
- [ ] Thematic proposals are merged using these boundaries.

## Evidence

[^fi-granularity-p8]: [[fixed-income-level-1-speed-review.pdf#page=8|Fixed Income Level I Speed Review, PDF p. 8]]
[^fi-granularity-p9]: [[fixed-income-level-1-speed-review.pdf#page=9|Fixed Income Level I Speed Review, PDF p. 9]]
[^fi-granularity-p10]: [[fixed-income-level-1-speed-review.pdf#page=10|Fixed Income Level I Speed Review, PDF p. 10]]
[^fi-granularity-p11]: [[fixed-income-level-1-speed-review.pdf#page=11|Fixed Income Level I Speed Review, PDF p. 11]]
[^fi-granularity-p12]: [[fixed-income-level-1-speed-review.pdf#page=12|Fixed Income Level I Speed Review, PDF p. 12]]
[^fi-granularity-p13]: [[fixed-income-level-1-speed-review.pdf#page=13|Fixed Income Level I Speed Review, PDF p. 13]]
[^fi-granularity-p14]: [[fixed-income-level-1-speed-review.pdf#page=14|Fixed Income Level I Speed Review, PDF p. 14]]
[^fi-granularity-p46]: [[fixed-income-level-1-speed-review.pdf#page=46|Fixed Income Level I Speed Review, PDF p. 46]]
[^fi-granularity-p47]: [[fixed-income-level-1-speed-review.pdf#page=47|Fixed Income Level I Speed Review, PDF p. 47]]
[^fi-granularity-p48]: [[fixed-income-level-1-speed-review.pdf#page=48|Fixed Income Level I Speed Review, PDF p. 48]]
[^fi-granularity-p49]: [[fixed-income-level-1-speed-review.pdf#page=49|Fixed Income Level I Speed Review, PDF p. 49]]
[^fi-granularity-p50]: [[fixed-income-level-1-speed-review.pdf#page=50|Fixed Income Level I Speed Review, PDF p. 50]]
[^fi-granularity-p60]: [[fixed-income-level-1-speed-review.pdf#page=60|Fixed Income Level I Speed Review, PDF p. 60]]
[^fi-granularity-p64]: [[fixed-income-level-1-speed-review.pdf#page=64|Fixed Income Level I Speed Review, PDF p. 64]]
[^fi-granularity-p68]: [[fixed-income-level-1-speed-review.pdf#page=68|Fixed Income Level I Speed Review, PDF p. 68]]
[^fi-granularity-p69]: [[fixed-income-level-1-speed-review.pdf#page=69|Fixed Income Level I Speed Review, PDF p. 69]]
[^fi-granularity-p70]: [[fixed-income-level-1-speed-review.pdf#page=70|Fixed Income Level I Speed Review, PDF p. 70]]
[^fi-granularity-p71]: [[fixed-income-level-1-speed-review.pdf#page=71|Fixed Income Level I Speed Review, PDF p. 71]]
[^fi-granularity-p72]: [[fixed-income-level-1-speed-review.pdf#page=72|Fixed Income Level I Speed Review, PDF p. 72]]
[^fi-granularity-p73]: [[fixed-income-level-1-speed-review.pdf#page=73|Fixed Income Level I Speed Review, PDF p. 73]]
[^fi-granularity-p80]: [[fixed-income-level-1-speed-review.pdf#page=80|Fixed Income Level I Speed Review, PDF p. 80]]
[^fi-granularity-p93]: [[fixed-income-level-1-speed-review.pdf#page=93|Fixed Income Level I Speed Review, PDF p. 93]]
[^fi-granularity-p98]: [[fixed-income-level-1-speed-review.pdf#page=98|Fixed Income Level I Speed Review, PDF p. 98]]
[^fi-granularity-p99]: [[fixed-income-level-1-speed-review.pdf#page=99|Fixed Income Level I Speed Review, PDF p. 99]]
[^fi-granularity-p100]: [[fixed-income-level-1-speed-review.pdf#page=100|Fixed Income Level I Speed Review, PDF p. 100]]
[^fi-granularity-p101]: [[fixed-income-level-1-speed-review.pdf#page=101|Fixed Income Level I Speed Review, PDF p. 101]]
[^fi-granularity-p102]: [[fixed-income-level-1-speed-review.pdf#page=102|Fixed Income Level I Speed Review, PDF p. 102]]
