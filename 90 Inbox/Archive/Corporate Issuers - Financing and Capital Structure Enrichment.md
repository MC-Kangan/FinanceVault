---
id: proposal-corporate-issuers-l1-financing-capital-structure-enrichment
type: proposal
title: Corporate Issuers - Financing and Capital Structure Enrichment
target: "[[Corporate Issuers - Financing and Capital Structure]]"
change_type: concept-enrichment-bundle
status: merged
tags:
  - cfa/level-1
---

# Corporate Issuers - Financing and Capital Structure Enrichment

## Rationale

The current financing notes omit the complete WACC formula, weight hierarchy, cost drivers, life-cycle comparison, MM equations, and the value bridges behind trade-off and pecking-order theories.

## Exact proposed content

### WACC and component costs

Enrich `Weighted Average Cost of Capital` with:

$$
WACC=w_d r_d(1-T)+w_{ps}r_{ps}+w_{ce}r_{ce}
$$

Use market-value weights when available. Otherwise use target capital-structure weights; if those are unavailable, estimate them from the current structure, trends or management statements, or averages for comparable companies. $T$ is the marginal tax rate, $r_d$ the before-tax marginal cost of debt, and $r_{ps}$ and $r_{ce}$ the marginal costs of preferred and common equity.[^ci-fin-p34]

Enrich `Cost of Debt` with the source convention:

$$
After\text{-}tax\ cost\ of\ debt=YTM(1-T)
$$

Make clear that the tax adjustment applies only to debt in the WACC formula and that the relevant costs are marginal, not historical coupon rates or accounting costs.[^ci-fin-p34]

Enrich `Cost of Preferred Stock`, `Cost of Equity`, and `Target Capital Structure` with the same marginal-cost and weight hierarchy so the component notes can be reached independently without losing the full WACC framework.[^ci-fin-p34]

### Drivers of financing cost and capital structure

Add the source's top-down and issuer-specific drivers to the component-cost notes. Economic and industry conditions affect all issuers. Issuer-specific factors include collateral and asset type, sales risk, profitability risk, operating leverage, financial leverage, and interest coverage. More stable, predictable, growing revenue reduces sales risk; a larger fixed-cost share raises operating leverage and profitability risk.[^ci-fin-p35]

Enrich `Target Capital Structure` with external factors—capital-market and economic conditions, industry characteristics, and regulation—and internal factors—business model, asset ownership, life-cycle stage, cash flow, and profitability. Capital-intensive businesses tend toward more leverage; capital-light businesses toward less.[^ci-fin-p36]

Add the source life-cycle comparison: start-ups have beginning revenue growth, negative cash flow, high business risk, little or no debt availability, and rely on leases or convertible/secured financing; growth firms have rising revenue and cash flow, medium risk, and rising debt availability; mature firms have slowing growth, stable cash flow, low risk, high debt availability, and can use unsecured debt.[^ci-fin-p36]

### Modigliani-Miller framework

Enrich `Modigliani-Miller Theory` with its assumptions: homogeneous expected cash flows; investors can borrow and lend at the risk-free rate; perfect capital markets with no transaction, bankruptcy, or agency costs and symmetric information; and independence of financing and investment decisions.[^ci-fin-p36]

Enrich `Modigliani-Miller Proposition I` with separate no-tax and tax cases:

$$
V_L=V_U \qquad \text{(without taxes)}
$$

$$
V_L=V_U+TD \qquad \text{(with taxes)}
$$

Without taxes, leverage does not change firm value. With corporate taxes, debt adds the present value of the interest tax shield under the source assumptions.[^ci-fin-p37]

Enrich `Modigliani-Miller Proposition II` with:

$$
r_e=r_0+(r_0-r_d)\frac{D}{E} \qquad \text{(without taxes)}
$$

$$
r_e=r_0+(r_0-r_d)(1-T)\frac{D}{E} \qquad \text{(with taxes)}
$$

Without taxes, the increase in the required return on equity exactly offsets cheaper debt and WACC remains constant. With taxes, the equity-cost slope is reduced by $(1-T)$ and WACC falls as leverage adds a tax shield in the simplified model.[^ci-fin-p37]

### Distress, agency, information, and financing hierarchy

Enrich `Cost of Financial Distress` with direct costs—legal and administrative cash expenses of bankruptcy—and indirect costs, including forgone investments, reduced ability to conduct business, and agency costs.[^ci-fin-p38]

Enrich `Static Trade-Off Theory` with:

$$
V_L=V_U+TD-PV(Costs\ of\ financial\ distress)
$$

The optimal leverage balances the marginal tax-shield benefit against the expected present value of distress costs; firm value rises and then falls as excessive leverage makes distress costs dominate.[^ci-fin-p38]

Enrich `Agency Cost of Equity` and `Free Cash Flow Hypothesis`: greater debt can reduce agency costs of equity by committing cash to debt service, reducing free cash flow under managerial discretion and limiting opportunities to misuse it.[^ci-fin-p39]

Enrich `Asymmetric Information Cost`: managers know more about performance and prospects than owners and creditors; greater asymmetry increases the returns demanded by both debt and equity suppliers.[^ci-fin-p39]

Enrich `Pecking Order Theory` with the source financing hierarchy:

$$
Internal\ capital>Debt>External\ equity
$$

The hierarchy follows the signaling and information costs of external financing, not a fixed target debt ratio.[^ci-fin-p39]

## Navigation changes on merge

Restructure the chapter map into WACC/components, cost and leverage drivers, MM theory, distress/trade-off theory, and agency/information theories. No new canonical concept is required; the weakness is depth rather than missing node coverage.

## Review checklist

- [x] WACC, MM, and trade-off formulas were visually checked against PDF pages 34-39.
- [x] Tax and no-tax cases remain sections of the same MM proposition nodes.
- [x] Trusted notes and Personal Notes remain unchanged at proposal stage.
- [x] User approves this enrichment bundle.
- [x] Merge preserves Personal Notes byte-for-byte and passes validation.

## Evidence

[^ci-fin-p34]: [[corporate-issuers-level-1-speed-review.pdf#page=34|Corporate Issuers Level I Speed Review, PDF p. 34]]
[^ci-fin-p35]: [[corporate-issuers-level-1-speed-review.pdf#page=35|Corporate Issuers Level I Speed Review, PDF p. 35]]
[^ci-fin-p36]: [[corporate-issuers-level-1-speed-review.pdf#page=36|Corporate Issuers Level I Speed Review, PDF p. 36]]
[^ci-fin-p37]: [[corporate-issuers-level-1-speed-review.pdf#page=37|Corporate Issuers Level I Speed Review, PDF p. 37]]
[^ci-fin-p38]: [[corporate-issuers-level-1-speed-review.pdf#page=38|Corporate Issuers Level I Speed Review, PDF p. 38]]
[^ci-fin-p39]: [[corporate-issuers-level-1-speed-review.pdf#page=39|Corporate Issuers Level I Speed Review, PDF p. 39]]
