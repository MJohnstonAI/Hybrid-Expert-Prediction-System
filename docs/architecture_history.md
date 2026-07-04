# HEPS ARCHITECTURE EVOLUTION & LEGACY EXPERT RECORD
**Status:** ARCHIVED / DEPRECATED (Do Not Re-Implement)  
**Last Review Date:** July 4, 2026  

## 1. Executive Summary
This document logs the experimental mathematical and physical hypotheses tested in earlier iterations of the Hybrid Expert Prediction System (HEPS v1.0 through v4.2). These modules have been permanently decommissioned, refactored, or absorbed into the core architecture. 

Autonomous agents are strictly forbidden from spinning up new active expert branches based on these concepts, as past validation cycles proved they introduce statistical redundancy, severe confirmation bias, or unverifiable physical assumptions.

---

## 2. Comprehensive Decommissioned Module Log

### 2.1 Variance Volume Density (VVD Engine)
* **Original Hypothesis:** Postulated that the physical balls within the chamber clustered into localized "mass pockets" during the draw sequence, which could be predicted by calculating a volumetric clustering density coefficient across the 1–50 matrix grid.
* **Observed Failure Mode:** Red-teaming and statistical back-testing revealed that the VVD calculations were perfectly correlated with standard **order statistics**. The model was not tracking "fluid volume density"; it was simply tracking the normal statistical variance of the distance between sorted numbers. Treating it as an independent expert artificially inflated the confidence scores of clustered numbers.
* **Evolutionary Fate:** Stripped of speculative physical framing and completely absorbed into `/core/heps_strategy.md` under **Lane 3: Sorted-Position Momentum (`expert_sorted_momentum`)** to serve as a pure mathematical boundary filter.

### 2.2 The High-Low Flow Metric
* **Original Hypothesis:** Modeled a macro-environmental "breathing effect" inside the machine, predicting that kinetic energy would rhythmically oscillate between the lower deciles (1–25) and upper deciles (26–50) from draw to draw.
* **Observed Failure Mode:** Operating as a primary generation expert, the High-Low Flow metric forced extreme, systemic over-corrections. It frequently caused the consensus layer to output high-entropy combinations consisting of either all-low or all-high lines, missing mid-field distribution patterns and destroying portfolio diversification.
* **Evolutionary Fate:** Demoted from an active number generator to a secondary system gate. It now acts as a silent **Sum/Spread Governor** within the synthesizer framework, preventing lines from being published if their calculated Macro-Sum breaks outside the strict historical boundary constraints ($110 \le \sum \le 160$).

### 2.3 Ink-Mass Weighting Mechanics
* **Original Hypothesis:** Proposed that differences in the physical weight of printed text digits on the balls (e.g., a two-digit number like "48" carrying slightly more ink mass than a single-digit number like "08") would impact the terminal velocity and drop rate of the ball within the pneumatic suction chamber.
* **Observed Failure Mode:** **Methodological Error / Hallucinated Edge.** Because the canonical ledger records data sequentially based on *sorted ascending order* rather than the *actual physical order of selection*, it was impossible to correlate ink mass with drop sequence. Without drawn-order data, the model was completely unfalsifiable and introduced dangerous noise into the dataset.
* **Evolutionary Fate:** **Permanently Terminated.** Extracted entirely from the codebase. No agent may re-introduce weight or ink-mass variables.

### 2.4 Pneumatic Drag Vector
* **Original Hypothesis:** Attempted to track continuous physical resistance along the chamber walls by charting lines that repeated exactly or moved to immediately adjacent slots on the physical selection grid.
* **Observed Failure Mode:** While the physical phenomenon of mechanical stiction was validated, maintaining a separate module created massive logic loops and code sprawl when calculating spatial vectors alongside the tracking matrices.
* **Evolutionary Fate:** Streamlined and merged directly into **Lane 2: The Kinetic Inertia & Step Drift Tracker (`expert_stiction_shadow`)**, focusing strictly on the clean $\pm 1$ and $\pm 2$ spatial tracking metrics.

---

## 3. Mandatory Agent Onboarding Rules
When designing automated optimization scripts or executing walk-forward back-tests in this repository, you must verify that your code does not inadvertently introduce proxy variables that mimic the decommissioned metrics listed above. All mathematical proposals must explicitly cross-reference this document to verify structural alignment with historical development conclusions.