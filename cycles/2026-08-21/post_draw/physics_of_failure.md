# Physics of Failure — Main 2026-08-21

Verified result: `2,4,5,24,49 | PB4`.

Previous state: `3,7,20,31,39 | PB13`.

Actual HLR: `LLLLH`; actual VVD: `[1,3,15,7,10]`; PB: `LOW`, VVD9.

## First failure stage

**Candidate acquisition.** The Main workflow over-concentrated on a narrow HLR/VVD point regime before the candidate universe was safely formed. Downstream assembly could not recover coordinates that had lost exposure.

## Slot attribution

- **S1=2:** `3 -> 2`, VVD1. Simple LOW/-1 shadow branch should have survived despite HIGH being the modal forecast.
- **S2=4:** `7 -> 4`, VVD3. Primarily a direction-routing miss, not an extreme displacement.
- **S3=5:** `20 -> 5`, VVD15. Principal tail event; motivates fixed target-blind rescue, not retrospective promotion of VVD15.
- **S4=24:** `31 -> 24`, VVD7. Alternate direction/global mobility mass was suppressed too early.
- **S5=49:** `39 -> 49`, VVD10. HIGH direction was correct, but exact-coordinate concentration excluded a structurally plausible high fifth-slot value.
- **PB4:** `13 -> 4`, LOW/VVD9. Direction was right; exact-ball components lacked genuine convergence.

## Root causes

1. hardening a probabilistic HLR view into a narrow scenario;
2. overweighting exact VVD/motif points relative to complete displacement distributions;
3. insufficient tail protection at fixed candidate exposure;
4. incomplete separation of global inclusion probability from exact-slot assignment;
5. hypothesis churn: attractive later narratives displaced calibrated probability mass.

## Corrective experiment

See `experiments/E0009/`.

Proposed order:

`state -> direction distribution -> displacement distribution -> coordinate probability -> convergence -> K compression -> assembly`.

No retrospective predictive credit is awarded. Evidence classification remains `INSUFFICIENT_EVIDENCE` until prospective testing.
