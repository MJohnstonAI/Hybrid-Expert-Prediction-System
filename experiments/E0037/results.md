# E0037 Results: Information Ceiling and Anytime-Valid Prequential Gate

**Evidence mode:** retrospective discovery, methodology and audit. **No slate, no authority change.**
**Code:** `scripts/e0037_prequential_gate.py` (standard library only). **Tests:** `tests/test_e0037_prequential_gate.py`.
**Rerun:** `python scripts/e0037_prequential_gate.py --part all --workers 6` (about 20 min on 6 cores). All seeds are fixed, so outputs are deterministic.
**Raw outputs:** `experiments/E0037/results_*.json`. Each file records the LF-normalized SHA-256 of the script that produced it.
**Data:** Main `data/draw_history.jsonl` and XTRA `data/powerball_xtra_history.jsonl`, 39 rows each, 2026-06-02 to 2026-10-13. Main LF-normalized SHA-256 starts `ea137a857dc57458`; XTRA starts `a7ce10e802422289`. Full hashes are in `results_replay.json`. XTRA has 18 rows pending official-source verification.

Sign convention throughout: `Delta = -log P_model(x) - 14.566342` nats. **Negative is better than uniform.**

---

## 0. Admissibility (all pass)

| Check | Result |
|---|---|
| F1 / G5: null recovery, max relative error at zero parameters (product, repeat, M1, M2a, M2b) | 5.6e-16 for all |
| F2 / G6: DP vs full enumeration of all 2,118,760 lines (M1, M2a, M2b at non-zero θ) | rel. error of Z ≤ 2.6e-13; moments ≤ 1.6e-11; slot marginals ≤ 4.2e-14; 10,001 sampled lines plus the previous draw ≤ 2.6e-13 |
| Cross-implementation: M1 partition vs E0032 `SlotProductField` (written by another agent) | agrees to 1e-10 |
| Cross-implementation: product law vs E0030 `SubsetModel` | agrees to 1e-15 |
| F3: target-row perturbation changes the frozen forecast hash | no (unit test) |
| F4: Ville's bound under H0, P(sup E ≥ 20) | 0.0018 (n=39, 4,000 reps); 0.006 (n=250); 0.010 (n=1080). All ≤ 0.05 |
| F4: martingale mean under H0 | composite n=39: mean E = 0.988 ± 0.022 (4,000 reps); light-tailed component BB_t005 at n=250: 0.9956 ± 0.0051. See note |
| F5: reproduction of E0032 Screen A (M1, 28-row prefix, targets 7..28) | mean log-prob delta −0.0508427 against reported −0.05084 (abs. diff. 2.7e-6). Full fit (α, β) = (0.03189, −0.001559) against reported (0.0319, −0.00156) |
| Newton convergence (every fit, every target) | converged; step < 1e-10 |

**F4 note.** At n=250 the sample mean of the composite E over 2,000 null replicates is 0.76, which naively looks inconsistent with 1. The per-component check shows why:

- light-tailed learners (BB_t005, var log E = 0.07) average 0.996 ± 0.005;
- aggressive learners (BB_t020, BB_t040, var log E = 5.4 and 14.5) carry their unit mean in events too rare to appear in 3,000 replicates.

The exact one-step identity `sum_x P_k(x) = 1` holds to 4e-16, so the martingale property holds exactly. The preregistered "mean ≈ 1" criterion is only informative for light-tailed components. That limitation is recorded here rather than hidden.

## 1. Part A: information ceiling (exact)

For any downstream decision, `KL(P_true||U) = D` bounds the attainable gain.

| D (nats/draw) | max K13 E[H] (lift) | min P(H≤1) | max P(H≥3) | max P(H≥4) | oracle draws to E=20 | equivalent ball-bias rel. sd |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.300 (0) | 0.611 | 0.103 | 0.013 | ∞ | 0 |
| 0.001 | 1.342 (+0.042) | 0.589 | 0.117 | 0.018 | 2,996 | 1.9% |
| 0.0026 | 1.368 (+0.068) | 0.576 | 0.126 | 0.022 | 1,152 | 3.1% |
| 0.005 | 1.395 (+0.095) | 0.562 | 0.135 | 0.026 | 599 | 4.3% |
| **0.009388 (SESOI)** | **1.430 (+0.130)** | 0.544 | 0.147 | 0.031 | 319 | 5.9% |
| 0.02 | 1.491 (+0.191) | 0.512 | 0.169 | 0.042 | 150 | 8.6% |
| 0.05 | 1.603 (+0.303) | 0.454 | 0.211 | 0.063 | 60 | 13.6% |
| 0.258 | 2.004 (+0.704) | 0.257 | 0.375 | 0.157 | 12 | 30.8% |

