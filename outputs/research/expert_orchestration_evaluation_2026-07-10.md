# HEPS Expert and Orchestration Evaluation - 2026-07-10

## Outcome

No new predictive expert or weight change is supported by the current 10-draw
mechanical-era ledger. The evidence does support an engineering improvement:
make post-draw scoring executable and auditable, and freeze expert weights until
enough independently generated slates exist for prequential calibration.

This work is paper-trading research only. It does not establish a durable edge
and is not gambling advice.

## Architecture Comparison

| Approach | Benefit | Failure Mode | Decision |
|---|---|---|---|
| Fixed documented 3/3/2/1/1 lane allocation | Simple and diversified in principle | The repo had no executable lane scorer or feedback record | Retain as the current generation doctrine |
| Retrospective grid-search winner | Finds combinations that fit the 10-row ledger | Selects the winner on the same targets used to report performance | Research-only; do not use for dynamic weights |
| Coverage-diverse portfolio selector | Raises unique three-number subset coverage | Higher coverage removed an observed 3-hit result in one prior hypothesis | Keep as an explicit experimental control |
| Prequential scoring with frozen weights | Creates comparable lane evidence without target leakage | Learns slowly and cannot manufacture signal from 10 rows | Implement now |
| Online adaptive expert weighting | Could eventually respond to changing evidence | With the current sample it would amplify noise and meta-overfit | Defer until at least 20 independent scored targets, then review rather than auto-merge |

## Reproducible Method

The ledger window was `2026-06-02` through `2026-07-07` (11 rows). Each
historical target was withheld and scored only from earlier rows. The compact
machine-readable report is
`outputs/research/expert_orchestration_evaluation_2026-07-10.json` and can be
recreated with:

```bash
python scripts/evaluate_expert_orchestration.py
```

The required baseline and validation commands also passed:

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
```

The null run estimated a per-line 3+ main-number rate of `0.472%`.
The exact uniform-random full-outcome probability is one in `33,900,160` per
submitted line (`C(50,5) * 16`), which remains visible even when a finite null
simulation records zero full matches.

## Expert Audit

Across eight targets with three or more prior training rows, a target-blind
top-10 number set has 1.0 expected hit per draw, or eight hits in total.

| Feature | Top-10 hits | Hits per draw | Mean rank of actual numbers |
|---|---:|---:|---:|
| midfield | 11 | 1.375 | 21.900 |
| residue partition frequency | 8 | 1.000 | 26.100 |
| high register | 8 | 1.000 | 27.025 |
| gap completion exposure | 8 | 1.000 | 28.475 |
| cold/void | 7 | 0.875 | 26.475 |
| pair bridge | 7 | 0.875 | 26.975 |
| hot frequency | 7 | 0.875 | 27.125 |
| Markov residue state | 5 | 0.625 | 27.425 |
| stiction/shadow | 5 | 0.625 | 31.400 |

Eleven midfield hits versus a chance expectation of eight is far too small a
difference to promote. More importantly, the accepted sorted-position momentum
lane is described in architecture documents but is not implemented as a
distinct executable feature in `feature_scores`. It should remain an explicit
implementation TODO rather than being silently approximated by `midfield`.

## Portfolio Audit

The new target-blind coverage selector increased the mean number of unique
triples in a 10-line portfolio:

- default HEPS, six-target window: `72.8` to `84.7`;
- prior hot/high hypothesis, six-target window: `79.7` to `98.0`;
- prior hot/void/high hypothesis, six-target window: `79.7` to `89.5`.

That structural coverage did not yield a held-out hit improvement. For the
prior hot/high hypothesis it removed the only observed 3+ event in both the
seven-target and five-target views. It is therefore not promoted.

## Implemented Improvement

`scripts/score_prediction.py` now validates and scores a stored pre-draw slate
against the canonical ledger. It reports:

- best overlap and exact/threshold 2+/3+/4+/5 line counts;
- same-line 3+/4+/5 main-plus-PowerBall outcomes;
- per-line rates so additional ticket volume remains visible;
- lane-level contributions;
- unique coordinate, pair, and triple coverage;
- mean and maximum cross-line overlap;
- obvious post-target leakage and malformed slate failures.

This closes the missing measurement loop without pretending that the current
sample can support automatic expert reweighting.

## Recommended Next Checkpoint

Generate and preserve slates before each future draw, score them after ledger
append, and review weights only after at least 20 independent scored targets.
At that checkpoint compare frozen expert lanes and the chaos lane using the same
KPIs and random/null baselines. Do not select a new expert from this 10-row
retrospective audit.
