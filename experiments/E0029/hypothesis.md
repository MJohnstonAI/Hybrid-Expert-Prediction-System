# E0029 — K13 Pattern-Constraint Triage and Spectral-Rescue Championship

**Experiment ID:** `E0029`  
**Lane:** Main  
**Stage:** frozen-K13 assembly / morphology / winner-float ranking  
**Mode:** paper trading only  
**Evidence classification:** `INSUFFICIENT_EVIDENCE`

## Research question

Once a Main K13 is frozen and all `C(13,5)=1,287` legal five-number lines are enumerated, can low-dimensional transition-pattern constraints eliminate or demote bad combinations while disproportionately preserving the true winner state?

This experiment isolates **line selection after acquisition**. It receives no candidate-acquisition credit.

## Motivation

HEPS already has evidence that:

- HLR can contain useful directional information;
- E0028 Last-Digit Sum Absolute-Delta (LDSAD) contains an interesting but post-hoc discovery concentration;
- total-sum and span absolute-delta transitions are plausible low-dimensional whole-line patterns;
- E0013 spectral is a stronger historical Main coalition ranker but remains unstable;
- hard morphology pruning is dangerous unless winner-retention exceeds line-space retention.

The intended architecture is therefore not a naive intersection of hard rules. It is a **risk-controlled pattern triage** followed by a separate coalition ranker.

## Pattern family

For every target, using only draws strictly before that target, construct four pattern lanes:

1. `BARP_HLR_RESIDUAL` — E0005 BARP HLR probability expressed as a residual tilt relative to the exact structural HLR slot null. HLR is used once as the signed-transition direction view; it is not multiplied with VVD or terminal views.
2. `LDSAD_ADAPTIVE_RESIDUAL` — target-excluded, strongly shrunk residual distribution for `abs(SLD_t-SLD_(t-1))` relative to its exact 5/50 structural expectation.
3. `SUMAD_ADAPTIVE_RESIDUAL` — target-excluded residual for `abs(sum_t-sum_(t-1))`.
4. `SPANAD_ADAPTIVE_RESIDUAL` — target-excluded residual for `abs(span_t-span_(t-1))`, where `span=S5-S1`.

Each lane is converted to an average-midrank percentile across the 1,287 K13 lines.

## Pattern-OR

Define one robustness/meta-pattern operator:

`PATTERN_OR(line) = max(HLR_pct, LDSAD_pct, SUMAD_pct, SPANAD_pct)`.

This is **not** interpreted as four independent likelihood votes. It is an anti-burial operator: a line may survive when one preregistered pattern lane provides strong support even if another pattern lane fails.

## Primary challenger — conservative gate with spectral rescue

The primary E0029 challenger is:

1. enumerate all 1,287 lines from frozen K13;
2. retain the top 80% by `PATTERN_OR`;
3. additionally retain any line in the top 5% of E0013 spectral rank, even if Pattern-OR would exclude it;
4. rank retained lines by E0013 spectral score using average-midrank handling;
5. place excluded lines below retained lines, ordered only for diagnostic completeness;
6. do not change K13 or line budget.

This is named:

`MAIN_PATTERN80_SPECTRAL5_RESCUE`.

The top-5% spectral rescue is a bounded preservation rule intended to prevent a morphology gate from deleting an elite independent coalition line at negligible compression cost.

## Discovery-only challengers

Also score, without promotion authority:

- Pattern-OR alone;
- equal-mean pattern consensus;
- Pattern-OR gates retaining 50%, 60%, 70%, and 80%;
- E0013 spectral alone;
- E0022 Dissent-OR;
- fixed post-hoc bands from E0028 and related discovery (`LDSAD 11..13`, `SUMAD 8..9`, `SPANAD 5..6`) as explicitly post-hoc upper-bound diagnostics only.

## Hypotheses

### H1 — pattern triage

At matched oracle-K13 exposure, adaptive Pattern-OR should rank the exact winner above random expectation and reduce catastrophic burial without using target outcomes in any target's feature estimates.

### H2 — staged cascade

A Pattern-OR gate followed by E0013 spectral should outperform E0013 spectral alone because the pattern family and spectral coalition geometry capture different line-level information.

### H3 — conservative elimination

The primary 80% Pattern-OR gate plus top-5% spectral rescue should eliminate a material fraction of K13 lines while retaining the winner materially more often than a random gate of the same size.

## Falsification

Reject predictive promotion if any of the following hold prospectively:

- winner-gate survival is not materially above the fraction of lines retained;
- winner percentile does not exceed random/ incumbent rankers across multiple future targets;
- the effect disappears under independent decoy seeds;
- the gain depends on the post-hoc fixed bands rather than target-excluded adaptive fields;
- a meaningful gain requires hard deletion that reduces winner retention below the governance safety threshold;
- Main results fail independent reproduction.

## Evidence boundary

The 2026-06-02 through 2026-09-01 replay is a **target-excluded blind replay designed after the outcomes existed**. It is discovery evidence, not prospective confirmation. No `BREAKTHROUGH` claim is permitted from E0029 alone.
