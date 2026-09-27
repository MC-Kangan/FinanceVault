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

The global graph is most useful for checking the overall structure and spotting isolated notes. System files, assets, archived proposals, and raw PDFs are filtered out by default.

## Colour legend

| Colour | Meaning |
| --- | --- |
| Gold | Home dashboard |
| Amber | Curriculum and topic maps |
| Purple | Concepts spanning both Financial Statement Analysis and Fixed Income |
| Green | Financial Statement Analysis concepts |
| Blue | Fixed Income concepts |
| Pink | Personal notes |
| Red | Proposals awaiting review |
| Grey | Registered source notes |

## Display choices

- Arrows are enabled so the direction of authored links is visible.
- Unresolved links and orphan notes are hidden to reduce noise.
- Labels remain visible longer, nodes are slightly enlarged, and link distance is shortened for a more readable cluster.
- To temporarily focus the global graph, use a search such as `path:"20 Concepts"` or `path:"10 Maps"` in its filter box.

See the [official Graph view guide](https://help.obsidian.md/plugins/graph) for navigation and force controls.
