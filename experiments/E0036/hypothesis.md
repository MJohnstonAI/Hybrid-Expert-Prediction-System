# E0036 — Power/Identifiability Gate and Unary-Residual Adequacy Test

**Date opened:** 2026-09-29
**Status:** RED-TEAM REVISED PREREGISTRATION — no implementation, no replay; fresh freeze/hash required before execution.
**Evidence classification sought:** `INSUFFICIENT_EVIDENCE` (expected) or `PROVISIONAL_SIGNAL` (only if all gates pass)
**Architecture status:** `experimental`
**Stage:** methodology | candidate_funnel
**Paper trading only:** true

---

> **RED-TEAM AMENDMENT — 2026-10-02**
>
> The 2026-09-29 preregistration draft was reviewed before implementation or replay and is **superseded by this corrected draft**. The original Git history remains the audit record. A new preregistration hash must be recorded before any E0036 run.
>
> Binding corrections:
> 1. Log-loss delta is defined only as `Delta_t = L_model,t - L_uniform,t = (-log P_M(x_t)) - 14.566342`; therefore **Delta < 0 means better than uniform**.
> 2. The structural question is renamed **unary-residual sufficiency / residual-interaction necessity**. The legal-order constraint already induces slot dependence; M1 does not assert ordinary conditional independence.
> 3. M2a/M2b can falsify *specific* low-dimensional interaction omissions only. Failure of both does not prove general residual independence; success of either establishes only incremental information in that preregistered basis.
> 4. Historical targets are **target-excluded retrospective discovery only** and can never promote a model. Promotion authority begins only with fresh targets occurring after the corrected protocol is frozen.
> 5. MDE is a detectability quantity, not a practical-importance threshold. Promotion uses statistical evidence plus a separately declared smallest effect size of interest (SESOI).
> 6. Checkpoints before the terminal confirmatory horizon are descriptive unless an explicit valid sequential alpha/e-value rule is added in a new amendment before prospective scoring. No repeated-look promotion is allowed under per-checkpoint Holm alone.
> 7. The historical `1-0.95^35` calculation is only an illustration under 35 independent 5% tests, not an estimate of HEPS's actual FWER.
> 8. E0032/BARP and similar point estimates without uncertainty are descriptive negative evidence, not statistically settled findings.


---

## 0. Purpose and standing

E0036 is a **gate experiment, not a feature-family experiment.**

It exists because the HEPS record currently cannot distinguish three states that are being conflated: a true null, an under-powered test, and a real but unmeasured effect. E0030 reports a paired exact-line log-loss delta of `+0.002634` nats/target (Main) with descriptive SE `0.002196` — a t-statistic of **1.20**, i.e. indistinguishable from the uniform null. E0035 reports the held-fixed field at `+0.001466` nats/target with **no standard error at all**. Across 35 registered experiments there is **no multiplicity control, no power analysis, and no stopping rule**.

E0036 therefore does two things in a fixed order:

1. **Phase A** — establish, before any model is fitted to outcomes, what effect size is detectable at the available and projected sample sizes, and declare a multiplicity and stopping budget.
2. **Phase B** — test whether the current coherent unary-residual family, or a strictly preregistered low-dimensional interaction extension, contains out-of-sample proper-score information beyond the exact uniform legal-line null.

**Phase A gates Phase B.** No interaction challenger may be fitted, and no K13 optimization may be performed, until the Phase A identifiability table exists and is recorded.

E0036 does not optimize K13. Compression is downstream of a probability-field gate that has not yet been passed (`governance/current_method_doctrine.md` §4, `AGENTS.md` §9).

---

## PHASE A — POWER AND IDENTIFIABILITY

### A.1 Reference noise scale

The only target-excluded, properly paired log-loss standard errors in the repository are from E0030 (`experiments/E0030/results.json`), which replayed **19 targets** on a 25-row ledger.

| Quantity | Value | Source |
|---|---|---|
| Uniform exact-line log loss | `log(2118760) = 14.566342` nats | `results.json:94` |
| `sigma` paired log-loss delta, Main mixture | `0.002196 × sqrt(19) = 0.0095737` | `results.json:124-125` |
| `sigma` paired log-loss delta, XTRA mixture | `0.001959 × sqrt(19) = 0.0085404` | `results.json:25031-25032` |
| `sigma` Main frequency component | `0.030916 × sqrt(19) = 0.1347579` | `results.json:106-107` |
| `sigma` XTRA recency component | `0.023029 × sqrt(19) = 0.1003795` | `results.json:25013-25014` |

