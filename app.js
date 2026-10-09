"use strict";
const filters = document.querySelectorAll("[data-filter]");
const cards = document.querySelectorAll(".project-card");
filters.forEach(button => button.addEventListener("click", () => {
  const selected = button.dataset.filter;
  let visible = 0;
  cards.forEach(card => { card.hidden = selected !== "all" && card.dataset.kind !== selected; if (!card.hidden) visible++; });
  filters.forEach(other => { const active = other === button; other.classList.toggle("active", active); other.setAttribute("aria-pressed", String(active)); });
  document.getElementById("filter-status").textContent = `Showing ${visible} project${visible === 1 ? "" : "s"}`;
}));
const theme = document.getElementById("theme");
function applyTheme(light) { document.body.classList.toggle("light", light); theme.setAttribute("aria-label", light ? "Switch to dark theme" : "Switch to light theme"); }
try { applyTheme(localStorage.getItem("portfolio-theme") === "light"); } catch (_) { /* Storage can be disabled. */ }
theme.addEventListener("click", () => { const light = !document.body.classList.contains("light"); applyTheme(light); try { localStorage.setItem("portfolio-theme", light ? "light" : "dark"); } catch (_) {} });
