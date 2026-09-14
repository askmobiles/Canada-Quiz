/* The River of Time — the crossing that turns Which Came First into a game.
 * ------------------------------------------------------------------------
 * WHY A RIVER AND NOT A LONGER STREAK
 *
 * The pair game was endless. Endless is fine for practice and hopeless as a
 * game: there is no moment where you have finished, so there is no moment worth
 * coming back for. The drawn driving game showed what works — ten situations, a
 * percentage that climbs where you can see it, and a card at the end telling you
 * how you did. People play that one twice.
 *
 * So history gets the same shape. Twelve stepping stones from one bank to the
 * other. Every pair you get right moves you one stone. Every pair you get wrong
 * costs one of three lifebuoys, and you stay where you are rather than sliding
 * back, because sliding back makes a hard question feel like a punishment and
 * people stop. Run out of buoys and you are in the water; reach the far bank and
 * you have crossed.
 *
 * The questions get harder as you go — that is the gap rule in
 * js/which-came-first.js, not here — so the last stones are the ones that
 * actually teach.
 *
 * This file only draws and keeps score. It knows nothing about events, years or
 * the diary. That keeps the picture and the history apart, which is why the
 * picture can be redrawn without anyone having to re-check 339 dates.
 */
(function () {
  "use strict";

  var STONES = 12;
  var BUOYS = 3;

  /* The scene is drawn at a fixed size and scaled by CSS, so one set of
     coordinates works on a phone and on a projector. */
  var VW = 960, VH = 230;
  var X0 = 150, X1 = 812;          // first and last stone
  var MIDY = 132;                  // the waterline the stones sit on

  function stoneAt(i) {
    var t = i / (STONES - 1);
    return {
      x: X0 + (X1 - X0) * t,
      /* a gentle S so the crossing reads as a path rather than a ruler */
      y: MIDY + Math.sin(t * Math.PI * 1.6) * 16
    };
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  /* A walker: head, body, two legs mid-stride. Small on purpose — the stones
     and the water are the picture, the figure is just where you are. */
  function walker(x, y, wet) {
    var g = '<g transform="translate(' + x.toFixed(1) + ',' + (y - 6).toFixed(1) + ') scale(1.3)">';
    if (wet) {
      /* In the water, drawn clear of the stone rather than tucked under it. The
         first version put the head behind the stone and all you could see was a
         red smudge — it did not read as falling in until it was drawn and
         looked at. Ring, head above the surface, both arms up. */
      g += '<ellipse cx="0" cy="6" rx="26" ry="8" fill="none" stroke="#e8f3f9" stroke-width="3"/>';
      g += '<ellipse cx="0" cy="6" rx="15" ry="5" fill="#7ab4d2"/>';
      g += '<line x1="-4" y1="-2" x2="-14" y2="-16" stroke="#e63946" stroke-width="4.5" stroke-linecap="round"/>';
      g += '<line x1="4" y1="-2" x2="14" y2="-16" stroke="#e63946" stroke-width="4.5" stroke-linecap="round"/>';
      g += '<circle cx="0" cy="-8" r="8" fill="#f2c6a0" stroke="#2b2d42" stroke-width="2"/>';
      return g + "</g>";
    }
    g += '<line x1="-5" y1="0" x2="0" y2="-12" stroke="#2b2d42" stroke-width="3.5" stroke-linecap="round"/>';
    g += '<line x1="5" y1="0" x2="0" y2="-12" stroke="#2b2d42" stroke-width="3.5" stroke-linecap="round"/>';
    g += '<line x1="0" y1="-12" x2="0" y2="-26" stroke="#e63946" stroke-width="7" stroke-linecap="round"/>';
    g += '<line x1="-8" y1="-20" x2="8" y2="-24" stroke="#2b2d42" stroke-width="3.5" stroke-linecap="round"/>';
    g += '<circle cx="0" cy="-33" r="7" fill="#f2c6a0" stroke="#2b2d42" stroke-width="2"/>';
    return g + "</g>";
  }

  function scene(at, buoys, done, won) {
    var s = [];
    s.push('<rect x="0" y="0" width="960" height="230" fill="#eaf4fa"/>');

    /* Both banks, and the trees that say which way is forward. */
    s.push('<path d="M0,86 Q60,80 104,96 L118,230 L0,230 Z" fill="#a8d5ae"/>');
    s.push('<path d="M960,86 Q900,80 856,96 L842,230 L960,230 Z" fill="#a8d5ae"/>');

    /* Water between the banks, with three drifting lines so it reads as moving
       water and not a blue floor. */
    s.push('<path d="M104,96 Q480,74 856,96 L842,230 L118,230 Z" fill="#8fc3de"/>');
    [128, 168, 206].forEach(function (y, i) {
      s.push('<path d="M' + (150 + i * 40) + ',' + y + ' q28,-7 56,0 t56,0 t56,0 t56,0 t56,0" ' +
             'stroke="#a9d4e8" stroke-width="3" fill="none" stroke-linecap="round" opacity=".9"/>');
    });

    /* A maple on the near bank, a flag on the far one: start here, finish there. */
    s.push('<rect x="44" y="58" width="8" height="34" rx="3" fill="#8a6a4a"/>');
    s.push('<circle cx="48" cy="38" r="20" fill="#e07a3f"/>');
    s.push('<circle cx="32" cy="46" r="13" fill="#d9662f"/>');
    s.push('<circle cx="64" cy="46" r="13" fill="#d9662f"/>');
    s.push('<rect x="906" y="30" width="5" height="62" fill="#6b7280"/>');
    s.push('<path d="M911,34 h40 v26 h-40 Z" fill="#e63946"/>');
    s.push('<path d="M925,38 l4,7 h-2 l4,6 h-3 l2,5 h-10 l2,-5 h-3 l4,-6 h-2 Z" fill="#fdfbf7"/>');

    /* The stones. Behind you they carry a tick, ahead of you they are plain,
       and the one you are on is ringed so a glance finds you. */
    for (var i = 0; i < STONES; i++) {
      var p = stoneAt(i);
      /* Once you are on the far bank every stone is behind you. Without this
         the last one still wore the you-are-here ring after the crossing was
         won, which read as unfinished. Found by looking at the picture. */
      var passed = won || i < at, here = !won && i === at;
      s.push('<ellipse cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" rx="26" ry="11" ' +
             'fill="' + (passed ? "#b9b2a6" : "#cfc8bb") + '" stroke="' + (here ? "#2b2d42" : "#a79f92") +
             '" stroke-width="' + (here ? 3 : 1.5) + '"/>');
      if (passed) {
        s.push('<path d="M' + (p.x - 7).toFixed(1) + ',' + p.y.toFixed(1) +
               ' l5,5 l9,-10" stroke="#2a9d8f" stroke-width="3.5" fill="none" ' +
               'stroke-linecap="round" stroke-linejoin="round"/>');
      }
    }

    /* Where the walker stands. Before the first answer they are on the bank. */
    var w;
    if (done && !won) {
      /* Just downstream of the stone they missed, so it is obvious which one. */
      w = stoneAt(Math.max(0, at));
      s.push(walker(w.x + 34, w.y + 44, true));
    } else if (won) {
      s.push(walker(884, 150, false));
    } else {
      w = stoneAt(at);
      s.push(walker(w.x, w.y - 4, false));
    }

    /* Lifebuoys, drawn as rings on the near bank: three left, two left, one. */
    for (var b = 0; b < BUOYS; b++) {
      var lost = b >= buoys;
      s.push('<circle cx="' + (26 + b * 30) + '" cy="200" r="11" fill="none" stroke="' +
             (lost ? "#cfc8bb" : "#e63946") + '" stroke-width="5"/>');
    }

    return '<svg class="wf-river-svg" viewBox="0 0 ' + VW + " " + VH + '" role="img" ' +
           'aria-label="' + esc(scene.label || "") + '" preserveAspectRatio="xMidYMid meet">' +
           s.join("") + "</svg>";
  }

  window.CQRiver = {
    stones: STONES,
    buoys: BUOYS,
    /* draw(box, at, buoysLeft, done, won, label) */
    draw: function (box, at, buoys, done, won, label) {
      if (!box) return;
      scene.label = label || "";
      box.innerHTML = scene(Math.min(at, STONES - 1), buoys, done, won);
    }
  };
}());
