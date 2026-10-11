---
id: proposal-fi-l1-bond-features-enrichment
type: proposal
title: Fixed Income - Bond Features Enrichment
target: "[[Fixed Income]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Fixed Income - Bond Features Enrichment

## Rationale

The canonical nodes exist, but many omit the comparisons, cash-flow mechanics, option-value equations, and taxation distinctions shown in the review deck. The merge will also create `Fixed Income - Bond Features` as a real subtopic map.

## Exact proposed content

Enrich `Bond Features` and `Bond Covenants`: bonds create a creditor-debtor relationship and expose investors to collateral, credit, and market risk. Core terms include maturity, par value, coupon, seniority, contingency provisions, yield measures, and yield curves. Affirmative covenants require actions such as using proceeds as specified, timely reporting, pari passu treatment, and cross-default protection; negative covenants restrict actions such as dividends, share repurchases, and issuance of more senior debt.[^fi-feat-p4][^fi-feat-p5][^fi-feat-p7]

Enrich repayment structures: a bullet bond pays principal at maturity; a fully amortizing bond reduces principal to zero through scheduled payments; a partially amortizing bond leaves a balloon payment at maturity. A sinking fund retires principal over time, reducing credit risk but increasing reinvestment risk for investors.[^fi-feat-p8]

Enrich coupon structures: fixed-rate coupons are fixed periodic payments. Floating-rate coupons equal a reference rate plus quoted margin and reset periodically. Deferred-coupon bonds pay no interest initially and then a higher coupon; zero-coupon bonds are the extreme case. Step-up, credit-linked, index-linked, inflation-linked, and payment-in-kind bonds alter payments according to the specified trigger or settlement form.[^fi-feat-p9][^fi-feat-p10]

Enrich embedded-option notes:

$$V_{callable}=V_{straight}-V_{call\ option}$$

The issuer owns the call option; therefore a callable bond normally has a lower price, higher yield, capped upside, and greater reinvestment risk than an otherwise identical straight bond. A make-whole call sets the call price from the yield to maturity of a sovereign benchmark plus a spread.[^fi-feat-p11]

$$V_{putable}=V_{straight}+V_{put\ option}$$

The investor owns the put option; therefore a putable bond normally has a higher price and lower yield than an otherwise identical straight bond and protects against rising rates.[^fi-feat-p12]

$$V_{convertible}=V_{straight}+V_{call\ option\ on\ equity}$$

$$Conversion\ price=\frac{Bond\ par\ value}{Conversion\ ratio},\qquad Conversion\ value=Stock\ price\times Conversion\ ratio$$

A convertible bond combines debt and equity features, commonly carries a lower yield and higher price, and lets the investor exchange the bond for a specified number of common shares. Contingent convertibles convert automatically after specified events; warrants give their holder the right to buy the issuer's shares at a fixed exercise price before expiry.[^fi-feat-p13][^fi-feat-p14]

Enrich market and tax classifications: domestic bonds are issued by entities incorporated in the country; foreign bonds by entities incorporated elsewhere; Eurobonds outside any single country's jurisdiction and usually in a currency other than the issuer's domestic currency; global bonds in the Eurobond market and at least one domestic market. Interest is generally ordinary income, while capital gains or losses may receive different treatment. Original-issue discount is generally amortized as taxable interest over the bond's life where the deck's OID tax rule applies.[^fi-feat-p15][^fi-feat-p16]

## Navigation changes on merge

Create `Fixed Income - Bond Features`, link it from `[[Fixed Income]]`, and place the relevant canonical concepts under repayment structure, coupon structure, embedded options, jurisdiction, and taxation.

## Review checklist

- [x] PDF pages 4-16 were visually inspected.
- [x] Option-value and conversion formulas were checked against the rendered slides.
- [x] No source recap diagram was treated as independent evidence.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^fi-feat-p4]: [[fixed-income-level-1-speed-review.pdf#page=4|Fixed Income Level I Speed Review, PDF p. 4]]
[^fi-feat-p5]: [[fixed-income-level-1-speed-review.pdf#page=5|Fixed Income Level I Speed Review, PDF p. 5]]
[^fi-feat-p7]: [[fixed-income-level-1-speed-review.pdf#page=7|Fixed Income Level I Speed Review, PDF p. 7]]
[^fi-feat-p8]: [[fixed-income-level-1-speed-review.pdf#page=8|Fixed Income Level I Speed Review, PDF p. 8]]
[^fi-feat-p9]: [[fixed-income-level-1-speed-review.pdf#page=9|Fixed Income Level I Speed Review, PDF p. 9]]
[^fi-feat-p10]: [[fixed-income-level-1-speed-review.pdf#page=10|Fixed Income Level I Speed Review, PDF p. 10]]
[^fi-feat-p11]: [[fixed-income-level-1-speed-review.pdf#page=11|Fixed Income Level I Speed Review, PDF p. 11]]
[^fi-feat-p12]: [[fixed-income-level-1-speed-review.pdf#page=12|Fixed Income Level I Speed Review, PDF p. 12]]
[^fi-feat-p13]: [[fixed-income-level-1-speed-review.pdf#page=13|Fixed Income Level I Speed Review, PDF p. 13]]
[^fi-feat-p14]: [[fixed-income-level-1-speed-review.pdf#page=14|Fixed Income Level I Speed Review, PDF p. 14]]
[^fi-feat-p15]: [[fixed-income-level-1-speed-review.pdf#page=15|Fixed Income Level I Speed Review, PDF p. 15]]
[^fi-feat-p16]: [[fixed-income-level-1-speed-review.pdf#page=16|Fixed Income Level I Speed Review, PDF p. 16]]
