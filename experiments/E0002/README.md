# E0002 — HEPS-Evolve v0.1

HEPS-Evolve is a quarantined evolutionary research engine for **Main 1-50 candidate ranking only**. It does not modify production HEPS experts, candidate authority, coalition assembly, morphology, winner-float ranking, portfolio selection, or PowerBall.

## Design principle

Use expensive models to invent genuinely new genes later; use ordinary Python to perform mutation, crossover, walk-forward scoring, null comparison, deduplication, caching, and survivor selection. The inner loop consumes **zero LLM tokens**.

## Why progressive screening

The engine deliberately does not score every organism against all 470 discovery targets from birth:

1. Tier 1: 80 deterministic evenly spaced discovery targets.
2. Tier 2: 200 targets.
3. Tier 3: all 470 discovery targets.
4. Only the final Tier-3 population may produce the frozen discovery champion.
5. Historical validation is opened only after the champion is frozen.

This makes small data a cheap **rejection filter**, not proof of signal.

## Run

```bash
python experiments/E0002/heps_evolve.py \
  --data experiments/E0002/data/train_main_2018_2025.csv \
  --seed-file experiments/E0002/seeds.json \
  --out-dir outputs/research/heps_evolve_e0002
```

Default search: population 100 × 20 generations, with progressive screening, 10 finalists, and 1,000 random validation trials.

Small engineering smoke run:

```bash
python experiments/E0002/heps_evolve.py \
  --data experiments/E0002/data/train_main_2018_2025.csv \
  --seed-file experiments/E0002/seeds.json \
  --out-dir outputs/research/heps_evolve_e0002_smoke \
  --population 40 --generations 5 --finalists 5 --null-trials 100 \
  --seed 20260807
```

## Tests

```bash
python -m unittest experiments/E0002/tests/test_heps_evolve.py
```

## Output

The engine writes:

- `results.json` — frozen champion, finalists, baselines, validation and random-null tails;
- `generation_summary.csv` — evolutionary progress and screening tier;
- `lineage.csv` — child-to-parent ancestry;
- `eval_cache.json` — reusable evaluation cache (generated output; do not treat as evidence by itself).

## Interpretation

A high historical fitness score means only **survive to harder testing**. It does not mean predictive breakthrough. Evolution searches too many hypotheses for ordinary historical p-values to be trusted without matched-search nulls and prospective frozen evidence.
