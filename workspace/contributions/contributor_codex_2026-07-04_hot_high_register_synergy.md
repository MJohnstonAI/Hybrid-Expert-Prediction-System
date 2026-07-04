# External AI Contribution Template

## Contributor

Model / agent: Codex

## Date

2026-07-04

## Proposal Summary

This contribution documents a research finding from the current South African PowerBall mechanical-era ledger (`2026-06-02` through `2026-07-03`, 10 rows). The strongest historical improvement came from a soft synergy between:

- hot-frequency recurrence;
- high-register continuation;
- Coulomb Void pressure as a secondary stabilizer.

The best walk-forward examples reached 3 main-number hits in a 10-line paper-trading slate. This is operationally meaningful for HEPS evaluation, but it is not yet statistically proven because the sample is small and multiple strategy variants were searched.

## Files Affected

- `scripts/research_strategy_scaffold.py`
- `outputs/research/strategy_scaffold_2026-07-04.json`
- `outputs/research/accuracy_experiment_2026-07-04.md`
- `workspace/contributions/contributor_codex_2026-07-04_hot_high_register_synergy.md`

No accepted architecture file was changed by this contribution.

## Proposed Strategy or Algorithm

The useful pattern was not a fully novel physics claim. It was a better feature combination:

1. **Hot-frequency anchor:** retain coordinates that have appeared more often in the current mechanical-era ledger.
2. **High-register continuation:** preserve exposure to the upper-number region, especially the `37-46` band that appeared repeatedly in the June 2026 data.
3. **Coulomb Void stabilizer:** include absence pressure so the slate does not collapse entirely into recently repeated values.
4. **Soft scoring only:** do not hard-reject numbers or sums; rank candidate slates by weighted features and keep multiple lines.
5. **Repeat/shadow PowerBall assignment:** test recent PowerBall repeat and +/-1/+/-2 support, but keep it provisional.

The two best-performing families were:

- `grid_triple_hot_cold_void_high_register`
- `grid_pair_hot_high_register`

## Evidence Claimed

Best targeted variant:

- strategy: `grid_triple_hot_cold_void_high_register`;
- feature mix: hot frequency + Coulomb cold/void + high-register continuation;
- min training rows: 3;
- candidate pool limit: 12;
- target draws tested: 7;
- best main-number overlap: 3;
- draws with 3+ main overlap: 1;
- draws with 4+ main overlap: 0;
- total 2+ lines: 8;
- total 3+ lines: 3;
- repeat/shadow PowerBall hits: 6.

Best 3-hit example:

- target date: `2026-06-16`;
- actual main numbers: `2, 19, 20, 40, 43`;
- generated line: `2, 39, 40, 43, 44`;
- hits: `2, 40, 43`;
- generated PowerBall: `5`;
- actual PowerBall: `11`.

Additional 3-hit examples appeared in the `grid_pair_hot_high_register` family:

- `2026-06-26`: generated `2, 37, 40, 44, 45`; actual `17, 26, 37, 40, 45`; hits `37, 40, 45`.
- `2026-06-30`: generated `2, 10, 40, 42, 44`; actual `21, 26, 40, 42, 44`; hits `40, 42, 44`.

## Backtest Method

The experiment used walk-forward evaluation:

1. Select a target draw.
2. Train/score only on rows with earlier `draw_date` values.
3. Generate 10 paper-trading lines.
4. Compare generated lines to the withheld target draw.
5. Repeat across target draws and strategy variants.

The experiment did not insert the target draw into its own training window. The full report is stored in `outputs/research/accuracy_experiment_2026-07-04.md`.

For context, a single random 5-number line has about a `0.48%` chance of matching 3+ main numbers against a target draw. A 10-line random slate has about a `4.68%` chance of at least one 3+ line. Across seven historical target draws, at least one 3+ event can still happen by chance before accounting for multiple strategy searches. Therefore, this finding should be treated as promising scaffolding, not proof.

## What Worked

- **The system did not chase one exact previous draw.** The best families combined recurrence with high-register pressure and cold/void balancing.
- **Soft governors worked better than hard filters.** No number was excluded outright because the current ledger is too small for fixed boundaries.
- **The high-register lane mattered.** The 3-hit examples consistently came from slates preserving the upper band where recent draws concentrated.
- **Feature synergy mattered more than single-lane purity.** Pure void, pure stiction, and pure high-register variants were less useful than hot/high-register or hot/cold/high-register blends.
- **The Coulomb family did contribute.** Coulomb Void was a weighted feature in the best targeted variant, while Coulomb Stiction / Shadow was useful as a tested trace feature but did not dominate the best result.
- **Walk-forward separation kept the result auditable.** Each target was evaluated using only earlier rows, so the 3-hit examples were not direct target leakage.

## Risks / Failure Modes

- The ledger has only 10 rows, so apparent success may be sample noise.
- The strategy search tested many variants; choosing the winner after seeing results creates meta-overfit.
- No variant reached a 4-main-number hit.
- The strongest variants are high-register-heavy, so they may fail if the next draw mean-reverts lower.
- Repeat/shadow PowerBall appeared useful mostly because recent PowerBalls repeated; this is not enough evidence for a durable PowerBall model.
- This contribution must not be represented as guaranteed, financially reliable, or suitable as gambling advice.

## Required Red-Team Questions

1. Does `grid_triple_hot_cold_void_high_register` continue to produce 2+ and 3+ main-number overlaps after at least 20 more mechanical-era draws?
2. Does it outperform a randomized null baseline after accounting for the number of strategy variants tested?
3. Is the high-register component genuinely useful, or is it only fitting the short June 2026 cluster?
4. Can the feature weights be selected before the target draw rather than after a retrospective sweep?
5. Does PowerBall repeat/shadow remain useful when evaluated across future draws, or was it only exploiting the recent `13`/`15` repeats?

## Merge Recommendation

- [ ] Accept
- [ ] Reject
- [x] Needs more testing

Recommendation: keep this as an experimental research lane. Do not merge it into `core/heps_architecture.md` until future walk-forward evidence shows persistence beyond the current 10-row sample.
