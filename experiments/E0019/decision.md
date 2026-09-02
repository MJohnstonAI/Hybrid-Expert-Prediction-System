# E0019 Decision

## Original decision

`RUN PROSPECTIVE SHADOW / DO NOT PROMOTE`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

The 2026-09-01 pre-draw artifact remains immutable and must continue to be scored exactly as frozen.

## 2026-09-02 mathematical review

### Retain

The **complete-line containment objective** remains methodologically useful:

`M(K) = sum of modeled legal-line probability mass for all 5-number lines contained inside K`.

This objective is better aligned with candidate acquisition than simply taking the top K marginal coordinates, because it measures the modelled probability that all five future winners survive the candidate basket.

### Supersede / reject for forward use

The historical E0019 probability operator:

`sqrt((P_BARP/P0_HLR) * (P_VVDR/P0_VVD))`

is **superseded and must not be reused in new predictive models**.

Reason:

- HLR is the sign of the sorted-slot transition;
- VVD is the absolute magnitude of that same transition;
- multiplying their residual ratios treats one information source as if it were two;
- the geometric mean attenuates but does not remove this double-counting;
- the underlying combined probability field was worse than flat on proper score in the discovery replay.

This is now recorded in `governance/methodology_deprecations.md` and `knowledge/failure_registry.jsonl`.

## 2026-09-01 prospective score

Actual Main: `14,16,31,34,40 | PB4`.

Frozen E0019 primary K13:

`20,22,23,26,30,31,32,34,35,39,41,43,49`

captured `31,34` = 2/5.

Exactly two hits at K13 is ordinary under the exact matched-exposure null and receives no promotion credit.

The diagnostic K20 additionally retained `40`, but K20 remains exposure diagnostic only.

## Successor requirement

Any E0019 successor must:

1. use one coherent signed-displacement transition representation per slot, or another explicit dependency model;
2. avoid multiplying HLR and VVD as independent evidence;
3. normalize over legal lines when feasible;
4. score the full probability field on proper scores before interpreting K13 recall as predictive lift;
5. retain the line-containment objective as a comparator;
6. preserve exact-slot and anywhere-coordinate scoring separately;
7. use matched K/exposure controls.

The intended successor research path is E0021.

## Current status

- Historical frozen E0019 arm: **immutable / scoreable**.
- E0019 HLR×VVD probability field: **REJECT for forward reuse**.
- E0019 line-mass containment objective: **retained as a research objective**.
- Production authority: **none**.
- Evidence classification: `INSUFFICIENT_EVIDENCE`.