These `sigma` values are **provisional inputs to Phase A, not frozen constants for Phase B.** Each model's own `sigma` must be re-estimated during the Phase A pilot (Section A.6), because interaction potentials inflate the left tail of the per-target log-loss difference and using the M1 scale would overstate M2's power.

### A.2 Exact uniform null reference values

For a legal sorted 5-of-50 line, and for a uniformly random 13-coordinate basket:

| Quantity | Exact value |
|---|---|
| Legal lines `C(50,5)` | `2,118,760` |
| Uniform line probability | `4.718971e-07` |
| `E[H]` random K13 | `13/50 × 5 = 1.30` |
| `sd(H)` random K13 per draw | `sqrt(5 × 0.26 × 0.74 × 45/49) = 0.939931` |
| `P(H=0)` | `0.205732` |
| `P(H=1)` | `0.405230` |
| `P(H <= 1)` | **`0.610962`** |
| `P(H >= 3)` | **`0.102993`** |
| `P(H >= 4)` | **`0.013094`** |
| `P(H = 5)` | `0.000607` |

### A.3 Minimum detectable effects — exact legal-line log loss (primary)

`MDE(n, power) = (z_{1-alpha/2} + z_{power}) · sigma / sqrt(n)`, two-sided `alpha = 0.05`, `z = 1.95996`.
50% = detection threshold (significance boundary); 80% and 90% = power targets.

**Main, sigma = 0.0095737** (nats/target)

| n targets | 50% | 80% | 90% | as % of 14.566342 |
|---|---|---|---|---|
| **28 (current)** | 0.003800 | **0.005067** | 0.005863 | 0.0348% |
| 34 | 0.003448 | 0.004599 | 0.005321 | 0.0316% |
| 100 | 0.002011 | 0.002681 | 0.003102 | 0.0184% |
| 250 | 0.001272 | 0.001696 | 0.001962 | 0.0116% |
| 500 | 0.000899 | 0.001199 | 0.001387 | 0.0082% |

**XTRA, sigma = 0.0085404** (nats/target)

| n targets | 50% | 80% | 90% | as % of 14.566342 |
|---|---|---|---|---|
| **28 (current)** | 0.003390 | **0.004521** | 0.005231 | 0.0310% |
| 34 | 0.003077 | 0.004103 | 0.004747 | 0.0282% |
| 100 | 0.001794 | 0.002392 | 0.002768 | 0.0164% |
| 250 | 0.001135 | 0.001513 | 0.001751 | 0.0104% |
| 500 | 0.000802 | 0.001070 | 0.001238 | 0.0073% |

### A.4 Minimum detectable effects — K13 and secondary metrics

Paired differences are computed conservatively as `Var(d) = 2·Var(H)` (zero correlation between the model basket and the random-basket control). This is the worst case for power and is stated as such; the realised paired variance is reported as a refinement and may only *improve* the MDE.

| Metric | n=28 (50% / 80% / 90%) | n=100 | n=250 | n=500 |
|---|---|---|---|---|
| K13 mean winner count | 0.528 / **0.704** / 0.814 | 0.279 / 0.372 / 0.431 | 0.177 / 0.236 / 0.273 | 0.125 / 0.167 / 0.193 |
| `P(H <= 1)` rate | 0.274 / **0.365** / 0.422 | 0.145 / 0.193 / 0.223 | 0.092 / 0.122 / 0.141 | 0.065 / 0.086 / 0.100 |
| `P(H >= 3)` rate | 0.171 / **0.228** / 0.263 | 0.090 / 0.120 / 0.139 | 0.057 / 0.076 / 0.088 | 0.040 / 0.054 / 0.062 |
| `P(H >= 4)` rate | 0.064 / **0.085** / 0.098 | 0.034 / 0.045 / 0.052 | 0.021 / 0.028 / 0.033 | 0.015 / 0.020 / 0.023 |
| `5/5` rate | 0.0138 / **0.0185** / 0.0214 | 0.0073 / 0.0098 / 0.0113 | 0.0046 / 0.0062 / 0.0071 | 0.0033 / 0.0044 / 0.0051 |

**5/5 is declared a very-low-power diagnostic with no threshold and no claim authority.** Expected number of 5/5 events under random K13:

