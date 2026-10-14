# E0037 — Information Ceiling and Anytime-Valid Prequential Gate

**Opened:** 2026-10-14 (SAST), before any E0037 code was executed on canonical data.
**Author / role:** Claude Opus 5.5. Roles: adversarial statistician, independent reproducer, meta-research auditor.
**Status:** preregistration. `experimental`. Paper trading only.
**Evidence classification sought:** `INSUFFICIENT_EVIDENCE` (expected). `PROVISIONAL_SIGNAL` is possible only through the prospective e-process rule in §6.
**Requested authority:** none over slates, K13 membership, line ranking, pruning or PowerBall selection. E0037 produces no prediction slate.

---

## 0. Why this experiment exists

HEPS has run 36 experiments without one probability field that beats the exact uniform legal-line null on proper score. It has also not shown that any downstream stage could profit even if such a field existed. E0036 correctly made the proper-score gate primary, but:

1. it was frozen on 2026-10-02 and **has no implementation**. Four draws (2026-10-02, -06, -09, -13) have since been resolved under a fully determined frozen specification;
2. its sequential rule leaves a 500-target terminal checkpoint, about 4.6 years at ~108 draws/yr. Interim looks are descriptive only;
3. it does not connect the log-loss gate to the K13, 4+ and portfolio metrics the director actually cares about.

E0037 addresses all three:

- **Part A, Information Ceiling.** This is an exact theorem plus tables. It bounds every downstream gain (K13 hits, catastrophe rate, 4+/5 containment, portfolio jackpot probability) by the true per-draw KL divergence of the draw law from uniform. It turns "proper score first" from a policy into a mathematical constraint.
- **Part B, Anytime-valid prequential e-process.** The cumulative likelihood ratio of any *predictable* forecaster against the simple uniform null is a nonnegative martingale under H0. By Ville's inequality, `P(sup_t E_t >= 1/alpha) <= alpha`. This gives HEPS a sequential rule that is valid at every draw, with no alpha-spending and no terminal checkpoint. The log of the e-value equals minus the cumulative paired log-loss delta, so the proper-score gate and the sequential test are one object.
- **Part C, Independent implementation of E0036 Phase B** (M0, M1, M2a, M2b) exactly per the frozen 2026-10-02 specification, run as one forecaster class inside Part B. This is also a reproduction check against the E0032 Screen A number (`-0.05084` log-probability per target, i.e. `+0.05084` in E0036 sign convention).
- **Part D, Power by simulation.** This gives the time to detection of realistic physical alternatives (static ball bias) for the actual forecasters, not the plug-in MDE formula.
- **Part E, Two audits.**
  - (E1) The prospective record of every frozen official Main K13 against the exact hypergeometric null.
  - (E2) A test of whether E0033's oracle-replacement construction is exchangeability-calibrated under the null.

## 1. Questions and hypotheses

**H0 (per lane; Main and XTRA independently):** successive Main lines are iid uniform over the `C(50,5)=2,118,760` legal sorted lines. Successive PowerBalls are iid uniform on 1..16.

**Q-A (theory):** what is the largest achievable improvement in each downstream metric as a function of the true per-draw KL divergence `D`?

**Q-B (primary empirical):** does any preregistered coherent forecaster class accumulate likelihood-ratio evidence against H0?

**Q-C (reproduction):** does an independent implementation of E0036 M1/M2a/M2b reproduce E0032 Screen A? What are the E0036 deltas on the 28 frozen retrospective targets and on the four post-freeze, specification-determined targets?

**Q-D (power):** under static ball-bias alternatives with relative inclusion standard deviation `s`, how many draws until the composite e-process reaches 20 or 80 with 80% probability?

**Q-E1:** is the prospective official K13 record distinguishable from random 13-baskets?

**Q-E2:** under synthetic null winners, does the E0033 oracle-replacement construction rank the true line above the exchangeable expectation of 0.5? A random-decoy construction serves as the control.

