---
id: proposal-fsa-l1-statements-revenue-eps-cash-flow-enrichment
type: proposal
title: Financial Statement Analysis - Statements Revenue EPS and Cash Flow Enrichment
target: "[[Financial Statement Analysis]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Financial Statement Analysis - Statements Revenue EPS and Cash Flow Enrichment

## Rationale

The current notes for the three financial statements, reporting sources, revenue and expense recognition, earnings per share, financial instruments, and cash-flow presentation usually contain only a definition and exam-focus sentence. The source slides contain additional formulas, comparison rules, workflows, and worked mechanics that should be retained because the deck is already a condensed review source.

## Exact proposed content

### Financial statements and reporting framework

Enrich `Balance Sheet`, `Accounting Equation`, `Income Statement`, `Cash Flow Statement`, and `Retained Earnings` with these distinctions and linkages:

- The balance sheet reports financial position at a point in time. Assets are controlled resources, liabilities are obligations owed, and equity is the residual interest. Preserve both $A=L+E$ and $\Delta A=\Delta L+\Delta E$.[^fsa-srecf-p4]
- The income statement and cash-flow statement report activity over a period. The income statement uses accrual accounting, while the cash-flow statement classifies cash movements as operating, investing, or financing.[^fsa-srecf-p5]
- Retained earnings follows $RE_{end}=RE_{begin}+NI-Dividends$; ending cash follows beginning cash plus the net cash movement for the period. Link these roll-forwards back to the balance sheet.[^fsa-srecf-p5]

Enrich `Financial Reporting` and `Financial Statement Analysis Process` with the purpose distinction and six-step process: establish purpose and context, collect data, process data, analyze and interpret, communicate conclusions and recommendations, and follow up or update the analysis.[^fsa-srecf-p6]

Enrich `Financial Reporting Sources`, `Financial Statement Footnotes`, `Segment Reporting`, `Audit Opinion`, `Management Discussion and Analysis`, and `Accounting Standard-Setting Bodies` with:

- The source hierarchy includes primary financial statements, notes, management discussion, the audit report, and supplementary sources such as proxy materials, conference calls, and press releases.[^fsa-srecf-p7]
- Footnotes are audited and necessary for understanding the statements; they disclose the preparation basis, accounting policies, methods, estimates, and segment information.[^fsa-srecf-p8]
- The slide's segment threshold is 10% of revenue, assets, or operating profit. A customer accounting for at least 10% of total revenue triggers disclosure of that fact, not the customer's identity.[^fsa-srecf-p8]
- An audit is an independent review providing reasonable assurance about fair presentation. Distinguish unqualified, qualified, adverse, and disclaimer opinions, and note the separate internal-control reporting requirement shown for US-listed companies.[^fsa-srecf-p9]
- MD&A is normally unaudited and covers the business, objectives and strategy, resources, risks and relationships, results, and critical performance measures.[^fsa-srecf-p10]
- FASB issues US GAAP and IASB issues IFRS; government bodies enforce reporting requirements. Retain the slide's SEC filing examples: S-1, DEF 14A, 8-K, Form 144, 10-K, and 10-Q.[^fsa-srecf-p11]

### Revenue and expense recognition

Enrich `Revenue Recognition` and `Performance Obligation` with the five-step model:

1. Identify the contract with the customer.
2. Identify the performance obligations.
3. Determine the transaction price.
4. Allocate the transaction price to the performance obligations.
5. Recognize revenue when each performance obligation is satisfied and control transfers.[^fsa-srecf-p15]

Add to `Long-Term Contract Revenue Recognition` the slide's input-method mechanics. In year 1, progress is $420/700=60\%$ and recognized revenue is $1{,}000\times60\%=600$ (thousand). After the year-2 modification, cumulative progress is $670/820=81.71\%$ and current-year revenue is cumulative revenue of $1{,}350\times81.71\%$ less the $600$ previously recognized, producing approximately $503.049$ thousand.[^fsa-srecf-p16]

Enrich `Principal-Agent Relationship`, `License Revenue`, and `Bill-and-Hold Arrangement`:

- A principal controls the good or service before transfer and reports gross revenue; an agent reports the fee or commission earned.[^fsa-srecf-p17]
- License revenue is recognized over the license term or at the transfer date according to the nature of the performance obligation shown in the slide.[^fsa-srecf-p17]
- A bill-and-hold sale is recognized only when the customer has obtained control even though physical delivery is delayed.[^fsa-srecf-p17]

