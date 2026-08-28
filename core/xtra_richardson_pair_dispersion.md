# XTRA Richardson Pair-Dispersion Shadow Expert

**Expert ID:** `XTRA_RICHARDSON_PAIR_DISPERSION`  
**Experiment:** `E0016`  
**Architecture status:** `shadow`  
**Evidence:** `PROVISIONAL_SIGNAL`  
**Mode:** `paper_trading_only`

## Purpose

Model whether the **separations between sorted XTRA slots** show forecastable expansion/contraction structure beyond the exact 5/50 pair-separation geometry, then feed only the residual information back into the existing distribution-first XTRA candidate field.

The name is inspired by Richardson turbulent pair dispersion. The operator is a statistical model of sorted slot separations; it is not a claim that lottery balls physically follow Richardson turbulence.

## Hard isolation boundary

- Use only `data/powerball_xtra_history.jsonl` from 2026-06-02 onward.
- Never use pre-June PowerBall Plus/XTRA history.
- Never import Main fitted states, candidate coordinates, pair counts, weights, or transition parameters.
- Main and XTRA may share the formula only.

## State representation

For every XTRA draw with sorted mains `S1<S2<S3<S4<S5`, define all ten pair separations:

`R_ab,t = S_b,t - S_a,t`, for `1 <= a < b <= 5`.

This is richer than adjacent-gap-only analysis because it includes both local and long-span slot relationships.

## Exact structural comparator

For each slot pair `(a,b)`, enumerate all legal `C(50,5)` sorted 5/50 lines and calculate the exact IID separation distribution:

`p0_ab(r) = P0(S_b-S_a=r)`.

This distribution is a comparator, not a predictive vote.

## Conditional Richardson estimator

For current separation `r_current`, use only historical transitions ending before the target.

Weight historical transitions by proximity of their previous separation:

`w_u = exp(-abs(R_ab,u - r_current)/5)`.

Freeze:

- kernel bandwidth `h=5`;
- structural shrinkage `kappa=8`.

Estimate the next separation distribution:

`p_hat_ab(r_next | r_current) =`

`(sum_u w_u * I(R_ab,u+1=r_next) + 8*p0_ab(r_next)) / (sum_u w_u + 8)`.

## Residual pair compatibility

For a legal candidate pair `x<y` assigned to sorted slots `(a,b)`, define:

`C_ab(x,y) = log(p_hat_ab(y-x | R_ab,current) / p0_ab(y-x))`.

Positive values mean that the candidate separation receives more support from the XTRA temporal model than from exact structural geometry alone.

Negative values mean less residual support.

## Distribution-first integration

Richardson must **not** hard-filter exact coordinates.

Start from the already-frozen XTRA slot marginals `base_j(n)` when available. If a standalone comparator is required, use exact sorted-slot structural marginals as the base.

For each pair `(a,b)`, propagate a message:

`m_a->b(y) = sum_x base_a(x) * exp(C_ab(x,y))`.

Normalize each message over legal coordinates in the destination slot.

For each slot `j`, combine inbound messages by geometric mean and multiply them into the base marginal. Renormalize to obtain a Richardson-updated shadow slot field.

Keep two artifacts separate:

1. exact-slot Richardson marginal `P_R(S_j=n)`;
2. global anywhere-coordinate marginal `P_R(n appears) = sum_j P_R(S_j=n)`.

Do not collapse these concepts prematurely.

## Shadow blend

For the E0016 prospective shadow lane:

- incumbent XTRA slot/global field weight: `0.50`;
- Richardson field weight: `0.50`;
- production Richardson weight: `0.00`.

The blend is counterfactual only and must not alter the authoritative XTRA prediction unless a later promotion decision explicitly grants authority.

## Required pre-draw outputs

Freeze before each eligible XTRA target:

- current ten-pair separation vector;
- exact structural pair-separation distributions/version hash;
- conditional Richardson distributions;
- residual pair-compatibility matrices;
- Richardson exact-slot marginals;
- Richardson global inclusion field 1..50;
- incumbent-vs-Richardson rank deltas;
- Richardson-only shadow K13/K20;
- 50/50 blended shadow K13/K20.

## Scoring

At identical K exposure, report:

- mean winner coordinate rank;
- K13 recall out of 5;
- K20 recall out of 5;
- K13 3+/5 indicator;
- catastrophic exclusion indicator;
- recall surplus versus exact matched K exposure;
- delta versus simple recency, frequency and incumbent XTRA field.

Do not credit Richardson for assembly outcomes when a winning coordinate was absent upstream.

## Current evidence

The E0016 post-June-only taste test reported directionally favourable XTRA results across 16 replay targets, including improved K13/K20 capture and mean rank, with combined K13 improvement on the final two canonical replay holdouts.

This is discovery evidence only. The sample is small and the approximate random-tail evidence was not confirmatory.

## Falsification

Downgrade or reject Richardson if prospective shadow results:

- fail to beat incumbent/simple controls at identical K;
- improve only by effectively increasing exposure;
- depend on one or two memorable targets;
- disappear after residualization against order-statistic/recency information;
- become unstable under small reasonable perturbations of training window.

## XTRA session instruction

The XTRA ChatGPT session should treat this expert as a **refinement layer over the current XTRA probability field**, not as a replacement architecture. It should diagnose which slot-pair separations contribute useful residual messages, prune redundant pair families only through evidence, and preserve Main/XTRA isolation throughout.
