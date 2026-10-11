---
id: proposal-fsa-l1-ratios-inventory-long-lived-assets-enrichment
type: proposal
title: Financial Statement Analysis - Ratios Inventory and Long-Lived Assets Enrichment
target: "[[Financial Statement Analysis]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Financial Statement Analysis - Ratios Inventory and Long-Lived Assets Enrichment

## Rationale

The existing ratio, inventory, intangible-asset, impairment, and disposal notes preserve atomic link targets but omit much of the compact formula and comparison content in the source slides. This bundle adds that source-backed detail without introducing outside curriculum material.

## Exact proposed content

### Analysis methods and limitations

Enrich `Common-Size Financial Statement`, `Horizontal Analysis`, and `Vertical Analysis` with the source formulas and use cases. A common-size income statement expresses each item as a percentage of revenue; a common-size balance sheet expresses each item as a percentage of total assets. Horizontal analysis compares changes through time, while vertical analysis compares components within a period.[^fsa-rila-p43]

Add the slide's limitations to the ratio-analysis branch: companies may operate in different businesses, accounting consistency may be imperfect, analyst judgment remains necessary, and alternative calculation methods may produce different ratios.[^fsa-rila-p43]

### Activity ratios

Enrich `Total Asset Turnover`, `Fixed Asset Turnover`, `Working Capital Turnover`, `Inventory Turnover`, `Days Inventory on Hand`, `Receivables Turnover`, `Days Sales Outstanding`, `Payables Turnover`, and `Days Payables Outstanding` with these formulas:

$$
Total\ asset\ turnover=\frac{Revenue}{Average\ total\ assets}
$$

$$
Fixed\ asset\ turnover=\frac{Revenue}{Average\ net\ fixed\ assets}
$$

$$
Working\ capital\ turnover=\frac{Revenue}{Average\ working\ capital}
$$

$$
Inventory\ turnover=\frac{COGS}{Average\ inventory},\qquad
Days\ inventory\ on\ hand=\frac{365}{Inventory\ turnover}
$$

$$
Receivables\ turnover=\frac{Revenue}{Average\ receivables},\qquad
Days\ sales\ outstanding=\frac{365}{Receivables\ turnover}
$$

$$
Payables\ turnover=\frac{Purchases}{Average\ trade\ payables},\qquad
Days\ payables\ outstanding=\frac{365}{Payables\ turnover}
$$

$$
Operating\ cycle=Days\ inventory\ on\ hand+Days\ sales\ outstanding
$$

$$
Cash\ conversion\ cycle=Operating\ cycle-Days\ payables\ outstanding
$$

[^fsa-rila-p44]

### Liquidity, solvency, and profitability ratios

Enrich `Current Ratio`, `Quick Ratio`, and `Cash Ratio` with:

$$
Current\ ratio=\frac{Current\ assets}{Current\ liabilities}
$$

$$
Quick\ ratio=\frac{Cash+Marketable\ securities+Receivables}{Current\ liabilities}
$$

$$
Cash\ ratio=\frac{Cash+Marketable\ securities}{Current\ liabilities}
$$

Also add the defensive-interval formula to the liquidity branch rather than creating a duplicate ratio node unless later sources show it recurring as an independent concept.[^fsa-rila-p45]

Enrich `Debt-to-Assets Ratio`, `Debt-to-Equity Ratio`, `Financial Leverage Ratio`, and `Interest Coverage Ratio` with:

$$
Debt\text{-}to\text{-}assets=\frac{Total\ debt}{Total\ assets},\qquad
Debt\text{-}to\text{-}equity=\frac{Total\ debt}{Total\ equity}
$$

$$
Financial\ leverage=\frac{Average\ total\ assets}{Average\ total\ equity}
$$

$$
Interest\ coverage=\frac{EBIT}{Interest\ payments}
$$

Add debt-to-capital and fixed-charge coverage to the solvency comparison section. Keep their exact slide formulas in the map unless they later recur strongly enough to justify independent concept notes.[^fsa-rila-p45]

