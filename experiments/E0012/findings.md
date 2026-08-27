# E0012 Findings — Gemini Contribution Audit

Evidence classification: `INSUFFICIENT_EVIDENCE`.

## 1. The revised SGCE is now a testable hypothesis, but strict W=50 has no eligible Main evidence yet

The director/Gemini supplied a concrete challenger specification on 2026-08-27: Jaccard pair weights, normalized spectral Laplacian, three-dimensional eigenspace, four k-means clusters, temperature `tau=0.5`, `K_core=10`, dynamic sum bounds and explicit static morphology constraints.

That is a major improvement in reproducibility over the original contribution.

However, the canonical Main ledger contains only 25 active-era draws through 2026-08-25. The challenger explicitly freezes `W=50` consecutive active-era draws. Therefore the strict frozen SGCE currently has **zero eligible Main targets**. Any use of fewer than 50 prior draws is a different partial-window model and receives zero confirmatory credit.

## 2. The written SGCE and supplied Python are two different algorithms

The written model specifies k-means clustering and node-to-assigned-centroid distance. The supplied Python does not run k-means, does not calculate centroid distance, and does not use `sigma_W`; it ranks nodes by standardized row norm of the three spectral eigenvectors.

The written model also leaves k-means initialization / `random_state` / `n_init` unfrozen. In exploratory replication, different seeds produced different Top-10 sets.

Until one implementation is selected and all stochastic settings are frozen, the two variants must be treated as distinct challengers.

## 3. Exploratory partial-window replay does not show a predictive acquisition edge

Because strict W50 testing is impossible at the current ledger size, an explicitly post-hoc exploratory replay was run using available prior history only.

For the supplied Python row-norm implementation across 17 targets:

- K10 captured 16 winner coordinates in total, mean `0.941` per target;
- exact-null expectation at K10 is `1.0` winner per target;
- simple frequency also captured 16 and simple recency 15;
- no 3+/5 K10 target occurred.

At K13 the row-norm SGCE captured 18 coordinates versus exact-null expectation `22.1` across the same 17 targets. At K18 it captured 25 versus exact-null expectation `30.6`.

For the written k-means/centroid interpretation, five tested random states produced K10 totals of `18,17,17,16,17`; the random exact-null expectation is 17. The best tested total is not statistically unusual at matched exposure.

These results do not reject every future W50 spectral model. They do reject any present claim that the revised SGCE has already demonstrated a predictive edge.

## 4. SGCE remains more natural as coalition evidence than candidate authority

Pair/co-occurrence topology directly concerns which coordinates associate with one another. That is naturally Stage 3 coalition information.

A graph expert may eventually earn candidate-funnel weight only if its coordinate-level residual score beats simple frequency/recency and exact matched-exposure controls prospectively. Spectral representation alone does not create predictive information.

A further structural caution remains: pair-graph degree and related spectral structure are coupled to marginal occurrence frequency. Any future SGCE must be residualized against frequency/recency before being counted as a separate information family under E0011.

## 5. The in-line filters are now reproducible, but no winner-retention edge is detected

Using the supplied current-window formulas as an exploratory geometry diagnostic, the combined sum/parity/decadal/max-gap filter retains about `46.44%` of all legal 5/50 lines.

The static parity/decadal/max-gap portion was satisfied by 15 of the 25 canonical active-era winners (`60%`) versus an exact-null legal-line retention rate of about `54.88%`; one-sided binomial `p≈0.380`. This is no detected winner-retention lift.

The individual static constraints are themselves broad:

- parity 2:3 or 3:2 retains about `65.13%` of legal lines;
- the supplied `floor(x/10)` three-bin rule retains about `93.53%`;
- max adjacent gap <=25 retains about `89.97%`.

Thus most compression currently comes from combining broad common-morphology rules, not from demonstrated predictive discrimination.

Applied only as an audit to the already-frozen 2026-08-28 HEPS portfolio using the current 25-draw sum band, the Gemini filter would retain 9 of 20 lines and delete 11. The frozen slate must not be changed after the fact.

## 6. `NULL_GAP_DM` still does not justify the max-gap filter

The rule `max adjacent gap <=25` is a legitimate morphology constraint to test, but it is **not** implied by `NULL_GAP_DM`.

Under the exact IID gap null, every legal six-component gap composition is equally probable. Therefore `NULL_GAP_DM` cannot label one legal composition invalid or intrinsically less null-valid than another.

Classification of the claimed `NULL_GAP_DM` filtering rationale: `REJECT`.

## 7. Dynamic K13..18 remains confounded by exposure

Exact matched-exposure geometry gives:

- K13: expected winners `1.3`, `P(3+)≈10.30%`, `P(5/5)≈0.0607%`;
- K18: expected winners `1.8`, `P(3+)≈24.13%`, `P(5/5)≈0.4044%`.

K18 therefore has about `6.66x` the exact-null 5/5 survival probability of K13 before predictive intelligence is added.

Exploratory macro-sum-volatility diagnostics still show no detected relationship strong enough to justify a volatility-controlled K expansion at this sample. Dynamic K may be researched, but it cannot be credited from raw recall.

## 8. Core + Rescue remains better posed at fixed total K

Gemini's motive—protecting tail/dissent coordinates—is valid as a research question, but E0007/E0009/E0011 already test it with cleaner exposure control: `Core13`, `Core12+Rescue1`, `Core11+Rescue2`.

`Core10 + Rescue6..8` changes total K to 16..18 and therefore mixes rescue quality with exposure expansion.

## Strongest counterargument

A true 50-draw spectral graph may behave differently from these short-window exploratory replays. Spectral clustering could detect residual community structure that raw pair persistence and expanding-window approximations cannot. For that reason SGCE should remain a live challenger rather than be permanently rejected.

## Recommendation

- Do **not** promote SGCE, adaptive K, or the morphology filters into production HEPS yet.
- Preserve the revised SGCE specification under E0012.
- Reconcile the written k-means model with the supplied row-norm Python implementation and freeze stochastic settings.
- Begin strict W50 scoring only once 50 prior active-era draws exist.
- If an earlier test is desired, preregister a separate `W=20` or expanding-window challenger rather than silently changing W50.
- Keep SGCE initially at coalition/shadow authority and require residualized incremental evidence before candidate-funnel promotion.
- Keep the frozen 2026-08-28 Main prediction unchanged.
