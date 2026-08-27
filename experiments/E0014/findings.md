# E0014 Findings — XTRA Research Transfer Championship

**Evidence scope:** exploratory XTRA-only replay through canonical 2026-08-21.  
**Paper trading only.**

## 1. Canonical-state finding

The authoritative XTRA manifest and ledger contain 24 rows through **2026-08-21**, latest canonical result:

`17,23,37,39,48 | PB2`.

Later cycle artifacts contain the 2026-08-25 working result and a frozen 2026-08-28 XTRA forecast, but that result has not been appended under the manifest's official single-source rule. E0014 therefore trains/scores only the 24 canonical rows. This provenance gap must be resolved before later data become confirmatory training observations.

## 2. Distribution-first methodology transfers cleanly

The strongest transfer from Main E0005/E0009/E0011 is methodological:

- maintain full HLR/VVD probability distributions;
- compare learned displacement probabilities with exact order-statistic structural nulls;
- derive global coordinate probability only after direction/magnitude probability is represented;
- preserve exact-slot and anywhere-coordinate support separately;
- count convergence only after structural/recency redundancy is removed;
- preserve rescue at fixed K;
- treat PowerBall as a separate conditional transition process.

These rules do not import Main fitted state and are appropriate for XTRA.

## 3. Spectral graph does not transfer as an XTRA candidate selector

At K13 across 16 expanding-history targets:

- random matched-exposure expectation: **20.8** winning coordinates total;
- simple frequency: **19**;
- simple recency: **19**;
- PPMI weighted degree: **21**;
- normalized-Laplacian spectral row norm: **20**.

No method produced a 4/5 or 5/5 target. PPMI degree's 21 total is essentially random expectation.

Disposition: `INSUFFICIENT_EVIDENCE`; no candidate authority.

## 4. Main E0013 PPMI spectral coalition signal does not reproduce in XTRA

The exact Main-derived mathematical formulation was rebuilt from XTRA pair counts only.

Future winning-line percentile versus matched random legal lines:

- PPMI spectral: **0.482**;
- raw pair counts: **0.611**;
- simple PMI: **0.529**;
- additive frequency: **0.540**.

Morphology-matched spectral percentile: **0.484**.

Oracle-K13 stage isolation (known five winners + eight random decoys; zero acquisition credit):

- spectral mean winner percentile: **0.473**;
- raw pair: **0.645**;
- simple PMI: **0.521**;
- frequency: **0.572**.

Thus the transferred E0013 PPMI spectral coalition score is below the random median both globally and in oracle isolation. The result is not merely weaker than Main; its sign is opposite the Main discovery.

Narrow disposition: `REJECT` the claim that **this exact PPMI spectral formulation currently reproduces as a positive XTRA coalition signal**. Do not generalize that rejection to every possible future graph operator.

The fact that raw pair counts rank better than spectral coherence is an interesting XTRA-specific lead but remains `INSUFFICIENT_EVIDENCE`: only 10/16 targets were above the random median and the effect has not survived permutation/multiple-testing controls as a distinct derivative.

## 5. VVD probability models still do not beat exact geometry

Across 80 slot-events:

- `NULL_VVD_STRUCTURAL` log loss: **2.9392**, Brier **0.94127**;
- best tested learned log loss (direction-conditioned beta=.1): **2.9531**, worse;
- its Brier **0.94069** is slightly better;
- at beta=.2, learned exact-mode hits were 6 versus structural null 4.

The mixed metric result is not enough. A genuine distributional improvement should not require choosing the metric after replay.

Disposition: `INSUFFICIENT_EVIDENCE`; distribution-first representation transfers, but learned XTRA VVD residuals have not demonstrated predictive lift.

## 6. The tested draw-level magnitude-regime Markov model is falsified

Using expanding historical total-VVD quartiles to define stiction/central/tail:

- exact structural regime baseline log loss **0.9824**, Brier **0.59793**;
- best Markov residual beta=.1 log loss **0.9980**, Brier **0.60587**;
- larger betas deteriorate further.

Disposition: `REJECT` this specific first-order q25/q75 regime-transition model.

This does **not** reject XTRA E0011's broader joint-HLR-conditioned regime architecture. E0011 is primarily an exposure/risk-control architecture; the rejected claim is that this simple historical Markov router predicts the next regime better than exact geometry.

