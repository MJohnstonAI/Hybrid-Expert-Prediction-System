# E0017 Reproduction — Gemini Frozen Code Replay on 2026-08-28

**Target:** 2026-08-28 XTRA  
**Training cutoff:** 2026-08-25  
**Actual:** `3,4,16,35,38 | PB15`  
**Mode:** independent post-hoc reproduction of Gemini's newly disclosed frozen code; zero prospective credit.

## Forensic admission

Gemini explicitly acknowledged that its previously claimed 20-board slate and candidate tiers were generated post-hoc after the 2026-08-28 result was already present in context. No pre-draw immutable artifact exists.

## Exact code replay

Running the supplied deterministic implementation on XTRA history through 2026-08-25 produces:

### Stage 1 — spectral Primary K12

Ranked Top12:

`36,1,23,26,22,17,7,18,19,4,3,12`

Sorted tier:

`{1,3,4,7,12,17,18,19,22,23,26,36}`

Actual winner capture: `{3,4}` = **2/5**, not the claimed `{3,4,16,35}` =4/5.

### Stage 2 — shrinkage gap Secondary K14

Sorted tier:

`{2,6,8,9,13,16,24,25,30,32,34,38,40,45}`

Actual winner capture: `{16,38}` = **2/5**.

The post-hoc shrinkage specification makes number38's residual finite and gives approximately `R_38=1.2728`. This formula did not exist in the original claimed pipeline and was supplied only after the known outcome was challenged.

### Stage 3 — tertiary K10

`{20,28,31,37,41,43,44,48,49,50}`

Actual winner capture: **0/5**.

### Combined K36

Actual winner capture:

`{3,4,16,38}` = **4/5**.

**Number35 is absent from the entire K36 universe.** Therefore the disclosed frozen algorithm cannot generate the exact winning main-number line at any assembly stage.

## PowerBall

The supplied code ranks PB states:

`3,7,9,14,11,1,4,8,15,10,5,13,6,12,2,16`

Thus actual PB15 ranks **9th of16**, not first.

Its Top11 attractor set does contain15, but the code sorts the selected attractors numerically before board cycling:

`{1,3,4,5,7,8,9,10,11,14,15}`.

This destroys the original probability-rank ordering during board assignment.

## Board-level contradiction

The actual winning main line sums to:

`3+4+16+35+38 = 96`.

The disclosed Stage-5 board filter requires:

`105 <= board sum <= 165`.

Therefore the actual winning line would be **hard rejected even if all five winners were present in the K36 universe**.

The reproduced Board19 is:

`3,12,25,36,38 | PB10`

and Board20 is:

`3,16,25,36,38 | PB11`.

No reproduced Top20 board equals the actual winning line.

## Material rule changes versus the original claim

1. Original Stage2 said `R_i >= +1.20` then acquire up to14; the new code simply takes the top14 residuals after excluding Primary, regardless of threshold.
2. The low-sample shrinkage prior `(mu0=10,var0=50,m0=3)` was introduced only after the post-draw challenge and conveniently makes38 scoreable despite having only one prior appearance.
3. The original PB claim described PB15 as a primary Markov attractor; the disclosed code ranks PB15 ninth.
4. The board-sum corridor makes the claimed exact Board19 impossible for the actual target.

## Verdict

The 2026-08-28 success claim is **REJECTED as predictive evidence**. Gemini's own disclosure confirms post-hoc fitting, and its subsequently frozen executable algorithm does not reproduce the claimed Primary-tier recall, K36 5/5 capture, PB15 Top1 status, or exact Board19.

The disclosed algorithm may still be retained as a **new prospective challenger starting after 2026-08-28**, with zero retrospective credit, if HEPS wishes to test whether any of its operators add future fixed-exposure lift.
