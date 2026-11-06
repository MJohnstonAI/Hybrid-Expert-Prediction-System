# HEPS Main — 2026-11-06 Pre-Draw Readiness and No-Promotion Audit

**Audit date:** 2026-11-06, before the Friday evening draw (South African local time)  
**Game:** South African PowerBall Main, active post-2026-06-02 HEPS era  
**Authority:** read-only scientific evaluation / no parameter promotion / no slate supersession  
**Evidence:** `INSUFFICIENT_EVIDENCE`  
**Official current pointer:** `cycles/2026-11-06/pre_draw/main_current_prediction.json`  
**Frozen slate:** `cycles/2026-11-06/pre_draw/main_e0030_e0033_experimental_slate.json`

## 1. Live data reconciliation

- Canonical ledger: `data/draw_history.jsonl` — **45 rows**, June 2 through November 3, 2026, internal draw ids 1–45.
- Main manifest: `data/draw_manifest.json` — `row_count=45`, `latest_draw_date=2026-11-03`, `last_synced=2026-11-06`.
- Latest actual: **13,15,32,34,43 | PB12** on November 3, corroborated by these public results histories:
  - https://za.national-lottery.com/powerball/results/2026-archive
  - https://www.powerball.net/southafrica/results/history/2026
  - https://www.lottery.co.za/powerball/results/2026
- Review found **no invalid canonical main-number ranges, date-order/gap violations, sequential draw-id errors, macro-sum discrepancies or manifest-count mismatch** in the 45 rows.
- Recorded physical mechanism provenance: **15 mechanical_machine, 2 electronic_rng, 28 unknown**. Do not describe all 45 as mechanically homogeneous or infer mechanism from outcomes.
- The official November 6 slate already declares `cutoff_date=2026-11-03`, `canonical_row_count=45`. There is no missing Main draw to append before tonight.

### Latest six completed results

| Date | Main numbers | PB | Realized sorted-slot HLR vs prior draw |
|---|---|---:|---|
| 2026-10-16 | 15,33,38,42,49 | 4 | HHHHH |
| 2026-10-20 | 1,18,21,41,47 | 5 | LLLLL |
| 2026-10-23 | 2,4,6,40,45 | 5 | HLLLL |
| 2026-10-27 | 3,4,5,38,48 | 3 | HRLLH |
| 2026-10-30 | 7,9,21,27,30 | 8 | HHHLL |
| 2026-11-03 | 13,15,32,34,43 | 12 | HHHHH |

**Null interpretation:** Relative to the immediately previous sorted draw, the exact conditional uniform legal-line probabilities of HHHHH were about **0.329924** on October 16 and **0.348213** on November 3; LLLLL on October 20 had probability about **0.580025**. Repeated high/low motifs alone do not establish a successor rule.

The October 27 `HRLLH` vector had a low individual conditional probability (**0.000080236**) under exact 5-of-50 legal-line enumeration, but the appropriate probability-ordered exact-null tail was **0.0023032**. With 44 inspected Main transitions, a conservative within-lane Bonferroni comparison is **0.10134**, before considering the wider HEPS hypothesis search. This is **exploratory anomaly detection only**, not predictive evidence.

## 2. Frozen October 16 prospective post-draw score

Artifact: `cycles/2026-10-16/pre_draw/main_prediction_e0033_point_k13.json`.  
Actual 2026-10-16: `15,33,38,42,49 | PB4`.

- The frozen K13 contained **only winner 15**: **1/5** coordinate retention.
- All 20 official Main lines had at most **1/5** overlap; 13 lines had zero and seven had one.
- **Three** 20-line PB assignments selected PB4; one line paired PB4 with its sole matching main coordinate.
- First binding failure: **candidate acquisition**, not Johnson geometry or downstream coalition ranking.
- One target gives no authority to retune acquisition or PB weights.

## 3. Tonight's frozen November 6 official/Main experimental slate

- Correct cutoff: **2026-11-03**, **45** Main rows.
- Experimental probability-field mixture weights:
  - uniform **0.9499471881**
  - cumulative frequency **0.0098229861**
  - recent five **0.0402298258**