## 2. Part A: information ceiling (exact)

Let `P` be the true law of the next line given the past, `U` uniform, and `D = KL(P||U)`.

- **Event ceiling.** For any event `A` defined by the outcome, such as a fixed basket having `H>=4` or a fixed 20-line slate containing the jackpot, data processing gives `kl(P(A) || U(A)) <= D`. Hence `P(A) <= kl^{-1}_+(U(A), D)` and `P(A) >= kl^{-1}_-(U(A), D)`.
- **Mean-hit ceiling.** For a fixed K-basket, `max E_P[H]` subject to `KL(P||U) <= D` is attained by the exponential tilt of `U` along `H`. `H` is hypergeometric under `U`, so the ceiling is computed exactly by a one-dimensional bisection.
- The conditional version applies per draw. The ceiling is concave in `D`, so the average lift over targets is bounded by the ceiling at the average conditional `D`.

**Frozen SESOI derived from the ceiling.** The smallest K13 effect of interest is a 10% relative lift, `+0.13` winners/draw. The minimum information required for that lift to be achievable is `D_SESOI = g13^{-1}(0.13) = 0.009388` nats/draw. This is the practical-significance threshold for log-loss in E0037. It is a property of the decision problem, not of the data.

## 3. Part B: forecasters (frozen)

Every forecaster maps the strictly earlier rows of its own lane to a normalized law over all legal lines, with full support. Every forecaster recovers `U` exactly when its parameters are zero. All normalizations are exact: elementary symmetric polynomials for product-weight laws, exact DP for chain laws, closed-form hypergeometric sums for the repeat law. Lanes are fitted independently; no fitted quantity crosses lanes.

| Class | ID | Law | Estimator (frozen) |
|---|---|---|---|
| Static ball bias | `BB_t005, BB_t010, BB_t020, BB_t040` | `P(x) ∝ exp(sum_{i in x} theta_i)`, multivariate Fisher noncentral | One-step ridge Newton from `theta=0` with prior `N(0,tau^2)`: `theta_i = (c_i - 0.1 n)/(0.0918367 n + 1/tau^2)`, where `c_i` is the count and `n` the number of prior draws, `tau in {0.05,0.10,0.20,0.40}` |
| Drifting ball bias | `BBEW_h8` | same law | Same one-step estimator using exponentially weighted counts, half-life 8 draws (`lambda=2^(-1/8)`), `tau=0.20` |
| Repeat persistence | `RP` | `P(x|p) ∝ exp(rho*|x ∩ p|)`, `p` = previous line | MAP for `rho` with prior `N(0,0.5^2)`, exact 1-D Newton |
| Transition (E0036) | `M1, M2a, M2b` | exactly per `experiments/E0036/hypothesis.md` §3 | exactly per E0036 §6: MAP, priors 0.25/0.50, Newton with backtracking from 0, tol 1e-10, minimum 6 training rows |

**Disclosure.** `RP` was added partly because the 2026-10-14 audit reported a Main consecutive-draw overlap of 0.368/draw against 0.5 expected (z=-1.26). That class is therefore outcome-motivated for Main, and its retrospective Main e-value is exploratory. BB and BBEW are the physically motivated ball-weight alternative. Their `tau` grid was fixed by physical scale (relative inclusion bias of about 5%, 9%, 18% and 37%), not by data.

**Composite e-process (primary statistic).** Each information class gets weight 1/4:

- BB: four tau values at 1/16 each;
- BBEW: 1/4;
- RP: 1/4;
- TRANS: M1, M2a and M2b at 1/12 each.

`E_t = sum_k w_k prod_{s<=t} P_k(x_s|past)/U(x_s)`.

**PowerBall e-process (per lane).** Dirichlet-multinomial prequential `P(k|past) = (c_k + a)/(n + 16a)`, `a in {1,4,16,64}`, equal weights.