- A **10% K13 lift requires D ≥ 0.0094 nats/draw**.
- **E0036's n=28 detectable K13 lift (0.704) requires D ≥ 0.258**, which corresponds to roughly 31% relative ball bias. That is a grossly unfair machine.
- Ball-bias constant: `D ≈ 2.722 s²`, where `s` is the relative standard deviation of inclusion probabilities.
- **Realistic (diffuse) bias.** At s = 5.9% (D ≈ SESOI), an *oracle* knowing the bias exactly has K13 lift +0.096. Its best 20 lines have 1.7× the uniform jackpot probability (34 per 2.1M instead of 20 per 2.1M).
- Rare-event ceilings (5/5, 20-line jackpot) are loose because they allow all the divergence to sit on one line. They are reported in `results_ceiling.json` but are not decision-relevant.

## 2. Part B: prequential e-process (retrospective, discovery)

Targets are rows 7..39 (33 per lane), and every forecaster scores the same targets.

### Composite e-process (frozen weights)

| Lane | Window | n | log E final | max E | anytime p |
|---|---|---:|---:|---:|---:|
| Main | all | 33 | −0.473 | 1.22 | 0.82 |
| Main | E0036 retrospective (rows 7..34) | 28 | −0.398 | 1.22 | 0.82 |
| Main | post-freeze (rows 36..39) | 4 | −0.112 | 1.00 | 1.00 |
| Main | excluding `electronic_rng` targets | 31 | −0.457 | 1.22 | 0.82 |
| XTRA | all | 33 | −0.160 | 1.00 | 1.00 |
| XTRA | E0036 retrospective | 28 | −0.459 | 1.00 | 1.00 |
| XTRA | post-freeze | 4 | +0.298 | 1.35 | 0.74 |

**No lane accumulates evidence against the uniform null.** The retrospective threshold for even a `PROVISIONAL_SIGNAL` label is E ≥ 80. The largest E observed is 1.35.

### Per-forecaster paired log-loss delta (all 33 targets)

| Forecaster | Main mean Δ (SE) | XTRA mean Δ (SE) |
|---|---:|---:|
| BB_t005 | +0.0007 (0.0012) | +0.0013 (0.0012) |
| BB_t010 | +0.0031 (0.0048) | +0.0054 (0.0048) |
| BB_t020 | +0.0158 (0.0177) | +0.0239 (0.0179) |
| BB_t040 | +0.0926 (0.0554) | +0.1123 (0.0571) |
| BBEW_h8 | +0.0070 (0.0103) | +0.0097 (0.0086) |
| RP | +0.0021 (0.0303) | +0.0121 (0.0116) |
| M1 (E0036) | +0.0392 (0.0298) | −0.0371 (0.0678) |
| M2a (E0036) | +0.1021 (0.0915) | +0.0289 (0.0794) |
| M2b (E0036) | +0.0719 (0.0386) | +0.0188 (0.0725) |
| E0030 incumbent | +0.0011 (0.0019) | +0.0021 (0.0013) |
| E0030 cumulative | +0.0467 (0.0385) | +0.0632 (0.0393) |
| E0030 recent5 | −0.0015 (0.0209) | +0.0216 (0.0222) |

- **17 of 18 preregistered forecaster-lane cells are worse than uniform.** The exception is XTRA M1 (t = −0.55), the degenerate band discussed in §5. Among the comparators, only Main recent5 is below zero (t = −0.07).
- Aggressive learning is monotonically worse: BB_t005 < BB_t010 < BB_t020 < BB_t040 in loss.
- Under simulated H0, BB_t040 reaches a median log E of −19 by n=250. That is the cost of learning frequencies that are not there.
- `RP` was fitted with a consistently negative ρ (−0.2 to −0.3) on Main, reflecting the observed 0.368 overlap per draw against 0.5 expected. It still earns **no** out-of-sample gain (Δ = +0.002). This is the clearest example in the record of a real-looking in-sample pattern with zero predictive value.

### PowerBall (Dirichlet-multinomial e-process, a ∈ {1, 4, 16, 64})

| Lane | log E final | max E | anytime p | best arm mean Δ |
|---|---:|---:|---:|---:|
| Main PB | +0.799 | 3.11 | 0.32 | DM_a4 −0.038 |
| XTRA PB | +1.682 | 5.38 | 0.19 | DM_a4 −0.070 |