| n targets | 28 | 34 | 100 | 250 | 500 | 1000 | 5000 | 8232 |
|---|---|---|---|---|---|---|---|---|
| expected 5/5 events | 0.017 | 0.021 | 0.061 | 0.152 | 0.304 | 0.607 | 3.04 | 5.00 |

At the observed ledger cadence of approximately **108 draws per year** (34 draws over 115 days), reaching even **one expected 5/5 event requires ~1,650 targets (~15 years)** and **five expected events requires ~8,232 targets (~76 years)**. 5/5 can never serve as a primary or secondary gate at any horizon this programme will reach. It is reported for completeness only.

### A.5 Multiplicity budget

**Historical exposure (declared, not repaired).**
`experiments/registry.csv` contains **35 numbered experiments** (E0001–E0035) plus four legacy/unnumbered entries. As an illustration only, **if** these were 35 independent 5% tests, the family-wise probability of at least one false positive would be `1 - 0.95^35 = 0.834`. HEPS's actual historical FWER is not identified by this calculation because experiments share data, contain multiple tests, and are dependent. **E0036 makes no claim on behalf of any historical effect size.** No retrospective HEPS result may be promoted on the basis of E0036's analysis. This is the single most important honesty clause in this document.

**E0036's own budget.**

| Class | Count | Control | Authority |
|---|---|---|---|
| Primary: `M1 vs M0`, `M2a vs M0`, `M2b vs M0` on exact-line log loss, per lane | 3 per lane, 6 total | **Holm-Bonferroni**, two-sided FWER `0.05` within lane; stricter cross-lane Bonferroni `0.05/6 = 0.008333` reported alongside | **Promotion-capable** |
| Interaction increment: `M2a vs M1`, `M2b vs M1` | 2 per lane | Holm step-down, tested **only if** the corresponding M2 variant rejected M0 at its own level; otherwise descriptive CI with no claim | Conditional |
| Secondary: Brier/calibration, K13 mean hits, `P(H<=1)`, `P(H>=3)`, `P(H>=4)` x 3 models | 15 per lane | Benjamini-Hochberg FDR `q = 0.10`, **labelling only** | **None — exploratory** |
| `5/5` containment | — | none | **None — diagnostic only** |
| M2 variant selection (if both reject) | — | predeclared tie-break: larger `|Delta|` wins; exact tie resolved by fixed priority `M2a > M2b` | — |

Additional exposure sources declared: Main and XTRA are **fitted independently with no parameter transfer** (`AGENTS.md` §1), so they are treated as two separate hypothesis families, not as replication of one. Two M2 interaction variants are the entire interaction search space; no additional basis may be added without a new preregistration.

### A.6 Sequential stopping and evidence-accumulation rule

- **Expanding window, target-excluded.** Minimum training length 6 draws. Targets are ledger rows 7 through 34, giving **28 retrospective targets**. The ledger size (34) and the usable target count (28) differ and both are reported in every table.
- **Descriptive checkpoints at n in {28, 100, 250}; terminal confirmatory checkpoint at n=500 unless a valid sequential alpha-spending/e-process rule is preregistered before prospective scoring.** Per-checkpoint Holm alone does not authorize repeated-look promotion.
- **No early stopping for benefit.** The only early stop is a falsification trigger (Section 5), which stops for *rejection*, never for success.
- **The model form and all hyperparameters in Section 6 are frozen at the hash of this file** before any replay. Only the fitted parameters update per target, via the preregistered estimator. Any change to model form, variant set, prior scales, metrics, thresholds or stopping rule voids the preregistration and requires a new experiment ID.
- At each checkpoint report: `Delta_M`, its SE, t-statistic or valid sequential evidence measure, multiplicity-adjusted result, MDE80 for detectability, and the separately frozen SESOI for practical significance.
- **Phase A pilot.** Before the Phase B gate is evaluated, re-estimate each model's own `sigma` on targets 7..28 and report a sensitivity grid over `sigma in {0.005, 0.01, 0.02, 0.05}`. The MDE reported for each model uses **that model's own** sigma. A conclusion that holds only at one sigma value is not a conclusion.
- **Accumulation horizon.** At the n=100 MDE80 of 0.002681 nats/target, accumulating a total log-loss advantage of 5 nats requires ~1,865 targets (~17 years at 108 draws/yr); at the n=250 MDE80 of 0.001696, ~2,948 targets (~27 years). HEPS should record this before committing to any long-horizon monitoring design.

