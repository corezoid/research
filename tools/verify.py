#!/usr/bin/env python3
"""Verify the corpus invariants against tools/manifest.json.

Checks:
  1. coverage    — every paper folder is in the manifest and vice versa
  2. files       — required files exist (README, PDF, CHANGELOG; paper.md iff has_md)
  3. checksums   — paper.pdf md5 equals the Zenodo deposit checksum (API); a
                   'known_mismatch' entry downgrades failure to a warning
  4. dois        — every DOI in the manifest resolves via doi.org
  5. bibtex      — the ```bibtex block in each paper README equals the
                   bibliography.bib entry for its citekey (whitespace-normalized)
  6. graph       — mermaid citation edges in the root README correspond 1:1 to
                   'Builds on'/'Cited by' relations in paper READMEs ('See also'
                   marks indirect relations and is ignored)

Usage: verify.py [--offline]   (--offline skips checks 3 and 4)
Exit code: 0 ok (warnings allowed), 1 any failure.
"""
import hashlib
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFFLINE = "--offline" in sys.argv
FAIL, WARN = [], []


def fail(msg):
    FAIL.append(msg)
    print(f"FAIL  {msg}")


def warn(msg):
    WARN.append(msg)
    print(f"WARN  {msg}")


def ok(msg):
    print(f"ok    {msg}")


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "corezoid-research-verify"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def head_status(url):
    """Status of the FIRST response only — a 30x from doi.org already proves the
    DOI resolves, and following the redirect (e.g. into ResearchGate's bot wall,
    which stalls connections) is both slow and irrelevant."""
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "corezoid-research-verify"})
    try:
        with _opener.open(req, timeout=15) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"network-error: {e}"


_m = json.load(open(os.path.join(ROOT, "tools/manifest.json")))
manifest = _m["papers"]
patents = _m.get("patents", [])
by_path = {p["path"]: p for p in manifest}

# 1. coverage: find every dir under papers/ that holds a paper artifact
found = set()
for dirpath, dirs, files in os.walk(os.path.join(ROOT, "papers")):
    if "paper.pdf" in files or "volume.pdf" in files:
        found.add(os.path.relpath(dirpath, ROOT))
for path in sorted(found - set(by_path)):
    fail(f"coverage: {path} exists but is not in tools/manifest.json")
for path in sorted(set(by_path) - found):
    fail(f"coverage: {path} is in the manifest but has no PDF on disk")
if found == set(by_path):
    ok(f"coverage: {len(found)} paper folders match the manifest")

# 2. files
for p in manifest:
    d = os.path.join(ROOT, p["path"])
    required = ["README.md", p["pdf"], "CHANGELOG.md"]
    missing = [f for f in required if not os.path.exists(os.path.join(d, f))]
    if missing:
        fail(f"files: {p['path']} missing {missing}")
    has_md = os.path.exists(os.path.join(d, "paper.md"))
    if has_md != p["has_md"]:
        fail(f"files: {p['path']} paper.md present={has_md}, manifest says has_md={p['has_md']}")
ok("files: layout checked")

# 3. checksums vs Zenodo
if not OFFLINE:
    for p in manifest:
        if not p.get("zenodo_id"):
            continue
        local = os.path.join(ROOT, p["path"], p["pdf"])
        lmd5 = hashlib.md5(open(local, "rb").read()).hexdigest()
        try:
            rec = fetch_json(f"https://zenodo.org/api/records/{p['zenodo_id']}")
            zmd5 = rec["files"][0]["checksum"].replace("md5:", "")
        except Exception as e:  # network flakiness must not hard-fail CI
            warn(f"checksum: {p['path']} — Zenodo API unreachable ({e})")
            continue
        if lmd5 == zmd5:
            ok(f"checksum: {p['path']} identical to Zenodo deposit")
        elif p.get("known_mismatch"):
            warn(f"checksum: {p['path']} differs from Zenodo (known: {p['known_mismatch'][:60]}…)")
        else:
            fail(f"checksum: {p['path']} md5 {lmd5} != Zenodo {zmd5}")

# 4. DOI resolution
if not OFFLINE:
    for p in manifest:
        if not p.get("doi"):
            continue
        code = head_status(f"https://doi.org/{p['doi']}")
        if code in (200, 301, 302, 303):
            ok(f"doi: {p['doi']} resolves ({code})")
        elif isinstance(code, str):  # transient network problem must not hard-fail CI
            warn(f"doi: {p['doi']} check inconclusive ({code})")
        else:
            fail(f"doi: {p['doi']} returned {code}")

# 5. bibtex blocks match bibliography.bib
bib = open(os.path.join(ROOT, "bibliography.bib"), encoding="utf-8").read()


def bib_entry(citekey):
    m = re.search(r"@\w+\{" + re.escape(citekey) + r",.*?\n\}", bib, re.S)
    return m.group(0) if m else None


