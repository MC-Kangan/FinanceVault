---
id: proposal-equity-l1-atomic-concept-boundaries
type: proposal
title: Equity Investments Level 1 - Atomic Concept Boundaries
target: Equity Investments
change_type: topic-expansion
status: pending-review
tags:
  - cfa/level-1
---

# Equity Investments Level 1 - Atomic Concept Boundaries

## Rationale

The source is already a condensed review deck, so recurring named ideas, formulas, security types, and reusable analytical tools should become atomic notes. This proposal defines the complete Level 1 concept set and resolves overlap with trusted FSA and Fixed Income notes before any merge.

## Financial Markets and Trading

- Financial System Functions, Market Regulation, Market Efficiency.[^eq-atomic-p4]
- Broker, Dealer, Broker-Dealer, Investment Bank, Exchange, Alternative Trading System, Securitizer, Arbitrageur, Depository Institution, Insurance Company, Settlement and Custody.[^eq-atomic-p5][^eq-atomic-p6]
- Primary Market, Initial Public Offering, Seasoned Offering, Underwritten Offering, Best-Efforts Offering, Private Placement, Shelf Registration, Dividend Reinvestment Plan, Rights Offering.[^eq-atomic-p7][^eq-atomic-p8]
- Call Market, Continuous Market, Quote-Driven Market, Brokered Market, Order-Driven Market, Order Priority, Uniform Pricing, Discriminatory Pricing.[^eq-atomic-p9][^eq-atomic-p10]
- Long Position, Short Position, Short Selling, Margin Buying, Margin Call, Bid-Ask Spread, Market Order, Limit Order, All-or-None Order, Hidden Order, Iceberg Order, Order Validity, Stop Order.[^eq-atomic-p12][^eq-atomic-p13][^eq-atomic-p14][^eq-atomic-p15][^eq-atomic-p16][^eq-atomic-p17]

Reuse/update [[Financial Leverage Ratio]] for the margin relation rather than creating a second leverage-ratio node.[^eq-atomic-p14]

## Security Market Indexes

- Security Market Index, Price Return Index, Total Return Index, Index Divisor, Index Use.[^eq-atomic-p21]
- Equity Index, Real Estate Index, Hedge Fund Index, Commodity Index; reuse/update [[Fixed-Income Index]].[^eq-atomic-p22]
- Price-Weighted Index, Market-Capitalization-Weighted Index, Float-Adjusted Market-Capitalization-Weighted Index, Equal-Weighted Index, Fundamentally Weighted Index.[^eq-atomic-p23][^eq-atomic-p24][^eq-atomic-p25]
- Index Rebalancing and Index Reconstitution.[^eq-atomic-p26]

## Market Efficiency and Behavioral Explanations

- Informational Market Efficiency, Operational Market Efficiency, Weak-Form Market Efficiency, Semi-Strong-Form Market Efficiency, Strong-Form Market Efficiency.[^eq-atomic-p29][^eq-atomic-p30]
- Calendar Anomaly, Momentum Anomaly, Overreaction, Size Effect, Value Effect, Closed-End Fund Discount, IPO Anomaly, Limits to Arbitrage.[^eq-atomic-p31][^eq-atomic-p32][^eq-atomic-p33]
- Overconfidence Bias, Representativeness Bias, Information Cascade, Herding, Mental Accounting, Conservatism Bias, Narrow Framing.[^eq-atomic-p34][^eq-atomic-p35]

These behavioural nodes should later be shared with the Portfolio Management map, not duplicated.

## Equity Securities

- Common Share, Callable Common Share, Putable Common Share.[^eq-atomic-p38]
- Preferred Share, Cumulative Preferred Share, Participating Preferred Share, Convertible Preferred Share.[^eq-atomic-p39]
- Private Equity, Venture Capital, Leveraged Buyout, Private Investment in Public Equity, Depositary Receipt, Sponsored Depositary Receipt, Unsponsored Depositary Receipt, American Depositary Receipt, Global Depositary Receipt.[^eq-atomic-p40][^eq-atomic-p41]
- Book Value of Equity, Market Value of Equity, Cost of Equity.[^eq-atomic-p42]

Do not reuse [[Callable Bond]], [[Putable Bond]], or [[Convertible Bond]]: these are distinct equity instruments.

## Industry and Company Analysis

