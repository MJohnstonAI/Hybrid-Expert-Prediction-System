# HEPS Main Session Handoff — 2026-09-02

**Game:** South African PowerBall Main 5/50 + PB 1/16  
**Purpose:** current-state handoff for future AI agents  
**Paper trading only**

## 1. Canonical latest draw

Latest verified Main draw:

- Date: 2026-09-01
- Main: `14,16,31,34,40`
- PowerBall: `4`
- Previous Main: `19,22,24,25,47 | PB11`
- Realized HLR: `LLHHL`
- Realized VVD: `[5,6,7,9,7]`
- Terminal digits: `[4,6,1,4,0]`

Canonical ledger is `data/draw_history.jsonl`, now through draw id 27.

## 2. What HEPS got right on 2026-09-01

### BARP direction

The frozen BARP modal HLR vector was `LLHHL` and the realized vector was exactly `LLHHL`.

This is a 5/5 directional hit and receives **positive one-target prospective credit**.

Do not promote BARP from one target. Reward it for the next cycle through bounded scenario/preservation allocation, not parameter retuning.

### Exact coordinates / candidate paths

Pre-draw diagnostics contained several realized coordinates:

- `31` — E0020 M3 rank 4 in S3; E0019 K13 survivor.
- `34` — E0020 M3 rank 1 in S4; E0019 K13 survivor.
- `40` — survived E0019 diagnostic K20 / E0016 reserve path.
- `14` — pre-draw M3 ranked first in S2 but realized in S1.
- `16` — ranked strongly across S1/S2 and realized in S2.

Important lesson: useful **anywhere-coordinate** information was partly lost by strict exact-slot provenance.

## 3. What failed

### Candidate compression remained the first failure stage

E0019 primary K13:

`20,22,23,26,30,31,32,34,35,39,41,43,49`

captured only `31,34` = 2/5.

At K13, exactly two hits is ordinary under the null; this receives no predictive promotion credit.

Diagnostic K20 additionally captured `40`, giving 3/5, but K20 exposure is larger and 3+ is not rare enough to establish edge.

### Old HLR×VVD field is superseded

Longcat 2.0 and subsequent HEPS audit identified the central mathematical defect:

- HLR = sign of the slot transition;
- VVD = absolute magnitude of the same transition;
- terminal digit and exact coordinate are further deterministic views of the same transition.

The E0019 formula multiplying HLR and VVD residual ratios is therefore not a coherent independent-evidence combination. Its line-mass containment objective remains useful; its old probability field does not.

### E0020 multiplicative synergy is rejected for acquisition

The terminal -> HLR -> VVD M1-M3 chain worsened proper score monotonically in replay. Terminal motifs remain diagnostic only.

The 2026-09-01 target still yielded useful terminal observations:

- S3 terminal 1 top-1 hit;
- S4 terminal 4 top-1 hit;
- S1 algebraic residue4 diagnostic was correct;
- S2 terminal6 and S5 terminal0 were present in secondary terminal support.

One target does not override the negative proper-score history.

## 4. Binding current methodology

Read before reusing any historical experiment:

1. `governance/current_method_doctrine.md`
2. `governance/methodology_deprecations.md`
3. `core/feature_dictionary.yaml`

Current doctrine:

- **Joint distribution first, compression second.**
- Use one signed-displacement information family per sorted-slot transition.
- HLR/VVD/terminal/exact coordinate may be reported as views but not multiplied/voted independently.
- Proper-score improvement is a primary gate before K-basket recall is called predictive lift.
- Exact-slot and anywhere-coordinate evidence are separate.
- Fixed-K adjacent-slot preservation is an allowed new shadow research path.

## 5. Evidence status after 2026-09-01

### Positive but not promotable

- BARP modal direction: exact 5/5 HLR hit on first clearly frozen 2026-09-01 target.
- E0013 PPMI spectral remains `PROVISIONAL_SIGNAL` coalition-only from discovery evidence; no candidate authority.

### Mixed / diagnostic

- E0020 terminal motifs: useful target-specific hits, but overall proper-score history remains negative.
- VVD-R: helped S3 coordinate rank on 2026-09-01 but harmed S5; slot-specific diagnostic only.
- E0016 nonequilibrium current: independent shadow, only 1/5 K13 capture on 2026-09-01; no one-target rejection.

### Superseded / rejected for forward use

- E0019 HLR×VVD residual-product probability field.
- E0020 terminal×HLR×VVD multiplicative coordinate chain.
- pure structural-null global mobility rescue.
- blind generic Core9+Rescue4 default rescue architecture.
- JOS-HDR exact-line density under exact uniform gap null.
- Johnson covering as candidate discovery.
- strict exact-slot provenance as a hard discard rule.

See `governance/methodology_deprecations.md`.

## 6. Friday 2026-09-04 expert-credit policy

Frozen policy file:

`cycles/2026-09-04/pre_draw/expert_credit_policy.json`

Interpretation:

- BARP HLR: high temporary preservation/scenario credit.
- terminal diagnostic: targeted medium shadow credit only.
- adjacent-slot preservation: medium new shadow at fixed K.
- VVD-R: slot-specific only; no global multiplier.
- E0019 line-mass K13: neutral comparator until corrected successor exists.
- E0016 current: unchanged independent shadow; no increased weight.

No parameters may be retuned from the 2026-09-01 outcome.

## 7. Highest-priority research after cleanup

1. **Corrected joint signed-displacement acquisition** — one transition representation, exact legal-line normalization, fixed-K containment objective.
2. **Adjacent-slot / anywhere-coordinate preservation** — test up to bounded seats at identical K.
3. **E0011 redundancy audit** — identify genuinely independent information families before convergence weighting.
4. **E0013 coalition challenger** — compare original PPMI with a marginal-conditioned/shrunk pair-association graph; do not apply a fictitious central-coordinate pair null.
5. **Mechanical/machine-conditioned bias** — high-value future research only when machine/ball-set metadata are prospectively knowable and strongly shrunk.
6. **PowerBall simplification** — strongly shrunk conditional challenger vs uniform/unconditional baseline on proper scores.

## 8. Do not waste tokens on these paths without new information

- inventing new HLR/VVD/terminal algebraic combinations;
- re-running rejected gap-density/JOS-HDR claims;
- treating structural-null global field as a candidate selector;
- adding more correlated expert votes for confidence;
- retuning rescue seats after each miss;
- broad physics metaphors without a new measurable information source;
- recursively reading all legacy contribution folders before consulting registries/deprecations.

## 9. Next target

Next Main target: **2026-09-04**.

Before generating a prediction, compute all fields strictly using rows through 2026-09-01, freeze the cycle artifact before result reveal, and preserve 2026-09-01 reward policy without outcome-conditioned retuning.