/* Canada Quiz — printable worksheet builder.
   Draws from the three question banks already on the site and lays them out for
   paper. No PDF library and no server: the browser's own print dialog does the
   work, and "Save as PDF" is one of its destinations.

   French: site.js loads its dictionary chunks by looking at which question
   scripts a page carries, then a MutationObserver translates whatever is added
   to the DOM. Because this page carries all three banks, every sheet built here
   is translated automatically on /fr/. The fixed labels below ("Name", "Answer
   key", and so on) are registered into the dictionary by
   tools/newq/build_printables.py so they are translated the same way. */
(function () {
  "use strict";

  var topicSel = document.getElementById("pw-topic");
  var levelSel = document.getElementById("pw-level");
  var countSel = document.getElementById("pw-count");
  var makeBtn = document.getElementById("pw-make");
  var printBtn = document.getElementById("pw-print");
  var out = document.getElementById("pw-out");
  if (!topicSel || !out) return;

  var LEVELS = ["easy", "medium", "hard"];
  var LEVEL_NAME = { easy: "Easy", medium: "Medium", hard: "Hard" };

  /* ---------- normalise the three bank shapes into one ---------- */
  function norm(x) {
    /* GK uses {q,o,a,e}; the Canada and citizenship banks use
       {q,options,answer,explain}. */
    var opts = x.options || x.o || [];
    var ans = (typeof x.answer === "number") ? x.answer : x.a;
    return { q: x.q, opts: opts, a: ans, e: x.explain || x.e || "" };
  }

  /* ---------- what can be printed ---------- */
  /* fun-questions.js and citizenship-questions.js declare their banks with
     `const`, which creates a global LEXICAL binding — it is reachable as a bare
     name but NOT as a property of window. Reading window.FUN_QUESTIONS returns
     undefined and silently drops 544 of the 949 questions, which is exactly
     what happened on the first build. gk-questions.js assigns window.GK_BANK
     directly, so that one is a property. */
  var topics = [];
  var fun = (typeof FUN_QUESTIONS !== "undefined") ? FUN_QUESTIONS : null;
  if (fun && fun.length) {
    topics.push({ id: "canada", label: "Canada", levels: false,
                  get: function () { return fun.map(norm); } });
  }
  var cit = (typeof CITIZENSHIP_QUESTIONS !== "undefined") ? CITIZENSHIP_QUESTIONS : null;
  if (cit && cit.length) {
    topics.push({ id: "cit", label: "Citizenship practice", levels: false,
                  get: function () { return cit.map(norm); } });
  }
  if (window.GK_BANK) {
    Object.keys(window.GK_BANK).forEach(function (subject) {
      topics.push({
        id: "gk:" + subject, label: subject, levels: true,
        get: function (level) {
          var b = window.GK_BANK[subject], list = [];
          (level === "all" ? LEVELS : [level]).forEach(function (lv) {
            (b[lv] || []).forEach(function (x) { list.push(norm(x)); });
          });
          return list;
        }
      });
    });
  }

  topics.forEach(function (t) {
    var o = document.createElement("option");
    o.value = t.id; o.textContent = t.label;
    topicSel.appendChild(o);
  });

  function current() {
    for (var i = 0; i < topics.length; i++) {
      if (topics[i].id === topicSel.value) return topics[i];
    }
    return topics[0];
  }

  function fillLevels() {
    var t = current();
    levelSel.innerHTML = "";
    if (!t || !t.levels) {
      var one = document.createElement("option");
      one.value = "all"; one.textContent = "All levels";
      levelSel.appendChild(one);
      levelSel.disabled = true;
      return;
    }
    levelSel.disabled = false;
    [["all", "All levels"]].concat(LEVELS.map(function (lv) {
      return [lv, LEVEL_NAME[lv]];
    })).forEach(function (pair) {
      var o = document.createElement("option");
      o.value = pair[0]; o.textContent = pair[1];
      levelSel.appendChild(o);
    });
  }
  topicSel.addEventListener("change", fillLevels);
  fillLevels();

  /* ---------- pick the questions ---------- */
  function pick(list, n) {
    var copy = list.slice(), out = [];
    while (copy.length && out.length < n) {
      out.push(copy.splice(Math.floor(Math.random() * copy.length), 1)[0]);
    }
    return out;
  }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  var LETTERS = ["A", "B", "C", "D", "E", "F"];

  function build() {
    var t = current();
    if (!t) return;
    var qs = pick(t.get(levelSel.value || "all"), parseInt(countSel.value, 10) || 15);
    if (!qs.length) return;

    out.innerHTML = "";
    var sheet = el("div", "pw-sheet");

    var head = el("div", "pw-head");
    head.appendChild(el("h2", null, t.label));
    head.appendChild(el("p", "muted", "Printable quiz sheet from canada-quiz.com"));
    sheet.appendChild(head);

    var meta = el("div", "pw-meta");
    /* the label and the ruled line are separate elements so the label is its
       own text node — build_fr's runtime lookup matches whole text nodes */
    ["Name:", "Date:", "Score:"].forEach(function (label) {
      var wrap = el("span");
      wrap.appendChild(el("strong", null, label));
      wrap.appendChild(document.createTextNode(" ______________________"));
      meta.appendChild(wrap);
    });
    sheet.appendChild(meta);

    qs.forEach(function (q, i) {
      var box = el("div", "pw-q");
      box.appendChild(el("p", null, (i + 1) + ". " + q.q));
      var ul = el("ul", "pw-opts");
      q.opts.forEach(function (opt, j) {
        ul.appendChild(el("li", null, LETTERS[j] + ")  " + opt));
      });
      box.appendChild(ul);
      sheet.appendChild(box);
    });

    var note = el("p", "pw-note",
      "canada-quiz.com — free to use and photocopy. "
      + "Unofficial practice. Not affiliated with the Government of Canada.");
    sheet.appendChild(note);

    /* the key starts on a fresh sheet of paper, so the questions can be
       photocopied on their own */
    var key = el("div", "pw-key");
    key.appendChild(el("h2", null, "Answer key"));
    key.appendChild(el("p", "muted", t.label));
    var ol = document.createElement("ol");
    qs.forEach(function (q) {
      var li = document.createElement("li");
      var strong = el("strong", null, LETTERS[q.a] + ")  " + (q.opts[q.a] || ""));
      li.appendChild(strong);
      if (q.e) li.appendChild(document.createTextNode("  " + q.e));
      ol.appendChild(li);
    });
    key.appendChild(ol);
    sheet.appendChild(key);

    out.appendChild(sheet);
    sheet.setAttribute("tabindex", "-1");
    sheet.focus();
  }

  makeBtn.addEventListener("click", build);
  printBtn.addEventListener("click", function () {
    if (!out.firstChild) build();
    window.print();
  });

  build();
})();
