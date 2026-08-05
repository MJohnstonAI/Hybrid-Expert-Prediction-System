# HEPS_BREAKTHROUGH_HANDOFF.md

## 1. Verdict

PROVISIONAL SIGNAL

## 2. Algorithm name

GPR-8 — Gap-Phase Residual Ensemble

## 3. Core idea

GPR-8 ranks each number using three strictly lagged signals: a sparse recurrence-phase score derived from the number’s draw-gap, a shrunk nonparametric gap hazard, and a modulo-8 residual-state score based on the immediately previous draw. Each component is standardized across numbers 1–50 and combined with fixed weights 0.50/0.25/0.25. The machinery is ordinary statistical scoring: no physical or quantum claim is made. Historical 2018–2025 data were used only to select and freeze generic parameters; the 2026 mechanical state is reset so current gaps use only prior mechanical draws. The model showed a repeatable Top-15 lift over recency but did not beat recency at Top-20 and did not beat the random mean-rank expectation. It therefore remains a prospective research lane, not an accepted HEPS module.

## 4. Mathematical definition

For target draw `t`, let `T` be the number of prior mechanical-era draws available and let `D_j` be the set of five main numbers in prior draw `j`.

For candidate `n in {1,...,50}`, define the recurrence gap

`g_t(n) = T - max{j : n in D_j}` if previously seen, otherwise `T + 1`.

### Phase component

Construct `phi(g) = [g, log(1+g), cos(pi*g), sin(2*pi*g/3), cos(2*pi*g/3), ..., sin(2*pi*g/8), cos(2*pi*g/8)]`, with the mathematically degenerate `sin(pi*g)` feature explicitly excluded. Standardize each feature using frozen `mu_j, sigma_j`, then

`P_t(n) = sigmoid(b0 + sum_j beta_j * (phi_j(g_t(n)) - mu_j) / sigma_j)`.

### Gap-hazard component

Let `b = min(g_t(n), 30)`. `G_t(n) = H[b]`, where `H` is the frozen Beta-shrunk empirical hazard table listed below.

### Modulo-8 residual component

Let `c_t(n) = |{x in D_(t-1) : x mod 8 = n mod 8}|`. Then `R_t(n) = Q[c_t(n)]`, with frozen table `Q[0..5]` below.

For any 50-vector `v`, define cross-candidate standardization `Z(v_n) = (v_n - mean(v))/sd(v)`; if `sd(v)=0`, set all `Z(v_n)=0`.

Final score:

`S_t(n) = 0.50*Z(P_t(n)) + 0.25*Z(G_t(n)) + 0.25*Z(R_t(n))`.

Rank 1–50 by descending `S_t(n)`. Use ascending number only as a deterministic tie-break.

## 5. Required inputs

- Mechanical-era draw history strictly before target `t`: draw date and five main numbers only.
- Frozen GPR-8 parameter set in Section 7.
- For parameter re-estimation/reproduction only: `Train on Main.xlsx`, 811 historical Main draws from 2018-01-09 through 2025-10-17. Do not carry its gap/recency state into 2026.
- Repository ledger must be updated through 2026-08-04 before reproducing the reported mechanical evaluation; current `main` was observed to stop at 2026-07-14.

## 6. Pre-draw procedure

1. Read only mechanical draws strictly before the target.
2. For each `n=1..50`, compute `g_t(n)`.
3. Compute frozen phase probability `P_t(n)`.
4. Compute `G_t(n)` from the capped gap-hazard table.
5. From the immediately previous mechanical draw, compute modulo-8 occupancy `c_t(n)` and `R_t(n)`.
6. Z-standardize each of the three 50-number component vectors independently.
7. Compute `S_t(n)` with weights 0.50/0.25/0.25.
8. Freeze the 1–50 ranking before the draw is revealed.
9. Score winner ranks and Top-K capture after the result is appended.

## 7. Parameters

Selection protocol: the earliest 30 historical draws were warm-up; targets 31–500 (`470` targets) formed the discovery/training block; targets 501–811 (`311` targets, `1,555` winning coordinates) formed the untouched historical validation block. Ninety-three exploratory variants across ten families were searched. Selection used the mean relative recall lift versus recency over `K={10,12,15,20,25}`. The selected weights were `0.50/0.25/0.25`. After red-team detection of the degenerate `sin(pi*gap)` implementation, that feature was removed and the same weights/hyperparameters were rerun without retuning. Final frozen parameters were then refit on historical targets 31–811.

