#!/usr/bin/env python3
"""Check that every relative markdown link in the repo resolves to a real file/dir.

Usage: check_links.py [repo_root]   (default: current directory)
Exit code 0 = all links resolve, 1 = broken links found.
"""
import os
import re
import sys
import urllib.parse

root = sys.argv[1] if len(sys.argv) > 1 else "."
bad = 0
for dirpath, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d != ".git"]
    for fn in files:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(dirpath, fn)
        text = open(path, encoding="utf-8").read()
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", text):
            link = m.group(1)
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = urllib.parse.unquote(link.split("#")[0])
            tp = os.path.normpath(os.path.join(dirpath, target))
            if not os.path.exists(tp):
                print(f"BROKEN {path}: {link}")
                bad += 1
print(f"broken links: {bad}")
sys.exit(1 if bad else 0)
