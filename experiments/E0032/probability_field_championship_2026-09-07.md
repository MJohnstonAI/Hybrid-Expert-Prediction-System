# E0032 Probability-Field Championship — 2026-09-07

**Target:** South African PowerBall Main, 2026-09-08  
**Cutoff:** canonical Main ledger through 2026-09-04, 28 draws  
**Evidence classification:** `INSUFFICIENT_EVIDENCE`  
**Status:** pre-target discovery / prospective-shadow preparation  
**Paper trading only:** yes

## Purpose

E0032 separates upstream probability estimation from fixed-K13 compression. This review asks which existing or narrowly-defined coherent Main probability field is sufficiently calibrated to justify feeding the Astra-derived K13 compression machinery.

The binding rule remains: proper score first, compression second. No field is promoted because a K13 optimizer produces attractive modeled utility.

## Fields reviewed

### Exact uniform legal-line null

`P0(L)=1/C(50,5)` for every legal five-number line.

This remains the proper-score control and cannot rank coordinates.

### E0030 adaptive uniform/frequency/recency mixture — extended without retuning

The already-defined E0030 algorithm was replayed unchanged through the current 2026-09-04 cutoff:

- component U: uniform coordinate-product law;
- component F: cumulative-frequency coordinate-product law with coordinate weight `1 + count/10`;
- component R: last-five-draw coordinate-product law with coordinate weight `1 + count_recent5/10`;
- initial component prior weights: `0.8 / 0.1 / 0.1`;
- each target updates component log weights using only the revealed target after its forecast;
- final mixture retains E0030's fixed 50% uniform floor through `effective=[0.5+0.5*posterior_U,0.5*posterior_F,0.5*posterior_R]`.

Across 23 target-excluded forecasts beginning after five observed draws, the extended Main replay gives:

- mean legal-line log-loss delta, model minus uniform: **+0.001878930740 nats/target**;
- cumulative log-loss delta: **+0.043215407019 nats**;
- mean full-line Brier delta, model minus uniform: **+1.805443215e-09**.

Positive deltas are worse than uniform. The difference is very small, but it is not evidence of predictive superiority.

Current 2026-09-08 effective mixture weights after updating only through 2026-09-04 are:

- Uniform: **0.936950434744**
- Cumulative frequency: **0.015461415406**
- Recent-five: **0.047588149850**

The underlying posterior component weights before the fixed uniform floor are:

- Uniform: `0.873900869488`
- Cumulative frequency: `0.030922830813`
- Recent-five: `0.095176299700`

This is therefore a deliberately near-null nonuniform challenger, not a high-confidence predictive field.

### E0032 minimal shared signed-displacement tilt

Previously screened in `upstream_field_screen_2026-09-07.md`:

- mean legal-line log-loss delta vs uniform: about **+0.05084 nats/target**;
- current full fit shrinks close to zero.

This field loses to the E0030 adaptive mixture and the uniform control.

### E0025 corrected nonlinear signed-transition field

Existing retrospective evidence reports mean legal-line log-loss delta vs uniform of **+0.2525717534 nats/target** over 19 targets through 2026-09-01. The field is materially worse than uniform despite modest raw K13 recall.

### E0026 corrected robust scenario-routed field

Existing E0026 replay reports mean exact-line log-loss delta model minus uniform of **+0.3967268048 nats/target** over its 12-target comparison. Scenario routing remains useful as a preservation research question, but the underlying probability field has not passed the proper-score gate.

### Coherent BARP-HLR residual line field

Previously screened in `upstream_field_screen_2026-09-07.md`:

- cumulative recent log-probability delta vs uniform: about `-2.2916 nats` in log-probability terms, equivalent to model log loss being about **+0.3819 nats/target worse** than uniform;
- 2026-09-04 alone was about **+1.4897 nats worse** in log loss.

Modal HLR accuracy therefore does not justify BARP as the upstream probability foundation.

## Championship verdict

### Proper-score champion

**Exact uniform legal-line null.**

No reviewed nonuniform field has demonstrated a positive proper-score advantage.

### Closest nonuniform challenger suitable for prospective shadowing

**E0030 adaptive uniform/frequency/recency mixture**, extended through 2026-09-04 with no formula or hyperparameter changes.

It is selected only as the least aggressive nonuniform shadow because:

1. its historical proper-score deficit is very small relative to the other screened fields;
2. its current effective weight is 93.7% uniform;
3. its algorithm was already defined before the 2026-09-08 target;
4. it produces a coherent full-support probability distribution;
5. it does not use HLR/VVD/terminal multiplication;
6. it can be frozen prospectively and falsified tomorrow.

This selection is **not** a predictive promotion. Uniform remains the formal calibration champion.

## E0032 compression of the closest nonuniform challenger

Using the same current E0030 mixture for all four E0032 K13 objectives, the four numerical arms converge to the same K13 under the declared exact/best-found optimization procedures:

`[2,4,5,14,16,19,22,24,27,31,34,39,40]`

Modeled fixed-basket hit distribution under the current mixture:

- `P(H=0) = 0.203876229363`
- `P(H=1) = 0.404222823241`
- `P(H=2) = 0.287432329175`
- `P(H=3) = 0.091076344531`
- `P(H=4) = 0.012764966911`
- `P(H=5) = 0.000627306780`

Derived metrics:

- `E[H] = 1.306512916726`
- `P(H<=1) = 0.608099052603`
- `P(H>=4) = 0.013392273691`
- `P(H=5) = 0.000627306780`

Uniform K13 controls:

- `E[H] = 1.3`
- `P(H<=1) = 0.610962072155`
- `P(H>=4) = 0.013093507523`
- `P(H=5) = 0.000607430761`

The modeled advantages are tiny and receive **zero predictive credit** because the upstream field has not beaten uniform on proper score.

## Current marginal ranking diagnostic

Top current anywhere-coordinate marginals from the E0030 mixture begin:

`40,34,4,5,24,2,16,27,14,19,22,31,39,45,47,7,38,43,50,25,...`

The first 13 define `K13_MEAN`. The nonlinear E0032 arms return the same basket, so there is no objective disagreement to exploit for this target under this near-null field.

## Decision for 2026-09-08

- Freeze the E0030-derived K13 above as an **E0032 prospective shadow basket**, not as a promoted probability model.
- Keep exact uniform as the proper-score champion and calibration reference.
- Do not resurrect BARP or E0026 as the authoritative upstream field merely to force more differentiated K13 baskets.
- Downstream assembly may be run on the frozen shadow K13, with stage-isolated attribution.
- One fresh target cannot promote the field or any compressor arm.

## Search-exposure disclosure

This 2026-09-07 review inspected existing field families already present in the repository plus the already-documented E0032 minimal signed field. The E0030 formula was not retuned for this target. The current selection is for prospective shadow testing only and all retrospective comparisons remain discovery evidence.
