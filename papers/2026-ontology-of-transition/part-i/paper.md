---
title: "Ontology of Transition—Part I: Causal Order of Events, Internal and External Clocks, Thermodynamics, and Information-Theoretic Distinguishability"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-07-21
doi: 10.5281/zenodo.21471785
series-doi: 10.5281/zenodo.21380580
version: v1
license: CC-BY-4.0
keywords: [process ontology, causal order, event time, internal time, external time, partial observability, discrete-event systems, stochastic thermodynamics, information-theoretic distinguishability]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.5281/zenodo.21471785](https://doi.org/10.5281/zenodo.21471785). This part is also published within the complete three-part volume, [doi:10.5281/zenodo.21380580](https://doi.org/10.5281/zenodo.21380580).

# Ontology of Transition—Part I

## Causal Order of Events, Internal and External Clocks, Thermodynamics, and Information-Theoretic Distinguishability

Alexander Vityaz
Corezoid Inc., Dnipro, Ukraine
corezoid.com · simulator.company
ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

**Standalone DOI:** https://doi.org/10.5281/zenodo.21471785

**Part of the complete three-part volume:** *Ontology of Transition: Causal Order, External Time, and the Thermodynamics of Physical Clock Records* — https://doi.org/10.5281/zenodo.21380580

## Abstract

This article takes transition rather than thing as the primary unit of ontological description. Its primitive structure is a locally finite causally ordered event set without presupposed numerical time. A system S is embedded in a metasystem M. The reading of S's internal event clock is an additive functional of selected intrinsic transitions; its accessible external-clock coordinate is a functional of a physical record of C<sub>M</sub> outside S. Transmission and registration may omit, aggregate, delay, or distort ticks, making the record partial and local. Calibration assigns durations to discrete ticks; continuous time enters only by interpolation or a scaling limit. Energy and calibrated skeletons make thermodynamic and path functionals invariant under admissible linearizations. A separation principle states that time, work, information-theoretic distinguishability, and entropy production share transition histories but are not identical: they differ in arguments, dependencies, symmetry properties, and physical prerequisites. Equilibrium, quasistatic, cyclic, and protocol-dependent counterexamples establish their irreducibility; their relations are conditional balances and bounds. Observation is a discrimination channel whose cost belongs to its physical implementation. A recognition scheme separates ensemble-stable object types from realization-stable object tokens. A thing is a stable, recognizable organization of transitions; operational clock discreteness does not imply discrete spacetime.

**Keywords:** process ontology; causal order; event time; external clocks; partial observability; discrete-event system; stochastic thermodynamics; entropy production; KL divergence; object type; object token.

## 1. From Thing to Transition

The conventional descriptive scheme presupposes a thing prior to its change:

*[see Eq. (1) in the PDF, § 1: "thing ⟶ change of the thing"]*

First an object is identified, then a state is ascribed to it, and only afterward is a change of that state considered. This sequence is natural in language and everyday experience, but it is not obligatory as an ontological commitment. The present work adopts the reverse order:

*[see Eq. (2) in the PDF, § 1: "transitions ⟶ stable regimes of transitions ⟶ things"]*

The thing is not thereby denied. Rather, it receives a derivative definition: a stable fragment of a process that preserves recognizable features over a certain time scale. An object is not the absence of change but a reproducible organization of change.

The notation

$$S_0 \longrightarrow S_1 \tag{3}$$

records only the endpoints. It does not indicate how long the transition lasted, which path realized it, how much work was performed, whether irreversibility arose, or whether the selected observation channel can distinguish the forward history from its time reverse. The basic unit of description below is therefore an explicit dynamical specification of a transition.

### 1.1 Contribution of This Work

The physical relations used in §§ 6–10 are established results of stochastic thermodynamics and information theory. The decomposition of energy into work and heat, the trajectory-level expression for entropy production, the data-processing inequality, nonequilibrium free energy, and Landauer's principle are not presented here as new results [21, 8, 29, 28, 24].

The article's original contribution consists of five steps:

1. the precedence relation among events is adopted as the primitive structure of description, while scalar clocks are constructed only on causally ordered local histories;

2. a system's internal time is defined by the accumulation of its own transitions, whereas its external time is defined by a physically transmitted record of a selected clock process in the metasystem;

3. partial observability of external states is introduced explicitly through a channel that may conceal events and thereby generate local time coordinates that are generally asynchronous;

4. continuous time parameterization and thermodynamic and informational functionals are separated from causal order, while energy balances are defined on an invariant energy skeleton of the history;

5. objecthood is operationalized through a recognition scheme in which ensemble stability and the stability of an individual realization are distinguished as object type and object token, respectively.

Thus, the article proposes neither a new formula of stochastic thermodynamics nor a proof of the fundamental discreteness of spacetime. It develops an original formal framework in which causal order, local clock records, thermodynamic and informational functionals, and operational criteria of objecthood are jointly defined, while their non-equivalence and invariance properties are established under explicit conditions. A worked example exercising the clock channel and the recognition scheme end to end is given in Appendix B.

The principal notation of the framework is collected below; each symbol is defined at the indicated equation or section and used consistently thereafter.

| Symbol | Meaning | Defined at |
|---|---|---|
| $\mathcal{E}_M=(E_M, \prec_M, \ell_M)$ | labeled, locally finite causal partial order of the metasystem | (4)–(6) |
| $H$; $\gamma_n$ | causally closed configuration; local chain of a sequential subsystem | (7)–(8) |
| $x_k$, $\lambda_k$, $p_k^S$ | system state, protocol value, and system marginal on the $k$-th slice | (11) |
| $\mathcal{M}_{ev}$; $\mathcal{M}_{th}$ | stochastic transition specification; its thermodynamic extension | (12); (40) |
| $\theta_S^{int}$, $\theta_{S,w}^{int}$ | internal event time of the system (weighted count of intrinsic changes) | (15)–(17) |
| $C$; $\theta_C^{int}$; $t_C$ | clock process; its internal tick count; its calibrated source coordinate | (19); (26) |
| $\rho$; $r_j$; $w_j$ | delivery record; register state; decoded tick increment | (20), (A1) |
| $\theta_{S\|C}^{ext}$; $t_{S\|C}$ | external time accessible to the system; its decoded calibrated coordinate | (20); (27) |
| $K_{C\to S}$; $O_S$, $O_M$ | history-dependent clock channel; state-observation channels | § 3.2; (32)–(36) |
| $\mathcal{A}(\mathcal{D})$; $\mathcal{C}_{S,O,path}(\mathcal{D})$, $\mathcal{C}_{S,O,ens}(\mathcal{D})$ | typed map of admissible characteristics; record of characteristics | (37)–(39) |
| $sk_E$; $sk_{clk}$ | energy skeleton; calibrated skeleton of an execution | § 6, Prop. I.1 |
| $\sigma$; $\Sigma$; $D_{end}^{O}$; $A^{O}$ | pathwise and mean entropy production; endpoint and path distinguishability | (53), (56); (57)–(58) |
| $R^*$; $B_a$; $\varepsilon$; $h$ | recognition scheme; type region; tolerance; averaging window | (74) |
| $\ell_{int}$, $\ell_{ext}$ | internal and external durations of an object segment | (82) |

## 2. Specification of a Transition

Let M be a metasystem containing the system under study S, and let

*[see Eq. (4) in the PDF, § 2: definition of the labeled causal partial order $\mathcal{E}_M=(E_M, \prec_M, \ell_M)$]*

be its labeled, locally finite causal partial order. Here $E_M$ is the set of events, $\ell_M$ their labels, and $\prec_M$ a strict precedence relation:

*[see Eq. (5) in the PDF, § 2: irreflexivity and transitivity of $\prec_M$]*

The relation $\prec_M$ is taken as a primitive of the construction: $e \prec_M f$ means that the outcome of $e$ may enter the conditions of $f$. It is not defined in terms of a numerical instant of time. For comparable events, local finiteness is additionally assumed:

*[see Eq. (6) in the PDF, § 2: finiteness of the set of events causally between two comparable events]*

Incomparable events may occur in parallel. Event conflict is not modeled separately in the present construction. Consequently, the global history of M is generally partially rather than linearly ordered. Scalar clocks do not reconstruct this entire structure: they provide an order-preserving valuation on a selected causal chain; a total order requires an additional rule for incomparable events. This separation between event order and clock readings accords with the logic of happened-before in distributed systems and employs the causal layer incorporated into the richer formalism of event structures [20, 32].

A realized configuration $H \subseteq E_M$ is assumed to be causally closed:

*[see Eq. (7) in the PDF, § 2: causal closure of a configuration]*

The local history of a single sequential subsystem is a chain

*[see Eq. (8) in the PDF, § 2: $\gamma_n = e_1 \prec_M e_2 \prec_M \cdots \prec_M e_n$]*

To associate events with states of the metasystem, one selects a nested sequence of causally closed configurations

*[see Eq. (9) in the PDF, § 2: nested sequence $H_0 \subset H_1 \subset \cdots \subset H_n$ with $H_k = H_{k-1} \cup \{e_k\}$]*

This selected linear execution does not render incomparable events causally related.

When the specification includes a control protocol, both the system state and the protocol value are likewise defined as functions of a causally closed configuration: $x = x(H)$ and $\lambda = \lambda(H)$. Let $E_S$ denote events that change $x$, and $E_\lambda$ events that change $\lambda$, under an admissible addition of an event to a configuration. For the thermodynamic history under consideration, each of the sets $E_S$ and $E_\lambda$ forms a local chain. If a single physical event changes both $x$ and $\lambda$, it is refined into two causally ordered elementary substeps; hence these sets are taken to be disjoint below. We adopt the axiom of protocol–system comparability:

*[see Eq. (10) in the PDF, § 2: comparability of every protocol event with every system event]*

It follows that the thermodynamically significant set $E_{th} = E_S \cup E_\lambda$ is itself a chain and has the same order in every linear execution of the given causal order. An event outside $E_{th}$ is called thermodynamically silent if its admissible addition does not change the pair $(x, \lambda)$. On the selected slices, states and distributions take the form

*[see Eq. (11) in the PDF, § 2: $m_k = m(H_k)$, $x_k = \pi_S(m_k)$, $\lambda_k = \lambda(H_k)$, $p_k^S = \pi_{S\#}p_k^M$]*

Here $\pi_S : X_M \to X_S$ specifies the boundary and state space of the system S. The phrase "state change" means a difference between configurations on two nested slices; it does not presuppose an already introduced continuous parameter.

A general stochastic specification of a transition is given by the tuple

*[see Eq. (12) in the PDF, § 2: $\mathcal{M}_{ev} = (\mathcal{E}_M, X_M, \pi_S, p_0^M, \lambda_\bullet, P^M)$]*

where $p_0^M \in \mathcal{P}(X_M)$ is the initial distribution; $\lambda_\bullet = (\lambda(H_0), \ldots, \lambda(H_n))$ takes values in $\Lambda$ and represents a single configuration-dependent protocol variable on the selected slices; and $P^M$ is a measure on causally admissible histories. This notation also encompasses non-Markovian models. In the fixed-length $n$ Markovian specialization, the measure is generated by transition kernels $K_k$:

*[see Eq. (13) in the PDF, § 2: Markovian factorization of $P^M$ through the kernels $K_k$]*

For histories of random length, a stopping law is specified in addition. System trajectory measures are obtained as pushforward measures under the deterministic projection:

*[see Eq. (14) in the PDF, § 2: $P^S = \pi_{S,\#}P^M$]*

Here $p_k^M$ describes the ensemble of the metasystem on the $k$th slice, $p_k^S$ is its system marginal, and $\omega = (m_0, e_1, m_1, \ldots, e_n, m_n)$ is an individual history. The same initial and final configurations may be connected by different event histories; consequently, clocks, work, entropy production, and path distinguishability are generally not determined by endpoints alone.

## 3. Local Clocks: Internal and External Time

### 3.1 Internal Event Time of a System

Let $\gamma_n$ be a local history of S, and let $x_k = \pi_S(m_k)$ be its states on successive causal slices. The predicate of an intrinsic change is

*[see Eq. (15) in the PDF, § 3.1: $\delta_S(e_k) = \mathbb{1}\{x_k \neq x_{k-1}\}$]*

For a nonnegative weight function $w_S : X_S \times X_S \to \mathbb{R}_{\geq 0}$ that is positive for every included change $x \to x'$, internal event time is defined as an additive measure of changes along the local history:

*[see Eq. (16) in the PDF, § 3.1: $\theta_{S,w}^{int}(\gamma_n) = \sum_{k=1}^{n} w_S(x_{k-1}, x_k)\,\delta_S(e_k)$]*

With unit weights, each intrinsic transition generates one internal tick:

*[see Eq. (17) in the PDF, § 3.1: $\theta_S^{int}(\gamma_n) = \sum_{k=1}^{n} \delta_S(e_k) = N_S(\gamma_n)$]*

Internal time is not a medium in which events occur: its reading is changed by the events themselves. Nor does it generate their order—the order is already specified by the relation $\prec_M$. This breaks the possible logical circle in which "change is defined in time, while time is defined through change."

In the theory of continuous-time random walks, the jump number is called discrete operational time [15]. Here the expression "internal event time" is used as the author's term for a measure of a system's own changes and does not claim the conventional meaning of internal time in other fields.

The ensemble-averaged internal time after $n$ events in the local record is

*[see Eq. (18) in the PDF, § 3.1: $\langle \theta_S^{int}(\gamma_n) \rangle = \mathbb{E}_{P^S}[\theta_S^{int}(\gamma_n)]$]*

With unit weights it measures mean dynamical activity, and for general $w_S$ it measures mean weighted activity, but not entropy, irreversibility, or work. A reversible transition also generates an internal tick; a spontaneous fluctuation may change the state without work by an external protocol. The number of ticks depends on the boundary of S, its state space, and the model's resolution. For smooth continuous trajectories, the counter must be replaced by an additional metric, path variation, or another clock function, and such a construction is no longer canonical.

### 3.2 External Clocks as a Metasystem Process

Because the global history of M may contain parallel events, merely counting all changes in the metasystem does not define a unique scalar clock. Within the selected decomposition, let us identify a clock subsystem C such that $C \subseteq M$ and $C \cap S = \emptyset$. It lies outside the boundary of S and has a causally ordered chain of ticks

*[see Eq. (19) in the PDF, § 3.2: $C = c_1 \prec_M c_2 \prec_M \cdots$, with $\theta_C^{int}(c_n) = \sum_{k=1}^{n} w_C(c_k)$, $w_C(c_k) > 0$]*

The process C is internal to the metasystem and serves as an external reference only relative to the boundary of S. If S significantly affects the order or statistics of the ticks of C, the joint dynamics of S+C must be modeled explicitly.

For C to serve as an external clock for S, its history must physically produce a record $\rho = (\rho_1, \rho_2, \ldots)$ accessible to the system through a history-dependent channel $K_{C \to S}$. External time is a functional of this record rather than a reading of the entire metasystem. Let $r_j$ be the register state after the $j$th attempt, and let $w_j \geq 0$ be the decoded increment. When $r_j \neq r_{j-1}$, the external time accessible to the system is

*[see Eq. (20) in the PDF, § 3.2: $\theta_{S|C}^{ext}(\rho_n) = \sum_{j=1}^{n} w_j\,\mathbb{1}\{r_j \neq r_{j-1}\}$]*

The index $j$ denotes the index of the source tick that generated the $j$th genuine, nonaggregated attempt; the complete message-provenance model is given in Appendix A. In an ideal channel without loss, duplication, or errors, $\iota(j) = j$, $w_j = w_C(c_j)$, and $\theta_{S|C}^{ext} = \theta_C^{int}$ at the corresponding events. In general, there is no literal equality. Let $\pi_C$ be the measurable projection of the complete history of M onto the clock history of C. Then

*[see Eq. (21) in the PDF, § 3.2: $P^{clock} = \pi_{C,\#}P^M$]*

At the level of probability laws on histories, the channel induces the distribution of output records

*[see Eq. (22) in the PDF, § 3.2: $P^{S|C}(B) = \int K_{C \to S}(B \mid \gamma_C)\, dP^{clock}(\gamma_C)$]*

The reading (20) is a functional $F_{tick}$ of a particular output record. For a stochastic, noisy, or incomplete channel, the appropriate state of knowledge of S may be a conditional distribution of the hidden source reading. Thus, the external states of the metasystem are not assumed to be fully observable to S: the channel may omit, aggregate, delay, or distort ticks. For a deterministic channel that neither creates spurious events nor duplicates them,

*[see Eq. (23) in the PDF, § 3.2: the undercount bound $0 \leq N_{S|C}^{ext}(H) \leq \theta_C^{int}(H)$]*

Here $N_{S|C}^{ext}$ is the number of successful registrations, and both quantities are counted within the same causally bounded window $H$. Noise may generate false ticks, in which case (23) must be replaced by an error model. Memory updating, decoding, the filtering distribution of the hidden clock state, and conditions for recovering message order are deferred to Appendix A.

### 3.3 Registration, Relativity, and Synchronization

An external tick is operationally accessible to the system only insofar as it leaves a distinguishable trace. A successful attempt $j$ becomes a registration event when

*[see Eq. (24) in the PDF, § 3.3: the register transition $(x, r_{j-1}) \to (x, r_j)$ with $r_j \neq r_{j-1}$]*

Reading an external clock is therefore itself an internal transition of the extended system $S^+ = S \cup R$. This does not erase the distinction between the two times: $\theta_S^{int}$ pertains to changes of the selected core S, whereas $\theta_{S|C}^{ext}$ pertains to changes in the register R causally induced by the reference C. The system boundary must be specified explicitly.

On a single segment of a history, one may have

*[see Eq. (25) in the PDF, § 3.3: $\Delta\theta_S^{int} = 0$ while $\Delta\theta_{S|C}^{ext} > 0$]*

when the core S does not change while the external register receives ticks. The converse is also possible: several intrinsic transitions of S may occur between two registered ticks of C. Hence internal and external time cannot be reduced to a single counter.

Systems $S_1$ and $S_2$ that use different clock processes or channels generally acquire different external coordinates. Synchronizing them requires either shared reference events or a protocol for exchanging records. Logical synchronization may reconcile the order of causally related events, but by itself it does not establish equal rates, equal durations, or physical simultaneity.

### 3.4 Calibration and Continuous Representation

Calibration of the source assigns positive increments of physical duration to the ticks of C:

*[see Eq. (26) in the PDF, § 3.4: $t_C(c_n) = t^* + \sum_{k=1}^{n} \tau_k$, $\tau_k > 0$]*

After message loss or aggregation, the system has its own decoded coordinate. Here the index $\ell$ refers to a delivery attempt rather than directly to a source tick: the duration decoder assigns a nonnegative increment $\hat{\tau}_\ell$. Throughout, an increment indexed by a source tick is a source quantity, while an increment indexed by a delivery attempt is its decoded counterpart. For a genuine, nonaggregated signal under exact decoding, $\hat{\tau}_\ell = \tau_{\iota(\ell)}$; in an ideal channel, $\iota(\ell) = \ell$ and $\hat{\tau}_\ell = \tau_\ell > 0$. Aggregated and spurious signals are treated in Appendix A. The decoded coordinate is

*[see Eq. (27) in the PDF, § 3.4: $t_{S|C}(\rho_j) = t^* + \sum_{\ell=1}^{j} \hat{\tau}_\ell\,\mathbb{1}\{r_\ell \neq r_{\ell-1}\}$, $\hat{\tau}_\ell \geq 0$]*

In general, $t_{S|C}(\rho_j)$ does not coincide with $t_C(c_j)$. Even when their values belong to $\mathbb{R}$, the domains of both coordinates remain discrete. A continuous coordinate is introduced through interpolation or obtained within a separately specified family of increasingly fine clocks whose mesh tends to zero. Causal order alone specifies "earlier/later" where events are comparable; the choice of a reference, unit, and measure adds "by how much."

For Markovian dynamics directly on $X_S$, a continuous generator appears as the limiting representation of the full transition kernel on the clock grid, including the probability of no jump:

*[see Eq. (28) in the PDF, § 3.4: $P(t_k, t_{k+1}) = I + \Delta t_k L_k + o(\Delta t_k)$, $\Delta t_k \to 0$]*

from which, under the appropriate convergence conditions, it follows that

*[see Eq. (29) in the PDF, § 3.4: $\partial_t p_t^S = L\,p_t^S$]*

For a Markov jump process directly on $X_S$, when all state transitions are counted, the rate of mean weighted internal time is

*[see Eq. (30) in the PDF, § 3.4: $d\langle\theta_{S,w}^{int}\rangle/dt = \sum_{x}\sum_{x' \neq x} p_t^S(x)\,k_t(x \to x')\,w_S(x, x')$]*

For $w_S \equiv 1$, this is the usual dynamical activity. Thus, stationarity of the distribution is compatible with continuing internal transitions:

*[see Eq. (31) in the PDF, § 3.4: $\partial_t p_t^S = 0$ while $d\langle\theta_S^{int}\rangle/dt > 0$]*

The relation between the number of configuration changes and dynamical activity is used in the statistical mechanics of trajectories [22, 30]. All subsequent continuous-time notation refers to such a calibrated clock representation and does not reinstate $t$ as an ontological primitive.

The hierarchy has four levels: events define causal order; internal clocks accumulate a system's own changes; the external channel transmits to the system a record of a selected clock process; and calibration assigns duration to ticks.

## 4. Observation as a Channel of Discrimination

The clock channel $K_{C \to S}$ is a history-dependent observation channel. A memoryless state-observation channel is a simpler special case. In the deterministic formulation for the metasystem,

*[see Eq. (32) in the PDF, § 4: $O_M : X_M \to Y$]*

whereas in the general case it is given by a Markov kernel

*[see Eq. (33) in the PDF, § 4: $O_M(dy \mid m)$]*

The channel determines which distinctions in $X_M$ are preserved in the observable space $Y$. For deterministic $O_M$, states satisfying

*[see Eq. (34) in the PDF, § 4: $m \sim_{O_M} m' \iff O_M(m) = O_M(m')$]*

are indistinguishable. A transition within a single equivalence class is a hidden event. Several hidden transitions, including a cycle that returns to the previous observable value, may leave no tick in the record. For a general kernel, its action on a distribution is defined as

*[see Eq. (35) in the PDF, § 4: $(O_M^* p_k)(B) = \int_{X_M} O_M(B \mid m)\,p_k^M(dm)$]*

In the deterministic case, $O_M^* p = O_{M\#}p$. Correlated noise and observational memory are represented by a separate kernel $O_{M,dy}(\cdot \mid \omega)$ on the space of histories. The observed trajectory measure is

*[see Eq. (36) in the PDF, § 4: $P^O(B) = \int O_M(B \mid \omega)\,dP^M(\omega)$]*

Even if the complete dynamics of M is Markovian, the coarse-grained dynamics in $Y$ may have memory: hidden degrees of freedom carry information between observations. The Markov property of the observed process therefore cannot be assumed automatically.

For observations of the system alone, the channel $O_S : X_S \rightsquigarrow Y$ is used below. If access to M occurs exclusively through S, then in the deterministic case $O_M = O_S \circ \pi_S$; kernels are composed accordingly. Neither $O_M$ nor $O_S$ requires a conscious observer. Either may be a measuring instrument, a receptor, a classification algorithm, or a statistical partition of the state space. Thermodynamic cost attaches not to an abstract channel as such but to its concrete physical realization (§ 11).

## 5. An Extensible Map of Characteristics

Not every system has an energy function, a thermal environment, and a notion of heat. A unified framework must therefore not be turned into a requirement to ascribe $W$, $Q$, and $\sigma$ to a text, an institution, or an arbitrary computational description.

Let $\mathcal{D}$ be a class of admissible specifications for which the available structures have been stated in advance. For each transition, define the set of admissible characteristics and the corresponding typed map:

*[see Eq. (37) in the PDF, § 5: $\mathcal{A}(\mathcal{D}) = \{F : F \text{ is defined in the class } \mathcal{D}\}$ and the typed map on $\mathcal{A}(\mathcal{D})$]*

A component enters the map only when its necessary prerequisites are specified in the model. At the level of an individual realization and at the ensemble level, respectively, this yields two mutually consistent expressions:

*[see Eq. (38) in the PDF, § 5: the pathwise record $\mathcal{C}_{S,O,path}(\mathcal{D}) = (\mathcal{E}_M;\ \theta_S^{int}, \theta_{S|C}^{ext};\ \ldots)$]*

*[see Eq. (39) in the PDF, § 5: the ensemble record $\mathcal{C}_{S,O,ens}(\mathcal{D}) = (\mathcal{E}_M;\ \langle\theta_S^{int}\rangle, \langle\theta_{S|C}^{ext}\rangle;\ \ldots)$]*

The first semicolon separates the primitive causal order of events from the local clocks; the second separates the clocks from the remaining derivative characteristics. The calibrated coordinate $t_C$ is added to the map only for a class $\mathcal{D}$ in which a reference, a unit, and an interpolation rule are specified. External clocks are not a complete measure of the activity of M: they pertain to the triple $(S, C, K_{C \to S})$.

For a stochastic system, changes in distributional entropy and informational distinguishabilities may be defined. For continuous $X$, one must fix a base measure or use relative entropy: differential entropy itself depends on the coordinates. After a calibrated clock representation has been selected, a thermodynamic specification takes the form

*[see Eq. (40) in the PDF, § 5: $\mathcal{M}_{th} = (\mathcal{M}_{ev}, t_C, E, T_b, \mathrm{Ldb})$]*

where $E(x, \lambda)$ is the energy function, $T_b$ is the temperature of the thermal environment, and $\mathrm{Ldb}$ denotes the conditions that make the dynamics consistent with the energetics, in particular local detailed balance. Energetics and dynamics play different roles and must be connected by the physical model. For such a specification, the map extends to

*[see Eq. (41) in the PDF, § 5: $\mathcal{O}_{th} = (\langle W \rangle_{th}, \langle Q \rangle_{th}, \Delta S_{sys}^{th}, \langle\sigma\rangle_{th}, D_{end}^{O,th}, A^{O,th})$]*

Here $\langle\sigma\rangle_{th}$ denotes mean trajectory-level entropy production; its definition through the forward and reverse process measures and its relation to $\Sigma$ are given in § 7. This notation asserts neither equality nor interchangeability among the components. The components are constructed from one process specification but have different mathematical types and levels of description.

### 5.1 The Separation Principle: Why the Projections of Transition Are Not Identical

A transition history provides common input to several characteristics, but is itself neither a clock reading, work, information-theoretic distinguishability, nor entropy production. Inferring an equality of time and work from the fact that both rely on changes of state commits the fallacy of the undistributed middle. Sharing a process specification does not make the resulting maps equal: clock readings, work, information-theoretic distinguishability, and entropy production have different domains, dependencies, and transformation properties. We refer to this claim as the separation principle.

Let $z_k = (x_k, \lambda_k, c_k, r_k)$ be an extended state containing the system state, protocol, selected clock, and accessible record, and let $\omega = (z_0, z_1, \ldots)$ be a history in a path space $\Omega$. The relevant valuations have schematically different arguments:

*[see the displayed schema of valuations in the PDF, § 5.1 (unnumbered): $(\omega; \pi_S, w_S) \mapsto \theta_{S,w}^{int} \in \mathbb{R}_{\geq 0}$; $(\omega; E, \lambda_\bullet) \mapsto (W, P, Q)$; $(P, Q; O) \mapsto D^{O}(P, Q) = D_{KL}(O^*P \,\|\, O^*Q) \geq 0$; $(\omega, P_F, P_R) \mapsto \sigma = D_{KL}(P_F \,\|\, P_R) \geq 0$]*

The last identification has the physical meaning of entropy production only under the conditions stated in § 7. External time has a further type: it is a functional of a record generated by a selected clock process and transmission channel, rather than a functional of the complete metasystem history.

Causal order is fixed by $\prec_M$; a clock neither creates nor replaces that order. Internal event time counts or weights selected intrinsic transitions at a stated system boundary and resolution. External time assigns readings to registered changes of a reference process. Both constructions are chronometric and depend on a clock scheme; neither is determined by energy transfer.

Work is an energetic valuation. Under convention (43), a protocol update $\lambda_k \to \lambda_{k+1}$ at fixed $x_k$ contributes

$$W_k = E(x_k, \lambda_{k+1}) - E(x_k, \lambda_k),$$

whereas a state transition at fixed protocol may contribute heat while producing no work. Thus every work-bearing act can be represented as a transition of an extended state, but not every transition is work. The bare sequence $x_0, x_1, \ldots$ is insufficient to determine $W$; the energetic structure and the work channel must also be specified.

Information-theoretic distinguishability is relational rather than a count of events. It compares two specified probability measures after a specified observation channel has acted on them. A physical record requires a distinguishable change or correlation in a receiver or memory, but that change realizes the record; it is not itself the value of the information measure. Many microscopic transitions may yield zero distinguishability at the selected observational level, while the absence of a registered event can be informative relative to a specified clock, observation window, and alternative measure.

Entropy production is distinct from both time and information-theoretic distinguishability in general. Under the hypotheses of § 7, it is the mean log-likelihood ratio between the forward path measure and the appropriately reversed path measure. Without those hypotheses, the same KL expression measures statistical irreversibility but need not represent thermodynamic entropy production.

The separations are exhibited by four counterexamples, C1–C4, collected in the table below. Information-theoretic zeros in the table refer only to the specified distinguishabilities, not to the absence of every kind of information in the system.

| Model or history | Internal time / activity | Work | Specified distinguishability | Mean entropy production |
|---|---|---|---|---|
| **C1.** Stationary equilibrium jump dynamics with nonzero mean activity, at fixed $\lambda$ and under detailed balance | The tick count is random, but its mean is positive | $W = 0$ | $D_{end} = 0$; $A^{O} = 0$ if the observed forward and reversed measures coincide | $\Sigma = 0$ |
| **C2.** Reversible quasistatic protocol between equilibria with $\Delta F \neq 0$ | Depends on duration and resolution | $\langle W \rangle \to \Delta F \neq 0$ | Endpoint distinguishability may be nonzero if the selected channel distinguishes the initial and final equilibrium distributions; directional distinguishability tends to zero | $\to 0$ |
| **C3.** Nontrivial reversible loop returning to its initial state or distribution | Positive; for example, two ticks in $x \to x' \to x$ | May be zero | $D_{end} = 0$; directional distinguishability vanishes only for reversal-invariant measures | Zero under reversible conditions |
| **C4.** The same chain $x_0, \ldots, x_n$ under two admissible protocol histories | The same under one internal-clock scheme | The histories are chosen so that $W_1 \neq W_2$ | May differ together with the measures and observed records | May differ |

Counterexample C1 rules out identities of time with work or entropy production. C2 separates reversible work from irreversibility and shows that event count does not determine work. C3 shows that accumulated time cannot be recovered from endpoint distinguishability. C4 explains why work is a functional of the extended history $(x, \lambda)$ rather than of intrinsic state changes alone.

There is also a structural distinction under time reversal. With unit weights, or with weights satisfying $w_S(\vartheta x', \vartheta x) = w_S(x, x')$, where $\vartheta$ is the state reversal of § 7, the intrinsic event measure is time-reversal even:

$$\theta_{S,w}^{int}(\bar{\omega}) = \theta_{S,w}^{int}(\omega).$$

Where the forward and reversed path measures are mutually absolutely continuous, trajectory-level entropy production is constructed from an oriented likelihood ratio and changes sign under the conjugate reversal:

$$\bar{\sigma}(\bar{\omega}) = -\sigma(\omega).$$

Here $\bar{\sigma}$ is the analogous log-likelihood functional of the conjugate reverse process. In Markov jump models, the mean rate of the unit-weight event counter is the dynamical activity. The counter should not, however, be identified without further assumptions with the entire time-symmetric part of the path action, which may also contain waiting-time, escape-rate, and other kinetic contributions. Internal event time and entropy production therefore probe different sectors of the same stochastic history: the activity counter is even under path reversal, whereas the trajectory-level log-likelihood ratio is odd under conjugate reversal. Its mean is nonnegative and should not itself be described as an odd observable. Without an additionally specified inner product, these sectors should not be called orthogonal in the literal mathematical sense.

The projections are nevertheless physically related. The first law couples work and heat; Landauer inequalities constrain the cost of specified information-processing operations; thermodynamic speed limits jointly constrain duration, activity, and entropy production; and the data-processing inequality bounds observable distinguishability. Thermodynamic uncertainty relations connect the precision of steady-state currents with dissipation, while specific models of Brownian and autonomous clocks yield model-dependent trade-offs among accuracy, resolution, and cost whose form depends on the clock architecture and drive [2, 3, 12]. These are conditional balances and bounds, not universal identities or fixed conversion rates.

Thus, a transition history provides a common process specification; a clock reading is a chronometric functional, work an energetic path functional, information-theoretic distinguishability a specified statistical relation, and entropy production a thermodynamic measure of the distinguishability between forward and physically reversed path measures under the conditions of § 7.

## 6. Work, Heat, and State Entropy

For brevity, §§ 6–10 assume a finite or countable state space $X_S$; in the continuous case, sums are replaced by integrals with respect to a specified reference measure. A calibrated clock record $t_k$ is fixed: it may be $t_C(c_k)$ under ideal access or the reconstructed coordinate $t_{S|C}$. Below, $p_t^S$, $\lambda_t$, and integrals over $t$ denote an interpolation or the continuous limit of this discrete sequence. At the level of an individual realization, work, heat, and entropy production are denoted by $W$, $Q$, and $\sigma$; angle brackets denote ensemble averages.

**Proposition I.1 (skeleton invariance).** *Assume axiom (10), the local-chain structure of the sets of system and protocol events with the substep refinement of § 2, and a calibrated clock record assigned to events independently of the linear extension. Then (i) all causally admissible linear executions of a finite configuration share the same energy skeleton, and work, heat, and the change of system entropy factor through it; and (ii) all such executions share the same calibrated skeleton.*

*Proof.* Let $L$ and $L'$ be two causally admissible linear executions of the same finite configuration $H$. Since $E_{th}(H)$ is a chain, their restrictions to thermodynamically significant events coincide:

$$L|_{E_{th}(H)} = L'|_{E_{th}(H)}.$$

Let $sk_E(L)$ denote the energy skeleton of an execution: its restriction to $E_{th}$ after removing repetitions of the pair $(x, \lambda)$ introduced by thermodynamically silent events. Then $sk_E(L) = sk_E(L')$. Permuting the remaining causally incomparable events can only insert zero energy increments and does not change $W$, $Q$, $\Delta S_{sys}$, or other functionals that factor through this skeleton.

For time-resolved path measures, a calibrated clock record $t = (t_0, t_1, \ldots)$ is additionally fixed on this local chain independently of the enumeration order of events outside $E_{th}$. The calibrated skeleton $sk_{clk}(L, t)$ consists of the sequence $(x, \lambda, t)$ and retains grid nodes with a repeated pair $(x, \lambda)$ and, in the continuous description, waiting times. Hence

$$sk_{clk}(L, t) = sk_{clk}(L', t),$$

but, unlike $sk_E$, this skeleton does not discard information about the absence of a jump between successive clock readings; this establishes the skeleton equalities. □

**Corollary I.1 (invariance of derived functionals).** *Pathwise entropy production, its mean, and observed path distinguishability — functionals of the forward and reverse path measures constructed in § 7 by pushforward through the calibrated skeleton, with observed path distinguishability defined in § 8 — do not depend on the representative of the linearization class.* The proof is immediate from Proposition I.1(ii).

**Remark.** Corollary I.1 becomes fully explicit in §§ 7–8: § 7 constructs the forward and reverse path measures by pushforward through the calibrated skeleton, while § 8 defines observed path distinguishability from their images under the observation channel. In §§ 6–10, the index $k$ refers to the corresponding energy or calibrated skeleton, refined where necessary into explicitly ordered elementary substeps. If the assignment of the clock record to events itself depends on an arbitrary linear extension, invariance of time-resolved functionals is not claimed: a separate synchronization model is required. Functionals specifically observing events outside the indicated skeletons are likewise not covered by this claim.

At slice $k$ of the selected clock, the mean energy of the system is

$$U_k = \sum_{x \in X_S} p_k^S(x)\,E(x, \lambda_k) \tag{42}$$

Under the discrete convention "protocol update first, state transition second," trajectory-level increments are defined by

*[see Eq. (43) in the PDF, § 6: the pathwise increments $W_k = E(x_k, \lambda_{k+1}) - E(x_k, \lambda_k)$, $Q_k = E(x_{k+1}, \lambda_{k+1}) - E(x_k, \lambda_{k+1})$, and their sum]*

Their ensemble averages are

*[see Eq. (44) in the PDF, § 6: $\langle W \rangle_k = \sum_x p_k^S(x)\,[E(x, \lambda_{k+1}) - E(x, \lambda_k)]$]*

*[see Eq. (45) in the PDF, § 6: $\langle Q \rangle_k = \sum_x [p_{k+1}^S(x) - p_k^S(x)]\,E(x, \lambda_{k+1})$]*

so that, under the sign convention $Q > 0$ for heat absorbed by the system,

$$U_{k+1} - U_k = \langle W \rangle_k + \langle Q \rangle_k \tag{46}$$

A different order of elementary substeps yields a different discretization but the same smooth limit. In this limit,

*[see Eq. (47) in the PDF, § 6: $dU = \langle \delta W \rangle + \langle \delta Q \rangle$, with $\langle \delta W \rangle = \sum_x p_t^S(x)\,\partial_\lambda E(x, \lambda_t)\,\dot{\lambda}_t\,dt$ and $\langle \delta Q \rangle = \sum_x E(x, \lambda_t)\,dp_t^S(x)$]*

Here all work is assumed to be performed through changes in $\lambda_t$. Nonconservative forces, chemical work, and particle exchange would require additional terms.

The integrated work of the external protocol is

*[see Eq. (48) in the PDF, § 6: $\langle W \rangle_{th} = \int_{t_0}^{t_1} \sum_x p_t^S(x)\,\partial_\lambda E(x, \lambda_t)\,\dot{\lambda}_t\,dt$]*

This separation of work and heat is standard in stochastic energetics [29]. Work characterizes energy exchange induced by a change in the external protocol; it may either be performed on the system or extracted from it.

The entropy of a distribution is defined as

$$S[p_t^S] = -k_B \sum_x p_t^S(x)\,\ln p_t^S(x) \tag{49}$$

and its change

$$\Delta S_{sys} := S[p_{t_1}^S] - S[p_{t_0}^S] \tag{50}$$

depends only on the endpoint distributions. This quantity does not measure the total irreversibility of the process.

## 7. Entropy Production and Time Reversal

For an isothermal process at temperature $T_b$, the mean dimensionless total entropy production is

*[see Eq. (51) in the PDF, § 7: $\Sigma_{th} = \Delta S_{sys}/k_B - \langle Q \rangle_{th}/(k_B T_b) \geq 0$]*

To relate this quantity to path distinguishability, the conditions must be stated explicitly. In what follows, we assume:

1. Markovian stochastic dynamics;

2. local detailed balance with respect to $E$ and $T_b$;

3. a physically correct reverse protocol;

4. reversal of all time-odd variables;

5. an initial distribution of the reverse process equal to the time-reversed final distribution of the forward process;

6. absolute continuity of the forward measure with respect to the reversed measure on the path set under consideration;

7. thermodynamic completeness of the state space $X_S$: hidden variables carry no unaccounted energy or entropy fluxes.

Let $\vartheta$ reverse the odd state variables, and let $\varsigma$ reverse the odd control parameters. An element of the space of calibrated paths has the form

*[see the displayed definition in the PDF, § 7 (unnumbered): $\omega_{clk} = (x_0, t_0, \lambda_0, e_1, x_1, t_1, \lambda_1, \ldots, e_n, x_n, t_n, \lambda_n)$]*

The reversed grid, protocol, and initial distribution of the reverse process are defined by

*[see the displayed definitions in the PDF, § 7 (unnumbered): $\bar{t}_k = t_0 + t_n - t_{n-k}$, $\bar{\lambda}_k = \varsigma\lambda_{n-k}$, $\bar{p}_0^S = \vartheta_\# p_n^S$]*

Set $\bar{z}_k = (\vartheta x_{n-k}, \bar{t}_k, \bar{\lambda}_k)$. The time-reversed trajectory then has the compact form

*[see Eq. (52) in the PDF, § 7: $\bar{\omega}_{clk} = (\bar{z}_0, \bar{e}_n, \ldots, \bar{e}_1, \bar{z}_n)$]*

Here the protocol is indexed by the slices $k = 0, \ldots, n$. We assume the involutivity $\vartheta^2 = \mathrm{id}$, $\bar{\bar{e}} = e$, and measurability of $\vartheta$, so that $\bar{\bar{\omega}} = \omega$ on admissible calibrated trajectories. For even control parameters, $\varsigma = \mathrm{id}$. Merely reversing the order relation $\mathcal{E}_M^{op}$ does not yet define a physical reverse process: admissible reverse events, the protocol, and a separate measure must be specified. For a finite discrete step, the reverse measure also changes the order of the elementary substeps: the forward order "work, then heat" corresponds to "reverse heat, then reverse work." If the same order of substeps is retained, the thermodynamic identification below is claimed only in the smooth limit.

Let $P_{th}^{M,clk}$ be the full path measure on calibrated causal histories. The path measure used below is its pushforward under the calibrated-skeleton map,

$$P_{th}^{clk} = sk_{clk\#}P_{th}^{M,clk},$$

and includes nodes without a state change on the discrete grid or waiting times in the continuous description. It need not coincide with measure (13), defined on a selected sequence of configurations, and a fortiori does not coincide with the measure of the embedded chain if the latter is constructed conditional on the occurrence of a jump. The reverse measure is constructed in the same way on the time-reversed calibrated skeleton. Denote $P_F = P_{th}^{clk}$ and $P_R = \Theta_\# P_{th}^{clk}$. When the clock record is fixed independently of linearization, $\sigma$, its mean, and the observed path distinguishability likewise do not depend on the representative of the linearization class; this proves Corollary I.1. For a realization $\omega_{clk}$, pathwise entropy production is defined by the Radon–Nikodym derivative

*[see Eq. (53) in the PDF, § 7: $\sigma(\omega_{clk}) = \ln \dfrac{dP_F}{dP_R}(\omega_{clk})$]*

The pathwise change in system entropy is

*[see Eq. (54) in the PDF, § 7: $\Delta s_{sys}(\omega_{clk}) = -k_B \ln p_n^S(x_n) + k_B \ln p_0^S(x_0)$]*

Local detailed balance and the chosen physical time reversal yield the identification

*[see Eq. (55) in the PDF, § 7: $\sigma(\omega_{clk}) = \Delta s_{sys}(\omega_{clk})/k_B - Q(\omega_{clk})/(k_B T_b)$]*

Without these physical conditions, formula (53) defines the statistical irreversibility of a trajectory, but not necessarily its thermodynamic entropy production.

Then

*[see Eq. (56) in the PDF, § 7: $\Sigma_{th} = \langle \sigma \rangle_{P_F} = D_{KL}(P_F \,\|\, P_R) \geq 0$]*

Relation (56) is a well-known result of stochastic thermodynamics [8, 28]. If S is a reduced observable description of a thermodynamically more complete system, the KL distinguishability of its paths generally provides only a lower bound on the full $\Sigma$. Under a different choice of reverse or reference measure, the KL divergence remains a measure of the distinguishability of histories but need no longer coincide with physical entropy production. The result of Kawai, Parrondo, and Van den Broeck [17] concerns a related but more specific connection between dissipation and the distinguishability of phase-space distributions of the forward and reverse processes, and is not used here as a source for the general pathwise equality.

Trajectory-level time asymmetry can also be used to estimate dissipation from stationary records [26].

## 8. Endpoint Distinguishability and Distinguishability of the Direction of Time

The distinguishability of the final and initial observed distributions is defined by

*[see Eq. (57) in the PDF, § 8: $D_{end}^{O} = D_{KL}(O^* p_n^S \,\|\, O^* p_0^S)$]*

This is a property of the endpoints, not of the entire history. For a cycle in which $p_n^S = p_0^S$, it vanishes even if work was performed and entropy was produced during the cycle.

Path distinguishability is defined on measures of histories:

*[see Eq. (58) in the PDF, § 8: $A^{O}_{th} = D_{KL}(O_\bullet^* P_F \,\|\, O_\bullet^* P_R)$]*

It answers the question of how distinguishable the observed forward history is from the observed time-reversed history. Under full observation and the conditions of § 7,

*[see Eq. (59) in the PDF, § 8: $A^{\mathrm{id}}_{th} = \Sigma_{th}$]*

For coarse-grained observation, the data-processing inequality gives

*[see Eq. (60) in the PDF, § 8: $A^{O}_{th} \leq \Sigma_{th}$]*

Coarse-graining can conceal part of the irreversibility, but it cannot increase the available KL distinguishability of the forward and reverse histories: this follows from the data-processing inequality because the same kernel $O_{S,\bullet}$ is applied to both measures. The external clock channel $K_{C \to S}$ is also a coarse-graining and can therefore conceal temporal asymmetry together with indistinguishable events. Kawai, Parrondo, and Van den Broeck (2007) obtained a related phase-space bound on dissipation, while Roldán and Parrondo (2010) showed how irreversibility can be estimated from stationary observed time series. The equality between full path distinguishability and $\Sigma$ is an equality between two KL measures under the conditions of § 7, not an identity between the concepts of "information" and "entropy."

## 9. Nonequilibrium Free Energy and Distinguishability from Equilibrium

For a system in contact with a thermal environment,

*[see Eq. (61) in the PDF, § 9: $F[p, \lambda] = U[p, \lambda] - T_b\,S[p]$]*

For an isothermal transition between equilibrium states, the Jarzynski equality and Jensen's inequality imply [16]

*[see Eq. (62) in the PDF, § 9: $\langle W \rangle_{th} \geq \Delta F$]*

The mean dissipated work is defined as

$$W_{diss} = \langle W \rangle_{th} - \Delta F \tag{63}$$

For an isothermal system in contact with a single heat reservoir, with equilibrium initial and final distributions corresponding to the initial and final values of the protocol, and in the absence of additional entropy fluxes, this quantity is related to the mean dimensionless entropy production by

$$W_{diss} = k_B T_b\,\Sigma_{th} \tag{64}$$

For a nonequilibrium distribution $p$ relative to the equilibrium distribution corresponding to the same energy function $E(\cdot, \lambda)$, the nonequilibrium free energy can be written as

*[see Eq. (65) in the PDF, § 9: $F[p, \lambda] = F_{eq}(\lambda) + k_B T_b\,D_{KL}(p \,\|\, p_{eq}^{\lambda})$]*

Thus, KL distinguishability from equilibrium contributes to the available free energy of a particular physical system [14, 24]. This does not imply that arbitrary information is equivalent to work: the equality pertains to a specified distribution, energy function, and thermal environment.

## 10. Example: Bit Erasure

Consider a symmetric two-state memory. Before erasure,

$$p_0 = (1/2,\, 1/2), \tag{66}$$

and after ideal erasure,

$$p_1 = (1,\, 0) \tag{67}$$

The exact state (67) is an idealization; physically, it is attained as the limit of a protocol with a vanishingly small error probability. The entropy of the memory changes by

$$\Delta S_{mem} = -k_B \ln 2 \tag{68}$$

In the reversible isothermal limit, the environment receives heat $k_B T_b \ln 2$, while the memory receives

$$Q = -k_B T_b \ln 2 \tag{69}$$

Therefore, the total entropy production is

$$\Sigma = \frac{-k_B \ln 2}{k_B} - \frac{-k_B T_b \ln 2}{k_B T_b} = 0 \tag{70}$$

In the symmetric protocol considered here, reducing the memory entropy requires a minimum work input of $k_B T_b \ln 2$, but in the reversible limit this reduction is fully compensated by the increase in the entropy of the environment. An irreversible implementation incurs additional dissipation and $\Sigma > 0$.

The example distinguishes three quantities:

1. the change in memory entropy;

2. the minimum work of erasure;

3. the entropy production of a particular protocol.

This example illustrates the standard symmetric form of Landauer's principle in the absence of accessible side information [21, 5], rather than asserting that erasing one bit always produces exactly $k_B \ln 2$ of total entropy.

## 11. Physical Implementation of Observation and External Clocks

The abstract channels $O_S$ and $K_{C \to S}$ do not themselves perform work. A cost arises when a channel is implemented by a physical register A with its own states, memory, and dynamics. One then considers the joint space

$$X_S \times X_A \tag{71}$$

and the joint evolution $p_t(x, a)$. Measurement is a correlation-generating transition

$$(x, a_0) \longrightarrow (x, a), \tag{72}$$

that implements the channel

*[see Eq. (73) in the PDF, § 11: $O_A(a \mid x) = \Pr[A_{k+1} = a \mid X_k = x, A_k = a_0]$]*

In the case of external clocks, the role of $x$ is played by the state or label of the clock process C, while the transition $a_{j-1} \to a_j$ constitutes a successful registration of the form (24). Without a physical change in the register, a signal may exist in the metasystem, but its tick does not enter the record accessible to the system. A channel without persistent memory may create a transient correlation, but it does not allow S to compare successive readings.

Once A is included within the physical boundary of the extended system, its own work, heat, entropy change, and entropy production can be defined. The cost of creating a correlation, the cost of signal transmission, the cost of reliably storing the result, and the cost of resetting the memory for reuse must be distinguished. Landauer's principle directly constrains logically irreversible memory erasure, rather than every act of discrimination or every clock tick as such.

Thus, thermodynamic cost pertains not to a channel as a mathematical mapping but to the chosen mechanism of its implementation. In the map (41), the observer and the clocks may remain outside the boundary of the thermodynamic system; an extended map for S+A+C must account for the balances of all included subsystems.

## 12. Object Types and Object Tokens

Let the recognition scheme be

*[see Eq. (74) in the PDF, § 12: $R^* = (O_S, \Phi, d, B, \varepsilon;\ q_{type}, q_{token}, h, \ell_{min}^{type}, \ell_{min}^{token})$]*

The components of the scheme are distributed between its two branches as follows:

| Component | Role | Branch |
|---|---|---|
| $O_S$ | system observation channel | both |
| $\Phi$ | maps an observed distribution or empirical measure to features | both |
| $d$ | metric on the feature space $Z$ | both |
| $B = \{B_a\}_{a \in A}$ | catalog of type regions | both |
| $\varepsilon$ | admissible deviation from a type region | both |
| $q_{type}$ | common ensemble clock | type |
| $q_{token}$ | rule for selecting the clock $q_{token}$ of an individual history | token |
| $h$ | size of the local averaging window | token |
| $\ell_{min}^{type}$ | minimum duration of a type manifestation | type |
| $\ell_{min}^{token}$ | minimum token duration | token |

Here $Z$ is the feature space and $A$ is the set of type indices; they are auxiliary structures rather than separate components of the tuple $R^*$. The clock $q_{type}$ must be common to the ensemble and independent of any particular realization; it may be the slice index $k$, the calibrated clock $t_C$, or the mean $\langle\theta_S^{int}\rangle$. The clock $q_{token}$ pertains to a specific history and may equal $\theta_S^{int}$, $\theta_{S|C}^{ext}$, $t_C$, or another monotone functional. If the catalog $B$ is not specified, the construction identifies stable regimes, but assigning them to the same type requires a separate classification stage.

For an index segment $I = [i, j]$, its duration with respect to the selected clock is

$$\ell_q(I) = q_j - q_i \tag{75}$$

Equation (75) is applied with $q = q_{type}$ in the ensemble branch and with $q = q_{token}$ in the realization branch. Duration is therefore not a hidden absolute parameter of the scheme: the choice of clock is part of the conditions for recognizing an object.

### 12.1 Object Type

The ensemble feature representation is

$$z_k^{type} = \Phi(O_S^* p_k^S) \tag{76}$$

For a type $a$, define the set of clock-indexed slices on which the ensemble representation is recognized as belonging to that type:

$$G_a^{type} = \{k : d(z_k^{type},\, B_a) \leq \varepsilon\} \tag{77}$$

An object type is specified by the region $B_a$ together with the recognition scheme $R^*$. Its ensemble manifestations are the maximal consecutive segments $I \subseteq G_a^{type}$ for which $\ell_{q_{type}}(I) \geq \ell_{min}^{type}$. Thus, the stability of a distribution defines a reproducible macroregime rather than an individual thing.

### 12.2 Object Token

For an individual realization $\omega = (x_0, e_1, x_1, \ldots)$ and an observed history $y_k \sim O_S(\cdot \mid x_k)$, set $q_k = q_{token}(\omega_k)$ and introduce the causal window

*[see Eq. (78) in the PDF, § 12.2: $J_{k,h}(q) = \{j \leq k : 0 \leq q_k - q_j \leq h\}$]*

If the window is nonempty, the local empirical measure of observations is

*[see Eq. (79) in the PDF, § 12.2: $\hat{\mu}_{k,h}(q) = |J_{k,h}(q)|^{-1} \sum_{j \in J_{k,h}(q)} \delta_{y_j}$]*

The parameter $h$ sets the scale of the selected clock over which rapid fluctuations are suppressed. Under irregular sampling, the equal weights in (79) may be replaced by a prespecified sampling measure. The corresponding feature representation is

$$z_{k,h}^{token}(q) = \Phi(\hat{\mu}_{k,h}(q)) \tag{80}$$

For a type $a$, set

$$G_a^{token}(h; q) = \{k : d(z_{k,h}^{token}(q),\, B_a) \leq \varepsilon\} \tag{81}$$

An object token of type $a$ is a maximal consecutive segment $I$ of this set for which $\ell_q(I) \geq \ell_{min}^{token}$. If the regions $B_a$ are not specified, it is appropriate to speak only of a stable realization-level regime, not of a token of a particular type.

Thus, an object type and an object token are distinct forms of process stability. Ensemble stability does not guarantee the stability of every realization, while a stable token does not require the entire ensemble to be stationary. Under a deterministic description or a degenerate distribution, these definitions may coincide, but in general they differ.

The stability of an object does not imply that its internal time has stopped. As long as $z_{k,h}^{token}(q)$ remains within the type region $B_a$, the realization may undergo many of its own transitions and accumulate a substantial $\theta_S^{int}$. A thing persists not because nothing within it changes, but because its changes do not destroy its recognizable organization. The converse is also possible: a token may continue to exist with respect to external time even though its internal event counter temporarily ceases to increase.

The same object segment therefore has at least two substantively different durations:

$$\ell_{int}(I) = \theta_S^{int}(j) - \theta_S^{int}(i), \qquad \ell_{ext}(I) = \theta_{S|C}^{ext}(j) - \theta_{S|C}^{ext}(i) \tag{82}$$

The first shows how many of its own changes the token has accumulated; the second shows how many accessible external ticks have elapsed in the metasystem. Their mismatch is part of the description of the object, not a defect of the clocks.

### 12.3 Gaps, Division, and Robustness of the Criterion

The strict condition (81) terminates a token when it leaves the type region. If identity is to be preserved across a brief gap or an absence of observations, an additional continuation predicate $CR(I_i, I_j)$ is required to link two stable segments. Such a predicate does not follow from the metric $d$ alone: it expresses a separate rule of identity and may account for the admissible duration of the gap according to the selected clock, causal reachability, or conserved quantities.

Division and merger likewise cannot be described by a single interval. They form a directed graph of token provenance: a vertex with several outgoing edges represents division, whereas a vertex with several incoming edges represents merger. A linear worldline is a special case of this structure.

Objecthood should not depend on a single precisely chosen threshold. Let $\mathcal{I}(\varepsilon) = \{I_1, \ldots, I_N\}$ be the segmentation of a history at threshold $\varepsilon$. Number its segments in the order of the original history,

*[see the displayed ordering condition in the PDF, § 12.3 (unnumbered): $\max I_i < \min I_{i+1}$, $i = 1, \ldots, N-1$]*

Only segments of the same chronological rank may be matched; a later segment in one segmentation cannot be matched with an earlier segment in another. Define the distance

*[see Eq. (83) in the PDF, § 12.3: $d_{seg}(\mathcal{I}, \mathcal{I}') = \max_{1 \leq i \leq N} d_H^{q^*}(I_i, I_i')$ when $N = N'$, and $+\infty$ when $N \neq N'$]*

Recognition is robust over a range of thresholds $E$ if

*[see Eq. (84) in the PDF, § 12.3: $\sup_{\varepsilon, \varepsilon' \in E} d_{seg}(\mathcal{I}(\varepsilon), \mathcal{I}(\varepsilon'))$ is small]*

Here $q^*$ denotes $q_{type}$ or $q$ in the corresponding branch, and

$$d_H^{q}(I, J) = d_H(\{q_{\min I}, q_{\max I}\},\, \{q_{\min J}, q_{\max J}\})$$

is the Hausdorff distance between the segment boundaries mapped to the clock coordinate. If $q$ is not injective on the set of all admissible boundaries, $d_H^{q}$ is a pseudometric. Because it takes the value $+\infty$ when the numbers of segments differ, $d_{seg}$ is, in general, an extended pseudometric. Quotienting by the zero-distance relation and requiring $q$ to be injective on all admissible boundaries yields an extended metric; it is finite on each sector with a fixed number of segments. The condition controls not only the proximity of the boundaries but also the number of identified tokens, thereby distinguishing robust objects from artifacts of fine-tuning the threshold.

The dependence of an object on $R^*$ does not entail arbitrariness. A recognition scheme is constrained by measurement reproducibility, robustness under small perturbations, and the ability of the identified patterns to support testable predictions. In this sense, the definition is close to Dennett's notion of "real patterns," but it is furnished with an explicit trajectory-level criterion [9].

## 13. Positioning the Proposed Framework

The process philosophies of Whitehead and Rescher assert the priority of becoming and process over substance [31, 25]. The present work adopts this general shift but articulates it through a stochastic specification of transitions, trajectory functionals, and an operational recognition scheme.

In distributed-systems theory, the happened-before relation distinguishes the causal partial order of events from logical-clock readings [20]. Event structures formalize causality, conflict, and concurrency without requiring a global time [32]. The proposed construction uses this distinction as an ontological layer, while adding internal measures of change, a physical external-clock channel, and thermodynamic functionals of calibrated trajectories.

At a more applied computational level, [Active Transaction Graphs](../../2026-active-transaction-graphs/) [33] provide an executable semantics for mediated transition histories, distinguishing state results, execution traces, and ledger effects. The present framework operates at a more primitive physical level: it begins with a causal partial order and introduces thermodynamic functionals only when an energy model, a calibrated clock, and the corresponding physical prerequisites have been specified.

The causal-set program treats a locally finite causal order as a candidate for the fundamental structure of spacetime [6]. No such physical hypothesis is adopted here: $\mathcal{E}_M$ is a labeled causal order of the events in the model, while discreteness pertains to operationally distinguishable and recorded events. Any connection to quantum gravity would require a separate formalism.

Relational approaches to time in physics hold that temporal structure is defined by correlations with a selected physical clock rather than by an external parameter: the Page–Wootters mechanism recovers dynamics from correlations between a subsystem and a clock subsystem within a stationary whole [23], relational quantum mechanics relativizes states to the observing system [27], and Machian analyses eliminate absolute time altogether [4]. The central relation (85) is a classical, operational counterpart of this family: external time is likewise borrowed from a designated clock process, but the mechanism here is an explicitly modeled, generally lossy delivery channel and register, and the construction neither requires nor implies a timeless global state or any quantum formalism.

Constructor theory describes physics in terms of possible and impossible transformations [10, 11]. The affinity here lies in the priority given to transformation; the difference lies in the focus on a particular realized trajectory, its cost, irreversibility, and observable distinguishability.

Categorical theories of processes provide an abstract language for composing processes and morphisms [1, 7]. The proposed framework is less general algebraically, but it connects the process description directly to probabilistic and thermodynamic quantities.

Ontic structural realism shifts the emphasis from individual objects to relations and structure [19]. Here the object receives a more specific definition: it is a stable feature regime of a trajectory relative to $R^*$.

Work on semantic information investigates the relation between information, a system's continued existence, and its goals [18]. In the present article, information is used in the narrower statistical sense of distinguishability between distributions and trajectory measures. Semantic value, agency, and purposiveness do not follow from this definition.

A complementary, goal-relative notion of noise is developed in [34], where a capacity-efficient good regulator is shown to factor through a projection that suppresses distinctions irrelevant to admissible action. This notion should be distinguished from the channel-relative concept used in the present article: here, indistinguishability is defined statistically with respect to an observation kernel and a specified pair of probability measures, without presupposing a goal or an action set.

Stochastic thermodynamics under coarse graining shows that hidden microstates can alter observed balances and induce effective memory [13]. The present work does not identify this result with a theory of clocks, but it does support the requirement that the channel and the boundary of the observed system be specified explicitly.

A domain-specific control-theoretic realization of this boundary dependence is developed in [35] ([The Computable Boundary of the Firm](../../2026-computable-boundary-of-the-firm/)), where the boundary of an organizational digital twin is represented through actor membership, interface permeability, and operational dynamics. Although that application concerns firms rather than physical clock records, it illustrates the general point that boundary selection changes the modeled state variables, available observations, admissible controls, and conditions of viability.

## 14. Scope and Limitations

First, the relation $\prec_M$ is taken as a primitive of the framework rather than derived from thermodynamics or changes of state. This removes circularity from the definition of time, but makes causal precedence an explicit postulate of the model.

Second, local finiteness and discrete clock events establish the discreteness of operationally accessible readings. They do not imply that physical spacetime is fundamentally discrete. A continuous coordinate $t$ requires an additional measure, calibration, and interpolation, as well as an explicit notion of convergence if a continuum limit is claimed.

Third, a partial order does not determine a unique global clock. Selecting the chain C excludes concurrent events, while any scalar linear extension discards part of the structure of causal independence. Event conflict is not modeled separately in the present causal order. External time is therefore always relative to a chosen reference process, boundary, and channel.

Fourth, $K_{C \to S}$ may omit, merge, delay, reorder, and distort ticks. Under noise, a reading should be represented by a conditional distribution or an uncertainty interval. Back-action of S on C, asymmetric delays, and synchronization among different systems require a separate model.

Fifth, the internal event measure is defined directly for locally finite discrete histories. It depends on the system boundary and the criterion for distinguishing states, is not work, information-theoretic distinguishability, state entropy, or entropy production, and does not preserve intervals between events. Diffusive and smooth trajectories require a metric, path variation, or another clock functional.

Sixth, the general map does not make thermodynamic components mandatory. Work, heat, and physical entropy production are defined only when an energy function, a thermal environment, and conditions linking the dynamics to the energetics are available. They cannot automatically be transferred to a text, an institution, or a computational model.

Seventh, the independence of thermodynamic functionals from a linear execution rests on Proposition I.1 and Corollary I.1: the protocol–system comparability axiom (10), the passage to the energy skeleton, and the specification of the calibrated clock record independently of linearization. If causally incomparable events can simultaneously modify $x$ or $\lambda$, or if the temporal assignment itself depends on an arbitrary linear extension, the causal model must be enlarged or the relevant layer must be defined relative to an explicitly chosen execution.

Eighth, the equality between entropy production and the KL divergence of forward and reverse trajectories is used only under the conditions of § 7. The conditional equality $A^{\mathrm{id}} = \Sigma$ is not an identity of information and entropy: coarse-graining the channel or changing the pair of compared measures generally destroys it. Partial observation may render the dynamics non-Markovian; in that case, the state space must be enlarged with hidden variables, or the trajectory measures and reverse process must be specified separately.

Ninth, common dependence on a transition history does not license the identification of clock readings, work, information-theoretic distinguishability, and entropy production. Relations among them are calibrations, inequalities, or model-dependent trade-offs requiring additional physical parameters; there is no universal conversion rate.

Tenth, the scheme $R^*$ does not provide a unique "true" partition of the world into things. It makes the channel, clock, scale, and recognition criterion explicit and testable. Different schemes may identify different but simultaneously stable objects.

Finally, a channel is not a subject of experience, and the article does not prove the metaphysical primacy of transition as a theorem of physics. Describing an agent would require memory, an action-selection rule, feedback, and a criterion for selecting protocols; consciousness lies beyond the scope of this work.

## 15. Conclusion

A transition is not reducible to the replacement of one state by another and does not presuppose an underlying continuous interval. The framework is grounded in a locally finite causal partial order of events. Along a local history, a system's internal time accumulates as its own states change. External time is likewise event-based: the selected reference process C changes within the metasystem M, while the system S receives only a physically transmitted and partially observed record of those changes.

The central relation is

*[see Eq. (85) in the PDF, § 15: $P^{S|C} = K_{C \to S}^* P^{clock}$, $\theta_{S|C}^{ext} = F_{tick}(\rho)$, with $C \subseteq M$, $C \cap S = \emptyset$]*

In other words, the external-clock reading available to the system is a functional of the transmitted record of a selected clock process, not a reading of an absolute metasystem time. The incompleteness of the channel makes this coordinate local and relative; registering a tick requires an internal change in the memory of S. A real-valued calibration turns the count into a duration, while a continuous coordinate $t$ is introduced as an effective interpolation or obtained in a separately specified scaling limit.

The common transition substrate does not make its valuations identical. Internal event time is a clock functional determined by a boundary, resolution, and weighting rule. Work is an energetic functional determined by an energy model, protocol, and work channel. Information-theoretic distinguishability is a relation between specified measures relative to an observation channel. Entropy production is a thermodynamic interpretation of forward–reverse path asymmetry under the conditions of § 7. A stationary equilibrium system with nonzero dynamical activity at fixed protocol and under detailed balance may accumulate internal ticks while work, directional distinguishability, and entropy production all vanish. Conversely, a reversible quasistatic protocol may perform nonzero work while entropy production tends to zero. These separations — the separation principle of § 5.1 — rule out any universal identity among time, work, information-theoretic distinguishability, and entropy production.

Their relations instead take the form of conditional balances and bounds. Landauer's principle concerns the cost of specified logically irreversible operations, not every act of observation or every tick. Thermodynamic speed limits relate achievable change, calibrated duration, dynamical activity, and dissipation without identifying them. Coarse-graining bounds observable path distinguishability by full path distinguishability. The physical model—not the concept of transition alone—determines which such relations exist and what scales enter them.

The principal ontological proposal of the article concerns the thing. At the ensemble level, an object type is defined by the stability of a macroregime; at the level of an individual history, an object token is defined by the stability of a realization relative to an explicitly selected clock and scale. In both cases, objecthood consists not in the absence of change but in preserving the recognizable organization of a process. The same token thereby carries two irreducible durations — the internal count of its own changes and the accessible external count (82); their mismatch is part of the description of the object, not a defect of the clocks:

> Transition is taken as primitive; a thing is defined as its stable organization.

The resulting picture is plural without being fragmented: causal order provides the primitive structure, whereas clocks, duration, work, information-theoretic distinguishability, and entropy production are distinct typed characteristics defined relative to a common process specification. Their irreducibility makes physical comparison meaningful, while the common specification makes their joint description coherent.

## Appendix A. Delivery, Registration, and Decoding of External Ticks

### A.1 Attempt Record and Memory Update

A complete protocol-level implementation of the clock channel refines the output record $\rho = (\rho_1, \rho_2, \ldots)$, the observed signals $y_j$, and the register states $r_j$:

*[see Eq. (A1) in the PDF, Appendix A: the channel $K_{C \to S}(\cdot \mid \gamma_C)$ with provenance sets $A_j$, the memory update $r_j = U_{mem}(r_{j-1}, y_j)$, and the decoded weight $w_j = D_w(r_{j-1}, y_j, r_j)$]*

Here $A_j$ is the set of source ticks represented by the $j$th attempt. For a genuine nonaggregated signal, $A_j = \{\iota(j)\}$, where $\iota(j)$ is the index of the tick that generated it; for an aggregated message, $|A_j| > 1$; for a false signal, $A_j = \emptyset$ and $\iota(j)$ is undefined. The decoder is chosen such that $w_j \geq 0$, and, upon successful registration $r_j \neq r_{j-1}$, a tick included in the count has $w_j > 0$. For an unsuccessful or rejected attempt, one sets $w_j = 0$.

An omission corresponds to a tick that belongs to no $A_j$; duplication is the occurrence of one index in several sets; aggregation is an $A_j$ containing more than one element. These cases are properties of a particular channel, not of the underlying causal order.

### A.2 Incomplete Knowledge and Message Order

For a noisy or incomplete channel, the system's state of knowledge may be a distribution over the hidden source reading. Set $J_n = \max\bigcup_{j \leq n} A_j$, with $\max \emptyset = 0$, and let $c_0$ denote the initial clock state before the first represented tick, with $\theta_C^{int}(c_0) = 0$. The complete register history available by step $n$ generates the $\sigma$-algebra $\mathcal{F}_n^R = \sigma(r_0, y_1, r_1, \ldots, y_n, r_n)$. Then

*[see Eq. (A2) in the PDF, Appendix A: the filtering distribution $\mu_{S|C,n}(B) = \Pr[\theta_C^{int}(c_{J_n}) \in B \mid \mathcal{F}_n^R]$]*

The raw record preserves source order if $j < j'$ implies $k < k'$ for every $k \in A_j$ and $k' \in A_{j'}$. If this condition is violated, the sequence must be reconstructed by a separate protocol, for example using stored tick numbers or causal labels. If $r_n$ is a sufficient state of the channel's entire memory, conditioning on $\mathcal{F}_n^R$ in (A2) may be replaced by conditioning on $r_n$. The filtering distribution does not assume that the external states of the metasystem are fully observable to S.

### A.3 Decoding Physical Duration

The calibration of the output register is specified by a separate duration decoder. Let $\hat{\tau}_j^{err} \geq 0$ denote its output in a registered case that is not an exact decoding of a genuine single or aggregated signal.

*[see Eq. (A3) in the PDF, Appendix A: $\hat{\tau}_j := D_\tau(r_{j-1}, y_j, r_j) \geq 0$, given by the four-case definition — $\tau_{\iota(j)}$ when $r_j \neq r_{j-1}$ and $A_j = \{\iota(j)\}$ (signal accepted and decoded exactly); $\sum_{k \in A_j}\tau_k$ when $r_j \neq r_{j-1}$ and $|A_j| > 1$ (aggregate accepted and decoded exactly); $\hat{\tau}_j^{err}$ when $r_j \neq r_{j-1}$, all other cases; and $0$ otherwise]*

In an ideal channel, $A_j = \{j\}$ and $\hat{\tau}_j = \tau_j > 0$. For a registered false or distorted signal, the value $\hat{\tau}_j^{err}$ is specified by the error model; such a contribution is a reading error rather than the duration of a genuine source tick. Thus, the positivity of the original increments $\tau_k$ is compatible with zero decoded increments for unsuccessful attempts.

## Appendix B. Worked Example: A Two-State System with a Lossy External Clock

### B.1 Setup

Let the system have two states, $a$ and $b$, observed through the identity channel, with unit weights in (17). The clock process emits five ticks with unit source calibration in (26), so its source coordinate advances by one unit per tick. The delivery channel of (A1) delivers the first and third ticks exactly, loses the second tick (it belongs to no provenance set), and aggregates the fourth and fifth ticks into a single message that is decoded exactly: the weight decoder of (A1) returns a decoded weight of 2 (one unit per represented tick) for use in (20), and the duration decoder of (A3) returns a decoded increment of 2 for use in (27). All three delivery attempts result in successful registrations, so the register changes three times. The system performs five intrinsic transitions ($a \to b \to a \to b \to a \to b$) and then remains in $b$. The interleaving of intrinsic transitions, source ticks, and registrations along the selected execution is shown in Table B1; every entry follows by direct application of the indicated equations. Explicitly, $t^* = 0$, $\tau_k = 1$ and $w_C = 1$ for every source tick, and the provenance sets are $A_1 = \{1\}$, $A_2 = \{3\}$, $A_3 = \{4, 5\}$.

**Table B1.** Event log of the worked example. Columns give, after each step: the system state; the internal event time (17); the number of successful registrations and the source tick count entering the undercount bound (23); the external time (20); the source coordinate (26); and the decoded coordinate (27). Each row is an observation cut along the selected execution and may group elementary events.

| Step | Event | $x$ | $\theta_S^{int}$ (17) | $N_{S\|C}^{ext}$ / $\theta_C^{int}$ (23) | $\theta_{S\|C}^{ext}$ (20) | $t_C$ (26) | $t_{S\|C}$ (27) |
|---|---|---|---|---|---|---|---|
| 0 | initial state | $a$ | 0 | 0 / 0 | 0 | 0 | 0 |
| 1 | tick 1 delivered; registration 1 | $a$ | 0 | 1 / 1 | 1 | 1 | 1 |
| 2 | intrinsic transition $a \to b$ | $b$ | 1 | 1 / 1 | 1 | 1 | 1 |
| 3 | intrinsic transition $b \to a$ | $a$ | 2 | 1 / 1 | 1 | 1 | 1 |
| 4 | tick 2 emitted and lost | $a$ | 2 | 1 / 2 | 1 | 2 | 1 |
| 5 | intrinsic transition $a \to b$ | $b$ | 3 | 1 / 2 | 1 | 2 | 1 |
| 6 | intrinsic transition $b \to a$ | $a$ | 4 | 1 / 2 | 1 | 2 | 1 |
| 7 | intrinsic transition $a \to b$ | $b$ | 5 | 1 / 2 | 1 | 2 | 1 |
| 8 | tick 3 delivered; registration 2 | $b$ | 5 | 2 / 3 | 2 | 3 | 2 |
| 9 | ticks 4 and 5 emitted; aggregated in channel | $b$ | 5 | 2 / 5 | 2 | 5 | 2 |
| 10 | aggregate delivered; registration 3 ($w_3 = 2$, $\hat{\tau}_3 = 2$) | $b$ | 5 | 3 / 5 | 4 | 5 | 4 |

### B.2 Clocks and the Channel

The log exhibits the clock-theoretic claims of § 3 on concrete numbers. The undercount bound (23) holds with room to spare: three registrations against five source ticks. The decoded coordinate (27) terminates at 4 while the source coordinate (26) terminates at 5; the missing unit is exactly the lost second tick, which cannot be recovered from the delivered record and the stipulated decoder alone — the record is partial in precisely the sense of § 3.2. The aggregated message illustrates the difference between counting registrations and accumulating decoded weight: the third registration is a single register change but carries decoded weight 2 for (20) and decoded duration 2 for (27), so both the external time and the decoded coordinate jump from 2 to 4 in one step. An exact instance of (25) occurs on steps 8–10, where the internal increment is 0 while the external increment is 2. Its converse occurs on steps 1–7, where the corresponding increments are 5 and 0.

### B.3 Token Segmentation and Robustness

Take as observations the eleven row states of Table B1, including the initial row, indexed by the row number $k = 0, \ldots, 10$, with observed sequence $a, a, b, a, a, b, a, b, b, b, b$, and let the token clock in (74) be the step index with averaging window $h = 2$, so that the causal window (78) contains at most the last three observations. Take the feature map $\Phi$ of (80) to be the empirical frequency of the state $b$ in the window, and let $d$ be the Euclidean metric on the feature line, with the induced point-to-set distance $d(z, B) = \inf_{b \in B} |z - b|$ used for the recognition regions: the alternating regime $[1/3, 2/3]$ and the frozen regime $[0.9, 1]$. The resulting feature values are $0, 0, 1/3, 1/3, 1/3, 1/3, 1/3, 2/3, 2/3, 1, 1$.

At tolerance $\varepsilon = 1/12$, with a common minimal token duration of one step for both regimes, the recognized sets (81) are $\{2, \ldots, 8\}$ for the alternating regime and $\{9, 10\}$ for the frozen regime, yielding two object tokens: an alternating token on the segment $[2, 8]$ and a frozen token on $[9, 10]$. The segmentation is robust in the sense of (84): the smallest feature-to-region distance that could change any membership is $0.9 - 2/3 \approx 0.233$, so over the entire threshold range $E = [0, 0.2]$ the segmentation is unchanged and the segmentation distance (83) is zero — the two tokens are not artifacts of a fine-tuned threshold.

The dual durations (82) complete the picture and are read directly from the two $\theta$ columns of Table B1. The alternating token accumulates four intrinsic transitions while the accessible external time advances by one unit: its internal duration is $5 - 1 = 4$ against an external duration of $2 - 1 = 1$. The frozen token accumulates no intrinsic transitions while the external register advances by two units: internal duration 0 against external duration $4 - 2 = 2$. At the level of recognized objects, the frozen token realizes (25) exactly, whereas the alternating token exhibits the opposite clock imbalance, $\ell_{int} > \ell_{ext}$, without zero external duration: a thing that persists by the world's clock while its own clock stands still, and a thing that lives fast by its own clock while the delivered clock barely moves. The mismatch is part of the description of each token, not a defect of either clock.

## References

[1] Abramsky, S., & Coecke, B. (2004). A categorical semantics of quantum protocols. In *Proceedings of the 19th Annual IEEE Symposium on Logic in Computer Science* (pp. 415–425). IEEE Computer Society. https://doi.org/10.1109/LICS.2004.1319636

[2] Barato, A. C., & Seifert, U. (2015). Thermodynamic uncertainty relation for biomolecular processes. *Physical Review Letters*, 114(15), 158101. https://doi.org/10.1103/PhysRevLett.114.158101

[3] Barato, A. C., & Seifert, U. (2016). Cost and precision of Brownian clocks. *Physical Review X*, 6(4), 041053. https://doi.org/10.1103/PhysRevX.6.041053

[4] Barbour, J. (1999). *The End of Time: The Next Revolution in Physics*. Oxford University Press.

[5] Bérut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider, R., & Lutz, E. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*, 483, 187–189. https://doi.org/10.1038/nature10872

[6] Bombelli, L., Lee, J., Meyer, D., & Sorkin, R. D. (1987). Space-time as a causal set. *Physical Review Letters*, 59(5), 521–524. https://doi.org/10.1103/PhysRevLett.59.521

[7] Coecke, B., & Kissinger, A. (2017). *Picturing Quantum Processes: A First Course in Quantum Theory and Diagrammatic Reasoning*. Cambridge University Press. https://doi.org/10.1017/9781316219317

[8] Crooks, G. E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. *Physical Review E*, 60(3), 2721–2726. https://doi.org/10.1103/PhysRevE.60.2721

[9] Dennett, D. C. (1991). Real patterns. *The Journal of Philosophy*, 88(1), 27–51. https://doi.org/10.2307/2027085

[10] Deutsch, D. (2013). Constructor theory. *Synthese*, 190, 4331–4359. https://doi.org/10.1007/s11229-013-0279-z

[11] Deutsch, D., & Marletto, C. (2015). Constructor theory of information. *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 471(2174), 20140540. https://doi.org/10.1098/rspa.2014.0540

[12] Erker, P., Mitchison, M. T., Silva, R., Woods, M. P., Brunner, N., & Huber, M. (2017). Autonomous quantum clocks: Does thermodynamics limit our ability to measure time? *Physical Review X*, 7(3), 031022. https://doi.org/10.1103/PhysRevX.7.031022

[13] Esposito, M. (2012). Stochastic thermodynamics under coarse graining. *Physical Review E*, 85(4), 041125. https://doi.org/10.1103/PhysRevE.85.041125. Erratum: *Physical Review E*, 86, 049904. https://doi.org/10.1103/PhysRevE.86.049904

[14] Esposito, M., & Van den Broeck, C. (2011). Second law and Landauer principle far from equilibrium. *EPL*, 95(4), 40004. https://doi.org/10.1209/0295-5075/95/40004

[15] Gorenflo, R., Mainardi, F., & Vivoli, A. (2007). Continuous-time random walk and parametric subordination in fractional diffusion. *Chaos, Solitons & Fractals*, 34(1), 87–103. https://doi.org/10.1016/j.chaos.2007.01.052

[16] Jarzynski, C. (1997). Nonequilibrium equality for free energy differences. *Physical Review Letters*, 78(14), 2690–2693. https://doi.org/10.1103/PhysRevLett.78.2690

[17] Kawai, R., Parrondo, J. M. R., & Van den Broeck, C. (2007). Dissipation: The phase-space perspective. *Physical Review Letters*, 98(8), 080602. https://doi.org/10.1103/PhysRevLett.98.080602

[18] Kolchinsky, A., & Wolpert, D. H. (2018). Semantic information, autonomous agency and non-equilibrium statistical physics. *Interface Focus*, 8(6), 20180041. https://doi.org/10.1098/rsfs.2018.0041

[19] Ladyman, J., & Ross, D., with Spurrett, D., & Collier, J. (2007). *Every Thing Must Go: Metaphysics Naturalized*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199276196.001.0001

[20] Lamport, L. (1978). Time, clocks, and the ordering of events in a distributed system. *Communications of the ACM*, 21(7), 558–565. https://doi.org/10.1145/359545.359563

[21] Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183–191. https://doi.org/10.1147/rd.53.0183

[22] Lecomte, V., Appert-Rolland, C., & van Wijland, F. (2007). Thermodynamic formalism for systems with Markov dynamics. *Journal of Statistical Physics*, 127, 51–106. https://doi.org/10.1007/s10955-006-9254-0

[23] Page, D. N., & Wootters, W. K. (1983). Evolution without evolution: Dynamics described by stationary observables. *Physical Review D*, 27(12), 2885–2892. https://doi.org/10.1103/PhysRevD.27.2885

[24] Parrondo, J. M. R., Horowitz, J. M., & Sagawa, T. (2015). Thermodynamics of information. *Nature Physics*, 11, 131–139. https://doi.org/10.1038/nphys3230

[25] Rescher, N. (1996). *Process Metaphysics: An Introduction to Process Philosophy*. State University of New York Press. https://doi.org/10.1515/9781438417110

[26] Roldán, É., & Parrondo, J. M. R. (2010). Estimating dissipation from single stationary trajectories. *Physical Review Letters*, 105(15), 150607. https://doi.org/10.1103/PhysRevLett.105.150607

[27] Rovelli, C. (1996). Relational quantum mechanics. *International Journal of Theoretical Physics*, 35(8), 1637–1678. https://doi.org/10.1007/BF02302261

[28] Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. *Reports on Progress in Physics*, 75(12), 126001. https://doi.org/10.1088/0034-4885/75/12/126001

[29] Sekimoto, K. (2010). *Stochastic Energetics*. Lecture Notes in Physics, Vol. 799. Springer. https://doi.org/10.1007/978-3-642-05411-2

[30] Shiraishi, N., Funo, K., & Saito, K. (2018). Speed limit for classical stochastic processes. *Physical Review Letters*, 121(7), 070601. https://doi.org/10.1103/PhysRevLett.121.070601

[31] Whitehead, A. N. (1978). *Process and Reality: An Essay in Cosmology* (D. R. Griffin & D. W. Sherburne, Eds., corrected ed.). Free Press. (Original work published 1929.)

[32] Winskel, G. (1987). Event structures. In W. Brauer, W. Reisig, & G. Rozenberg (Eds.), *Petri Nets: Applications and Relationships to Other Models of Concurrency* (pp. 325–392). Lecture Notes in Computer Science, Vol. 255. Springer. https://doi.org/10.1007/3-540-17906-2_31

[33] Vityaz, A. (2026). *Active Transaction Graphs: A Formal Framework for Transactional Interactive Systems*. Zenodo. doi:[10.5281/zenodo.20747873](https://doi.org/10.5281/zenodo.20747873). ([In this repository](../../2026-active-transaction-graphs/).)

[34] Vityaz, A. (2026). *On the Necessity of Noise Suppression for Minimal Good Regulators: Factorization Theorems and a Closure Conjecture*. Preprint. doi:[10.13140/RG.2.2.33143.07843](https://doi.org/10.13140/RG.2.2.33143.07843).

[35] Vityaz, A. (2026). *The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin*. Zenodo. doi:[10.5281/zenodo.20745927](https://doi.org/10.5281/zenodo.20745927). ([In this repository](../../2026-computable-boundary-of-the-firm/).)
