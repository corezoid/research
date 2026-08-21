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

## Patents

USPTO patents by the author live under `patents/`, one folder per patent **family**
(application → A1 publication → B2 grant is one folder, arXiv-style), each with
`README.md` + `patent.pdf` (the official publication — a public record, downloadable
from Google Patents: `patents.google.com/patent/<number>/en` → citation_pdf_url).

Rules:

- **Only publicly published documents.** Granted patents (B2) and published
  applications (A1) belong here. Provisional applications, unpublished filings, and
  invention ideas stay in the private drafts repository until the USPTO publishes them.
- When a tracked application publishes (A1) or grants (B2): add/update the family folder,
  the `## Patents` table in the root README, the `@patent` entry in `bibliography.bib`,
  and the entry in `tools/manifest.json` (CI enforces all of these).
- Patent READMEs link thematically related papers with **"See also"** only — patents are
  not part of the papers citation graph, and CI rejects `Builds on`/`Cited by` there.
- Authoritative metadata source: the PDF's own front page (fields (45), (57), (72), (73)),
  plus Google Patents for current legal status.
- After merging: tag `patents/<slug>/v1` and create a GitHub Release titled
  `<Title> — <number>` (same convention as papers). When a tracked application later
  grants, update the folder (rename to the grant number, replace the PDF) and edit the
  existing release rather than minting a second one.

### Non-US registrations

Ukrainian inventions and utility models are indexed as a single table in `patents/ua/README.md`,
not as a folder per family:

- **No `patent.pdf`.** The Ukrainian register (sis.ukrpatent.org) serves documents through a
  JavaScript application with no direct PDF link, so the register entry is linked as the
  authoritative record instead. A folder holding no `patent.pdf` is outside the manifest checks
  by design — do not add such folders to `tools/manifest.json`, and do not create per-patent
  folders until official publications can actually be attached.
- Titles are recorded in Ukrainian as registered, with an English gloss, and statuses are quoted
  from the register rather than restated.
- Scope decision: Russian, Mexican and Japanese members of the same families, industrial designs,
  and trademarks are deliberately excluded.

## Interviews

Public interviews and profiles live under `interviews/`, indexed by the table in
`interviews/README.md`, one folder per conversation named `<year>-<outlet>-<slug>/`.

Rules:

- **Primary sources, not contributions.** Interviews are outside the papers citation
  graph: they use **"See also"** links only, never `Builds on`/`Cited by`, and they are
  never added to `tools/manifest.json`, `bibliography.bib`, or the mermaid graph.
- **Never re-host the original article.** Link to the outlet's URL as the version of
  record. Only an English translation prepared for this repository is committed here, as
  `english.md` (or `english.pdf`).
- **Print-only originals cite the issue, not a URL.** For a magazine feature with no public web
  version, give outlet, issue number, date and page range in place of a link (and never link a
  scan of the printed pages — that would re-host the article).
- **Third-party media stays out.** Photographs, infographics and other artwork belonging
  to the outlet or its illustrators are not reproduced, even when present in the
  translation source — this repository's CC BY 4.0 text license cannot be extended to
  them. Reference the original article instead, crediting the illustrator.
- **Corezoid's own slides inside an outlet's article are ours.** Where a publication illustrates
  an interview with diagrams the company supplied (credited to Corezoid, © corezoid.com), their
  wording may be transcribed as `slides.md` — diagram labels are not selectable text and are
  otherwise invisible to search and screen readers. Transcribe the wording; do not reproduce the
  images, and keep the surrounding interview linked, not copied.
- Every `english.md` opens with a provenance header: outlet, publication date, original
  title, original language, link to the original, and a note that the translation is
  unofficial and that copyright in the original belongs to the outlet.
- **Do not link a translation before the file exists.** `tools/check_links.py` fails the
  build on unresolvable relative links; rows awaiting a translation say
  *in preparation*, or link the outlet's own English version where one was published.
- Verify each original URL still resolves when editing the table; several outlets block
  automated fetches, so check with a browser user agent before concluding a link is dead.
- **Recorded conversations are linked, never transcribed.** Video and podcast appearances go in
  the `## Video and podcast` table with the recording as the source. Do not commit a transcript
  reconstructed from machine-generated captions: auto-captions arrive without punctuation and
  mis-hear exactly the terms that matter (in the 2020 Большая Рыба interview, "Corezoid" is
  absent from the Russian auto-captions and "Витязь" appears once against eight false
  positives). A quotation the speaker never said is worse than no transcript. Only a
  transcript checked against the recording by a person may be added, and then it is labelled
  as such.

## Press releases

Historical press releases and news items live under `press/`, one folder per item named
`<year>-<slug>/` (years vary — the section spans decades), indexed by the table in
`press/README.md`. They follow the same rules as interviews: outside the citation graph,
"See also" links only, never in `tools/manifest.json` or `bibliography.bib`; originals linked,
never re-hosted; only an `english.md` translation with a provenance header is committed.
Historical URLs quoted inside a release (e.g. a 2001 Privat24 address) are preserved as
published and are not expected to resolve.

## Announcements are not works

Corezoid's blog announces some papers under its own editorial headline — *The Science of
Effective Control* is the blog's title for *On the Necessity of Noise Suppression for Minimal
Good Regulators*. Such a headline is not a separate work: link it from the paper's `## Links`
section as a plain-language announcement, and never create a folder, citekey, or bibliography
entry for it. When a title appears in a tracker or a content plan with no DOI and no PDF, check
the blog before treating it as a missing publication.

## Metadata rules

- One human-authored source of truth: the paper's front matter + root `CITATION.cff`. Everything else (BibTeX, badges) is derived from it.
- **Never add a `.zenodo.json`** next to `CITATION.cff` — Zenodo silently ignores `CITATION.cff` when `.zenodo.json` is present.
- ORCID format differs by file: full URL in `CITATION.cff` (`https://orcid.org/…`), bare digits elsewhere.
- BibTeX entries use `@misc` with `publisher = {Zenodo}` and the version DOI, matching Zenodo's own export.