### A.7 Which historical HEPS effect sizes were undetectable when tested

| Result | Observed | SE / power available | Detectable? |
|---|---|---|---|
| E0030 Main mixture, n=19 | `+0.002634` | MDE50 = 0.004614 | **No.** Below the significance boundary. Correctly "indistinguishable." |
| E0030 XTRA mixture, n=19 | `+0.003349` | MDE50 = 0.004116 | **No.** |
| E0030 Main frequency, n=19 | `+0.083460` | t = 2.70, power ~72% | Detected, **under-powered.** This is a *detected negative*, not a weak positive. |
| E0030 XTRA recency, n=19 | `+0.049289` | t = 2.14, power ~52% | Marginally detected, severely under-powered. |
| E0030 Main joint K13 | 23/95 vs null 24.7 | z = -0.42 | **No.** |
| E0030 XTRA joint K13 | 17/95 vs null 24.7 | z = -1.88 | Marginally, and in the **wrong direction**. |
| E0035 held-fixed field | `+0.001466` | **no SE reported** | **Uninterpretable.** Reporting defect. |
| E0032 Screen A | `-0.05084`/target | **no SE reported** | **Uninterpretable.** Reporting defect. |
| E0032 Screen B (BARP line field) | `-0.3819`/target | **no SE reported** | **Uninterpretable.** Reporting defect. |
| E0035 BB vs POINT, n=25 | 4 better / 17 equal / 4 worse | sign test on 8 discordant: p = 1.0 | **No.** A coin flip. |
| E0034 percentile comparison | 0.624 vs 0.611 vs 0.568 | **no CIs reported** | **Uninterpretable.** Reporting defect. |
| E0030 4+/5 across all arms | 0 events | random K13 expects 0.33 in 19 draws | **No** — and 0.33 events is itself unremarkable. |

**The canonical multiplicity illustration.** E0028 reports that the band `LDSAD in 11..13` occurred 11 times in 26 transitions (42.31%) against an exact structural-null probability of 10.94% (`experiments/E0028/decision.md:13`). If that band had been fixed *a priori*, the binomial z-statistic would be `(11 - 2.844)/1.591 = 5.13` — an overwhelming signal. It was **discovered on the same data**, so it is a discovery statistic with zero inferential content. This single case demonstrates why the ~83% historical family-wise false-positive probability is not a theoretical concern but a measured one. E0036 will not repeat it. Historical multiplicity is treated as an exposure warning, not repaired retrospectively.

**Three "no standard error reported" entries are themselves findings.** E0032 and E0035 report point estimates on a proper score without any dispersion measure, which makes them uninterpretable against any threshold. E0036 requires a paired SE for every proper-score claim.

---

## PHASE B — UNARY-RESIDUAL ADEQUACY TEST

### 1. Hypothesis

> **H1 (unary adequacy).** The coherent unary-residual family `M1` contains no out-of-sample proper-score information beyond the exact uniform legal-line null, at the available sample size.
>
> **H2 (interaction increment).** A strictly preregistered, low-dimensional interaction extension `M2` contains out-of-sample proper-score information beyond `M1` and beyond `M0`.
>
> **H3 (unary-residual sufficiency / residual-interaction necessity).** After exact legal-line geometry is imposed, does adding a preregistered low-dimensional interaction potential improve out-of-sample proper score beyond the unary residual model? M1 does not imply ordinary slot independence because legal ordering already couples the slots. Failure of M2a/M2b does not prove general interaction absence.

H1 is the incumbent's burden. H2 is the challenger's burden. H3 is a restricted model-adequacy question: whether either preregistered interaction basis adds information beyond M1. It is not a universal test of conditional independence.

### 2. Formal null and alternative

Let `X` be a legal sorted 5-subset of `{1..50}`, drawn from the true unknown law `P_true`.

- **Null `H0`:** `P_true = P0`, the uniform law over the `2,118,760` legal lines. `P0(x) = 1/C(50,5) = 4.718971e-07`.
- **Alternative `H_A`:** `P_true != P0`, with the specific low-dimensional alternatives parameterised in Section 3.

