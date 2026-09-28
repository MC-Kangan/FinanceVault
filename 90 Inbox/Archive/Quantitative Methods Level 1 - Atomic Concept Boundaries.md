---
id: proposal-quant-l1-atomic-concept-boundaries
type: proposal
title: Quantitative Methods Level 1 - Atomic Concept Boundaries
target: Quantitative Methods
change_type: concept-bundle
status: merged
tags:
  - cfa/level-1
---

# Quantitative Methods Level 1 - Atomic Concept Boundaries

## Rationale

The deck is already a condensed review source, so named ideas that own a formula, recur, have distinct exam behaviour, or provide a useful cross-topic destination should become canonical notes. Closely dependent vocabulary stays inside its parent concept when a separate node would add little navigation value.

## Proposed concepts by chapter

### Interest Rates and Investment Returns

Create or enrich: `Interest Rate`, `Required Rate of Return`, `Discount Rate`, `Opportunity Cost`, `Nominal Risk-Free Rate`, `Real Risk-Free Rate`, `Inflation Premium`, `Default Risk Premium`, `Liquidity Premium`, `Maturity Premium`, [[Holding Period Return]], `Arithmetic Mean Return`, `Geometric Mean Return`, `Harmonic Mean Return`, `Time-Weighted Return`, `Money-Weighted Return`, `Future Value Factor`, `Present Value Factor`, `Annualized Return`, `Continuous Compounding`, `Gross Return`, `Net Return`, `Nominal Return`, `Real Return`, `After-Tax Return`, `Leveraged Return`, `Time Value of Money`, and `Cash Flow Additivity Principle`.[^quant-boundaries-p4][^quant-boundaries-p10]

### Descriptive Statistics

Create or enrich: `Descriptive Statistics`, `Population and Sample`, `Parameter and Sample Statistic`, `Arithmetic Mean`, `Weighted Mean`, `Trimmed Mean`, `Winsorized Mean`, `Median`, `Mode`, `Quantile`, `Interquartile Range`, `Box-and-Whisker Plot`, `Range`, `Mean Absolute Deviation`, [[Variance]], [[Standard Deviation]], `Target Downside Deviation`, `Coefficient of Variation`, `Scatter Plot`, `Covariance`, [[Correlation]], `Spurious Correlation`, `Skewness`, and `Kurtosis`. Distribution shape labels such as leptokurtic, mesokurtic, and platykurtic should be aliases or sections within `Kurtosis`, not separate notes.[^quant-boundaries-p12][^quant-boundaries-p20]

### Probability Foundations

Create or enrich: `Random Variable`, `Expected Value`, `Conditional Probability`, `Joint Probability`, `Independent Events`, `Total Probability Rule`, `Conditional Expected Value`, `Conditional Variance`, `Bayes' Formula`, [[Portfolio Expected Return]], [[Portfolio Variance]], `Normal Distribution`, `Standard Normal Distribution`, `Z-Score`, `Shortfall Risk`, `Safety-First Ratio`, `Lognormal Distribution`, and `Student's t-Distribution`. Outcomes and events remain defined within `Random Variable` unless a later source makes them reusable nodes.[^quant-boundaries-p23][^quant-boundaries-p30]

### Sampling and Inference

Create or enrich: `Sampling Error`, `Sampling Distribution`, `Simple Random Sampling`, `Stratified Random Sampling`, `Systematic Sampling`, `Cluster Sampling`, `Convenience Sampling`, `Judgmental Sampling`, `Monte Carlo Simulation`, `Bootstrap`, `Jackknife`, `Central Limit Theorem`, `Standard Error`, `Hypothesis Testing`, `Null and Alternative Hypotheses`, `One-Tailed and Two-Tailed Tests`, `Significance Level`, `Confidence Level`, `Test Statistic`, `Critical Value`, `P-Value`, `Type I Error`, `Type II Error`, `Power of a Test`, `One-Sample Mean Test`, `Difference in Means Test`, `Paired Comparisons Test`, `Chi-Square Test of Variance`, `F-Test`, `Parametric Test`, `Nonparametric Test`, `Pearson Correlation Test`, `Spearman Rank Correlation`, and `Contingency Table Test`.[^quant-boundaries-p34][^quant-boundaries-p48]

### Simple Linear Regression

