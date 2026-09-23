---
title: "A Phase Model of Enterprise Evolution: From Fragmentation to the Autonomous Enterprise"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-03
doi: 10.13140/RG.2.2.24883.39207
version: v1
license: CC-BY-4.0
keywords: [cybernetics, regulation theory, noise suppression, Conant–Ashby theorem, enterprise architecture, digital twin, management debt, actor graphs]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.13140/RG.2.2.24883.39207](https://doi.org/10.13140/RG.2.2.24883.39207).

# A Phase Model of Enterprise Evolution: From Fragmentation to the Autonomous Enterprise

**Alexander Vityaz** · Corezoid Inc., Dnipro, Ukraine · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

## Abstract

This paper presents a four-phase model of enterprise evolution grounded in two results from regulation theory: the Conant–Ashby good regulator theorem [1] and the factorisation necessity theorem for minimal good regulators [33]. The model describes the progression from a fragmented polycentric architecture (Phase 1) through a centralised digital core (Phase 2), a digital twin of the organisation (Phase 3), to the autonomous enterprise (Phase 4). Each phase is characterised by a structural limit beyond which further improvement in the quality of regulation requires an architectural transition. Management debt [34] is interpreted as the accounting shadow of unsuppressed organisational noise. A worked example, a retrospective case study, diagnostic metrics, and a proof sketch of the factorisation theorem are provided.

**Keywords:** cybernetics, regulation theory, noise suppression, Conant–Ashby theorem, enterprise architecture, digital twin, management debt, actor graphs.

## 1. Introduction

Enterprise architecture maturity models have a long history. The Capability Maturity Model Integration (CMMI) [5], the TOGAF Architecture Development Method [31], Gartner’s IT Score frameworks [19], and the numerous domain-specific models catalogued in Wendler’s meta-review [35] all propose staged progressions from ad hoc practice to optimised capability. These models have proven useful as assessment instruments but share a common limitation: their phase definitions are empirical and descriptive rather than derived from a formal theory of regulation.

A parallel tradition in cybernetics — originating with Wiener [36], Ashby [2], Beer [3, 4], and Conant and Ashby [1] — provides precisely such a theory. The Conant–Ashby theorem states that every good regulator of a system must be a model of that system. Ashby’s Law of Requisite Variety [2] relates regulatory capacity to the variety of disturbances. Beer’s Viable System Model (VSM) [3, 4] operationalises these principles as a recursive five-system architecture for organisational viability. Yet the connection between cybernetic regulation theory and enterprise architecture maturity modelling has remained largely unexplored (for partial exceptions, see Schwaninger [28, 29] and Espejo and Reyes [12]).

This paper proposes a phase model that bridges the two traditions. The four phases are derived from two formal requirements — the Conant–Ashby theorem and the factorisation necessity theorem [33] — rather than from empirical observation of best practices. The central claim is that each phase defines a bounded region of improvement, and that transitions between phases are compelled once the structural limit of the current architecture is reached.

Within this framework, management debt is understood as the accounting shadow of unsuppressed organisational noise. When distinctions that do not alter the set of admissible actions are not eliminated at the input, they materialise as ownership ambiguity, clarification overhead, escalations, omission duration, rework, and direct loss [34].

The paper also provides a worked example (Section 6), a retrospective case study (Section 9), and a diagnostic framework linking formal metrics to observable phase indicators (Section 11).

## 2. Related Work

**Enterprise architecture maturity models.** CMMI [5] defines five maturity levels for software processes; TOGAF ADM [31] provides a cyclical method for architecture development; the Architecture Capability Maturity Model (ACMM) [32] and the Strategic Alignment Maturity Model (SAMM) [20] assess organisational readiness. Wendler [35] catalogues over 100 maturity models across domains. De Bruin et al. [7] propose a general framework for maturity model development. The present model differs from these in that its phases are derived from regulatory-theoretic constraints rather than from empirical best-practice surveys.

**Cybernetics and organisational design.** Beer’s VSM [3, 4] decomposes viable organisations into five interacting systems (S1–S5) with recursive structure. Espejo and Harnden [11] and Espejo and Reyes [12] develop the VSM into a methodology for organisational diagnosis. Schwaninger [28, 29] applies cybernetic principles to management theory. The present paper draws explicitly on Beer’s S3/S4/S5 hierarchy for the meta-regulation architecture in Phase 3, extending it with the formal apparatus of pragmatic equivalence and noise leakage.

**Organisational information processing.** Galbraith [15] proposes that organisations process information to reduce uncertainty. Tushman and Nadler [32] develop an information processing model of organisational design. Daft and Lengel [9] introduce media richness theory as a response to information equivocality. The present paper operationalises these ideas through the lens of goal-relevant noise: information processing overhead is recast as the cost of failing to suppress pragmatically irrelevant distinctions.

**Digital twins.** The digital twin concept originates in product lifecycle management (Grieves [17]; Grieves and Vickers [18]) and has been extended to manufacturing (Tao et al. [30]) and smart cities (Fuller et al. [14]). The application to organisational structure — a Digital Twin of the Organisation (DTO) — is more recent and less formalised. The present paper provides a formal grounding for the DTO concept through the Conant–Ashby theorem: the digital twin is the model that the regulator is required to contain.

**Technical and organisational debt.** Cunningham [8] introduced the metaphor of technical debt for deferred software quality. Kruchten et al. [21] developed a taxonomy. The concept of management debt, as formalised in [34], extends the debt metaphor to deferred or unmade management decisions, with formal accounting mechanics and attribution to actor accounts.

**Noise suppression and information bottleneck.** The information bottleneck method (Tishby et al. [25]) formalises the trade-off between compression and relevance preservation. Stavrou and Kountouris [27] develop a goal-oriented rate-distortion theory. The factorisation theorem [33] establishes that minimal good regulators necessarily factorise through a noise-suppressing projection, connecting the information bottleneck framework to regulatory efficiency.

**Autonomous organisations.** Laloux [22] describes self-managing organisations. Robertson [24] formalises holacratic governance. Brynjolfsson and McAfee [6] and Davenport and Ronanki [10] discuss AI-driven decision-making. The present model characterises autonomy not as a governance philosophy but as a formal state of the regulation loop: Phase 4 is the condition under which the human exits the operational cycle and operates solely at the level of goal definition (S5).

## 3. Methodology

This paper is a theoretical contribution in the design-science tradition [23]. The artefact is a phase model: a prescriptive framework that classifies enterprise states by their regulatory architecture and identifies the structural limits that compel transitions. The model is derived deductively from two formal results (the Conant–Ashby theorem and the factorisation theorem) and one empirical observation (that each phase exhibits diminishing returns prior to its structural limit).

The formal apparatus (notation, definitions, proof sketch) is intended to be precise but deliberately lightweight: the paper is a position paper, not a full formal theory. A worked example (Section 6) grounds the notation in a concrete scenario. A retrospective case study (Section 9) provides preliminary empirical evidence. The diagnostic metrics are proposed as testable predictions; their systematic empirical validation is a subject for future work (see Section 14).

## 4. Notation

The following notation is used throughout:

- $D$ — a finite set of disturbances (incoming events, requests, incidents);
- $R$ — a finite set of regulator actions;
- $E$ — a finite set of outcomes; $E_{\text{acc}} \subseteq E$ — the set of acceptable outcomes;
- $P\colon D \times R \to E$ — the plant function;
- $A(d) := \{r \in R \mid P(d, r) \in E_{\text{acc}}\}$ — the set of admissible actions for disturbance $d$;
- $d_1 \sim_{\text{prag}} d_2 \iff A(d_1) = A(d_2)$ — pragmatic equivalence;
- $\Sigma_{\text{prag}} := D/{\sim_{\text{prag}}}$ — the pragmatic signal space;
- $\sigma_{\text{prag}}\colon D \twoheadrightarrow \Sigma_{\text{prag}}$ — the noise-suppressing projection;
- $g\colon \Sigma_{\text{prag}} \to R$ — the essential regulator;
- $\pi^* = g \circ \sigma_{\text{prag}}$ — the factorised minimal good regulator;
- $V_{\text{leak}}(\pi) := \sum_{s \in \Sigma_{\text{prag}}} \log_2 |R_s(\pi)|$ — the noise leakage of the regulator.

Formal objects are defined here and used in the worked example (Section 6), the phase descriptions, and the proof sketch (Appendix A). The notation is intentionally aligned with the full treatment in [33].

## 5. Theoretical Foundations

### 5.1. The Conant–Ashby Theorem

**Theorem 1** (Conant and Ashby, 1970)**.** *Every good regulator of a system must be a model of that system.*

In the notation of this paper: any function $\pi\colon D \to R$ satisfying $\forall d \in D\colon P(d, \pi(d)) \in E_{\text{acc}}$ must distinguish those disturbances that require different actions. The regulator must contain, in its input–output behaviour, a homomorphic image of the relevant structure of the environment.

The preconditions of the theorem are: finite state spaces, a deterministic plant function, and a well-defined goal (acceptable outcome set). These preconditions are satisfied when an enterprise is modelled at the level of discrete events, decisions, and outcomes — the level at which process mining, event-sourced ledgers, and workflow engines operate. The model does not claim to capture the full richness of organisational dynamics (strategic behaviour, emergent properties, stochastic environments); it claims to capture the regulatory layer at which formalisation is tractable and actionable. Extensions to stochastic settings are addressed in [33, Section 5.3].

### 5.2. The Factorisation Theorem

**Theorem 2** (Vityaz, 2026)**.** *Every minimal good regulator (in the sense of minimising noise leakage $V_{\text{leak}}$, conditional action entropy, or any noise-monotone functional) factorises through the pragmatic signal space:*

$$\pi^* = g \circ \sigma_{\text{prag}} \tag{1}$$

*for some $g\colon \Sigma_{\text{prag}} \to R$.*

A proof sketch is provided in Appendix A. The full proof, together with stochastic extensions and an axiomatic characterisation, is given in [33].

The theorem establishes that noise suppression is not an optional architectural feature but a necessary consequence of capacity-efficient regulation. A regulator that does not suppress noise expends action variety on distinctions that do not change admissibility — a direct waste of regulatory capacity.

### 5.3. The Self-Computation Principle

The expression $AG = (\lambda AG.\, AG(AG))(\lambda AG.\, AG(AG))$ is introduced in this paper as a design principle, not as a computational specification. Its intended interpretation is that of a fixed point: the actor graph is a structure that, when applied to itself as input, reproduces itself (possibly with modifications derived from the input event stream).

The expression is syntactically related to the $\Omega$ combinator of the untyped lambda calculus, which has no normal form. The analogy is intentional but bounded. In the untyped lambda calculus, $\Omega$ diverges. In the intended interpretation, divergence is prevented by the timescale-separated meta-regulation hierarchy (S3/S4/S5): the fast loop enforces invariants that bound the depth of self-modification, the medium loop calibrates parameters within bounded ranges, and the slow loop provides an external termination condition (human goal-setting).

The self-computation principle is accordingly a conjecture about the limit behaviour of mature actor-graph architectures, not a formal theorem. Its rigorous treatment — including a fixed-point semantics grounded in domain theory or coalgebra — is a subject for future work.

## 6. Worked Example

To ground the formal apparatus in a concrete scenario, we present a simplified enterprise case.

**Setting.** A retail company receives three types of incoming events: $D = \{d_1, d_2, d_3\}$, where $d_1$ = customer complaint about delivery delay, $d_2$ = customer complaint about damaged packaging, $d_3$ = supplier notification of shipment dispatch. The regulator has four available actions: $R = \{r_1, r_2, r_3, r_4\}$, where $r_1$ = issue refund, $r_2$ = issue replacement, $r_3$ = acknowledge and file, $r_4$ = escalate to manager. The acceptable outcomes are $E_{\text{acc}} = \{\text{customer retained, issue resolved without escalation}\}$.

**Admissible action sets.** Suppose the plant function $P$ yields:

- $A(d_1) = \{r_1, r_2\}$ — refund or replacement resolve a delivery delay.
- $A(d_2) = \{r_1, r_2\}$ — refund or replacement resolve damaged packaging.
- $A(d_3) = \{r_3\}$ — a supplier dispatch notification requires only acknowledgement.

**Pragmatic equivalence.** Since $A(d_1) = A(d_2) = \{r_1, r_2\}$ and $A(d_3) = \{r_3\}$, we obtain two pragmatic classes: $s_1 = \{d_1, d_2\}$ and $s_2 = \{d_3\}$. Thus $\Sigma_{\text{prag}} = \{s_1, s_2\}$.

**Noise leakage.** Consider a regulator $\pi_A$ that distinguishes all three events: $\pi_A(d_1) = r_1$, $\pi_A(d_2) = r_2$, $\pi_A(d_3) = r_3$. This regulator is good ($\pi_A(d) \in A(d)$ for all $d$), but on class $s_1$ it produces two distinct outputs ($r_1$ and $r_2$), so $|R_{s_1}(\pi_A)| = 2$. The noise leakage is $V_{\text{leak}}(\pi_A) = \log_2 2 + \log_2 1 = 1$ bit.

Now consider a factorised regulator $\pi_B = g \circ \sigma_{\text{prag}}$ with $g(s_1) = r_1$, $g(s_2) = r_3$. This regulator is good and $|R_s(\pi_B)| = 1$ for both classes, so $V_{\text{leak}}(\pi_B) = 0$. The factorised regulator expends no action variety on the distinction between $d_1$ and $d_2$, which does not change the admissible action set — it suppresses the noise.

**Management debt interpretation.** In a Phase 1 organisation, no system records that $d_1$ and $d_2$ are pragmatically equivalent. A customer service agent receiving $d_1$ may escalate ($r_4$) while another agent receiving $d_2$ issues a refund ($r_1$). The difference in treatment is not goal-relevant but generates clarification overhead, repeat discussions, and ownership ambiguity — all measurable as management debt. A Phase 2 digital core would encode the equivalence $A(d_1) = A(d_2)$ in its routing rules, eliminating this source of debt.

## 7. The Phase Model

### 7.1. Phase 1: The Fragmented Company

The technology landscape is formed reactively. Systems are procured or developed in layers to address the immediate needs of individual departments. The result is a polycentric structure: a multiplicity of disconnected centres of logic, data, and authority. This pattern is well-documented in the enterprise architecture literature (Ross, Weill, and Robertson [26]).

Formally, the organisation lacks a unified regulator $\pi\colon D \to R$. Instead, a collection of local functions $\{\pi_i\}$ operates, each defined over its own subset $D_i$ and lacking access to the global state.

**Economic consequences** are measurable. The proportion of work objects without an unambiguous owner (Ownership Ambiguity Rate) tends to increase and, in limit cases, reaches critical values. The density of clarifying messages per unit of work communication (Clarification Density) grows with each additional system layer. The frequency with which previously resolved topics are reopened (Repeat Discussion Index) reflects the absence of a unified decision registry. All three metrics are direct indicators of management debt [34].

**The growth of noise as a structural property.** The defining characteristic of Phase 1 is not merely a high level of noise but its uncontrolled growth. Each local subsystem $\pi_i$ processes the disturbance stream without classifying goal-relevant distinctions. Pragmatic equivalence classes are recorded nowhere: no subsystem knows which differences between events lead to different admissible action sets and which do not. Noise leakage $V_{\text{leak}}$ is maximal.

The standard response to problems within this phase — procurement of the next system — increases the effective variety of $D$ (new event types, new interfaces, new points of misalignment) without creating a suppression mechanism. Each attempt to improve global regulation within Phase 1 introduces a new source of noise. Coordination costs grow faster than the gains from automation. This is a structural limit: without a unified noise-suppressing mechanism $\sigma_{\text{prag}}$, improvement of global regulation is not possible. Local improvements (e.g., a CRM that improves sales process efficiency) remain achievable, but they do not reduce $V_{\text{leak}}$ at the organisational level.

The IT budget in this state is not an investment but the cost of maintaining escalating disorder. The phase transition to Phase 2 becomes economically inevitable when the cost of coordinating the polycentric structure exceeds the cost of deploying a regulator.

### 7.2. Phase 2: The Digital Core

The strategy of the second phase is the deployment of a unified digital core in the role of regulator. The Conant–Ashby theorem provides the necessary condition: the regulator must contain a model of the object under control. The factorisation theorem provides the architectural requirement: the regulator must be structured as the composition $\pi^* = g \circ \sigma_{\text{prag}}$.

In practice, this entails two components.

First, **noise suppression** ($\sigma_{\text{prag}}$). Before the system can make decisions, it must classify incoming disturbances by pragmatic equivalence: two events are equivalent if and only if their admissible action sets coincide. Distinctions that do not alter the admissible action set constitute noise, and the expenditure of resources on processing them is a direct economic loss. Implementation mechanisms include event normalisation, semantic deduplication, filtering by speech act type, and linking to sources and prior decisions. In one instantiation, the Corezoid platform realises $\sigma_{\text{prag}}$ through these mechanisms; alternative implementations are discussed in Section 10.

Second, **essential regulation** ($g$). The dispatching of pragmatic classes into concrete actions: commitment, deferral, bundling, assignment of an executor, risk-based routing.

Legacy systems are not eliminated at this phase; they are encapsulated. The regulator wraps them as controlled black boxes connected to the core through programmatic interfaces and service-level agreements — a pattern well established in the service-oriented architecture and API-first literature [13, 26]. The governing principle is the replacement of components without halting business operations.

The architectural foundation of self-computation (see Section 5.3) is laid at this phase as a design provision. In Phase 2, this remains a design provision; its activation is the subject of Phase 3.

**Measurable results** of the transition include a reduction in Decision Latency, Escalation Density, and Omission Duration. Management debt does not disappear but for the first time becomes an accounting object with double-entry bookkeeping [34]: it is recorded, qualified, and attributed to the account of the responsible Decision Owner.

**The structural limit of Phase 2.** The digital core resolves the coordination problem but creates a new one: the projection $\sigma_{\text{prag}}$ is calibrated manually. Filtering parameters, classification rules, and routing thresholds are set by humans on the basis of their understanding of the system. The model of the object under control, required by the Conant–Ashby theorem, exists only in fragmentary form: as a collection of processes within the core, not as a complete description of the organisation. As business complexity grows, manual calibration of $\sigma_{\text{prag}}$ falls behind reality. Noise does not grow in an uncontrolled manner as in Phase 1, but classification errors — the suppression of legitimate signals (False Suppression Rate) and the late detection of duplicates (Late-Duplicate Rate) — accumulate. The quality of regulation is bounded by the incompleteness of the model.

### 7.3. Phase 3: The Digital Twin

The Conant–Ashby theorem requires that the regulator be a model of the object under control. The structural limit of Phase 2 is precisely the deficit of such a model. Phase 3 eliminates it: a Digital Twin of the Organisation (DTO) is constructed.

The DTO concept, originating in product lifecycle management [17, 18] and extended to manufacturing [30] and urban systems [14], is applied here to organisational structure. The formal grounding is direct: the Conant–Ashby theorem requires the regulator to contain a model; the DTO is that model, rendered as an explicit, computable artefact.

The method is a transition from analytical descriptions to geometric models. The organisation is described not by textual regulations but by actor graphs in which each node is an actor with a defined role and each edge is an interaction channel with a defined semantics. The pragmatic signal space $\Sigma_{\text{prag}}$, introduced at Phase 2 as the basis for noise suppression, is formalised as a structural element of the twin’s architecture.

The self-computation principle introduced in the preceding phase moves from design provision to active operation. This entails the following:

- The twin recomputes its own structure in real time on the basis of the event stream.
- The projection $\sigma_{\text{prag}}$ is calibrated automatically through meta-regulation. The meta-regulation architecture follows Beer’s Viable System Model [3, 4], adapted to the formal apparatus of this paper. The three levels correspond to Beer’s Systems 3, 4, and 5: **S3 (fast loop)** enforces hard invariants — mandatory validation routes, work-in-progress limits, the rule “no due date without a calendar booking” — corresponding to Beer’s System 3 function of internal stability and resource allocation. **S4 (medium loop)** performs adaptive calibration of $\sigma_{\text{prag}}$ parameters by metrics (Late-Duplicate Rate, False Suppression Rate, cost of poor quality, Human-Interrupt Load), with canary deployment and rollback — corresponding to Beer’s System 4 function of environmental scanning and adaptation. **S5 (slow loop)** encompasses decisions on the composition of the acceptable outcome set $E_{\text{acc}}$ and the enumeration of algedonic events — signals that must bypass noise suppression by definition — corresponding to Beer’s System 5 function of identity and policy.
- Management debt is detected from digital traces prior to the materialisation of consequences.

In one implementation, the simulator.company design environment and the Corezoid computation environment provide the tooling for real-time model processing; alternative platforms are discussed in Section 10.

**The structural limit of Phase 3.** The digital twin produces a complete model and automatic calibration of $\sigma_{\text{prag}}$, yet the human remains a participant in the operational loop: making decisions on exceptions, processing algedonic signals, correcting $g$ in non-standard situations. As long as the human is an element of the operational loop, the throughput of the regulator is bounded by the throughput of the human.

### 7.4. Phase 4: The Autonomous Enterprise

Phase 4 is the state in which operational activity and the overwhelming majority of decisions are delegated to the regulator. The human role shifts to level S5 within the meta-regulation hierarchy: the definition of goals ($E_{\text{acc}}$), policies, and system identity.

Formally, this is the state of complete factorisation $\pi^*_{\text{org}} = g \circ \sigma_{\text{prag}}$, where $\sigma_{\text{prag}}$ is an automatically calibrated projection, $g$ is an automatically routed dispatcher, and the closure of the meta-regulation loop is ensured by the timescale-separated hierarchy described above [33, Conjecture 6.1].

**Limitations.** Autonomy does not signify the absence of the human. It signifies that the human ceases to be an element of the operational loop and becomes the architect of goals and constraints.

The following remain outside the scope of automation:

1. The definition of $E_{\text{acc}}$ — what constitutes an acceptable outcome — remains a strategic decision.
2. Algedonic events — signals that by definition cannot be suppressed (in Beer’s terminology: System 1 bypass [3]) — require human intervention.
3. The revision of pragmatic equivalence itself — the decision as to which distinctions are goal-relevant — resides in the slow loop S5.

**Governance and alignment.** The autonomous regulator must remain aligned with organisational goals as these evolve. Misalignment may arise from model drift (the DTO diverging from reality), distributional shift (genuinely novel disturbances outside the space on which $\sigma_{\text{prag}}$ was calibrated), or adversarial manipulation. These risks are mitigated by the meta-regulation hierarchy — particularly the S3 hard invariants and S4 anomaly detection — but cannot be eliminated entirely. The boundary between Phase 3 and Phase 4 is accordingly a matter of degree: an organisation is in Phase 4 to the extent that Human-Interrupt Load is reduced to S5-level intervention.

## 8. The Logic of Phase Transitions

Table 1: Phase transition mechanisms and structural limits.

| Transition | Pressure mechanism | Limit of the current phase |
|---|---|---|
| $1 \to 2$ | Uncontrolled growth of noise; each new subsystem increases the effective variety of $D$ without suppression | Global regulation cannot be improved by adding systems |
| $2 \to 3$ | Manual calibration of $\sigma_{\text{prag}}$ falls behind complexity; accumulation of classification errors | Incompleteness of the model of the object under control |
| $3 \to 4$ | The human in the operational loop bounds the throughput of the regulator | Human throughput |

At each phase, improvement within the phase is possible — up to a limit. Beyond that limit, further investment within the current architecture yields diminishing returns and, subsequently, negative returns (at Phase 1: each new system worsens the global regulatory position, even as it may improve local efficiency).

## 9. Retrospective Case Study: Corezoid Deployment at a CIS Financial Services Group

This section presents a retrospective analysis of a transition from Phase 1 to Phase 2 observed during the deployment of the Corezoid digital core at a financial services group operating across multiple CIS jurisdictions in the period 2015–2020. The analysis is based on the author’s direct involvement as platform architect. Quantitative figures are approximated from operational records; exact values are subject to commercial confidentiality.

**Phase 1 baseline (pre-2016).** The organisation operated over 40 distinct IT systems across retail banking, card processing, lending, and insurance units. Each unit maintained its own event handling logic. Customer-facing processes (loan application, card issuance, claim handling) traversed multiple systems with manual handoffs. Characteristic indicators:

- Ownership Ambiguity Rate was high: approximately 30% of customer-facing processes had no single designated owner across the full chain.
- Decision Latency for a standard loan approval averaged 3–5 business days, of which an estimated 60–70% was attributable to inter-system coordination and clarification, not to credit analysis.
- Repeat Discussion Index was not formally measured, but retrospective analysis of internal communication logs indicated that approximately 25% of coordination messages referenced previously discussed topics.
- $V_{\text{leak}}$ was not computed at the time, but the structural signature was unmistakable: the same customer event (e.g., a payment failure) triggered different responses depending on which system first received it, even when the admissible action sets were identical.

The organisation had invested in three successive integration middleware layers over the preceding decade, each adding new event types and interfaces without establishing pragmatic equivalence classes.

**Transition to Phase 2 (2016–2018).** The Corezoid digital core was deployed as a unified event-processing layer. The implementation followed the factorised architecture $\pi^* = g \circ \sigma_{\text{prag}}$:

- $\sigma_{\text{prag}}$ was realised through event normalisation across all 40+ source systems, deduplication of customer events arriving from multiple channels, and classification by business intent (action request, status query, notification).
- $g$ was implemented as a state-machine-based dispatcher routing pragmatic classes to processing pipelines with defined SLAs.
- Legacy systems were encapsulated as API-connected black boxes; no legacy system was decommissioned during the initial deployment.

**Observed outcomes (2018–2020).** After stabilisation:

- Decision Latency for standard loan approval was reduced to under 4 hours (from 3–5 days), with the reduction attributable primarily to the elimination of inter-system coordination delays.
- Ownership Ambiguity Rate dropped to approximately 5% for digitised processes (those fully routed through the core).
- Escalation Density decreased by an estimated 40% in the first year of full operation.
- Over 50 million customer-facing transactions were processed through the core per month by 2020, across card processing, lending, insurance claims, and retail banking workflows.

**Observed structural limit.** By 2019, the organisation began to encounter the Phase 2 ceiling described in Section 7.2. The projection $\sigma_{\text{prag}}$ was calibrated manually by business analysts, and as the number of event types grew (new product lines, regulatory changes, new channels), classification errors accumulated. False Suppression of legitimate escalation signals in the insurance claims pipeline was identified as a recurring problem. The cost of recalibrating $\sigma_{\text{prag}}$ manually grew faster than the complexity it was managing. This is the structural limit predicted by the model: the incompleteness of the manually maintained model of the object under control.

**Limitations of this case study.** This is a single retrospective case based on the author’s direct involvement. The quantitative figures are approximated. The case does not constitute independent empirical validation; it serves as preliminary evidence that the phase structure and the predicted structural limits correspond to observable organisational dynamics. Systematic multi-case validation is a priority for future work (Section 14).

## 10. Alternative Implementations

The theoretical model is implementation-agnostic. The factorisation $\pi^* = g \circ \sigma_{\text{prag}}$ specifies an architectural requirement — the separation of noise suppression from essential regulation — but does not prescribe a particular technology stack.

The noise-suppressing projection $\sigma_{\text{prag}}$ may be realised through process mining platforms (Celonis, Minit), business process management engines (Camunda, Zeebe), enterprise service buses, event-driven middleware, or LLM-based extraction pipelines. The essential regulator $g$ may be realised through workflow engines, rule engines, or human dispatchers augmented by decision support.

In the author’s practice, Corezoid serves as the digital core (Phase 2) and the computation environment for the DTO (Phase 3), while simulator.company provides the design environment for actor-graph modelling. These are discussed as a concrete instantiation, not as the sole possible implementation.

## 11. Diagnostics

The metrics in this table are proposed as diagnostic indicators. Their operational measurement methodology — including data sources, computation procedures, and threshold calibration — is specified for management debt metrics in [34] and for noise leakage metrics in [33, Appendix A]. The case study in Section 9 provides preliminary observed values for a Phase $1 \to 2$ transition. Systematic empirical validation of the expected phase-metric correspondence is a priority for future work (Section 14).

## 12. Limitations of the Model

1. **Finite deterministic assumption.** The formal apparatus assumes finite $D$, $R$, $E$ and a deterministic plant function $P$. Real enterprises exhibit stochastic dynamics, incomplete information, and strategic behaviour. The stochastic extension in [33, Section 5.3] partially addresses this; a full treatment of strategic (game-theoretic) behaviour is beyond the scope of the current model.

Table 2: Diagnostic indicators by phase.

| Indicator | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|---|---|---|---|---|
| Ownership Ambiguity Rate | increasing | decreasing | low | $\approx 0$ |
| Decision Latency | not measured | measured, decreasing | low; routine decisions auto-routed | minimal |
| Noise leakage $V_{\text{leak}}$ | maximal, increasing | decreasing (manual calibration) | automatically calibrated | minimal |
| Omission Duration | not recorded | recorded | detected prior to materialisation | prevented |
| False Suppression Rate | undefined | measured, reduced manually | automatically calibrated (S4) | minimal |
| Human-Interrupt Load | 100% of operational decisions | decreasing | exceptions and algedonic signals only | S5 only |
| Management debt | accumulates without control | becomes an accounting object | attributed automatically | minimised architecturally |
| Model of the object under control | absent | fragmentary | complete digital twin | self-computing actor graph |

2. **Discrete-event level of analysis.** The model captures the regulatory layer at which events, decisions, and outcomes are discrete and traceable. It does not claim to model organisational culture, tacit knowledge, or emergent social dynamics.

3. **Sequential phase assumption.** The model describes a linear progression $1 \to 2 \to 3 \to 4$. In practice, organisations may exhibit mixed states (e.g., Phase 2 in some business units while remaining in Phase 1 in others) or may skip phases under specific conditions. The model is intended as an idealised trajectory, not a strict prescription.

4. **Operationalisation of pragmatic equivalence.** Computing $A(d)$ requires knowledge of $P$ and $E_{\text{acc}}$, which in a real enterprise must be inferred from data. The computational complexity of learning $\sigma_{\text{prag}}$ from observations, and the sample complexity of doing so reliably, remain open problems [33, Section 7].

5. **Boundary between Phase 3 and Phase 4.** The distinction rests on the degree of Human-Interrupt Load reduction. A sharp boundary criterion has not been established; the transition is better understood as a continuum.

## 13. Conclusion

The four phases are not a maturity gradient. They are the consequence of two mathematical results and one economic observation. The Conant–Ashby theorem states that a regulator must be a model — without a model there is no regulation, only reaction. The factorisation theorem states that a minimal regulator must suppress noise — without noise suppression, resources are expended on distinguishing what is goal-irrelevant. The economic observation is that each phase defines a bounded region of improvement: noise either grows without control (Phase 1), or is bounded by the incompleteness of the model (Phase 2), or by human throughput (Phase 3).

A phase transition is not a matter of digital ambition. It is the only means of further reducing noise leakage $V_{\text{leak}}$, management debt, and the cost of coordination.

## 14. Future Work

1. **Empirical validation.** Systematic multi-case studies applying the diagnostic framework to enterprises at different phases. Priority: longitudinal studies demonstrating the correspondence between formal metrics and observed organisational states across industries and jurisdictions.

2. **Formal semantics of self-computation.** A rigorous fixed-point interpretation of the self-computation principle, grounded in domain theory or coalgebraic semantics, with explicit termination guarantees provided by the meta-regulation hierarchy.

3. **Learning $\sigma_{\text{prag}}$ from data.** PAC-style sample complexity bounds for learning the pragmatic projection from observed event streams, connecting to the deterministic information bottleneck framework [16, 27].

4. **Management debt detection.** Algorithms for detecting management debt from digital traces prior to materialisation, with precision/recall characterisation and failure-mode analysis.

5. **Game-theoretic extension.** Extension of the regulation model to settings where agents within the organisation behave strategically, potentially misrepresenting disturbances or outcomes.

## A. Proof Sketch of the Factorisation Theorem

The full proof is given in [33, Theorem 5.4]. The following is a sketch sufficient for the purposes of this paper.

**Setup.** Let $(D, R, E, P)$ be a regulation system with goal $E_{\text{acc}} \subseteq E$ satisfying the viability condition ($\forall d \in D\ \exists r \in R\colon P(d, r) \in E_{\text{acc}}$). Let $G$ denote the set of all good regulators. For $\pi \in G$ and $s \in \Sigma_{\text{prag}}$, define $R_s(\pi) := \{\pi(d) \mid \sigma_{\text{prag}}(d) = s\}$. The noise leakage is $V_{\text{leak}}(\pi) := \sum_s \log_2 |R_s(\pi)|$.

**Claim.** Any $\pi^* \in G$ minimising $V_{\text{leak}}$ satisfies $\pi^* = g \circ \sigma_{\text{prag}}$ for some $g\colon \Sigma_{\text{prag}} \to R$.

**Sketch.** Suppose $\pi^*$ is not constant on some pragmatic class $s$, i.e., $|R_s(\pi^*)| > 1$. Then there exist $d_a, d_b$ with $\sigma_{\text{prag}}(d_a) = \sigma_{\text{prag}}(d_b) = s$ and $\pi^*(d_a) \neq \pi^*(d_b)$. Since $d_a \sim_{\text{prag}} d_b$, we have $A(d_a) = A(d_b)$, so $\pi^*(d_a) \in A(d_b)$. Define $\pi'$ to agree with $\pi^*$ everywhere except on class $s$, where $\pi'(d) := \pi^*(d_a)$ for all $d$ with $\sigma_{\text{prag}}(d) = s$. Then $\pi'$ is good (since $\pi^*(d_a) \in A(d)$ for all $d$ in class $s$) and $|R_s(\pi')| = 1 < |R_s(\pi^*)|$, so $V_{\text{leak}}(\pi') < V_{\text{leak}}(\pi^*)$, contradicting the minimality of $\pi^*$. Therefore $|R_s(\pi^*)| = 1$ for all $s$, and $\pi^*$ factors through $\sigma_{\text{prag}}$. $\square$

The same factorisation is shown in [33] to arise under conditional action entropy minimisation, mutual information minimisation in a stochastic setting, and all noise-monotone functionals.

## Author’s Note

The Corezoid platform and the simulator.company environment were designed and built by the author specifically to solve the regulatory problems described in this paper. The theoretical framework formalises the architectural principles that emerged from over twenty years of engineering practice, beginning with the *Konveyer* graph execution engine (c. 2005), its consumer application walk2web (c. 2007),[^1] the enterprise evolution into Corezoid, the simulator.company design environment, and the subsequent formalisation as Actor Graph Theory. Theory and platform are co-evolved; the formal results presented here are grounded in this practice. Alternative implementation paths are discussed in Section 10.

[^1]: walk2web was an early graph-based web visualisation application built on the *Konveyer* engine. It appears as a reference example of web-resource graph visualisation (Figure 4) in Dougherty, M., Meyer, E. T., Madsen, C., van den Heuvel, C., Thomas, A., and Wyatt, S. *Researcher Engagement with Web Archives: State of the Art*. JISC Report, August 2010 (SSRN: 1714997); see also the companion report: Thomas, A., Meyer, E. T., Dougherty, M., van den Heuvel, C., Madsen, C., and Wyatt, S. *Researcher Engagement with Web Archives: Challenges and Opportunities for Investment*. JISC Report, August 2010 (SSRN: 1715000). Danziger, M. *Information Visualization for the People*. S.M. Thesis, MIT, 2008, cites walk2web as an example of casual information visualisation that makes complex data structures accessible to non-expert users, within the framework of Casual Infovis (Pousman, S., Stasko, J., and Mateas, M. Casual Information Visualization. *IEEE TVCG*, 13(6):1145–1152, 2007). Van den Heuvel, in his research on Paul Otlet’s vision of a global knowledge infrastructure, situates tools such as walk2web within the lineage of Otlet’s “réseau mondial” — a networked system for organising and distributing knowledge; see van den Heuvel, C. Web 2.0 and the Semantic Web in Research from a Historical Perspective. *Knowledge Organization*, 36(4):214–226, 2009; van den Heuvel, C. and Rayward, W. B. Facing Interfaces: Paul Otlet’s Visualizations of Data Integration. *Journal of the American Society for Information Science and Technology*, 62(12):2313–2326, 2011. The present work carries this lineage from knowledge organisation into algorithm execution.

## References

[1] Conant, R. C. and Ashby, W. R. Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2):89–97, 1970.

