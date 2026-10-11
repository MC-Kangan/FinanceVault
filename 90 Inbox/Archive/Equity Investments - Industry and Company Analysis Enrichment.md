---
id: proposal-equity-l1-industry-company-analysis-enrichment
type: proposal
title: Equity Investments - Industry and Company Analysis Enrichment
target: "[[Equity - Industry and Company Analysis]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Equity Investments - Industry and Company Analysis Enrichment

## Rationale

This is the largest gap in the current Equity notes. The deck contains a complete research, business-model, leverage, industry-analysis, strategy, and forecasting workflow that should remain searchable at atomic concept level.

## Exact proposed content

### Research, business model, revenue, and cost

Enrich `Equity Research Report`: a company report combines company and industry analysis with valuation and a recommendation. A sell-side initial report is extensive and aimed at readers unfamiliar with the issuer; later reports are shorter updates, often around quarterly results, for an already familiar audience.[^eq-co-p45]

Enrich `Business Model`, `Bottom-Up Forecasting`, and `Top-Down Forecasting`. Determining the business model is the first step because it summarizes drivers of financial results and position. Information sources are issuer sources, public third-party sources, proprietary third-party sources, and proprietary primary research. Bottom-up revenue decomposes volume and price or product, segment, and geography; top-down uses market share, addressable market or market size, and GDP growth. The approaches may be combined.[^eq-co-p46]

Enrich `Pricing Power`: the ability to set prices and other economic terms without reducing volume depends on market structure and competitive position. Price-taker conditions include little differentiation, low entry barriers, substitutes, low loyalty, and low switching costs. Pricing power is associated with differentiation, barriers, few economical substitutes, switching costs, and retention. Assess it using margins as well as price history.[^eq-co-p47]

Enrich `Cost Structure`: operating costs cover acquisition, production, sale, improvement, delivery, management, and compliance; classify them by output behavior, nature, or function. Investing costs acquire or produce long-term tangible and intangible assets; financing costs are payments to debt and equity investors.[^eq-co-p48]

Enrich `Economies of Scale` and `Economies of Scope`: scale lowers unit cost as output grows, commonly by spreading fixed costs, though bargaining power may also lower variable cost. Scope lowers unit cost as product or business lines grow by sharing costs.[^eq-co-p49]

Enrich `Cash Conversion Cycle` and `Sources and Uses of Capital`: a shorter cash-conversion cycle reduces external financing needs; negative working capital makes suppliers a financing source. Sources include operating cash flow and negative working capital, debt issuance, equity issuance, and asset disposals. Uses include cash and investments on hand, positive working capital, capital expenditures and intangibles, acquisitions, debt repayment, dividends, and repurchases.[^eq-co-p50]

### Returns and leverage

Enrich `Return on Invested Capital`, `Return on Assets`, `Return on Equity`, and `DuPont Analysis`: compare long-run invested-capital returns with investors' required returns; ROIC and ROA are unlevered measures augmented by financial leverage; ROE is the comprehensive levered profitability measure. Preserve:

$$
ROE=Net\ profit\ margin\times Total\ asset\ turnover\times Equity\ multiplier
$$

Add the operating-income bridge $Sales=PQ$, variable cost $=VQ$, contribution $=Q(P-V)$, operating income $=Q(P-V)-F$, and, assuming no tax, net income $=Q(P-V)-F-I$.[^eq-co-p51]

Enrich `Operating Risk`, `Operating Leverage`, and `Degree of Operating Leverage`:

$$
DOL=\frac{\%\Delta EBIT}{\%\Delta Q}
=\frac{\Delta EBIT/EBIT}{\Delta Q/Q}
=\frac{Q(P-V)}{Q(P-V)-F}
=\frac{EBIT+F}{EBIT}
$$

Operating risk is EBIT sensitivity to units sold and rises as fixed operating cost increases relative to variable cost; fixed operating cost creates operating leverage.[^eq-co-p52]

Enrich `Financial Risk`, `Degree of Financial Leverage`, `Total Leverage`, and `Degree of Total Leverage`:

