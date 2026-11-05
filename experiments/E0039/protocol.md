# E0039 — Decade groups, transition residuals and fixed-K13 compression

Declared 2026-11-05 before evaluation. Role: hypothesis explorer, quantitative tester, implementation auditor. Evidence classification INSUFFICIENT_EVIDENCE; architecture status experimental; paper trading only. No production/slate/pruning authority requested.

## Hypotheses and scope

Test whether decade group structure, decade-specific occupancy or binned movement residuals improve full-support legal-line probability and fixed-K13 acquisition. This is a new full-field experiment, not reuse of E0023's minimum-conditioned downstream score upstream. Main is primary; XTRA is an independently fitted transfer check with pending official-source provenance. No PB model, portfolio or morphology pruning changes.

Data: unchanged active ledgers, 45 draws per lane through 2026-11-03. Expanding history; minimum six prior draws; 39 targets per lane. Report all 39 and last six separately. All results are known, including the last six from E0038: **post_hoc_replay**, no untouched validation or confirmatory credit. Snapshot/code hashes and full forecast parameters precede scoring in each iteration.

## Finite model library (no tuning)

Decades are 1–10, 11–20, 21–30, 31–40, 41–50; no alternative boundary search. Occupancy shell s=(s1,..,s5), sum=5. Exact null mass p0(s)=product C(10,sd)/C(50,5). Each shell contains product C(10,sd) legal lines.

1. GROUP: counts of sorted occupancy shapes (e.g. 2,2,1,0,0), shrunk to their exact null masses with concentration 20. Within a shape, retain null proportions over shells and uniform lines within shells. This symmetry implies every coordinate has marginal 0.1; check exactly. It may inform line grouping, not rank individual candidates.
2. SHELL: counts of 126 decade-specific shells, Dirichlet shrinkage to exact p0 with concentration 20; uniform lines within each shell.
3. SHELL_TRANS: shell counts conditional on previous occupancy **shape**, concentration 20 toward the prior-only SHELL distribution. This deliberately tests temporal information versus the unconditional comparator without sparse exact-shell-to-shell fitting.
4. VVD_RESIDUAL: per-slot absolute movement bins 0,1–3,4–10,11–49. For historical transitions accumulate observed bin counts O and expected counts E using the exact sorted-slot null conditional on each previous slot. Let b=E/n. Residual weight (O+20*b)/(E+20*b); if E=0 use weight1. For next-line slot j and coordinate x select weight by bin abs(x-pj). Normalize product of these **residual weights only** over legal sorted lines by exact DP. Do not multiply slot-null densities into the joint field.
5. SIGNED_RESIDUAL: same estimator with signed bins <=-11,-10..-4,-3..-1,0,1..3,4..10,>=11. Alternative to VVD, not an independent vote multiplied with it.
6. SAFE_MIX: 0.5 uniform plus 0.1 each of the five models, a fixed convex mixture of normalized laws. No fitted ensemble weights, retrospective selection or independent-evidence claim.

Comparators: uniform legal line, unchanged E0030 incumbent, cumulative frequency and recent5. No hyperparameter grid, additional window search, revised bins or outcome-chosen seed.

## Acquisition comparison

All models receive diagnostic top-marginal K13 with a shared seeded tie permutation (20261105 + lane*10000 + chronological index). Rounding only for tie decisions at 12 decimal places; probabilities remain unrounded. Retain candidate-slot marginals for transition models; top marginal is a benchmark, not an E0026 routed decision. GROUP has no predictive number ranking and its basket is explicitly a random tie control.

For SHELL and SHELL_TRANS additionally enumerate every allocation (k1,..,k5), 0<=kd<=10, sum=13. Compute exact mean hits, P(H>=4), P(H=5), P(H<=1) by independent hypergeometric allocation within each decade conditional on shell, then average with its forecast probability. Four objectives: mean, four-plus, five, minimize catastrophe. Ties within 1e-12 resolved lexicographically by allocation. Coordinates within selected decades use the same seeded tie order; no within-decade predictive information is claimed. These are exact global optima under the **shell model**, not under truth. Compare to the same-K random hypergeometric null and simple frequency, and disclose loss of mean hits when optimizing tails.

## Metrics and falsification

Primary: mean joint log-loss delta model minus uniform, negative better. Secondary: per-coordinate Brier, K13 total hits/mean, <=1 catastrophes, >=3/4/5 survival, full-line mass for allocation arms, paired SE. Report whole-window and final-six results without choosing a winner by window. No promotion if proper score loses to uniform, gain fails against simple controls or independent prospective confirmation is absent. Nominal e-values/p-values from this newly designed replay have no confirmatory use.

Search exposure: five new fields + one fixed mixture + four controls, two windows, two lanes, eight shell-allocation objective arms plus diagnostic top-K comparisons; one seed rule; extensive prior HEPS search unquantified. Six or 39 replay targets are inadequate to establish a durable small edge. No predictive promotion under any replay outcome. A prospective successor would need independent review, fixed multiplicity/sequential rules and a power plan before activation; this experiment creates no new prospective authority.

## Verification

Check exact shell null sums/counts; GROUP marginal symmetry; DP uniform recovery; compare non-flat DP normalizer and slot marginals with exhaustive 2,118,760-line enumeration; compare allocation probabilities to direct small-universe enumeration; verify all target forecasts depend only on history. Check model invariance under subtraction of a history-only feature constant: that centering cancels in a normalized exponential model and cannot repair coordinate-height collapse. Preserve all failed models and report all variants.
