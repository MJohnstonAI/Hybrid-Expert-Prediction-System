# HEPS — 9 and 13 October 2026 Draw Update and Null-First Post-Draw Audit

**Audit date:** 2026-10-14 (SAST)  
**Evidence:** descriptive post-draw audit / `INSUFFICIENT_EVIDENCE`  
**Authority:** research interpretation only; no new predictive method, parameter retuning or slate authority.

## 1. Canonical data update

Both active ledgers start 2026-06-02 and now contain **39 rows through 2026-10-13**. The first 37 rows were preserved byte-for-byte. Main and XTRA have independent fitted states.

| Date | Main winning numbers | Main PB | XTRA winning numbers | XTRA PB |
|---|---|---:|---|---:|
| 2026-10-09 | 3,14,17,19,37 | 16 | 2,38,40,44,46 | 15 |
| 2026-10-13 | 3,15,24,30,31 | 7 | 19,39,40,41,48 | 2 |

Canonical artifacts: `data/draw_history.jsonl`, `data/draw_manifest.json`, `data/powerball_xtra_history.jsonl`, `data/powerball_xtra_manifest.json`.

Dated / corroborating published records:
- https://za.national-lottery.com/powerball/results/09-october-2026
- https://www.lottery.co.za/powerball-xtra/results
- https://www.thesouthafrican.com/lotto-results/powerball-results/the-powerball-and-powerball-xtra-results-for-tuesday-13-october-2026/
- https://www.africanlottery.net/powerball/results/13-oct-2026/
- https://resultsza.co.za/

**XTRA provenance:** The configured official Sizekhaya/National Lottery endpoint did not yield usable results. New XTRA rows have cross-archive corroboration but remain flagged `pending_official_source_verification`. The XTRA manifest lists **18** pending dates total; the older 2026-08-14 and 2026-08-18 records retain their separate `user_reported_pending_external_verification` convention. Do not silently equate either with verified official results. The October 9 Main archive reports machine name GRACE; its draw method is recorded as unknown. Draw method/machine for October 13 remain unknown.

## 2. October 9 Main official E0033 Physics of Failure

Frozen pre-draw source: `cycles/2026-10-09/pre_draw/current_prediction.json`, pointing at `cycles/2026-10-09/pre_draw/main_prediction_e0033_2026-10-09.json`.

- Prior draw: `12,18,21,35,46 | PB10`.
- Actual: `3,14,17,19,37 | PB16`.
- Actual Main signed-slot direction: **LLLLL**; frozen BARP modal: **LLHHL**, for **3/5** modal slot directions.
- Actual PB direction: **H**; frozen PB modal: **L**.
- Official K13: `2,5,9,19,22,27,28,31,34,38,39,43,50`. Retention: **only 19**, **1/5**.
- Official frozen 20-line portfolio: **max 1/5** Main overlap; 13 lines overlap zero coordinates, 7 overlap one. **Zero PB16 assignments**. The actual PB16 was **rank 10/16** in the stored PB probability ranking.
- Published PB16 probability in frozen file: 0.0545432 versus uniform 0.0625, implying a realized PB log-loss deficit of **+0.13617 nats** on this target, not a long-run model verdict.
- Anywhere-coordinate top-25 ranks for actual winners were: 3 outside 25, 14 outside 25, 17 at 20, 19 at 7, 37 at 25. A larger diagnostic basket retaining more winners gets **zero fixed-K13 credit**.
- A random K13 has `P(H<=1)=0.610962`. This poor one-target result is common under the exact null; it does not prove systematic underperformance.
- Under exact legal-line enumeration relative to the 6 October prior draw, the all-low vector `LLLLL` has structural probability **0.181103**. It does not justify a special post-hoc all-low expert.

**First binding failure:** K13 coordinate acquisition. Coalition assembly, Johnson coverage, and PPMI ordering cannot recover winner coordinates excluded upstream.

### October 9 director HHHLL/PB-L shadow