[2] Ashby, W. R. *An Introduction to Cybernetics*. Chapman & Hall, 1956.

[3] Beer, S. *Brain of the Firm*. Allen Lane, 1972.

[4] Beer, S. *The Heart of Enterprise*. John Wiley & Sons, 1979.

[5] CMMI Institute. *CMMI for Development*, Version 1.3. Carnegie Mellon University, 2010.

[6] Brynjolfsson, E. and McAfee, A. *The Second Machine Age*. W. W. Norton, 2014.

[7] De Bruin, T., Freeze, R., Kulkarni, U., and Rosemann, M. Understanding the main phases of developing a maturity assessment model. In *Proc. ACIS*, 2005.

[8] Cunningham, W. The WyCash portfolio management system. In *OOPSLA ’92 Addendum*, 1992.

[9] Daft, R. L. and Lengel, R. H. Organisational information requirements, media richness and structural design. *Management Science*, 32(5):554–571, 1986.

[10] Davenport, T. H. and Ronanki, R. Artificial intelligence for the real world. *Harvard Business Review*, 96(1):108–116, 2018.

[11] Espejo, R. and Harnden, R. (eds.). *The Viable System Model: Interpretations and Applications of Stafford Beer’s VSM*. John Wiley & Sons, 1989.

[12] Espejo, R. and Reyes, A. *Organizational Systems: Managing Complexity with the Viable System Model*. Springer, 2011.

