# E0011 Reproduction Plan

Required reproductions:

- **Null invariant reproduction:** independently enumerate all legal 5/50 combinations or use exact order-statistic formulas and confirm `P(n appears)=0.1` for all `n=1..50`.
- **Expert residualization reproduction:** reimplement structural+recency residualization and compare the residual Spearman matrix and incremental proper scores.
- **Tail-rescue reproduction:** run strict walk-forward fixed-K comparisons for Core13, Core12+Rescue1 and Core11+Rescue2 using only prospectively available rescue signals.
- **PB transition reproduction:** independently implement hierarchical exact-state and VVD-state transition posteriors and score against uniform/unconditional-frequency baselines.

Use only canonical ledger rows available before each target. Label all historical replay as `post_hoc_replay`; first confirmatory evidence begins 2026-08-28 or later.
