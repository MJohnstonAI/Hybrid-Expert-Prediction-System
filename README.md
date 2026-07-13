# Hybrid Expert Prediction System

Private HEPS research workspace for South African PowerBall mechanical-era analysis, paper-trading prediction experiments, blind backtests, and multi-agent strategy review.

## Purpose

HEPS is a file-based AI research engine. It keeps a canonical draw ledger, a master architecture file, AI-model contribution files, red-team reviews, prediction slates, post-game analyses, and self-improvement logs in one auditable GitHub workspace.

## Current modelling doctrine

- Use post-May/June 2026 South African PowerBall mechanical-era data as the active modelling dataset.
- Do not rely on the old pre-transition draw history as an active modelling dependency.
- Earlier HEPS strategies and algorithms may still be reused, but they must be recalibrated on the new active dataset.
- Treat all prediction slates as paper-trading research only.
- Never present a prediction as guaranteed, financially reliable, or actionable gambling advice.

## Repository structure

```text
configs/                  Agent rules and operating constraints
core/                     Master HEPS architecture and accepted strategy
data/                     Canonical draw ledger, manifest, schema
scripts/                  Validation and update utilities
workspace/contributions/  External AI model proposals
workspace/reviews/        Red-team critique, Q&A, merge decisions
outputs/predictions/      Prediction slate outputs
outputs/post_game/        Post-draw retrospective analysis
outputs/improvement/      Self-improvement tracker
outputs/research/         Machine-readable research and experiment artifacts
```

## Source of truth hierarchy

1. `data/draw_history.jsonl` — canonical mechanical-era draw ledger.
2. `data/draw_manifest.json` — current dataset state and latest draw.
3. `configs/agent.md` — rules all AI agents must follow.
4. `core/heps_architecture.md` — accepted HEPS architecture and strategy.
5. `workspace/contributions/` — sandboxed external AI proposals.
6. `workspace/reviews/` — red-team critique and merge decisions.
7. `outputs/` — generated prediction slates, post-game reports, and improvement logs.

## Current research handovers

AI agents evaluating ensemble architecture, the Coulomb family, July 2026 failures, or future blind-test design should read the following files before proposing changes:

1. `workspace/contributions/contributor_chatgpt_sol_2026-07-13_coalition_heps.md`
   - ChatGPT Sol's scenario-preserving coalition architecture;
   - candidate, assembly, and routing failure decomposition;
   - low-Coulomb topology proposal;
   - structural portfolio-diversity design;
   - walk-forward and matched-null protocol.
2. `workspace/reviews/red_team_chatgpt_sol_2026-07-13_coalition_heps.md`
   - independent limitations and promotion gates;
   - tiny-sample and multiple-search warnings;
   - required ablations and prospective evidence.
3. `outputs/research/chatgpt_sol_coalition_heps_experiment_spec_2026-07-13.json`
   - machine-readable architecture tournament specification.

These files are challenger research only. They do not modify the accepted architecture in `core/heps_architecture.md`.

## Standard workflow

1. Read `configs/agent.md`.
2. Read `core/heps_architecture.md`.
3. Read relevant current research handovers.
4. Validate `data/draw_history.jsonl`.
5. Generate a prediction slate under `outputs/predictions/`.
6. After the draw, append the actual result to the ledger.
7. Write post-game analysis under `outputs/post_game/`.
8. Record proposed improvements under `outputs/improvement/`.
9. Submit any architecture change as a proposal under `workspace/contributions/`.
10. Red-team the proposal before editing `core/heps_architecture.md`.

## Quick validation

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
```

## Append a draw

```bash
python scripts/append_draw.py --date YYYY-MM-DD --main 1,2,3,4,5 --pb 11 --machine "Khaya" --source-url "https://example.com/source"
```

## Score a stored prediction

After the target result has been appended and validated, score the preserved
pre-draw slate without automatically changing expert weights:

```bash
python scripts/score_prediction.py --prediction outputs/predictions/<stored-slate>.json
```

## Important correction

For the draw `21, 26, 40, 42, 44`, the macro-sum is `173`, not `193`.
