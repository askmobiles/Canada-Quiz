/* ============================================================
   Canada Quiz — visitor tracking (one file for the whole site)
   ------------------------------------------------------------
   This file is loaded by all 218 pages, English and French.
   Nothing else anywhere on the site needs to change.

   TO TURN IT ON, fill in one or both lines below, then push.

   1) CLOUDFLARE  — easiest, you already own the domain there.
      Cloudflare dashboard -> Analytics & Logs -> Web Analytics
      -> Add a site -> canada-quiz.com. It shows you a snippet
      containing  "token":"abc123..."  — paste ONLY that token.
      Free, unlimited, no cookies, so no cookie banner needed.

   2) GOOGLE ANALYTICS 4 — deeper: which quizzes get finished,
      pass rates, English vs French, where people come from.
      analytics.google.com -> Admin -> Create property ->
      Web data stream for canada-quiz.com -> copy the
      Measurement ID, which looks like  G-ABCD1234XY.

   Using both is fine, and is what I would do.
   ============================================================ */
var GA4_ID = "";              // <-- paste your G-XXXXXXXXXX here
var CF_BEACON_TOKEN = "";     // <-- paste your Cloudflare token here

(function () {
  "use strict";

  /* ---------- 1. Google Analytics 4 ---------- */
  if (GA4_ID && GA4_ID.indexOf("G-") === 0) {
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA4_ID;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    gtag("js", new Date());
    gtag("config", GA4_ID, { anonymize_ip: true });
  }

  /* ---------- 2. Cloudflare Web Analytics (optional) ---------- */
  if (CF_BEACON_TOKEN) {
    var c = document.createElement("script");
    c.defer = true;
    c.src = "https://static.cloudflareinsights.com/beacon.min.js";
    c.setAttribute("data-cf-beacon", '{"token":"' + CF_BEACON_TOKEN + '"}');
    document.head.appendChild(c);
  }

  /* ---------- 3. What did people actually DO? ---------- */
  function track(name, params) {
    if (typeof window.gtag === "function") window.gtag("event", name, params || {});
  }
  /* Any other script on the site can report something: CQ_TRACK("name", {..}) */
  window.CQ_TRACK = track;

  var page = (location.pathname.split("/").pop() || "index.html").replace(".html", "");
  var lang = /\/fr\//.test(location.pathname) ? "fr" : "en";
  var kind = "other";
  /* driving first — a page like "manitoba-class-5-mock-test" would otherwise
     fall through to "other" and disappear into the noise, and driving is the
     part of the site we are betting on */
  if (/-g1-|class-5|class-7|road-signs|rules-of-the-road|driving|licence/.test(page)) kind = "driving";
  else if (/quiz|citizenship/.test(page)) kind = "quiz";
  else if (/game|puzzle|snake|memory|charades|imposter|chess|checkers|sudoku|crossword|scramble|bee|tiles|wheel|draw|answers|categories|story|head|rather|showdown|tictactoe|beaver|inukshuk|word|typing|colour|color|minesweeper|rubik|2048|connections/.test(page)) kind = "game";
  else if (/blog|canada|history|citizen|tips|facts|flag|symbol|language|holiday|animal|geography|government|indigenous|confederation|rights|province/.test(page)) kind = "article";

  /* Did they stay long enough to really use it? */
  var stayed = false;
  setTimeout(function () {
    stayed = true;
    track("engaged_15s", { page_name: page, content_kind: kind });
  }, 15000);

  /* Clicks on quiz answers, game buttons and category cards */
  var started = false;
  document.addEventListener("click", function (e) {
    var t = e.target;
    if (!t || !t.className || typeof t.className !== "string") return;
    if (/\boption\b/.test(t.className)) {
      if (!started) {
        started = true;
        track("quiz_start", { page_name: page, content_kind: kind, language: lang });
      }
      track("quiz_answer", { page_name: page });
    } else if (/\bbtn\b/.test(t.className)) {
      var label = (t.textContent || "").trim().slice(0, 40);
      track("button_click", { page_name: page, button_label: label, content_kind: kind });
    }
  }, true);

  /* ---------- 3b. Who FINISHED, and did they pass? ----------
     This is the number that actually matters on a quiz site: not how many
     people opened a page, but how many played it to the end.

     Every quiz and every driving test — all 218 pages, both languages —
     ends by putting a .result-big element on the screen. So instead of
     editing every quiz one by one, we simply watch for that element to
     appear. New quizzes are covered automatically, with nothing to add. */
  function readResult(box) {
    var txt = (box.textContent || "").replace(/\s+/g, " ");
    /* the score line is the reliable place to read from; the whole panel is
       only a fallback, because it also contains the missed-question review */
    var scoreEl = box.querySelector(".score");
    var scoreTxt = scoreEl ? scoreEl.textContent : txt;
    var got = null, outOf = null;
    /* "You scored 17 out of 20" · "17 / 20" · "Vous avez obtenu 17 sur 20" */
    var m = scoreTxt.match(/(\d+)\s*(?:\/|out of|sur)\s*(\d+)/i);
    if (m) { got = parseInt(m[1], 10); outOf = parseInt(m[2], 10); }

    var passed = null;
    if (box.querySelector(".result-big.pass")) passed = true;
    else if (box.querySelector(".result-big.fail")) passed = false;
    else if (/\bPASS\b|RÉUSSI|REUSSI/i.test(txt)) passed = true;
    else if (/TRY AGAIN|\bFAIL\b|ÉCHEC|ECHEC/i.test(txt)) passed = false;

    var out = { page_name: page, content_kind: kind, language: lang };
    if (got !== null && outOf) {
      out.score = got;
      out.out_of = outOf;
      out.percent = Math.round((got / outOf) * 100);
    }
    if (passed !== null) out.passed = passed ? "yes" : "no";
    return out;
  }

  /* Careful: on some pages the result screen already sits in the HTML from the
     start, hidden with display:none. So "does it exist?" would fire the moment
     the page opened. What we look for is the result screen becoming VISIBLE. */
  function visibleResult() {
    var all = document.querySelectorAll(".result-big");
    for (var i = 0; i < all.length; i++) {
      if (all[i].offsetParent !== null) return all[i];
    }
    return null;
  }

  var reported = false;
  function checkForResult() {
    var box = visibleResult();
    if (!box) { reported = false; return; }  /* hidden again — next play counts */
    if (reported) return;
    reported = true;
    var panel = (box.closest && box.closest("section")) || box.parentElement || document.body;
    /* let the rest of the result screen finish drawing before reading it */
    setTimeout(function () { track("quiz_complete", readResult(panel)); }, 150);
  }

  if (window.MutationObserver) {
    var pending = null;
    new MutationObserver(function () {
      if (pending) return;
      pending = setTimeout(function () { pending = null; checkForResult(); }, 200);
    }).observe(document.documentElement, {
      childList: true, subtree: true,
      attributes: true, attributeFilter: ["style", "class", "hidden"]
    });
  }

  /* ---------- 4. A private counter just for the owner ----------
     Stored only in this browser. Visit  yoursite.com/?mystats
     on your own phone or computer to see your own play history.
     No personal data, nothing sent anywhere.                     */
  try {
    var K = "cq_local_stats";
    var d = JSON.parse(localStorage.getItem(K) || "{}");
    d[page] = (d[page] || 0) + 1;
    d._total = (d._total || 0) + 1;
    d._first = d._first || new Date().toISOString().slice(0, 10);
    localStorage.setItem(K, JSON.stringify(d));

    if (location.search.indexOf("mystats") > -1) {
      var rows = Object.keys(d).filter(function (k) { return k[0] !== "_"; })
        .sort(function (a, b) { return d[b] - d[a]; })
        .map(function (k) { return "<tr><td style='padding:4px 12px'>" + k + "</td><td style='padding:4px 12px;text-align:right'><b>" + d[k] + "</b></td></tr>"; })
        .join("");
      var box = document.createElement("div");
      box.style.cssText = "position:fixed;inset:auto 10px 10px 10px;max-height:60vh;overflow:auto;background:#fff;border:3px solid #111;border-radius:14px;padding:14px;z-index:99999;font:14px system-ui";
      box.innerHTML = "<b>Your own visits on this device</b> (since " + d._first + ")<br>Total: <b>" + d._total +
        "</b><table style='margin-top:8px;width:100%'>" + rows + "</table>" +
        "<button style='margin-top:10px;padding:6px 14px;border-radius:8px;border:2px solid #111;background:#fff;font-weight:800' onclick='this.parentNode.remove()'>Close</button>";
      document.body.appendChild(box);
    }
  } catch (err) { /* private mode — ignore */ }
})();
