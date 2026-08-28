# Main Physics Shadow Experts — E0016

## Scope

This document defines the two director-approved physics-derived Main research roles introduced by `experiments/E0016/`.

They are statistical operators inspired by nonequilibrium transport and anomalous diffusion. They are **not claims that sorted lottery numbers literally travel as physical particles**.

Hard data boundary: `data/draw_history.jsonl` from **2026-06-02 onward only** for these experts. Pre-June PRNG-era history has zero fitted-state authority.

---

## `MAIN_NONEQUILIBRIUM_CURRENT`

### Role

Candidate-funnel **shadow score**.

Purpose: test whether directed next-draw inclusion transitions contain residual temporal asymmetry after shrinkage toward the flat 5/50 global inclusion baseline.

### Construction

For each prior consecutive pair of Main draws `D_u -> D_(u+1)` and each source coordinate `i in D_u`, record whether every destination coordinate `n in 1..50` appears in the next draw.

Shrink the conditional next-inclusion probability toward `0.1`:

`p(i->n) = (hits(i,n) + 10*0.1) / (exposures(i) + 10)`.

Convert to residual log odds:

`r(i->n) = logit(p(i->n)) - logit(0.1)`.

Define antisymmetric probability current:

`A(i,n) = 0.5 * (r(i->n) - r(n->i))`.

For the current draw `D_t`, score candidate `n`:

`J_t(n) = mean_{i in D_t} A(i,n)`.

Z-score the 1..50 vector with a zero-variance guard.

### Shadow comparator

E0016 freezes a **50% incumbent / 50% current-score** counterfactual blend for research scoring only.

Production candidate weights remain unchanged.

### Authority

- diagnostic: yes;
- shadow score/rank: yes;
- shadow K13/K20 counterfactuals: yes;
- change production K or exposure: no;
- hard elimination: no.

### Interpretation rule

Do not describe positive current as proof that the draw machine is a nonequilibrium physical system. The expert measures chronological statistical asymmetry. Future residualization must test whether it adds information beyond recency/frequency.

---

## `MAIN_LEVY_TAIL_DIAGNOSTIC`

### Role

Tail-risk diagnostic only.

Purpose: measure whether the current exact structural VVD model may be under-allocating probability to legal large displacement states.

### Null-residualized heavy-tail family

For slot `j` and previous coordinate `p`, obtain the exact structural displacement distribution:

`q0(d | p) = NULL_VVD_STRUCTURAL`.

Define a low-complexity tail-tilt family:

`q_alpha(d | p) proportional to q0(d | p) * (d+1)^alpha`

with frozen grid:

`alpha in {0, 0.5, 1.0, 1.5, 2.0}`.

`alpha=0` is exactly the structural null and must remain in every comparison.

Select alpha, if any, using only prior post-June slot events by expanding walk-forward log loss. Report whether the selected heavy-tail alternative actually beats the structural null.

### Outputs

- selected alpha by slot;
- log-loss delta versus `NULL_VVD_STRUCTURAL`;
- null 90th-percentile displacement threshold;
- tail probability mass;
- diagnostic tail-pressure flag.

### Authority

- diagnostic: yes;
- normal candidate ranking: no;
- rescue-seat allocation: no;
- change K: no;
- hard elimination: no.

The notable 2026-08-21 tail description receives no special future weight.

---

## Computational rule

Both experts must run numerically without LLM calls in the inner loop. Their presence must not materially slow routine HEPS analysis.

## Promotion rule

Any authority increase requires a separate prospective experiment, matched exposure, redundancy controls and a deliberate promotion decision. One successful future target is insufficient.