**Named comparators (reported, not gated):** the E0030 incumbent adaptive mixture, re-implemented exactly from `experiments/E0030/prototype.py` (`forecast` and replay weight update), and its cumulative-frequency and recent-5 components.

## 4. Data and windows

- Ledgers: `data/draw_history.jsonl` and `data/powerball_xtra_history.jsonl`, 39 rows each, 2026-06-02..2026-10-13. SHA-256 values are recorded in `results.json`. No pre-2026-06-02 rows.
- Targets: rows 7..39 in each lane, 33 targets. Every forecaster scores the same targets.
- Reported sub-windows:
  - E0036 retrospective, rows 7..34, 28 targets, through 2026-09-25;
  - row 35 (2026-09-29), zero E0036 credit;
  - E0036 post-freeze, rows 36..39, 2026-10-02..2026-10-13. These are labelled `spec_frozen_implementation_late`. The model was fully determined before those outcomes, but this implementation was written after them.
- Mixed-mechanism disclosure: Main rows 30–31 are `electronic_rng`. Primary analysis includes them, and a sensitivity analysis excluding them as targets is reported. No regime inference is drawn.
- XTRA provenance: 18 rows pending official verification. Every XTRA headline carries this caveat.

## 5. Metrics

- **Primary, per forecaster:**
  - `d_t = -log P(x_t) - 14.566342` (negative is better);
  - mean `Delta`, its SE and t-statistic;
  - cumulative `S = sum d_t`;
  - `log E = -S`.
- **Primary, per lane:**
  - composite `E_final`;
  - `max_t E_t`;
  - anytime-valid p-value `min(1, 1/max_t E_t)`.
- **Secondary, exploratory, BH labelling only:**
  - Top-13 by exact anywhere-marginal per forecaster;
  - hits `H`, `P(H<=1)`, `H>=3` and `H>=4` against the exact hypergeometric null;
  - Brier on the 50 anywhere marginals.
- **PowerBall:** per-lane DM e-process and per-arm log-loss delta against `log 16`.

## 6. Decision rules

**Retrospective (targets through 2026-10-13).** Discovery only. Whatever the e-value, no promotion. A lane composite `max_t E_t >= 80` would label that lane `PROVISIONAL_SIGNAL` for prospective follow-up only. Otherwise the result is `INSUFFICIENT_EVIDENCE` with the ceiling-based interpretation.

**Prospective (first target 2026-10-16, the first draw after this file and the frozen code are committed).**

- The prospective composite e-process restarts at 1. It is evaluated after every draw, with no other looks needed or allowed to matter.
- A family of four lanes is monitored: Main lines, XTRA lines, Main PB and XTRA PB. A lane's H0 is rejected at familywise 0.05 if its prospective `E_t >= 80` at any time.
- A lane may claim *practical* predictive information only if, in addition, the leading forecaster's prospective mean improvement `-Delta` exceeds `D_SESOI = 0.009388` nats/draw.
- Futility review at 100 prospective targets per lane. If `log E < 0`, every class has prospective mean `Delta >= 0`, and the one-sided 95% upper bound on the best class's improvement is below `D_SESOI`, record that the field-level route to a 10% K13 lift is not supported at that horizon.
- Forecaster definitions, weights and the tau grid may not change. Any change starts a new e-process under a new experiment ID.

## 7. Falsification and admissibility

| ID | Condition | Consequence |
|---|---|---|
| F1 | any forecaster at zero parameters differs from `U` by more than `1e-12` (relative) on tested lines | REJECT implementation |
| F2 | DP log-partition differs from full 2,118,760-line enumeration by more than `1e-9` relative, or DP slot marginals or feature moments disagree | REJECT implementation |
| F3 | perturbing the target row changes any forecast for that target | REJECT temporal integrity |
| F4 | composite e-process under simulated H0 has a mean final value inconsistent with 1 (MC 99% interval), or empirical `P(sup E >= 20)` exceeds 0.05 by more than its MC 99% margin | REJECT the e-process implementation |
| F5 | M1 fails to reproduce E0032 Screen A to within 0.002 nats/target on the 28-row prefix (targets 7..28) | flag as reproduction discrepancy; investigate before reporting E0036 numbers |
| F6 (Q-E2) | under synthetic null winners, the E0033-construction mean PPMI percentile lies within ±0.02 of 0.5 and the Johnson-20+PPMI Top-10 4+ rate lies within MC error of the random-order rate | E0033 construction is calibrated; the hypothesis of an oracle-insertion artifact is rejected |

