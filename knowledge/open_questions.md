# HEPS Open Questions — Current Priority Registry

**Updated:** 2026-09-02

This file contains only active/high-value questions. The pre-cleanup question list is preserved in `knowledge/open_questions_archive_pre_2026-09-02.md`. Historical questions should not be revived without checking `governance/methodology_deprecations.md` and the latest claim/failure registries.

## Q001 — Does BARP HLR contain incremental direction information?

The 2026-09-01 frozen BARP modal vector `LLHHL` exactly matched the realized five-slot HLR vector.

This is encouraging but only one target.

Resolution requires:

- frozen full per-slot HLR probability vectors;
- comparison against `NULL_HLR_STRUCTURAL` and `NULL_HLR_JOINT_243` where appropriate;
- prospective Brier/log-loss, not only modal-vector hit rate;
- no parameter retuning from the 2026-09-01 success.

Primary path: `experiments/E0005/` plus Friday 2026-09-04 cycle scoring.

## Q002 — Can one signed-displacement transition model beat the old HLR×VVD field?

This is now the central Main acquisition question.

Can `MAIN_SIGNED_SLOT_TRANSITION` produce a better calibrated full-support field than:

- exact structural null;
- E0019 historical HLR×VVD product;
- simple frequency/recency;
- E0016 nonequilibrium current;
- marginal Top-K rules?

Primary gate: prospective proper-score improvement first, then matched K13 containment/recall.

Primary path: `experiments/E0021/`.

## Q003 — Can K13 improve without optimization over misspecification?

HEPS still targets K13 as the primary acquisition research basket, but an optimized K13 is not evidence by itself.

Required simultaneous conditions:

1. full probability field is calibrated better than structural/simple controls;
2. K13 recall exceeds matched-random/simple comparators;
3. catastrophic 0/1 exclusions do not worsen;
4. gains survive multiple prospective targets and independent reproduction.

E0019's line-containment objective is retained; its old probability operator is not.

## Q004 — Does adjacent-slot / anywhere-coordinate preservation improve fixed-K survival?

The 2026-09-01 draw motivates this question prospectively:

- 14 ranked strongly pre-draw in S2 but realized in S1;
- 16 ranked strongly across S1/S2 and realized in S2.

Test a bounded fixed-K challenger that may preserve up to two strong adjacent-slot coordinates by **displacing** existing K13 members. No K expansion or union credit.

Score exact-slot rank and anywhere-coordinate rank separately.

Primary path: E0021 adjacent-slot arm.

## Q005 — Which experts are genuinely independent information sources?

HLR, VVD, terminal digit and exact target coordinate derived from one sorted-slot transition are now one information family.

The active redundancy question concerns genuinely different sources such as:

- signed-transition field;
- E0016 nonequilibrium current;
- E0013 coalition topology;
- machine/ball-set metadata if prospectively available;
- any future exogenous mechanical covariate.

Resolution requires residual dependence and incremental proper-score/stage-isolation testing.

Primary path: E0011 redundancy audit.

## Q006 — Does E0013 coalition topology survive stronger marginal-conditioned controls?

E0013 remains one of the more promising learned downstream signals, but its discovery p-values are post-search and its graph should be challenged with stronger controls.

Do **not** subtract a supposed central-coordinate structural `P0(i,j)`; unordered anywhere-coordinate pairs have identical IID pair co-inclusion probability under 5/50.

Instead test a shrunk association statistic conditional on observed marginals `C_i,C_j`, then compare:

- original PPMI spectral;
- marginal-conditioned/shrunk spectral;
- raw pair counts;
- smoothed PMI without spectral projection;
- random/frequency/incumbent line ranking.

Coalition-only authority remains binding.

## Q007 — Does terminal symbolic dynamics add information as a separate calibrated model?

E0020's multiplicative terminal×HLR×VVD chain is rejected for acquisition.

The remaining legitimate question is narrower:

Can a prospectively frozen terminal model beat exact slot-specific terminal nulls on proper score, after multiplicity correction, and add incremental information when combined through a coherent ensemble rather than a likelihood product?

Until then terminal motifs remain diagnostic/hedge only.

## Q008 — Is there a real machine/ball-set non-exchangeability signal?

If a durable mechanical-era edge exists, persistent or regime-specific ball/machine bias is a higher-value hypothesis than inventing additional transforms of the previous winning numbers.

Required prerequisites:

- machine/ball-set state known or provenance-qualified before the target;
- no outcome-optimized regime boundary;
- strong hierarchical shrinkage;
- pooled versus machine-conditioned controls;
- proper-score and matched-exposure evaluation.

Unknown machine identity remains a hard limitation in the current ledger.

## Q009 — Can Richardson pair dispersion be converted to coherent exact joint inference?

The pair-separation estimator itself remains a valid shadow component, but E0016's geometric-mean message passing is heuristic and uses all ten slot pairs.

Test whether direct legal-line scoring with pair potentials and exact normalization improves proper score versus:

- structural pair null;
- incumbent slot field;
- heuristic Richardson marginals;
- simple pair baselines.

Main and XTRA must remain separate.

## Q010 — What is the correct near-term PowerBall model?

With the current small sample, conditional state counts are sparse.

The near-term championship should compare:

- uniform 1/16;
- strongly shrunk unconditional frequency;
- strongly shrunk exact-current-state conditional model;
- strongly shrunk VVD-state conditional model;
- a dependency-aware or pooled model only if preregistered.

Primary metric: proper score. Exact hit rate is secondary.

HLR/VVD/terminal/exact-state views of the same PB transition may not be counted as independent votes.

## Q011 — Can full-support modelling reduce catastrophic exclusions?

The 2026-08-21 and 2026-09-01 failures both show that candidate compression can lose useful information even when some upstream structure is correct.

Question:

Can a calibrated full-support field plus fixed-K containment optimization reduce catastrophic 0/1 survival without merely increasing K or flattening the field back to the null?

This is a core E0021/E0011 evaluation target.

## Q012 — Can portfolio diversification improve consistency without pretending to improve expectation?

Given large model uncertainty, how should HEPS allocate a fixed line budget to reduce concentration on noisy top-ranked lines while preserving calibrated line probability mass?

This is a variance/robustness question, not a claim that diversification changes the underlying lottery expectation.

## Resolution rule

When a question is resolved:

1. update `knowledge/claim_registry.jsonl` or `knowledge/failure_registry.jsonl`;
2. link the supporting experiment/review package;
3. mark the experiment/strategy status in `experiments/registry.csv`;
4. if a method is no longer safe to reuse, add it to `governance/methodology_deprecations.md`;
5. do not delete historical evidence.