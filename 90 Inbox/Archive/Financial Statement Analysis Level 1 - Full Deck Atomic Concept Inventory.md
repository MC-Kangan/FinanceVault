---
id: proposal-fsa-l1-full-deck-atomic-inventory
type: proposal
title: Financial Statement Analysis Level 1 - Full Deck Atomic Concept Inventory
target: "[[Financial Statement Analysis]]"
change_type: source-inventory-and-granularity-revision
status: merged
tags:
  - cfa/level-1
---

# Financial Statement Analysis Level 1 - Full Deck Atomic Concept Inventory

## Rationale

This replaces the pilot's narrow page selection with a full-deck concept inventory. The deck is already condensed study material, so a recurring named concept, distinct accounting treatment, formula, or useful cross-topic link is retained as its own proposed canonical note. Recap slides remain navigation checks rather than duplicate content.

## Proposed atomic inventory

| PDF pages | Proposed canonical nodes | Handling |
| --- | --- | --- |
| 4-5 | existing `Balance Sheet`, `Accounting Equation`; new `Income Statement`, `Cash Flow Statement`, `Retained Earnings` | Link the three statements rather than keeping one broad “statements” node.[^fsa-inventory-p4][^fsa-inventory-p5] |
| 6-11 | `Financial Reporting`, `Financial Statement Analysis Process`, `Financial Reporting Sources`, `Financial Statement Footnotes`, `Segment Reporting`, `Audit Opinion`, `Management Discussion and Analysis`, `Accounting Standard-Setting Bodies` | Separate source/evidence concepts from the analysis process.[^fsa-inventory-p6][^fsa-inventory-p11] |
| 15-17 | `Revenue Recognition`, `Performance Obligation`, `Long-Term Contract Revenue Recognition`, `Principal-Agent Relationship`, `License Revenue`, `Bill-and-Hold Arrangement` | `Revenue Recognition` is the hub; each special case is directly addressable.[^fsa-inventory-p15][^fsa-inventory-p16][^fsa-inventory-p17] |
| 18-21 | `Expense Recognition`, `Capitalization versus Expensing`, `Capitalized Interest`, `Research and Development Costs`, `Unusual or Infrequent Items`, `Discontinued Operations`, `Change in Accounting Principle`, `Change in Accounting Estimate`, `Prior-Period Error` | Preserve separate effects and retrospective/prospective treatments.[^fsa-inventory-p18][^fsa-inventory-p19][^fsa-inventory-p20][^fsa-inventory-p21] |
| 22-25 | `Basic Earnings per Share`, `Diluted Earnings per Share`, `If-Converted Method`, `Treasury Stock Method` | Convertible preferred and debt examples remain inside `If-Converted Method`; options and warrants link to `Treasury Stock Method`.[^fsa-inventory-p22][^fsa-inventory-p25] |
| 29-33 | `Intangible Asset`, `Goodwill`, `Financial Asset Classification`, `Amortized Cost`, `Fair Value through Profit or Loss`, `Fair Value through Other Comprehensive Income`, `Financial Liability Measurement` | Avoid a single “financial instruments” note swallowing three measurement bases.[^fsa-inventory-p29][^fsa-inventory-p30][^fsa-inventory-p31][^fsa-inventory-p33] |
| 36-39 | `Cash Flow Classification`, `Direct Method CFO`, `Indirect Method CFO`, `Cash Flow from Investing`, `Cash Flow from Financing`, `Operating Cash Flow Quality` | Existing FCF/FCFF/FCFE notes remain separate and link from this branch.[^fsa-inventory-p36][^fsa-inventory-p39] |
| 43 | `Common-Size Financial Statement`, `Horizontal Analysis`, `Vertical Analysis` | Use as analysis methods and map-level navigation.[^fsa-inventory-p43] |
| 44 | `Receivables Turnover`, `Days Sales Outstanding`, `Inventory Turnover`, `Days Inventory on Hand`, `Payables Turnover`, `Days Payables Outstanding`, `Working Capital Turnover`, `Fixed Asset Turnover`, `Total Asset Turnover` | Each repeated ratio receives its own note with formula, interpretation, and pitfalls.[^fsa-inventory-p44] |
| 45 | existing `Current Ratio`, `Interest Coverage Ratio`; new `Quick Ratio`, `Cash Ratio`, `Debt-to-Assets Ratio`, `Debt-to-Equity Ratio`, `Financial Leverage Ratio` | Ratios remain atomic link targets for equity and credit analysis.[^fsa-inventory-p45] |
| 46-47 | existing `Net Profit Margin`, `Return on Equity`, `DuPont Analysis`; new `Gross Profit Margin`, `Operating Profit Margin`, `Pretax Margin`, `Return on Assets`, `Operating Return on Assets` | Preserve direct connections from margins and turnover to DuPont components.[^fsa-inventory-p46][^fsa-inventory-p47] |
| 50-52 | `Inventory Cost Method`, `Specific Identification`, `Weighted Average Cost`, `First-In First-Out`, `Last-In First-Out`, `Inventory Write-Down`, `Net Realizable Value` | FIFO and LIFO are separate recurring concepts; statement and ratio effects live in their notes.[^fsa-inventory-p50][^fsa-inventory-p51][^fsa-inventory-p52] |
| 54-59 | existing `Intangible Asset`; new `Asset Impairment`, `Recoverable Amount`, `Value in Use`, `Asset Held for Sale`, `Impairment Reversal`, `Long-Lived Asset Disposal` | Connect IFRS/US-GAAP contrasts without using the standards as aliases.[^fsa-inventory-p54][^fsa-inventory-p55][^fsa-inventory-p56][^fsa-inventory-p57][^fsa-inventory-p59] |
| 62-70 | detailed in the companion `Leases, Pensions, and Share-Based Compensation` proposal | Includes separate lease models, DC/DB plans, funded status, pension expense, and settlement types.[^fsa-inventory-p62][^fsa-inventory-p70] |
| 73-79 | detailed in the companion `Income Taxes` proposal | Includes separate DTA, DTL, tax-base, difference, allowance, and tax-rate nodes.[^fsa-inventory-p73][^fsa-inventory-p79] |
| 82-83 | `Financial Reporting Quality`, `Earnings Quality`, `Aggressive Accounting`, `Conservative Accounting`, `Fraud Triangle` | Quality dimensions and accounting posture are contrasts, not synonyms.[^fsa-inventory-p82][^fsa-inventory-p83] |
| 84-86 | `Financial Statement Forecasting`, `Forecasting Bias`, `Porter's Five Forces`, `Inflation and Financial Forecasts`, `Normalized Earnings` | Link forecast drivers back to statements, ratios, and valuation inputs.[^fsa-inventory-p84][^fsa-inventory-p85][^fsa-inventory-p86] |