[13] Erl, T. *SOA: Principles of Service Design*. Prentice Hall, 2008.

[14] Fuller, A., Fan, Z., Day, C., and Barlow, C. Digital twin: Enabling technologies, challenges and open research. *IEEE Access*, 8:108952–108971, 2020.

[15] Galbraith, J. R. *Designing Complex Organizations*. Addison-Wesley, 1973.

[16] Strouse, D. J. and Schwab, D. J. The deterministic information bottleneck. *Neural Computation*, 29(6):1611–1630, 2017.

[17] Grieves, M. Digital twin: Manufacturing excellence through virtual factory replication. White paper, Florida Institute of Technology, 2014.

[18] Grieves, M. and Vickers, J. Digital twin: Mitigating unpredictable, undesirable emergent behavior in complex systems. In *Transdisciplinary Perspectives on Complex Systems*, pp. 85–113. Springer, 2017.

[19] Gartner, Inc. IT Score for digital business. Gartner Research, 2019.

[20] Luftman, J. Assessing business-IT alignment maturity. *Communications of the AIS*, 4(14), 2000.

[21] Kruchten, P., Nord, R. L., and Ozkaya, I. Technical debt: From metaphor to theory and practice. *IEEE Software*, 29(6):18–21, 2012.

[22] Laloux, F. *Reinventing Organizations*. Nelson Parker, 2014.

