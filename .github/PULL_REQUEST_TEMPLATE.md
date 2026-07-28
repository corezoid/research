<!-- For publishing a new paper (or a new version), complete the checklist. See PUBLISHING.md for the full workflow. -->

## Paper

- **Title:**
- **Version:** v1
- **Zenodo DOI:**

## Checklist

- [ ] `papers/<year>-<slug>/` follows the standard layout (`README.md`, `paper.pdf`, `paper.md`, `CHANGELOG.md`)
- [ ] `paper.pdf` is byte-identical to the Zenodo deposit
- [ ] `paper.md` front matter: title, author + ORCID, date, doi, keywords, abstract, version
- [ ] Paper `README.md` has: abstract, DOI badge, **How to cite** (formatted + BibTeX), links (Zenodo, distribution channels), **Related work** cross-links
- [ ] Root `README.md` index table updated (and citation graph, if this paper cites earlier ones)
- [ ] `bibliography.bib` entry added
- [ ] **Related work** sections of cited papers updated with a back-link
- [ ] Language is English or Ukrainian
- [ ] No files from local `raw/` sources committed as-is (normalized names/formats only)
- [ ] After merge: tag `papers/<slug>/vN` + GitHub Release
