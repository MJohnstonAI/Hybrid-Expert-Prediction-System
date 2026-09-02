# HEPS Pre-Draw Slate Supersession Policy

**Effective:** 2026-09-02  
**Authority:** binding governance clarification

## Principle

A HEPS pre-draw freeze is a **version lock**, not a prediction lock.

A frozen artifact may never be silently edited in place. However, before the target result is known, a materially improved method or corrected implementation may issue a new versioned prediction artifact that supersedes the earlier one.

Example:

`main_prediction_v35.json -> main_prediction_v35_2.json`

The earlier file remains immutable for audit and is marked `superseded_pre_draw`. The newest explicitly designated version becomes the active official forecast.

## Absolute boundary

Once the target result is known or reasonably available to the agent, no new prediction version may be created for that target and no existing prediction artifact may be altered.

## Requirements for pre-draw supersession

A new version must record:

1. the exact artifact it supersedes;
2. the reason for supersession;
3. the new method/operator or implementation correction;
4. whether the change is predictive, calibration, candidate-acquisition, assembly, portfolio-geometry, or PowerBall-only;
5. identical-exposure comparisons where applicable;
6. the time/date of the new freeze;
7. all prior versions remain available for post-draw scoring.

## Scientific scoring

Post-draw analysis must score:

- the final active pre-draw version as the official HEPS prediction;
- superseded versions separately as historical pre-draw counterfactuals;
- the incremental effect of the superseding change where possible.

Supersession does not erase prior evidence and does not permit outcome-conditioned retuning.

## Director authority

Before result reveal, the HEPS director may authorize a new official slate when a new experiment, mathematical correction, implementation fix, or portfolio construction is judged to improve the current prediction. This authorization does not waive evidence labels or permit retrospective claims.
