# Glossary

The corpus's own terms, worded as closely as possible to the defining text. Each entry names the
work that defines it (paths relative to the corpus root); read that text before relying on a
formal detail. Maintained by hand — add a term when a new work introduces one.

## Formal model

- **Actor Graph (AG)** — a named mathematical object with pluggable execution semantics; people,
  software, AI and organisations are actors, and interactions are mediated by actor-valued edges.
  Its central construction is *triple-identity accountable mediation*: a persistent link carries a
  LinkID, each occurrence a TransactionID, the reusable mediator actor an ActorID. Account mutation
  is transaction-sourced. — `papers/2026-actor-graphs`
- **Active Transaction Graph (ATG)** — the execution specialisation of Actor Graphs: actors, possibly
  recursive; formally relevant interaction is transactional; edges are first-class computational
  entities; observational semantics is the triple **(result, trace, ledger)**. Explicit edge
  mediation is proved non-eliminable in ledger-sensitive systems. — `papers/2026-active-transaction-graphs`
- **Universal computing element (UCE)** — the patented computing node (object queue, counters,
  functions) integrable with any external service via API; the engineering ancestor of the actor
  model in Corezoid. — `patents/US11237835-api-controlled-universal-computing-elements`
- **Actor graph engine** — patented engine that converts data about an object into an actor-graph
  model and answers simulation requests against it. — `patents/US20240378338-actor-graph-engine`

## Regulation and cybernetics

- **Good Regulator Theorem (Conant–Ashby)** — every good regulator of a system must be a model of that
  system. The corpus's common foundation; applied "within its proper scope" (it requires model
  correspondence but is agnostic about the medium). — `papers/2026-noise-suppression-minimal-good-regulators`, `papers/2026-compact-company`
- **Noise suppression / factorization theorem** — a *minimal* good regulator must factorize through a
  noise-suppressing projection onto a pragmatic signal space: π* = g ∘ σ_prag. Called the
  **Vityaz–Ashby theorem** in *What Is Work*. — `papers/2026-noise-suppression-minimal-good-regulators`
- **Noise leakage** — quantitative measure of control capacity spent on goal-irrelevant
  distinctions; minimizing it forces the factorization above. — same
- **Meta-regulation** — "who regulates the noise suppressor?"; conjectured to close via a three-level
  hierarchy with timescale separation (a conjecture, not a theorem). — same
- **Regulatory quality R(σ)** — fraction of a finite system's variance explained by an asymptotic
  model at observation scale σ; below a critical scale σ* model-based regulation is impossible. — `papers/2026-regulatory-quality-asymptotic-models`

## The enterprise

- **Phase model** — four phases: fragmented polycentric architecture → digital core → digital twin
  of the organisation → autonomous enterprise; each has a structural ceiling that only an
  architectural transition removes. — `papers/2026-phase-model-of-enterprise-evolution`
- **Digital twin of an organisation (DTO)** — executable model of the company's actors, roles,
  states, constraints and transitions; the Actor Graph is its theory, the twin its synchronized,
  versioned embodiment. — `papers/2026-company-brain`, `papers/2026-compact-company`
- **Company Brain** — the cognitive organ of an enterprise that emerges when digital core, digital
  twin, meta-regulation and human goal-setting converge into one regulatory loop. AI is a local
  computational framework inside the AG macro-framework, not a sovereign regulator. — `papers/2026-company-brain`
- **Big Graph of Company Context (BGCC)** — the concrete Actor Graph instance for a given
  organisation. — `papers/2026-company-brain`
- **Hybrid Intelligence protocol** — formal transaction loop between the AI subgraph and the human
  inside the Actor Graph. — `papers/2026-company-brain`
- **Management debt** — the consequence of a management decision not made, deferred, inadequately
  formalised or not executed, where that absence raises ambiguity, delays, manual intervention,
  error and loss probability. **Omission debt**: debt from an obligated party's failure to decide;
  recorded on the responsible actor's account from observable evidence, not surveys. Interpreted as
  "the accounting shadow of unsuppressed organisational noise". — `papers/2026-management-debt-part-i`, `papers/2026-phase-model-of-enterprise-evolution`
- **Fragmentation tax** — the compounding cost of fragmentation across software, integrations,
  processes, vendors and routines; also a *grounding* tax (after Clark–Brennan), because functions
  operate on incompatible projections of the same company. — `papers/2026-how-to-become-a-smart-company`
- **Smart Company** — an organisation with a proactive, executable digital twin in which actors,
  processes, connections, states and transitions are explicit; its two properties are
  **plasticity** (structure available for deliberate change, metaprogramming) and a **Company Brain**.
  Diagnostic: does the company know how many APIs it uses? — `papers/2026-how-to-become-a-smart-company`
- **Compact Company** — an organizationally closed firm whose human core is minimized under legal,
  governance, capacity and viability constraints, with most operational variety carried by an
  executable graph of human, software, LLM and external actors. Minimizing the human core is NP-hard.
  Related: **opacity rent**, **hot and warm human reserves**. — `papers/2026-compact-company`
- **Computable boundary of the firm / Executable Boundary Actor (Actor∂S)** — viability requires
  observability of causally significant actors' membership and tunable interface permeability
  (Theorem 1); the engineering pattern is an actor that executes the boundary. — `papers/2026-computable-boundary-of-the-firm`

## Work, cognition, learning, software

- **Law of Information Conservation** — artifact quality is a function of the information accounted
  for; the information volume a task requires is fixed by the task, not the tool. With the **Law of
  the Bottleneck** (human reading/verification throughput) and the **Law of Factorization** it
  explains the AI productivity paradox in high-context work. **AImatics**: LLM as interface,
  executable graph as the deterministic filter. — `papers/2026-what-is-work`
- **Metaunderstanding** — the discipline of designing **mental tags**: units of meaning that occupy
  one attention slot, unpack into a class of decisions, and pack recursively; **tag accounts** record
  tag values as actor account balances. Thesis: "what is compressed is not knowledge but policy". — `papers/2026-metaunderstanding`
- **Learning quantum** — a minimal, completed and verified transition from one capability state to
  another; the unit of **quantum learning**, which replaces the linear programme with an individual
  graph of transitions. — `papers/2026-quantum-learning`
- **Code as regenerable artifact** — AI separates intelligibility from execution precision; the
  verified Actor Graph becomes the source of operational truth, code a regenerable implementation. — `papers/2026-beyond-programming-languages`
- **Register** — the set of concepts and ways of reasoning a person or company is able to use. AI
  adapts to the user's register and so masks the gap it should expose; the book's method for raising
  the register is describing the world as actor graphs. — `codex-of-actors/chapter-00-why-do-you-need-this-book`

## Foundations

- **Ontology of Transition** — transition, not the static thing, is the primitive unit of
  description; events form a locally finite causal order without presupposed time. Internal time
  accumulates from the system's own changes; external time is reconstructed from a physical, lossy
  clock record. A **thing** is a stable, recognizable organization of transitions (object *types* and
  *tokens*). Separation Principle: time, work, entropy production and distinguishability are distinct
  functionals of one causal carrier. — `papers/2026-ontology-of-transition`
