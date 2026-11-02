/**
 * CampusConnect Admin Dashboard Scripts
 */

document.addEventListener("DOMContentLoaded", function () {
  // 1. Mobile Sidebar Toggle
  const sidebarToggle = document.getElementById("adminSidebarToggle");
  const sidebar = document.querySelector(".admin-sidebar");

  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener("click", function () {
      sidebar.classList.toggle("show");
    });
  }

  // 2. Generic Edit Modal Data Population
  document.querySelectorAll("[data-bs-target='#editModal']").forEach(button => {
    button.addEventListener("click", function () {
      const form = document.getElementById("editForm");
      if (!form) return;

      const actionUrl = this.getAttribute("data-action");
      if (actionUrl) {
        form.setAttribute("action", actionUrl);
      }

      // Populate input fields matching data-* attributes
      const dataset = this.dataset;
      for (const key in dataset) {
        const input = form.querySelector(`[name="${key}"]`);
        if (input) {
          if (input.type === "checkbox") {
            input.checked = dataset[key] === "true" || dataset[key] === "1";
          } else {
            input.value = dataset[key];
          }
        }
      }
    });
  });

  // 3. Quick Table Search in Admin Tables
  const adminTableSearch = document.getElementById("adminTableSearch");
  if (adminTableSearch) {
    adminTableSearch.addEventListener("input", function (e) {
      const query = e.target.value.toLowerCase().trim();
      const rows = document.querySelectorAll(".admin-table tbody tr");
      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(query) ? "" : "none";
      });
    });
  }
});
