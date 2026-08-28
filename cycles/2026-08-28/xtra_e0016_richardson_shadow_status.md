# XTRA E0016 Richardson Shadow Ingestion Status — 2026-08-28

**Target:** 2026-08-28 PowerBall XTRA  
**Mode:** `paper_trading_only`  
**Expert:** `XTRA_RICHARDSON_PAIR_DISPERSION`  
**Architecture status:** `shadow`  
**Evidence:** `PROVISIONAL_SIGNAL`  
**Production weight:** `0`  
**Self-selected role:** XTRA quantitative auditor / candidate-acquisition integrator

## Intent

Ingest the director-approved E0016 Richardson residual pair-dispersion expert into the independent XTRA research lane while preserving temporal integrity, Main/XTRA isolation, fixed exposure, and the already-frozen 2026-08-28 incumbent prediction.

## Repository state reconstructed

The canonical XTRA manifest and ledger still end at:

`2026-08-21: 17,23,37,39,48 | PB2`

with 24 canonical rows.

The existing 2026-08-28 incumbent XTRA pre-draw artifact was frozen from a provenance-qualified working 2026-08-25 state:

`4,7,15,18,29 | PB16`

but that 2026-08-25 row is not yet canonical under `data/powerball_xtra_manifest.json`.

## 2026-08-28 Richardson integrity decision

**Do not create or score a target-valid E0016 Richardson candidate field for 2026-08-28 from the current canonical ledger.**

Reason:

1. E0016 requires only canonical XTRA draws strictly before the target.
2. Richardson is a one-step conditional pair-separation model whose current state must be the immediately preceding canonical XTRA draw.
3. The canonical ledger currently omits the intervening 2026-08-25 draw.
4. Using 2026-08-21 as the current state for a 2026-08-28 target would skip a draw and change the statistical target.
5. Importing the working 2026-08-25 row into E0016 without satisfying the manifest provenance rule would violate the frozen protocol.

Therefore no 2026-08-28 Richardson K13/K20 receives prospective league credit from this session.

## Incumbent preservation

The authoritative incumbent remains unchanged:

- primary HLR: `H,H,H,H,H | L`;
- flagship: `7,19,28,39,48 | PB10`;
- broad acquisition K25: `{5,6,7,11,12,16,17,18,19,20,21,23,27,28,29,31,32,35,39,40,43,45,46,48,50}`.

E0016 does not modify any of these outputs.

## Full-marginal integration prerequisite

A second integration requirement was identified: the existing 2026-08-28 incumbent artifact records directional probabilities, slot hierarchies, a broad K25 and lines, but not a complete normalized `P(S_j=n)` field for all five sorted slots.

For future E0016 targets, the incumbent XTRA cycle must freeze the complete five-slot marginal field **before** Richardson is run. This is required for an auditable 50/50 incumbent/Richardson blend.

If no incumbent full slot field is available, `scripts/physics_shadow_e0016.py` may use exact structural slot marginals only as a labelled standalone Richardson comparator. Such a structural-base output must not be mislabeled as an incumbent/Richardson blend.

## Future E0016 execution order

For the first target whose canonical ledger is verified through the immediately preceding XTRA draw:

1. freeze incumbent full HLR probability distributions;
2. freeze incumbent full VVD distributions;
3. freeze incumbent normalized slot marginals `P(S_j=n)`;
4. run E0016 with all ten pair separations, `h=5`, `kappa=8`;
5. store Richardson slot marginals and global 1..50 inclusion field;
6. freeze Richardson-only K13/K20;
7. freeze true 50/50 incumbent/Richardson blended K13/K20 at identical K;
8. preserve the production incumbent independently;
9. after result reveal, score mean winner rank, K13/K20 recall, 3+/4+/5 survival, catastrophic exclusion and per-winner helpful/neutral/harmful attribution.

## Pair-family and redundancy policy

E0016 v1 remains all-ten-pairs. No adjacent-only, long-span-only, lower-field or upper-field subset may replace it after a target result. Any reduced pair family must be a separately preregistered derivative.

Richardson residual dependence must be tested against `XTRA_HLR_SLOT`, `XTRA_VVD_DELTA`, `XTRA_SORTED_SLOT_DENSITY`, simple recency and simple frequency before authority can increase.

## PowerBall isolation

Richardson has zero XTRA PowerBall authority. E0015 conditional PowerBall residual convergence remains the separate PB shadow lane.

## Evidence interpretation

The E0016 replay is discovery evidence only. Richardson remains `PROVISIONAL_SIGNAL / shadow`; this status note creates no new predictive evidence and no retrospective credit.
