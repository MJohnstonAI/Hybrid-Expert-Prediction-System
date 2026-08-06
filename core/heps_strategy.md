# HEPS STRATEGIC COMPENDIUM & COGNITIVE SPECIFICATION

This document serves as the authoritative mathematical and semantic reference for autonomous HEPS agents. It defines the active expert lanes and the synthesis protocol used to combine their outputs into final prediction slates.

---

## 1. Expert Roster & Strategy Specifications

### Lane 1: The Coulomb Void Starvation Engine (`expert_void_bridge`)

**Core principle:** Track prolonged numerical absence and under-filled regions as temporal/spatial starvation features.

For a number `x` with starvation interval `t_x`:

$$C(x) = 1 - e^{-\lambda t_x}$$

This is a research score, not proof that an overdue number becomes intrinsically more likely in a fair draw.

**Behavioral role:** nominate deep-void, unseen, canyon-fill, and bridge candidates for the coalition synthesizer.

### Lane 2: The Kinetic Inertia & Step Drift Tracker (`expert_stiction_shadow`)

**Core principle:** Track exact repeats and local ±1/±2 numerical shadows around recent winning coordinates.

A simple displacement diagnostic is:

$$V_t = X_t - X_{t-1}$$

Sorted values are order statistics, not physical draw order. This lane is therefore treated as a numerical-neighborhood feature rather than proof of a physical trajectory.

**Behavioral role:** nominate exact-repeat and local-neighbor candidates and provide pair-edge support when two candidates form a credible local coalition.

### Lane 3: Sorted-Position Momentum (`expert_sorted_momentum`)

**Core principle:** Model historical distributions for sorted Slot1–Slot5 order statistics and reject or penalize structurally implausible line geometries.

**Behavioral role:** provide slot-compatibility evidence and identify anchors/bridges that make a pair-of-pairs coalition structurally coherent.

### Lane 4: The Tri-Cluster High-Register Engine (`expert_tri_cluster_high`)

**Core principle:** Track empirical clustered/high-register structures without treating them as mandatory.

**Behavioral role:** generate cluster candidates and pair structures, especially when multiple supported high-register coordinates can coexist in the same line.

### Lane 5: The Randomized Control Baseline (`expert_chaos_hedge`)

**Core principle:** Represent filtered lottery entropy and protect the research program from confirmation bias.

**Behavioral role:** produce one mandatory control line that bypasses the optimized coalition synthesizer.

### Supporting feature: Stale-Hot / Return-Horizon Expert

A candidate may receive support when it has both:

- sufficient historical recurrence to avoid being a pure one-off frequency artifact; and
- a meaningful but capped absence interval.

This feature is particularly useful for identifying "rested" anchors and should be kept distinct from pure cold/overdue logic.

---

## 2. HEPS v33.3 Synthesis Protocol — Coulomb Pair-of-Pairs + Anchor

### 2.1 Architectural objective

The previous HEPS synthesizer could identify strong candidates but frequently failed to keep complementary winners together on the same final line. HEPS v33.3 changes the synthesis problem from:

> rank individual five-number lines independently

into:

> preserve expert provenance, identify supported pairs/hyperedges, assemble coherent pair-of-pairs coalitions, and select the final portfolio jointly.

The primary synthesis topology is:

$$L = P_A \cup \{a\} \cup P_B$$

where:

- `P_A` is a supported two-number pair;
- `P_B` is a second supported pair disjoint from `P_A`;
- `a` is a compatible anchor not contained in either pair.

This creates a five-number coalition with explicit expert attribution.

### 2.2 Pair construction

For candidate pair `(i,j)`, calculate a soft interaction score from available evidence:

$$E(i,j) = \alpha C_{void} + \beta C_{shadow} + \gamma C_{adj} + \delta C_{bridge} + \epsilon C_{consensus} + \zeta C_{role} - \rho P_{redundancy}$$

where the terms represent normalized evidence from:

- void / temporal-starvation compatibility;
- stiction or ±1/±2 shadow support;
- adjacency / short-span geometry;
- historical or structural bridge evidence;
- cross-expert agreement;
- complementary expert roles;
- redundancy penalties.

The exact coefficients remain calibration parameters. Agents must not tune them on the target draw being evaluated.

### 2.3 Anchor selection

An anchor is a candidate capable of linking two pairs into one structurally coherent line. Prefer anchors with one or more of:

- cross-expert consensus;
- stale-hot return-horizon support;
- strong historical recurrence without immediate over-concentration;
- sorted-position compatibility;
- midfield or register-bridge function;
- low redundancy across the existing portfolio.

### 2.4 Coalition score

For disjoint pairs `P_A`, `P_B` and anchor `a`:

$$Coalition(P_A,a,P_B) = E(P_A) + E(P_B) + A(a) + \eta X(P_A,a,P_B) - \kappa R(L)$$

where:

- `A(a)` is anchor evidence;
- `X` rewards cross-pair complementarity and valid line geometry;
- `R(L)` penalizes excessive portfolio duplication, not merely local clustering.

A dual-cluster line must **not** be rejected solely because it contains two adjacent or compact pairs. The 2026-07-31 winning topology `(10,11) + 37 + (45,46)` demonstrates why the architecture must allow two separated pair clusters joined by one anchor.

### 2.5 Expert-preserving synthesis

Do not average all experts into a single number score before assembly. Preserve three classes:

