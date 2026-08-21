# Actor Graphs: Triple-Identity Accountable Mediation and Coinductive Disclosure

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21995981-blue.svg)](https://doi.org/10.5281/zenodo.21995981)

**Alexander Vityaz** ([ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)) · Corezoid Inc., Dnipro, Ukraine
**Published:** August 18, 2026 · **Version:** v1 · **License:** [CC BY 4.0](../../LICENSE-CC-BY-4.0)

*Subtitle: Identity-Faithful Representations, Transaction-Sourced Accounts, and a Presheaf Accountability Skeleton*

## Abstract

This paper defines an **Actor Graph (AG)** as a named mathematical object with pluggable execution semantics. Its central contribution is **triple-identity accountable mediation**: a persistent structural relation carries a LinkID, each recognised occurrence carries a TransactionID, and the reusable mediator actor carries an ActorID. Link and transaction references preserve Local versus OpaqueExternal constructors. Identity-faithful representation is defined by recoverability of this sorted signature, and a non-collapse theorem formalises the independent discriminators required by the link/occurrence/mediator identity split.

Account mutation is transaction-sourced. Typed account state is a dependent sum; every account type has a deterministic effect action, each conserved type additionally has an abelian effect group and equivariant valuation, and a successful commit couples canonical record creation, typed history append, account postings, and causal events. This yields deterministic state, order independence for commuting effects over causal linear extensions, closed-boundary conservation, and an explicit open-boundary flow identity.

Recursive structure is given by a finitary polynomial functor and its final coalgebra. Raw finite observations are adequate for identity-preserving bisimulation under C0–C7, while registry-backed back-reference compression is proved adequate under S1–S4. At the resolved accountability layer, ActorID, LinkID, TransactionID, AccountCoordinate, and PostingOccurrence sorts form an ID-normal skeleton. Its instance category is a presheaf topos with pointwise limits and colimits, adhesive structural gluing, and a categorical obstruction to reconstruction after identity collapse. Identity-preserving adjacency stores (LinkID, EdgeActorID) pairs; mediator-only and numeric matrices are explicit lossy projections. Closure under graph-valued continuation is proved at the signature level and interpreted, without a geometric claim, as structural self-similarity. Programming-language macro-expressibility and relative maximality remain open programmes.

**Keywords:** Actor Graphs; actor-valued edges; triple-identity accountable mediation; typed link references; transaction-sourced accounts; coinductive disclosure; identity-preserving bisimulation; presheaf accountability skeleton; signature closure

## Files

| File | Description |
|------|-------------|
| [paper.pdf](paper.pdf) | Canonical PDF (identical to the Zenodo deposit) |

## How to cite

> Vityaz, A. (2026). *Actor Graphs: Triple-Identity Accountable Mediation and Coinductive Disclosure*. Zenodo. https://doi.org/10.5281/zenodo.21995981

```bibtex
@misc{vityaz2026actorgraphs,
  author       = {Vityaz, Alexander},
  title        = {Actor Graphs: Triple-Identity Accountable Mediation and Coinductive Disclosure},
  year         = {2026},
  month        = aug,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21995981},
  url          = {https://doi.org/10.5281/zenodo.21995981}
}
```

## Related work in this repository

The paper's own annotated corpus list (front matter) describes each relation; the annotations below follow it.

- **Builds on** [Active Transaction Graphs](../2026-active-transaction-graphs/) — the execution specialisation of Actor Graphs: transaction primacy, first-class edge mediation, recursive actors, and (result, trace, ledger) semantics.
- **Builds on** [On the Necessity of Noise Suppression for Minimal Good Regulators](../2026-noise-suppression-minimal-good-regulators/) — provides the cybernetic factorisation result used by several Actor Graph applications.
- **Builds on** [A Phase Model of Enterprise Evolution](../2026-phase-model-of-enterprise-evolution/) — places Actor Graphs in the transition from a digital core to a digital twin and autonomous enterprise.
- **Builds on** [Company Brain](../2026-company-brain/) — applies Actor Graphs to the computable geometric model and digital twin of an organisation.
- **Builds on** [The Computable Boundary of the Firm](../2026-computable-boundary-of-the-firm/) — develops actor membership, boundary observability, permeability, and the Executable Boundary Actor.
- **Builds on** [Management Debt — Part I](../2026-management-debt-part-i/) — develops attributable actor accounts and ledger consequences for managerial omissions.
- **Builds on** [Beyond Programming Languages](../2026-beyond-programming-languages/) — argues that verified Actor Graphs can become the source of operational truth while code becomes a regenerable process implementation.
- **Builds on** [The Compact Company](../2026-compact-company/) — applies a typed temporal Actor Graph to organisational closure, firm boundaries, continuity, and the minimum human core.
- Also builds on the [Ontology of Transition](../2026-ontology-of-transition/) volume — develops the event order, physical records, and operational time used by dynamic Actor Graph models *(the volume sits outside the per-paper citation graph; see its parts)*.
- **Cited by** [How to Become a Smart Company](../2026-how-to-become-a-smart-company/) — the essay's reference [2]: the Actor Graph as the executable model that makes organisational structure available for metaprogramming.
- Also cites a work not part of this repository: *On the Nature of the Regulator: A Symposium on Frameworks and Actor Graphs* (doi: 10.13140/RG.2.2.30218.02244) — positions the Actor Graph as a macro-framework for regulation with AI as a local framework within it.

## Links

- Version of record: https://doi.org/10.5281/zenodo.21995981

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
