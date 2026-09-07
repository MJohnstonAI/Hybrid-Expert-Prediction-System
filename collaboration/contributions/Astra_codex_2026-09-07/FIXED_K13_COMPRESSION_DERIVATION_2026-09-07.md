# Optimal Fixed-K13 Compression and Exact Inference Without Full Legal-Line Enumeration

**Author:** Codex, GPT-6  
**Date:** 2026-09-07  
**Source task:** `01a07bd5-8a21-7b50-ba0d-8e10d32e1668`  
**Evidence classification:** `INSUFFICIENT_EVIDENCE` for predictive benefit  
**Architecture status:** `experimental`  
**Scope:** mathematical derivation and synthetic verification; no fitted forecast or predictive backtest

## Research intent and provenance

Role: decision theorist and exact-inference auditor. Research targets: Q003 (optimal fixed-K13 objective) and Q004 (scenario-constrained preservation), in the Candidate Funnel and methodology stages.

The director asked: “Derive the mathematically optimal and computationally efficient fixed-K=13 compression rule for a coherent probability distribution over legal 5/50 lines. Determine which quantities can be computed analytically or by dynamic programming without explicit enumeration of all 2,118,760 states.” This contribution preserves all substantive research disclosed in response, including formulas, counterexample, computational limits, and verification results. The final appendix makes the synthetic checks reproducible.

Thesis: optimal compression is objective-dependent. Exact inference and evaluation can be inexpensive for structured probability fields, while global basket optimization is a separate problem.

Data/training window: none. Validation: synthetic legal five-subsets and the analytic uniform 5/50 null. Prospective targets: zero. No historical draw was fitted, no result-conditioned parameters were chosen, and no frozen slate was revised. The synthetic random seed is 7; 20 small-universe cases were checked. Additional controls are a fixed counterexample and the exact uniform null. Numerical falsification criterion: discrepancy above `1e-12` between the stated DP calculations and exhaustive small-universe calculations. These checks verify implementation identities, not universal optimality of a heuristic or predictive performance.

Authority requested: contribution intake and peer review only. No core or production change. Known overlap: [E0031](../../../experiments/E0031/hypothesis.md), the retained E0019 containment objective, and E0025 DP infrastructure. The five-line witness below also appears in E0031; it is not claimed as newly discovered here. Its objective values were independently recalculated in this session. Existing experiment packages remain intact.

Strongest counterargument: a correct optimizer can amplify a misspecified probability field. Optimization error and estimation error must be evaluated separately.

## 1. Main result

There is no objective-independent “optimal K13.” For a coherent line distribution, Top-13 marginals exactly maximize expected winners retained. Maximizing four-plus survival or complete-line containment requires a different, joint optimization.

For HEPS's preferred slot-residual product model, normalization and all coordinate marginals cost `O(5 × 50)`; the complete hit-count distribution of any fixed basket costs `O(5² × 50)`. Neither requires enumerating all 2,118,760 lines. These are arithmetic complexity orders, not measured runtimes.

The derivations concern mathematical optimality under a supplied probability model, not evidence that the model predicts future draws.

## 2. Define the decision objective

Let

\[
\Omega=\{x=(x_1<\cdots<x_5):x_j\in\{1,\ldots,50\}\},\qquad X\sim P,
\]

and choose a basket \(B\subseteq\{1,\ldots,50\}\), \(|B|=13\). Define

\[
H_B=|X\cap B|.
\]

For a declared utility \(u:\{0,\ldots,5\}\to\mathbb R\), the exact Bayes rule is

\[
\boxed{B_u^\star\in\arg\max_{|B|=13}\mathbb E_P[u(H_B)].}
\]

| Objective | Utility |
|---|---|
| Expected winner-coordinate survival | \(u(h)=h\) |
| Four-plus survival | \(u(h)=\mathbf1\{h\ge4\}\) |
| Complete-line containment | \(u(h)=\mathbf1\{h=5\}\) |
| Avoid catastrophic 0/1 retention | \(u(h)=\mathbf1\{h\ge2\}\) |

