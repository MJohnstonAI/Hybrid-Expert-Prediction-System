# E0009 Reproduction Plan

No independent reproduction has yet been completed.

## Required implementation

An independent reproducer should implement E0009 from the written protocol without using target outcomes in feature or weight selection.

For each walk-forward target:

1. construct exact structural slot, HLR and VVD baselines from the previous draw;
2. freeze any learned HLR residual probabilities;
3. freeze full per-slot VVD-R distributions;
4. derive slot-coordinate distributions and global 1..50 marginal inclusion probabilities;
5. apply a preregistered convergence weighting rule;
6. allocate any tail-rescue exposure using the frozen target-blind rule;
7. freeze K7/K10/K13/K16/K20 candidate baskets;
8. reveal the target and score proper probability metrics and candidate recall;
9. preserve all outputs, including losing variants.

## PowerBall reproduction

Implement the PowerBall field independently:

- full HLR probability vector;
- full VVD distribution;
- shrinkage-weighted exact-current-state successor distribution;
- shrinkage-weighted current-VVD successor distribution;
- exact-ball posterior/ranking after legal direction-displacement translation;
- convergence/conflict flag.

## Reproduction labels

Use one of:

- `code_reproduction`
- `independent_implementation`
- `conceptual_replication`

Independent implementation is preferred before any promotion decision.
