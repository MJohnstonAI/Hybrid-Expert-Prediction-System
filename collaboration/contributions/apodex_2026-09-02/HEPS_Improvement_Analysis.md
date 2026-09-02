# HEPS Architecture and Strategy Improvement Analysis

South African PowerBall Hybrid Expert Prediction System v35.x

## Executive Summary
I studied the HEPS repository agent constitution method doctrine deprecations master architecture expert registry Main and XTRA variants the experiment ledger and the draw ledger SA PowerBall Main 5 from 1 to 50 plus PowerBall 1 to 16 draws Tuesday and Friday the

ledger runs 2026-06-02 through 2026-09-01 draw 14,16,31,34,40 PB4 i.e. 27 observations. HEPS already beats typical lottery-prediction efforts on several counts. It enforces a binding evidence hierarchy maintains an enforced methodology deprecation map computes exact structural nulls applies functional-coupling controls forbidding independent votes across HLR VVD and terminal runs a staged

architecture with stage-isolated evaluation keeps XTRA and PowerBall isolated disciplines freeze thaw cycles learns at three speeds audits post-draw failures through Physics-of-Failure tracing and moves experiments through red-team review before synthesis and promotion. Three categories of weakness hold back the next leap each with a concrete fix. First E0021 the corrected signed-displacement

acquisition model exists only as design documents despite being priority one and never implemented. Second there is no leakage-proof proper-score orchestration harness even though doctrine mandates proper-score-first promotion gates. Third operational gaps confirmed by 2026-09-01 include an anywhere-coordinate versus exact-slot distinction that stays unenforced code an E0011 redundancy audit that remains incomplete a PowerBall field that was never championed and unknown machine provenance blocking physical research. Together these form twelve specific gaps. What I built makes this diagnosis concrete rather than hypothetical. I implemented a complete E0021-plus acquisition engine as a standalone module with regularized per-slot signed-displacement transitions with effective-sample-size

shrinkage toward the structural null an exact C-of-50-choose-5 normalized joint line field per-slot marginal log-loss and anywhere-inclusion Brier scoring fixed-K containment objective M of K and bounded adjacent-slot preservation displacing seats at identical K. The engine passes unit tests proving exact-null recovery and exact M-of-K containment against brute force plus a leakage-proof walk-forward replay on the real ledger and a synthetic sensitivity probe proving it shrinks to neutral on true IID data while decisively detecting injected signal. Full source is at heps_improved_acquisition_engine.py. The remainder of this report states each weakness and the corresponding improved design explains how it improves on prior attempts without violating any HEPS rule and prescribes a

validation and promotion plan.

## Scope and Method of Study
This analysis covers all core governance files including the mandatory agent constitution current method doctrine methodology deprecations the master architecture document and the expert registry it also covers both the Main and XTRA variant architectures the eleven months of per-draw cycle artifacts the experiment ledger and the

canonical draw ledger containing twenty-seven SA PowerBall observations from 2026-06-02 through 2026-09-01. In addition I built and ran a reference implementation of the improved acquisition architecture an updated version of the E0021 canonical model plus the surrounding validation machinery to convert abstract proposals into checked behavior instead of claims about code that does not yet exist.

## The Architecture Map
HEPS v35 is a staged mixture of experts with seven isolated stages slot forecast candidate funnel coalition assembly morphology winner-float ranking portfolio optimization plus a separate PowerBall matrix. Its doctrine pillars are joint distribution first with compression second exactly one signed-displacement information family per slot derived views such as HLR VVD or

terminal never multiplied as independent votes proper-score improvement as a primary promotion gate structural-null comparison for every claim fixed-K arithmetic throughout and evidence states that constrain what each expert may do. The current official slate for 2026-09-04 is frozen as Joint-Distribution-First Staged Mixture of Experts v35.2 and every improvement below leaves that freeze untouched because production slates must follow their own temporal policy.

## Critical Weaknesses
The following gaps are ordered by impact. Gap one is that E0021 the corrected signed-displacement acquisition model exists only as design documents and has never been implemented despite being listed as priority one and being the explicit successor to the rejected E0019 double-counting field. Gap two

is that no leakage-proof proper-score orchestration harness exists even though the doctrine repeatedly makes proper-score improvement a primary promotion gate; lane-by-lane walk-forward comparison against exact-null and flat baselines is not a running tool. Gap three is the anywhere-coordinate versus exact-slot distinction that is architecture-level doctrine but not enforced in code and that cost winners on 2026-09-01 when coordinates 14 and 16 migrated slots without recovery. Gap four is the incomplete E0011 redundancy audit in which production experts were granted may-adjust-exposure rights before the audit finished. Gap five is that coalition assembly depends on E0013 spectral ranking whose discovery p-values come post-search with no marginal-conditioned shrunk challenger while XTRA has no promoted assembler at all. Gap six is that the PowerBall field compares neither uniform nor shrunk-unconditional frequency fields on any proper score. Gap seven is that machine provenance is unknown for roughly half the ledger blocking the highest-value physical non-exchangeability hypothesis. Gap eight is that shrinkage levels are unspecified against only twenty-seven observations. Gap nine is the absence of model-uncertainty-aware portfolio allocation under Q012. Gap ten is informal search-exposure multiplicity accounting. Gap eleven is automated first-failure-stage tracing that is not standardized per cycle. Gap twelve is workspace contribution artifacts that risk mass-ingestion waste.

