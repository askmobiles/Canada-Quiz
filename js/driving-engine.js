/* ==========================================================================
   Canada Quiz — driving-engine.js
   THE QUIZ BRAIN FOR EVERY PROVINCE. Written once, never changed per province.

   A page loads three files, in this order:
       js/driving/signs.js      <- the shared road-sign drawings (all provinces)
       js/driving/on.js         <- ONE province: its test format + questions
       js/driving-engine.js     <- this file

   Then the page calls ONE of:
       CQDrive.mock("#mount")             the full timed practice test
       CQDrive.studySigns("#mount")       study the signs, by category
       CQDrive.studyRules("#mount")       study the rules, by chapter

   Everything the visitor reads is stored in BOTH languages inside the data
   files, so a French page is never half English. The engine picks the language
   from the web address: /fr/anything.html is French, everything else English.
   ========================================================================== */
(function () {
  "use strict";

  var LANG = /(^|\/)fr\//.test(location.pathname) ? "fr" : "en";
  var P = window.CQ_PROVINCE || null;
  var SIGNS = window.CQ_SIGNS || {};
  var META = window.CQ_SIGN_META || {};

  /* ---------------------------------------------------------------
     Words the engine itself prints. Both languages, side by side.
     --------------------------------------------------------------- */
  var S = {
    startTest:    { en: "Start the practice test",     fr: "Commencer le test pratique" },
    tryAgain:     { en: "Try again",                   fr: "Réessayer" },
    next:         { en: "Next question →",             fr: "Question suivante →" },
    seeResult:    { en: "See my result →",             fr: "Voir mon résultat →" },
    questionOf:   { en: "Question %1 of %2",           fr: "Question %1 sur %2" },
    pass:         { en: "PASS",                        fr: "RÉUSSI" },
    fail:         { en: "TRY AGAIN",                   fr: "À REPRENDRE" },
    scored:       { en: "You scored %1 out of %2",     fr: "Vous avez obtenu %1 sur %2" },
    passMsg:      { en: "Well done. Keep practising until you pass every time.",
                    fr: "Bravo. Continuez à pratiquer jusqu'à réussir chaque fois." },
    failMsg:      { en: "Not this time. Look at the questions you missed below, then try again.",
                    fr: "Pas cette fois. Regardez ci-dessous les questions manquées, puis réessayez." },
    sectionRule:  { en: "You must get %1 of %2 right in this section.",
                    fr: "Vous devez obtenir %1 bonnes réponses sur %2 dans cette section." },
    bothNeeded:   { en: "You must pass BOTH sections. Doing well in one does not make up for the other.",
                    fr: "Vous devez réussir LES DEUX sections. Une bonne note dans l'une ne compense pas l'autre." },
    overallRule:  { en: "You must get %1 of the %2 questions right to pass.",
                    fr: "Vous devez répondre correctement à %1 des %2 questions pour réussir." },
    sectionInfo:  { en: "You must get %1 of %2 right in this section.",
                    fr: "Vous devez obtenir %1 bonnes réponses sur %2 dans cette section." },
    timeUp:       { en: "Time is up — here is your result.",
                    fr: "Le temps est écoulé — voici votre résultat." },
    review:       { en: "The questions you missed",    fr: "Les questions manquées" },
    allRight:     { en: "You did not miss a single question. Excellent.",
                    fr: "Vous n'avez manqué aucune question. Excellent." },
    yourAnswer:   { en: "Your answer:",                fr: "Votre réponse :" },
    correct:      { en: "Correct answer:",             fr: "Bonne réponse :" },
    correctMark:  { en: "Correct",                     fr: "Bonne réponse" },
    wrongMark:    { en: "Not quite",                   fr: "Pas tout à fait" },
    quit:         { en: "Leave the test",              fr: "Quitter le test" },
    quitAsk:      { en: "Leave the test? Your answers will be lost.",
                    fr: "Quitter le test ? Vos réponses seront perdues." },
    allSigns:     { en: "All signs",                   fr: "Tous les panneaux" },
    allTopics:    { en: "All chapters",                fr: "Tous les chapitres" },
    showAnswer:   { en: "Show the answer",             fr: "Afficher la réponse" },
    practiceThis: { en: "Practise this section",       fr: "Pratiquer cette section" },
    stopPractice: { en: "Back to studying",            fr: "Retour à l'étude" },
    noTimer:      { en: "No timer — take your time.",  fr: "Sans chronomètre — prenez votre temps." },
    of:           { en: "of",                          fr: "sur" },
    signsCount:   { en: "%1 signs",                    fr: "%1 panneaux" },
    qCount:       { en: "%1 questions",                fr: "%1 questions" },
    startOver:    { en: "Start over",                  fr: "Recommencer" },
    cat: {
      regulatory:  { en: "Regulatory signs",   fr: "Panneaux de prescription" },
      warning:     { en: "Warning signs",      fr: "Panneaux d'avertissement" },
      temporary:   { en: "Construction signs", fr: "Panneaux de chantier" },
      information: { en: "Information signs",  fr: "Panneaux d'information" },
      lights:      { en: "Traffic lights",     fr: "Feux de circulation" },
      markings:    { en: "Road markings",      fr: "Marques sur la chaussée" }
    },
    catNote: {
      regulatory:  { en: "These tell you the law. You must obey them.",
                     fr: "Ils indiquent la loi. Vous devez les respecter." },
      warning:     { en: "Yellow diamonds. They warn you about what is ahead.",
                     fr: "Losanges jaunes. Ils annoncent ce qui vient devant vous." },
      temporary:   { en: "Orange signs. Road work, workers and lower speed limits.",
                     fr: "Panneaux orange. Travaux, ouvriers et limites de vitesse réduites." },
      information: { en: "Green and blue signs. Directions, services and distances.",
                     fr: "Panneaux verts et bleus. Directions, services et distances." },
      lights:      { en: "What each light and arrow means at an intersection.",
                     fr: "Ce que signifie chaque feu et chaque flèche à une intersection." },
      markings:    { en: "The painted lines on the road are signs too.",
                     fr: "Les lignes peintes sur la chaussée sont aussi des signaux." }
    }
  };

  function T(key, a, b) {
    var e = S[key];
    var s = e ? (e[LANG] || e.en) : key;
    if (a !== undefined) s = s.replace("%1", a);
    if (b !== undefined) s = s.replace("%2", b);
    return s;
  }
  function L(obj) {                       /* {en:…, fr:…} -> the right one */
    if (!obj) return "";
    return typeof obj === "string" ? obj : (obj[LANG] || obj.en || "");
  }
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
                    .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function el(sel) {
    return typeof sel === "string" ? document.querySelector(sel) : sel;
  }
  function shuffle(list) {
    var a = list.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function pick(list, n) { return shuffle(list).slice(0, n); }

  function signHTML(id, big) {
    var art = SIGNS[id];
    if (!art) return "";
    return '<div class="dq-sign' + (big ? " dq-sign-lg" : "") + '">' + art + "</div>";
  }
  function qText(q)  { return (q[LANG] || q.en).q; }
  function qOpts(q)  { return (q[LANG] || q.en).a; }
  function qExpl(q)  { return (q[LANG] || q.en).e; }

  function bySec(id)   { return P.questions.filter(function (q) { return q.sec === id; }); }
  function byTopic(t)  { return P.questions.filter(function (q) { return q.topic === t; }); }
  function signsInCat(c) {
    return Object.keys(META).filter(function (k) { return META[k].cat === c; });
  }

  /* =========================================================================
     1. THE MOCK TEST — exactly the real format the province declares
     ========================================================================= */
  function mock(mount) {
    var host = el(mount);
    if (!host || !P) return;
    host.setAttribute("data-no-i18n", "");   /* already in the right language */

    var qs = [], cur = 0, answered = false, picked = -1, left = 0, tick = null;

    function build() {
      qs = [];
      P.sections.forEach(function (sec) {
        pick(bySec(sec.id), sec.ask).forEach(function (q) {
          qs.push({ q: q, sec: sec.id, given: -1 });
        });
      });
    }

    function total() {
      return P.sections.reduce(function (n, s) { return n + s.ask; }, 0);
    }

    function screenStart() {
      var rows = P.sections.map(function (s) {
        return '<span class="pill">' + esc(L(s.name)) + " — " + s.ask + " " +
               esc(T("qCount", "").trim() || "questions") + "</span>";
      }).join(" ");
      host.innerHTML =
        '<section class="panel center">' +
          '<div style="font-size:46px">🚗</div>' +
          "<h2>" + esc(L(P.name)) + " " + esc(P.licence) + " — " +
             esc(LANG === "fr" ? "test pratique" : "practice test") + "</h2>" +
          "<p>" + P.sections.map(function (s) {
              return '<span class="pill">' + esc(L(s.name)) + ": " + s.ask + "</span>";
            }).join(" &nbsp; ") +
            ' &nbsp; <span class="pill">' + P.minutes + " min</span></p>" +
          '<p class="muted" style="max-width:620px;margin:8px auto 0">' +
            esc(P.overallPass ? T("overallRule", P.overallPass, total())
                              : T("bothNeeded")) + "</p>" +
          '<p style="margin-top:18px"><button class="btn btn-lg" id="dq-go">' +
            esc(T("startTest")) + "</button></p>" +
        "</section>";
      host.querySelector("#dq-go").onclick = start;
    }

    function start() {
      build(); cur = 0; answered = false;
      left = P.minutes * 60;
      host.innerHTML =
        '<section class="panel">' +
          '<div class="quiz-meta">' +
            '<span class="pill" id="dq-count"></span>' +
            '<span class="pill" id="dq-sec"></span>' +
            '<span class="timer" id="dq-timer"></span>' +
          "</div>" +
          '<div class="progress"><span id="dq-bar"></span></div>' +
          '<div id="dq-art"></div>' +
          '<h3 id="dq-q" style="margin-top:10px"></h3>' +
          '<div class="options" id="dq-opts"></div>' +
          '<div id="dq-exp" class="explain" style="display:none"></div>' +
          '<div class="center" style="margin-top:18px">' +
            '<button class="btn" id="dq-next" style="display:none"></button></div>' +
          '<div class="center" style="margin-top:10px">' +
            '<button class="btn btn-ghost" id="dq-quit">' + esc(T("quit")) + "</button></div>" +
        "</section>";
      host.querySelector("#dq-next").onclick = next;
      host.querySelector("#dq-quit").onclick = function () {
        if (confirm(T("quitAsk"))) { stopClock(); screenStart(); }
      };
      startClock();
      show();
    }

    function startClock() {
      stopClock();
      paintClock();
      tick = setInterval(function () {
        left--;
        paintClock();
        if (left <= 0) { stopClock(); finish(true); }
      }, 1000);
    }
    function stopClock() { if (tick) { clearInterval(tick); tick = null; } }
    function paintClock() {
      var t = host.querySelector("#dq-timer");
      if (!t) return;
      var m = Math.floor(left / 60), s = left % 60;
      t.textContent = m + ":" + (s < 10 ? "0" : "") + s;
      t.style.color = left <= 60 ? "var(--red-dark)" : "";
    }

    function show() {
      var item = qs[cur], q = item.q;
      var sec = P.sections.filter(function (s) { return s.id === item.sec; })[0];
      answered = false; picked = -1;
      host.querySelector("#dq-count").textContent = T("questionOf", cur + 1, qs.length);
      host.querySelector("#dq-sec").textContent = L(sec.name);
      host.querySelector("#dq-bar").style.width = ((cur / qs.length) * 100) + "%";
      host.querySelector("#dq-art").innerHTML = q.sign ? signHTML(q.sign, true) : "";
      host.querySelector("#dq-q").textContent = qText(q);
      var box = host.querySelector("#dq-opts");
      box.innerHTML = qOpts(q).map(function (a, i) {
        return '<button class="option" data-i="' + i + '">' + esc(a) + "</button>";
      }).join("");
      Array.prototype.forEach.call(box.children, function (b) {
        b.onclick = function () { answer(parseInt(b.getAttribute("data-i"), 10)); };
      });
      host.querySelector("#dq-exp").style.display = "none";
      var nb = host.querySelector("#dq-next");
      nb.style.display = "none";
      nb.textContent = (cur === qs.length - 1) ? T("seeResult") : T("next");
    }

    function answer(i) {
      if (answered) return;
      answered = true; picked = i;
      var item = qs[cur], q = item.q;
      item.given = i;
      var box = host.querySelector("#dq-opts");
      Array.prototype.forEach.call(box.children, function (b, k) {
        b.disabled = true; b.classList.add("disabled");
        if (k === q.c) b.classList.add("correct");
        else if (k === i) b.classList.add("wrong");
      });
      var exp = host.querySelector("#dq-exp");
      exp.innerHTML = "<strong>" + esc(i === q.c ? T("correctMark") : T("wrongMark")) +
                      ".</strong> " + esc(qExpl(q));
      exp.style.display = "";
      host.querySelector("#dq-next").style.display = "";
    }

    function next() {
      if (!answered) return;
      if (cur === qs.length - 1) { stopClock(); finish(false); return; }
      cur++; show();
    }

    function finish(ranOut) {
      var per = {}, all = 0;
      P.sections.forEach(function (s) { per[s.id] = 0; });
      qs.forEach(function (it) {
        if (it.given === it.q.c) { per[it.sec]++; all++; }
      });
      var passed = P.overallPass
        ? (all >= P.overallPass)
        : P.sections.every(function (s) { return per[s.id] >= s.pass; });

      var lines = P.sections.map(function (s) {
        var got = per[s.id], ok = got >= s.pass;
        var mark = P.overallPass ? "•" : (ok ? "✅" : "❌");
        var note = P.overallPass ? "" :
          " <span class=\"muted\">(" + esc(T("sectionRule", s.pass, s.ask)) + ")</span>";
        return '<p class="score" style="margin:4px 0">' +
          mark + " " + esc(L(s.name)) + " — <strong>" + got + " / " + s.ask +
          "</strong>" + note + "</p>";
      }).join("");

      var missed = qs.filter(function (it) { return it.given !== it.q.c; });
      var rev = missed.length
        ? missed.map(function (it) {
            var q = it.q, opts = qOpts(q);
            return '<div class="panel" style="margin:12px 0">' +
              (q.sign ? signHTML(q.sign) : "") +
              "<p><strong>" + esc(qText(q)) + "</strong></p>" +
              '<p class="muted">' + esc(T("yourAnswer")) + " " +
                 esc(it.given >= 0 ? opts[it.given] : "—") + "</p>" +
              "<p>" + esc(T("correct")) + " <strong>" + esc(opts[q.c]) + "</strong></p>" +
              '<div class="explain">' + esc(qExpl(q)) + "</div></div>";
          }).join("")
        : '<p class="muted">' + esc(T("allRight")) + "</p>";

      host.innerHTML =
        '<section class="panel center">' +
          (ranOut ? '<p class="muted">' + esc(T("timeUp")) + "</p>" : "") +
          '<div class="result-big">' + (passed ? "✅" : "❌") + "</div>" +
          '<div class="result-big ' + (passed ? "pass" : "fail") + '">' +
             esc(passed ? T("pass") : T("fail")) + "</div>" +
          '<p class="score">' + esc(T("scored", all, qs.length)) + "</p>" +
          '<div style="margin:14px 0">' + lines + "</div>" +
          '<p class="muted">' + esc(passed ? T("passMsg") : T("failMsg")) + "</p>" +
          '<p style="margin:20px 0"><button class="btn btn-lg" id="dq-again">' +
             esc(T("tryAgain")) + "</button></p>" +
          '<h3 style="margin-top:26px">' + esc(T("review")) + "</h3>" +
          '<div style="text-align:left">' + rev + "</div>" +
        "</section>";
      host.querySelector("#dq-again").onclick = start;
      window.scrollTo(0, 0);
    }

    screenStart();
  }

  /* =========================================================================
     2. STUDY THE SIGNS — every sign, grouped, with its name and a practice run
     ========================================================================= */
  function studySigns(mount) {
    var host = el(mount);
    if (!host || !P) return;
    host.setAttribute("data-no-i18n", "");
    var cats = ["regulatory", "warning", "temporary", "information", "lights", "markings"];

    var nav = cats.map(function (c) {
      return '<button class="btn btn-ghost dq-tab" data-c="' + c + '">' +
             esc(L(S.cat[c])) + "</button>";
    }).join(" ");

    host.innerHTML =
      '<div class="center dq-tabs" style="margin-bottom:14px">' + nav + "</div>" +
      '<div id="dq-cat"></div>';

    function paint(c) {
      Array.prototype.forEach.call(host.querySelectorAll(".dq-tab"), function (b) {
        b.classList.toggle("on", b.getAttribute("data-c") === c);
      });
      var ids = signsInCat(c);
      var cards = ids.map(function (id) {
        return '<div class="dq-card">' + signHTML(id) +
               "<p>" + esc(L(META[id])) + "</p></div>";
      }).join("");
      var qcount = bySec("signs").filter(function (q) {
        return q.sign && META[q.sign] && META[q.sign].cat === c;
      }).length;
      el("#dq-cat").innerHTML =
        '<section class="panel">' +
          "<h2>" + esc(L(S.cat[c])) + "</h2>" +
          '<p class="muted">' + esc(L(S.catNote[c])) + " " +
             esc(T("signsCount", ids.length)) + ".</p>" +
          '<div class="dq-gallery">' + cards + "</div>" +
          (qcount ? '<p class="center" style="margin-top:18px">' +
             '<button class="btn btn-green" id="dq-prac">' + esc(T("practiceThis")) +
             " (" + esc(T("qCount", qcount)) + ")</button></p>" : "") +
        "</section>" +
        '<div id="dq-prac-box"></div>';
      var pb = el("#dq-prac");
      if (pb) pb.onclick = function () {
        practice(el("#dq-prac-box"), bySec("signs").filter(function (q) {
          return q.sign && META[q.sign] && META[q.sign].cat === c;
        }));
      };
      window.scrollTo(0, 0);
    }

    Array.prototype.forEach.call(host.querySelectorAll(".dq-tab"), function (b) {
      b.onclick = function () { paint(b.getAttribute("data-c")); };
    });
    paint("regulatory");
  }

  /* =========================================================================
     3. STUDY THE RULES — chapter by chapter, no timer
     ========================================================================= */
  function studyRules(mount) {
    var host = el(mount);
    if (!host || !P) return;
    host.setAttribute("data-no-i18n", "");
    var topics = P.topics || [];

    host.innerHTML =
      '<div class="center dq-tabs" style="margin-bottom:14px">' +
        topics.map(function (t) {
          return '<button class="btn btn-ghost dq-tab" data-t="' + t.id + '">' +
                 esc(L(t)) + "</button>";
        }).join(" ") +
      "</div><div id=\"dq-cat\"></div>";

    function paint(id) {
      Array.prototype.forEach.call(host.querySelectorAll(".dq-tab"), function (b) {
        b.classList.toggle("on", b.getAttribute("data-t") === id);
      });
      var t = topics.filter(function (x) { return x.id === id; })[0];
      var list = byTopic(id);
      el("#dq-cat").innerHTML =
        '<section class="panel">' +
          "<h2>" + esc(L(t)) + "</h2>" +
          '<p class="muted">' + esc(T("qCount", list.length)) + " · " + esc(T("noTimer")) + "</p>" +
          '<div id="dq-learn"></div>' +
        "</section>" +
        '<div id="dq-prac-box"></div>';
      el("#dq-learn").innerHTML = list.map(function (q, i) {
        var opts = qOpts(q);
        return "<details class=\"dq-learn\"><summary>" + (i + 1) + ". " + esc(qText(q)) +
          "</summary><p><strong>" + esc(T("correct")) + " " + esc(opts[q.c]) +
          "</strong></p><div class=\"explain\">" + esc(qExpl(q)) + "</div></details>";
      }).join("");
      practice(el("#dq-prac-box"), list, true);
      window.scrollTo(0, 0);
    }

    Array.prototype.forEach.call(host.querySelectorAll(".dq-tab"), function (b) {
      b.onclick = function () { paint(b.getAttribute("data-t")); };
    });
    if (topics.length) paint(topics[0].id);
  }

  /* =========================================================================
     Shared: an untimed practice run over any list of questions
     ========================================================================= */
  function practice(box, list, autoOpen) {
    if (!box || !list || !list.length) return;
    var qs = shuffle(list), cur = 0, score = 0, done = false;

    function frame() {
      box.innerHTML =
        '<section class="panel" id="dq-p">' +
          '<div class="quiz-meta"><span class="pill" id="dq-pc"></span>' +
          '<span class="pill" id="dq-ps"></span></div>' +
          '<div class="progress"><span id="dq-pb"></span></div>' +
          '<div id="dq-part"></div>' +
          '<h3 id="dq-pq" style="margin-top:10px"></h3>' +
          '<div class="options" id="dq-po"></div>' +
          '<div id="dq-pe" class="explain" style="display:none"></div>' +
          '<div class="center" style="margin-top:16px">' +
            '<button class="btn" id="dq-pn" style="display:none"></button></div>' +
        "</section>";
      box.querySelector("#dq-pn").onclick = function () {
        if (cur === qs.length - 1) { end(); return; }
        cur++; show();
      };
      show();
    }

    function show() {
      done = false;
      var q = qs[cur];
      box.querySelector("#dq-pc").textContent = T("questionOf", cur + 1, qs.length);
      box.querySelector("#dq-ps").textContent = score + " / " + qs.length;
      box.querySelector("#dq-pb").style.width = ((cur / qs.length) * 100) + "%";
      box.querySelector("#dq-part").innerHTML = q.sign ? signHTML(q.sign, true) : "";
      box.querySelector("#dq-pq").textContent = qText(q);
      var o = box.querySelector("#dq-po");
      o.innerHTML = qOpts(q).map(function (a, i) {
        return '<button class="option" data-i="' + i + '">' + esc(a) + "</button>";
      }).join("");
      Array.prototype.forEach.call(o.children, function (b) {
        b.onclick = function () { hit(parseInt(b.getAttribute("data-i"), 10)); };
      });
      box.querySelector("#dq-pe").style.display = "none";
      var n = box.querySelector("#dq-pn");
      n.style.display = "none";
      n.textContent = (cur === qs.length - 1) ? T("seeResult") : T("next");
    }

    function hit(i) {
      if (done) return;
      done = true;
      var q = qs[cur];
      if (i === q.c) score++;
      var o = box.querySelector("#dq-po");
      Array.prototype.forEach.call(o.children, function (b, k) {
        b.disabled = true; b.classList.add("disabled");
        if (k === q.c) b.classList.add("correct");
        else if (k === i) b.classList.add("wrong");
      });
      var e = box.querySelector("#dq-pe");
      e.innerHTML = "<strong>" + esc(i === q.c ? T("correctMark") : T("wrongMark")) +
                    ".</strong> " + esc(qExpl(q));
      e.style.display = "";
      box.querySelector("#dq-ps").textContent = score + " / " + qs.length;
      box.querySelector("#dq-pn").style.display = "";
    }

    function end() {
      var pct = Math.round((score / qs.length) * 100);
      box.innerHTML =
        '<section class="panel center">' +
          '<div class="result-big">' + (pct >= 80 ? "✅" : "📘") + "</div>" +
          '<p class="score">' + esc(T("scored", score, qs.length)) + " — " + pct + "%</p>" +
          '<p style="margin-top:16px"><button class="btn" id="dq-pr">' +
             esc(T("startOver")) + "</button></p>" +
        "</section>";
      box.querySelector("#dq-pr").onclick = function () {
        qs = shuffle(list); cur = 0; score = 0; frame();
      };
      window.scrollTo(0, box.getBoundingClientRect().top + window.pageYOffset - 80);
    }

    if (autoOpen) frame();
    else { frame(); window.scrollTo(0, box.getBoundingClientRect().top + window.pageYOffset - 80); }
  }

  /* ------------------------------------------------------------------ API */
  window.CQDrive = {
    lang: LANG,
    province: P,
    text: T,
    pickLang: L,
    signHTML: signHTML,
    mock: mock,
    studySigns: studySigns,
    studyRules: studyRules
  };
})();
