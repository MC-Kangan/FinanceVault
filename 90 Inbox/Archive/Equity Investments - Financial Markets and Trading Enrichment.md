---
id: proposal-equity-l1-financial-markets-trading-enrichment
type: proposal
title: Equity Investments - Financial Markets and Trading Enrichment
target: "[[Equity - Financial Markets and Trading]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Equity Investments - Financial Markets and Trading Enrichment

## Rationale

The current notes identify the market institutions and order types, but most omit the distinctions, mechanics, risks, and formulas retained by the review deck. This proposal adds only content visually verified on PDF pages 4-17.

## Exact proposed content

### Financial system and intermediaries

Enrich `Financial System Functions` with saving, borrowing, raising equity, managing risk, exchanging assets, and information-motivated trading. Add that the system establishes equilibrium required returns and supports allocational efficiency. Enrich `Market Regulation` with controlling fraud and agency problems, establishing standards and fairness, preventing undercapitalized firms from exploiting investors, and funding long-term liabilities. A well-functioning system is complete, operationally efficient, informationally efficient, and allocationally efficient.[^eq-mkt-p4]

Enrich `Broker`, `Dealer`, `Broker-Dealer`, and `Investment Bank`:

- A broker searches for counterparties and does not trade with the client; a block broker serves large traders.
- A dealer trades from inventory and provides liquidity. A broker-dealer may face a conflict between agency and principal roles.
- An investment bank advises issuers and arranges transactions.[^eq-mkt-p5]

Enrich `Exchange`, `Alternative Trading System`, `Securitizer`, `Arbitrageur`, `Depository Institution`, `Insurance Company`, and `Settlement and Custody`:

- Exchanges have regulatory authority; alternative trading systems, ECNs, and MTFs perform a trading function without that authority.
- Securitizers pool assets and sell securities backed by the pool.
- Arbitrageurs trade identical or similar instruments at different prices and help move liquidity across markets.
- Depository institutions, insurers, and settlement or custodial services perform the support roles shown in the deck.[^eq-mkt-p6]

### Primary markets and market organization

Enrich `Primary Market`, `Initial Public Offering`, `Seasoned Offering`, `Underwritten Offering`, and `Best-Efforts Offering`. Classify markets by delivery date, maturity, position or underlying, and capital flow. An IPO is the first public issue; a seasoned offering is a later issue. In an underwritten offering the bank guarantees the full issue, while in a best-efforts offering it acts as broker and has no obligation for unsold securities.[^eq-mkt-p7]

Enrich `Private Placement`, `Shelf Registration`, `Dividend Reinvestment Plan`, and `Rights Offering`:

- Private placements are sold to qualified investors.
- Shelf registration lets a seasoned issuer sell when capital is needed or market conditions are favorable.
- A dividend reinvestment plan reinvests dividends in newly issued shares.
- A rights offering lets existing shareholders buy new shares at a discount.[^eq-mkt-p8]

Enrich `Call Market` and `Continuous Market`. A call market gathers orders and selects one price that maximizes executable volume; matching is easier but occurs only at specified times. A continuous market permits trading whenever open, although counterparties arriving at different times may miss each other.[^eq-mkt-p9]

Enrich `Quote-Driven Market`, `Brokered Market`, `Order-Driven Market`, `Order Priority`, `Uniform Pricing`, and `Discriminatory Pricing`:

- Quote-driven or dealer markets are commonly OTC; brokered markets are useful for unique or illiquid instruments; order-driven markets match orders according to rules.
- Priority is price, then display, then time.
- Preserve the slide's three pricing labels: uniform, discriminatory, and derivative pricing.[^eq-mkt-p9][^eq-mkt-p10]

### Positions, short sales, and margin

Enrich `Long Position` and `Short Position`, and add the slide's option-exposure matrix: buying a call is long the option and long underlying exposure; selling a call is short both; buying a put is long the option but short underlying exposure; selling a put is short the option but long underlying exposure.[^eq-mkt-p12]

Enrich `Short Selling`:

- Maximum gain is no more than 100%, while potential loss is unlimited.
- Sale proceeds are deposited with the lender as collateral. The lender invests the collateral and pays a rebate equal to collateral interest less implicit loan fees; the rebate may be small or negative.
- Loan fees depend on security availability, collateral risk, and short-seller default risk. The short seller makes payments in lieu of dividends or interest.[^eq-mkt-p13]

