# HEPS Main — Physics of Failure — 2026-09-04

## Verified result

**Main:** `4,7,27,38,50`  
**PowerBall:** `10`  
**Previous Main:** `14,16,31,34,40 | PB4`

Derived transition:

- signed slot transition: `[-10,-9,-4,+4,+10]`
- HLR: `LLLHH`
- VVD: `[10,9,4,4,10]`
- Main sum: `126`; SUMAD = `|126-135| = 9`
- SLD: `4+7+7+8+0 = 26`; LDSAD = `|26-15| = 11`
- span: `50-4 = 46`; SPANAD = `|46-26| = 20`
- PB transition: `4 -> 10`; PB VVD = `6`

## Executive diagnosis

The first binding failure was **candidate acquisition/compression**, not E0029 pattern triage, E0013 coalition ranking, or Johnson portfolio geometry.

The official v35.3 Pattern-Triage K13 was:

`3,8,18,19,20,23,32,34,35,39,40,48,50`

It retained only winner `50`, so K13 recall was **1/5**. Once `4,7,27,38` were excluded, the exact winning line could not exist anywhere in the 1,287-line assembly universe. Therefore downstream line ranking and portfolio selection receive neither credit nor blame for exact-line failure.

## Stage-by-stage audit

### Stage 1 — HLR / signed-transition forecast

Frozen slotwise modal HLR: `LHLHH`.

Realized HLR: `LLLHH`.

Result: **4/5 directions correct**. The miss was S2:

- S1 LOW: correct
- S2 HIGH: wrong; realized LOW
- S3 LOW: correct
- S4 HIGH: correct
- S5 HIGH: correct

The exact legal-line BARP residual field had realized `LLLHH` as approximately the **8th-highest joint HLR state**, with pre-draw mass about `0.02251` (2.25%). Thus the realized direction state was present in the pre-draw scenario distribution but was not dominant.

Interpretation: directional state estimation remained informative enough to avoid complete failure, but the 2026-09-01 exact 5/5 HLR success did not repeat. No parameter promotion is justified.

Evidence: `INSUFFICIENT_EVIDENCE`.

### Stage 2 — Official E0026/frozen K13 acquisition

Official K13 hits:

- S1 winner `4`: excluded
- S2 winner `7`: excluded
- S3 winner `27`: excluded
- S4 winner `38`: excluded
- S5 winner `50`: retained

Total: **1/5**.

For random fixed K13, expected winner count is `5*(13/50)=1.3`; the official basket therefore finished slightly below random expectation on this target.

The decisive failure was not that HLR failed to allow LOW/HIGH states. It was that the candidate compression did not retain sufficiently low S1/S2 coordinates, the realized S3 coordinate 27, or S4 coordinate 38.

### Stage 2 shadow comparison — superseded E0026-R

The superseded pre-draw E0026-R K13 was:

`12,13,15,17,18,19,33,37,38,39,48,49,50`

It retained `38` and `50`: **2/5**.

Notably:

- `38` had primary S4 provenance in that frozen artifact and realized exactly in S4;
- `50` had primary S5 provenance and realized exactly in S5.

This is useful prospective shadow evidence for slot provenance, but it does **not** validate the E0026-R probability field. Its prior holdout was tied against the comparator and its full-support exact-line proper score was worse than uniform. A one-target 2/5 result has no promotion authority; under a random K13 the probability of 2+ winner coordinates is about `0.389`.

Evidence remains `INSUFFICIENT_EVIDENCE`.

### Invalid pure-M(K) E0026 diagnostic

The invalidated `[27..39]` basket happened to contain `27` and `38` (2/5), but it could not represent the realized `LLLHH` line because it contained no S1-LOW coordinate below 14, no S2-LOW coordinate below 16, and no S5-HIGH coordinate above 40. It also omitted winner 50.

Therefore its raw 2/5 is not admissible predictive credit and confirms why scenario-provenance constraints are required.

### Stage 3.5 — E0029 Pattern-OR triage

Because the exact winner was not in K13, E0029 cannot be scored on exact winning-line rank or gate survival for this target. This is a **stage-isolation rule**, not a missing-data inconvenience.

However the realized line produced two noteworthy prospective pattern diagnostics:

- `LDSAD = 11`, which lands inside the frozen E0028 primary discovery band `11..13`;
- `SUMAD = 9`, which lands inside the fixed post-hoc diagnostic band `8..9`;
- `SPANAD = 20`, which misses the fixed diagnostic `5..6` band.

The E0028 `11..13` LDSAD band therefore records its **first fresh prospective hit** on 2026-09-04. This is positive evidence, but because the band was discovered post-hoc and has search/multiplicity exposure, one fresh hit is not sufficient for promotion or hard pruning.

E0028 evidence remains `INSUFFICIENT_EVIDENCE`.

### Stage 3/5 — E0013 spectral coalition / Top-20 ranking

No downstream coalition rank can recover an omitted coordinate. The frozen K13 contained only one of five winners, so the exact winning line was absent from all 1,287 combinations.

The official 20-line portfolio's best Main overlap was only **1/5**; every overlap came from winner `50`.

