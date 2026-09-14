/* Read the Road — the road-sign game for people who are not taking a test.
 * -----------------------------------------------------------------------
 * WHY THIS EXISTS
 *
 * The site already had eighty road signs drawn, named in both languages, and
 * 120 sourced questions about them — all of it locked behind pages built for
 * someone studying for a G1. That leaves out almost everybody who needs to read
 * a sign: the grandmother who walks to the plaza and takes the bus, the child
 * walking to school, the parent who has driven for twenty years and has never
 * once been asked what a flashing amber actually means.
 *
 * So this is the same knowledge with the door open. Four ways in:
 *
 *   name  Name the sign      — recognition. The picture, four names.
 *   act   What do you do?     — meaning. The real MTO questions, which ask what
 *                               you should DO, because knowing a sign is called
 *                               a crossover is worth nothing at the kerb.
 *   kids  The walk to school  — twenty-eight signs a child meets, in a child's
 *                               words, each with one line they can repeat to a
 *                               grown-up. That line is the teaching.
 *   two   Pass the phone      — two players, two scores side by side. A child
 *                               and a grandparent can play the same round.
 *
 * WHERE THE CONTENT COMES FROM — nothing invented here
 *   CQ_SIGNS       js/driving/signs.js     80 original drawings
 *   CQ_SIGN_META   js/driving/signs.js     names + category, EN and FR
 *   CQ_DRIVE_Q     js/driving/on.js        sign questions, written from the
 *                                          free official MTO Driver's Handbook
 *   CQ_KID_SIGNS   js/driving/kid-signs.js the child's wording
 *
 * WRONG ANSWERS COME FROM THE SAME FAMILY
 * A round where the real answer is the only warning sign among three
 * information signs teaches colour-matching, not signs. Every wrong name is
 * pulled from the same category as the right one, so the question stays a
 * question.
 *
 * Both languages live in this file, because every string here is built by a
 * script after the page loads and build_fr.py never sees those. Same rule as
 * js/word-banks.js and js/driving-map.js.
 */
