# Publishing workflow

The full lifecycle of a paper, from draft to published and versioned. Drafting happens in a private drafts repository (`research-drafts`, internal); this repository holds only published work.

## Lifecycle at a glance

```
draft (research-drafts, private)
  → review (draft PR in research-drafts)
  → Zenodo deposit (DOI minted)
  → publish PR into corezoid/research
  → tag papers/<slug>/v1 + GitHub Release
  → distribute (ResearchGate, Substack, LinkedIn — all pointing at the DOI)
  → revisions: new Zenodo version DOI → v2 tag
```

## 1. Draft

1. In `research-drafts`, create a branch `article/<slug>` and a folder `drafts/<slug>/` from `_template/`.
2. Open a **draft PR** early. The PR is the review thread: line-level comments on prose, suggestions, decisions.
3. Keep `CHANGELOG.md` in the draft folder as the paper evolves.

Language policy: papers are published in **English or Ukrainian**. Originals in other languages stay in `research-drafts` until an EN/UK version exists.

## 2. Review

- Reviewers comment on the draft PR.
- The PR is marked "Ready for review" when the text is final.
- Merge into `main` of `research-drafts` = editorially approved, ready to publish.

## 3. Zenodo deposit (DOI)

Each paper gets its **own Zenodo record** (do not use the repo-level GitHub–Zenodo release integration for papers — it mints a DOI for the whole repository snapshot, not the paper):

1. Upload the final PDF to [zenodo.org](https://zenodo.org/) → *New upload*, type **Publication**.
2. Metadata: title exactly as in the paper; author `Vityaz, Alexander` with affiliation `Corezoid Inc., Dnipro, Ukraine` and ORCID `0009-0006-0489-7881`; license **CC BY 4.0**; keywords.
3. Publish. Zenodo mints two DOIs:
   - **Version DOI** — this exact text (cite this for reproducibility);
   - **Concept DOI** — resolves to the latest version.
4. In *Related identifiers*, add `is supplemented by` → the paper's folder URL in this repository.

> ORCID tip: with Zenodo added as a *trusted party* in the author's ORCID account, every new DOI is pushed to the ORCID "Works" list automatically.

## 4. Publish into this repository

Open a PR against `corezoid/research` (use the PR template checklist) that adds `papers/<year>-<slug>/`:

```
papers/<year>-<slug>/
├── README.md      # abstract, metadata, DOI badge, How to cite, Related work
├── paper.pdf      # canonical PDF — identical to the Zenodo deposit
├── paper.md       # readable markdown version (front matter: title, author, date, doi, keywords, abstract, version)
└── CHANGELOG.md   # version history of the text
```

The same PR must also update:

- the paper index table in the root `README.md` (and the citation graph if the new paper cites earlier ones);
- [`bibliography.bib`](bibliography.bib) — add the BibTeX entry;
- **Related work** sections of already-published papers that the new paper cites (cross-links are bidirectional).

Merge to `main` = publication.

## 5. Tag and release

```bash
git tag -a "papers/<slug>/v1" -m "<Paper title> v1 — <DOI>"
git push origin "papers/<slug>/v1"
```

Create a GitHub Release from the tag, titled `<Paper title> v1`, with the abstract, the DOI badge, and the changelog as release notes.

## 6. Distribute

ResearchGate, Substack, LinkedIn, etc. are **distribution channels, not the citation target**. Always reference the Zenodo DOI:

- ResearchGate is not the version of record. Historical `10.13140/RG.2.2.*` DOIs (generated on RG for some earlier uploads) remain valid, but an RG-hosted text can be replaced without version history — so for new papers mint the DOI on Zenodo and paste it into RG's DOI field instead of generating one there;
- Substack/blog posts should link to the DOI and to the paper folder here.

## 7. Revisions (v2, v3, …)

Papers are versioned like arXiv: integer versions, each immutable.

1. Revise the text (via `research-drafts` if the change is substantial).
2. On Zenodo: open the existing record → *New version* → upload the new PDF → publish. A new **version DOI** is minted under the same concept DOI.
3. PR here: replace `paper.pdf`/`paper.md`, bump `version:` and `doi:` in the front matter, describe the change in `CHANGELOG.md` ("Changes from v1: …").
4. Tag `papers/<slug>/v2` + Release.

Old versions remain retrievable via git tags and via their Zenodo version DOIs.

## Metadata rules

- One human-authored source of truth: the paper's front matter + root `CITATION.cff`. Everything else (BibTeX, badges) is derived from it.
- **Never add a `.zenodo.json`** next to `CITATION.cff` — Zenodo silently ignores `CITATION.cff` when `.zenodo.json` is present.
- ORCID format differs by file: full URL in `CITATION.cff` (`https://orcid.org/…`), bare digits elsewhere.
- BibTeX entries use `@misc` with `publisher = {Zenodo}` and the version DOI, matching Zenodo's own export.
