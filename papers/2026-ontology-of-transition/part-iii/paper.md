---
title: "Ontology of Transition—Part III: The Thermodynamic Price of External Time: Rate–Distortion Bounds for Physical Clock Records"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-07-21
doi: 10.5281/zenodo.21473025
series-doi: 10.5281/zenodo.21380580
version: v1
license: CC-BY-4.0
keywords: [external time, physical clock records, indirect rate–distortion, remote source coding, rate–distortion theory, Landauer principle, renewal work, reusable memory, thermodynamics of information, Blahut–Arimoto algorithm, entropy of innovations]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.5281/zenodo.21473025](https://doi.org/10.5281/zenodo.21473025).

# Ontology of Transition—Part III

## The Thermodynamic Price of External Time: Rate–Distortion Bounds for Physical Clock Records

**Alexander Vityaz** · Corezoid Inc., Dnipro, Ukraine · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

**Standalone DOI:** [10.5281/zenodo.21473025](https://doi.org/10.5281/zenodo.21473025)

**Part of the complete three-part volume:** *Ontology of Transition: Causal Order, External Time, and the Thermodynamics of Physical Clock Records* — complete-volume DOI: [10.5281/zenodo.21380580](https://doi.org/10.5281/zenodo.21380580)

## Abstract

This article is Part III of the three-part scientific work *Ontology of Transition*. The work's central idea is that transition, rather than the static thing, is the primary unit of description, while operational time is realized through physical records of transitions whose production, transmission, interpretation, and reuse have distinct informational and thermodynamic limits.

External time is operationally available to a system only through a physical record of a selected clock process, delivered through a possibly noisy, incomplete channel $K_{C \to S}$ ([Part I](../part-i/) [1]). [Part II](../part-ii/) [2] quantified two costs of that mediation: a channel information floor on reconstruction (its Theorem II.A) and a thermodynamic precision floor on the reading register (its Theorem II.D). This paper adds a renewal-work bound to the series' cost decomposition. For a finite classical footprint with equal-free-energy logical states, exact isothermal renewal without accessible correlated side information obeys $\beta \langle W_{\mathrm{renew}} \rangle \geq R^{\mathrm{clock}}_K(D) \geq R(D)$, where $R^{\mathrm{clock}}_K$ is the indirect (remote) rate–distortion function determined by the physical clock-delivery channel — the classical indirect rate–distortion problem induced by the delivered clock record [3, 4, 5]. The bound extends to correlated finite histories without i.i.d. assumptions; closed forms are derived for a uniform $M$-phase clock behind a symmetric channel and behind an erasure-and-substitution channel, with the exact indirect frontier proved via the Wolf–Ziv reduction; a sequential-ring corollary shows the asymptotic renewal cost equals the entropy of innovations, not the tick count. Target distortions below the channel's Bayes risk are unattainable at any reset budget. The three floors — information destroyed in the channel, precision paid in register dissipation, reuse paid in reset work — constrain different observables by different mechanisms and none implies another. The result does not identify time with work; it prices one specified operation: making a prescribed resolution of external time reusable at a chosen system boundary. All closed forms are verified against a Blahut–Arimoto solver to machine precision, and the literal decoder attains the indirect frontier at minimum distortion exactly. The causal (nonanticipative) version is posed as the open target.

**Keywords:** *external time; rate–distortion; Landauer principle; clock records; renewal work; indirect source coding*

## 1. From ontology to reset work

[Part I](../part-i/) [1] establishes that the external time accessible to a system is not a direct reading of the metasystem: it is a functional of a physical record produced by a selected clock process and delivered through a possibly noisy, incomplete, and history-dependent channel $K_{C \to S}$, and it separates the costs of signal generation, transmission, registration, storage, and memory reset. [Part II](../part-ii/) [2] made two of those costs quantitative: the reconstruction error that the channel itself destroys (an exact minimax floor of $n p \sigma^2$ per window, [2, Thm. II.A]) and the precision that the reading register must pay for in dissipation while it runs (a thermodynamic uncertainty floor $2/\Sigma_{\mathrm{reg}}$, [2, Thm. II.D]). What remained unpriced is the cost that appears only when the observer is reusable: the record and everything computed from it must eventually be returned to a standard state.

This paper proves the following bound:

> **A reusable observer cannot reconstruct an external clock to prescribed accuracy and then complete a closed renewal of the entire information-bearing footprint for less work than the rate–distortion information required by that reconstruction.**

In the symmetric Landauer regime, and under the assumptions of Theorem III.1 below,

*[see the displayed bound in the PDF, Section 1 — $\langle W_{\mathrm{renew}} \rangle / (k_B T) \geq R^{\mathrm{clock}}_K(D) \geq R(D)$]*

where $D$ is the allowed clock-reconstruction distortion, $R^{\mathrm{clock}}_K(D)$ is the indirect (remote) rate–distortion function fixed by the actual clock-delivery channel, and $R(D)$ is the ordinary rate–distortion function of the hidden source reading. This is not the identity "time is work." It is a conditional lower bound on one specified physical operation: resetting a reusable record of external time.

## 2. Operational model

Let $\Theta \in \mathcal{T}$ be the hidden reading of a selected external clock process; $\rho \in \mathcal{Y}$ the record delivered through $K_{C \to S}$; $G \in \mathcal{G}$ the complete finite information-bearing footprint to be returned to its standard state, including the raw register, decoded output, correlated workspace, and any copies that do not survive renewal; $\hat{\Theta}$ the decoded clock reading; $d(\theta, \hat{\theta}) \geq 0$ a specified distortion function. The information flow is $\Theta \to \rho \to G \to \hat{\Theta}$, and the target accuracy is $E\,d(\Theta, \hat{\Theta}) \leq D$. All entropies and mutual informations use natural logarithms (nats).

(Notation guard: throughout the series, $p$ denotes the loss probability of the clock channel and $q = 1 - p$ its delivery or flush probability [2, §6]. In this paper the record channel's substitution error is therefore written $u$ and its erasure probability $\varepsilon$; $q$ keeps its series meaning and is not reused.)

Define the ordinary source rate–distortion function

*[see the displayed definition of $R(D)$ in the PDF, Section 2]*

and, for the fixed physical delivery law $P(\theta, \rho) = P(\theta)\,K_{C \to S}(\rho \mid \theta)$, the indirect clock rate–distortion function

*[see the displayed definition of $R^{\mathrm{clock}}_K(D)$ in the PDF, Section 2]*

The second quantity is the minimum information rate that must be retained from the actually delivered record, rather than from an unrealistically available source state. If the requested distortion is below the Bayes risk imposed by the channel, the feasible set is empty and $R^{\mathrm{clock}}_K(D) = +\infty$ by convention.

## 3. The classical reduction

The indirect rate–distortion function is a classical object: introduced by Dobrushin and Tsybakov [3], given its operational transmission form by Wolf and Ziv [4], and named and systematized by Witsenhausen [5]. Its key structural property, which this paper uses twice, is the reduction to an ordinary problem on the record alphabet.

**Lemma III.1 (Wolf–Ziv reduction [4]).** Define the modified distortion $\tilde{d}(\rho, \hat{\theta}) := E[d(\Theta, \hat{\theta}) \mid \rho]$. Then

*[see the displayed reduction identity in the PDF, Section 3 — $R^{\mathrm{clock}}_K(D) = \inf\{I(\rho; \hat{\Theta}) : E\,\tilde{d} \leq D\}$ over kernels $P(\hat{\theta} \mid \rho)$]*

i.e. the indirect problem for $\Theta$ observed through $K$ equals the ordinary rate–distortion problem for the source $\rho$ under $\tilde{d}$.

*Proof.* For any decoder $P(\hat{\theta} \mid \rho)$, the Markov chain $\Theta \to \rho \to \hat{\Theta}$ gives $E\,d(\Theta, \hat{\Theta}) = E\big[E[d(\Theta, \hat{\Theta}) \mid \rho, \hat{\Theta}]\big] = E[\tilde{d}(\rho, \hat{\Theta})]$, since conditionally on $\rho$ the pair $(\Theta, \hat{\Theta})$ is independent. The two constraint sets therefore coincide, and the objective $I(\rho; \hat{\Theta})$ is the same. □

The primitive inequalities of the next section are likewise classical — Shannon's rate–distortion theory [6], Landauer's bound [7], the information thermodynamics of measurement and erasure [8] — and are not claimed as new. The contribution is the composite bound and its clock-record interpretation (§13).

## 4. Clock-record rate–distortion–renewal theorem

**Theorem III.1 (single record).** Assume that: (1) $G$ is a finite classical memory whose logical states have equal internal free energy at the beginning and end of the renewal protocol; (2) it is reset exactly to one standard state while coupled to a bath at temperature $T$; (3) the reset controller has no access to $\Theta$, $\rho$, a surviving copy of $\hat{\Theta}$, a correlated random seed, or any other side information with which the record could be uncomputed; (4) $G$ includes the entire clock-correlated footprint that is erased; in particular, the decoded output cannot be retained elsewhere and silently excluded from the accounting; (5) $W_{\mathrm{renew}}$ is the average work supplied to return $G$ to its standard state, not the dissipated-work quantity $W - \Delta F$.

The completeness requirement on $G$ is necessarily boundary-relative. Determining which registers, copies, correlated workspaces, and surviving records belong to the renewed system is not merely an implementation detail: it specifies the physical boundary across which information and work are accounted. A related formal treatment of the system boundary as an explicit information-bearing object of control is developed in [18] (see [The Computable Boundary of the Firm](../../2026-computable-boundary-of-the-firm/)). In the present theorem, the boundary is fixed rather than optimized, but it must be stated explicitly for the reset-work attribution to be well posed.

Under these assumptions, every implementation satisfying $E\,d(\Theta, \hat{\Theta}) \leq D$ obeys

*[see the displayed chain in the PDF, Section 4 — $\langle W_{\mathrm{renew}} \rangle / (k_B T) \geq H(G) \geq I(\rho; G) \geq I(\rho; \hat{\Theta}) \geq R^{\mathrm{clock}}_K(D) \geq R(D)$]*

*Proof.* The symmetric Landauer bound for exact local reset gives $\beta \langle W_{\mathrm{renew}} \rangle \geq H(G)$. Trivially $H(G) \geq I(\rho; G)$. Because $\rho \to G \to \hat{\Theta}$, the data-processing inequality gives $I(\rho; G) \geq I(\rho; \hat{\Theta})$. The induced decoder $P(\hat{\theta} \mid \rho)$ is one of the kernels over which $R^{\mathrm{clock}}_K(D)$ is minimized, hence $I(\rho; \hat{\Theta}) \geq R^{\mathrm{clock}}_K(D)$. Finally, $\Theta \to \rho \to \hat{\Theta}$ implies $I(\rho; \hat{\Theta}) = I(\Theta; \hat{\Theta}) + I(\rho; \hat{\Theta} \mid \Theta) \geq I(\Theta; \hat{\Theta}) \geq R(D)$; taking the infimum over admissible record decoders yields $R^{\mathrm{clock}}_K(D) \geq R(D)$. □

**What the two lower bounds mean.** $k_B T R(D)$ is the best possible floor for an observer that could encode the source reading directly. $k_B T R^{\mathrm{clock}}_K(D)$ includes the informational penalty of receiving only the partial record $\rho$. The gap $R^{\mathrm{clock}}_K(D) - R(D) \geq 0$ is a precise candidate for the price of mediated access to external time.

## 5. Finite-history version

Let $\Theta^n$ be a hidden clock history, $\rho^n$ its delivered record, $G_n$ the complete block footprint renewed after use, and $\hat{\Theta}^n$ the reconstruction, with the per-symbol distortion $d_n = (1/n)\sum_i d(\theta_i, \hat{\theta}_i)$. Define $R^{\mathrm{clock}}_{K,n}(D) := (1/n)\inf$ over $P(\hat{\theta}^n \mid \rho^n)$ with $E\,d_n \leq D$ of $I(\rho^n; \hat{\Theta}^n)$, and the direct block function $R^{(n)}_\Theta(D)$ analogously. The same proof, with vectors replacing single variables, gives

*[see the displayed block inequality in the PDF, Section 5 — $\langle W^{(n)}_{\mathrm{renew}} \rangle / (n k_B T) \geq R^{\mathrm{clock}}_{K,n}(D) \geq R^{(n)}_\Theta(D)$]*

The finite-block inequality accommodates correlated clock histories and a history-dependent channel $K_{C \to S}$; no i.i.d. assumption is needed. Stationarity or ergodicity becomes relevant only in the long-history limit.

## 6. Closed form: a uniform M-phase clock

Let $\Theta$ be uniform on $\mathbb{Z}_M$ with Hamming distortion $d(\theta, \hat{\theta}) = \mathbb{1}\{\theta \neq \hat{\theta}\}$. If the clock-reading error probability is $p_e$, then for $0 \leq p_e \leq 1 - 1/M$ the ordinary rate–distortion function is $R(p_e) = \ln M - h_2(p_e) - p_e \ln(M - 1)$, where $h_2$ is the binary entropy (nats). Hence $\langle W_{\mathrm{renew}} \rangle \geq k_B T [\ln M - h_2(p_e) - p_e \ln(M-1)]$; for exact reconstruction $\langle W_{\mathrm{renew}} \rangle \geq k_B T \ln M$; for $p_e \geq 1 - 1/M$ a constant guess meets the target and the floor is zero.

**Channel-aware closed form.** Let the record pass through an $M$-ary symmetric channel with substitution error $0 \leq u < 1 - 1/M$. The posterior given $\rho$ assigns probability $1 - u$ to $\Theta = \rho$ and $u/(M-1)$ to each other value, so Lemma III.1's modified distortion is affine in the Hamming indicator on the record alphabet:

*[see the displayed expression for $\tilde{d}(\rho, \hat{\theta}) = u + c\,\mathbb{1}\{\hat{\theta} \neq \rho\}$, $c = 1 - Mu/(M-1)$, in the PDF, Section 6]*

The constraint $E\,\tilde{d} \leq D$ is therefore equivalent to a Hamming constraint on $(\rho, \hat{\Theta})$ at level $\delta(D, u) = (D - u)/c$, the feasibility floor is $D \geq u$ (the Bayes risk), and since $\rho$ is itself uniform on $\mathbb{Z}_M$, Lemma III.1 reduces the indirect problem to the ordinary uniform-source problem at level $\delta$:

*[see the displayed closed form for $R^{\mathrm{clock}}_K(D) = \ln M - h_2(\delta) - \delta \ln(M-1)$ in the PDF, Section 6]*

continuously, since $\delta(1 - 1/M, u) = 1 - 1/M$. Channel noise does not merely change the achieved error: it raises the minimum reusable-memory rate, and target distortions below $u$ are physically unattainable regardless of reset work.

## 7. Minimal test model: loss, substitution, and raw-memory overhead

Take a uniform $M$-phase clock and a delivered record for which the complete renewed footprint is just the raw register, $G = A = \rho \in \mathbb{Z}_M \cup \{\bot\}$. For every true phase $\theta$: an erasure $\bot$ occurs with probability $\varepsilon$; conditional on non-erasure, the correct phase is delivered with probability $1 - u$ and each wrong phase with probability $u/(M-1)$. Decoding a received phase literally and guessing uniformly after erasure gives $D = (1 - \varepsilon)u + \varepsilon(1 - 1/M)$. The raw register entropy is $H(A) = h_2(\varepsilon) + (1 - \varepsilon)\ln M$, and the clock information reaching it is $I(\Theta; A) = (1 - \varepsilon)[\ln M - h_2(u) - u \ln(M-1)]$. The induced reconstruction channel $\Theta \to \hat{\Theta}$ is $M$-ary symmetric at error $D$, so $I(\Theta; \hat{\Theta}) = R(D)$, and the model separates the quantities through two valid chains: $H(A) \geq I(A; \hat{\Theta}) \geq R^{\mathrm{clock}}_K(D) \geq R(D)$, and $H(A) \geq I(\Theta; A) \geq I(\Theta; \hat{\Theta}) = R(D)$. There is no universal ordering between $I(A; \hat{\Theta})$ and $I(\Theta; A)$; they answer different questions.

**Proposition III.1 (exact indirect frontier).** Put $D_B = (1 - \varepsilon)u + \varepsilon(1 - 1/M)$, $c = 1 - Mu/(M-1)$, and $\delta(D) = (D - D_B)/((1 - \varepsilon)c)$ for $D \in [D_B, 1 - 1/M]$. Then

*[see the displayed closed form for $R^{\mathrm{clock}}_K(D) = (1-\varepsilon)[\ln M - h_2(\delta) - \delta \ln(M-1)]$ in the PDF, Section 7]*

with $R^{\mathrm{clock}}_K = +\infty$ for $D < D_B$ and 0 for $D \geq 1 - 1/M$. In particular $R^{\mathrm{clock}}_K(D_B) = (1 - \varepsilon)\ln M$.

*Proof.* By Lemma III.1 compute $\tilde{d}$ on the record alphabet. For $a = \bot$ the posterior of $\Theta$ is uniform, so $\tilde{d}(\bot, \hat{\theta}) = 1 - 1/M$ for every $\hat{\theta}$: the erased branch contributes the constant $\varepsilon(1 - 1/M)$ to distortion for any decoder and can contribute zero rate. For $a \neq \bot$, as in §6, $\tilde{d}(a, \hat{\theta}) = u + c \cdot \mathbb{1}\{\hat{\theta} \neq a\}$. Writing $B = \mathbb{1}\{\rho = \bot\}$ (a function of $\rho$) and $\pi = P(\hat{\Theta} \neq \rho \mid B = 0)$, the constraint $E\,\tilde{d} \leq D$ is equivalent to $\pi \leq \delta(D)$. Converse: $I(\rho; \hat{\Theta}) = I(B; \hat{\Theta}) + I(\rho; \hat{\Theta} \mid B) \geq (1 - \varepsilon) I(\rho; \hat{\Theta} \mid B = 0) \geq (1 - \varepsilon)[\ln M - h_2(\pi) - \pi \ln(M-1)] \geq (1 - \varepsilon)[\ln M - h_2(\delta) - \delta \ln(M-1)]$, using that $\rho \mid B = 0$ is uniform on $\mathbb{Z}_M$ and that the uniform-source Hamming rate–distortion function is nonincreasing. Achievability: on $B = 0$ use the optimal symmetric test channel at Hamming level $\delta$ (whose output marginal is uniform); on $B = 1$ draw $\hat{\Theta}$ uniformly, independently of everything. Then $\hat{\Theta}$ is uniform and independent of $B$, so $I(B; \hat{\Theta}) = 0$ and $I(\rho; \hat{\Theta} \mid B = 1) = 0$, giving $I(\rho; \hat{\Theta}) = (1 - \varepsilon)[\ln M - h_2(\delta) - \delta \ln(M-1)]$ exactly. □

**Remark (exact attainment).** The frontier of Proposition III.1 is attained at $D_B$ by the literal decoder itself: its output marginal is uniform on $\mathbb{Z}_M$ ($H(\hat{\Theta}) = \ln M$), its conditional entropy is $H(\hat{\Theta} \mid A) = \varepsilon \ln M$ (deterministic on delivery, uniform on erasure), hence $I(A; \hat{\Theta}) = (1 - \varepsilon)\ln M = R^{\mathrm{clock}}_K(D_B)$, while its distortion equals $D_B$ by construction. The minimum-distortion point of the indirect frontier is therefore achieved exactly, not merely approached.

Consequently $H(A) - R^{\mathrm{clock}}_K(D_B) = h_2(\varepsilon)$ is the raw cost of retaining the erasure flag, while $R^{\mathrm{clock}}_K(D_B) - R(D_B)$ quantifies the additional rate required because the observer encodes a noisy record rather than the hidden clock state itself.

**Numerical checkpoint.** For $M = 8$, $\varepsilon = 0.2$, $u = 0.1$: $D = 0.255$; $H(A) = 2.164$ nat, $I(\Theta; A) = 1.248$ nat, $R^{\mathrm{clock}}_K(D_B) = 1.664$ nat, $R(D) = 1.015$ nat. At $T = 300$ K ($k_B T \approx 4.142$ zJ): ideal reset of the raw register requires at least $\approx 8.96$ zJ; the direct source floor is $\approx 4.21$ zJ; the stronger channel-aware floor at minimum attainable distortion is $\approx 6.89$ zJ. The differences are the energetic prices of raw representation, channel constraints, and unused record entropy respectively. Appendix N verifies both closed forms against a Blahut–Arimoto solver to machine precision; the exact attainment at $D_B$ is the Remark above.

> **Figure III.1.** *[see the figure in the PDF, Section 7]* Thermodynamic rate–distortion hierarchy for the noisy external-clock record at $(M, \varepsilon, u) = (8, 0.2, 0.1)$: raw-register cost $H(A)$, channel-aware frontier $R^{\mathrm{clock}}_K(D)$, source–record information $I(\Theta; A)$, and direct frontier $R_\Theta(D)$ separate as the allowed distortion varies; the literal decoder sits on the frontier at $D_B$. Curves are the solver-verified closed forms of §6 and Proposition III.1.

## 8. Sequential ring corollary: renewal pays for innovation, not ticks

Consider a genuinely evolving $M$-phase clock $\Theta_{k+1} = \Theta_k + 1 + J_k \pmod M$, with $\Theta_0$ uniform and independent jitter $P(J_k = 0) = 1 - \eta$, $P(J_k = \pm 1) = \eta/2$. For $M \geq 3$ the step alphabet $\{0, 1, 2\}$ is injective mod $M$, so the increments are recoverable from the recorded path, and an exact length-$n$ history has entropy $H(\Theta_0, \ldots, \Theta_n) = \ln M + n[h_2(\eta) + \eta \ln 2]$. Lossless closed renewal therefore obeys

*[see the displayed per-step bound in the PDF, Section 8 — $\langle W^{(n)}_{\mathrm{renew}} \rangle / (n k_B T) \geq h_2(\eta) + \eta \ln 2 + (\ln M)/n$]*

In the long-history limit the work floor per step is the entropy of the unpredictable innovations, not the number of ticks. For a deterministic ring ($\eta = 0$) only the initial phase must be retained: the optimally compressed renewal cost per tick tends to zero even though the clock keeps changing state. This is a quantitative corollary of the separation principle of [1].

## 9. Tightness

The inequality is one-shot, but simultaneous equality is generally unavailable for a single noisy symbol: $H(G) = I(\Theta; G)$ requires $G$ conditionally deterministic given $\Theta$, whereas a single-letter rate–distortion optimum is often stochastic. The bound becomes operationally tight in the asymptotic i.i.d. setting if long record blocks are encoded by a deterministic rate–distortion code; the code index is the only clock-correlated memory that remains; encoding, reconstruction, and workspace cleanup are performed reversibly or fully included in the accounting; and the code-index register is reset quasistatically. Then $H(G_n)/n \to R^{\mathrm{clock}}_K(D)$ and $\langle W^{(n)}_{\mathrm{renew}} \rangle / n \to k_B T R^{\mathrm{clock}}_K(D)$. Finite-time reset, finite baths, imperfect control, and uncompressed raw records all increase the required work.

## 10. Three floors of the accessible clock

The series now prices the accessible clock coordinate three times, and the three floors are mathematically disjoint.

**Floor 1 — channel information ([2], Theorem II.A).** Reconstruction: the minimax mean-squared error through the erasure channel is exactly $n p \sigma^2$ per window. It constrains an estimation error, is enforced by conditioning (the exact Bayes filter), and is paid in lost calibration fluctuation. It binds even for a dissipationless, never-reset observer.

**Floor 2 — register precision ([2], Theorem II.D).** Reading: for a register in a nonequilibrium steady state, $\mathrm{Var}(\hat{t})/\langle \hat{t} \rangle^2 \geq 2/\Sigma_{\mathrm{reg}}$. It constrains the relative variance of a current, is enforced by the thermodynamic uncertainty relation, and is paid in the register's own dissipation while it runs. It binds even for a perfect channel ($\sigma^2 = 0$, $p = 0$), where Floor 1 vanishes.

**Floor 3 — renewal work (Theorem III.1 here).** Reuse: $\beta \langle W_{\mathrm{renew}} \rangle \geq R^{\mathrm{clock}}_K(D)$. It constrains the average reset work, is enforced by Landauer's bound plus data processing, and is chargeable even at zero entropy production, since a quasistatic reset saturates it: it bounds work, not dissipation. It binds even for an infinitely dissipative register and vanishes only if the observer never reuses its footprint.

No floor implies another: Floor 1 survives $\Sigma_{\mathrm{reg}} \to \infty$ and $W \to \infty$; Floor 2 survives $\sigma^2 = 0$; Floor 3 survives $\Sigma_{\mathrm{reg}} \to 0$. They constrain three different observables (mean-squared error; relative variance; work) by three different mechanisms (Bayes conditioning; TUR; Landauer). The channel is nonetheless present inside Floor 3: $R^{\mathrm{clock}}_K$ internalizes it, and its domain boundary — infeasibility below the Bayes risk — is Floor 1's destruction re-expressed as unattainability. Two scope remarks carry over. Floor 2 is proved in [2] for erasure-type registers and fails for the aggregating channel by weight–count anticorrelation. Floor 1's underlying Bayes-variance form, risk $\geq E[\mathrm{Var}(t_C \mid \text{record})]$, is channel-agnostic, but its exact constant $n p \sigma^2$ is specific to the erasure channel of [2]; Floor 3 is channel-agnostic outright — any delivery law enters only through $R^{\mathrm{clock}}_K$.

## 11. What the theorem does not say

The theorem does not establish a universal energetic cost of time. It does not imply that: every clock tick dissipates $k_B T$ times some fixed information; measurement or discrimination necessarily has the Landauer cost at the moment it occurs; generation, transmission, registration, storage, and reset have one interchangeable cost; time, work, information, or entropy production are identical; a memory that is never reset has already paid the reset bound; or that correlations may be used during reset for free. The reset-work bound can be saturated quasistatically with zero irreversible entropy production, and therefore must not be restated as a lower bound on dissipated work or on $\Sigma$.

If correlated side information $Z$ survives and is available to the reset controller, then for any decoder of the form $\hat{\Theta} = \delta(G, Z)$ the conditional extension is $\beta \langle W_{\mathrm{renew}} \rangle \geq H(G \mid Z) \geq I(\Theta; G \mid Z) \geq I(\Theta; \hat{\Theta} \mid Z) \geq R_{\cdot \mid Z}(D)$, and the local cost can be smaller [9]; if $Z$ survives but is unavailable to the controller, the unconditional $H(G)$ is the relevant cost. Information about external time may migrate between registers, but deleting the last usable copy is the operation to which the closed-renewal cost belongs. Accordingly, the system boundary must identify both the information-bearing footprint being renewed and every surviving copy excluded from that renewal accounting [18]. The source also needs a nontrivial prior — a random query time, a stochastic clock path, or uncertainty induced by partial observation; if $\Theta$ is deterministic its rate–distortion function is zero and the bound is vacuous. For nondegenerate memory states the first step must be replaced by the appropriate generalized free-energy inequality; the simple $k_B T H(G)$ form is specific to the symmetric equal-free-energy model of [1].

## 12. The open target: causal external-time rate–distortion

The finite-history theorem permits block encoding after the complete record is available; a real observer reconstructs time online. A causal extension would impose nonanticipation, $P(\hat{\theta}_i \mid \rho^n, \hat{\theta}^{i-1}) = P(\hat{\theta}_i \mid \rho^i, \hat{\theta}^{i-1})$, leading to a causal indirect rate–distortion function, naturally expressed through directed information, with target statement $\liminf \beta \langle W^{(n)}_{\mathrm{renew}} \rangle / n \geq R^{\mathrm{causal}}_K(D)$. That extension would exercise the full distinctive architecture of [1]: causal partial order, a selected clock subsystem, loss, delay, duplication, aggregation and out-of-order delivery, finite reusable memory, and physically implemented reset. The single-record theorem is the present foundation; a causal history theorem remains open.

## 13. Relation to prior work

The proof ingredients are established: Shannon rate–distortion theory [6]; the indirect rate–distortion function itself [3, 4, 5]; Landauer erasure [7]; data processing; information thermodynamics of measurement and erasure [8]; model-specific accuracy–dissipation relations for physical clocks [10, 11, 12]. None of the primitive inequalities is claimed as new. The specific contribution is their integration into the external-clock architecture of [1, 2]: the hidden clock state belongs to a metasystem outside the observed boundary; the observer has access only to a record delivered through $K_{C \to S}$; clock accuracy is a reconstruction distortion; reusable memory carries an explicit reset cost; and the resulting bound separates direct source complexity, channel-mediated complexity, and raw-register overhead. The explicit treatment of that boundary as part of the information and work attribution is aligned with the boundary formalism developed in [18]. To the best of our knowledge, this is the first explicit rate–distortion lower bound on the thermodynamic renewal cost of a reusable, lossy external-time record.

**Closest precedents and the remaining gap.** Sagawa & Ueda [8]: work bounds for measurement and erasure in terms of entropy and mutual information — no external clock, reconstruction distortion, or clock-delivery channel. Erker et al. [11]: autonomous clockwork with a tick register whose reset is recognized as an additional Landauer cost — the derived accuracy–dissipation relation excludes record measurement/erasure; no lossy decoder or rate–distortion bound. Still, Sivak, Bell & Crooks [13]: dissipation bounded by non-predictive information retained in a driven system's memory — prediction of a driving signal, not renewal of an external-time record through a specified channel. Gagliardi, Pecchia & Di Carlo [14]: rate–distortion in thermodynamic feedback — feedback benefit, not renewal cost. Nair [15]: rate–distortion limits in optical metrology — probe/channel energy, not Landauer reset work of reusable memory. Gammaitoni [16]: imperfect binary erasure of the form $k_B T[\ln 2 - h_2(p)]$ — the error belongs to the erasure operation itself, not to a clock record subsequently reset exactly. del Rio et al. [9]: side information turns erasure work into a conditional-entropy problem — supplies the boundary condition of §11, not the clock theorem. Hsieh [17]: bounds information transmission by work extractable from maintained correlations — distinct from the cost of erasing a reusable channel record.

## 14. Outlook

(1) Extend the Blahut–Arimoto verification of Appendix N to record alphabets with delay and out-of-order delivery. (2) Prove the nonanticipative finite-memory version using directed information. (3) Derive conditional bounds when the observer retains side information. (4) Connect the information floor to a concrete reset protocol for a double-well, nanomagnetic, or electronic memory [12]. (5) Separate measured work into generation, transmission, registration, compression, and reset terms, closing the loop with the cost taxonomy of [1, §11].

The division across the three parts is therefore explicit: Part I says external time is a functional of a partial physical record; Part II says what the channel and the running register irreducibly cost; Part III says how much reusable physical memory — and therefore how much ideal reset work — is required to realize that functional at a chosen accuracy.

## Appendix N. Numerical verification

All computations use NumPy; the stochastic checks report their PCG64 seeds, sample sizes, and target quantities to support independent reproduction.

### N.1. Channel-aware closed form (§6)

A Blahut–Arimoto solver (fixed-point iteration on the output marginal, tolerance $10^{-13}$, with bisection on the Lagrange slope to hit each target distortion) was run on the record alphabet $\mathbb{Z}_M$ with the modified distortion of Lemma III.1. Twelve points across four regimes $(M, u) \in \{(8, 0.10), (5, 0.20), (3, 0.05), (12, 0.15)\}$, at 15%, 50%, and 85% of the feasible distortion range: the solver agrees with the closed form at every point, worst deviation $8.9 \cdot 10^{-16}$ nat — machine precision. The solver has no knowledge of the closed form.

### N.2. Exact indirect frontier (Proposition III.1)

The same solver on the $(M+1)$-letter alphabet $\mathbb{Z}_M \cup \{\bot\}$ with $\tilde{d}(\bot, \cdot) = 1 - 1/M$ constant: nine points across $(M, \varepsilon, u) \in \{(8, 0.2, 0.1), (5, 0.3, 0.15), (6, 0.1, 0.05)\}$ at 20%, 55%, and 90% of the feasible range agree with Proposition III.1 at every point, worst deviation $5.0 \cdot 10^{-16}$ nat.

### N.3. Ring history entropy (§8)

Exact enumeration of all path laws at $(M, n, \eta) = (3, 6, 0.3)$ and $(5, 4, 0.2)$: the map $(\Theta_0, J_1, \ldots, J_n) \mapsto (\Theta_0, \ldots, \Theta_n)$ is bijective ($2187 = 3 \cdot 3^6$ and $405 = 5 \cdot 3^4$ distinct paths respectively — the $M = 3$ boundary of the hypothesis is exercised), and the exact path entropy equals $\ln M + n[h_2(\eta) + \eta \ln 2]$ to $4 \cdot 10^{-14}$.

### N.4. Test model: end-to-end chain

Seed 13, $10^6$ samples at $(M, \varepsilon, u) = (8, 0.2, 0.1)$: empirical $D = 0.2545$ (theory 0.2550), $H(A) = 2.1642$ (2.1640), $I(\Theta; A) = 1.2490$ (1.2478), $I(\Theta; \hat{\Theta}) = 1.0168$ ($R(D) = 1.0155$). The literal decoder gives $I(A; \hat{\Theta}) = 1.6643$ against $(1 - \varepsilon)\ln M = 1.6636$, confirming the exact attainment of the Remark after Proposition III.1 within sampling error. The full chain realizes as $2.164 \geq 1.664 \geq 1.664 \geq 1.015$. Lemma III.1's identity $E\,d(\Theta, \hat{\Theta}) = E\,\tilde{d}(\rho, \hat{\Theta})$ was additionally verified on a randomly drawn decoder kernel: 0.87096 vs 0.87100 (sampling error $3.5 \cdot 10^{-5}$).

## References

[1] Vityaz, A. (2026). *Ontology of Transition—Part I: Causal Order of Events, Internal and External Clocks, Thermodynamics, and Information-Theoretic Distinguishability*. Zenodo. https://doi.org/10.5281/zenodo.21471785 — in this repository: [`../part-i/`](../part-i/)

[2] Vityaz, A. (2026). *Ontology of Transition—Part II: The Unidentifiable Clock: Reconstruction Limits and Gauge Freedom of External Time under Lossy Delivery*. Zenodo. https://doi.org/10.5281/zenodo.21472271 — in this repository: [`../part-ii/`](../part-ii/)

[3] Dobrushin, R. L., & Tsybakov, B. S. (1962). Information transmission with additional noise. *IRE Transactions on Information Theory*, 8(5), S293–S304.

[4] Wolf, J. K., & Ziv, J. (1970). Transmission of noisy information to a noisy receiver with minimum distortion. *IEEE Transactions on Information Theory*, 16(4), 406–411.

[5] Witsenhausen, H. S. (1980). Indirect rate distortion problems. *IEEE Transactions on Information Theory*, 26(5), 518–521.

[6] Shannon, C. E. (1959). Coding theorems for a discrete source with a fidelity criterion. *IRE National Convention Record*, Part 4, 142–163.

[7] Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5, 183–191.

[8] Sagawa, T., & Ueda, M. (2009). Minimal energy cost for thermodynamic information processing: measurement and information erasure. *Physical Review Letters*, 102, 250602.

[9] del Rio, L., Åberg, J., Renner, R., Dahlsten, O., & Vedral, V. (2011). The thermodynamic meaning of negative entropy. *Nature*, 474, 61–63.

[10] Barato, A. C., & Seifert, U. (2016). Cost and precision of Brownian clocks. *Physical Review X*, 6, 041053.

[11] Erker, P., Mitchison, M. T., Silva, R., Woods, M. P., Brunner, N., & Huber, M. (2017). Autonomous quantum clocks: does thermodynamics limit our ability to measure time? *Physical Review X*, 7, 031022.

[12] Gopal, A., Esposito, M., & Freitas, N. (2023). Thermodynamic cost of precise timekeeping in an electronic underdamped clock. arXiv:2308.10074.

[13] Still, S., Sivak, D. A., Bell, A. J., & Crooks, G. E. (2012). Thermodynamics of prediction. *Physical Review Letters*, 109, 120604.

[14] Gagliardi, A., Pecchia, A., & Di Carlo, A. (2016). Large deviation theory to model systems under an external feedback. arXiv:1603.03786.

[15] Nair, R. (2018). Fundamental quantum limits in optical metrology from rate-distortion theory. *Journal of Physics A*, 51, 434001.

[16] Gammaitoni, L. (2011). Beating the Landauer's limit by trading energy with uncertainty. arXiv:1111.2937.

[17] Hsieh, C.-Y. (2022). Dynamical Landauer Principle: Quantifying Information Transmission by Thermodynamics. arXiv:2201.12110.

[18] Vityaz, A. (2026). *The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin*. Zenodo. https://doi.org/10.5281/zenodo.20745927 — in this repository: [`../../2026-computable-boundary-of-the-firm/`](../../2026-computable-boundary-of-the-firm/)
