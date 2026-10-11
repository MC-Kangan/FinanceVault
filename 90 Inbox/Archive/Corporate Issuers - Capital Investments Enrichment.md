---
id: proposal-corporate-issuers-l1-capital-investments-enrichment
type: proposal
title: Corporate Issuers - Capital Investments Enrichment
target: "[[Corporate Issuers - Capital Investments]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Corporate Issuers - Capital Investments Enrichment

## Rationale

The source gives a compact capital-budgeting framework with classifications, cash-flow rules, complete NPV/IRR mechanics, project-ranking conflicts, real options, and behavioral errors. Most of that detail is absent from the trusted notes.

## Exact proposed content

### Project classification and cash-flow principles

Enrich `Maintenance Project`, `Compliance Project`, and `Expansion Project`. Business-maintenance projects include going-concern investments that continue operations, improve efficiency, or manage risk, plus regulatory/compliance projects. Business-growth projects include expansion within the existing business, normally low-to-moderate risk, and new lines of business outside the current business, normally higher risk. R&D and acquisitions may occur in either category depending on whether they remain within the core business.[^ci-cap-p24]

Enrich `After-Tax Incremental Cash Flow`, `Externality`, `Opportunity Cost`, and `Sunk Cost`. Capital budgeting uses the timing of after-tax incremental cash flows, includes positive or negative externalities and opportunity costs, and excludes costs already incurred. A common pitfall is including financing flows inside project cash flows when the discount rate already captures the capital providers' required return.[^ci-cap-p25]

### NPV, IRR, and ROIC

Enrich `Net Present Value` with:

$$
NPV=CF_0+\frac{CF_1}{(1+r)^1}+\frac{CF_2}{(1+r)^2}+\cdots+\frac{CF_n}{(1+r)^n}
$$

where $CF_0$ is normally the initial investment and $r$ is the required return of capital suppliers, equivalently the cost of capital to the issuer. For a single or independent project, accept when $NPV>0$ and reject when $NPV<0$. NPV directly estimates the expected change in firm value but does not itself communicate project scale.[^ci-cap-p25]

Enrich `Money-Weighted Return` with a clearly labelled Corporate Issuers subsection using `Internal Rate of Return` and `IRR` as aliases:

$$
0=CF_0+\frac{CF_1}{(1+IRR)^1}+\frac{CF_2}{(1+IRR)^2}+\cdots+\frac{CF_n}{(1+IRR)^n}
$$

IRR communicates profitability, but non-conventional cash flows may produce multiple IRRs or no IRR and the method assumes reinvestment at the IRR. For conventional independent projects, NPV and IRR give the same accept/reject decision: accept if $NPV>0$ and $IRR$ exceeds the cost of capital.[^ci-cap-p26]

Create `Conventional Cash Flow` and `Non-Conventional Cash Flow`. Conventional project cash flows change sign once; non-conventional cash flows change sign more than once and may produce multiple or nonexistent IRRs.[^ci-cap-p26]

Enrich `Return on Invested Capital` with:

$$
ROIC=\frac{After\text{-}tax\ operating\ profit}{Average\ invested\ capital}
=\frac{Operating\ profit\times(1-T)}{Average\ long\text{-}term\ liabilities+Average\ equity}
$$

The source excludes working capital from invested capital and decomposes ROIC as:

$$
ROIC=After\text{-}tax\ operating\ profit\ margin\times Capital\ turnover
$$

ROIC above the cost of capital indicates value creation. Its inputs are available to outside analysts, but it is accounting-based, backward-looking, potentially volatile, and aggregated enough to hide profitable or unprofitable areas.[^ci-cap-p27]

### Project interaction and ranking conflicts

Enrich `Independent Project`, `Mutually Exclusive Project`, `Capital Rationing`, and `Project Sequencing`. Accept every positive-NPV independent project when funds are unlimited. Mutually exclusive projects compete directly, so choose the highest positive NPV. Capital rationing imposes a fixed funding pool, while project sequencing requires projects to be undertaken in time order.[^ci-cap-p28]

Enrich `NPV Profile` and `Crossover Rate`. NPV and IRR rankings may conflict because projects differ in cash-flow size or timing and because NPV assumes reinvestment at the cost of capital while IRR assumes reinvestment at the project IRR. The crossover rate is the discount rate at which competing projects have equal NPVs; calculate it as the IRR of the differences between their cash-flow streams. For mutually exclusive projects, use NPV as the final decision criterion.[^ci-cap-p28][^ci-cap-p29]

### Real options

Enrich `Real Option`, `Timing Option`, `Abandonment Option`, `Growth Option`, `Flexibility Option`, and `Fundamental Option`. Create `Sizing Option` as the parent of abandonment and growth options. Timing options allow delay; sizing options change project scale; flexibility options include price-setting and production flexibility; and fundamental options concern projects whose value is intrinsically option-like, such as a mine or oil well.[^ci-cap-p30]

Use the source's project-value bridge:

$$
NPV_{with\ option}=NPV_{without\ option}+Value\ of\ real\ options-Cost\ of\ real\ option
$$

Decision trees and option-pricing models value options by assigning probabilities and expected timing to possible outcomes.[^ci-cap-p30]

### Common investment-decision errors

Replace the generic `Capital Budgeting Error` note with the source taxonomy. Cognitive errors include internal forecasting errors, incorrect overhead or discount rates, failure to incorporate competitor responses, treating internal funds as free and external funds as expensive, and inconsistent handling of inflation. Cash flows and discount rates must both be nominal or both real. Behavioral errors include inertia despite falling returns, relying on accounting measures such as EPS, net income, or ROE, pet-project bias, and failure to consider alternatives.[^ci-cap-p31]

## Navigation changes on merge

Add `Conventional Cash Flow`, `Non-Conventional Cash Flow`, and `Sizing Option` to the chapter map. Group the map into project types, incremental cash flows, decision methods, project interactions, real options, and decision errors.

## Review checklist

- [x] Every formula and decision rule was visually checked against PDF pages 24-31.
- [x] The IRR content enriches the existing `Money-Weighted Return` node rather than creating a duplicate.
- [x] Trusted notes and Personal Notes remain unchanged at proposal stage.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes byte-for-byte and passes validation.

## Evidence

[^ci-cap-p24]: [[corporate-issuers-level-1-speed-review.pdf#page=24|Corporate Issuers Level I Speed Review, PDF p. 24]]
[^ci-cap-p25]: [[corporate-issuers-level-1-speed-review.pdf#page=25|Corporate Issuers Level I Speed Review, PDF p. 25]]
[^ci-cap-p26]: [[corporate-issuers-level-1-speed-review.pdf#page=26|Corporate Issuers Level I Speed Review, PDF p. 26]]
[^ci-cap-p27]: [[corporate-issuers-level-1-speed-review.pdf#page=27|Corporate Issuers Level I Speed Review, PDF p. 27]]
[^ci-cap-p28]: [[corporate-issuers-level-1-speed-review.pdf#page=28|Corporate Issuers Level I Speed Review, PDF p. 28]]
[^ci-cap-p29]: [[corporate-issuers-level-1-speed-review.pdf#page=29|Corporate Issuers Level I Speed Review, PDF p. 29]]
[^ci-cap-p30]: [[corporate-issuers-level-1-speed-review.pdf#page=30|Corporate Issuers Level I Speed Review, PDF p. 30]]
[^ci-cap-p31]: [[corporate-issuers-level-1-speed-review.pdf#page=31|Corporate Issuers Level I Speed Review, PDF p. 31]]
