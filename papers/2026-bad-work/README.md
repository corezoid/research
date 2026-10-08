# BAD WORK: Work without a Control Loop and a State Structure Isn't Worth Doing

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23015137-blue.svg)](https://doi.org/10.5281/zenodo.23015137)

**Alexander Vityaz** ([ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)) · Corezoid Inc., Dnipro, Ukraine
**Published:** September 28, 2026 · **Version:** v1 · **License:** [CC BY 4.0](../../LICENSE-CC-BY-4.0)

## Abstract

Work that crosses programs, APIs, organizations, and people can outlive any one execution context. A timeout may leave the outcome of an external action unknown; a restart may erase the information needed to decide what is admissible next. This article proposes a compact organizational analogue of Alan Perlis's pairing of a loop and a structured variable: the control loop and the state structure. The control loop relates observed consequences to a goal and selects clarification, retry, compensation, or escalation. The state structure preserves participants, obligations, confirmed facts, unknown outcomes, and transition history. The proposal is connected to the Conant-Ashby regulator theorem and developed through actor graphs with stateful mediator actors, persistent interaction history, and accounting consequences. A bank debit example separates safety, liveness, and conformance. The practical criterion is a handoff test: another executor should be able to resume unfinished work from saved state without reconstructing the system's memory by hand.

**Keywords:** control loop; state structure; actor graph; distributed systems; durable execution; verification; organizational memory

A short essay (5 pages) that applies results proved elsewhere in this corpus; it states a practical criterion — the handoff test — rather than new theorems.

## Files

| File | Description |
|------|-------------|
| [paper.pdf](paper.pdf) | Canonical PDF (identical to the Zenodo deposit) |
| [paper.md](paper.md) | Readable markdown version |

## How to cite

> Vityaz, A. (2026). *BAD WORK: Work without a Control Loop and a State Structure Isn't Worth Doing*. Zenodo. https://doi.org/10.5281/zenodo.23015137

```bibtex
@misc{vityaz2026badwork,
  author       = {Vityaz, Alexander},
  title        = {BAD WORK: Work without a Control Loop and a State Structure Isn't Worth Doing},
  year         = {2026},
  month        = sep,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23015137},
  url          = {https://doi.org/10.5281/zenodo.23015137}
}
```

## Related work in this repository

- **Builds on** [On the Necessity of Noise Suppression for Minimal Good Regulators](../2026-noise-suppression-minimal-good-regulators/) — reference [6]: the factorisation result used to keep in the state structure only the distinctions needed to choose an action, so that noise does not become extra work.
- **Builds on** [Actor Graphs](../2026-actor-graphs/) — reference [7]: the formal background for the stateful mediator actors, persistent interaction history and accounting consequences the essay relies on.

## Links

- Version of record: https://doi.org/10.5281/zenodo.23015137

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