$$
DFL=\frac{\%\Delta NI}{\%\Delta EBIT}
=\frac{\Delta NI/NI}{\Delta EBIT/EBIT}
=\frac{Q(P-V)-F}{Q(P-V)-F-I}
=\frac{EBIT}{EBIT-I}
$$

$$
DTL=DFL\times DOL
=\frac{\%\Delta NI}{\%\Delta Q}
=\frac{Q(P-V)}{Q(P-V)-F-I}
=\frac{EBIT+F}{EBIT-I}
$$

Financial risk comes from how operations are financed and rises with fixed-cost financial obligations; fixed financial cost creates financial leverage.[^eq-co-p53]

### Industry structure and strategy

Enrich `Industry Analysis`: structural differences drive profitability differences. Industry and competitive forces can act as a ceiling, not a floor, on company returns; competition pulls profitability toward an industry base rate. Industry analysis sharpens forecasts and can identify overlooked candidates.[^eq-co-p54]

Enrich `Industry Classification`: government schemes group by production characteristics but may update slowly. Commercial schemes include GICS, ICB, and TRBC; they are global, reviewed at least annually, and hierarchical from sub-industry to industry to industry group to sector. GICS and ICB cover public companies; the slide states TRBC also covers private companies, non-profits, and government entities. Alternative grouping uses geography, country, business-cycle sensitivity, statistical similarity, or ESG characteristics.[^eq-co-p55][^eq-co-p56]

Enrich `Industry Survey`, `Market Share`, `Industry Concentration`, and `Herfindahl-Hirschman Index`: measure size with annual sales from a product or customer perspective; measure growth with annual rates or CAGR; distinguish growth from mature industries and assess cycle sensitivity through discretionary demand, pricing, interest-rate exposure, and durable versus recurring purchases. Use a time series of the ROIC distribution for profitability where available. Treat market shares as ranges; rising concentration is associated with lower competitive intensity and higher profitability. Preserve $HHI=\sum s_i^2$.[^eq-co-p57][^eq-co-p58]

Enrich `Porter's Five Forces` and `PESTLE Analysis`: the five forces are rivalry, new entrants, substitutes, supplier power, and buyer power, used to assess long-run profitability. PESTLE covers political, economic, social, technological, legal, and environmental influences and focuses more on growth and market-share dynamics.[^eq-co-p59]

Enrich `Cost Leadership`, `Differentiation Strategy`, and `Focus Strategy` with their source drivers and risks. Cost leadership uses scale, input access, control, aggressive volume pricing, low-cost distribution, and scope; risks include inflation, discipline loss, premiumization, and technology. Differentiation uses brand, service, proprietary channels or IP, quality, features, experience, premium pricing, and integration; risks include imitation, excessive premium, sophisticated buyers, and limited share. Focus targets a particular group using cost or differentiation elements; risks include narrowing differences, larger rivals' pricing, and sophisticated buyers.[^eq-co-p60][^eq-co-p61]

### Forecasting

Enrich `Financial Statement Forecasting`: forecast drivers where possible for explanation and accuracy, individual lines for less material items, summary measures for efficiency at the cost of transparency, and ad hoc objects for items not yet in historical statements.[^eq-co-p61]

Enrich `Historical Forecasting`, `Base-Rate Forecasting`, `Convergence Forecasting`, and `Management Guidance`:

- Historical results fit stable industries, low-cycle-sensitivity companies, immaterial items, and items without a distinct analyst view; an over-the-cycle average or median can suit a cyclical company's multi-year forecast.
- Base-rate convergence uses a long-period industry or peer average or median. It fits established industries and maturing smaller firms, but not changing industries, highly cyclical firms where the long run obscures the outlook, or dominant leaders.
- Guidance is commonly a range embedding sub-forecasts and assumptions; use it when available and when management has a reliable record. Discretionary analyst forecasts are common for cyclical firms, firms without comparables or guidance, and firms undergoing fundamental change.[^eq-co-p62][^eq-co-p63][^eq-co-p64]

