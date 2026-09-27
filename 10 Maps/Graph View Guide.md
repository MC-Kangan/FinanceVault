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

The global graph is configured as a curriculum knowledge graph. It shows canonical concepts plus level, topic, and cross-topic maps. Sources, transcripts, proposals, personal notes, templates, system documentation, attachments, and raw PDFs are excluded.

## Global graph filter

The filter box should contain:

```text
path:"20 Concepts" OR file:"CFA Level 1" OR file:"Financial Statement Analysis" OR file:"Fixed Income" OR file:"Credit Analysis Bridge"
```

This includes everything in `20 Concepts/` and explicitly includes the level, topic, and cross-topic maps. System maps such as this guide are omitted. If the Graph settings are accidentally reset, paste this expression into **Filters → Search files**.

## Colour legend

| Colour | Meaning |
| --- | --- |
| Gold | CFA level maps |
| Amber | Topic maps |
| Purple | Cross-topic maps and concepts spanning both FSA and Fixed Income |
| Green | Financial Statement Analysis concepts |
| Blue | Fixed Income concepts |

## Colour-group queries

Add the groups in this order because the first matching group controls a node's colour:

| Order | Query | Meaning |
| --- | --- | --- |
| 1 | `file:"CFA Level 1"` | CFA level maps |
| 2 | `file:"Financial Statement Analysis" OR file:"Fixed Income"` | Topic maps |
| 3 | `file:"Credit Analysis Bridge"` | Cross-topic maps |
| 4 | `path:"20 Concepts" "Financial Statement Analysis" "Fixed Income"` | Concepts used by both topics |
| 5 | `path:"20 Concepts" "Financial Statement Analysis"` | FSA concepts |
| 6 | `path:"20 Concepts" "Fixed Income"` | Fixed Income concepts |

## Display choices

- Arrows are enabled so the direction of authored links is visible.
- Attachments, unresolved links, and orphan notes are hidden to reduce noise.
- Labels remain visible longer, nodes are slightly enlarged, and link distance is shortened for a more readable cluster.
- To focus temporarily, replace the filter with `path:"20 Concepts" "Fixed Income"`, `path:"20 Concepts" "Financial Statement Analysis"`, or `file:"CFA Level 1"`.

## Manual recovery

1. Open **Graph view**.
2. Select **Open graph settings**.
3. Under **Filters**, paste the global graph filter above.
4. Turn off **Tags** and **Attachments**.
5. Turn on **Existing files only** and turn off orphan display.
6. Under **Groups**, add the six queries in the listed order and choose the colours from the legend.
7. Under **Display**, enable arrows and slightly increase node and link thickness.

See the [official Graph view guide](https://help.obsidian.md/plugins/graph) for navigation and force controls.
