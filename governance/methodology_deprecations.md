# HEPS Methodology Deprecations and Do-Not-Reuse Map

**Effective:** 2026-09-02  
**Purpose:** prevent historical research artifacts from being reused as if they were current HEPS recommendations.

Historical files are retained for auditability. A deprecated or rejected method may still be cited to explain what was tested, but it must not be copied into a new predictive pipeline unless the stated new-information requirement is satisfied.

## Binding interpretation rule

If a historical experiment contains a formula listed here, the experiment's frozen predictions remain valid for historical scoring, but the formula has **no forward reuse authority** unless explicitly stated otherwise.

| Method / claim | Current status | Why | Forward rule |
|---|---|---|---|
| E0019 `sqrt(HLR residual ratio * VVD residual ratio)` | **SUPERSEDED / REJECT as combination rule** | HLR is sign of signed displacement and VVD is magnitude of the same transition; multiplication double-counts one information source. Underlying field was worse than flat proper score. | Preserve E0019's line-mass objective only. Replace field with one signed-displacement transition model. |
| E0020 `terminal * HLR * VVD` M1->M3 chain | **REJECT for coordinate acquisition** | Terminal, HLR and VVD are deterministic views of the same slot transition; proper score worsened monotonically M0->M3. | Terminal models remain diagnostic/shadow only. Do not multiply these ratios. |
| `product_j q_j(x_j)` as the Main joint legal-line field | **REJECT / modeling trap** | The five sorted-slot marginals already contain order-statistic geometry and are mechanically dependent. Multiplying them re-multiplies structural geometry and does not recover the exact uniform legal-line null when learned residual signal is zero. | Start from uniform `P0_line=1/C(50,5)` and tilt it only by residual ratios `T_j=q_j/P0_j`, then normalize over legal lines. Require exact null-recovery test. |
| Pure structural-null global mobility rescue | **REJECT** | Every Main coordinate has IID anywhere-inclusion probability 0.1; null field cannot rank predictive rescue coordinates. | Requires a genuinely non-flat residual signal and fixed-K matched control. |
| Blind Core9+Rescue4 diversification as a general rule | **REJECT as default architecture** | Historical proxy audit showed rescue seats displaced stronger consensus seats and reduced winner-coordinate capture. | Any rescue family must compete at identical K and earn seats prospectively. |
| JOS-HDR exact-line density under `NULL_GAP_DM` | **REJECT** | All legal six-gap compositions are equiprobable under the exact IID gap null. | Only null-residualized feature classes may be researched. |
| Multiplying per-slot HLR marginals to obtain joint HLR vector probability | **REJECT** | Sorted slots are mechanically dependent. | Use exact `NULL_HLR_JOINT_243` enumeration. |
| Treating HLR/VVD/terminal/slot-coordinate projections as independent convergence votes | **REJECT** | Functional coupling / shared transition source. | Count as one information family unless a coherent dependency model proves incremental information. |
| Strict exact-slot provenance as a hard candidate discard | **SUPERSEDED as hard rule** | 2026-09-01 showed useful anywhere-coordinate evidence could migrate to an adjacent sorted slot (14/16 example). | Score exact-slot and anywhere-coordinate evidence separately; adjacent-slot preservation may be tested at fixed K. |
| Terminal algebraic equation mining after result reveal | **REJECT** | High apophenia/multiple-testing risk; current finite library did not beat slot-aware null. | Only finite preregistered rule libraries with multiplicity correction; diagnostic until prospective proper-score lift. |
| General drift/diffusion tensor, optimal-transport flow, nucleation, heat-kernel E0013 augmentation, routine Levy candidate ranking | **REJECT current formulations** | E0016 taste test found no stable lift or added complexity without stage improvement. | Requires materially new information/operator and fresh preregistration; renaming is insufficient. |
| E0016 Richardson geometric-mean message passing as exact inference | **MISLEADING INTERPRETATION / HEURISTIC ONLY** | Protocol uses all ten slot pairs, not a five-node chain; update is not exact sum-product posterior inference. | Pair estimator may remain shadow. Prefer direct legal-line scoring/exact normalization when feasible. |
| E0013 correction by subtracting a coordinate-specific "central geometry" `P0(i,j)` | **REJECT as formulated** | For unordered anywhere-coordinate pairs in uniform 5/50, every distinct pair has identical null co-inclusion probability. | Test a marginal-conditioned/shrunk association null given `C_i,C_j`, not a fictitious central-coordinate pair bias. |
| E0014 XTRA raw-pair oracle strength interpreted using best-rank-for-every-tie | **DOWNGRADED / INVALID AS LIFT EVIDENCE** | E0022 showed discrete raw-pair/frequency scores had large tie blocks. The historical strict-greater rank gave every tied winner the best rank in its tie block, inflating raw-pair oracle percentile from about 0.628 in reproduction to about 0.459 under average midrank. | Historical E0014 files remain immutable. Future oracle/rank comparisons must use average midrank or another explicit tie-aware rule; do not cite the old raw-pair ~0.645 result as predictive lift without this correction. |
| Johnson covering as candidate discovery | **FORBIDDEN** | Johnson solves downstream coverage/assembly geometry, not predictive coordinate discovery. | Candidate universe must be frozen first. |
| Raw K13/K20 recall without matched exposure | **INVALID EVIDENCE** | Recall scales mechanically with K and can reward exposure expansion. | Always compare identical K/exposure and exact hypergeometric controls. |
| K-basket recall promotion when underlying probability field is worse than flat | **FORBIDDEN PROMOTION PATH** | Basket optimizer can exploit score misspecification. | Proper-score improvement is a primary gate before predictive promotion. |
| One successful target triggering parameter retuning or expert promotion | **FORBIDDEN** | One draw is high-variance evidence and creates outcome-conditioned overfit. | Reward only through predeclared bounded preservation/allocation; no retrospective parameter changes. |
| Sparse PB conditional transition certainty | **NO HIGH-CONFIDENCE AUTHORITY** | Current per-state counts are too sparse and shrinkage dominates. | Compare strongly shrunk conditional model prospectively against uniform and unconditional shrunk baseline on proper scores. |

