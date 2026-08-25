# E0011 Findings — Initial Synthesis

Evidence classification: `INSUFFICIENT_EVIDENCE`.

## What survives the Ox Alpha review

The strongest contribution is methodological rather than predictive.

- Exact structural nulls should be implemented as a complete comparator/calibration pipeline.
- Expert agreement must be residualized before it is treated as independent convergence.
- Prospective experiments need an explicit power/effect-size horizon rather than a fixed target count being mistaken for proof.
- PowerBall state-transition models should use shrinkage because exact-state observations are sparse.

## What does not survive

A pure structural-null global candidate field is flat: every main coordinate has inclusion probability 0.1 under IID 5/50. It therefore cannot select a superior K13 or identify 'high null mobility' coordinates. Ox Alpha's proposed null-mobility rescue is rejected as mathematically undefined.

The PowerBall frequency posterior is retained only as a baseline. The actual experimental question is conditional: what follows the current PB state and current PB VVD, after shrinkage toward simple baselines?

## Convergence correction

HEPS currently risks confidence inflation when several experts encode the same order-statistic or recency information. E0011 therefore treats convergence as an incremental-information problem rather than a vote count.

A source earns separate convergence weight only if it adds proper-score information after exact structural and recency controls, or if residual dependence is sufficiently low under a frozen rule.

## Tail rescue correction

Tail rescue remains a legitimate risk-control question after the 2026-08-21 failure, but it must preserve fixed total K. The proposed comparison is Core13 versus Core12+Rescue1 versus Core11+Rescue2. Rescue seats must come from a non-flat residual signal, never from the pure structural null.

## PowerBall correction

The preferred experimental ordering is:

`HLR distribution -> VVD distribution -> conditional exact-PB successor -> conditional VVD successor -> legal exact-ball translation -> residual convergence`.

If the paths disagree, HEPS should diversify rather than manufacture an exact-ball primary.

## Confidence

High confidence in the mathematical rejection of null-derived global candidate ranking; moderate confidence that residualization will improve calibration discipline; low confidence that any accepted component will improve actual hit rate until prospectively demonstrated.
