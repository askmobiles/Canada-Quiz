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
    /* THE FOURTH iPad FIX — the one with evidence.

       An on-page log from an iPhone on iOS 18.7 (6 September 2026) showed:
       the first utterance plays, `speaking` goes to 1, and then NOTHING —
       no onstart, no onend, and the flag never clears. Every utterance the
       page starts afterwards reports speaking=1 and makes no sound. The tap
       authorizes one utterance; the ones the page starts on its own are
       refused, silently.

       So on Apple devices the text is never cut up. Cutting was a fix for
       Chrome, which does stop after about fifteen seconds; Apple's engine
       reads long text without complaint. One utterance per tap. */
    if (APPLE) return text ? [text] : [];
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
  /* ------------------------------------------------------------ diagnostics
     The reader has now been "fixed" for the iPad three times from a desk with
     no iPad on it. This log is the fourth approach: the phone tells us what it
     did. Open any story with  #ra-debug  on the end of the address and a panel
     shows every event — start, end, error, the engine's own flags — with times.
     A screenshot of that panel is worth more than another guess. */
  var VERSION = "reader 6 (recorded stories)";
  var LOG = [];
  var logBox = null;
  function log(msg) {
    var s = window.speechSynthesis;
    var line = ((now() % 100000) / 1000).toFixed(1) + "s " + msg +
               "  [spk=" + (s.speaking ? 1 : 0) + " pnd=" + (s.pending ? 1 : 0) + " pau=" + (s.paused ? 1 : 0) + "]";
    LOG.push(line);
    if (LOG.length > 60) LOG.shift();
    if (logBox) logBox.textContent = LOG.join("\n");
  }
  function mountDebug() {
    if (logBox || (location.hash || "").indexOf("ra-debug") < 0) return;
    logBox = document.createElement("pre");
    logBox.setAttribute("data-no-i18n", "");
    logBox.style.cssText = "position:fixed;left:0;right:0;bottom:0;max-height:45vh;overflow:auto;margin:0;padding:8px 10px;" +
      "background:#111;color:#9f9;font:11px/1.35 monospace;z-index:99999;white-space:pre-wrap";
    document.body.appendChild(logBox);
    log(VERSION + " · " + (APPLE ? "apple" : "other") + " · voices=" + voices.length + " · " + navigator.userAgent.slice(0, 60));
  }
  window.addEventListener("hashchange", mountDebug);

  /* ------------------------------------------------- speaking, one at a time

     Nothing is queued: one bite is spoken, and the next is handed over only
     when the engine has finished with the last. What "finished" means, and
     what to do when the engine misbehaves, is where every iPad bug has lived:

       * a bite gets SIX seconds to start — Apple's engine is slow, not broken;
       * finished = onend fired, or the engine reports it stopped after having
         started (Safari often skips onend), or the bite has been "speaking"
         for longer than it could possibly take — Safari can also leave
         `speaking` stuck at true after a bite ends, and a reader that trusts
         that flag waits forever, which reads as "stopped after the first
         paragraph";
       * the next bite is never started from inside the previous one's onend
         handler. WebKit drops a speak() issued during another utterance's end
         event. Every hand-over goes through a short timer;
       * on Apple, if the engine still claims to be busy when we are about to
         speak, it is cleared with cancel() and given a moment to settle first
         — a speak() that follows cancel() too closely is swallowed;
       * a bite that never started is said once more with no voice chosen,
         then skipped rather than blocking the rest of the story;
       * resume() before and after every speak(), because Safari parks the
         engine paused after a cancel. Harmless elsewhere.
  */
  function speakSeq(list, isLive, done) {
    var i = 0, tries = 0, guard = null, cancelled = false, delay = null;

    function stopGuard() {
      if (guard) { clearInterval(guard); guard = null; }
      if (delay) { clearTimeout(delay); delay = null; }
    }
    function alive() { return !cancelled && isLive(); }
    function unpause() { try { if (window.speechSynthesis.paused) window.speechSynthesis.resume(); } catch (e) { } }
    function later(fn, ms) { delay = setTimeout(function () { delay = null; if (alive()) fn(); }, ms); }

    function go() {
      stopGuard();
      if (!alive()) return;
      if (i >= list.length) { log("sequence done"); done && done(); return; }

      var s = window.speechSynthesis;
      /* an engine that says it is busy when nothing of ours is playing is the
         stuck-flag bug; clear it and come back after it has settled */
      if (APPLE && (s.speaking || s.pending) && !going) {
        log("engine busy before speak — cancel and wait");
        try { s.cancel(); } catch (e) { }
        going = true;
        later(function () { going = false; go(); }, 250);
        return;
      }
      going = false;

      var text = list[i];
      var u = utter(text, tries > 0 || voiceBroken);
      var moved = false, started = false, quietSince = 0, startedAt = 0;
      /* the longest this bite could take at this rate, with slack */
      /* Apple never clears `speaking`, so this timer is the only thing that
         ends a story there; it must be longer than the reading could take,
         because ending it early would cancel the audio mid-sentence. */
      var maxMs = 5000 + text.length * (APPLE ? 170 : 120);

      function advance(why) {
        if (moved) return;
        moved = true; stopGuard();
        log("bite " + (i + 1) + "/" + list.length + " done: " + why);
        i++; tries = 0;
        later(go, APPLE ? 120 : 0);
      }
      function failed(why) {
        if (moved) return;
        moved = true; stopGuard();
        log("bite " + (i + 1) + " failed: " + why + (tries ? " — skipping" : " — retry, no voice"));
        if (tries === 0) {
          voiceBroken = true;
          tries = 1;
          try { window.speechSynthesis.cancel(); } catch (e) { }
          later(go, 350);
        } else {
          i++; tries = 0;
          later(go, 120);
        }
      }

      u.onstart = function () { started = true; startedAt = now(); log("onstart " + (i + 1)); };
      u.onend = function () { log("onend " + (i + 1)); advance("onend"); };
      u.onerror = function (e) {
        var kind = (e && e.error) || "?";
        log("onerror " + (i + 1) + ": " + kind);
        if (kind === "interrupted" || kind === "canceled") return;
        failed(kind);
      };

      unpause();
      try { window.speechSynthesis.speak(u); log("speak " + (i + 1) + " (" + text.length + " chars" + (u.voice ? ", voice" : "") + ")"); }
      catch (e) { failed("speak threw"); return; }
      unpause();

      var t0 = now();
      guard = setInterval(function () {
        if (!alive()) { stopGuard(); return; }
        var s = window.speechSynthesis;
        if (started && now() - startedAt > maxMs) { advance("overran " + maxMs + "ms — stuck flag"); return; }
        if (s.speaking) { if (!started) { started = true; startedAt = now(); log("speaking seen " + (i + 1)); } quietSince = 0; return; }
        if (started) {
          if (!quietSince) quietSince = now();
          else if (now() - quietSince > 400) advance("engine quiet");
          return;
        }
        if (now() - t0 > 6000) failed("never started in 6s");
      }, 150);
    }

    var going = false;
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

    if (APPLE) {
      /* one utterance for the whole story (see bites). With no events from
         the engine there is nothing to drive a paragraph highlight, so the
         whole story is marked instead of pretending to know where it is. */
      var all = [];
      for (var k = 0; k < storyParas.length; k++) {
        var tx = (storyParas[k].textContent || "").replace(/\s+/g, " ").trim();
        if (!tx) continue;
        if (!/[.!?…]$/.test(tx)) tx += ".";
        all.push(tx);
        storyParas[k].classList.add("ra-now");
      }
      storyIdx = storyParas.length;
      log("apple: whole story as one utterance, " + all.join(" ").length + " chars");
      storyRun = speakSeq([all.join(" ")], function () { return storyOn; }, function () { stopStory(); });
      return;
    }

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

  /* ------------------------------------------------ a recorded story
     Where the build has recorded the story (audio/stories/<page>-<lang>.mp3,
     made by tools/newq/build_story_audio.py), the page carries an empty
     <div class="ra-audio" data-audio="<page>"> and this turns it into the
     Play button. A file plays on every device, which the speech engine does
     not (see the FOURTH iPad FIX above). The speech engine is still used for
     quizzes, where there are thousands of questions and no files. */
  var audioEl = null, audioBtn = null;

  function fmt(sec) {
    sec = Math.max(0, Math.round(sec || 0));
    return Math.floor(sec / 60) + ":" + (sec % 60 < 10 ? "0" : "") + (sec % 60);
  }

  function mountAudio(host) {
    var slug = host.getAttribute("data-audio");
    if (!slug || host.querySelector("audio")) return false;
    var base = FR ? "../" : "";
    audioEl = document.createElement("audio");
    audioEl.preload = "none";                    /* nothing downloads until Play */
    audioEl.src = base + "audio/stories/" + slug + "-" + (FR ? "fr" : "en") + ".mp3";
    audioBtn = document.createElement("button");
    audioBtn.type = "button";
    audioBtn.className = "ra-btn ra-story btn btn-ghost";
    audioBtn.setAttribute("aria-pressed", "false");
    var time = document.createElement("span");
    time.className = "ra-time";
    function label(state) {
      audioBtn.textContent = state === "playing" ? T("⏸ Pause", "⏸ Pause")
                           : state === "paused" ? T("▶ Keep reading", "▶ Continuer la lecture")
                           : T("🔊 Read the story to me", "🔊 Lis-moi l'histoire");
      audioBtn.appendChild(time);
      audioBtn.setAttribute("aria-pressed", state === "playing" ? "true" : "false");
    }
    label("idle");
    audioBtn.addEventListener("click", function () {
      if (audioEl.paused) {
        stop();                                  /* silence the quiz reader */
        var p = audioEl.play();
        if (p && p.catch) p.catch(function (e) { log("audio play refused: " + e); });
      } else {
        audioEl.pause();
      }
    });
    audioEl.addEventListener("play", function () { label("playing"); log("audio playing " + slug); });
    audioEl.addEventListener("pause", function () { label(audioEl.ended ? "idle" : "paused"); });
    audioEl.addEventListener("ended", function () { label("idle"); clearMark(); log("audio ended"); });
    audioEl.addEventListener("error", function () { label("idle"); log("audio error " + (audioEl.error && audioEl.error.code)); });
    audioEl.addEventListener("timeupdate", function () {
      if (audioEl.duration) {
        time.textContent = " " + fmt(audioEl.currentTime) + " / " + fmt(audioEl.duration);
        markByTime(audioEl.currentTime / audioEl.duration);
      }
    });
    host.appendChild(audioBtn);
    host.appendChild(audioEl);
    return true;
  }

  /* The recording has no idea where paragraph three starts, so the highlight
     follows the clock: the share of the story's characters read so far, plus
     a fixed allowance per sentence for the pause the voice leaves. Close
     enough for a finger to follow; never claimed to be exact. */
  var weights = null;
  function markByTime(frac) {
    if (!storyParas.length) return;
    if (!weights) {
      weights = [];
      for (var i = 0; i < storyParas.length; i++) {
        var tx = (storyParas[i].textContent || "").replace(/\s+/g, " ").trim();
        var sentences = (tx.match(/[.!?…](\s|$)/g) || []).length || 1;
        weights.push(tx.length + sentences * 9);   /* 0.45 s pause ≈ 9 chars */
      }
    }
    var total = 0, i;
    for (i = 0; i < weights.length; i++) total += weights[i];
    var target = frac * total, acc = 0, at = 0;
    for (i = 0; i < weights.length; i++) { acc += weights[i]; if (acc >= target) { at = i; break; } at = i; }
    for (i = 0; i < storyParas.length; i++) storyParas[i].classList.toggle("ra-now", i === at);
  }

  function mountStory() {
    var blocks = document.querySelectorAll(".kid-story");
    if (!blocks.length || document.querySelector(".ra-story")) return;
    /* collect the paragraphs first: the recorded player highlights them too */
    var hostAudio = document.querySelector(".ra-audio");
    if (hostAudio) {
      storyParas = [];
      var lede0 = document.querySelector(".kid-lede");
      if (lede0) storyParas.push(lede0);
      for (var b0 = 0; b0 < blocks.length; b0++) {
        var ps0 = blocks[b0].querySelectorAll("h2, h3, p, .kid-wow");
        for (var i0 = 0; i0 < ps0.length; i0++) storyParas.push(ps0[i0]);
      }
      if (mountAudio(hostAudio)) { log("recorded story mounted"); return; }
    }
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
      if (storyOn) { log("stop tapped"); stopStory(); return; }
      log("read tapped · paragraphs=" + storyParas.length);
      storyOn = true;
      storyIdx = 0;
      storyBtn.textContent = storyLabel();
      storyBtn.setAttribute("aria-pressed", "true");
      speakPara();
    });
    blocks[0].insertBefore(storyBtn, blocks[0].firstChild);
  }

  function start() {
    mountDebug();
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
            ".ra-time{font-weight:600;opacity:.75;font-variant-numeric:tabular-nums}" +
            ".ra-audio audio{display:none}" +
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
