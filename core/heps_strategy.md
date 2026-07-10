# HEPS STRATEGIC COMPENDIUM & COGNITIVE SPECIFICATION

This document serves as the authoritative mathematical and semantic reference for all autonomous agents. It defines the explicit internal mechanics of the five core "Expert" lanes and the exact protocol for synthesizing their outputs into production prediction slates.

---

## 1. The Expert Roster & Strategy Specifications

### Lane 1: The Coulomb Void Starvation Engine (`expert_void_bridge`)
* **Core Principle:** Models spatial field deprivation under the hypothesis that prolonged absence of hits in a specific numerical sector creates a geometric vacuum dynamic.
* **Mathematical Mechanics:** The sector tension $C(x)$ for any number $x$ in the 1–50 matrix is calculated based on its starvation interval $t_x$ (draws elapsed since last hit):

$$C(x) = 1 - e^{-\lambda t_x}$$

* **Behavioral Constraints:** When $C(x) > 0.85$, the engine triggers a "Void Breach" protocol, forcing the selection of clusters within that starved sector.

### Lane 2: The Kinetic Inertia & Step Drift Tracker (`expert_stiction_shadow`)
* **Core Principle:** Models short-term mechanical stiction and drag. It assumes the pneumatic machine state changes gradually, causing numbers to repeat (stiction) or shift by small spatial increments ($\pm 1$ or $\pm 2$ grid slots).
* **Mathematical Mechanics:** Evaluates velocity vectors across consecutive draws:

$$V_t = X_t - X_{t-1}$$

* **Behavioral Constraints:** If $V_t \in \{-1, 0, 1\}$ over a 3-draw window, it projects a "shadow line" over the active coordinates, highly weighting the immediate physical neighbors of the last drawn numbers.

### Lane 3: Sorted-Position Momentum (`expert_sorted_momentum`)
* **Core Principle:** Evaluates the historical behavior of the draw pool strictly as **order statistics**. It tracks the specific mathematical distribution of numbers when sorted from lowest (Slot 1) to highest (Slot 5).
* **Mathematical Mechanics:** Maps the probability density function (PDF) for each sorted slot. For example, it restricts Slot 1 to its historical boundary ($1 \le X_{(1)} \le 15$) and Slot 5 to its boundary ($35 \le X_{(5)} \le 50$).
* **Behavioral Constraints:** Rejects any candidate combination where the numbers cross their respective slot-bound statistical distributions, preventing structurally impossible combinations.

### Lane 4: The Tri-Cluster High-Register Engine (`expert_tri_cluster_high`)
* **Core Principle:** Captures extreme upper-quadrant fluid clumping behaviors where heavy-ink ball dynamics restrict high-velocity air currents, trapping multiple balls in a narrow spatial band at the end of the field.
* **Mathematical Mechanics:** Tracks the occurrence of three numbers falling within an isolated 5-unit register (e.g., `41, 43, 44`).
* **Behavioral Constraints:** Activated only when the rolling Macro-Sum exceeds its 10-draw moving average by 15%, shifting allocation weights heavily toward the 40–50 decile.

### Lane 5: The Randomized Control Baseline (`expert_chaos_hedge`)
* **Core Principle:** Serves as the system's control group and mathematical anchor. It represents pure, filtered lottery entropy.
* **Mathematical Mechanics:** Generates combinations using uniform pseudo-random number generation across the 5/50 + 1/16 fields.
* **Behavioral Constraints:** Bypasses all advanced stiction and void filters. It exists entirely to protect the portfolio against systemic confirmation bias and over-tuning.

---

## 2. Synthesis Protocol: Generating the Prediction Slates

To translate these independent expert outputs into the final 10-line production portfolio, the Synthesizer Agent (`agent_synthesizer`) must execute the following structured pooling matrix:

### The Portfolio Allocation Blueprint
Every production slate deployment file generated in `/outputs/predictions/` must allocate its 10 slots strictly according to this diversified lane portfolio:

| Rank | Dedicated Research Lane | Primary Mathematical Target |
| :--- | :--- | :--- |
| **1–3** | `tri_cluster_high` | Captures high-register momentum and pneumatic clumping. |
| **4–6** | `void_bridge` | Targets localized collapse within high-tension starvation sectors. |
| **7–8** | `stiction_shadow` | Plays the $\pm 1$ spatial drift lines and immediate repeat patterns. |
| **9** | `sorted_momentum` | Leverages order statistics median slot distribution curves. |
| **10** | `chaos_hedge` | The pure random-filtered control line to anchor the portfolio. |

### The Dynamic Consensus Layer
For overlapping lines, the final confidence score ($HEPS_{score}$) for any candidate combination is synthesized using dynamic expert weighting:

$$HEPS_{score} = w_1 E_1 + w_2 E_2 + w_3 E_3 + w_4 E_4$$

`scripts/score_prediction.py` records portfolio and lane-level evidence after
each draw cycle. It does **not** automatically change the weights ($w_i$) from a
single result. Preserve weights across independently generated pre-draw slates;
after at least 20 scored targets, compare each lane against chaos/random-null
baselines and submit any proposed weight change through the contribution,
red-team, and merge-decision workflow. The 20-target threshold is a minimum
review gate, not evidence that a predictive edge exists.

The current research scorer does not yet implement a distinct
`sorted_position_momentum` feature. Do not treat the generic `midfield` score as
an equivalent implementation; retain this as an explicit calibration TODO.
