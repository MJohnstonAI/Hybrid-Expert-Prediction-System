# HEPS Test Checklist

Before accepting any generated prediction or strategy update:

- [ ] `python scripts/validate_draws.py data/draw_history.jsonl` passes.
- [ ] Latest draw in `data/draw_manifest.json` matches the ledger tail.
- [ ] No target draw appears inside the training window.
- [ ] A random-filtered baseline is reported.
- [ ] Prediction slate uses multiple portfolio lanes.
- [ ] No claim of guaranteed outcome.
- [ ] Any master architecture edit has a merge decision file.
