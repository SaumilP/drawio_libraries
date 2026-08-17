# Draw.io Architecture Libraries — Catalog

This catalog is generated from the `.xml` library files present in this repository.
Update descriptions and screenshots as you polish the libraries.

## 📦 Available Libraries

### Build Pipeline Shapes

**Description**

Symbols for modeling build and CI/CD pipelines, focusing on stages, transitions, and execution flow rather than specific tooling.

**Concise notes**

- Ideal for CI/CD and DevOps diagrams
- Emphasizes flow and sequencing
- Tool-agnostic representation

---

### Dataflowdiagram Limited Shapes

**Description**

A minimal set of symbols for expressing data flows between systems, optimized for clarity in high-level diagrams.

**Concise notes**

- Reduced symbol set for simplicity
- Best for executive or overview diagrams
- Avoids visual clutter

---

### Dataflowdiagram Shapes

**Description**

A richer collection of data-flow symbols allowing more detailed representation of data movement, transformation, and storage.

**Concise notes**

- More expressive than the limited set
- Suitable for technical deep dives
- Useful for ETL and integration flows

---

### Additional Or Support

**Description**

Generic support symbols that complement other libraries, filling common gaps in architectural and design diagrams.

**Concise notes**

- Auxiliary shapes
- Use alongside primary libraries
- Not domain-specific

---

### AI Machine Learning

**Description**

Icons representing common AI and machine learning concepts, pipelines, and components used in modern intelligent systems.

**Concise notes**

- Conceptual AI/ML components
- Suitable for solution overviews
- Avoids model-specific detail

---

### Any Others

**Description**

A collection of uncategorized or experimental shapes that do not yet belong to a dedicated library.

**Concise notes**

- Catch-all category
- Review before reuse
- Candidates for future reclassification

---

### Apache Software Foundation Logos

**Description**

Official and commonly used logos for Apache Software Foundation projects, useful for open-source and platform diagrams.

**Concise notes**

- Product identification only
- Not architectural primitives
- Best used sparingly

---

### Apps And Logos

**Description**

A mixed set of application and tool logos intended to visually identify external systems or platforms in diagrams.

**Concise notes**

- Logo-centric
- Useful for context diagrams
- Avoid overuse in design-heavy views

---

### Aws Services

**Description**

Original hand-drawn pictogram icons covering 28 of the most commonly diagrammed AWS services across seven categories: Compute, Storage, Database, Networking, Security, Messaging & Integration, and Observability. Each icon is a simple, generic concept glyph (a cylinder for a database, a key for IAM, a bucket for S3, and so on) on a category-colored badge — not a reproduction of AWS's trademarked icon artwork. draw.io already ships the official AWS Architecture Icons built in (File → More Shapes → AWS) for that.

**Concise notes**

- Original glyphs and category color-coding, not vendor pictograms
- Complements, not replaces, draw.io's built-in AWS icon set
- Good for quick, semantic AWS architecture sketches

---

### Aws Services (3D)

**Description**

The same 28 icons and titles as `aws-services.xml`, restyled with a gradient-filled badge, a soft drop shadow, a glossy top highlight, and a subtle embossed glyph shadow for a raised, dimensional look. Pick this library instead of the flat one when a diagram calls for a more polished, presentation-style visual treatment.

**Concise notes**

- Same service names/tags as `aws-services.xml` — pick one style per diagram
- Gradient + shadow + gloss, no external image dependencies
- Still original artwork, not AWS's trademarked icons

---

### Azure Additional Or Support

**Description**

A smaller (79-shape) supplementary Azure pack covering adjacent concepts not in `custom-azure.xml` — automation, migration, containers, cloud adoption, and similar. Use alongside Custom Azure, not instead of it.

**Concise notes**

- Azure-specific extensions
- Complements `custom-azure.xml`, doesn't replace it
- Use for clarity, not completeness

---

### Azure Services

**Description**

Original hand-drawn pictogram icons covering 28 of the most commonly diagrammed Azure services across the same seven categories as `aws-services.xml` and `gcp-services.xml` (Compute, Storage, Database, Networking, Security, Messaging & Integration, Observability), in a matching visual system with a distinct color palette. Reuses glyphs from the AWS/GCP sets where an Azure service is conceptually identical (a database is a cylinder, IAM/Entra ID is a key), and adds new glyphs for Azure-specific concepts (Blob Storage, App Service, Defender for Cloud, Event Hubs, Azure Advisor). Not a reproduction of Microsoft's trademarked icon artwork.

**Concise notes**

- Same visual system as `aws-services.xml` / `gcp-services.xml` for true multi-cloud consistency
- Distinct color palette so all three libraries stay visually distinguishable
- Complements `custom-azure.xml` (a different, non-original visual style) rather than replacing it

---

### Azure Services (3D)

**Description**

The same 28 icons and titles as `azure-services.xml`, restyled with a gradient-filled badge, a soft drop shadow, a glossy top highlight, and a subtle embossed glyph shadow for a raised, dimensional look — matching `aws-services-3d.xml` and `gcp-services-3d.xml`.

