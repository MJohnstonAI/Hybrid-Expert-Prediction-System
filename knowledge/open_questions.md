# HEPS Open Questions — Current Priority Registry

**Updated:** 2026-09-05

This file contains only active/high-value questions. Historical questions remain archived and must not be revived without checking current doctrine, deprecations, claim/failure registries, and the latest cycle evidence.

## Q001 — Does BARP HLR contain incremental direction information?

Prospective observations now include:

- 2026-09-01: frozen modal `LLHHL`, realized `LLHHL` — 5/5 direction hit;
- 2026-09-04: frozen slotwise modal `LHLHH`, realized `LLLHH` — 4/5 direction hit.

These are encouraging but still too few for promotion. Resolution requires frozen full probability vectors and prospective proper-score comparison against `NULL_HLR_STRUCTURAL` / `NULL_HLR_JOINT_243`, without retuning from either target.

Primary path: E0005 plus future prospective cycle scoring.

## Q002 — Can one signed-displacement model beat structural/simple controls?

Can `MAIN_SIGNED_SLOT_TRANSITION` produce a better calibrated full-support legal-line field than exact structural nulls, simple frequency/recency and rejected historical transition products?

Primary gate: prospective log/Brier improvement first, matched-K acquisition second.

Primary path: E0021.

## Q003 — What is the mathematically optimal fixed-K13 acquisition objective?

HEPS currently retains complete-line containment mass `M(K)` as a useful objective, but it is not assumed optimal.

The 2026-09-04 failure shows that aggregate mass optimization can under-protect plausible opposing-tail scenarios. Required research should compare expected containment with scenario-conditioned, lower-tail/CVaR, catastrophic-exclusion and one-seat-regret formulations while keeping K exactly 13.

This is the highest-value hard research problem and a candidate for external frontier-model review.

Primary path: E0026 successor research.

## Q004 — Can scenario-constrained slot routing reduce catastrophic exclusions?

The official 2026-09-04 K13 retained only `50` from `4,7,27,38,50`, despite the transition model assigning nonzero mass to the realized `LLLHH` scenario. The superseded E0026-R basket retained `38@S4` and `50@S5` in their primary routed slots.

Question: can candidate + admissible slot + scenario probability be converted into materially better fixed-K13 survival without collapsing to unrestricted anywhere marginals or sacrificing proper score?

Required controls:

- random K13;
- frequency/recency K13;
- marginal signed-transition K13;
- E0021 incumbent;
- E0026 routed and robust variants.

Primary path: E0026.

## Q005 — Can K13 protect plausible opposing-tail movement?

The 2026-09-04 realized signed transition was:

`[-10,-9,-4,+4,+10]`.

HEPS needs a preregistered stress criterion that asks whether a fixed K13 retains legal-line support under plausible simultaneous deep-low lower slots and high upper slots, without target-specific tuning and without increasing K.

This is a risk-control problem, not permission to train toward `4,7,27,38,50` retrospectively.

## Q006 — Which experts are genuinely independent information sources?

HLR, VVD, terminal digit and exact coordinate are one transition information family. The unresolved question concerns incremental information from genuinely different sources such as:

- signed transition;
- E0016 chronology/current;
- E0013 coalition topology;
- candidate-frozen whole-line delta patterns;
- machine/ball-set metadata if prospectively available.

Resolution requires residual-dependence and incremental proper-score/stage-isolation testing.

Primary path: E0011 redundancy audit.

## Q007 — Does E0013 coalition topology survive stronger marginal-conditioned controls?

E0013 remains coalition-only `PROVISIONAL_SIGNAL`. Test shrunk association conditional on observed coordinate marginals `C_i,C_j`, then compare with original PPMI spectral, raw pair counts, smoothed PMI, frequency, random and incumbent rankings.

Do not invent a coordinate-varying central-pair structural null under uniform 5/50.

## Q008 — Can E0029 Pattern-OR earn real triage authority?

E0029 remains `INSUFFICIENT_EVIDENCE` / prospective shadow.

Its first fresh target, 2026-09-04, could not score exact-winning-line gate survival because four winners were absent from K13 upstream. Therefore the prospective evidence counter remains effectively unresolved for the stage-isolated winner-line question.

Promotion requires multiple future targets where all five winners survive K13, with gate survival materially above line-retention fraction and no post-hoc retuning.

## Q009 — Does E0028 LDSAD survive prospectively?

The discovery-derived fixed band `11..13` scored its first fresh hit on 2026-09-04 with actual LDSAD `11`.

This is one prospective shadow success only. Continue scoring the frozen band and adaptive residual formulation against exact structural-null retention and matched random bands. Do not widen/move the band based on outcomes.

## Q010 — Is there a real machine/ball-set non-exchangeability signal?

If a durable mechanical-era edge exists, prospectively known physical metadata may be more valuable than additional transforms of past winning numbers.

Prerequisites remain known/qualified machine or ball-set state, strong hierarchical shrinkage, pooled controls and no outcome-optimized regime split.

## Q011 — What is the correct near-term PowerBall model?

The deterministic Director motif `VVD10 -> next two VVD sum to 12` failed its first fresh test on 2026-09-04 and should not be reused as a predictive rule.

The legitimate question is broader: can a strongly shrunk PB model beat uniform `1/16` prospectively on proper score?

Compare:

- uniform;
- unconditional Dirichlet shrinkage;
- exact-state conditional shrinkage;
- VVD-state conditional shrinkage;
- any coherent dependency-aware model fixed before target reveal.

Primary metric: proper score; exact hits secondary.

## Q012 — What sample size is required to detect a real HEPS edge?

HEPS now needs an explicit information/power analysis for:

- fixed-K13 winner-coordinate lift;
- 3+/4+/5 survival;
- proper log/Brier improvement;
- multiple strategy/model search exposure;
- sequential stopping rules.

The aim is to distinguish "no detected edge yet" from "experiment is underpowered to resolve the proposed effect." This is a second high-value hard research task suitable for a frontier model.

## Q013 — Can portfolio diversification improve consistency without pretending to improve expectation?

Given model uncertainty, how should a fixed line budget reduce concentration while preserving calibrated line probability mass and high-order K13 coverage?

This remains a variance/robustness question. Johnson geometry receives no predictive-information credit.

## Resolution rule

When a question is resolved or materially updated:

1. update `knowledge/claim_registry.jsonl` or `knowledge/failure_registry.jsonl`;
2. link supporting experiment/cycle artifacts;
3. update `experiments/registry.csv` where applicable;
4. add unsafe historical methods to `governance/methodology_deprecations.md`;
5. preserve all historical evidence.
