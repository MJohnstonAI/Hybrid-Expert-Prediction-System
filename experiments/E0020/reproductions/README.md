# E0020 Reproduction

Run from repository root:

```bash
python scripts/main_terminal_motif.py --ledger data/draw_history.jsonl --trials 5000 --seed 20260901
```

The runner is standard-library only and uses Main post-2026-06-02 data. It does not read XTRA state.

An independent implementation is still required before any promotion review. Reproduction should verify exact terminal null aggregation, walk-forward target exclusion, suffix backoff, marginal-preserving shuffle controls, algebraic-rule expected hit counts, and M0-M3 coordinate scoring.