Create or enrich: `Simple Linear Regression`, `Ordinary Least Squares`, `Regression Assumptions`, `Homoskedasticity`, `Heteroskedasticity`, `Regression ANOVA`, `Total Sum of Squares`, `Regression Sum of Squares`, `Sum of Squared Errors`, `Mean Square Regression`, `Mean Squared Error`, `Coefficient of Determination`, `F-Statistic`, `Standard Error of Estimate`, `Slope Coefficient Test`, `Forecast Standard Error`, `Prediction Interval`, `Indicator Variable`, `Log-Lin Model`, `Lin-Log Model`, and `Log-Log Model`. Dependent variable, independent variable, intercept, slope, error term, and residual remain within `Simple Linear Regression` unless later sources require standalone nodes.[^quant-boundaries-p52][^quant-boundaries-p59]

### Big Data Analysis

Create or enrich: `Fintech`, `Big Data`, `Alternative Data`, `Artificial Intelligence`, `Machine Learning`, `Training Validation and Test Sets`, `Supervised Learning`, `Unsupervised Learning`, `Overfitting`, `Underfitting`, `Data Visualization`, `Text Analytics`, and `Natural Language Processing`. Volume, velocity, variety, and veracity remain properties within `Big Data`, not separate notes.[^quant-boundaries-p62][^quant-boundaries-p66]

## Alias and cross-topic policy

- `Internal Rate of Return` and `IRR` should resolve to `Money-Weighted Return` in this return-measure context, subject to collision validation.
- `CV` should be considered for `Coefficient of Variation` only if it does not collide with an existing normalized alias.
- `R-squared`, `R²`, and `R2` should resolve to `Coefficient of Determination`.
- `OLS` should resolve to `Ordinary Least Squares`; `NLP` should resolve to `Natural Language Processing`; `ML` should resolve to `Machine Learning`; `AI` should resolve to `Artificial Intelligence`.
- Cross-topic connections should link return measures to [[Portfolio Management]], risk premiums and interest rates to [[Fixed Income]], and regression/correlation applications to both portfolio and equity analysis only where the source-supported explanation is meaningful.

## Proposed visual assets

No crops are created at proposal stage. During merge, the most useful candidates are the sampling-to-estimation framework on PDF page 34, the hypothesis-testing decision/error framework on pages 41–43, and the regression ANOVA decomposition on page 55. Each replacement-ready asset should follow `quant-l1-speed-review-pNN-description.png` and retain a text explanation plus exact PDF citation.

## Review checklist

- [x] Candidate boundaries follow the review deck's granularity.
- [x] Obvious existing concepts are designated for enrichment, not duplication.
- [x] Alias candidates are recorded but not committed to trusted notes.
- [x] Trusted concepts and Personal Notes remain unchanged.
- [x] User approves the atomic boundaries.
- [x] Full normalized-alias collision check passes during merge.
- [x] Every promoted formula is visually verified; no figure crop was promoted in this merge.
- [x] Vault validation passes after merge.

## Evidence

[^quant-boundaries-p4]: [[quantitative-methods-level-1-speed-review.pdf#page=4|Quantitative Methods Level I Speed Review, PDF p. 4]]
[^quant-boundaries-p10]: [[quantitative-methods-level-1-speed-review.pdf#page=10|Quantitative Methods Level I Speed Review, PDF p. 10]]
[^quant-boundaries-p12]: [[quantitative-methods-level-1-speed-review.pdf#page=12|Quantitative Methods Level I Speed Review, PDF p. 12]]
[^quant-boundaries-p20]: [[quantitative-methods-level-1-speed-review.pdf#page=20|Quantitative Methods Level I Speed Review, PDF p. 20]]
[^quant-boundaries-p23]: [[quantitative-methods-level-1-speed-review.pdf#page=23|Quantitative Methods Level I Speed Review, PDF p. 23]]
[^quant-boundaries-p30]: [[quantitative-methods-level-1-speed-review.pdf#page=30|Quantitative Methods Level I Speed Review, PDF p. 30]]
[^quant-boundaries-p34]: [[quantitative-methods-level-1-speed-review.pdf#page=34|Quantitative Methods Level I Speed Review, PDF p. 34]]
[^quant-boundaries-p48]: [[quantitative-methods-level-1-speed-review.pdf#page=48|Quantitative Methods Level I Speed Review, PDF p. 48]]
[^quant-boundaries-p52]: [[quantitative-methods-level-1-speed-review.pdf#page=52|Quantitative Methods Level I Speed Review, PDF p. 52]]
[^quant-boundaries-p59]: [[quantitative-methods-level-1-speed-review.pdf#page=59|Quantitative Methods Level I Speed Review, PDF p. 59]]
[^quant-boundaries-p62]: [[quantitative-methods-level-1-speed-review.pdf#page=62|Quantitative Methods Level I Speed Review, PDF p. 62]]
[^quant-boundaries-p66]: [[quantitative-methods-level-1-speed-review.pdf#page=66|Quantitative Methods Level I Speed Review, PDF p. 66]]
