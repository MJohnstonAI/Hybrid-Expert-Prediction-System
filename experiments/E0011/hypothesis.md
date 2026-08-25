# E0011 — Null-Control, Residual Convergence and Conditional PowerBall Transitions

## Status

`PROPOSED PROSPECTIVE SHADOW`

Evidence classification: `INSUFFICIENT_EVIDENCE`

Paper trading only.

## Origin

Synthesis on 2026-08-25 after red-team review of the Ox Alpha contribution dated 2026-08-24.

The contribution is not accepted wholesale. E0011 keeps only the parts that survive mathematical and architectural review and explicitly records the rejected parts so they cannot drift into HEPS as folklore.

## Accepted research ideas

1. **Null-control pipeline as comparator, not candidate selector.** Exact structural nulls remain the mandatory calibration/reference model. Under IID 5/50, the global marginal inclusion probability is `P(n appears)=0.1` for every coordinate, so a pure structural-null global field cannot rank a predictive K13.
2. **Statistical-power honesty gate.** Every prospective comparison must state the minimum effect worth detecting, paired metric, approximate target horizon and dependence assumptions. Small-n non-significance is not evidence of absence.
3. **Expert residualization / redundancy audit.** Convergence confidence may count only information that remains after removing exact structural-null and simple-recency effects. Correlated experts may not be counted as independent votes merely because they have different names.
4. **Conditional PowerBall transition shrinkage.** PowerBall modelling should estimate `P(PB_{t+1}=n | PB_t=s)` and `P(VVD_{t+1}=d | VVD_t=v)` with shrinkage toward simple baselines, then combine them with HLR direction before translating to exact balls.
5. **Algebraic motifs remain diagnostic.** Algebraically equivalent formulas and matrix-wide correlated lane agreement do not earn independent convergence weight.

## Rejected Ox Alpha elements

### Rejected R1 — null-derived global-mobility rescue

A structural-null field has `P(n appears)=0.1` for all 50 main coordinates. Therefore a rule that selects rescue coordinates by 'highest null global mobility' is undefined because every coordinate ties. This rule is rejected.

Tail rescue remains an open E0009/E0007 question, but any rescue selector must use a genuinely non-flat, prospectively frozen residual signal and fixed total K.

### Rejected R2 — pure null K13 retained-mass ranking

For any flat K13 coordinate basket under IID 5/50, exact 5/5 survival is `C(13,5)/C(50,5)`. A pure null global marginal cannot prefer one 13-number set over another. Null-first remains a comparator/calibration pipeline only.

### Rejected R3 — unconditional PowerBall frequency as the state-transition model

A symmetric Dirichlet posterior over unconditional PB counts is a useful baseline but does not implement the XTRA-inspired state-transition method. The experimental model must be conditional on current PB state and current PB VVD, with strong shrinkage because observations per state are sparse.

### Rejected R4 — significance language stronger than evidence

A non-significant or null-like result such as `p≈0.45` supports 'no detected advantage at this sample/exposure', not proof that an effect is zero. Future reviews must preserve that distinction.

## Core falsifiable hypothesis

A HEPS convergence score that:

- calibrates every component against exact structural nulls;
- residualizes expert scores against structural geometry and recency;
- counts only demonstrably non-redundant residual information;
- uses hierarchical conditional PB transition distributions;

will improve calibration and reduce false confidence relative to raw expert-vote convergence. Predictive lift is not assumed and must be demonstrated prospectively.

## Relationship to E0009

E0011 is a methodological companion to E0009. E0009 remains the distribution-first candidate-field experiment. E0011 supplies the corrected null-control, redundancy and PB-transition rules that E0009 may use prospectively after they are frozen.

## First eligible target

`2026-08-28` or later.

No 2026-08-25 Main target is claimed by E0011; this package was created on the day of that draw and receives no credit for it.