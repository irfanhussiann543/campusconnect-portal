/**
 * CampusConnect Public Interactive JavaScript
 */

document.addEventListener("DOMContentLoaded", function () {
  // 1. Animated Counter for Highlights Statistics
  const counters = document.querySelectorAll(".counter-value");
  let animated = false;

  function runCounters() {
    if (animated) return;
    const statsSection = document.querySelector(".stats-bar") || document.querySelector(".counter-value");
    if (!statsSection) return;

    const rect = statsSection.getBoundingClientRect();
    if (rect.top <= window.innerHeight && rect.bottom >= 0) {
      animated = true;
      counters.forEach(counter => {
        const target = parseFloat(counter.getAttribute("data-target"));
        const isDecimal = target % 1 !== 0;
        const duration = 1800;
        const startTime = performance.now();

        function updateCounter(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          // Ease-out expo function
          const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
          const currentVal = easeProgress * target;

          if (isDecimal) {
            counter.innerText = currentVal.toFixed(1);
          } else {
            counter.innerText = Math.floor(currentVal).toLocaleString();
          }

          if (progress < 1) {
            requestAnimationFrame(updateCounter);
          } else {
            counter.innerText = isDecimal ? target.toFixed(1) : target.toLocaleString();
          }
        }

        requestAnimationFrame(updateCounter);
      });
    }
  }

  window.addEventListener("scroll", runCounters);
  runCounters(); // Initial check in case it's in view

  // 2. Client-side Live Filter for Faculty Directory
  const facultySearchInput = document.getElementById("facultySearchInput");
  const facultyCards = document.querySelectorAll(".faculty-item");

  if (facultySearchInput) {
    facultySearchInput.addEventListener("input", function (e) {
      const term = e.target.value.toLowerCase().trim();
      facultyCards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(term)) {
          card.style.display = "";
        } else {
          card.style.display = "none";
        }
      });
    });
  }

  // 3. Client-side Filter for Notice Board & Events
  const noticeCategoryTabs = document.querySelectorAll(".category-tab-btn");
  const noticeItems = document.querySelectorAll(".notice-item");

  if (noticeCategoryTabs.length > 0) {
    noticeCategoryTabs.forEach(tab => {
      tab.addEventListener("click", function () {
        noticeCategoryTabs.forEach(t => t.classList.remove("active", "btn-primary-cc"));
        noticeCategoryTabs.forEach(t => t.classList.add("btn-outline-secondary"));
        this.classList.remove("btn-outline-secondary");
        this.classList.add("active", "btn-primary-cc");

        const selectedCategory = this.getAttribute("data-category");

        noticeItems.forEach(item => {
          const itemCategory = item.getAttribute("data-category");
          if (selectedCategory === "All" || itemCategory === selectedCategory) {
            item.style.display = "";
          } else {
            item.style.display = "none";
          }
        });
      });
    });
  }

  // 4. Auto-dismiss Flash Alerts after 5 seconds
  const flashAlerts = document.querySelectorAll(".alert-dismissible");
  flashAlerts.forEach(alert => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      if (bsAlert) {
        bsAlert.close();
      }
    }, 5000);
  });

  // 5. Back to Top Button
  const backToTopBtn = document.getElementById("backToTopBtn");
  if (backToTopBtn) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 400) {
        backToTopBtn.style.display = "block";
      } else {
        backToTopBtn.style.display = "none";
      }
    });

    backToTopBtn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
});
