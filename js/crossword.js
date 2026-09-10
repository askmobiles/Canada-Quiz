/* canada-quiz.com — the crossword.
 *
 * WHY THE PUZZLES ARE NOT TRANSLATED
 * ----------------------------------
 * Everything else on this site is built in English and translated one text node
 * at a time by the French build. A crossword cannot work that way, because in a
 * crossword the answer IS the grid. ORIGNAL is seven letters where MOOSE is
 * five, and it crosses different words in different places. So the page carries
 * two separate banks — PUZZLES_EN and PUZZLES_FR, both generated from the same
 * six themes — and picks between them here by the same test the rest of the
 * site uses: is /fr/ in the path.
 *
 * Before this file existed, the French page ran the English puzzles. A French
 * visitor was asked to spell MOOSE from "Large animal with big antlers".
 *
 * THE WORDS IN THE GRID
 * ---------------------
 * French answers are set without accents — ERABLE, TEMPETE, SENAT. That is the
 * ordinary convention for a French crossword, and it is also the only thing the
 * A-Z keys under the grid can produce. The clues keep their accents, because a
 * clue is read rather than typed.
 */
(function () {
  "use strict";

  var grid = document.getElementById("grid");
  if (!grid || typeof PUZZLES_EN === "undefined") return;

  var FR = /\/fr\//.test(location.pathname);
  var BANK = FR ? PUZZLES_FR : PUZZLES_EN;
  var W = FR ? {
    across: "Horizontal",
    down: "Vertical",
    begin: "Touchez une case pour commencer",
    type: "Tapez votre réponse",
    good: "Ça se présente bien, continuez !",
    wrong1: "1 lettre est incorrecte (en rouge).",
    wrongN: "%d lettres sont incorrectes (en rouge).",
    win: "🎉 Vous avez terminé les mots croisés !",
    all: "Tous les thèmes"
  } : {
    across: "Across",
    down: "Down",
    begin: "Tap a square to begin",
    type: "Type your answer",
    good: "Looking good — keep going!",
    wrong1: "1 letter is wrong (in red).",
    wrongN: "%d letters are wrong (in red).",
    win: "🎉 You completed the crossword!",
    all: "All themes"
  };

  var themes = [];
  for (var i = 0; i < BANK.length; i++) {
    if (themes.indexOf(BANK[i].theme) < 0) themes.push(BANK[i].theme);
  }

  var theme = null;          // null means every theme
  var pool = BANK.slice();
  var seen = [];             // puzzles already dealt, so New Puzzle moves on
  var P = null, user = [], active = null, dir = "A";

  function el(id) { return document.getElementById(id); }

  function filled(r, c) {
    return P && r >= 0 && c >= 0 && r < P.rows && c < P.cols && P.cells[r][c] !== null;
  }

  /* THE THEME PICKER
     A teacher taking a class through winter vocabulary, or a study group on how
     Canada is governed, wants that theme and not a random one. Choosing a theme
     narrows the pool; New Puzzle then deals the next grid within it. */
  function buildThemes() {
    var box = el("themes");
    if (!box) return;
    box.innerHTML = "";
    var names = [null].concat(themes);
    for (var i = 0; i < names.length; i++) {
      (function (name) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "cw-theme" + (name === theme ? " on" : "");
        b.textContent = name === null ? W.all : name;
        b.setAttribute("data-no-i18n", "");   // already in the right language
        b.onclick = function () {
          theme = name;
          pool = name === null ? BANK.slice()
                               : BANK.filter(function (p) { return p.theme === name; });
          seen = [];
          buildThemes();
          newGame();
        };
        box.appendChild(b);
      }(names[i]));
    }
  }

  /* Deal the next unseen puzzle in the pool, then start the pool again. Random
     choice would repeat the puzzle somebody had just finished often enough to
     be irritating; this walks through them. */
  function next() {
    if (seen.length >= pool.length) seen = [];
    for (var i = 0; i < pool.length; i++) {
      if (seen.indexOf(i) < 0) { seen.push(i); return pool[i]; }
    }
    return pool[0];
  }

  function newGame() {
    P = next();
    user = P.cells.map(function (row) {
      return row.map(function (x) { return x === null ? null : ""; });
    });
    active = null; dir = "A";
    el("msg").textContent = "";
    el("cluebar").textContent = W.begin;
    render(); buildClues(); buildKb();
  }

  function render() {
    grid.style.gridTemplateColumns = "repeat(" + P.cols + ",1fr)";
    grid.innerHTML = "";
    var word = activeWord();
    for (var r = 0; r < P.rows; r++) {
      for (var c = 0; c < P.cols; c++) {
        var d = document.createElement("div");
        if (P.cells[r][c] === null) {
          d.className = "cw-cell block";
        } else {
          d.className = "cw-cell";
          if (active && active.r === r && active.c === c) d.classList.add("active");
          else if (word && inWord(word, r, c)) d.classList.add("hl");
          if (P.num[r][c] > 0) {
            var s = document.createElement("span");
            s.className = "cw-num"; s.textContent = P.num[r][c];
            d.appendChild(s);
          }
          var t = document.createElement("span");
          t.textContent = user[r][c] || "";
          d.appendChild(t);
          d.onclick = (function (rr, cc) {
            return function () { clickCell(rr, cc); };
          }(r, c));
        }
        grid.appendChild(d);
      }
    }
  }

  function inWord(w, r, c) {
    for (var i = 0; i < w.length; i++) if (w[i][0] === r && w[i][1] === c) return true;
    return false;
  }

  function clickCell(r, c) {
    if (active && active.r === r && active.c === c) dir = (dir === "A") ? "D" : "A";
    active = { r: r, c: c };
    updateClue(); render();
  }

  function activeWord() {
    if (!active) return null;
    var dr = dir === "D" ? 1 : 0, dc = dir === "A" ? 1 : 0;
    var r = active.r, c = active.c;
    while (filled(r - dr, c - dc)) { r -= dr; c -= dc; }
    var cells = [];
    while (filled(r, c)) { cells.push([r, c]); r += dr; c += dc; }
    return cells.length > 1 ? cells : [[active.r, active.c]];
  }

  function entryAt(r0, c0) {
    var list = dir === "A" ? P.across : P.down;
    for (var i = 0; i < list.length; i++) {
      if (list[i].row === r0 && list[i].col === c0) return list[i];
    }
    return null;
  }

  function updateClue() {
    var w = activeWord();
    if (!w) return;
    var e = entryAt(w[0][0], w[0][1]);
    /* A square can belong to only one word. Tap the middle of a Down word where
       nothing runs across, and the old page answered "Type your answer" — true,
       but useless, because the clue the square actually has was sitting right
       there. If this direction has no word, swing to the one that does. */
    if (!e) {
      dir = (dir === "A") ? "D" : "A";
      w = activeWord();
      e = w ? entryAt(w[0][0], w[0][1]) : null;
    }
    el("cluebar").textContent = e
      ? (e.num + " " + (dir === "A" ? W.across : W.down) + " : " + e.clue)
      : W.type;
    var on = document.querySelectorAll(".cw-clue");
    for (var i = 0; i < on.length; i++) on[i].classList.remove("on");
    if (e) {
      var pick = document.querySelector('.cw-clue[data-k="' + dir + e.num + '"]');
      if (pick) pick.classList.add("on");
    }
  }

  function type(ch) {
    if (!active) return;
    user[active.r][active.c] = ch;
    var dr = dir === "D" ? 1 : 0, dc = dir === "A" ? 1 : 0;
    var r = active.r + dr, c = active.c + dc;
    if (filled(r, c)) active = { r: r, c: c };
    updateClue(); render();
    if (isComplete()) win();
  }

  function del() {
    if (!active) return;
    if (user[active.r][active.c]) {
      user[active.r][active.c] = "";
    } else {
      var dr = dir === "D" ? 1 : 0, dc = dir === "A" ? 1 : 0;
      if (filled(active.r - dr, active.c - dc)) {
        active = { r: active.r - dr, c: active.c - dc };
        user[active.r][active.c] = "";
      }
    }
    render();
  }

  function buildClues() {
    var box = el("clues");
    box.innerHTML = "";
    function col(title, list, d) {
      var wrap = document.createElement("div");
      var h = document.createElement("h3");
      h.textContent = title;
      h.setAttribute("data-no-i18n", "");
      wrap.appendChild(h);
      list.slice().sort(function (a, b) { return a.num - b.num; }).forEach(function (e) {
        var cl = document.createElement("div");
        cl.className = "cw-clue";
        cl.dataset.k = d + e.num;
        cl.textContent = e.num + ". " + e.clue;
        cl.setAttribute("data-no-i18n", "");
        cl.onclick = function () {
          dir = d; active = { r: e.row, c: e.col }; updateClue(); render();
        };
        wrap.appendChild(cl);
      });
      return wrap;
    }
    box.appendChild(col(W.across, P.across, "A"));
    box.appendChild(col(W.down, P.down, "D"));
  }

  var KB = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["DEL", "Z", "X", "C", "V", "B", "N", "M"]];

  function buildKb() {
    var kb = el("kb");
    kb.innerHTML = "";
    KB.forEach(function (row) {
      var kr = document.createElement("div");
      kr.className = "cw-krow";
      row.forEach(function (k) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "cw-key" + (k === "DEL" ? " wide" : "");
        b.textContent = k;
        b.setAttribute("data-no-i18n", "");
        b.onclick = function () { if (k === "DEL") del(); else type(k); };
        kr.appendChild(b);
      });
      kb.appendChild(kr);
    });
  }

  function isComplete() {
    for (var r = 0; r < P.rows; r++) {
      for (var c = 0; c < P.cols; c++) {
        if (P.cells[r][c] !== null && !user[r][c]) return false;
      }
    }
    return true;
  }

  function check() {
    render();
    var wrong = 0, cells = document.querySelectorAll(".cw-cell"), idx = 0;
    for (var r = 0; r < P.rows; r++) {
      for (var c = 0; c < P.cols; c++) {
        var e = cells[idx++];
        if (P.cells[r][c] !== null && user[r][c] && user[r][c] !== P.cells[r][c]) {
          e.classList.add("bad"); wrong++;
        }
      }
    }
    var m = el("msg");
    if (isComplete() && wrong === 0) { win(); return; }
    if (wrong === 0) { m.style.color = "#5f6b7a"; m.textContent = W.good; }
    else {
      m.style.color = "#e63946";
      m.textContent = wrong === 1 ? W.wrong1 : W.wrongN.replace("%d", wrong);
    }
  }

  function reveal() {
    for (var r = 0; r < P.rows; r++) {
      for (var c = 0; c < P.cols; c++) {
        if (P.cells[r][c] !== null) user[r][c] = P.cells[r][c];
      }
    }
    render();
    el("msg").textContent = "";
  }

  function win() {
    var m = el("msg");
    m.style.color = "#2a9d8f";
    m.textContent = W.win;
  }

  document.addEventListener("keydown", function (e) {
    if (!active) return;
    if (e.key === "Backspace") { e.preventDefault(); del(); return; }
    if (e.key === "ArrowRight") { dir = "A"; if (filled(active.r, active.c + 1)) active.c++; }
    else if (e.key === "ArrowLeft") { dir = "A"; if (filled(active.r, active.c - 1)) active.c--; }
    else if (e.key === "ArrowDown") { dir = "D"; if (filled(active.r + 1, active.c)) active.r++; }
    else if (e.key === "ArrowUp") { dir = "D"; if (filled(active.r - 1, active.c)) active.r--; }
    else if (/^[a-zA-Z]$/.test(e.key)) { type(e.key.toUpperCase()); return; }
    else return;
    updateClue(); render();
  });

  el("cw-check").onclick = check;
  el("cw-reveal").onclick = reveal;
  el("cw-new").onclick = newGame;

  buildThemes();
  newGame();
}());