- Phase model: L1 logistic regression, `C=0.1`, liblinear solver; periods 2–8, with `sin(pi*g)` excluded.
- Phase intercept `b0 = -2.195421421477160`.
- Nonzero standardized phase coefficients `(feature, mu, sigma, beta)`:

  - `log_gap`: mu=2.08140010678943, sigma=0.82905687855001, beta=-0.0299276266996155
  - `sin_g_p3`: mu=0.031425300823625, sigma=0.724311429662214, beta=-0.0044293537384761
  - `cos_g_p3`: mu=-0.0512291933418694, sigma=0.686848580895916, beta=0.019341196357027
  - `sin_g_p4`: mu=0.0557746478873239, sigma=0.72345951516806, beta=0.00803191688419053
  - `cos_g_p4`: mu=-0.0493213828425096, sigma=0.686340236151443, beta=-0.00712506900352874
  - `sin_g_p5`: mu=0.0743772306020437, sigma=0.721828551356678, beta=-0.00860545049101482
  - `cos_g_p5`: mu=-0.0474393244076665, sigma=0.686426311058888, beta=0.0228507472707761
  - `cos_g_p6`: mu=-0.0452112676056338, sigma=0.687270939739649, beta=-0.0267055790964603
  - `sin_g_p7`: mu=0.11374018920466, sigma=0.715820193379292, beta=0.00433733090800729
  - `sin_g_p8`: mu=0.132016528824671, sigma=0.712202448422174, beta=-0.027756928445179

- Gap hazard: cap `30`; Beta prior mean `0.10`, prior strength `10`.
- Frozen `H[1..30]`:

`[0.099361430396, 0.104905018429, 0.101329955668, 0.105671010919, 0.100000000000, 0.109798775153, 0.088321884200, 0.095161290323, 0.106420927467, 0.087217043941, 0.102694828842, 0.087662337662, 0.105075690116, 0.103482587065, 0.122787610619, 0.099496221662, 0.090655509066, 0.087155963303, 0.096989966555, 0.077777777778, 0.116232464930, 0.088235294118, 0.103960396040, 0.110192837466, 0.129230769231, 0.095406360424, 0.066406250000, 0.133333333333, 0.106280193237, 0.089041095890]`

- Residue modulus: `8`; Beta prior mean `0.10`, prior strength `300`.
- Frozen `Q[0..5]`:

`[0.099387129724, 0.102011038508, 0.095971563981, 0.097058823529, 0.097719869707, 0.100000000000]`

## 8. Walk-forward evidence

### Historical untouched validation (corrected GPR-8)

- Targets tested: 311; winners: 1,555.
- Winner mean rank: 25.03; median rank: 25.0; MRR: 0.0916.
- Top-10 recall: 333/1555 (21.4%).
- Top-15 recall: 499/1555 (32.1%).
- Top-20 recall: 652/1555 (41.9%).
- Top-20 3+/5 capture: 118/311 (37.9%).
- Recency comparison: mean rank 25.39; Top-10 314/1,555; Top-15 459/1,555; Top-20 629/1,555.

### 2026 mechanical-era sensitivity block

State was reset at the mechanical transition. The first five mechanical draws (2026-06-02 through 2026-06-16) were warm-up; 14 targets from 2026-06-19 through 2026-08-04 were scored, giving 70 winning coordinates. Because the numerical-degeneracy correction was made after the initial mechanical result summary had been inspected, this block is conservatively treated as a sensitivity check, not fresh confirmation.

- Winner mean rank: 25.81; median rank: 24.5; MRR: 0.0779.
- Top-10 recall: 14/70 (20.0%).
- Top-15 recall: 25/70 (35.7%).
- Top-20 recall: 30/70 (42.9%).
- Top-20 3+/5 capture: 5/14 (35.7%).
- Random expectation: mean rank 25.50; Top-10 20%; Top-15 30%; Top-20 40%.
- Recency: mean rank 27.33; Top-10 10/70; Top-15 18/70; Top-20 30/70.
- Frequency: mean rank 27.46; Top-10 15/70; Top-15 20/70; Top-20 24/70.
- Current HEPS candidate-engine artifact was not present on the queried repository `main` paths, so no paired HEPS-engine comparison is claimed here.

