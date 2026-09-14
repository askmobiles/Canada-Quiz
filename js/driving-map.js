/* Tap your province on the map of Canada, get its four driving pages.
   ------------------------------------------------------------------
   The driving hub lists thirteen cards. That works if you already know which
   card is yours. A map works if you do not — and it is the faster way in even
   when you do, because a thumb finds a shape on a map quicker than an eye finds
   a name in a list of thirteen.

   The shapes come from js/canada-map-svg.js, the one copy of Canada on the
   site. Only the wiring is here.

   Both languages live in this file, the same as js/word-banks.js, and for the
   same reason: a string built by a script is never seen by build_fr.py, so a
   label written in English here would still be English on the French page. The
   links themselves need no translation — the French page is one folder deep and
   its twin has the same file name, so a relative link lands on the French page
   by itself. */
(function () {
  var fr = ((document.documentElement.getAttribute("lang") || "en").toLowerCase().indexOf("fr") === 0);

  /* t = the prefix the practice and mock tests use, p = the prefix the road
     signs and rules pages use. Ontario is the one place where they are the
     same string; everywhere else the test carries its licence class and the
     reference pages do not. These are read off the real file names, not
     guessed — get one wrong and the map sends a learner to a 404. */
  var PLACES = [
    { id: "ON", en: "Ontario",                   fr: "Ontario",                      t: "ontario-g1",            p: "ontario-g1" },
    { id: "QC", en: "Quebec",                    fr: "Québec",                  t: "quebec-class-5",        p: "quebec" },
    { id: "BC", en: "British Columbia",          fr: "Colombie-Britannique",         t: "bc-class-7l",           p: "bc" },
    { id: "AB", en: "Alberta",                   fr: "Alberta",                      t: "alberta-class-7",       p: "alberta" },
    { id: "MB", en: "Manitoba",                  fr: "Manitoba",                     t: "manitoba-class-5",      p: "manitoba" },
    { id: "SK", en: "Saskatchewan",              fr: "Saskatchewan",                 t: "saskatchewan-class-7",  p: "saskatchewan" },
    { id: "NS", en: "Nova Scotia",               fr: "Nouvelle-Écosse",         t: "nova-scotia-class-7",   p: "nova-scotia" },
    { id: "NB", en: "New Brunswick",             fr: "Nouveau-Brunswick",            t: "new-brunswick-class-7", p: "new-brunswick" },
    { id: "NL", en: "Newfoundland and Labrador", fr: "Terre-Neuve-et-Labrador",      t: "newfoundland-class-5",  p: "newfoundland" },
    { id: "PE", en: "Prince Edward Island",      fr: "Île-du-Prince-Édouard", t: "pei-class-7",        p: "pei" },
    { id: "YT", en: "Yukon",                     fr: "Yukon",                        t: "yukon-class-7",         p: "yukon" },
    { id: "NT", en: "Northwest Territories",     fr: "Territoires du Nord-Ouest",    t: "nwt-class-7",           p: "nwt" },
    { id: "NU", en: "Nunavut",                   fr: "Nunavut",                      t: "nunavut-class-7",       p: "nunavut" }
  ];

  var WORDS = {
    en: { practice: "Practice test", mock: "Mock test", signs: "Road signs",
          rules: "Rules of the road", prompt: "Tap your province or territory on the map." },
    fr: { practice: "Test pratique", mock: "Examen blanc", signs: "Panneaux routiers",
          rules: "Code de la route", prompt: "Touchez votre province ou territoire sur la carte." }
  };
  var W = fr ? WORDS.fr : WORDS.en;

  /* Codes that carry a hit oval, i.e. the places too small to tap or outline. */
  var TINY = {};
  if (window.CQMapSVG) {
    window.CQMapSVG.hit.forEach(function (h) { TINY[h["data-id"]] = true; });
  }

  var byId = {};
  PLACES.forEach(function (p) { byId[p.id] = p; });

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function show(place) {
    var box = document.getElementById("dm-panel");
    if (!box || !place) return;
    var links = [
      [place.t + "-practice-test.html", W.practice],
      [place.t + "-mock-test.html", W.mock],
      [place.p + "-road-signs.html", W.signs],
      [place.p + "-rules-of-the-road.html", W.rules]
    ];
    box.innerHTML =
      '<h3 class="dm-name">' + esc(fr ? place.fr : place.en) + "</h3>" +
      '<div class="dm-links">' +
      links.map(function (l) {
        return '<a class="btn" href="' + esc(l[0]) + '">' + esc(l[1]) + "</a>";
      }).join("") + "</div>";
    box.classList.add("is-on");

    var svg = document.getElementById("dm-svg");
    if (svg) {
      /* Prince Edward Island is a few pixels across. A 3px outline on a shape
         that small does not outline it, it fills it in, and the island turns
         into a black dot. So a place that has a finger-sized oval over it is
         marked by ringing the oval instead. Found by drawing it and looking. */
      Array.prototype.forEach.call(svg.querySelectorAll("[data-id]"), function (el) {
        var id = el.getAttribute("data-id");
        var tiny = TINY[id] && el.classList.contains("dm-p");
        el.classList.toggle("on", !tiny && id === place.id);
      });
    }
  }

  function init() {
    var svg = document.getElementById("dm-svg");
    if (!svg || !window.CQMap) return;
    CQMap.draw(svg, {
      placeClass: "dm-p", usaClass: "dm-usa", waterClass: "dm-water",
      hitClass: "dm-hit", shapesId: "dm-shapes", watersId: "dm-waters",
      labelsId: "dm-labels", labelsClass: "dm-hide"
    });

    /* A province is a link, not a decoration: it answers to a tap, to Enter and
       to the space bar, and a screen reader reads out its name. */
    Array.prototype.forEach.call(svg.querySelectorAll("[data-id]"), function (el) {
      var place = byId[el.getAttribute("data-id")];
      if (!place) return;
      el.setAttribute("tabindex", "0");
      el.setAttribute("role", "button");
      el.setAttribute("aria-label", fr ? place.fr : place.en);
      el.addEventListener("click", function () { show(place); });
      el.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); show(place); }
      });
    });

    var p = document.getElementById("dm-panel");
    if (p) p.innerHTML = '<p class="muted dm-prompt">' + esc(W.prompt) + "</p>";
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
