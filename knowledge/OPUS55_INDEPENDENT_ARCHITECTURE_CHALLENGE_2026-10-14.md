# HEPS — Opus 5.5 Independent Architecture Challenge

**Date:** 2026-10-14 (SAST)
**Author:** Claude Opus 5.5. Roles: adversarial statistician, independent reproducer, meta-research auditor.
**Branch:** `research/opus-55-independent-challenge`. Nothing on `main` was modified.
**Experiment:** `experiments/E0037/`. The preregistration was committed before any code ran.
**Data:** Main and XTRA, 39 rows each, 2026-06-02 to 2026-10-13. The live ledgers match the expected state. Validation passed: `validate_draws`, `sync_manifest --check`, `check_stationarity`.
**Authority:** none. No prediction slate was generated, and no frozen artifact, ledger, existing experiment or governance file was edited.

---

## A. Executive verdict

**Predictive verdict: `INSUFFICIENT_EVIDENCE`, a negative result at the available power.** No information source available before a draw improves a coherent legal-line probability distribution over the exact fair-draw null, in either lane.

- Main composite e-process: max E = 1.22 over 33 targets.
- XTRA composite e-process: max E = 1.00.
- Retrospective `PROVISIONAL_SIGNAL` threshold: 80.
- 17 of 18 preregistered forecaster-lane cells score worse than uniform on exact-line log loss.
- The official frozen Main K13 record is 14 hits in 10 draws against 13.0 expected from random baskets.

**Methodological verdict: a methodological improvement without predictive lift.** This is the main contribution. Three results change how HEPS should be run.

1. **The Information Ceiling (exact).** Every downstream gain is bounded by `D = KL(P_true || U)` per draw. That covers K13 hits, catastrophe rate, 3+/4+ survival and portfolio events.
   - A 10% K13 lift (+0.13 winners/draw) requires D ≥ 0.0094 nats/draw, equivalent to about a 6% relative ball bias known *perfectly*.
   - The K13 lift that E0036 could detect at n=28 (0.70) requires D ≥ 0.26, equivalent to about a 31% ball bias.
   - **Compression, assembly and portfolio work cannot create what the field lacks.** That is now a theorem, not a policy.
2. **The anytime-valid prequential e-process.**
   - `log E = −Σ Delta`. The proper-score gate and a sequential test valid at *every* draw are one object.
   - Under H0, P(ever reaching 80) ≤ 1/80, with no alpha-spending and no 500-target terminal checkpoint.
   - It is frozen prospectively from 2026-10-16.
3. **Audit corrections to the evidence base.**
   - E0033's oracle-replacement construction is not exchangeability-calibrated. Under null winners it manufactures PPMI "signal": on 2026-09-08 a random winner gets percentile 0.767, against 0.507 under the calibrated control.
   - E0036's own pilot rule shows its MDE table understated the noise by 22–65×.
   - E0036's preferred M1 field degenerates into contiguous tail-band baskets.

**Mathematically correct versus informative.** HEPS now has several *mathematically correct* algorithms: exact DP normalization, the top-marginal K13 theorem, and Johnson coverage. Correct mathematics applied to a field with no information yields correct answers to the wrong question. An algorithm is predictive only if its input distribution differs from the truth-generating law less than uniform does, measured in out-of-sample log loss. No HEPS field has shown that.

---

## B. Critical architecture failures (Deliverable 1)

### B1. There is no upstream information; "acquisition" is random selection from estimation noise.

Every coherent field ever scored is at or worse than uniform on exact-line log loss:

| Field | Mean Δ (nats/target; negative is better) | Source |
|---|---|---|
| E0030 incumbent mixture | +0.0011 Main, +0.0021 XTRA | E0037 reproduction |
| E0032 Screen A (= E0036 M1) | **+0.0508**, reproduced to 2.7e-6 | E0037 F5 |
| E0032 Screen B (BARP line field) | +0.382 | E0032 |
| E0036 M1 / M2a / M2b, Main | +0.045 / +0.106 / +0.073 | E0037 Part C |
| Ball-bias learners (4 τ), drift learner, repeat model | all ≥ 0 in both lanes | E0037 Part B |

The incumbent gives about 93% weight to uniform, so its residual tilt is noise of order 1e-3 nats, and its top-13 is effectively a random basket. The prospective record confirms this:

