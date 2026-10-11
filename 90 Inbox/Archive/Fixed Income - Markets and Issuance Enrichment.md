---
id: proposal-fi-l1-markets-issuance-enrichment
type: proposal
title: Fixed Income - Markets and Issuance Enrichment
target: "[[Fixed Income]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Fixed Income - Markets and Issuance Enrichment

## Rationale

The current nodes name market structures but omit issuance methods, funding alternatives, repo formulas, and public-sector bond distinctions. The merge will create `Fixed Income - Markets and Issuance` as a subtopic map.

## Exact proposed content

Enrich `Bond Classification` and `Fixed-Income Index`: classify bonds by issuer, credit quality, and maturity. Fixed-income indexes typically hold more constituents, rebalance more often, and use market value of outstanding debt as a common weighting basis; distinguish aggregate from narrower indexes.[^fi-mkt-p21][^fi-mkt-p22]

Enrich `Primary Bond Market`: public offerings may use firm-commitment or best-efforts underwriting, syndication, auctions, reopenings, and shelf registration; private placements restrict participation to selected investors. Enrich `Secondary Bond Market`: organized exchanges centralize trading, while OTC markets rely on dealers and bid/ask quotes; on-the-run sovereigns commonly have narrower spreads, while distressed debt may trade below par and provide equity-like returns.[^fi-mkt-p23][^fi-mkt-p24]

Create `Commercial Paper` and enrich `Short-Term Funding` and `Corporate Bond Funding`: nonfinancial companies use uncommitted or committed credit lines, revolving credit agreements, secured asset-based lending, factoring, and unsecured commercial paper. Investment-grade bonds are more bond-like, often unsecured with fewer restrictions and lower credit-spread share of YTM; high-yield bonds are more equity-like, often secured with more restrictions and a higher credit-spread share.[^fi-mkt-p25][^fi-mkt-p26]

Enrich bank funding and asset-backed commercial paper: banks use demand and savings deposits, negotiable or non-negotiable certificates of deposit, interbank funds, central-bank facilities, commercial paper, and ABCP. ABCP is an off-balance-sheet financing alternative in which a bank-sponsored SPE issues the paper, with the bank serving as sponsor and backup credit provider.[^fi-mkt-p27][^fi-mkt-p28]

Enrich `Repurchase Agreement` and add `Reverse Repurchase Agreement` as an alias or separate canonical node after alias validation. A repo is a security sale combined with an agreement to repurchase it later at a fixed price and is economically a collateralized loan; the seller is the cash borrower and retains economic exposure to the security. Overnight and term repos differ by maturity.[^fi-mkt-p29]

$$Purchase\ price_1=Purchase\ price_0\left(1+\frac{days}{360}\times repo\ rate\right)$$

$$Initial\ margin=\frac{Bond\ price_0}{Purchase\ price_0},\qquad Haircut=\frac{Bond\ price_0-Purchase\ price_0}{Bond\ price_0}$$

Repo rates tend to be higher for longer terms, lower-quality or less-liquid collateral, non-delivery of collateral, and lower borrower credit quality. Uses include financing security ownership, earning a short-term return, and borrowing securities for short sales; risks include default, collateral, margin, legal, netting, and settlement risk.[^fi-mkt-p30][^fi-mkt-p31]

Enrich `Public-Sector Bonds`: sovereign debt may be on-the-run or off-the-run, domestic or external, and carries rollover and currency risks. Single-price auctions give successful bidders one price, while multiple-price auctions use each accepted bid price. Agency/quasi-government, local-government general-obligation and revenue bonds, and supranational bonds have distinct issuers and repayment support.[^fi-mkt-p32][^fi-mkt-p33][^fi-mkt-p34]

## Navigation changes on merge

Create `Fixed Income - Markets and Issuance`, link it from `[[Fixed Income]]`, and organize the chapter under indexes/classification, primary/secondary markets, corporate and bank funding, repos, and public-sector issuance.

## Review checklist

- [x] PDF pages 21-34 were visually inspected.
- [x] Repo formulas and auction distinctions were checked visually.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^fi-mkt-p21]: [[fixed-income-level-1-speed-review.pdf#page=21|Fixed Income Level I Speed Review, PDF p. 21]]
[^fi-mkt-p22]: [[fixed-income-level-1-speed-review.pdf#page=22|Fixed Income Level I Speed Review, PDF p. 22]]
[^fi-mkt-p23]: [[fixed-income-level-1-speed-review.pdf#page=23|Fixed Income Level I Speed Review, PDF p. 23]]
[^fi-mkt-p24]: [[fixed-income-level-1-speed-review.pdf#page=24|Fixed Income Level I Speed Review, PDF p. 24]]
[^fi-mkt-p25]: [[fixed-income-level-1-speed-review.pdf#page=25|Fixed Income Level I Speed Review, PDF p. 25]]
[^fi-mkt-p26]: [[fixed-income-level-1-speed-review.pdf#page=26|Fixed Income Level I Speed Review, PDF p. 26]]
[^fi-mkt-p27]: [[fixed-income-level-1-speed-review.pdf#page=27|Fixed Income Level I Speed Review, PDF p. 27]]
[^fi-mkt-p28]: [[fixed-income-level-1-speed-review.pdf#page=28|Fixed Income Level I Speed Review, PDF p. 28]]
[^fi-mkt-p29]: [[fixed-income-level-1-speed-review.pdf#page=29|Fixed Income Level I Speed Review, PDF p. 29]]
[^fi-mkt-p30]: [[fixed-income-level-1-speed-review.pdf#page=30|Fixed Income Level I Speed Review, PDF p. 30]]
[^fi-mkt-p31]: [[fixed-income-level-1-speed-review.pdf#page=31|Fixed Income Level I Speed Review, PDF p. 31]]
[^fi-mkt-p32]: [[fixed-income-level-1-speed-review.pdf#page=32|Fixed Income Level I Speed Review, PDF p. 32]]
[^fi-mkt-p33]: [[fixed-income-level-1-speed-review.pdf#page=33|Fixed Income Level I Speed Review, PDF p. 33]]
[^fi-mkt-p34]: [[fixed-income-level-1-speed-review.pdf#page=34|Fixed Income Level I Speed Review, PDF p. 34]]
