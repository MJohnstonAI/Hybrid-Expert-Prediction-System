# Red-Team Review: ChatGPT Sol Coalition-HEPS

**Reviewer posture:** external quantitative auditor  
**Date:** 2026-07-13  
**Reviewed proposal:** `workspace/contributions/contributor_chatgpt_sol_2026-07-13_coalition_heps.md`  
**Decision:** `hold_for_implementation_and_blind_evidence`

## 1. Overall assessment

The proposal addresses a real architectural weakness: HEPS can produce apparently diverse lines that remain highly correlated in register, sum, cluster location, and expert provenance.

The proposed separation of candidate discovery, coalition assembly, and final portfolio routing is methodologically stronger than evaluating only the best submitted overlap.

However, the proposal remains a design specification. It has not yet demonstrated predictive value.

## 2. Highest-value contributions

1. **Failure-stage decomposition** — candidate failure, assembly failure, and routing failure should be measured separately.
2. **Scenario preservation** — competing expert hypotheses should not be averaged away before line generation.
3. **Structural diversity** — portfolio correlation must include register and sum geometry, not only exact coordinate overlap.
4. **Provenance protection** — a PowerBall candidate cannot be counted as a main-number candidate; post-draw claims require frozen artifacts.
5. **Claims register** — preliminary conversational results are explicitly excluded from validated evidence.
6. **Matched-null requirement** — line constraints must also be represented in null simulations.

## 3. Critical risks

### 3.1 Tiny sample

The mechanical-era dataset contains only eleven canonical draws through 2026-07-07 on the current default branch. The proposed eight-target tournament has very low statistical power and high result variance.

No architecture should be promoted because it produces one or two 3-main results in this window.

### 3.2 Architecture designed after observing targets

Coalition-HEPS was formulated after discussing June and July outcomes, especially the 10 July low-register draw. A walk-forward replay remains retrospectively informed even when each target uses only earlier rows.

The architecture may be evaluated for internal consistency on the historical window, but only later frozen targets count as genuinely prospective evidence.

### 3.3 Multiple-hypothesis search

The proposal introduces many choices:

- feature definitions;
- age caps;
- distance weights;
- scenario lanes;
- pair and triple coefficients;
- role templates;
- candidate-pool sizes;
- portfolio quotas;
- structural-correlation weights.

Searching these options against eight targets would almost guarantee meta-overfitting. The experiment registry must record every tested variant, including unsuccessful ones.

### 3.4 Exact winning combination fallacy

If the exact 10 July winning combination appears anywhere in a large generated candidate universe, this is not operational success unless:

- the candidate universe size is reported;
- the line rank is reported;
- the submitted line limit is fixed;
- the selection rule was frozen before the result;
- equivalent random candidate universes are scored.

### 3.5 Unsupported physical interpretation

Coulomb, stiction, flow reversal, wall pressure, and fatigue must remain feature metaphors unless direct physical evidence is added. Number labels are not known chamber positions.

### 3.6 Portfolio expansion inflation

A 20-line expansion naturally has more opportunities than a 10-line core. Results must always retain their line-volume denominators and matched controls.

## 4. Minimum implementation gates

Before any performance claim, require:

- append and validate the 2026-07-10 draw;
- implement the proposed architecture in repository code;
- unit-test feature boundaries, duplicates, and target isolation;
- produce frozen JSON for every architecture and target;
- hash configuration and input-ledger state;
- preserve candidate, generated, and selected stages;
- run matched seeded null portfolios;
- publish aggregate and per-target reports;
- rerun from a clean checkout with one documented command.

## 5. Mandatory metrics

For each target and architecture:

```text
candidate_pool_size
candidate_capture_top_10
candidate_capture_top_15
candidate_capture_top_20
candidate_capture_top_25
oracle_candidate_overlap
best_generated_overlap
best_selected_overlap
lines_with_2_plus
lines_with_3_plus
lines_with_4_plus
lines_with_5
powerball_candidates_covered
same_line_3_plus_pb
same_line_4_plus_pb
submitted_line_count
matched_null_percentile
```

## 6. Required ablations

Run the full model and:

- minus temporal void;
- minus stale-hot;
- minus numerical bridge;
- minus exact stiction and shadows;
- minus pair affinity;
- minus triple affinity;
- minus minority-hypothesis coverage;
- minus structural-correlation penalty;
- without register-profile quotas;
- hot/high only;
- Coulomb only;
- unrestricted random;
- structure-matched random.

A feature should not be credited merely because the full architecture succeeds once.

## 7. Promotion criteria

The challenger may move to `experimental_active` only if:

1. the historical pipeline is reproducible;
2. it does not materially underperform the current champion on candidate recall;
3. any 3+ improvement survives matched-null analysis;
4. the improvement is not confined to the draw that motivated the architecture;
5. at least one future slate is frozen before its result;
6. no historical artifacts are regenerated after scoring;
7. the merge decision documents the number of variants explored.

## 8. Final verdict

Coalition-HEPS is a credible research direction because it targets an identifiable ensemble-design problem. It is not yet a validated prediction architecture.

**Recommendation:** implement as a challenger, preserve the existing champion, and prohibit promotion until reproducible and prospective evidence exists.
