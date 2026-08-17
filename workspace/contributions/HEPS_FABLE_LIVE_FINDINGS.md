# HEPS FABLE 5 — Candidate-Acquisition Review

Status: **LIVE (rev 2, 2026-08-17).** Supersedes rev 1 ("FINAL, read-only"). Rev 1 was compressed to an 800-word ceiling that has since been withdrawn; this revision restores suppressed detail and **corrects three rev-1 errors** (§0).

Reproducibility: rev 1 relied on a throwaway script, leaving its numbers unauditable (AGENTS §16 defect). Rev 2 replaces it with a persisted, seeded, stdlib-only artifact:

- `experiments/E0007/reproductions/fable5_acquisition_probe.py`
- `experiments/E0007/reproductions/fable5_acquisition_probe_results.json`

```bash
python experiments/E0007/reproductions/fable5_acquisition_probe.py \
  --json experiments/E0007/reproductions/fable5_acquisition_probe_results.json
```

Authority caveat (unchanged): the probe implements the *probe author's proxy* frequency / recency / starvation / ±1±2-shadow rules over `data/draw_history.jsonl`, not frozen HEPS expert scores. Walk-forward, 19 scored targets (draw ids 4–22), post-hoc replay, zero predictive credit. Diagnostic only.

## 0. Corrections to rev 1

| # | Rev-1 claim | Rev-2 finding | Impact |
|---|---|---|---|
| C1 | Proper-score deltas listed as negative (`recency −2.59`, `starvation −0.93`, …) while simultaneously described as "worse than flat" | Sign-convention error: **positive = worse** under log loss. Rev-1 magnitudes were also **sums over 50 coordinates**, not means. Rev-2 per-coordinate means (×50 in brackets): recency +0.0517 [2.585], shadow +0.0429 [2.145], frequency +0.0283 [1.415], starvation +0.0186 [0.930], linear pool +0.0098 [0.490], log pool +0.0067 [0.335]. Recency and starvation reproduce rev 1 to 3 s.f.; the other four differ in magnitude (and frequency/starvation swap rank) because rev 1's exact weights are unrecoverable | Headline conclusion unchanged and **strengthened**: all six rules are worse than flat, p ≤ 0.026, every bootstrap CI excludes zero. Rank order among failing rules is *not* reproducible and must not be cited |
| C2 | "the rescue-vs-displaced trade is **null**" | The trade is **significantly negative**: −0.368 winners/draw, t = −2.69, p = 0.015, CI95 [−0.632, −0.105] | Upgrade. E0007 Arm B is not merely unsupported; in this proxy it is **actively harmful** |
| C3 | "displaced core seats 10–13 at 0.092" | Displaced seats hit at **0.171** vs rescue seats **0.079** (exchangeable 0.100) | Reverses the interpretation: consensus seats 10–13 are the *best-performing* seats in the basket, not marginal filler |

Rev-1 §7 fatal-risk, §11 missing-data, and §5 experiment-design conclusions survive unchanged.

## 1. Executive Verdict

HEPS's K13 championship is **not currently decidable**, and the defect is the estimand, not the algorithm.

Exact hypergeometric reference for any fixed 13-basket under an exchangeable 5/50 draw (`Hypergeom(N=50, K=13, n=5)`):

| x winners in K13 | P(x) |
|---|---|
| 0 | 0.20573 |
| 1 | 0.40523 |
| 2 | 0.28604 |
| 3 | 0.08990 |
| 4 | 0.01249 |
| 5 | 0.00061 |

Mean 1.30, variance 0.8834, **sd 0.9399**. P(≥3) = 0.10299; P(≤1) = 0.61096; P(5/5) = 6.07 × 10⁻⁴.

Power consequences at α = 0.05, 80%:

