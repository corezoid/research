# An Exercise in Futility: Work without a Control Loop and a State Structure Isn't Worth Doing

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23015137-blue.svg)](https://doi.org/10.5281/zenodo.23015137)

**Alexander Vityaz** ([ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)) · Corezoid Inc., Dnipro, Ukraine
**Published:** September 28, 2026 · **Version:** v1 (revised September 30, 2026) · **License:** [CC BY 4.0](../../LICENSE-CC-BY-4.0)

## Abstract

In many organizations, unfinished work can only be picked up by the person who started it. When a process runs across several systems, services and people, sending a request, receiving it and getting the result become separate events. After a failure, two questions arise: what actually happened, and which commitments are still open. Too often the answers live in one manager’s memory or in message threads. Every incident, handover or absence then forces the team to rebuild context by hand. In this essay I develop an idea from computer scientist Alan Perlis, “a program without a loop and a structured variable isn’t worth writing,” into a principle for managing work: work without a control loop and a state structure isn’t worth doing. The control loop compares results against the goal. When an outcome is unclear, it triggers clarification, retry, compensation or escalation under rules agreed in advance. The state structure is the shared record of who is involved, what has been promised, what is confirmed and what is still unknown. It stays intact when systems restart or people change. Using the example of a bank payment whose confirmation was lost, I show why a business process must be able to say “we don’t know yet” instead of guessing. I then show how to describe people, software and organizations in one model, so that a payment is never taken twice and the outcome of every case is eventually established. I close with a handoff test any manager can run tomorrow: hand one unfinished commitment to a colleague and see whether the records alone tell them what is done, what is open and what to do next.

**Keywords:** control loop, state structure, handoff test, actor graph, mediator actor, outcome unknown, safety and liveness, good regulator, Alan Perlis, accountability, handover, business continuity, key-person dependency, operational risk, process management

A short essay (5 pages) that applies results proved elsewhere in this corpus; it states a practical criterion — the handoff test — rather than new theorems.

> **Version note.** This folder holds the author's revised text of September 30, 2026, retitled *An Exercise in Futility*
> (first deposited as *BAD WORK*). The Zenodo record behind the DOI still carries the first deposit; the body of
> the essay is unchanged, while the title, abstract and keywords were rewritten. See [CHANGELOG.md](CHANGELOG.md).

## Files

| File | Description |
|------|-------------|
| [paper.pdf](paper.pdf) | Canonical PDF (author's revised version; newer than the Zenodo deposit) |
| [paper.md](paper.md) | Readable markdown version |

## How to cite

> Vityaz, A. (2026). *An Exercise in Futility: Work without a Control Loop and a State Structure Isn't Worth Doing*. Zenodo. https://doi.org/10.5281/zenodo.23015137

```bibtex
@misc{vityaz2026futility,
  author       = {Vityaz, Alexander},
  title        = {An Exercise in Futility: Work without a Control Loop and a State Structure Isn't Worth Doing},
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
