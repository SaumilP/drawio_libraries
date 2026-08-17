# Contributing

Contributions are welcome, especially:

- new libraries with a clear, narrow scope
- refinements to existing symbols
- visual consistency improvements
- documentation and examples

## Guidelines

1. Keep symbols **semantic**, not vendor-marketing heavy — architecture first, symbols represent concepts, not logos.
2. Avoid duplicating icons with different names across libraries.
3. Prefer fewer, clearer symbols over large, unfocused icon sets.
4. Match the naming and sizing conventions already used in the target library.
5. Don't redistribute trademarked vendor icon artwork without a clear license to do so. For cloud provider icons, follow the pattern in `aws-services.xml` / `gcp-services.xml`: original, non-trademarked pictograms rather than copies of a vendor's official artwork.

## Adding a new library

1. Build the library in draw.io / diagrams.net and export it as an `.xml` library file into `libraries/`, using kebab-case for the filename (e.g. `my-new-library.xml`).
2. Add a preview screenshot to `screenshots/` with the same base filename.
3. Add a row to the table in `README.md` and a full entry in `CATALOG.md` (see existing entries for the expected format). `tools/generate_catalog.py` can generate a starting point, but most of the descriptive text in `CATALOG.md` is written and maintained by hand — see `tools/HELP.md`.
4. Run `python3 tools/generate_gallery_data.py` to regenerate `docs/gallery-data.json` from the new README row, so the [live gallery](https://saumilp.github.io/drawio_libraries/) picks up the new library. Commit the updated JSON along with your other changes.
5. Open the library in draw.io (**File → Open Library from → Device**) to confirm it loads and every shape renders correctly before opening a PR.

## Reporting issues

Use the issue templates for bug reports and new library requests. For anything else, a blank issue is fine.

## Code of Conduct

This project follows the [Code of Conduct](./CODE_OF_CONDUCT.md).