## Repeat-driven priorities

The first merge batch should prioritize concepts that recur across multiple pages or bridge modules:

1. `Intangible Asset` — initial recognition, useful life, impairment, and IFRS/US-GAAP development-cost treatment.[^fsa-inventory-p29][^fsa-inventory-p54][^fsa-inventory-p56]
2. `Capitalization versus Expensing` — financial-statement effects, R&D, intangible assets, and aggressive/conservative reporting.[^fsa-inventory-p18][^fsa-inventory-p19][^fsa-inventory-p54][^fsa-inventory-p83]
3. `Operating Cash Flow Quality` — cash-flow classification and the reporting-quality branch.[^fsa-inventory-p36][^fsa-inventory-p82]
4. `Deferred Tax Asset` and `Valuation Allowance` — tax accounting and aggressive/conservative accounting.[^fsa-inventory-p76][^fsa-inventory-p83]
5. `Interest Coverage Ratio`, `Debt-to-Equity Ratio`, and cash-flow concepts — direct bridges to `Corporate Credit Analysis`.[^fsa-inventory-p45]

## Exclusions

Pages 1-3, 14, 28, 35, 42, 49, 61, 72, and 81 are covers or section dividers. Pages 12-13, 26-27, 34, 41, 48, 53, 58, 60, 66, 71, 80, and 87 are recap maps used only for completeness checks. Page 88 is a closing slide. These pages do not create duplicate concept notes.

