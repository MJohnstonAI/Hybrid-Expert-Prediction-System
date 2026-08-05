# Red-Team Review — Candidate Recall Guard + Directional Scenario Routing

Date: 2026-08-05
Reviewer role: external auditor / quantitative red team
Verdict: ACCEPT METHODOLOGY WITH STRICT EVIDENCE LIMITS

## What survives review

### 1. Candidate discovery must be separated from assembly

The 2026-08-04 target is decisive on this architectural point. Only `16` from the actual `16,24,29,34,38` entered the frozen 22-number hierarchy. No five-number assembler could recover the other four. The failure must be attributed upstream.

### 2. Dual pools are legitimate risk control

A compact core pool is useful for coalition density, but a broader rescue pool reduces catastrophic exclusion risk. This is not a predictive claim; larger pools mechanically improve recall under the null. Both raw recall and recall-adjusted assembly performance must therefore be reported.

### 3. HLR can be retained as a challenger, not promoted as an edge

The visual pattern idea is falsifiable and did make a correct pre-draw PB direction call for 2026-08-04. However:

- sorted-slot H/L/R states have strong non-50/50 structural probabilities;
- a legacy holdout shows a motif classifier underperforming the exact fair modal direction in every slot;
- the mechanical PB-direction advantage is only 9/14 versus 7/14 and is far too small for significance.

Therefore HLR must be scored relative to the conditional combinatorial null, not against a naïve 1/3 H/L/R baseline.

### 4. PowerBall direction and exact-ball selection should be separate KPIs

The 2026-08-04 H direction succeeded, while the exact VVD/HLR primary candidate 13 missed the main PB15. This is precisely why the layers must not be conflated.

## Failure modes to guard against

1. **Pool inflation masquerading as improved prediction.** A 25-number pool has expected winner recall 2.5 under the null versus 1.3 for a 13-number pool. Report pool size with every recall number.
2. **Directional base-rate neglect.** From current PB15, `L` has fair probability 14/16 = 87.5%. A correct `L` on the next draw would not be surprising.
3. **Post-hoc motif selection.** Every director/AI motif must be frozen before the target draw.
4. **Cross-game credit leakage.** A main-PowerBall prediction that happens to match XTRA cannot be reported as a prospective XTRA success unless XTRA was explicitly targeted pre-draw.
5. **Machine-swap speculation.** Do not infer machine identity from numerical similarity. Require authoritative machine metadata.
6. **Weight chasing.** The mechanical sample is too small; current single-feature candidate recall is approximately null-equivalent.

## Recommendation

Accept the v33.4 workflow changes as an experimental architecture upgrade because they improve attribution, preserve minority hypotheses and prevent one-stage failure from being misdiagnosed as another. Do not claim that v33.4 increases fair-draw winning probability.
