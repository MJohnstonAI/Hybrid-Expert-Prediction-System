# HEPS Agent Collaboration Guide

This file is the root onboarding guide for AI agents collaborating on the
Hybrid Expert Prediction System (HEPS). It summarizes the mandatory operating
rules from the current repository. Keep future edits narrow, evidence-based,
and grounded in observed repo workflows.

## Mission and Safety Frame

- HEPS is a private, proprietary, paper-trading research workspace for South
  African PowerBall mechanical-era analysis.
- All generated slates, backtests, and diagnostics are experimental calibration
  artifacts only.
- Never present any output as guaranteed, financially reliable, or suitable as
  gambling advice.
- Avoid language that frames HEPS output as a durable predictive edge unless it
  is supported by walk-forward validation and random/null baselines.

## Source of Truth and Read Order

Before strategy, modeling, prediction, or architecture work, read:

1. `README.md`
2. `configs/agent.md`
3. `core/heps_architecture.md`
4. `core/heps_strategy.md`
5. `docs/architecture_history.md`

Use this source-of-truth order:

1. `data/draw_history.jsonl` - canonical mechanical-era draw ledger.
2. `data/draw_manifest.json` - current dataset state and latest draw summary.
3. `configs/agent.md` - detailed operating constraints.
4. `core/heps_architecture.md` - accepted architecture and strategy doctrine.
5. `workspace/contributions/` - external AI proposals.
6. `workspace/reviews/` - red-team, Q&A, and merge decisions.
7. `outputs/` - generated prediction, post-game, research, and improvement
   artifacts.

Do not use old pre-transition draw history as an active modeling dependency
unless the user explicitly requests it and the work is clearly labeled as
legacy analysis.

## Data and Validation Rules

- Main numbers are sorted order statistics, not physical draw order.
- South African PowerBall active bounds are five unique main numbers from
  `1-50` and one PowerBall from `1-16`.
- Preserve the known correction: `21 + 26 + 40 + 42 + 44 = 173`.
- If appending a draw, use `scripts/append_draw.py`; do not hand-edit ledger
  rows unless explicitly directed.

Validate before prediction, backtest, post-game analysis, or ledger changes:

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
```

For quick research or CI-style smoke checks, a smaller null-model trial count is
acceptable only when clearly labeled as a smoke check.

## Modeling and Backtest Doctrine

- All model improvements must respect walk-forward validation: no target draw
  may appear inside its own training window.
- Random/null baselines are mandatory for claims of improvement.
- In-sample pattern discovery is not evidence of a durable edge unless it
  survives out-of-sample testing.
- Treat the current post-May/June 2026 mechanical-era sample as small and
  provisional.
- The algebraic sequence feature module is calibration and diagnostic
  infrastructure, not a standalone prediction engine.
- Distributional diagnostics should be reported as diagnostics unless the
  existing combiner explicitly supports them as feature inputs.

## Accepted Strategy Lanes

Maintain diversified portfolio lanes rather than one monolithic expert:

- tri-cluster / high-register continuation
- void-bridge / canyon-fill
- stiction-shadow continuation
- sorted-position momentum
- chaos / randomized baseline

Treat tri-cluster as a portfolio lane, not a universal forced rule. Treat
mechanical hypotheses as provisional until enough post-transition evidence
supports them.

## Deprecated or Forbidden Reintroductions

- Do not reintroduce ink-mass weighting.
- Do not make physical drop-order, laminar-path, or pneumatic trajectory claims
  without true drawn-order data.
- Do not recreate deprecated modules from `docs/architecture_history.md` under
  new names.
- Do not treat sorted slots as physical ball trajectory data.
- Check proposed model features against `docs/architecture_history.md` so old
  failure modes are not reintroduced as proxy variables.

## Contribution and Merge Workflow

Architecture changes must use the repo's review path:

1. Write the proposal under `workspace/contributions/`.
2. Add a red-team review under `workspace/reviews/`.
3. Add a Q&A grounding log when unresolved evidence questions remain.
4. Add a merge decision before changing core architecture files.

Do not rewrite `core/heps_architecture.md` directly based on a single model
proposal. Record uncertainty explicitly; prefer a short TODO over unsupported
claims.

## Artifact Destinations

- Prediction slates go under `outputs/predictions/` and must use
  `paper_trading_only`.
- Post-game analyses go under `outputs/post_game/`.
- Improvement proposals go under `outputs/improvement/`.
- Research and backtest outputs go under `outputs/research/`.

Prediction slates should include dataset state, target draw date, branch or
version, generation timestamp, lane allocation, slate rationale, and uncertainty
notes.

Post-game reports should include the actual draw, slate hit counts, best
overlap, PowerBall result, +/-1 drift support, macro-sum/spread comparison,
expert contribution notes, recommended adjustments, and merge/no-merge decision.

## Engineering Rules

- Keep changes narrow and evidence-based.
- Prefer existing Python scripts and file-based workflows over introducing new
  frameworks.
- Add or update tests for mathematical feature work, especially residue
  partitioning, gap distributions, and no-leakage behavior.
- Preserve user or unrelated working-tree changes.
- Do not invent undocumented workflows to make the guide feel complete.

## Current TODOs

- TODO: `core/heps_strategy.md` references `scripts/score_prediction.py`, but
  that file is not currently present. Do not instruct agents to run it until it
  is implemented.
- TODO: Decide whether root `AGENTS.md` should replace `configs/agent.md` as
  the primary guide or serve as a root-level index pointing to it.
- TODO: Clean up stale references such as `/data/draw_history.json` in
  `outputs/post_game/self_improvement.md`; the actual canonical ledger is
  `data/draw_history.jsonl`.

