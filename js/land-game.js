/* The engine every land plays on.
 * ======================================================================
 * WHY THIS IS SEPARATE
 *
 * The drawn driving game, Read the Road and the River of Time each grew their
 * own copy of the same loop: show a picture, ask one question, big buttons,
 * count, show a card at the end. Three copies is where a fourth stops being
 * acceptable — so this is the loop, once, and a land is now just a list of
 * scenes plus a name.
 *
 * A land supplies window.CQ_LAND before this file loads:
 *
 *   CQ_LAND = {
 *     scenes: [ { id, draw(fr), en:{q,a[],c,e}, fr:{…} }, … ],
 *                  draw() is handed the language because words drawn INSIDE a
 *                  picture are invisible to build_fr.py and to the runtime
 *                  translator alike — the French page showed an English removal
 *                  van until somebody looked at a screenshot of it.
 *     round:  how many to play        (default: all of them)
 *     words:  { …optional overrides… }
 *   }
 *
 * WHAT THE ENGINE DECIDES, AND WHY
 *
 * No pass mark. These lands teach things a child should carry, not things they
 * are examined on, and a child who scores six has not failed at respect — they
 * have found four things worth talking about. The end card says how many were
 * new to you and keeps the picture and the explanation for each one.
 *
 * The explanation shows whether you were right or wrong. Being wrong is exactly
 * when a person reads it.
 *
 * Both languages live here, because everything this file writes is built after
 * the page loads and build_fr.py only ever sees the HTML.
 */
(function () {
  "use strict";

  var host = document.getElementById("land-game");
  if (!host || !window.CQ_LAND || !CQ_LAND.scenes || !CQ_LAND.scenes.length) return;

  var FR = /(^|\/)fr\//.test(location.pathname);
  var SCENES = CQ_LAND.scenes;
  var ROUND = CQ_LAND.round || SCENES.length;

  var W = FR ? {
    start: "Commencer", intro: "Choisis ce que tu ferais.",
    situation: "Situation", of: "sur", score: "Score", right: "Justes",
    good: "Bonne r&eacute;ponse", bad: "Pas cette fois",
    next: "Suivante &rarr;", see: "Voir mon r&eacute;sultat &rarr;",
    again: "Rejouer", learned: "Ce que tu as appris",
    allRight: "Tout juste. Tu peux expliquer chacune de ces situations &agrave; un adulte.",
    someWrong: "Voici celles qui t'ont attrap&eacute;. Ce sont celles qui valent la peine d'&ecirc;tre lues.",
    talk: "Montre cette page &agrave; un adulte et parlez-en ensemble."
  } : {
    start: "Start", intro: "Choose what you would do.",
    situation: "Situation", of: "of", score: "Score", right: "Right",
    good: "Correct", bad: "Not this time",
    next: "Next &rarr;", see: "See my result &rarr;",
    again: "Play again", learned: "What you learned",
    allRight: "All of them. You could explain every one of these to a grown-up.",
    someWrong: "These are the ones that caught you. They are the ones worth reading.",
    talk: "Show this page to a grown-up and talk it through together."
  };
  var over = (CQ_LAND.words && (FR ? CQ_LAND.words.fr : CQ_LAND.words.en)) || {};
  Object.keys(over).forEach(function (k) { W[k] = over[k]; });

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1)), x = a[i]; a[i] = a[j]; a[j] = x;
    }
    return a;
  }
  function L(s) { return FR ? s.fr : s.en; }
  function svg(inner) {
    return '<svg class="land-svg" viewBox="0 0 500 300" role="img" aria-hidden="true" ' +
           'preserveAspectRatio="xMidYMid meet">' + inner + "</svg>";
  }

  var order = [], at = 0, right = 0, missed = [], answered = false;

  function intro() {
    host.setAttribute("data-no-i18n", "");
    host.innerHTML = '<p class="land-intro">' + W.intro + "</p>" +
      '<div class="center"><button class="btn" id="land-go">' + W.start + "</button></div>";
    host.querySelector("#land-go").onclick = begin;
  }

  function begin() {
    order = shuffle(SCENES).slice(0, ROUND);
    at = 0; right = 0; missed = [];
    deal();
  }

  function deal() {
    answered = false;
    var s = order[at], w = L(s);
    host.innerHTML =
      '<div class="land-bar">' +
      '<div class="land-stat"><span>' + W.score + "</span>" + right + " / " + at + "</div>" +
      '<div class="land-stat"><span>' + W.right + "</span>" +
      (at ? Math.round(right * 100 / at) : 0) + "%</div></div>" +
      svg(s.draw(FR)) +
      '<p class="land-count">' + W.situation + " " + (at + 1) + " " + W.of + " " + order.length + "</p>" +
      '<p class="land-q">' + w.q + "</p>" +
      '<div class="land-opts">' +
      w.a.map(function (o, i) {
        return '<button type="button" class="land-opt" data-i="' + i + '">' + o + "</button>";
      }).join("") + "</div>" +
      '<p class="land-fb" id="land-fb"></p>' +
      '<div class="center land-after" id="land-after"></div>';
    Array.prototype.forEach.call(host.querySelectorAll(".land-opt"), function (b) {
      b.onclick = function () { answer(+b.getAttribute("data-i"), b); };
    });
  }

  function answer(i, btn) {
    if (answered) return;
    answered = true;
    var s = order[at], w = L(s), win = i === w.c;
    var opts = host.querySelectorAll(".land-opt");
    for (var j = 0; j < opts.length; j++) {
      opts[j].disabled = true;
      if (j === w.c) opts[j].classList.add("win");
    }
    if (win) { right++; } else { btn.classList.add("lose"); missed.push(s); }

    var fb = host.querySelector("#land-fb");
    fb.className = "land-fb " + (win ? "ok" : "no");
    fb.innerHTML = "<b>" + (win ? W.good : W.bad) + "</b> &mdash; " + w.e;

    at++;
    var b = document.createElement("button");
    b.className = "btn";
    b.innerHTML = at >= order.length ? W.see : W.next;
    b.onclick = at >= order.length ? result : deal;
    host.querySelector("#land-after").appendChild(b);
  }

  function result() {
    var h = '<div class="land-big">' + Math.round(right * 100 / order.length) + "%</div>" +
            '<p class="land-sub">' + right + " / " + order.length + "</p>";
    if (!missed.length) {
      h += '<p class="land-all">' + W.allRight + "</p>";
    } else {
      h += '<p class="land-head2">' + W.learned + "</p>" +
           '<p class="muted land-note">' + W.someWrong + "</p><ul class=\"land-missed\">" +
           missed.map(function (s) {
             var w = L(s);
             return "<li>" + svg(s.draw(FR)) + "<div><b>" + w.a[w.c] + "</b><br>" + w.e + "</div></li>";
           }).join("") + "</ul>";
    }
    h += '<p class="land-talk">' + W.talk + "</p>" +
         '<div class="center land-after"><button class="btn" id="land-again">' + W.again + "</button></div>";
    host.innerHTML = h;
    host.querySelector("#land-again").onclick = begin;
  }

  intro();
}());
