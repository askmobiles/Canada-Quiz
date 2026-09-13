/* Canada Quiz — Road Trip Across Canada.

   WHAT THIS IS
   ------------
   A journey, not a quiz. You start on the Pacific and drive east, and every
   province you enter asks you ITS OWN questions, out of that province's own
   bank. Get one wrong and you lose fuel. Run the tank dry and the trip ends
   where you are — in Manitoba, or halfway across Ontario — and that is the
   score: how far you got.

   WHY IT IS BUILT THIS WAY
   ------------------------
   The lesson IS the mechanic. Nobody reads "driving rules are set by each
   province, not by Ottawa" and remembers it. Driving across the country and
   being asked about school buses in Saskatchewan and then about seat belts in
   Quebec teaches it without a sentence of explanation.

   It also costs almost nothing in new content, which is the honest reason it
   was built first: the thirteen banks in js/driving/ already hold 1,417
   questions and EVERY ONE of them already carries its French. Nothing here
   needs the dictionary.

   NOTHING IS DRAWN TWICE
   ----------------------
   The questions come from the province banks. The pictures come from
   window.CQDriveScene, which js/driving-game.js exposes. This file owns the
   journey and nothing else.

   LANGUAGE
   --------
   Same rule as js/driving-engine.js: every word this file prints is stored in
   both languages right here, and the bank entries carry en:{} and fr:{}. A
   French page is therefore never half English, and no dictionary chunk has to
   reach this page at all. */
