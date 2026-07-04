# HEPS Test Checklist

Before accepting any generated prediction or strategy update:

- [ ] `python scripts/validate_draws.py data/draw_history.jsonl` passes.
- [ ] `python scripts/sync_manifest.py --check` passes.
- [ ] `python scripts/simulate_null_model.py --trials 100000 --seed 20260704` reports a randomized null-model baseline.
- [ ] No target draw appears inside the training window.
- [ ] Prediction slate uses multiple portfolio lanes.
- [ ] No claim of guaranteed outcome.
- [ ] Any master architecture edit has a merge decision file.