A tradeoff between these requires explicit weights, constraints, or a lexicographic priority. Coherence alone cannot determine that preference. A scenario-dependent or robust objective must likewise be declared rather than silently substituted for expected utility.

## 3. Exact closed-form compression for expected survival

Define the anywhere-inclusion probabilities

\[
\pi_i=P(i\in X)=\sum_{j=1}^{5}P(X_j=i).
\]

The sum is exact because a coordinate cannot occupy two sorted slots in the same legal line. Then

\[
\mathbb E[H_B]=\sum_{i\in B}\pi_i,
\qquad
\boxed{B_{\mathrm{mean}}^\star=\operatorname{Top13}(\pi_1,\ldots,\pi_{50}).}
\]

Proof: replacing a selected coordinate \(a\) by an excluded coordinate \(b\) changes the objective by \(\pi_b-\pi_a\). Therefore a basket containing the 13 largest marginals is globally optimal. Ties may be resolved by a declared deterministic rule; all tied maximizers have the same expected-hit value.

This also minimizes expected excluded winners, since \(\mathbb E[5-H_B]=5-\mathbb E[H_B]\), and expected set symmetric-difference loss, since \(|X\triangle B|=18-2H_B\). No independence assumption is needed.

The marginals must come from the normalized joint distribution. They are not generally the original slot distributions used to construct its potentials.

## 4. Why four-plus and five-of-five need joint information

Write \(F_q(B)=P(H_B\ge q)\). For a 12-coordinate set \(A\) and alternatives \(a,b\notin A\),

\[
\boxed{
F_q(A\cup\{b\})-F_q(A\cup\{a\})
=P(H_A=q-1,b\in X,a\notin X)
-P(H_A=q-1,a\in X,b\notin X).
}
\]

Only outcomes where the existing basket has exactly \(q-1\) hits can change threshold success. Thus a coordinate's value depends on its ability to complete the existing basket to the required threshold. Unconditional inclusion probability does not capture that.

### 4.1 A strict counterexample

Consider these five legal lines, with zero probability on other lines:

| Line | Probability |
|---|---:|
| 1,2,3,4,5 | 40/101 |
| 6,7,8,9,10 | 30/101 |
| 11,12,13,14,15 | 20/101 |
| 1,6,11,12,16 | 10/101 |
| 2,7,11,13,16 | 1/101 |

The unique Top-13 marginal basket is \(\{1,\ldots,13\}\), but:

| Objective | Top-13 marginals | Global optimum |
|---|---:|---:|
| Four-plus survival | 81/101 | 101/101 |
| Complete containment | 70/101 | 80/101 |

A four-plus optimal witness is `{2,3,4,5,6,8,9,10,11,12,13,15,16}`. A containment-optimal witness is `{1,2,3,4,5,6,7,8,9,10,11,12,16}`. The stated optima were checked over all 13-subsets of 1..16; coordinates outside this support cannot improve a nondecreasing hit-count objective.

Adding a uniform component with weight \(0<\epsilon<1\),

\[
P_\epsilon=(1-\epsilon)P+\epsilon P_0,
\]

gives full support while preserving both strict disadvantages: every fixed-K13 has the same uniform-null objective, and all marginals receive the same uniform addition. The counterexample therefore does not depend on zero probabilities.

### 4.2 Complete-line compression and reverse KL

For complete containment, the exact rule is

\[
\boxed{B_5^\star\in\arg\max_{|B|=13}M(B)},
\qquad
M(B)=\sum_{\substack{x\in\Omega\\x\subseteq B}}P(x).
\]

For fixed \(B\) with \(M(B)>0\), the distribution supported inside \(B\) minimizing \(D_{\mathrm{KL}}(Q\|P)\) is

\[
Q_B(x)=P(x\mid X\subseteq B),
\]