- Frozen Main K13 contains 13 unique legal coordinates; 20 official lines are distinct and entirely within K13; every stored line HLR matches the preceding November 3 sorted draw.
- Independent exact enumeration of all **1,287** K13 five-sets verifies that the Johnson 20-line portfolio retains **788** possible within-K13 winning states at 4+ main overlap (**61.2277% conditional coverage only**).
- The primary model's *reported* 40-target historical mean exact legal-line log-loss difference `L_model - L_uniform` is **+0.001420684 nats/target** (**worse** than uniform). This was read from the frozen artifact; its estimator has **not** been independently reproduced in this audit.
- The frozen artifact reports K13 51/40 = **1.275** mean winner coordinates per target compared with exact IID 1.30. **29/40** target baskets excluded four or five winning coordinates (`H<=1`). Fair-draw K13 has `P(H<=1)=0.610962072`; the one-sided probability of at least 29 catastrophes over 40 correctly target-excluded K13 selections is about **0.09195**. Not a robust predictive conclusion.
- The frozen PB model reports mean log-loss difference **-0.0003562 nats/target** versus PB-uniform over 40 replay targets, a tiny retrospective improvement, not demonstrated prospective authority.
- Model diagnostic BARP HLR is **LHLHL** but is a deterministic transition representation; it cannot be multiplied as an independent expert vote.
- All current scores remain `INSUFFICIENT_EVIDENCE`; **none** justifies a higher-confidence predictive claim.

## 4. Additional simple matched-K exploratory control

To stress-test complex acquisition against trivial alternatives, using only prior outcomes for *each* replay target, all from draw #6 to #45 (40 target-excluded replay targets), select 13 numbers by descending raw occurrence count with ascending-number tie-break:

| K13 acquisition control | 40-target winner retention | Mean H | H<=1 rate |
|---|---:|---:|---:|
| Cumulative frequency (all previous draws) | 50/200 | 1.250 | 26/40 |
| Last-five-draw frequency | 53/200 | 1.325 | 23/40 |
| Last-ten-draw frequency | 47/200 | 1.175 | 30/40 |
| Exact uniform random K13 reference | expected 52/200 | 1.300 | 61.10% |
| Frozen E0030-style slate reported replay | 51/200 | 1.275 | 29/40 |

**Interpretation constraints:** These specific simple controls were evaluated **after all 40 outcomes were visible**. Their results are retrospective discovery, exposed to choice of window and tie-break. Cohort equivalence to the frozen E0030 scorer is assumed from the reported 40-target count and has not been proven by independent reproduction of its exact scorer. Comparisons are stage-isolated and *not* a proper-score substitute. There is no evidence supporting a swap to five-draw frequency or changing the November 6 K13.

## 5. Explicit pre-draw decision

**NO CURRENT MODEL PROMOTION OR TUNING.** Existing frozen Main November 6 K13, PB ranking, 20 line memberships and probabilities remain unchanged.

This is an evidence-constrained decision, not an assertion that the incumbent model is good or reliably predictive. Under a fair IID mechanism, expected predictive skill does not arise from adding more historical pattern functions; additional observations can improve estimates of noise without creating useful information.

Allow a **separately preregistered future challenger**, for the *next eligible* target rather than using November 6 as an unannounced adaptive test, to compare:
1. Exact uniform full-support field versus incumbent E0030 mixture using paired, prospective exact-line log loss.
2. A strongly shrunk simple five-draw-frequency model, with full-support probabilities and the same fixed K13 budget, only after freezing the hyperparameters and evaluation horizon.
3. E0036 Phase A power/identifiability and Phase B unary-residual adequacy test, independently reproduced with proper scoring, SESOI and multiplicity control.

Retain the corrected E0036 as methodology-only and keep Main and XTRA fitted independently.

**Temporal integrity:** Do not reissue or alter the existing November 6 official frozen slate on the basis of November 6 results once they become known. Before-result supersession is permitted only by the binding governance policy and an explicitly justified, versioned change. This audit authorizes none.

**Code and data changes in this audit:** None to predictions, numeric ledgers, manifests, experts, model weights or scripts. This file records scientific readiness and no-promotion findings only.
