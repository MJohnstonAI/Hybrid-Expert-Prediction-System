# HEPS 2026-11-27 — Seven-Draw Main/XTRA Acquisition Replay and Tie-Sensitivity Audit

**Status:** RESEARCH ONLY / EXPLORATORY WALK-FORWARD / INSUFFICIENT_EVIDENCE  
**Created:** 2026-11-27 before the evening draw.  
**Data:** canonical Main `data/draw_history.jsonl` and XTRA `data/powerball_xtra_history.jsonl`, each 51 draws from 2026-06-02 through 2026-11-24.  
**Seven target draws:** 2026-11-03, 06, 10, 13, 17, 20, 24.  
**Temporal rule:** every target prediction uses only its preceding draws (44 prior draws for 2026-11-03 through 50 for 2026-11-24); no target values are used in its own forecast. Main and XTRA fitted state completely separate.

## Evidence limitation

These are **retrospective prefix-only replays, not originally committed pre-draw prediction slates for all seven dates**. The incumbent E0030 mixture formula was registered months before the target window; the specialist scoring/ranking proxy is now specified after the historical results are known, although its per-target computation uses strictly past draw data. Thus this is NOT a genuinely independent blind confirmation of the new specialist rule. The seven targets and all multiple-armed comparisons are exploratory. The original 2026-08-21 XTRA reserve did not have a complete deterministic reusable ranker; the proxy below **must not** be misidentified as an exact reproduction of that reserve.

## Replayed incumbent

Reimplemented from `experiments/E0030/prototype.py` and `experiments/E0030/protocol.yaml`:

1. Three exactly normalized fixed-size 5-of-50 product-weight models with coordinate weights `1`, `1+cumulative_count/10`, `1+last_five_count/10`; all features from available prefix only.
2. Adaptive mixture starts with component prior `[0.8, 0.1, 0.1]`; its log weights update sequentially using past actual five-number line probabilities. Effective mixture weights are `[0.5+0.5*posterior_null, 0.5*posterior_frequency, 0.5*posterior_recent5]`.
3. Exact inclusion marginals computed with elementary symmetric polynomials. Freeze top K=13. Two tie policies are reported because near-equal coordinate weights materially influence the basket:
   - **ASC:** ascending-number tie break. This matches the 2026-11-06 designated Main E0030-style basket more closely.
   - **SEEDED:** original prototype's `Random(20260905 + target_index + (100000 if XTRA else 0)).sample(range(1,51),50)` tie priority, using the Python MT19937 integer-seed and sample algorithm; floating near-ties are grouped at tolerance 1e-14. This is a reconstructed seeded policy rather than a byte-identical run of the original Python implementation.
4. No target results influence the forecast for the same target. The ranked marginal inclusion field and its log score are identical across the two tie policies.

## New specialist proxy (not the frozen 21-August reserve algorithm)

Each game fitted separately. From the prefix, compute slotwise absolute displacements of consecutive sorted five-number results. Count previous-displacement -> next-displacement transitions pooled over the five Main-number sorted slots only (do not pool with the separate 1/16 PowerBall lane).

For a candidate coordinate x and sorted slot j, given the current predecessor coordinate p_j and previous displacement d_j:

- Base successor-displacement frequency `p_base(d)=(count_next[d]+1)/(total_pooled_next+50)`;
- Strongly shrunk conditional successor frequency `p_cond(d|d_j)=(count(d_j->d)+5*p_base(d))/(count_from(d_j)+5)`;
- Slot weight `q_j(x) ∝ P0_orderstat_j(x) * [p_cond(|x-p_j| | d_j)/p_base(|x-p_j|)]^0.20`;
- Normalize each slot over legal x. Define cross-slot specialist coordinate score `S(x)=max_j q_j(x)/max_y q_j(y)`. Rank by decreasing S, ascending coordinate tie.
- These are heuristic candidate scores, **not** claimed to form a calibrated legal joint-line distribution. HLR/VVD are not counted as independent likelihood experts.

The `beta=0.20` shrinkage is borrowed from the pre-2026-08-21 XTRA direct-transition experiment; the five pseudo-counts and general signed-displacement architecture are also historically motivated. The new max-normalized-slot-score operator and candidate-list construction were not historically pre-frozen. No hyperparameters were altered after inspecting seven-draw results in this research audit.

For each target compute:
- Core13;
- Hybrid12+1 (top 12 core, highest-ranked eligible specialist outside them);
- Hybrid11+2;
- Hybrid7+6;
- Hybrid3+10;
- Specialist13 (top 13 independent specialist candidates).
Exactly K13 numbers per arm. No special credit for union or larger K. All scores below are number **containment within K13**, not 5-number ticket hits. PowerBall selection and 20-line assembly were NOT tested.

## Seven-draw summary — ASC tie policy

