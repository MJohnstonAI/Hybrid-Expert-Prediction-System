# E0027 Decision — SmokeField / Non-Colliding Slot Diffusion

## Decision

`REJECT PREDICTIVE PROMOTION / RETAIN ONLY A GAP-PRESSURE REGULARIZATION NOTE`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## 1. Particle orientation / acceleration

`REJECT CURRENT FORM`.

Acceleration-persistence produced materially worse proper scores than the exact uniform legal-line null. Adding gap pressure repaired some of that overfit but the combined model remained far inferior to uniform.

Do not add acceleration, velocity persistence, Brownian drift, or diffusion width as a new independent Main expert from E0027.

## 2. Non-crossing particle constraint

`RETAIN AS EXISTING LEGAL-LINE GEOMETRY, NOT A NEW EXPERT`.

The useful part of the non-colliding-particle analogy is already enforced by HEPS legal ordering:

`x1 < x2 < x3 < x4 < x5`.

This is exact combinatorial geometry and receives no predictive vote.

## 3. Adjacent gap pressure

`DIAGNOSTIC / REGULARIZATION RESEARCH NOTE ONLY`.

Gap pressure modestly improved the tested signed-transition field:

- mean line log-score delta improved by about `+0.120`;
- mean coordinate Brier improved by about `-0.00306`;
- Brier improved on `14/19` eligible targets.

However:

- signed + pressure still remained worse than the exact uniform null;
- K13 mean winner capture did not improve over signed transition;
- there were no 4+/5 or 5/5 target containments;
- pressure alone had poor K13 acquisition performance.

Therefore the effect is interpreted as regularization of a misspecified transition model, not independent lottery information.

Future use is permitted only inside a new preregistered transition-model repair where pressure is treated as a dependent regularizer and the whole field must beat uniform/simple controls prospectively.

## 4. Horizontal pair-collision / separation ranker

`REJECT CURRENT FORM`.

In matched oracle-K13 tests with 100 random-decoy replicates per target:

- signed-transition winner percentile: `0.517629`;
- signed + pair weight 0.1: `0.517433`;
- signed + pair weight 0.25: `0.517090`;
- signed + pair weight 0.5: `0.517019`;
- pair collision only: `0.497486`.

No tested pair-collision weight improved the incumbent signed-transition ranker. Pair dynamics alone was essentially random.

Do not add pair-separation collision as a coalition expert from E0027.

## 5. Relationship to E0016 and E0026

E0027 strengthens E0016's earlier negative result for generic Main drift/diffusion. The more structured SmokeField formulation still fails to earn predictive authority.

E0026 remains conceptually distinct and active as a proposed acquisition refinement because scenario-constrained slot routing is a probability-consistency rule, not a smoke/diffusion claim.

The only SmokeField concept that should influence E0026 is the already-binding non-crossing legal-order constraint. Gap pressure may be tested later as a dependent regularizer inside a repaired transition field, never as an independent vote.

## 6. Friday 2026-09-04

`ZERO PREDICTION AUTHORITY`.

Do not revise the frozen Main K13 or Friday slate because of E0027.

## Architecture decision

**Do not add HEPS SmokeField, Brownian diffusion, particle acceleration, or pair-collision as predictive experts.**

Record E0027 as negative evidence to prevent rediscovery. Preserve only the narrow observation that adjacent-gap mean-reversion/pressure may deserve a future regularization test inside a stronger signed-transition model.