Enrich `Expense Recognition` and `Capitalization versus Expensing` with matching versus period-cost treatment and the complete comparison table:

| Effect | Capitalize initially | Expense initially |
| --- | --- | --- |
| Assets and equity | Higher | Lower |
| Current net income | Higher | Lower |
| Later net income | Lower | Higher |
| Total net income over the full life | Same | Same |
| Net-income volatility | Lower | Higher |
| First-year ROA and ROE | Higher | Lower |
| Later ROA and ROE | Lower | Higher |
| CFO | Higher | Lower |
| CFI | Lower | Higher |
| Total cash flow | Same | Same |

The comparison must be cited to the source table rather than generalized beyond it.[^fsa-srecf-p18]

Enrich `Capitalized Interest` and `Research and Development Costs`:

- Interest incurred to construct an asset requiring a long preparation period is capitalized. For interest coverage, the slide includes both capitalized and expensed interest in the denominator.[^fsa-srecf-p19]
- Research cost is expensed. Under the slide's IFRS treatment, development cost may be capitalized when criteria including technical feasibility, intent and ability to complete, and ability to use or sell are satisfied.[^fsa-srecf-p19]

Enrich `Unusual or Infrequent Items`, `Discontinued Operations`, `Change in Accounting Principle`, `Change in Accounting Estimate`, and `Prior-Period Error`:

- Material or relevant items are separately disclosed. Examples shown include gains or losses on asset sales, impairments, and restructuring charges.[^fsa-srecf-p20]
- Discontinued operations are shown separately net of tax.[^fsa-srecf-p21]
- A change in accounting principle is retrospective, a change in accounting estimate is prospective, and a prior-period error requires restatement of prior periods.[^fsa-srecf-p21]

### Earnings per share

Enrich `Basic Earnings per Share` with:

$$
Basic\ EPS=\frac{Net\ income-Preferred\ dividends}{Weighted\ average\ common\ shares\ outstanding}
$$

Shares issued or repurchased are time-weighted, while a stock split is reflected retrospectively for all presented periods.[^fsa-srecf-p22]

Enrich `Diluted Earnings per Share` and `If-Converted Method` with separate mechanics for convertible preferred shares and convertible debt:

$$
Diluted\ EPS_{preferred}=\frac{NI-Preferred\ dividends+Convertible\ preferred\ dividends}{WASO+Shares\ from\ assumed\ conversion}
$$

$$
Diluted\ EPS_{debt}=\frac{NI-Preferred\ dividends+After\text{-}tax\ interest}{WASO+Shares\ from\ assumed\ conversion}
$$

Use the inputs on PDF pages 23-24 as worked mechanics, but do not invent any answer that is not displayed in the source.[^fsa-srecf-p23][^fsa-srecf-p24]

Enrich `Treasury Stock Method` with:

$$
Incremental\ shares=Shares\ issued\ on\ exercise-Shares\ repurchased\ with\ exercise\ proceeds
$$

Apply time weighting when the options or warrants were not outstanding for the full period.[^fsa-srecf-p25]

### Intangibles and financial instruments

Enrich `Intangible Asset` with purchased versus internally generated assets; finite-lived assets are amortized systematically, reviewed for useful-life changes, and tested for impairment, while indefinite-lived assets are not amortized and are tested at least annually.[^fsa-srecf-p29]

Enrich `Goodwill` with the acquisition calculation and treatment:

$$
Goodwill=Purchase\ consideration-Fair\ value\ of\ identifiable\ net\ assets\ acquired
$$

The slide example pays 10 million for 80% of a target whose identifiable net assets have a fair value of 10 million, producing 2 million of goodwill on the stated basis. Goodwill is not amortized and is tested annually for impairment.[^fsa-srecf-p30]

Enrich `Financial Asset Classification`, `Amortized Cost`, `Fair Value through Profit or Loss`, `Fair Value through Other Comprehensive Income`, and `Financial Liability Measurement` with the source comparison:

| Measurement category | Balance-sheet measurement | Income-statement / OCI treatment shown |
| --- | --- | --- |
| Amortized cost | Amortized cost | Realized gain or loss in income |
| FVPL | Fair value | Realized and unrealized gains or losses in income |
| FVOCI | Fair value | Realized gains or losses in income; unrealized gains or losses in OCI |