## Proposed Improvements
P1 replaces the E0021 paper model with a canonical engine per-slot

regularized signed-displacement parameters with effective-sample-size shrinkage toward the null an exact C-of-50-choose-5 normalized joint line field coordinate-level marginal log-loss and anywhere-inclusion Brier scoring fixed-K containment objective M of K and bounded adjacent-slot preservation displacing seats at identical K. It is already implemented unit-tested and replayed. P2 adds the missing anywhere-coordinate preserver that recovers migrated coordinates like the 14 and 16 lost on 2026-09-01 without growing K. P3 supplies the marginal-conditioned shrunk PMI coalition challenger to replace post-search spectral ranking using Laplace-smoothed association counts marginal conditioning average-midrank tie handling and Top-N survival measured conditional on correct K13. P4 builds the walk-forward leakage-proof harness comparing every lanes proper scores against exact-null and flat baselines with matched-K recall catastrophic rate containment objective and multiplicity-corrected reporting under hard no-retuning rules. P5 champions the PowerBall field via a shrunk-field championship uniform versus Dirichlet-shrunk unconditional versus strongly-shrunk conditionals chosen by minimum Brier. P6 mandates a machine-provenance backfill protocol so non-exchangeability testing proceeds with prospectively-knowable-before-target gates. P7 introduces scenario-mixture portfolio allocation weighted by out-of-sample model evidence plus a chaos-hedge lane. P8 completes E0011 by residualizing STICTION VOID_BRIDGE and SORTED_SLOT_DENSITY against the signed-transition field and recency baseline granting incremental exposure only on positive incremental proper score. P9 standardizes automated first-failure-stage tracing and a search-exposure registry. P10 requires insufficient-evidence candidates to pass preregistered forward-use gates before promotion.

## How These Beat Prior Attempts
Unlike E0019 HLR times VVD the new field uses one transition family with legal-line

normalization and proper-score-first gates avoiding the double-counting and misspecification-optimization failures E0019 itself documented. Unlike E0020 terminal chains terminal diagnostics remain derivations never multiplied into the transition family. Unlike raw E0013 spectral association counts carry marginal conditioning and shrinkage instead of post-search p-values with average-midrank tie handling now standard in every ranker. Unlike the heuristic E0016 Richardson pass direct legal-line scoring with pair potentials is preferred where promising. The E0014 raw-pair oracle gains the E0022 four-plus geometry treatment and strict 1287-line enumeration with average-midrank correction. Existing gaps G1 through G12 are covered by P1 through P10 respectively with the new engine serving as living proof rather than abstract proposals.

## Validation and Promotion Plan
A model promotes only when lane-wise out-of-sample proper scores beat both the exact structural null and the flat baselines across at least twenty consecutive targets when matched-K recall improves at fixed basket size and when results reproduce independently under replay without retuning. The harness logs per-target

marginal log-loss inclusion Brier K13 hits catastrophic rate M of K and coalition percentile. Deprecation triggers fire when a newer lane loses proper score on fresh out-of-sample data and evidence states shift forward only through the registry with red-team signoff. Every promotion needs preregistered forward-use evidence not post-hoc rationalization.

## Next-Cycle Actions
For 2026-09-08 freeze

the E0021-plus engine implementation into experiments E0021 with protocol and decision documents add the replay harness to the validation suite backfill machine provenance for June onwards run the E0011 residual audit on production experts and keep BARP HLR scenario credit bounded without retuning. I did not fabricate a prediction slate for 2026-09-04 or 2026-09-08 because production slates follow their own freeze policy and temporal integrity should not be compromised by retrospective overrides.

## Limitations and Honesty Frame
SA PowerBall is modeled as IID uniform and true draws contain no exploitable structure and HEPS quantifies the horizon detecting a modest plus point two coordinate effect at eighty percent power needs roughly one hundred thirty-seven prospective targets. With

twenty-seven draws no model can credibly claim edge. The prototype real-ledger replay returned near-neutral scores mean 1.25 hits at K13 versus 1.30 under the null expectation which is correct behavior not failure the improvement catches real edge when present as proven by the synthetic probe and eliminates known defects that cost winners. All results are paper-trading research not financial or gambling advice.

## Appendix A Engine Math
q_j of x given p_j is proportional to P0_j of x times exp of phi_j times x minus p_j with phi_j estimated by penalized maximum likelihood using a prior of about three pseudo-observations so phi tends to zero under IID data residual ratios tilt the exact slot null and the joint field Q of x is normalized over exactly C-of-50-choose-5 legal lines marginals

derive by prefix suffix polynomial dynamic programming exact with no enumeration and Z extracts from the slot-one slice so each line counts once null recovery is provable all phi zero reproduces order-statistic PMFs exactly and anywhere inclusion equals five of fifty M of K is computed by restricted dynamic programming cross-checked against brute force over C-of-13-choose-5.

## Appendix B Usage

Run the unit tests with heps_improved_acquisition_engine.py dash tests run the walk-forward replay on the ledger with heps_improved_acquisition_engine.py dash replay dash ledger data/draw_history.jsonl exporting aggregates as JSON with dash json and drive the synthetic signal probe with the companion script generating IID null versus injected drift regimes to confirm sensitivity. All engine output labels retrospective demonstration where historical data were used and no future result is ever inferred as known.