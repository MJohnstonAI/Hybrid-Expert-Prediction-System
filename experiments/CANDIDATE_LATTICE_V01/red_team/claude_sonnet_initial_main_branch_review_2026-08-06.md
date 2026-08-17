# HEPS Red-Team Review — Candidate Lattice / HLR-VVD External Brief

> Provenance note: user-supplied external review from Claude (Anthropic), dated 2026-08-06. This was the first review and was later superseded on repository provenance by `claude_sonnet_rereview_2026-08-06.md` after it was established that the reviewer had inspected the `main`-branch state rather than `agent/ai-collaboration-restructure`. Its statistical objections remain part of the evidence record.

**Reviewer:** Claude (Anthropic)
**Date:** 2026-08-06

## Proposal Reviewed

An externally-supplied brief (no repo source path attached) proposing a 10-stage
"Candidate Lattice" architecture: Hard Slot Feasibility → mandatory HLR forecast
→ VVD movement feasibility → cross-slot constraint propagation → candidate
meta-lattice → safe exclusion → scenario-conditioned sub-baskets → coalition
assembly → morphology → winner-float ranking → portfolio optimization. The
brief references `governance/`, `core/expert_registry.yaml`,
`core/feature_dictionary.yaml`, `knowledge/`, `experiments/registry.csv`,
`experiments/CANDIDATE_LATTICE_V01/`, `experiments/REGIME_STATIONARITY_AUDIT/`,
`cycles/2026-08-07/`, PR #6, and branch `agent/ai-collaboration-restructure`,
and claims a "frozen 2026-08-07" prediction slate built from a previous draw of
`16, 24, 29, 34, 38` / PB `15` with a training cutoff of `2026-08-04`.

## Data Integrity Check

- **Latest verified ledger row available to this reviewer:** draw_id 13,
  `2026-07-14`, main `9, 13, 21, 36, 40`, PB `4`. `validate_draws.py` and
  `sync_manifest.py --check` both pass against this ledger.
- The brief's claimed previous draw (`16, 24, 29, 34, 38` / PB `15`, cutoff
  `2026-08-04`) does not appear anywhere in the ledger available to this
  reviewer. It cannot be confirmed as real, newer, or fabricated without
  access to the actual file.
- None of `governance/`, `core/expert_registry.yaml`,
  `core/feature_dictionary.yaml`, `knowledge/open_questions.md`,
  `knowledge/CANDIDATE_LATTICE_RESEARCH_GUIDE_2026-08-06.md`,
  `experiments/registry.csv`, `experiments/CANDIDATE_LATTICE_V01/`,
  `experiments/REGIME_STATIONARITY_AUDIT/`, or `cycles/2026-08-07/` are present
  in the repository state supplied for this review.
- **Recommendation:** confirm provenance of this brief and reconcile any
  claimed newer draws with the canonical ledger via the existing validators
  before treating any of its retrospective claims as evidence.

## Methodology Check

- **Walk-forward?** Partially. The brief itself labels its 3-target HLR-vector
  rank result (3/243, 8/243, 8/243) as non-confirmatory because the
  architecture was reportedly built after seeing those results. That
  self-flagging is correct and should be preserved, not softened later.
- **Target leakage risk:** high by construction. A 243-cell HLR vector space
  crossed with a 7-point basket-size sweep and a 10-stage pipeline is a very
  large hypothesis space to evaluate against what is, at most, a handful of
  new draws beyond the verified 13-row ledger.
- **Baseline included?** The brief calls for random/recency/order-statistic
  baselines but does not supply results against them in-document. See the
  independent check below, run against the verified ledger.
- **Sample size adequate?** No. At most ~13–18 mechanical-era rows exist in
  any version of this ledger this reviewer can verify. That is not enough
  data to support a 243-state joint model or a 7-point basket sweep without
  the results being dominated by post-hoc selection.

## Statistical Concerns

An independent walk-forward check was run against the actual 13-row ledger
(`min_train=3`, 10 held-out targets). Two naive candidate-basket heuristics —
top-K by raw frequency and top-K by recency of last appearance — were compared
against the exact random-basket expectation. Under exchangeability, for any
*fixed* basket of size K, P(a uniformly random 5-number draw is fully
contained in that basket) = C(K,5) / C(50,5), regardless of how the basket was
chosen — this is the correct null, not a simulation approximation.