The classification decision first distinguishes debt from equity and then considers the business model and contractual cash-flow characteristics. Financial liabilities are generally measured at amortized cost or fair value in the source framework.[^fsa-srecf-p31][^fsa-srecf-p32][^fsa-srecf-p33]

### Cash-flow statement

Enrich `Cash Flow Classification` with the complete source comparison:

| Item | US GAAP | IFRS alternatives shown |
| --- | --- | --- |
| Interest received | CFO | CFO or CFI |
| Interest paid | CFO | CFO or CFF |
| Dividends received | CFO | CFO or CFI |
| Dividends paid | CFF | CFO or CFF |

For a mature company, CFO above net income is presented as desirable; strong reported income accompanied by weak CFO can indicate weak earnings quality or aggressive accounting. Add this interpretation to `Operating Cash Flow Quality` and link it to `Earnings Quality`.[^fsa-srecf-p36]

Enrich `Direct Method CFO` with the slide's working-capital equations:

$$
AR_{beg}+Revenue-Cash\ received=AR_{end}
$$

$$
AP_{beg}+Purchases-Cash\ paid=AP_{end}
$$

$$
Inventory_{beg}+Purchases-COGS=Inventory_{end}
$$

$$
Interest\ payable_{beg}+Interest\ expense-Cash\ paid=Interest\ payable_{end}
$$

$$
Tax\ payable_{beg}+Taxable\ income\times Tax\ rate-Cash\ paid=Tax\ payable_{end}
$$

[^fsa-srecf-p37]

Enrich `Indirect Method CFO` with:

$$
CFO=NI+Noncash\ charges\pm Nonoperating\ items-\Delta Current\ assets+\Delta Current\ liabilities
$$

[^fsa-srecf-p38]

Retain `Cash Flow from Investing` and `Cash Flow from Financing` as separate link targets, but do not add answers to the practice tables on PDF page 39 because the slide does not display them.[^fsa-srecf-p39]

Enrich `Free Cash Flow`, `Free Cash Flow to the Firm`, and `Free Cash Flow to Equity` with all four source formulas:

$$
FCFF=NI+Interest(1-t)+NCC-WCInv-FCInv
$$

$$
FCFF=CFO+Interest(1-t)-FCInv
$$

$$
FCFE=FCFF-Interest(1-t)+Net\ borrowing
$$

$$
FCFE=CFO-FCInv+Net\ borrowing
$$

[^fsa-srecf-p40]

## Navigation changes on merge

Create real subtopic maps named `FSA - Financial Statements and Reporting`, `FSA - Income Statement Analysis`, `FSA - Financial Instruments`, and `FSA - Cash Flow Analysis`. Link them from `Financial Statement Analysis` and distribute the enriched concepts among them. Do not add these map links to trusted notes until approval.

## Review checklist

- [x] Every proposed claim and formula is drawn from the registered FSA source.
- [x] Formula, table, and worked-example transcription was visually checked against the rendered slide.
- [x] No answers were inferred for blank practice tables.
- [x] Existing aliases and filenames remain canonical.
- [x] Trusted notes and Personal Notes remain unchanged at proposal stage.
- [x] User approves this enrichment bundle.
- [x] Merge preserves every Personal Notes block byte-for-byte.
- [x] Post-merge validation and graph inspection pass.

## Evidence

