# HEPS Red-Team Review - Candidate Discovery and Coalition Engine

## Proposal reviewed

`workspace/contributions/contributor_gpt56_sol_candidate_discovery_and_coalition_engine.md`

## Data and leakage check

- Canonical ledger validated at 13 rows through `2026-07-14`.
- Manifest check and required 100,000-trial null passed.
- Each of 10 historical targets used only earlier rows.
- Reliability updates occur after target scoring.
- Synthetic leakage rejection is tested.

## Statistical objections

1. The model constants were designed after viewing the era ledger. Target-row
   exclusion does not make the results prospective.
2. The combined candidate engine is not better than uniform rank and is weaker
   than recency-only on the most useful Top-20 diagnostic.
3. Selecting K=20 after K=15 failed would be meta-overfit if its historical
   performance were claimed as validation. K=20 may be frozen only as the next
   assembly-opportunity tier.
4. Assembly has only three eligible historical targets at K=20. Zero successes
   supplies negative evidence but cannot precisely estimate effect size.
5. The 1/4/16 threshold weights, temperature, and mixture constants are
   decision utilities, not learned or calibrated probabilities.
6. PB Top-3 `5/10` was found inside the same small search environment and is not
   a promotion case.
7. Degree-preserving swaps maintain the intended invariants, but finite-chain
   mixing was not formally established. Any future positive tail result needs
   multiple-chain convergence or an exact conditional sampler.

## Interaction audit

Pair-of-pairs and triple learning is correctly disabled. Six repeated pairs and
zero repeated triples are insufficient; the most repeated pair has adjusted
value `1.0` after the 1,225-pair search.

## Engineering review

- The experimental script reuses current expert generators and leaves accepted
  architecture files unchanged.
- Degree-preserving swaps retain candidate exposures and unique line counts.
- The research harness is relatively large, but keeping it separate avoids
  silently changing the accepted `portfolio_orchestration.py` selector.
- The complete JSON output retains per-target evidence and denominators.

## Decision

- [x] Accept as provisional research and measurement infrastructure
- [ ] Accept candidate predictive improvement
- [ ] Accept coalition predictive improvement
- [ ] Replace core allocation or current production selector

## Conditions for reconsideration

Freeze one model version for 20 future targets, preserve every pre-draw artifact,
and use K=20/10-line exposure-matched assembly reward as the primary endpoint.
Do not tune after individual failures.