## 9. Null and statistical assessment

Historical validation was used for model selection across 93 variants, so raw p-values there are exploratory and must not be read as confirmatory. For corrected GPR-8, exact random tails were Top-15 p=0.033 and Top-20 p=0.056; Bonferroni adjustment over the 93-variant search removes any nominal significance.

On the 14-target mechanical sensitivity block, exact random tails were Top-10 p=0.552, Top-15 p=0.170, Top-20 p=0.349; mean-rank lower-tail p=0.577. Against recency, exact draw-level sign-flip tests gave p=0.097 for the Top-15 hit-count advantage and p=0.609 for Top-20 (tie), with p=0.166 for the mean-rank improvement. Denominators are 14 targets / 70 winners.

The model therefore fails the BREAKTHROUGH criteria: it does not establish better mean ranking than random, does not beat recency at Top-20, and lacks a fresh untouched post-correction confirmation block. Repository-only reproducibility is also incomplete until the canonical ledger is updated through 2026-08-04.

## 10. Why this might add independent information

The three inputs are not identical transforms of recency. The phase term allows non-monotone recurrence effects at short integer gap periods; the hazard table estimates pooled conditional hit rates by current gap with shrinkage toward the fair-draw prior; the modulo-8 term conditions on the previous draw’s residue occupancy. Their validation errors were only partially aligned, so standardized combination improved balanced Top-K compression relative to each component. If any real machine/process memory exists, these features could capture it without using candidate identity or future targets. However the apparent lift is small, multiple-search exposure is large, and the corrected implementation lacks a fresh untouched confirmation block. The proper interpretation is therefore 'possible independent information worth one frozen prospective test', not evidence that the lottery is predictably non-random.

## 11. Falsification rule

Freeze the corrected GPR-8 parameters above. Do not retrain or change weights. Evaluate the next 12 South African PowerBall mechanical-era Main draws after 2026-08-04 (60 winning coordinates), using only history available before each target. Reject GPR-8 if, after all 12 targets, **either** (a) cumulative Top-20 recall is not strictly greater than simple recency on the same targets, **or** (b) mean winner rank is not strictly lower than recency. Even if both survive, do not promote to BREAKTHROUGH unless the Top-20 advantage is not driven by one draw and an exact/matched-null assessment is at least directionally unusual.

## 12. Integration specification

Do not merge into accepted HEPS architecture yet. In the experimental harness, expose one score per candidate:

`candidate_score_gpr8[n] = S_t(n)` for `n=1..50`.

HEPS may consume this only as an isolated candidate-discovery lane: rank by the score, inspect Top-K sets, and compare against recency/frequency. Do not alter coalition assembly, line construction, bonus-ball logic, or accepted expert weights. If the prospective falsification test fails, delete/retire the lane rather than retuning it on the failed targets.

## 13. Minimal pseudocode

```text
prior = mechanical_draws_before(target)
for n in 1..50:
    g[n] = draws_since_last_hit(prior, n) else len(prior)+1
    phase[n] = frozen_sparse_logit(phi_without_sin_pi_gap(g[n]))
    gap_h[n] = H[min(g[n], 30)]
    c = count(x in prior[-1] where x mod 8 == n mod 8)
    resid[n] = Q[c]
zp = zscore_across_50(phase)
zg = zscore_across_50(gap_h)
zr = zscore_across_50(resid)
score[n] = 0.50*zp[n] + 0.25*zg[n] + 0.25*zr[n]
return rank_desc(score)
```

## 14. Failed-neighbour warning

- Lag-graph diffusion was clearly weak: best validation Top-20 598/1,555 and mean winner rank about 25.85.
- Slot-flow / ordered-coordinate transition geometry did not beat recency: best Top-20 about 622/1,555, mean rank about 25.40.
- Tree ensembles on lagged local features failed to justify complexity; best family member Top-20 616/1,555.
- Previous-PowerBall-Plus/XTRA cross-game residual features did not produce a stable independent gain.
- Modulo-8 residual alone was insufficient; it is retained only as a low-weight component and performed poorly in the mechanical post-hoc component check.
- Raw lag/spectral models did not outperform the corrected composite consistently.
- **Do not reuse the original `sin(pi*gap)` Fourier feature.** For integer gaps it is identically zero; floating-point standardization can manufacture numerical pseudo-signal.

## 15. Confidence

LOW