[^fsa-srecf-p4]: [[financial-statement-analysis-level-1-speed-review.pdf#page=4|Financial Statement Analysis Level I Speed Review, PDF p. 4]]
[^fsa-srecf-p5]: [[financial-statement-analysis-level-1-speed-review.pdf#page=5|Financial Statement Analysis Level I Speed Review, PDF p. 5]]
[^fsa-srecf-p6]: [[financial-statement-analysis-level-1-speed-review.pdf#page=6|Financial Statement Analysis Level I Speed Review, PDF p. 6]]
[^fsa-srecf-p7]: [[financial-statement-analysis-level-1-speed-review.pdf#page=7|Financial Statement Analysis Level I Speed Review, PDF p. 7]]
[^fsa-srecf-p8]: [[financial-statement-analysis-level-1-speed-review.pdf#page=8|Financial Statement Analysis Level I Speed Review, PDF p. 8]]
[^fsa-srecf-p9]: [[financial-statement-analysis-level-1-speed-review.pdf#page=9|Financial Statement Analysis Level I Speed Review, PDF p. 9]]
[^fsa-srecf-p10]: [[financial-statement-analysis-level-1-speed-review.pdf#page=10|Financial Statement Analysis Level I Speed Review, PDF p. 10]]
[^fsa-srecf-p11]: [[financial-statement-analysis-level-1-speed-review.pdf#page=11|Financial Statement Analysis Level I Speed Review, PDF p. 11]]
[^fsa-srecf-p15]: [[financial-statement-analysis-level-1-speed-review.pdf#page=15|Financial Statement Analysis Level I Speed Review, PDF p. 15]]
[^fsa-srecf-p16]: [[financial-statement-analysis-level-1-speed-review.pdf#page=16|Financial Statement Analysis Level I Speed Review, PDF p. 16]]
[^fsa-srecf-p17]: [[financial-statement-analysis-level-1-speed-review.pdf#page=17|Financial Statement Analysis Level I Speed Review, PDF p. 17]]
[^fsa-srecf-p18]: [[financial-statement-analysis-level-1-speed-review.pdf#page=18|Financial Statement Analysis Level I Speed Review, PDF p. 18]]
[^fsa-srecf-p19]: [[financial-statement-analysis-level-1-speed-review.pdf#page=19|Financial Statement Analysis Level I Speed Review, PDF p. 19]]
[^fsa-srecf-p20]: [[financial-statement-analysis-level-1-speed-review.pdf#page=20|Financial Statement Analysis Level I Speed Review, PDF p. 20]]
[^fsa-srecf-p21]: [[financial-statement-analysis-level-1-speed-review.pdf#page=21|Financial Statement Analysis Level I Speed Review, PDF p. 21]]
[^fsa-srecf-p22]: [[financial-statement-analysis-level-1-speed-review.pdf#page=22|Financial Statement Analysis Level I Speed Review, PDF p. 22]]
[^fsa-srecf-p23]: [[financial-statement-analysis-level-1-speed-review.pdf#page=23|Financial Statement Analysis Level I Speed Review, PDF p. 23]]
[^fsa-srecf-p24]: [[financial-statement-analysis-level-1-speed-review.pdf#page=24|Financial Statement Analysis Level I Speed Review, PDF p. 24]]
[^fsa-srecf-p25]: [[financial-statement-analysis-level-1-speed-review.pdf#page=25|Financial Statement Analysis Level I Speed Review, PDF p. 25]]
[^fsa-srecf-p29]: [[financial-statement-analysis-level-1-speed-review.pdf#page=29|Financial Statement Analysis Level I Speed Review, PDF p. 29]]
[^fsa-srecf-p30]: [[financial-statement-analysis-level-1-speed-review.pdf#page=30|Financial Statement Analysis Level I Speed Review, PDF p. 30]]
[^fsa-srecf-p31]: [[financial-statement-analysis-level-1-speed-review.pdf#page=31|Financial Statement Analysis Level I Speed Review, PDF p. 31]]
[^fsa-srecf-p32]: [[financial-statement-analysis-level-1-speed-review.pdf#page=32|Financial Statement Analysis Level I Speed Review, PDF p. 32]]
[^fsa-srecf-p33]: [[financial-statement-analysis-level-1-speed-review.pdf#page=33|Financial Statement Analysis Level I Speed Review, PDF p. 33]]
[^fsa-srecf-p36]: [[financial-statement-analysis-level-1-speed-review.pdf#page=36|Financial Statement Analysis Level I Speed Review, PDF p. 36]]
[^fsa-srecf-p37]: [[financial-statement-analysis-level-1-speed-review.pdf#page=37|Financial Statement Analysis Level I Speed Review, PDF p. 37]]
[^fsa-srecf-p38]: [[financial-statement-analysis-level-1-speed-review.pdf#page=38|Financial Statement Analysis Level I Speed Review, PDF p. 38]]
[^fsa-srecf-p39]: [[financial-statement-analysis-level-1-speed-review.pdf#page=39|Financial Statement Analysis Level I Speed Review, PDF p. 39]]
[^fsa-srecf-p40]: [[financial-statement-analysis-level-1-speed-review.pdf#page=40|Financial Statement Analysis Level I Speed Review, PDF p. 40]]