Note on construction admissibility. The doctrine's residual-ratio form and E0032 Screen A's exponential form are **the same family up to slot normalisation**: since `T_j(x) = exp(phi_j(delta_j))/Z_j` is already normalised to have `P0_j`-mean 1, we have `prod_j T_j(x_j) proportional to exp(sum_j phi_j(delta_j))`, and `P0_line` is constant on legal lines. Expressing M1 in exponential form is therefore *not* the `prod_j q_j(x_j)` modelling trap rejected in `governance/methodology_deprecations.md` — that trap re-multiplies order-statistic geometry and fails null recovery, and this construction provably satisfies null recovery (Section 3, M1). This equivalence is stated explicitly to forestle the objection.

### 3. Model definitions

Let `p = (p_1 < ... < p_5)` be the immediately preceding sorted Main (or XTRA) line and `delta_j = x_j - p_j`.

**M0 — exact uniform legal-line null.**
`P0(x) = 1/C(50,5)` for every legal `x`. Zero parameters.

**M1 — coherent unary-residual family (doctrine §3 / E0032 Screen A).**
```
w1(x) = exp( alpha * sum_{j=1..5} sign(delta_j)
           + beta  * sum_{j=1..5} sign(delta_j) * log(1 + |delta_j|) )
P1(x) = w1(x) / sum_{y legal} w1(y)
```
- Parameters: **2**, shared across slots. `alpha, beta ~ N(0, 0.25^2)`, independent, MAP by penalised maximum likelihood.
- This is a faithful re-implementation of `experiments/E0032/upstream_field_screen_2026-09-07.md:11-13`, making M1 a **replication target** for a screen that previously scored `-0.05084` nats/target against uniform.
- **Exact null recovery:** `alpha = beta = 0` gives `w1 == 1` identically, hence `P1 == P0` exactly. Verified numerically to `<= 1e-12`.
- **Exact normalisation:** `w1` is chain-structured over sorted slots, so the partition function is computed exactly by dynamic programming over states `(slot j, coordinate x_j)` — `O(5 × 50^2) = 12,500` operations. No enumeration of `2,118,760` lines is required in production.

**M2a — adjacent-slot displacement cross-potential.**
```
w2a(x) = exp( alpha * sum_{j=1..5} sign(delta_j)
            + beta  * sum_{j=1..5} sign(delta_j) * log(1 + |delta_j|)
            + ca    * sum_{j=1..4} tanh(delta_j) * tanh(delta_{j+1}) )
```
- Parameters: **3**. `ca ~ N(0, 0.50^2)`. Exact DP normalisation, same chain structure.
- `tanh` is bounded, so the potential cannot diverge on extreme displacements — a deliberate, preregistered boundedness choice.
- **Non-degeneracy:** `tanh(delta_j) tanh(delta_{j+1})` cannot be written as a sum of single-coordinate functions, so `ca = 0` recovers M1 **exactly** and `ca != 0` is a genuine second-order term. This is the direct test of adjacent-slot conditional independence.

**M2b — adjacent-gap run potential.**
Let `g_1 = x_1 - 1`, `g_i = x_i - x_{i-1} - 1` for `i = 2..5`, `g_6 = 50 - x_5`; these form a weak composition of 45 into 6 parts. Define `u(g) = 1 if g >= 1 else 0`.
```
w2b(x) = exp( alpha * sum_{j=1..5} sign(delta_j)
            + beta  * sum_{j=1..5} sign(delta_j) * log(1 + |delta_j|)
            + cb    * sum_{i=1..5} u(g_i) * u(g_{i+1}) )
```
- Parameters: **3**. `cb ~ N(0, 0.50^2)`. Exact DP normalisation; chain-structured over the gap composition (`O(6 × 46^2)`).
- **Non-degeneracy:** `u(g_i) u(g_{i+1})` is not additively separable, so `cb = 0` recovers M1 exactly. This probes whether the *clustering* structure of the winning line (runs of adjacent numbers) carries information beyond the displacement model.

**Parameter budget: 0 + 2 + 3 + 3 = 8 parameters across three tested models.** No free `50 × 50` pair tables, no per-coordinate free parameters, no high-order interaction basis.

**Named baselines reported alongside, outside the M0/M1/M2 gate:** the E0030 adaptive mixture exactly as implemented in `experiments/E0030/prototype.py`; strongly shrunk cumulative-frequency; strongly shrunk recent-five; uniform Top13 with exact hypergeometric controls.

**Information-family compliance.** `sign(delta_j)`, `|delta_j|`, `x_j` and `x_j mod 10` enter only as basis functions inside one jointly fitted transition model. They receive **no independent convergence votes** and are never multiplied as separate likelihood ratios (`governance/current_method_doctrine.md` §2). Terminal digit is not used at all.

