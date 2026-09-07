/* canada-quiz.com — search across every page.
 *
 * WHY THIS IS NOT A SEARCH ENGINE
 * -------------------------------
 * The site has no server. There is nothing to query. So the whole index — one
 * line per page: address, name, description, section — is built at build time
 * into search-index.json and read once, here, in the browser. About 200 pages
 * in each language, roughly 30 KB, cached like any other file. After the first
 * keystroke nothing touches the network again.
 *
 * That is also why the search works on a school wifi that has died, and why it
 * cannot record what anybody typed: the typing never leaves the page.
 *
 * THE FRENCH SIDE
 * ---------------
 * Every visible string in here is a pair, chosen by the same test the rest of
 * the site uses: is /fr/ in the path. Nothing here goes through the dictionary,
 * because build_fr.py translates text nodes in the HTML and none of this text
 * exists until somebody types.
 *
 * MATCHING
 * --------
 * Accents and case are folded away before comparing, so "quebec" finds
 * "Québec" and "ecole" finds "école" — which matters on a bilingual site where
 * people type on an English keyboard. Every word in the query must appear
 * somewhere in the entry (name, description or section), in any order. A page
 * whose NAME matches sorts above one where only the description does.
 */
(function () {
  "use strict";

  var box = document.getElementById("cq-search");
  if (!box) return;

  var FR = /\/fr\//.test(location.pathname);
  var W = FR ? {
    ph: "Chercher un quiz, un jeu, une province…",
    hint: "Tapez quelques lettres. La recherche se fait dans votre navigateur.",
    none: "Rien ne correspond à « %s ».",
    tryagain: "Essayez un mot plus court, ou parcourez toutes les pages.",
    all: "Toutes les pages",
    one: "1 page",
    many: "%d pages",
    clear: "Effacer",
    inside: "dans la page",
    loading: "Recherche dans le texte des pages…"
  } : {
    ph: "Search for a quiz, a game, a province…",
    hint: "Type a few letters. The search runs inside your browser.",
    none: "Nothing matches “%s”.",
    tryagain: "Try a shorter word, or look through every page.",
    all: "All the pages",
    one: "1 page",
    many: "%d pages",
    clear: "Clear",
    inside: "mentioned on the page",
    loading: "Searching inside the pages…"
  };

  var input = box.querySelector("input");
  var out = box.querySelector(".cq-results");
  var count = box.querySelector(".cq-count");
  var clear = box.querySelector(".cq-clear");
  var data = null, words = null, wordsWanted = false, pending = null;

  input.placeholder = W.ph;
  if (clear) clear.textContent = W.clear;
  count.textContent = W.hint;

  function fold(s) {
    s = String(s).toLowerCase();
    /* Normalize is on every browser that matters; the fallback keeps the
       search working rather than throwing on an old one. */
    if (s.normalize) s = s.normalize("NFD").replace(/[̀-ͯ]/g, "");
    return s.replace(/[’']/g, "'");
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
                    .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function load(then) {
    if (data) { then(); return; }
    var x = new XMLHttpRequest();
    x.open("GET", "search-index.json", true);
    x.onload = function () {
      try { data = JSON.parse(x.responseText); } catch (e) { data = []; }
      for (var i = 0; i < data.length; i++) {
        data[i].f = fold(data[i].t + " " + data[i].d + " " + data[i].g);
        data[i].ft = fold(data[i].t);
      }
      then();
      loadWords();
    };
    x.onerror = function () { data = []; then(); };
    x.send();
  }

  /* THE SECOND FILE, AND WHY IT IS SECOND
     The small index above knows each page's name and description, and answers
     most searches the moment it lands. It cannot see inside a page, so
     "Jean Chrétien" — a name in a table on the prime ministers page — found
     nothing at all.
     words is every word on every page mapped back to the pages carrying it.
     It is about half a megabyte, so it is fetched BEHIND the small one and
     only here, on the search page. While it is still coming the search already
     works; when it arrives the current query is simply run again. */
  function loadWords() {
    if (words || wordsWanted) return;
    wordsWanted = true;
    var x = new XMLHttpRequest();
    x.open("GET", "search-words.json", true);
    x.onload = function () {
      try { words = JSON.parse(x.responseText); } catch (e) { words = {}; }
      if (input.value.trim()) render(input.value.trim());
    };
    x.onerror = function () { words = {}; };
    x.send();
  }

  /* Which pages carry this word. A term is also treated as a prefix, so
     "chret" finds "chretien" while somebody is still typing. */
  function pagesFor(term) {
    if (!words) return null;
    var hit = {};
    if (words[term]) {
      var a = words[term].split(",");
      for (var i = 0; i < a.length; i++) hit[a[i]] = 1;
    }
    if (term.length >= 4) {
      for (var w in words) {
        if (w.length > term.length && w.indexOf(term) === 0) {
          var b = words[w].split(",");
          for (var j = 0; j < b.length; j++) hit[b[j]] = 1;
        }
      }
    }
    return hit;
  }

  function render(q) {
    var terms = fold(q).split(/\s+/).filter(Boolean);
    if (!terms.length) {
      out.innerHTML = "";
      count.textContent = W.hint;
      return;
    }
    /* every term, looked up once in the word index */
    var inside = null;
    if (words) {
      for (var t2 = 0; t2 < terms.length; t2++) {
        var got = pagesFor(terms[t2]);
        if (inside === null) { inside = got; continue; }
        for (var key in inside) { if (!got[key]) delete inside[key]; }
      }
    }

    var hits = [];
    for (var i = 0; i < data.length; i++) {
      var e = data[i], ok = true;
      for (var j = 0; j < terms.length; j++) {
        if (e.f.indexOf(terms[j]) < 0) { ok = false; break; }
      }
      if (ok) {
        /* a name match beats a description match, and an earlier one beats a
           later one, so "flag" puts the flag page first */
        var pos = e.ft.indexOf(terms[0]);
        hits.push([pos < 0 ? 500 : pos, e, false]);
      } else if (inside && inside[i]) {
        /* found in the body of the page, not in its name — worth showing, but
           under everything that matched by name */
        hits.push([1000, e, true]);
      }
    }
    hits.sort(function (a, b) {
      if (a[0] !== b[0]) return a[0] - b[0];
      return a[1].t.localeCompare(b[1].t);
    });

    if (!hits.length) {
      /* the half-megabyte file may still be on its way; say so rather than
         telling somebody their word is not on the site when it may be */
      count.textContent = words ? W.none.replace("%s", q) : W.loading;
      out.innerHTML = '<p class="cq-empty">' + esc(W.tryagain) + " " +
        '<a href="all-pages.html">' + esc(W.all) + "</a></p>";
      return;
    }
    count.textContent = hits.length === 1 ? W.one
                                          : W.many.replace("%d", hits.length);
    var html = [];
    for (var k = 0; k < hits.length && k < 60; k++) {
      var h = hits[k][1];
      html.push('<li><a href="' + esc(h.u) + '">' + esc(h.t) + "</a>" +
                '<span class="cq-sec">' + esc(h.g) + "</span>" +
                (hits[k][2] ? '<span class="cq-in">' + esc(W.inside) + "</span>" : "") +
                "<p>" + esc(h.d) + "</p></li>");
    }
    out.innerHTML = '<ul class="cq-list">' + html.join("") + "</ul>";
  }

  function run() {
    var q = input.value.trim();
    load(function () { render(q); });
    /* the address bar carries the query, so a search can be sent to somebody */
    if (window.history && history.replaceState) {
      var u = location.pathname + (q ? "?q=" + encodeURIComponent(q) : "");
      history.replaceState(null, "", u);
    }
    if (clear) clear.hidden = !q;
  }

  input.addEventListener("input", function () {
    clearTimeout(pending);
    pending = setTimeout(run, 90);
  });
  box.addEventListener("submit", function (e) { e.preventDefault(); run(); });
  if (clear) {
    clear.hidden = true;
    clear.addEventListener("click", function () {
      input.value = "";
      input.focus();
      run();
    });
  }

  var m = /[?&]q=([^&]*)/.exec(location.search);
  if (m) {
    input.value = decodeURIComponent(m[1].replace(/\+/g, " "));
    run();
  }
  /* On a phone the keyboard covering the page before anything is on it is
     worse than one extra tap, so focus only on a wide screen. */
  if (window.matchMedia && window.matchMedia("(min-width:900px)").matches) {
    input.focus();
  }
})();