A useful caution is that one highly ranked frozen line, `3,8,19,39,48`, had the correct realized HLR state `LLLHH` yet matched **zero** actual Main coordinates. This demonstrates that getting the directional pattern right is not equivalent to acquiring the correct coordinates.

E0013 remains `PROVISIONAL_SIGNAL`; no new credit or downgrade can be inferred from exact-winner rank because acquisition failed first.

### Stage 6 — Johnson geometry

No blame. Johnson only redistributes a fixed line budget inside the already-frozen K13. With 4/5 winners missing upstream, no 20-line geometry can construct the exact winning line.

Status: deterministic portfolio geometry only.

## PowerBall audit

Actual PB: `10` from previous PB `4`, so realized PB VVD = `6`.

Frozen calls:

- formal HEPS primary `PB4`: miss
- unconditional Dirichlet shadow leader `PB11`: miss by one coordinate, but exact-hit score is still zero
- revised Director VVD-sum challenger `PB9`: miss
- older Director `PB14`: miss

### VVD10 -> next-two-VVD sum 12 hypothesis

The pre-draw Director hypothesis was:

`10 -> 7 -> 5`, because `7+5=12`, implying `PB4+5=PB9`.

Actual continuation was:

`10 -> 7 -> 6`, because PB moved `4 -> 10`.

Thus the completed pair is:

`7 + 6 = 13`, not 12.

This is the first fresh prospective test of the exact deterministic motif and it **fails**. The specific rule `after PB VVD10, the next two PB VVDs sum to 12` should therefore be classified `REJECT` as a deterministic prediction rule. The broader question of whether PB VVD-state transitions contain any shrunk predictive information remains `INSUFFICIENT_EVIDENCE` and should be tested only through a preregistered proper-score model.

## Core Physics-of-Failure interpretation

The draw produced a pronounced **outer expansion** relative to 2026-09-01:

- S1 collapsed from 14 to 4 (`-10`)
- S2 collapsed from 16 to 7 (`-9`)
- S3 drifted down from 31 to 27 (`-4`)
- S4 expanded from 34 to 38 (`+4`)
- S5 expanded from 40 to 50 (`+10`)

This is a roughly bilateral stretch around the middle slots: strong negative displacement at the low end and strong positive displacement at the high end. The official K13 was too concentrated in previously favoured interior coordinates and did not preserve enough low-tail S1/S2 or the 38 S4 route.

The realized VVD vector `[10,9,4,4,10]` also shows that the miss was not a small perturbation around the prior line. The draw simultaneously generated two extreme magnitude-10 slot transitions at S1 and S5. Any future candidate funnel that over-compresses tail movement will remain vulnerable to this failure mode.

## What should change for the next target

1. **Do not retune to 4,7,27,38,50.** These are now outcome-known and may update only predeclared sufficient statistics.
2. Preserve E0026's scenario-conditioned slot provenance, but audit whether its compression objective systematically underweights simultaneous low-tail/high-tail displacement states.
3. Add a preregistered catastrophic-tail stress metric: for every candidate K13, measure containment under joint scenarios with large opposing-end signed displacement, without increasing K.
4. Keep E0028 LDSAD `11..13` frozen exactly as-is and score future targets prospectively; do not move the band after this success.
5. Do not promote SUMAD `8..9` from this hit because it remains post-hoc discovery-only.
6. Reject the exact PB VVD10 -> next-two-sum12 deterministic motif; if retained at all, convert it into a finite preregistered PB transition feature and compare proper scores against uniform and the shrunk unconditional baseline.
7. Candidate acquisition remains the highest-priority research bottleneck. Assembly changes cannot solve a 1/5 K13.

## Evidence update

- Main BARP/HLR: `INSUFFICIENT_EVIDENCE` — 4/5 directional hit, no promotion.
- Official E0026/frozen K13: `INSUFFICIENT_EVIDENCE` — 1/5, candidate acquisition failed.
- Superseded E0026-R: `INSUFFICIENT_EVIDENCE` — 2/5 with correct S4/S5 provenance, useful shadow observation only.
- E0028 LDSAD 11..13: `INSUFFICIENT_EVIDENCE` — first fresh prospective hit.
- E0029 Pattern-OR: `INSUFFICIENT_EVIDENCE` — unscorable on exact winner because K13 failed upstream.
- E0013 spectral: `PROVISIONAL_SIGNAL` — no exact-winner rank attribution because acquisition failed.
- Johnson four-plus-first: deterministic geometry only.
- PB formal models: `INSUFFICIENT_EVIDENCE` — all exact calls missed.
- Director PB VVD10 -> two-following-sum12 deterministic motif: `REJECT`.

## First failure stage

**Candidate Funnel / K13 compression.**

Winner trace:

`4@S1 -> excluded at acquisition`  
`7@S2 -> excluded at acquisition`  
`27@S3 -> excluded at acquisition`  
`38@S4 -> excluded from official K13; present in superseded E0026-R shadow`  
`50@S5 -> retained`

No downstream stage could recover the four excluded coordinates under the fixed-K13 architecture.
