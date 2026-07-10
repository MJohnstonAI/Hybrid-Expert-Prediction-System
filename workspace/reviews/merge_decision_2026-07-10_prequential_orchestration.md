# HEPS Merge Decision - Prequential Orchestration

## Proposal

`workspace/contributions/contributor_codex_2026-07-10_prequential_orchestration.md`

## Reviewer

Codex red-team pass, evidence constrained by repository rules.

## Date

2026-07-10

## Decision

- [x] Merge scoring infrastructure into the active workflow
- [ ] Merge coverage selection as the production default
- [ ] Merge new expert weights or a new predictive expert
- [x] Hold predictive changes for more data

## Accepted Changes

- Add executable prediction and lane scoring.
- Align scoring with the game objective by tracking exact 3/4/5-main bands and
  same-line 3+/4+/5-plus-PowerBall outcomes per submitted line.
- Add target-blind portfolio coverage diagnostics as an opt-in experiment.
- Add unit and CI validation for the new tooling.
- Replace single-draw automatic tuning doctrine with evidence accumulation and
  a minimum 20-target review checkpoint.

## Rejected Changes

- No promotion of midfield, hot/high, void, stiction, algebraic, or coverage
  variants based on the 10-row ledger.
- No claim that increased subset coverage is a predictive edge.

## Required Follow-Up

- Preserve future slates before their target draws.
- Score each slate after the canonical result is appended.
- Re-run the lane comparison after at least 20 independent scored targets.
- Define and test a true sorted-position feature before claiming that the
  documented lane is executable.

## Architecture Files to Update

- `core/heps_strategy.md`: clarify the calibration loop and frozen-weight gate.
- `outputs/post_game/self_improvement.md`: remove automatic single-draw rewrite
  behavior and use the canonical `.jsonl` ledger.

## Notes

This decision improves measurement quality, not lottery predictability. All
outputs remain paper-trading research only.
