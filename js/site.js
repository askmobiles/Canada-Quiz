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
  var NAV = [
    { href: "index.html",       label: "Home" },
    { href: "quizzes.html",     label: "Quizzes" },
    { href: "games.html",       label: "Family Games" },
    { href: "citizenship.html", label: "Citizenship" },
    { href: "driving-test.html", label: "Driving Test" },
    { href: "daily.html",       label: "Daily" },
    { href: "blog.html",        label: "Blog" }
  ];

  var FOOTER_LINKS = [
    { href: "index.html",   label: "Home" },
    { href: "about.html",   label: "About" },
    { href: "contact.html", label: "Contact" },
    { href: "privacy.html", label: "Privacy Policy" },
    { href: "terms.html",   label: "Terms & Conditions" }
  ];

  var BRAND      = "Canada Quiz & Family Fun Games";
  var FOOTER_TAG = "Free quizzes, family games and citizenship practice — no signup, no ads in your face.";
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
    location.href = next === "fr" ? BASE + "fr/" + file : BASE + file;
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
        node.nodeValue = lead + fr + trail;
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

  function loadFrench(done) {
    var s = document.createElement("script");
    /* the ?v= stamp must match ASSET_VER in tools/rewrite_pages.py, so a new
       dictionary is never served from the visitor's old saved copy */
    s.src = BASE + "js/i18n-fr.js?v=20260807b";
    s.onload = function () { DICT = window.CQ_FR || null; done(); };
    s.onerror = function () { done(); };
    document.head.appendChild(s);
  }

  /* ---------------------------------------------------------------
     4. BUILD THE HEADER + FOOTER (already in the right language)
     --------------------------------------------------------------- */
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function headerHTML() {
    var links = NAV.map(function (n) {
      var on = n.href === file ? ' class="on" aria-current="page"' : "";
      return '<a href="' + n.href + '"' + on + ">" + esc(T(n.label)) + "</a>";
    }).join("");

    var other = lang === "fr" ? "en" : "fr";
    var tip = lang === "fr" ? "Switch to English" : "Passer en français";
    var btn = '<button type="button" class="lang-btn" data-no-i18n data-set-lang="' + other + '"' +
              ' aria-label="' + esc(tip) + '" title="' + esc(tip) + '">' +
              '<span aria-hidden="true">🌐</span> ' + other.toUpperCase() + "</button>";

    return '<div class="container">' +
      '<a class="brand" href="index.html" aria-label="' + esc(BRAND) + '">' +
        '<img src="' + BASE + 'brand/logo-horizontal-white.svg" alt="' + esc(BRAND) +
        '" class="brand-logo" width="230" height="55">' +
      "</a>" +
      '<nav class="nav" aria-label="' + esc(T("Main navigation")) + '">' + links + btn + "</nav>" +
      "</div>";
  }

  function footerHTML() {
    var links = FOOTER_LINKS.map(function (n) {
      return '<a href="' + n.href + '">' + esc(T(n.label)) + "</a>";
    }).join(" · ");
    return '<div class="container center">' +
      '<img src="' + BASE + 'brand/logo-horizontal-white.svg" alt="' + esc(BRAND) +
      '" class="footer-logo" width="200" height="48">' +
      "<p>" + esc(T(FOOTER_TAG)) + "</p>" +
      '<div class="footer-links">' + links + "</div>" +
      '<p class="muted" style="color:#b4a9cc;font-size:12px">' + esc(T(COPYRIGHT)) + "</p>" +
      '<p class="muted" style="color:#b4a9cc;font-size:12.5px">' + esc(T(DISCLAIMER)) + "</p>" +
      "</div>";
  }

  function paint() {
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
      if (window.innerWidth >= 900) map.setAttribute("open", "");
    }
    f.setAttribute("data-no-i18n", "");

    h.addEventListener("click", function (e) {
      var b = e.target && e.target.closest ? e.target.closest("[data-set-lang]") : null;
      if (b) { e.preventDefault(); setLang(b.getAttribute("data-set-lang")); }
    });

    /* icons — same on every page */
    if (!document.querySelector('link[rel="apple-touch-icon"]')) {
      var a = document.createElement("link");
      a.rel = "apple-touch-icon";
      a.href = BASE + "brand/apple-touch-icon.png";
      document.head.appendChild(a);
    }
    var ico = document.querySelector('link[rel="icon"]');
    if (!ico) { ico = document.createElement("link"); ico.rel = "icon"; document.head.appendChild(ico); }
    ico.href = BASE + "brand/favicon.svg";
    ico.type = "image/svg+xml";
  }

  /* ---------------------------------------------------------------
     5. GO
     --------------------------------------------------------------- */
  function start() {
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
