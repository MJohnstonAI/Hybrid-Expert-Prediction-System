# Hybrid Expert Prediction System

Private HEPS research workspace for South African PowerBall mechanical-era analysis, paper-trading prediction experiments, blind backtests, and multi-agent strategy review.

## Purpose

HEPS is a file-based AI research engine. It keeps a canonical draw ledger, a master architecture file, AI-model contribution files, red-team reviews, prediction slates, post-game analyses, and self-improvement logs in one auditable GitHub workspace.

## Current architecture

**HEPS v33.3 — Coalition Assembly Breakthrough**

The accepted main-number synthesis method is now the **Coulomb Pair-of-Pairs + Anchor Coalition Assembler**. It preserves complementary expert evidence, generates supported pair structures, joins two disjoint pairs around an anchor, and selects the final portfolio jointly for coverage/redundancy rather than treating every expert line independently.

The 2026-07-31 retrospective diagnostic improved the previous best assembled overlap from **2/5 to 4/5** when the frozen candidate hierarchy already contained all five winners. The exact winning line was also present in the challenger set at rank **19 of 417**. This is treated as an architectural assembly breakthrough, not proof of a durable exact-win predictive edge.

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
outputs/research/         Research and backtest artifacts
```

## Source of truth hierarchy

1. `data/draw_history.jsonl` — canonical mechanical-era draw ledger.
2. `data/draw_manifest.json` — current dataset state and latest draw.
3. `configs/agent.md` — rules all AI agents must follow.
4. `core/heps_architecture.md` — accepted HEPS architecture.
5. `core/heps_strategy.md` — accepted expert and synthesis protocol.
6. `workspace/contributions/` — external proposals and discovery records.
7. `workspace/reviews/` — red-team critique and merge decisions.
8. `outputs/` — generated prediction, post-game, and research artifacts.

## Standard workflow

1. Read `configs/agent.md`.
2. Read `core/heps_architecture.md` and `core/heps_strategy.md`.
3. Validate `data/draw_history.jsonl`.
4. Generate expert candidate evidence and preserve provenance.
5. Run pair-of-pairs + anchor coalition synthesis.
6. Select nine model-driven lines jointly for coverage plus one chaos/control line.
7. Save the frozen prediction slate under `outputs/predictions/`.
8. After the draw, append the actual result to the ledger.
9. Score candidate recall separately from coalition assembly performance.
10. Write post-game analysis and improvement notes.

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

After the target result has been appended and validated, score the preserved pre-draw slate without automatically changing expert weights:

```bash
python scripts/score_prediction.py --prediction outputs/predictions/<stored-slate>.json
```

## Coalition assembly research chain

The 2026-08-01 ChatGPT Sol research package is now the evidence and review record behind the accepted HEPS v33.3 experimental core module:

1. `workspace/contributions/contributor_chatgpt_sol_2026-08-01_coalition_assembly.md`
2. `workspace/reviews/red_team_chatgpt_sol_2026-08-01_coalition_assembly.md`
3. `workspace/reviews/qna_grounding_chatgpt_sol_2026-08-01_coalition_assembly.md`
4. `workspace/reviews/merge_decision_chatgpt_sol_2026-08-01_coalition_assembly.md`
5. `scripts/coalition_cover_optimizer.py`
6. `outputs/research/chatgpt_sol_coalition_assembly_2026-08-01.json`

Key research finding: jointly optimized portfolio coverage can materially improve conditional 3+ assembly when the frozen candidate pool already contains all five winners. The pair-of-pairs + anchor model is therefore accepted as the preferred experimental synthesis method, while exact 5/5 remains dependent on whether expert interaction scores can distinguish the correct coalition prospectively.

## Important correction

For the draw `21, 26, 40, 42, 44`, the macro-sum is `173`, not `193`.
