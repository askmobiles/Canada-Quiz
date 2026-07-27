/* ============================================================
   Canada Quiz — visitor tracking (one file for the whole site)
   ------------------------------------------------------------
   TO TURN IT ON: paste your Google Analytics ID on the line below,
   between the quotes. It looks like:  G-ABCD1234XY
   Nothing else needs to change anywhere on the site.
   ============================================================ */
var GA4_ID = "";              // <-- paste your G-XXXXXXXXXX here
var CF_BEACON_TOKEN = "";     // optional: Cloudflare Web Analytics token

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

  var page = (location.pathname.split("/").pop() || "index.html").replace(".html", "");
  var kind = "other";
  if (/quiz|citizenship/.test(page)) kind = "quiz";
  else if (/game|puzzle|snake|memory|charades|imposter|chess|checkers|sudoku|crossword|scramble|bee|tiles|wheel|draw|answers|categories|story|head|rather|showdown|tictactoe|beaver|inukshuk|word|typing|colour|color|minesweeper|rubik|2048|connections/.test(page)) kind = "game";
  else if (/blog|canada|history|citizen|tips|facts|flag|symbol|language|holiday|animal|geography|government|indigenous|confederation|rights|province/.test(page)) kind = "article";

  /* Did they stay long enough to really use it? */
  var stayed = false;
  setTimeout(function () {
    stayed = true;
    track("engaged_15s", { page_name: page, content_kind: kind });
  }, 15000);

  /* Clicks on quiz answers, game buttons and category cards */
  document.addEventListener("click", function (e) {
    var t = e.target;
    if (!t || !t.className || typeof t.className !== "string") return;
    if (/\boption\b/.test(t.className)) {
      track("quiz_answer", { page_name: page });
    } else if (/\bbtn\b/.test(t.className)) {
      var label = (t.textContent || "").trim().slice(0, 40);
      track("button_click", { page_name: page, button_label: label, content_kind: kind });
    }
  }, true);

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