## 7. Residual PCA/SVD routing fails

With residual HLR, VVD, gap, sum and span features:

- k=2 next-total-VVD MAE **19.96** versus baseline **18.83**;
- k=3 **19.34** versus **18.83**;
- k=2 next-sum MAE **26.44** versus **23.12**;
- k=3 **26.31** versus **23.12**.

Disposition: `REJECT` the tested PCA(2)+KMeans(k=2/3) predictive router. Retain PCA only as descriptive/diagnostic unless a materially different preregistered residual representation is proposed.

## 8. Morphology is not a hard-prediction engine

Dynamic rolling-five sum corridors:

- alpha1.0 lift **0.73**;
- alpha1.5 **0.89**;
- alpha2.0 **1.06**.

Static filters:

- parity lift **1.06**;
- decade-spread lift **0.94**;
- max adjacent gap <=25 lift **1.11**;
- combined lift **1.03**.

The max-gap rule retained all 16 replay winners but also retains ~90% of legal space. The result is broad and underpowered, not evidence for hard elimination.

Disposition: `INSUFFICIENT_EVIDENCE`; morphology remains soft ranking/diversity only.

## 9. Fixed-K rescue helps a weak core, but does not create absolute edge

Simple-frequency Core13 captures **19** winner coordinates.

At the same K13 exposure:

- Core12 + Recency1: **21**, with 3 unique rescues and 1 displaced baseline winner;
- Core12 + Stiction/Shadow1: **21**, also 3 unique rescues and 1 displaced baseline winner;
- spectral/algebraic one-seat variants: **19**;
- two-seat rescue variants: 17–19.

Random K13 expectation across 16 targets is **20.8**.

Therefore one rescue seat improves the particular frequency core but still lands at random expectation. Two rescue seats over-diversify and displace useful core coordinates.

Disposition: `INSUFFICIENT_EVIDENCE`, but preserve the fixed-K architecture question. If rescues continue, **one seat** is the cleaner XTRA challenger than two under current evidence.

## 10. Conditional PowerBall convergence is the strongest extracted XTRA result

Across the same 16 expanding-history targets:

- uniform 1/16 log loss: **2.7726**;
- simple global frequency: **2.8726**;
- exact-state successor, tau4: **2.7568**;
- VVD+HLR successor, tau4: **2.8437**;
- geometric residual convergence of exact-state and VVD+HLR, tau4: **2.6600**.

The convergence model also produced **4/16 Top-1 hits** and mean exact rank **7.5**. Tau8 was still better than uniform on log loss (**2.6770**) but weaker than tau4.

This is important because neither component alone explains the improvement: exact-state alone is only slightly better than uniform; VVD+HLR alone is worse. The pooled distribution improves calibration, consistent with the HEPS doctrine that non-identical conditional paths should converge at the probability-distribution level rather than by raw vote counts.

However, tau4 was selected after testing tau4/tau8 and several model variants. Historical performance is discovery evidence only.

Disposition: `PROVISIONAL_SIGNAL`. Create a separate prospective shadow derivative with tau=4 frozen and no production authority.

## 11. Main-derived methodologies that transfer cleanly

Transfer:

- exact structural-null comparator/calibration;
- distribution-first HLR/VVD state representation;
- global-anywhere versus exact-slot coordinate separation;
- fixed-K rescue accounting;
- outcome-space/expert residualization;
- stage isolation and oracle diagnostics;
- morphology compression-lift scoring;
- conditional PB state/VVD transition shrinkage;
- Physics-of-Failure attribution between acquisition and assembly;
- external-contribution decomposition and stage remapping.

Do not transfer as predictive facts:

- Main spectral clusters/edges;
- Main E0013 positive result itself;
- Main fitted VVD or HLR distributions;
- Main PCA regimes;
- Main morphology corridors;
- Main pair motifs;
- Main PB transitions;
- Main candidate coordinates or expert weights.

## 12. Overall finding

No Main-derived main-number operator creates an XTRA breakthrough in this championship. The initial-acquisition problem remains open.

The strongest new derivative is **conditional XTRA PowerBall residual convergence** (`PROVISIONAL_SIGNAL`).

The strongest falsification is that **Main E0013 PPMI spectral coalition coherence does not reproduce in XTRA at the current canonical sample**.
