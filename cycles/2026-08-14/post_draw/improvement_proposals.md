# 2026-08-14 Improvement Proposals

These are research proposals, not architecture promotions.

## 1. BARP — state-duration direction challenger

Formalize Grok's Boundary-Adjusted Run Persistence concept as a probabilistic HLR residual model. It should ask whether persistence/flip probability depends on current H/L run length after shrinkage toward `NULL_HLR_STRUCTURAL`.

Requirements:

- deterministic run definition;
- explicit handling of REPEAT;
- hierarchical shrinkage rather than discretionary bin pooling;
- full three-state probability output;
- walk-forward Brier/log-loss comparison against the exact structural null and plain empirical HLR.

## 2. VVD-R — distributional VVD residual

Replace brittle point-magnitude forecasts with a frozen probability distribution over legal displacement magnitudes:

`P(D_j=d) proportional to P0(D_j=d | previous slot) * R_j(d)`.

`P0` is `NULL_VVD_STRUCTURAL`; `R_j` is a heavily shrunk learned residual. The post-14-August `+2` residual on Slots1/3/5 is only a new challenger feature and receives no historical credit.

## 3. Coordinate Mobility / Slot Migration

Model global candidate survival separately from exact-slot assignment:

- `P(number n appears anywhere next draw)`;
- `P(number n occupies slot j | appears)`.

The 14 August winner14 is the motivating example: prior coordinate14 survived but migrated from Slot2 to Slot1. Earlier wrong-slot candidate hits should be audited similarly.

## 4. Coulomb expert-preservation rescue

Test a candidate-basket architecture in which strong independent Coulomb support receives protected rescue exposure even when slot consensus disagrees. A possible challenger is `Core9 + Rescue4 = K13`, but exact quotas must be earned by matched walk-forward tests.

Potential rescue families:

- exact structural rescue;
- Coulomb repeat/shadow preservation;
- coordinate-mobility rescue;
- adversarial/diversity rescue.

## 5. Joint VVD-Gap Residual

Gemini correctly identified the weakness of independent slot evaluation but its proposed JOS-HDR exact-line density is mathematically invalid under `NULL_GAP_DM`, which is uniform over exact legal gap compositions.

Repair the idea by modelling **feature-class residuals** rather than exact-line probability:

- span and span movement;
- min/max internal gap;
- boundary-gap mass;
- gap entropy/imbalance;
- gap-vector displacement;
- signed five-slot movement pattern;
- joint VVD structure.

Every feature class must be compared with its exact combinatorial base rate and heavily shrunk. The module initially scores joint compatibility only and has no hard-veto authority.

## 6. Orthogonal Main/XTRA rescue control

The director reported that an independently generated XTRA prediction contained Main winners14,39,44. Do not infer cross-game causality. Instead freeze Main and XTRA independently and measure cross-game winner rescue against matched random baskets of identical exposure.

Possible value: XTRA may act as an orthogonal anti-consensus diversification basket even if the games are statistically independent.

## 7. PowerBall direction versus exact-ball separation

Treat direction/state and exact PB magnitude as separate research questions. The LOW call from prior PB10 succeeded while exact `{5,8,9}` failed. Future PB experiments should score directional probabilities and exact-ball probabilities separately.

## 8. Do not retune Friday into a success

Specifically prohibited:

- redefining E0003 Slot1 VVD9 as a `9+/-2` success;
- adding VVD1 to E0004 Slot4 closure after seeing the result;
- claiming winner44 as an E0004 exact-slot success;
- backfilling the later conversation synthesis as a repository-frozen slate;
- treating the Main/XTRA 3-number overlap as causal evidence without exposure controls.
