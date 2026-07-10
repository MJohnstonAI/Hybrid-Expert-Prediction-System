# HEPS Q&A Grounding Log - Prequential Orchestration

## Open Questions

- What number of scored targets will ultimately be sufficient for stable lane
  weighting? This depends on effect size and baseline variance and is not known
  from the current ledger.
- How should a true sorted-position expert be defined in executable code? The
  current `midfield` feature is not a substitute for slot-specific calibration.

## Resolved Questions

- Does higher unique-triple coverage prove a better predictor? No. The held-out
  audit increased coverage without improving results.
- Should one draw automatically change gamma or expert weights? No. One result
  is recorded as evidence only.
- What is the next tuning gate? At least 20 independently generated and scored
  target slates, followed by review against random/null baselines. This is a
  minimum checkpoint, not proof of adequate sample size.

## Evidence Links / Source Notes

- `data/draw_history.jsonl`
- `outputs/research/expert_orchestration_evaluation_2026-07-10.json`
- `outputs/research/expert_orchestration_evaluation_2026-07-10.md`
- `scripts/simulate_null_model.py`

## Final Interpretation

Merge the measurement and validation loop. Hold all predictive weight changes,
the new coverage selector default, and any new sorted-position implementation
until future prequential evidence exists.
