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
| Orange | Chapter/subtopic maps |
| Purple | Concepts whose `topics` property contains two or more major topics |
| Green | Financial Statement Analysis concepts |
| Blue | Fixed Income concepts |
| Red | Equity Investments concepts |
| Teal | Portfolio Management concepts |

## Colour-group queries

Add the groups in this order because the first matching group controls a node's colour:

| Order | Query | Meaning |
| --- | --- | --- |
| 1 | `file:"CFA Level 1"` | CFA level maps |
| 2 | `file:"Financial Statement Analysis" OR file:"Fixed Income" OR file:"Equity Investments" OR file:"Portfolio Management"` | Major topic maps |
| 3 | `tag:#map/subtopic` | Chapter/subtopic maps |
| 4 | Pairwise combinations of two `topics` property queries | Cross-topic concepts |
| 5 | `path:"20 Concepts" [topics:"Financial Statement Analysis"]` | FSA concepts |
| 6 | `path:"20 Concepts" [topics:"Fixed Income"]` | Fixed Income concepts |
| 7 | `path:"20 Concepts" [topics:"Equity Investments"]` | Equity concepts |
| 8 | `path:"20 Concepts" [topics:"Portfolio Management"]` | Portfolio concepts |

The purple group in `.obsidian/graph.json` enumerates every pair of the four current major topics. Keep it before the single-topic colour groups so a shared concept receives the cross-topic colour first. The property filters are intentional: plain-text searches can produce false matches from prose or citations.

## Display choices

- Arrows are enabled so the direction of authored links is visible.
- Attachments, unresolved links, and orphan notes are hidden to reduce noise.
- Labels remain visible longer, nodes are slightly enlarged, and link distance is shortened so chapter maps pull their concepts into visible clusters.
- To focus temporarily, search for a chapter map such as `file:"Equity - Equity Valuation"`, then use its local graph at depth 1 or 2.

## Manual recovery

1. Open **Graph view**.
2. Select **Open graph settings**.
3. Under **Filters**, paste the global graph filter above.
4. Turn off **Tags** and **Attachments**.
5. Turn on **Existing files only** and turn off orphan display.
6. Under **Groups**, add the eight groups in the listed order and choose the colours from the legend. Copy the complete purple cross-topic query from `.obsidian/graph.json`.
7. Under **Display**, enable arrows and slightly increase node and link thickness.

See the [official Graph view guide](https://help.obsidian.md/plugins/graph) for navigation and force controls.
