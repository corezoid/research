# The Compact Company: An Actor-Graph Theory of the Firm in the LLM Era

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21774758-blue.svg)](https://doi.org/10.5281/zenodo.21774758)

**Alexander Vityaz** ([ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)) · Corezoid Inc., Dnipro, Ukraine
**Published:** August 2026 · **Version:** v1 · **License:** [CC BY 4.0](../../LICENSE-CC-BY-4.0)

## Abstract

This paper introduces the **Compact Company** as a distinct category in organizational theory. A Compact Company is an organizationally closed firm whose human core is minimized by cost or headcount while remaining sufficient to satisfy legal, governance, capacity, and probabilistic viability requirements. The category is distinct from one-person, small, virtual, lean, and AI-native businesses. Most of its operational and regulatory variety is realized by an executable graph of human, software, LLM, agentic, and external actors.

The economic mechanism behind this organizational form arises from the ability of large language models to reduce the costs of semantic coordination: interpreting incomplete instructions, decomposing tasks, transferring context, preparing decisions, and processing standard exceptions. This shift changes the Coasean choice between the market and internal organization. Its effects may contract the firm along one dimension while expanding it along another: the human core can shrink as the number and variety of controlled transactions increase.

The theoretical object of the paper is a typed temporal actor graph. Its contribution lies not in a new graphical notation but in four constructions. First, the paper introduces an organizationalclosure operator that uses weak probabilistic bisimulation to represent an internal graph as a composite institutional actor while preserving the type distinction between a graph and a node. Second, it defines the boundary of the firm as an operator that attributes a particular transaction across authority, accountability, data regime, economic outcome, and control. Third, it formalizes continuity and succession through the resilience of the authority-and-state graph to families of individual and correlated failures. Fourth, it formulates compactness as the minimization of the human core under viability constraints and shows that even a simplified version of the problem is NP-hard by reduction from Minimum Set Cover.

The Conant–Ashby Good Regulator Theorem is applied within its proper scope. It rules out effective regulation without model correspondence while remaining agnostic about the medium that carries the model. This paper advances an independent thesis: for a compact digital firm, an executable digital twin provides the most complete non-personal carrier of critical organizational state and policy. The actor graph supplies the theory of the company; the digital twin provides its synchronized, versioned, and executable embodiment.

The transition to a Compact Company constitutes an institutional migration. The explication of roles, authority, and organizational state redistributes power and reduces opacity rents. A minimal human core must therefore preserve formal resilience together with a verifiable capacity for human response through hot and warm reserves.

## Files

| File | Description |
|------|-------------|
| [paper.pdf](paper.pdf) | Canonical PDF (identical to the Zenodo deposit) |
| [paper.md](paper.md) | Readable markdown version |

## How to cite

> Vityaz, A. (2026). *The Compact Company: An Actor-Graph Theory of the Firm in the LLM Era*. Zenodo. https://doi.org/10.5281/zenodo.21774758

```bibtex
@misc{vityaz2026compactcompany,
  author       = {Vityaz, Alexander},
  title        = {The Compact Company: An Actor-Graph Theory of the Firm in the LLM Era},
  year         = {2026},
  month        = aug,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21774758},
  url          = {https://doi.org/10.5281/zenodo.21774758}
}
```

## Related work in this repository

This paper is the synthesizing step of the author's research program; §3.11 sets out the genealogy of the theory explicitly.

- Builds on [Active Transaction Graphs](../2026-active-transaction-graphs/) — supplies the formal substrate: actors defined by state, interface, and transition; recursive representation of an actor by an internal graph; edges as first-class mediating actors; and the "result–trace–ledger" observational semantics (reference [51], §3.11).
- Builds on [The Computable Boundary of the Firm](../2026-computable-boundary-of-the-firm/) — establishes the boundary as an independent object of the governance model and proves observability and controllability as viability conditions; this paper refines that boundary into the transactional operator *B*<sub>t</sub><sup>U</sup> over modes I, D, M, P, and U (reference [52], §3.11, §7).
- Builds on [On the Necessity of Noise Suppression for Minimal Good Regulators](../2026-noise-suppression-minimal-good-regulators/) — supplies the factorization of the minimal regulator through a projection suppressing action-irrelevant distinctions, the basis for the distributed regulator *R*<sub>H</sub> ∪ *R*<sub>A</sub> ∪ *R*<sub>D</sub> (reference [53], §3.11, §9.1).
- Builds on [Company Brain](../2026-company-brain/) — connects the digital core, digital twin, meta-regulation, and human goal formation in one control loop; §12.2 refines its architectural thesis so that the twin embodies an organizationally closed actor graph (reference [56], §3.11, §12.2).
- Builds on [Management Debt—Part I](../2026-management-debt-part-i/) — supplies the attribution of materialised debt to actor accounts, given an architectural continuation here as mode U, rule debt, and false compactness (reference [62], §3.11, §17.3).
- Also cites [Regulatory Quality of Asymptotic Models](../2026-regulatory-quality-asymptotic-models/) (reference [54], §3.11, §17.1 — the critical scale below which a model fails to distinguish the system), [A Phase Model of Enterprise Evolution](../2026-phase-model-of-enterprise-evolution/) (reference [57], §3.11, §12.2), [Metaunderstanding](../2026-metaunderstanding/) (reference [58], §3.11 — pragmatic policy compression), and [What Is Work](../2026-what-is-work/) (reference [59], §3.11, §8.1 — redistribution of information-processing work after a rapid first LLM output). §3.11 classes these as adjacent metrics, mechanisms, and architectural constraints rather than proofs of the central propositions.
- Also cites [How to Become a Smart Company](../2026-how-to-become-a-smart-company/) (reference [61], §3.11 — the fragmentation tax, and the distinction between local functional amplification by AI tools and the architectural integrity of the company).
- Also cites works not part of this repository: *The Law of Functional Migration* [50], *On the Nature of the Regulator* [55], and *Convergence Theory and Practice for Iterative Generation with Drifting Goals* [60].
- Cited by [Actor Graphs](../2026-actor-graphs/) — whose typed temporal Actor Graph this paper applies to organisational closure and firm boundaries

## Links

- Version of record: https://doi.org/10.5281/zenodo.21774758
- ResearchGate: https://www.researchgate.net/publication/411189149

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
