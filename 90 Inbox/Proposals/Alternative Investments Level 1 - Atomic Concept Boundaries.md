---
id: proposal-alternatives-l1-atomic-concept-boundaries
type: proposal
title: Alternative Investments Level 1 - Atomic Concept Boundaries
target: Alternative Investments
change_type: concept-bundle
status: pending-review
tags:
  - cfa/level-1
---

# Alternative Investments Level 1 - Atomic Concept Boundaries

## Rationale

The deck is already a condensed review source. Named structures, stages, fee provisions, strategy families, investment forms, and recurring risk concepts therefore become canonical notes when they are useful navigation targets. Closely dependent labels remain sections or aliases when separating them would add little study value.

## Proposed concepts by chapter

### Foundations and Structures

Create or enrich: `Alternative Investments`, `Direct Alternative Investment`, `Fund Investment`, `Co-Investment`, `Limited Partnership`, `General Partner`, `Limited Partner`, `Limited Partnership Agreement`, `Side Letter`, `Alternative Investment Life Cycle`, `Capital Commitment`, `Capital Call`, `Capital Deployment`, `Capital Distribution`, `J-Curve Effect`, [[Money-Weighted Return]], `Multiple of Invested Capital`, [[Leveraged Return]], `Fair Value Hierarchy`, `Management Fee`, `Incentive Fee`, `Two and Twenty`, `Hurdle Rate`, `Hard Hurdle Rate`, `Soft Hurdle Rate`, `High-Water Mark`, `Deal-by-Deal Waterfall`, `Whole-of-Fund Waterfall`, `Clawback Provision`, `Catch-Up Clause`, and `Custom Fee Arrangement`.[^alt-boundaries-p4][^alt-boundaries-p13]

`General Partner` and `Limited Partner` should remain separate nodes because their control, liability, fee, and distribution interests differ. Fund phases should remain separate nodes linked through `Alternative Investment Life Cycle` because capital calls, deployment, distributions, and the J-curve recur throughout private-market study.

### Private Capital

Create or enrich: [[Private Equity]], `Venture Capital`, `Pre-Seed Capital`, `Seed-Stage Financing`, `Early-Stage Financing`, `Later-Stage Financing`, `Mezzanine-Stage Financing`, `Growth Capital`, `Private Investment in Public Equity`, `Leveraged Buyout`, `Management Buyout`, `Management Buy-In`, `Private Equity Exit`, `Initial Public Offering`, `Direct Listing`, `Special Purpose Acquisition Company`, `Secondary Sale`, `Recapitalization`, `Private Debt`, `Direct Lending`, `Venture Debt`, `Mezzanine Debt`, `Distressed Debt`, `Unitranche Debt`, `Private Capital Performance Bias`, and `Vintage Year`.[^alt-boundaries-p17][^alt-boundaries-p22]

The named venture-financing stages remain atomic because questions distinguish the company's development stage and use of proceeds. IPO, direct listing, SPAC, MBS, covered bonds, and convertible bonds must reuse existing equity or fixed-income nodes where present.

### Real Estate and Infrastructure

Create or enrich: `Real Estate Investment`, `Residential Real Estate`, `Commercial Real Estate`, `Direct Real Estate Investment`, `Indirect Real Estate Investment`, `Real Estate Investment Trust`, [[Mortgage-Backed Securities]], [[Covered Bond]], `Infrastructure Investment`, `Public-Private Partnership`, `Economic Infrastructure`, `Social Infrastructure`, `Direct Infrastructure Investment`, `Indirect Infrastructure Investment`, `Greenfield Investment`, `Brownfield Investment`, `Secondary-Stage Infrastructure`, and `Infrastructure Risk and Return`.[^alt-boundaries-p24][^alt-boundaries-p29]

Debt-versus-equity and public-versus-private real-estate routes should be explained inside the parent investment-form notes rather than turned into four nearly empty duplicates.

### Natural Resources and Commodities

Create or enrich: `Land Investment`, `Farmland Investment`, `Timberland Investment`, `Timberland Investment Management Organization`, `Commodity Investment`, `Commodity Futures Pricing`, `Cost of Carry`, `Convenience Yield`, `Contango`, and `Backwardation`.[^alt-boundaries-p29][^alt-boundaries-p31]

### Hedge Funds

Create or enrich: `Hedge Fund`, `Lockup Period`, `Notice Period`, `Equity Hedge Strategy`, `Market-Neutral Strategy`, `Fundamental Long-Short Strategy`, `Fundamental Growth Strategy`, `Fundamental Value Strategy`, `Short-Bias Strategy`, `Event-Driven Strategy`, `Merger Arbitrage`, `Distressed Securities Strategy`, `Activist Shareholder Strategy`, `Special Situations Strategy`, `Relative Value Strategy`, `Convertible Bond Arbitrage`, `Fixed-Income Asset-Backed Strategy`, `Fixed-Income General Strategy`, `Multi-Strategy Hedge Fund`, `Opportunistic Strategy`, `Macro Strategy`, `Managed Futures`, `Multi-Manager Strategy`, `Separately Managed Account`, `Fund of Hedge Funds`, [[Beta]], `Strategy Beta`, `Alpha`, [[Hedge Fund Index]], `Selection Bias`, `Survivorship Bias`, `Backfill Bias`, and `Equal-Weighted Index Bias`.[^alt-boundaries-p33][^alt-boundaries-p38]