| Lane | Core13 | Hybrid12+1 | Hybrid11+2 | Hybrid7+6 | Hybrid3+10 | Specialist13 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Main (total captured of 35 possible) | **13** | 11 | 11 | 11 | 11 | 12 |
| XTRA (total captured of 35 possible) | 5 | 6 | 6 | 6 | 6 | 6 |

| Date | Main Core13 | Main 12+1 | Main 11+2 | Main Specialist13 | XTRA Core13 | XTRA 12+1 | XTRA 11+2 | XTRA Specialist13 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-11-03 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 |
| 2026-11-06 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 |
| 2026-11-10 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 3 |
| 2026-11-13 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| 2026-11-17 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| 2026-11-20 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 0 |
| 2026-11-24 | **5** | 4 | 4 | 2 | 1 | 1 | 1 | 0 |

## Seven-draw summary — SEEDED prototype tie policy

| Lane | Core13 | Hybrid12+1 | Hybrid11+2 | Hybrid7+6 | Hybrid3+10 | Specialist13 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Main (total captured of 35 possible) | 12 | **13** | 12 | 11 | 11 | 12 |
| XTRA (total captured of 35 possible) | 5 | 6 | 6 | 6 | **7** | 6 |

For Main seeded-tie Core13, daily capture was `[1,1,2,0,1,2,5]`; Hybrid12+1 was `[1,2,2,0,1,2,5]`. For XTRA, the same seeded core captures `[0,1,1,1,0,1,1]`.

**Critical tie sensitivity:** merely changing the tie policy reverses the apparent seven-draw Main winner (Core13 under ASC versus Hybrid12+1 under SEEDED). This illustrates instability in the nearly flat probability field and forbids declaring either arm a proven winner from seven draws.

## The 2026-11-24 Main 5/5 K13 event

Actual Main result: `[7,17,24,36,45] | PB4`. The prefix-only E0030-style candidate set **under ASC** is `[5,7,9,17,24,31,36,37,39,40,43,45,46]` and contains all five actual main winning numbers. Independently reconstructed SEEDED priority orders the near-tied marginal group `[45,7,39,5,16]` and retains `45,7,39,5`, excluding 16; it also captures all five.

This is a reconstructed **K13 containment** success, not evidence of an actually pre-draw-frozen Nov24 K13 or a winning submitted five-number ticket. At this target, there were five practically equal-ranked candidates for four seats; another arbitrary tie resolution could omit winner 7 and reduce containment to 4/5.

The exact fair-lottery null probability of all five winners lying inside a preselected fixed K13 is `C(13,5)/C(50,5)=0.0006074307614` (0.06074%). The probability of at least one such event across seven independent fixed-K13 targets is `~0.0042443` (0.4244%). This is **unadjusted** for the large HEPS history of alternative models, tie policies, target windows and research selection; it must not be interpreted as a validated statistical discovery.

## Longer E0030-style walk-forward diagnostic

Walk-forward from initial five training draws over all remaining **46 historical targets per game**, using the same formula:

| Lane | ASC Core13 captured | SEEDED Core13 captured | Uniform-null expected | Mean full-field exact-line log-loss delta versus uniform |
| --- | ---: | ---: | ---: | ---: |
| Main | 63 / 46 = 1.370/draw | 55 / 46 = 1.196/draw | 1.300/draw | **+0.0006001 nats** |
| XTRA | 46 / 46 = 1.000/draw | 42 / 46 = 0.913/draw | 1.300/draw | **+0.0021319 nats** |

Positive log-loss delta is **worse than uniform**. Full-field scores do not improve when basket ties are changed. The ASC seven-draw Main total of 13 hits is only modestly unusual: exact single-arm null `P(total hits >=13 across 7 fixed K13)=0.08837`, without multiplicity correction. One exceptionally good containment target contributes heavily to that seven-draw score.

## Interpretation and decision for 2026-11-27

- The specialist proxy does not show stable superiority; a 3/5 single-target success (XTRA 2026-11-10) was not replicated across the seven draws.
- The incumbent Main candidate field generated one exceptional historical K13 containment event, but its long-window proper score still loses marginally to the uniform null. **Do not claim predictive lift**.
- The seven-draw winner changes under plausible tie treatment; **do not select the architecture from this window**.
- Retain the incumbent designated slate under the existing no-promotion governance rule. Freeze the new specialist and 12+1 challenger *prospectively* before the draw if operationally available, with fully specified tie and rank rules, otherwise do not retroactively attribute credit.
- A stronger future tournament must include controls and separate proper-score assessment; maintain lane isolation, fixed K13, matched 20-line budgets, and a predeclared primary metric and sample horizon.
- No Main/XTRA model state, historical prediction file, production slate, or frozen prior forecast has been altered by this note.

**Evidence status:** `INSUFFICIENT_EVIDENCE`; research audit only.
