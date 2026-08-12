/* kids-quiz.js — the three questions at the bottom of a For Kids story.

   Deliberately tiny and deliberately gentle. These are six to nine year olds:
   there is no timer, no score to be ashamed of, and a wrong answer shows the
   right one with a friendly sentence rather than a red cross and nothing else.

   It writes into markup that is already in the page — an .options box and an
   #explain-box — rather than building its own, so the two things that make the
   site usable for this age group attach with no extra work:
   read-aloud.js reads the question and answers out loud, and
   game-fullscreen.js can put the quiz on a television. */
(function () {
  "use strict";

  var Q = window.KIDS_Q || [];
  if (!Q.length) return;

  var FR = /\/fr\//.test(location.pathname);
  function T(en, fr) { return FR ? fr : en; }
  function L(pair) { return FR ? pair[1] : pair[0]; }

  var host = document.getElementById("kq");
  if (!host) return;
  var qEl = document.getElementById("kq-q");
  var box = document.getElementById("kq-opts");
  var exp = document.getElementById("explain-box");
  var next = document.getElementById("kq-next");
  var done = document.getElementById("kq-done");
  if (!qEl || !box || !exp || !next || !done) return;

  var i = 0, right = 0, answered = false;

  /* The answers are written with the correct one first, because that is far
     easier to read and check in the source file. If they were shown that way a
     child would work out the trick in two questions, so they are shuffled here
     on every play. correct holds where the right answer landed this time. */
  var order = [], correct = 0;

  function shuffle(q) {
    order = q.a.map(function (_, n) { return n; });
    for (var k = order.length - 1; k > 0; k--) {
      var j = Math.floor(Math.random() * (k + 1));
      var t = order[k]; order[k] = order[j]; order[j] = t;
    }
    correct = order.indexOf(q.c);
  }

  function draw() {
    answered = false;
    var q = Q[i];
    shuffle(q);
    qEl.textContent = (i + 1) + ". " + L(q.q);
    box.innerHTML = "";
    exp.hidden = true;
    exp.className = "kq-exp";
    next.hidden = true;
    order.forEach(function (src, n) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "option";
      b.textContent = L(q.a[src]);
      b.addEventListener("click", function () { pick(n, b); });
      box.appendChild(b);
    });
  }

  function pick(n, btn) {
    if (answered) return;
    answered = true;
    var q = Q[i];
    var opts = box.querySelectorAll(".option");
    for (var k = 0; k < opts.length; k++) {
      opts[k].disabled = true;
      if (k === correct) opts[k].classList.add("correct");
    }
    if (n === correct) { right++; btn.classList.add("correct"); }
    else { btn.classList.add("wrong"); }
    exp.hidden = false;
    exp.className = "kq-exp " + (n === correct ? "good" : "oops");
    exp.textContent = (n === correct ? T("Yes! ", "Oui ! ") : T("Not quite. ", "Presque. "))
                    + L(q.e);
    next.hidden = false;
    next.textContent = (i === Q.length - 1)
      ? T("See how you did", "Voir ton résultat")
      : T("Next question", "Question suivante");
  }

  next.addEventListener("click", function () {
    if (i < Q.length - 1) { i++; draw(); return; }
    host.querySelector(".kq-play").hidden = true;
    done.hidden = false;
    /* Nobody fails a story. Every ending is encouraging, and the button to go
       round again is the point — a child who got one wrong should want to. */
    var msg = right === Q.length
      ? T("Perfect! You got all " + Q.length + ".", "Parfait ! Tu as eu les " + Q.length + ".")
      : (right >= Q.length - 1
         ? T("Very good — " + right + " out of " + Q.length + ".",
             "Très bien — " + right + " sur " + Q.length + ".")
         : T("You got " + right + " out of " + Q.length + ". Read the story again and try once more!",
             "Tu as eu " + right + " sur " + Q.length + ". Relis l'histoire et réessaie !"));
    done.innerHTML = "";
    var big = document.createElement("div");
    big.className = "kq-score";
    big.textContent = (right === Q.length ? "🌟 " : "🍁 ") + msg;
    var again = document.createElement("button");
    again.type = "button";
    again.className = "btn btn-green";
    again.textContent = T("Play again", "Rejouer");
    again.addEventListener("click", function () {
      i = 0; right = 0;
      done.hidden = true;
      host.querySelector(".kq-play").hidden = false;
      draw();
    });
    done.appendChild(big);
    done.appendChild(again);
  });

  draw();
})();
