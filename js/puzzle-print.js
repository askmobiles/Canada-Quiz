/* Canada Quiz — the puzzle print engine.

   WHY THIS FILE EXISTS
   --------------------
   Every puzzle on this site is generated in the browser. Printing one used to
   be impossible, and the Word Search page said so in its own FAQ. Teachers ask
   for paper: a sheet a child can do with a pencil, and an answer key the
   teacher keeps.

   THE ONE RULE HERE
   -----------------
   A sheet is never drawn twice. This file does NOT know how to make a word
   search or a sudoku. Each game page already has a generator, and it hands
   this engine the puzzle it has just built. So the printed sheet can never
   drift away from the puzzle on the screen — there is only one generator per
   puzzle, ever.

   A game page calls:

       CQPrint.sheet({
         title: "Word Search",
         note:  "Find all ten words.",
         sheets: [ htmlForCopy1, htmlForCopy2, ... ],
         keys:   [ keyForCopy1,  keyForCopy2,  ... ]   // optional
       });

   MULTIPLE COPIES
   ---------------
   A teacher wants thirty different sheets, not thirty photocopies of one, so
   neighbours cannot read across. CQPrint.build() calls the page's own
   generator again for each copy and collects what it draws.

   PAPER, NOT SCREEN
   -----------------
   The sheet carries its own markup and its own classes. It borrows nothing
   from the game's stylesheet, because a game board is styled for a thumb on a
   phone and that is the wrong thing on A4. Backgrounds are dropped (school
   printers waste toner on them and many drop them anyway). The answer key
   always starts on a new sheet of paper, so the questions can be photocopied
   without the answers going out with them.

   FRENCH
   ------
   The labels below are registered as (English, French) pairs by
   tools/newq/build_printpuzzles.py, which writes them into tools/extra_fr.json.
   On a French page site.js has a dictionary loaded, and this engine asks it to
   translate the sheet BEFORE opening the print dialog — waiting for the
   MutationObserver would be a race against the browser's print window, and a
   race that is lost prints an English sheet on a French page. */