with minimum divergence \(-\log M(B)\). In fact,

\[
D_{\mathrm{KL}}(Q\|P)=D_{\mathrm{KL}}(Q\|Q_B)-\log M(B)
\]

for such supported distributions. Thus maximizing containment also minimizes reverse-KL compression loss. Forward KL is infinite when the compressed distribution discards positive-probability lines. If \(M(B)=0\), the finite reverse-KL construction is unavailable.

## 5. Exact O(mn) inference for the HEPS slot-product field

The current doctrine specifies a uniform legal-line baseline tilted by slot residuals:

\[
P(x)=\frac1Z\prod_{j=1}^{5}w_j(x_j),\qquad x_1<\cdots<x_5,
\]

where \(w_j(v)=T_j(v)\), with the constant uniform baseline absorbed into \(Z\). In the doctrine, \(T_j(v)=q_j(v)/P_{0,j}(v)\) on legal slot support. Do not instead multiply the five structural slot marginals into the line field. When every residual weight is 1, this model recovers the uniform legal-line null exactly.

Assume nonnegative potentials and \(Z>0\). Here \(m=5\), \(n=50\).

Define the prefix partition function

\[
L_j(v)=\sum_{1\le x_1<\cdots<x_j\le v}\prod_{\ell=1}^{j}w_\ell(x_\ell).
\]

Its recurrence is

\[
\boxed{L_j(v)=L_j(v-1)+w_j(v)L_{j-1}(v-1)}
\]

with \(L_0(v)=1\), \(L_j(0)=0\) for \(j>0\), and \(Z=L_5(50)\). The terms partition paths into those excluding \(v\) and those using it as their final coordinate.

This costs \(O(mn)\), and only \(O(m)\) working memory if just \(Z\) is required. In an in-place implementation, update \(j\) in descending order to prevent reuse of a coordinate.

For all slot marginals, compute suffix messages

\[
R_j(v)=R_j(v+1)+w_j(v)R_{j+1}(v+1),
\]

where \(R_6(v)=1\) and \(R_j(51)=0\) for \(j\le5\). Then

\[
\boxed{P(X_j=v)=\frac{L_{j-1}(v-1)w_j(v)R_{j+1}(v+1)}{Z}.}
\]

All 250 slot marginals and 50 anywhere marginals therefore cost \(O(mn)\) overall, using \(O(mn)\) stored messages. Legal ordering creates the slot dependence; these recurrences preserve it exactly. Summing the anywhere marginals must give 5.

## 6. One polynomial DP gives every basket-survival metric

For a fixed basket, let \(b_v=\mathbf1\{v\in B\}\). Replace the scalar prefix recurrence by

\[
D_j(v;z)=D_j(v-1;z)+w_j(v)z^{b_v}D_{j-1}(v-1;z),
\]

with \(D_0(v;z)=1\) and the analogous zero boundaries for positive \(j\). Then

\[
\boxed{G_B(z)=\frac{D_5(50;z)}Z=\sum_{h=0}^{5}P(H_B=h)z^h.}
\]

Only six polynomial coefficients are needed. Complexity is \(O(nm^2)\), with \(O(m^2)\) working memory. From the coefficients we obtain exactly:

- expected retained winners and their variance;
- \(P(H_B\ge3)\), \(P(H_B\ge4)\), and \(P(H_B=5)\);
- catastrophic \(P(H_B\le1)\);
- any utility \(\mathbb E[u(H_B)]\);
- lower-tail utility or loss-CVaR calculations, with the chosen tail convention specified.

For containment alone,

\[
\boxed{M(B)=Z_B/Z,}
\]

where \(Z_B\) uses the scalar recurrence while scanning only the 13 selected coordinates in sorted order. This costs \(O(mK)\), retaining each coordinate's original slot potential. Do not renumber coordinates or reinterpret a coordinate's basket rank as its forecast slot.

Define the binomial moments

\[
\mu_r(B)=\mathbb E\binom{H_B}{r}.
\]

