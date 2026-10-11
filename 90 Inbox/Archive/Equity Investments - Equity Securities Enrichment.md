---
id: proposal-equity-l1-equity-securities-enrichment
type: proposal
title: Equity Investments - Equity Securities Enrichment
target: "[[Equity - Equity Securities]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Equity Investments - Equity Securities Enrichment

## Rationale

The existing notes name the security types but omit many shareholder rights, preference-share features, depositary-receipt distinctions, and relative-risk comparisons in the review deck.

## Exact proposed content

Enrich `Common Share`, `Callable Common Share`, and `Putable Common Share`:

- Common shares represent ownership and have a residual claim on net assets in liquidation. Dividends are not contractual obligations.
- Common shareholders participate in governance through voting. Statutory voting gives one vote per share; cumulative voting multiplies shares owned by the number of directors being elected; proxy voting delegates the vote.
- Companies may issue classes with different rights. A callable common share lets the issuer buy it back; a putable common share lets its holder sell it back to the issuer.[^eq-sec-p38]

Enrich `Preferred Share`, `Cumulative Preferred Share`, `Participating Preferred Share`, and `Convertible Preferred Share`:

- Preferred shares rank ahead of common shares for dividends and liquidation distributions.
- Debt-like features in the slide are fixed dividends, typically no voting rights, no participation in operating performance, and callable or putable features. Equity-like features are possible perpetuity and non-contractual dividends.
- Cumulative shares accrue unpaid dividends; participating shares may receive the standard preferred dividend plus an additional dividend; convertible shares can be exchanged for a specified number of common shares.
- The slide associates convertible preferred shares with a higher dividend and less price volatility than the underlying common shares.[^eq-sec-p39]

Enrich `Private Equity` with the slide's characteristics: no active secondary market, less transparency than public securities, more ability to focus on long-term prospects without public short-term pressure, lower costs, and potentially greater investor return if the firm goes public. Preserve the already linked venture-capital, leveraged-buyout, and PIPE categories.[^eq-sec-p40]

Enrich `Depositary Receipt`: a DR represents ownership in a foreign company and its price is affected by the price drivers of the underlying shares. A basket of listed DRs is an ETF representing a DR portfolio.[^eq-sec-p40]

Enrich `Sponsored Depositary Receipt`, `Unsponsored Depositary Receipt`, `American Depositary Receipt`, and `Global Depositary Receipt`:

- The foreign company participates directly in a sponsored DR issuance and investors have the same rights as direct common shareholders.
- The foreign company does not participate in an unsponsored issue; investors receive dividends but the DR issuer holds the voting rights.
- An ADR is US-dollar denominated and trades like common stock in the United States; a GDR is issued outside the company's home country and outside the United States.
- Retain the slide's ADR comparison: Level I does not raise capital and trades OTC with low listing fees and no size or earnings requirement; Levels II and III trade on exchanges with high listing fees and size or earnings requirements; Level III raises capital; Rule 144A raises capital through private offerings with low fees and no size or earnings requirement.[^eq-sec-p41]

Enrich relative-risk and value notes:

- Preferred shares are less risky than common shares; putable shares are less risky than callable or non-callable shares; cumulative or participating preferred shares are less risky than non-cumulative or non-participating shares under the slide's comparisons.
- `Return on Equity` is used to assess whether management uses equity capital efficiently to generate profit, and `Cost of Equity` proxies the investor's minimum required return.
- `Book Value of Equity` equals assets minus liabilities; `Market Value of Equity` equals price times shares outstanding. They are rarely equal. Management directly affects book value but only indirectly affects market value.[^eq-sec-p42]

## Review checklist

- [x] Pages 38-42 were visually inspected.
- [x] The ADR comparison table was transcribed from the rendered slide.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^eq-sec-p38]: [[equity-investments-level-1-speed-review.pdf#page=38|Equity Investments Level I Speed Review, PDF p. 38]]
[^eq-sec-p39]: [[equity-investments-level-1-speed-review.pdf#page=39|Equity Investments Level I Speed Review, PDF p. 39]]
[^eq-sec-p40]: [[equity-investments-level-1-speed-review.pdf#page=40|Equity Investments Level I Speed Review, PDF p. 40]]
[^eq-sec-p41]: [[equity-investments-level-1-speed-review.pdf#page=41|Equity Investments Level I Speed Review, PDF p. 41]]
[^eq-sec-p42]: [[equity-investments-level-1-speed-review.pdf#page=42|Equity Investments Level I Speed Review, PDF p. 42]]
