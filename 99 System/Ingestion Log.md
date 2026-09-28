---
id: system-ingestion-log
type: map
title: Ingestion Log
status: trusted
tags:
  - system/log
---

# Ingestion Log

This is the human-readable ledger for source registration, transcription, proposal review, and trusted merges. Git commit IDs can be added after the vault is placed under version control.

| Date | Source | Level | Registered file | Transcript | Trusted merge | Git commit |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09-26 | [[Source - Financial Statement Analysis Level 1 Speed Review]] | 1 | `financial-statement-analysis-level-1-speed-review.pdf` | [[Transcript - Financial Statement Analysis Level 1 Speed Review]] | Full atomic inventory, taxes, leases, pensions, and share-based compensation merged | Initial repository snapshot |
| 2026-09-26 | [[Source - Fixed Income Level 1 Speed Review]] | 1 | `fixed-income-level-1-speed-review.pdf` | [[Transcript - Fixed Income Level 1 Speed Review]] | Full-deck and atomic-boundary proposals merged | Initial repository snapshot |
| 2026-09-28 | [[Source - Equity Investments Level 1 Speed Review]] | 1 | `equity-investments-level-1-speed-review.pdf` | [[Transcript - Equity Investments Level 1 Speed Review]] | Full-deck inventory and atomic concepts merged; six chapter maps created | `1ca2ec7`, graph `177c6eb` |
| 2026-09-28 | [[Source - Portfolio Management Level 1 Speed Review]] | 1 | `portfolio-management-level-1-speed-review.pdf` | [[Transcript - Portfolio Management Level 1 Speed Review]] | Full-deck inventory and atomic concepts merged; four chapter maps created | `1ca2ec7`, graph `177c6eb` |

## Entry checklist

- Source note and immutable PDF registered.
- Transcript created and page coverage recorded.
- Proposal filenames or scope recorded.
- Approval and merge date recorded.
- Validator and automated tests passed.
- Global graph and representative local graph visually inspected after map and colour updates.
- Git commit or tag added when available.