def norm(s):
    return "\n".join(line.strip() for line in s.strip().splitlines() if line.strip())


for p in manifest:
    readme = open(os.path.join(ROOT, p["path"], "README.md"), encoding="utf-8").read()
    m = re.search(r"```bibtex\n(.*?)```", readme, re.S)
    entry = bib_entry(p["citekey"])
    if not entry:
        fail(f"bibtex: {p['citekey']} not found in bibliography.bib")
        continue
    if not m:
        fail(f"bibtex: {p['path']}/README.md has no ```bibtex block")
        continue
    if norm(m.group(1)) != norm(entry):
        fail(f"bibtex: {p['path']} README block differs from bibliography.bib entry {p['citekey']}")
    else:
        ok(f"bibtex: {p['path']} in sync")

# 5b. patents: coverage, files, bibtex sync, no graph-relation wording
pat_by_path = {p["path"]: p for p in patents}
pat_found = set()
patents_root = os.path.join(ROOT, "patents")
if os.path.isdir(patents_root):
    for dirpath, dirs, files in os.walk(patents_root):
        if "patent.pdf" in files:
            pat_found.add(os.path.relpath(dirpath, ROOT))
for path in sorted(pat_found - set(pat_by_path)):
    fail(f"patents: {path} exists but is not in tools/manifest.json")
for path in sorted(set(pat_by_path) - pat_found):
    fail(f"patents: {path} is in the manifest but has no patent.pdf on disk")
for p in patents:
    d = os.path.join(ROOT, p["path"])
    if not os.path.exists(os.path.join(d, "README.md")):
        fail(f"patents: {p['path']} missing README.md")
        continue
    readme = open(os.path.join(d, "README.md"), encoding="utf-8").read()
    if re.search(r"-\s*\*{0,2}(Builds on|Cited by)", readme):
        fail(f"patents: {p['path']} uses 'Builds on/Cited by' — patents must use 'See also' (they are outside the papers citation graph)")
if patents and pat_found == set(pat_by_path):
    ok(f"patents: {len(patents)} patent folders match the manifest")

for p in patents:
    d = os.path.join(ROOT, p["path"])
    if not os.path.exists(os.path.join(d, "README.md")):
        continue
    readme = open(os.path.join(d, "README.md"), encoding="utf-8").read()
    m = re.search(r"```bibtex\n(.*?)```", readme, re.S)
    entry = bib_entry(p["citekey"])
    if not entry:
        fail(f"patents bibtex: {p['citekey']} not found in bibliography.bib")
    elif not m:
        fail(f"patents bibtex: {p['path']}/README.md has no ```bibtex block")
    elif norm(m.group(1)) != norm(entry):
        fail(f"patents bibtex: {p['path']} README block differs from bibliography.bib entry {p['citekey']}")
    else:
        ok(f"patents bibtex: {p['path']} in sync")

# 6. citation graph <-> Related work
root_readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
gm = re.search(r"```mermaid\n(.*?)```", root_readme, re.S)
edges = set(re.findall(r"(\w+)\s*-->\|cites\|\s*(\w+)", gm.group(1))) if gm else set()
node_of = {p["path"]: p["node"] for p in manifest if p["node"]}
path_of_node = {v: k for k, v in node_of.items()}

# relations declared in paper READMEs (series container README is a summary, skip it)
declared = set()  # (citing_node, cited_node)
for p in manifest:
    if p.get("series") or not p["node"]:
        continue
    readme = open(os.path.join(ROOT, p["path"], "README.md"), encoding="utf-8").read()
    for line in readme.splitlines():
        ls = line.strip()
        if ls.lower().startswith("- **see also**") or ls.lower().startswith("- see also"):
            continue
        links = re.findall(r"\]\((\.\./[^)#]+?)/?\)", ls)
        for link in links:
            target = os.path.normpath(os.path.join(p["path"], link))
            if target not in node_of:
                continue
            if re.match(r"-\s*\*{0,2}Builds on", ls):
                declared.add((p["node"], node_of[target]))
            elif re.match(r"-\s*\*{0,2}Cited by", ls):
                declared.add((node_of[target], p["node"]))

for e in sorted(edges - declared):
    fail(f"graph: mermaid edge {e[0]}→{e[1]} has no matching Builds-on/Cited-by line in {path_of_node.get(e[0], e[0])}")
for e in sorted(declared - edges):
    fail(f"graph: relation {e[0]}→{e[1]} declared in READMEs but missing from the mermaid graph")
if edges and edges == declared:
    ok(f"graph: {len(edges)} edges consistent with Related-work sections")

print(f"\n{len(FAIL)} failure(s), {len(WARN)} warning(s)")
sys.exit(1 if FAIL else 0)
