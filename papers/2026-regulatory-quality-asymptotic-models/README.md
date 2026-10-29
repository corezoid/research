# Regulatory Quality of Asymptotic Models: A Quantitative Framework with Arithmetic Benchmark

[![DOI](https://img.shields.io/badge/DOI-10.13140%2FRG.2.2.31082.79042-blue.svg)](https://doi.org/10.13140/RG.2.2.31082.79042)

**Alexander Vityaz** ([ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)) · Corezoid Inc., Dnipro, Ukraine
**Published:** March 2026 · **Version:** v1 · **License:** [CC BY 4.0](../../LICENSE-CC-BY-4.0)

## Abstract

We introduce a quantitative framework for measuring how well an asymptotic model regulates a finite system, grounded in the Conant–Ashby Good Regulator Theorem. The central construct is *regulatory quality* $R(\sigma)$, a function of observation scale $\sigma$ that measures the fraction of system variance explained by a model after symmetric smoothing. We prove, for general bounded sequences with asymptotically predictable means, the existence of a critical scale $\sigma^*$ below which model-based regulation is impossible. We establish conditions under which a structurally richer model achieves a smaller critical scale. As a benchmark, we apply the framework to the distribution of primes across consecutive decades (intervals of width 10), using the chain $r_\mathrm{PNT} \preceq \mathrm{Li}(x) \preceq \mathcal{R}(x)$ as a hierarchy of regulators. Numerical experiments on $10^6$ decades (primes up to $10^7$) confirm the theoretical predictions: a sharp threshold phenomenon in $R(\sigma)$, logarithmic scaling $\sigma^* \sim \ln N$, and monotone ordering of critical scales across the regulator hierarchy.

**Keywords:** regulation theory, Conant–Ashby theorem, Ashby's Law, model quality, prime distribution, noise suppression, threshold phenomena

**MSC 2020:** 93B05 (Controllability), 94A17 (Measures of information), 11N05 (Distribution of primes)

> **Erratum (Theorem 3.5 / Theorem B).** The proof of part (a) does not hold: pointwise dominance of the
> smoothed residuals, $|\varepsilon^{(2)}_\sigma(k)| \leq |\varepsilon^{(1)}_\sigma(k)|$, bounds their second moments but
> not their variances, because the variance also subtracts the squared mean. Counterexample:
> $\varepsilon^{(1)} = (2, 2)$, $\varepsilon^{(2)} = (0, 2)$ satisfy the dominance yet $\mathrm{Var}(\varepsilon^{(1)}) = 0 < 1 = \mathrm{Var}(\varepsilon^{(2)})$;
> any constant-preserving positive averaging keeps the dominance, so comparing *smoothed* residuals does not repair it.
> Parts (a)–(b) are therefore false as stated, and (c) is unproven. They hold if condition (i) is replaced by dominance of the
> *centred* residuals, $|\varepsilon^{(2)}_\sigma(k) - \bar\varepsilon^{(2)}_\sigma| \leq |\varepsilon^{(1)}_\sigma(k) - \bar\varepsilon^{(1)}_\sigma|$,
> or supplemented by equal mean residuals, $\bar\varepsilon^{(2)}_\sigma = \bar\varepsilon^{(1)}_\sigma$, for all $\sigma$. Theorem A
> (Lemmas 3.1–3.2, Theorem 3.3) and the numerical results are unaffected. The PDF is the author's text and is unchanged;
> see [CHANGELOG.md](CHANGELOG.md).

## Files

| File | Description |
|------|-------------|
| [paper.pdf](paper.pdf) | Canonical PDF (author's copy of the ResearchGate deposit) |
| [paper.md](paper.md) | Readable markdown version |

## How to cite

> Vityaz, A. (2026). *Regulatory Quality of Asymptotic Models: A Quantitative Framework with Arithmetic Benchmark*. Preprint, ResearchGate. https://doi.org/10.13140/RG.2.2.31082.79042

```bibtex
@misc{vityaz2026regulatory,
  author       = {Vityaz, Alexander},
  title        = {Regulatory Quality of Asymptotic Models: A Quantitative Framework with Arithmetic Benchmark},
  year         = {2026},
  howpublished = {Preprint, ResearchGate},
  doi          = {10.13140/RG.2.2.31082.79042},
  url          = {https://doi.org/10.13140/RG.2.2.31082.79042}
}
```

## Related work in this repository

- Builds on [On the Necessity of Noise Suppression for Minimal Good Regulators](../2026-noise-suppression-minimal-good-regulators/) — reference [8]; Section 6.3 uses the present framework as a concrete case study for the noise suppression necessity result.
- Builds on [Active Transaction Graphs](../2026-active-transaction-graphs/) — reference [9], cited in Section 6.5 as a non-arithmetic application domain for the framework.
- Cited by [The Compact Company](../2026-compact-company/) — which uses the critical scale of model quality to bound the classes of situations in which the human core can safely contract.

## Links

- Version of record: https://doi.org/10.13140/RG.2.2.31082.79042
- ResearchGate: https://www.researchgate.net/publication/402229391

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
