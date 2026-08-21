# PowerBall XTRA — S1 VVD0→10 Conditional Freeze

**Target:** Friday 2026-08-21  
**Mode:** `paper_trading_only`  
**Authority:** experimental XTRA-native direct-transition specialist  
**State source:** canonical XTRA ledger through 2026-08-18  
**Latest XTRA:** `7,11,18,26,31 | PB12`  
**Latest VVD:** `0,16,10,20,17 | 10`

## Hypothesis

Current S1 coordinate is 7 and current S1 VVD is 0. Across all completed XTRA VVD transitions pooled over S1-S5+PB, the successor set after VVD0 is:

`10,10,1,14,6,8,10`

Thus:

- `P(next VVD=10 | current VVD=0) = 3/7 = 42.86%`;
- pooled unconditional next-VVD10 frequency is `12/126 = 9.52%`;
- raw transition lift is approximately `4.50x`;
- using the existing five-observation shrinkage toward the pooled base rate gives a likelihood-ratio near `3.04x`.

The three historical `0→10` completions occurred independently in different XTRA lanes (S2, S3 and PB). Therefore current S1 VVD0 is a legitimate cross-lane transfer opportunity under E0009 methodology.

If the separately frozen S1-H HLR shadow is correct:

`S1 = 7 + VVD10 = 17`.

## Structural red-team control

Exact exchangeable 5/50 order-statistic geometry gives:

- `P(S1=17) ≈ 1.9313%` unconditionally;
- `P(S1=17 | S1>7) ≈ 4.2510%`.

So VVD0→10 has a strong empirical transition residual but maps to a relatively low-base-rate S1 coordinate. This specialist therefore remains `INSUFFICIENT_EVIDENCE`; it must not overwrite the structural/FCPC S1 field.

## Downstream conditional consequence

If S1=17 is imposed, every downstream slot must be reconditioned jointly. S2=13 and all S2 values <=17 become impossible.

Under the exact structural null conditional on `S1=17`, the remaining four numbers are the order statistics of a 4-number sample from 18..50. The conditional slot modes / central structure are:

- S2: mode 18; `P(18)=12.12%`, `P(19)=10.98%`, `P(20)=9.92%`, `P(21)=8.93%`;
- S3: modes 28/29 (about 5.65% each), conditional mean 30.6;
- S4: modes 39/40 (about 5.65% each), conditional mean 37.4;
- S5: mode 50; then49,48,47, conditional mean 44.2.

This is notable because the conditional structural shape after S1=17 independently overlaps several already-frozen tonight candidates: S3 28, S4 38/39, and S5 47/50. The main collision is S2, where the previous direct-VVD primary 13 is invalidated.

## Frozen conditional specialist lines

Pure conditional-structural specialist:

**17,18,28,39,50 | PB2**

FCPC-preserving conditional specialist (uses the first feasible strong FCPC coordinates downstream rather than repairing to the previous S2=13):

**17,21,28,38,47 | PB2**

These are separate challengers only. They do not replace `powerball_xtra_pre_draw.md` or the LRH S1-H shadow freeze.

## Scoring after draw

Score separately:

1. S1 HLR HIGH;
2. S1 VVD0→10 magnitude;
3. exact S1=17;
4. conditional downstream feasibility and exact slots;
5. candidate recall of each specialist line;
6. do not award the old S2=13 expert any credit if it is invalid under the S1=17 branch.

**Evidence:** `INSUFFICIENT_EVIDENCE`; first prospective S1 use of the pooled cross-lane `0→10` transfer.