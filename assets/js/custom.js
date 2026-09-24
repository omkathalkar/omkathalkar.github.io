// Scroll-reveal: add .reveal to any element you want to animate in
(function () {
  "use strict";

  // ── Scroll Reveal ──────────────────────────────────────────────────────────
  function initReveal() {
    const els = document.querySelectorAll(".reveal");
    if (!els.length) return;
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("visible");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    els.forEach((el) => io.observe(el));
  }

  // ── Stat Counter ───────────────────────────────────────────────────────────
  function animateCounter(el) {
    const target = parseInt(el.getAttribute("data-target"), 10);
    const suffix = el.getAttribute("data-suffix") || "";
    const duration = 1200;
    const step = 16;
    const increment = target / (duration / step);
    let current = 0;

    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      el.textContent = Math.floor(current) + suffix;
    }, step);
  }

  function initCounters() {
    const counters = document.querySelectorAll(".stat-number[data-target]");
    if (!counters.length) return;

    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            animateCounter(e.target);
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    counters.forEach((c) => io.observe(c));
  }

  // ── Auto-wrap key sections in .reveal ─────────────────────────────────────
  function wrapReveal() {
    // News rows
    document.querySelectorAll(".news table tr").forEach((el, i) => {
      el.classList.add("reveal", `reveal-delay-${Math.min(i + 1, 4)}`);
    });
    // Publication entries
    document.querySelectorAll(".publications ol > li, .publications ul > li").forEach((el, i) => {
      el.classList.add("reveal", `reveal-delay-${Math.min(i + 1, 4)}`);
    });
    // Project cards
    document.querySelectorAll(".projects .card").forEach((el, i) => {
      el.classList.add("reveal", `reveal-delay-${Math.min(i + 1, 4)}`);
    });
    // Stat cards (already have .reveal via HTML, just init observer)
    document.querySelectorAll(".stat-card").forEach((el, i) => {
      el.classList.add("reveal", `reveal-delay-${Math.min(i + 1, 4)}`);
    });
  }

  // ── Typewriter / cycling role text ─────────────────────────────────────────
  function initTypewriter() {
    const el = document.getElementById("om-role-typer");
    if (!el) return;

    const phrases = [
      "PHD RESEARCHER · NATIONAL TECHNICAL UNIVERSITY OF ATHENS",
      "EFFICIENT AI INFERENCE · KV-CACHE OPTIMIZATION",
      "COMPUTER VISION · ENVIRONMENTAL AI",
    ];

    let phraseIdx = 0;
    let charIdx = 0;
    let deleting = false;
    const TYPE_MS = 38;
    const DEL_MS = 18;
    const PAUSE_MS = 2600;
    const END_PAUSE_MS = 400;

    function tick() {
      const phrase = phrases[phraseIdx];
      if (!deleting) {
        el.textContent = phrase.slice(0, ++charIdx);
        if (charIdx === phrase.length) {
          deleting = true;
          setTimeout(tick, PAUSE_MS);
          return;
        }
        setTimeout(tick, TYPE_MS);
      } else {
        el.textContent = phrase.slice(0, --charIdx);
        if (charIdx === 0) {
          deleting = false;
          phraseIdx = (phraseIdx + 1) % phrases.length;
          setTimeout(tick, END_PAUSE_MS);
          return;
        }
        setTimeout(tick, DEL_MS);
      }
    }

    tick();
  }

  document.addEventListener("DOMContentLoaded", function () {
    wrapReveal();
    initReveal();
    initCounters();
    initTypewriter();
  });
})();