The XTRA PB2 frequency (8 of 39) drives the XTRA value. A fixed, pre-specifiable test that does not know which ball is "hot" gives E = 5.4, i.e. an anytime p of 0.19, against the post-hoc familywise 0.040 reported on 2026-10-14. That gap is what post-hoc statistic selection costs. It does not meet the threshold of 80 (familywise over four lanes), nor even 20.

### Secondary K13 metrics (exploratory)

No discoveries survive Benjamini–Hochberg at q=0.10 across the 72 tests (9 forecasters × 4 metrics × 2 lanes). The smallest raw p-value (0.010) is XTRA RP total hits, and it is in the *wrong* direction: 29 hits against 42.9 expected.

## 3. Part C: E0036 Phase B, independent implementation of the frozen 2026-10-02 specification

### Retrospective window (rows 7..34, 28 targets): discovery only

| Lane | M1 Δ (SE, t) | M2a Δ (SE) | M2b Δ (SE) | Holm rejections |
|---|---|---|---|---|
| Main | +0.0450 (0.0350, 1.29) | +0.1063 (0.1069) | +0.0734 (0.0452) | none; G1 fails for all three |
| XTRA | −0.0021 (0.0732, −0.03) | +0.0776 (0.0872) | +0.0480 (0.0810) | none |

- **F6 (conditional exchangeability).** In both lanes M2a and M2b are *worse* than M1. Neither preregistered interaction basis adds information beyond the unary residual model.
- **F8 (rng sensitivity).** Excluding Main draw_ids 30–31 as targets moves M1 Main from +0.0392 to +0.0418 (33-target window). The conclusion is unchanged.

### Post-freeze specification-determined targets (2026-10-02 to 2026-10-13, n=4)

These targets are labelled `spec_frozen_implementation_late`: the model was fully determined at the freeze, but this implementation was written after the outcomes.

| Lane | M1 Δ | M2a Δ | M2b Δ |
|---|---|---|---|
| Main | +0.0119 (0.0216) | +0.0254 (0.1066) | +0.0524 (0.0422) |
| XTRA | −0.2356 (0.2197) | −0.2424 (0.1982) | −0.1875 (0.1821) |

None are significant. Main moves against the models and XTRA moves for them. See §5 for why the XTRA movement is a degenerate-basket effect.

### E0036 Phase A pilot σ (targets 7..28): its own pilot rule, executed

