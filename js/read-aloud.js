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

  /* ------------------------------------------------- cutting text into bites

     Safari on an iPad and an iPhone will not read a long utterance. Hand it a
     whole paragraph and it stays silent — no error, no sound, and onend often
     never fires either, so a reader that chains one paragraph to the next just
     stops. On an iPad the story reader spoke the headings and skipped every
     paragraph, because headings are short and paragraphs are not. On Android
     and on a computer the same page read fine, which is why it looked like an
     iPad problem rather than a code problem.

     Safari also cuts speech off at roughly fifteen seconds. Both problems go
     away if we never hand it more than a sentence or two at a time, so every
     piece of text is cut into bites of about 140 characters, splitting at a
     full stop where there is one, then at a comma, then at a space. At the
     reading speed used here a bite of that size takes about ten seconds, which
     is comfortably under the cut-off. */
  var MAX = 140;

  function bites(text) {
    text = String(text || "").replace(/\s+/g, " ").trim();
    var out = [];
    while (text.length > MAX) {
      var head = text.slice(0, MAX + 1);
      var cut = Math.max(head.lastIndexOf(". "), head.lastIndexOf("! "),
                         head.lastIndexOf("? "), head.lastIndexOf("; "),
                         head.lastIndexOf(" : "));
      if (cut > 50) cut += 1;
      else {
        cut = Math.max(head.lastIndexOf(", "), head.lastIndexOf(" — "));
        if (cut > 50) cut += 1;
        else {
          cut = head.lastIndexOf(" ");
          if (cut < 30) cut = MAX;          /* one enormous word: cut it anyway */
        }
      }
      out.push(text.slice(0, cut).trim());
      text = text.slice(cut).trim();
    }
    if (text) out.push(text);
    return out;
  }

  /* Apple devices. An iPad in Safari calls itself a Mac, so the touch-point
     count is what tells them apart from a real desktop. */
  var APPLE = /iPhone|iPad|iPod/.test(navigator.userAgent) ||
              (/Macintosh/.test(navigator.userAgent) && navigator.maxTouchPoints > 1);

  /* Set once, the first time a voiced utterance turns out to be silent. After
     that we stop choosing a voice at all and let the device choose. On Apple
     devices we never choose one in the first place: iOS picks a good voice from
     the language on its own, and handing it a voice object it has not finished
     loading is the most reliable way to get silence out of it. */
  var voiceBroken = APPLE;

  /* Every utterance we ever create, kept alive. Safari and Chrome both garbage
     collect an utterance that nothing references while it is still playing —
     and a collected utterance never fires onend, so the reader stops dead at
     the end of that sentence with no error. Holding them here is the fix
     everybody eventually finds. */
  var KEEP = [];

  function utter(text, plain) {
    var u = new SpeechSynthesisUtterance(text);
    u.lang = LANG;
    if (!plain && !voiceBroken) {
      var v = pickVoice();
      if (v) u.voice = v;
    }
    /* A little slower than default. These are children, and the sentences
       carry the fact being taught. */
    u.rate = 0.9;
    u.pitch = 1;
    KEEP.push(u);
    if (KEEP.length > 40) KEEP.splice(0, KEEP.length - 40);
    return u;
  }

  /* ------------------------------------------------- speaking, one at a time

     THE THIRD iPad FIX, and the one that explains the first two.

     Nothing is ever queued: one bite is spoken, and the next is handed over
     only when the engine has finished with the last. The second fix did that,
     and it still stopped after the first paragraph on an iPhone. Here is why.

     It treated "no sound within 0.85 seconds" as a failure, said the bite
     again, and after 0.85 more seconds skipped it. An iPhone or iPad routinely
     takes one to two seconds to start a voice — longer for the first sentence
     after a pause, longer still on an older device. So from the second sentence
     on, every bite was declared dead before it had a chance to begin, repeated,
     and skipped. The first paragraph read because the button tap arrived with
     a longer allowance. Everything after it was silence. The timeouts that
     looked like robustness were the bug.

     Now:

       * a bite gets SIX seconds to start. Apple's engine is slow, not broken;
       * "finished" means onend fired, or the engine reports it stopped after
         having started (Safari often skips onend);
       * a bite that never started is cancelled, and only after a short pause
         is it said once more with no voice chosen — Safari swallows a speak()
         that follows a cancel() too closely, which is what turned the old
         retry into a second silence;
       * Safari also parks the engine in a "paused" state after a cancel, from
         which nothing ever plays again until resume() is called — so resume()
         is called before and after every speak(). It is harmless elsewhere.
  */
  function speakSeq(list, isLive, done) {
    var i = 0, tries = 0, guard = null, cancelled = false, delay = null;

    function stopGuard() {
      if (guard) { clearInterval(guard); guard = null; }
      if (delay) { clearTimeout(delay); delay = null; }
    }
    function alive() { return !cancelled && isLive(); }
    function unpause() { try { if (window.speechSynthesis.paused) window.speechSynthesis.resume(); } catch (e) { } }

    function go() {
      stopGuard();
      if (!alive()) return;
      if (i >= list.length) { done && done(); return; }

      var u = utter(list[i], tries > 0 || voiceBroken);
      var moved = false, started = false, quietSince = 0;

      function advance() {
        if (moved) return;
        moved = true; stopGuard();
        i++; tries = 0;
        go();
      }
      function failed() {
        if (moved) return;
        moved = true; stopGuard();
        if (tries === 0) {
          /* never started: clear whatever Safari is holding, wait for it to
             settle, then say the same bite once more with no voice chosen */
          voiceBroken = true;
          tries = 1;
          try { window.speechSynthesis.cancel(); } catch (e) { }
          delay = setTimeout(function () { delay = null; if (alive()) go(); }, 350);
        } else {
          i++; tries = 0; go();
        }
      }

      u.onstart = function () { started = true; };
      u.onend = advance;
      u.onerror = function (e) {
        /* "interrupted" and "canceled" are us stopping it, not a failure */
        if (e && (e.error === "interrupted" || e.error === "canceled")) return;
        failed();
      };

      unpause();
      try { window.speechSynthesis.speak(u); }
      catch (e) { failed(); return; }
      unpause();

      var t0 = now();
      guard = setInterval(function () {
        if (!alive()) { stopGuard(); return; }
        var s = window.speechSynthesis;
        if (s.speaking) { started = true; quietSince = 0; return; }
        if (started) {
          /* began, and the engine now says it is over. Give onend a moment to
             arrive on its own; if it does not, move on anyway. */
          if (!quietSince) quietSince = now();
          else if (now() - quietSince > 400) advance();
          return;
        }
        if (now() - t0 > 6000) failed();
      }, 150);
    }

    go();
    return { cancel: function () { cancelled = true; stopGuard(); } };
  }

  function now() { return (new Date()).getTime(); }

  var sayer = null;

  function say(text) {
    if (!on || !text) return;
    text = text.replace(/\s+/g, " ").trim();
    if (!text || text === lastSaid) return;
    lastSaid = text;
    var mine = text;
    stop();
    if (sayer) { sayer.cancel(); sayer = null; }
    /* A question plus four answers is easily past the limit on its own, so the
       quiz reader is read one bite at a time as well. The short wait is for
       Safari, which swallows a speak() that follows a cancel() too closely. */
    setTimeout(function () {
      if (!on || lastSaid !== mine) return;
      sayer = speakSeq(bites(text), function () { return on && lastSaid === mine; }, null);
    }, APPLE ? 300 : 0);
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

  /* ------------------------------------------------- reading a whole story */
  /* The For Kids pages are the reason this file exists at all: a six-year-old
     cannot read the story, only the pictures. This reads the story itself,
     paragraph by paragraph, and highlights the one being read so a child can
     follow along with a finger — which is how children learn to read. */
  var storyOn = false, storyIdx = 0, storyParas = [], storyBtn = null;

  function storyLabel() {
    return storyOn ? T("⏹ Stop reading", "⏹ Arrêter la lecture")
                   : T("🔊 Read the story to me", "🔊 Lis-moi l'histoire");
  }

  function clearMark() {
    for (var i = 0; i < storyParas.length; i++) storyParas[i].classList.remove("ra-now");
  }

  var storyRun = null;

  function stopStory() {
    storyOn = false;
    clearMark();
    if (storyRun) { storyRun.cancel(); storyRun = null; }
    stop();
    if (storyBtn) {
      storyBtn.textContent = storyLabel();
      storyBtn.setAttribute("aria-pressed", "false");
    }
  }

  function speakPara() {
    if (!storyOn) return;
    if (storyRun) { storyRun.cancel(); storyRun = null; }
    clearMark();
    if (storyIdx >= storyParas.length) { stopStory(); return; }

    var el = storyParas[storyIdx];
    el.classList.add("ra-now");
    /* keep the highlighted paragraph on screen without yanking the page */
    try { el.scrollIntoView({ block: "center", behavior: "smooth" }); } catch (e) { }

    var parts = bites(el.textContent);
    if (!parts.length) { storyIdx++; speakPara(); return; }

    var mine = storyIdx;
    storyRun = speakSeq(
      parts,
      function () { return storyOn && storyIdx === mine; },
      function () { storyIdx++; speakPara(); }
    );
  }

  function mountStory() {
    var blocks = document.querySelectorAll(".kid-story");
    if (!blocks.length || document.querySelector(".ra-story")) return;
    storyParas = [];
    var lede = document.querySelector(".kid-lede");
    if (lede) storyParas.push(lede);
    /* The long stories are several .kid-story sections, not one. Reading only
       the first meant a child heard a quarter of the story and then silence.
       Headings are read too: they are how a child hears the story turn. */
    for (var b = 0; b < blocks.length; b++) {
      var ps = blocks[b].querySelectorAll("h2, h3, p, .kid-wow");
      for (var i = 0; i < ps.length; i++) storyParas.push(ps[i]);
    }
    var wow = document.querySelector(".kid-wow");
    if (wow && storyParas.indexOf(wow) < 0) storyParas.push(wow);
    if (!storyParas.length) return;

    storyBtn = document.createElement("button");
    storyBtn.type = "button";
    storyBtn.className = "ra-btn ra-story btn btn-ghost";
    storyBtn.setAttribute("data-no-i18n", "");
    storyBtn.setAttribute("aria-pressed", "false");
    storyBtn.textContent = storyLabel();
    storyBtn.addEventListener("click", function () {
      if (storyOn) { stopStory(); return; }
      storyOn = true;
      storyIdx = 0;
      storyBtn.textContent = storyLabel();
      storyBtn.setAttribute("aria-pressed", "true");
      speakPara();
    });
    blocks[0].insertBefore(storyBtn, blocks[0].firstChild);
  }

  function start() {
    mountStory();
    var boxes = document.querySelectorAll(OPTS);
    if (!boxes.length) return;
    /* one button, on the first answer area — pages have only one at a time */
    mount(boxes[0]);
    for (var i = 0; i < boxes.length; i++) watch(boxes[i]);
    if (on && visible(boxes[0])) readNow(boxes[0]);
  }

  var css = ".ra-btn{display:block;margin:0 auto 12px;font-size:14px;padding:8px 16px}" +
            ".ra-story{margin-bottom:16px}" +
            /* the paragraph being read, so a child can follow with a finger */
            ".ra-now{background:#fff3c4;border-radius:10px;box-shadow:0 0 0 8px #fff3c4}" +
            "@media(prefers-reduced-motion:reduce){.ra-now{transition:none}}" +
            "@media(max-width:520px){.ra-btn{width:100%;box-sizing:border-box}}";
  var st = document.createElement("style");
  st.textContent = css;
  document.head.appendChild(st);

  /* stop talking when the page is hidden — nobody wants a phone in a bag
     reading a quiz to a pocket */
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stopStory();
  });
  window.addEventListener("pagehide", stopStory);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
  /* the driving engine writes its play area after load, so try again */
  window.addEventListener("load", function () { setTimeout(start, 400); });
})();