Then the exact identities

\[
P(H_B\ge4)=\mu_4(B)-4\mu_5(B),\qquad P(H_B=5)=\mu_5(B)
\]

make clear why first-order marginals alone cannot determine these objectives. Equivalently, \(\mu_r(B)\) is the sum of \(P(S\subseteq X)\) over all r-subsets \(S\) of \(B\); the hit-count DP avoids materializing that collection.

## 7. Other quantities that avoid full enumeration

| Quantity/model | Exact method | Cost or limitation |
|---|---|---|
| Uniform slot marginal | \(\binom{v-1}{j-1}\binom{50-v}{5-j}/\binom{50}{5}\) | Closed form |
| Uniform hit-count distribution | \(\binom{13}{h}\binom{37}{5-h}/\binom{50}{5}\) | Closed form |
| Slot HLR, VVD, terminal probabilities | Aggregate exact slot marginals | \(O(mn)\) |
| Joint HLR scenario probability | Mask each slot to its specified direction; compute \(Z_s/Z\) | \(O(mn)\) per scenario; at most 243 |
| Scenario-conditioned basket metrics | Masked polynomial DP | \(O(m^2n)\) per scenario |
| Observed-line log loss | \(\log Z-\sum_j\log w_j(x_j)\) | \(O(m)\) after \(Z\) |
| Full-line Brier score | \(1-2P(x_{\rm obs})+Z(w^2)/Z(w)^2\) | One extra scalar DP |
| Joint entropy, positive potentials | \(\log Z-\sum_{j,v}P(X_j=v)\log w_j(v)\) | From existing marginals |
| Additive statistics, such as sum or digit sum | Add statistic index to DP | Multiplies cost by statistic range |
| Adjacent-slot pair potentials | Forward–backward with pair transitions | Typically \(O(mn^2)\); hit counts add a factor \(m\) |
| Mixture of S tractable components | Compute each normalized component; average probabilities | Linear in S for ordinary probabilities and hit metrics |
| Arbitrary dense line probabilities | No generic compact recurrence | Must generally inspect the explicit input |

Here \(Z(w^2)\) means replace every local potential by its square and rerun the partition DP. The Brier convention is the unscaled multiclass sum over all legal lines. A positive-probability observed line is required for finite log loss; zero-weight entropy terms need the usual limiting convention.

### 7.1 Scenarios and mixtures

For an HLR scenario \(s\), mask coordinate \(v\) in slot \(j\) according to its sign relative to the frozen previous slot coordinate. This preserves exact joint ordering. The unmasked denominator \(Z\) yields \(P(s)=Z_s/Z\); conditional calculations use denominator \(Z_s\) when it is positive. Impossible scenarios have zero mass and no defined conditional distribution.

For a mixture \(P=\sum_s\alpha_sP_s\), average normalized component distributions, not slot potentials. Mixing potentials generally defines a different model. Linear mixture aggregation applies to marginals, scenario probabilities, hit distributions, and expected utilities. Entropy is not the weighted sum of component entropies, and the single-component Brier shortcut cannot be used by simply averaging component Brier scores; cross terms must be included.

### 7.2 Dependence limits

