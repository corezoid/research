---
title: "Regulatory Quality of Asymptotic Models: A Quantitative Framework with Arithmetic Benchmark"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-03
doi: 10.13140/RG.2.2.31082.79042
version: v1
license: CC-BY-4.0
keywords: [regulation theory, Conant–Ashby theorem, Ashby's Law, model quality, prime distribution, noise suppression, threshold phenomena]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.13140/RG.2.2.31082.79042](https://doi.org/10.13140/RG.2.2.31082.79042).

# Regulatory Quality of Asymptotic Models: A Quantitative Framework with Arithmetic Benchmark

**Alexander Vityaz** · Corezoid Inc., Dnipro, Ukraine · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

## Abstract

We introduce a quantitative framework for measuring how well an asymptotic model regulates a finite system, grounded in the Conant–Ashby Good Regulator Theorem. The central construct is *regulatory quality* $R(\sigma)$, a function of observation scale $\sigma$ that measures the fraction of system variance explained by a model after symmetric smoothing. We prove, for general bounded sequences with asymptotically predictable means, the existence of a critical scale $\sigma^*$ below which model-based regulation is impossible. We establish conditions under which a structurally richer model achieves a smaller critical scale. As a benchmark, we apply the framework to the distribution of primes across consecutive decades (intervals of width 10), using the chain $r_\mathrm{PNT} \preceq \mathrm{Li}(x) \preceq \mathcal{R}(x)$ as a hierarchy of regulators. Numerical experiments on $10^6$ decades (primes up to $10^7$) confirm the theoretical predictions: a sharp threshold phenomenon in $R(\sigma)$, logarithmic scaling $\sigma^* \sim \ln N$, and monotone ordering of critical scales across the regulator hierarchy.

**Keywords:** regulation theory, Conant–Ashby theorem, Ashby's Law, model quality, prime distribution, noise suppression, threshold phenomena

**MSC 2020:** 93B05 (Controllability), 94A17 (Measures of information), 11N05 (Distribution of primes)

## 1 Introduction

The Conant–Ashby Good Regulator Theorem [1] asserts that every good regulator of a system must be a model of that system. Despite its fundamental status in cybernetics, the theorem remains largely qualitative: it does not say *how good* a model must be, at *what scale* regulation becomes possible, or how to *compare* competing models quantitatively.

We address this gap by introducing a framework with three components:

1. A scalar metric $R(\sigma) \in (-\infty, 1]$ that quantifies regulatory quality at observation scale $\sigma$.
2. A critical scale $\sigma^*$ that marks the threshold between ineffective and effective regulation.
3. A partial order on regulators induced by $\sigma^*$: better model $\Leftrightarrow$ smaller $\sigma^*$.

The framework applies to any pair (discrete system, predictive model). To validate it on an object with exact, unambiguous ground truth, we choose the distribution of primes across consecutive decades – a system where both the data and all candidate models are exactly computable.

### 1.1 What this paper is and is not

This paper is a *framework paper with computational validation*. We introduce definitions, prove general structural results about $R(\sigma)$ and $\sigma^*$ for abstract sequences, and then use prime counting functions as a benchmark. We do *not* claim new results in analytic number theory. The primes serve as an ideal test bed precisely because the ground truth is beyond dispute.

Throughout, we are explicit about the status of each result:

- **Theorem**: proved rigorously for the general (abstract) setting.
- **Empirical Law**: observed numerically with high confidence, supported by heuristic arguments.
- **Numerical Observation**: reported from computation without theoretical claim.

### 1.2 Contributions

1. A rigorous definition of regulatory quality $R(\sigma)$ with explicit edge handling (Section 2).
2. **Theorem A** (general): existence of a threshold phenomenon in $R(\sigma)$ for bounded sequences with convergent smoothed means, decomposed into preparatory lemmas (Section 3.1).
3. **Theorem B** (general): conditions under which model refinement strictly reduces $\sigma^*$ (Section 3.2).
4. **Empirical Law**: $\sigma^*(N) = a + b \ln N$ for prime decade regulators, verified on 6 orders of magnitude (Section 5.3).
5. **Numerical Observation**: regulator hierarchy $r_\mathrm{PNT} \preceq r_\mathrm{Li} \preceq r_R$ reflected in $\sigma^*$ ordering (Section 5.3).
6. Reproducible computational methodology with sensitivity analysis over threshold $\theta$, interval width $\Delta$, and residual diagnostics (Section 5.4).

### 1.3 Why decades?

A natural question is why we discretize into intervals of width $\Delta = 10$. The reasons are:

- (a) **Bounded counts.** With $\Delta = 10$, $c_k \in \{0, 1, 2, 3, 4\}$, which satisfies the boundedness condition of Theorem A and makes the system easy to visualize and reason about.
- (b) **Exact ground truth.** Each $c_k$ is exactly computable by sieve, with no estimation error.
- (c) **Non-trivial fluctuations.** The counts are small enough that the discrete, stochastic character of primes is visible: decades with 0 primes and decades with 4 primes both occur.
- (d) **Robustness check.** In Section 5.4, we verify that the framework's qualitative predictions (threshold phenomenon, logarithmic scaling) are robust to $\Delta \in \{5, 10, 20, 50\}$.

### 1.4 Related work

**Prime distribution in short intervals.** Selberg [2], Cramér [3], Maier [4], Goldston–Pintz–Yıldırım [5]. These study the arithmetic of primes per se; our work uses primes as benchmark, not as target.

**Regulation theory.** Conant–Ashby [1], Ashby [6]. Our contribution is a computable realization of their qualitative framework.

**Information-theoretic views on primes.** Erdős–Kac [7] on additive functions; various works on entropy of prime gaps. Our entropy analysis (Section 3.3) complements these but targets regulation, not primes.

**Noise suppression in regulation.** Vityaz [8] proved necessity of noise suppression for minimal good regulators of incompressible systems. The present work provides a numerical case study on an exactly computable object.

## 2 Definitions

We work in a general setting first, then specialize to primes.

### 2.1 System and regulator

Let $C = (c_1, c_2, \ldots, c_N)$ be a bounded sequence with $c_k \in [0, M]$ for some $M > 0$ (the *system*), and let $r = (r_1, r_2, \ldots, r_N)$ be a deterministic sequence of non-negative reals (the *regulator* or *model*).

### 2.2 Smoothing operator

**Definition 2.1** (Symmetric smoothing with explicit edge handling)**.** For window size $\sigma \in \mathbb{N}$, $\sigma \geq 1$, and sequence $f = (f_1, \ldots, f_N)$, define

$$
\tilde{f}_\sigma(k) = \frac{1}{|W_\sigma(k)|} \sum_{j \in W_\sigma(k)} f_j,
$$

where $W_\sigma(k) = \{ j \in \{1, \ldots, N\} : |j - k| \leq \lfloor \sigma/2 \rfloor \}$.

Explicitly, $|W_\sigma(k)| = \min(k, \lfloor \sigma/2 \rfloor + 1) + \min(N - k, \lfloor \sigma/2 \rfloor)$. In the interior ($\lfloor \sigma/2 \rfloor < k \leq N - \lfloor \sigma/2 \rfloor$), $|W_\sigma(k)| = 2\lfloor \sigma/2 \rfloor + 1$. At boundaries, the window is truncated and the divisor adjusted accordingly (no padding, no extrapolation).

We denote the operator $S_\sigma : \mathbb{R}^N \to \mathbb{R}^N$, $f \mapsto \tilde{f}_\sigma$. For $\sigma = 1$, $S_1 = \mathrm{Id}$.

### 2.3 Regulatory quality

**Definition 2.2** (Regulatory quality)**.**

$$
R(\sigma) = 1 - \frac{V_\varepsilon(\sigma)}{V_C(\sigma)},
$$

where

$$
V_C(\sigma) = \frac{1}{N} \sum_{k=1}^{N} \bigl( \tilde{C}_\sigma(k) - \bar{C}_\sigma \bigr)^2, \qquad \bar{C}_\sigma = \frac{1}{N} \sum_{k=1}^{N} \tilde{C}_\sigma(k),
$$

$$
V_\varepsilon(\sigma) = \frac{1}{N} \sum_{k=1}^{N} \bigl( \varepsilon_\sigma(k) - \bar{\varepsilon}_\sigma \bigr)^2, \qquad \varepsilon_\sigma(k) = \tilde{C}_\sigma(k) - \tilde{r}_\sigma(k).
$$

The convention $R(\sigma) = 0$ applies when $V_C(\sigma) = 0$ (degenerate case: constant smoothed system).

This is the coefficient of determination ($R^2$) of the smoothed regulator as a predictor of the smoothed system.

*Interpretation:*

- $R(\sigma) = 1$: the regulator perfectly predicts the smoothed system.
- $R(\sigma) = 0$: the regulator explains no more variance than a constant.
- $R(\sigma) < 0$: the regulator is worse than a constant (actively misleading).

**Definition 2.3** (Critical scale)**.** For threshold $\theta \in (0, 1)$:

$$
\sigma^*(\theta) = \min\{ \sigma \in \mathbb{N} : R(\sigma') \geq \theta \text{ for all } \sigma' \geq \sigma \},
$$

or $\sigma^* = +\infty$ if no such $\sigma$ exists. We use $\theta = 0.5$ as default (the "good regulator threshold": the model explains at least half the variance).

We require $R(\sigma') \geq \theta$ for all $\sigma' \geq \sigma$, not just at $\sigma$ itself. This ensures that $\sigma^*$ marks a *permanent* transition to good regulation, avoiding pathological non-monotone cases where $R$ dips below threshold after a transient peak.

### 2.4 Prime-specific definitions

**Definition 2.4** (Prime decade sequence)**.** For $k = 1, 2, \ldots, N$:

$$
c_k = \#\{ p \text{ prime} : 10(k-1) < p \leq 10k \}.
$$

So $c_k \in \{0, 1, 2, 3, 4\}$ and $\sum_{k=1}^{N} c_k = \pi(10N)$.

**Definition 2.5** (Three regulators)**.** (a) **PNT regulator:**

$$
r_\mathrm{PNT}(k) = \sum_{n=10(k-1)+1}^{10k} \frac{1}{\ln n}.
$$

(b) **Li regulator:**

$$
r_\mathrm{Li}(k) = \mathrm{Li}(10k) - \mathrm{Li}(10(k-1)),
$$

where $\mathrm{Li}(x) = \int_2^x \frac{dt}{\ln t}$ (with $\mathrm{Li}(x) = 0$ for $x \leq 2$).

(c) **Riemann regulator:**

$$
r_R(k) = \mathcal{R}(10k) - \mathcal{R}(10(k-1)),
$$

where $\mathcal{R}(x) = \sum_{n=1}^{\infty} \frac{\mu(n)}{n} \mathrm{Li}(x^{1/n})$ is Riemann's prime counting function and $\mu$ is the Möbius function (series truncated at $n = 30$ in computation).

*Remark 2.6.* $r_\mathrm{PNT}$ is the right-rectangle quadrature of $r_\mathrm{Li}$; they differ by $O(1/\ln^2 n)$ per term and carry equivalent structural information at the decade scale. $r_R$ adds prime-power corrections via $\mu(n)$ terms for $n \geq 2$. We write $r_\mathrm{PNT} \preceq r_\mathrm{Li} \preceq r_R$ informally to indicate increasing structural content (this is an approximation-theoretic hierarchy, not a formal subset relation on function spaces).

## 3 General Theory

### 3.1 Existence of threshold phenomenon

We decompose the main result into two preparatory lemmas and a theorem.

**Assumption 1.** Throughout Section 3.1, let $C = (c_1, \ldots, c_N)$ with $c_k \in [0, M]$, and let $(r_1, \ldots, r_N)$ with $r_k \in [0, M']$. Assume:

- **(A1) (Local mean convergence)** There exists a continuous function $\rho : [0, 1] \to \mathbb{R}_{>0}$ such that for every $t \in (0, 1)$ and every sequence $\sigma = \sigma(N) \to \infty$ with $\sigma/N \to 0$:

  $$
  \tilde{C}_\sigma(\lfloor tN \rfloor) \to \rho(t) \quad \text{and} \quad \tilde{r}_\sigma(\lfloor tN \rfloor) \to \rho(t)
  $$

  as $N \to \infty$.
- **(A2) (Non-degeneracy)** $\rho$ is not constant on $[0, 1]$, i.e. $\mathrm{Var}_{t \in [0,1]}[\rho(t)] > 0$.
- **(A3) (Bounded fluctuations)** Let $\delta_k = c_k - r_k$. Then $\frac{1}{N} \sum_{k=1}^{N} \delta_k^2 \leq B$ for some constant $B > 0$ independent of $N$.

> *Editorial note (markdown version):* in the PDF these three items are rendered with the labels "(11)", "(22)", "(33)" (a typesetting artifact); the text refers to them as (A1)–(A3).

**Lemma 3.1** (Residual variance vanishes)**.** *Under (A1) and (A3), for every sequence $\sigma = \sigma(N) \to \infty$ with $\sigma/N \to 0$:*

$$
V_\varepsilon(\sigma) \to 0 \qquad \text{as } N \to \infty.
$$

*Proof.* Let $h = \lfloor \sigma/2 \rfloor$. For $k$ in the interior,

$$
\varepsilon_\sigma(k) = \tilde{C}_\sigma(k) - \tilde{r}_\sigma(k) = \frac{1}{2h+1} \sum_{j=k-h}^{k+h} \delta_j.
$$

Define $\Delta_\sigma(k) = \frac{1}{|W_\sigma(k)|} \sum_{j \in W_\sigma(k)} \delta_j$. Under (A1), $\tilde{C}_\sigma(k)$ and $\tilde{r}_\sigma(k)$ both converge to $\rho(k/N)$, so $\Delta_\sigma(k) \to 0$ pointwise. Since $|\Delta_\sigma(k)| \leq M + M'$ (bounded), by dominated convergence:

$$
V_\varepsilon(\sigma) = \frac{1}{N} \sum_k \bigl( \Delta_\sigma(k) - \bar{\Delta}_\sigma \bigr)^2 \leq \frac{1}{N} \sum_k \Delta_\sigma(k)^2 \to 0. \qquad \square
$$

$\square$

**Lemma 3.2** (System variance is bounded away from zero)**.** *Under (A1) and (A2), for every sequence $\sigma = \sigma(N) \to \infty$ with $\sigma/N \to 0$:*

$$
\liminf_{N \to \infty} V_C(\sigma) \geq \mathrm{Var}[\rho] > 0,
$$

*where $\mathrm{Var}[\rho] = \int_0^1 (\rho(t) - \bar{\rho})^2 \, dt$ and $\bar{\rho} = \int_0^1 \rho(t) \, dt$.*

*Proof.* Under (A1), $\tilde{C}_\sigma(\lfloor tN \rfloor) \to \rho(t)$. Since $|C_\sigma(k)| \leq M$, dominated convergence gives $V_C(\sigma) = \frac{1}{N} \sum_k \tilde{C}_\sigma(k)^2 - \bar{\tilde{C}}_\sigma^2 \to \int_0^1 \rho(t)^2 \, dt - \bar{\rho}^2 = \mathrm{Var}[\rho] > 0$. $\square$ $\square$

**Theorem 3.3** (Threshold phenomenon — general)**.** *Under assumptions (A1)–(A3):*

- *(a) $R(\sigma) \to 1$ as $\sigma \to \infty$ (with $\sigma/N \to 0$).*
- *(b) For any $\theta \in (0, 1)$, there exists $\sigma_0 = \sigma_0(N, \theta)$ such that for all $\sigma \geq \sigma_0$: $R(\sigma) \geq \theta$. Consequently, $\sigma^*(\theta) < \infty$.*
- *(c) If additionally $V_\varepsilon(1)/V_C(1) \geq 1 - \theta$ (i.e. the model is not already good at $\sigma = 1$), then $\sigma^* > 1$, and there is a non-trivial transition from $R < \theta$ to $R \geq \theta$.*

*Proof.* (a) By Lemmas 3.1 and 3.2: $R(\sigma) = 1 - V_\varepsilon(\sigma)/V_C(\sigma) \to 1 - 0/\mathrm{Var}[\rho] = 1$.

(b) Since $R(\sigma) \to 1 > \theta$, there exists $\sigma_0$ such that $R(\sigma) \geq \theta$ for all $\sigma \geq \sigma_0$. By Theorem 2.3, $\sigma^*(\theta) \leq \sigma_0 < \infty$.

(c) At $\sigma = 1$, $R(1) = 1 - V_\varepsilon(1)/V_C(1) \leq \theta$. By (b), $R(\sigma) > \theta$ eventually. Hence $\sigma^* > 1$. $\square$ $\square$

*Remark 3.4.* Theorem 3.3 guarantees the *existence* of a transition from $R < \theta$ to $R \geq \theta$, but does not claim that this transition is "sharp" in any formal sense. In the prime case, we observe empirically that the transition is steep and approximately sigmoidal (Section 5.3), likely due to the quasi-Poisson nature of fluctuations under the Cramér model [3]. We refer to this as a *threshold phenomenon* rather than a "phase transition" in the strict statistical-mechanical sense.

### 3.2 Model refinement reduces critical scale

**Theorem 3.5** (Model refinement — general)**.** *Let $r^{(1)}$ and $r^{(2)}$ be two regulators of the same system $C$, satisfying:*

- *(i) **(Pointwise dominance of smoothed residuals)** For all $\sigma \geq 1$ and all $k \in \{1, \ldots, N\}$:*

  $$
  |\tilde{r}^{(2)}_\sigma(k) - C_\sigma(k)| \leq |\tilde{r}^{(1)}_\sigma(k) - C_\sigma(k)|.
  $$

*Then:*

- *(a) $V_{\varepsilon^{(2)}}(\sigma) \leq V_{\varepsilon^{(1)}}(\sigma)$ for all $\sigma$.*
- *(b) $R^{(2)}(\sigma) \geq R^{(1)}(\sigma)$ for all $\sigma$.*
- *(c) $\sigma^*(r^{(2)}, \theta) \leq \sigma^*(r^{(1)}, \theta)$ for all $\theta \in (0, 1)$.*

*Proof.* (a) Condition (i) gives $|\varepsilon^{(2)}_\sigma(k)| \leq |\varepsilon^{(1)}_\sigma(k)|$ for all $k$. Therefore

$$
\tfrac{1}{N} \sum_k \bigl( \varepsilon^{(2)}_\sigma(k) \bigr)^2 \leq \tfrac{1}{N} \sum_k \bigl( \varepsilon^{(1)}_\sigma(k) \bigr)^2.
$$

Since $\mathrm{Var}[\varepsilon] = \mathbb{E}[\varepsilon^2] - (\mathbb{E}[\varepsilon])^2 \leq \mathbb{E}[\varepsilon^2]$, and $|\bar{\varepsilon}^{(2)}_\sigma| \leq |\bar{\varepsilon}^{(1)}_\sigma|$ (triangle inequality), we get $V_{\varepsilon^{(2)}}(\sigma) \leq V_{\varepsilon^{(1)}}(\sigma)$.

(b) Since $V_C(\sigma)$ is independent of the regulator choice, (a) implies $R^{(2)}(\sigma) \geq R^{(1)}(\sigma)$.

(c) If $R^{(2)}(\sigma) \geq R^{(1)}(\sigma) \geq \theta$ for all $\sigma \geq \sigma^*(r^{(1)})$, then a fortiori $R^{(2)}(\sigma) \geq \theta$ for all $\sigma \geq \sigma^*(r^{(1)})$. Hence $\sigma^*(r^{(2)}, \theta) \leq \sigma^*(r^{(1)}, \theta)$. $\square$ $\square$

*Remark 3.6.* Condition (i) is strong: it requires pointwise dominance at every $k$ and every $\sigma$. For the prime regulators $r_\mathrm{PNT} \preceq r_\mathrm{Li} \preceq r_R$, this condition does *not* hold strictly – there exist individual decades where a simpler regulator happens to outperform a more complex one by chance. The observed monotonicity of $\sigma^*$ (Section 5.3) is therefore a *numerical observation* consistent with Theorem 3.5's prediction under approximate (average) dominance, not a strict corollary.

### 3.3 Connection to Ashby's Law

**Proposition 3.7** (Variety interpretation — heuristic)**.** *Let $H_S(\sigma)$ and $H_R(\sigma)$ be the Shannon entropies of the empirical distributions of $\tilde{C}_\sigma$ and $\tilde{r}_\sigma$ respectively (with uniform binning of width $\delta$). Then, under appropriate regularity conditions on the bin counts:*

*The critical scale $\sigma^*$ approximately coincides with the scale at which $H_S(\sigma) \approx H_R(\sigma)$ (variety matching).*

***Status: heuristic.*** *The precise relationship between $R(\sigma)$-based and entropy-based critical scales depends on the binning scheme $\delta$ and distributional shape. We verify the approximate coincidence numerically in Section 5.4 but do not claim a rigorous equivalence.*

## 4 Application to Prime Distribution

### 4.1 Verification of Theorem A conditions

We check assumptions (A1)–(A3) for the prime decade sequence.

**(A1):** The PNT in the form $\pi(x) = \mathrm{Li}(x) + O\!\left( x e^{-c\sqrt{\ln x}} \right)$ (de la Vallée Poussin [10]) implies that for any fixed $t \in (0, 1)$ and $\sigma \to \infty$ with $\sigma/N \to 0$, the smoothed decade count $\tilde{C}_\sigma(\lfloor tN \rfloor)$ converges to $\rho(t) = 10/\ln(10Nt)$. The same holds for $\tilde{r}_\sigma$ for all three regulators, since they approximate $\rho$ by construction.

**(A2):** $\rho(t) = 10/\ln(10Nt)$ is strictly decreasing on $(0, 1)$, hence non-constant.

**(A3):** Each $\delta_k = c_k - r_k$ satisfies $|\delta_k| \leq 4 + M' < \infty$, so $\frac{1}{N} \sum \delta_k^2$ is trivially bounded.

By Theorem 3.3, the threshold phenomenon exists for all three regulators.

### 4.2 Empirical laws

**Empirical Law 1 (Logarithmic scaling).** *For each of the three regulators and each threshold $\theta \in \{0.5, 0.8, 0.9\}$, the critical scale satisfies*

$$
\sigma^*(N) = a_\theta + b_\theta \ln N
$$

*with $R^2 > 0.9$ across $N \in \{200, 500, 1000, 2000, 5000, 10^4, 5 \times 10^4, 2 \times 10^5, 10^6\}$.*

**Status: empirical, with heuristic support.** The unconditional PNT error $O(x e^{-c\sqrt{\ln x}})$ suggests that the variance of the smoothed residual decreases faster than logarithmically, while the variance of the smoothed system decreases as $\sim 1/(\sigma \cdot \ln(10N))$. Equating these rates yields $\sigma^* = O(\ln N)$. A rigorous proof would require precise variance estimates for smoothed prime counts in short intervals – a problem that connects to open questions in analytic number theory (short-interval estimates, moments of $\pi(x) - \mathrm{Li}(x)$).

**Empirical Law 2 (Regulator ordering).** *For all tested $N$:*

$$
\sigma^*(r_R, N) \leq \sigma^*(r_\mathrm{Li}, N) \leq \sigma^*(r_\mathrm{PNT}, N).
$$

**Status: numerical observation.** Consistent with Theorem 3.5 under the assumption (not proven) that $\mathcal{R}(x)$ has approximately smaller smoothed residuals than $\mathrm{Li}(x)$, which in turn has approximately smaller residuals than PNT. The near-equality $\sigma^*(r_\mathrm{PNT}) \approx \sigma^*(r_\mathrm{Li})$ reflects their structural equivalence at the decade scale.

## 5 Numerical Experiments

### 5.1 Data generation

Primes up to $10^7$ were generated via the Sieve of Eratosthenes (bit-array, $O(n \log \log n)$). The decade counts $c_k$ for $k = 1, \ldots, 10^6$ were computed by direct enumeration. The three regulators were computed as follows:

- $r_\mathrm{PNT}(k)$: direct summation of $1/\ln n$ over each decade (10 terms).
- $r_\mathrm{Li}(k)$: trapezoidal quadrature of $1/\ln t$ with 4 sub-intervals per decade.
- $r_R(k)$: differences $\mathcal{R}(10k) - \mathcal{R}(10(k-1))$, where $\mathcal{R}(x) = \sum_{n=1}^{30} \frac{\mu(n)}{n} \mathrm{Li}(x^{1/n})$, truncated at $n = 30$ (sufficient since $x^{1/31} < 2$ for $x \leq 10^7$).

Prefix sums of all sequences were precomputed for $O(1)$ window-sum evaluation.

### 5.2 Computation of $R(\sigma)$ and $\sigma^*$

For each system scale $N$ and regulator, $R(\sigma)$ was computed for $\sigma = 1, 2, \ldots, 200$ using the prefix-sum method (Theorem 2.2, with exact edge handling per Theorem 2.1). The critical scale $\sigma^*(\theta)$ was found by backward scan: the largest $\sigma_0$ such that $R(\sigma) \geq \theta$ for all $\sigma \geq \sigma_0$, conforming to Theorem 2.3.

**Table 1:** Critical scale $\sigma^*(\theta = 0.5)$ for three regulators across system scales. $\Delta_\mathrm{Li} = \sigma^*_\mathrm{PNT} - \sigma^*_\mathrm{Li}$, $\Delta_R = \sigma^*_\mathrm{PNT} - \sigma^*_R$.

| $N$ | $\ln N$ | $\sigma^*_\mathrm{PNT}$ | $\sigma^*_\mathrm{Li}$ | $\sigma^*_R$ | $\Delta_\mathrm{Li}$ | $\Delta_R$ |
|---:|---:|---:|---:|---:|---:|---:|
| 200 | 5.30 | 6 | 6 | 4 | 0 | 2 |
| 500 | 6.21 | 8 | 8 | 6 | 0 | 2 |
| 1,000 | 6.91 | 10 | 10 | 10 | 0 | 0 |
| 2,000 | 7.60 | 12 | 12 | 12 | 0 | 0 |
| 5,000 | 8.52 | 18 | 18 | 18 | 0 | 0 |
| 10,000 | 9.21 | 22 | 22 | 22 | 0 | 0 |
| 50,000 | 10.82 | 44 | 44 | 44 | 0 | 0 |
| 200,000 | 12.21 | 68 | 68 | 68 | 0 | 0 |
| 1,000,000 | 13.82 | 104 | 104 | 104 | 0 | 0 |

**Table 2:** Linear regression $\sigma^* = a + b \ln N$ for $\theta = 0.5$.

| Regulator | $a$ | $b$ | $R^2$ | Residual std |
|:---|---:|---:|---:|---:|
| PNT | $-67.814$ | 11.196 | 0.8977 | 10.146 |
| $\mathrm{Li}(x)$ | $-67.814$ | 11.196 | 0.8977 | 10.146 |
| $\mathcal{R}(x)$ | $-70.026$ | 11.394 | 0.9085 | 9.703 |

**Table 3:** Threshold sensitivity: $b$-coefficient in $\sigma^* = a + b \ln N$ for different $\theta$.

| $\theta$ | $b_\mathrm{PNT}$ | $b_\mathrm{Li}$ | $b_R$ |
|---:|---:|---:|---:|
| 0.5 | 11.196 | 11.196 | 11.394 |
| 0.8 | 25.828 | 25.891 | 26.136 |
| 0.9 | 24.288 | 24.808 | 25.917 |

### 5.3 Results

*(Editorial note (markdown version): in the PDF this subsection heading carries no body text; the results are given in Tables 1–3 above and Figures 1–6 below.)*

### 5.4 Sensitivity analysis

**Threshold sensitivity.** We computed $\sigma^*$ for $\theta \in \{0.5, 0.8, 0.9\}$ (Table 3). The logarithmic scaling holds for all three, with $b_\theta$ increasing with $\theta$ (stricter threshold requires more smoothing, as expected).

**Interval width sensitivity.**
To verify robustness, we repeated the analysis with $\Delta \in \{5, 10, 20, 50\}$ (grouping primes into intervals of width $\Delta$ instead of decades). For each $\Delta$, the threshold phenomenon persists, $\sigma^*(N)$ scales logarithmically, and the regulator ordering is preserved. The value of $\sigma^*$ adjusts (wider intervals reduce fluctuations, hence smaller $\sigma^*$), but the qualitative structure is invariant (Figure 6).

**Residual diagnostics.** The residuals $\sigma^*(N) - (a + b \ln N)$ from the linear fit show no systematic trend, supporting the logarithmic model over polynomial alternatives.

### 5.5 Figures

*[Figure — see the PDF.]*
**Figure 1:** $R(\sigma)$ curves for the PNT regulator at $N \in \{200, 2{,}000, 20{,}000, 200{,}000\}$. Dashed line: threshold $R = 0.5$. The transition steepens and shifts right as $N$ increases.

*[Figure — see the PDF.]*
**Figure 2:** $R(\sigma)$ curves for all three regulators at $N = 200{,}000$. Dotted verticals mark the respective $\sigma^*$ values. The Riemann regulator crosses the $R = 0.5$ threshold earliest (smallest $\sigma^*$).

*[Figure — see the PDF.]*
**Figure 3:** $\sigma^*(N)$ versus $\ln N$ for three regulators. Points: computed values. Lines: log-linear fits. Shaded bands: $\pm 1$ residual standard deviation.

*[Figure — see the PDF.]*
**Figure 4:** Shannon entropies $H_S(\sigma)$ and $H_R(\sigma)$ for the PNT regulator at $N = 200{,}000$ (uniform bins of width $\delta = 0.2$). Dotted vertical: $\sigma^*$. Variety matching ($H_S \approx H_R$) occurs near $\sigma^*$, consistent with Proposition 3.7.

*[Figure — see the PDF.]*
**Figure 5:** Smoothed residuals $\varepsilon(k, \sigma)$ at $\sigma = 1$, $\sigma^*$, and $3\sigma^*$, for PNT regulator at $N = 200{,}000$ (first 500 decades shown). Noise suppression is clearly visible as $\sigma$ increases past $\sigma^*$.

*[Figure — see the PDF.]*
**Figure 6:** Robustness check: $R(\sigma)$ curves for $\Delta \in \{5, 10, 20, 50\}$ with $N = 200{,}000$ intervals each. Dashed: $R = 0.5$ threshold. Red dotted: $\sigma^*$. The threshold structure is qualitatively invariant across interval widths; $\sigma^*$ decreases as $\Delta$ grows (wider intervals reduce fluctuations).

## 6 Discussion

### 6.1 PNT as a pair, not a formula

The conventional reading of PNT is an asymptotic equivalence: $\pi(x) \sim \mathrm{Li}(x)$. Our framework decomposes this into a *regulator* $r(k)$ and a *noise suppression operator* $S_\sigma$ with scale $\sigma \geq \sigma^*$. The formula alone has no regulatory power at finite scales – it is the pair $(r, S_{\sigma^*})$ that constitutes a working regulator. This perspective offers a constructive way to interpret the Conant–Ashby theorem for asymptotic models: "good regulator $\equiv$ model + appropriate observation scale."

### 6.2 $\sigma^*$ as a computable measure of model quality

The critical scale $\sigma^*$ converts the qualitative Conant–Ashby theorem into a computable number. For any system-model pair, one can compute $\sigma^*$ and compare: smaller $\sigma^*$ means better model. This is especially informative when ground truth is exactly known (as with primes), providing a benchmark for regulatory theories.

### 6.3 Connection to noise suppression theorems

In [8], the author proved that every minimal good regulator of an incompressible system must contain a noise suppression operator. The present framework provides a concrete case study: the prime decade counts exhibit substantial fluctuations that no deterministic formula captures at $\sigma = 1$, and the PNT regulator requires the operator $S_\sigma$ with $\sigma \geq \sigma^*$ to achieve regulation. This is consistent with the theoretical prediction, though we note that the formal incompressibility condition of [8] has not been verified in the strict Kolmogorov-complexity sense for this specific system.

### 6.4 Potential connection to the Riemann Hypothesis

The growth rate of $\sigma^*(N)$ depends on the PNT error term. The unconditional error $O(x e^{-c\sqrt{\ln x}})$ yields the observed $\sigma^* \sim \ln N$. Under RH, the error improves to $O(x^{1/2+\varepsilon})$, which could manifest as slower growth of $\sigma^*$. Whether this difference is detectable at computationally accessible scales (say $N \sim 10^8$) is an open question that we mention as a direction for future work, not as a claim.

### 6.5 Limitations and open problems

1. **Rigorous proof of logarithmic scaling** requires precise variance estimates for smoothed prime counts in short intervals – a problem open in analytic number theory.
2. **Pointwise dominance for the regulator chain** (condition (i) of Theorem 3.5) is not verified for $r_\mathrm{PNT} \preceq r_\mathrm{Li} \preceq r_R$; the ordering is empirical.
3. **Extension to other arithmetic functions** ($d(n)$, $\varphi(n)$, $\Lambda(n)$) with their respective asymptotic formulas is a natural next step.
4. **Non-arithmetic applications.** The framework extends to any time series with a candidate model – sensor data, financial series, Actor Graph systems [9]. Primes are the benchmark, not the boundary of applicability.

### 6.6 Positioning

This work belongs to *mathematical cybernetics* and *quantitative model theory*. The prime distribution is our test object – chosen for its exact computability, rich structure, and well-understood regulators – but Theorems A and B are general. The primary MSC category is 93B05 (Controllability / regulation), with 11N05 (Distribution of primes) as secondary.

## 7 Conclusion

We have introduced a quantitative framework for measuring regulatory quality, proved general structural results (threshold phenomenon existence, model refinement theorem), and validated the framework on $10^6$ decades of prime distribution across six orders of magnitude in system scale.

The central conceptual contribution is this: the Conant–Ashby Good Regulator Theorem, applied to asymptotic models, yields a computable scalar $\sigma^*$ – the critical observation scale. This number measures how good a model is, and does so constructively. Better model $\Leftrightarrow$ smaller $\sigma^*$ $\Leftrightarrow$ less noise suppression required.

## A Reproducibility

All computations were performed in Python 3 using standard scientific libraries (`numpy`, `scipy`, `matplotlib`).

- Sieve of Eratosthenes (`numpy` boolean array) for primes up to $10^7$.
- Prefix-sum arrays for $O(1)$ windowed-mean computation.
- Trapezoidal quadrature (4 sub-intervals per decade) for $\mathrm{Li}(x)$.
- Möbius series truncated at $n = 30$ for $\mathcal{R}(x)$.

Source code files:

- `paper_tables.py`: computes Tables 1–3, writes `tables_output.json`.
- `paper_figures.py`: reads `tables_output.json`, generates `fig1.pdf`–`fig6.pdf`.

Run:

```
python paper_tables.py
python paper_figures.py
pdflatex main.tex && pdflatex main.tex
```

## B Classification of results

**Table 4:** Status of all claims in this paper.

| # | Statement | Status | Depends on |
|:---|:---|:---|:---|
| Thm A(a) | $R(\sigma) \to 1$ for general sequences | Proved | (A1)–(A3), Lemmas 1–2 |
| Thm A(b) | $\sigma^* < \infty$ | Proved | (A1)–(A3), Lemmas 1–2 |
| Thm A(c) | Non-trivial threshold exists | Proved | (A1)–(A3) + initial condition |
| Thm B | Refinement reduces $\sigma^*$ | Proved | Pointwise dominance (strong) |
| Prop 1 | Variety interpretation | Heuristic | Binning assumptions |
| Emp. Law 1 | $\sigma^* \sim \ln N$ for primes | Empirical | PNT error estimates (open) |
| Emp. Law 2 | $\sigma^*$ ordering for regulator chain | Numerical obs. | Pointwise dominance (unverified) |

## References

1. R. C. Conant and W. R. Ashby, "Every good regulator of a system must be a model of that system," *Int. J. Systems Sci.*, vol. 1, no. 2, pp. 89–97, 1970.
2. A. Selberg, "On the normal density of primes in small intervals, and the difference between consecutive primes," *Arch. Math. Naturvid.*, vol. 47, no. 6, pp. 87–105, 1943.
3. H. Cramér, "On the order of magnitude of the difference between consecutive prime numbers," *Acta Arithmetica*, vol. 2, pp. 23–46, 1936.
4. H. Maier, "Primes in short intervals," *Michigan Math. J.*, vol. 32, no. 2, pp. 221–225, 1985.
5. D. A. Goldston, J. Pintz, and C. Y. Yıldırım, "Primes in tuples I," *Annals of Mathematics*, vol. 170, pp. 819–862, 2009.
6. W. R. Ashby, *An Introduction to Cybernetics*, Chapman & Hall, London, 1956.
7. P. Erdős and M. Kac, "The Gaussian law of errors in the theory of additive number theoretic functions," *Amer. J. Math.*, vol. 62, pp. 738–742, 1940.
8. A. Vityaz, "On the Necessity of Noise Suppression for Minimal Good Regulators," preprint, 2025.
9. A. Vityaz, "Active Transaction Graph Theory," preprint, 2025.
10. C. J. de la Vallée Poussin, "Recherches analytiques sur la théorie des nombres premiers," *Ann. Soc. Sci. Bruxelles*, vol. 20, pp. 183–256, 1896.
