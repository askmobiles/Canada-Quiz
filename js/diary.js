/* Canada Diary — the pickers and the reader settings.
 *
 * IMPORTANT: this file NEVER creates a note and never fetches one. Every note
 * is already printed into the HTML by tools/newq/build_diary.py. All this does
 * is hide and show. That is deliberate: if the notes only appeared after a tap,
 * Google would index one day and ignore the other hundred and thirty.
 *
 * With JavaScript switched off the page degrades to the full list in date
 * order, which is a perfectly good page.
 */
(function () {
  "use strict";

  var root = document.documentElement;
  var list = document.getElementById("dlist");
  if (!list) return;

  var notes = [].slice.call(list.querySelectorAll(".dnote"));
  var eraHeads = [].slice.call(list.querySelectorAll(".dera"));
  if (!notes.length) return;

  /* ------------------------------------------------------------------ *
   * READER SETTINGS
   * Stored on the reader's own device. It never leaves the browser and
   * it is not tracking. Wrapped in try/catch because a private window
   * and blocked site data both throw, and a settings panel must never
   * break the page.
   * ------------------------------------------------------------------ */
  var DEFAULTS = { hand: "friendly", size: "normal", paper: "aged" };
  var prefs = { hand: DEFAULTS.hand, size: DEFAULTS.size, paper: DEFAULTS.paper };

  try {
    var saved = JSON.parse(localStorage.getItem("cq-read") || "{}");
    ["hand", "size", "paper"].forEach(function (k) {
      if (saved && typeof saved[k] === "string") prefs[k] = saved[k];
    });
  } catch (e) { /* keep the defaults */ }

  function applyPrefs() {
    var cls = root.className.split(/\s+/).filter(function (c) {
      return c && c.indexOf("rd-") !== 0;
    });
    cls.push("rd-hand-" + prefs.hand, "rd-size-" + prefs.size, "rd-paper-" + prefs.paper);
    root.className = cls.join(" ");
    try { localStorage.setItem("cq-read", JSON.stringify(prefs)); } catch (e) {}
    document.querySelectorAll(".d-opt").forEach(function (b) {
      b.setAttribute("aria-pressed", String(prefs[b.dataset.set] === b.dataset.val));
    });
  }

  var readBtn = document.getElementById("d-readbtn");
  var readPanel = document.getElementById("d-readpanel");
  if (readBtn && readPanel) {
    readBtn.addEventListener("click", function () {
      var open = readPanel.hasAttribute("hidden");
      if (open) readPanel.removeAttribute("hidden");
      else readPanel.setAttribute("hidden", "");
      readBtn.setAttribute("aria-expanded", String(open));
    });
  }
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest && ev.target.closest(".d-opt");
    if (!b) return;
    prefs[b.dataset.set] = b.dataset.val;
    applyPrefs();
  });

  /* ------------------------------------------------------------------ *
   * THE PICKERS
   * ------------------------------------------------------------------ */
  var T = {
    en: {
      months: ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"],
      eras: ["Before Canada", "1867 – 1899", "1900 – 1949", "1950 – 1999", "2000 – today"],
      todayIs: "Today is {d}.",
      nothing: "Nothing is written for this date yet.",
      nothingSub: "Here is the rest of this month instead. A day with nothing worth recording is left empty rather than filled with something invented.",
      one: "1 note", many: "{n} notes",
      coming: "Still to come",
      pickMonth: "Choose a month", pickEra: "Choose a time"
    },
    fr: {
      months: ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
               "août", "septembre", "octobre", "novembre", "décembre"],
      eras: ["Avant le Canada", "1867 – 1899", "1900 – 1949", "1950 – 1999", "2000 à aujourd'hui"],
      todayIs: "Nous sommes le {d}.",
      nothing: "Rien n'est encore inscrit à cette date.",
      nothingSub: "Voici plutôt le reste du mois. Une journée sans rien qui mérite d'être noté reste vide plutôt que d'être remplie par une invention.",
      one: "1 note", many: "{n} notes",
      coming: "Encore à venir",
      pickMonth: "Choisissez un mois", pickEra: "Choisissez une époque"
    }
  };
  var lang = (root.getAttribute("lang") || "en").slice(0, 2) === "fr" ? "fr" : "en";
  var t = T[lang];

  var now = new Date();
  var TM = now.getMonth() + 1, TD = now.getDate();

  var pick = document.getElementById("d-pick");
  var chips = document.getElementById("d-chips");
  var said = document.getElementById("d-said");
  var tabs = {
    today: document.getElementById("d-t-today"),
    month: document.getElementById("d-t-month"),
    era: document.getElementById("d-t-era"),
    all: document.getElementById("d-t-all")
  };
  if (pick) pick.removeAttribute("hidden");   /* only shown when JS is running */

  var view = "today", selMonth = TM, selEra = 0;
  var emptyBox = null;

  function isFuture(n) { return n.classList.contains("fut"); }
  function mOf(n) { return n.dataset.m ? +n.dataset.m : 0; }
  function dOf(n) { return n.dataset.d ? +n.dataset.d : 0; }
  function eOf(n) { return +n.dataset.era; }

  function show(n, on) {
    if (on) n.removeAttribute("hidden");
    else n.setAttribute("hidden", "");
  }

  function countText(k) {
    return k === 1 ? t.one : t.many.replace("{n}", k);
  }

  function clearEmpty() {
    if (emptyBox && emptyBox.parentNode) emptyBox.parentNode.removeChild(emptyBox);
    emptyBox = null;
  }

  function showEmptyNotice() {
    clearEmpty();
    emptyBox = document.createElement("div");
    emptyBox.className = "d-empty";
    var a = document.createElement("p");
    a.appendChild(document.createElement("strong")).textContent = t.nothing;
    var b = document.createElement("p");
    b.textContent = t.nothingSub;
    emptyBox.appendChild(a); emptyBox.appendChild(b);
    list.parentNode.insertBefore(emptyBox, list);
  }

  function render() {
    clearEmpty();
    var shown = 0, i;

    if (view === "all") {
      notes.forEach(function (n) { show(n, true); shown++; });
      eraHeads.forEach(function (h) { show(h, true); });
      said.textContent = countText(shown);
    } else {
      eraHeads.forEach(function (h) { show(h, false); });

      if (view === "today") {
        var hits = notes.filter(function (n) {
          return !isFuture(n) && mOf(n) === TM && dOf(n) === TD;
        });
        var month = notes.filter(function (n) {
          return !isFuture(n) && mOf(n) === TM;
        });
        var future = notes.filter(isFuture);
        var keep = hits.length ? hits : month;
        notes.forEach(function (n) { show(n, keep.indexOf(n) >= 0 || future.indexOf(n) >= 0); });
        shown = keep.length;
        var dtxt = lang === "en" ? (t.months[TM - 1] + " " + TD) : (TD + " " + t.months[TM - 1]);
        said.textContent = t.todayIs.replace("{d}", dtxt) + " " + countText(shown);
        if (!hits.length) showEmptyNotice();
      } else if (view === "month") {
        notes.forEach(function (n) {
          var on = !isFuture(n) && mOf(n) === selMonth;
          show(n, on); if (on) shown++;
        });
        said.textContent = countText(shown);
      } else {
        notes.forEach(function (n) {
          var on = !isFuture(n) && eOf(n) === selEra;
          show(n, on); if (on) shown++;
        });
        said.textContent = countText(shown);
      }
    }

    Object.keys(tabs).forEach(function (k) {
      if (tabs[k]) tabs[k].setAttribute("aria-selected", String(k === view));
    });
  }

  function buildChips() {
    chips.innerHTML = "";
    if (view === "month") {
      t.months.forEach(function (name, i) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "d-chip";
        b.textContent = name;
        b.setAttribute("aria-pressed", String(i + 1 === selMonth));
        b.addEventListener("click", function () { selMonth = i + 1; buildChips(); render(); });
        chips.appendChild(b);
      });
    } else if (view === "era") {
      t.eras.forEach(function (name, i) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "d-chip";
        b.textContent = name;
        b.setAttribute("aria-pressed", String(i === selEra));
        b.addEventListener("click", function () { selEra = i; buildChips(); render(); });
        chips.appendChild(b);
      });
    }
  }

  Object.keys(tabs).forEach(function (k) {
    if (!tabs[k]) return;
    tabs[k].addEventListener("click", function () {
      view = k; buildChips(); render();
      window.scrollTo(0, 0);
    });
  });

  /* a note linked directly by its anchor must be visible when the page opens */
  if (location.hash && document.getElementById(location.hash.slice(1))) {
    view = "all";
  }

  applyPrefs();
  buildChips();
  render();
})();
