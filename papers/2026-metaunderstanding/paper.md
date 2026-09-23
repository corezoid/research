---
title: "Metaunderstanding: Recursive Compression, Tag Accounts, and Actor Graphs as the Next Layer of Mind in the Age of AI"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-04
doi: null
researchgate: https://www.researchgate.net/publication/403758098
version: v1
license: CC-BY-4.0
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [ResearchGate 403758098](https://www.researchgate.net/publication/403758098).

# Metaunderstanding: Recursive Compression, Tag Accounts, and Actor Graphs as the Next Layer of Mind in the Age of AI

**Alexander Vityaz** · Corezoid Inc., Dnipro, Ukraine · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

## Abstract

The mind is not a library but a compressor-regulator. The Conant–Ashby theorem requires that every good regulator contain a model of the system it regulates [1]. The cognitive bottleneck of working memory and attention requires that this model be compressed [2, 3]. It follows that intelligence-as-control must model, and intelligence-as-computation must compress.

Metaunderstanding is defined as the discipline of designing *Mental Tags*—pragmatically oriented units of meaning that occupy a single attention slot, unpack into a class of decisions, and recursively pack into higher-order tags. The Noise Suppression Theorem (Vityaz, 2026) establishes the architectural necessity:

$$\pi^* = g \circ \sigma_{prag},$$

where $\sigma_{prag}$ eliminates distinctions that do not alter the action space [7]. The Information Bottleneck provides the criterion for goal-directed optimal compression [4], and MDL supplies the criterion of brevity and explanatory power [5, 6].

At the computational level, Tag Accounts-OS is introduced on top of Actor Graphs: tag values are recorded as actor account balances, and search, comparison, and matching are performed by comparing tag clouds rather than traversing the entire graph. A Regret Bound theorem for $\kappa$-compression shows that the losses from recursive compression are bounded above and admit a telescoping bound across hierarchy levels. The central thesis of this manifesto is: **What is compressed is not knowledge but policy.**

The paper rests on three tiers of claims: classical scientific results (Conant–Ashby, Information Bottleneck, MDL, chunking), the author's Noise Suppression Theorem, and the engineering construct of Tag Accounts + Actor Graphs.

---

## 1. Introduction

### 1.1 Motivation: The Trap of the "Comfortable Mirror"

For a long time, interface design followed a single guiding principle: the simpler the interaction, the better. This made sense as long as humans controlled machines that were fundamentally inferior in language and context.

With the advent of LLMs, this contract breaks down. The system no longer merely answers. It *mirrors*: it adapts register, lexicon, depth, and rhythm of its response [12, 13]. The dialogue becomes smooth.

It is precisely in this smoothness that a new danger arises. A locally correct answer can be obtained without any growth in the world model. The result is already there, the task is complete, yet no transferable invariant has emerged. An illusion of competence arises:

- the action has been performed;
- resistance has disappeared;
- the architecture of understanding has not changed.

The problem is not that AI "simplifies". The problem is that **simplification can preserve a weak model**. The new contract must be stated differently:

**Not to simplify the text, but to compress meaning for action.**

### 1.2 Cognitive Constraints

Human cognition runs into two hardware limitations simultaneously.

#### 1.2.1 Storage Limit

AI operates on corpora whose volume exceeds an individual's lifetime reading by orders of magnitude. Consequently, competing with the machine on the volume of erudition is a losing strategy.

#### 1.2.2 RAM Limit

Even if the entire world could be "loaded", there would still be nothing to manage it with. Working memory can hold only a few chunks [2, 3]. Hence the critical resource is not the sum of facts but the *form of their representation*.

This yields a direct engineering conclusion:

**In the age of AI, the winner is not whoever knows more but whoever compresses better.**

### 1.3 The Mind as Compressor-Regulator

The Conant–Ashby theorem establishes the minimal frame: a good regulator must contain a model of the system [1]. In other words, control is impossible without an internal representation of the world. But if the model must exist and RAM is small, then the model must be short. Therefore, the mind is not an accumulator of descriptions but a system of *model compression for action*.

---

## 2. Theoretical Foundations

### 2.1 The Noise Suppression Theorem

The Noise Suppression Theorem (Vityaz, 2026) formalizes an architectural necessity: a minimal good regulator must not expend control capacity on distinctions that do not change the class of admissible actions [7].

**Theorem (Noise Suppression, Vityaz 2026).** Let $S$ be a finite set of environmental states, $A$ a finite set of regulator actions, and $\pi : S \to \Delta(A)$ a stochastic policy. Define the pragmatic equivalence relation $s_1 \sim_{prag} s_2$ if and only if $\pi^*(s_1) = \pi^*(s_2)$ for the optimal policy $\pi^*$. Let $\sigma_{prag} : S \to S / \sim_{prag}$ be the canonical projection onto pragmatic equivalence classes. Then for any minimal good regulator there exists a mapping $g : S / \sim_{prag} \to \Delta(A)$ such that

$$\pi^* = g \circ \sigma_{prag}.$$

In other words, the optimal policy factorizes through the suppression of pragmatically irrelevant distinctions. Proof: see [7].

Here:

- $\sigma_{prag}$ is the projection onto the space of pragmatically significant distinctions;
- $g$ is the regulator operating after noise suppression;
- $V_{leak}$ is the cost of distinctions that do not affect decisions (formally: the amount of information in $S$ lost under $\sigma_{prag}$ that does *not* affect $\pi^*$; see Section 5.2).

The critical distinction:

- *physical equivalence*: how something is actually structured;
- *pragmatic equivalence*: whether it changes the class of actions.

Noise consists of distinctions within a single pragmatic class. Metaunderstanding is the discipline of constructing and maintaining $\sigma_{prag}$.

### 2.2 Information Bottleneck and MDL

The Information Bottleneck provides the criterion: a compressed representation must preserve not the full richness of the world but only the information relevant to the goal [4]. MDL adds a second test: a good model is a short description that still explains the data [5, 6].

Together they set the working standard:

**A good model is short, transferable, and preserves the class of decisions.**

### 2.3 Knowledge vs. World Model: An End-to-End Example

One need not know all of dentistry—surgery, pharmacology, anatomy, materials, and protocols. To manage treatment, a different structure suffices: teeth can be healthy or diseased; pain can be prevented; specialists and procedures exist; prevention is cheaper than catastrophe.

**Metaunderstanding replaces terabytes of facts with gigabytes of structures.**

We now show how this works across the full pipeline.

**Step 1. Tags.** Let actor $a$ = "wisdom tooth".

| Tag | Family | Level | Counterexample |
|-----|--------|-------|----------------|
| pain-probability | stat | 0 | cavity-free tooth |
| prevention-cheaper | mental | 0 | acute trauma (emergency surgery needed) |
| specialist-exists | mental | 0 | no dentist within range |
| compliance-policy | manual | 0 | procedure outside coverage |
| dental-control | mental | 1 ($\kappa$) | — |

Meta-tag dental-control = $\kappa(\{\text{prevention-cheaper, specialist-exists}\})$.

**Step 2. Accounts (Tag Accounts).**

| Tag | FD | FC | PD | PC | $\bar{w} = \phi_0$ |
|-----|----|----|----|----|---------|
| pain-probability | 3 | 0 | 5 | 0 | 3 |
| prevention-cheaper | 2 | 0 | 2 | 0 | 2 |
| specialist-exists | 1 | 0 | 1 | 0 | 1 |
| compliance-policy | 1 | 1 | 1 | 0 | 0 |

Gap for pain-probability: Planned – Fact = 5 – 3 = 2—the model expects more confirmation than is available, signaling a need to refine $\sigma_{prag}$ (perhaps an examination is needed).

**Step 3. Query and matching.**

Query: "what to do about a wisdom tooth if my insurance covers it?"

1. **Index:** $\text{Index}_{mental}[\text{prevention-cheaper}] \cup \text{Index}_{mental}[\text{specialist-exists}] \to$ candidate $a$.

2. **Filter:** $\text{Index}_{manual}[\text{compliance-policy}]$: $\bar{w} = 0$ (FD=FC), so the constraint is neutral—candidate passes.

3. **Score:** $\text{Sim}(q, a) = 1.0 \cdot \cos_{mental} + 0.3 \cdot \cos_{stat} = 0.94.^1$

4. **Verify:** $\delta(\text{dental-control})$ yields $\{\text{prevention-cheaper, specialist-exists}\}$; both tags are confirmed.

^1 This value is illustrative; exact computation requires specifying the full tag vector space and vector normalization. What matters here is the pipeline structure, not the specific number.

**Step 4. Trace.**

$$\text{prevention-cheaper} \to a = \text{"wisdom tooth"} \to \text{Acct}_{mental}(a, \text{prevention-cheaper}) \to \text{PostTag\#7} \to \text{Event\#12: exam 2025-11.}$$

The entire match is fully explainable: from the matched tag to the originating event.

---

## 3. Representational Framework

### 3.1 What Is a Mental Tag

A *Mental Tag* is a unit of compressed meaning defined not by the elegance of its formulation but by the strength of its influence on decisions. Experimental evidence shows that expert superiority is due not to expanded working memory but to the quality of chunks [9, 10, 11].

A good tag must:

1. occupy a single attention slot;
2. change the class of actions or risks;
3. have a counterexample;
4. have links;
5. unpack into a verifiable policy.

A tag is not a word. A tag is a control interface.

### 3.2 Four Tag Families

**Statistical tags show where the noise is. Mental tags show how control is structured.**

#### 3.2.1 Statistical Tags ($\tau = \text{stat}$)

Frequencies, TF-IDF, n-grams, topic profiles. They serve navigation and surface diagnostics.

#### 3.2.2 Mental Tags ($\tau = \text{mental}$)

Invariants, causal structures, failure modes, architectural trade-offs, and patterns. They serve control.

#### 3.2.3 Manual Tags ($\tau = \text{manual}$)

Accountability, SLAs, compliance, priorities, prohibitions. This is the governance layer.

#### 3.2.4 Hybrid Tags ($\tau = \text{hybrid}$)

Pipelines of the form: statistics → clustering → interpretation → manual validation. Their purpose is to scale the production of meaning.

**Remark (hybrid is a mode, not a family).** The hybrid type is not an independent semantic family alongside statistical, mental, and manual tags. It is a *mode of origin*: the process by which a statistical signal matures into a mental tag. Mature hybrid tags are reclassified as mental or stat; $\lambda_{hybrid}$ in scoring is small by default (see Table 1).

### 3.3 The Law of Recursive Compression

Let $T_k$ denote the set of tags at level $k$. Christiansen and Chater showed that the incoming stream is rapidly overwritten and the system is forced to compress recursively at each level of representation [8]. Let $C \subseteq T_k$ be a cluster that is activated within a single decision class. The packing operator:

$$\kappa : \mathcal{P}(T_k) \to T_{k+1}, \quad t^1 = \kappa(C).$$

The unpacking operator:

$$\delta : T_{k+1} \to \mathcal{P}(T_k).$$

Compression is correct if the optimal policy does not degrade:

$$\sup_{s \in S} \left\| \pi^*(s \mid C) - \pi^*(s \mid \kappa(C)) \right\|_{TV} \leq \varepsilon_k,$$

where $\| \cdot \|_{TV}$ is the total variation distance and $\varepsilon_k \geq 0$ is the tolerance at level $k$. Equivalently, the expected regret from replacing $C$ with $\kappa(C)$ does not exceed $\varepsilon_k$. When $\varepsilon_k = 0$, exact pragmatic equivalence obtains; in practice the tolerance is chosen so that the cumulative error $\sum_k \varepsilon_k$ remains bounded (for the formal bound, see the Regret Bound theorem in Section 5.2).

As long as recurring action patterns exist, there is an opportunity to move up a level:

$$\text{data} \to T_1 \to T_2 \to T_3 \to \cdots$$

### 3.4 What Is Compressed Is Not Knowledge but Policy

The tag hierarchy mirrors the control hierarchy. A low-level tag activates a technique. A Meta-Tag activates a mode. A meta-meta-tag sets a posture.

**Remark (Meta-Tag is a level, not a family).** A *Meta-Tag* is not a separate tag family alongside statistical, mental, and manual tags. It is the next compression level *within the mental hierarchy*: the result of applying $\kappa$ to a cluster of mental tags that are systematically co-activated. Table 1 records the orthogonality of family (semantic type) and level (compression depth).

Table 1 records the orthogonality of family (semantic type) and level (compression depth).

**Table 1:** Family × level: two independent dimensions of a tag.

| | **Level 0 (base)** | **Level 1 ($\kappa$)** | **Level 2+ ($\kappa^2,\ldots$)** |
|---|---|---|---|
| **stat** | TF-IDF, n-gram | topic cluster | meta-topic |
| **mental** | invariant, trade-off | DS Trade-offs | architectural posture |
| **manual** | SLA, prohibition | governance package | compliance regime |
| **hybrid**\* | statistical signal | interpretation | → mental/stat |

\* hybrid is a mode of origin; mature tags are reclassified.

**The higher the tag level, the larger the decision space that can be controlled through a single working-memory slot.**

### 3.5 The Funnel of Forced Curiosity

The brain resists constructing new equivalence classes. An external engineering mechanism is therefore needed.

1. **Injection.** A term is introduced that raises the level of the model.

2. **Detection.** The term either provokes a question or increases $V_{leak}$.

3. **Blocking.** If a correct decision is impossible without the new tag, the system has the right to halt further simplification. However, blocking must not be a dead-end; along with refusal, the system offers a micro-scenario of $\delta$-unpacking—a minimal set (definition, example, counterexample) sufficient to form the tag "here and now". *Ethical constraint:* Blocking must respect user autonomy—it proposes rather than imposes; in educational contexts, the learner's right to skip the step is preserved.

4. **Compression.** A *Mental Tag* is formed: definition, examples, counterexample, actions.

5. **Refactoring.** Clusters are packed into the next level.

The purpose of the funnel is to make the growth of the world model unavoidable.

### 3.6 Tag Algebra and Tag Debt

#### 3.6.1 Basic Operations

| Operation | Meaning | Example |
|-----------|---------|---------|
| Define($t$) | invariant + boundaries | Idempotency |
| Ground($t$) | 2 examples + 1 counterexample | PUT / upsert / append-only log |
| Link($t_i, t_j$) | edge in the tag graph | Retry Safety ↔ Idempotency |
| $\kappa(C)$ | packing into a Meta-Tag | DS Trade-offs |
| $\delta(t^1)$ | unpacking | DS Trade-offs → CAP, EC, Idempotency |

Validity criterion for Link($t_i, t_j$): a link is considered substantive if the default action sets of the two tags overlap, i.e., there exist situations in which activating one tag changes the policy of the other.

#### 3.6.2 Refactoring

- **Merge:** two tags yield a single interface.
- **Split:** a tag loses its boundaries.
- **Rename:** a meaning collision is eliminated.
- **Deprecate:** a tag no longer changes decisions.

#### 3.6.3 Tag Debt

Tag Debt is vocabulary without leverage: it consists of tags lacking counterexamples, links, or default actions.

---

## 4. Computational Architecture

### 4.1 Actor Graphs: A Unified Form for Objects and Edges

In *Actor Graphs*, both vertices and edges are represented as actors. Consequently, if an edge is also an actor, it can carry tags, events, accounts, and history.

The specification includes:

- actor anatomy: graph, time, events, triggers, account trees;
- Event actor with Event account and Tag field;
- account tree as Fact/Planned × Debit/Credit;
- edge actors;
- connection rules.

Key consequence: because an edge is a full-fledged actor with its own tags, accounts, and events, search and matching extend not only to entities but also to *interactions between them*. Matching edges becomes as natural as matching objects.

### 4.2 Tag Accounts-OS: Meaning as Accounting

**A tag is an account. The value of a tag is the account balance.**

Let $a$ be an actor, $t$ a tag, and $\tau$ a tag type. Then:

$$\text{Acct}_\tau(a, t)$$

is the tag account, and

$$w_\tau(a, t) := \text{Balance}(\text{Acct}_\tau(a, t))$$

is its value.

Since the balance decomposes as $(Fact / Planned) \times (Debit / Credit)$, the tag automatically becomes a multi-channel signal:

- Fact—accumulated evidence;
- Planned—target hypothesis;
- Gap = Planned – Fact—model error.

For retrieval and ranking, the full four-component vector is not used directly; instead, a scalar projection—the operator $\phi$ mapping the accounting balance to a retrieval weight—is applied:

$$\bar{w}_\tau(a, t) = \phi(w_\tau(a, t)).$$

The default form is the net fact:

$$\phi_0(w) = \text{FD} - \text{FC},$$

i.e., the difference between factual debit and credit. When accounting for the gap with the model, an extended projection is used, e.g., $\phi_1(w) = (\text{FD} - \text{FC}) + \alpha(\text{PD} - \text{PC})$, where $\alpha$ weights the contribution of the planned component. It is $\bar{w}_\tau$ that enters the tag clouds and participates in scoring and ranking.

This is where the bridge between the *Information Bottleneck* (Part II) and the accounting mechanism is completed. Gap = Planned – Fact is not merely a bookkeeping difference but a *model-error signal* that triggers correction of $\sigma_{prag}$ via the following mechanism:

1. **Detection.** If $|\text{Gap}(a, t)| > \theta$ for tag $t$ of actor $a$, the system records that the current projection $\sigma_{prag}$ is missing distinctions that turned out to be action-relevant.

2. **Split or Define.** A $\delta$-unpacking is triggered: the pragmatic class that produced the error is split (Split) or gives rise to a new tag (Define) that refines the boundaries of the equivalence class.

3. **Update of $\sigma_{prag}$.** The refined relation $\sim_{prag}$ yields a finer projection; the corresponding tags and accounts are updated via PostTag.

Thus the four-component tag balance implements the very feedback loop that the *Information Bottleneck* describes through the $\beta$-trade-off between compression and relevance.

A new meaning always opens a new account:

$$\text{OpenTagAccount}(a, \tau, t) \to \text{acctId}.$$

A change to a tag is recorded as a posting:

$$\text{PostTag}(a, \tau, t, \Delta; \text{plane, side; eventRef}).$$

Consequently, every tag becomes traceable:

$$\text{tag} \to \text{account} \to \text{postings} \to \text{events.}$$

### 4.3 Roll-up: Recursive Compression as Bookkeeping

If a meta-tag is implemented as a parent account, then:

$$w_{meta}(a, t^1) = \sum_{t \in \text{Children}(t^1)} w_{mental}(a, t).$$

Linear summation is not accidental: it inherits the fundamental property of accounting—*balance additivity*. The debit and credit of a parent account equal the sums of debits and credits of its child accounts; any nonlinearity would violate the closure of postings and render auditing impossible. If a task requires nonlinear aggregation (e.g., max or a weighted $\ell_p$-mean), this is realized at the level of the projection $\phi$ *after* roll-up, not within it.

$\kappa$ becomes an operation on the plan of accounts. Recursive compression becomes account refactoring, not a metaphor.

### 4.4 Tag Clouds as Signatures

For type $\tau$:

$$C_\tau(a) := \{(t, \bar{w}_\tau(a, t)) \mid \bar{w}_\tau(a, t) \neq 0\}.$$

The full actor signature:

$$C(a) = \{C_{stat}(a), C_{manual}(a), C_{mental}(a), C_{hybrid}(a)\}.$$

**Remark.** The $C_{hybrid}$ channel is auxiliary: it reflects an unfinished tag-production pipeline rather than an independent semantic type. Mature hybrid tags are reclassified as mental or stat; $\lambda_{hybrid}$ in scoring is small by default (justification in Section 4.5.2).

A graph $G$, viewed as a top-level actor, also has its own clouds:

$$\bar{w}_\tau(G, t) = \text{Compress}_\tau \left( \sum_{a \in A(G)} \beta_\tau(a) \cdot \bar{w}_\tau(a, t) \right).$$

Here:

- $\beta_\tau(a) \in [0, 1]$ is the *significance weight* of actor $a$ for channel $\tau$. Default: $\beta_\tau(a) = 1$ (uniform contribution). Examples of refinements include: $\beta_{mental}$ proportional to the actor's depth in the hierarchy, and $\beta_{stat}$ proportional to the actor's data volume.

- $\text{Compress}_\tau : \mathbb{R} \to \mathbb{R}$ is a monotone subadditive function preventing domination by large subgraphs. Default: $\text{Compress}_\tau$ = id (identity). Alternatives: log(1 + x), tanh, hard threshold.

In summary, the tag cloud of a graph is the compressed sum of its components' clouds.

### 4.5 Mental Search and Matching

Full graph traversal is expensive. The practical architecture divides into three steps:

1. **Index:** retrieval by signatures;
2. **Score:** ranking by similarity;
3. **Verify:** local structural verification.

#### 4.5.1 Index

$$\text{Index}_\tau[t] := \{a \mid \bar{w}_\tau(a, t) \neq 0\}.$$

#### 4.5.2 Similarity

$$\text{Sim}(q, a) = \sum_\tau \lambda_\tau \cdot \frac{\langle \mathbf{v}_\tau(q), \mathbf{v}_\tau(a) \rangle}{\|\mathbf{v}_\tau(q)\| \|\mathbf{v}_\tau(a)\|},$$

where $\mathbf{v}_\tau(a)$ is the vector of values $\bar{w}_\tau(a, t)$ over all tags in cloud $C_\tau(a)$.

The weights $\lambda_\tau$ set the channel priority during retrieval. Default values: $\lambda_{manual} = \infty$ (hard filter; see Query-by-Example below), $\lambda_{mental} = 1.0$, $\lambda_{stat} = 0.3$, $\lambda_{hybrid} = 0.1$. Justification for the hierarchy:

- *manual*—hard constraints (compliance, SLA): violation renders a candidate invalid, so manual operates as a filter rather than a weight;

- *mental*—the primary control signal: determines the decision class and carries the highest $\lambda$;

- *stat*—surface navigation: useful for preliminary narrowing but does not determine policy;

- *hybrid*—unfinished pipeline: $\lambda_{hybrid}$ is small because these tags have not yet passed validation. As they are reclassified into mental/stat, their contribution is redistributed.

The specific values of $\lambda_\tau$ are calibrated per domain; the defaults above reflect the structural channel hierarchy.

#### 4.5.3 Query-by-Example

$$\text{Cand} = \left( \bigcup_{t \in T_{M}(q)} \text{Index}_{mental}[t] \right) \cap \left( \bigcap_{t \in T_{manual}(q)} \text{Index}_{manual}[t] \right).$$

First, candidates are gathered via semantic anchors; they are then filtered by governance constraints, ranked, and locally verified.

#### 4.5.4 Fragments and Explainability

A fragment $F$ is aggregated as:

$$\bar{w}_\tau(F, t) = \sum_{x \in F} \alpha_\tau(x) \cdot \bar{w}_\tau(x, t).$$

It then becomes a "super-actor" for the same retrieval mechanism.

Every match can be reconstructed via its trace:

$$\text{matched tags} \to \text{carrier actors} \to \text{accounts} \to \text{postings} \to \text{events.}$$

---

## 5. Operationalization and Evaluation

### 5.1 Growth Protocol

The full cycle is captured by the Funnel (Part III): Injection → Detection → Blocking → Compression → Linking → Refactoring → Operate.

### 5.2 Metrics

#### 5.2.1 $V_{leak}$: Cost of Irrelevant Distinctions

**Definition.** Let $\sigma_{prag} : S \to S / \sim_{prag}$ be the current projection. Then:

$$V_{leak} := H(S) - H(S/\sim_{prag}) - I_{action},$$

where $H$ is entropy and $I_{action}$ is the mutual information between the discarded distinctions and the optimal policy $\pi^*$. Under an ideal $\sigma_{prag}$ we have $V_{leak} = 0$: everything discarded is truly irrelevant.

**Measurement procedure.** Count how many distinctions in the current model (tags, attributes, graph branches) do not change any default action. Each such distinction contributes to $V_{leak}$. In the finite discrete case, $I_{action} = 0$ for each distinction that does not alter any action, so counting such distinctions yields an unnormalized proxy for $V_{leak}$.

**Example.** In the dental case (Section 2.3): the distinction between a "ceramic" and a "composite" filling does not change the decision "go see a dentist" and therefore contributes to $V_{leak}$.

#### 5.2.2 Compression Ratio: Tag Capacity

**Definition.**

$$\text{CR}(t) := \frac{|\{s \in S \mid t \text{ is activated on } s\}|}{|\delta(t)|},$$

i.e., the ratio of the number of situations covered by the tag to the number of sub-tags after unpacking.

**Procedure.** For each tag, count (numerator) how many objects or situations activate it and (denominator) how many elements $\delta$ yields. A high CR indicates effective compression.

**Example.** dental-control covers all situations involving toothache, prevention, and dentist selection (≈ 20 scenarios); $\delta$ yields 2 sub-tags ⇒ CR = 10.

#### 5.2.3 DES (Decision Equivalence Score): Correctness of $\kappa$

**Definition.** Let $d_{TV}(P, Q) := \sup_{A \in \Omega} |P(A) - Q(A)|$ denote total variation distance.

$$\text{DES}(\kappa, C) := 1 - \sup_{s \in S} d_{TV}\left( \pi^*(s \mid C), \pi^*(s \mid \kappa(C)) \right).$$

DES = 1 indicates exact pragmatic equivalence; DES < 1 – $\varepsilon_k$ signals overcompression.

**Theorem (Regret Bound for $\kappa$-compression).** Let $S$ be a finite state set, $A$ a finite action set, $r : S \times A \to [0, R_{max}]$ a bounded reward function, and $\pi^*$ the optimal policy.

Let $C \subseteq T_k$ be a tag cluster and $\kappa(C) = t^1$ its compression. Then the expected loss from replacing $C$ with $\kappa(C)$ is bounded:

$$\sup_{s \in S} \left| V^*(s \mid C) - V^*(s \mid \kappa(C)) \right| \leq R_{max} \cdot (1 - \text{DES}(\kappa, C)),$$

where $V^*(s \mid X) := \sum_{a \in A} \pi^*(a \mid X) r(s, a)$ is the expected reward under representation $X$. Here $\pi^*(a \mid X)$ denotes the output of the optimal policy when the agent observes the world through the set of active tags (not a conditional probability in the Bayesian sense).

**Proof.** Fix an arbitrary $s \in S$ and write $P := \pi^*(s \mid C)$, $Q := \pi^*(s \mid \kappa(C))$. Partition $A$ into $A^+ := \{a : P(a) > Q(a)\}$ and $A^- := A \setminus A^+$. Then:

$$V^*(s \mid C) - V^*(s \mid \kappa(C)) = \sum_{a \in A} (P(a) - Q(a)) r(s, a)$$

$$= \sum_{a \in A^+} (P(a) - Q(a)) r(s, a) + \sum_{a \in A^-} (P(a) - Q(a)) r(s, a).$$

The first sum is bounded above:

$$\sum_{a \in A^+} (P(a) - Q(a)) r(s, a) \leq R_{max} \sum_{a \in A^+} (P(a) - Q(a)) = R_{max} \cdot d_{TV}(P, Q),$$

since $r(s, a) \leq R_{max}$ and $\sum_{a \in A^+} (P(a) - Q(a)) = d_{TV}(P, Q)$ by definition of total variation distance.

The second sum is $\leq 0$, since on $A^-$ we have $P(a) - Q(a) \leq 0$ and $r \geq 0$.

An analogous bound on the absolute value gives:

$$\left| V^*(s \mid C) - V^*(s \mid \kappa(C)) \right| \leq R_{max} \cdot d_{TV}(P, Q).$$

Taking the sup over $s$ and substituting the definition of DES:

$$\sup_{s \in S} \left| V^*(s \mid C) - V^*(s \mid \kappa(C)) \right| \leq R_{max} \cdot \sup_{s \in S} d_{TV}\left( \pi^*(s \mid C), \pi^*(s \mid \kappa(C)) \right) = R_{max} \cdot (1 - \text{DES}(\kappa, C)).$$ □

**Corollary (Telescoping bound for recursive compression).** Consider a chain of compressions: $T_0 \xrightarrow{\kappa_0} T_1 \xrightarrow{\kappa_1} \cdots \xrightarrow{\kappa_{n-1}} T_n$, where $\text{DES}(\kappa_k) \geq 1 - \varepsilon_k$ at each level. Then the total loss is bounded:

$$\sup_s \left| V^*(s \mid T_0) - V^*(s \mid T_n) \right| \leq R_{max} \cdot \sum_{k=0}^{n-1} \varepsilon_k.$$

**Proof.** By the triangle inequality for $d_{TV}$:

$$d_{TV}\left( \pi^*(s \mid T_0), \pi^*(s \mid T_n) \right) \leq \sum_{k=0}^{n-1} d_{TV}\left( \pi^*(s \mid T_k), \pi^*(s \mid T_{k+1}) \right) \leq \sum_{k=0}^{n-1} \varepsilon_k.$$

Applying the main theorem to the left-hand side yields the result. □

The telescoping bound explains why controlling $\varepsilon_k$ at each compression level is critical: errors accumulate. If $\varepsilon_k \to 0$ sufficiently fast (e.g., $\varepsilon_k = O(2^{-k})$), the cumulative regret remains finite even with an infinite hierarchy depth.

**DES measurement procedure.** For each meta-tag, compare the default actions activated by the meta-tag with the union of actions of its descendants. If actions have appeared or vanished, DES decreases.

**Example.** $\kappa(\{\text{prevention-cheaper, specialist-exists}\}) = \text{dental-control}$. Both child tags lead to "schedule a dentist visit" and "verify insurance"—the meta-tag activates the same actions ⇒ DES = 1.0, regret = 0.

#### 5.2.4 Tag Debt: Dead Accounts

**Definition.**

$$\text{TD}(a) := \left| \left\{ t \mid \text{Acct}_\tau(a, t) \text{ exists}, \left| \text{Transactions}(\text{Acct}_\tau(a, t)) \right| \leq 1, \delta(t) = \varnothing \right\} \right|.$$

The account is open but inactive: no postings, no counterexamples, no default actions.

**Procedure.** Traverse all open Tag Accounts of an actor. If an account has $\leq 1$ posting, the tag has no counterexample, and it has no links, it counts as Tag Debt.

**Example.** The tag "dental nomenclature" was opened after reading an article but has neither associated actions nor counterexamples and therefore counts as Tag Debt.

### 5.3 The Role of AI

AI is needed in three modes:

- **Decompressor:** unpack a tag on demand;
- **Compiler:** help pack a cluster;
- **Tester:** find counterexamples and spurious abstractions.

### 5.4 Two Failure Modes

**Abstraction without leverage.** The word exists but the action does not—Tag Debt.

**Overcompression.** A Meta-Tag has destroyed distinctions important for the decision. Antidote: Split + mandatory $\delta$.

---

## 6. Related Work

### 6.1 Positioning Against Adjacent Paradigms

Metaunderstanding arises at the intersection of several traditions. Here we map the boundaries and points of contact.

**Predictive Processing and Active Inference.** Friston's free-energy principle [14] formalizes the agent as a system minimizing surprise through updating a generative model. Common ground: both paradigms are driven by the imperative to "compress representations for action"; $\sigma_{prag}$ in our terminology is a discrete analogue of free-energy reduction. The difference: Metaunderstanding focuses not on Bayesian updating but on *discrete tag algebra and bookkeeping traceability*. Active Inference does not offer an accounting mechanism for auditable storage of compressed representations—this is the niche of Tag Accounts-OS.

**Conceptual Spaces.** Gärdenfors [15] models concepts as convex regions in a geometric quality space. A Mental Tag is the discrete analogue: not a region in a continuous space but a control interface with a counterexample and a default action. Common ground: both approaches place "compression for decision" above formal definition—it is precisely this stance that Metaunderstanding inherits. Difference: Conceptual Spaces operates via a similarity metric; Tag Accounts operates via account balances.

**Sensemaking.** Weick [16] and Klein et al. [17] describe how organizations construct "good enough" models for action under uncertainty. Metaunderstanding inherits the central insight of sensemaking—that the model is not for truth but for action—and formalizes what sensemaking describes narratively: a *Mental Tag* is the product of sensemaking, and Tag Debt is its failure. Difference: Zettelkasten has neither bookkeeping semantics nor a formal compression-correctness criterion (DES).

**Personal Knowledge Management and Zettelkasten.** Luhmann's method [18]—a recursive system of notes with cross-references—inspires the $\kappa/\delta$ operators: a note ≈ a level-0 tag; a cluster of notes ≈ a meta-tag. Difference: Zettelkasten has neither bookkeeping semantics nor a formal compression-correctness criterion (DES).

**Category Theory and Compositional Cognitive Science.** Spivak [19] and Phillips [20] build compositional models of cognition via functors and (co)limits. $\kappa$ as packing and $\delta$ as unpacking can be viewed as special case of adjoint functors; formalizing this connection is a direction for future work.

**Folksonomies and Tag Systems.** Halpin et al. [21] study collaborative tagging on the web. Metaunderstanding differs from folksonomies in three respects:

- tags are typed (stat/mental/manual/hybrid);
- tags carry accounts with debit/credit;
- tags are governed by a formal criterion of pragmatic correctness rather than popularity statistics.

---

## 7. Conclusion

### 7.1 Mini-Manifesto in 10 Lines

1. AI removes the ceiling on knowledge accumulation but not on attention.

2. A good regulator must contain a model of the system.

3. Working memory is small; therefore the model must be compressed.

4. $\pi^* = g \circ \sigma_{prag}$; noise suppression is an architectural necessity (Noise Suppression Theorem).

5. A *Mental Tag* is a unit of compressed meaning: 1 slot → a class of decisions.

6. Statistical tags describe the surface; mental tags govern action.

7. Tags compress recursively: cluster → *Meta-Tag* → higher.

8. What is compressed is not knowledge but policy.

9. Tag Accounts and Actor Graphs make meaning computable and auditable.

10. AI remains the decompressor and tester; agency is maintained at the level of invariant architecture.

Next step: empirical validation on a real Actor Graphs instance—measuring $V_{leak}$, CR, DES, and Tag Debt on a working graph of a company or project.

---

## Reference Links

NotebookLM workspace: [Open NotebookLM notebook](https://notebooklm.google.com)

---

## References

[1] R. C. Conant and W. R. Ashby. Every good regulator of a system must be a model of that system. *Int. J. Systems Science*, 1(2):89–97, 1970.

[2] G. A. Miller. The magical number seven, plus or minus two. *Psychological Review*, 63(2):81–97, 1956.

[3] N. Cowan. The magical number 4 in short-term memory. *Behavioral and Brain Sciences*, 24(1):87–114, 2001.

[4] N. Tishby, F. C. Pereira, and W. Bialek. The information bottleneck method. *Proc. 37th Allerton Conf.*, pp. 368–377, 1999.

[5] J. Rissanen. Modeling by the shortest data description. *Automatica*, 14(5):465–471, 1978.

[6] P. D. Grünwald. *The Minimum Description Length Principle*. MIT Press, 2007.

[7] A. Vityaz. On the necessity of noise suppression for minimal good regulators. Preprint, January 2026. DOI: 10.13140/RG.2.2.33143.07843.

[8] M. H. Christiansen and N. Chater. The now-or-never bottleneck. *Behavioral and Brain Sciences*, 39:e62, 2016.

[9] W. G. Chase and H. A. Simon. Perception in chess. *Cognitive Psychology*, 4(1):55–81, 1973.

[10] J. Sweller. Cognitive load during problem solving. *Cognitive Science*, 12(2):257–285, 1988.

[11] D. Norris and K. Kalm. Chunking and data compression in verbal short-term memory. *Cognition*, 208:104534, 2021.

[12] H. Giles, J. Coupland, and N. Coupland (eds.). *Contexts of Accommodation*. Cambridge Univ. Press, 1991.

[13] K. G. Niederhoffer and J. W. Pennebaker. Linguistic style matching in social interaction. *J. Language and Social Psychology*, 21(4):337–360, 2002.

[14] K. Friston. The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2):127–138, 2010.

[15] P. Gärdenfors. *Conceptual Spaces: The Geometry of Thought*. MIT Press, 2000.

[16] K. E. Weick. *Sensemaking in Organizations*. Sage, 1995.

[17] G. Klein, B. Moon, and R. R. Hoffman. Making sense of sensemaking 1: Alternative perspectives. *IEEE Intelligent Systems*, 21(4):70–73, 2006.

[18] S. Ahrens. *How to Take Smart Notes*. CreateSpace, 2017.

[19] D. I. Spivak. *Category Theory for the Sciences*. MIT Press, 2014.

[20] S. Phillips and W. H. Wilson. Category theory as the language of consciousness. *Neuroscience of Consciousness*, 2018(1):niy004, 2018.

[21] H. Halpin, V. Robu, and H. Shepherd. The complex dynamics of collaborative tagging. *Proc. 16th Int. Conf. World Wide Web*, pp. 211–220, 2007.