- 12 targets (E0007's declared window) detect only **Δ = 0.760 two-sided (+58% lift)** or Δ = 0.675 one-sided;
- Δ = 0.20 requires **173 targets two-sided / 137 one-sided** (rev 1 said ~141; that figure was one-sided-only and is superseded);
- Δ = 0.50 requires 22 targets one-sided.

At three draws/week, 173 targets ≈ **13 months** of prospective data. E0007 and E0005 as frozen will both terminate in "no evidence" for **statistical, not scientific, reasons** — a Type II failure guaranteed at design time.

**Corrected mechanism for the fix (important; rev 1 stated this wrongly).** Rev 1 justified the proper-score estimand as "~50 Bernoulli observations per draw, ~10× resolution." That reasoning is invalid: the 50 coordinates are **not independent** — they are constrained by Σpₙ = 5 and are negatively correlated, exactly as the hypergeometric variance already encodes. The real and larger gain is **variance reduction in a paired, continuous statistic**:

- K13 winner count: integer-valued, near-degenerate (81% of mass on {0,1,2}), per-draw sd 0.94 against a mean of 1.30;
- paired per-draw log-loss delta vs flat: continuous, observed **sd = 0.0147** against an observed effect of 0.0098.

Empirically the same proxy consensus that is undetectable at K13 is detected by the paired proper score in **≈18 targets two-sided / 14 one-sided** — a **~9.8× sample-size efficiency gain** over the Δ = 0.20 K13 test. The gain comes from pairing and from removing the top-13 truncation that discards all information about *how* wrong a vector is, not from a fictitious 50× independent replication.

## 2. Dominant Bottleneck

**Measurement/estimand power**, sitting on top of a **missing-information / omitted-variable** problem (§11). Explicitly *not*:

- not consensus suppression — §3 shows the consensus core is the strongest part of the basket, and dissent-preservation is negative;
- not the ranking algorithm or the assembly stage — the proxy fails before Johnson is reached;
- not Johnson geometry, which is downstream of a frozen K and cannot repair acquisition.

E0007's founding premise from the 2026-08-14 Physics-of-Failure ("candidate acquisition is the dominant failure stage") is **confirmed** as a localization; its proposed *remedy* (rescue seats) is falsified in proxy (§3).

## 3. E0007 Verdict

`INSUFFICIENT_EVIDENCE` as an experiment; the Core9+Rescue4 challenger is **falsified in proxy** and should not enter a 12-target prospective window in its current form.

### 3.1 The rescue trade is negative, not null

Per-seat hit rates over 19 targets, 4 seats each (76 seat-observations per arm), exchangeable reference 5/50 = 0.100:

| Seat class | Hits/seats | Rate |
|---|---|---|
| Displaced consensus seats 10–13 (what Arm B gives up) | 13/76 | **0.171** |
| Rescue seats (what Arm B buys) | 6/76 | **0.079** |

Paired per-draw trade (rescue hits − displaced hits): mean **−0.368 winners/draw**, sd 0.597, t = −2.69, **p = 0.015**, bootstrap CI95 [−0.632, −0.105]. Arm B − Arm A is identical by construction (−0.368), because the two arms differ only in seats 10–13.

Interpretation: the coordinates consensus ranks 10th–13th are the **highest-yielding seats in the entire basket** (0.171 > 0.100 exchangeable), while dissent-nominated coordinates underperform exchangeable (0.079). E0007's own predeclared "likely failure mode" — that rescue redistributes correlated information while weakening the core — is the observed outcome, and the loss is larger than that framing anticipated. Caveat: p = 0.015 is unadjusted, post-hoc, in-proxy, and on a comparison chosen after seeing the data; treat as a strong design warning, not a confirmed effect.

### 3.2 Rescue-family breakdown (19 nominations per family)

| Family | Hits/seats | Rate |
|---|---|---|
| shadow (Coulomb/stiction proxy) | 3/19 | 0.158 |
| frequency | 2/19 | 0.105 |
| recency | 1/19 | 0.053 |
| starvation | 0/19 | **0.000** |

Only shadow exceeds exchangeable, and 3/19 is fully consistent with chance (P(X≥3 | n=19, p=0.1) ≈ 0.27). Starvation contributes **zero hits in 19 nominations** while consuming a permanent seat — the clearest deletion candidate in the rescue design.

### 3.3 Rescue seats are not orthogonal — quantified

Mean pairwise K13 basket overlap, exchangeable expectation 13²/50 = 3.38:

| Pair | Mean overlap | vs exchangeable |
|---|---|---|
| frequency ∩ recency | 7.58 | +4.20 |
| recency ∩ shadow | **6.32** | +2.94 |
| frequency ∩ shadow | 4.95 | +1.57 |
| starvation ∩ shadow | 2.47 | −0.91 |
| frequency ∩ starvation | 0.05 | −3.33 |
| recency ∩ starvation | **0.00** | −3.38 |

(rev 1 reported recency∩shadow as 6.42; reproduced value is 6.32.)

Two structural facts:

1. **frequency, recency and shadow are one axis.** Overlaps of 7.58/6.32/4.95 against 3.38 mean E0007's "orthogonal families" are largely three renamings of *short-horizon recurrence*. Counting them as independent rescue votes inflates confidence exactly as AGENTS §8 warns (Q007, expert redundancy).
2. **recency ∩ starvation = 0.00 is a deterministic artifact, not a second information source.** Under the probe's definitions recency weight = 1/age and starvation weight = age, so the rankings are exact reverses over one statistic; disjointness at K=13 is algebraically forced whenever ties do not straddle the boundary. A **sign flip of one variable is not a second variable.** Any HEPS diversity metric that rewards low basket overlap will score this pair as maximally diverse while it carries strictly one degree of freedom — a live scoring hazard if "expert diversity" is ever operationalized as set disjointness.

### 3.4 Reproducibility defect in Arm A

Protocol line `A_consensus_only.rule` = "top 13 from the frozen incumbent consensus candidate score for that target" names **no versioned artifact, script, or commit**. No `expert_registry.yaml` entry, module path, or frozen output file resolves "the incumbent consensus candidate score". As written, the championship's control arm cannot be replicated by an independent agent — blocking the reproduction requirement in `E0007/findings.md` and the promotion gate in `E0007/decision.md`.

### 3.5 What E0007 should keep

Hypothesis B (coordinate mobility: `P(appears anywhere)` vs `P(occupies exact slot)`, Q017) is **not** tested by the rescue census and remains the most valuable surviving part of E0007. It is a genuine estimand change rather than a reshuffling of seats, and it maps naturally onto the §5 vector formulation.

## 4. E0005 Verdict

`INSUFFICIENT_EVIDENCE`; keep as a diagnostic, do not gate acquisition on it.

The protocol is **methodologically clean** and should be preserved as a template: fully predeclared formulas (`odds_final = odds_emp · (P0(H)/P0(L))^0.6`, κ = 10 shrinkage toward `NULL_VVD_STRUCTURAL`), deterministic sparse-pooling and REPEAT rules, explicit structural-null anchoring, and the 2026-08-14 `+2` residual explicitly denied retrospective credit. Little in HEPS is this well specified.

Three defects nonetheless make it undecidable in its declared window:

1. **No declared mapping to the acquisition estimand.** BARP/VVD-R optimize per-slot HLR Brier/log-loss and VVD log-loss/RPS. Nothing states how a slot-direction probability gain converts into candidate-coordinate survival. `resulting_candidate_coordinate_recall_at_fixed_exposure` appears only as a *secondary* metric with no threshold, so even a real BARP win cannot be shown to improve K13 acquisition.
2. **Effective sample is far smaller than it appears.** ~21 transitions × 5 slots is not 105 observations: sorted order statistics are strongly dependent within a draw (Slot_i < Slot_{i+1} by construction), and the falsification rule ("better on a majority of slots") treats five correlated tests as independent. BARP then partitions those ~21 transitions into per-slot run-length bins; its own sparse-pooling trigger (<3 prior transitions) will fire on most bins for most of the window, so BARP frequently collapses to its pooled prior and is **structurally unable to differ from the baseline it is tested against**.
3. **Direction is the low-information half.** `NULL_HLR_STRUCTURAL` already matched all five realized directions on 2026-08-14 (`HHLLL`). Slot-1 and Slot-5 HLR is near-deterministic under order-statistic geometry — a low Slot1 is very likely to move up, a high Slot5 down — so BARP's headroom over the exact null is concentrated in the middle slots and is small. Beating a strong exact null on a nearly-determined variable is the least informative test available.

Recommended amendment: add the slot-mass → 50-coordinate mapping (§8) so E0005 is scored on the same estimand as everything else, and replace "majority of slots" with a single draw-level paired score.

## 5. Best Next Experiment — FCPC-13

**Frozen Candidate-Probability Championship.** Replaces the K13 winner-count championship as the primary acquisition test.

- **Entrant contract.** Every entrant emits pre-draw a vector p₁…p₅₀ with **Σpₙ = 5 exactly** and pₙ ∈ (0,1). Entrants: incumbent consensus (pinned to a commit); linear pool; log pool; frequency; recency; starvation; stiction/shadow; E0007 Core9+Rescue4 expressed as a vector; E0005 slot mass mapped to coordinates (§8).
- **Comparator.** Flat pₙ = 0.1 is primary and confirmatory; recency and frequency are secondary reference entrants. Flat is the exact exchangeable null for this estimand: Σpₙ = 5 with all coordinates equal is precisely the `Hypergeom(50,K,5)` marginal, so it is a **structural null in the AGENTS §8 sense, not a heuristic baseline** — and consequently not an ensemble vote.
- **K is demoted to a derived metric.** Top-13 of each vector is reported for continuity with Q003 but is **never the test statistic**.
- **Frozen inputs.** Ledger rows strictly before the target; vectors committed to git before the draw; commit hash recorded in the cycle directory.
- **Scoring.** Paired per-draw Bernoulli log loss and Brier over all 50 coordinates; Δ vs flat with paired t and bootstrap CI. Secondary: calibration curve, K13 winners retained, 3+/4+/5, 0/1 catastrophe rate.
- **Targets.** 20 fresh prospective draws, fixed stopping, no interim promotion, no interim peeking at cumulative Δ.
- **Exposure control.** Σpₙ = 5 makes exposure matching automatic and **K-inflation impossible** — a challenger cannot quietly widen its basket, because probability mass is conserved by construction.
- **Multiplicity.** Entrants fixed at freeze; Holm across entrants.

Power check from §1: with the observed paired sd (0.0147), an effect the size of the proxy consensus deficit is detectable in ~18 targets, so a 20-target window is adequately powered for *this* estimand — unlike the 12-target K13 window, which is not powered for any plausible effect.

## 6. Why This Has Highest Expected Information Value

FCPC-13 tests the claim HEPS actually needs — *does any expert carry incremental information beyond flat, recency and order-statistic structure?* — instead of an artifact of basket truncation. Top-13 truncation destroys most available signal: it discards the magnitude of each probability and all information about the 37 excluded coordinates, then quantizes what remains into an integer with sd 0.94.

**Strong prior from the proxy census (19 targets, all rules worse than flat):**

| Rule | Δ mean log loss vs flat | t | p | bootstrap CI95 |
|---|---|---|---|---|
| log pool | +0.0067 | +2.49 | 0.023 | [+0.0015, +0.0118] |
| linear pool | +0.0098 | +2.91 | 0.009 | [+0.0033, +0.0162] |
| starvation | +0.0186 | +2.43 | 0.026 | [+0.0041, +0.0334] |
| frequency | +0.0283 | +5.37 | <0.001 | [+0.0181, +0.0384] |
| shadow | +0.0429 | +4.52 | <0.001 | [+0.0238, +0.0602] |
| recency | +0.0517 | +5.92 | <0.001 | [+0.0352, +0.0683] |

Positive = worse than flat. Brier agrees on all six (t = +2.43 to +6.54). **Every CI excludes zero**, so this is not a null result — it is a consistent, significant finding that these proxy rules are **anti-informative**: they lose to a uniform vector that uses no data at all.

Corroborating K13 view (mean winners retained, exchangeable 1.30): starvation 1.474, frequency 1.316, linear pool 1.316, log pool 1.211, shadow 1.158, recency 0.947, flat 1.105. Note the **estimand disagreement**: starvation looks best on K13 (+0.174) while ranking third-worst on log loss, and flat looks poor on K13 (−0.195) while winning decisively on proper score. With 19 targets no K13 difference approaches significance (all far below the Δ = 0.76 detectable at n = 12), so **the K13 ordering is noise while the proper-score ordering is signal** — a direct empirical demonstration of the §1 argument.

Positive structure worth keeping: log pool (+0.0067) and linear pool (+0.0098) are the *least bad* entrants and beat every constituent rule. Pooling correctly shrinks overconfident rules toward flat, so an honest ensemble's main achieved function today is **damage limitation, not information addition** — itself a promotable architectural finding if it replicates prospectively.

If this pattern replicates on frozen HEPS experts, the correct conclusion is that the current feature set is anti-informative and the answer is **information acquisition (§11), not another ranking algorithm**.

## 7. Fatal Risks

- Vectors not committed before the draw (temporal-integrity breach, AGENTS §2).
- Σpₙ ≠ 5, which silently breaks exposure matching and invalidates the flat comparison.
- Entrants added after early targets are seen (garden of forking paths; the entrant set must be frozen).
- Treating derived K13 numbers as confirmatory after demoting them to secondary.
- **Using draws 16–22 as verified evidence.** All seven carry `draw_method_unknown` / `machine_name_unknown`; draws 21–22 additionally carry `source_url_missing` and `user_reported_pending_external_verification`. Every number in this document depends on them: **all 19 proxy targets contain flagged rows in their history, and 7 of the 19 targets are themselves flagged rows.** This is the largest single threat to the census's validity.
- Interim peeking with continued sampling, which voids the fixed-stopping guarantee.

## 8. Minimal Protocol Amendments

**E0007:**

1. Pin Arm A to a named script + commit + seed (§3.4); until then the control arm is unreproducible.
2. Cut rescue seats from four to **one** (highest-margin dissenter), or to zero pending FCPC-13 — §3.1 shows four seats cost 0.368 winners/draw in proxy.
3. Delete the starvation rescue family (0 hits / 19 nominations).
4. Restate the 12-target falsification rule as "**no evidence**", never "rejected": powered only for Δ ≈ 0.7 (§1), a null there carries almost no information.
5. Retain Hypothesis B (mobility, Q017) as the primary surviving line.

**E0005:**

1. Add a slot-mass → 50-coordinate mapping, `p_n = Σ_slots P(slot occupies n)` normalized to Σ = 5. This is exactly the order-statistic marginal the structural null already computes, so it needs no new theory and lets E0005 enter FCPC-13 on the common estimand.
2. Replace the "majority of slots" falsification rule with a single draw-level paired score (five correlated slots are not five tests).
3. Pre-register the expected sparse-pooling firing rate; if BARP collapses to its pooled prior on >50% of bins, the arm is untestable in that window and should be deferred rather than run.

## 9. Falsification Rule

If after 20 prospective targets no entrant beats flat on paired mean log loss with Holm-adjusted p < 0.05 **and** a bootstrap CI excluding zero, classify the current acquisition feature set as carrying **no measurable incremental information**, deprioritize new ranking algorithms, and redirect effort to §11.

Symmetric commitment (required so the test can fail in both directions): if entrants are significantly **worse** than flat under the same criterion, that is a positive finding of anti-informativeness and obliges HEPS to shrink production candidate scores toward the exchangeable marginal rather than keep re-weighting them.

## 10. Orthogonal Breakthrough Finding

**None.** No transform passed the novelty test against existing recency / starvation / shadow / order-statistic state. §3.3 is the reason: candidate transforms kept resolving to the same short-horizon recurrence axis, and the one pair with zero overlap (recency/starvation) is an algebraic sign flip rather than an independent source.

Nearest miss worth recording: **pooling** is not a new information source but is the only operation observed to *reduce* damage relative to its constituents (§6).

Two inherited negative structural results are confirmed as still binding and should be cited before any new geometry-based compression claim: E0006's proof that under `NULL_GAP_DM` every legal six-gap composition is equiprobable and in one-to-one correspondence with a legal 5/50 line — so an exact-line HDR cannot isolate a high-probability subset — and the corollary that a fixed K22 carrying no genuine information still captures 5/5 with probability ≈1.243%. Both eliminate whole families of proposals cheaply.

## 11. Missing-Data Finding

Missing variable: **`machine_name` / `draw_method` for draws 16–22** — all `unknown`, whereas draws 1–15 carry `PB1` / `SIZWE` / `Khaya` with `mechanical_machine`.

Why this is the highest-value acquisition target:

- Machine/ball-set identity is the **only externally pre-specifiable partition** in the ledger. AGENTS §7 forbids scanning outcomes for a split point and presenting the best split as evidence; a sourced machine label is exempt because it is fixed independently of outcomes.
- It is the **sole variable that can convert a mechanical-bias hypothesis into a testable conditional**. Sorted order statistics cannot: they are a deterministic transform of the unordered draw and carry no information about the physical apparatus. Every current HEPS expert operates downstream of that transform, so none can test the bias hypothesis however it is re-weighted.
- The gap covers **7 of 22 rows (32%), all of them the most recent** — precisely the rows that dominate every recency-weighted model and every walk-forward target in the census.
- Cost is a lookup, not an experiment. Acquisition: backfill from a director-approved source, then **record prospectively at freeze time** so the gap cannot reopen.

Until this is backfilled, `scripts/check_stationarity.py` cannot condition on machine identity for a third of the active era, and the pooled-versus-conditioned comparison required by AGENTS §7 is unavailable for the most recent draws.

Secondary data finding: draws 21–22 remain `user_reported_pending_external_verification` with `source_url_missing`, yet are already load-bearing — draw 22 is the 2026-08-14 Physics-of-Failure target that motivated **both** E0005 and E0007. External verification of these two rows is a prerequisite for treating either experiment's motivating observation as evidence.

## 12. Recoverability and Provenance

- Reproduce every number: `python experiments/E0007/reproductions/fable5_acquisition_probe.py --json experiments/E0007/reproductions/fable5_acquisition_probe_results.json` (seed 20260817, stdlib only — numpy/scipy are not installed in this environment).
- The JSON artifact carries per-target detail — winners, per-rule log loss and Brier, K13 winners retained, all pairwise overlaps, core/displaced/rescue seat attribution, and quality flags — so later agents can re-derive or challenge any table above without rerunning the probe.
- The probe self-labels `authority: diagnostic_only` and `paper_trading_only: true`. It must not be cited as a frozen HEPS expert, an ensemble vote, or prospective evidence.
- Nothing in `data/`, `core/`, or any frozen cycle artifact was modified. No other model's experiment package was overwritten.

## 13. Final Classification

`INSUFFICIENT_EVIDENCE` overall for candidate acquisition.

Component classifications:

| Claim | Classification |
|---|---|
| Proxy acquisition rules carry incremental information beyond flat | `REJECT` (in proxy; all six significantly worse than flat) |
| E0007 Core9+Rescue4 improves winner survival at fixed K | `REJECT` (in proxy; −0.368 winners/draw, p = 0.015) |
| E0007 rescue families are orthogonal | `REJECT` (overlaps 4.95–7.58 vs 3.38 exchangeable) |
| K13 winner count is a decidable estimand in ≤20 targets | `REJECT` (Δ = 0.20 needs 173 targets) |
| E0007 Hypothesis B (coordinate mobility, Q017) | `INSUFFICIENT_EVIDENCE` — untested, retained |
| E0005 BARP / VVD-R | `INSUFFICIENT_EVIDENCE` — clean protocol, wrong estimand, underpowered |
| Pooling reduces damage relative to constituent rules | `PROVISIONAL_SIGNAL` (in proxy only) |
| Machine identity is the binding missing variable | `PROVISIONAL_SIGNAL` — structural argument, not yet tested |

`REJECT` entries above are rejections **of the proxy claim as measured**, and transfer to the corresponding HEPS experts by analogy, not by direct measurement. Only the K13 power result is model-free.

## 14. Confidence

**LOW-MODERATE**, unchanged from rev 1. Limiting factors:

- proxy rules are not frozen HEPS experts, so §3 and §6 verdicts transfer by analogy;
- 19 post-hoc targets over a 22-draw ledger;
- 7 of 19 targets rest on unverified user-reported rows;
- the §3.1 significance test was selected after inspecting the data and is unadjusted.

Raised relative to rev 1 on two points only: the arithmetic is now reproducible from a persisted seeded artifact, and the §1 power calculation is a closed-form combinatorial result independent of the proxy rules — it holds for *any* fixed 13-basket and is the most transferable finding in this document.

---

Search discipline: 4 proxy rules + 2 pools + flat null examined; no parameters tuned; no rule added or removed after seeing scores. The recommendation was **not** chosen by score — *all* families failed to beat flat, which is why the recommendation is an estimand change plus a data-acquisition action rather than a winning model.