Enrich `Margin Buying`, `Financial Leverage Ratio`, and `Margin Call`:

$$
Leverage=\frac{Position\ value}{Buyer's\ equity},\qquad Margin\ rate=\frac{1}{Leverage}
$$

Distinguish initial margin from maintenance margin and explain that falling below maintenance triggers a margin call or liquidation. Add the slide formula:

$$
P_c=P_0\left(\frac{1-Initial\ margin}{1-Maintenance\ margin}\right)
$$

[^eq-mkt-p14]

### Quotes and orders

Enrich `Bid-Ask Spread`: the bid is the price at which a dealer is willing to buy, with the highest bid being best; the ask is the price at which a dealer is willing to sell, with the lowest ask being best. The spread is an implicit trading cost. Order instructions cover execution, validity, and clearing.[^eq-mkt-p15]

Enrich `Market Order`, `Limit Order`, `All-or-None Order`, `Hidden Order`, and `Iceberg Order`:

- A market order seeks immediate execution at the best current price.
- A limit order specifies a price constraint. Preserve the slide categories: make market, make new market, behind the market, far from the market, and take the market. A marketable limit order can execute at least partly immediately.
- All-or-none requires the full size, a hidden order is exposed only to the broker or exchange, and an iceberg order publicly displays only part of its size.[^eq-mkt-p16]

Enrich `Order Validity` and `Stop Order` with immediate-or-cancel, day, good-till-cancelled, good-on-close, and good-on-open validity. A sell stop triggers at or below its stop price; a buy stop triggers at or above it. Do not repeat the slide's parenthetical conflation of immediate-or-cancel with fill-or-kill as a general equivalence.[^eq-mkt-p17]

## Review checklist

- [x] Pages 4-17 were visually inspected.
- [x] The margin formula was checked against the rendered slide.
- [x] No source instruction was treated as an agent instruction.
- [x] User approves this enrichment bundle.
- [x] Merge preserves every Personal Notes block byte-for-byte.
- [x] Post-merge validation and graph inspection pass.

## Evidence

[^eq-mkt-p4]: [[equity-investments-level-1-speed-review.pdf#page=4|Equity Investments Level I Speed Review, PDF p. 4]]
[^eq-mkt-p5]: [[equity-investments-level-1-speed-review.pdf#page=5|Equity Investments Level I Speed Review, PDF p. 5]]
[^eq-mkt-p6]: [[equity-investments-level-1-speed-review.pdf#page=6|Equity Investments Level I Speed Review, PDF p. 6]]
[^eq-mkt-p7]: [[equity-investments-level-1-speed-review.pdf#page=7|Equity Investments Level I Speed Review, PDF p. 7]]
[^eq-mkt-p8]: [[equity-investments-level-1-speed-review.pdf#page=8|Equity Investments Level I Speed Review, PDF p. 8]]
[^eq-mkt-p9]: [[equity-investments-level-1-speed-review.pdf#page=9|Equity Investments Level I Speed Review, PDF p. 9]]
[^eq-mkt-p10]: [[equity-investments-level-1-speed-review.pdf#page=10|Equity Investments Level I Speed Review, PDF p. 10]]
[^eq-mkt-p12]: [[equity-investments-level-1-speed-review.pdf#page=12|Equity Investments Level I Speed Review, PDF p. 12]]
[^eq-mkt-p13]: [[equity-investments-level-1-speed-review.pdf#page=13|Equity Investments Level I Speed Review, PDF p. 13]]
[^eq-mkt-p14]: [[equity-investments-level-1-speed-review.pdf#page=14|Equity Investments Level I Speed Review, PDF p. 14]]
[^eq-mkt-p15]: [[equity-investments-level-1-speed-review.pdf#page=15|Equity Investments Level I Speed Review, PDF p. 15]]
[^eq-mkt-p16]: [[equity-investments-level-1-speed-review.pdf#page=16|Equity Investments Level I Speed Review, PDF p. 16]]
[^eq-mkt-p17]: [[equity-investments-level-1-speed-review.pdf#page=17|Equity Investments Level I Speed Review, PDF p. 17]]