### 4. Estimands

Sign convention throughout: `d_t^M = (-log P_M(x_t)) - (-log P0(x_t)) = (-log P_M(x_t)) - 14.566342`. **`Delta < 0` means the model is better than uniform; `Delta > 0` means worse.** This matches E0030's convention.

- **Primary:** `Delta_M1`, `Delta_M2a`, `Delta_M2b` — expected paired exact-line log-loss difference versus `M0`, estimated by the expanding-window walk-forward mean of `d_t^M`.
- **Key secondary:** `Delta_int = Delta_M2 - Delta_M1` — incremental value of the interaction over the unary family. This is the direct test of H3.
- **Diagnostic:** `S_M = sum_t d_t^M`, the cumulative paired log-loss delta.
- **Exploratory only:** `Delta_Brier`, `Delta_K13hits`, `Delta_P(H<=1)`, `Delta_P(H>=3)`, `Delta_P(H>=4)`. `5/5` reported with no estimand and no threshold.

### 5. Decision thresholds

A model `M` is promoted to *shadow with prospective authority* **only if every one of the following holds**, evaluated at a binding checkpoint:

| Gate | Condition |
|---|---|
| **G1** | `Delta_M < 0` (beats uniform) |
| **G2** | Holm-adjusted `p < 0.05` within lane, two-sided |
| **G3** | prospective statistical evidence passes the declared confirmatory test, and the estimated improvement magnitude meets the separately frozen SESOI; MDE is reported for detectability only |
| **G4** | Full support retained: `min over legal x of P_M(x) > 0`, verified numerically |
| **G5** | Exact null recovery: all parameters forced to 0 gives `max |P_M(x) - 1/C(50,5)| <= 1e-12` over legal `x` |
| **G6** | DP/enumeration agreement: on `>= 10,000` deterministically sampled legal lines plus the previous draw, DP-derived probabilities match brute-force enumeration to `<= 1e-9` relative |
| **G7** | Independent reimplementation of the estimator by a second reviewer |

**MDE interpretation.** MDE describes what effect sizes the design can detect at a specified power; it is not an economic-value threshold. Practical significance is governed by a separately frozen SESOI. Until a SESOI is frozen, E0036 may diagnose detectability and model adequacy but may not promote on practical significance.

G2-G3 failure of an admissibility gate (G4-G7) is an immediate `REJECT` of the family regardless of G1-G3. M2 additionally requires `Delta_M2 < Delta_M1`, with the M1-vs-M2 contrast reported.

A Main-consistent result that fails in XTRA is reported as lane-specific with explicit disclosure; Main and XTRA are not mutual replication sets because they are independently fitted systems. Promotion, if ever permitted, is lane-specific and prospective only. Main and XTRA are independent systems (`AGENTS.md` §1) and neither transfers authority to the other.

### 6. Hyperparameters frozen before replay

| Item | Fixed value |
|---|---|
| `alpha, beta` prior | independent `N(0, 0.25^2)`, per lane, fitted independently |
| `ca, cb` prior | independent `N(0, 0.50^2)`, per lane, fitted independently |
| Estimator | MAP penalised maximum likelihood; penalty `= sum log N(0, sd^2)` |
| Optimiser | deterministic Newton with backtracking line search, `tol = 1e-10`, max 200 iterations |
| Initialisation | fixed at `(0, 0)` / `(0, 0, 0)` — no random restarts |
| Partition function | exact DP, `tol = 1e-12`, integer-indexed |
| Minimum training rows | 6 |
| Window | expanding only; no window-length search |
| Model/variant set | exactly `M0, M1, M2a, M2b`; no additions |
| Metrics | exactly as listed in Section 4; no additions |
| Thresholds | exactly Section 5; no post-hoc adjustment |
| Preregistration hash | SHA-256 of this file recorded in the run manifest |

No target-conditioned selection of any hyperparameter is permitted. A variant added after replay begins voids the preregistration.

### 7. Exact data boundaries

| Lane | File | SHA-256 | Rows | Range |
|---|---|---|---|---|
| Main | `data/draw_history.jsonl` | `2DA888679F9D397CE57246C324108952DD952F4B756905F4803AB928DAD528D6` | 34 | `draw_id` 1..34, 2026-06-02..2026-09-25 |
| XTRA | `data/powerball_xtra_history.jsonl` | `07DF3FBEFB46182E553712DBEB045B1BE0EFA0D9DB66E4A5AC3860E1CABD35F2` | 34 | `draw_id` 1725..1758, 2026-06-02..2026-09-25 |