## Review checklist

- [x] All 88 pages have a page-separated structured transcription.
- [x] Content pages were visually inventoried; formula-heavy and requested areas were inspected at readable resolution.
- [x] Repeated concepts and cross-module destinations have priority.
- [x] Existing trusted notes remain unchanged.
- [ ] User approves the revised granularity.
- [ ] Detailed thematic proposals are prepared and approved before merge.

## Evidence

[^fsa-inventory-p4]: [[financial-statement-analysis-level-1-speed-review.pdf#page=4|Financial Statement Analysis Level I Speed Review, PDF p. 4]]
[^fsa-inventory-p5]: [[financial-statement-analysis-level-1-speed-review.pdf#page=5|Financial Statement Analysis Level I Speed Review, PDF p. 5]]
[^fsa-inventory-p6]: [[financial-statement-analysis-level-1-speed-review.pdf#page=6|Financial Statement Analysis Level I Speed Review, PDF p. 6]]
[^fsa-inventory-p11]: [[financial-statement-analysis-level-1-speed-review.pdf#page=11|Financial Statement Analysis Level I Speed Review, PDF p. 11]]
[^fsa-inventory-p15]: [[financial-statement-analysis-level-1-speed-review.pdf#page=15|Financial Statement Analysis Level I Speed Review, PDF p. 15]]
[^fsa-inventory-p16]: [[financial-statement-analysis-level-1-speed-review.pdf#page=16|Financial Statement Analysis Level I Speed Review, PDF p. 16]]
[^fsa-inventory-p17]: [[financial-statement-analysis-level-1-speed-review.pdf#page=17|Financial Statement Analysis Level I Speed Review, PDF p. 17]]
[^fsa-inventory-p18]: [[financial-statement-analysis-level-1-speed-review.pdf#page=18|Financial Statement Analysis Level I Speed Review, PDF p. 18]]
[^fsa-inventory-p19]: [[financial-statement-analysis-level-1-speed-review.pdf#page=19|Financial Statement Analysis Level I Speed Review, PDF p. 19]]
[^fsa-inventory-p20]: [[financial-statement-analysis-level-1-speed-review.pdf#page=20|Financial Statement Analysis Level I Speed Review, PDF p. 20]]
[^fsa-inventory-p21]: [[financial-statement-analysis-level-1-speed-review.pdf#page=21|Financial Statement Analysis Level I Speed Review, PDF p. 21]]
[^fsa-inventory-p22]: [[financial-statement-analysis-level-1-speed-review.pdf#page=22|Financial Statement Analysis Level I Speed Review, PDF p. 22]]
[^fsa-inventory-p25]: [[financial-statement-analysis-level-1-speed-review.pdf#page=25|Financial Statement Analysis Level I Speed Review, PDF p. 25]]
[^fsa-inventory-p29]: [[financial-statement-analysis-level-1-speed-review.pdf#page=29|Financial Statement Analysis Level I Speed Review, PDF p. 29]]
[^fsa-inventory-p30]: [[financial-statement-analysis-level-1-speed-review.pdf#page=30|Financial Statement Analysis Level I Speed Review, PDF p. 30]]
[^fsa-inventory-p31]: [[financial-statement-analysis-level-1-speed-review.pdf#page=31|Financial Statement Analysis Level I Speed Review, PDF p. 31]]
[^fsa-inventory-p33]: [[financial-statement-analysis-level-1-speed-review.pdf#page=33|Financial Statement Analysis Level I Speed Review, PDF p. 33]]
[^fsa-inventory-p36]: [[financial-statement-analysis-level-1-speed-review.pdf#page=36|Financial Statement Analysis Level I Speed Review, PDF p. 36]]
[^fsa-inventory-p39]: [[financial-statement-analysis-level-1-speed-review.pdf#page=39|Financial Statement Analysis Level I Speed Review, PDF p. 39]]
[^fsa-inventory-p43]: [[financial-statement-analysis-level-1-speed-review.pdf#page=43|Financial Statement Analysis Level I Speed Review, PDF p. 43]]
[^fsa-inventory-p44]: [[financial-statement-analysis-level-1-speed-review.pdf#page=44|Financial Statement Analysis Level I Speed Review, PDF p. 44]]
[^fsa-inventory-p45]: [[financial-statement-analysis-level-1-speed-review.pdf#page=45|Financial Statement Analysis Level I Speed Review, PDF p. 45]]
[^fsa-inventory-p46]: [[financial-statement-analysis-level-1-speed-review.pdf#page=46|Financial Statement Analysis Level I Speed Review, PDF p. 46]]
[^fsa-inventory-p47]: [[financial-statement-analysis-level-1-speed-review.pdf#page=47|Financial Statement Analysis Level I Speed Review, PDF p. 47]]
[^fsa-inventory-p50]: [[financial-statement-analysis-level-1-speed-review.pdf#page=50|Financial Statement Analysis Level I Speed Review, PDF p. 50]]
[^fsa-inventory-p51]: [[financial-statement-analysis-level-1-speed-review.pdf#page=51|Financial Statement Analysis Level I Speed Review, PDF p. 51]]
[^fsa-inventory-p52]: [[financial-statement-analysis-level-1-speed-review.pdf#page=52|Financial Statement Analysis Level I Speed Review, PDF p. 52]]
[^fsa-inventory-p54]: [[financial-statement-analysis-level-1-speed-review.pdf#page=54|Financial Statement Analysis Level I Speed Review, PDF p. 54]]
[^fsa-inventory-p55]: [[financial-statement-analysis-level-1-speed-review.pdf#page=55|Financial Statement Analysis Level I Speed Review, PDF p. 55]]
[^fsa-inventory-p56]: [[financial-statement-analysis-level-1-speed-review.pdf#page=56|Financial Statement Analysis Level I Speed Review, PDF p. 56]]
[^fsa-inventory-p57]: [[financial-statement-analysis-level-1-speed-review.pdf#page=57|Financial Statement Analysis Level I Speed Review, PDF p. 57]]
[^fsa-inventory-p59]: [[financial-statement-analysis-level-1-speed-review.pdf#page=59|Financial Statement Analysis Level I Speed Review, PDF p. 59]]
[^fsa-inventory-p62]: [[financial-statement-analysis-level-1-speed-review.pdf#page=62|Financial Statement Analysis Level I Speed Review, PDF p. 62]]
[^fsa-inventory-p70]: [[financial-statement-analysis-level-1-speed-review.pdf#page=70|Financial Statement Analysis Level I Speed Review, PDF p. 70]]
[^fsa-inventory-p73]: [[financial-statement-analysis-level-1-speed-review.pdf#page=73|Financial Statement Analysis Level I Speed Review, PDF p. 73]]
[^fsa-inventory-p76]: [[financial-statement-analysis-level-1-speed-review.pdf#page=76|Financial Statement Analysis Level I Speed Review, PDF p. 76]]
[^fsa-inventory-p79]: [[financial-statement-analysis-level-1-speed-review.pdf#page=79|Financial Statement Analysis Level I Speed Review, PDF p. 79]]
[^fsa-inventory-p82]: [[financial-statement-analysis-level-1-speed-review.pdf#page=82|Financial Statement Analysis Level I Speed Review, PDF p. 82]]
[^fsa-inventory-p83]: [[financial-statement-analysis-level-1-speed-review.pdf#page=83|Financial Statement Analysis Level I Speed Review, PDF p. 83]]
[^fsa-inventory-p84]: [[financial-statement-analysis-level-1-speed-review.pdf#page=84|Financial Statement Analysis Level I Speed Review, PDF p. 84]]
[^fsa-inventory-p85]: [[financial-statement-analysis-level-1-speed-review.pdf#page=85|Financial Statement Analysis Level I Speed Review, PDF p. 85]]
[^fsa-inventory-p86]: [[financial-statement-analysis-level-1-speed-review.pdf#page=86|Financial Statement Analysis Level I Speed Review, PDF p. 86]]
