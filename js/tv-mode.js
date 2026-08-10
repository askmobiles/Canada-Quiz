/* "Play on TV" — one button on every game and quiz page.

   What a web page is actually allowed to do, and what it is not:

     * It CANNOT start AirPlay screen mirroring. Apple only lets Control Centre
       do that; a website has no way to ask. Anyone promising a one-tap AirPlay
       button on the web is mirroring a <video>, which is not a game.
     * It CAN cast itself straight to a Chromecast, through the Presentation
       API, in Chrome and Edge (Android and desktop). That is a real one-tap
       connect, so when the browser offers it we show a real Connect button and
       a list of the screens it found.
     * Everywhere else the honest answer is three short steps, and those steps
       are different on an iPad, an Android phone, a Mac and a Windows laptop.
       So the button opens a small card with the steps for THAT device only.

   The same button also turns on TV mode: much bigger text and bigger answer
   buttons, for people reading from a couch instead of holding the tablet.
   TV mode is remembered, so the next game opens the same way.

   Front end only. Nothing is sent anywhere. */
(function () {
  "use strict";

  var FR = /\/fr\//.test(location.pathname);
  function T(en, fr) { return FR ? fr : en; }

  var KEY = "cq_tv_mode";
  var castReq = null, castAvailable = false, castConn = null;

  /* ------------------------------------------------------------------ css */
  var css = ""
    + ".tv-btn{position:fixed;z-index:10000;background:#1e4f8a;color:#fff;border:none;"
    + "right:calc(12px + env(safe-area-inset-right,0px));"
    + "bottom:calc(64px + env(safe-area-inset-bottom,0px));"
    + "border-radius:999px;padding:13px 20px;font-weight:800;font-size:15px;font-family:inherit;"
    + "cursor:pointer;box-shadow:0 3px 12px rgba(0,0,0,.3);display:none;"
    + "-webkit-tap-highlight-color:transparent}"
    + ".tv-btn:active{transform:scale(.96)}"
    + ".tv-btn.on{background:#1f7a6f}"
    + "@media (hover:none) and (pointer:coarse){.tv-btn{display:block}}"
    + "@media (max-width:900px){.tv-btn{display:block}}"
    + "html.fs-touch .tv-btn{display:block}"
    /* on a desktop the button only appears when casting is genuinely possible */
    + "html.tv-can-cast .tv-btn{display:block}"
    /* in play mode it shrinks into a small round toggle at the top left, so it
       can still be reached from the far side of the room */
    + "body.play-mode .tv-btn{display:block;padding:0;width:48px;height:48px;font-size:20px;"
    + "right:auto;left:calc(10px + env(safe-area-inset-left,0px));"
    + "bottom:auto;top:calc(10px + env(safe-area-inset-top,0px));z-index:10001}"

    /* ------------------------------------------------------------- sheet */
    + ".tv-sheet{position:fixed;inset:0;z-index:10002;display:flex;align-items:flex-end;"
    + "justify-content:center;background:rgba(12,16,32,.5);padding:0}"
    + "@media (min-width:640px){.tv-sheet{align-items:center;padding:20px}}"
    + ".tv-card{background:var(--card,#fff);color:var(--ink,#22203a);width:100%;max-width:520px;"
    + "max-height:88vh;overflow:auto;border-radius:18px 18px 0 0;padding:20px 20px 24px;"
    + "box-sizing:border-box;box-shadow:0 -8px 40px rgba(0,0,0,.35);text-align:left;"
    + "animation:tvUp .2s ease-out}"
    + "@media (min-width:640px){.tv-card{border-radius:18px}}"
    + "@keyframes tvUp{from{transform:translateY(24px);opacity:0}to{transform:none;opacity:1}}"
    + ".tv-card h3{margin:0 0 4px;font-size:20px}"
    + ".tv-card p{margin:0 0 12px;font-size:14.5px;line-height:1.55;color:var(--muted,#5d5876)}"
    + ".tv-card ol{margin:0 0 14px;padding-left:22px;font-size:15px;line-height:1.7}"
    + ".tv-card li{margin:0 0 4px}"
    + ".tv-card .tv-x{float:right;border:0;background:transparent;font-size:20px;cursor:pointer;"
    + "color:var(--muted,#5d5876);width:32px;height:32px;border-radius:50%;padding:0}"
    + ".tv-sec{border-top:1px solid var(--line,#e6e2d8);margin-top:14px;padding-top:14px}"
    + ".tv-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}"
    + ".tv-row .btn{flex:1 1 auto}"
    + ".tv-devs{display:flex;flex-direction:column;gap:6px;margin:8px 0 0}"
    + ".tv-note{font-size:13px;color:var(--muted,#5d5876);margin-top:10px;line-height:1.5}"

    /* ----------------------------------------------------------- TV mode */
    /* Deliberately NO font-size rules here. The first version set sizes like
       "h2 { 1.45em }", which is 1.45x the PARENT, not 1.45x whatever that
       heading already was — so on Charades, where the word to act out is a
       54px h2, "bigger TV text" shrank it to 30px. Scaling is done instead by
       raising the zoom cap inside game-fullscreen.js, which scales every page
       proportionally and can never make anything smaller.
       All that is left here is contrast: greys wash out on a lit TV. */
    + "body.tv-mode.play-mode .pm-host .muted{color:#4a4560}"
    + "body.tv-mode.play-mode .pm-host{--muted:#4a4560}";

  var st = document.createElement("style");
  st.textContent = css;
  document.head.appendChild(st);

  /* --------------------------------------------------------- which device */
  function platform() {
    var ua = navigator.userAgent || "";
    var mac = /Macintosh/.test(ua);
    var touch = (navigator.maxTouchPoints || 0) > 1;
    if (/iPhone|iPod/.test(ua)) return "ios";
    if (/iPad/.test(ua) || (mac && touch)) return "ipad";   /* iPadOS reports Macintosh */
    if (/Android/.test(ua)) return "android";
    if (mac) return "mac";
    if (/Windows/.test(ua)) return "windows";
    if (/Tizen|Web0S|SMART-TV|BRAVIA|CrKey/i.test(ua)) return "tv";
    return "other";
  }

  var STEPS = {
    ios: [
      ["Make sure the phone and the TV are on the same Wi-Fi.", "Assurez-vous que le téléphone et la télé sont sur le même Wi-Fi."],
      ["Swipe down from the top-right corner of the screen.", "Balayez vers le bas depuis le coin supérieur droit de l’écran."],
      ["Tap Screen Mirroring, then choose your TV.", "Touchez Recopie de l’écran, puis choisissez votre télé."],
      ["Come back here and press Full screen.", "Revenez ici et appuyez sur Plein écran."]
    ],
    ipad: [
      ["Make sure the iPad and the TV are on the same Wi-Fi.", "Assurez-vous que l’iPad et la télé sont sur le même Wi-Fi."],
      ["Swipe down from the top-right corner of the screen.", "Balayez vers le bas depuis le coin supérieur droit de l’écran."],
      ["Tap Screen Mirroring, then choose your TV or Apple TV.", "Touchez Recopie de l’écran, puis choisissez votre télé ou votre Apple TV."],
      ["Turn the iPad sideways, come back here and press Full screen.", "Tournez l’iPad de côté, revenez ici et appuyez sur Plein écran."]
    ],
    android: [
      ["Make sure the phone and the TV are on the same Wi-Fi.", "Assurez-vous que le téléphone et la télé sont sur le même Wi-Fi."],
      ["Open the Chrome menu (⋮) and tap Cast, or use Smart View in the quick settings.", "Ouvrez le menu de Chrome (⋮) et touchez Caster, ou utilisez Smart View dans les réglages rapides."],
      ["Choose your TV or Chromecast.", "Choisissez votre télé ou votre Chromecast."],
      ["Come back here and press Full screen.", "Revenez ici et appuyez sur Plein écran."]
    ],
    mac: [
      ["Make sure the Mac and the TV are on the same Wi-Fi.", "Assurez-vous que le Mac et la télé sont sur le même Wi-Fi."],
      ["Click Control Centre in the menu bar, then Screen Mirroring.", "Cliquez sur le Centre de contrôle dans la barre de menus, puis sur Recopie d’écran."],
      ["Choose your TV or Apple TV. An HDMI cable works just as well.", "Choisissez votre télé ou votre Apple TV. Un câble HDMI fonctionne aussi bien."],
      ["Come back here and press Full screen.", "Revenez ici et appuyez sur Plein écran."]
    ],
    windows: [
      ["For a wireless TV, press the Windows key and K, then pick your TV.", "Pour une télé sans fil, appuyez sur la touche Windows et K, puis choisissez votre télé."],
      ["Or open the Chrome menu (⋮) and click Cast, then Sources → Cast tab.", "Ou ouvrez le menu de Chrome (⋮), cliquez sur Caster, puis Sources → Caster l’onglet."],
      ["Or simply run an HDMI cable from the laptop to the TV.", "Ou branchez simplement un câble HDMI entre le portable et la télé."],
      ["Come back here and press Full screen.", "Revenez ici et appuyez sur Plein écran."]
    ],
    tv: [
      ["You are already on the TV — nothing to connect.", "Vous êtes déjà sur la télé — rien à connecter."],
      ["Press Full screen and turn on big TV text below.", "Appuyez sur Plein écran et activez le grand texte télé ci-dessous."]
    ],
    other: [
      ["Put the device and the TV on the same Wi-Fi.", "Mettez l’appareil et la télé sur le même Wi-Fi."],
      ["Use your device's screen mirroring or cast feature and pick the TV.", "Utilisez la recopie d’écran ou la diffusion de votre appareil et choisissez la télé."],
      ["An HDMI cable from a laptop to the TV always works.", "Un câble HDMI entre un portable et la télé fonctionne toujours."],
      ["Come back here and press Full screen.", "Revenez ici et appuyez sur Plein écran."]
    ]
  };

  var HEADING = {
    ios: ["Send this to your TV from an iPhone", "Envoyer ceci à votre télé depuis un iPhone"],
    ipad: ["Send this to your TV from an iPad", "Envoyer ceci à votre télé depuis un iPad"],
    android: ["Send this to your TV from Android", "Envoyer ceci à votre télé depuis Android"],
    mac: ["Send this to your TV from a Mac", "Envoyer ceci à votre télé depuis un Mac"],
    windows: ["Send this to your TV from Windows", "Envoyer ceci à votre télé depuis Windows"],
    tv: ["Playing on the TV", "Jouer sur la télé"],
    other: ["Send this to your TV", "Envoyer ceci à votre télé"]
  };

  /* --------------------------------------------------------------- casting */
  /* Chrome and Edge can hand this exact page to a Chromecast. Safari cannot,
     and there is no way to make it — that is a browser limit, not ours. */
  function setupCast() {
    try {
      if (!("PresentationRequest" in window)) return;
      if (location.protocol !== "https:" && location.hostname !== "localhost" &&
          location.hostname !== "127.0.0.1") return;
      castReq = new PresentationRequest([location.href]);
      castReq.getAvailability().then(function (a) {
        castAvailable = !!a.value;
        if (castAvailable) document.documentElement.classList.add("tv-can-cast");
        a.onchange = function () {
          castAvailable = !!a.value;
          document.documentElement.classList.toggle("tv-can-cast", castAvailable);
        };
      }, function () { });
    } catch (e) { }
  }

  function startCast(statusEl) {
    if (!castReq) return;
    statusEl.textContent = T("Looking for screens…", "Recherche d’écrans…");
    castReq.start().then(function (conn) {
      castConn = conn;
      statusEl.textContent = T("Connected to " + (conn.name || "your screen") + ".",
                               "Connecté à " + (conn.name || "votre écran") + ".");
      conn.onclose = function () {
        statusEl.textContent = T("Disconnected.", "Déconnecté.");
      };
    }, function (err) {
      statusEl.textContent = (err && err.name === "NotAllowedError")
        ? T("No screen chosen.", "Aucun écran choisi.")
        : T("No screen found. Use the steps above instead.",
            "Aucun écran trouvé. Utilisez plutôt les étapes ci-dessus.");
    });
  }

  /* -------------------------------------------------------------- TV mode */
  function tvOn() { return document.body.classList.contains("tv-mode"); }

  function setTv(on) {
    document.body.classList.toggle("tv-mode", !!on);
    try { localStorage.setItem(KEY, on ? "1" : "0"); } catch (e) { }
    tvBtn.classList.toggle("on", !!on);
    tvBtn.setAttribute("aria-pressed", on ? "true" : "false");
    if (on && !document.body.classList.contains("play-mode")) {
      var fs = document.querySelector(".fs-btn");
      if (fs) fs.click();                 /* big text only makes sense full screen */
    }
    setTimeout(function () { window.dispatchEvent(new Event("resize")); }, 80);
  }

  /* ---------------------------------------------------------------- sheet */
  function openSheet() {
    var plat = platform();
    var wrap = document.createElement("div");
    wrap.className = "tv-sheet";
    wrap.setAttribute("data-no-i18n", "");

    var card = document.createElement("div");
    card.className = "tv-card";

    var x = document.createElement("button");
    x.type = "button"; x.className = "tv-x"; x.textContent = "✕";
    x.setAttribute("aria-label", T("Close", "Fermer"));
    card.appendChild(x);

    var h = document.createElement("h3");
    h.textContent = "📺 " + HEADING[plat][FR ? 1 : 0];
    card.appendChild(h);

    var lead = document.createElement("p");
    lead.textContent = T("The whole screen goes to the TV, and you keep tapping on this device.",
                         "Tout l’écran va à la télé, et vous continuez à toucher sur cet appareil.");
    card.appendChild(lead);

    var ol = document.createElement("ol");
    STEPS[plat].forEach(function (s) {
      var li = document.createElement("li");
      li.textContent = s[FR ? 1 : 0];
      ol.appendChild(li);
    });
    card.appendChild(ol);

    /* the real one-tap connect, only where the browser can actually do it */
    if (castAvailable && castReq) {
      var sec = document.createElement("div");
      sec.className = "tv-sec";
      var st2 = document.createElement("p");
      st2.style.margin = "0 0 8px";
      st2.textContent = T("A screen was found on your Wi-Fi. You can connect in one tap:",
                          "Un écran a été trouvé sur votre Wi-Fi. Vous pouvez vous connecter d’une seule touche :");
      var cb = document.createElement("button");
      cb.type = "button"; cb.className = "btn btn-lg"; cb.style.width = "100%";
      cb.textContent = T("📡 Connect to a screen", "📡 Se connecter à un écran");
      var status = document.createElement("p");
      status.className = "tv-note"; status.textContent = "";
      cb.addEventListener("click", function () { startCast(status); });
      sec.appendChild(st2); sec.appendChild(cb); sec.appendChild(status);
      card.appendChild(sec);
    }

    var sec2 = document.createElement("div");
    sec2.className = "tv-sec";
    var p2 = document.createElement("p");
    p2.style.margin = "0";
    p2.textContent = T("Big TV text makes the questions and buttons much larger, for reading from across the room.",
                       "Le grand texte télé agrandit beaucoup les questions et les boutons, pour lire de loin.");
    var row = document.createElement("div");
    row.className = "tv-row";
    var toggle = document.createElement("button");
    toggle.type = "button";
    toggle.className = "btn " + (tvOn() ? "btn-ghost" : "btn-lg");
    toggle.textContent = tvOn()
      ? T("Turn big TV text off", "Désactiver le grand texte télé")
      : T("Turn big TV text on", "Activer le grand texte télé");
    toggle.addEventListener("click", function () {
      setTv(!tvOn());
      close();
    });
    row.appendChild(toggle);
    sec2.appendChild(p2); sec2.appendChild(row);
    card.appendChild(sec2);

    var note = document.createElement("p");
    note.className = "tv-note";
    note.textContent = T("Tip: Top Answers, Trivia Showdown and Charades are the best ones on a TV. "
                       + "Skip Hide & Find — everybody would watch where the objects go.",
                         "Astuce : Top Answers, Duel de quiz et les charades sont les meilleurs à la télé. "
                       + "Évitez Cache-cache : tout le monde verrait où vont les objets.");
    card.appendChild(note);

    wrap.appendChild(card);
    document.body.appendChild(wrap);

    function close() { if (wrap.parentNode) wrap.parentNode.removeChild(wrap); }
    x.addEventListener("click", close);
    wrap.addEventListener("click", function (e) { if (e.target === wrap) close(); });
    document.addEventListener("keydown", function esc(e) {
      if (e.key === "Escape") { close(); document.removeEventListener("keydown", esc); }
    });
  }

  /* --------------------------------------------------------------- button */
  var tvBtn = document.createElement("button");
  tvBtn.className = "tv-btn";
  tvBtn.type = "button";
  tvBtn.setAttribute("data-no-i18n", "");
  tvBtn.setAttribute("aria-label", T("Play on TV", "Jouer à la télé"));
  tvBtn.addEventListener("click", openSheet);

  function paintBtn() {
    tvBtn.textContent = document.body.classList.contains("play-mode")
      ? "📺"
      : T("📺 Play on TV", "📺 Jouer à la télé");
  }

  function mount() {
    document.body.appendChild(tvBtn);
    paintBtn();
    try {
      if (localStorage.getItem(KEY) === "1") {
        document.body.classList.add("tv-mode");
        tvBtn.classList.add("on");
      }
    } catch (e) { }
    /* the label changes shape when play mode comes and goes */
    if (window.MutationObserver) {
      new MutationObserver(paintBtn).observe(document.body,
        { attributes: true, attributeFilter: ["class"] });
    }
  }

  setupCast();
  if (document.body) mount();
  else document.addEventListener("DOMContentLoaded", mount);
})();