| K  | method   | mean overlap | expected overlap | 5-of-5 | 4-plus | exp. P(5/5) | exp. P(4+) |
|----|----------|-------------:|------------------:|-------:|-------:|------------:|-----------:|
| 13 | freq     | 1.30 | 1.30 | 0 | 0 | 0.0607% | 1.309% |
| 13 | recency  | 1.10 | 1.30 | 0 | 0 | 0.0607% | 1.309% |
| 16 | freq     | 1.50 | 1.60 | 0 | 0 | 0.2062% | 3.127% |
| 16 | recency  | 1.70 | 1.60 | 0 | 0 | 0.2062% | 3.127% |
| 18 | freq     | 1.70 | 1.80 | 0 | 0 | 0.4044% | 5.026% |
| 18 | recency  | 2.00 | 1.80 | 0 | 1 | 0.4044% | 5.026% |
| 20 | freq     | 1.90 | 2.00 | 0 | 0 | 0.7317% | 7.592% |
| 20 | recency  | 2.40 | 2.00 | 0 | 1 | 0.7317% | 7.592% |
| 22 | freq     | 2.30 | 2.20 | 0 | 1 | 1.2429% | 10.910% |
| 22 | recency  | 2.50 | 2.20 | 0 | 1 | 1.2429% | 10.910% |
| 25 | freq     | 2.70 | 2.50 | 0 | 2 | 2.5076% | 17.434% |
| 25 | recency  | 2.60 | 2.50 | 0 | 1 | 2.5076% | 17.434% |
| 30 | freq     | 3.00 | 3.00 | 0 | 3 | 6.7259% | 32.595% |
| 30 | recency  | 2.90 | 3.00 | 0 | 2 | 6.7259% | 32.595% |

**Both heuristics track the random-basket expectation almost exactly at every
K tested.** Zero 5-of-5 captures anywhere, consistent with expectation given
per-draw odds of 0.06%–6.7% over only 10 trials. Observed 4-plus counts land
within one of theoretical expectation in every row. This is a clean null,
consistent with every other HEPS family tested to date (Coulomb Void,
Coulomb Stiction/Shadow — 9 sub-features, BH-corrected — and the dual-synergy
lab).

The brief's core combinatorics (C(13,5)/C(50,5) ≈ 0.0607%, C(18,5)/C(50,5) ≈
0.4044%, ≈6.66× ratio) is arithmetically correct, but describes only how much
coverage a larger *random* basket buys — not evidence that any selection
method (frequency, recency, or the proposed HLR/VVD/lattice stack) can
identify which specific numbers belong in a smaller one. The brief
acknowledges this in passing ("simply reducing one random 18-basket to one
13-basket loses that advantage") but the machinery proposed to recover the
advantage has not, on the data actually available, been shown to beat the
naive baselines above.

The 243-way HLR flow-vector ranking is being fit and evaluated against
approximately 3 labeled examples per the brief's own numbers. This has
essentially no statistical power. The brief's own INSUFFICIENT_EVIDENCE
labeling of this component should be treated as final, not as a launching
point for further build-out, until a materially larger labeled sample or a
strict pre-registration protocol exists.

## Engineering Concerns

- The proposed 10-stage pipeline is substantially more complex than anything
  in the currently accepted architecture. Complexity is a direct cost here:
  every additional stage is another place for post-hoc parameter selection to
  enter, and each stage needs its own leakage-safe walk-forward test before
  the next stage can be trusted to sit on top of it.
- Recommend testing for *any* departure from uniformity first, using the
  diagnostics that already exist (`algebraic_sequence_features.py`: chi-square
  gap fit, Markov fit, entropy, autocorrelation reports) before investing in
  another candidate-selection layer. If those diagnostics stay null on the
  current ledger, no downstream selection architecture — Candidate Lattice or
  otherwise — has a foundation to build on.
- If `governance/`, `core/expert_registry.yaml`, and `experiments/` genuinely
  exist in the live repository, they represent a structural migration away
  from what `AGENTS.md` and `configs/agent.md` currently describe. A change of
  that size needs its own contribution + red-team + merge-decision cycle per
  `configs/agent.md` §5, not to arrive as a side effect of a candidate-
  discovery proposal.

## Decision

- [ ] Accept
- [ ] Reject
- [x] Rework — insufficient evidence; requires provenance confirmation and
      re-testing against the verified ledger before further architectural
      investment

## Conditions for Merge

1. Confirm the source and provenance of this brief and reconcile every
   referenced repo path against the actual repository state.
2. Re-run its core claims (HLR-vector ranking, VVD feasibility pruning)
   against the verified ledger with explicit random-basket and recency-basket
   controls, following the pattern demonstrated in this review.
3. Do not introduce `governance/`, `core/expert_registry.yaml`, or
   `experiments/` restructuring without a dedicated contribution + red-team +
   merge-decision cycle.
4. Do not treat the "frozen 2026-08-07" slate as reviewable or actionable
   until the underlying file is confirmed to exist and its target-draw
   grounding matches the canonical ledger.
5. Any future basket-size or HLR/VVD experiment should be pre-registered
   (candidate basket frozen and hashed before the target draw), given how
   easily post-hoc search reproduces apparent structure in a 13-row sample.

## Notes

This review does not dispute that cross-slot constraint propagation and
coverage-optimized portfolio assembly are legitimate combinatorial
techniques in general. The concern is narrower: on the only data this
reviewer can verify, they have not been shown to outperform a naive
frequency or recency basket, and the proposal's internal structure (243-way
search, 7-point basket sweep, 10-stage pipeline) creates far more researcher
degrees of freedom than the ~13–18 available draws can support without a
pre-registration discipline stricter than what is currently described.
