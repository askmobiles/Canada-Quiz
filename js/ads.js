/* Canada Quiz — ads.js
   ---------------------------------------------------------------------------
   WHY THIS FILE EXISTS

   The Google AdSense script used to sit in the <head> of every page. Google's
   ad code is big (about 220 KB) and it starts downloading before the page has
   even drawn, so on a phone it steals bandwidth from the picture and the text
   the visitor is actually waiting for. PageSpeed measured this as the single
   biggest thing slowing the site down on mobile.

   So now we load AdSense LATE instead:
       * as soon as the visitor touches, scrolls, clicks or types  — OR
       * a short moment after the page has finished loading,
   whichever happens first.

   The visitor still sees the same ads. They just arrive after the page is
   readable instead of fighting with it. Nothing about the ads themselves
   changes — it is still normal AdSense Auto ads, no pop-ups, no interstitials.
   --------------------------------------------------------------------------- */
(function () {
  var CLIENT = "ca-pub-7256851069341390";
  var SRC = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + CLIENT;
  var IDLE_DELAY = 1200;   // ms after the page finishes loading
  var loaded = false;

  // Ask the browser to warm up the connections a moment before we need them,
  // so the ad code arrives faster once we do ask for it.
  function warm() {
    var hosts = [
      "https://pagead2.googlesyndication.com",
      "https://googleads.g.doubleclick.net",
      "https://tpc.googlesyndication.com",
      "https://fundingchoicesmessages.google.com"
    ];
    for (var i = 0; i < hosts.length; i++) {
      var l = document.createElement("link");
      l.rel = "preconnect";
      l.href = hosts[i];
      l.crossOrigin = "anonymous";
      document.head.appendChild(l);
    }
  }

  function load() {
    if (loaded) return;
    loaded = true;
    off();
    warm();
    var s = document.createElement("script");
    s.async = true;
    s.src = SRC;
    s.crossOrigin = "anonymous";
    s.setAttribute("data-ad-client", CLIENT);
    document.head.appendChild(s);
  }

  var EVENTS = ["pointerdown", "touchstart", "keydown", "scroll", "wheel", "mousemove"];
  function on() {
    for (var i = 0; i < EVENTS.length; i++) {
      window.addEventListener(EVENTS[i], load, { passive: true, once: true });
    }
  }
  function off() {
    for (var i = 0; i < EVENTS.length; i++) {
      window.removeEventListener(EVENTS[i], load);
    }
  }

  function arm() {
    if (window.requestIdleCallback) {
      requestIdleCallback(load, { timeout: IDLE_DELAY });
    } else {
      setTimeout(load, IDLE_DELAY);
    }
  }

  on();
  if (document.readyState === "complete") arm();
  else window.addEventListener("load", arm, { once: true });
})();
