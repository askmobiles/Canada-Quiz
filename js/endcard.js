/* endcard.js — one shared "game over" card that appears in the MIDDLE of the
   play area instead of under it.

   Any game can call:

     CQEnd.show(hostSelectorOrElement, {
       icon:  '🏔️',
       title: 'Game over',
       sub:   'Your Inukshuk is 12 stones tall!',
       tone:  'lose' | 'win' | 'draw' | 'time',      // colours the title
       actions: [ { label:'Play again', fn: reset, cls:'btn-lg' },
                  { label:'All games', href:'games.html', cls:'btn-ghost' } ]
     });

     CQEnd.hide();              // remove it
     CQEnd.hide(host);          // remove only the one over that host

   The card is inserted INSIDE the host element so it stays put in full-screen
   play mode, and so a canvas or board underneath still shows through.
   A small ✕ dismisses the card without starting a new game, in case the player
   wants to look at the final board.                                          */
(function () {
  "use strict";

  var FR = /\/fr\//.test(location.pathname);
  function T(en, fr) { return FR ? fr : en; }

  var CSS = ""
    + ".cq-end{position:absolute;inset:0;z-index:40;display:flex;align-items:center;"
    + "justify-content:center;padding:14px;box-sizing:border-box;"
    + "background:rgba(12,16,32,.42);backdrop-filter:blur(2px);"
    + "-webkit-backdrop-filter:blur(2px);border-radius:inherit;"
    + "animation:cqEndFade .18s ease-out}"
    + "@keyframes cqEndFade{from{opacity:0}to{opacity:1}}"
    + "@keyframes cqEndPop{from{opacity:0;transform:translateY(10px) scale(.94)}"
    + "to{opacity:1;transform:none}}"
    + ".cq-end-card{position:relative;max-width:290px;width:100%;text-align:center;"
    + "background:var(--card,#fff);border-radius:16px;padding:20px 18px 18px;"
    + "box-shadow:0 18px 44px rgba(0,0,0,.34);animation:cqEndPop .22s ease-out}"
    + ".cq-end-icon{font-size:42px;line-height:1;margin-bottom:4px}"
    + ".cq-end-title{margin:0 0 4px;font-size:21px;font-weight:800;line-height:1.25;"
    + "color:var(--ink,#22203a)}"
    + ".cq-end-win .cq-end-title{color:#1c7c54}"
    + ".cq-end-lose .cq-end-title{color:#c8102e}"
    + ".cq-end-time .cq-end-title{color:#d97706}"
    + ".cq-end-sub{margin:0 0 14px;font-size:14.5px;line-height:1.5;"
    + "color:var(--muted,#5d5876)}"
    + ".cq-end-btns{display:flex;flex-direction:column;gap:8px}"
    + ".cq-end-btns .btn{width:100%;box-sizing:border-box;margin:0}"
    + ".cq-end-x{position:absolute;top:6px;right:8px;width:30px;height:30px;padding:0;"
    + "border:0;background:transparent;font-size:19px;line-height:30px;cursor:pointer;"
    + "color:var(--muted,#5d5876);border-radius:50%}"
    + ".cq-end-x:hover{background:rgba(0,0,0,.07)}"
    + ".cq-end-peek{position:absolute;left:0;right:0;bottom:8px;text-align:center;"
    + "font-size:12px;color:#fff;opacity:.85;pointer-events:none}"
    + "@media(max-height:430px){.cq-end-card{padding:12px 14px 12px;max-width:330px}"
    + ".cq-end-icon{font-size:28px}.cq-end-title{font-size:17px}"
    + ".cq-end-sub{font-size:13px;margin-bottom:9px}"
    + ".cq-end-btns{flex-direction:row;flex-wrap:wrap;justify-content:center}"
    + ".cq-end-btns .btn{width:auto}}";

  var styled = false;
  function ensureCss() {
    if (styled) return;
    styled = true;
    var s = document.createElement("style");
    s.setAttribute("data-cq-end", "1");
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  function resolve(host) {
    if (!host) return null;
    if (typeof host === "string") return document.querySelector(host);
    return host;
  }

  function hide(host) {
    var scope = resolve(host) || document;
    var old = scope.querySelectorAll ? scope.querySelectorAll(".cq-end") : [];
    for (var i = 0; i < old.length; i++) {
      if (old[i].parentNode) old[i].parentNode.removeChild(old[i]);
    }
    if (!host) {
      var all = document.querySelectorAll(".cq-end");
      for (var j = 0; j < all.length; j++) {
        if (all[j].parentNode) all[j].parentNode.removeChild(all[j]);
      }
    }
  }

  function show(host, opts) {
    var el = resolve(host);
    if (!el) return null;
    opts = opts || {};
    ensureCss();
    hide(el);

    if (getComputedStyle(el).position === "static") el.style.position = "relative";

    var wrap = document.createElement("div");
    wrap.className = "cq-end" + (opts.tone ? " cq-end-" + opts.tone : "");
    wrap.setAttribute("data-no-i18n", "");
    wrap.setAttribute("role", "dialog");
    wrap.setAttribute("aria-live", "polite");

    var card = document.createElement("div");
    card.className = "cq-end-card";

    if (opts.icon) {
      var ic = document.createElement("div");
      ic.className = "cq-end-icon";
      ic.setAttribute("aria-hidden", "true");
      ic.textContent = opts.icon;
      card.appendChild(ic);
    }
    if (opts.title) {
      var h = document.createElement("p");
      h.className = "cq-end-title";
      h.textContent = opts.title;
      card.appendChild(h);
    }
    if (opts.sub) {
      var p = document.createElement("p");
      p.className = "cq-end-sub";
      p.textContent = opts.sub;
      card.appendChild(p);
    }

    var btns = document.createElement("div");
    btns.className = "cq-end-btns";
    var acts = opts.actions || [];
    for (var i = 0; i < acts.length; i++) {
      (function (a) {
        var b = document.createElement(a.href ? "a" : "button");
        b.className = "btn " + (a.cls || (btns.children.length ? "btn-ghost" : "btn-lg"));
        b.textContent = a.label;
        if (a.href) {
          b.href = a.href;
        } else {
          b.type = "button";
          b.addEventListener("click", function (e) {
            e.preventDefault();
            hide(el);
            if (typeof a.fn === "function") a.fn();
          });
        }
        btns.appendChild(b);
      })(acts[i]);
    }
    card.appendChild(btns);

    var x = document.createElement("button");
    x.type = "button";
    x.className = "cq-end-x";
    x.setAttribute("aria-label", T("Close and look at the board", "Fermer et regarder le plateau"));
    x.textContent = "✕";
    x.addEventListener("click", function () { hide(el); });
    card.appendChild(x);

    wrap.appendChild(card);

    var peek = document.createElement("div");
    peek.className = "cq-end-peek";
    peek.textContent = T("Tap outside to see the board", "Touchez à côté pour voir le plateau");
    wrap.appendChild(peek);

    wrap.addEventListener("click", function (e) {
      if (e.target === wrap || e.target === peek) hide(el);
    });

    // Some play areas listen for swipes and drags on themselves (the cube
    // scene, the snake canvas). Without this the game would swallow a tap
    // meant for the card, so nothing happens when you press Play again.
    ["pointerdown", "pointerup", "mousedown", "mouseup", "touchstart",
      "touchend", "click"].forEach(function (type) {
        wrap.addEventListener(type, function (e) { e.stopPropagation(); },
          { passive: true });
      });

    el.appendChild(wrap);
    if (btns.firstChild && btns.firstChild.focus) {
      try { btns.firstChild.focus({ preventScroll: true }); } catch (err) { }
    }
    return wrap;
  }

  window.CQEnd = { show: show, hide: hide, T: T };
})();
