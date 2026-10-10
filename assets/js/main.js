/* Om Kathalkar — site interactions (no dependencies) */
(function () {
  "use strict";

  /* ---------- Latest strip: rotates through the newest updates ---------- */
  var latest = document.querySelector("[data-latest]");
  if (latest) {
    var items = JSON.parse(latest.getAttribute("data-latest"));
    var i = 0, timer = null;
    var dateEl = latest.querySelector(".latest-date");
    var textEl = latest.querySelector(".latest-text");
    var posEl = latest.querySelector(".latest-pos");
    var bar = latest.querySelector(".latest-bar");
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    function show(n) {
      i = (n + items.length) % items.length;
      dateEl.textContent = items[i][0] + " —";
      textEl.textContent = items[i][1];
      textEl.classList.remove("fade-in"); void textEl.offsetWidth; textEl.classList.add("fade-in");
      posEl.textContent = (i + 1) + " / " + items.length;
      bar.innerHTML = reduce ? "" : "<i></i>";
    }
    function restart() { clearInterval(timer); if (!reduce) timer = setInterval(function () { show(i + 1); }, 6000); }
    latest.querySelector("[data-prev]").addEventListener("click", function () { show(i - 1); restart(); });
    latest.querySelector("[data-next]").addEventListener("click", function () { show(i + 1); restart(); });
    show(0); restart();
  }

  /* ---------- KV-cache demo ---------- */
  var kv = document.querySelector("[data-kv]");
  if (kv) {
    var range = kv.querySelector("input[type=range]");
    var toks = Array.prototype.slice.call(kv.querySelectorAll(".tok"));
    var order = toks.map(function (t, idx) { return { idx: idx, s: parseFloat(t.dataset.score) }; })
      .sort(function (a, b) { return b.s - a.s || a.idx - b.idx; });
    function update() {
      var pct = parseInt(range.value, 10);
      var keep = Math.max(1, Math.ceil(toks.length * pct / 100));
      var kept = {};
      order.slice(0, keep).forEach(function (o) { kept[o.idx] = true; });
      toks.forEach(function (t, idx) { t.classList.toggle("off", !kept[idx]); });
      kv.querySelector("[data-budget]").textContent = pct + "%";
      kv.querySelector("[data-kept]").textContent = keep + " of " + toks.length;
      kv.querySelector(".kv-fill").style.width = pct + "%";
    }
    range.addEventListener("input", update);
    update();
  }

  /* ---------- Filters (publications, featured, news pages) ---------- */
  document.querySelectorAll("[data-filter-group]").forEach(function (group) {
    var scope = document.querySelector(group.getAttribute("data-filter-group"));
    group.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-filter]");
      if (!btn) return;
      var f = btn.getAttribute("data-filter");
      group.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
      scope.querySelectorAll("[data-kind]").forEach(function (el) {
        var kinds = el.getAttribute("data-kind").split(" ");
        el.hidden = !(f === "all" || kinds.indexOf(f) >= 0);
      });
      scope.querySelectorAll(".year-group").forEach(function (g) {
        g.hidden = !g.querySelector("[data-kind]:not([hidden])");
      });
    });
  });

  /* ---------- Copy email ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var label = btn.textContent;
      function done() { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = label; }, 2000); }
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, done); else done();
    });
  });
})();