## 8. Part D: power simulation (frozen design)

- Alternatives: Fisher noncentral with true `theta ~ N(0, sigma^2)`, centred, chosen so that the relative inclusion standard deviation is `s in {0, 0.02, 0.05, 0.10, 0.20}`. `s=0` is the null and serves as the F4 check.
- 200 replicates per `s`, horizon 1,080 draws (about 10 years), deterministic seeds `20261014 + 1000*idx_s + rep`.
- Forecasters: the BB class and BBEW (the TRANS and RP classes are not simulated because their alternatives are not ball bias). The simulated composite is BB(4 tau)+BBEW, renormalised.
- Reports, at n in {39, 100, 250, 500, 1080}:
  - the probability that `sup E >= 20` and `>= 80`;
  - the median `log E`;
  - the exact true expected Top-13 hits of the `BB_t010` basket under the true law;
  - the exact oracle `D`.

## 9. Part E audits (frozen)

**E1.** Use the designated official (or sole frozen, where no designation exists) Main K13 for each frozen cycle: 2026-08-11, 08-28, 09-01, 09-04, 09-08 (shadow, no official designation), 09-11, 09-15, 09-18, 10-02 and 10-09. Score each against the ledger. Report:

- total hits against `13/50*5` per draw;
- the exact distribution of the total by convolution of hypergeometric pmfs;
- one-sided p-values in both directions;
- `H<=1`, `H>=3` and `H>=4` counts against expectation.

**E2.** For each E0033 target (2026-09-01, 09-04, 09-08):

- use the actual frozen K13 and the actual pre-target history;
- draw 400 synthetic null winners uniformly from all legal lines; for each, sample 8 oracle-replacement variants exactly as E0033 does (keep in-K13 winners, inject the rest, retain 8 of the K13 non-winners);
- compute the midrank percentile of the synthetic winner line under the PPMI line score of `scripts/xtra_algorithm_championship.py` and under the frequency line score;
- compute the Johnson `four_plus_first` 20-line set with PPMI reordering, and record whether the Top-10 contains a 4+ line;
- run the same with random-decoy universes (the E0029 construction) as the calibrated control;
- seed `20261014`.

## 10. Multiplicity exposure (declared)

- Main-line classes: 4, with 9 forecasters in total. They are combined into one composite e-process per lane, which is valid for any fixed weights. Per-forecaster deltas are descriptive.
- Lanes: 4 (Main lines, XTRA lines, Main PB, XTRA PB), Bonferroni 0.05/4, threshold 80.
- Secondary K13 metrics: 9 forecasters × 4 metrics × 2 lanes, BH q=0.10, labels only.
- No hyperparameter is tuned on outcomes. Any additional forecaster examined after this file is committed must be reported as post-registration exploration.

## 11. Self-critique (before results)

- The most likely outcome is a null. A null e-value at n=33 says almost nothing about small biases; Part D quantifies exactly how little.
- Part A assumes a correct reading of "information". The ceiling bounds what the *true* law permits. A learned model achieves less, and a misspecified one can do worse than the null.
- The retrospective e-value is valid as a test only if the forecasters were fixed independently of the outcomes. The `RP` class violates that for Main, as disclosed. The prospective e-process has no such caveat.
- The one-step ridge estimator is a definition, not exact MAP. Validity does not depend on optimality, only on predictability.