**Concise notes**

- Same service names/tags as `azure-services.xml` — pick one style per diagram
- Gradient + shadow + gloss, no external image dependencies
- Still original artwork, not Microsoft's trademarked icons

---

### Buildings

**Description**

Physical building and location symbols used to represent offices, data centers, or geographic context.

**Concise notes**

- Physical context modeling
- Useful in hybrid/on-prem diagrams
- Non-technical elements

---

### C4 Model

**Description**

Standard C4 notation shapes for Context, Container, and Component diagrams: Person, Software System, Container, Container: Database, and Component, each with an internal and an external (gray) variant, plus dashed System Boundary and Container Boundary containers. Follows the conventional C4 color scheme (Simon Brown's open notation) — darker blue for higher-level elements, lighter blue for lower-level ones, gray for anything outside the system being described.

**Concise notes**

- Covers Context, Container, and Component diagram levels
- Internal/external variants for every element type
- Labels use the standard `Name` / `[Type: Technology]` two-line format — edit the placeholder text after dragging onto the canvas

---

### Chart Icons

**Description**

Generic chart and visualization symbols for representing metrics, analytics, and reporting concepts.

**Concise notes**

- Abstract data visualization
- Not tied to specific tools
- Works well in dashboards

---

### Custom Azure

**Description**

The main, large (174-shape) Azure service icon pack, covering most core Azure services. Start here for Azure diagrams; see Azure Additional Or Support for a smaller set of supplementary shapes.

**Concise notes**

- The primary Azure library in this repo
- Useful for internal diagrams
- Validate consistency before reuse

---

### Kubernetes

**Description**

Custom Kubernetes icons representing clusters, workloads, and supporting components in container orchestration diagrams.

**Concise notes**

- Kubernetes-focused
- Suitable for platform diagrams
- Complements cloud-native libraries

---

### Databases

**Description**

Icons representing a variety of database technologies and storage concepts for system and data architecture diagrams.

**Concise notes**

- Technology-agnostic grouping
- Good for data layer views
- Mix of SQL and NoSQL concepts

---

### Delivery Icons

**Description**

Symbols related to delivery, distribution, and movement, often used in logistics or deployment-oriented diagrams.

**Concise notes**

- Conceptual delivery metaphors
- Useful for process flows
- Not infrastructure-specific

---

### Developer Tools

**Description**

Icons for common developer tools and platforms, used to illustrate tooling ecosystems and development workflows.

**Concise notes**

- Tool identification
- Best for ecosystem diagrams
- Avoid mixing with core architecture symbols

---

### Devices

**Description**

Icons representing physical and virtual devices such as desktops, mobile devices, and endpoints.

**Concise notes**

- Endpoint representation
- Useful in network diagrams
- Non-backend focused

---

### Devops Observability

**Description**

Original hand-drawn pictogram icons covering 28 cloud-native DevOps and observability tools across seven categories: Containers & Orchestration (Docker, Helm, Istio, Containerd), CI/CD (Jenkins, GitHub Actions, GitLab CI, ArgoCD), Config Management & IaC (Ansible, Pulumi, Chef, Puppet), Messaging & Streaming (Kafka, RabbitMQ, NATS, ZeroMQ), Observability (Prometheus, Grafana, Elasticsearch, Jaeger), Networking & Proxy (Nginx, HAProxy, Envoy, Traefik), and Testing & Quality (SonarQube, Selenium, JMeter, Postman). Doesn't overlap with `hashicorp-draw-io.xml` (Terraform/Vault/Consul/Nomad/Packer/Vagrant) or `databases.xml` (Postgres/MySQL/MongoDB/Redis). Not a reproduction of any tool's trademarked logo.

**Concise notes**

- Fills a real gap: `developer-tools.xml` is heavily Microsoft/.NET-flavored and doesn't cover this ecosystem
- Same visual system as the cloud provider libraries, own distinct color palette
- Original glyphs represent each tool's function, not its actual brand mark

---

### Devops Observability (3D)

**Description**

The same 28 icons and titles as `devops-observability.xml`, restyled with a gradient-filled badge, a soft drop shadow, a glossy top highlight, and a subtle embossed glyph shadow for a raised, dimensional look.

**Concise notes**

- Same tool names/tags as `devops-observability.xml` — pick one style per diagram
- Gradient + shadow + gloss, no external image dependencies
- Still original artwork, not the tools' trademarked logos

---

### Flat Color Icons

**Description**

A stylistically consistent set of flat-color icons for general illustration and visual enhancement.

**Concise notes**

- Visual consistency
- Not domain-specific
- Best for presentation diagrams

---

### Font Awesome

**Description**

A collection of commonly recognized Font Awesome icons adapted for use in draw.io diagrams.

**Concise notes**

- Familiar iconography
- Generic usage
- Avoid overuse in technical diagrams

---

### Gcp Services

**Description**

Original hand-drawn pictogram icons covering 28 of the most commonly diagrammed Google Cloud services across seven categories: Compute, Storage, Database, Networking, Security, Messaging & Integration, and Observability. Where a GCP service is conceptually identical to its AWS counterpart in `aws-services.xml` (a database is a cylinder, IAM is a key, regardless of vendor), the same glyph is reused; services with a genuinely distinct character (Firestore, Bigtable, Spanner, Cloud Functions, etc.) get their own icon. Uses a distinct color palette from `aws-services.xml` so the two libraries stay visually distinguishable — not a reproduction of Google's trademarked icon artwork.

**Concise notes**

- Original glyphs and category color-coding, not vendor pictograms
- Shares iconography with `aws-services.xml` where the underlying concept is the same
- Good for quick, semantic GCP architecture sketches

---

### Gcp Services (3D)

**Description**

The same 28 icons and titles as `gcp-services.xml`, restyled with a gradient-filled badge, a soft drop shadow, a glossy top highlight, and a subtle embossed glyph shadow for a raised, dimensional look. Pick this library instead of the flat one when a diagram calls for a more polished, presentation-style visual treatment.

**Concise notes**

- Same service names/tags as `gcp-services.xml` — pick one style per diagram
- Gradient + shadow + gloss, no external image dependencies
- Still original artwork, not Google's trademarked icons

---

### Hashicorp Icons

**Description**

Icons representing HashiCorp tools, suitable for infrastructure, provisioning, and secrets-management diagrams.

**Concise notes**

- HashiCorp ecosystem focus
- Useful in IaC diagrams
- Product identification only

---

### Integration Patterns

**Description**

12 abstract Enterprise Integration Pattern (EIP) icons — Aggregator, Conditional, Content Enricher, Content Filter, Splitter, and similar — representing conceptual messaging/routing/transformation patterns, not any specific product. Not to be confused with `integration.xml`, which is product-specific.

**Concise notes**

- Pattern-oriented, tool-agnostic
- Ideal for integration architecture at the conceptual level
- See `integration.xml` for BizTalk/Azure tooling icons instead

---

### Integration

**Description**

A large (265-shape) icon pack for Microsoft BizTalk Server and Azure integration tooling — adapters (FTP, SFTP, HTTP, SQL, SAP, etc.), BizTalk Server components, Azure Service Bus, Logic Apps, and related infrastructure. Product/tool-specific, unlike the conceptual `integration-patterns.xml`.

**Concise notes**

- Tool and product-specific, not conceptual
- Use for BizTalk/Azure integration architecture diagrams
- See `integration-patterns.xml` for vendor-neutral EIP notation instead

---

### Office365

**Description**

Icons for Microsoft Office 365 applications and services, useful in productivity and collaboration diagrams.

**Concise notes**

- SaaS identification
- Not infrastructure primitives
- Use in user-centric diagrams

---

### OSA Icons

**Description**

A collection of OSA-related icons used for specialized or domain-specific architectural illustrations.

**Concise notes**

- Niche usage
- Domain-specific
- Validate meaning before reuse

---

### Power Bi

**Description**

Icons representing Power BI and related analytics concepts for reporting and data-visualization architectures.

**Concise notes**

- Analytics-focused
- Suitable for BI flows
- Product-centric

---

### Powerapps And Flows

**Description**

Symbols for Microsoft Power Apps and Power Automate, used to illustrate low-code solutions and automation workflows.

**Concise notes**

- Low-code platform focus
- Useful in business automation diagrams
- SaaS-centric

---

### Users And Roles

**Description**

Icons representing users, roles, and personas, intended to model access, responsibilities, and interaction points.

**Concise notes**

- Identity and role modeling
- Useful in security and access diagrams
- Conceptual, not technical

---

## 🚀 How to Use These Libraries

1. Open **draw.io / diagrams.net**
2. Go to **File → Open Library from → Device**
3. Select the desired `.xml` library file
4. Drag symbols directly onto your canvas

> You can load **multiple libraries at once** for richer diagrams.

---

## 🧭 Design Philosophy

All libraries follow the same guiding principles:

- **Semantic over decorative** — symbols represent concepts
- **Consistent sizing & alignment**
- **Minimal visual noise**
- **Readable at scale**
- **Tool-agnostic architectural meaning**

These libraries are meant to support **design discussions**, not replace architectural thinking.

---

## 📦 Versioning & Releases

Libraries are released as **versioned packs** via GitHub Releases.

Each release:

- is tagged (e.g. `v1.0.0`)
- includes a ZIP with stable `.xml` files
- guarantees backward compatibility within a major version

👉 See **GitHub Releases** for downloadable packs.

---

## 🛠 Adding a New Library (Guidelines)

If you want to contribute a new library:

- Keep scope **narrow and well-defined**
- Avoid duplicating symbols across libraries
- Use consistent naming and sizing
- Provide a short description for catalog inclusion
- Add at least one preview screenshot

---

## 📌 Notes on Screenshots

Screenshots referenced above should be placed in:

```
screenshots/
├── aws-core.png
├── cloud-native.png
├── devops.png
├── system-design.png
└── security.png
└── ...
```