Enrich `Gross Profit Margin`, `Operating Profit Margin`, `Pretax Margin`, `Net Profit Margin`, `Return on Assets`, `Operating Return on Assets`, and `Return on Equity` with:

$$
Gross\ profit\ margin=\frac{Gross\ profit}{Revenue},\quad
Operating\ profit\ margin=\frac{Operating\ profit}{Revenue}
$$

$$
Pretax\ margin=\frac{EBT}{Revenue},\quad
Net\ profit\ margin=\frac{Net\ income}{Revenue}
$$

$$
ROA=\frac{Net\ income}{Average\ total\ assets}
$$

$$
Adjusted\ ROA=\frac{Net\ income+After\text{-}tax\ interest}{Average\ total\ assets}
$$

$$
ROE=\frac{Net\ income}{Average\ total\ equity}
$$

Add the source's return-on-capital formula to the profitability comparison section and link it to the existing `Return on Invested Capital` concept only if the definitions are clearly distinguished during merge.[^fsa-rila-p46]

Enrich `DuPont Analysis` with all three source decompositions:

$$
ROE=ROA\times Financial\ leverage
$$

$$
ROE=Net\ profit\ margin\times Total\ asset\ turnover\times Financial\ leverage
$$

$$
ROE=Tax\ burden\times Interest\ burden\times EBIT\ margin\times Total\ asset\ turnover\times Financial\ leverage
$$

where the source defines tax burden as net income divided by EBT and interest burden as EBT divided by EBIT.[^fsa-rila-p47]

### Inventory methods and write-downs

Enrich `Inventory Cost Method`, `First-In First-Out`, `Last-In First-Out`, `Specific Identification`, and `Weighted Average Cost` with the rising-price comparison. LIFO is shown as available under US GAAP but not IFRS.[^fsa-rila-p50]

| Rising-price effect | LIFO | FIFO |
| --- | --- | --- |
| COGS | Higher | Lower |
| Operating income, tax, and net income | Lower | Higher |
| Inventory and working capital | Lower | Higher |
| CFO | Higher | Lower |
| Profit margins and current ratio | Lower | Higher |
| Debt-to-assets and debt-to-equity | Higher | Lower |
| Inventory turnover | Higher | Lower |

[^fsa-rila-p50]

Enrich `Net Realizable Value` and `Inventory Write-Down` with:

$$
NRV=Estimated\ selling\ price-Estimated\ selling\ costs
$$

Under the slide's IFRS treatment, inventory is measured at the lower of cost and NRV, and a previous write-down may be reversed up to the original amount. Under the slide's US-GAAP treatment, non-LIFO inventory uses lower of cost and NRV; LIFO or retail-method inventory uses replacement cost constrained by NRV as the ceiling and NRV less normal profit as the floor, with no reversal.[^fsa-rila-p51]

An inventory write-down reduces inventory and profit, weakens the profit, liquidity, and solvency measures identified in the slide, and mechanically improves activity ratios. High turnover and low days inventory may indicate efficient management or inventory shortages. Agricultural, forest, and mineral inventories with active markets may be measured at NRV with gains and losses reported in income.[^fsa-rila-p52]

### Intangibles, impairment, held-for-sale assets, and disposal

Enrich `Intangible Asset` and `Research and Development Costs` with the source's three acquisition routes: separately purchased, internally generated, and acquired in a business combination. Research is expensed; IFRS development may be capitalized after the stated criteria are met, while the slide limits US-GAAP capitalization largely to qualifying software development.[^fsa-rila-p54]

Enrich `Asset Impairment`, `Recoverable Amount`, and `Value in Use` with:

$$
Recoverable\ amount=\max(Fair\ value-Loss\ on\ sale,\ Value\ in\ use)
$$

The source defines value in use as the present value of expected future cash flows. The IFRS impairment loss is carrying amount less recoverable amount; the US-GAAP sequence first assesses recoverability using undiscounted cash flows and then measures loss using fair value.[^fsa-rila-p55][^fsa-rila-p56]

