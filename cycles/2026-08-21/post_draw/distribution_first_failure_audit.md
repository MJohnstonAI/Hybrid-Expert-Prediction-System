# 2026-08-21 Main — Distribution-First Failure Audit

Verified result: `2,4,5,24,49 | PB4`.

Previous state: `3,7,20,31,39 | PB13`.

Actual Main HLR: `LLLLH`.

Actual Main VVD: `[1,3,15,7,10]`.

PB direction/VVD: `LOW / 9`.

## First failure stage

`candidate_acquisition`.

The pre-draw reasoning concentrated too strongly on a small number of HLR and VVD point hypotheses. This deprived legal alternate regimes of sufficient candidate exposure before coalition assembly could help.

## Failure decomposition

### S1 — 2

`3 -> 2`, LOW, VVD1. This was a simple adjacent shadow and should have retained explicit LOW-branch probability even if HIGH was the modal structural direction. Future S1 routing must preserve LOW/REPEAT/HIGH probability mass rather than convert the modal state into a veto.

### S2 — 4

`7 -> 4`, LOW, VVD3. This was not an intrinsically extreme movement. The failure was mainly directional over-concentration.

### S3 — 5

`20 -> 5`, LOW, VVD15. This was the principal tail displacement. It should not be retroactively promoted to a central pattern. Instead it motivates a fixed target-blind tail-rescue allocation.

### S4 — 24

`31 -> 24`, LOW, VVD7. The working HIGH scenario suppressed this branch. Global coordinate/mobility probability and alternate-direction mass should survive until K compression.

### S5 — 49

`39 -> 49`, HIGH, VVD10. Direction was correct, but the exact-coordinate shortlist was too narrow. High-register structural slot mass should have retained 49.

### PowerBall — 4

`13 -> 4`, LOW, VVD9. LOW direction was correctly favoured, but exact-ball components did not converge on 4. The correct lesson is not to invent a new algebraic rule for 9 after the result. Future PB confidence should be based on frozen convergence of direction, displacement and exact-state transition models.

## Architectural action

Research package `experiments/E0009/` now specifies the proposed correction:

`state -> direction distribution -> displacement distribution -> coordinate probability -> convergence -> candidate compression -> assembly`.

Key controls:

- full HLR probabilities rather than one hard vector;
- full VVD distributions rather than exact-point dominance;
- S1 as a scenario-routing anchor only, not a physical causal claim;
- full 1..50 marginal inclusion probabilities before K13;
- separate global-coordinate mobility probability;
- preregistered tail-rescue exposure;
- PB convergence confidence and diversification when components disagree;
- structural and matched-exposure null comparisons.

## Evidence decision

`INSUFFICIENT_EVIDENCE`.

This post-draw diagnosis is useful architecture research but receives zero predictive credit for the known 2026-08-21 outcome. E0009 must succeed prospectively before any promotion.
