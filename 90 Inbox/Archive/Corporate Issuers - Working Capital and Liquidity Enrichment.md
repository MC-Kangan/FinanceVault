---
id: proposal-corporate-issuers-l1-working-capital-liquidity-enrichment
type: proposal
title: Corporate Issuers - Working Capital and Liquidity Enrichment
target: "[[Corporate Issuers - Working Capital and Liquidity]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Corporate Issuers - Working Capital and Liquidity Enrichment

## Rationale

The current notes contain the correct node names but omit the source lists, formulas, and risk-return comparison that make this chapter useful for revision.

## Exact proposed content

### Sources and deterioration of liquidity

Enrich `Primary Liquidity Source` with cash and marketable securities that can be sold quickly without significant value loss, borrowing or supplier trade credit, cash flow from operations, and free cash flow. Preserve the source convention:

$$
Free\ cash\ flow=CFO-Investments\ in\ long\text{-}term\ assets
$$

[^ci-wc-p16]

Enrich `Secondary Liquidity Source` with dividend suspension or reduction, delayed or reduced capital expenditure, equity issuance, contract renegotiation, asset sales, bankruptcy protection and reorganization. Explain that these actions may dilute shareholders, sacrifice opportunities, impair long-term value, or incur liquidation costs such as fees and illiquidity discounts.[^ci-wc-p16]

Enrich `Liquidity Drag` as a force that slows cash inflows, including uncollected receivables, obsolete inventory, and borrowing constraints. Enrich `Liquidity Pull` as a force that accelerates outflows, including early payment, reduced trade-credit limits or short-term credit lines, and chronic liquidity shortages.[^ci-wc-p17]

### Liquidity and operating-efficiency measures

Ensure the three liquidity-ratio notes contain their exact formulas:

$$
Current\ ratio=\frac{Current\ assets}{Current\ liabilities}
$$

$$
Quick\ ratio=\frac{Cash+Short\text{-}term\ marketable\ securities+Receivables}{Current\ liabilities}
$$

$$
Cash\ ratio=\frac{Cash+Short\text{-}term\ marketable\ securities}{Current\ liabilities}
$$

Higher values generally indicate greater liquidity, but the ratios become progressively narrower from current to quick to cash.[^ci-wc-p17]

Create `Operating Cycle` and connect it to `Cash Conversion Cycle`. The operating cycle covers inventory conversion plus receivables collection; the cash conversion cycle measures the time between paying suppliers and collecting cash from the subsequent sale:

$$
Operating\ cycle=DOH+DSO
$$

$$
Cash\ conversion\ cycle=DOH+DSO-DPO
$$

A shorter or even negative cash conversion cycle indicates more efficient operations in the source's framing.[^ci-wc-p18]

### Trade credit

Enrich `Trade Credit` and `Effective Annual Rate` using payment terms of the form `a/m, net n`: receive an $a\%$ discount by paying on day $m$, otherwise pay the full amount on day $n$. The annualized opportunity cost of forgoing the discount is:

$$
EAR=\left(1+\frac{Discount\%}{100\%-Discount\%}\right)^{\frac{Days\ in\ year}{Payment\ period-Discount\ period}}-1
$$

For `a/m, net n`, this becomes:

$$
EAR=\left(1+\frac{a\%}{100\%-a\%}\right)^{\frac{365}{n-m}}-1
$$

The common error is treating the discount percentage itself as the borrowing cost without adjusting the base or annualizing the period.[^ci-wc-p18]

### Working-capital definitions and policies

Correctly distinguish the two source definitions:

$$
Total\ working\ capital=Current\ assets-Current\ liabilities
$$

$$
Net\ working\ capital=(Current\ assets-Cash-Marketable\ securities)
-(Current\ liabilities-Short\text{-}term\ and\ current\ debt)
$$

The deck's `Total Working Capital` label therefore differs from the convention used in some other finance texts; preserve the source wording and flag the convention in both notes.[^ci-wc-p19]

Enrich the working-capital policy notes with both asset and financing choices:

| Policy | Current-asset stance | Financing stance | Risk/return |
| --- | --- | --- | --- |
| Aggressive | Minimize excess cash, receivables, and inventories | Short-term liabilities finance variable current assets and part of permanent current assets | Higher |
| Moderate | Between the two extremes | Short-term liabilities finance variable current assets; long-term debt and equity finance permanent current and non-current assets | Moderate |
| Conservative | Hold more cash, receivables, and inventories | Long-term debt and equity finance non-current, permanent current, and part of variable current assets | Lower |

[^ci-wc-p19][^ci-wc-p20]

### Short-term funding

Enrich `Short-Term Funding` with its objectives: maintain sufficient and diversified credit sources for ongoing needs, preserve adequate capacity for changing cash needs, secure competitive rates and terms, and consider both implicit and explicit costs. Strategy depends on company size and creditworthiness, legal and regulatory constraints, and the availability of underlying assets as collateral.[^ci-wc-p21]

## Navigation changes on merge

Add `Operating Cycle` to the chapter map. Reorganize the map into liquidity sources, deterioration, ratios and cycles, trade credit, working-capital definitions/policies, and short-term funding. Preserve links back to FSA ratio notes.

## Review checklist

- [x] Formulas and policy directions were visually checked against PDF pages 16-21.
- [x] The source-specific working-capital terminology is explicitly flagged.
- [x] Trusted notes and Personal Notes remain unchanged at proposal stage.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes byte-for-byte and passes validation.

## Evidence

[^ci-wc-p16]: [[corporate-issuers-level-1-speed-review.pdf#page=16|Corporate Issuers Level I Speed Review, PDF p. 16]]
[^ci-wc-p17]: [[corporate-issuers-level-1-speed-review.pdf#page=17|Corporate Issuers Level I Speed Review, PDF p. 17]]
[^ci-wc-p18]: [[corporate-issuers-level-1-speed-review.pdf#page=18|Corporate Issuers Level I Speed Review, PDF p. 18]]
[^ci-wc-p19]: [[corporate-issuers-level-1-speed-review.pdf#page=19|Corporate Issuers Level I Speed Review, PDF p. 19]]
[^ci-wc-p20]: [[corporate-issuers-level-1-speed-review.pdf#page=20|Corporate Issuers Level I Speed Review, PDF p. 20]]
[^ci-wc-p21]: [[corporate-issuers-level-1-speed-review.pdf#page=21|Corporate Issuers Level I Speed Review, PDF p. 21]]
