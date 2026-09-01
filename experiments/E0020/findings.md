# E0020 Findings — Main Terminal Motifs

## Executive result

`INSUFFICIENT_EVIDENCE`.

The XTRA observation generated a legitimate Main question, but the current Main ledger does not show predictive terminal-motif edge strong enough to alter HEPS.

## 1. Repeated words exist, but multiplicity matters

Across S1..S5, same-slot repeated length-3 words occurred 4 times versus 1.1044 on average in 5,000 within-slot marginal-preserving shuffles. The unadjusted empirical p-value is approximately 0.0302.

However eight primary sequence diagnostics were inspected (same/cross L2-L4, ABA, ABAB). Holm adjustment raises the length-3 result to approximately 0.242. It is therefore a discovery clue, not evidence of a stable edge.

The most interesting exact replay is S3 word `2,7,0`, whose two historical occurrences were both followed by terminal `7`. Other repeated words did not show stable continuation.

## 2. Suffix prediction does not beat the exact terminal null

Across 90 Main slot-target observations:

- exact terminal null log loss: 2.289626;
- same-slot longest suffix: 2.332522;
- cross-slot longest suffix: 2.321306;
- Markov-1: 2.344822.

Lower is better. All three learned terminal models were worse than the exact slot-aware null overall.

Slot-specific diagnostics show some heterogeneity (especially S1), but selecting a slot/model after seeing these results would create another researcher-degree-of-freedom problem. A walk-forward champion selector among M0/same/cross/Markov also failed to beat M0.

## 3. The proposed synergy chain currently hurts proper score

Using the same-slot suffix model and exact residual ratios:

- M0 structural coordinate log loss: 3.367651;
- M1 + terminal motif: 3.410547;
- M2 + HLR: 3.436837;
- M3 + VVD: 3.748890.

Mean actual-coordinate rank also deteriorated from 11.87 under M0 to 14.93 under M3.

This does not prove terminal/HLR/VVD information is absent. It shows this particular residual-combination path is not presently an acquisition improvement on the available 18-target replay.

## 4. Algebraic library

Among the six preregistered Main algebraic rules, the best was `(2b-a) mod 10` with 11/90 terminal hits versus approximately 9.24 expected under the relevant slot-specific terminal nulls. The unadjusted upper-tail probability is ~0.318. No edge detected.

For PowerBall, `repeat_b` produced 5/18 terminal hits versus 2.1875 expected under the exact non-uniform PB terminal null. The unadjusted p-value is ~0.058, but Holm adjustment across six rules is ~0.349. PB suffix and Markov models were both worse than the exact PB terminal null on log loss.

## 5. Current 2026-09-01 state

No current Main slot has an exact same-slot suffix match of length >=3. Current same-slot suffix supports are:

- S1: L1, support 3;
- S2: L2, support 1;
- S3: no historical suffix continuation;
- S4: L1, support 1;
- S5: L1, support 2.

This is not a strong motif state.

The finite algebraic rules show visible current convergence for some slots (for example S1 several rules output residue 4, and S5 several output residue 2), but the historical algebraic championship did not beat the exact null. These calls therefore remain shadow diagnostics only.

## 6. Current M4 shadow

For prospective bookkeeping only, M3 is ranked inside the already-frozen E0019 K20 envelope. This does not change E0019 or the production slate. The top shadow line is `[26,30,32,34,43]`.

## Strongest supporting evidence

Nominal excess of same-slot L3 repeated words and one exact S3 continuation replay.

## Strongest counterargument

The actual predictive suffix models are worse than the exact terminal null, the L3 excess does not survive multiplicity correction, and the M1-M3 synergy chain worsens coordinate proper scores.

## Recommendation

Retain E0020 as a low-cost prospective shadow. Do not modify the frozen 2026-09-01 Main prediction. Revisit only if prospective terminal log loss or exact-coordinate rank improves consistently versus exact null and no-motif controls.