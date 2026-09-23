---
title: "On the Necessity of Noise Suppression for Minimal Good Regulators: Factorization Theorems and a Closure Conjecture"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-01
doi: 10.13140/RG.2.2.33143.07843
version: v1
license: CC-BY-4.0
keywords: [cybernetics, regulation theory, noise suppression, Conant–Ashby theorem, Ashby's law, information bottleneck, state abstraction, meta-regulation, AI, large language models]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.13140/RG.2.2.33143.07843](https://doi.org/10.13140/RG.2.2.33143.07843).

# On the Necessity of Noise Suppression for Minimal Good Regulators: Factorization Theorems and a Closure Conjecture

**Alexander Vityaz** · Corezoid Inc., Dnipro, Ukraine · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

## Abstract

We prove a factorization necessity result: any *minimal* good regulator (i.e., capacity-efficient in the sense of not expending control capacity on goal-irrelevant distinctions) must factorize through a noise-suppressing projection onto a pragmatic signal space. Building on classical cybernetics (Conant–Ashby, Ashby's Law of Requisite Variety), we introduce a goal-relevant equivalence relation on disturbances and a quantitative notion of *noise leakage*. The main theorem shows that minimizing leakage forces the regulator to be constant on pragmatic equivalence classes, yielding $\pi^* = g \circ \sigma_\mathrm{prag}$. We also show that the same quotient structure is induced by several standard efficiency objectives (noise leakage, conditional entropy, and an information-cost formulation in a stochastic setting). We discuss meta-regulation ("who regulates the noise suppressor?") and conjecture that finite systems close the regress via a three-level hierarchy with timescale separation. An operational AI case study is provided in Appendix A.

---

## 1 Introduction

Cybernetics as the science of control and communication was founded by Wiener [14], who emphasized the central role of feedback. Shannon [9] laid the mathematical foundations of information theory, formalizing the concept of noise in communication channels. The Conant–Ashby theorem [3] states that every good regulator of a system must be a model of that system. Ashby's Law of Requisite Variety [1] relates regulatory capacity to the variety of disturbances. Beer [2] developed these ideas into the Viable System Model (VSM), where variety attenuation plays a central role.

None of these results, however, directly answers an architectural question which repeatedly appears in engineering practice:

> *Must a good regulator contain a noise suppression mechanism?*

As stated, the answer is "not necessarily" if one allows regulators to waste internal capacity on distinctions that do not matter for achieving the goal. The main point of this paper is that **capacity-efficient** (i.e., non-wasteful) regulation makes noise suppression unavoidable.

### Our contribution

We formalize "noise" not as a statistical component of a disturbance, but as **goal-irrelevant distinctions**: differences between disturbances that do not change the set of admissible (goal-achieving) actions. This yields a natural **pragmatic equivalence relation** and a quotient (signal) space. We then prove that any good regulator minimizing natural measures of wasted discrimination necessarily factorizes into:

1. a noise-suppressing projection $\sigma : D \twoheadrightarrow \Sigma$,
2. followed by an essential regulator $g : \Sigma \to R$.

#### Why this does not follow from Conant–Ashby

Conant–Ashby requires that a good regulator must be a model in the sense of distinguishing those environmental situations requiring different actions. It does not, by itself, enforce which distinctions are safe (or necessary) to discard, nor does it impose a factorized internal architecture. Our results isolate the "discard" part as a necessary consequence of capacity-efficiency, rather than of mere goal-achievement.

#### Terminology

We use **viability** (Section 2) in the classical sense: the plant admits at least one goal-achieving action for every disturbance. We use **minimal** (or **capacity-efficient**) to mean "minimal with respect to a resource criterion" (Sections 5–5.3), avoiding semantic overload with Beer's VSM.

### 1.1 Related Work

**Good regulator theorem.** The Conant–Ashby theorem [3] states that "every good regulator of a system must be a model of that system." Here "model" is best read as a homomorphism: the regulator must distinguish those environmental states that require different actions. A critical discussion in informal commentary emphasizes that the theorem does not imply an internal state reconstruction and that non-minimal regulators can be good without being models.^1

**Ashby's goal-relative view of noise.** Ashby noted that noise is not intrinsically distinguishable from other variety; only relative to a recipient and a goal does the message/noise distinction become meaningful [1, p. 157]. We operationalize this idea via admissible action sets.

**Information Bottleneck (IB).** The IB method [12] solves $\min_{p(t|x)} I(X; T) - \beta I(T; Y)$. Our deterministic factorization can be seen as the lossless limit where the "relevant variable" is the admissible-action set and one requires perfect preservation; the deterministic IB framework [11] formalizes this limit. Kolchinsky et al. [6] connect IB to predictive coding and establish bounds on sufficient statistics, complementing our deterministic characterization.

**Goal-oriented rate-distortion.** Stavrou and Kountouris [10] develop a rate-distortion theory for goal-oriented semantics. Under a $0/\infty$ distortion induced by admissible action sets, one recovers the same quotient structure as our pragmatic signal space.

**State abstraction in RL.** State abstraction work (e.g., $a^*$-irrelevance) groups states with identical sets of optimal actions [7]. Bisimulation metrics provide continuous relaxations and value-function guarantees [4]. Our contribution is a necessity statement in a static reachability-style setting, rather than a possibility result for simplifying RL.

**Empowerment.** Klyubin et al. [5] introduced empowerment—the channel capacity from actions to future states—as an intrinsic utility function. Salge et al. [8] showed that empowerment-maximizing agents naturally develop noise-robust representations. In our framework, empowerment becomes a natural secondary criterion for selecting among minimal regulators: once noise leakage is minimized, one may choose $g$ to maximize future controllability.

**Information-theoretic limits on control.** Touchette and Lloyd [13] study information constraints in control, complementing our focus on goal-relevant abstraction and leakage minimization.

^1 See J. Swentworth, Fixing the Good Regulator Theorem, LessWrong (2021): https://www.lesswrong.com/posts/Dx9LoqsEh3gHNJMDk/

---

## 2 Regulation Model

**Definition 2.1 (Regulation System).** A regulation system is a tuple $(D, R, E, P)$, where $D$ is a finite set of disturbances, $R$ is a finite set of regulator actions, $E$ is a finite set of outcomes, and $P : D \times R \to E$ is the plant function.

**Definition 2.2 (Goal and Regulator).** A goal is a subset $E_\mathrm{acc} \subseteq E$ of acceptable outcomes. A regulator is a function $\pi : D \to R$. A regulator $\pi$ is **good** if
$$\forall d \in D : P(d, \pi(d)) \in E_\mathrm{acc}.$$

**Definition 2.3 (Viability).** A system satisfies the **viability condition** if
$$\forall d \in D \, \exists r \in R : P(d, r) \in E_\mathrm{acc}.$$

**Definition 2.4 (Admissible Actions).** For $d \in D$, the set of admissible actions is
$$A(d) := \{r \in R \mid P(d, r) \in E_\mathrm{acc}\}.$$

---

## 3 Two Levels of Equivalence

**Definition 3.1 (Physical Equivalence).** Two disturbances $d_1, d_2 \in D$ are **physically equivalent**, $d_1 \sim_\mathrm{phys} d_2$, if
$$\forall r \in R : P(d_1, r) = P(d_2, r).$$

**Definition 3.2 (Pragmatic Equivalence).** Two disturbances $d_1, d_2 \in D$ are **pragmatically equivalent**, $d_1 \sim_\mathrm{prag} d_2$, if
$$A(d_1) = A(d_2).$$

**Definition 3.3 (Signal Spaces).** Define $\Sigma_\mathrm{phys} := D/{\sim_\mathrm{phys}}$ and $\Sigma_\mathrm{prag} := D/{\sim_\mathrm{prag}}$ with canonical projections $\sigma_\mathrm{phys} : D \twoheadrightarrow \Sigma_\mathrm{phys}$ and $\sigma_\mathrm{prag} : D \twoheadrightarrow \Sigma_\mathrm{prag}$.

**Lemma 3.4.** *Physical equivalence implies pragmatic equivalence. The converse is false in general.*

**Proof.** If $d_1 \sim_\mathrm{phys} d_2$, then for all $r$, $P(d_1, r) = P(d_2, r)$, hence $P(d_1, r) \in E_\mathrm{acc} \Leftrightarrow P(d_2, r) \in E_\mathrm{acc}$, so $A(d_1) = A(d_2)$ and thus $d_1 \sim_\mathrm{prag} d_2$. A counterexample is given by a plant where outcomes differ but all outcomes are acceptable, so admissible sets coincide. $\square$

**Remark 3.5 (Two-stage noise suppression).** Lemma 3.4 yields a two-stage attenuation pipeline:
$$D \xrightarrow{\sigma_\mathrm{phys}} \Sigma_\mathrm{phys} \twoheadrightarrow \Sigma_\mathrm{prag},$$
corresponding to (i) sensory/physical indistinguishability and (ii) goal-oriented (teleological) abstraction.

**Remark 3.6 (Mathematics as a universal noise suppressor).** From this perspective, mathematics itself can be viewed as a universal noise suppressor: it constructs quotient representations by declaring goal-irrelevant distinctions equivalent and derives regulators that depend only on the induced signal space. Definitions implement the projection $\sigma$; proofs certify that the induced abstraction preserves goal-achievability. In this sense, formalization is not merely a descriptive tool but an architectural component enabling capacity-efficient regulation.

---

## 4 Illustrative Examples

**Example 4.1 (Pragmatic abstraction can be strictly coarser than physical abstraction).** Let $D = \{d_1, d_2\}$, $R = \{0, 1\}$, and $E = \{e_a, e_b\}$ with $E_\mathrm{acc} = E$ (all outcomes acceptable). Define a plant by
$$P(d_1, 0) = e_a, \quad P(d_1, 1) = e_b, \quad P(d_2, 0) = e_b, \quad P(d_2, 1) = e_a.$$
Then $d_1 \not\sim_\mathrm{phys} d_2$ (outcomes differ), but $A(d_1) = A(d_2) = \{0, 1\}$, hence $d_1 \sim_\mathrm{prag} d_2$.

**Example 4.2 (Non-uniqueness of the factor $g$).** In the setting of the previous example, $\Sigma_\mathrm{prag}$ has a single class $s$, and any constant regulator (always output $0$ or always output $1$) is good. Thus $\pi = g \circ \sigma_\mathrm{prag}$ holds for two different choices of $g(s) \in \{0, 1\}$.

---

## 5 Factorization Theorems

Let $\mathcal{G}$ denote the set of all good regulators.

### 5.1 Leakage Minimality

**Definition 5.1 (Noise Leakage).** For $\pi \in \mathcal{G}$ and $s \in \Sigma_\mathrm{prag}$, define $R_s(\pi) := \{\pi(d) \mid \sigma_\mathrm{prag}(d) = s\}$. The **noise leakage** is
$$V_\mathrm{leak}(\pi) := \sum_{s \in \Sigma_\mathrm{prag}} \log_2 |R_s(\pi)|.$$

**Remark 5.2 (Interpretation of $V_\mathrm{leak}$).** For a fixed pragmatic class $s$, the quantity $\log_2 |R_s(\pi)|$ is the number of bits needed to specify which of the (goal-equivalent) actions in $R_s(\pi)$ is taken. Thus $V_\mathrm{leak}(\pi)$ measures the total "residual variety" of the regulator's output within pragmatic equivalence classes: it penalizes expending action variety on distinctions that do not change admissibility. Other monotone penalties of $|R_s(\pi)|$ would lead to the same factorization conclusion; $\log_2$ is chosen for its standard information-theoretic interpretation.

**Definition 5.3 (Leakage-minimal good regulator).** A regulator $\pi^* \in \mathcal{G}$ is **leakage-minimal** if it minimizes $V_\mathrm{leak}(\pi)$ over $\mathcal{G}$.

**Theorem 5.4 (Factorization Through Noise Suppression).** *Any leakage-minimal good regulator $\pi^*$ factorizes through the pragmatic signal space:*
$$\pi^* = g \circ \sigma_\mathrm{prag}$$
*for some $g : \Sigma_\mathrm{prag} \to R$.*

**Proof.** Fix $s \in \Sigma_\mathrm{prag}$. By definition of $\sim_\mathrm{prag}$, admissibility is class-invariant: $A(s) := A(d)$ is well-defined for any $d$ with $\sigma_\mathrm{prag}(d) = s$.

If $|R_s(\pi^*)| > 1$ for some $s$, choose $d_a, d_b$ in class $s$ with $\pi^*(d_a) \neq \pi^*(d_b)$ and let $r^* := \pi^*(d_a) \in A(s)$. Define
$$\pi'(d) := \begin{cases} r^* & \text{if } \sigma_\mathrm{prag}(d) = s, \\ \pi^*(d) & \text{otherwise}. \end{cases}$$

Then $\pi'$ remains good and strictly reduces $\log_2 |R_s(\pi)|$ for that class while leaving other classes unchanged, hence $V_\mathrm{leak}(\pi') < V_\mathrm{leak}(\pi^*)$, contradicting minimality. Therefore $|R_s(\pi^*)| = 1$ for all $s$, and defining $g(s)$ as the unique element of $R_s(\pi^*)$ yields $\pi^* = g \circ \sigma_\mathrm{prag}$. $\square$

**Corollary 5.5 (Impossibility without noise suppression).** *No leakage-minimal good regulator can exist without being (functionally) equivalent to a composition of a noise suppressor and an essential regulator. In particular, any minimal regulator must ignore distinctions within pragmatic equivalence classes.*

**Remark 5.6 (Non-uniqueness of $g$).** The factor $g$ is not unique: for each pragmatic class $s$, any choice $g(s) \in A(s)$ yields a factorized good regulator. The theorem asserts necessity of factorization, not uniqueness of the factor.

**Remark 5.7 (On "definitional" concerns).** Theorem 5.4 is elementary once the goal-relevant notion of noise is fixed. This is not a weakness: the technical content is intentionally lightweight, while the substantive contribution is the teleological definition of noise and the demonstration that multiple independent efficiency criteria all collapse to the same quotient structure (Sections 5.2–5.3).

### 5.2 Entropy-based minimality

Assume a distribution on $D$ (e.g., uniform unless stated otherwise).

**Definition 5.8 (Conditional action entropy).** For $\pi \in \mathcal{G}$, define
$$H_\mathrm{cond}(\pi) := H(\pi(D) \mid \sigma_\mathrm{prag}(D)).$$

**Theorem 5.9 (Entropy-based factorization).** *Any good regulator minimizing $H_\mathrm{cond}(\pi)$ factorizes:*
$$\pi^* = g \circ \sigma_\mathrm{prag}.$$

**Proof.** $H(\pi(D) \mid \sigma_\mathrm{prag}(D)) = 0$ if and only if $\pi(D)$ is a deterministic function of $\sigma_\mathrm{prag}(D)$, i.e., $\pi$ is constant on pragmatic classes. Since viability guarantees $A(s) \neq \emptyset$ for each class $s$, one can pick any $g(s) \in A(s)$ and define $\hat{\pi} = g \circ \sigma_\mathrm{prag}$ which is good and satisfies $H_\mathrm{cond}(\hat{\pi}) = 0$. Hence any entropy-minimizer must achieve $0$ and therefore factorize. $\square$

### 5.3 Stochastic extension: information-minimal $\tau$-regulation

**Definition 5.10 (Stochastic plant).** A stochastic plant is a Markov kernel $P(\cdot \mid d, r) \in \Delta(E)$ assigning to each $(d, r)$ a distribution over outcomes.

**Definition 5.11 ($\tau$-admissible actions).** Fix a reliability threshold $\tau \in (0, 1]$. Define
$$A_\tau(d) := \left\{ r \in R \,\middle|\, \mathbb{E}_{e \sim P(\cdot | d, r)}[e \in E_\mathrm{acc}] \geq \tau \right\}.$$

**Definition 5.12 ($\tau$-pragmatic equivalence and projection).** Define $d_1 \sim_{\mathrm{prag}, \tau} d_2$ iff $A_\tau(d_1) = A_\tau(d_2)$. Let $\sigma_{\mathrm{prag}, \tau} : D \twoheadrightarrow \Sigma_{\mathrm{prag}, \tau}$ be the canonical projection and set $S := \sigma_{\mathrm{prag}, \tau}(D)$ for random $D$.

**Theorem 5.13 (Stochastic factorization via information cost).** *Let $D$ be a random variable on $D$. Consider any $\tau$-good stochastic policy $p(r \mid d)$ such that $\mathrm{supp}(p(\cdot \mid d)) \subseteq A_\tau(d)$ for all $d$. Then there exists a $\tau$-good policy $\bar{p}(r \mid d) = q(r \mid S)$ (i.e., $D \to S \to R$) such that*
$$I(D; \bar{R}) \leq I(D; R).$$
*Consequently, minimizing $I(D; R)$ over $\tau$-good policies admits an optimal solution satisfying the Markov chain $D \to S \to R$.*

**Proof.** Given $p(r \mid d)$, define the class-averaged decoder
$$q(r \mid s) := \mathbb{P}(R = r \mid S = s),$$
and set $\bar{p}(r \mid d) := q(r \mid \sigma_{\mathrm{prag}, \tau}(d))$.

*$\tau$-goodness.* If $q(r \mid s) > 0$, then $r \in A_\tau(d)$ for some $d$ with $\sigma_{\mathrm{prag}, \tau}(d) = s$. Since $A_\tau(\cdot)$ is constant on the class $s$, we have $r \in A_\tau(d')$ for all $d'$ in the class; hence $\mathrm{supp}(\bar{p}(\cdot \mid d)) \subseteq A_\tau(d)$.

*Information reduction.* By construction $D \to S \to \bar{R}$, so by data processing $I(D; \bar{R}) \leq I(D; S)$. More directly, note that $I(D; R) = I(S; R) + I(D; R \mid S) \geq I(S; R)$. Since $\bar{R}$ depends on $D$ only through $S$, we have $I(D; \bar{R}) = I(S; \bar{R}) = I(S; R)$, thus $I(D; \bar{R}) \leq I(D; R)$. $\square$

**Remark 5.14 (Information Bottleneck view).** Theorem 5.13 is a task/risk-constrained compression statement: among $\tau$-good policies, the information-minimal one does not transmit any input information beyond what is needed to identify the $\tau$-pragmatic class.

### 5.4 Axiomatic characterization and non-triviality

**Definition 5.15 (Noise-monotone functional).** A functional $M : \mathcal{G} \to \mathbb{R}$ is **noise-monotone** if whenever $\pi$ varies within some pragmatic class $s$ (i.e., $|R_s(\pi)| > 1$), there exists a good regulator $\pi^{\downarrow s}$ that is constant on $s$ and satisfies $M(\pi^{\downarrow s}) < M(\pi)$.

**Theorem 5.16 (Factorization for noise-monotone criteria).** *If $\pi^* \in \mathcal{G}$ minimizes a noise-monotone functional $M$, then $\pi^* = g \circ \sigma_\mathrm{prag}$ for some $g$.*

**Proof.** If $\pi^*$ were not constant on some class $s$, noise-monotonicity would produce a strictly better $\pi^{\downarrow s}$, contradicting optimality. Hence $\pi^*$ is constant on all classes and factors through the quotient. $\square$

**Remark 5.17 (Criterion independence).** Theorems 5.4, 5.9, 5.13, and 5.16 show that factorization is not an artifact of a single objective: leakage, conditional entropy, mutual information, and all noise-monotone criteria force the same quotient structure.

**Remark 5.18 (Circuit complexity counterexample (non-noise-monotone criterion)).** Not every "natural" minimality criterion is noise-monotone. Consider Boolean circuit complexity $C(\pi)$, i.e., the size of the smallest circuit computing $\pi$ from $d$.

Fix $D = R = \{0, 1\}^n$, $E = \{0, 1\}$, $E_\mathrm{acc} = \{1\}$, and choose any surjective function $h : \{0, 1\}^n \to \{0, 1\}^m$ with high circuit complexity (such functions exist by counting). Define a plant by
$$P(d, r) := \mathbf{1}\{h(d) = h(r)\}.$$

Then
$$A(d) = \{r \in R \mid h(r) = h(d)\},$$
so $\Sigma_\mathrm{prag}$ is in bijection with hash values $h(d)$.

*A simple good regulator with high leakage:* the identity regulator $\pi_\mathrm{id}(d) = d$ is good (trivially $h(d) = h(\pi_\mathrm{id}(d))$) and has small circuit complexity.

*Factorized good regulators require computing $h$:* any regulator constant on pragmatic classes must output a fixed representative $r_s$ for each $s \in \{0, 1\}^m$, i.e., $\pi(d) = r_{h(d)}$, which (in general) inherits the high circuit complexity of $h$.

Thus minimizing circuit complexity among good regulators may select $\pi_\mathrm{id}$, which violates factorization (and exhibits large noise leakage). Therefore $C(\pi)$ is not noise-monotone, and the information-theoretic nature of the criteria in Theorems 5.4–5.13 is essential.

---

## 6 Meta-Regulation and Closure

Theorems above establish that minimal regulation is equivalent to $\pi = g \circ \sigma$. But what ensures adequacy of $\sigma$ itself? If $\sigma$ is also "regulated", one may fear an infinite regress.

### 6.1 The regress problem

If one insists that the noise suppressor $\sigma_1 = \sigma$ is itself minimal relative to some meta-goal, one obtains $\sigma_1 = g_2 \circ \sigma_2$, and so on. In finite systems, an infinite strictly descending regress is impossible, suggesting closure mechanisms.

### 6.2 A three-level closure hypothesis

**S3: Hard invariants (fast loop).** Deterministic constraints preventing catastrophic failures of $\sigma$ (e.g., mandatory validation routes, WIP limits, "no due date without booking").

**S4: Adaptive calibration (medium loop).** A meta-controller adjusting $\sigma$ parameters via logged metrics (leakage proxies, false suppression, COPQ, human escalation rate), using canary deployment and rollback.

**S5: Policy and identity (slow loop).** Human governance determining what constitutes $E_\mathrm{acc}$ and which events are "algedonic" (must bypass suppression).

**Conjecture 6.1 (Regulation closure).** *Every finite regulation system either has an external goal source, or contains a hierarchy of meta-loops with timescale separation that closes at a self-referential policy/identity level.*

**Remark 6.2 (Status).** Conjecture 6.1 is a conceptual synthesis aligned with Beer's VSM [2]. A fully formal proof would require explicit modeling of meta-parameters, timescale separation, and fixed-point conditions.

---

## 7 Limitations and Future Directions

1. **Finiteness.** We assume finite $(D, R, E)$. Continuous extensions require measure-theoretic quotient constructions and regularity assumptions.

2. **Static plant.** The core model is single-shot. Extensions to MDP/POMDP settings connect to RL state abstraction and bisimulation.

3. **Choice among minimizers.** Factorization identifies a family of minimal regulators; selecting $g$ may depend on cost, robustness margins, and empowerment-like criteria [5, 8].

4. **Learning $\sigma_\mathrm{prag}$.** PAC-style sample complexity bounds for learning the pragmatic projection from data remain an open direction.

---

## 8 Conclusion

We have proven that minimal good regulators necessarily factorize through a noise-suppressing projection onto a pragmatic signal space. This provides a formal statement of a widely used engineering intuition: effective regulation requires discarding goal-irrelevant distinctions. We strengthened the necessity claim by showing the same factorization arises under multiple independent criteria, including a stochastic information-cost formulation relevant to modern ML. Finally, we framed meta-regulation as a closure problem and proposed a three-level hierarchy as a practical closure mechanism.

---

## Appendix A: Case Study: AI as a Universal Noise Suppressor

The factorization $\pi \approx g \circ \sigma$ becomes operationally relevant when the raw event stream is dominated by *friendly noise* (high-volume, well-intended communications that create spurious obligations). We briefly summarize an illustrative operational architecture (based on real-world practice) where LLM-based agents realize $\sigma$ and $g$.

### Setting

Inputs are heterogeneous communications (chats, emails, meeting transcripts). The system maintains an event-sourced ledger of obligations and a calendar graph with a meta-calendar defined as the aggregate (sum) of all actor calendars.

### Noise suppressor $\sigma$ (LLM extractor)

The extractor converts raw events into candidate obligation specs and suppresses noise via:

i. normalization and canonicalization,
ii. semantic deduplication and clustering,
iii. intent filtering (FYI / opinion / discussion),
iv. linking to sources and prior solutions, and
v. preliminary risk/size estimation.

### Essential regulator $g$ (dispatcher)

The dispatcher maps pragmatic classes to actions: **commit** vs. **icebox** vs. **bundle**, **human** vs. **AI** vs. **hybrid** execution, and **risk-aware routing** (e.g., security/compliance).

### Ledger & calendar invariants

A central operational invariant is **no due date without booking**: any transaction with a due date must reserve a time slot in the responsible actors' calendars and therefore appears in the company meta-calendar. Meetings are treated as work: they consume time credits and must produce an artifact transaction (decision, task, or protocol), otherwise the time is accounted as burn.

### Operational calibration

The noise suppressor is meta-regulated through (a) **hard invariants** (fast loop), (b) **parameter tuning** by metrics such as late-duplicate rate, resurrection rate, COPQ, and human-interrupt load (medium loop), and (c) **policy/value decisions** (slow loop). This case study is deliberately concise; detailed metrics and calibration recipes depend on organization-specific constraints.

---

## References

[1] W. R. Ashby. *An Introduction to Cybernetics*. Chapman & Hall, 1956.

[2] S. Beer. *Brain of the Firm*. Allen Lane, 1972.

[3] R. C. Conant and W. R. Ashby. Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2):89–97, 1970. DOI: [10.1080/00207727008920220](https://doi.org/10.1080/00207727008920220)

[4] N. Ferns, P. Panangaden, and D. Precup. Metrics for finite Markov decision processes. In *Proceedings of UAI*, 2004.

[5] A. S. Klyubin, D. Polani, and C. L. Nehaniv. Empowerment: A universal agent-centric measure of control. In *Proc. IEEE Congress on Evolutionary Computation*, pp. 128–135, 2005. DOI: [10.1109/CEC.2005.1554676](https://doi.org/10.1109/CEC.2005.1554676)

[6] A. Kolchinsky, B. D. Tracey, and D. H. Wolpert. Nonlinear information bottleneck. *Entropy*, 21(12):1181, 2019. DOI: [10.3390/e21121181](https://doi.org/10.3390/e21121181)

[7] L. Li, T. J. Walsh, and M. L. Littman. Towards a unified theory of state abstraction for MDPs. In *Proceedings of ISAIM*, 2006.

[8] C. Salge, C. Glackin, and D. Polani. Empowerment—an introduction. In *Guided Self-Organization: Inception*, pp. 67–114. Springer, 2014. DOI: [10.1007/978-3-642-53734-9_4](https://doi.org/10.1007/978-3-642-53734-9_4)

[9] C. E. Shannon. A mathematical theory of communication. *Bell System Technical Journal*, 27(3):379–423, 1948. DOI: [10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x)

[10] P. A. Stavrou and M. Kountouris. A rate distortion approach to goal-oriented communication. In *Proceedings of IEEE ISIT*, 2022. DOI: [10.1109/ISIT50566.2022.9834459](https://doi.org/10.1109/ISIT50566.2022.9834459)

[11] D. J. Strouse and D. J. Schwab. The deterministic information bottleneck. *Neural Computation*, 29(6):1611–1630, 2017. DOI: [10.1162/NECO_a_00961](https://doi.org/10.1162/NECO_a_00961)

[12] N. Tishby, F. C. Pereira, and W. Bialek. The information bottleneck method. In *Proceedings of the 37th Allerton Conference*, pp. 368–377, 1999.

[13] H. Touchette and S. Lloyd. Information-theoretic limits on control. *Physical Review Letters*, 84(6):1156, 2000. DOI: [10.1103/PhysRevLett.84.1156](https://doi.org/10.1103/PhysRevLett.84.1156)

[14] N. Wiener. *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press, 1948.
