---
id: proposal-equity-l1-security-market-indexes-enrichment
type: proposal
title: Equity Investments - Security Market Indexes Enrichment
target: "[[Equity - Security Market Indexes]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Equity Investments - Security Market Indexes Enrichment

## Rationale

The existing index notes are mostly definitions. The deck contains calculation formulas, index uses, weighting trade-offs, and rebalancing rules that should be retained.

## Exact proposed content

Enrich `Security Market Index`, `Index Divisor`, `Price Return Index`, and `Total Return Index`:

$$
V=\frac{\sum_{i=1}^{n}m_iP_i}{D}
$$

The divisor is chosen at inception to produce a convenient initial value. Add:

$$
PR_1=\frac{V_1-V_0}{V_0}=\sum_{i=1}^{n}w_iPR_i
$$

$$
TR_1=\frac{V_1-V_0+D_1}{V_0}=\sum_{i=1}^{n}w_iTR_i
$$

Because total return includes distributions, its value will exceed the price-return index over time under the slide's stated comparison.[^eq-idx-p21]

Enrich `Index Use` with gauges of market sentiment, benchmarks for active portfolios, proxies for measuring and modeling returns and systematic risk, model portfolios for index funds and ETFs, and proxies for asset classes in allocation models.[^eq-idx-p21]

Enrich the index-type notes:

- `Equity Index`: broad-market, multi-market, sector, and style indexes. The slide's multi-market fundamental approach weights securities within a country by market capitalization and countries by relative GDP.
- `Fixed-Income Index`: a broad universe across many dimensions, high turnover as securities mature, and dealer-market illiquidity.
- `Real Estate Index`: appraisal, repeat-sales, and REIT indexes.
- `Hedge Fund Index`: voluntary participation can create survivorship bias.
- `Commodity Index`: performance may differ materially from the underlying commodities.[^eq-idx-p22]

Enrich `Price-Weighted Index`: the index is the arithmetic average of security prices and can be replicated with an equal number of shares. It is simple, but high-priced securities have more influence. Adjust the divisor after a stock split to maintain the index level.[^eq-idx-p23]

Enrich `Market-Capitalization-Weighted Index`, `Float-Adjusted Market-Capitalization-Weighted Index`, and the free-float distinction. Market-cap weight equals the stock's market capitalization divided by total index market capitalization. The benefit is representation of the stock's actual market fraction; the disadvantage is greater influence from large-cap firms and a momentum tilt. Float adjustment uses shares available to the investing public; free-float adjustment further excludes shares unavailable to foreign investors.[^eq-idx-p24]

Enrich `Equal-Weighted Index`: each constituent has equal weight, the index return is the arithmetic mean of constituent holding-period returns, and replication uses equal dollar investments. It is simple but has small-cap bias and requires frequent rebalancing.[^eq-idx-p25]

Enrich `Fundamentally Weighted Index`: weights use company-size measures independent of security price, including book value, cash flow, revenue, earnings, dividends, and employees. The resulting index has a value tilt and may have a contrarian effect.[^eq-idx-p25]

Enrich `Index Rebalancing` and `Index Reconstitution`:

- Rebalancing adjusts constituent weights. Price-weighted indexes are not rebalanced; market-cap-weighted indexes largely rebalance themselves except for events such as mergers, acquisitions, and liquidations; equal-weighted indexes require the most frequent rebalancing.
- Reconstitution changes constituents when a security no longer meets the criteria and is replaced; it is part of the rebalancing cycle.[^eq-idx-p26]

## Review checklist

- [x] Pages 21-26 were visually inspected.
- [x] All three index formulas were checked against the rendered slides.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^eq-idx-p21]: [[equity-investments-level-1-speed-review.pdf#page=21|Equity Investments Level I Speed Review, PDF p. 21]]
[^eq-idx-p22]: [[equity-investments-level-1-speed-review.pdf#page=22|Equity Investments Level I Speed Review, PDF p. 22]]
[^eq-idx-p23]: [[equity-investments-level-1-speed-review.pdf#page=23|Equity Investments Level I Speed Review, PDF p. 23]]
[^eq-idx-p24]: [[equity-investments-level-1-speed-review.pdf#page=24|Equity Investments Level I Speed Review, PDF p. 24]]
[^eq-idx-p25]: [[equity-investments-level-1-speed-review.pdf#page=25|Equity Investments Level I Speed Review, PDF p. 25]]
[^eq-idx-p26]: [[equity-investments-level-1-speed-review.pdf#page=26|Equity Investments Level I Speed Review, PDF p. 26]]
