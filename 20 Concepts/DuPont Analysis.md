---
id: concept-dupont-analysis
type: concept
title: DuPont Analysis
aliases:
- DuPont Decomposition
- DuPont Identity
- 杜邦分析
first_level: 1
topics:
- '[[Financial Statement Analysis]]'
- '[[Equity Investments]]'
prerequisites:
- '[[Return on Equity]]'
- '[[Net Profit Margin]]'
used_in: []
related:
- '[[Return on Equity]]'
- '[[Return on Assets]]'
- '[[Operating Risk]]'
contrasts_with: []
source_notes:
- '[[Source - Financial Statement Analysis Level 1 Speed Review]]'
- '[[Source - Equity Investments Level 1 Speed Review]]'
status: trusted
tags:
- cfa/level-1
---
# DuPont Analysis

> [!summary]
> DuPont analysis decomposes return on equity into operating and financing drivers so an analyst can identify why ROE differs across companies or periods.[^fsa-l1-p47]

## Level 1 - Foundation

### Two-part decomposition

$$
\text{ROE}=\text{ROA}\times\text{Financial Leverage Ratio}
$$
[^fsa-l1-p47]

### Three-part decomposition

$$
\text{ROE}=\underbrace{\frac{\text{Net Income}}{\text{Revenue}}}_{\text{Net Profit Margin}}
\times\underbrace{\frac{\text{Revenue}}{\text{Average Total Assets}}}_{\text{Total Asset Turnover}}
\times\underbrace{\frac{\text{Average Total Assets}}{\text{Average Shareholders' Equity}}}_{\text{Financial Leverage}}
$$
[^fsa-l1-p47]

### Five-part decomposition

$$
\text{ROE}=\frac{\text{NI}}{\text{EBT}}
\times\frac{\text{EBT}}{\text{EBIT}}
\times\frac{\text{EBIT}}{\text{Revenue}}
\times\frac{\text{Revenue}}{\text{Average Total Assets}}
\times\frac{\text{Average Total Assets}}{\text{Average Equity}}
$$
[^fsa-l1-p47]

The first two terms are the tax burden and interest burden; the remaining terms represent operating margin, asset turnover, and financial leverage.[^fsa-l1-p47]

### Visual relationship

![[source-fsa-l1-speed-review-p047-dupont-relationship.png|900]][^fsa-l1-p47]

The source figure places the two-, three-, and five-part decompositions together for rapid comparison.[^fsa-l1-p47]

### Common pitfalls

Do not interpret a higher [[Return on Equity]] without identifying the driver: stronger [[Net Profit Margin]] and asset efficiency have different implications from higher leverage.[^fsa-l1-p47]

### Cross-topic applications

<!-- merged:eq-pm-applications -->

**Equity Investments application:** ROIC relative to required return helps assess value creation. ROIC/ROA are unlevered-style measures; leverage converts operating into equity returns. Visually verified: $ROE=\text{net margin}\times\text{asset turnover}\times\text{equity multiplier}$.[^eq-l1-p51]

## Connections

- Begin with [[Return on Equity]].
- Use [[Net Profit Margin]] as the profitability component.
- Return to [[Financial Statement Analysis]] for the ratio-analysis map.

## Personal Notes
<!-- personal:start -->
<!-- personal:end -->

## Sources
[^fsa-l1-p47]: [[financial-statement-analysis-level-1-speed-review.pdf#page=47|Financial Statement Analysis Level I Speed Review, PDF p. 47]]
[^eq-l1-p51]: [[equity-investments-level-1-speed-review.pdf#page=51|Equity Investments Level I Speed Review, PDF p. 51]]
