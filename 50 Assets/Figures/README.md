---
id: system-figure-replacement-guide
type: map
title: Figure Replacement Guide
status: trusted
tags:
  - system/assets
---

# Figure Replacement Guide

Replace an existing PNG in this folder with a higher-quality crop using the exact same filename. Obsidian embeds are filename-based, so no concept note needs to be edited when the filename remains unchanged.

## Export standard

- Export as PNG in sRGB.
- Use at least 1,600 px on the longest edge; use 2,000-2,400 px when the figure contains small labels or formulas.
- Crop to the complete explanatory figure, with roughly 24-40 px of clean padding.
- Preserve every relevant axis, legend, label, arrow, formula, and comparison panel.
- Exclude slide titles, page numbers, logos, and unrelated prose unless they are needed to understand the figure.
- Check readability at normal mobile width before replacing the current file.
- Keep the exact filename below. Replacing the file in place automatically updates every embed.

## Replacement inventory

| Priority | Topic | Concept note | Source and page | Exact filename | Desired crop |
| --- | --- | --- | --- | --- | --- |
| High | Fixed Income - Bond Structure and Features | [[Bullet Bond]]; the same figure also compares fully and partially amortizing structures | [[fixed-income-level-1-speed-review.pdf#page=8\|Fixed Income, PDF p. 8]] | `source-fi-l1-speed-review-p008-principal-repayment-structures.png` | The complete three cash-flow timelines for bullet, fully amortizing, and partially amortizing bonds. Include every maturity cash flow and timeline label; exclude the surrounding paragraph text. The present crop cuts off the right ends of the timelines. |
| Medium | Fixed Income - Repo Markets | [[Repurchase Agreement]] | [[fixed-income-level-1-speed-review.pdf#page=29\|Fixed Income, PDF p. 29]] | `source-fi-l1-speed-review-p029-repo-mechanics.png` | The full two-stage repo flow diagram at `T=0` and `T=t`, including both parties, bond arrows, cash arrows, and `P_0`/`P_t`. The current composition is correct but only 500 x 330 px. |
| High | Fixed Income - Yield Curves and Term Structure | [[Term Structure of Interest Rates]] | [[fixed-income-level-1-speed-review.pdf#page=54\|Fixed Income, PDF p. 54]] | `source-fi-l1-speed-review-p054-yield-curves.png` | All three panels showing normal, flat, and inverted/non-normal spot, par, and forward curves. Include the complete axes and a readable legend. The present crop cuts off the lower-right panel. |
| High | Fixed Income - Interest Rate Risk | [[Convexity]] | [[fixed-income-level-1-speed-review.pdf#page=66\|Fixed Income, PDF p. 66]] | `source-fi-l1-speed-review-p066-convexity-price-yield.png` | The full price-yield curve, duration tangent, reference dashed lines, error arrows, and both axis labels. The present crop clips both axes and the right side. |
| Low | Fixed Income - Credit Risk | [[Credit Risk]] | [[fixed-income-level-1-speed-review.pdf#page=81\|Fixed Income, PDF p. 81]] | `source-fi-l1-speed-review-p081-credit-risk-framework.png` | Only the complete framework: top-down Country/Conditions/Currency and bottom-up Capacity/Capital/Character/Collateral/Covenants around `Cs of Credit`. Keep both dashed group boundaries. The existing crop is structurally sound; replace it only for sharper text. |
| High | Fixed Income - Credit Analysis and Seniority | [[Debt Seniority]] | [[fixed-income-level-1-speed-review.pdf#page=88\|Fixed Income, PDF p. 88]] | `source-fi-l1-speed-review-p088-seniority-ranking.png` | The entire ranking ladder from First Lien/Mortgage through Junior Subordinated, plus Highest/Lowest Ranking and the Secured Debt/Unsecured Debt explanations. Exclude unrelated slide prose. The current crop contains stray text and omits part of the explanatory columns. |
| High | Financial Statement Analysis - Ratio Analysis | [[DuPont Analysis]] | [[financial-statement-analysis-level-1-speed-review.pdf#page=47\|FSA, PDF p. 47]] | `source-fsa-l1-speed-review-p047-dupont-relationship.png` | The complete two-part, three-part, and five-part DuPont decompositions, including the tax-burden and interest-burden labels at the bottom. The present crop truncates the bottom of the five-part explanation. |

## Replacement workflow

1. Open the cited PDF page at high zoom.
2. Crop only the region described above and export it as a sharp PNG.
3. Rename it to the exact filename in the table.
4. Replace the existing file in `50 Assets/Figures/`.
5. Open the owning concept note and confirm the figure is legible at desktop and mobile widths.
6. Run the vault validator; no Markdown changes should be required.