Record that an impairment reduces carrying value and net income but is noncash and therefore does not directly reduce CFO. Finite-lived intangibles follow the applicable impairment framework; indefinite-lived intangibles are tested annually and impaired when carrying amount exceeds the relevant fair-value benchmark in the source.[^fsa-rila-p56]

Enrich `Asset Held for Sale` and `Impairment Reversal`: classification requires intent to sell and a highly probable sale; measure at fair value less costs to sell and stop depreciation. The slide permits IFRS reversals for assets held for use or sale, while US GAAP prohibits reversal for held-for-use assets and permits it for held-for-sale assets within the stated constraints.[^fsa-rila-p57]

Enrich `Long-Lived Asset Disposal` with:

$$
Gain\ or\ loss\ on\ sale=Sale\ proceeds-Book\ value
$$

Abandonment produces a loss equal to the remaining book value. Preserve the slide's exchange-treatment mechanics as a concise comparison, without adding unstated tax or commercial-substance rules.[^fsa-rila-p59]

## Navigation changes on merge

Create subtopic maps `FSA - Financial Statement Analysis Techniques`, `FSA - Inventories`, and `FSA - Long-Lived Assets`. Link them from `Financial Statement Analysis`, distribute the relevant concepts among them, and remove the large flat index once every concept remains reachable through a chapter map.

## Review checklist

- [x] Every proposed formula and comparison comes from the registered FSA source.
- [x] Formula signs, denominators, and table directions were visually checked against rendered pages.
- [x] The proposal avoids filling in blank practice answers.
- [x] Existing aliases and canonical filenames remain unchanged.
- [x] Trusted notes and Personal Notes remain unchanged at proposal stage.
- [x] User approves this enrichment bundle.
- [x] Merge preserves every Personal Notes block byte-for-byte.
- [x] Post-merge validation and graph inspection pass.

## Evidence

[^fsa-rila-p43]: [[financial-statement-analysis-level-1-speed-review.pdf#page=43|Financial Statement Analysis Level I Speed Review, PDF p. 43]]
[^fsa-rila-p44]: [[financial-statement-analysis-level-1-speed-review.pdf#page=44|Financial Statement Analysis Level I Speed Review, PDF p. 44]]
[^fsa-rila-p45]: [[financial-statement-analysis-level-1-speed-review.pdf#page=45|Financial Statement Analysis Level I Speed Review, PDF p. 45]]
[^fsa-rila-p46]: [[financial-statement-analysis-level-1-speed-review.pdf#page=46|Financial Statement Analysis Level I Speed Review, PDF p. 46]]
[^fsa-rila-p47]: [[financial-statement-analysis-level-1-speed-review.pdf#page=47|Financial Statement Analysis Level I Speed Review, PDF p. 47]]
[^fsa-rila-p50]: [[financial-statement-analysis-level-1-speed-review.pdf#page=50|Financial Statement Analysis Level I Speed Review, PDF p. 50]]
[^fsa-rila-p51]: [[financial-statement-analysis-level-1-speed-review.pdf#page=51|Financial Statement Analysis Level I Speed Review, PDF p. 51]]
[^fsa-rila-p52]: [[financial-statement-analysis-level-1-speed-review.pdf#page=52|Financial Statement Analysis Level I Speed Review, PDF p. 52]]
[^fsa-rila-p54]: [[financial-statement-analysis-level-1-speed-review.pdf#page=54|Financial Statement Analysis Level I Speed Review, PDF p. 54]]
[^fsa-rila-p55]: [[financial-statement-analysis-level-1-speed-review.pdf#page=55|Financial Statement Analysis Level I Speed Review, PDF p. 55]]
[^fsa-rila-p56]: [[financial-statement-analysis-level-1-speed-review.pdf#page=56|Financial Statement Analysis Level I Speed Review, PDF p. 56]]
[^fsa-rila-p57]: [[financial-statement-analysis-level-1-speed-review.pdf#page=57|Financial Statement Analysis Level I Speed Review, PDF p. 57]]
[^fsa-rila-p59]: [[financial-statement-analysis-level-1-speed-review.pdf#page=59|Financial Statement Analysis Level I Speed Review, PDF p. 59]]