(function () {
  "use strict";

  var ROOT_ID = "cqp-root";

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  /* ---------- pieces a game can use to lay its puzzle out ---------- */

  /* A square grid of single characters. rows is an array of arrays, or an
     array of strings. Pass "" or null for a blank cell (a sudoku hole). */
  function grid(rows, opts) {
    opts = opts || {};
    var n = rows.length, o = [], r, c, row, v;
    o.push('<table class="cqp-grid' + (opts.cls ? " " + opts.cls : "") +
           '" style="--cqp-n:' + n + '">');
    for (r = 0; r < n; r++) {
      row = rows[r];
      o.push("<tr>");
      for (c = 0; c < row.length; c++) {
        v = row[c];
        if (v === null || v === undefined) v = "";
        o.push('<td' + (v === "" ? ' class="cqp-blank"' : "") + ">" +
               (v === "" ? "&nbsp;" : esc(v)) + "</td>");
      }
      o.push("</tr>");
    }
    o.push("</table>");
    return o.join("");
  }

  /* A sudoku grid — same as grid() but with the 3x3 boxes ruled. */
  function sudokuGrid(rows) { return grid(rows, { cls: "cqp-sudoku" }); }

  /* A crossword grid. cells is rows of letters with null for a black square,
     num is the same shape carrying the clue number or 0. Pass letters=false
     for the puzzle and true for the answer key. */
  function crossword(cells, num, letters) {
    var o = [], r, c, v, n;
    o.push('<table class="cqp-grid cqp-cw" style="--cqp-n:' + cells[0].length + '">');
    for (r = 0; r < cells.length; r++) {
      o.push("<tr>");
      for (c = 0; c < cells[r].length; c++) {
        v = cells[r][c];
        if (v === null || v === undefined) { o.push('<td class="cqp-block"></td>'); continue; }
        n = num && num[r] ? num[r][c] : 0;
        o.push("<td>" + (n > 0 ? '<i class="cqp-num">' + n + "</i>" : "") +
               (letters ? esc(v) : "&nbsp;") + "</td>");
      }
      o.push("</tr>");
    }
    o.push("</table>");
    return o.join("");
  }

  /* Two columns of clues, Across and Down. */
  function clues(acrossTitle, across, downTitle, down) {
    function col(title, list) {
      var o = ['<div class="cqp-cluecol"><h2 class="cqp-cluehead">' + esc(title) + "</h2><dl>"];
      list.slice().sort(function (a, b) { return a.num - b.num; }).forEach(function (e) {
        o.push("<dt>" + e.num + ".</dt><dd>" + esc(e.clue) + "</dd>");
      });
      o.push("</dl></div>");
      return o.join("");
    }
    return '<div class="cqp-clues">' + col(acrossTitle, across) +
           col(downTitle, down) + "</div>";
  }

  /* The word list under a word search, or any short list of items laid out in
     columns so it does not run down a whole page. */
  function words(list, cols) {
    var o = ['<ul class="cqp-words" style="--cqp-cols:' + (cols || 3) + '">'];
    for (var i = 0; i < list.length; i++) o.push("<li>" + esc(list[i]) + "</li>");
    o.push("</ul>");
    return o.join("");
  }

  /* A numbered list of things to answer, each with a ruled line to write on.
     lineWidth is a CSS length; pass 0 for no line (the item is its own answer
     space, as in a crossword clue list). */
  function questions(items, lineWidth, cols) {
    var w = (lineWidth === 0 || lineWidth === "0") ? null
            : (lineWidth || "2.6cm");
    /* Thirty sums one per line down a page is not what a maths worksheet looks
       like, and it spills four questions onto a second sheet of paper for no
       reason. Columns fix both. CSS columns keep the numbering continuous. */
    var o = ['<ol class="cqp-qs' + (cols > 1 ? " cqp-cols" : "") +
             '" style="--cqp-cols:' + (cols || 1) + '">'], i;
    for (i = 0; i < items.length; i++) {
      /* The row is a flex box INSIDE the <li>, never the <li> itself.
         Making the list item a flex container removes its number in Chrome's
         print renderer, and a worksheet a teacher cannot say "number seven"
         about is worse than one with ragged lines. */
      o.push('<li><span class="cqp-qrow"><span class="cqp-q">' + items[i] + "</span>" +
             (w ? '<span class="cqp-line" style="min-width:' + w + '"></span>' : "") +
             "</span></li>");
    }
    o.push("</ol>");
    return o.join("");
  }

  /* A plain numbered answer list for the key. */
  function answers(items, cols) {
    var o = ['<ol class="cqp-key-list' + (cols > 1 ? " cqp-cols" : "") +
             '" style="--cqp-cols:' + (cols || 1) + '">'];
    for (var i = 0; i < items.length; i++) o.push("<li>" + items[i] + "</li>");
    o.push("</ol>");
    return o.join("");
  }

  /* Cards to cut out — charades words, prompt cards. An item may be a plain
     string, or {main, sub} when the card needs a second smaller line (the
     category, so a child miming "Rooster" and a child miming "Frozen" know
     which kind of thing they are being asked for). */
  function cards(list) {
    var o = ['<div class="cqp-cards">'], i, x;
    for (i = 0; i < list.length; i++) {
      x = list[i];
      if (x && typeof x === "object") {
        o.push('<div class="cqp-card"><b>' + esc(x.main) + "</b>" +
               (x.sub ? '<i class="cqp-cardsub">' + esc(x.sub) + "</i>" : "") + "</div>");
      } else {
        o.push('<div class="cqp-card"><b>' + esc(x) + "</b></div>");
      }
    }
    o.push("</div>");
    return o.join("");
  }

  /* A bordered grid of whole words — the sixteen tiles of Word Groups. Not
     grid(), which rules 9mm squares for single letters. */
  function tiles(list, cols) {
    var o = ['<div class="cqp-tiles" style="--cqp-cols:' + (cols || 4) + '">'];
    for (var i = 0; i < list.length; i++) {
      o.push('<span class="cqp-tile">' + esc(list[i]) + "</span>");
    }
    o.push("</div>");
    return o.join("");
  }

  /* A labelled box with ruled lines inside it, for an answer a child writes
     out rather than picks. */
  function boxes(labels, lines) {
    var o = ['<div class="cqp-boxes">'], i, j;
    for (i = 0; i < labels.length; i++) {
      o.push('<div class="cqp-box"><b>' + esc(labels[i]) + "</b>");
      for (j = 0; j < (lines || 1); j++) o.push('<span class="cqp-line"></span>');
      o.push("</div>");
    }
    o.push("</div>");
    return o.join("");
  }

  /* Ruled blank lines to write on, for a play sheet with no fixed answer. */
  function blanks(labels) {
    var o = ['<ul class="cqp-blanks">'];
    for (var i = 0; i < labels.length; i++) {
      o.push('<li><span class="cqp-blabel">' + esc(labels[i]) +
             '</span><span class="cqp-line"></span></li>');
    }
    o.push("</ul>");
    return o.join("");
  }

  /* ---------- what each sheet is called, and what it tells the child -------

     These live HERE and not on the ten game pages, and that is not tidiness.
     tools/split_fr.py decides which French keys a page may download by scanning
     a short list of JavaScript FILES. A string sitting in a game's inline
     <script> matches no file, so it is dropped from every chunk — which is
     exactly why the first build printed English sheets on the French pages
     while the dictionary held perfect translations. Scanning the inline blocks
     instead was tried and took the core chunk from 3 KB to 1,076 KB, because
     those blocks carry the word lists and the question banks.

     So the wording a sheet shows belongs to the printer, and the puzzle
     belongs to the game. The pairs are registered by
     tools/newq/build_printpuzzles.py. Times Tables and Math Race are not here:
     they carry their own T(en, fr) and need no dictionary. */
  var SHEET = {
    /* Each note is ONE unbroken string literal, however long the line. It has
       to be: tools/split_fr.py finds a key by searching this file's text for
       it, and a string split across a + never appears whole. Written as two
       joined halves on the first build, the notes matched nothing and printed
       in English on the French pages while the dictionary held the French. */
    "word-search": {
      title: "Word Search",
      note: "Find every word in the list. Words run across, down or diagonally, and some are written backwards."
    },
    "sudoku": {
      title: "Sudoku",
      note: "Fill every empty square so each row, each column and each small box of nine contains the numbers 1 to 9 exactly once."
    },
    "crossword": {
      title: "Crossword",
      note: "Write one letter in each white square. The number in a square is the clue number."
    },
    "scramble": {
      title: "Word Scramble",
      note: "Unscramble each Canadian word and write it on the line. The hint is there if you get stuck."
    },
    "word-groups": {
      title: "Word Groups",
      groups: ["Group 1", "Group 2", "Group 3", "Group 4"],
      note: "Sort the sixteen words into four groups of four. Write each group on a line, and say what the four words have in common."
    },
    "categories": {
      title: "Categories",
      note: "Write something for every category that starts with the big letter. One word each, and no repeats."
    },
    "charades": {
      title: "Charades cards", noname: true,
      note: "Cut along the dotted lines, fold the cards and put them in a bowl. One player takes a card and acts it out — no talking, no pointing."
    },
    "would-you-rather": {
      title: "Would You Rather?",
      note: "Circle the one you would pick, then write one reason on the line."
    }
  };
  function spec(key) {
    var s = SHEET[key] || {};
    return { title: s.title || "", note: s.note || "", noname: !!s.noname,
             groups: s.groups || [] };
  }

  /* ---------- the sheet ---------- */

  function page(spec, bodyHTML, n, total, isKey) {
    var o = [];
    o.push('<section class="cqp-sheet' + (isKey ? " cqp-keysheet" : "") + '">');
    o.push('<header class="cqp-head">');
    /* The title sits in its own <span>, so its text node is EXACTLY the title
       and the dictionary can match it. Written as "Word Groups — Answer key" in
       one node, the key page printed an English title under a French one,
       because "Word Groups — " is not a key and "Word Groups" is. The dash
       between them is its own node and too short to be looked up. */
    o.push('<h1 class="cqp-title"><span>' + esc(spec.title) + "</span>" +
           (isKey ? ' &mdash; <span class="cqp-keyword">Answer key</span>' : "") +
           "</h1>");
    o.push('<p class="cqp-src" data-no-i18n>canada-quiz.com</p>');
    o.push("</header>");
    /* A sheet that gets cut into thirty cards has nobody's name on it. */
    if (!isKey && !spec.noname) {
      o.push('<div class="cqp-meta"><span>Name:</span><span>Date:</span></div>');
    }
    /* "1 / 3", not "Sheet 1 of 3". A counter built from words would be one
       text node with a number inside it, which the dictionary cannot match —
       the same fault that left nine French meta descriptions in English. */
    if (total > 1) {
      o.push('<p class="cqp-copy" data-no-i18n>' + n + " / " + total + "</p>");
    }
    if (spec.note && !isKey) o.push('<p class="cqp-note">' + spec.note + "</p>");
    o.push('<div class="cqp-body">' + bodyHTML + "</div>");
    /* One literal, for the same reason the notes above are. */
    o.push('<footer class="cqp-foot">Free to use and to photocopy. Unofficial practice. Not affiliated with the Government of Canada.</footer>');
    o.push("</section>");
    return o.join("");
  }

  function sheet(spec) {
    var old = document.getElementById(ROOT_ID);
    if (old && old.parentNode) old.parentNode.removeChild(old);

    var list = spec.sheets || [], keys = spec.keys || [];
    if (!list.length) return;

    var o = [], i;
    for (i = 0; i < list.length; i++) o.push(page(spec, list[i], i + 1, list.length, false));
    for (i = 0; i < keys.length; i++) {
      if (keys[i]) o.push(page(spec, keys[i], i + 1, keys.length, true));
    }

    var root = document.createElement("div");
    root.id = ROOT_ID;
    root.className = "cqp";
    root.innerHTML = o.join("");
    document.body.appendChild(root);
    /* The print rules hang off this class, never off the page. Without it a
       global "hide everything except the sheet" rule would hide the whole of
       every other page on the site the moment anyone pressed Ctrl+P. */
    document.body.className += " cqp-printing";

    /* Translate before printing, not after. See the note at the top. */
    if (window.CQ && window.CQ.lang === "fr" && window.CQ.translateNode) {
      try { window.CQ.translateNode(root); } catch (e) {}
    }

    function cleanup() {
      if (root.parentNode) root.parentNode.removeChild(root);
      document.body.className =
        document.body.className.replace(/\s*\bcqp-printing\b/g, "");
      if (window.removeEventListener) window.removeEventListener("afterprint", cleanup);
    }
    if (window.addEventListener) window.addEventListener("afterprint", cleanup);
    /* Safari fires no afterprint; sweep up on the next turn of the loop. */
    setTimeout(function () { if (document.getElementById(ROOT_ID)) cleanup(); }, 45000);

    /* One frame, so the browser has laid the sheet out before it measures it
       for pagination. Printing in the same tick puts the answer key on page 1
       on some builds of Chrome. */
    if (window.requestAnimationFrame) {
      requestAnimationFrame(function () { setTimeout(function () { window.print(); }, 30); });
    } else {
      setTimeout(function () { window.print(); }, 60);
    }
  }

  /* ---------- many copies from the page's own generator ---------- */

  /* make() must build a NEW puzzle and return {body, key}. Called once per
     copy, so thirty children get thirty different puzzles. */
  function build(spec, make, copies) {
    copies = Math.max(1, Math.min(40, parseInt(copies, 10) || 1));
    var sheets = [], keys = [], one, i;
    for (i = 0; i < copies; i++) {
      one = make(i);
      if (!one) continue;
      sheets.push(one.body);
      keys.push(one.key || "");
    }
    spec.sheets = sheets;
    spec.keys = keys.join("") ? keys : [];
    sheet(spec);
  }

  /* ---------- ?print=1&copies=N — how the hub page drives a game ---------- */

  /* A game page calls CQPrint.auto(fn) at the end of its script. If the URL
     asks for a print, fn(copies) runs once the page has settled. The hub page
     at printable-puzzles.html links here rather than generating anything
     itself, which is the whole reason no puzzle is drawn twice. */
  function auto(fn) {
    var q = {};
    location.search.replace(/^\?/, "").split("&").forEach(function (kv) {
      if (!kv) return;
      var p = kv.split("=");
      q[decodeURIComponent(p[0])] = decodeURIComponent(p[1] || "");
    });
    if (!q.print) return;
    var go = function () { try { fn(q.copies || 1, q); } catch (e) {} };
    if (document.readyState === "complete") setTimeout(go, 250);
    else window.addEventListener("load", function () { setTimeout(go, 250); });
  }

  window.CQPrint = {
    sheet: sheet, build: build, auto: auto, spec: spec,
    grid: grid, sudokuGrid: sudokuGrid, crossword: crossword, clues: clues,
    words: words, tiles: tiles, boxes: boxes,
    questions: questions, answers: answers, cards: cards, blanks: blanks,
    esc: esc
  };
})();
