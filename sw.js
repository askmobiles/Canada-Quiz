/* Canada Quiz — service worker.  GENERATED FILE: edit tools/sw_template.js.

   This is what turns the site into an app you can keep on your phone: an icon
   on the home screen, no browser bar, and the games still working with no
   signal at all.

   Rules, and the reason for each one:

     * Only same-origin GET requests are touched. AdSense and Google Analytics
       live on other domains and are passed straight through, so nothing about
       ads or stats changes and nothing of theirs is ever stored here.

     * Pages (navigations) are NETWORK FIRST. When a new build is pushed,
       anyone online sees it on the next tap — a cached page can never get
       stuck in front of a fresh one. Offline, the saved copy is served, and
       if that page was never visited, offline.html is.

     * Files with a ?v= stamp are CACHE FIRST. That stamp is a hash of the file
       itself, so the address changes whenever the bytes change. Serving those
       from the cache forever is free and always correct.

     * Everything else is STALE WHILE REVALIDATE: instant from the cache, and
       quietly refreshed in the background for next time.

     * The runtime cache is capped, so a tablet never fills up with 250 pages
       and a 2.4 MB French dictionary it will not read again.
*/
var VERSION = "0b04ed9ca9f5";
var SHELL = "cq-shell-" + VERSION;
var RUNTIME = "cq-run-" + VERSION;
var MAX_RUNTIME = 220;

/* The handful of files worth having before the first tap offline. */
var PRECACHE = [
  "index.html",
  "games.html",
  "quizzes.html",
  "offline.html",
  "citizenship.html",
  "driving-test.html",
  "daily.html",
  "css/style.css?v=067f9fdc",
  "js/site.js?v=e0e44d26",
  "js/game-fullscreen.js?v=35da7b56",
  "js/endcard.js?v=e6598278",
  "js/tv-mode.js?v=836e4dd9",
  "js/pwa.js?v=cb9b3ff7",
  "brand/logo-horizontal-white.svg",
  "brand/favicon.svg",
  "brand/icon-192.png",
  "brand/icon-512.png",
  "brand/apple-touch-icon.png",
  "site.webmanifest"
];

self.addEventListener("install", function (e) {
  e.waitUntil(
    caches.open(SHELL).then(function (c) {
      /* addAll fails the whole install if a single file 404s, which would
         leave the visitor with no service worker at all. One at a time, and
         a miss is survivable. */
      return Promise.all(PRECACHE.map(function (u) {
        return c.add(new Request(u, { cache: "reload" })).catch(function () { });
      }));
    })
    /* Deliberately NO skipWaiting() here. A new worker waits its turn, js/pwa.js
       notices and offers the visitor a Refresh button, and only that button
       sends the skip-waiting message below. Taking over on our own would
       reload the page under somebody mid-quiz. */
  );
});

self.addEventListener("activate", function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) {
        if (k !== SHELL && k !== RUNTIME) return caches.delete(k);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener("message", function (e) {
  if (e.data === "skip-waiting") self.skipWaiting();
});

function trim(name, max) {
  caches.open(name).then(function (c) {
    c.keys().then(function (keys) {
      if (keys.length <= max) return;
      for (var i = 0; i < keys.length - max; i++) c.delete(keys[i]);
    });
  });
}

function isPage(req) {
  return req.mode === "navigate" ||
    (req.headers.get("accept") || "").indexOf("text/html") !== -1;
}

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;

  var url;
  try { url = new URL(req.url); } catch (err) { return; }
  if (url.origin !== self.location.origin) return;   /* ads, fonts, analytics */

  /* ---------------------------------------------------------- pages ----- */
  if (isPage(req)) {
    e.respondWith(
      fetch(req).then(function (res) {
        if (res && res.ok) {
          var copy = res.clone();
          caches.open(RUNTIME).then(function (c) {
            c.put(req, copy); trim(RUNTIME, MAX_RUNTIME);
          });
        }
        return res;
      }).catch(function () {
        return caches.match(req).then(function (hit) {
          return hit || caches.match("offline.html") ||
            new Response("Offline", { status: 503, headers: { "Content-Type": "text/plain" } });
        });
      })
    );
    return;
  }

  /* --------------------------------------- stamped files never change ---- */
  if (url.search.indexOf("v=") !== -1) {
    e.respondWith(
      caches.match(req).then(function (hit) {
        if (hit) return hit;
        return fetch(req).then(function (res) {
          if (res && res.ok) {
            var copy = res.clone();
            caches.open(RUNTIME).then(function (c) {
              c.put(req, copy); trim(RUNTIME, MAX_RUNTIME);
            });
          }
          return res;
        });
      })
    );
    return;
  }

  /* ------------------------------------------------- everything else ----- */
  e.respondWith(
    caches.match(req).then(function (hit) {
      var net = fetch(req).then(function (res) {
        if (res && res.ok) {
          var copy = res.clone();
          caches.open(RUNTIME).then(function (c) {
            c.put(req, copy); trim(RUNTIME, MAX_RUNTIME);
          });
        }
        return res;
      }).catch(function () { return hit; });
      return hit || net;
    })
  );
});
