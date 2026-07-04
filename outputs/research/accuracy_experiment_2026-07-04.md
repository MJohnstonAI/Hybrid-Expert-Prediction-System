# HEPS Accuracy Experiment - 2026-07-04

## Scope

Dataset: `data/draw_history.jsonl`, rows 1-10, draw dates `2026-06-02` through `2026-07-03`.

This is a paper-trading research scaffold only. Each historical target draw was scored from earlier rows only. Strategy selection after reviewing these results is still meta-overfit on a very small sample.

## Method

The research scaffold tested HEPS-style soft features:

- hot frequency;
- cold/void absence, corresponding to the Coulomb Void Potential expert;
- recency stiction and +/-1/+/-2 shadows, corresponding to the Coulomb Stiction / Shadow expert;
- recent pair-bridge support;
- midfield support;
- high-register continuation.

The first full scaffold report is stored at `outputs/research/strategy_scaffold_2026-07-04.json`.

An additional targeted sweep tested the strongest families across:

- `min_train` values: 3, 4, 5, 6;
- candidate pool limits: 12, 15, 18, 21;
- repeat/shadow PowerBall assignment.

## Best Historical Improvement

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
- actual main: `2, 19, 20, 40, 43`;
- generated line: `2, 39, 40, 43, 44`;
- main hits: `2, 40, 43`;
- generated PowerBall: `5`;
- actual PowerBall: `11`.

Second robust family:

- strategy: `grid_pair_hot_high_register`;
- best examples reached 3 main hits on `2026-06-26` and `2026-06-30` depending on pool/training settings;
- no tested setting reached 4 main hits.

## Coulomb Expert Contribution

The Coulomb family did contribute to the successful experiments, but not as a standalone winning expert.

- **Coulomb Void Potential** was directly weighted in the best targeted variant, `grid_triple_hot_cold_void_high_register`, as the `cold_void` feature.
- **Coulomb Stiction / Shadow** was tested directly and appeared in feature traces, but the pure stiction-heavy variants did not produce the best 3-hit result.
- The strongest result came from synergy: hot-frequency recurrence and high-register continuation selected the active band, while Coulomb Void pressure helped stabilize the slate by keeping absence pressure in the candidate pool.

In practical terms, the Coulomb expert was part of the success as a balancing/field-pressure component. It was not the sole driver.

## Failure Modes

- No honest walk-forward test found a 4-main hit.
- The best variants are dominated by recent hot/high-register structure, which can easily overfit the current 10-row sample.
- PowerBall repeat/shadow performed well historically because recent PowerBall values repeated, especially `13` and `15`; this is not enough evidence for a stable rule.
- The dataset is too small for statistical confidence. These results are useful as scaffolding, not as validation of a predictive edge.

## Next-Test Candidate From Best Targeted Variant

Generated from all current rows using `grid_triple_hot_cold_void_high_register`, candidate pool limit 12, repeat/shadow PowerBall assignment:

| Rank | Main Numbers | PowerBall |
|---:|---|---:|
| 1 | `2, 37, 40, 41, 43` | 15 |
| 2 | `2, 37, 40, 44, 46` | 14 |
| 3 | `2, 37, 41, 45, 46` | 16 |
| 4 | `2, 37, 43, 46, 49` | 13 |
| 5 | `2, 37, 43, 44, 45` | 1 |
| 6 | `2, 37, 41, 44, 47` | 2 |
| 7 | `2, 37, 43, 47, 48` | 3 |
| 8 | `2, 40, 41, 46, 49` | 4 |
| 9 | `2, 40, 43, 45, 46` | 5 |
| 10 | `2, 40, 41, 44, 45` | 6 |

## Conclusion

Success: the scaffold found repeatable 3-main-hit historical examples and improved the total 2+ line count over the earlier default pass. The Coulomb Void component was part of the best targeted feature mix.

Failure: it did not unlock any 4-main-hit result, and the apparent improvement is not statistically reliable on 10 draws. The best next action is to keep this as an experimental lane and require future walk-forward evidence before promoting it into the accepted HEPS architecture.
