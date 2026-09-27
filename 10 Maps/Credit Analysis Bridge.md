---
id: map-credit-analysis-bridge
type: map
title: Credit Analysis Bridge
aliases:
  - Accounting to Credit Analysis
status: trusted
tags:
  - cfa/level-1
  - map/cross-topic
---
Open graph view

# Credit Analysis Bridge

This route makes the accounting-to-credit connection explicit:

```mermaid
flowchart LR
  BS[Balance Sheet] --> CR[Current Ratio]
  FCF[Free Cash Flow] --> CCA[Corporate Credit Analysis]
  ICR[Interest Coverage Ratio] --> CCA
  DE[Debt-to-EBITDA Ratio] --> CCA
  NPM[Net Profit Margin] --> CCA
  CCA --> CRISK[Credit Risk]
  CRISK --> EL[Expected Loss]
```

## Navigate the route

1. Start with [[Corporate Credit Analysis]].
2. Follow coverage to [[Interest Coverage Ratio]] and leverage to [[Debt-to-EBITDA Ratio]].
3. Follow profitability to [[Net Profit Margin]] and cash generation to [[Free Cash Flow]].
4. Return to the [[Financial Statement Analysis]] map for calculations and to [[Fixed Income]] for credit interpretation.

