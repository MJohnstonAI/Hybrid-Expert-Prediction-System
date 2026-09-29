# Main terminal-digit audit

Intent: independent data-quality auditor and quantitative tester. User source is read-only; no core, ledger, frozen cycle, or architecture changes. Classification pending evaluation; authority requested: diagnostic only.

Hypothesis: Main terminal-digit marginals or previous digit sum improve next-draw probability beyond exact uniform legal 5/50 geometry and simple shrunk frequency. Source workbook is reconciled to the canonical ledger before chronological evaluation. No pre-June data or PB digits enter Main fitting.

Discovery-only sequential replay, not untouched or prospective validation. Evaluate both the matched workbook subset and the complete active ledger separately, never pool these overlapping samples as independent evidence. First eight draws initialize each replay. Targets use earlier observations only.

Predeclared models: sum frequency (20 prior-draw equivalents toward exact sum null); rolling-eight sum frequency (same shrinkage); sum transition conditioned on previous sum <=17, 18..27, >=28 (20 prior-transition equivalents toward exact null); adaptive absolute-sum-delta residual (20 prior-transition equivalents, exact previous-sum-conditioned null, normalized over legal next sums). Score mean negative log probability of observed sum and resulting complete legal line (uniform within sum); compare all four arms and exact null. No hyperparameter selection. Slot digit diagnostics: unconditional and previous-same-slot-digit conditional counts, 20 prior-draw equivalents toward exact slot digit null; score marginal log loss only, never multiply into a joint field.

Diagnostics: aggregate digits, sum mean/variance, lags 1..5; 20,000 chronological permutations for maximum absolute sum autocorrelation and maximum standardized count over all contiguous three-wide LDSAD bands 0..2 through 43..45. This limited correction does not account for HEPS's historical broader searches. Fixed historical 11..13 band reported separately; one new target since its original freeze is not independent rediscovery.

Falsification: non-positive mean log-score gain fails this replay gate. Positive gain alone cannot promote with this sample/search. Minimum effect of interest 0.02 nats/draw; future horizon must be sized using observed paired variance (rough independent approximation n=((1.96+0.84)*sd/0.02)^2), adjusted for serial dependence and multiplicity. No fixed short horizon claimed adequate. No K13 or downstream lift claim is attempted unless full-field evidence warrants further research.
