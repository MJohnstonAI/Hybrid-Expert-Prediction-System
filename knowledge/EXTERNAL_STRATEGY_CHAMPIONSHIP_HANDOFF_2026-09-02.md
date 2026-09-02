# External Strategy Championship Handoff — 2026-09-02

Experiment: `experiments/E0024/`

Read:

1. `experiments/E0024/results.json`
2. `experiments/E0024/decision.md`
3. `experiments/E0024/findings.md`
4. `experiments/E0024/protocol.yaml`
5. `experiments/E0024/red_team/README.md`

## Binding conclusions for other AI agents

### Portfolio

Do **not** replace E0022 `four_plus_first` Johnson with pure balanced-overlap selection for the HEPS 4+/5 objective.

At K13 / 20 lines:

- E0022 4+-first = `788/1287` 4+/5 winner states;
- E0024 exact 7/8 exposure-balanced nibble = `772/1287`.

Pairwise/exposure balance may be a secondary tie-break only when primary 4+/5 coverage is tied.

### Main machine state

Machine identity is a legitimate external covariate but has **no prediction authority** yet.

- permutation association p ≈ `0.181`;
- fixed tau=8 conditioning worsens Brier although K13 capture rises 17→21;
- a tau=64 retrospective five-target partition gives tiny Brier lift and K13 3→6.

Treat the tau=64 result only as a future research lead. Do not use it to revise Friday 2026-09-04 or any slate unless exact target machine information is prospectively available before ticket cutoff and the model is frozen and validated.

### XTRA machine state

Negative. No transfer from Main.

### Change points

No promotion:

- Main best corrected p ≈ `0.132`;
- XTRA ≈ `0.488`.

Do not create outcome-defined regimes.

### Physical video

No usable pre-outcome physical-motion dataset was found. Status `DATA_GAP_NOT_TESTABLE`.

### Highest-value follow-up

Obtain a reliable post-June ledger of `machine_name + ball_set` provenance. If equipment identity is not pre-cutoff observable, model a prospectively known distribution over the active equipment pool rather than using oracle target identity.

## Friday status

E0024 does **not** justify changing the frozen Main or XTRA Friday slates.
