/* ==========================================================================
   Canada Quiz — site.js
   ONE file that controls every page. Loaded by all pages.

   It does three jobs:
     1. Draws the SAME header on every page (logo, menu, language button)
     2. Draws the SAME footer on every page
     3. Switches the whole site between English and French

   HOW FRENCH WORKS
     Every English page  ->  https://canada-quiz.com/about.html
     Its French twin     ->  https://canada-quiz.com/fr/about.html
   The French pages are built automatically by build_fr.py from the English
   ones, so you NEVER write a page twice. This file also translates any text
   that the games and quizzes create while you play.

   TO CHANGE THE MENU OR FOOTER ANYWHERE ON THE SITE, edit this file only.
   ========================================================================== */
(function () {
  "use strict";

  /* Where the site root is, relative to this page.
     "" on English pages, "../" on the French pages inside /fr/ */
  var BASE = (function () {
    var s = document.currentScript;
    if (s && s.src) {
      var m = /^(.*?)js\/site\.js/.exec(s.getAttribute("src") || "");
      if (m) return m[1];
    }
    return "";
  })();

  /* ---------------------------------------------------------------
     1. THE MENU — change a link here and it changes on all pages
     --------------------------------------------------------------- */
  /* The menu, with its sub-menus. Written from tools/menu.json by
     tools/newq/reg_menu.py, which also writes the same menu into the HTML of
     every page. Change tools/menu.json, never these lines. */
  /*MENU*/var MENU = [{"href":"quizzes.html","en":"Quizzes","fr":"Quiz","items":[["quizzes.html","All quizzes","Tous les quiz"],["citizenship.html","Citizenship test practice","Pratique de l'examen de citoyenneté"],["canada-quiz.html","Canada quiz","Quiz sur le Canada"],["gk-quiz.html","General knowledge","Culture générale"],["canada-map.html","Map of Canada quiz","Quiz de la carte du Canada"],["province-quiz.html","Province quiz","Quiz des provinces"],["world-quiz.html","World quiz","Quiz sur le monde"],["daily.html","Daily quiz","Quiz du jour"],["which-came-first.html","Which came first?","Lequel est arrivé en premier ?"]]},{"href":"teachers.html","en":"School","fr":"École","items":[["teachers.html","For teachers","Pour les enseignants"],["remembrance-day-quiz.html","Remembrance Day quiz","Quiz du jour du Souvenir",{"hot":["Nov 11","11 nov."],"icon":"poppy"}],["canada-map.html","Map of Canada quiz","Quiz de la carte du Canada"],["history-grade-3.html","Grade 3 · Early Canada","3e année · Le Canada d'autrefois"],["provinces-and-territories-grade-4.html","Grade 4 · Provinces and territories","4e année · Provinces et territoires"],["history-grade-5.html","Grade 5 · First Peoples and Europeans","5e année · Premiers Peuples et Européens"],["history-grade-6.html","Grade 6 · Communities, past and present","6e année · Les communautés, hier et aujourd'hui"],["history-grade-7.html","Grade 7 · New France to 1850","7e année · De la Nouvelle-France à 1850"],["history-grade-8.html","Grade 8 · Creating Canada","8e année · La création du Canada"],["geography-grade-9.html","Grade 9 · Geography of Canada","9e année · Géographie du Canada"],["history-grade-10.html","Grade 10 · Canada since 1914","10e année · Le Canada depuis 1914"],["civics-grade-10.html","Grade 10 · Civics and Citizenship","10e année · Civisme et citoyenneté"],["printable-quizzes.html","Printable worksheets","Feuilles à imprimer"],["printable-canada-maps.html","Printable maps","Cartes à imprimer"]]},{"href":"games.html","en":"Games","fr":"Jeux","items":[["games.html","All family games","Tous les jeux en famille"],["trivia-showdown.html","Trivia Showdown","Duel de quiz"],["canada-road-trip.html","Road Trip Across Canada","Traversée du Canada en voiture"],["charades.html","Charades","Mime"],["would-you-rather.html","Would you rather?","Préférerais-tu ?"],["crossword.html","Crosswords","Mots croisés"],["word-search.html","Word search","Mots cachés"],["chess.html","Chess","Échecs"],["printable-puzzles.html","Printable puzzles","Casse-têtes à imprimer"]]},{"href":"for-kids.html","en":"Kids","fr":"Enfants","items":[["for-kids.html","True stories for kids","Histoires vraies pour enfants"],["20-fun-facts-about-canada-for-kids.html","20 fun facts about Canada","20 faits amusants sur le Canada"],["rights-and-respect.html","Rights and Respect","Droits et respect"],["times-tables.html","Times tables","Tables de multiplication"],["math-race.html","Math Race","Course de calcul"],["which-canadian-animal-quiz.html","Which Canadian animal are you?","Quel animal canadien es-tu ?"]]},{"href":"driving-test.html","en":"Driving","fr":"Conduite","items":[["driving-test.html","Driving test practice","Pratique de l'examen de conduite"],["canada-driving-test-by-province.html","Tests by province","Examens par province"],["ontario-g1-practice-test.html","Ontario G1 practice","Pratique G1 de l'Ontario"],["ontario-g1-mock-test.html","Ontario G1 mock test","Examen simulé G1 de l'Ontario"],["read-the-road.html","Read the Road (signs game)","Lire la route (jeu des panneaux)"],["ontario-driving-scenarios.html","What would you do?","Que feriez-vous ?"],["how-to-get-a-drivers-licence-in-canada.html","How to get a licence","Comment obtenir un permis"]]},{"href":"blog.html","en":"Blog","fr":"Blogue","items":[["blog.html","All articles","Tous les articles"],["blog.html#sec-cit","Citizenship and your first years","Citoyenneté et premières années"],["blog.html#sec-money","Money and everyday life","L'argent et la vie de tous les jours"],["blog.html#sec-driving","Driving in Canada","Conduire au Canada"],["blog.html#sec-gov","Government, work and the economy","Gouvernement, travail et économie"],["blog.html#sec-history","History and symbols","Histoire et symboles"],["blog.html#sec-family","Canada for families","Le Canada en famille"],["blog.html#sec-more","More about Canada","Encore sur le Canada"]]},{"href":"search.html","en":"Search","fr":"Rechercher","icon":"search","items":[]}];/*/MENU*/

  var FOOTER_LINKS = [
    { href: "./",           label: "Home" },
    { href: "about.html",   label: "About" },
    { href: "contact.html", label: "Contact" },
    { href: "all-pages.html", label: "All Pages" },
    /* This list is the footer a visitor SEES: paint() replaces the footer that
       came from the server with this one. So a link added to the template in
       tools/rewrite_pages.py and not added here is invisible to everyone
       except a crawler running without JavaScript — which is exactly how the
       teachers link was lost on its first build. Change the two together. */
    { href: "teachers.html", label: "For Teachers" },
    { href: "privacy.html", label: "Privacy Policy" },
    { href: "terms.html",   label: "Terms & Conditions" }
  ];

  var BRAND      = "Canada Quiz & Family Fun Games";
  var FOOTER_TAG = "Free quizzes, family games and citizenship practice — no signup, nothing on the site costs money.";
  var COPYRIGHT  = "© 2026 Canada Quiz & Family Fun Games. All rights reserved.";
  var DISCLAIMER = "Unofficial practice site. Not affiliated with the Government of Canada.";

  /* ---------------------------------------------------------------
     2. WHICH PAGE AND WHICH LANGUAGE ARE WE ON?
     The URL decides. /fr/anything.html is French, everything else English.
     --------------------------------------------------------------- */
  var file = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  if (!file || file.indexOf(".") === -1) file = "index.html";

  var isFR = /(^|\/)fr\/[^\/]*$/.test(location.pathname) ||
             document.documentElement.getAttribute("data-lang") === "fr";
  var lang = isFR ? "fr" : "en";

  window.CQ = window.CQ || {};
  window.CQ.lang = lang;

  function setLang(next) {
    if (next === lang) return;
    /* the home page is /  and  /fr/  — never index.html, which is a second
       URL for the same page */
    var f = file === "index.html" ? "" : file;
    location.href = next === "fr" ? BASE + "fr/" + f : (BASE + f || "./");
  }
  window.CQ.setLang = setLang;

  /* ---------------------------------------------------------------
     3. TRANSLATION ENGINE
     Swaps English text for French anywhere on the page — including
     questions and words that appear later, while you play.
     --------------------------------------------------------------- */
  var DICT = null;

  var SKIP_TAGS = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, CODE: 1, PRE: 1, TEXTAREA: 1, SVG: 1, CANVAS: 1 };
  var ATTRS = ["placeholder", "title", "aria-label", "alt", "value"];

  function norm(s) { return String(s).replace(/\s+/g, " ").trim(); }

  function upper1(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  function lower1(s) { return s.charAt(0).toLowerCase() + s.slice(1); }

  /* Sentences the games build with a number inside, e.g. "Q3 of 5" */
  var PATTERNS = [
    [/^Score: ?(\d+) ?\((\d+) words?\)$/i, "Score : $1 ($2 mots)"],
    [/^(\d+) words?$/i,                  "$1 mots"],
    [/^(\d+) letters?$/i,                "$1 lettres"],
    [/^(\d+) Across$/i,                  "$1 Horizontal"],
    [/^(\d+) Down$/i,                    "$1 Vertical"],
    [/^Q(\d+) of (\d+)$/i,               "Q$1 sur $2"],
    [/^Question (\d+) of (\d+)$/i,       "Question $1 sur $2"],
    [/^(\d+) of (\d+)$/,                 "$1 sur $2"],
    [/^(\d+) \/ (\d+)$/,                 "$1 / $2"],
    [/^Score: ?(.+)$/i,                  "Score : $1"],
    [/^Time: ?(.+)$/i,                   "Temps : $1"],
    [/^Time left: ?(.+)$/i,              "Temps restant : $1"],
    [/^Round (\d+)$/i,                   "Manche $1"],
    [/^Level (\d+)$/i,                   "Niveau $1"],
    [/^(\d+) points?$/i,                 "$1 points"],
    [/^You scored (\d+) out of (\d+)$/i, "Vous avez obtenu $1 sur $2"],
    [/^Player (\d+)$/i,                  "Joueur $1"],
    [/^Team (\d+)$/i,                    "Équipe $1"]
  ];

  /* one string, trying a capital / small first letter as well */
  function core(t) {
    var d = DICT[t];
    if (d) return d;
    var lc = lower1(t);
    if (lc !== t && DICT[lc]) return upper1(DICT[lc]);
    var uc = upper1(t);
    if (uc !== t && DICT[uc]) return lower1(DICT[uc]);
    return null;
  }

  function lookup(raw, depth) {
    if (!DICT) return null;
    var t = norm(raw);
    if (!t || t.length < 2) return null;

    var d = core(t);
    if (d) return d;

    /* strip a leading emoji / arrow and trailing punctuation, then retry */
    var m = /^([^A-Za-z0-9(]*)(.*?)([\s.:!?…]*)$/.exec(t);
    if (m && m[2] && m[2].length > 1 && m[2] !== t) {
      var inner = core(m[2]);
      if (inner) return m[1] + inner + m[3];
    }

    /* "Q3 of 5", "Score: 12" … */
    for (var i = 0; i < PATTERNS.length; i++) {
      if (PATTERNS[i][0].test(t)) return t.replace(PATTERNS[i][0], PATTERNS[i][1]);
    }

    /* "12. City with the CN Tower" — a numbered list item */
    if (!depth) {
      var n = /^(\d+[.)])\s+(.+)$/.exec(t);
      if (n) {
        var rest = lookup(n[2], 1);
        if (rest) return n[1] + " " + rest;
      }
    }

    /* "Something: something else" — translate the two halves separately */
    if (!depth) {
      var s = /^(.{2,60}?):\s*(.+)$/.exec(t);
      if (s) {
        var a = lookup(s[1], 1), b = lookup(s[2], 1);
        if (a || b) return (a || s[1]) + " : " + (b || s[2]);
      }
    }
    return null;
  }

  /* T() = translate one short label used by the header and footer */
  function T(s) { var f = lookup(s); return f || s; }

  function translateNode(node) {
    if (!node) return;
    if (node.nodeType === 3) {                       /* a piece of text */
      var p = node.parentNode;
      if (!p || SKIP_TAGS[p.nodeName]) return;
      if (p.closest && p.closest("[data-no-i18n]")) return;
      var v = node.nodeValue, fr = lookup(v);
      if (fr) {
        /* keep the original spacing around the words */
        var lead = v.slice(0, v.length - v.replace(/^\s+/, "").length);
        var trail = v.slice(v.replace(/\s+$/, "").length);
        var out = lead + fr + trail;
        /* Writing nodeValue fires a characterData mutation even when the text
           does not change, and the observer below translates whatever changed.
           A phrase that is already French — "Coups : 0" looks up to itself —
           therefore looped forever and froze the tab. Only write a real
           change. This is what locked up New Game on the French Memory page. */
        if (out !== v) node.nodeValue = out;
      }
      return;
    }
    if (node.nodeType !== 1) return;
    if (SKIP_TAGS[node.nodeName]) return;
    if (node.hasAttribute && node.hasAttribute("data-no-i18n")) return;

    for (var i = 0; i < ATTRS.length; i++) {
      var a = ATTRS[i];
      if (node.hasAttribute && node.hasAttribute(a)) {
        if (a === "value" && node.nodeName !== "BUTTON" &&
            node.type !== "button" && node.type !== "submit") continue;
        var t = lookup(node.getAttribute(a));
        if (t) node.setAttribute(a, t);
      }
    }
    var kids = node.childNodes;
    for (var j = 0; j < kids.length; j++) translateNode(kids[j]);
  }

  /* js/puzzle-print.js builds a print sheet and opens the print dialog in the
     same breath. Waiting for the MutationObserver below would be a race
     against the print window, and losing that race prints an English sheet on
     a French page, so the sheet is translated synchronously instead. */
  window.CQ.translateNode = translateNode;

  function translatePage() {
    if (!DICT) return;
    document.documentElement.lang = "fr";
    var t = lookup(document.title);
    if (t) document.title = t;
    var md = document.querySelector('meta[name="description"]');
    if (md) { var d = lookup(md.content); if (d) md.content = d; }
    translateNode(document.body);
  }

  function watch() {
    if (!window.MutationObserver || !DICT) return;
    var mo = new MutationObserver(function (muts) {
      for (var i = 0; i < muts.length; i++) {
        var m = muts[i];
        for (var j = 0; j < m.addedNodes.length; j++) translateNode(m.addedNodes[j]);
        if (m.type === "characterData" && m.target) translateNode(m.target);
      }
    });
    mo.observe(document.body, { childList: true, subtree: true, characterData: true });
  }

  var FRVER = {core:"1d3df759",gk:"62ff2d6c",cit:"c1170e37",fun:"a82bda89",drive:"9ea6f05c",kids:"71e99c45"};
  function loadFrench(done) {
    /* The dictionary is split into chunks by tools/split_fr.py. Every French
       page needs "core" (the header, footer and UI strings site.js injects);
       the question chunks are only needed by pages that actually carry that
       quiz engine. Deciding from the scripts already on the page means no page
       has to declare anything, and a new quiz page picks up its chunk on its
       own. This is why a French driving page fetches 3.7 KB where it used to
       fetch 3.3 MB. */
    var want = ["core"];
    var map = [["gk-questions", "gk"], ["citizenship-questions", "cit"],
               ["fun-questions", "fun"], ["driving-engine", "drive"],
               ["kids-quiz", "kids"]];
    for (var i = 0; i < map.length; i++) {
      if (document.querySelector('script[src*="' + map[i][0] + '"]')) want.push(map[i][1]);
    }
    var left = want.length;
    function one() { if (--left <= 0) { DICT = window.CQ_FR || null; done(); } }
    for (var j = 0; j < want.length; j++) {
      var s = document.createElement("script");
      s.src = BASE + "js/i18n-fr-" + want[j] + ".js?v=" + FRVER[want[j]];
      s.onload = one;
      s.onerror = one;
      document.head.appendChild(s);
    }
  }

  /* ---------------------------------------------------------------
     4. BUILD THE HEADER + FOOTER (already in the right language)
     --------------------------------------------------------------- */
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  var ICON = {
    search: '<svg class="nav-ico" aria-hidden="true" viewBox="0 0 24 24" width="17" height="17"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/></svg>'
  };

  function headerHTML() {
    /* One item per section. The section is "on" when this page is the
       section's own page or any page in its list. */
    function lab(o) { return lang === "fr" ? o.fr : o.en; }
    var links = '<ul class="nav-list">' + MENU.map(function (m, k) {
      var mine = m.href === file || m.items.some(function (it) { return it[0].split("#")[0] === file; });
      var top = '<a class="nav-top' + (mine ? ' on"' : '"') + ' href="' + m.href + '"' +
                (m.href === file ? ' aria-current="page"' : "") + ">" +
                (m.icon ? ICON[m.icon] : "") + esc(lab(m)) + "</a>";
      if (!m.items.length) return '<li class="nav-item">' + top + "</li>";
      var sub = m.items.map(function (it) {
        var here = it[0] === file, hot = it[3];
        var a = '<a href="' + it[0] + '"' + (here ? ' class="on" aria-current="page"' : "") + ">";
        var t = esc(lang === "fr" ? it[2] : it[1]);
        /* the featured item (menu.json, 4th part): highlighted, with a small tag */
        if (hot) return '<li class="sub-hot' + (hot.icon ? " ico-" + hot.icon : "") + '">' + a +
               "<span>" + t + '</span><span class="sub-tag">' + esc(hot.hot[lang === "fr" ? 1 : 0]) + "</span></a></li>";
        return "<li>" + a + t + "</a></li>";
      }).join("");
      return '<li class="nav-item has-sub">' + top +
        '<button type="button" class="sub-btn" aria-expanded="false" aria-controls="cq-sub-' + k + '"' +
        ' aria-label="' + esc(lab(m)) + '">▾</button>' +
        '<ul class="sub" id="cq-sub-' + k + '">' + sub + "</ul></li>";
    }).join("") + "</ul>";

    var other = lang === "fr" ? "en" : "fr";
    var tip = lang === "fr" ? "Switch to English" : "Passer en français";
    var btn = '<button type="button" class="lang-btn" data-no-i18n data-set-lang="' + other + '"' +
              ' aria-label="' + esc(tip) + '" title="' + esc(tip) + '">' +
              '<span aria-hidden="true">🌐</span> ' + other.toUpperCase() + "</button>";

    /* Dark/light switch. Only on pages that carry the theme loader at the top
       of <head> (tools/newq/build_dark.py): the Canada Diary and the printable
       sheets stay on paper, so they get no switch at all. */
    if (document.documentElement.getAttribute("data-theme-ok")) {
      var tt = lang === "fr" ? "Mode sombre ou clair" : "Dark or light mode";
      btn += '<button type="button" class="lang-btn cq-theme-btn" data-no-i18n data-cq-theme' +
             ' aria-label="' + esc(tt) + '" title="' + esc(tt) + '">' +
             '<span class="t-moon" aria-hidden="true">🌙</span><span class="t-sun" aria-hidden="true">☀️</span></button>';
    }

    return '<div class="container">' +
      '<a class="brand" href="./" aria-label="' + esc(BRAND) + '">' +
        '<img src="' + BASE + 'brand/logo-horizontal-white.svg?v=bb66f331" alt="' + esc(BRAND) +
        '" class="brand-logo" width="230" height="55">' +
      "</a>" +
      '<nav class="nav" id="cq-menu" aria-label="' + esc(T("Main navigation")) + '">' + links + "</nav>" +
      '<div class="hdr-tools">' + btn +
        '<button type="button" class="menu-btn" aria-expanded="false" aria-controls="cq-menu">' +
        '<span aria-hidden="true">☰</span> ' + (lang === "fr" ? "Menu" : "Menu") + "</button></div>" +
      "</div>";
  }

  function footerHTML() {
    var links = FOOTER_LINKS.map(function (n) {
      return '<a href="' + n.href + '">' + esc(T(n.label)) + "</a>";
    }).join(" · ");
    return '<div class="container center">' +
      '<img src="' + BASE + 'brand/logo-horizontal-white.svg?v=bb66f331" alt="' + esc(BRAND) +
      '" class="footer-logo" width="200" height="48">' +
      "<p>" + esc(T(FOOTER_TAG)) + "</p>" +
      '<div class="footer-links">' + links + "</div>" +
      '<p class="muted" style="color:#b4a9cc;font-size:12px">' + esc(T(COPYRIGHT)) + "</p>" +
      '<p class="muted" style="color:#b4a9cc;font-size:12.5px">' + esc(T(DISCLAIMER)) + "</p>" +
      "</div>";
  }

  /* Flip dark/light and remember the choice. css/dark.css is only on the page
     already if the visitor arrived in dark mode, so it is fetched on the
     first switch; window.CQ_DARK is its stamped address, set by the loader. */
  function toggleTheme() {
    var d = document.documentElement;
    var dark = d.getAttribute("data-theme") !== "dark";
    if (dark && !document.getElementById("cq-dark") && window.CQ_DARK) {
      var l = document.createElement("link");
      l.rel = "stylesheet"; l.id = "cq-dark"; l.href = window.CQ_DARK;
      document.head.appendChild(l);
    }
    if (dark) d.setAttribute("data-theme", "dark"); else d.removeAttribute("data-theme");
    try { localStorage.setItem("cq-theme", dark ? "dark" : "light"); } catch (e) {}
  }

  function paint() {
    /* Read the screen width ONCE, before we start rewriting the page. Asking
       for it after an innerHTML change forces the browser to stop and redo the
       whole layout on the spot; PageSpeed measured 128 ms lost that way. */
    var wideScreen = window.innerWidth >= 900;

    var h = document.querySelector("header.site-header");
    if (!h) {
      h = document.createElement("header");
      h.className = "site-header";
      document.body.insertBefore(h, document.body.firstChild);
    }
    h.innerHTML = headerHTML();
    h.setAttribute("data-no-i18n", "");   /* already in the right language */

    var f = document.querySelector("footer.site-footer");
    if (!f) {
      f = document.createElement("footer");
      f.className = "site-footer";
      document.body.appendChild(f);
    }
    /* Keep the "All pages" list that is already written into the page —
       it is one long block, so we do not want a second copy inside this file.
       On the French pages it is already in French (build_fr.py did that). */
    var map = f.querySelector(".footer-map");
    f.innerHTML = footerHTML();
    if (map) {
      var box = f.querySelector(".container") || f;
      var last = box.querySelector("p.muted");
      if (last) box.insertBefore(map, last); else box.appendChild(map);
      /* open on a big screen, folded away on a phone */
      if (wideScreen) map.setAttribute("open", "");
    }
    f.setAttribute("data-no-i18n", "");

    /* A page with its own sticky bar (the games search) parks it just under
       the sticky header, not underneath it. Measured after the paint, and
       only on such a page, so no other page pays for the layout read. */
    if (document.querySelector(".game-nav")) {
      var setH = function () {
        var sticky = window.getComputedStyle(h).position === "sticky";
        document.documentElement.style.setProperty("--hdr-h", (sticky ? h.offsetHeight : 0) + "px");
      };
      window.requestAnimationFrame(setH);
      window.addEventListener("resize", setH);
    }

    /* the menu: Menu button, section arrows, and closing on a click outside
       or on Escape */
    function closeSubs(except) {
      var open = h.querySelectorAll(".nav-item.open");
      for (var i = 0; i < open.length; i++) {
        if (open[i] === except) continue;
        open[i].classList.remove("open");
        var sb = open[i].querySelector(".sub-btn");
        if (sb) sb.setAttribute("aria-expanded", "false");
      }
    }
    function toggleSub(item) {
      var on = !item.classList.contains("open");
      closeSubs(item);
      item.classList.toggle("open", on);
      var sb = item.querySelector(".sub-btn");
      if (sb) sb.setAttribute("aria-expanded", on ? "true" : "false");
    }
    /* a phone, or any touch screen such as an iPad: tap a section name to
       open its list (a finger cannot hover) */
    var narrow = window.matchMedia ? window.matchMedia("(max-width: 899px), (hover: none), (pointer: coarse)") : { matches: false };
    document.addEventListener("click", function (e) {
      if (!h.contains(e.target)) { closeSubs(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        closeSubs();
        if (h.classList.contains("menu-open")) {
          h.classList.remove("menu-open");
          var mb = h.querySelector(".menu-btn");
          if (mb) { mb.setAttribute("aria-expanded", "false"); mb.focus(); }
        }
      }
    });
    h.addEventListener("click", function (e) {
      var mb = e.target && e.target.closest ? e.target.closest(".menu-btn") : null;
      if (mb) {
        var openNow = !h.classList.contains("menu-open");
        h.classList.toggle("menu-open", openNow);
        mb.setAttribute("aria-expanded", openNow ? "true" : "false");
        if (!openNow) closeSubs();
        return;
      }
      var sbtn = e.target && e.target.closest ? e.target.closest(".sub-btn") : null;
      if (sbtn) { e.preventDefault(); toggleSub(sbtn.parentNode); return; }
      /* On a phone, tapping a section name opens its list instead of leaving
         the page; the section's own page is the first line of that list. */
      var top = e.target && e.target.closest ? e.target.closest(".has-sub > .nav-top") : null;
      if (top && narrow.matches && !top.parentNode.classList.contains("open")) {
        e.preventDefault(); toggleSub(top.parentNode); return;
      }
      var b = e.target && e.target.closest ? e.target.closest("[data-set-lang]") : null;
      if (b) { e.preventDefault(); setLang(b.getAttribute("data-set-lang")); return; }
      var t = e.target && e.target.closest ? e.target.closest("[data-cq-theme]") : null;
      if (t) { e.preventDefault(); toggleTheme(); }
    });

    /* icons — same on every page */
    if (!document.querySelector('link[rel="apple-touch-icon"]')) {
      var a = document.createElement("link");
      a.rel = "apple-touch-icon";
      a.href = BASE + "brand/apple-touch-icon.png?v=e5ca0b50";
      document.head.appendChild(a);
    }
    var ico = document.querySelector('link[rel="icon"]');
    if (!ico) { ico = document.createElement("link"); ico.rel = "icon"; document.head.appendChild(ico); }
    ico.href = BASE + "brand/favicon.svg?v=2e301691";
    ico.type = "image/svg+xml";
  }

  /* ---------------------------------------------------------------
     FLAGS ON WINDOWS
     Windows draws no flag emoji: a Canadian flag shows as the two letters
     "CA", and a flag question in the world quiz cannot be answered. Where the
     browser can draw other emoji but not flags, this adds a small font that
     holds only the flags (fonts/TwemojiCountryFlags.woff2, Twemoji graphics,
     CC BY 4.0; credited on sources.html). Its unicode-range covers flags
     only, so the browser downloads it only on a page that actually shows a
     flag, and every other character keeps the site's own font.
     --------------------------------------------------------------- */
  function fixFlags() {
    try {
      var c = document.createElement("canvas");
      c.width = c.height = 1;
      var x = c.getContext("2d", { willReadFrequently: true });
      x.textBaseline = "top";
      x.font = '100px "Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif';
      x.scale(0.01, 0.01);
      var px = function (t, f) {
        x.clearRect(0, 0, 100, 100); x.fillStyle = f; x.fillText(t, 0, 0);
        return x.getImageData(0, 0, 1, 1).data.join(",");
      };
      /* drawn in colour = the same pixel whatever the fill colour */
      var colour = function (t) { var a = px(t, "#fff"), b = px(t, "#000"); return a === b && b.indexOf("0,0,0,") !== 0; };
      if (!window.CQ_FORCE_FLAGS && (!colour("\ud83d\ude0a") || colour("\ud83c\udde8\ud83c\udde6"))) return;
      var st = document.createElement("style");
      st.textContent = '@font-face{font-family:"Twemoji Country Flags";unicode-range:U+1F1E6-1F1FF,U+1F3F4,' +
        'U+E0062-E0063,U+E0065,U+E0067,U+E006C,U+E006E,U+E0073-E0074,U+E0077,U+E007F;' +
        'src:url("' + BASE + 'fonts/TwemojiCountryFlags.woff2") format("woff2");font-display:swap}' +
        'body,button,input,select,textarea{font-family:"Twemoji Country Flags",-apple-system,BlinkMacSystemFont,' +
        '"Segoe UI",Roboto,"Nunito",Helvetica,Arial,sans-serif}';
      document.head.appendChild(st);
    } catch (e) {}
  }

  /* ---------------------------------------------------------------
     5. GO
     --------------------------------------------------------------- */
  function start() {
    fixFlags();
    if (lang === "fr") {
      document.documentElement.classList.add("lang-fr");
      loadFrench(function () { paint(); translatePage(); watch(); });
    } else {
      paint();
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();

/* Question-bank accordions: Open all / Close all */
(function () {
  function init() {
    document.querySelectorAll(".qbank .qb-openall").forEach(function (btn) {
      var bank = btn.closest(".qbank");
      if (!bank) return;
      btn.setAttribute("aria-expanded", "false");
      btn.addEventListener("click", function () {
        var accs = bank.querySelectorAll("details.qb-acc");
        var anyClosed = Array.prototype.some.call(accs, function (d) { return !d.open; });
        Array.prototype.forEach.call(accs, function (d) { d.open = anyClosed; });
        btn.textContent = anyClosed ? btn.dataset.close : btn.dataset.open;
        btn.setAttribute("aria-expanded", anyClosed ? "true" : "false");
      });
    });
    function openTarget() {
      // A hash is not always a valid CSS selector. The browser percent-encodes
      // anything non-ASCII, so a French page reaching #mélange arrives here as
      // "#m%C3%A9lange" and querySelector throws, killing everything after it
      // in this function. Found 29 September 2026 when the quiz topic slugs
      // started putting real hashes on these pages for the first time.
      var el = null;
      try { el = location.hash && document.querySelector(location.hash); }
      catch (e) {
        try { el = document.getElementById(decodeURIComponent(location.hash.slice(1))); }
        catch (e2) { el = null; }
      }
      while (el) { if (el.tagName === "DETAILS") el.open = true; el = el.parentElement; }
    }
    window.addEventListener("hashchange", openTarget);
    openTarget();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();

/* Quiz play screen — fun and study personalities.
   Engine-agnostic by design. Every quiz engine on this site already emits
   .progress, .quiz-meta, .option, .option.correct/.wrong, .result-big and
   .score, so this reads those rather than hooking into any single engine.
   Nothing here modifies quiz logic; it only adds presentation. */
(function () {
  var FUN = false, ON = false, streak = 0, best = 0, marks = [], celebrated = false;

  function el(tag, cls) { var e = document.createElement(tag); if (cls) e.className = cls; return e; }

  function streakChip(meta) {
    var c = meta.querySelector(".qz-streak");
    if (!c) { c = el("span", "qz-streak"); meta.appendChild(c); }
    return c;
  }
  function paintStreak() {
    if (!FUN) return;
    var metas = document.querySelectorAll(".quiz-meta");
    for (var i = 0; i < metas.length; i++) {
      var c = streakChip(metas[i]);
      var t = streak > 1 ? "🔥 " + streak + " in a row" : (streak === 1 ? "🔥 1" : "⭐ 0");
      if (c.textContent === t) continue;
      c.textContent = t;
      c.classList.add("qz-pop");
      (function (x) { setTimeout(function () { x.classList.remove("qz-pop"); }, 260); })(c);
    }
  }
  function paintPct(bar) {
    var fill = bar.firstElementChild; if (!fill) return;
    var meta = bar.parentNode && bar.parentNode.querySelector(".quiz-meta");
    if (!meta) return;
    var lab = meta.querySelector(".qz-pct");
    if (!lab) { lab = el("span", "qz-pct"); meta.appendChild(lab); }
    var w = parseInt(fill.style.width, 10) || 0;
    var txt = w + "%";
    /* Only write when the value really changed. Writing textContent is itself a
       DOM mutation, so an unconditional write here re-triggers the observer that
       called us and spins forever. */
    if (lab.textContent !== txt) lab.textContent = txt;
  }
  function paintSegs() {
    if (FUN) return;
    var bars = document.querySelectorAll(".progress");
    for (var i = 0; i < bars.length; i++) {
      var bar = bars[i], row = bar.nextElementSibling;
      if (!row || !row.classList || !row.classList.contains("qz-segs")) {
        row = el("div", "qz-segs");
        bar.parentNode.insertBefore(row, bar.nextSibling);
      }
      if (row.childNodes.length === marks.length) continue;
      row.innerHTML = "";
      for (var k = 0; k < marks.length; k++) row.appendChild(el("i", marks[k]));
    }
  }
  function watchBars() {
    var bars = document.querySelectorAll(".progress");
    for (var i = 0; i < bars.length; i++) {
      var bar = bars[i];
      if (bar.__qz || !window.MutationObserver) { paintPct(bar); continue; }
      bar.__qz = 1;
      (function (b) {
        new MutationObserver(function () { paintPct(b); }).observe(b,
          { attributes: true, subtree: true, attributeFilter: ["style"] });
      })(bar);
      paintPct(bar);
    }
  }
  function confetti() {
    var cols = ["#e63946", "#ffb703", "#2a9d8f", "#4895ef", "#f4845f"], box = el("div", "qz-burst");
    for (var n = 0; n < 70; n++) {
      var p = el("i");
      p.style.left = (n * 1.43) % 100 + "vw";
      p.style.top = "-20px";
      p.style.background = cols[n % cols.length];
      p.style.animationDelay = (n % 6) * 0.09 + "s";
      box.appendChild(p);
    }
    document.body.appendChild(box);
    setTimeout(function () { if (box.parentNode) box.parentNode.removeChild(box); }, 2400);
  }
  function checkResult() {
    var r = document.querySelector(".result-big");
    /* Result screen gone again = the visitor started a new round, so clear the
       run. Resetting on progress-width instead would misfire: some engines leave
       their bar at 0% throughout, which wiped the history on every mutation. */
    if (!r || !r.offsetParent) {
      if (celebrated) { celebrated = false; marks = []; streak = 0; best = 0; paintSegs(); paintStreak(); }
      return;
    }
    if (celebrated) return;
    celebrated = true;
    if (!FUN) return;
    var host = r.parentNode;
    if (best > 1 && host && !host.querySelector(".qz-best")) {
      var b = el("span", "qz-best");
      b.textContent = "🔥 Best streak: " + best + " in a row";
      var sc = host.querySelector(".score");
      if (sc && sc.nextSibling) host.insertBefore(b, sc.nextSibling); else host.appendChild(b);
    }
    confetti();
  }
  function init() {
    FUN = document.body.classList.contains("qmode-fun");
    ON = FUN || document.body.classList.contains("qmode-study");
    if (!ON) return;
    watchBars(); paintStreak();
    document.addEventListener("click", function (e) {
      var opt = e.target && e.target.closest && e.target.closest(".option");
      if (!opt) return;
      setTimeout(function () {
        if (opt.classList.contains("correct")) { streak++; if (streak > best) best = streak; marks.push("ok"); }
        else if (opt.classList.contains("wrong")) { streak = 0; marks.push("no"); }
        else return;
        paintStreak(); paintSegs(); watchBars();
      }, 30);
    }, true);
    if (window.MutationObserver) {
      var busy = false;
      new MutationObserver(function () {
        if (busy) return;
        busy = true;
        try { watchBars(); checkResult(); } finally { busy = false; }
      })
        .observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ["style", "class"] });
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
