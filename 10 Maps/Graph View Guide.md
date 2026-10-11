---
id: map-graph-view-guide
type: map
title: Graph View Guide
status: trusted
tags:
  - map/system
---

# Graph View Guide

The graph is an exploration tool; the maps and typed relationships remain the authoritative navigation layer.

## Recommended way to use it

1. Open a concept such as [[Corporate Credit Analysis]].
2. Run **Open local graph** from the command palette.
3. Start at depth 1 to see direct prerequisites, applications, sources, and maps.
4. Move to depth 2 only when you want to explore adjacent concepts.
5. Click a node to open it; hover over a node to isolate its immediate links.

The global graph is configured as a curriculum knowledge graph. It shows canonical concepts, CFA level maps, major topic maps, and chapter/subtopic maps. Sources, transcripts, proposals, personal notes, templates, system documentation, attachments, and raw PDFs are excluded.

## Global graph filter

The filter box should contain:

```text
path:"20 Concepts" OR (path:"10 Maps" -file:"Graph View Guide")
```

This includes everything in `20 Concepts/` and the curriculum maps in `10 Maps/`. The system-only Graph View Guide is omitted. If the Graph settings are accidentally reset, paste this expression into **Filters → Search files**.

## Colour legend

| Colour | Meaning |
| --- | --- |
| Gold | CFA level maps |
| Amber | Topic maps |
| Light blue | Fixed Income chapter/subtopic maps |
| Light violet | Ethics chapter/subtopic maps |
| Orange | Chapter/subtopic maps |
| Purple | Concepts whose `topics` property contains two or more major topics |
| Green | Financial Statement Analysis concepts |
| Blue | Fixed Income concepts |
| Red | Equity Investments concepts |
| Teal | Portfolio Management concepts |
| Pink | Quantitative Methods concepts |
| Cyan | Alternative Investments concepts |
| Yellow | Corporate Issuers concepts |
| Bright teal | Derivatives concepts |
| Indigo | Economics concepts |
| Violet | Ethical and Professional Standards concepts |

## Colour-group queries

Add the groups in this order because the first matching group controls a node's colour:

| Order | Query | Meaning |
| --- | --- | --- |
| 1 | `file:"CFA Level 1"` | CFA level maps |
| 2 | All nine major topic-map filenames joined with `OR` | Major topic maps |
| 3 | `file:"Fixed Income - Bond Features" OR file:"Fixed Income - Markets and Issuance" OR file:"Fixed Income - Valuation and Yields" OR file:"Fixed Income - Interest Rate Risk" OR file:"Fixed Income - Credit Risk" OR file:"Fixed Income - Securitization"` | Fixed Income chapter maps |
| 4 | All eight `Ethics - ...` chapter-map filenames joined with `OR` | Ethics chapter maps |
| 5 | `tag:#map/subtopic` | Other chapter/subtopic maps |
| 6 | Pairwise combinations of two `topics` property queries | Cross-topic concepts |
| 7-16 | Single-topic `topics` property queries | Concepts for the ten major topics in legend order |

The purple group in `.obsidian/graph.json` enumerates every pair of the ten current major topics. Keep it before the single-topic colour groups so a shared concept receives the cross-topic colour first. The property filters are intentional: plain-text searches can produce false matches from prose or citations.

## Display choices

- Arrows are enabled so the direction of authored links is visible.
- Attachments, unresolved links, and orphan notes are hidden to reduce noise.
- Labels remain visible longer, nodes are slightly enlarged, and link distance is shortened so chapter maps pull their concepts into visible clusters.
- To focus temporarily, search for a chapter map such as `file:"FSA - Income Taxes"` or `file:"Equity - Equity Valuation"`, then use its local graph at depth 1 or 2.

## Financial Statement Analysis hierarchy

The FSA topic map now branches into twelve orange chapter maps covering reporting, the income statement, financial instruments, cash flows, analysis techniques, inventories, long-lived assets, leases, employee compensation, income taxes, reporting quality, and forecasting. This replaces the former flat FSA concept index; green concepts should cluster around these chapter nodes while genuine cross-topic concepts retain the purple bridge colour.

## Equity Investments hierarchy

The Equity topic map branches into six orange chapter maps: Financial Markets and Trading, Security Market Indexes, Market Efficiency, Equity Securities, Industry and Company Analysis, and Equity Valuation. Red Equity concepts should cluster around these chapter nodes; accounting-derived valuation and analysis concepts may appear as purple bridges where their `topics` properties include another major CFA topic.

## Fixed Income hierarchy

The Fixed Income topic map branches into six light-blue chapter maps: Bond Features, Markets and Issuance, Valuation and Yields, Interest Rate Risk, Credit Risk, and Securitization. Blue concepts should cluster around these chapter nodes. Accounting-derived credit measures, mortgage-backed securities, repos, and credit risk retain their purple cross-topic bridge colour when their `topics` properties include another major CFA topic.

## Ethical and Professional Standards hierarchy

The Ethics topic map branches into eight light-violet chapter maps: Professionalism, Integrity of Capital Markets, Duties to Clients, Duties to Employers, Investment Analysis Recommendations and Actions, Conflicts of Interest, CFA Institute Member and Candidate Responsibilities, and Global Investment Performance Standards. Violet concept nodes should cluster around these chapter maps. The official 2024 standard names are canonical; older deck terminology is retained only as aliases.

## Manual recovery

1. Open **Graph view**.
2. Select **Open graph settings**.
3. Under **Filters**, paste the global graph filter above.
4. Turn off **Tags** and **Attachments**.
5. Turn on **Existing files only** and turn off orphan display.
6. Under **Groups**, add the sixteen groups in the listed order and choose the colours from the legend. Copy the complete topic-map and purple cross-topic queries from `.obsidian/graph.json`.
7. Under **Display**, enable arrows and slightly increase node and link thickness.

See the [official Graph view guide](https://help.obsidian.md/plugins/graph) for navigation and force controls.
