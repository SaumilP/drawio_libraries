#!/usr/bin/env python3
"""
Validate every draw.io library file in libraries/*.xml:
  - the outer <mxlibrary>...</mxlibrary> wrapper contains valid JSON
  - each shape entry decodes to well-formed XML (compressed "xml" entries,
    or plain "data" data-URI entries)
  - every screenshot referenced from README.md / CATALOG.md exists on disk

Usage:
  python3 tools/validate_libraries.py [--libs-dir libraries] [--screenshots-dir screenshots]
"""

from __future__ import annotations

import argparse
import base64
import glob
import json
import os
import re
import sys
import urllib.parse
import zlib
import xml.etree.ElementTree as ET


def decode_compressed_entry(xml_b64: str) -> str:
    raw = base64.b64decode(xml_b64)
    dec = zlib.decompressobj(-15)
    data = dec.decompress(raw) + dec.flush()
    return urllib.parse.unquote(data.decode("utf-8"))


def decode_xml_entry(xml_field: str) -> str:
    """The 'xml' field is usually base64(raw-deflate(percent-encoded XML)), but a
    few libraries store it as plain HTML-escaped XML instead (no compression)."""
    stripped = xml_field.strip()
    if stripped.startswith("&lt;") or stripped.startswith("<"):
        import html
        return html.unescape(xml_field)
    return decode_compressed_entry(xml_field)


def validate_library_file(path: str) -> list[str]:
    errors = []
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("<mxlibrary"):
        return [f"{path}: does not start with <mxlibrary"]
    if not content.rstrip().endswith("</mxlibrary>"):
        return [f"{path}: does not end with </mxlibrary>"]

    try:
        start = content.index(">") + 1
        end = content.rindex("</mxlibrary>")
        entries = json.loads(content[start:end])
    except (ValueError, json.JSONDecodeError) as e:
        return [f"{path}: outer JSON payload is invalid: {e}"]

    if not isinstance(entries, list) or len(entries) == 0:
        return [f"{path}: expected a non-empty JSON array of shape entries"]

    for i, entry in enumerate(entries):
        title = entry.get("title", f"<entry {i}>")
        if "xml" in entry:
            try:
                decoded = decode_xml_entry(entry["xml"])
                ET.fromstring(decoded)
            except Exception as e:
                errors.append(f"{path}: entry '{title}' has invalid/undecodable xml: {e}")
        elif "data" in entry:
            data_val = entry["data"]
            if not (data_val.startswith("data:image/") or data_val.startswith("http://") or data_val.startswith("https://")):
                errors.append(f"{path}: entry '{title}' has a 'data' field that's neither an image data URI nor a URL")
        else:
            errors.append(f"{path}: entry '{title}' has neither 'xml' nor 'data' field")

    return errors


def validate_referenced_screenshots(repo_root: str) -> list[str]:
    errors = []
    for doc in ("README.md", "CATALOG.md"):
        doc_path = os.path.join(repo_root, doc)
        if not os.path.exists(doc_path):
            continue
        with open(doc_path, "r", encoding="utf-8") as f:
            text = f.read()
        for match in re.finditer(r"!\[[^\]]*\]\((screenshots/[^)]+)\)", text):
            rel_path = match.group(1)
            if not os.path.exists(os.path.join(repo_root, rel_path)):
                errors.append(f"{doc}: references missing screenshot {rel_path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--libs-dir", default="libraries")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    all_errors = []
    lib_files = sorted(glob.glob(os.path.join(args.libs_dir, "*.xml")))
    if not lib_files:
        print(f"No library files found in {args.libs_dir}", file=sys.stderr)
        return 1

    for path in lib_files:
        all_errors.extend(validate_library_file(path))

    all_errors.extend(validate_referenced_screenshots(args.repo_root))

    if all_errors:
        print(f"Validation FAILED ({len(all_errors)} issue(s)):\n")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(f"Validation OK: {len(lib_files)} library files, all entries well-formed, all referenced screenshots present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