- Equity Research Report, Business Model, Bottom-Up Forecasting, Top-Down Forecasting, Pricing Power, Cost Structure, Economies of Scale, Economies of Scope, Cash Conversion Cycle, Sources and Uses of Capital.[^eq-atomic-p45][^eq-atomic-p46][^eq-atomic-p47][^eq-atomic-p48][^eq-atomic-p49][^eq-atomic-p50]
- Return on Invested Capital, Operating Risk, Operating Leverage, Degree of Operating Leverage, Financial Risk, Degree of Financial Leverage, Total Leverage, Degree of Total Leverage.[^eq-atomic-p51][^eq-atomic-p52][^eq-atomic-p53]
- Industry Analysis, Industry Classification, Industry Survey, Market Share, Industry Concentration, Herfindahl-Hirschman Index, PESTLE Analysis, Cost Leadership, Differentiation Strategy, Focus Strategy.[^eq-atomic-p54][^eq-atomic-p55][^eq-atomic-p56][^eq-atomic-p57][^eq-atomic-p58][^eq-atomic-p59][^eq-atomic-p60]
- Historical Forecasting, Base-Rate Forecasting, Convergence Forecasting, Management Guidance, Revenue Forecasting, Expense Forecasting, Capital Expenditure Forecasting, Scenario Analysis, Sensitivity Analysis.[^eq-atomic-p61][^eq-atomic-p62][^eq-atomic-p63][^eq-atomic-p64][^eq-atomic-p65][^eq-atomic-p66][^eq-atomic-p67]

