/* canada-quiz.com — the quiz block on a province facts page.
 *
 * WHY A QUIZ SITS ON A REFERENCE PAGE
 * -----------------------------------
 * The same reason which-came-first.js exists. Search Console measured it twice:
 * what-is-confederation earns impressions and zero clicks, prime-ministers-of-
 * canada earns impressions and zero clicks. Both state facts, and Google prints
 * facts in its own box above the result. Nobody needs to click through.
 *
 * A page of provincial facts would join them. So the facts are the top of the
 * page and this is the bottom of it: eight questions drawn from what the reader
 * just read. A search engine can print Manitoba's capital. It cannot take the
 * quiz on the reader's behalf.
 *
 * NO ANALYTICS CODE HERE, ON PURPOSE
 * ----------------------------------
 * js/analytics.js already watches for two things sitewide: a click on anything
 * whose class contains "option", and an element with class "result-big"
 * becoming visible. Those fire quiz_start, quiz_answer and quiz_complete across
 * all 218 quiz pages. This file therefore uses those two class names and adds
 * no tracking of its own — one mechanism, not two that can disagree.
 *
 * WHERE THE QUESTIONS COME FROM
 * -----------------------------
 * window.PROV_QUIZ, written into the page by tools/newq/build_province.py. Each
 * question carries both languages, so the French page runs from French text
 * rather than from anything translated at runtime. build_fr.py does not touch
 * script contents, which is exactly why the pair has to travel in the data.
 *
 * Every answer also carries a short "why", because a quiz that only says WRONG
 * teaches nothing. The explanation is the part a teacher actually wants.
 */
(function () {
  "use strict";

  var FR = /\/fr\//.test(location.pathname);
  var bank = window.PROV_QUIZ || [];
  if (!bank.length) return;

  var wrap = document.getElementById("pf-quiz");
  if (!wrap) return;

  var UI = FR ? {
    start:   "Commencer le questionnaire",
    q:       "Question",
    of:      "sur",
    next:    "Question suivante",
    see:     "Voir mon résultat",
    again:   "Recommencer",
    right:   "Bonne réponse !",
    wrong:   "Pas tout à fait.",
    score:   "Votre résultat",
    perfect: "Parfait ! Tu connais le Manitoba.",
    good:    "Bien joué.",
    ok:      "Pas mal — relis le haut de la page et réessaie.",
    low:     "Relis la page, puis réessaie. Tout est là-haut."
  } : {
    start:   "Start the quiz",
    q:       "Question",
    of:      "of",
    next:    "Next question",
    see:     "See my score",
    again:   "Play again",
    right:   "Correct!",
    wrong:   "Not quite.",
    score:   "Your score",
    perfect: "Perfect. You know this place.",
    good:    "Nicely done.",
    ok:      "Not bad — read the top of the page again and retry.",
    low:     "Have another read of the page, then try again. It is all up there."
  };

  function txt(o) { return FR ? o.fr : o.en; }

  var order = [], at = 0, score = 0, locked = false;

  function shuffled(n) {
    var a = [], i, j, t;
    for (i = 0; i < n; i++) a.push(i);
    for (i = a.length - 1; i > 0; i--) {
      j = Math.floor(Math.random() * (i + 1));
      t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function begin() {
    order = shuffled(bank.length);
    at = 0; score = 0;
    ask();
  }

  function ask() {
    locked = false;
    wrap.innerHTML = "";

    var q = bank[order[at]];

    var head = el("p", "muted");
    head.style.margin = "0 0 6px";
    head.style.fontSize = "14px";
    head.textContent = UI.q + " " + (at + 1) + " " + UI.of + " " + bank.length;
    wrap.appendChild(head);

    var h = el("h3", null, txt(q));
    h.style.margin = "0 0 14px";
    wrap.appendChild(h);

    var opts = el("div", "options");
    /* The answers are shuffled too, so the right one is not always in the same
       place — otherwise a second run is a memory test of positions, not facts. */
    var ord = shuffled(q.a.length);
    ord.forEach(function (k) {
      var b = el("button", "option");
      b.type = "button";
      b.textContent = txt(q.a[k]);
      b.addEventListener("click", function () { answer(k === q.c, b, q); });
      opts.appendChild(b);
    });
    wrap.appendChild(opts);

    var fb = el("div", "pf-fb");
    fb.style.marginTop = "14px";
    wrap.appendChild(fb);
  }

  function answer(ok, btn, q) {
    if (locked) return;
    locked = true;
    if (ok) score++;

    var buttons = wrap.querySelectorAll("button.option");
    for (var i = 0; i < buttons.length; i++) buttons[i].disabled = true;
    btn.style.borderColor = ok ? "#1f7a6f" : "#c1121f";
    btn.style.background = ok ? "#eef6f4" : "#fdf0f1";

    var fb = wrap.querySelector(".pf-fb");
    var line = el("p", null, (ok ? UI.right : UI.wrong) + " " + txt(q.why));
    line.style.margin = "0 0 12px";
    fb.appendChild(line);

    var go = el("button", "btn btn-lg");
    go.type = "button";
    go.textContent = (at === bank.length - 1) ? UI.see : UI.next;
    go.addEventListener("click", function () {
      at++;
      if (at >= bank.length) done(); else ask();
    });
    fb.appendChild(go);
  }

  function done() {
    wrap.innerHTML = "";
    var pct = Math.round(score / bank.length * 100);

    /* class "result-big" is what js/analytics.js watches for to fire
       quiz_complete. Do not rename it. */
    var big = el("div", "result-big", score + " / " + bank.length);
    big.style.textAlign = "center";
    wrap.appendChild(big);

    var msg = pct === 100 ? UI.perfect : pct >= 70 ? UI.good : pct >= 40 ? UI.ok : UI.low;
    var p = el("p", null, UI.score + ": " + msg);
    p.style.textAlign = "center";
    wrap.appendChild(p);

    var again = el("button", "btn btn-lg");
    again.type = "button";
    again.textContent = UI.again;
    again.addEventListener("click", begin);
    var holder = el("p", "center");
    holder.style.textAlign = "center";
    holder.appendChild(again);
    wrap.appendChild(holder);
  }

  /* The page ships with a Start button so nothing moves until the reader asks
     for it — a quiz that auto-starts under a wall of facts is a surprise, and
     a reader who came for the capital city should be able to leave with it. */
  var startBtn = el("button", "btn btn-lg");
  startBtn.type = "button";
  startBtn.textContent = UI.start;
  startBtn.addEventListener("click", begin);
  var holder = el("p");
  holder.style.textAlign = "center";
  holder.appendChild(startBtn);
  wrap.appendChild(holder);
})();
