---
id: proposal-derivatives-l1-atomic-concept-boundaries
type: proposal
title: Derivatives Level 1 - Atomic Concept Boundaries
target: Derivatives
change_type: concept-bundle
status: merged
tags:
  - cfa/level-1
---

# Derivatives Level 1 - Atomic Concept Boundaries

## Rationale

The deck is already a condensed review source. Named contracts, market mechanisms, pricing rules, payoff measures, and replication techniques therefore become canonical notes when they have distinct exam behavior, a formula, or a useful cross-topic destination. Related labels remain sections or aliases when separating them would create thin duplicate nodes.

## Proposed concepts by chapter

### Instruments and Markets

Create or enrich: `Derivative`, `Hedging`, `Speculation`, `Arbitrage`, `Hedge Accounting`, `Cash Flow Hedge`, `Fair Value Hedge`, `Net Investment Hedge`, `Basis Risk`, `Forward Commitment`, `Contingent Claim`, `Exchange-Traded Derivative`, `Over-the-Counter Derivative`, `Central Counterparty`, `Forward Contract`, `Non-Deliverable Forward`, `Futures Contract`, `Price Limit`, `Settlement Price`, `Circuit Breaker`, `Mark-to-Market`, `Initial Margin`, `Maintenance Margin`, `Margin Call`, `Variation Margin`, `Forward-Futures Price Difference`, `Swap Contract`, `Off-Market Forward`, `Interest Rate Swap`, `Fixed-Rate Payer`, `Floating-Rate Payer`, `Option`, `Option Premium`, `Strike Price`, `European Option`, `American Option`, `Call Option`, `Put Option`, `Moneyness`, and `Credit Default Swap`.[^der-boundaries-p4][^der-boundaries-p15]

Long and short option positions, in-the-money/at-the-money/out-of-the-money classifications, and payoff-versus-profit distinctions belong as clearly separated sections inside the contract and moneyness notes rather than creating many thin files.

### Forward Commitments Pricing and Valuation

Create or enrich: `Law of One Price`, `No-Arbitrage Pricing`, `Replication`, `Risk-Neutral Pricing`, `Derivative Price`, `Derivative Value`, `Forward Pricing`, `Forward Valuation`, [[Cost of Carry]], [[Convenience Yield]], `Foreign Exchange Forward`, `Forward Rate Agreement`, `FRA Settlement`, `Interest Rate Futures`, `Basis Point Value`, `Convexity Bias`, `Swap Rate`, and `Interest Rate Swap Valuation`.[^der-boundaries-p18][^der-boundaries-p26]

Forward price and forward value remain separate nodes because the deck explicitly distinguishes the fixed delivery price from the changing mark-to-market value. `FRA` and `CDS` become aliases only; they never become filenames.

### Option Value and Binomial Pricing

Create or enrich: `Option Intrinsic Value`, `Option Time Value`, `Option Value Bounds`, `Option Value Drivers`, `Put-Call Parity`, `Put-Call Forward Parity`, `Fiduciary Call`, `Protective Put`, `Synthetic Position`, `Equity as a Call Option`, `Debt as Risk-Free Debt Minus a Put`, `One-Period Binomial Model`, `Risk-Neutral Probability`, `Hedged Portfolio`, and `Hedge Ratio`.[^der-boundaries-p29][^der-boundaries-p36]

The corporate-securities option analogy should connect Derivatives to [[Equity Investments]], [[Fixed Income]], and [[Credit Risk]]. The worked binomial examples remain inside their parent concept notes rather than becoming standalone example nodes.

## Alias and cross-topic policy

- `ETD`, `OTC`, `CCP`, `NDF`, `FRA`, `MRR`, `BPV`, `CDS`, and relevant Chinese translations become aliases only after normalized collision validation.
- `Exercise Price` resolves to `Strike Price`; `Exercise Value` resolves to `Option Intrinsic Value`.
- `Swap` should resolve to `Swap Contract`, while `Interest Rate Swap` remains a more specific canonical child concept.
- Existing [[Cost of Carry]] and [[Convenience Yield]] notes receive Derivatives context and source citations rather than duplicates.
- Cross-topic links should connect CDS to [[Credit Risk]], interest-rate futures and swaps to [[Fixed Income]], hedge accounting to [[Financial Statement Analysis]], and option-based firm-value claims to both equity and credit analysis.

## Proposed visual assets

No crop is created at proposal stage. High-value replacement-ready candidates are the option payoff/profit grid on PDF page 14, the FRA settlement timeline on page 23, the put-call parity replication structure on page 31, and the one-period binomial/hedge-ratio examples on pages 33-36. Use `derivatives-l1-speed-review-pNNN-description.png`, retain searchable explanatory text, and cite the exact supporting PDF page.

## Review checklist

- [x] Candidate boundaries follow the review deck's granularity.
- [x] Existing concepts are designated for enrichment, not duplication.
- [x] Alias candidates are recorded but not committed to trusted notes.
- [x] Trusted concepts and Personal Notes remain unchanged.
- [x] User approved the atomic boundaries.
- [x] Full normalized-alias collision check passes during merge.
- [x] Every promoted formula is visually verified during merge.
- [x] Vault validation passes after merge.

## Evidence

[^der-boundaries-p4]: [[derivatives-level-1-speed-review.pdf#page=4|Derivatives Level I Speed Review, PDF p. 4]]
[^der-boundaries-p15]: [[derivatives-level-1-speed-review.pdf#page=15|Derivatives Level I Speed Review, PDF p. 15]]
[^der-boundaries-p18]: [[derivatives-level-1-speed-review.pdf#page=18|Derivatives Level I Speed Review, PDF p. 18]]
[^der-boundaries-p26]: [[derivatives-level-1-speed-review.pdf#page=26|Derivatives Level I Speed Review, PDF p. 26]]
[^der-boundaries-p29]: [[derivatives-level-1-speed-review.pdf#page=29|Derivatives Level I Speed Review, PDF p. 29]]
[^der-boundaries-p36]: [[derivatives-level-1-speed-review.pdf#page=36|Derivatives Level I Speed Review, PDF p. 36]]
