# ChatGPT Sol Contribution — Coalition Assembly Breakthrough

**Date:** 2026-08-01  
**Status:** accepted experimental HEPS v33.3 core synthesis improvement  
**Scope:** main-field coalition assembly after candidate discovery

## 1. Executive summary

HEPS repeatedly demonstrated a separation between **candidate discovery** and **coalition assembly**: expert systems could identify many or all eventual winning coordinates, yet the final line composer frequently dispersed those coordinates across different submitted lines.

The 2026-07-31 result exposed the failure clearly. The frozen 17-number candidate hierarchy contained all five eventual main winners:

`10, 11, 37, 45, 46`

The published pre-draw portfolio nevertheless assembled at most two of them on one line.

This contribution introduces the **Coulomb Pair-of-Pairs + Anchor Coalition Assembler**, a synthesizer-stage architecture that preserves expert provenance, constructs supported pair edges, combines two disjoint pairs around an anchor, and selects the final portfolio jointly for conditional coalition coverage.

## 2. Breakthrough diagnostic

Relative to the previous HEPS selector:

- previous published best overlap on 2026-07-31: **2/5** mains;
- retrospective graph-assembly line: `02,10,11,37,46` = **4/5** mains;
- exact winning line `10,11,37,45,46` was present in the generated pair-of-pairs + anchor challenger set;
- exact winning line ranked **19th among 417** generated challenger coalitions;
- winning topology is naturally represented as `(10,11) + 37 + (45,46)`.

The HEPS director has accepted this as a **breakthrough improvement in coalition assembly capability over HEPS v33.2**.

The evidence boundary remains explicit: these 4/5 and exact-line-rank findings are retrospective diagnostics. They justify the architecture change but do not prove a durable exact-win predictive edge.

## 3. Problem definition

Given a frozen candidate set `V`, individual candidate support is not enough. HEPS needs to estimate which candidates belong together.

Represent the assembly problem as a graph/hypergraph:

- nodes = main-number candidates;
- node attributes = expert scores, recurrence state, void age, register, sorted-slot fit;
- edges = supported candidate pairs;
- hyperedges = pair-of-pairs + anchor coalitions;
- final portfolio = jointly selected five-node hyperedges.

## 4. Algorithms tested

The research cycle tested:

1. individual-score ranking;
2. structural-likelihood ranking;
3. hybrid node + structure scoring;
4. role-constrained coalition scoring;
5. pair graphs;
6. dual-cluster / pair-of-pairs generation;
7. scenario-mixture scoring;
8. maximum-coverage portfolio selection.

A key negative result was that increasingly elaborate scalar line scores did **not** reliably outperform matched-random portfolios. This rejected the simplistic idea that assembly can be solved by merely adding more synergy terms to one averaged score.

The stronger result came from preserving expert interactions and treating final selection as a combinatorial portfolio problem.

## 5. Proposed synthesis topology

The primary line structure is:

`pair_A + anchor + pair_B`

Requirements:

- `pair_A` contains two distinct candidates;
- `pair_B` contains two distinct candidates and is disjoint from `pair_A`;
- `anchor` is distinct from all four paired candidates;
- each element retains expert provenance;
- dual-cluster layouts are allowed when structurally supported.

## 6. Pair evidence

A pair may receive support from:

- Coulomb temporal-void compatibility;
- stiction / ±1 / ±2 shadow structure;
- direct adjacency or compact spacing;
- stale-hot return-horizon logic;
- historical/structural pair bridging;
- sorted-position compatibility;
- cross-expert consensus;
- complementary expert roles.

A generic interaction score is:

$$E(i,j)=\alpha C_{void}+\beta C_{shadow}+\gamma C_{adj}+\delta C_{bridge}+\epsilon C_{consensus}+\zeta C_{role}-\rho P_{redundancy}$$

Coefficients must be calibrated without target leakage.

## 7. Anchor evidence

Prefer anchors that:

- are supported by several experts;
- exhibit stale-hot recurrence without requiring immediate repetition;
- bridge low/high or cluster structures;
- fit sorted-position expectations;
- reduce portfolio redundancy;
- connect two otherwise complementary pairs.

For 2026-07-31, `37` is the natural hot/consensus anchor linking the low pair `10,11` and high pair `45,46`.

## 8. Coalition score

For disjoint pairs `P_A`, `P_B` and anchor `a`:

$$Coalition(P_A,a,P_B)=E(P_A)+E(P_B)+A(a)+\eta X(P_A,a,P_B)-\kappa R(L)$$

where `X` measures cross-pair structural compatibility and `R` penalizes portfolio duplication.

The synthesizer must not penalize a line merely because two separated adjacent pairs coexist.

## 9. Portfolio-level optimization

The second improvement is to select the ten lines jointly rather than independently.

Track and maximize, subject to redundancy constraints:

- unique candidate exposure;
- unique supported-pair exposure;
- unique triple exposure;
- scenario/lane diversity;
- conditional 3+ and 4+ coverage;
- low duplication across submitted lines.

One chaos/random-control line remains outside the optimized selector.

## 10. Conditional coverage experiment

The research package includes a maximum-coverage optimizer and matched random baselines. When a frozen candidate pool already contains all five winners, optimized ten-line designs materially increase **conditional 3+ assembly coverage** versus ten random distinct lines.

Representative results:

- 18 candidates: approximately **78.99% optimized vs 64.66% random**;
- 17 candidates: approximately **86.26% vs 71.06%**;
- 14 candidates: approximately **99.55% vs 89.69%**.

These figures address 3+ coalition retention, not exact 5/5 prediction.

## 11. Exact 5/5 limitation

If every five-number subset of `n` candidates is equally likely and HEPS submits `k` distinct lines, then:

$$P(5/5)=\frac{k}{\binom{n}{5}}$$

Therefore coverage optimization alone cannot improve exact 5/5. Exact improvement requires validated non-uniform coalition evidence from the expert graph/hypergraph.

This limitation remains a mandatory red-team safeguard after architecture promotion.

## 12. HEPS v33.3 integration

The director has approved:

1. Pair-of-pairs + anchor becomes the preferred main-number synthesis method.
2. Expert identities are preserved through assembly.
3. At least three final lines are coalition-champion lines.
4. Final model-driven lines are jointly checked for maximum coverage and redundancy.
5. One chaos/random-control line remains mandatory.
6. Candidate recall and assembly performance are scored separately after every draw.
7. The previous independent-line selector remains a benchmark/control.

## 13. Final status

**ACCEPTED EXPERIMENTAL CORE MODULE — HEPS v33.3 COALITION ASSEMBLY BREAKTHROUGH.**

The architecture is promoted because it materially improves HEPS's ability to keep complementary candidates together when candidate discovery has already succeeded. Prospective/null validation continues before any claim of durable predictive advantage.