(function () {
  "use strict";

  var root = document.getElementById("rt");
  if (!root) return;

  var FR = /\/fr\//.test(location.pathname) ||
           document.documentElement.getAttribute("data-lang") === "fr";
  var LANG = FR ? "fr" : "en";
  var BASE = FR ? "../" : "";

  function t(o) { return o[LANG] || o.en; }

  /* ---------------------------------------------------------------- words */
  var S = {
    title:      { en: "Road Trip Across Canada", fr: "Traversée du Canada en voiture" },
    lede:       { en: "Drive east from the Pacific. Every province asks you its own questions — because every province writes its own rules.",
                  fr: "Roulez vers l'est depuis le Pacifique. Chaque province vous pose ses propres questions, parce que chaque province écrit ses propres règles." },
    start:      { en: "Start the trip", fr: "Commencer le voyage" },
    again:      { en: "Drive again", fr: "Reprendre la route" },
    next:       { en: "Keep driving →", fr: "Continuer la route →" },
    fuel:       { en: "Fuel", fr: "Essence" },
    nowIn:      { en: "Now in", fr: "Vous êtes en" },
    nowInTerr:  { en: "Now in", fr: "Vous êtes au" },
    arrived:    { en: "You made it to the Atlantic.", fr: "Vous avez atteint l'Atlantique." },
    ranDry:     { en: "The tank ran dry.", fr: "Le réservoir est vide." },
    gotAsFar:   { en: "You got as far as %1.", fr: "Vous vous êtes rendu jusqu'en %1." },
    crossed:    { en: "%1 of %2 provinces and territories crossed",
                  fr: "%1 provinces et territoires sur %2 traversés" },
    rightPct:   { en: "%1% right", fr: "%1 % de bonnes réponses" },
    best:       { en: "Best so far: %1", fr: "Meilleur résultat : %1" },
    correct:    { en: "Correct", fr: "Bonne réponse" },
    notQuite:   { en: "Not quite", fr: "Pas tout à fait" },
    theAnswer:  { en: "The answer:", fr: "La bonne réponse :" },
    lostFuel:   { en: "You lose one tank of fuel.", fr: "Vous perdez un plein d'essence." },
    loading:    { en: "Loading the next province…", fr: "Chargement de la prochaine province…" },
    failLoad:   { en: "That province's questions could not be loaded. Check your connection and try again.",
                  fr: "Les questions de cette province n'ont pas pu être chargées. Vérifiez votre connexion et réessayez." },
    route:      { en: "Your route", fr: "Votre trajet" },
    look:       { en: "Look at the picture and decide.", fr: "Regardez l'image et décidez." }
  };

  /* ------------------------------------------------------------- the route
     Ten along the Trans-Canada Highway from west to east, then the three
     territories. It is not one single road and the page says so — it is a tour
     of all thirteen, in an order a person could actually drive. */
  var ROUTE = [
    { c: "bc", en: "British Columbia",        fr: "Colombie-Britannique" },
    { c: "ab", en: "Alberta",                 fr: "Alberta" },
    { c: "sk", en: "Saskatchewan",            fr: "Saskatchewan" },
    { c: "mb", en: "Manitoba",                fr: "Manitoba" },
    { c: "on", en: "Ontario",                 fr: "Ontario" },
    { c: "qc", en: "Quebec",                  fr: "Québec" },
    { c: "nb", en: "New Brunswick",           fr: "Nouveau-Brunswick" },
    { c: "ns", en: "Nova Scotia",             fr: "Nouvelle-Écosse" },
    { c: "pe", en: "Prince Edward Island",    fr: "Île-du-Prince-Édouard" },
    { c: "nl", en: "Newfoundland and Labrador", fr: "Terre-Neuve-et-Labrador" },
    { c: "yt", en: "Yukon",                   fr: "Yukon" },
    { c: "nt", en: "Northwest Territories",   fr: "Territoires du Nord-Ouest" },
    { c: "nu", en: "Nunavut",                 fr: "Nunavut" }
  ];
  var PER_STOP = 2;          /* questions asked in each province */
  var START_FUEL = 5;
  var KEY = "cq_roadtrip_best";

  /* --------------------------------------------------------------- state */
  var leg = 0, askedHere = 0, fuel = START_FUEL, right = 0, asked = 0;
  var bank = [], used = {}, cur = null, curScene = null, answered = false;
  var playing = false;

  /* ------------------------------------------------------------ the banks
     Each province file starts with `window.CQ_DRIVE_Q = []`, so loading one
     replaces the last. That is why a province is fetched only when you reach
     it: thirteen banks at once is well over a megabyte, and most trips end
     long before Newfoundland. */
  var loaded = {};
  function loadBank(code, done, fail) {
    if (loaded[code]) { bank = loaded[code]; done(); return; }
    var s = document.createElement("script");
    s.src = BASE + "js/driving/" + code + ".js";
    s.onload = function () {
      var q = window.CQ_DRIVE_Q || [];
      loaded[code] = q.slice();
      bank = loaded[code];
      done();
    };
    s.onerror = fail;
    document.head.appendChild(s);
  }

  /* ----------------------------------------------------------- the screen */
  function el(tag, cls, html) {
    var d = document.createElement(tag);
    if (cls) d.className = cls;
    if (html !== undefined) d.innerHTML = html;
    return d;
  }
  function clear() { root.innerHTML = ""; }

  function roadStrip() {
    var wrap = el("div", "rt-road");
    var i, p;
    for (i = 0; i < ROUTE.length; i++) {
      p = el("span", "rt-stop" + (i < leg ? " done" : (i === leg ? " here" : "")));
      p.setAttribute("title", t(ROUTE[i]));
      if (i === leg) p.innerHTML = "&#128663;";
      wrap.appendChild(p);
    }
    return wrap;
  }

  function hud() {
    var h = el("div", "rt-hud");
    var f = el("div", "rt-fuel");
    f.appendChild(el("span", "rt-lab", t(S.fuel)));
    var i;
    for (i = 0; i < START_FUEL; i++) {
      f.appendChild(el("span", "rt-can" + (i < fuel ? "" : " out"),
                       i < fuel ? "&#9608;" : "&#9617;"));
    }
    h.appendChild(f);
    var pl = el("div", "rt-place");
    pl.innerHTML = "<span class=\"rt-lab\">" + t(S.nowIn) + "</span> <b>" +
                   t(ROUTE[leg]) + "</b>";
    h.appendChild(pl);
    return h;
  }

  /* --------------------------------------------------------- picking a question */
  function pick() {
    var pool = [], i;
    for (i = 0; i < bank.length; i++) {
      if (!used[bank[i].id]) pool.push(bank[i]);
    }
    if (!pool.length) { used = {}; pool = bank.slice(); }
    var q = pool[Math.floor(Math.random() * pool.length)];
    used[q.id] = 1;
    return q;
  }

  /* Ontario is the one leg that can show a drawing. The scenes in
     js/driving/scenes.js are written from the Ontario handbook and each one
     names its chapter, so showing one in Saskatchewan would be telling a
     Saskatchewan learner that Ontario's rules are theirs. They are not. */
  function sceneForLeg() {
    if (ROUTE[leg].c !== "on") return null;
    if (!window.CQDriveScene || !CQDriveScene.scenes || !CQDriveScene.scenes.length) return null;
    var list = CQDriveScene.scenes;
    return list[Math.floor(Math.random() * list.length)];
  }

  /* ------------------------------------------------------------ the rounds */
  function ask() {
    answered = false;
    curScene = (askedHere === 0) ? sceneForLeg() : null;
    clear();
    root.appendChild(roadStrip());
    root.appendChild(hud());

    var card = el("div", "rt-card");
    var text, options, correctIdx;

    if (curScene) {
      /* A scene entry is shaped differently from a bank entry: the picture
         spec is in .sc, the question and each answer carry {en,fr} of their
         own, and the explanation is .why. draw() takes the spec, not the
         entry. */
      var pic = el("div", "rt-pic");
      try { pic.innerHTML = CQDriveScene.draw(curScene.sc); } catch (e) { pic.innerHTML = ""; }
      card.appendChild(pic);
      text = t(curScene.q);
      options = curScene.a.map(function (x) { return t(x); });
      correctIdx = curScene.c;
      cur = { e: t(curScene.why || { en: "", fr: "" }), a: options, c: correctIdx };
    } else {
      var q = pick();
      var d = q[LANG] || q.en;
      text = d.q;
      options = d.a;
      correctIdx = q.c;
      cur = { e: d.e || "", a: options, c: correctIdx };
      /* the shared road-sign drawings, from js/driving/signs.js */
      if (q.sign && window.CQ_SIGNS && CQ_SIGNS[q.sign]) {
        var sp = el("div", "rt-sign");
        sp.innerHTML = CQ_SIGNS[q.sign];
        card.appendChild(sp);
      }
    }

    card.appendChild(el("p", "rt-q", text));
    var opts = el("div", "rt-opts");
    options.forEach(function (a, i) {
      var b = el("button", "rt-opt", a);
      b.type = "button";
      b.onclick = function () { answer(i, b); };
      opts.appendChild(b);
    });
    card.appendChild(opts);
    card.appendChild(el("div", "rt-fb"));
    root.appendChild(card);
  }

  function answer(i, btn) {
    if (answered) return;
    answered = true;
    asked++;
    var good = (i === cur.c);
    var opts = root.querySelectorAll(".rt-opt");
    var k;
    for (k = 0; k < opts.length; k++) {
      opts[k].disabled = true;
      if (k === cur.c) opts[k].className = "rt-opt good";
      else if (k === i) opts[k].className = "rt-opt bad";
    }
    var fb = root.querySelector(".rt-fb");
    if (good) {
      right++;
      fb.innerHTML = '<p class="rt-good"><b>' + t(S.correct) + "</b> " + esc(cur.e) + "</p>";
    } else {
      fuel--;
      fb.innerHTML = '<p class="rt-bad"><b>' + t(S.notQuite) + "</b> " +
                     t(S.lostFuel) + "</p><p class=\"rt-why\"><b>" + t(S.theAnswer) +
                     "</b> " + esc(cur.a[cur.c]) + " — " + esc(cur.e) + "</p>";
      root.querySelector(".rt-hud").replaceWith(hud());
    }
    var go = el("button", "btn btn-lg rt-next", t(S.next));
    go.type = "button";
    go.onclick = advance;
    fb.appendChild(go);
    go.focus({ preventScroll: true });
  }

  function advance() {
    if (fuel <= 0) { finish(false); return; }
    askedHere++;
    if (askedHere >= PER_STOP) {
      askedHere = 0;
      leg++;
      if (leg >= ROUTE.length) { finish(true); return; }
      travel();
      return;
    }
    ask();
  }

  /* ------------------------------------------------------- crossing a border */
  function travel() {
    clear();
    root.appendChild(roadStrip());
    root.appendChild(el("p", "rt-loading", t(S.loading)));
    loadBank(ROUTE[leg].c, function () { used = {}; ask(); }, function () {
      clear();
      root.appendChild(el("p", "rt-bad", t(S.failLoad)));
      var b = el("button", "btn rt-next", t(S.again));
      b.type = "button";
      b.onclick = start;
      root.appendChild(b);
    });
  }

  /* ---------------------------------------------------------------- ending */
  function finish(made) {
    playing = false;
    var crossed = made ? ROUTE.length : leg;
    var pct = asked ? Math.round((right / asked) * 100) : 0;
    var best = 0;
    try { best = parseInt(localStorage.getItem(KEY) || "0", 10) || 0; } catch (e) {}
    if (crossed > best) {
      best = crossed;
      try { localStorage.setItem(KEY, String(best)); } catch (e) {}
    }
    clear();
    root.appendChild(roadStrip());
    var box = el("div", "rt-end");
    box.appendChild(el("p", "rt-endhead", made ? t(S.arrived) : t(S.ranDry)));
    if (!made) {
      box.appendChild(el("p", "rt-endsub",
        t(S.gotAsFar).replace("%1", t(ROUTE[Math.max(0, leg)]))));
    }
    box.appendChild(el("p", "rt-big",
      t(S.crossed).replace("%1", crossed).replace("%2", ROUTE.length)));
    box.appendChild(el("p", "rt-endsub", t(S.rightPct).replace("%1", pct)));
    box.appendChild(el("p", "rt-endsub", t(S.best).replace("%1", best)));
    var b = el("button", "btn btn-lg rt-next", t(S.again));
    b.type = "button";
    b.onclick = start;
    box.appendChild(b);
    root.appendChild(box);
  }

  function esc(s) {
    return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  /* ----------------------------------------------------------------- start */
  function start() {
    leg = 0; askedHere = 0; fuel = START_FUEL; right = 0; asked = 0;
    used = {}; playing = true;
    travel();
  }

  function intro() {
    clear();
    root.appendChild(roadStrip());
    var box = el("div", "rt-end");
    box.appendChild(el("p", "rt-endsub", t(S.lede)));
    var b = el("button", "btn btn-lg rt-next", t(S.start));
    b.type = "button";
    b.onclick = start;
    box.appendChild(b);
    var best = 0;
    try { best = parseInt(localStorage.getItem(KEY) || "0", 10) || 0; } catch (e) {}
    if (best) box.appendChild(el("p", "rt-endsub", t(S.best).replace("%1", best)));
    root.appendChild(box);
  }

  /* ---------- test hook (harmless in production) ----------
     Same idea as window.__mrTest in math-race. Without it a browser test can
     only guess at the answers, runs out of fuel in Manitoba every time, and the
     Ontario leg — the only one that draws a picture — is never reached, so the
     drawing is never looked at. */
  window.__rtTest = {
    correct: function () { return cur ? cur.c : -1; },
    where: function () { return ROUTE[leg] ? ROUTE[leg].c : null; },
    fuel: function () { return fuel; }
  };

  intro();
}());