For arbitrary interactions among all five slots, the small prefix recurrence is no longer valid. Exact inference depends on the factorization's induced width; dense dependence can remove the computational advantage. This is the standard variable-elimination limitation described in [CMU's exact-inference notes](https://www.cs.cmu.edu/~epxing/Class/10708-19/notes/lecture-04/).

Although repository descriptions prescribe full enumeration for the joint HLR null, masked DP computes the same mathematical probabilities exactly. Changing the repository implementation would require equivalence verification and would not alter the meaning of `NULL_HLR_JOINT_243`.

Coherence alone does not imply tractable inference. An arbitrary supplied table can encode independent information across its entries; no generic small DP is established for that representation.

## 8. Fast evaluation is distinct from fast global optimization

There are

\[
\binom{50}{13}=354,860,518,600
\]

possible baskets. For general slot-dependent weights, neither \(F_4(B)\) nor \(M(B)\) becomes an additive coordinate score. Replacing sums with maxima in the inference DP would solve a different problem, such as selecting a best line or allowing incompatible decisions, rather than selecting one shared basket before the outcome.

### 8.1 Exact branch-and-bound using DP probability bounds

An exact approach avoiding legal-line enumeration is:

1. At a search node, let \(A\) be selected coordinates, \(U\) undecided coordinates, and \(r=13-|A|\) remaining seats. Reject infeasible nodes where \(r<0\) or \(r>|U|\).
2. Every completion \(B=A\cup C\), \(C\subseteq U\), \(|C|=r\), satisfies

   \[
   H_B\le |X\cap A|+\min(r,|X\cap U|).
   \]

3. Therefore a valid threshold upper bound is

   \[
   \boxed{F_q(B)\le P\bigl(|X\cap A|+\min(r,|X\cap U|)\ge q\bigr).}
   \]

4. Compute the bound with a two-count DP recording hits in \(A\) and \(U\). For the slot-product field, augment the recurrence with two generating variables, multiplying the contribution of coordinate \(v\) by \(z^{\mathbf1\{v\in A\}}t^{\mathbf1\{v\in U\}}\). Sum normalized coefficients satisfying the displayed bound event. A direct implementation costs \(O(nm^3)\).
5. Prune branches whose bound cannot beat the best exactly evaluated feasible basket.

This supplies a global certificate when all remaining bounds are closed. If stopped early, report the best objective value and remaining upper bound. Runtime can still be large; the bound permits outcome-specific choices of the remaining seats and can be loose. Multi-start swap search supplies useful incumbents but does not certify global optimality. Floating-point certificates must account for numerical tolerance; exact recurrences do not automatically imply exact floating-point bounds.

The branch-and-bound method here is a derived proposal, not a newly implemented or benchmarked solver in this contribution. The synthetic checks below do not test its full search or its runtime.

### 8.2 A tractable special case

For coordinate-product probabilities

\[
P(X)\propto\prod_{i\in X}a_i,
\]

selecting the 13 largest \(a_i\) maximizes every nondecreasing hit-count utility. The exchange difference factors into \(a_b-a_a\) times a nonnegative quantity: pair each outcome containing \(a\) but not \(b\) with the outcome replacing \(a\) by \(b\). Their other four coordinates have the same product weight, and the utility difference is nonnegative when the higher-weight coordinate is selected. Repeated exchanges reach the top-weight basket.

Its partition function is the elementary symmetric polynomial \(e_5(a)\), computable in \(O(mn)\). General slot-specific potentials and mixtures with conflicting coordinate preferences do not inherit this guarantee.

## 9. Consequences for HEPS and authority boundaries

Use an explicit objective and retain slot/scenario provenance alongside the resulting basket:

- Expected survival: exact joint marginals → Top-13.
- Four-plus survival: maximize \(P(H_B\ge4)\), evaluated by polynomial DP.
- Complete containment: maximize \(Z_B/Z\), evaluated by restricted scalar DP.
- Scenario protection: add preregistered scenario constraints or a robust objective; this changes the decision criterion and must be stated.

The unconstrained Top-13 theorem does not authorize erasing E0026's routed tensor or changing its operational policy. Additional routing constraints can change the feasible set and thus the optimum. Preserve candidate coordinate, admissible slot, scenario probability, and legal-line support. This contribution does not grant any new candidate or pruning authority.

Under the uniform null, every K13 is equivalent:

\[
\mathbb EH_B=1.3,\quad
P(H_B\ge4)=1.3093507523\%,\quad
P(H_B=5)=0.06074307614\%.
\]

The catastrophic 0/1 probability is approximately \(61.09620722\%\). The uniform control cannot rank coordinates. It also verifies that no computational optimization creates predictive information.

After candidate freeze, the existing requirement to enumerate all \(\binom{13}{5}=1,287\) lines for downstream assembly remains intact. Avoiding global 5/50 enumeration for probability inference does not waive that stage requirement.

No predictive backtest or pipeline change was made. Predictive evidence remains `INSUFFICIENT_EVIDENCE`: exact compression cannot repair a misspecified probability field. Proper-score improvement versus structural/simple controls must precede claims of acquisition lift.

## 10. Verification performed in the source session

The independent inline Python check used standard-library arithmetic, seed 7, 20 positive random slot-product fields on n=10, m=5, and random K=7 baskets. Each small universe has 252 legal lines. It compared:

- partition normalization;
- all sorted-slot marginals;
- all six basket hit-count probabilities;
- restricted-partition containment;
- the squared-probability sum used by the full-line Brier identity.

The maximum absolute probability discrepancy was `2.220446049250313e-16`, below the declared `1e-12` threshold. The reported rounded discrepancy was `2.3e-16`.

The same check recovered:

```text
uniform_Z                         2118760.0
uniform_expected_hits             1.3
uniform_4plus                     0.013093507523268327
uniform_5                         0.0006074307613887368
uniform_catastrophe_0or1           0.6109620721554117
K13_choices                       354860518600
counterexample_top13_4plus         81/101
counterexample_global_4plus        101/101
counterexample_top13_containment   70/101
counterexample_global_containment  80/101
```

These are synthetic/analytic implementation checks. They are not a new predictive result, a benchmark of full-scale global search, or an exhaustive test of every model extension in Section 7.

## 11. Reproducible synthetic verification

The following standalone standard-library Python reproduces the core checks without reading or writing ledger, cycle, or experiment files. It uses zero-based coordinates internally. The counterexample uses one-based labels as printed in Section 4.

```python
import itertools
import math
import random

random.seed(7)


def partition(w, allowed=None):
    m, n = len(w), len(w[0])
    d = [1.0] + [0.0] * m
    for v in range(n):
        if allowed is not None and v not in allowed:
            continue
        for j in range(m, 0, -1):
            d[j] += w[j - 1][v] * d[j - 1]
    return d[m]


def counts(w, basket):
    m, n = len(w), len(w[0])
    d = [[0.0] * (m + 1) for _ in range(m + 1)]
    d[0][0] = 1.0
    for v in range(n):
        b = int(v in basket)
        for j in range(m, 0, -1):
            for h in range(b, j + 1):
                d[j][h] += w[j - 1][v] * d[j - 1][h - b]
    return d[m]


def marginals(w):
    m, n = len(w), len(w[0])
    left = [[0.0] * (n + 1) for _ in range(m + 1)]
    right = [[0.0] * (n + 2) for _ in range(m + 2)]
    left[0] = [1.0] * (n + 1)
    right[m + 1] = [1.0] * (n + 2)
    for j in range(1, m + 1):
        for v in range(1, n + 1):
            left[j][v] = (
                left[j][v - 1] + w[j - 1][v - 1] * left[j - 1][v - 1]
            )
    for j in range(m, 0, -1):
        for v in range(n, 0, -1):
            right[j][v] = (
                right[j][v + 1] + w[j - 1][v - 1] * right[j + 1][v + 1]
            )
    z = left[m][n]
    return [
        [left[j - 1][v - 1] * w[j - 1][v - 1]
         * right[j + 1][v + 1] / z for v in range(1, n + 1)]
        for j in range(1, m + 1)
    ]


max_error = 0.0
for trial in range(20):
    n, m = 10, 5
    w = [[random.uniform(0.1, 2) for _ in range(n)] for _ in range(m)]
    basket = set(random.sample(range(n), 7))
    lines = list(itertools.combinations(range(n), m))
    weights = [math.prod(w[j][v] for j, v in enumerate(x)) for x in lines]
    z = sum(weights)
    assert math.isclose(partition(w), z, rel_tol=1e-12)
    exact = [
        sum(p for x, p in zip(lines, weights) if len(set(x) & basket) == h) / z
        for h in range(m + 1)
    ]
    got = [value / partition(w) for value in counts(w, basket)]
    slot = marginals(w)
    for j in range(m):
        for v in range(n):
            reference = sum(p for x, p in zip(lines, weights) if x[j] == v) / z
            max_error = max(max_error, abs(slot[j][v] - reference))
    max_error = max(
        max_error,
        max(abs(a - b) for a, b in zip(exact, got)),
        abs(partition(w, basket) / partition(w) - exact[5]),
    )
    squared_mass = sum((p / z) ** 2 for p in weights)
    dp_squared_mass = partition([[v * v for v in row] for row in w]) / partition(w) ** 2
    max_error = max(max_error, abs(squared_mass - dp_squared_mass))
assert max_error < 1e-12

w = [[1.0] * 50 for _ in range(5)]
z = partition(w)
hit = [value / z for value in counts(w, set(range(13)))]
assert z == math.comb(50, 5)
print({
    "synthetic_cases": 20,
    "max_absolute_error": max_error,
    "uniform_Z": z,
    "uniform_expected_hits": sum(i * p for i, p in enumerate(hit)),
    "uniform_4plus": sum(hit[4:]),
    "uniform_5": hit[5],
    "uniform_catastrophe_0or1": sum(hit[:2]),
    "K13_choices": math.comb(50, 13),
})

lines = [
    {1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15},
    {1, 6, 11, 12, 16}, {2, 7, 11, 13, 16},
]
masses = [40, 30, 20, 10, 1]
marginal_basket = set(range(1, 14))
for threshold in (4, 5):
    def value(basket):
        return sum(p for x, p in zip(lines, masses) if len(x & basket) >= threshold)

    best = max(
        (value(set(basket)), basket)
        for basket in itertools.combinations(range(1, 17), 13)
    )
    assert best[0] == {4: 101, 5: 80}[threshold]
    print({
        "threshold": threshold,
        "top_marginal_mass_over_101": value(marginal_basket),
        "best_mass_over_101": best[0],
        "best_basket": best[1],
    })
```

## 12. Sources and peer-review handoff

Repository interpretation sources:

- [AGENTS.md](../../../AGENTS.md): constitutional invariants, stage separation, fixed-K integrity, and contribution obligations.
- [Current method doctrine](../../../governance/current_method_doctrine.md): residual-ratio legal-line construction, null recovery, and proper-score-first gates.
- [Methodology deprecations](../../../governance/methodology_deprecations.md): retain the E0019 containment objective without reusing its rejected field.
- [Nomenclature](../../../governance/nomenclature.md): exact-slot versus anywhere-coordinate probabilities and E0026 routed support.
- [Research protocol](../../../governance/research_protocol.md): synthetic versus prospective evidence and dependency controls.
- [External contribution protocol](../../../governance/external_contribution_protocol.md): component decomposition and authority separation.
- [Open questions](../../../knowledge/open_questions.md): Q003 and Q004.
- [E0031 hypothesis](../../../experiments/E0031/hypothesis.md) and [results](../../../experiments/E0031/results.json): overlapping threshold-compression and counterexample research; no new full-package reproduction claimed here.
- [Collaboration conventions](../../README.md): source-area placement and intake semantics.

External methodological reference consulted: [CMU 10-708, Lecture 4: Exact Inference](https://www.cs.cmu.edu/~epxing/Class/10708-19/notes/lecture-04/), for the relationship between exact inference, variable elimination, and treewidth. The HEPS-specific formulas above are derived in this contribution rather than attributed to that source.

Suggested independent review: check objective semantics first; reproduce the appendix; test scenario masks and pair-potential extensions separately; verify branch-and-bound bounds before treating them as numerical certificates; and retain proper-score/prospective gates before testing operational acquisition changes. No contribution storage action promotes these operators.