| Model | Main σ | XTRA σ | MDE80 at n=28 (Main) | MDE80 at n=500 (Main) |
|---|---:|---:|---:|---:|
| M1 | 0.209 | 0.388 | 0.110 | 0.026 |
| M2a | 0.608 | 0.479 | 0.322 | 0.076 |
| M2b | 0.265 | 0.450 | 0.140 | 0.033 |
| E0030 incumbent (E0036's provisional σ source) | 0.0093 | 0.0082 | 0.0049 | 0.0012 |

E0036's provisional σ (0.0096) describes the near-uniform E0030 mixture, not the E0036 models. The pilot shows the models' σ is **22–65× larger**. Even at E0036's terminal checkpoint (n=500), the M1 MDE80 (0.026) is 2.8× the information-ceiling SESOI (0.0094). **As designed, E0036 cannot resolve a practically significant M1 effect at any planned checkpoint.**

## 4. Part D: power by simulation (static ball bias; 200 replicates; composite of BB(4 τ) and BBEW)

| rel. bias s | D (nats/draw) | P(E≥20) by n=39 | n=100 | n=250 | n=500 | n=1080 | learned K13 E[H] at n=39 / 1080 | oracle K13 E[H] |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 0 (H0) | 0 | 0.000 | 0.005 | 0.005 | 0.005 | 0.010 | 1.300 / 1.300 | 1.300 |
| 2% | 0.0011 | 0.000 | 0.000 | 0.000 | 0.005 | 0.015 | 1.302 / 1.307 | 1.333 |
| 5% | 0.0068 | 0.000 | 0.000 | 0.005 | 0.020 | 0.115 | 1.308 / 1.340 | 1.382 |
| 10% | 0.0272 | 0.010 | 0.030 | 0.085 | 0.245 | 0.885 | 1.337 / 1.422 | 1.466 |
| 20% | 0.1077 | 0.020 | 0.175 | 0.860 | 1.000 | 1.000 | 1.432 / 1.609 | 1.638 |

At about 108 draws per year:

- a **10%** relative ball bias, which is large for a certified machine, is detected with roughly 88% probability only after **about 10 years**;
- a **5%** bias is detected with 11.5% probability in 10 years;
- at the current n=39, even a **20%** bias is detected 2% of the time, and the learned K13 gains just +0.13 winners per draw.

## 5. Transition-family identifiability

**Oracle divergence of the full-data M1 MAP fit.**

- Main: θ = (0.0577, −0.0318), D = 0.0019. Even if this fit were the truth, an oracle needs about 1,542 draws (roughly 14 years) to reach E=20.
- XTRA: θ = (0.0717, 0.0391), D = 0.084. That is a large in-sample divergence, but in-sample fits overstate divergence, and the out-of-sample record (33 targets, cumulative +1.2 nats for M1) does not confirm it.

**Degenerate baskets.** On XTRA the fitted α > 0 makes the M1 anywhere-marginal ranking monotone in the coordinate. **The M1 K13 is the fixed band [38..50] on all 33 XTRA targets.** That band scored 3/5, 0/5, 4/5 and 4/5 over the October targets (51 hits against 42.9 over 33 targets, z ≈ 1.5).

Main M1 K13s are likewise contiguous tail bands, for example [2..14], [3..14, 39] and [38..50]. So `alpha * sum sign(delta_j)` acts largely as a **static coordinate-height tilt**, not as a transition-specific signal. This is the F017 band-collapse pathology reappearing inside the doctrine-preferred model form.

## 6. Part E1: official frozen Main K13 record (10 frozen cycles, 2026-08-11 to 2026-10-09)

| Total hits | Expected (random 13-basket) | P(total ≥ obs) | H≤1 (exp.) | H≥3 (exp.) | H≥4 (exp.) |
|---:|---:|---:|---:|---:|---:|
| 14 | 13.0 | 0.42 | 6 (6.11) | 0 (1.03) | 0 (0.13) |

Every basket was verified to exist in its source file; see `results_audit.json`. The prospective acquisition record is **exactly what random 13-baskets produce**.

## 7. Part E2: E0033 oracle-replacement calibration

Each null cell uses 400 synthetic uniform winners × 8 variants. "Actual" uses the real winner with exhaustive variants, as in E0033.

| Target | Construction | PPMI winner pct | Freq winner pct | Top-20 4+ | Top-10 4+ (PPMI order) | Top-10 4+ (random order) |
|---|---|---:|---:|---:|---:|---:|
| 09-01 | actual (E0033) | 0.111 | 0.962 | 0.921 | **0.588** | 0.461 |
| 09-01 | null, E0033 construction | 0.431 | 0.587 | 0.721 | 0.314 | 0.366 |
| 09-01 | null, random decoys (control) | 0.490 | 0.494 | 0.607 | 0.316 | 0.310 |
| 09-04 | actual (E0033) | 0.510 | 0.308 | 0.889 | **0.446** | 0.444 |
| 09-04 | null, E0033 construction | 0.506 | 0.463 | 0.633 | 0.326 | 0.324 |
| 09-04 | null, random decoys | 0.521 | 0.482 | 0.616 | 0.320 | 0.315 |
| 09-08 | actual (E0033) | 0.869 | 0.049 | 0.764 | **0.558** | 0.382 |
| 09-08 | null, E0033 construction | **0.767** | **0.092** | 0.570 | **0.413** | 0.290 |
| 09-08 | null, random decoys | 0.507 | 0.487 | 0.626 | 0.328 | 0.320 |

**Reproduction.** The "actual" rows reproduce E0033's published Top-10/Top-20 figures to four decimals.

**F6 not triggered, so the artifact hypothesis is confirmed.** The E0033 construction keeps 8 *model-selected* decoys and injects random winners. Winners and decoys are therefore not exchangeable. On 09-08 a purely random winner line gets a PPMI percentile of 0.767 (the control gives 0.507), and PPMI reordering lifts Top-10 4+ by +0.12 over random order, with no information at all. The PPMI line score acts as an anti-frequency score:

- `log((C_ij + 0.5) T / ((C_i + 1)(C_j + 1)))` is positive for pairs of rarely drawn numbers even when they *never* co-occurred;
- it therefore favours the injected random winners over frequency-selected decoys.

**Net PPMI-ordering effect after subtracting the null artifact:** +0.18, 0.00 and +0.05 on the three targets. That is noise-level on three heavily correlated targets.

**Top-20 Johnson coverage.** The reported 76–92% coverage sits against an exchangeable expectation of 61.2% (788/1287). Under the null E0033 construction the expectation is 57–72%. The three reported targets are three draws of a wide per-target distribution. Johnson four-plus-first remains valid *geometry*, but "robust 76–92%" overstates what it delivers on average.

**Control.** The E0029 random-decoy construction is calibrated (0.49–0.52), so E0029's discovery replay is not affected by this artifact.
