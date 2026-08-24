# External AI Contribution: Null-First Architecture Improvements

## Contributor

Model / agent: ox-alpha (Cline)
Session type: collaborative brainstorming / architecture challenge
Self-selected role: meta-research auditor / architecture challenger
Canonical identifiers used per `governance/nomenclature.md`.

## Date

2026-08-24 (pre-freeze for prospective target 2026-08-25)

## Proposal Summary

Five recommendations, ordered by expected value:

1. **P1 — Null-first production baseline pipeline.** Build one complete end-to-end
   pipeline in which every learned expert is replaced by its exact structural null.
   This becomes the mandatory comparator, a fallback slate generator, and the bar
   any future learned expert must beat prospectively.
2. **P2 — Statistical-power honesty gate.** Add an explicit power analysis to the
   question registry so that Q001/Q002-class comparisons are labelled resolvable or
   `long_horizon` at n=24 active draws, preventing implicit post-hoc tuning pressure.
3. **P3 — Freezable tail-rescue rule** for `E0009`/Q022, preregistered before the
   2026-08-25 target: fixed 10% exposure to coordinates ranked lowest by null-first
   marginal but highest by global mobility.
4. **P4 — Expert redundancy residualization audit** (Q007): residualize the three
   production Coulomb/order-statistic experts against the exact slot null so that
   E0009 convergence confidence does not double-count correlated signals.
5. **P5 — PowerBall Dirichlet posterior** (Q023): symmetric Dirichlet-Multinomial
   posterior over the 1-16 field as the shrinkage-weighted successor distribution.

## Files Affected

If accepted after red-team review:

- New experiment package `experiments/E0010/` (or next free ID) housing P1/P3/P5
  protocol, results, findings, red-team, reproductions, decision files.
- Append-only addition to `knowledge/open_questions.md` (power-gate labels; no
  deletions).
- No change to `core/heps_architecture.md` or `core/expert_registry.yaml` from this
  session. Promotion follows `governance/promotion_policy.md`; this document claims
  no authority to promote anything.

## Proposed Strategy or Algorithm

### P1 — Null-first production baseline pipeline

Replace each learned stage with its exact structural counterpart:

- Slot marginals: `NULL_ORDER_STATISTIC_SLOT`,
  `P0(X_(j)=n) = C(n-1,j-1) * C(50-n,5-j) / C(50,5)`.
- Joint state weighting: `NULL_HLR_JOINT_243`, enumerated over all `C(50,5)`
  legal next draws relative to the frozen previous draw.
- Displacement weighting: `NULL_VVD_STRUCTURAL`, conditional on previous
  same-slot coordinate.
- Gap diagnostics: `NULL_GAP_DM = DirichletMultinomial(45, [1,1,1,1,1,1])`.

Pipeline:

```
previous draw -> joint-243 state mixture -> per-slot displacement distributions
-> full 50-coordinate marginal -> K13 basket by retained-mass maximization
-> assembly/morphology (unchanged) -> portfolio (unchanged)
```

Properties: zero fitted parameters; fully reproducible from the canonical ledger;
walk-forward clean by construction because nothing is fitted on outcomes.

Three uses:

1. mandatory matched-exposure comparator required by E0009 anyway;
2. complete fallback slate generator if time-constrained before a target;
3. the reference bar — any learned expert must beat it prospectively under
   proper scores at matched exposure before added authority.

### P2 — Statistical-power honesty gate

For each open question requiring paired prospective comparison, precompute the
minimum number of targets needed to detect a declared minimum effect (for example,
paired multiclass Brier delta of 0.01 versus the exact null) at a stated
significance level under a simple independence approximation, and record the
assumptions openly rather than pretending precision.

Questions whose resolution horizon exceeds practical collection get an explicit
`long_horizon` label in `knowledge/open_questions.md`. This makes stagnation a
declared property of the design instead of an implicit accumulation of unresolved
experiments.

### P3 — Freezable tail-rescue rule (E0009 component D / Q022)

Preregistered rule, frozen before target 2026-08-25:

1. compute the null-first marginal from P1;
2. compute global mobility `P(n appears anywhere)` from the same marginal
   summed over slots;
3. reserve exactly 10% of total candidate exposure for the legal coordinates with
   the lowest slot-marginal mass but the highest global mobility;
4. report which core candidates each rescue displaced, per Gate E of
   `collaboration/research_priority_board.md`;
5. evaluate only against identical total candidate exposure.

Target-blind by construction: the rule references no realized outcome. The
2026-08-21 S3 event (`20 -> 5`, VVD15) motivates the question but does not tune
the constant; 10% is declared here before evaluation and may be falsified like any
hyperparameter.

