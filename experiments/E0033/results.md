# E0033 Results — Last Three Main Draws

Evidence classification: `INSUFFICIENT_EVIDENCE`.

These are post-hoc stage-isolation results. They do not establish predictive lift.

## Frozen acquisition inputs

### 2026-09-01

Actual: `14,16,31,34,40`.

Frozen E0019 K13: `20,22,23,26,30,31,32,34,35,39,41,43,49`.

Actual winners already present: `31,34` (2/5). Missing winners injected: `14,16,40`. Exhaustive valid eight-decoy choices: 165.

### 2026-09-04

Actual: `4,7,27,38,50`.

Frozen official v35.3 K13: `3,8,18,19,20,23,32,34,35,39,40,48,50`.

Winner already present: `50` (1/5). Missing winners injected: `4,7,27,38`. Exhaustive valid eight-decoy choices: 495.

### 2026-09-08

Actual: `4,8,13,37,49`.

Frozen E0032 shadow K13: `2,4,5,14,16,19,22,24,27,31,34,39,40`.

Winner already present: `4` (1/5). Missing winners injected: `8,13,37,49`. Exhaustive valid eight-decoy choices: 495.

Total oracle-adjusted K13 universes scored: 1,155.

## Direct exact-line ranking remains weak

Median exact-winner rank among 1,287 lines under E0013 spectral:

- 2026-09-01: 1,062
- 2026-09-04: 1,108
- 2026-09-08: 735

No E0013 exact winner reached Top-20 in any replacement variant for these three targets.

Simple alternative exact-line rankers were also unstable. Frequency was relatively useful on 2026-09-01 (median exact rank 27; Top-20 in 31.5% of replacement variants) but failed on the next two. Positive-PMI was relatively useful on 2026-09-08 (median exact rank 162) but not on 2026-09-01 or 2026-09-04.

Conclusion: no tested direct five-line ranker consistently identifies exact 5/5.

## Four-node nucleus completion

The nucleus-completion idea is mathematically attractive but the tested nucleus rankers are not stable enough yet.

### E0013 spectral nucleus

Top-20 4+/5 success across oracle-replacement variants:

- 2026-09-01: 1.21%
- 2026-09-04: 0.00%
- 2026-09-08: 39.39%

Exact 5/5 Top-20: 0% on all three.

### Frequency nucleus

- 2026-09-01: Top-10 4+ = 53.33%; Top-20 4+ = 100%; exact Top-20 = 6.67%.
- 2026-09-04: Top-10 4+ = 0%; Top-20 4+ = 0%.
- 2026-09-08: Top-10 4+ = 0%; Top-20 4+ = 0%.

### Positive-PMI nucleus

- 2026-09-01: Top-10 4+ = 0.61%; Top-20 4+ = 6.06%; exact Top-20 = 0%.
- 2026-09-04: Top-10 4+ = 0.40%; Top-20 4+ = 2.63%; exact Top-20 = 0%.
- 2026-09-08: Top-10 4+ = 51.92%; Top-20 4+ = 100%; exact Top-20 = 1.82%.

The strongest nucleus lane changed by target: frequency on 01-Sep, PPMI on 08-Sep, and none worked on 04-Sep. This is evidence of instability, not a promotable rule.

## Geometry-first Johnson result

The accepted E0022 `four_plus_first` Johnson geometry was much more robust for the 4+/5 objective.

Without changing K13 and without using target information to select lines, the deterministic Johnson portfolios achieved the following 4+/5 coverage across the exhaustive oracle-replacement universes:

### Budget 10

- 2026-09-01: 82.42%
- 2026-09-04: 39.60%
- 2026-09-08: 28.28%

### Budget 20

- 2026-09-01: 92.12%
- 2026-09-04: 88.89%
- 2026-09-08: 76.36%

Exact 5/5 presence in the 20-line Johnson set:

- 2026-09-01: 0%
- 2026-09-04: 6.06%
- 2026-09-08: 0%

This is deterministic coverage behavior, not predictive information.

## Geometry-first + PPMI ordering

A useful new observation is that Johnson can first choose the fixed 20-line 4+/5 coverage set, after which a pre-target coalition score can reorder those same 20 lines without changing Top-20 coverage.

Reordering the already-selected Johnson-20 set by simple positive-PMI pair score produced:

| Target | Top-10 contains 4+ | Top-20 contains 4+ | Median first 4+ rank | Exact 5/5 Top-10 | Exact 5/5 Top-20 |
|---|---:|---:|---:|---:|---:|
| 2026-09-01 | 58.79% | 92.12% | 8 | 0% | 0% |
| 2026-09-04 | 44.65% | 88.89% | 10 | 2.83% | 6.06% |
| 2026-09-08 | 55.76% | 76.36% | 7 | 0% | 0% |

This is substantially more stable for **floating a 4+/5 line upward** than the direct E0013 or nucleus-completion rankers in these three targets.

The PPMI reordering result is post-hoc discovery. It does not revive simple PMI as a proven predictive assembler and must be frozen prospectively before receiving any credit.

## Main conclusion

The last-three-draw blind stage-isolation test rejects the idea that the current spectral nucleus ranker alone solves assembly.

The strongest practical finding is a two-layer assembly objective:

1. **geometry first:** choose a 20-line set that maximizes 4+/5 winner-state coverage inside a correct K13;
2. **ranking second:** reorder that fixed set using a separately defined coalition score, so ranking cannot destroy coverage.

On these three targets, simple positive-PMI ordering of the fixed Johnson-20 set floated a 4+/5 line into the Top-10 in roughly 45% to 59% of oracle-replacement variants while preserving 76% to 92% Top-20 4+/5 coverage.

Exact 5/5 remains unsolved. No tested ranker consistently places the true exact five-number coalition into Top-20, even when all five winners are guaranteed to be in K13.
