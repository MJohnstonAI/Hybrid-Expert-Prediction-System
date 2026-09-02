# E0025 Decision — Apodex Infrastructure Extraction

## Decision

`ACCEPT SELECTED METHODOLOGY / REJECT CURRENT PREDICTIVE ENGINE / AUTHORIZE REPAIRED SHADOWS`

Evidence classification: `INSUFFICIENT_EVIDENCE` for prediction.

Paper trading only.

## Accepted components

The following Apodex contributions are useful and may be reimplemented in canonical HEPS code after independent tests:

1. exact legal-line dynamic programming for null-residual fields;
2. exact-null recovery tests;
3. fixed-K complete-line containment `M(K)` dynamic programming;
4. strict walk-forward proper-score harness architecture;
5. machine-provenance backfill as a data-quality priority;
6. search-exposure accounting and automated first-failure-stage tracing as governance infrastructure.

These are methodological/infrastructure contributions, not predictive lift.

## Rejected current implementations

### One-parameter signed displacement

`P0_j(x)*exp(phi_j*(x-p_j))` is rejected as the E0021 transition implementation because the previous-coordinate factor cancels in normalization. It is a slot-coordinate tilt, not a genuinely previous-state-dependent signed transition.

### Adjacent-slot preserver

The supplied preserver is rejected because it starts from Top13 on `p_anywhere` and then requires an omitted coordinate to beat the weakest Top13 member on the same score. That condition is structurally unavailable except tie artefacts, so the preservation arm is effectively inert.

### PowerBall championship

The supplied PB scoring routine is rejected because it mixes opposite log-loss signs and does not score withheld realized PB targets.

### Coalition PMI probability interpretation

The supplied smoothed association may remain an algorithmic idea, but the denominators are not coherent singleton/pair event probabilities. It must be re-derived before probability or PMI claims are used.

## Corrected PB derivative

A fresh walk-forward reconstruction of unconditional Dirichlet-shrunk PB fields found alpha=2 directionally better than uniform over the current 24 evaluable targets, but the alpha was selected after inspecting seven values and the advantage is not statistically significant.

Decision:

`AUTHORIZE ZERO-WEIGHT PROSPECTIVE SHADOW FROM 2026-09-04`.

No production or portfolio authority.

## Main Friday implication

Apodex does **not** justify changing the current Friday Main K13 or Main slate. Its supplied Main engine reproduced only 1.25 mean K13 hits versus 1.30 IID expectation and was worse than the structural null on both tested proper-score deltas.

A repaired signed-transition implementation may be built and frozen for a later target, with first priority on genuinely previous-state-dependent basis functions plus exact legal-line normalization.

## Follow-up response review — 2026-09-02

Apodex explicitly accepted the three major defects identified in the first red-team review and supplied replacement specifications. This materially improves the contribution, but two proposed repairs remain mathematically defective as written.

### Signed-transition basis — accepted with construction correction

The nonlinear basis `sign(Delta)` plus `sign(Delta)*log(1+abs(Delta))` is genuinely previous-state dependent and may enter a repaired E0021 challenger.

However, the follow-up proposes legal-line factors `P0_j(x)*R_j(x|p)`. Multiplying exact slot null marginals across slots reintroduces order-statistic geometry. The legal-line model must instead begin from the uniform exact 5-of-50 line null and multiply only residual ratios. Equivalently, after fitting the conditional slot models, the full-line DP can use the residual potentials `R_j` alone because slot normalizing constants factor out.

### Adjacent-slot repair — still rejected

The follow-up still requires an omitted coordinate to have greater `p_anywhere` than a current Top13 incumbent. For a K13 defined as the Top13 under that same score, this remains impossible except ties. A future challenger must instead permit a bounded sacrifice in primary anywhere score in exchange for preregistered migration evidence, preferably only when `M(K)` improves or under a fixed composite preservation score.

### Coalition challenger — promising but exact null needs structural odds offset

Marginal-conditioned pair overlap is a strong derivative idea. Ordinary hypergeometric overlap assumes conditional odds ratio 1, whereas exact uniform 5-of-50 sampling gives structural negative pair association (2x2 odds ratio approximately 0.7822222). A correct challenger should use a conditional distribution/log-linear offset preserving that exact structural odds ratio before empirical-Bayes shrinkage.

### Synthetic evidence — downgraded

The follow-up states that measured synthetic results were not actually available and supplies a simulation protocol instead. Any earlier claim that the synthetic probe had empirically proved null neutrality/signal sensitivity is therefore withdrawn from HEPS evidence credit.

### Shrinkage — re-derive

The proposed interpretation of `s_prior` as a fixed fractional prior weight is not established by the stated penalty `N/(2*s_prior)||theta||^2`. Future use should specify an explicit Gaussian prior or calibrate penalty curvature to expected Fisher information under the exact null.

### Physical-regime research

Machine/ball-set metadata remains the highest-value independent-information proposal. Observed exogenous regime labels with hierarchical shrinkage are preferred. The proposed latent 2–4-regime EM mixture is deferred as too parameter-rich for the current Main sample.

Full details: `experiments/E0025/followup_red_team_2026-09-02.md`.

## Evidence credit

Apodex receives positive methodological credit for implementation scaffolding, governance priorities, an honest neutral replay result, and a useful nonlinear signed-transition basis proposal. No predictive `BREAKTHROUGH` or production authority is granted.
