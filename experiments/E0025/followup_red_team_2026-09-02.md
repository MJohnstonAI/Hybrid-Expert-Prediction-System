# E0025 Follow-up Red-Team — Apodex Response 2026-09-02

## Overall assessment

Apodex's follow-up materially improves the original contribution because it explicitly accepts the three core defects found in the first audit and supplies clearer replacement hypotheses. However, two of the proposed repairs still contain structural problems and must not be implemented verbatim.

Evidence classification remains `INSUFFICIENT_EVIDENCE` for prediction.

## A. Signed-transition replacement

### Accepted part

The nonlinear basis

- `h1(Δ)=sign(Δ)`
- `h2(Δ)=sign(Δ) log(1+|Δ|)`

is genuinely previous-state dependent and is a valid low-dimensional one-family transition representation.

### Critical correction required

Apodex then proposes full-line slot factors

`A_j(x)=P0_j(x) R_j(x|p_j)`

and a legal-line DP proportional to `product_j A_j(x_j)`.

That is not the current HEPS null-preserving construction. Multiplying the five exact slot marginal nulls over a legal line reintroduces order-statistic geometry multiple times. Zero residual signal would not return to the exact uniform 5-of-50 line law.

Correct construction:

1. Fit each conditional slot model against its exact slot null:
   `q_j(x|p_j) ∝ P0_j(x) R_j(x|p_j)`.
2. Form residual ratio:
   `T_j(x|p_j)=q_j(x|p_j)/P0_j(x)`.
3. Build the full legal-line field from the exact uniform legal-line null:
   `Q(line) ∝ P0_line(line) * product_j T_j(x_j|p_j)`.
4. Since `P0_line=1/C(50,5)` is constant and per-slot normalizers factor out, ranking/DP weights may use `product_j R_j(x_j|p_j)` directly.
5. Mandatory unit test: `alpha=beta=0` for all slots must yield exactly uniform probability over all 2,118,760 legal lines and exact structural slot marginals.

This preserves the useful Apodex nonlinear basis while keeping v35 joint-distribution doctrine intact.

## B. Adjacent-slot preservation remains logically dead

Apodex correctly observes the original Top13 paradox, but its replacement still requires, for omitted candidate `u` and incumbent `v*`:

`p_any(u) > p_any(v*)`.

If K13 is the strict Top13 under `p_any`, every omitted `u` satisfies `p_any(u) <= p_any(v)` for every incumbent at the boundary. Therefore the new final swap condition is still unavailable except ties.

### Recommended repair

A true preservation challenger must explicitly accept a bounded primary-score sacrifice in exchange for orthogonal migration evidence. Two clean designs are permitted for testing:

1. **Constrained line-mass swap**: among candidates with fixed migration criteria and anywhere rank <= K+s, allow a swap only if the complete-line containment objective `M(K)` improves; or
2. **Predeclared composite preservation score**: define before replay a standardized combination of anywhere score and migration score, then select exactly K=13 by that score. Compare against pure `p_any` Top13 at matched K.

Do not use hindsight coordinates or enlarge K.

## C. PowerBall championship

The follow-up PB protocol is methodologically sound in structure:

- strict withheld-target walk-forward;
- uniform, unconditional Dirichlet and strongly-shrunk conditional lanes;
- multiclass log loss primary, Brier secondary;
- prospectively fixed priors/state variables.

This is compatible with the repaired PB tooling already created in E0025. The specific hyperparameter rule supplied by Apodex should be treated as a new prospective challenger, not retrospective evidence.

## D. Coalition residual — structural correction

Conditioning pair overlap on observed marginals is the right research direction, but the ordinary hypergeometric law

`C_ij ~ Hypergeometric(N,C_i,C_j)`

corresponds to conditional odds ratio 1. Under exact 5-of-50 sampling, distinct coordinates are structurally negatively associated within each draw:

- `P(i)=P(j)=0.1`
- `P(i,j)=20/(50*49)=0.0081632653`
- structural 2x2 odds ratio is approximately `0.7822222`, not 1.

Therefore a more exact marginal-conditioned null should preserve this structural odds ratio, e.g. Fisher's noncentral hypergeometric conditional distribution (or equivalent log-linear model with fixed structural offset), followed by empirical-Bayes shrinkage.

This corrected operator is a legitimate E0013 challenger candidate.

## E. Synthetic sensitivity claim downgraded

The original report implied the synthetic probe had already demonstrated null neutrality and signal detection. The follow-up states measured numerical results cannot be supplied and instead gives a protocol specification. Therefore prior wording suggesting synthetic empirical proof receives no evidence credit.

The proposed simulation must also use the corrected uniform-line residual construction above, not `product_j P0_j R_j`.

## F. Shrinkage interpretation requires re-derivation

Apodex's penalty is stated as

`N/(2 s_prior) * ||theta||^2`.

The follow-up interprets `s_prior≈3` and later `s_prior(N)=delta/(1-delta)*N` as controlling a fixed fractional prior weight. That interpretation is not generally valid because likelihood curvature and penalty curvature scale differently. The prior should instead be specified directly (e.g. Gaussian variance fixed prospectively) or calibrated to expected Fisher information under the exact null.

No `s_prior` scaling rule should be promoted until this is re-derived and unit-tested.

## G. Physical-state research

Machine/ball-set metadata remains the most promising independent-information proposal. Prefer observed state labels with hierarchical shrinkage. The latent 2–4-regime EM mixture is too parameter-rich for the present Main sample and should remain deferred until substantially more data or externally observed regime labels exist.

## Recommended derivative work

1. Repair E0021 with Apodex nonlinear signed basis but HEPS residual-ratio/uniform-line construction.
2. Build a genuinely operative fixed-K migration challenger using `M(K)` or a preregistered composite score.
3. Add a structural-odds-offset pair residual challenger to E0013.
4. Continue E0025 PB walk-forward shadows.
5. Backfill machine/ball-set provenance and create a hierarchical observed-regime experiment when metadata quality permits.

No Friday Main production change is justified by this follow-up alone.