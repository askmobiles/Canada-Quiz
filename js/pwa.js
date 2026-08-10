/* pwa.js — "keep this on your device".

   Three jobs:
     1. Register the service worker, which is what makes the site work with no
        signal and lets a phone install it.
     2. Offer an Install button. Android and desktop Chrome hand us a real
        install prompt; Safari does not offer one to any website, so on an
        iPhone or iPad we show the two steps instead — Share, then Add to Home
        Screen. That is not a workaround we invented, it is the only route
        Apple provides.
     3. Tell the visitor, quietly and once, when a new version has downloaded,
        with a Refresh button. Without this a family that installed the app in
        August would still be playing the August build in December.

   No banner appears on top of the page and nothing pops up. The button lives
   in the footer, and a visitor who dismisses it is not asked again.

   Installing is also the real cure for Safari's "typing while in full screen"
   warning: a home-screen app has no browser bar to leave in the first place. */
(function () {
  "use strict";

  var FR = /\/fr\//.test(location.pathname);
  function T(en, fr) { return FR ? fr : en; }

  var BASE = FR ? "../" : "";
  var DISMISS = "cq_install_hidden";

  var standalone = (window.matchMedia && matchMedia("(display-mode: standalone)").matches) ||
                   navigator.standalone === true;

  /* ------------------------------------------------------------ register */
  // Browsers only allow a service worker on https or on localhost. Testing the
  // offline behaviour needs the localhost case too, and checking for https
  // alone is what made the first test run look like it was hanging: there was
  // never a worker to wait for.
  var secure = location.protocol === "https:" ||
               location.hostname === "localhost" ||
               location.hostname === "127.0.0.1" ||
               location.hostname === "[::1]";

  var reg = null;
  if ("serviceWorker" in navigator && secure) {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register(BASE + "sw.js", { scope: BASE || "/" })
        .then(function (r) {
          reg = r;
          r.addEventListener("updatefound", function () {
            var sw = r.installing;
            if (!sw) return;
            sw.addEventListener("statechange", function () {
              if (sw.state === "installed" && navigator.serviceWorker.controller) {
                offerRefresh(sw);
              }
            });
          });
        })
        .catch(function () { });
    });
  }

  // Reload ONLY when an existing worker was replaced, never on the very first
  // install. Without this test, the worker claiming the page for the first
  // time counted as a controller change and every brand-new visitor got a
  // surprise reload one second after the page appeared — which also broke the
  // test run, because the navigation it was in the middle of was cancelled.
  var hadController = ("serviceWorker" in navigator) && !!navigator.serviceWorker.controller;
  var reloading = false;
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.addEventListener("controllerchange", function () {
      if (!hadController || reloading) return;
      reloading = true;
      location.reload();
    });
  }

  /* ------------------------------------------------------------- styles */
  var css = ""
    + ".pwa-btn{display:inline-block;margin:10px auto 0;background:#fff;color:#22203a;"
    + "border:2px solid #fff;border-radius:999px;padding:9px 18px;font-weight:800;"
    + "font-size:14px;font-family:inherit;cursor:pointer;line-height:1.2}"
    + ".pwa-btn:hover{background:#ffe9ec}"
    + ".pwa-wrap{margin-top:10px}"
    + ".pwa-tip{position:fixed;left:12px;right:12px;bottom:12px;z-index:10050;max-width:460px;"
    + "margin:0 auto;background:var(--card,#fff);color:var(--ink,#22203a);border-radius:14px;"
    + "padding:14px 16px;box-shadow:0 8px 30px rgba(0,0,0,.3);font-size:14.5px;line-height:1.55;"
    + "text-align:left}"
    + ".pwa-tip b{display:block;margin-bottom:4px;font-size:15.5px}"
    + ".pwa-tip .row{display:flex;gap:8px;margin-top:10px}"
    + ".pwa-tip .row .btn{flex:1 1 auto;font-size:14px;padding:9px 14px}";
  var st = document.createElement("style");
  st.textContent = css;
  document.head.appendChild(st);

  /* ---------------------------------------------------------- update bar */
  function offerRefresh(sw) {
    if (document.querySelector(".pwa-tip.upd")) return;
    var box = document.createElement("div");
    box.className = "pwa-tip upd";
    box.setAttribute("data-no-i18n", "");
    var b = document.createElement("b");
    b.textContent = T("A new version is ready", "Une nouvelle version est prête");
    var p = document.createElement("div");
    p.textContent = T("Refresh to get the newest questions and games.",
                      "Actualisez pour obtenir les nouvelles questions et les nouveaux jeux.");
    var row = document.createElement("div"); row.className = "row";
    var go = document.createElement("button");
    go.type = "button"; go.className = "btn"; go.textContent = T("Refresh", "Actualiser");
    go.addEventListener("click", function () {
      if (sw) sw.postMessage("skip-waiting");
      setTimeout(function () { location.reload(); }, 300);
    });
    var no = document.createElement("button");
    no.type = "button"; no.className = "btn btn-ghost";
    no.textContent = T("Later", "Plus tard");
    no.addEventListener("click", function () { box.remove(); });
    row.appendChild(go); row.appendChild(no);
    box.appendChild(b); box.appendChild(p); box.appendChild(row);
    document.body.appendChild(box);
  }

  /* --------------------------------------------------------- install UI */
  var deferred = null;

  function iosSteps() {
    if (document.querySelector(".pwa-tip.ios")) return;
    var box = document.createElement("div");
    box.className = "pwa-tip ios";
    box.setAttribute("data-no-i18n", "");
    var b = document.createElement("b");
    b.textContent = T("Add Canada Quiz to your home screen",
                      "Ajouter Canada Quiz à votre écran d’accueil");
    var p = document.createElement("div");
    p.textContent = T("1. Tap the Share button at the top of Safari — the square with the arrow. "
                    + "2. Scroll down and tap Add to Home Screen. "
                    + "3. Tap Add. The games then open like an app, with no address bar, and most of them still work with no signal.",
                      "1. Touchez le bouton Partager en haut de Safari — le carré avec la flèche. "
                    + "2. Faites défiler et touchez Sur l’écran d’accueil. "
                    + "3. Touchez Ajouter. Les jeux s’ouvrent ensuite comme une application, sans barre d’adresse, et la plupart fonctionnent sans réseau.");
    var row = document.createElement("div"); row.className = "row";
    var ok = document.createElement("button");
    ok.type = "button"; ok.className = "btn"; ok.textContent = T("Got it", "Compris");
    ok.addEventListener("click", function () { box.remove(); });
    row.appendChild(ok);
    box.appendChild(b); box.appendChild(p); box.appendChild(row);
    document.body.appendChild(box);
  }

  function mountButton() {
    if (standalone) return;                      /* already installed */
    try { if (localStorage.getItem(DISMISS) === "1") return; } catch (e) { }

    var foot = document.querySelector(".site-footer .container");
    if (!foot) return;
    if (foot.querySelector(".pwa-wrap")) return;

    var apple = (navigator.vendor || "").indexOf("Apple") === 0 ||
                /iPad|iPhone|iPod/.test(navigator.userAgent);
    var touch = (navigator.maxTouchPoints || 0) > 0;
    /* Only offer it where installing is a real thing: a phone or tablet, or a
       browser that has already told us it can install. */
    if (!deferred && !(apple && touch)) return;

    var wrap = document.createElement("div");
    wrap.className = "pwa-wrap";
    wrap.setAttribute("data-no-i18n", "");
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "pwa-btn";
    btn.textContent = T("📲 Install the app on this device",
                        "📲 Installer l’application sur cet appareil");
    btn.addEventListener("click", function () {
      if (deferred) {
        deferred.prompt();
        deferred.userChoice.then(function (c) {
          if (c && c.outcome === "accepted") {
            try { localStorage.setItem(DISMISS, "1"); } catch (e) { }
            wrap.remove();
          }
        });
        deferred = null;
      } else {
        iosSteps();
      }
    });
    wrap.appendChild(btn);

    var links = foot.querySelector(".footer-links");
    if (links && links.parentNode) links.parentNode.insertBefore(wrap, links.nextSibling);
    else foot.appendChild(wrap);
  }

  window.addEventListener("beforeinstallprompt", function (e) {
    e.preventDefault();
    deferred = e;
    mountButton();
  });

  window.addEventListener("appinstalled", function () {
    try { localStorage.setItem(DISMISS, "1"); } catch (e) { }
    var w = document.querySelector(".pwa-wrap");
    if (w) w.remove();
  });

  // js/site.js redraws the whole footer on DOMContentLoaded. This file is a
  // deferred script, so it runs just BEFORE that event — the first version put
  // the button in and site.js immediately replaced the footer underneath it,
  // and the button silently vanished on every page. mountButton() checks for
  // itself before adding anything, so simply trying again after site.js has
  // had its turn is both safe and enough.
  function mountLater() {
    mountButton();
    setTimeout(mountButton, 0);
    setTimeout(mountButton, 400);
    setTimeout(mountButton, 1500);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mountLater);
  } else {
    mountLater();
  }
  window.addEventListener("load", mountButton);
})();
