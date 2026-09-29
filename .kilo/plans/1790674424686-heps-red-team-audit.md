# HEPS Red-Team Audit — Deliverable 1

**Role:** external Senior Quantitative Research Scientist (adversarial statistician / Bayesian modeller)
**Date:** 2026-09-29 (pre-evening draw; 2026-09-29 result treated as unrevealed)
**Status:** DELIVERABLE 1 only. Experiment design and code gated on approval.

---

## Phase 0 — Repository verification: PASS

All canonical values match after the repository sync.

| Item | Verified source | Value | Match |
|---|---|---|---|
| Main rows / latest | `data/draw_manifest.json:20-33` | 34 rows, `2026-09-25`, `draw_id` 34 | yes |
| Latest Main | `data/draw_history.jsonl:34` | `[5,9,22,34,38] \| PB3` | yes |
| Latest macro sum | `data/draw_manifest.json:30` | 108 (verified: 5+9+22+34+38) | yes |
| XTRA rows / latest | `data/powerball_xtra_manifest.json:9-12` | 34 rows, `2026-09-25`, `draw_id` 1758 | yes |
| Active start | both manifests | 2026-06-02, both lanes | yes |
| Registry tail | `experiments/registry.csv:40` | E0035 | yes |

Additional integrity observations (not discrepancies, but newly relevant):

- **`data/draw_history.jsonl:30-31` (2026-09-11, 2026-09-15) are `draw_method: "electronic_rng"`, `machine_name: "rng"`.** These are the only two such rows. The active series is described throughout as the *mechanical era* (e.g. `experiments/E0034/decision.md:13`, "Main Mechanical-Era ledger"). That label is no longer accurate for 2 of 34 rows. `governance/current_method_doctrine.md` §12 and `AGENTS.md` §11 require mixed-mechanism disclosure; no active experiment has yet accounted for this segment.
- **XTRA provenance is weaker than Main.** 13 of 34 XTRA rows carry `pending_official_source_verification`, and the official source returned HTTP 403 (`powerball_xtra_manifest.json:29-43,52`). Main rows 32-34 were verified against a director-approved archive on 2026-09-29 with explicit notes that mechanism was *not* inferred.
- **Shell access is restricted in this session** (`git *` and compound commands denied). The statistics below are computed from committed artifacts by hand and are reproducible from the cited files.

---

## A. What HEPS gets right

1. **The probability contract is correct and is the strongest asset in the repository.** `governance/current_method_doctrine.md` §3 fixes the exact IID null as uniform over `C(50,5)=2,118,760` legal sorted lines, and imposes a mandatory null-recovery test: a field whose residual ratios are all 1 must reduce *exactly* to that uniform null. This makes misspecification detectable instead of invisible, and it is the reason E0032 could refuse to attach a good compressor to a bad field (`experiments/E0032/upstream_field_screen_2026-09-07.md:33`).
2. **The information-family rule is right and is actively preventing a specific fraud.** `AGENTS.md` §3 and doctrine §2 correctly forbid treating `sign(DELTA)`, `abs(DELTA)`, `x_j`, and `x_j mod 10` as independent evidence, because they are deterministic views of one transition. This is the single most common inflation in applied lottery modelling, and HEPS bans it by name.
3. **Proper-score-first gating is the right ordering** (doctrine §4, `AGENTS.md` §9), including the explicit 2×2 reading: better K13 recall with worse proper score is optimisation over misspecification, not lift.
4. **Governance is genuine scientific memory.** Frozen pre-draw artifacts, a deprecation map with forward-reuse rules, evidence labels held separate from architecture status, and historical-precedence rules. `governance/methodology_deprecations.md` is unusually disciplined — it blocks specific formulas, not just conclusions.
5. **Negative results are preserved as first-class contributions.** E0030 is a complete, reproducible negative (`experiments/E0030/findings.md`), and E0034 is a clean `REJECT` with a forward rule against reopening by retuning. This is rarer and more valuable than a spurious hit.
6. **E0035's upstream warning is the most intellectually honest statement in the record:** *"E0035 cannot establish a predictive edge even if compression metrics improve. The experiment tests decision robustness under field uncertainty, not new predictive information."* (`experiments/E0035/decision.md:36-38`). That is exactly the right conclusion and it is being drawn while the rest of the programme continues.

