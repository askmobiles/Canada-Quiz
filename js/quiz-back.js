/* canada-quiz.com — the Back button on the multi-topic quiz pages.
 *
 * The problem, reported 28 September 2026 from an iPad: on money-quiz.html and
 * its eight siblings the topic list and the quiz are the same page. Tapping a
 * topic's Start button hides one block and shows another — the browser never
 * navigates, so nothing enters history and the address bar still reads
 * money-quiz.html no matter which of the six topics you are in. Press Back and
 * the browser does the only thing it can: leaves for whatever came before the
 * page, usually quizzes.html. The player loses their place and lands two levels
 * out.
 *
 * The fix is to give each topic a real address. Starting a topic pushes
 * #topic-slug, so Back returns to the topic cards instead of leaving, the
 * address bar says where you are, and the address can be sent to somebody else
 * and opened straight into that topic.
 *
 * This file is deliberately generic and attaches itself to whatever the page
 * already has, because the nine pages are hand-written and come in three
 * shapes:
 *
 *   seven pages   startCat(name)         + backToCats()   screens start-screen/quiz-screen/result-screen
 *   canada-quiz   startCat(name)         + no back at all  screens start/quiz/result
 *   gk-quiz       startCat(name, label)  + backToStart()   screens start/quiz/result
 *
 * Nothing here is added to a page that has no startCat, so rewrite_pages.py can
 * hang it on the quiz pages only and it stays inert everywhere else.
 *
 * It adds no visible words, which is on purpose: the French pages get the
 * behaviour for free without a single entry in the dictionary, and a topic slug
 * is derived from the heading the page itself prints, so the French page slugs
 * come out French without anything being translated.
 */
(function () {
  "use strict";

  if (typeof window.startCat !== "function") return;

  var startScreen = document.getElementById("start-screen")
                 || document.getElementById("start");

  /* the page's own "show me the topic list again" function, before we wrap it */
  var origBack = (typeof window.backToCats === "function" && window.backToCats)
              || (typeof window.backToStart === "function" && window.backToStart)
              || null;

  /* true while WE are driving startCat — stops a restore pushing a second
     history entry and trapping the player in a loop of their own Back presses */
  var restoring = false;

  /* Slugs stay plain ASCII on purpose. A French topic like "Mélange" would
     otherwise reach the address bar as "#m%C3%A9lange" — the browser
     percent-encodes it — and that string is neither a valid CSS selector nor
     equal to the slug we compared it against. It becomes "melange" instead:
     readable, shareable, and the same on both sides of the comparison. */
  function slugOf(s) {
    var t = String(s == null ? "" : s);
    if (t.normalize) t = t.normalize("NFD").replace(/[̀-ͯ]/g, "");
    return t.toLowerCase()
      .replace(/['’]/g, "")          // don't turn "Canada's" into "canada-s"
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");
  }

  function currentSlug() {
    try { return decodeURIComponent(location.hash.slice(1)); }
    catch (e) { return location.hash.slice(1); }
  }

  function cards() {
    var root = startScreen || document;
    return Array.prototype.slice.call(root.querySelectorAll(".card"));
  }

  /* Open a topic by clicking its own Start button rather than calling startCat
     directly. The three page shapes pass different arguments — gk-quiz wants
     (name, label) — and the button already closes over the right ones. */
  function openTopic(slug) {
    var hit = null;
    cards().forEach(function (c) {
      var h = c.querySelector("h3");
      var b = c.querySelector("button");
      if (h && b && slugOf(h.textContent) === slug) hit = b;
    });
    if (!hit) return false;
    restoring = true;
    try { hit.click(); } finally { restoring = false; }
    return true;
  }

  function showList() {
    /* startCat adds this to hide the written-out answers while a test is in
       progress. finish() takes it off, but a player who presses Back in the
       middle of a round never reaches finish(), so take it off here too. */
    document.body.classList.remove("quiz-live");
    if (origBack) { origBack(); return; }
    ["result-screen", "quiz-screen", "result", "quiz"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.style.display = "none";
    });
    if (startScreen) startScreen.style.display = "block";
    window.scrollTo(0, 0);
  }

  function bare() {
    return location.pathname + location.search;
  }

  /* --- which card did the player actually tap? ---------------------------
     The address has to come from the heading the card PRINTS, not from what
     startCat is handed. On the French pages those differ: js/quiz-cats-fr.js
     puts "Argent canadien" on the card while startCat still receives the
     English BANK key "Canadian Money". Slugging the argument gave
     #canadian-money, and then restoring — which finds a topic by its heading —
     looked for "argent-canadien" and found nothing, so Forward and shared links
     both died quietly. Caught 29 September 2026 by testing the French pages.
     Listening in the capture phase means this runs before the button's own
     onclick reaches startCat. */
  var tapped = "";
  document.addEventListener("click", function (e) {
    var el = e.target;
    while (el && el !== document) {
      if (el.classList && el.classList.contains("card")) {
        var h = el.querySelector("h3");
        tapped = h ? slugOf(h.textContent) : "";
        return;
      }
      el = el.parentNode;
    }
    tapped = "";
  }, true);

  /* --- starting a topic now adds an address ------------------------------ */
  var origStart = window.startCat;
  window.startCat = function () {
    var out = origStart.apply(this, arguments);
    if (!restoring) {
      /* the tapped card's heading first; failing that, gk-quiz passes
         (name, label) and the label is what its card prints, and everywhere
         else the first argument is the printed name */
      var slug = tapped || slugOf(arguments.length > 1 && arguments[1]
                                  ? arguments[1] : arguments[0]);
      if (slug && currentSlug() !== slug) {
        history.pushState({ cqTopic: slug }, "", "#" + slug);
      }
    }
    tapped = "";
    return out;
  };

  /* --- the page's own back button clears the address to match ------------- */
  function wrapBack(name) {
    if (typeof window[name] !== "function") return;
    var fn = window[name];
    window[name] = function () {
      var out = fn.apply(this, arguments);
      document.body.classList.remove("quiz-live");
      if (location.hash) history.pushState({ cqTopic: null }, "", bare());
      return out;
    };
  }
  wrapBack("backToCats");
  wrapBack("backToStart");

  /* --- Back and Forward -------------------------------------------------- */
  window.addEventListener("popstate", function () {
    var slug = currentSlug();
    if (!slug) { showList(); return; }
    if (!openTopic(slug)) showList();
  });

  /* --- somebody opened a link straight to one topic ----------------------- */
  /* The cards are built by the page's own script, and on gk-quiz that happens
     after its question bank loads, so try again for a couple of seconds rather
     than giving up on the first miss. */
  function deepLink(tries) {
    var slug = currentSlug();
    if (!slug) return;
    if (openTopic(slug)) return;
    if (tries > 0) setTimeout(function () { deepLink(tries - 1); }, 150);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { deepLink(14); });
  } else {
    deepLink(14);
  }
})();
