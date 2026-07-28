# The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20745927-blue.svg)](https://doi.org/10.5281/zenodo.20745927)

**Alexander Vityaz** ([ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)) · Corezoid Inc., Dnipro, Ukraine
**Published:** June 2026 · **Version:** v1 · **License:** [CC BY 4.0](../../LICENSE-CC-BY-4.0)

## Abstract

In the practice of digital twins of organizations (DTOs), the boundary of the enterprise is often not instantiated as an independent object of the control model. This paper develops a stochastic model of the firm as a controlled Markov process in which actor membership, interface permeability, and operational dynamics are integrated into a single object of control, while viability is defined as the retention of an essential variable within the homeostatic set *K*. A **necessary condition** for viability in a nonstationary, overloading environment is proved: boundary representation—namely, observability of the membership of causally significant actors and tunability of permeability—is necessary to prevent asymptotic collapse (Theorem 1). A **conditional sufficiency** result is also formulated: if the representation makes it possible to construct a policy with compensated overload and Lyapunov drift toward an optimum, then the system preserves practical (recurrent) viability (Theorem 2). The bridge "residual entropy ⇒ positive risk" is derived through an explicit anti-concentration lemma (Lemma 2), rather than postulated. Distributed and centralized representations are equivalent in policy expressiveness under the idealization of synchronous communication (Theorem 3); when one moves to an asynchronous model with losses, they diverge: a communication lower bound Ω(|N(a)|) applies to distributed labeling (Lemma 3), whereas a consistency–availability dichotomy applies to the centralized case (Lemma 4), yielding regime-dependent dominance of centralization with respect to the communication component of context-grounding costs (Theorem 4). The engineering implication is the pattern of an **Executable Boundary Actor**, *Actor∂S*.

## Files

| File | Description |
|------|-------------|
| [paper.pdf](paper.pdf) | Canonical PDF (identical to the Zenodo deposit) |
| [paper.md](paper.md) | Readable markdown version |

## How to cite

> Vityaz, A. (2026). *The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin*. Zenodo. https://doi.org/10.5281/zenodo.20745927

```bibtex
@misc{vityaz2026boundary,
  author       = {Vityaz, Alexander},
  title        = {The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin},
  year         = {2026},
  month        = jun,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20745927},
  url          = {https://doi.org/10.5281/zenodo.20745927}
}
```

## Related work in this repository

- Builds on [Active Transaction Graphs](../2026-active-transaction-graphs/) — the transactional interpretation of actors used to crystallize boundary representation into the *Actor∂S* root object (§6).
- Builds on [Management Debt — Part I](../2026-management-debt-part-i/) — supplies the recognition and attribution rules under which materialised boundary losses may be posted to the responsible Decision Owner (§4, §6).
- Cited by [Ontology of Transition — Part I](../2026-ontology-of-transition/part-i/) and [Part III](../2026-ontology-of-transition/part-iii/).
- Also cites *The Actor Codex, Chapter X. The Boundaries of the Firm* (working draft, in preparation) — not part of this repository.

## Links

- Version of record: https://doi.org/10.5281/zenodo.20745927

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
