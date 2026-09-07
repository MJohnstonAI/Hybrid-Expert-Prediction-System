# E0032 Upstream Probability-Field Screen — 2026-09-07

**Purpose:** prevent a mathematically correct K13 compressor from being attached to an obviously weak probability field.

**Evidence:** discovery / diagnostic only. No predictive promotion. No 2026-09-08 result was available or used.

## Screen A — two-parameter coherent signed-displacement tilt

A deliberately minimal Main field was tested as a diagnostic implementation of the E0021 doctrine:

`P_theta(x | p) proportional to exp(alpha * sum_j sign(delta_j) + beta * sum_j sign(delta_j)*log(1+abs(delta_j)))`

over legal sorted 5/50 lines, with exact dynamic-programming normalization and a fixed strong Gaussian shrinkage prior (`sigma=0.25`) on the two shared coefficients.

This is one transition information family and recovers the uniform legal-line null exactly at `alpha=beta=0`.

Using the current 28-draw Main ledger through 2026-09-04, an expanding-prefix diagnostic beginning after six observed draws produced mean target log-probability delta versus uniform of approximately **-0.05084 nats per target** (negative is worse). The full-current fit shrank close to zero (`alpha≈0.0319`, `beta≈-0.00156`).

Interpretation: the minimal signed-displacement tilt does not presently justify itself as the upstream predictive field.

## Screen B — coherent BARP-HLR residual line field

The frozen E0005 BARP slot probability formula was converted diagnostically into one coherent legal-line field by using each slot's BARP H/L/R probability only as a residual potential relative to the exact structural HLR mass, followed by exact legal-line normalization.

This integration is **new post-hoc methodology**, even though the BARP formula itself was frozen earlier, so the score below is discovery-only.

For targets 2026-08-18 through 2026-09-04, cumulative legal-line log-probability delta versus the exact uniform line null was approximately **-2.2916 nats**, or **-0.3819 nats per target**. The 2026-09-04 target alone was approximately **-1.4897 nats** versus uniform.

Interpretation: modal-direction anecdotes do not translate into a calibrated full-line probability advantage under this coherent integration.

## Decision

Neither screened field earns use as an authoritative E0032 upstream probability source. Numerical `K13_MEAN`, `K13_4PLUS`, `K13_5`, and `K13_ROBUST` baskets therefore remain **pending** rather than being frozen from a field that already fails the proper-score gate.

This is not a claim that no Main signal exists. It is a refusal to let improved compression mathematics disguise weak probability estimation.