1. **Consensus candidates** — supported by multiple experts.
2. **Specialist candidates** — strongly supported by one expert, such as Coulomb void.
3. **Coalition candidates** — individually moderate but strongly compatible as a pair or pair-of-pairs structure.

Each candidate line must retain the expert provenance for both pairs and the anchor.

---

## 3. Maximum-Coverage Portfolio Selection

HEPS v33.3 does not simply take the ten highest independently scored coalitions. It selects the portfolio jointly.

The optimization objective is to maximize useful candidate interaction coverage while controlling redundancy. At minimum track:

- unique candidate count;
- unique supported pairs;
- unique triples;
- overlap between submitted lines;
- scenario / expert-lane diversity;
- estimated 3+ and 4+ conditional coverage.

The existing `scripts/coalition_cover_optimizer.py` is the reference research implementation for this family of selectors.

### Conditional coverage finding

When a frozen candidate pool already contains all five eventual winners, research found that optimized 10-line designs can materially improve the chance that at least three winning candidates are kept together relative to ten random distinct lines. This is an assembly/coverage improvement only.

If every five-number subset has equal posterior probability, exact 5/5 probability remains proportional only to the number of distinct submitted lines. Therefore exact-win improvement requires genuinely informative pair/coalition evidence, not coverage optimization alone.

---

## 4. Breakthrough Diagnostic — 31 July 2026

Actual main result:

`10, 11, 37, 45, 46`

The frozen pre-draw 17-number HEPS candidate hierarchy contained all five winners, but the previous published final portfolio assembled at most **2/5** on one line.

The new coalition research produced:

- retrospective graph line `02,10,11,37,46` = **4/5** main hits;
- exact winning line `10,11,37,45,46` present in the pair-of-pairs + anchor challenger set;
- exact winning line ranked **19th of 417** generated coalition challengers;
- winning structure represented naturally as `(10,11) + 37 + (45,46)`.

HEPS therefore recognizes this work as a **breakthrough improvement in coalition assembly capability over the previous synthesizer**.

Evidence boundary: these assembly diagnostics are retrospective. They justify the architectural change, but they do not prove a durable prospective lottery-prediction edge.

---

## 5. Final 10-Line Portfolio Blueprint

The expert lanes still create diverse evidence, but the final portfolio is now synthesized through the coalition layer.

| Final ranks | Line class | Purpose |
|---|---|---|
| **1–3** | `pair_of_pairs_anchor` | Highest-supported cross-expert pair-of-pairs coalitions |
| **4–5** | `void_led_coalition` | Preserve Coulomb temporal-void / unseen candidate evidence |
| **6–7** | `tri_cluster_coalition` | Preserve clustered / high-register hypotheses |
| **8** | `stiction_or_sorted_coalition` | Preserve local shadow or order-statistic structure |
| **9** | `maximum_coverage_coalition` | Add the line with highest marginal pair/triple coverage |
| **10** | `chaos_hedge` | Mandatory matched-random / filtered-random control |

The chaos line must not be optimized by the coalition model.

---

## 6. PowerBall Synthesis

Matrix B remains separate from Matrix A. Current research features may include:

- recurrence / frequency support;
- return horizon / capped absence;
- stale-hot compromise;
- exact repeat and ±1/±2 shadow;
- low/high register hedge;
- circuit-breaker logic.

A PowerBall ranking must still be compared against the 1/16 uniform null. A correct top-ranked PowerBall is a prospective success event, not by itself proof of predictive edge.

---

## 7. Required Prediction Artifact Fields

Every prediction artifact must include:

- target draw date;
- ledger cutoff date;
- architecture version;
- candidate hierarchy;
- candidate expert provenance;
- generated pair set or summary;
- top pair-of-pairs + anchor challengers;
- final ten submitted lines;
- pair A, pair B and anchor rationale for coalition lines;
- coverage / redundancy diagnostics;
- PowerBall ranking;
- mandatory chaos-control line;
- `paper_trading_only` status.

---

## 8. Post-Draw Attribution Protocol

Score the system in this order:

1. **Candidate discovery:** how many actual winning mains were in the frozen candidate pool?
2. **Pair discovery:** how many actual winning pairs were represented by supported edges?
3. **Coalition generation:** did any generated challenger contain 3+, 4+ or 5 winners?
4. **Portfolio selection:** did the final ten retain the best generated coalition?
5. **PowerBall:** was the PB ranked and/or selected correctly?
6. **Null comparison:** how does cumulative performance compare with matched random controls?

Failure labels:

- candidate failure;
- pair-edge failure;
- anchor failure;
- coalition-generation failure;
- final-selection/routing failure;
- regime failure;
- PowerBall candidate failure;
- PowerBall pairing failure;
- null-equivalent result.

Do not automatically retune expert weights from a single draw. Preserve frozen pre-draw artifacts for scoring.

---

## 9. Validation Doctrine

The Pair-of-Pairs + Anchor Coalition Assembler is an accepted experimental core module and the preferred HEPS synthesis method from v33.3 onward.

It must continue to be evaluated prospectively against:

- the previous independent-line selector;
- unweighted maximum coverage;
- weighted/hypergraph coalition variants;
- the mandatory chaos/random baseline.

Claims of durable predictive advantage still require walk-forward or prospective evidence and matched-null comparison. Architectural improvement and predictive edge are separate claims.