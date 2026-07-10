# External AI Contribution

## Contributor

Model / agent: Codex

## Date

2026-07-10

## Proposal Summary

Replace the aspirational single-draw dynamic-weight feedback loop with an
executable prequential scoring stage. Preserve current expert weights while the
mechanical-era sample is small. Keep a target-blind triple-coverage selector as
research infrastructure only.

## Files Affected

- `scripts/score_prediction.py`
- `scripts/portfolio_orchestration.py`
- `scripts/evaluate_expert_orchestration.py`
- `scripts/research_strategy_scaffold.py`
- `scripts/simulate_null_model.py`
- `tests/test_score_prediction.py`
- `tests/test_portfolio_orchestration.py`
- `tests/test_simulate_null_model.py`
- `.github/workflows/validate-draws.yml`
- `AGENTS.md`
- `README.md`
- `configs/agent.md`
- `outputs/research/expert_orchestration_evaluation_2026-07-10.json`
- `outputs/research/expert_orchestration_evaluation_2026-07-10.md`
- `core/heps_architecture.md`
- `core/heps_strategy.md`
- `outputs/post_game/self_improvement.md`

## Proposed Strategy or Algorithm

1. Store every prediction slate before its target draw.
2. Score the stored slate against the later canonical ledger row.
3. Record portfolio and lane metrics, including joint main-plus-PowerBall
   outcomes, exact 3/4/5 bands, submitted-line denominators, and cross-line
   coverage.
4. Do not alter expert weights from one result.
5. After at least 20 independently scored targets, compare frozen lanes against
   chaos/null baselines and submit any weight change through the review path.

The experimental coverage selector greedily balances stand-alone model utility
with newly covered three-number subsets. It never reads the target row.

## Evidence Claimed

- Ledger and manifest validation passed for 10 rows through `2026-07-03`.
- The required 100,000-trial null run estimated `0.472%` 3+ main hits per line.
- Existing number-level experts did not show robust superiority across seven
  withheld targets.
- Coverage selection increased mean unique triples but did not improve held-out
  hits and sometimes reduced them.
- The previous architecture referenced `scripts/score_prediction.py`, but the
  file did not exist; this contribution implements the missing measurement
  stage without enabling automatic reweighting.

## Backtest Method

For each target, feature scores and candidate lines used only earlier ledger
rows. Fixed hypotheses were compared over minimum-training windows of three and
five rows. The experiment retained negative results rather than choosing a new
winner.

## Risks / Failure Modes

- Ten rows are insufficient for reliable expert tuning.
- The earlier hot/high hypotheses remain meta-overfit because they were chosen
  after viewing retrospective results.
- A generated date on the target date is not proof of pre-draw generation;
  timestamp provenance still depends on preserving the artifact in version
  history before the result is known.
- More combinatorial coverage is not the same as predictive accuracy.

## Required Red-Team Questions

1. Does the scorer reject malformed and obviously post-target artifacts?
2. Are lane metrics descriptive rather than an automatic tuning trigger?
3. Does the coverage experiment improve held-out results, not just geometry?
4. Is the 20-target checkpoint a review gate rather than a claim of adequacy?

## Merge Recommendation

- [x] Accept scoring and validation infrastructure
- [ ] Accept coverage selection as the production default
- [ ] Accept new predictive weights
- [x] Needs more testing for all predictive changes