Frozen source: `cycles/2026-10-09/pre_draw/hhhll_pb_l_scenario_shadow.json`. The four shadow lines are a **separate four-line exposure**, not part of the official fixed20. Actual Main HLR `LLLLL` and PB H violated the shadow's Main `HHHLL` / PB L scenario. Max shadow Main overlap was **1/5** and there were **no correct PB assignments**. Do not use post-result scenario switching to rewrite either slate.

## 3. October 13 descriptive evaluation

No October 13 frozen prediction directory was present at the time of this audit. **No HEPS prospective prediction score is assigned** to this target.

- Main: prior `3,14,17,19,37`; actual `3,15,24,30,31`; HLR `RHHHL`; PB `16 -> 7` = L.
- XTRA: prior `2,38,40,44,46`; actual `19,39,40,41,48`; HLR `HHRLH`; PB `15 -> 2` = L.
- The Main `RHHHL` vector has exact structural null probability 0.0031773 and a *discrete, probability-ordered exact-tail* probability of **0.05743** given the previous line.
- The XTRA `HHRLH` vector has exact structural null probability **0.000203893**, but a relevant *discrete, probability-ordered exact-tail* probability of **0.005572** given its previous line. Across 38 XTRA transitions the conservative Bonferroni upper adjustment is **0.212**, and across 76 Main+XTRA transitions it is **0.423**. This is an **exploratory rarity diagnostic**, not a mechanism finding or prospective predictive signal.
- October 9 XTRA was all-even. The exact per-draw uniform probability of five even main numbers is `C(25,5)/C(50,5)=0.025076`. The probability of at least one all-even draw in 39 independent fair draws is about **0.6286**. This is not strong anomalous evidence.

## 4. Frequencies, overlap and PowerBall diagnostics

- Main's leading anywhere-coordinate frequency is **40 appearing 8/39**. For a predeclared number under the uniform 5/50 null, `P(Binomial(39,0.1)>=8)=0.03662`, but searching 50 numbers destroys standalone significance. It receives **no predictive promotion**.
- Main consecutive-draw coordinate overlap across 38 transitions: **14 total = 0.3684 per draw**, versus exact uniform expectation 0.5. Approximate z = **-1.26**, not persuasive evidence of anti-repeat.
- XTRA consecutive-draw overlap: **19 total = 0.5 per draw**, exactly the fair-draw expectation.
- XTRA PB2 occurred **8 times in 39 draws** versus `39/16=2.4375` expected under uniform. For a *prespecified* PB number, `P(Binomial(39,1/16)>=8)=0.002490`. A familywise exact multinomial probability of **at least one of 16 PB values reaching 8+ hits** is **0.03962** for one lane. Inspecting both independent Main and XTRA PB lanes gives a two-lane family probability about **0.07766**. This ignores prior HEPS model/feature search and hence remains **exploratory**.
- The XTRA PB2 frequency deserves a **prospectively frozen** calibration challenger (strongly shrunk unconditional frequency versus uniform, E0015-style conditional research and incumbent). This must be evaluated on proper log score, not on a "hot ball" betting claim. No parameter may be retroactively selected using October 13 as if it were held out.

## 5. Research decision

**No predictive breakthrough and no model promotion.** Keep the exact uniform legal-line null as first control and E0036's corrected power/identifiability framework as first methodological priority.

Most defensible next actions:
1. **E0036 Phase A and Phase B:** Independently implement/reproduce null recovery, exact normalization and paired proper scores, with valid prospective freeze, SESOI and multiplicity/sequential controls. The corrected protocol was frozen 2026-10-02 but no E0036 implementation/results are recorded.
2. **Fixed K13 stage isolation:** Attribute failure to acquisition before analyzing assembly. Evaluate candidate survival, low-probability scenario robustness and proper scores at matched K13 only. October 9 may motivate hypotheses, but cannot tune them retrospectively.
3. **Separate PB and provenance audit:** Freeze a strongly shrunk XTRA PB2 frequency challenger against uniform and incumbent; continue official-result verification and independently sourced machine metadata. Main and XTRA stay independent.

This document is a post-result audit, not a newly backdated prediction. Do not edit the 2026-10-09 official or shadow pre-draw files or invent a 2026-10-13 pre-draw forecast.
