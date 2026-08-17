# E0008 — XTRA FCPC Retrospective Walk-Forward Replay

Status: `DIAGNOSTIC_ONLY` / zero predictive credit

Series: South African PowerBall XTRA

Data boundary: 2026-06-02 through 2026-08-14 only. No Main state and no pre-June XTRA/Plus rows.

## Question

Does the FCPC architecture reveal marginal candidate information that a hard K13 winner-count championship could hide?

## Design

This is a retrospective blind walk-forward replay. For target draw t, every entrant may use only XTRA rows strictly before t. The proxy rule definitions are imported unchanged from the persisted FABLE-5 acquisition probe; they are not fitted or tuned to XTRA.

Warm-up: first 3 XTRA draws. Scored targets: 19, from 2026-06-12 through 2026-08-14.

Entrants:

- flat marginal null p_n = 0.1;
- frequency proxy;
- recency proxy;
- starvation proxy;
- +/-1/2 shadow proxy;
- equal-weight linear pool;
- equal-weight logarithmic pool.

Every non-flat entrant emits a 50-coordinate marginal vector with 0<p_n<1 and sum p_n=5, using the same normalization logic as `experiments/E0007/reproductions/fable5_acquisition_probe.py`.

## Gate 1 — Information detection

Primary diagnostic score: mean Bernoulli log loss across all 50 marginal inclusion coordinates. Lower is better. Report paired per-draw delta versus flat. Secondary: Brier delta.

This evaluates marginal inclusion information only; it says nothing about same-line dependence or coalition assembly.

## Gate 2 — K13 compression

Derive deterministic Top-13 from each vector and report:

- mean winners retained;
- lift versus exchangeable expectation 1.30;
- 0/1 catastrophic rate;
- 3+/5, 4+/5 and 5/5 rates.

## Dependency diagnostics

Report mean Spearman dependence between probability vectors and mean Top-13 basket overlap. Absolute dependence matters: anti-correlated rankings are not treated as independent evidence.

## Core9+Rescue4 proxy

Repeat the FABLE proxy rescue construction and compare four rescue seats with the displaced consensus seats 10-13. This is a diagnostic of architecture only, not the actual frozen HEPS E0007 expert definitions.

## Governance

- No result from E0008 may be claimed as prospective predictive evidence.
- No proxy result may be attributed to the actual HEPS production experts.
- Any shrinkage strength inspected after seeing these results is exploratory only and requires prospective freezing before credit.
- K13 remains an operational compression metric, not the primary statistical test.