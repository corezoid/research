---
title: "The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-06-18
doi: 10.5281/zenodo.20745927
version: v1
license: CC-BY-4.0
keywords: [Actor Model, law of requisite variety, Conant–Ashby theorem, viability theory, information entropy, anti-concentration, transaction costs, digital twin of an organization, CAP theorem]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.5281/zenodo.20745927](https://doi.org/10.5281/zenodo.20745927).

# The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin

Alexander Vityaz · *Corezoid Inc., Dnipro, Ukraine* · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

**Subject classification:** cybernetics, control theory, information theory, mathematical modeling, distributed systems, institutional economics.

## Abstract

In the practice of digital twins of organizations (DTOs), the boundary of the enterprise is often not instantiated as an independent object of the control model. This paper develops a stochastic model of the firm as a controlled Markov process in which actor membership, interface permeability, and operational dynamics are integrated into a single object of control, while viability is defined as the retention of an essential variable within the homeostatic set $K$. A **necessary condition** for viability in a nonstationary, overloading environment is proved: boundary representation—namely, observability of the membership of causally significant actors and tunability of permeability—is necessary to prevent asymptotic collapse (Theorem 1). A **conditional sufficiency** result is also formulated: if the representation makes it possible to construct a policy with compensated overload and Lyapunov drift toward an optimum, then the system preserves practical (recurrent) viability (Theorem 2). The bridge "residual entropy $\Rightarrow$ positive risk" is derived through an explicit anti-concentration lemma (Lemma 2), rather than postulated. Distributed and centralized representations are equivalent in policy expressiveness under the idealization of synchronous communication (Theorem 3); when one moves to an asynchronous model with losses, they diverge: a communication lower bound $\Omega(|N(a)|)$ applies to distributed labeling (Lemma 3), whereas a consistency–availability dichotomy applies to the centralized case (Lemma 4), yielding regime-dependent dominance of centralization with respect to the communication component of context-grounding costs (Theorem 4). The engineering implication is the pattern of an **Executable Boundary Actor**, $Actor_{\partial S}$.

**Keywords:** *cybernetics, boundary of the firm, law of requisite variety, viability theory, information-theoretic control, transaction costs, organizational digital twin, distributed systems, Actor Model.*

## 1 Introduction and Positioning

In neo-institutional economics, the firm exists insofar as the costs of internal, directive coordination are lower than the transaction costs of the market price mechanism [1, 4]. The limit of the firm is determined by a boundary at which the marginal cost of internal coordination equals the marginal cost of external coordination.

The idea that a boundary is not merely a line of separation, but a constitutive element of a viable system, is present in cybernetics. In autopoiesis (Maturana and Varela [6]), the membrane is continuously produced by the system for the purpose of self-definition; in Beer's Viable System Model [5], the *System 4* circuit faces the environment and manages permeability. These concepts provide motivation rather than the formal apparatus of the present paper: below, we do not map System 4 directly into the construction, but instead formalize the thesis common to these traditions—that the boundary is controllable.

When moving from descriptive macro-models to systems IT engineering and the architecture of digital twins, a gap emerges: the boundary is implemented physically (firewalls, API gateways) and legally (SLAs), but it is **not algorithmically represented** in the twin's control model. This paper translates the thesis of the constitutive boundary into a rigorous setting in which viability is a measurable event, and proves a necessary condition for boundary representation, supplemented by a conditional sufficiency result (with a gap between the two). The question of distributed versus centralized architecture is reframed as a question of provable bounds on coordination costs.

## 2 Formal Model

### 2.1 Actors, membership, criticality

Let $A$ be a finite set of actors. Each $a \in A$ and time $t \in \mathbb{N}$ is assigned a membership status $z_t(a) \in \{I, E\}$; the vector of memberships is $z_t \in \{I, E\}^A$. The internal system is $S_t = \{a : z_t(a) = I\}$.

An actor is causally significant, or boundary-critical, $a \in A_t^{crit}$, if safe control or the transition of the essential variable is *not invariant* under a flip of that actor's membership: formally, there exists a state in which either the prescribed protocol $\rho_t(a)$ or the distribution of $\xi_{t+1}$ changes when $z_t(a)$ is replaced by $\neg z_t(a)$. In other words, $a$ is critical exactly when the protocols for $I$ and $E$ differ on that actor over a safety-critical set. This separates the definition from the tautology "can have an effect" and embeds the distinguishability of protocols directly into the criterion. The set of move-eligible actors $A_t^{move} \subseteq A$ (whose membership may be changed) generally intersects with, but is not identical to, $A_t^{crit}$: criticality concerns influence, whereas move-eligibility concerns controllability.

### 2.2 State, environment, dynamics

The state is $x_t \in \mathcal{X}$. The environment generates an exogenous process $\theta_t \in \Theta$, noise $w_t$, and topological noise $\nu_t$. Control has three components:

$$u_t = (u_t^{op},\, u_t^{perm},\, u_t^{topo}).$$

Permeability filters the disturbance, topology changes membership, and the operational state evolves with an explicit dependence on the boundary:

$$\theta_t^{eff} = \Pi(\theta_t, u_t^{perm}), \qquad z_{t+1} = G(z_t, u_t^{topo}, \nu_t),$$

$$x_{t+1} = F(x_t, z_t, u_t^{op}, \theta_t^{eff}, w_t), \qquad \xi_t = g(x_t, z_t).$$

Crucially, the disturbance $\theta_t^{eff}$ acts on $x_{t+1}$ (and thereby on $\xi_{t+1}$), rather than on $x_t$. This causal ordering determines the correct indexing of the informational conditions below.

### 2.3 Viability

The essential variable $\xi_t = g(x_t, z_t) \in \Xi$ is kept within the homeostatic set $K \subseteq \Xi$. We assume that $\Xi$ is quantized into a finite number of distinguishable levels, which is natural for operationally distinguishable outcomes; the continuous case requires an analogue based on bounded density, as noted after Lemma 2. Under a policy $\pi$,

$$\mathrm{Viab}_T(\pi) = \{\xi_t \in K \;\; \forall t \leq T\}, \qquad V_T(\pi) = P_\pi(\mathrm{Viab}_T(\pi)).$$

Define the conditional exit risk relative to the viability event as $\bar{q}_t := P(\xi_{t+1} \notin K \mid \mathrm{Viab}_t)$; then, by the chain rule, $V_T(\pi) = \prod_{t<T}(1 - \bar{q}_t)$. The system is **strictly viable** if $\inf_T V_T(\pi) \geq \delta > 0$ (retention forever), which, when $\sup_t \bar{q}_t < 1$, is equivalent to $\sum_t \bar{q}_t < \infty$ (if some $\bar{q}_t = 1$, the product is zero regardless of the sum). Collapse means $V_T(\pi) \to 0$, which follows when $\bar{q}_t \geq \varepsilon > 0$ on time steps of positive density. Under persistent disturbance, strict retention over an infinite horizon is typically unattainable: a persistent small exit risk $q_\infty > 0$ yields $\sum_t q_t = \infty$ and $\prod_t (1 - q_t) = 0$. Therefore we also introduce **practical (recurrent) viability**: the process is positive recurrent to $K$, and $\limsup_T \frac{1}{T} \sum_{t \leq T} P(\xi_t \notin K) \leq \epsilon$ for small $\epsilon$. The necessity result below rules out both forms; sufficiency is naturally formulated for practical viability, with strict viability as a subregime characterized by summable risk.

### 2.4 Information structure

The regulator observes $o_t = O_M(x_t, \theta_t)$, with filtration $\mathcal{F}_t^M = \sigma(o_0, \ldots, o_t)$; admissible policies are $\mathcal{F}_t^M$-measurable and take values in $\mathcal{U}_M$. For actor $a$, the Bayesian error of recognizing membership is

$$e_t(a) = \mathbb{E}\left[\min_{s \in \{I,E\}} P\left(z_t(a) \neq s \mid \mathcal{F}_t^M\right)\right].$$

**Definition (boundary representation).** $M$ represents the boundary, $M \models \partial S$, if: **(i)** for all $a \in A_t^{crit}$, the error $e_t(a) \leq \eta_0$ is small, and for all $a \in A_t^{move}$, `move`$(a) \in \mathcal{U}_M$ is available (implemented through $u_t^{topo}$); **(ii)** $u_t^{perm} \in \mathcal{U}_M$. The notation $M \nvDash \partial S$ means that at least one condition is violated, not that all boundary data are literally absent. Partial representation is possible, for example when $z$ is observable but $u^{perm}$ is unavailable: there exists $a \in A_t^{crit}$ with $e_t(a) \geq \eta > 0$, or `move` is unavailable for drifting actors, or $u_t^{perm} \notin \mathcal{U}_M$.

### 2.5 Finiteness of the regulator

Introduce the *survival filtration* $\mathcal{G}_t := \sigma(\mathrm{Viab}_t, \mathcal{F}_{t-1}^M)$: past observations together with the fact of survival up to time $t$, but *without* the current observation $o_t$. Therefore the action $u_t$, which depends on $o_t$, is not $\mathcal{G}_t$-measurable, and the control term below remains nonzero. Useful control information about the disturbance per time step is bounded:

$$I(\theta_t^{eff}; u_t \mid \mathcal{G}_t) \leq C_R < \infty.$$

*Remark (the dual budget; Future Work).* Observing $z_t^{crit}$ with small $e_t$ under drift itself consumes bandwidth on the order of $\sim H(z_t^{crit})$; strictly speaking, the regulator allocates a single budget between boundary tracking and disturbance regulation. This strengthens the thesis (in a high-drift regime, the boundary-observation budget becomes binding), but a full analysis of the two-loop budget is left for future work.

**Axiom P (protocol discontinuity at the boundary).** In the spirit of the distinction between coordination mechanisms in Coase and Williamson [1, 4], the coordination protocol is discontinuous at the boundary: $\rho_t(I) \neq \rho_t(E)$ on a safety-critical set (a deterministic directive internally, a contractual protocol externally). This is an assumption of the paper, motivated by opportunism and asset specificity [4], rather than something derived from [1].

**Axiom O (informational overload under survival).** The environment is informationally overloading even conditional on survival so far: $H(\theta_t \mid \mathcal{G}_t) \geq C_R + \varepsilon_{dec} + 1 + \log|K| + \Delta$ for some $\Delta > 0$. Conditioning on $\mathcal{G}_t$ (and not only on $\mathcal{F}_{t-1}^M$) is an explicit condition of *survival independence*: survival so far does not make the remaining disturbance benign, thereby excluding survivorship bias when risk estimates are transferred to the event $\mathrm{Viab}_t$. Without overload, the regulatory bound (Lemma 1) is empty, and boundary representation is not necessary; this delineates the domain of applicability.

**Axiom E (safety effect of protocol mismatch).** For a boundary-critical actor $a$, applying a protocol that does not match the true membership ($\hat{\rho}_t(a) \neq \rho_t(a)$) on safety-critical time steps creates a positive conditional exit risk:

$$P\left(\xi_{t+1} \notin K \mid \mathrm{Viab}_t, \hat{\rho}_t(a) \neq \rho_t(a)\right) \geq \gamma > 0.$$

This assumption makes the bridge "dispatching error $\Rightarrow$ risk" explicit: a protocol error at the boundary is not locally compensable, but threatens the essential variable. The motivation is hold-up and asset specificity [4].

## 3 The Informational Limit and the Collapse Condition

**Lemma 1 (lower bound on regulation, correct indexing, and conditioning).** Suppose that the essential variable decodes the effective disturbance that preceded the transition, given the control and the survival history: $H(\theta_t^{eff} \mid \xi_{t+1}, u_t, \mathcal{G}_t) \leq \varepsilon_{dec}$. Then

$$H(\xi_{t+1} \mid \mathcal{G}_t) \geq H(\theta_t^{eff} \mid \mathcal{G}_t) - I(\theta_t^{eff}; u_t \mid \mathcal{G}_t) - \varepsilon_{dec}.$$

*Proof.* $I(\theta_t^{eff}; \xi_{t+1}, u_t \mid \mathcal{G}_t) = H(\theta_t^{eff} \mid \mathcal{G}_t) - H(\theta_t^{eff} \mid \xi_{t+1}, u_t, \mathcal{G}_t) \geq H(\theta_t^{eff} \mid \mathcal{G}_t) - \varepsilon_{dec}$. On the other hand, by the chain rule, $I(\theta_t^{eff}; \xi_{t+1}, u_t \mid \mathcal{G}_t) = I(\theta_t^{eff}; u_t \mid \mathcal{G}_t) + I(\theta_t^{eff}; \xi_{t+1} \mid u_t, \mathcal{G}_t) \leq I(\theta_t^{eff}; u_t \mid \mathcal{G}_t) + H(\xi_{t+1} \mid \mathcal{G}_t)$. Combining the two inequalities yields the claim. □

Conditioning is performed on $\mathcal{G}_t = \sigma(\mathrm{Viab}_t, \mathcal{F}_{t-1}^M)$ (the past plus survival, without the current $o_t$), while the action $u_t$ depends on the *new* observation $o_t \notin \mathcal{G}_t$. Hence the control term $I(\theta_t^{eff}; u_t \mid \mathcal{G}_t)$ is nonzero and is honestly bounded by $\leq C_R$ (§2.5). This is the standard setup of Touchette and Lloyd [11], in which the controller acts on past information. Conditioning on $\mathcal{F}_t^M$ would zero out this term, since $u_t$ would be an $\mathcal{F}_t^M$-measurable constant. The indexing of $\xi_{t+1}$ is consistent with the causal ordering in §2.2: the post-disturbance variable can decode $\theta_t^{eff}$, whereas the upstream variable $\xi_t$ cannot. Under Axiom O, the residual $h_t := H(\theta_t^{eff} \mid \mathcal{G}_t) - C_R - \varepsilon_{dec} \geq 1 + \log|K| + \Delta$ is positive and separated from the threshold; all quantities are conditioned on the same $\mathcal{G}_t$, which avoids mixing conditioning regimes.

**Lemma 2 (anti-concentration: residual entropy $\Rightarrow$ positive risk).** Let $\Xi$ be finite, let $K \subseteq \Xi$, let $K^c = \Xi \setminus K$ with $|K^c| \geq 2$, and suppose that $H(\xi_{t+1} \mid \mathcal{G}_t) \geq h_t$ with $h_t > 1 + \log|K|$. Then the conditional exit risk under survival is

$$q_t := P(\xi_{t+1} \notin K \mid \mathcal{G}_t) \geq \frac{h_t - 1 - \log|K|}{\log|K^c|} =: \varepsilon_{haz} > 0.$$

*Proof.* Let $p_t = P(\xi_{t+1} \in K \mid \mathcal{G}_t) = 1 - q_t$. By the grouping decomposition of entropy with respect to the partition $\Xi = K \sqcup K^c$,

$$H(\xi_{t+1} \mid \mathcal{G}_t) = H_b(p_t) + p_t H(\xi_{t+1} \mid \xi_{t+1} \in K, \cdot) + q_t H(\xi_{t+1} \mid \xi_{t+1} \in K^c, \cdot)$$

$$\leq 1 + p_t \log|K| + q_t \log|K^c|,$$

where $H_b \leq 1$ is binary entropy and the conditional entropies are bounded by the logarithms of the corresponding cardinalities. Since $p_t \leq 1$, we have $h_t \leq 1 + \log|K| + q_t \log|K^c|$, whence $q_t \geq (h_t - 1 - \log|K|)/\log|K^c| > 0$ (the denominator is positive when $|K^c| \geq 2$). □

This is the bridge that was previously relegated to a postulate: under overload (Axiom O $\Rightarrow h_t \geq 1 + \log|K| + \Delta$), exit from homeostasis has a uniformly positive conditional probability $\varepsilon_{haz} \geq \Delta/\log|K^c|$. The formulation is discrete (quantization of $\Xi$, §2.3), which makes the grouping inequality exact and avoids the sign subtleties of differential entropy.

**Corollary 1 (asymptotic collapse).** Because $\mathrm{Viab}_t \in \mathcal{G}_t$, the bound in Lemma 2 transfers to the conditional risk under survival *identically*, without survivorship bias: $\bar{q}_t = P(\xi_{t+1} \notin K \mid \mathrm{Viab}_t) = \mathbb{E}[q_t \mid \mathrm{Viab}_t] \geq \varepsilon_{haz}$ (the inner conditioning on $\mathcal{G}_t$ already incorporates survival so far; this is exactly what the survival-independence condition in Axiom O guarantees). If $\bar{q}_t \geq \varepsilon_{haz}$ on a set of critical time steps of positive density $\kappa_0 \in (0, 1]$, with $\kappa(T) \sim \kappa_0 T \to \infty$, then

$$V_T(\pi) \leq (1 - \varepsilon_{haz})^{\kappa(T)} \to 0.$$

*Proof.* $\mathrm{Viab}_{t_k+1} = \mathrm{Viab}_{t_k} \cap \{\xi_{t_k+1} \in K\}$, so $P(\mathrm{Viab}_{t_k+1}) \leq (1 - \varepsilon_{haz}) P(\mathrm{Viab}_{t_k})$; telescoping yields the bound. The argument uses the tower property and does not require independence between time steps—only a uniform lower bound $\bar{q}_t \geq \varepsilon_{haz}$ over the survival history. □

## 4 Necessity and Sufficiency

**Axiom NS (nonstationarity of the environment).** (a) The transaction-cost-optimal configuration $z_t^*$ drifts: on a set of time steps of positive density, $\Pr(z_{t+1}^* \neq z_t^*) \geq \beta > 0$. (b, disjunctive) The required level of filtering drifts, so that *no* fixed, uncontrolled filter $\Pi_0$ can continuously preserve the balance: for any $\Pi_0$, on a set of time steps of positive density, at least one of the following two horns holds:

- **under-filtering:** $H(\Pi_0(\theta_t) \mid \mathcal{G}_t) \geq C_R + \varepsilon_{dec} + 1 + \log|K| + \Delta$ (the filter passes excessive variety); **or**

- **over-filtering:** under $\Pi_0$, the decodability condition of Lemma 1 / the inflow of required input is violated: $\theta_t^{eff} = \Pi_0(\theta_t)$ is so impoverished that the operational state $x_{t+1} = F(\cdot, \theta_t^{eff}, \cdot)$ does not receive the input needed to retain $\xi$, and $P(\xi_{t+1} \notin K \mid \mathcal{G}_t) \geq \varepsilon' > 0$ (the filter cuts off useful signal; isolation leads to "starvation").

The disjunction is justified by nonstationarity: a fixed filter is tuned to one level, whereas the required level drifts. Therefore, on some time steps it under-filters (the environment has become noisier than the threshold), and on others it over-filters (the environment has become quieter while the filter still removes needed input). The trivial filter $\Pi_0 \equiv c$ falls into the over-filtering horn. This removes the falsity of the earlier universal form, in which the trivial filter with $H = 0$ was a counterexample.

**Theorem 1 (necessity of boundary representation).** *Under Axioms O, P, and NS, and finite regulator capacity $C_R < \infty$: if $M \nvDash \partial S$, then $V_T(\pi) \to 0$ for every admissible $\pi$.*

*Proof.* A violation of representation is a failure of (i) or (ii).

**Case 1 (no controllable permeability).** $u^{perm} \notin \mathcal{U}_M$ means that the regulator cannot change the filter; therefore $\theta_t^{eff} = \Pi_0(\theta_t)$ for some fixed, uncontrolled $\Pi_0$. By the disjunctive Axiom NS(b), one of the two horns is triggered on time steps of positive density. **Under-filtering horn:** $H(\Pi_0(\theta_t) \mid \mathcal{G}_t)$ is at least the threshold; by Lemma 1, the residual satisfies $h_t \geq 1 + \log|K| + \Delta$, and by Lemma 2, $\bar{q}_t \geq \varepsilon_{haz}$. **Over-filtering horn:** the inflow is impoverished, and $\bar{q}_t \geq \varepsilon' > 0$ directly (input deprivation: the firm "starves"). In both cases, $\bar{q}_t$ is bounded away from zero on time steps of positive density; by Corollary 1, $V_T \to 0$. Thus every static firewall, including the trivial $\Pi_0 \equiv c$, is covered: it either lets noise through or cuts off signal, and both horns lead to collapse.

**Case 2a (unobservability; relying on Axiom E).** There exists $a \in A_t^{crit}$ with $e_t(a) \geq \eta$. By the definition of criticality (§2.1) and Axiom P, the protocols for $I/E$ differ on a safety-critical set; therefore a Bayesian error $e_t(a) \geq \eta$ entails a probability of protocol mismatch $P(\hat{\rho}_t(a) \neq \rho_t(a) \mid \mathrm{Viab}_t) \geq \eta$. By Axiom E, each mismatch produces an exit risk of at least $\gamma$, hence

$$\bar{q}_t = P(\xi_{t+1} \notin K \mid \mathrm{Viab}_t) \geq \eta\gamma > 0$$

on time steps of positive density; by Corollary 1, $V_T \to 0$. This is the only case that relies on postulate E; the necessity results for permeability (Case 1) and controllability (Case 2b) are derived without it. The formulation in terms of Bayesian error allows partial predictability of $z$.

**Case 2b (uncontrollability).** $z_t$ is frozen (`move` $\notin \mathcal{U}_M$), while $z_t^*$ drifts (NS(a)). Define the mismatch loss $\ell(z_t, z_t^*) = \mathbb{E}[$ difference in expected coordination costs under $z_t$ versus $z_t^*] \geq 0$. Since $A$ is finite, the instantaneous gap $\|z_t - z_t^*\| \leq |A|$ is bounded. Suppose that on a set of time steps of *positive density* $\kappa_0 \in (0, 1]$ (a Cesàro condition), $\mathbb{E}[\ell(z_t, z_t^*)] \geq c > 0$; then the accumulated debt $L_T = \sum_{t \leq T} \ell$ satisfies $\mathbb{E} L_T \geq c\kappa_0 T$.

The accumulated mismatch loss $L_T$ is a control-theoretic quantity rather than, by itself, an accounting recognition rule. When the persistence of $z_t \neq z_t^*$ results from an unmade, deferred, or unexecuted boundary decision and produces an observable consequence, it may satisfy the recognition conditions for management debt developed in [19] ([Management Debt—Part I](../2026-management-debt-part-i/)). This supplies a possible accounting layer for attributing materialised boundary losses to the responsible Decision Owner.

Let the margin satisfy $m_{t+1} = m_t - \ell(z_t, z_t^*) + r_t$, with bounded increments $|m_{t+1} - m_t| \leq b$ and drift $\mathbb{E}[\ell - r \mid \mathcal{F}_t] \geq c' > 0$. Decompose $m_t = m_0 + M_t - D_t$, where $M_t = \sum_{s<t}(m_{s+1} - m_s - \mathbb{E}[m_{s+1} - m_s \mid \mathcal{F}_s])$ is a martingale with bounded increments, and $D_t \geq c'\kappa_0 t$ is accumulated drift. By Azuma's inequality, $|M_t| = O(\sqrt{t \log t})$ almost surely (Borel–Cantelli), whereas $D_t$ grows linearly. Hence $m_t \leq m_0 - c'\kappa_0 t + O(\sqrt{t \log t}) \to -\infty$ almost surely, and the boundary of $K$ (the margin-depletion threshold) is reached with probability tending to 1. Therefore $V_T \to 0$. *(This uses Azuma's inequality and divergence of drift to $-\infty$, rather than a supermartingale convergence theorem, which would yield a finite limit.)* ∎

*Remark (coverage of practical viability).* In all three cases, not only strict viability but also practical viability is violated: when $M \nvDash \partial S$, the regulator lacks the lever—filtering, dispatching, or movement—by which $\xi$ can be returned to $K$. Therefore $\limsup_T \frac{1}{T} \sum_t P(\xi_t \notin K)$ is bounded away from zero. The necessity of representation thus rules out both forms of viability.

**Theorem 2 (conditional sufficiency through Lyapunov drift).** *Assume: (S1) $M$ represents the boundary; (S2) overload is compensated by available filtering—after optimal filtering, residual variety fits within capacity, $H(\theta_t^{eff} \mid \mathcal{G}_t) \leq C_R$ (then $h_t \leq 0 < 1 + \log|K|$, and Lemma 2 does not force exit).*

*Furthermore, suppose: (S3) there exists a Lyapunov function $V : \Xi \to [0, \infty)$, bounded on $K$, and constants $\lambda < 1$, $b < \infty$ such that the following drift condition holds relative to the process state:*

$$\mathbb{E}[V(\xi_{t+1}) \mid x_t, z_t] \leq \lambda V(\xi_t) + b \mathbf{1}\{\xi_t \in K\}.$$

*Then the process $\xi_t$ is positive recurrent to $K$ at a geometric rate; the system is practically viable. In the subregime of summable risk ($\sum_t \bar{q}_t < \infty$—for example, a vanishing disturbance or an absorbing safe kernel in $K$), strict viability $\inf_T V_T \geq \delta > 0$ is also attainable.*

*Proof.* Condition (S3) is the standard Foster–Lyapunov drift condition [17]; outside $K$, the drift is strictly negative ($\mathbb{E}[V(\xi_{t+1}) \mid x_t, z_t] \leq \lambda V(\xi_t)$, $\lambda < 1$), which implies geometric ergodicity and an exponential tail bound for the return time to $K$. Hence $\limsup_T \frac{1}{T} \sum_{t \leq T} P(\xi_t \notin K) \leq \epsilon$, i.e., practical viability. Condition (S2) ensures that residual entropy does not force exit through Lemma 2, thereby making the drift in (S3) implementable by the available control. For strict viability under summable risk: $V_T = \prod_{t<T}(1 - \bar{q}_t)$, and if $\sup_t \bar{q}_t < 1$ and $\sum_t \bar{q}_t < \infty$, then $\prod_t (1 - \bar{q}_t) \geq \exp\left(-\frac{1}{1 - \sup \bar{q}_t} \sum_t \bar{q}_t\right) > 0$ (using $\ln(1-x) \geq -x/(1-x)$), whence $\inf_T V_T \geq \delta > 0$. □

*Remark.* Condition (S3) is not an "inverse" of Lemma 2: low entropy by itself does not concentrate mass in $K$ (it may concentrate in $K^c$ when $|K^c| \geq |K|$). An active pull of the mode into $K$ by the policy's drift is required, and this is precisely what (S3) provides. Under persistent disturbance, strict retention forever is unattainable ($\bar{q}_t \to \bar{q}_\infty > 0$), and the naturally attainable object is practical recurrence.

Taken together, Theorems 1 and 2 give a **necessary condition and conditional sufficiency** (not a full characterization: necessity rests on representation, whereas sufficiency also relies on the independent constructive conditions (S2)–(S3), so a gap remains between them). Under overload, boundary representation is necessary for viability, both strict and practical; under compensated overload and Lyapunov drift toward the optimum, it is sufficient for practical viability, and for strict viability in the subregime of summable risk. This is substantially stronger than a one-sided necessary condition, but it does not identify the two conditions.

## 5 Equivalence of Architectures and the Costs of Centralization

**Theorem 3 (equivalence in expressiveness; idealization).** *Under the idealization of synchronous, reliable communication with zero message cost: let $R_{dist}$ be distributed labeling (the attribute $z_t(a)$ is local to nodes), and let $R_{cent}$ be a centralized meta-actor; assume that both represent the boundary. Then the classes of achievable viable policies coincide:* $\mathrm{Pol}(R_{dist}) = \mathrm{Pol}(R_{cent})$.

*Proof (simulation relation).* Construct a simulation in both directions. Forward: $R_{cent}$ simulates the policy of $R_{dist}$ by answering each local query with the value from the registry (in the synchronous model, instantaneously and exactly), so the filtration of observations coincides. Reverse: $R_{dist}$ simulates $R_{cent}$ by synchronously replicating the registry to all nodes. In both cases, the observed $\sigma$-algebra and the image of actions coincide; therefore the measurable policies and their achievable outcomes are identical. □

*Remark (breakdown of the idealization).* Theorem 3 is valid *only* under free synchronous communication. The remainder of §5 formalizes precisely the breakdown of this idealization: in an asynchronous model with losses (partitions), the implementations no longer induce the same filtration within bounded time, and the equivalence disappears. The difference between architectures lies not in expressiveness, but in cost and availability when one moves to a realistic model.

Fix this model as follows: asynchronous message passing with arbitrary delays and losses. In $R_{dist}$, membership $z(a)$ is replicated across $N(a)$—the nodes that store a copy and initiate boundary-critical transactions. Correctness of `move`$(a)$ is linearizability: after the linearization point, no transaction is dispatched using an outdated value.

**Lemma 3 (communication lower bound $\Omega(|N(a)|)$).** *Any protocol that correctly implements an eager-atomic* `move`$(a)$ *in $R_{dist}$ requires at least $|N(a)| - 1$ successfully delivered (acknowledged) notifications per transition in any successful execution.*

*Proof (indistinguishability; cf. lower bounds for atomic snapshot and write-all [13]).* If a node $n \in N(a)$, distinct from the coordinator, receives no notification, then the scenarios "move executed" ($z(a) = v'$) and "move did not occur" ($z(a) = v$) are indistinguishable for $n$: the same empty history and identical local state. Then $n$ dispatches a transaction using the stale value $v \neq v'$, violating linearizability. Hence each of the $|N(a)| - 1$ nodes must *receive* (not merely be sent) at least one notification. □

*Remark.* The bound is for eager (push) protocols and for *delivered* notifications; message loss in the asynchronous model only increases the expected number of *send attempts* needed to achieve $|N(a)| - 1$ deliveries, thereby strengthening the lower bound on cost. Lazy (pull) protocols, in which a node queries the owner on each transaction, shift the cost to reads and reduce to the centralized model (Lemma 4).

**Lemma 4 (consistency–availability dichotomy).** *Define $\delta_{avail} = \limsup_t P(\text{response time} > \tau)$ and $\delta_{cons} = P(\text{dispatch using stale } z)$. In an asynchronous model with partitions, it is impossible to have both $\delta_{avail} = 0$ and $\delta_{cons} = 0$.*

*Proof (partition; cf. CAP [12], FLP [14]).* Partition the network between $A_{\partial S}$ and node $n$. The coordinator performs `move`$(a) : v \to v'$ in $O(1)$ time on its side. Node $n$ initiates a transaction. If $n$ responds within $\leq \tau$ ($\delta_{avail} = 0$), it has not received $v'$ and dispatches using $v$ ($\delta_{cons} > 0$). If $n$ waits for a linearizable value ($\delta_{cons} = 0$), it blocks until the partition is resolved ($\delta_{avail} > 0$). The conjunction is impossible. In particular, an $O(1)$ write with $\delta_{cons} \approx 0$ entails $\delta_{avail} > 0$. □

**Theorem 4 (regime-dependent dominance in communication cost).** *Let $\mu = \mu(\pi) \leq \beta$ be the endogenous frequency of executed moves (a control variable: the policy tolerates mismatch in order to economize on moves—Coasian hysteresis), rather than the drift frequency $\beta$. Then the expected communication cost of a write/topological move is* $\Theta(\mu |N(a)|)$ *in $R_{dist}$ (Lemma 3), and* $\Theta(\mu)$ *in $R_{cent}$ when $\delta_{cons} \approx 0$, at the cost of $\delta_{avail} > 0$ (Lemma 4). The gap* $\Theta(\mu(|N(a)| - 1))$ *is positive when $\mu > 0$ and $|N(a)| \geq 2$, and grows without bound as connectivity $|N(a)|$ increases, provided that $\mu$ is bounded away from zero.* ∎

*Qualification on the scale of the cost.* The estimate $\Theta(\mu)$ for $R_{cent}$ concerns the communication cost of the *write/move path*, not the total cost of all runtime-read transactions: centralization can shift cost from the write path to the read path, because every boundary-critical node may have to read from $A_{\partial S}$. The full cost is accounted for through $Cost_{Grounding}$ (§6); the theorem is limited specifically to the write/move component.

**Corollary.** A centralized $A_{\partial S}$ is not a logical necessity (Theorem 3), but it dominates in cost with respect to the *communication write component* under $\mu > 0$, dense connectivity among critical nodes, and critical consistency—while provably shifting risk from consistency to availability (Lemma 4). The optimal frequency of moves $\mu^*$ is endogenous and is typically strictly smaller than $\beta$: boundary hysteresis is a consequence, not a defect.

## 6 Context-Grounding Costs and the $Actor_{\partial S}$ Pattern

**Formalization of the Cost of Grounding.** Decompose the cost of context grounding under a topological move into two components:

$$Cost_{Grounding}(\texttt{move}) = \underbrace{c_{msg} \cdot M(\texttt{move})}_{\text{communication}} + \underbrace{c_{err} \cdot P(\text{protocol error})}_{\text{semantic}},$$

where $M(\texttt{move})$ is the number of coordination messages, and $c_{msg}, c_{err}$ are unit costs. Theorems 3–4 bound the *communication* component: Lemma 3 gives $M \geq |N(a)| - 1$ in a distributed implementation. The semantic component (restoring shared context in Clark's sense [9]) and the organizational cost of a move (contract renegotiation, asset transfer—at a different time scale) are not bounded by the theorems and enter as motivation rather than formal claims. This removes the earlier conflation of "grounding" with message complexity.

In the Actor Model paradigm [10], and more specifically in the transactional interpretation of actors developed in [Active Transaction Graphs](../2026-active-transaction-graphs/) [18], boundary representation crystallizes into the root object $Actor_{\partial S}$. In this interpretation, the boundary actor is not merely a registry of membership states, but a transactional mediator that binds actor status, protocol selection, permeability control, traceability, and accounting consequences into a single executable object:

$$Actor_{\partial S} = \langle z_t,\, \rho_t,\, \Pi_t,\, IAM_t,\, SLA_t,\, c_t,\, Cost_{Grounding},\, \Delta Benefit,\, \texttt{move\_inside()},\, \texttt{move\_outside()} \rangle.$$

where $z_t$ is the single source of truth about membership; $\rho_t$ is the protocol map (directive/contract/API, renamed from the earlier $\pi$ to avoid collision with policy); $\Pi_t$ is the implementation of controllable filtering $\Pi(\cdot, u_t^{perm})$; $IAM_t, SLA_t$ are external constraints and obligations; $c_t, Cost_{Grounding}$ are cost functions; $\Delta Benefit(a) = \mathbb{E}[\ell(z_t, z_t^*) - \ell(G(z_t, \texttt{move}(a)), z_t^*)] - Cost(\texttt{move}(a))$ is the marginal Coasian *benefit* of a specific move `move`$(a)$ net of its cost (the move is beneficial when $\Delta Benefit(a) > 0$; this generates the hysteresis in Theorem 4—when marginal benefit is small, the policy tolerates mismatch); and `move_inside`, `move_outside` are atomic operations implementing $u_t^{topo}$.

The accounting component of $Actor_{\partial S}$ may therefore include management-debt postings associated with delayed or omitted boundary moves, subject to the recognition and attribution rules of [19].

## 7 Related Work

The positioning is worth emphasizing separately. **Cybernetics of the boundary:** the VSM [5] (System 4 as an environment-facing circuit) and autopoiesis [6] (the constitutive membrane) provide the qualitative thesis; the contribution here is its computable formalization with a measurable viability condition. **Transaction-cost economics:** Coase [1] explains the existence of the boundary, while Williamson [4] explains its position through opportunism, asset specificity, and hold-up; these are precisely the mechanisms that make observing membership costly (linked here to Axiom P and endogenous $\eta$). **Boundary dynamics:** the literature on make-or-buy decisions under uncertainty and real options on integration is a direct competitor in the formulation of the question "when should the boundary move?"; the present paper differs by using an informational rather than a contractual criterion. **Digital twins:** unlike standards for architecture description [8], the relevant objects are executable twins and organization-as-POMDP formulations; it is against them that the thesis of algorithmic blindness is directed. **Informational limits:** Lemma 1 is an application of the information-theoretic form of the good-regulator theorem [3] (rather than the law of requisite variety [2], which merely motivates overload) to the essential variable of the boundary; the novelty is not the entropy bound itself [11], but its coupling with anti-concentration (Lemma 2) into a collapse condition.

## 8 Conclusion and Future Work

This paper gives a necessary condition and a conditional sufficiency result: in a nonstationary, overloading environment and under a finite regulator, boundary representation—the observability of the membership of causally significant actors and the tunability of permeability—is *necessary* for viability (Theorem 1, both strict and practical) and, under compensated overload with Lyapunov drift toward the optimum, *sufficient* for practical (recurrent) viability (Theorem 2). Strict retention forever is a subregime characterized by summable risk. A gap remains between the necessary and sufficient conditions: sufficiency relies on additional constructive assumptions, and narrowing this gap is a matter for future work. The architectural choice between distributed and centralized representations is logically neutral (Theorem 3), but in an asynchronous model with losses, centralization dominates in cost with respect to the communication component (Theorem 4), at the price of availability. The conclusion is deliberately limited to what has been proved: the paper establishes *conditions of viability* and *cost regimes*; the claim that enterprise evolution is algorithmically *optimizable* is a research program that rests on the sufficiency result (Theorem 2) and requires a constructive policy minimizing Coasian cost subject to the viability constraint.

**Future Work.** (1) A two-loop budget $C_R$ shared between boundary observation and regulation (see the remark to §2.5). (2) Strategic actors: endogenous $z_t(a)$, partly chosen by actor $a$ itself, with opportunistic obscuring of status—this makes $\eta$ endogenous and activates Williamsonian hold-up. (3) Formulation as constrained optimization (maximization of discounted value subject to viability), which is the natural setting for "optimizability." (4) Multiple intersecting boundaries $z_t(a) \in \{I, E\}^{\text{types}}$—a typed $Actor_{\partial S}$. (5) Two-scale dynamics, with operations, permeability, and moves occurring at different frequencies. (6) Acquisition of the boundary model—identifying which actor has become critical—as an epistemic learning problem under drift. (7) Accounting consequences: formal recognition and attribution of materialised boundary losses as management debt, including postings to the responsible Decision Owner's account.

## References

[1] Coase, R. H. (1937). *The Nature of the Firm*. Economica, 4(16), 386–405.

[2] Ashby, W. R. (1956). *An Introduction to Cybernetics*. London: Chapman & Hall.

[3] Conant, R. C., & Ashby, W. R. (1970). *Every good regulator of a system must be a model of that system*. International Journal of Systems Science, 1(2), 89–97.

[4] Williamson, O. E. (1985). *The Economic Institutions of Capitalism*. New York: Free Press.

[5] Beer, S. (1972). *Brain of the Firm*. London: Allen Lane.

[6] Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition*. Dordrecht: Reidel.

[7] Aubin, J.-P. (1991). *Viability Theory*. Boston: Birkhäuser.

[8] ISO/IEC/IEEE 42010:2022. *Software, systems and enterprise — Architecture description*.

[9] Clark, H. H. (1996). *Using Language* [Grounding in Communication]. Cambridge University Press.

[10] Agha, G. (1986). *Actors: A Model of Concurrent Computation in Distributed Systems*. MIT Press.

[11] Touchette, H., & Lloyd, S. (2000). *Information-theoretic limits of control*. Physical Review Letters, 84(6), 1156–1159.

[12] Gilbert, S., & Lynch, N. (2002). *Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services*. ACM SIGACT News, 33(2), 51–59.

[13] Lynch, N. (1996). *Distributed Algorithms*. San Francisco: Morgan Kaufmann.

[14] Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985). *Impossibility of distributed consensus with one faulty process*. Journal of the ACM, 32(2), 374–382.

[15] Grossman, S. J., & Hart, O. D. (1986). *The costs and benefits of ownership: A theory of vertical and lateral integration*. Journal of Political Economy, 94(4), 691–719.

[16] Meyn, S. P., & Tweedie, R. L. (1993). *Markov Chains and Stochastic Stability*. London: Springer (Foster–Lyapunov drift conditions).

[17] Vityaz, A. (in preparation). *The Actor Codex. Chapter X. The Boundaries of the Firm* [Working draft]. Corezoid Inc., 2026.

[18] Vityaz, A. (2026). *Active Transaction Graphs: A Formal Framework for Transactional Interactive Systems*. Zenodo. https://doi.org/10.5281/zenodo.20747873 — in this repository: [../2026-active-transaction-graphs/](../2026-active-transaction-graphs/)

[19] Vityaz, A. (2026). *Management Debt—Part I: Concept, Metrics, and Principles for Attributing Materialised Debts to Actor Accounts*. Zenodo. doi:10.5281/zenodo.21069692 — in this repository: [../2026-management-debt-part-i/](../2026-management-debt-part-i/)
