/* Shared full-screen "play mode" for every game page.
   - Shows a floating "Full screen" button on ANY touch device (phone AND tablet/iPad,
     in portrait or landscape) — not just narrow screens.
   - Tapping it hides the site header/footer/hero/ads and fills the screen with the game.
   - Requests native fullscreen where the browser supports it (Android, iPad Safari).
   - LOCKS the play screen while you play:
       * no pinch-zoom, no double-tap zoom
       * no pull-to-refresh, no rubber-band bounce
       * no accidental text selection or long-press menus
       * screen orientation frozen where the browser allows it
       * screen kept awake (Wake Lock) so tablets don't dim mid-game
   - Desktop with a mouse is left untouched.
   - Works in English and French (URL decides). */
(function () {
  var FR = /\/fr\//.test(location.pathname);
  function T(en, fr) { return FR ? fr : en; }

  var css = ''
    // --- floating buttons -------------------------------------------------
    + '.fs-btn{position:fixed;z-index:10000;background:#1f7a6f;color:#fff;border:none;'
    + 'right:calc(12px + env(safe-area-inset-right,0px));bottom:calc(12px + env(safe-area-inset-bottom,0px));'
    + 'border-radius:999px;padding:13px 20px;font-weight:800;font-size:15px;font-family:inherit;cursor:pointer;'
    + 'box-shadow:0 3px 12px rgba(0,0,0,.3);display:none;-webkit-tap-highlight-color:transparent}'
    + '.fs-btn:active{transform:scale(.96)}'
    + '.fs-exit{position:fixed;z-index:10001;background:#c1121f;color:#fff;border:none;'
    + 'right:calc(10px + env(safe-area-inset-right,0px));top:calc(10px + env(safe-area-inset-top,0px));'
    + 'border-radius:999px;width:48px;height:48px;font-size:22px;font-weight:900;cursor:pointer;'
    + 'box-shadow:0 3px 12px rgba(0,0,0,.3);display:none;-webkit-tap-highlight-color:transparent}'
    + '.fs-exit:active{transform:scale(.94)}'
    // show the button on touch devices of ANY width (iPad landscape is 1180px wide)
    + '@media (hover:none) and (pointer:coarse){.fs-btn{display:block}}'
    + '@media (max-width:900px){.fs-btn{display:block}}'
    + 'html.fs-touch .fs-btn{display:block}'
    // --- play mode --------------------------------------------------------
    // Everything that is NOT the game gets hidden. .pagedoc is the written
    // summary block under each page; it was added after this file was written,
    // so in play mode it kept rendering behind the game and showed through —
    // "About this game" text sitting under the spinning wheel. Any page-level
    // block added in future should be added to this list too.
    + 'body.play-mode .site-header,body.play-mode .site-footer,body.play-mode .hero,'
    + 'body.play-mode .howto,body.play-mode .ad-slot,body.play-mode .ad-label,'
    + 'body.play-mode .pagedoc,body.play-mode .cq-fig,body.play-mode .cq-sources'
    + '{display:none!important}'
    + 'body.play-mode{overflow:hidden;overscroll-behavior:none;position:fixed;inset:0;width:100%;'
    + 'background:var(--bg,#fdfaf3);'
    + '-webkit-text-size-adjust:100%;-webkit-user-select:none;user-select:none;'
    + '-webkit-touch-callout:none;touch-action:manipulation}'
    // an opaque backdrop, so nothing at all can show through from behind
    + 'body.play-mode .pm-host{background:var(--bg,#fdfaf3)!important}'
    + 'body.play-mode .pm-host{position:fixed!important;inset:0!important;margin:0!important;'
    + 'border-radius:0!important;max-width:none!important;width:100%!important;height:100%!important;'
    + 'overflow:auto!important;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;z-index:9998;'
    + 'padding:calc(60px + env(safe-area-inset-top,0px)) calc(10px + env(safe-area-inset-right,0px)) '
    + 'calc(16px + env(safe-area-inset-bottom,0px)) calc(10px + env(safe-area-inset-left,0px));'
    + 'box-sizing:border-box}'
    // Sit the game in the middle of the screen instead of pinned to the top.
    // Children still stretch to full width, so nothing moves sideways.
    // "safe" keeps the top reachable if a game is taller than the screen;
    // browsers that do not know it simply ignore the line and start at the top.
    + 'body.play-mode .pm-host{display:flex;flex-direction:column;justify-content:safe center}'
    + 'body.play-mode .pm-host>*{flex:0 0 auto}'
    // the two pages that use the shared .game-wrap box get a bigger board
    + 'body.play-mode .pm-host .game-wrap{max-width:min(96vw,74vh)!important}'
    // inputs still need to be selectable/typable inside a game
    + 'body.play-mode input,body.play-mode textarea{-webkit-user-select:text;user-select:text}'
    // comfortable tap targets on touch while playing
    + '@media (hover:none) and (pointer:coarse){body.play-mode .pm-host button,'
    + 'body.play-mode .pm-host .btn{min-height:46px}}'
    + 'body.play-mode .pm-veiled{display:none!important}'
    + 'body.play-mode .fs-btn{display:none!important}'
    + 'body.play-mode .fs-exit{display:block}';

  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  // mark real touch devices so the button also appears on tablets in landscape
  try {
    if (('ontouchstart' in window) || (navigator.maxTouchPoints || 0) > 0) {
      document.documentElement.classList.add('fs-touch');
    }
  } catch (e) {}

  function host() {
    var marked = document.querySelector('[data-fs-host]');
    if (marked) return marked;

    // A quiz is not one panel — the question screen and the result screen are
    // separate siblings, and the result appears only at the end. If we pinned
    // play mode to the first .panel, the result screen would be stranded
    // behind it. So for quizzes we take the whole <main> and rely on the CSS
    // above to hide the article text around it.
    if (document.querySelector('.options, #dq-opts, #dq-po')) {
      var m = document.querySelector('main');
      if (m) return m;
    }
    return document.querySelector('.panel') || document.querySelector('main');
  }

  var enterBtn = document.createElement('button');
  enterBtn.className = 'fs-btn';
  enterBtn.type = 'button';
  enterBtn.textContent = T('⛶ Full screen', '⛶ Plein écran');
  enterBtn.setAttribute('aria-label', T('Play in full screen', 'Jouer en plein écran'));
  enterBtn.setAttribute('data-no-i18n', '');

  var exitBtn = document.createElement('button');
  exitBtn.className = 'fs-exit';
  exitBtn.type = 'button';
  exitBtn.setAttribute('aria-label', T('Exit full screen', 'Quitter le plein écran'));
  exitBtn.setAttribute('data-no-i18n', '');
  exitBtn.textContent = '✕';

  // ---------------------------------------------------------------- native
  // iPhone and iPad are deliberately left OUT of native fullscreen.
  //
  // Safari has an anti-phishing rule: the moment a page in NATIVE fullscreen
  // sees a key press, it throws up "It looks like you are typing while in full
  // screen — canada-quiz.com may be showing a fake keyboard to trick you into
  // disclosing personal or financial information." An iPad in a keyboard case
  // triggers that on any keystroke, and it landed on a family playing
  // Minesweeper. Nothing was wrong with the page, but a visitor reading that
  // sentence has no way to know it, and a quiz site cannot afford it.
  //
  // The CSS play mode below already hides the header, footer, article and ads
  // and pins the game to the screen, so on an iPad we simply keep Safari's own
  // slim toolbar and lose nothing that matters. Android and desktop have no
  // such warning and still get true fullscreen.
  var IOS = /iPad|iPhone|iPod/.test(navigator.userAgent) ||
            (/Macintosh/.test(navigator.userAgent) && (navigator.maxTouchPoints || 0) > 1);

  function nativeOn() {
    if (IOS) return null;
    var el = document.documentElement;
    try {
      if (el.requestFullscreen) return el.requestFullscreen({ navigationUI: 'hide' });
      if (el.webkitRequestFullscreen) return el.webkitRequestFullscreen();
    } catch (e) {}
    return null;
  }
  function nativeOff() {
    try {
      if (document.fullscreenElement || document.webkitFullscreenElement) {
        if (document.exitFullscreen) document.exitFullscreen();
        else if (document.webkitExitFullscreen) document.webkitExitFullscreen();
      }
    } catch (e) {}
  }

  // ----------------------------------------------------------- orientation
  // Freeze the screen the way the player is holding it, so a game does not
  // reflow mid-move. A page can ask for a specific one with
  // <body data-fs-orient="landscape">. Silently ignored where unsupported (iOS).
  function orientLock() {
    try {
      var so = screen.orientation;
      if (!so || !so.lock) return;
      var want = (document.body.getAttribute('data-fs-orient') || '').trim();
      var target = want || (so.type || '').replace(/-(primary|secondary)$/, '') || 'any';
      var p = so.lock(target);
      if (p && p.catch) p.catch(function () {});
    } catch (e) {}
  }
  function orientUnlock() {
    try { if (screen.orientation && screen.orientation.unlock) screen.orientation.unlock(); } catch (e) {}
  }

  // -------------------------------------------------------------- wake lock
  var wake = null;
  function wakeOn() {
    try {
      if (!navigator.wakeLock || !navigator.wakeLock.request) return;
      navigator.wakeLock.request('screen').then(function (w) { wake = w; }, function () {});
    } catch (e) {}
  }
  function wakeOff() {
    try { if (wake && wake.release) { wake.release(); wake = null; } } catch (e) {}
  }
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'visible' && document.body.classList.contains('play-mode') && !wake) wakeOn();
  });

  // ------------------------------------------------------------ gesture lock
  // Block pinch-zoom and double-tap-zoom, but leave one-finger scrolling
  // inside the game panel working normally.
  function blockMulti(e) {
    if (document.body.classList.contains('play-mode') && e.touches && e.touches.length > 1) {
      e.preventDefault();
    }
  }
  function blockGesture(e) {
    if (document.body.classList.contains('play-mode')) e.preventDefault();
  }
  var lastTap = 0;
  function blockDoubleTap(e) {
    if (!document.body.classList.contains('play-mode')) return;
    var now = Date.now();
    if (now - lastTap < 320) e.preventDefault();
    lastTap = now;
  }
  document.addEventListener('touchstart', blockMulti, { passive: false });
  document.addEventListener('touchmove', blockMulti, { passive: false });
  document.addEventListener('gesturestart', blockGesture, { passive: false });
  document.addEventListener('gesturechange', blockGesture, { passive: false });
  document.addEventListener('dblclick', blockGesture, { passive: false });
  document.addEventListener('touchend', blockDoubleTap, { passive: false });
  document.addEventListener('contextmenu', function (e) {
    if (document.body.classList.contains('play-mode')) {
      var n = e.target && e.target.tagName;
      if (n !== 'INPUT' && n !== 'TEXTAREA') e.preventDefault();
    }
  });

  // ------------------------------------------------------------- viewport
  var vp = document.querySelector('meta[name="viewport"]');
  var vpSaved = vp ? vp.getAttribute('content') : null;
  function vpLock() {
    if (!vp) return;
    vp.setAttribute('content',
      'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover');
  }
  function vpRestore() {
    if (vp && vpSaved !== null) vp.setAttribute('content', vpSaved);
  }

  // ------------------------------------------------------------- bigger board
  // On a tablet the screen is much taller than the game board, so the board
  // ends up small and stranded in the middle. If there is spare room we gently
  // scale the whole game up with CSS zoom, which the browser also applies to
  // taps and clicks — so nothing needs to know it happened.
  // Canvas games are left alone: they work out their own pointer positions.
  function fitZoom(h) {
    try {
      if (!h) return;
      h.style.zoom = '';
      if (document.querySelector('canvas')) return;
      if (!(window.CSS && CSS.supports && CSS.supports('zoom', '1.2'))) return;

      // TV mode (js/tv-mode.js) means somebody is watching this from a couch
      // rather than holding the tablet, so fill the height instead of stopping
      // politely at 1.6, and do it on a phone too — a mirrored phone is still
      // a big screen at the other end. Scaling with zoom, rather than with
      // font-size rules, is what stops "bigger" ever making something smaller.
      var tv = document.body.classList.contains('tv-mode');
      var CAP = tv ? 2.6 : 1.6;
      var FLOOR = tv ? 1.04 : 1.12;

      var availH = h.clientHeight;
      if (!availH) return;
      if (!tv && h.clientWidth < 700 && availH < 700) return;  // phones already fill up

      var kids = [], i;
      for (i = 0; i < h.children.length; i++) {
        var r = h.children[i].getBoundingClientRect();
        if (r.height) kids.push(r);
      }
      if (!kids.length) return;
      var top = kids[0].top, bottom = kids[0].bottom;
      for (i = 1; i < kids.length; i++) {
        if (kids[i].top < top) top = kids[i].top;
        if (kids[i].bottom > bottom) bottom = kids[i].bottom;
      }
      var contentH = bottom - top;
      if (contentH < 40) return;

      var z = Math.min(availH / (contentH + 30), CAP);
      // In TV mode always give at least a quarter more, even where the page
      // already fills the height. Someone across the room needs the text
      // bigger more than they need to avoid a scroll, and the width guard
      // below still eases back if that pushes the board off the side.
      if (tv && z < 1.25) z = 1.25;
      if (z < FLOOR) return;                    // not enough spare room to bother
      h.style.zoom = z;
      // if scaling up pushed the board off the side, ease back until it fits
      var guard = 0;
      while (h.scrollWidth > h.clientWidth + 2 && z > 1.02 && guard++ < 34) {
        z -= 0.05;
        h.style.zoom = z;
      }
      if (z <= 1.02) h.style.zoom = '';
    } catch (e) {
      if (h) h.style.zoom = '';
    }
  }

  // ---------------------------------------------------------- enter / exit
  /* Hide everything on the page that is not the game.
     Naming the blocks one by one in CSS was never going to hold: the driving
     pages have several sibling panels of explanation, and a page can grow a
     new section any time. So instead we walk the real page and hide every
     top-level block that does not contain the game. Nothing can show through
     behind the play screen, whatever a page is made of. */
  function veil(h) {
    if (!h) return;
    var main = document.querySelector('main') || document.body;
    var kids = main.children, i, el;
    for (i = 0; i < kids.length; i++) {
      el = kids[i];
      if (el === h || el.contains(h) || h.contains(el)) continue;
      el.classList.add('pm-veiled');
    }
  }
  function unveil() {
    var v = document.querySelectorAll('.pm-veiled'), i;
    for (i = 0; i < v.length; i++) v[i].classList.remove('pm-veiled');
  }

  function enter() {
    var h = host();
    if (h) h.classList.add('pm-host');
    veil(h);
    document.body.classList.add('play-mode');
    vpLock();
    var p = nativeOn();
    if (p && p.then) p.then(orientLock, orientLock); else setTimeout(orientLock, 80);
    wakeOn();
    window.scrollTo(0, 0);
    setTimeout(function () { window.dispatchEvent(new Event('resize')); fitZoom(h); }, 60);
  }
  function exit() {
    document.body.classList.remove('play-mode');
    unveil();
    var h = document.querySelector('.pm-host');
    if (h) { h.style.zoom = ''; h.classList.remove('pm-host'); }
    orientUnlock();
    wakeOff();
    nativeOff();
    vpRestore();
    setTimeout(function () { window.dispatchEvent(new Event('resize')); }, 60);
  }

  enterBtn.addEventListener('click', enter);
  exitBtn.addEventListener('click', exit);

  // turning the tablet sideways changes how much room there is
  var refit = null;
  window.addEventListener('resize', function () {
    if (!document.body.classList.contains('play-mode')) return;
    clearTimeout(refit);
    refit = setTimeout(function () { fitZoom(document.querySelector('.pm-host')); }, 180);
  });

  // if the player leaves native fullscreen with a system gesture, keep the
  // CSS play mode but let the orientation go free again
  function onFsChange() {
    if (!(document.fullscreenElement || document.webkitFullscreenElement)) orientUnlock();
  }
  document.addEventListener('fullscreenchange', onFsChange);
  document.addEventListener('webkitfullscreenchange', onFsChange);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && document.body.classList.contains('play-mode')) exit();
  });

  function mount() {
    document.body.appendChild(enterBtn);
    document.body.appendChild(exitBtn);
  }
  if (document.body) mount();
  else document.addEventListener('DOMContentLoaded', mount);
})();
