# Help

Python script can be used to generate CATALOG.md file but with basic information. Most of the details into CATALOG.md must be retained without changes.

## Howto(s)

### Generate Catalog from library XML files

```bash
python3 tools/generate_catalog.py --libs-dir libraries --screenshots-dir screenshots --out CATALOG-tmp.md
```

### Validate library files before opening a PR

Checks that every `libraries/*.xml` file is well-formed (outer JSON payload, every
shape entry decodes cleanly) and that every screenshot referenced from README.md /
CATALOG.md exists on disk. This is the same check CI runs on every push and PR.

```bash
python3 tools/validate_libraries.py
```
