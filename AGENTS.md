# HEPS Agent Collaboration Guide

This file is the root onboarding guide for AI agents collaborating on the Hybrid Expert Prediction System (HEPS). It summarizes the mandatory operating rules from the current repository. Keep future edits narrow, evidence-based, and grounded in observed repo workflows.

## Mission and Safety Frame

- HEPS is a private, proprietary, paper-trading research workspace for South African PowerBall mechanical-era analysis.
- All generated slates, backtests, and diagnostics are experimental calibration artifacts only.
- Never present any output as guaranteed, financially reliable, or suitable as gambling advice.
- Avoid language that frames HEPS output as a durable predictive edge unless it is supported by walk-forward/prospective validation and random/null baselines.

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
4. `core/heps_architecture.md` - accepted architecture doctrine.
5. `core/heps_strategy.md` - accepted expert and synthesis mechanics.
6. `workspace/contributions/` - external AI proposals.
7. `workspace/reviews/` - red-team, Q&A, and merge decisions.
8. `outputs/` - generated prediction, post-game, research, and improvement artifacts.

Do not use old pre-transition draw history as an active modeling dependency unless the user explicitly requests it and the work is clearly labeled as legacy analysis.

## Data and Validation Rules

- Main numbers are sorted order statistics, not physical draw order.
- South African PowerBall active bounds are five unique main numbers from `1-50` and one PowerBall from `1-16`.
- Preserve the known correction: `21 + 26 + 40 + 42 + 44 = 173`.
- If appending a draw, use `scripts/append_draw.py`; do not hand-edit ledger rows unless explicitly directed.

Validate before prediction, backtest, post-game analysis, or ledger changes:

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
```

For quick research or CI-style smoke checks, a smaller null-model trial count is acceptable only when clearly labeled as a smoke check.

## Modeling and Backtest Doctrine

- All model improvements must respect walk-forward validation: no target draw may appear inside its own training window.
- Random/null baselines are mandatory for claims of predictive improvement.
- In-sample pattern discovery is not evidence of a durable edge unless it survives out-of-sample testing.
- Treat the current post-May/June 2026 mechanical-era sample as small and provisional.
- Separate candidate-discovery performance from coalition-assembly performance.
- A selector receives no credit for winners that were absent from the frozen candidate pool.
- Distributional diagnostics should remain diagnostics unless the accepted combiner explicitly supports them as feature inputs.

## Accepted HEPS v33.3 Architecture — Coalition Assembly Breakthrough

The preferred main-number synthesis method is now the **Coulomb Pair-of-Pairs + Anchor Coalition Assembler**.

This is a synthesizer above the expert roster, not a new standalone expert. It preserves expert identity and searches for:

`pair_A + anchor + pair_B`

The two pairs must be disjoint and the anchor distinct from both. Candidate pair support may come from Coulomb void, stale-hot return horizon, stiction/±1/±2 shadow, adjacency/short-span geometry, pair bridge evidence, sorted-position compatibility, cross-expert consensus, and complementary role structure.

Dual-cluster structures are explicitly legal. Do not reject one low pair plus one high pair merely because the line looks over-clustered.

### 2026-07-31 breakthrough diagnostic

The frozen 17-number hierarchy contained all five actual winners `10,11,37,45,46`, while the previous submitted portfolio assembled at most 2/5. The new retrospective coalition diagnostic produced `02,10,11,37,46` for 4/5, and the exact winning line appeared at rank 19 among 417 pair-of-pairs + anchor challengers.

This is accepted as a **breakthrough in assembly architecture relative to HEPS v33.2**. It is not proof of a durable prospective exact-win edge.

### Required top-10 synthesis

- 3 pair-of-pairs + anchor champion lines;
- 2 void-led coalition lines;
- 2 tri-cluster/high-register coalition lines;
- 1 stiction or sorted-structure coalition line;
- 1 cross-expert maximum-coverage coalition line;
- 1 chaos/random-control line.

The nine model-driven lines must be checked jointly for redundancy and marginal pair/triple coverage. The chaos line remains outside the optimizer.

Before changing this accepted module, read the complete evidence chain:

1. `workspace/contributions/contributor_chatgpt_sol_2026-08-01_coalition_assembly.md`
2. `workspace/reviews/red_team_chatgpt_sol_2026-08-01_coalition_assembly.md`
3. `workspace/reviews/qna_grounding_chatgpt_sol_2026-08-01_coalition_assembly.md`
4. `workspace/reviews/merge_decision_chatgpt_sol_2026-08-01_coalition_assembly.md`
5. `outputs/research/chatgpt_sol_coalition_assembly_2026-08-01.json`
6. `scripts/coalition_cover_optimizer.py`

## Other Accepted Strategy Lanes

Maintain diversified expert evidence rather than one monolithic predictor:

- tri-cluster / high-register continuation;
- void-bridge / canyon-fill;
- stiction-shadow continuation;
- sorted-position momentum;
- stale-hot / return-horizon support;
- chaos / randomized baseline.

Treat tri-cluster as a portfolio component, not a universal forced rule. Treat mechanical hypotheses as provisional until enough post-transition evidence supports them.

## Historical Experimental Discovery — Dual-Synergy Candidate

The earlier 2026-07-10 aggressive dual-synergy work remains discovery history rather than accepted core replacement. Its first genuinely unseen target failed with a best overlap of one main number. Preserve its frozen artifacts and do not confuse it with the accepted v33.3 coalition assembler.

## Deprecated or Forbidden Reintroductions

- Do not reintroduce ink-mass weighting.
- Do not make physical drop-order, laminar-path, or pneumatic trajectory claims without true drawn-order data.
- Do not recreate deprecated modules from `docs/architecture_history.md` under new names.
- Do not treat sorted slots as physical ball trajectory data.
- Check proposed model features against `docs/architecture_history.md` so old failure modes are not reintroduced as proxy variables.

## Contribution and Merge Workflow

Architecture changes must use the repo's review path:

1. Write the proposal under `workspace/contributions/`.
2. Add a red-team review under `workspace/reviews/`.
3. Add a Q&A grounding log when unresolved evidence questions remain.
4. Add a merge decision before changing core architecture files.

## Artifact Destinations

- Prediction slates go under `outputs/predictions/` and must use `paper_trading_only`.
- Post-game analyses go under `outputs/post_game/`.
- Improvement proposals go under `outputs/improvement/`.
- Research and backtest outputs go under `outputs/research/`.

Prediction slates should include dataset state, target date, architecture version, candidate hierarchy/provenance, pair-of-pairs challenger summary, final portfolio, PowerBall ranking, coverage diagnostics, and uncertainty notes.

Post-game reports must include actual draw, candidate recall, pair recall, best generated coalition, best submitted overlap, PowerBall result, assembly failure stage, expert contribution notes, null comparison, and recommended adjustments.

## Engineering Rules

- Keep changes narrow and evidence-based.
- Prefer existing Python scripts and file-based workflows over introducing new frameworks.
- Add or update tests for mathematical feature work and no-leakage behavior.
- Preserve user or unrelated working-tree changes.
- Do not invent undocumented workflows to make the guide feel complete.

## Current Notes and TODOs

- `scripts/score_prediction.py` scores stored pre-draw slates against the canonical ledger and reports portfolio and lane evidence. It does not automatically tune expert weights from a single result.
- `scripts/coalition_cover_optimizer.py` is the reference research implementation for joint coverage optimization; production integration may be hardened without changing the accepted pair-of-pairs + anchor doctrine.
- Future validation should compare v33.3 against the previous independent-line selector and matched random controls.
