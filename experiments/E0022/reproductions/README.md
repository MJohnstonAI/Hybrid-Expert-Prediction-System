# E0022 Reproduction Guide

## Scope

Reproduce the oracle-K13 stage-isolation audit, tie-safe rank correction and deterministic Johnson 4+/5 coverage calculations.

No pre-June 2026 data are allowed.

## Runner

From repository root:

```bash
python scripts/oracle_k13_assembly_evolution.py \
  --reps 30 \
  --xtra-supplement experiments/E0022/xtra_replay_supplement.jsonl \
  --output outputs/research/e0022_oracle_k13_assembly_evolution.json
```

The XTRA supplement is explicitly noncanonical replay-only. It must not be used to update `data/powerball_xtra_history.jsonl`.

## Tests

Run the repository CI-compatible unit-test discovery:

```bash
python -m unittest discover -s tests -v
```

The E0022 tests verify:

- average-midrank tie handling;
- K13 has exactly 1,287 possible five-number winner states;
- a 10-line 4+-first Johnson portfolio covers 410 of those states at >=4/5;
- at budget 20, the evolved four-plus-first objective covers 788 states versus 757 for the historical three-plus-first objective;
- both 20-line portfolios still cover exactly 20 exact 5/5 states.

## Required interpretation

All E0022 predictive ranker results are post-hoc/discovery evidence because the strategies were designed after the replay outcomes existed.

Only the exact Johnson coverage arithmetic and tie-ranking correction are deterministic/methodological results. `MAIN_ASSEMBLY_DISSENT_OR` remains prospective shadow only.