- 10 official K13s scored 14 hits against 13.0 expected (p=0.42);
- 6 draws had H≤1, against 6.1 expected;
- 0 draws had H≥3, against 1.0 expected.

**Sign-convention hazard.** E0032 reported Screen A as "−0.05084 log-prob delta (negative is worse)". E0036 adopted the opposite convention (negative is better) but copied −0.05084 into its A.7 table. In E0036's convention the value is **+0.0508 ± 0.045**: worse than uniform, not significant.

### B2. The objective hierarchy is inverted.

Most HEPS effort since August has gone into stages 2–6: K13 objectives (E0026, E0031/32, E0035), triage (E0028/29), coalition ranking (E0013/22/23/33), Burgers (E0034) and Johnson geometry. The ceiling theorem shows all of these are bounded by D. At plausible D (≤0.005 nats/draw), even an *oracle* field gives at most +0.095 K13 winners per draw. A field learned from 39 draws realises a small fraction of that; in Part D it is +0.01 to +0.04 even under strong bias. E0035's prospective tie and E0032's identical four-objective baskets are what the ceiling predicts.

### B3. The sample cannot identify the effects being chased.

- **Power.** With 39 draws per lane, even a 20% relative ball bias is detected only 2% of the time by n=39. A 10% bias needs about 10 years for 88% detection, and a 5% bias reaches 11.5% in 10 years.
- **E0036's MDE table.** It used σ=0.0096 from the near-uniform E0030 mixture. The models' own σ is 0.21 (M1), 0.61 (M2a) and 0.27 (M2b). Its MDE80 at n=500 (0.026) exceeds the SESOI.
- **Machine metadata.** Main machine identity is unknown for 20 of 39 draws, and the best-documented machine has 7 draws. XTRA machine identity is unknown for all draws.

### B4. Evaluation artifacts have inflated apparent evidence.

- **Non-exchangeable stage isolation (E0033).** E0033 keeps model-selected decoys and injects random winners. Any ranker correlated with the acquisition score is then biased. The PPMI line score is effectively anti-frequency: `log((C_ij + 0.5)T/((C_i + 1)(C_j + 1)))` is positive for rare pairs that *never* co-occurred. The "PPMI floats 4+ into Top-10" observation (45–59%) is largely artifact on 2026-09-08 and noise-level net of the artifact. PPMI ordering nevertheless entered the official 2026-10-09 slate ordering.
- **Post-hoc statistic selection.**
  - XTRA PB2: familywise p=0.040 after choosing the statistic. A pre-specifiable Dirichlet e-value gives 5.4 (anytime p=0.19).
  - LDSAD 11..13: z=5.13 as a discovery statistic.
  - The 2026-09-01 HLR 5/5 narrative.
- **Patterns that are structural.** Main's consecutive-draw overlap deficit (0.37 against 0.5) produces a fitted repeat coefficient ρ ≈ −0.25 in every fit, yet the repeat model earns **zero** out-of-sample gain (Δ=+0.002). A visible pattern is not a predictive one.
- **Degenerate baskets.** F017's [27..39] band collapse reappears inside E0036 M1. The sign term `α·Σ sign(δ_j)` acts as a static coordinate-height tilt, and on XTRA it produced the K13 [38..50] for all 33 targets.

### B5. Method churn and no independent information source.

The 10 official K13s came from at least 6 different methods:

- candidate lattice;
- E0019 line mass;
- v35 pattern triage;
- E0032;
- E0033 with the E0030 field;
- E0035 variants.

No method has accumulated more than a handful of prospective targets, and with no valid sequential rule no claim could ever mature. Every forecaster is a transformation of past winning numbers. External information is limited:

- public coverage says the national lottery's draws moved to an independently audited RNG (Szrek2Solutions with Trusted Audit) under the previous operator;
- in 2025 the operator said it uses "certified draw machines and random number generators";
- the 2026 ledger records named machines for some draws, `electronic_rng` for two, and unknown for most;
- these statements predate the current operator (Sizekhaya), and I found no official step-by-step procedure.

**If draws are audited-RNG, there is no physical mechanism for a ball-level edge at all.**

---

## C. New ideas investigated (Deliverable 2: strategies ranked)

Every strategy below is scored against the six required questions. The ranking reflects scientific plausibility, incremental information, identifiability, feasibility and decision value. Novelty was not a criterion.