**Strictly excluded:** `Train on Main.xlsx`, `Train on Plus.xlsx`, every row dated before 2026-06-02, and every row dated after 2026-09-25 in the retrospective window.

**Target-exclusion.** Target `t` uses only rows with `draw_date < draw_date(t)`. Targets are rows 7..34, giving **28 retrospective targets**.

**2026-09-29 is target 29 and is SHADOW ONLY.** Its result must not be used to select variants, adjust thresholds, or rescore the retrospective window.

**XTRA provenance caveat (mandatory on every XTRA headline).** 13 of 34 XTRA rows carry `pending_official_source_verification`; the official Sizekhaya/National Lottery source returned HTTP 403 and verification proceeded against a designated non-official archive (`data/powerball_xtra_manifest.json:29-43, 52`). XTRA is fitted independently with **no parameter transfer** from Main. An XTRA-only result cannot support promotion on its own.

**Mixed-mechanism disclosure.** Main rows 30 and 31 (2026-09-11, 2026-09-15) carry `draw_method: "electronic_rng"`, `machine_name: "rng"`. The active series is the **"active post-2026-06-02 HEPS era"**, not the "mechanical era" (`governance/current_method_doctrine.md` §12). Primary analysis **includes** these rows. A preregistered, non-selective sensitivity analysis excluding rows 30-31 is reported alongside. Both are reported; the inclusive result governs. This is a provenance fact, not a regime signal, and no mechanism inference is drawn from it.

### 8. Walk-forward protocol

Strict order per `AGENTS.md` §6, repeated for each target and each lane:

1. select rows with `draw_date < target draw_date` (expanding, target-excluded);
2. fit `M1`, `M2a`, `M2b` by the preregistered MAP estimator; `M0` is parameter-free;
3. compute exact partition functions by DP; freeze all probabilities; record a freeze hash;
4. reveal the target;
5. score `d_t^M`, Brier, and (K13 metrics only after the probability-field gate) K13 diagnostics;
6. append the target to state for `t+1` only.

No target's outcome may influence its own features, parameters, thresholds or variant selection.

### 9. Validation requirements before any result is reported

- `python scripts/validate_draws.py data/draw_history.jsonl`
- `python scripts/sync_manifest.py --check`
- `python scripts/check_stationarity.py`
- `python -m unittest discover -s tests -v`
- E0036-specific unit tests: null recovery to `1e-12`; DP vs enumeration to `1e-9`; partition function vs direct enumeration on a small toy alphabet; parameter estimator against a closed-form two-parameter optimum; temporal-exclusion assertion that fails loudly if any target row is read during its own fit.

### 10. Falsification conditions

| ID | Condition | Consequence |
|---|---|---|
| F1 | Null recovery fails (G5) | `REJECT` the family |
| F2 | DP disagrees with enumeration (G6) | `REJECT` the implementation |
| F3 | Any parameter/feature for target `t` depends on the outcome at `t` | `REJECT` for temporal-integrity violation |
| F4 | Improvement obtained only by pushing `P_M(x)` below `1e-300` for some legal `x` | `REJECT` — full support lost |
| F5 | M2's gain versus M0 vanishes under the multiplicity budget | `INSUFFICIENT_EVIDENCE` |
| F6 | M2 beats M0 but `Delta_M2 >= Delta_M1` | `INSUFFICIENT_EVIDENCE`, recorded as **conditional-exchangeability confirmation**: the interaction term adds nothing and the unary factorisation is not the binding constraint |
| F7 | Checkpoint result flips sign between adjacent checkpoints | Report as unstable; **no promotion** |
| F8 | Estimate at n=28 depends materially on excluding rows 30-31 | Report both; **no promotion** until mechanism provenance is resolved |
| F9 | G1-G3 pass but G4-G7 fail | `REJECT` regardless of the proper score |

### 11. Expected failure modes