Enrich `Revenue Forecasting`, `Expense Forecasting`, `Capital Expenditure Forecasting`, and `Scenario Analysis`: top-down revenue uses GDP-relative growth, market growth, and share; bottom-up uses volume and price, segments, capacity, or yield. Exclude non-recurring items. Forecast cost of sales through gross margin while considering hedges and business-model differences; model variable SG&A as a percentage of sales and working capital through efficiency ratios. Split maintenance capex from growth capex. Project capital structure with leverage ratios, historical practice, financial strategy, and capex needs. The final forecast adds different outcomes based on key risks and their likelihood.[^eq-co-p65][^eq-co-p66][^eq-co-p67]

## Review checklist

- [x] Pages 45-67 were visually inspected.
- [x] DOL, DFL, DTL, ROE, operating-income, and HHI formulas were checked visually.
- [x] No forecasting rule was added beyond the source.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^eq-co-p45]: [[equity-investments-level-1-speed-review.pdf#page=45|Equity Investments Level I Speed Review, PDF p. 45]]
[^eq-co-p46]: [[equity-investments-level-1-speed-review.pdf#page=46|Equity Investments Level I Speed Review, PDF p. 46]]
[^eq-co-p47]: [[equity-investments-level-1-speed-review.pdf#page=47|Equity Investments Level I Speed Review, PDF p. 47]]
[^eq-co-p48]: [[equity-investments-level-1-speed-review.pdf#page=48|Equity Investments Level I Speed Review, PDF p. 48]]
[^eq-co-p49]: [[equity-investments-level-1-speed-review.pdf#page=49|Equity Investments Level I Speed Review, PDF p. 49]]
[^eq-co-p50]: [[equity-investments-level-1-speed-review.pdf#page=50|Equity Investments Level I Speed Review, PDF p. 50]]
[^eq-co-p51]: [[equity-investments-level-1-speed-review.pdf#page=51|Equity Investments Level I Speed Review, PDF p. 51]]
[^eq-co-p52]: [[equity-investments-level-1-speed-review.pdf#page=52|Equity Investments Level I Speed Review, PDF p. 52]]
[^eq-co-p53]: [[equity-investments-level-1-speed-review.pdf#page=53|Equity Investments Level I Speed Review, PDF p. 53]]
[^eq-co-p54]: [[equity-investments-level-1-speed-review.pdf#page=54|Equity Investments Level I Speed Review, PDF p. 54]]
[^eq-co-p55]: [[equity-investments-level-1-speed-review.pdf#page=55|Equity Investments Level I Speed Review, PDF p. 55]]
[^eq-co-p56]: [[equity-investments-level-1-speed-review.pdf#page=56|Equity Investments Level I Speed Review, PDF p. 56]]
[^eq-co-p57]: [[equity-investments-level-1-speed-review.pdf#page=57|Equity Investments Level I Speed Review, PDF p. 57]]
[^eq-co-p58]: [[equity-investments-level-1-speed-review.pdf#page=58|Equity Investments Level I Speed Review, PDF p. 58]]
[^eq-co-p59]: [[equity-investments-level-1-speed-review.pdf#page=59|Equity Investments Level I Speed Review, PDF p. 59]]
[^eq-co-p60]: [[equity-investments-level-1-speed-review.pdf#page=60|Equity Investments Level I Speed Review, PDF p. 60]]
[^eq-co-p61]: [[equity-investments-level-1-speed-review.pdf#page=61|Equity Investments Level I Speed Review, PDF p. 61]]
[^eq-co-p62]: [[equity-investments-level-1-speed-review.pdf#page=62|Equity Investments Level I Speed Review, PDF p. 62]]
[^eq-co-p63]: [[equity-investments-level-1-speed-review.pdf#page=63|Equity Investments Level I Speed Review, PDF p. 63]]
[^eq-co-p64]: [[equity-investments-level-1-speed-review.pdf#page=64|Equity Investments Level I Speed Review, PDF p. 64]]
[^eq-co-p65]: [[equity-investments-level-1-speed-review.pdf#page=65|Equity Investments Level I Speed Review, PDF p. 65]]
[^eq-co-p66]: [[equity-investments-level-1-speed-review.pdf#page=66|Equity Investments Level I Speed Review, PDF p. 66]]
[^eq-co-p67]: [[equity-investments-level-1-speed-review.pdf#page=67|Equity Investments Level I Speed Review, PDF p. 67]]
