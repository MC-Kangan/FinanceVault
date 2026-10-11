---
id: proposal-equity-l1-equity-valuation-enrichment
type: proposal
title: Equity Investments - Equity Valuation Enrichment
target: "[[Equity - Equity Valuation]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Equity Investments - Equity Valuation Enrichment

## Rationale

The current valuation notes name models but often omit their formulas, model-selection structure, assumptions, comparative-multiple mechanics, and asset-based suitability tests.

## Exact proposed content

Enrich `Equity Valuation Model` with three families: present-value models (DDM, FCFE, FCFF, residual income), market-multiple models (P/E, P/B, P/S, P/CF, and enterprise-value multiples), and asset-based valuation.[^eq-val-p71]

Enrich `Cash Dividend`, `Share Repurchase`, `Stock Dividend`, `Stock Split`, and `Ex-Dividend Date`: a cash dividend distributes cash; a special dividend is irregular or supplements the regular dividend. The sequence is declaration, ex-dividend, holder-of-record, and payment date. The ex-date is the first day the share trades without the dividend; the holder-of-record date is typically one or two business days later in the slide. A repurchase can be viewed as equivalent to a cash dividend; a stock dividend distributes additional shares; distinguish stock splits and reverse splits.[^eq-val-p72]

Enrich `Dividend Discount Model`:

$$
V_0=\sum_{i=1}^{\infty}\frac{D_i}{(1+r)^i}
$$

For a finite horizon:

$$
V_0=\frac{D_1}{(1+r)}+\frac{D_2}{(1+r)^2}+\cdots+\frac{D_n}{(1+r)^n}+\frac{P_n}{(1+r)^n}
$$

[^eq-val-p73]

Enrich `Gordon Growth Model` and `Sustainable Growth Rate`:

$$
V_0=\frac{D_1}{r-g},\qquad g=Retention\ rate\times ROE=(1-Payout\ ratio)\times ROE
$$

Assume perpetual constant dividend growth and $g<r$.[^eq-val-p73]

Enrich `Two-Stage Dividend Discount Model`: a finite high-growth period is followed by perpetual sustainable growth.

$$
V_0=\sum_{i=1}^{n}\frac{D_0(1+g_h)^i}{(1+r)^i}+\frac{D_{n+1}/(r-g_s)}{(1+r)^n}
$$

Enrich `Preferred Stock Valuation` with $V_0=D/r$.[^eq-val-p73]

Enrich `Free Cash Flow to Equity`: intrinsic equity value is the present value of expected FCFE, which measures dividend-paying capacity and can value a non-dividend-paying stock.

$$
V_0=\sum_{t=1}^{\infty}\frac{FCFE_t}{(1+r)^t}
$$

[^eq-val-p74]

Enrich `Price Multiple`, `Trailing Price Multiple`, and `Leading Price Multiple`: compare price with a monetary flow or value, using a similar company or industry average or median as benchmark. The slide lists P/E, P/B, P/S, and P/CF. Trailing multiples use current or trailing denominator values such as $P_0/E_0$; leading multiples use forward values such as $P_0/E_1$.[^eq-val-p74]

Enrich `Justified Price-to-Earnings Ratio` and `Price-to-Earnings Ratio`:

$$
\frac{P_0}{E_1}=\frac{D_1/E_1}{r-g}=\frac{1-b}{r-g}
$$

$$
\frac{P_0}{E_0}=\frac{D_1/E_0}{r-g}=\frac{(1-b)(1+g)}{r-g}
$$

P/E is inversely related to required return and positively related to growth; the relationship with payout is ambiguous. Multiples enable cross-sectional and time-series comparisons and are popular, but may conflict with DCF conclusions, lose comparability under differing accounting methods, and be distorted for cyclical companies by current conditions.[^eq-val-p75]

Enrich `Enterprise Value` and `Enterprise Value to EBITDA`:

$$
EV/EBITDA=\frac{Enterprise\ value}{EBITDA}
$$

$$
Enterprise\ value=Market\ value\ of\ common\ stock+Market\ value\ of\ preferred\ stock+Market\ value\ of\ debt-Cash-Cash\ equivalents
$$

EV is often viewed as takeover cost and is useful for comparing companies with materially different capital structures.[^eq-val-p76]

Enrich `Asset-Based Valuation`:

$$
Market\ value\ of\ equity=Market\ value\ of\ assets-Market\ value\ of\ liabilities
$$

It is appropriate for primarily tangible short-term assets, assets with ready market values, private firms, or liquidation. It is inappropriate when market values are hard to determine, fair and book values differ substantially, it would understate company value as a floor, or the environment is hyperinflationary.[^eq-val-p76]

## Review checklist

- [x] Pages 71-76 were visually inspected.
- [x] Every DDM, FCFE, P/E, EV, and asset-based formula was checked visually.
- [x] No valuation content was added beyond the slide deck.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes and passes validation.

## Evidence

[^eq-val-p71]: [[equity-investments-level-1-speed-review.pdf#page=71|Equity Investments Level I Speed Review, PDF p. 71]]
[^eq-val-p72]: [[equity-investments-level-1-speed-review.pdf#page=72|Equity Investments Level I Speed Review, PDF p. 72]]
[^eq-val-p73]: [[equity-investments-level-1-speed-review.pdf#page=73|Equity Investments Level I Speed Review, PDF p. 73]]
[^eq-val-p74]: [[equity-investments-level-1-speed-review.pdf#page=74|Equity Investments Level I Speed Review, PDF p. 74]]
[^eq-val-p75]: [[equity-investments-level-1-speed-review.pdf#page=75|Equity Investments Level I Speed Review, PDF p. 75]]
[^eq-val-p76]: [[equity-investments-level-1-speed-review.pdf#page=76|Equity Investments Level I Speed Review, PDF p. 76]]