- **FM1 — null result (most likely).** Predicted: no model clears G3 at n=28, because `MDE80` (Main) is 0.005067 nats/target while a correctly-specified null model yields `E|Delta| ~ 0.0026`. **This is the expected outcome and is a legitimate contribution**: it would establish that the acquisition architecture is unfalsifiable at the current sample size and should trigger the A.6 accumulation-horizon decision.
- **FM2 — sigma inflation.** M2a/M2b interaction potentials create heavy left tails in `d_t`; one unlucky line can cost many nats. Using M1's sigma for M2 would **overstate** M2's power. Mitigated by the pilot re-estimation and the sensitivity grid.
- **FM3 — variant selection.** Two M2 variants create a selection opportunity. Mitigated by Holm across three primary comparisons and the predeclared tie-break.
- **FM4 — DP implementation error.** Mitigated by mandatory enumeration cross-check (G6).
- **FM5 — conditioning leakage.** M1/M2 are conditional on the previous sorted line `p`. The implementation must not read any target coordinate. Covered by F3 and by a dedicated unit test.
- **FM6 — post-hoc contamination.** All 28 retrospective targets are already known. Mitigated by freezing every choice in this file, with the file hash recorded.
- **FM7 — historical false discovery.** ~83% family-wise false-positive probability across the existing record. E0036 re-claims nothing historical; any promotion additionally requires prospective accumulation beyond n=28.
- **FM8 — XTRA provenance.** 13/34 rows pending official verification. Every XTRA conclusion carries the caveat and cannot support promotion alone.
- **FM9 — mechanism heterogeneity.** The two `electronic_rng` rows are unmodelled. If the active series genuinely mixes mechanisms, no single law is correct and all models are misspecified. This is not detectable from the ledger and requires external equipment evidence; E0036 discloses it (F8) rather than resolving it.

### 12. Requested authority

- **Evidence classification sought:** `INSUFFICIENT_EVIDENCE` (expected) or `PROVISIONAL_SIGNAL` (only on full G1-G7 passage).
- **Architecture status:** `experimental`.
- **Zero** production authority, **zero** candidate-discovery authority, **zero** hard-pruning authority, **zero** K change.
- One frozen **SHADOW** forecast for target 2026-09-29, with no effect on any production slate.
- No modification of E0035 frozen artifacts, E0033 assembly semantics, or the incumbent K13.
- **If the gate fails**, E0036 requests authority to record a **demonstrated null** and to recommend that the programme cease generating candidate-feature families, choosing between (a) a long-horizon fixed-protocol monitoring design sized from the A.6 horizon table, and (b) recording the null and stopping. This recommendation is itself treated as a deliverable under `AGENTS.md` §18.

---

## 13. Self-critique (registered before any result exists)

The strongest argument against this experiment: **it is very likely to be a well-designed instrument for measuring nothing**, and a null at n=28 may be misread as evidence that no edge exists rather than as evidence that n=28 cannot resolve one. The MDE table makes that risk explicit and bounded, but the risk of misinterpretation is real and is the main reason G3 exists — a promotion requires an effect larger than the sample can trivially produce, not merely a favourable p-value.

A second objection: the three M-terms are all built from the same signed-displacement information family, so M2a and M2b are not independent tests of H3. They are two low-dimensional probes of one structural assumption. This is intentional and is why the interaction budget is Holm-controlled across them rather than treated as replication.

A third objection: conditioning on the previous line `p` makes M1/M2 a transition model, while the E0030 field that E0035 holds fixed is an exchangeable coordinate-marginal model. They are **not the same family**, and M1 is not a faithful reimplementation of the field currently in production. M1 is a faithful reimplementation of E0032 Screen A, which is the point: M1 is the doctrine-preferred family, tested on its own terms. E0030 is carried as a named baseline and is reported but is not the gate.

---

## 14. Status

- Phase 0 repository verification: **PASS** (34 rows both lanes, 2026-09-25, `[5,9,22,34,38]|PB3`, XTRA `1758`).
- E0035 2026-09-15 post-draw scoring: **complete** (prospective tie, 1/5 both arms, both `H<=1`, no promotion).
- Terminology revision to "active post-2026-06-02 HEPS era": **complete** in `governance/current_method_doctrine.md` §12, `core/heps_architecture.md`, `knowledge/open_questions.md` Q010.
- `experiments/registry.csv` E0036 row: **deliberately not yet added** — added on approval, to avoid registering an unapproved preregistration.
- DELIVERABLE 2 (this preregistration): **complete, awaiting red-team review.**
- DELIVERABLE 3 (implementation), 4 (replay), 5 (shadow), 6 (self-critique post-result): **not started, gated.**