---

## B. The three most significant methodological weaknesses

### B1. The entire K13 candidate-acquisition programme is performing at or below random selection

This is the finding that should reorganise the programme, and it is visible directly in the committed numbers.

For a uniformly random 13-coordinate basket against a 5-of-50 draw:
- expected winner coordinates per draw = `13/50 × 5` = **1.30**
- per-draw hypergeometric sd = `sqrt(5 × 0.26 × 0.74 × 45/49)` = **0.940**
- `P(H ≤ 1)` = `[C(37,5) + 13·C(37,4)] / C(50,5)` = **0.6110**
- `P(H ≥ 3)` = **0.1030**, `P(H ≥ 4)` = **0.0131**

Now the observed results:

| Experiment | Observed | Random-K13 expectation | Verdict |
|---|---|---|---|
| E0030 Main joint K13 | 23/95 coords = 1.21/draw | 24.7/95 = 1.30/draw | **below random** (z = −0.42) |
| E0030 XTRA joint K13 | 17/95 coords = 0.89/draw | 24.7/95 = 1.30/draw | **well below random** (z = −1.88) |
| E0030 Main H≤1 | 13/19 = 68.4% | 61.1% | **worse than random** |
| E0035 POINT_MEAN | 1.24 hits/draw, 18/25 H≤1 (72%) | 1.30, 61.1% | **worse than random** |
| E0035 BB_ROBUST | 1.20 hits/draw, 17/25 H≤1 (68%) | 1.30, 61.1% | **worse than random** |

Every arm of the current candidate-funnel architecture retains *fewer* winner coordinates than a basket chosen at random, and is *more* likely to produce a catastrophic `H≤1` draw. E0035's headline "reduced H≤1 catastrophes by one draw" (18→17) is an improvement from *worse-than-random to still-worse-than-random*, not a gain against a null. Meanwhile zero 4+ and zero 5/5 outcomes across 25 targets is entirely unremarkable: random K13 expects 0.33 four-plus draws in 25.

This reframes the stated bottleneck. The problem is not that candidate acquisition is "the current bottleneck" to be improved. The problem is that candidate acquisition has **no measurable positive value over uniform selection**, and the compression research (E0032, E0035) is refining a decision rule whose input is indistinguishable from noise.

### B2. The negatives are under-powered, so the record cannot distinguish a true null from an inconclusive test

E0030 reports paired log-loss deltas with descriptive standard errors. Converting to t-statistics against the uniform null:

| Field | Mean Δ log-loss | SE | t | Reading |
|---|---|---|---|---|
| Main mixture | +0.002634 | 0.002196 | 1.20 | not significant |
| XTRA mixture | +0.003349 | 0.001959 | 1.71 | not significant |
| Main frequency | +0.083460 | 0.030916 | **2.70** | **significantly worse** |
| XTRA recency | +0.049289 | 0.023029 | **2.14** | **significantly worse** |

(Uniform mean log loss = 14.5663 nats.)

So the correct reading of E0030 is *not* "the mixture is slightly worse than uniform." It is: **the mixture is statistically indistinguishable from uniform, and the components that deviate most from uniform deviate significantly in the wrong direction.** The frequency component is a *detected negative* at t = 2.70, not a weak positive.

The decisive number: at n = 19 the minimum detectable effect at 80% power is `2.80 × 0.002196` = **0.0061 nats per target**, i.e. **0.042% of log loss**. And with 35 registered experiments (`experiments/registry.csv`) each testing for improvement at a conventional 5% one-sided threshold with no multiplicity control, the family-wise probability of at least one false positive is `1 − 0.95^35` ≈ **84%**. Q012 in `knowledge/open_questions.md:118-128` asks for exactly this power analysis; it has never been done, and it is the reason the programme cannot currently tell a real null from an under-powered one.