### P4 — Expert redundancy residualization audit (Q007)

For each of `MAIN_STICTION_SHADOW`, `MAIN_VOID_BRIDGE`,
`MAIN_SORTED_SLOT_DENSITY` (and optionally `MAIN_HARMONIC_BOUNDARY`):

1. score all active-era targets against their own historical outputs;
2. residualize each expert's scores against `NULL_ORDER_STATISTIC_SLOT` and a
   simple recency control;
3. compute the mutual rank correlation matrix of the residuals;
4. report which experts are statistically indistinguishable proxies of the same
   recency/order-statistic information.

Output feeds E0009 component F: convergence confidence may count only components
whose residuals are demonstrably not redundant.

### P5 — PowerBall Dirichlet posterior (Q023)

For the 1-16 field, maintain a symmetric Dirichlet-Multinomial posterior over the
next PowerBall value, updated only through the frozen formula (fast-speed update):

```
p(n) proportional to alpha + count of n in a declared window
```

with `alpha` fixed at preregistration. This satisfies E0009's requirement for
shrinkage-weighted successor distributions exactly, and plugs into the existing
convergence gate: high exact-ball confidence requires independent-path agreement;
disagreement triggers diversification.

## Evidence Claimed

None. This document proposes methods and preregistrations; it claims zero
predictive evidence and requests no evidence classification for itself. All
component concepts are already classified `INSUFFICIENT_EVIDENCE` in the registry,
and this contribution changes no classification.

## Backtest Method

Not applicable yet — no backtest is reported here. Evaluation plan when
implemented:

- strict walk-forward order per `governance/research_protocol.md` section 2;
- discovery/validation/prospective windows declared in the experiment package
  protocol before scoring;
- proper probability scores (multiclass Brier/log loss) versus exact structural
  nulls at matched exposure;
- candidate survival judged against exact retained probability mass
  (`C(K,5)/C(50,5)` for flat baskets), never raw hit counts;
- multiple-testing exposure recorded per package;
- replay over past targets labelled `post_hoc_replay` and given zero confirmatory
  weight.

## Risks / Failure Modes

- **Null-first pipeline may be unbeatable-by-construction noise**, revealing the
  uncomfortable possibility that no learned expert can ever beat geometry at this
  sample size. That is a valid scientific outcome, not a failure of the project.
- **Tail rescue trades central mass for tail coverage**: it must show net
  survival improvement at identical exposure or it degrades the primary K13 metric.
- **Power analysis under independence assumptions understates dependence** between
  consecutive-draw comparisons; treat horizon numbers as order-of-magnitude.
- **Residualization audit needs historical per-target expert outputs**; if frozen
  artifacts are incomplete for early cycles, coverage must be disclosed rather
  than reconstructed from memory.
- **This session could not execute the mandated validation scripts** because
  Python is unavailable in its environment. Any implementation must run:
  `python scripts/validate_draws.py data/draw_history.jsonl`,
  `python scripts/sync_manifest.py --check`,
  `python scripts/structural_null.py ...` per AGENTS.md section 15 before freeze.
- **Operational gap observed:** `cycles/2026-08-25/` contains XTRA artifacts but no
  Main pre-draw freeze while the draw is imminent. If P1 is approved, its fallback
  use case applies directly.

## Required Red-Team Questions

1. Is the P1 marginal computation exactly correct under the joint-243 mixture, i.e.,
   does summing legal completions preserve total probability mass at 1?
2. Does the 10% tail-rescue allocation implicitly increase effective K, and how is
   matched exposure enforced when rescued coordinates overlap core baskets?
3. Are the three production Coulomb/order-statistic experts genuinely distinct once
   residualized, or should two be demoted to aliases before E0009 convergence math?
4. Is a Dirichlet posterior over 16 balls distinguishable from simple frequency
   ranking at active sample sizes, or is P5 unfalsifiable decoration?
5. Do the power-analysis assumptions survive the dependence between consecutive
   walk-forward targets?
6. Does anything here conflict with the binding nomenclature or with E0001/E0007/
   E0009 frozen protocols?

## Merge Recommendation

- [ ] Accept
- [ ] Reject
- [x] Needs more testing

Recommendation: open a new experiment package carrying P1+P3+P5 as one
preregistered prospective shadow targeting 2026-08-25 or later, with P2 and P4 as
supporting methodology tasks inside the same package. Nothing here promotes any
expert or alters doctrine without reproduction, red-team review, and synthesis as
required by the constitution.

Paper trading only. These are experimental research artifacts, not gambling advice.
