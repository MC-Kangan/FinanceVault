---
id: proposal-fi-l1-markets-issuance-funding
type: proposal
title: Fixed Income Level 1 - Markets Issuance and Funding
target: "[[Fixed Income]]"
change_type: topic-expansion
status: merged
tags:
  - cfa/level-1
---

# Fixed Income Level 1 - Markets, Issuance, and Funding

## Rationale

Create a navigable market-structure layer linking instrument classification, issuance, trading, issuer funding choices, repo financing, and public-sector bonds.

## Proposed canonical concepts

### `Bond Classification`

- Classify bonds by issuer, credit quality, and maturity. Government debt includes bills, notes, and bonds; credit quality separates investment grade from speculative grade; maturity choice helps issuers match funding needs and investors match horizons.[^fi-markets-p21]

Aliases to review: `Fixed-Income Classification`, `债券分类`.

### `Fixed-Income Index`

- Fixed-income indices generally contain more securities and turn over more frequently than equity indices, and most are weighted by the market value of outstanding debt.[^fi-markets-p22]
- Separate broad aggregate indices from narrower indices selected by criteria such as sector, credit quality, geography, or ESG attributes.[^fi-markets-p22]

Aliases to review: `Bond Index`, `Fixed Income Index`, `债券指数`.

### `Primary Bond Market`

- Define the primary market as first sale by the issuer. Compare public and private offerings, underwritten and best-efforts offerings, syndication, auctions, reopenings, and shelf registration.[^fi-markets-p23]

Aliases to review: `Primary Market`, `Bond Issuance`, `债券一级市场`.

### `Secondary Bond Market`

- Define subsequent trading among investors and contrast organized exchanges with dealer-based OTC markets. More liquid issues, including on-the-run sovereigns and frequent issuers, tend to have narrower bid-ask spreads.[^fi-markets-p24]
- Distressed debt can remain tradeable at prices far below par and may produce equity-like return behavior.[^fi-markets-p24]

Aliases to review: `Secondary Market`, `Bond Trading`, `债券二级市场`.

### `Short-Term Funding`

- For nonfinancial firms, distinguish uncommitted and committed credit lines, revolving credit, secured asset-based loans, factoring, and commercial paper; commercial paper is unsecured and commonly exposes the issuer to rollover risk.[^fi-markets-p25]
- For banks, cover retail and commercial deposits, negotiable and non-negotiable certificates of deposit, interbank funds, central-bank facilities, commercial paper, and asset-backed commercial paper.[^fi-markets-p27][^fi-markets-p28]

Aliases to review: `Short-Term Financing`, `Money Market Funding`, `短期融资`, `ABCP`.

### `Corporate Bond Funding`

- Compare investment-grade and high-yield long-term debt: high-yield cash flows are more equity-like, secured structures and restrictive covenants are more common, and a larger share of YTM reflects credit spread.[^fi-markets-p26]

Aliases to review: `Long-Term Corporate Funding`, `Corporate Debt Funding`, `公司长期融资`.

### `Repurchase Agreement`

- Define a repo as a security sale combined with an agreement to repurchase it later at a specified price. Economically, it is collateralized borrowing; the cash lender's perspective is a reverse repo.[^fi-markets-p29]

$$
P_t=P_0\left(1+\frac{t}{360}\times r_{\text{repo}}\right)
$$

$$
\text{Initial margin}=\frac{\text{Collateral value}_0}{P_0}
$$

$$
\text{Haircut}=\frac{\text{Collateral value}_0-P_0}{\text{Collateral value}_0}
$$

[^fi-markets-p30]

![[source-fi-l1-speed-review-p029-repo-mechanics.png]]

Figure: At initiation the cash borrower delivers the security and receives cash; at maturity those flows reverse at the repurchase price.[^fi-markets-p29]

- Cover repo uses for financing security ownership, earning secured short-term income, and borrowing securities for short sales. Capture default, collateral, margining, legal, netting, and settlement risk, plus the operational role of a triparty agent.[^fi-markets-p31]

Aliases to review: `Repo`, `Reverse Repo`, `回购协议`.

### `Sovereign and Non-Sovereign Bonds`

- Sovereign bonds are national-government obligations supported by taxing authority; distinguish on-the-run and off-the-run issues, domestic and external debt, currency risk, and the maturity tradeoff between borrowing cost and rollover risk.[^fi-markets-p32]
- Compare single-price and multiple-price auctions and retain the role of noncompetitive and competitive bids.[^fi-markets-p33]
- Distinguish quasi-government or agency bonds, local-government bonds, and supranational bonds; local-government debt includes general-obligation and revenue bonds.[^fi-markets-p34]

Aliases to review: `Government Bonds`, `Sovereign Bonds`, `Public Sector Bonds`, `政府债券`.

## Link and alias changes

- `Repurchase Agreement` should connect to proposed `Money Market Yield Measures` and `Short-Term Funding`.
- `Sovereign and Non-Sovereign Bonds` should connect to proposed `Sovereign Credit Analysis` and `Municipal Credit Analysis`.
- `Corporate Bond Funding` should connect to existing `Credit Risk` and `Corporate Credit Analysis`.
- Proposed aliases remain unregistered until collision validation passes.

## Review checklist

- [x] Claims and formulas were visually checked against pages 21-34.
- [x] Proposed repo figure is legible and page-addressable.
- [x] Existing canonical concepts were not edited.
- [ ] User approves concept boundaries and aliases.
- [ ] Approved concepts are created through the merge workflow.

## Evidence

[^fi-markets-p21]: [[fixed-income-level-1-speed-review.pdf#page=21|Fixed Income Level I Speed Review, PDF p. 21]]
[^fi-markets-p22]: [[fixed-income-level-1-speed-review.pdf#page=22|Fixed Income Level I Speed Review, PDF p. 22]]
[^fi-markets-p23]: [[fixed-income-level-1-speed-review.pdf#page=23|Fixed Income Level I Speed Review, PDF p. 23]]
[^fi-markets-p24]: [[fixed-income-level-1-speed-review.pdf#page=24|Fixed Income Level I Speed Review, PDF p. 24]]
[^fi-markets-p25]: [[fixed-income-level-1-speed-review.pdf#page=25|Fixed Income Level I Speed Review, PDF p. 25]]
[^fi-markets-p26]: [[fixed-income-level-1-speed-review.pdf#page=26|Fixed Income Level I Speed Review, PDF p. 26]]
[^fi-markets-p27]: [[fixed-income-level-1-speed-review.pdf#page=27|Fixed Income Level I Speed Review, PDF p. 27]]
[^fi-markets-p28]: [[fixed-income-level-1-speed-review.pdf#page=28|Fixed Income Level I Speed Review, PDF p. 28]]
[^fi-markets-p29]: [[fixed-income-level-1-speed-review.pdf#page=29|Fixed Income Level I Speed Review, PDF p. 29]]
[^fi-markets-p30]: [[fixed-income-level-1-speed-review.pdf#page=30|Fixed Income Level I Speed Review, PDF p. 30]]
[^fi-markets-p31]: [[fixed-income-level-1-speed-review.pdf#page=31|Fixed Income Level I Speed Review, PDF p. 31]]
[^fi-markets-p32]: [[fixed-income-level-1-speed-review.pdf#page=32|Fixed Income Level I Speed Review, PDF p. 32]]
[^fi-markets-p33]: [[fixed-income-level-1-speed-review.pdf#page=33|Fixed Income Level I Speed Review, PDF p. 33]]
[^fi-markets-p34]: [[fixed-income-level-1-speed-review.pdf#page=34|Fixed Income Level I Speed Review, PDF p. 34]]
