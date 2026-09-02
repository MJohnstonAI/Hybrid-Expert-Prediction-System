# E0013 Decision — Positive-PMI Spectral Coalition Ranking

## Decision

`RUN PROSPECTIVE SHADOW / NO PRODUCTION PROMOTION`

Evidence classification: `PROVISIONAL_SIGNAL`.

## Why this differs from E0012 SGCE candidate selection

E0012 found no acquisition lift from the supplied Jaccard/eigenvector-node ranking. E0013 uses spectral information only after the candidate universe is frozen and tests whether pair-community structure helps identify which candidates belong together.

The exploratory signal is strong enough to justify prospective preservation but not architecture authority because the PPMI spectral formulation was selected after comparing multiple graph variants.

## Authority

- may score completed lines in shadow: yes;
- may rank the frozen K universe in shadow: yes;
- may add/remove/prune candidates: no;
- may alter frozen historical portfolios: no;
- may influence future production portfolio allocation: no, pending prospective evidence/reproduction.

## Residual-control clarification — 2026-09-02

A proposed Longcat-style correction suggested subtracting a coordinate-specific structural pair probability `P0(i,j)` to remove supposed central-coordinate order-statistic geometry.

That correction is **rejected as formulated for E0013's graph**.

E0013 nodes are unordered coordinates appearing anywhere in a uniform 5-from-50 set. For every distinct pair `(i,j)`:

`P0(i,j)=C(48,3)/C(50,5)=20/(50*49)`.

This null is identical for every distinct coordinate pair, so there is no coordinate-varying central-pair structural bias to subtract.

A legitimate stronger E0013 challenger should instead control **observed coordinate marginals**, for example through a shrunk or conditional association statistic for `C_ij` given `C_i` and `C_j`, and compare it prospectively with the existing smoothed PPMI graph.

Do not replace the current graph with a mathematically vacuous constant-null subtraction merely because it is called residualization.

## First prospective target

2026-08-28. Shadow ranking over the already-frozen K13 is stored under `cycles/2026-08-28/pre_draw/e0013_ppmi_spectral_shadow.json`.

When acquisition fails to preserve all five winners, do not credit or blame E0013 for the missing coordinates.

## Promotion gate

Require repeated prospective winner-rank/percentile gain versus matched random, raw-pair, simple-PMI, frequency and incumbent ranking; a marginal-conditioned/redundancy audit; multiple-testing honesty; and independent reproduction before any core architecture change.

Current forward interpretation is governed by `governance/current_method_doctrine.md` and `governance/methodology_deprecations.md`.