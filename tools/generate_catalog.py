#!/usr/bin/env python3
"""
Generate CATALOG.md from draw.io / diagrams.net library XML files.

Usage:
  python3 tools/generate_catalog.py --libs-dir libraries --screenshots-dir screenshots --out CATALOG.md
"""

from __future__ import annotations

import argparse
import os
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class LibInfo:
    file_path: str
    rel_path: str
    name: str
    shape_count: int
    notes: str


def safe_title_from_filename(path: str) -> str:
    base = os.path.basename(path)
    name = os.path.splitext(base)[0]
    name = name.replace("_", " ").replace("-", " ").strip()
    return " ".join(w.capitalize() for w in name.split())


def extract_library_name(root: ET.Element, fallback: str) -> str:
    """
    draw.io library XML formats vary.
    We attempt common patterns and fall back to filename-based title.
    """
    # Try attributes on root
    for attr in ("title", "name", "id"):
        v = root.attrib.get(attr)
        if v and len(v.strip()) > 2:
            return v.strip()

    # Try a <mxlibrary> element (common in draw.io libraries)
    mxlib = root.find(".//mxlibrary")
    if mxlib is not None:
        for attr in ("title", "name"):
            v = mxlib.attrib.get(attr)
            if v and len(v.strip()) > 2:
                return v.strip()

    # Try <Library> or other nodes with name/title
    for tag in ("Library", "library"):
        node = root.find(f".//{tag}")
        if node is not None:
            v = node.attrib.get("name") or node.attrib.get("title")
            if v and len(v.strip()) > 2:
                return v.strip()

    return fallback


def count_shapes(root: ET.Element) -> int:
    """
    Count likely 'shape entries'. There isn't a single standard across all libraries.
    We count a mix of common markers:
      - <shape> tags
      - <mxCell> entries with 'value' and 'style' (heuristic)
      - <diagram> entries (rare in library packs)
      - <entry> items
    """
    # Strong signals
    shape_tags = root.findall(".//shape")
    entry_tags = root.findall(".//entry")

    # Heuristic: mxCell nodes that look like library items
    mx_cells = root.findall(".//mxCell")
    mx_like = 0
    for c in mx_cells:
        style = c.attrib.get("style", "")
        value = c.attrib.get("value", "")
        if style and (value or "shape=" in style or "image=" in style):
            mx_like += 1

    # Prefer explicit tags if present; otherwise use heuristic
    if len(shape_tags) > 0:
        return len(shape_tags)
    if len(entry_tags) > 0:
        return len(entry_tags)
    if mx_like > 0:
        return mx_like
    return len(mx_cells)


def read_xml(path: str) -> ET.Element:
    # Some draw.io exports contain invalid control characters; strip them if necessary.
    with open(path, "rb") as f:
        raw = f.read()
    # Remove ASCII control chars except \t \n \r
    raw = re.sub(rb"[\x00-\x08\x0b\x0c\x0e-\x1f]", b"", raw)
    return ET.fromstring(raw)


def discover_xml_files(libs_dir: str) -> List[str]:
    xmls = []
    if os.path.isdir(libs_dir):
        for fn in sorted(os.listdir(libs_dir)):
            if fn.lower().endswith(".xml"):
                xmls.append(os.path.join(libs_dir, fn))
    return xmls


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--libs-dir", default="libraries", help="Directory containing .xml libraries")
    ap.add_argument("--screenshots-dir", default="screenshots", help="Screenshots directory for previews")
    ap.add_argument("--out", default="CATALOG.md", help="Output catalog markdown file")
    args = ap.parse_args()

    xml_files = discover_xml_files(args.libs_dir)
    if not xml_files:
        raise SystemExit(f"No .xml files found under: {args.libs_dir}")

    libs: List[LibInfo] = []
    for fp in xml_files:
        fallback = safe_title_from_filename(fp)
        try:
            root = read_xml(fp)
            name = extract_library_name(root, fallback)
            shapes = count_shapes(root)
            notes = "Placeholder: add a 1–2 line description of this library’s intent and scope."
        except Exception as e:
            name = fallback
            shapes = 0
            notes = f"Could not parse XML cleanly ({e}). Validate file and regenerate."
        rel = os.path.join(args.libs_dir, os.path.basename(fp))
        libs.append(LibInfo(file_path=fp, rel_path=rel, name=name, shape_count=shapes, notes=notes))

    # Write catalog
    out_lines = []
    out_lines.append("# Draw.io Architecture Libraries — Catalog\n")
    out_lines.append(
        "This catalog is generated from the `.xml` library files present in this repository.\n"
        "Update descriptions and screenshots as you polish the libraries.\n"
    )

    out_lines.append("## 📦 Available Libraries\n")
    out_lines.append("| Library | File | Items | Preview | Notes |\n")
    out_lines.append("|---|---|---:|---|---|\n")

    for lib in libs:
        screenshot_name = os.path.splitext(os.path.basename(lib.rel_path))[0] + ".png"
        screenshot_path = os.path.join(args.screenshots_dir, screenshot_name).replace("\\", "/")
        preview_md = f"![]({screenshot_path})"
        out_lines.append(
            f"| **{lib.name}** | `{lib.rel_path}` | {lib.shape_count} | {preview_md} | {lib.notes} |\n"
        )

    out_lines.append("\n---\n")
    out_lines.append("## 🚀 How to Use\n")
    out_lines.append("1. Open **draw.io / diagrams.net**\n")
    out_lines.append("2. **File → Open Library from → Device**\n")
    out_lines.append("3. Select any `.xml` file under `libraries/`\n")
    out_lines.append("4. Drag symbols into your diagram\n\n")

    out_lines.append("## 📸 Screenshot naming convention\n")
    out_lines.append(
        "For each library `libraries/<name>.xml`, add a screenshot at:\n\n"
        "```\n"
        "screenshots/<name>.png\n"
        "```\n\n"
        "This keeps previews stable and makes the catalog render correctly.\n"
    )

    with open(args.out, "w", encoding="utf-8") as f:
        f.writelines(out_lines)

    print(f"Wrote {args.out} with {len(libs)} libraries.")


if __name__ == "__main__":
    main()
