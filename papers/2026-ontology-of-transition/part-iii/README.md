# Ontology of Transition — Part III: The Thermodynamic Price of External Time: Rate–Distortion Bounds for Physical Clock Records

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21473025.svg)](https://doi.org/10.5281/zenodo.21473025)

**Alexander Vityaz** ([ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)) · Corezoid Inc., Dnipro, Ukraine
**Published:** July 2026 · **Version:** v1 · **License:** [CC BY 4.0](../../../LICENSE-CC-BY-4.0)

> Part III of the three-part volume *[Ontology of Transition](../)* ([complete-volume DOI 10.5281/zenodo.21380580](https://doi.org/10.5281/zenodo.21380580)).

## Abstract

This article is Part III of the three-part scientific work *Ontology of Transition*. The work's central idea is that transition, rather than the static thing, is the primary unit of description, while operational time is realized through physical records of transitions whose production, transmission, interpretation, and reuse have distinct informational and thermodynamic limits.

External time is operationally available to a system only through a physical record of a selected clock process, delivered through a possibly noisy, incomplete channel *K*(C→S) (Part I [1]). Part II [2] quantified two costs of that mediation: a channel information floor on reconstruction (its Theorem II.A) and a thermodynamic precision floor on the reading register (its Theorem II.D). This paper adds a renewal-work bound to the series' cost decomposition. For a finite classical footprint with equal-free-energy logical states, exact isothermal renewal without accessible correlated side information obeys *β⟨W_renew⟩ ≥ R_K^clock(D) ≥ R(D)*, where *R_K^clock* is the indirect (remote) rate–distortion function determined by the physical clock-delivery channel — the classical indirect rate–distortion problem induced by the delivered clock record [3, 4, 5]. The bound extends to correlated finite histories without i.i.d. assumptions; closed forms are derived for a uniform *M*-phase clock behind a symmetric channel and behind an erasure-and-substitution channel, with the exact indirect frontier proved via the Wolf–Ziv reduction; a sequential-ring corollary shows the asymptotic renewal cost equals the entropy of innovations, not the tick count. Target distortions below the channel's Bayes risk are unattainable at any reset budget. The three floors — information destroyed in the channel, precision paid in register dissipation, reuse paid in reset work — constrain different observables by different mechanisms and none implies another. The result does not identify time with work; it prices one specified operation: making a prescribed resolution of external time reusable at a chosen system boundary. All closed forms are verified against a Blahut–Arimoto solver to machine precision, and the literal decoder attains the indirect frontier at minimum distortion exactly. The causal (nonanticipative) version is posed as the open target.

**Keywords:** external time; physical clock records; indirect rate–distortion; remote source coding; rate–distortion theory; Landauer principle; renewal work; reusable memory; thermodynamics of information; Blahut–Arimoto algorithm; entropy of innovations

## Contents

| Section | Content |
|---------|---------|
| §1–2 | From ontology to reset work; operational model and the two rate–distortion functions |
| §3 | **Lemma III.1** — the Wolf–Ziv reduction to the record alphabet |
| §4 | **Theorem III.1** — clock-record rate–distortion–renewal bound (single record) |
| §5 | Finite-history version (correlated histories, no i.i.d. assumption) |
| §6 | Closed form for a uniform *M*-phase clock; channel-aware closed form |
| §7 | Minimal test model; **Proposition III.1** — exact indirect frontier; Figure III.1 |
| §8 | Sequential ring corollary: renewal pays for innovation, not ticks |
| §9–11 | Tightness; the three floors of the accessible clock; what the theorem does *not* say |
| §12–14 | The open causal target; relation to prior work; outlook |
| App. N | Numerical verification (N.1–N.4), Blahut–Arimoto cross-checks |

## Files

| File | Description |
|------|-------------|
| [paper.pdf](paper.pdf) | Canonical PDF (identical to the Zenodo deposit) |
| [paper.md](paper.md) | Readable markdown version |

## How to cite

> Vityaz, A. (2026). *Ontology of Transition—Part III: The Thermodynamic Price of External Time: Rate–Distortion Bounds for Physical Clock Records*. Zenodo. https://doi.org/10.5281/zenodo.21473025

```bibtex
@misc{vityaz2026ontology3,
  author       = {Vityaz, Alexander},
  title        = {Ontology of Transition---Part III: The Thermodynamic Price of External Time: Rate--Distortion Bounds for Physical Clock Records},
  year         = {2026},
  month        = jul,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21473025},
  url          = {https://doi.org/10.5281/zenodo.21473025}
}
```

To cite the architecture and conclusions of the three-part work as a whole, use the [complete-volume DOI](../#how-to-cite) instead.

## Related work in this repository

- **Builds on** [Ontology of Transition — Part I](../part-i/) — supplies the external-clock architecture: causal order, the selected clock subsystem, the delivery channel *K*(C→S), and the separation principle whose cost taxonomy §14 closes the loop with.
- **Builds on** [Ontology of Transition — Part II](../part-ii/) — its Theorem II.A and Theorem II.D become Floors 1 and 2 of the three-floor synthesis in §10; Part III adds Floor 3.
- **Builds on** [The Computable Boundary of the Firm](../../2026-computable-boundary-of-the-firm/) — cited (ref. [18]) for the formal treatment of the system boundary as an explicit information-bearing object of control, which the reset-work attribution of Theorem III.1 requires.
- **Builds on** [Active Transaction Graphs](../../2026-active-transaction-graphs/) — the foundational framework of the corpus, reached through Part I and the boundary paper.

## Links

- Version of record: https://doi.org/10.5281/zenodo.21473025
- Complete volume: https://doi.org/10.5281/zenodo.21380580 · [series overview](../)

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
