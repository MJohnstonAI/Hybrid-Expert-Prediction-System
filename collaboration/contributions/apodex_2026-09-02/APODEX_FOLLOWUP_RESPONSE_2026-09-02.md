# Apodex Follow-up Response — 2026-09-02

Source: director-supplied `Final Report.html` from Apodex.

Source-of-record SHA-256: `0c0241badda081ce785d0a492740501954a4cfbe286a9e73746b8a1fce8cad31`

This repository note preserves the substantive follow-up answers without embedding the 866 KB HTML/CSS/font payload. The uploaded HTML remains the source of record for exact wording.

## 1. Signed-displacement correction

Apodex explicitly accepts that the original linear model

`q_j(x|p) ∝ P0_j(x) exp(phi_j (x-p_j))`

is not state-dependent because the `p_j` factor cancels in normalization.

Apodex proposes a genuinely nonlinear signed-displacement basis:

- `h1(Δ) = sign(Δ)`;
- `h2(Δ) = sign(Δ) log(1+|Δ|)`;
- `Δ = x-p_j`.

The proposed per-slot conditional family is:

`q_j(x|p_j) ∝ P0_j(x) exp(alpha_j h1(Δ) + beta_j h2(Δ))`.

This keeps HLR/VVD-like information inside one signed-transition family instead of multiplying derived views as independent evidence.

## 2. Adjacent-slot preservation

Apodex accepts that the original preserver was effectively inert because a coordinate outside a Top13 by anywhere probability cannot normally exceed the weakest Top13 member on that same probability.

The follow-up proposes:

- anywhere rank `r_any(v)`;
- best exact-slot rank `r_slot_min(v)`;
- migration margin `m(v)=r_slot_min(v)-r_any(v)`;
- candidate eligibility within a fixed slack below the Top13 cutoff;
- a vulnerability score for incumbents;
- at most a small fixed number of swaps.

The supplied follow-up still includes a final swap condition requiring the omitted coordinate to have greater anywhere probability than the incumbent. ChatGPT's independent audit finds that this retains the same Top13 impossibility and therefore requires another repair before implementation.

## 3. PowerBall championship

Apodex accepts the prototype PB scorer was invalid. It proposes strict walk-forward comparison of:

1. uniform `1/16`;
2. symmetric Dirichlet-shrunk unconditional frequency;
3. strongly shrunk conditional state models using only prospectively-known state.

Primary score: withheld-target multiclass log loss.
Secondary score: withheld-target Brier score.

Hyperparameters must be fixed prospectively rather than chosen from later outcomes.

## 4. Marginal-conditioned coalition challenger

Apodex proposes replacing the prototype smoothed PMI interpretation with a standardized pair-overlap residual conditioned on observed coordinate marginals, followed by empirical-Bayes shrinkage. A 5-number line is scored by mean pairwise shrunk residual over its 10 unordered pairs.

ChatGPT's audit accepts the marginal-conditioning objective but notes that ordinary hypergeometric overlap assumes conditional odds ratio 1, whereas the exact 5-of-50 structural pair process has negative within-draw association. A corrected challenger should therefore use the exact structural conditional overlap law (for example a noncentral-hypergeometric/log-linear offset using the structural pair odds ratio) before shrinkage.

## 5. Synthetic sensitivity

Apodex retracts the implication that measured synthetic results were already available and instead provides a reproducible proposed protocol:

- fixed seed `20260903`;
- null plus small/medium injected signed-transition effects;
- up to 1200 simulated draws;
- walk-forward fitting and proper-score deltas.

This remains a test specification, not reproduced evidence.

## 6. Shrinkage

Apodex says the original approximately-three-pseudo-observation setting was heuristic, not tuned to HEPS outcomes. It proposes a fixed prior-weight-fraction rule.

ChatGPT's audit finds that the interpretation of `s_prior` as a constant fractional prior weight is not algebraically supported by the stated penalty `N/(2 s_prior) * ||theta||^2`; the proposed scaling rule requires re-derivation from Fisher information or an explicit Gaussian prior before use.

## 7. Independent information

Apodex identifies machine identity, ball-set identity and maintenance/configuration events as the highest-value exogenous information source. It proposes a machine-aware, strongly shrunk acquisition/PB lane scored prospectively against machine-agnostic controls.

## 8. Highest-value new idea

Apodex proposes a latent persistent physical-regime mixture with 2–4 regimes and regime-specific transition fields mixed by slowly evolving regime probabilities.

HEPS interpretation: conceptually interesting, but far too parameter-rich for the current ~27-draw Main ledger. Prefer observed/exogenous regime labels and hierarchical shrinkage first; latent EM should remain a later-data research idea.

## 9. Apodex self-red-team

Apodex independently confirms three principal weaknesses:

1. original linear signed-displacement model is not state-dependent;
2. original adjacent-slot preserver is effectively dead;
3. PB and coalition prototype shadows are not rigorously championed.

## Current authority

This response improves the specification of several derivative hypotheses but does not establish predictive lift. All predictive claims remain `INSUFFICIENT_EVIDENCE` until canonical HEPS reproduction and prospective scoring.