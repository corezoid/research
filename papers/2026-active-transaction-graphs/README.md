# Active Transaction Graphs: A Formal Framework for Transactional Interactive Systems

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20747873-blue.svg)](https://doi.org/10.5281/zenodo.20747873)

**Alexander Vityaz** ([ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)) · Corezoid Inc., Dnipro, Ukraine
**Published:** March 2026 · **Version:** v1 · **License:** [CC BY 4.0](../../LICENSE-CC-BY-4.0)

## Abstract

We introduce Active Transaction Graphs (ATGs), a formal framework for interactive systems in which persistent state, mediated interaction, execution traceability, and accounting consequences must be modeled simultaneously. The framework is based on five core commitments: participating entities are modeled as actors, actors may be recursively structured, formally relevant interaction is transactional, graph edges are first-class computational entities, and observational semantics is determined by the triple (result, trace, ledger).

We distinguish explicitly between the minimal formal core of the framework, derived results, architectural principles, and conjectural extensions. Within the formal layer, we prove a noise projection theorem, show that finite Petri nets embed into ATGs, and show that CHAM-style systems arise as quotients of ATGs under suitable erasures. We further prove that explicit edge mediation is semantically non-eliminable in ledger-sensitive mediated systems. A worked example based on invoice approval and payment illustrates the formalism.

The framework can be extended upward with a signal layer, whose projection onto the transactional layer explains the classification of noise as semantically irrelevant interaction.

The resulting framework is intended not as a replacement for classical models of computation but as a semantic envelope for transactional interactive systems, including workflow engines, enterprise platforms, and mixed human–AI operational environments.

## Files

| File | Description |
|------|-------------|
| [paper.pdf](paper.pdf) | Canonical PDF (identical to the Zenodo deposit) |
| [paper.md](paper.md) | Readable markdown version |

## How to cite

> Vityaz, A. (2026). *Active Transaction Graphs: A Formal Framework for Transactional Interactive Systems*. Zenodo. https://doi.org/10.5281/zenodo.20747873

```bibtex
@misc{vityaz2026atg,
  author       = {Vityaz, Alexander},
  title        = {Active Transaction Graphs: A Formal Framework for Transactional Interactive Systems},
  year         = {2026},
  month        = mar,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20747873},
  url          = {https://doi.org/10.5281/zenodo.20747873}
}
```

## Related work in this repository

This paper is foundational for the collection; it does not cite the other papers here.

- Cited by [The Computable Boundary of the Firm](../2026-computable-boundary-of-the-firm/)
- Cited by [Management Debt—Part I](../2026-management-debt-part-i/)
- Cited by [Ontology of Transition—Part I](../2026-ontology-of-transition/part-i/) and [Part II](../2026-ontology-of-transition/part-ii/)
- Cited by [Regulatory Quality of Asymptotic Models](../2026-regulatory-quality-asymptotic-models/)
- Cited by [Company Brain](../2026-company-brain/)
- Cited by [Beyond Programming Languages](../2026-beyond-programming-languages/)
- Cited by [Quantum Learning](../2026-quantum-learning/)
- Cited by [The Compact Company](../2026-compact-company/) — which inherits the actor, transaction, active edge, recursion, and ledger semantics as the formal substrate of its theory of the firm
- Cited by [Actor Graphs](../2026-actor-graphs/) — which defines the Actor Graph as a named mathematical object with pluggable execution semantics; this paper is its execution specialisation

## Links

- Version of record: https://doi.org/10.5281/zenodo.20747873
- Interactive notebook (NotebookLM): https://notebooklm.google.com/notebook/a815acc0-5739-49f5-9cc4-f044c846e3d1
- Plain-language announcement: [Active Transaction Graphs](https://corezoid.com/blog/active-transaction-graphs-research-announcement/) (Corezoid blog, March 16, 2026)

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
