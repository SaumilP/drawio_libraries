# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project uses tagged releases (see [GitHub Releases](https://github.com/SaumilP/drawio_libraries/releases))
rather than strict semantic versioning.

## [Unreleased]

### Added
- `libraries/aws-services.xml` and `libraries/aws-services-3d.xml` — 28 original AWS service icons (not AWS's trademarked artwork), in flat and gradient/shadow 3D styles.
- `libraries/gcp-services.xml` and `libraries/gcp-services-3d.xml` — 28 original Google Cloud service icons, same treatment.
- `libraries/c4-model.xml` — standard C4 notation shapes (Person, Software System, Container, Component, boundaries) in internal/external variants.
- Real, non-empty example diagrams in `examples/` built from this repo's own libraries.
- `docs/dfd_doc.md` — a proper guide to the two Data Flow Diagram libraries.
- `.github/` community health files: issue templates, PR template, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- `tools/validate_libraries.py` and a CI workflow that validates every library file's XML integrity on push/PR.
- README badges (release, license, last commit, issues).

### Changed
- Clarified the `README.md`/`CATALOG.md` descriptions for `integration.xml` vs `integration-patterns.xml` and `custom-azure.xml` vs `azure-additional-or-support.xml`, which previously read as near-identical.

### Fixed
- `docs/` was tracked as `Docs/` in git, a case-sensitivity mismatch invisible on case-insensitive filesystems (macOS/Windows) but broken on GitHub's case-sensitive storage.

### Removed
- `libraries/DataFlowDiagram_Limited_Shapes.drawio` — an undocumented, near-duplicate of `libraries/DataFlowDiagram_Shapes.xml` under a confusing filename.

## [1.0.0] - 2026-01-25

Initial architecture library release.

### Added
- 27 draw.io/diagrams.net shape libraries covering cloud architecture, DevOps, integration, data flow, and general design symbols.
- `CATALOG.md` with previews and descriptions for every library.
- `tools/generate_catalog.py` to help regenerate catalog scaffolding.
