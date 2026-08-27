# E0012 — Gemini SGCE, In-Wheel Pruning and Adaptive-K Audit

## Status

`ACTIVE AUDIT / NO PREDICTIVE AUTHORITY`

Evidence classification: `INSUFFICIENT_EVIDENCE`

Paper trading only.

## Origin

Red-team review of `collaboration/gemini-code-1787815167938.md` on 2026-08-27.

## Questions

1. Does pairwise co-occurrence graph structure contain future information beyond simple frequency/recency and matched random line geometry?
2. Does moving morphology/polarity/sum filtering inside the wheel generator add predictive information, or only computational efficiency?
3. Does macro-sum volatility justify expanding candidate exposure from K13 toward K18 after matched-exposure controls?
4. Does Gemini's `Core10 + Rescue6..8` proposal add anything beyond the already-registered fixed-K rescue questions in E0007/E0009/E0011?

## Prior architectural constraints

- `NULL_GAP_DM` is uniform over all legal six-gap compositions; it is a structural null, not a predictive line filter.
- Raw K expansion must not receive predictive credit for exposure-driven recall gains.
- Pair/co-occurrence evidence belongs primarily to coalition/assembly unless a separately validated coordinate-level residual score is defined.
- The frozen 2026-08-28 Main artifact remains immutable.

## Falsifiable hypothesis

A fully specified SGCE or adaptive-K challenger may receive predictive authority only if a prospectively frozen implementation improves proper score, candidate recall, or line rank versus matched controls after residualizing simple frequency/recency and preserving explicit exposure denominators.

No predictive edge is assumed from the Gemini contribution itself.