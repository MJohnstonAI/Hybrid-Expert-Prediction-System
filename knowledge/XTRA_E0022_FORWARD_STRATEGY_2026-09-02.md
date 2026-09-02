# HEPS XTRA Forward Strategy after E0022 — 2026-09-02

**Status:** active methodology handoff  
**Predictive assembly evidence:** `INSUFFICIENT_EVIDENCE`  
**Promoted XTRA predictive coalition assembler:** none  
**Paper trading only.**

## Binding execution order

For future XTRA targets:

1. maintain Main/XTRA fitted-state isolation;
2. build/freeze the XTRA probability field and candidate rankings from XTRA-only data;
3. freeze K13 before assembly;
4. score acquisition first at identical K;
5. enumerate all `C(13,5)=1,287` five-number lines from the frozen K13;
6. never hard-prune the 1,287-line universe by morphology before assembly evaluation;
7. use no promoted predictive XTRA coalition ranker, because E0022 promoted none;
8. if a shadow ranker is tested, use average-midrank tie handling and compare against simple/random controls;
9. optionally apply Johnson `four_plus_first` only after K13 and line budget are frozen;
10. freeze the final fixed-budget portfolio and score it separately from acquisition/ranking.

## Acquisition remains the primary predictive bottleneck

E0022 improves what HEPS does **after** a correct K13. It does not solve candidate acquisition.

If K13 omits any winner, the exact winning line cannot appear among the 1,287 assembly states. Therefore XTRA acquisition/Richardson research remains independent and upstream.

Richardson remains a shadow candidate-field refinement. Do not reuse its pair information as a second coalition vote without a new residualized experiment.

## Tie correction

The prior E0014 XTRA raw-pair oracle advantage is downgraded.

Reproduced mean winning-line percentile:

- optimistic best-in-tie: about `0.628`;
- average-midrank corrected: about `0.459`.

Therefore raw-pair ranking is not a predictive XTRA breakthrough.

Any future discrete ranker must use average midrank or another explicit tie-aware rule.

## No Main fitted-state transfer

Do not import Main E0013 spectral state, Main pair counts, Main frequency/recency state, or Main coalition rankings into XTRA.

Methodology may transfer only as a fresh XTRA-specific preregistered experiment.

## Johnson `four_plus_first`

Allowed as deterministic fixed-budget portfolio geometry after K13 is frozen.

For K13:

- 10-line 4+/5 state coverage: about `31.86%`;
- 20-line: about `61.23%`;
- 30-line: about `80.73%`;
- 50-line: about `97.20%`.

At 20 lines this improves the legacy `three_plus_first` geometry from about `58.82%` to `61.23%`.

This does **not** increase exact 5/5 probability under a uniform winner-state model. For M distinct submitted lines, exact 5/5 state coverage remains `M/1287`.

## Terminal / HLR / VVD caution from current doctrine

Terminal digit, HLR and VVD are deterministic projections of the same underlying slot transition. They may be reported as interpretable diagnostics, but they must not be multiplied or counted as independent convergence votes.

The earlier idea of resolving a terminal motif by separately multiplying terminal, HLR and VVD evidence is therefore diagnostic-only unless replaced by a coherent single-transition model and prospectively validated on proper scores.

## Future XTRA assembly reporting

Whenever all five winners are inside K13, report:

- exact winning-line rank among all 1,287;
- average-midrank percentile;
- Top-20 and Top-100 survival;
- catastrophic burial;
- 4+/5 coverage of the fixed-budget portfolio;
- exact 5/5 line inclusion;
- comparison with random/simple controls at the same line budget.

When K13 misses at least one winner, classify the first failure as acquisition and do not use downstream ranker performance to imply predictive success.

## Evidence language

- E0022 overall: `INSUFFICIENT_EVIDENCE` for prediction.
- XTRA raw pair: downgraded; no predictive authority.
- XTRA predictive coalition assembler: none promoted.
- Johnson four-plus-first: accepted deterministic portfolio geometry only.
- Richardson: upstream shadow/provisional candidate-field research, not assembly authority.