Strategy families and their named sub-strategies remain separate because the deck repeatedly contrasts position construction, market exposure, and source of return.

### Digital Assets

Create or enrich: `Distributed Ledger Technology`, `Cryptography`, `Permissionless Network`, `Permissioned Network`, `Blockchain`, `Consensus Mechanism`, `Proof of Work`, `Proof of Stake`, `Cryptocurrency`, `Tokenization`, `Non-Fungible Token`, `Security Token`, `Utility Token`, `Governance Token`, `Digital Asset Characteristics`, `Cryptocurrency Wallet`, `Centralized Cryptocurrency Exchange`, `Decentralized Cryptocurrency Exchange`, `Direct Cryptocurrency Investment Risk`, `Cryptocurrency Trust`, `Cryptocurrency Futures`, and `Asset-Backed Token`.[^alt-boundaries-p40][^alt-boundaries-p45]

## Alias and cross-topic policy

- `MOIC` resolves to `Multiple of Invested Capital`; `GP` and `LP` resolve to `General Partner` and `Limited Partner`; `LPA` resolves to `Limited Partnership Agreement`.
- `IRR` and `Internal Rate of Return` continue to resolve to the existing `Money-Weighted Return` node rather than creating a second return concept.
- `PIPE`, `LBO`, `MBO`, `MBI`, `REIT`, `PPP`, `TIMO`, `SMA`, `FOF`, `CTA`, `DLT`, `PoW`, `PoS`, `NFT`, and relevant Chinese translations become aliases only after normalized collision validation.
- Existing `Mortgage-Backed Securities`, `Covered Bond`, `Convertible Bond`, `Beta`, and `Hedge Fund Index` notes receive Alternative Investments context rather than duplicates.
- Cross-topic links should connect private-company financing to [[Equity Investments]], private debt and structured-credit strategies to [[Fixed Income]], and return/risk/bias concepts to [[Quantitative Methods]] and [[Portfolio Management]] only where the source-supported explanation is meaningful.

## Proposed visual assets

No crop is created at proposal stage. High-value replacement-ready candidates are the alternative-investment J-curve on PDF page 7, the infrastructure stage risk-return diagram on page 28, and the private-capital risk-return comparison on page 21. Use `alternatives-l1-speed-review-pNN-description.png`, retain searchable explanatory text, and cite the exact supporting PDF page.

## Review checklist

- [x] Candidate boundaries follow the review deck's granularity.
- [x] Obvious existing concepts are designated for enrichment, not duplication.
- [x] Alias candidates are recorded but not committed to trusted notes.
- [x] Trusted concepts and Personal Notes remain unchanged.
- [ ] User approves the atomic boundaries.
- [ ] Full normalized-alias collision check passes during merge.
- [ ] Every promoted formula and selected figure is visually verified.
- [ ] Vault validation passes after merge.

## Evidence

[^alt-boundaries-p4]: [[alternative-investments-level-1-speed-review.pdf#page=4|Alternative Investments Level I Speed Review, PDF p. 4]]
[^alt-boundaries-p13]: [[alternative-investments-level-1-speed-review.pdf#page=13|Alternative Investments Level I Speed Review, PDF p. 13]]
[^alt-boundaries-p17]: [[alternative-investments-level-1-speed-review.pdf#page=17|Alternative Investments Level I Speed Review, PDF p. 17]]
[^alt-boundaries-p22]: [[alternative-investments-level-1-speed-review.pdf#page=22|Alternative Investments Level I Speed Review, PDF p. 22]]
[^alt-boundaries-p24]: [[alternative-investments-level-1-speed-review.pdf#page=24|Alternative Investments Level I Speed Review, PDF p. 24]]
[^alt-boundaries-p29]: [[alternative-investments-level-1-speed-review.pdf#page=29|Alternative Investments Level I Speed Review, PDF p. 29]]
[^alt-boundaries-p31]: [[alternative-investments-level-1-speed-review.pdf#page=31|Alternative Investments Level I Speed Review, PDF p. 31]]
[^alt-boundaries-p33]: [[alternative-investments-level-1-speed-review.pdf#page=33|Alternative Investments Level I Speed Review, PDF p. 33]]
[^alt-boundaries-p38]: [[alternative-investments-level-1-speed-review.pdf#page=38|Alternative Investments Level I Speed Review, PDF p. 38]]
[^alt-boundaries-p40]: [[alternative-investments-level-1-speed-review.pdf#page=40|Alternative Investments Level I Speed Review, PDF p. 40]]
[^alt-boundaries-p45]: [[alternative-investments-level-1-speed-review.pdf#page=45|Alternative Investments Level I Speed Review, PDF p. 45]]
