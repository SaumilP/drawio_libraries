# Draw.io Architecture Libraries

Reusable **draw.io / diagrams.net libraries** for creating **clean, consistent, and professional architecture diagrams**.

This repository provides curated symbol libraries for **system design, cloud architecture, DevOps, and security diagrams**, optimized for clarity, reuse, and documentation quality.

---

## 🎯 Purpose

Architectural diagrams often fail due to:

- inconsistent symbols
- visual clutter
- lack of shared semantics

This project solves that by offering **standardized, reusable libraries** that help teams produce diagrams that are:

- easier to read
- easier to maintain
- easier to review

---

## 📚 Library Catalog

A visual catalog with descriptions and previews is available here:

👉 **[CATALOG.md](./CATALOG.md)**

Each library is independently usable and versioned.

---

## 📦 Included Libraries

| Library              | Description                                                |
|----------------------|------------------------------------------------------------|
| **Azure**            | Azure icons (Containers,                                   |
| **Databases**        | Containers, Kubernetes, ingress, service mesh components   |
| **Developer Topols** | CI/CD pipelines, artifact registries, environments         |
| **Hashicorp Icons**  | C4-style components, boundaries, flows                     |
| **Power BI**         | IAM, trust boundaries, firewalls, access controls          |
| **Integrations**     | Security concepts, controls, monitoring, incident response |

> Libraries are intentionally **minimal and semantic** rather than exhaustive icon packs.

---

## 🚀 How to Use

### Option 1: Load a single library
1. Open **draw.io / diagrams.net**
2. Go to **File → Open Library from → Device**
3. Select the `.xml` library file
4. Drag symbols into your diagram

### Option 2: Use a release pack (recommended)
1. Download a release ZIP from **GitHub Releases**
2. Extract the libraries
3. Import one or more `.xml` files into draw.io

---

## 🧭 Design Principles

These libraries follow a few strict rules:

- **Architecture first** — symbols represent concepts, not vendors
- **Consistent sizing** — predictable alignment and spacing
- **Low visual noise** — diagrams stay readable at scale
- **Print & dark-mode friendly**
- **Tool-agnostic semantics** (works beyond draw.io)

---

## 🧩 Typical Use Cases

- System architecture diagrams
- C4 (Context / Container / Component) diagrams
- Cloud and infrastructure design reviews
- DevOps and CI/CD flows
- Technical documentation and RFCs
- Architecture review boards (ARB) material

---

## 📦 Releases & Versioning

This repository publishes **versioned release packs**.

Each release:
- is tagged (e.g. `v1.0.0`)
- includes a downloadable ZIP
- contains stable library definitions

👉 See **GitHub Releases** for downloadable packs.

---

## 🤝 Contributing

Contributions are welcome, especially:
- new libraries with clear scope
- refinements to existing symbols
- visual consistency improvements
- documentation and examples

**Contribution guidelines:**
1. Keep symbols **semantic**, not vendor-marketing heavy
2. Avoid duplicating icons with different names
3. Prefer fewer, clearer symbols over large icon sets
4. Include a short description for catalog inclusion

---

## 🛣 Roadmap

- [ ] Expand catalog previews
- [ ] Add more C4-aligned symbols
- [ ] Add example diagrams per library
- [ ] Provide light/dark theme variants
- [ ] Improve cross-library consistency

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## ⭐ Why This Repo Exists

Good diagrams are a **force multiplier** for engineering teams.

This repository exists to make **clear architecture diagrams the default, not the exception**.
