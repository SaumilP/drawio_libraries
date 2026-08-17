(function () {
  "use strict";

  const grid = document.getElementById("grid");
  const searchInput = document.getElementById("search");
  const categoriesEl = document.getElementById("categories");
  const resultCount = document.getElementById("result-count");
  const emptyState = document.getElementById("empty-state");
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxClose = document.querySelector(".lightbox-close");

  let libraries = [];
  let activeCategory = "All";

  function cardHTML(lib) {
    return `
      <article class="card" data-name="${escapeAttr(lib.name.toLowerCase())}" data-notes="${escapeAttr(lib.notes.toLowerCase())}" data-category="${escapeAttr(lib.category)}">
        <a class="card-thumb" href="${lib.screenshot}" data-lightbox="${lib.screenshot}" aria-label="Enlarge preview of ${escapeAttr(lib.name)}">
          <img src="${lib.screenshot}" alt="Preview of ${escapeAttr(lib.name)} shapes" loading="lazy">
        </a>
        <div class="card-body">
          <div class="card-category">${lib.category}</div>
          <div class="card-title-row">
            <h2 class="card-title">${lib.name}</h2>
            <span class="card-count">${lib.shapeCount} shapes</span>
          </div>
          <p class="card-notes">${lib.notes}</p>
          <div class="card-actions">
            <a class="primary" href="${lib.downloadUrl}" download>Download .xml</a>
            <a href="${lib.sourceUrl}" target="_blank" rel="noopener">View source</a>
          </div>
        </div>
      </article>
    `;
  }

  function escapeAttr(str) {
    return String(str).replace(/"/g, "&quot;");
  }

  function render() {
    const query = searchInput.value.trim().toLowerCase();

    const filtered = libraries.filter((lib) => {
      const matchesCategory = activeCategory === "All" || lib.category === activeCategory;
      const matchesQuery =
        !query ||
        lib.name.toLowerCase().includes(query) ||
        lib.notes.toLowerCase().includes(query) ||
        lib.category.toLowerCase().includes(query);
      return matchesCategory && matchesQuery;
    });

    grid.innerHTML = filtered.map(cardHTML).join("");
    resultCount.textContent = `${filtered.length} of ${libraries.length} libraries`;
    emptyState.hidden = filtered.length !== 0;
  }

  function renderCategoryChips() {
    const categories = ["All", ...new Set(libraries.map((l) => l.category))].sort((a, b) =>
      a === "All" ? -1 : b === "All" ? 1 : a.localeCompare(b)
    );

    categoriesEl.innerHTML = categories
      .map(
        (cat) =>
          `<button type="button" class="chip" data-category="${escapeAttr(cat)}" aria-pressed="${cat === activeCategory}">${cat}</button>`
      )
      .join("");

    categoriesEl.querySelectorAll(".chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        activeCategory = chip.dataset.category;
        categoriesEl.querySelectorAll(".chip").forEach((c) => c.setAttribute("aria-pressed", String(c === chip)));
        render();
      });
    });
  }

  function openLightbox(src) {
    lightboxImg.src = src;
    lightbox.hidden = false;
  }

  function closeLightbox() {
    lightbox.hidden = true;
    lightboxImg.src = "";
  }

  grid.addEventListener("click", (e) => {
    const thumb = e.target.closest("[data-lightbox]");
    if (!thumb) return;
    e.preventDefault();
    openLightbox(thumb.dataset.lightbox);
  });

  lightboxClose.addEventListener("click", closeLightbox);
  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeLightbox();
  });

  searchInput.addEventListener("input", render);

  fetch("gallery-data.json")
    .then((res) => res.json())
    .then((data) => {
      libraries = data;
      renderCategoryChips();
      render();
    })
    .catch((err) => {
      grid.innerHTML = "";
      resultCount.textContent = "";
      emptyState.hidden = false;
      emptyState.textContent = "Could not load gallery-data.json.";
      console.error(err);
    });
})();
