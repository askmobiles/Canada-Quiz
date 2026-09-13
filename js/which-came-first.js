/* canada-quiz.com — Which Came First?
 *
 * WHY THIS EXISTS
 * ---------------
 * Search Console, 28 days: the two pages Google showed most were
 * prime-ministers-of-canada (305 impressions) and canada-population-timeline
 * (123). Both got zero clicks. The queries behind them were "list of canadian
 * prime ministers", "the first prime minister of canada", "canada population
 * 1918", "population of canada in 1850" — every one a question Google answers
 * in its own box. Nobody needs to click.
 *
 * The one query that did produce a click was "where should i live in canada
 * quiz". Somebody wanting to DO something, not read something.
 *
 * A search engine can print a date. It cannot make the choice for you. That is
 * the whole design of this game.
 *
 * THE DATA
 * --------
 * WF_EVENTS is written into the page by tools/newq/build_first.py from the same
 * 339 sourced notes that make the Canada Diary. Each carries an English title,
 * a French title, a year, an era and the diary anchor it came from, so every
 * answer can be followed back to a sourced entry.
 *
 * WHY PAIRS ARE MADE HERE AND NOT AT BUILD TIME
 * ---------------------------------------------
 * 339 events give 56,885 pairs with different years. Baking a few hundred into
 * the page would make it stale and enormous; baking all of them would make the
 * file unreadable. The page carries the events, the browser makes the pairs,
 * and the file still diffs cleanly between builds.
 */
(function () {
  "use strict";

  var pairBox = document.getElementById("wf-pair");
  if (!pairBox || typeof WF_EVENTS === "undefined") return;

  var FR = /\/fr\//.test(location.pathname);
  var W = FR ? {
    correct: "Bonne réponse",
    wrong: "Pas celui-là",
    streak: "Série",
    best: "Record",
    right: "Justes",
    ancient: "Il y a des milliers d'années",
    y1000: "Vers l'an 1000",
    story: "Lire l'histoire complète",
    vs: "LEQUEL EST ARRIVÉ EN PREMIER ?",
    tap: "Touchez un événement"
  } : {
    correct: "Correct",
    wrong: "Not that one",
    streak: "Streak",
    best: "Best",
    right: "Right",
    ancient: "Thousands of years ago",
    y1000: "About the year 1000",
    story: "Read the full story",
    vs: "WHICH CAME FIRST?",
    tap: "Tap an event"
  };

  var KEY = "cq-wcf-best";
  var streak = 0, right = 0, asked = 0, best = 0, answered = false, cur = null;

  try { best = parseInt(localStorage.getItem(KEY), 10) || 0; } catch (e) { best = 0; }

  function el(id) { return document.getElementById(id); }
  function title(e) { return FR ? e.f : e.t; }

  /* The diary writes "Thousands of years ago" rather than -13000, and "About the
     year 1000" for the Norse landing, because those are estimates rather than
     dates. The game shows the same words, so a reader who follows the link does
     not meet a different claim on the other page. */
  function yearLabel(e) {
    if (e.y < 0) return W.ancient;
    if (e.y === 1000) return W.y1000;
    return String(e.y);
  }

  /* HOW A PAIR IS CHOSEN
     Early rounds take events far apart, so the first answer is a win and the
     rules explain themselves. The gap then narrows, so round twelve is a real
     question. Without this the first pair could be 1982 against 1984 and a new
     player would think the game was a coin toss. */
  function minGap() {
    if (asked < 3) return 200;
    if (asked < 6) return 80;
    if (asked < 10) return 25;
    if (asked < 16) return 8;
    return 1;
  }

  function pick() {
    var gap = minGap(), a, b, tries = 0;
    do {
      a = WF_EVENTS[Math.floor(Math.random() * WF_EVENTS.length)];
      b = WF_EVENTS[Math.floor(Math.random() * WF_EVENTS.length)];
      tries++;
    } while (tries < 400 && (a === b || Math.abs(a.y - b.y) < gap));
    // a last resort that can never loop for ever: any two different years
    if (a === b || a.y === b.y) {
      for (var i = 0; i < WF_EVENTS.length; i++) {
        if (WF_EVENTS[i].y !== a.y) { b = WF_EVENTS[i]; break; }
      }
    }
    return Math.random() < 0.5 ? [a, b] : [b, a];
  }

  function scores() {
    var s = el("wf-scores");
    s.innerHTML = "";
    [[W.streak, streak], [W.best, best], [W.right, right + " / " + asked]]
      .forEach(function (row) {
        var d = document.createElement("div");
        d.className = "wf-score";
        d.setAttribute("data-no-i18n", "");
        d.innerHTML = "<span></span>";
        d.firstChild.textContent = row[0];
        d.appendChild(document.createTextNode(String(row[1])));
        s.appendChild(d);
      });
  }

  function card(e) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "wf-card";
    b.setAttribute("data-no-i18n", "");
    var t = document.createElement("div");
    t.className = "wf-t";
    t.textContent = title(e);
    var y = document.createElement("div");
    y.className = "wf-y";
    y.textContent = "";
    b.appendChild(t);
    b.appendChild(y);
    b.onclick = function () { answer(e, b); };
    b._y = y;
    b._e = e;
    return b;
  }

  function deal() {
    answered = false;
    cur = pick();
    el("wf-vs").textContent = W.vs;
    el("wf-msg").textContent = W.tap;
    el("wf-msg").style.color = "#5f6b7a";
    el("wf-links").innerHTML = "";
    pairBox.innerHTML = "";
    pairBox.appendChild(card(cur[0]));
    pairBox.appendChild(card(cur[1]));
    scores();
  }

  function answer(chosen, btn) {
    if (answered) return;
    answered = true;
    asked++;
    var other = (chosen === cur[0]) ? cur[1] : cur[0];
    var win = chosen.y < other.y;

    // reveal both years at once, so the pair teaches even when it is wrong
    var cards = pairBox.querySelectorAll(".wf-card");
    for (var i = 0; i < cards.length; i++) {
      cards[i]._y.textContent = yearLabel(cards[i]._e);
      cards[i].disabled = true;
    }
    btn.classList.add(win ? "win" : "lose");
    if (!win) {
      for (var j = 0; j < cards.length; j++) {
        if (cards[j]._e === other) cards[j].classList.add("win");
      }
    }

    var m = el("wf-msg");
    if (win) {
      right++; streak++;
      if (streak > best) {
        best = streak;
        try { localStorage.setItem(KEY, String(best)); } catch (e) {}
      }
      m.style.color = "#2a9d8f";
      m.textContent = W.correct;
    } else {
      streak = 0;
      m.style.color = "#e63946";
      m.textContent = W.wrong;
    }
    scores();

    // both events link back to the sourced diary entry they came from
    var links = el("wf-links");
    links.innerHTML = "";
    [cur[0], cur[1]].forEach(function (e) {
      var a = document.createElement("a");
      a.href = "canada-diary.html#" + e.a;
      a.textContent = title(e) + " — " + W.story;
      a.setAttribute("data-no-i18n", "");
      links.appendChild(a);
    });
  }

  el("wf-next").onclick = deal;
  el("wf-reset").onclick = function () {
    streak = 0; right = 0; asked = 0;
    deal();
  };

  document.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && answered) deal();
  });

  deal();
}());