| Rank | Strategy | Information exploited | New or transformation? | Why might it beat the null? | Simplest baseline | Falsifier | Prospective test | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | **Anytime-valid prequential gate plus Information Ceiling** (MDL / prequential / e-value) | none new; it measures whether any forecaster has information | methodology | it does not try to; it makes every claim falsifiable at every draw and bounds downstream gains | uniform | E ≥ 80 under H0 more often than 1/80 (Ville); verified 0.6–1% at 20 | frozen e-process from 2026-10-16 | **implemented** (E0037 A, B) |
| 2 | **Physical ball-bias field with external metadata** (hierarchical Fisher/Wallenius law; priors from machine, ball-set and certification data) | ball-set or machine identity and measured ball properties, known before the cutoff | **genuinely new**, if obtainable | only plausible physical mechanism for a mechanical draw | metadata-free ball-bias field (implemented; null) | operator confirms audited RNG, or no metadata knowable before the cutoff, or prospective E < 1 at 250 draws | new single-purpose e-process | metadata-free version **implemented** (null); data acquisition needed |
| 3 | **Exchangeability-calibrated stage isolation** (random-decoy universes plus null-construction baselines) | none; it removes artifacts | methodology | not predictive; it prevents false credit | random decoys (E0029) | null-construction percentile ≈ 0.5 for E0033 (rejected: 0.767) | re-audit all oracle-K13 claims | E0033 audit **implemented** |
| 4 | **Structured coherent joint fields** (E0036 M1/M2a/M2b, sparse interactions) | past transitions | transformation | only if temporal dependence exists | uniform | Δ ≥ 0 out of sample; M2 ≤ M1 | inside the frozen e-process | **implemented** (independent implementation of the frozen spec); null; M1 identifiability defect |
| 5 | **Robust or posterior-uncertainty acquisition** (E0035 family, CVaR) | the same field | transformation | only redistributes risk when D > 0 | top-13 marginals | tie with POINT (as observed) | park until a field passes the gate | assessed via ceiling; low value now |
| 6 | **Regime / change-point routing** | past outcomes | transformation | needs genuine regimes | single regime | no external regime evidence | unidentifiable at n=39 without metadata | not pursued |
| 7 | **Cross-lane joint e-process** (product of the independent lanes' e-values for a shared hypothesis class, with no parameter pooling) | two independent processes | methodology | the product doubles expected log-evidence growth, roughly halving time to detection, for hypotheses that should hold in both lanes | per-lane e-processes | — | optional amendment | proposed only |

Notes on strategies 1–4:

- **(1)** It also supplies the SESOI (0.0094 nats/draw), derived from the director's own objective, a 10% K13 lift.
- **(2)** The ceiling shows the bias must be about 6% or more relative just for a 10% K13 lift to be *possible*. Part D shows that even 10% takes years to detect.
- **(4)** The sign term confounds a static coordinate-height tilt with transition information. Any successor must centre it, for example on `sign(δ_j) − E_U[sign(δ_j) | p]`, before being trusted. That would be a *new* frozen forecaster and a new e-process.

---

## D. Implemented experiments

All code is standard library only, deterministic and seeded. The tests are `tests/test_e0037_prequential_gate.py` (19 tests). Rerun with:

```
python -m unittest tests.test_e0037_prequential_gate -v
python scripts/e0037_prequential_gate.py --part all --workers 6   # ~20 min, writes experiments/E0037/results_*.json
```

| Artifact | Content | Evidence type |
|---|---|---|
| `experiments/E0037/hypothesis.md`, `protocol.yaml` | preregistration (commit `a0383fc`, before any code ran) | design |
| `scripts/e0037_prequential_gate.py` | exact laws, chain DP, E0036 MAP fits, e-process, power, audits | code |
| `results_verification.json` | full 2,118,760-line enumeration agreement ≤ 2.6e-13; null recovery 5.6e-16 | verification |
| `results_screen_a.json` | E0032 Screen A reproduced to 2.7e-6 nats/target | **independent implementation** reproduction |
| `results_replay.json` | 33 targets per lane; every forecaster; windows; per-target freeze hashes | **retrospective discovery** |
| `results_ceiling.json` | Information Ceiling tables and SESOI | exact theory |
| `results_power.json`, `results_null_check.json` | power under ball bias; Ville and martingale checks | simulation |
| `results_transition_divergence.json` | oracle KL of the full-data M1 fits | diagnostic |
| `results_audit.json` | official K13 record; E0033 null-construction audit, which reproduces E0033's published figures to 4 d.p. | audit and reproduction |
| `results.md`, `decision.md` | summary tables and decision | — |

**Repository validation (AGENTS.md §17), run 2026-10-14:**

| Check | Result |
|---|---|
| `validate_draws.py` | pass (39 rows) |
| `sync_manifest.py --check` | pass |
| `check_stationarity.py` | runs; reports mixed method and machine identity |
| `simulate_null_model.py --trials 100000 --seed 20260704` | runs |
| `structural_null.py --basket-size 13` | K13 P(4+) = 0.013094 and P(5/5) = 0.000607, matching E0037 |
| `unittest discover` | 88 tests, 87 pass |

The one failure is **pre-existing and unrelated**: `test_e0035_uncertainty_k13.test_full_protocol_replay_and_emit_result` hard-asserts a canonical cutoff of 2026-09-11 against the live ledger, which now runs to 2026-10-13. I did not edit another agent's test. It needs a snapshot-pinned loader or an updated assertion, at the director's discretion.

**Evidence separation.**

- *Retrospective discovery:* everything scored through 2026-10-13.
- *Independently reproduced:*
  - E0032 Screen A, by a new implementation;
  - E0033 Top-10/Top-20 figures;
  - E0030 incumbent field, against its prototype;
  - E0032 slot-product normalization.
- *Specification-prospective, implementation-late:* E0036 targets from 2026-10-02 to 10-13. These cannot promote anything.
- *Future prospective validation:* the E0037 e-process from 2026-10-16. Its forecasters are frozen by the commit containing this report.

---

## E. Performance comparison

### Primary: exact-line log loss against the uniform null (33 targets per lane)

| Forecaster | Main Δ (SE) | XTRA Δ (SE) |
|---|---:|---:|
| Uniform (M0) | 0 | 0 |
| BB τ=0.05 / 0.10 / 0.20 / 0.40 | +0.0007 / +0.0031 / +0.016 / +0.093 | +0.0013 / +0.0054 / +0.024 / +0.112 |
| Drifting ball bias (half-life 8) | +0.0070 (0.0103) | +0.0097 (0.0086) |
| Repeat persistence | +0.0021 (0.0303) | +0.0121 (0.0116) |
| E0036 M1 / M2a / M2b | +0.039 / +0.102 / +0.072 | −0.037 / +0.029 / +0.019 |
| **E0030 incumbent** | +0.0011 (0.0019) | +0.0021 (0.0013) |
| **Composite e-process: max E (anytime p)** | **1.22 (0.82)** | **1.00 (1.00)** |

For the gentlest learner, the one-sided 95% upper bound on its *achieved* improvement is about 0.0013 nats/draw on Main and 0.0007 on XTRA. Both are below the SESOI.

### Secondary (exploratory; 0 of 72 survive BH at q=0.10)

- K13 hits for every forecaster are within noise of 1.30 per draw.
- The most "successful" basket is XTRA M1's fixed [38..50] band: 51 hits against 42.9 expected (z≈1.5). It is a static-band artifact.

### PowerBall (Dirichlet e-process)

| Lane | max E | anytime p |
|---|---:|---:|
| Main | 3.1 | 0.32 |
| XTRA | 5.4 | 0.19 |

Neither reaches 20, let alone 80.

### Acquisition audit

Official frozen K13 scored 14 hits against 13.0 expected.

### Assembly audit (E0033 construction against null)

Under synthetic null winners:

- PPMI percentile ranges 0.43–0.77, against 0.5 for an exchangeable construction;
- PPMI Top-10 4+ reaches 0.41 on 2026-09-08, against 0.29 for random order.

The published E0033 PPMI-ordering effect is not distinguishable from the construction artifact plus noise.

---

## F. What HEPS should retain, reject or research further

### Retain (component level)

- The exact uniform legal-line null, exact DP normalization, the null-recovery contract and the top-marginal K13 theorem. All are verified again here.
- Johnson `four_plus_first` as *geometry*. Expectation is 61.2% 4+ coverage of exchangeable winner states; the three published 76–92% figures are draws from a wide per-target distribution.
- E0029's **random-decoy** oracle construction. It is calibrated (null percentile 0.49–0.52).
- The E0036 *gate idea*. The executed pilot rule shows it needs the e-process to be usable.
- Main/XTRA independence and the provenance flags.

### Reject or downgrade

- **E0033 oracle-replacement as lift evidence.** Downgrade it to "uncalibrated construction". Any future model-selected-decoy result must be reported against its null-construction baseline.
- **PPMI ordering as an assembly signal.** Keep it as a shadow scored only in random-decoy universes. It should not order official slates on current evidence.
- **E0036 M1 uncentred sign term as a transition feature.** It is confounded with a static height tilt and produces band baskets.
- **Aggressive frequency learning** (E0030 cumulative component, BB_t040). It is consistently worse than uniform, and under H0 its median log E is −19 by n=250.

### Research further

- External draw-mechanism and equipment metadata (§H2).
- The XTRA PB frequency and the XTRA high-band, but only as *monitored* components of the frozen e-process.
- Exchangeability re-audit of all oracle-K13 claims (§H3).

### Proposed deprecation-map row (for director approval; not enacted)

| Method / claim | Status | Why | Forward rule |
|---|---|---|---|
| E0033 oracle-replacement with model-selected decoys as ranker-lift evidence | DOWNGRADED / UNCALIBRATED | Winners and decoys are not exchangeable. Under null winners, PPMI percentile was 0.767 on 2026-09-08 (E0037 audit). | Use random-decoy universes, or report the null-construction baseline alongside every result. |

---

## G. Proposed next HEPS architecture

```
Stage 0   Exact nulls (uniform legal line; PB 1/16)                    [production, unchanged]
Stage 1*  FIELD GATE: frozen coherent forecasters -> per-draw log-ratio
          -> composite e-process per lane (Main, XTRA, Main-PB, XTRA-PB) [shadow governance, NEW]
            |-- E < 20 : NULL REGIME  -> stages 2-6 run in geometry-only mode; no performance attribution
            |-- E >= 80: SIGNAL REGIME -> leading forecaster becomes the field for stage 2 (after director review)
Stage 2*  Candidate K = top-K marginals of the gated field (mechanical; no separate optimizer) [experimental]
Stage 3   Enumerate C(13,5)=1287                                         [unchanged]
Stage 3.5 Pattern triage (E0029)       -> shadow, scored only in random-decoy universes   [shadow]
Stage 4-5 Coalition / ranking (E0013, PPMI) -> shadow, exchangeable controls only        [shadow]
Stage 6   Johnson four_plus_first geometry, fixed budget                 [production geometry]
Stage 7   PowerBall: uniform default; Dirichlet e-process gate           [shadow]
Side:     External metadata intake (draw method, machine, ball set) -> new forecasters only
          when knowable before cutoff; each starts its own e-process     [experimental]
```

**Differences from the incumbent:**

1. A new Stage 1* gate, whose authority is limited to labelling the regime.
2. In the null regime, the separate K13 optimizers (E0026, E0032, E0035) and coalition rankers lose "official" status, because their outputs are indistinguishable from random by the ceiling and the record. They remain shadows.
3. Stage isolation must use exchangeable controls.
4. Forecasters stay frozen for at least 100 targets; no per-draw method changes.

None of these components is eligible for promotion today.

---

## H. Three strongest follow-up experiments

### H1. E0037 prospective monitoring (already frozen)

Highest value, identifiable, zero marginal cost.

- **Run:** score each new draw with the frozen code. The window `prospective_confirmatory_from_2026_10_16` fills automatically.
- **Success:** a lane's prospective E ≥ 80, *and* the leading forecaster's prospective mean improvement exceeds 0.0094 nats/draw. That earns `PROVISIONAL_SIGNAL` and triggers an independent second implementation (E0036 G7).
- **Failure / futility:** after 100 prospective targets per lane, log E < 0, every class has Δ ≥ 0, and the 95% upper bound is below the SESOI. Record that the field-level route to a 10% K13 lift is unsupported.

### H2. Draw-mechanism and equipment provenance (E0038 candidate)

The only route to genuinely new information.

- **Acquire in writing from the operator (Sizekhaya), per draw:**
  - draw method (RNG or mechanical);
  - machine and ball-set identifiers;
  - whether they are fixed before ticket sales close;
  - ball-set certification measurements, such as weights.
- **Success:**
  - metadata available for at least 80% of draws, with pre-cutoff timestamps;
  - a hierarchical ball-bias forecaster using it, frozen and run as a fresh single e-process, reaches E ≥ 20 within 250 draws.
- **Failure:**
  - the operator confirms audited-RNG draws. Record that no physical mechanism exists and retire the physical-bias line; or
  - metadata is not knowable before the cutoff; or
  - E < 1 at 250 draws.

### H3. Exchangeability re-audit of every oracle-K13 result (E0039 candidate)

Re-score E0022, E0023, E0029, E0033 and E0034 claims under the null-construction baseline, using synthetic uniform winners with the exact historical construction.

- **Success:** each claim is restated as lift over the null construction, with a CI clustered by target.
- **Failure:** any claim whose lift loses significance is downgraded in the claim registry.

This needs no new data and closes the evidence-inflation channel found in B4.

---

## Appendix 1. Phase 2 questions, answered

- **A. Is the upstream field informative?**
  - Not detectably.
  - The bound on what the tested learners *achieve* is below the SESOI.
  - No temporal-dependence family (repeat, transition, interaction) beats uniform.
- **B. Is K13 the right objective?**
  - For a coherent field, top-13 marginals maximise E[H]; that theorem is accepted.
  - Alternative objectives (4+, containment, CVaR) differ only to second order in D.
  - At D ≈ 0 every K13 is equivalent, so objective research is premature until Stage 1* passes.
- **C. Are patterns structural?** Largely, yes.
  - Overlap deficit: fitted ρ ≈ −0.25, out-of-sample gain 0.
  - LLLLL has structural probability 0.18.
  - The M1 height tilt produces bands.
  - The e-process automatically prices every pattern against the exact null.
- **D. Is the sample sufficient?** No.
  - Power is about 2% for a 20% bias at n=39, and about 10 years for a 10% bias.
  - 5/5 is never a usable metric.
- **E. Is an independent source missing?**
  - Yes: the draw mechanism and equipment metadata.
  - Public reporting indicates audited-RNG draws under the previous operator, alongside named machines in 2026 records. No step-by-step official procedure was found.
  - Without operator-confirmed pre-cutoff metadata, **credible external predictive information is unavailable**.

## Appendix 2. Limitations

- All replay evidence is retrospective. My forecaster choices were made after reading HEPS reports. The repeat class is disclosed as outcome-motivated for Main.
- The one-step ridge estimator is a definition, not exact MAP. Validity does not require optimality.
- The E0036 implementation is the *first* one, so G7 still needs a second implementer. M1 is cross-validated against E0032's independent reported numbers.
- The F4 "mean ≈ 1" criterion is uninformative for heavy-tailed components. Ville's bound and exact normalization carry the validity argument, and the light-tailed component check passed.
- External-mechanism statements come from news coverage and operator statements (2020, 2025), not from an official procedure document. They predate the current operator.

## Sources (external)

- [Ithuba and RNG vendor Szrek2Solutions confirm the validity of the surprising draw results — World Lottery Association](https://www.world-lotteries.org/insights/news/member-news/ithuba-and-rng-vendor-szrek2solutions-confirm-the-validity-of-the-surprising-draw-results)
- [Ithuba and Szrek2Solutions confirm validity of surprising South Africa national lottery result — LotteryDaily](https://lotterydaily.com/2020/12/21/business/ithuba-and-szrek2solutions-confirm-validity-of-surprising-south-africa-national-lottery-result/)
- [Ithuba and RNG vendor Szrek2Solutions — Public Gaming](https://publicgaming.com/news-categories-m/lottery/7060-ithuba-and-rng-vendor-szrek2solutions-confirm-the-validity-of-the-surprising-draw-results)
- [Fair and transparent: National Lottery denies claims of rigged system — Sowetan (2025-08-08)](https://www.sowetan.co.za/news/2025-08-08-fair-and-transparent-national-lottery-denies-claims-of-rigged-system/)
- [Integrity of South African lottery again under scrutiny — LotteryDaily (2025-08-11)](https://lotterydaily.com/2025/08/11/business/south-africa-lottery-8/)
