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
| 2026-09-26 / 2026-10-03 | [[Source - Financial Statement Analysis Level 1 Speed Review]] | 1 | `financial-statement-analysis-level-1-speed-review.pdf` | [[Transcript - Financial Statement Analysis Level 1 Speed Review]] | Full atomic inventory merged; 120 accounting concepts enriched from visually reviewed pages; twelve chapter maps created; final validation and graph review completed | Pending Git commit |
| 2026-09-26 / 2026-10-04 | [[Source - Fixed Income Level 1 Speed Review]] | 1 | `fixed-income-level-1-speed-review.pdf` | [[Transcript - Fixed Income Level 1 Speed Review]] | Full inventory merged; 105 existing concepts enriched from visually reviewed pages; `Commercial Paper` added; six chapter maps created; final validation and graph review completed | Pending Git commit |
| 2026-09-28 / 2026-10-03 | [[Source - Equity Investments Level 1 Speed Review]] | 1 | `equity-investments-level-1-speed-review.pdf` | [[Transcript - Equity Investments Level 1 Speed Review]] | Full inventory merged; 168 existing concepts enriched from visually reviewed pages; existing `Loss Aversion Bias` reused as a cross-topic node; six chapter maps retained; final validation and graph review completed | Pending Git commit |
| 2026-09-28 | [[Source - Portfolio Management Level 1 Speed Review]] | 1 | `portfolio-management-level-1-speed-review.pdf` | [[Transcript - Portfolio Management Level 1 Speed Review]] | Full-deck inventory and atomic concepts merged; four chapter maps created | `1ca2ec7`, graph `177c6eb` |
| 2026-10-03 | [[Source - Economics Level 1 Speed Review]] | 1 | `economics-level-1-speed-review.pdf` | [[Transcript - Economics Level 1 Speed Review]] | Full-deck inventory and atomic concepts merged; six chapter maps created; global graph and representative navigation paths verified | Pending Git commit |
| 2026-10-04 | [[Source - Ethics Level 1 Speed Review]] and [[Source - CFA Code and Standards English]] | 1 | `ethics-level-1-speed-review.pdf`; `cfa-code-and-standards-english.pdf` | [[Transcript - Ethics Level 1 Speed Review]]; [[Transcript - CFA Code and Standards English]] | 31 Ethics concepts merged; one major topic map and eight chapter maps created; current 2024 official standard names used with older deck terms retained as aliases | Pending Git commit |

| 2026-10-10 | [[Source - Corporate Issuers Level 1 Speed Review]] | 1 | `corporate-issuers-level-1-speed-review.pdf` | [[Transcript - Corporate Issuers Level 1 Speed Review]] | Five detailed chapter enrichments merged; 116 existing concepts enriched; 19 omitted concepts added; five chapter maps reorganized; final validation and graph review completed | Pending Git commit |

## Entry checklist

- Source note and immutable PDF registered.
- Transcript created and page coverage recorded.
- Proposal filenames or scope recorded.
- Approval and merge date recorded.
- Validator and automated tests passed.
- Global graph and representative local graph visually inspected after map and colour updates.
- Git commit or tag added when available.