(function () {
  "use strict";

  var host = document.getElementById("rr-game");
  if (!host) return;

  var FR = /(^|\/)fr\//.test(location.pathname);
  var SIGNS = window.CQ_SIGNS || {};
  var META = window.CQ_SIGN_META || {};
  var KIDS = window.CQ_KID_SIGNS || [];
  var QS = [];

  /* The Ontario question bank is 235 KB — bigger than everything else on this
     page put together, and two of the four games never touch it. A family
     opening this on a phone to name signs with a child should not pay for it.
     So it is fetched the first time a mode actually needs it, the same way the
     road trip fetches a province only when you arrive there. */
  /* Works out ../js/ vs js/ by reading a script tag build_fr.py has already
     corrected, rather than guessing from the URL. */
  function bankPath() {
    var tags = document.getElementsByTagName("script");
    for (var i = 0; i < tags.length; i++) {
      var src = tags[i].getAttribute("src") || "";
      var m = src.match(/^(.*?)js\/driving\/signs\.js/);
      if (m) return m[1] + "js/driving/on.js";
    }
    return (FR ? "../" : "") + "js/driving/on.js";
  }

  var bankState = 0;                       // 0 none, 1 loading, 2 ready
  function loadBank(then) {
    if (bankState === 2) { then(); return; }
    if (bankState === 1) { bankWaiting.push(then); return; }
    bankState = 1;
    bankWaiting = [then];
    var sc = document.createElement("script");
    /* The French twin lives one folder down, and build_fr.py rewrites the src of
       every <script> in the HTML to "../js/…" — but it cannot rewrite a path a
       script builds at run time. Without the prefix this 404s on the French page
       and the mode silently falls back to naming signs, which is exactly what it
       did the first time. Take the prefix from a tag the build already fixed. */
    sc.src = bankPath();
    sc.onload = function () {
      QS = (window.CQ_DRIVE_Q || []).filter(function (q) {
        return q.sec === "signs" && q.sign && SIGNS[q.sign];
      });
      bankState = 2;
      bankWaiting.forEach(function (f) { f(); });
      bankWaiting = [];
    };
    /* If it will not load, the game still works — it falls back to naming
       signs rather than showing a broken screen. */
    sc.onerror = function () {
      bankState = 2; QS = [];
      bankWaiting.forEach(function (f) { f(); });
      bankWaiting = [];
    };
    document.head.appendChild(sc);
  }
  var bankWaiting = [];

  var ROUND = 10;

  var W = FR ? {
    pick: "Choisissez un jeu",
    modeName: "Nommez le panneau",
    modeNameSub: "Regardez le panneau, choisissez son nom",
    modeAct: "Que faites-vous ?",
    modeActSub: "Ce que le panneau vous demande de faire",
    modeKids: "Le chemin de l'école",
    modeKidsSub: "Pour les enfants — 28 panneaux, en mots simples",
    modeTwo: "Passez le téléphone",
    modeTwoSub: "À deux, chacun son tour",
    right: "Score",
    correct: "Justes",
    percent: "Justes",
    q: "Question",
    of: "sur",
    nameQ: "Quel est ce panneau ?",
    kidQ: "Que veut dire ce panneau ?",
    next: "Suivant →",
    good: "Bonne réponse",
    bad: "Pas tout à fait",
    again: "Rejouer",
    other: "Choisir un autre jeu",
    result: "Votre résultat",
    p1: "Joueur 1",
    p2: "Joueur 2",
    turnOf: "Au tour de",
    winner: "gagne !",
    tie: "Égalité !",
    namePlease: "Écrivez les deux noms, puis commencez.",
    start: "Commencer",
    teach: "Dites cette phrase à voix haute à quelqu'un. C'est comme cela qu'on enseigne.",
    notOfficial: "Pratique gratuite. Aucun lien avec un gouvernement.",
    loading: "Un instant\u2026"
  } : {
    pick: "Pick a game",
    modeName: "Name the sign",
    modeNameSub: "Look at the sign, choose its name",
    modeAct: "What do you do?",
    modeActSub: "What the sign is asking you to do",
    modeKids: "The walk to school",
    modeKidsSub: "For children — 28 signs, in simple words",
    modeTwo: "Pass the phone",
    modeTwoSub: "Two players, taking turns",
    right: "Score",
    correct: "Correct",
    percent: "Correct",
    q: "Question",
    of: "of",
    nameQ: "What is this sign?",
    kidQ: "What does this sign tell you?",
    next: "Next →",
    good: "Correct",
    bad: "Not quite",
    again: "Play again",
    other: "Pick another game",
    result: "Your result",
    p1: "Player 1",
    p2: "Player 2",
    turnOf: "Turn:",
    winner: "wins!",
    tie: "A tie!",
    namePlease: "Put in both names, then start.",
    start: "Start",
    teach: "Say that line out loud to somebody. That is the teaching.",
    notOfficial: "Free practice. Not affiliated with any government.",
    loading: "One moment\u2026"
  };

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function rnd(n) { return Math.floor(Math.random() * n); }
  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = rnd(i + 1); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  function name(id) { var m = META[id]; return m ? (FR ? m.fr : m.en) : id; }
  function art(id) { return '<div class="rr-art">' + (SIGNS[id] || "") + "</div>"; }

  /* ---- question makers ------------------------------------------------- */

  var idsByCat = {};
  Object.keys(META).forEach(function (id) {
    if (!SIGNS[id]) return;
    (idsByCat[META[id].cat] = idsByCat[META[id].cat] || []).push(id);
  });
  var allIds = Object.keys(META).filter(function (id) { return SIGNS[id]; });

  /* Name the sign: three wrong names from the same category, so the colour and
     the shape cannot give the answer away on their own. */
  function qName() {
    var id = allIds[rnd(allIds.length)];
    var pool = (idsByCat[META[id].cat] || []).filter(function (x) { return x !== id; });
    if (pool.length < 3) pool = allIds.filter(function (x) { return x !== id; });
    var wrong = shuffle(pool).slice(0, 3);
    var opts = shuffle([id].concat(wrong));
    return {
      art: id,
      q: W.nameQ,
      opts: opts.map(name),
      c: opts.indexOf(id),
      e: ""
    };
  }

  /* What do you do: a real sign question, already sourced and already bilingual. */
  function qAct() {
    if (!QS.length) return qName();
    var q = QS[rnd(QS.length)];
    var L = FR ? q.fr : q.en;
    var order = shuffle(L.a.map(function (t, i) { return i; }));
    return {
      art: q.sign,
      q: L.q,
      opts: order.map(function (i) { return L.a[i]; }),
      c: order.indexOf(q.c),
      e: L.e
    };
  }

  /* The walk to school: the child's own wording, with three wrong lines taken
     from other child signs so every option is readable by the same child. */
  function qKid() {
    if (!KIDS.length) return qName();
    var k = KIDS[rnd(KIDS.length)];
    var pool = KIDS.filter(function (x) { return x.id !== k.id; });
    var wrong = shuffle(pool).slice(0, 3);
    var all = shuffle([k].concat(wrong));
    var txt = function (x) { return (FR ? x.fr : x.en)[0]; };
    return {
      art: k.id,
      q: W.kidQ,
      opts: all.map(txt),
      c: all.indexOf(k),
      e: (FR ? k.fr : k.en)[1],
      teach: true
    };
  }

  var MAKE = { name: qName, act: qAct, kids: qKid };

  /* ---- state ----------------------------------------------------------- */

  var mode = null, asked = 0, right = 0, cur = null, answered = false;
  var two = false, turn = 0, names = ["", ""], score = [0, 0];

  function pct() { return asked ? Math.round(right * 100 / asked) : 0; }

  /* ---- screens --------------------------------------------------------- */

  function menu() {
    mode = null; two = false;
    var cards = [
      ["name", "&#128064;", W.modeName, W.modeNameSub],
      ["act", "&#128663;", W.modeAct, W.modeActSub],
      ["kids", "&#127890;", W.modeKids, W.modeKidsSub],
      ["two", "&#128241;", W.modeTwo, W.modeTwoSub]
    ];
    host.innerHTML =
      '<h2 class="rr-h">' + esc(W.pick) + "</h2>" +
      '<div class="rr-modes">' +
      cards.map(function (c) {
        return '<button type="button" class="rr-mode" data-mode="' + c[0] + '">' +
               '<span class="rr-emoji" aria-hidden="true">' + c[1] + "</span>" +
               '<span class="rr-mode-t">' + esc(c[2]) + "</span>" +
               '<span class="rr-mode-s">' + esc(c[3]) + "</span></button>";
      }).join("") + "</div>";
    host.setAttribute("data-no-i18n", "");
    Array.prototype.forEach.call(host.querySelectorAll(".rr-mode"), function (b) {
      b.onclick = function () {
        if (b.getAttribute("data-mode") === "two") twoSetup();
        else start(b.getAttribute("data-mode"));
      };
    });
  }

  function twoSetup() {
    host.innerHTML =
      '<h2 class="rr-h">' + esc(W.modeTwo) + "</h2>" +
      '<p class="muted">' + esc(W.namePlease) + "</p>" +
      '<div class="rr-names">' +
      '<input class="rr-in" id="rr-n1" maxlength="14" placeholder="' + esc(W.p1) + '">' +
      '<input class="rr-in" id="rr-n2" maxlength="14" placeholder="' + esc(W.p2) + '">' +
      "</div>" +
      '<div class="center"><button class="btn" id="rr-go">' + esc(W.start) + "</button> " +
      '<button class="btn btn-ghost" id="rr-back">' + esc(W.other) + "</button></div>";
    host.querySelector("#rr-go").onclick = function () {
      names[0] = host.querySelector("#rr-n1").value.trim() || W.p1;
      names[1] = host.querySelector("#rr-n2").value.trim() || W.p2;
      two = true; turn = 0; score = [0, 0];
      start("name");
    };
    host.querySelector("#rr-back").onclick = menu;
  }

  function start(m) {
    mode = m; asked = 0; right = 0;
    if (!two) { score = [0, 0]; }
    /* Only these two ask what you would DO, so only these two need the bank. */
    if (m === "act" || two) {
      host.innerHTML = '<p class="rr-loading">' + esc(W.loading) + "</p>";
      loadBank(deal);
    } else {
      deal();
    }
  }

  /* In two-player the question type rotates, so neither player can settle into
     one kind and neither gets an easier round than the other. */
  function pickMaker() {
    if (!two) return MAKE[mode];
    return [qName, qKid, qAct][asked % 3];
  }

  function deal() {
    answered = false;
    cur = pickMaker()();
    var total = two ? ROUND * 2 : ROUND;

    var head = two
      ? '<div class="rr-turn">' + esc(W.turnOf) + " <b>" + esc(names[turn]) + "</b></div>" +
        '<div class="rr-scores"><div class="rr-score"><span>' + esc(names[0]) + "</span>" + score[0] + "</div>" +
        '<div class="rr-score"><span>' + esc(names[1]) + "</span>" + score[1] + "</div></div>"
      : '<div class="rr-scores"><div class="rr-score"><span>' + esc(W.right) + "</span>" + right + " / " + asked + "</div>" +
        '<div class="rr-score"><span>' + esc(W.percent) + "</span>" + pct() + "%</div></div>";

    host.innerHTML = head +
      art(cur.art) +
      '<p class="rr-count">' + esc(W.q) + " " + (asked + 1) + " " + esc(W.of) + " " + total + "</p>" +
      '<p class="rr-q">' + esc(cur.q) + "</p>" +
      '<div class="rr-opts">' +
      cur.opts.map(function (o, i) {
        return '<button type="button" class="rr-opt" data-i="' + i + '">' + esc(o) + "</button>";
      }).join("") + "</div>" +
      '<p class="rr-fb" id="rr-fb"></p>' +
      '<div class="center rr-after" id="rr-after"></div>';

    Array.prototype.forEach.call(host.querySelectorAll(".rr-opt"), function (b) {
      b.onclick = function () { answer(+b.getAttribute("data-i"), b); };
    });
  }

  function answer(i, btn) {
    if (answered) return;
    answered = true;
    asked++;
    var win = i === cur.c;
    var opts = host.querySelectorAll(".rr-opt");
    for (var j = 0; j < opts.length; j++) {
      opts[j].disabled = true;
      if (j === cur.c) opts[j].classList.add("win");
    }
    if (!win) btn.classList.add("lose");

    if (win) { right++; if (two) score[turn]++; }

    var fb = host.querySelector("#rr-fb");
    fb.className = "rr-fb " + (win ? "ok" : "no");
    var line = win ? W.good : W.bad;
    /* The child's meaning line shows whether they were right or wrong — being
       wrong is exactly when you want to read what it means. */
    if (cur.e) line += " — " + cur.e;
    fb.textContent = line;

    if (cur.teach) {
      var t = document.createElement("span");
      t.className = "rr-teach";
      t.textContent = W.teach;
      fb.appendChild(document.createElement("br"));
      fb.appendChild(t);
    }

    if (two) turn = 1 - turn;

    var total = two ? ROUND * 2 : ROUND;
    var after = host.querySelector("#rr-after");
    if (asked >= total) {
      var b = document.createElement("button");
      b.className = "btn";
      b.textContent = W.next;
      b.onclick = result;
      after.appendChild(b);
    } else {
      var n = document.createElement("button");
      n.className = "btn";
      n.textContent = W.next;
      n.onclick = deal;
      after.appendChild(n);
    }
  }

  function result() {
    var h;
    if (two) {
      var who = score[0] === score[1] ? null : (score[0] > score[1] ? 0 : 1);
      h = '<h2 class="rr-h">' + esc(W.result) + "</h2>" +
          '<div class="rr-scores big"><div class="rr-score"><span>' + esc(names[0]) + "</span>" + score[0] + "</div>" +
          '<div class="rr-score"><span>' + esc(names[1]) + "</span>" + score[1] + "</div></div>" +
          '<p class="rr-big">' + (who === null ? esc(W.tie) : esc(names[who]) + " " + esc(W.winner)) + "</p>";
    } else {
      h = '<div class="rr-big">' + pct() + "%</div>" +
          '<p class="rr-sub">' + right + " / " + asked + " " + esc(W.correct) + "</p>";
    }
    host.innerHTML = h +
      '<div class="center rr-after">' +
      '<button class="btn" id="rr-again">' + esc(W.again) + "</button> " +
      '<button class="btn btn-ghost" id="rr-menu">' + esc(W.other) + "</button></div>" +
      '<p class="muted rr-note">' + esc(W.notOfficial) + "</p>";
    host.querySelector("#rr-again").onclick = function () {
      if (two) { turn = 0; score = [0, 0]; }
      start(mode);
    };
    host.querySelector("#rr-menu").onclick = menu;
  }

  menu();
}());
