/* canada-quiz.com — the Share button.
 *
 * Asked for 28 September 2026. The site already had the receiving half — the
 * cards in images/social/ that make a pasted link look like something — but
 * nothing on the page ever invited anyone to send a link. The cards only helped
 * people who thought to copy the address out of the bar themselves.
 *
 * It appears in one place on purpose: the moment somebody finishes a quiz, a
 * personality quiz or a game and is looking at their score. That is when a
 * person feels like telling someone. A share button in the header, which is
 * where they usually go, is furniture nobody reads.
 *
 * On a phone it opens the system share sheet, so the visitor picks WhatsApp or
 * Messages or whatever they actually use, and the site never sees the choice.
 * On a desktop, where navigator.share mostly does not exist, it copies the link
 * and says so.
 *
 * The address it shares is location.href, which since js/quiz-back.js includes
 * the topic — so sharing from the end of Saving & Spending sends a link that
 * opens Saving & Spending, not the front of the site.
 *
 * Two result surfaces are covered, which between them are every page that ends
 * in a score:
 *   - the quiz pages' own  #result-screen / #result  panel   (20 pages)
 *   - the shared end card js/endcard.js draws, .cq-end       (12 game pages)
 *
 * No words are added to the markup, so the French pages need no dictionary
 * entry: the two strings below are chosen by the same URL test the rest of the
 * site uses.
 */
(function () {
  "use strict";

  var FR = /(^|\/)fr\/[^\/]*$/.test(location.pathname);
  var SHARE = FR ? "Partager" : "Share";
  var COPIED = FR ? "Lien copié" : "Link copied";
  var FAILED = FR ? "Copie impossible" : "Couldn't copy";

  function title() {
    /* the <title> carries the site name for Google's results page; a share
       sheet has its own line for that, so trim it back to the page itself */
    return (document.title || "Canada Quiz")
      .replace(/\s*[|—-]\s*Canada Quiz.*$/, "")
      .trim() || "Canada Quiz";
  }

  function toast(btn, msg) {
    var old = btn.textContent;
    btn.textContent = msg;
    btn.disabled = true;
    setTimeout(function () {
      btn.textContent = old;
      btn.disabled = false;
    }, 1800);
  }

  function track(how) {
    try {
      if (typeof window.gtag === "function") {
        window.gtag("event", "share_click", {
          method: how,
          page_location: location.href
        });
      }
    } catch (e) { /* analytics must never break a button */ }
  }

  function doShare(btn) {
    var data = { title: title(), text: title(), url: location.href };
    if (navigator.share) {
      navigator.share(data).then(function () { track("sheet"); })
        /* the visitor closing the sheet rejects the promise; that is a normal
           thing to do and must not look like an error */
        .catch(function () {});
      return;
    }
    var url = location.href;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () {
        toast(btn, COPIED); track("copy");
      }).catch(function () { legacy(btn, url); });
    } else {
      legacy(btn, url);
    }
  }

  /* clipboard access needs a secure context, so an older browser or a page
     opened over plain http still gets something that works */
  function legacy(btn, url) {
    try {
      var t = document.createElement("textarea");
      t.value = url;
      t.setAttribute("readonly", "");
      t.style.position = "fixed";
      t.style.top = "-1000px";
      document.body.appendChild(t);
      t.select();
      var ok = document.execCommand && document.execCommand("copy");
      document.body.removeChild(t);
      toast(btn, ok ? COPIED : FAILED);
      if (ok) track("copy-legacy");
    } catch (e) {
      toast(btn, FAILED);
    }
  }

  /* Copy the classes off the button it will stand next to, so it matches
     whatever that page's buttons look like — full width where they are full
     width, same height, same rounding — instead of a smaller odd one out.
     Any colour class is dropped: Share is the quieter, secondary action and
     should not compete with "Pick another topic". */
  function make(like) {
    var b = document.createElement("button");
    b.type = "button";
    var cls = "btn btn-ghost";
    if (like && like.className) {
      cls = like.className.split(/\s+/).filter(function (c) {
        return c === "btn" || c === "btn-lg" || c === "btn-block";
      }).join(" ");
      if (cls.indexOf("btn") !== 0) cls = "btn " + cls;
      cls += " btn-ghost";
    }
    b.className = cls.trim();
    b.setAttribute("data-cq-share", "1");
    b.setAttribute("data-no-i18n", "");   // the label is already in the right language
    b.textContent = SHARE;
    b.addEventListener("click", function () { doShare(b); });
    return b;
  }

  function addTo(row) {
    if (!row || row.querySelector("[data-cq-share]")) return;
    row.appendChild(make(row.querySelector(".btn")));
  }

  /* Put it beside the buttons that are already there rather than at the bottom
     of the panel. Guessing "the first div" was not good enough: on
     citizenship.html and the personality quizzes that div holds text, so the
     button fell through to the end of the whole section, and on scramble.html
     it landed inside a paragraph. Finding the last existing .btn and sitting
     next to it works on all twenty result panels whatever their markup. */
  function addBeside(panel) {
    if (!panel || panel.querySelector("[data-cq-share]")) return;
    var btns = panel.querySelectorAll(".btn");
    var last = btns.length ? btns[btns.length - 1] : null;
    if (last && last.parentNode) {
      last.parentNode.insertBefore(make(last), last.nextSibling);
    } else {
      panel.appendChild(make(null));
    }
  }

  /* --- the quiz pages' own result panel ---------------------------------- */
  var panel = document.getElementById("result-screen")
           || document.getElementById("result");

  function fitPanel() {
    if (!panel) return;
    if (getComputedStyle(panel).display === "none") return;
    addBeside(panel);
  }

  if (panel) {
    fitPanel();
    /* the panel is revealed by a style change, which is an attribute mutation */
    if (window.MutationObserver) {
      new MutationObserver(fitPanel)
        .observe(panel, { attributes: true, attributeFilter: ["style", "class"] });
    }
  }

  /* --- the shared end card the games draw -------------------------------- */
  if (window.MutationObserver) {
    new MutationObserver(function (recs) {
      for (var i = 0; i < recs.length; i++) {
        var added = recs[i].addedNodes;
        for (var j = 0; j < added.length; j++) {
          var n = added[j];
          if (n.nodeType !== 1) continue;
          var card = n.classList && n.classList.contains("cq-end")
                   ? n : (n.querySelector && n.querySelector(".cq-end"));
          if (card) addTo(card.querySelector(".cq-end-btns"));
        }
      }
    }).observe(document.body, { childList: true, subtree: true });
  }
})();