## Historical artifacts that require warning-first reading

Future agents should read the relevant decision/failure record before copying formulas from:

- `experiments/E0019/` — retain line-containment objective; do not reuse HLR×VVD residual product.
- `experiments/E0020/` — retain terminal diagnostics; do not reuse M1-M3 multiplicative chain.
- `experiments/E0007/` — do not assume blind rescue improves K13.
- `experiments/E0006/` — original JOS-HDR claim rejected; only repaired null-residual research remains open.
- `experiments/E0014/` — XTRA raw-pair oracle percentiles require the E0022 average-midrank correction before interpretation.
- `experiments/E0016/` — distinguish sound estimators from heuristic Richardson message passing and rejected physics expansions.
- `experiments/E0022/` — 4+-first Johnson is deterministic geometry; Dissent-OR is shadow only; searched nucleus/completion variants are not predictive breakthroughs.
- legacy `workspace/contributions/` — discovery history only unless a current experiment/claim registry explicitly promotes a derivative.

## Reuse checklist for AI agents

Before reusing an old strategy, answer all of the following:

1. Is it listed in this deprecation map?
2. Is the claimed signal independent of the information already in the current field?
3. Does it beat the exact structural/simple baseline on a proper score?
4. Is exposure identical in the comparison?
5. Was the result discovered post-hoc or frozen prospectively?
6. Has multiplicity/search-degree exposure been recorded?
7. Is the proposed stage the natural information stage?
8. Does the latest `knowledge/failure_registry.jsonl` contradict the old claim?

If any answer is unresolved, the strategy remains `INSUFFICIENT_EVIDENCE` or historical-only.