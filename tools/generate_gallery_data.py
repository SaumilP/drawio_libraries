#!/usr/bin/env python3
"""
Generate docs/gallery-data.json for the GitHub Pages gallery (docs/index.html)
from the "Included Libraries" table in README.md plus shape counts read
directly from libraries/*.xml.

README.md's table is the single source of truth for the name/file/screenshot/
notes mapping (screenshot filenames don't always match the library's
filename, e.g. `power-bi.xml` -> `screenshots/powerbi.png`), so this script
parses it rather than re-deriving that mapping.

Usage:
  python3 tools/generate_gallery_data.py [--readme README.md] [--libs-dir libraries] [--out docs/gallery-data.json]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import xml.etree.ElementTree as ET

REPO = "SaumilP/drawio_libraries"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"
BLOB_BASE = f"https://github.com/{REPO}/blob/{BRANCH}"

ROW_RE = re.compile(
    r"\|\s*\*\*(?P<name>[^*]+)\*\*\s*\|\s*`(?P<file>[^`]+)`\s*\|\s*!\[\]\((?P<screenshot>[^)]+)\)\s*\|\s*(?P<notes>.+?)\s*\|\s*$"
)

# filename keyword -> category, checked in order, first match wins
CATEGORY_RULES = [
    (("aws", "azure", "gcp", "custom-azure"), "Cloud Providers"),
    (
        (
            "build_pipeline",
            "devops",
            "kubernetes",
            "hashicorp",
            "developer-tools",
        ),
        "DevOps & CI/CD",
    ),
    (("dataflow", "integration"), "Data Flow & Integration"),
    (("c4-model",), "Architecture Notation"),
    (("office365", "power-bi", "powerapps"), "Microsoft 365 & Power Platform"),
]
DEFAULT_CATEGORY = "General & Design"


def categorize(file_path: str) -> str:
    lowered = file_path.lower()
    for keywords, category in CATEGORY_RULES:
        if any(k in lowered for k in keywords):
            return category
    return DEFAULT_CATEGORY


def read_xml(path: str) -> ET.Element:
    with open(path, "rb") as f:
        raw = f.read()
    raw = re.sub(rb"[\x00-\x08\x0b\x0c\x0e-\x1f]", b"", raw)
    return ET.fromstring(raw)


def count_shapes(path: str) -> int:
    """Count entries in the <mxlibrary> JSON payload; this is the format
    every library file in this repo actually uses."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    try:
        start = content.index(">") + 1
        end = content.rindex("</mxlibrary>")
        entries = json.loads(content[start:end])
        if isinstance(entries, list):
            return len(entries)
    except (ValueError, json.JSONDecodeError):
        pass
    return 0


def parse_readme_table(readme_path: str) -> list[dict]:
    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    rows = []
    in_table = False
    for line in lines:
        if line.strip().startswith("## 📦 Included Libraries"):
            in_table = True
            continue
        if in_table and line.strip() == "---":
            break
        if not in_table:
            continue
        m = ROW_RE.match(line.strip())
        if m:
            rows.append(m.groupdict())
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--libs-dir", default="libraries")
    ap.add_argument("--out", default="docs/gallery-data.json")
    args = ap.parse_args()

    rows = parse_readme_table(args.readme)
    if not rows:
        raise SystemExit("No library rows found in README.md — did the table format change?")

    items = []
    for row in rows:
        file_rel = row["file"].strip()
        file_abs = file_rel
        shape_count = count_shapes(file_abs) if os.path.exists(file_abs) else 0

        items.append(
            {
                "name": row["name"].strip(),
                "file": file_rel,
                "category": categorize(file_rel),
                "shapeCount": shape_count,
                "notes": row["notes"].strip(),
                "screenshot": f"{RAW_BASE}/{row['screenshot'].strip()}",
                "downloadUrl": f"{RAW_BASE}/{file_rel}",
                "sourceUrl": f"{BLOB_BASE}/{file_rel}",
            }
        )

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)
        f.write("\n")

    print(f"Wrote {args.out} with {len(items)} libraries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
