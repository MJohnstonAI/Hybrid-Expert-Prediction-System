# E0026 Implementation Erratum — 2026-09-04

## Status

`INVALIDATE FIRST PURE-M(K) FRIDAY CHALLENGER AS NON-CONFORMING E0026 IMPLEMENTATION`

Evidence classification remains `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Why the first challenger was invalid

The frozen diagnostic basket `[27,28,29,30,31,32,33,34,35,36,37,38,39]` was produced by maximizing aggregate complete-line mass after mixing scenario-conditioned fields.

That implementation preserved candidate-by-slot marginals `U_j(n)` but **discarded the scenario label at the K13 optimization stage**. This violated the E0026 research object:

`candidate + admissible slot provenance + scenario probability`.

For previous Main state `[14,16,31,34,40]`, coordinate 27 can occupy S1 only inside HLR scenarios with `S1=HIGH`. Under any scenario with `S1=LOW`, `F_1(27,s)=0` because `27 < 14` is false. The first implementation aggregated support across all scenarios and then allowed a K13 that contained no coordinate below 14, thereby assigning zero basket containment to every S1-LOW scenario regardless of their pre-draw probability.

Likewise, the basket contained no coordinate above 40, so it assigned zero basket containment to every S5-HIGH scenario.

This is not the intended slot-routed architecture.

## Correct E0026 semantics

Future E0026 code must retain scenario-specific support through compression:

- `R_j(n,s)=F_j(n,s) q_j(n|s,history)`;
- `P(L|s)` normalized only over legal sorted lines compatible with scenario `s`;
- `M_s(K)=sum_{L subset K} P(L|s)`;
- candidate provenance must remain `candidate + slot + scenario`, not only aggregated `U_j(n)`;
- aggregate `U_j(n)=sum_s w_s U_j(n,s)` may be reported but must not drive K13 alone.

The robust K13 objective must penalize or constrain catastrophic scenario loss. A valid form is a preregistered function of the scenario-specific masses, e.g. expected mass plus lower-tail protection, or explicit minimum coverage across all scenarios above a preregistered probability threshold.

## Friday artifact status

`cycles/2026-09-04/pre_draw/e0026_slot_routed_comparison_slate.json` remains immutable as an audit artifact showing the failure mode of aggregate pure-M(K) compression, but it is **not a valid E0026 prediction slate** and must not be credited as such after the draw.

The official v35.2 slate remains unchanged unless a corrected, separately frozen, pre-result E0026 challenger is produced.

## Scientific lesson

E0026 is not merely 'maximize M(K) on a mixture'. Its defining correction is to preserve **candidate identity, admissible slot provenance, and scenario probability together through the K13 compression stage**.