Update rather than duplicate [[Return on Equity]], [[Return on Assets]], [[DuPont Analysis]], [[Financial Leverage Ratio]], [[Financial Statement Forecasting]], and [[Porter's Five Forces]].[^eq-atomic-p51][^eq-atomic-p59][^eq-atomic-p61]

## Equity Valuation

- Equity Valuation Model, Dividend Discount Model, Residual Income Model, Price Multiple, Asset-Based Valuation.[^eq-atomic-p71]
- Cash Dividend, Share Repurchase, Stock Dividend, Stock Split, Ex-Dividend Date.[^eq-atomic-p72]
- Gordon Growth Model, Two-Stage Dividend Discount Model, Preferred Stock Valuation, Sustainable Growth Rate.[^eq-atomic-p73]
- Price-to-Earnings Ratio, Price-to-Book Ratio, Price-to-Sales Ratio, Price-to-Cash-Flow Ratio, Trailing Price Multiple, Leading Price Multiple, Justified Price-to-Earnings Ratio.[^eq-atomic-p74][^eq-atomic-p75]
- Enterprise Value and Enterprise Value to EBITDA.[^eq-atomic-p76]

Reuse/update [[Free Cash Flow to Equity]] and [[Free Cash Flow to the Firm]]; their valuation applications belong in those canonical nodes and on the Equity Investments map.[^eq-atomic-p71][^eq-atomic-p74]

### Visually verified formulas

$$
ROE=\text{net margin}\times\text{asset turnover}\times\text{equity multiplier}
$$

$$
DOL=\frac{\%\Delta EBIT}{\%\Delta Q}=\frac{EBIT+F}{EBIT},
\quad
DFL=\frac{\%\Delta NI}{\%\Delta EBIT}=\frac{EBIT}{EBIT-I}
$$

$$
DTL=DOL\times DFL=\frac{\%\Delta NI}{\%\Delta Q}=\frac{EBIT+F}{EBIT-I}
$$

[^eq-atomic-p51][^eq-atomic-p52][^eq-atomic-p53]

$$
V_0=\frac{D_1}{r-g},
\quad
g=(1-\text{dividend payout ratio})ROE
$$

$$
\frac{P_0}{E_1}=\frac{1-b}{r-g},
\quad
\frac{P_0}{E_0}=\frac{(1-b)(1+g)}{r-g}
$$

[^eq-atomic-p73][^eq-atomic-p75]

## Alias decisions

- P/E Ratio, PE Ratio, Price Earnings Ratio, and 市盈率 resolve to Price-to-Earnings Ratio.
- ADR resolves to American Depositary Receipt; GDR resolves to Global Depositary Receipt.
- ROIC, DOL, DFL, DTL, HHI, LBO, and PIPE resolve to their full canonical names.
- Final merge is blocked if the generated alias registry detects any collision.

## High-value visual candidates

- source-equity-l1-speed-review-p041-adr-levels.png — Equity Securities → American Depositary Receipt; crop the ADR Levels I/II/III table from PDF p. 41.
- source-equity-l1-speed-review-p073-ddm-models.png — Equity Valuation → Dividend Discount Model; crop the DDM/Gordon/two-stage relationship from PDF p. 73.

Searchable text and LaTeX remain primary. No crop is proposed for merge yet.

## Review checklist

- [x] Named concepts inventoried at review-deck granularity.
- [x] Overlaps resolved to existing trusted concepts.
- [x] Key formulas visually verified.
- [x] Alias variants mapped to canonical English titles.
- [x] No trusted note changed.
- [ ] User approves concept boundaries, map creation, and updates.

## Evidence

[^eq-atomic-p4]: [[equity-investments-level-1-speed-review.pdf#page=4|Equity Investments Level I Speed Review, PDF p. 4]]
[^eq-atomic-p5]: [[equity-investments-level-1-speed-review.pdf#page=5|Equity Investments Level I Speed Review, PDF p. 5]]
[^eq-atomic-p6]: [[equity-investments-level-1-speed-review.pdf#page=6|Equity Investments Level I Speed Review, PDF p. 6]]
[^eq-atomic-p7]: [[equity-investments-level-1-speed-review.pdf#page=7|Equity Investments Level I Speed Review, PDF p. 7]]
[^eq-atomic-p8]: [[equity-investments-level-1-speed-review.pdf#page=8|Equity Investments Level I Speed Review, PDF p. 8]]
[^eq-atomic-p9]: [[equity-investments-level-1-speed-review.pdf#page=9|Equity Investments Level I Speed Review, PDF p. 9]]
[^eq-atomic-p10]: [[equity-investments-level-1-speed-review.pdf#page=10|Equity Investments Level I Speed Review, PDF p. 10]]
[^eq-atomic-p12]: [[equity-investments-level-1-speed-review.pdf#page=12|Equity Investments Level I Speed Review, PDF p. 12]]
[^eq-atomic-p13]: [[equity-investments-level-1-speed-review.pdf#page=13|Equity Investments Level I Speed Review, PDF p. 13]]
[^eq-atomic-p14]: [[equity-investments-level-1-speed-review.pdf#page=14|Equity Investments Level I Speed Review, PDF p. 14]]
[^eq-atomic-p15]: [[equity-investments-level-1-speed-review.pdf#page=15|Equity Investments Level I Speed Review, PDF p. 15]]
[^eq-atomic-p16]: [[equity-investments-level-1-speed-review.pdf#page=16|Equity Investments Level I Speed Review, PDF p. 16]]
[^eq-atomic-p17]: [[equity-investments-level-1-speed-review.pdf#page=17|Equity Investments Level I Speed Review, PDF p. 17]]
[^eq-atomic-p21]: [[equity-investments-level-1-speed-review.pdf#page=21|Equity Investments Level I Speed Review, PDF p. 21]]
[^eq-atomic-p22]: [[equity-investments-level-1-speed-review.pdf#page=22|Equity Investments Level I Speed Review, PDF p. 22]]
[^eq-atomic-p23]: [[equity-investments-level-1-speed-review.pdf#page=23|Equity Investments Level I Speed Review, PDF p. 23]]
[^eq-atomic-p24]: [[equity-investments-level-1-speed-review.pdf#page=24|Equity Investments Level I Speed Review, PDF p. 24]]
[^eq-atomic-p25]: [[equity-investments-level-1-speed-review.pdf#page=25|Equity Investments Level I Speed Review, PDF p. 25]]
[^eq-atomic-p26]: [[equity-investments-level-1-speed-review.pdf#page=26|Equity Investments Level I Speed Review, PDF p. 26]]
[^eq-atomic-p29]: [[equity-investments-level-1-speed-review.pdf#page=29|Equity Investments Level I Speed Review, PDF p. 29]]
[^eq-atomic-p30]: [[equity-investments-level-1-speed-review.pdf#page=30|Equity Investments Level I Speed Review, PDF p. 30]]
[^eq-atomic-p31]: [[equity-investments-level-1-speed-review.pdf#page=31|Equity Investments Level I Speed Review, PDF p. 31]]
[^eq-atomic-p32]: [[equity-investments-level-1-speed-review.pdf#page=32|Equity Investments Level I Speed Review, PDF p. 32]]
[^eq-atomic-p33]: [[equity-investments-level-1-speed-review.pdf#page=33|Equity Investments Level I Speed Review, PDF p. 33]]
[^eq-atomic-p34]: [[equity-investments-level-1-speed-review.pdf#page=34|Equity Investments Level I Speed Review, PDF p. 34]]
[^eq-atomic-p35]: [[equity-investments-level-1-speed-review.pdf#page=35|Equity Investments Level I Speed Review, PDF p. 35]]
[^eq-atomic-p38]: [[equity-investments-level-1-speed-review.pdf#page=38|Equity Investments Level I Speed Review, PDF p. 38]]
[^eq-atomic-p39]: [[equity-investments-level-1-speed-review.pdf#page=39|Equity Investments Level I Speed Review, PDF p. 39]]
[^eq-atomic-p40]: [[equity-investments-level-1-speed-review.pdf#page=40|Equity Investments Level I Speed Review, PDF p. 40]]
[^eq-atomic-p41]: [[equity-investments-level-1-speed-review.pdf#page=41|Equity Investments Level I Speed Review, PDF p. 41]]
[^eq-atomic-p42]: [[equity-investments-level-1-speed-review.pdf#page=42|Equity Investments Level I Speed Review, PDF p. 42]]
[^eq-atomic-p45]: [[equity-investments-level-1-speed-review.pdf#page=45|Equity Investments Level I Speed Review, PDF p. 45]]
[^eq-atomic-p46]: [[equity-investments-level-1-speed-review.pdf#page=46|Equity Investments Level I Speed Review, PDF p. 46]]
[^eq-atomic-p47]: [[equity-investments-level-1-speed-review.pdf#page=47|Equity Investments Level I Speed Review, PDF p. 47]]
[^eq-atomic-p48]: [[equity-investments-level-1-speed-review.pdf#page=48|Equity Investments Level I Speed Review, PDF p. 48]]
[^eq-atomic-p49]: [[equity-investments-level-1-speed-review.pdf#page=49|Equity Investments Level I Speed Review, PDF p. 49]]
[^eq-atomic-p50]: [[equity-investments-level-1-speed-review.pdf#page=50|Equity Investments Level I Speed Review, PDF p. 50]]
[^eq-atomic-p51]: [[equity-investments-level-1-speed-review.pdf#page=51|Equity Investments Level I Speed Review, PDF p. 51]]
[^eq-atomic-p52]: [[equity-investments-level-1-speed-review.pdf#page=52|Equity Investments Level I Speed Review, PDF p. 52]]
[^eq-atomic-p53]: [[equity-investments-level-1-speed-review.pdf#page=53|Equity Investments Level I Speed Review, PDF p. 53]]
[^eq-atomic-p54]: [[equity-investments-level-1-speed-review.pdf#page=54|Equity Investments Level I Speed Review, PDF p. 54]]
[^eq-atomic-p55]: [[equity-investments-level-1-speed-review.pdf#page=55|Equity Investments Level I Speed Review, PDF p. 55]]
[^eq-atomic-p56]: [[equity-investments-level-1-speed-review.pdf#page=56|Equity Investments Level I Speed Review, PDF p. 56]]
[^eq-atomic-p57]: [[equity-investments-level-1-speed-review.pdf#page=57|Equity Investments Level I Speed Review, PDF p. 57]]
[^eq-atomic-p58]: [[equity-investments-level-1-speed-review.pdf#page=58|Equity Investments Level I Speed Review, PDF p. 58]]
[^eq-atomic-p59]: [[equity-investments-level-1-speed-review.pdf#page=59|Equity Investments Level I Speed Review, PDF p. 59]]
[^eq-atomic-p60]: [[equity-investments-level-1-speed-review.pdf#page=60|Equity Investments Level I Speed Review, PDF p. 60]]
[^eq-atomic-p61]: [[equity-investments-level-1-speed-review.pdf#page=61|Equity Investments Level I Speed Review, PDF p. 61]]
[^eq-atomic-p62]: [[equity-investments-level-1-speed-review.pdf#page=62|Equity Investments Level I Speed Review, PDF p. 62]]
[^eq-atomic-p63]: [[equity-investments-level-1-speed-review.pdf#page=63|Equity Investments Level I Speed Review, PDF p. 63]]
[^eq-atomic-p64]: [[equity-investments-level-1-speed-review.pdf#page=64|Equity Investments Level I Speed Review, PDF p. 64]]
[^eq-atomic-p65]: [[equity-investments-level-1-speed-review.pdf#page=65|Equity Investments Level I Speed Review, PDF p. 65]]
[^eq-atomic-p66]: [[equity-investments-level-1-speed-review.pdf#page=66|Equity Investments Level I Speed Review, PDF p. 66]]
[^eq-atomic-p67]: [[equity-investments-level-1-speed-review.pdf#page=67|Equity Investments Level I Speed Review, PDF p. 67]]
[^eq-atomic-p71]: [[equity-investments-level-1-speed-review.pdf#page=71|Equity Investments Level I Speed Review, PDF p. 71]]
[^eq-atomic-p72]: [[equity-investments-level-1-speed-review.pdf#page=72|Equity Investments Level I Speed Review, PDF p. 72]]
[^eq-atomic-p73]: [[equity-investments-level-1-speed-review.pdf#page=73|Equity Investments Level I Speed Review, PDF p. 73]]
[^eq-atomic-p74]: [[equity-investments-level-1-speed-review.pdf#page=74|Equity Investments Level I Speed Review, PDF p. 74]]
[^eq-atomic-p75]: [[equity-investments-level-1-speed-review.pdf#page=75|Equity Investments Level I Speed Review, PDF p. 75]]
[^eq-atomic-p76]: [[equity-investments-level-1-speed-review.pdf#page=76|Equity Investments Level I Speed Review, PDF p. 76]]
