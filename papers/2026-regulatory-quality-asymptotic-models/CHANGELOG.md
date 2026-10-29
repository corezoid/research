# Changelog

## Repository — 2026-10-29

Erratum for Theorem 3.5 (Theorem B, model refinement), added to `README.md` and as editorial notes in
`paper.md`: the proof of part (a) infers a variance inequality from pointwise dominance of the
smoothed residuals, which only bounds second moments. Counterexample $\varepsilon^{(1)} = (2,2)$,
$\varepsilon^{(2)} = (0,2)$: the dominance holds, yet the variances are 0 and 1. A full regulator-level
example was also checked numerically: $C = (2,3,4,1,4,0)$, $r^{(1)} = (4,0,2,0,2,0)$,
$r^{(2)} = (3.938, 0.474, 3.11, 0.029, 2.12, 0)$ satisfy condition (i) for every $\sigma$, yet
$R^{(2)}(4) \approx 0.663 < R^{(1)}(4) \approx 0.742$. Parts (a)–(b) are false as stated and (c) is unproven;
they hold under dominance of the centred residuals, or under (i) plus equal mean residuals.
Theorem A and the numerical results are unaffected. `paper.pdf` (the author's text) is unchanged
until the author issues a corrected version.

## Repository — 2026-09-23

Added `paper.md`, a markdown reading version of the unchanged PDF. Its prose was checked word by
word against the PDF's text layer; formulas, tables and figures remain authoritative in
`paper.pdf`. The text of the paper itself is unchanged.

## v1 — 2026-03

Initial published version. DOI: [10.13140/RG.2.2.31082.79042](https://doi.org/10.13140/RG.2.2.31082.79042).