### B3. The load-bearing conditional-independence assumption has never been tested

The entire candidate-funnel architecture — doctrine §3, E0021, E0030, E0026, E0032, E0035 — rests on one construction:

```
Q(x) = P0_line(x) · Π_j T_j(x_j)      for legal sorted x
```

`AGENTS.md` §7 states plainly: *"Sorted slots are dependent. Do not multiply per-slot structural marginals and call the product an exact joint null."* The product form has been corrected once already (E0019's `Π_j q_j(x_j)` was rejected precisely because it re-multiplied order-statistic geometry and failed null recovery). The *residual* product `Π_j T_j(x_j)` fixes null recovery but silently introduces a different untested assumption: **that the residual ratios `T_j` are conditionally independent across sorted slots given the line geometry.** Nothing in the repository tests this. E0032's DP evaluates the product form exactly; it never checks whether the product form is the right functional family.

This is the assumption that, if false, invalidates E0021, E0026, E0030, E0032 and E0035 simultaneously — the entire acquisition architecture — and it is testable cheaply and decisively.

---

## C. Apparent signals that are almost certainly structural artefacts

1. **BARP modal HLR 5/5 on 2026-09-01, 4/5 on 2026-09-04.** Already correctly downgraded to "one-target prospective evidence, not a promotion" (`AGENTS.md` §10). But the decisive evidence already exists and is not being weighed: E0032 Screen B integrated the frozen BARP formula into one coherent legal-line field and scored it at **−0.382 nats per target versus uniform** (`upstream_field_screen_2026-09-07.md:27`). A rule that hits 5/5 on modal direction while losing 0.38 nats/draw on the proper score is a direction-marginal artefact, not information. This is settled and should be recorded as settled.
2. **E0032 Screen A, the minimal signed-displacement tilt, scored −0.0508 nats/target** with coefficients shrinking to ≈0 (α≈0.0319, β≈−0.00156). The doctrine-preferred representation, in its cleanest two-parameter form, is *worse than uniform* and correctly shrank itself toward zero. That is a null result about the signed-displacement family at this sample size, and it is stronger than the anecdotes that motivated the family.
3. **LDSAD band 11..13.** Discovery-derived, explicitly multiplicity-exposed in its own registry entry, one prospective hit. Artefact until independently frozen.
4. **E0013 PPMI coalition topology.** Registry notes frequency looked strong on 2026-09-01 and PPMI on 2026-09-08 — *which signal wins changes per target*, which is the signature of noise, not of a stable rule. `experiments/E0033/decision.md:17` already says this.
5. **Any "recent-draw" pattern in E0035's diagnostic** (`:40-48`) — post-hoc by the experiment's own admission, designed after those results existed. Zero credit, correctly.
6. **Machine/ball-set non-exchangeability.** Draws 30-31 introduce `rng` into a mechanical-era series. This is a *provenance* fact, not a signal. Treating it as a regime boundary would be the exact "infer mechanism from outcome pattern" error that `AGENTS.md` §11 forbids.

---

## D. Diagnostic of K13 failure: probability-field error, not compression error

**Verdict: probability-field error, and it is upstream and total.**

The reasoning is decisive because E0032 already ran the decisive experiment. E0032 built four mathematically correct fixed-K13 objectives over one frozen field — `K13_MEAN` (provably Bayes-optimal for `E[H]`), `K13_4PLUS`, `K13_5`, `K13_ROBUST` — and then declined to freeze any of them, because the upstream field failed the proper-score gate first. That is the correct decision and it localises the failure precisely:

- **Compression is not the bottleneck.** A compressor cannot manufacture information that is absent from, or misspecified in, its input. Given a field that is indistinguishable from uniform, *every* K13 objective is near-degenerate, and empirically they are: E0035's `POINT_MEAN` and `POINT_ROBUST` produced **identical** baskets and metrics, and `BB_MEAN` and `BB_ROBUST` produced **identical** baskets and metrics. Two of four arms are exact duplicates. E0032's accepted theorem that Top13 marginals are globally optimal for `E[H]` means the remaining freedom is largely illusory.
- **The field is the bottleneck, and it is at zero.** Uniform log loss is 14.5663 nats. E0035's held-fixed field sits at +0.001466 nats/target worse than uniform, with an MDE of ~0.0061 at n=19. The field is not weakly informative; it is uninformative to within measurement error, and the parts that are *not* uninformative are harmful (frequency, t = 2.70).

The 2026-09-01 lesson in `AGENTS.md` §10 — that "strict slot provenance lost useful anywhere-coordinate information" — is real but it is a *second-order* effect. It explains why 14 and 16 were dropped from a K13. It does not explain why the K13 retains fewer winners than random selection. Preserving adjacent-slot evidence in a field that carries no information produces a marginally better basket drawn from a null distribution.

---

## E. Information gaps

1. **No power or identifiability analysis exists anywhere** (Q012, open since 2026-09-05, never actioned). Without it, no HEPS result — positive or negative — is interpretable. This is the highest-leverage gap.
2. **No multiplicity control across the experiment series.** ~35 registered experiments, no family-wise accounting, no pre-registered stopping rule.
3. **The conditional-independence assumption in `Π_j T_j(x_j)` is untested** (B3).
4. **The `electronic_rng` segment in rows 30-31 is unmodelled and unreconciled** with the "mechanical era" framing used by E0034 and the manifest's `observed_draw_methods`.
5. **E0021 has never been implemented.** `experiments/E0021/` contains `hypothesis.md`, `decision.md`, `protocol.yaml` — no code, no results. The doctrine's preferred representation exists as a design document. E0032 Screen A probed a 2-parameter shadow of it and found it worse than uniform.
6. **XTRA provenance is materially weaker than Main** (13/34 rows pending official verification after an HTTP 403), and no experiment currently reports XTRA conclusions with that caveat attached to the headline number.
7. **No experiment has ever been scored as a genuine end-to-end proper-score improvement.** Every one of E0001-E0035 is `INSUFFICIENT_EVIDENCE` or `REJECT`.

---

## F. Recommendations

### Retain (high value, do not touch)
- The probability contract and null-recovery test (doctrine §3). This is the correct foundation.
- E0032's exact DP (`experiments/E0032/k13_dp.py`) and E0030's normalised-probability / hypergeometric / matched-exposure infrastructure. Both are exact, verified, and reusable.
- E0033's exhaustive oracle-replacement enumeration (prevents cherry-picking which non-winners are removed).
- E0022 four-plus-first Johnson geometry — assembly/portfolio only, zero candidate authority, as already scoped.
- The full negative-result corpus. E0030 and E0034 are publishable-quality nulls.
- The governance layer as-is.

### Reject / freeze
- **Freeze all new candidate-feature families.** E0023 shell, E0027 SmokeField, E0028 LDSAD, E0034 Burgers, E0035 bootstrap compression have each consumed a cycle and returned null. The pattern is the finding.
- **Formally retire the BARP modal-HLR direction claim** on the E0032 Screen B evidence (−0.382 nats/target). Record it as settled, not open.
- **Do not reopen Burgers/PDE variants** by retuning viscosity or discretisation — E0034's own forward rule.
- **Stop treating K13 recall as a progress metric** until the field passes the proper-score gate. Per doctrine §4 and `AGENTS.md` §9 this is already policy; it is not being followed in practice, because B1 shows the metric is *negative*.

### Simplify
- **Collapse the four K13 arms to one.** `POINT_MEAN` ≡ `POINT_ROBUST` and `BB_MEAN` ≡ `BB_ROBUST` on the current field. Two duplicate arms inflate apparent search breadth at zero information cost. Keep `Top13` marginals; it is provably optimal for `E[H]` and needs no optimiser.
- **Retire the "one new expert per cycle" cadence.** Complexity is not progress (`AGENTS.md` §18).

### One immediate housekeeping item (not an experiment)
**E0035's frozen prospective target 2026-09-15 is now in the ledger and appears unscored.** Actual result: `[7,23,25,27,50] | PB7`.
- `POINT_MEAN` `[4,8,9,13,14,16,19,22,27,31,37,38,40]` → intersection `{27}` → **1/5**
- `BB_ROBUST` `[4,9,13,14,16,19,22,27,31,34,37,38,40]` → intersection `{27}` → **1/5**

A tie at 1/5, with `H≤1` for both arms. This is HEPS's first clean frozen one-seat prospective comparison and it is a null. It should be recorded in `experiments/E0035/decision.md` under a post-draw scoring section (permitted by `AGENTS.md` §13), with the frozen artifacts left immutable.

---

## Recommended research direction (for approval — preregistration withheld per instructions)

**Single highest-value untested hypothesis: conditional exchangeability of the slot residual ratios.**

> Under the load-bearing construction `Q(x) = P0_line(x)·Π_j T_j(x_j)`, are the residual ratios `T_j(x_j)` conditionally independent across sorted slots given the exact order-statistic geometry?

Why this and not a seventh feature family:

- It is the **only** untested assumption that, if false, invalidates E0021, E0026, E0030, E0032 and E0035 at once. A positive finding redirects the whole acquisition architecture; a negative finding retires it. Either outcome is decision-relevant and neither adds a new expert.
- It is **cheap and exact**. `C(50,5)=2,118,760` legal lines is tractable, and the E0032 DP already evaluates the product form without enumeration.
- It has a **built-in exact null**: if the true field is the uniform legal-line null, residual dependence is zero by construction, and the test statistic has a computable null distribution. No simulation-favourable assumptions required.
- It is **falsifiable before any prospective target**, so it does not consume the 2026-09-29 shadow slot.
- It directly implements `AGENTS.md` §18's stated value of "stronger nulls, cleaner dependency modelling."

Directionally, I expect this to **fail to reject conditional independence** (residual ratios estimated from ~30 draws will be too noisy to detect dependence even if it exists), and the honest null conclusion is itself the deliverable: it would establish that the acquisition architecture is unfalsifiable at the current sample size, which is exactly the finding that should trigger the power analysis in E and end the feature-factory cadence.

**Runner-up, and arguably the true root question:** Q012 — a formal power/identifiability analysis stating, for each primary metric, the effect size HEPS *could* detect at n = 34 and at n = 100/250/500, with a pre-registered multiplicity budget and stopping rule. This is the analysis that would tell the programme whether any of the 35 completed experiments could ever have succeeded, and it is the input to every future go/no-go decision.

**Recommendation:** run both, as a single experiment package, with the power analysis as the *gating* component — the dependence test is only interpretable once the detectable effect size is known. If forced to choose exactly one, choose the power analysis, because it determines whether the dependence test would have power to reject anything.

---

## Status and gate

- Phase 0 verification: **PASS**
- DELIVERABLE 1 (red-team audit): **complete** (A-F above)
- DELIVERABLE 2 (single preregistered experiment): **withheld pending approval**
- DELIVERABLE 3-6 (implementation, replay, prospective shadow, self-critique): **not started, gated**

Two decisions needed from the director:

1. **Approve the research direction** — the power-analysis-gated conditional-exchangeability package, or an alternative of your choosing.
2. **Confirm the next unused experiment ID.** `experiments/registry.csv` ends at E0035, so the next ID is **E0036**, assuming the 2026-09-15 scoring housekeeping does not consume it.

I am currently in plan mode and cannot write to `experiments/` or run replay code. Implementation requires switching to an implementation-capable agent.
