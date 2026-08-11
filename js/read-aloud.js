/* read-aloud.js — a Read aloud button for children who cannot read yet.

   Google's assistant reviewed the site and made one criticism worth acting on:
   the quizzes teach through written explanations, so a child in kindergarten
   or grade one needs an adult beside them to read the screen. This fixes that
   without changing a single quiz.

   How it works, and why this way:

   * The browser's own speechSynthesis does the talking. No account, no server,
     no cost, and on most phones the voice is already on the device, so it
     keeps working with no signal — the same promise as the rest of the site.

   * It does NOT hook into any quiz's code. Twelve quizzes and six driving
     provinces are written twelve different ways; wiring each one would break
     the next time any of them changed. Instead it watches the play area for
     changes and reads whatever question and answers are on screen. A new quiz
     built next year is read aloud with no work at all.

   * It is off until somebody turns it on, and it stays off for everyone else.
     A page that starts talking by itself is a page a teacher closes. The
     choice is remembered per device.

   * Turning it on is also the tap that browsers require before any speech is
     allowed, so the first question speaks immediately rather than silently
     failing the way an autoplaying reader would.

   English or French follows the page, not the device: a French page asks for
   a French voice, and if the device has none it says so rather than reading
   French words in an English accent. */
(function () {
  "use strict";

  if (!("speechSynthesis" in window) || !window.SpeechSynthesisUtterance) return;

  var FR = /\/fr\//.test(location.pathname);
  function T(en, fr) { return FR ? fr : en; }
  var LANG = FR ? "fr-CA" : "en-CA";
  var KEY = "cq_read_aloud";

  /* The three shapes a question takes across the site. Every quiz puts its
     answers in .options; the heading above it is the question. */
  var OPTS = ".options";
  var HEADS = "h1,h2,h3";
  var EXPLAIN = "#explain-box,.explain,.explain-box,#dq-exp,.dq-exp,.result-big";

  var on = false;
  try { on = localStorage.getItem(KEY) === "1"; } catch (e) { }

  /* ------------------------------------------------------------ speaking */
  var lastSaid = "";
  var voices = [];

  function loadVoices() { voices = window.speechSynthesis.getVoices() || []; }
  loadVoices();
  if (typeof speechSynthesis.addEventListener === "function") {
    speechSynthesis.addEventListener("voiceschanged", loadVoices);
  }

  function pickVoice() {
    var want = FR ? "fr" : "en";
    var exact = null, loose = null;
    for (var i = 0; i < voices.length; i++) {
      var l = (voices[i].lang || "").toLowerCase().replace("_", "-");
      if (l === LANG.toLowerCase()) { exact = voices[i]; break; }
      if (!loose && l.indexOf(want) === 0) loose = voices[i];
    }
    return exact || loose || null;
  }

  function stop() {
    try { window.speechSynthesis.cancel(); } catch (e) { }
  }

  function say(text) {
    if (!on || !text) return;
    text = text.replace(/\s+/g, " ").trim();
    if (!text || text === lastSaid) return;
    lastSaid = text;
    stop();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = LANG;
    var v = pickVoice();
    if (v) u.voice = v;
    /* A little slower than default. These are children, and the sentences
       carry the fact being taught. */
    u.rate = 0.92;
    u.pitch = 1;
    try { window.speechSynthesis.speak(u); } catch (e) { }
  }

  /* --------------------------------------------------------- what to read */
  function visible(el) {
    if (!el) return false;
    if (el.closest && el.closest('[style*="display:none"]')) return false;
    return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
  }

  function panelOf(box) {
    return (box.closest && (box.closest(".panel") || box.closest("section"))) || box.parentNode;
  }

  function questionText(box) {
    /* the nearest heading above the answers, inside the same panel */
    var panel = panelOf(box);
    if (!panel) return "";
    var heads = panel.querySelectorAll(HEADS);
    var best = "";
    for (var i = 0; i < heads.length; i++) {
      if (!visible(heads[i])) continue;
      /* only headings that come before the answers */
      if (heads[i].compareDocumentPosition(box) & Node.DOCUMENT_POSITION_FOLLOWING) {
        var t = (heads[i].textContent || "").trim();
        if (t) best = t;
      }
    }
    return best;
  }

  function answersText(box) {
    var out = [];
    var items = box.querySelectorAll("button,.option,li,label");
    for (var i = 0; i < items.length; i++) {
      if (!visible(items[i])) continue;
      var t = (items[i].textContent || "").replace(/\s+/g, " ").trim();
      if (t && out.indexOf(t) < 0) out.push(t);
    }
    return out;
  }

  function readNow(box) {
    var q = questionText(box);
    var a = answersText(box);
    if (!q && !a.length) return;
    /* "Question. Answer one is … Answer two is …" reads badly out loud.
       Numbering them is what a teacher does, and it lets a child say "three"
       instead of repeating the whole sentence back. */
    var parts = [];
    if (q) parts.push(q);
    for (var i = 0; i < a.length; i++) parts.push((i + 1) + ". " + a[i]);
    say(parts.join(". "));
  }

  function readExplanation(panel) {
    var e = panel.querySelector(EXPLAIN);
    if (e && visible(e)) say(e.textContent || "");
  }

  /* ----------------------------------------------------------- the button */
  var btn = null;

  function label() {
    return on ? T("🔊 Reading aloud — tap to stop", "🔊 Lecture à voix haute — touchez pour arrêter")
              : T("🔊 Read aloud", "🔊 Lire à voix haute");
  }

  function mount(box) {
    var panel = panelOf(box);
    if (!panel || panel.querySelector(".ra-btn")) return;
    btn = document.createElement("button");
    btn.type = "button";
    btn.className = "ra-btn btn btn-ghost";
    btn.setAttribute("data-no-i18n", "");
    btn.setAttribute("aria-pressed", on ? "true" : "false");
    btn.textContent = label();
    btn.addEventListener("click", function () {
      on = !on;
      try { localStorage.setItem(KEY, on ? "1" : "0"); } catch (e) { }
      btn.textContent = label();
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      if (!on) { stop(); return; }
      /* the tap that unlocks speech is this one, so read straight away */
      lastSaid = "";
      readNow(box);
    });
    panel.insertBefore(btn, panel.firstChild);
  }

  /* ------------------------------------------------------------- watching */
  function watch(box) {
    var panel = panelOf(box);
    var timer = null;
    var mo = new MutationObserver(function () {
      if (!on) return;
      clearTimeout(timer);
      /* One question redraw fires many mutations. Wait for the dust, then
         read once. Without this a child hears the first word four times. */
      timer = setTimeout(function () {
        if (!visible(box)) return;
        var marked = box.querySelector(".correct,.right,.wrong,.is-correct,[aria-disabled='true']");
        if (marked) readExplanation(panel);
        else readNow(box);
      }, 320);
    });
    mo.observe(panel, { childList: true, subtree: true, characterData: true });
  }

  function start() {
    var boxes = document.querySelectorAll(OPTS);
    if (!boxes.length) return;
    /* one button, on the first answer area — pages have only one at a time */
    mount(boxes[0]);
    for (var i = 0; i < boxes.length; i++) watch(boxes[i]);
    if (on && visible(boxes[0])) readNow(boxes[0]);
  }

  var css = ".ra-btn{display:block;margin:0 auto 12px;font-size:14px;padding:8px 16px}" +
            "@media(max-width:520px){.ra-btn{width:100%;box-sizing:border-box}}";
  var st = document.createElement("style");
  st.textContent = css;
  document.head.appendChild(st);

  /* stop talking when the page is hidden — nobody wants a phone in a bag
     reading a quiz to a pocket */
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stop();
  });
  window.addEventListener("pagehide", stop);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
  /* the driving engine writes its play area after load, so try again */
  window.addEventListener("load", function () { setTimeout(start, 400); });
})();
