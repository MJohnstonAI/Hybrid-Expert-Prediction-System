# E0037 Decision: Information Ceiling and Anytime-Valid Prequential Gate

## Decision

`ACCEPT AS METHODOLOGY / RETROSPECTIVE NULL / FREEZE PROSPECTIVE E-PROCESS / ZERO SLATE AUTHORITY`

- Evidence classification (predictive): **`INSUFFICIENT_EVIDENCE`**. No lane accumulated evidence against the exact uniform null. The largest composite E was 1.35; the threshold is 80.
- Architecture status: `experimental`. The e-process monitor is proposed as `shadow` governance infrastructure, pending director review.
- Paper trading only. No slate was produced and no existing authority changed.

## What is accepted (methodology, not prediction)

1. **The information-ceiling theorem and tables.** Every downstream gain (K13 hits, catastrophe rate, 3+/4+ survival, portfolio events) is bounded by `D = KL(P_true||U)`.
   - The derived SESOI is `D_SESOI = 0.009388` nats/draw, the minimum information for a 10% K13 lift.
   - The ceiling explains why the K13 and assembly programme has not exceeded chance and cannot do so unless D is non-trivial.
2. **The prequential e-process as HEPS's proper-score gate and sequential rule.**
   - `log E = -sum Delta`, so the proper-score gate and the anytime-valid test are one object.
   - It is valid at every draw with no alpha-spending. It replaces the need for E0036's n=500 terminal checkpoint for detection purposes.
3. **Exact infrastructure.**
   - Chain DP with expectation semiring, verified against all 2,118,760 lines.
   - Elementary-symmetric product law, cross-checked against E0030.
   - M1 partition, cross-checked against E0032.

## Findings recorded

- **F-E0037-1. Official K13 record.** 14 hits in 10 frozen official Main K13 cycles against 13.0 expected (p=0.42). Catastrophes and 3+ counts are at random-basket rates.
- **F-E0037-2. E0036 Phase B implemented per the frozen spec.**
  - Main M1/M2a/M2b are worse than uniform on 28 retrospective targets.
  - XTRA shows no significant effect.
  - M2a and M2b are worse than M1 in both lanes (F6: the specific interaction bases add nothing).
  - The four post-freeze targets are specification-determined but the implementation came late. They are not significant.
- **F-E0037-3. E0036 Phase A correction from its own pilot rule.** The models' own σ is 0.21–0.61, against the provisional 0.0096. MDE80 at n=500 (0.026 for Main M1) exceeds the SESOI. E0036's checkpoints cannot resolve a practically important M1 effect.
- **F-E0037-4. E0036 M1 basket degeneracy.** The sign term behaves as a static coordinate-height tilt. On XTRA it produced the fixed K13 [38..50] on every target. That basket's October 3/4/4-of-5 hits are a band streak inside a z≈1.5 overall record, not transition evidence.
- **F-E0037-5. E0033 oracle-replacement is not exchangeability-calibrated.** Model-selected decoys plus random injected winners bias rankers correlated with the acquisition score. PPMI is effectively anti-frequency.
  - On 2026-09-08, a null random winner scores PPMI percentile 0.767, against 0.507 under random decoys.
  - The E0033 PPMI-ordering "float" result is largely artifact on that target and noise-level net of the artifact overall.
  - E0029's random-decoy construction is calibrated and unaffected.
- **F-E0037-6. Power.**
  - 10% relative ball bias: about 10 years to reach 88% detection probability.
  - 5% relative ball bias: 11.5% probability in 10 years.
  - At n=39, a 20% bias is detected 2% of the time.
- **F-E0037-7. PowerBall.** The pre-specifiable Dirichlet e-value for XTRA PB is 5.4 (anytime p=0.19), against the post-hoc familywise 0.040. The pre-specified test has not reached significance.

## Prospective freeze

- Start: the first draw dated on or after **2026-10-16**.
- Forecasters, weights, priors, τ grid, half-life, PB concentrations and thresholds are frozen exactly as in `hypothesis.md` and `protocol.yaml`.
- The frozen code is `scripts/e0037_prequential_gate.py` at the commit that adds this decision. The window `prospective_confirmatory_from_2026_10_16` is computed automatically from the ledger.
- Rejection rule: a lane's prospective composite E ≥ 80, over the four-lane family.
- Practical significance additionally requires the leading forecaster's prospective mean improvement to exceed 0.009388 nats/draw.
- Futility review at 100 prospective targets per lane.
- No forecaster may be added, removed or reweighted. Any change requires a new experiment ID and a fresh e-process starting at 1.
- **The prospective monitor produces probabilities for scoring only. It has no slate, K13, ranking, pruning or PowerBall-selection authority.**

## Recommendations to the director (not enacted)

1. Adopt the e-process as the HEPS proper-score gate. Require every future predictive claim to report its prospective log E.
2. Downgrade E0033's PPMI-ordering evidence. Stage-isolation constructions must use exchangeable (random-decoy) universes, or report the null-construction baseline next to every oracle result. Proposed deprecation-map row: see the Opus 5.5 report §F.
3. Stop generating new candidate-feature families until some field earns prospective log E > 0 trend. Each new family dilutes search exposure, and the ceiling shows downstream work cannot compensate.
4. Treat XTRA PB and the XTRA M1 high-band as the two leads to *monitor* prospectively under the frozen e-process. They have **no** authority.
