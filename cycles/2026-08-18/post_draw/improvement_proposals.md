# 2026-08-18 — Improvement Proposals for 2026-08-21 Research

Evidence classification: `INSUFFICIENT_EVIDENCE`.

## 1. Restore probability-first VVD use

Do not let E0008 point motifs override `NULL_VVD_STRUCTURAL` or E0005 VVD-R. Use motif signals only as residual modifiers until they demonstrate prospective lift.

## 2. Preserve Friday HLR disagreement

From current `[3,7,20,31,39]`, exact structural geometry strongly favors `HHHHH` (joint probability 0.386814, rank 1/243). The director challenger `HHLHH` remains structurally plausible (0.0326663, rank 7/243) but differs only at S3. BARP reconstructed from the frozen formula currently gives modal `HHHLH`, creating a useful S4 disagreement. Do not force consensus before freeze.

## 3. Direct cross-lane VVD successors worth shadow testing

Current VVD state is `[11,8,1,8,5] | PB10`.

- VVD8 -> VVD2 occurred 2/10 pooled opportunities versus unconditional VVD2 rate 8.73%. Relevant to S2/S4. For S4 HIGH, VVD2 maps `31 -> 33`.
- VVD1 -> VVD8 occurred 4/14 versus unconditional VVD8 rate 9.52%. Relevant to S3. Under S3 LOW this maps `20 -> 12`; under HIGH it maps `20 -> 28`.
- VVD5 -> VVD7 and VVD5 -> VVD5 each occurred 3/12. Under S5 HIGH these map `39 -> 46` and `39 -> 44`.

These are small-sample exploratory transitions, not promoted rules.

## 4. Candidate relay remains soft only

Historical co-occurrence gives number40 four links into the current draw `{3,7,20,31,39}`, more than any other noncurrent coordinate. But walk-forward graph ranking is near matched-exchangeable performance. Keep 40 as a soft relay/cluster candidate, not a hard anchor.

## 5. PowerBall direction and magnitude should be separated

From PB13, exact structural direction is LOW 75%, REPEAT 6.25%, HIGH 18.75%. The recent `LHLHLHLH` alternation also points LOW but should not be treated as independent evidence.

For magnitude, PB history favors VVD2 and VVD5 by raw frequency. The only earlier PB VVD10 was followed by VVD5, mapping LOW `13 -> 8`. Algebraic VVD2 maps `13 -> 11`. Pooled six-lane VVD10->VVD3 is exploratory and maps `13 -> 10`. VVD8 -> PB5 remains a weaker algebraic branch.

## 6. Working Friday candidate regions, not frozen

- S1 HIGH: `5,10,14,4`
- S2 HIGH: `8,11,9,15,13`
- S3 LOW challenger: `19,18,12`; HIGH structural control: `21,25,27,28`
- S4 HIGH: `33,40,32,41`; BARP LOW hedge: `30,29,22`
- S5 HIGH: `44,46,47,40`
- PB LOW: `8,11,10,5`

No Friday slate is frozen by this document.