[23] Peffers, K., Tuunanen, T., Rothenberger, M. A., and Chatterjee, S. A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3):45–77, 2007.

[24] Robertson, B. J. *Holacracy: The New Management System for a Rapidly Changing World*. Henry Holt, 2015.

[25] Tishby, N., Pereira, F. C., and Bialek, W. The information bottleneck method. In *Proc. 37th Allerton Conference*, pp. 368–377, 1999.

[26] Ross, J. W., Weill, P., and Robertson, D. C. *Enterprise Architecture as Strategy*. Harvard Business School Press, 2006.

[27] Stavrou, P. A. and Kountouris, M. A rate distortion approach to goal-oriented communication. In *Proc. IEEE ISIT*, 2022.

[28] Schwaninger, M. Intelligent organizations: An integrative framework. *Systems Research and Behavioral Science*, 18(2):137–158, 2001.

[29] Schwaninger, M. *Intelligent Organizations: Powerful Models for Systemic Management*. 2nd ed. Springer, 2009.

[30] Tao, F., Cheng, J., Qi, Q., Zhang, M., Zhang, H., and Sui, F. Digital twin-driven product design, manufacturing and service with big data. *International Journal of Advanced Manufacturing Technology*, 94:3563–3576, 2018.

[31] The Open Group. *TOGAF Standard*, Version 9.2. Van Haren Publishing, 2018.

[32] Tushman, M. L. and Nadler, D. A. Information processing as an integrating concept in organizational design. *Academy of Management Review*, 3(3):613–624, 1978.

[33] Vityaz, O. On the Necessity of Noise Suppression for Minimal Good Regulators: Factorization Theorems and a Closure Conjecture. Preprint, 2026. Available at: [https://www.researchgate.net/publication/400615896](https://www.researchgate.net/publication/400615896)

[34] Vityaz, O. Management Debt: Concept, Metrics, and Principles for Attributing Materialised Debts to Actor Accounts. Part I. Preprint, 2026. Available at: [https://www.researchgate.net/publication/402775057](https://www.researchgate.net/publication/402775057)

[35] Wendler, R. The maturity of maturity model research: A systematic mapping study. *Information and Software Technology*, 54(12):1317–1339, 2012.

[36] Wiener, N. *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press, 1948.

NotebookLM for this article.
