/* canada-quiz.com — "What Would You Do?" the driving scene game.
 *
 * WHY A SECOND ENGINE AND NOT THE QUIZ ONE
 * ----------------------------------------
 * js/driving-engine.js asks questions in words and shows a sign beside them.
 * That is the written test, and it belongs on the practice pages. This is a
 * different thing: the picture IS the question. You look down on a corner from
 * above — your car, the other cars, the light, the bus, the person stepping off
 * the curb — you choose what to do, and it tells you straight away whether you
 * were right and why.
 *
 * Search Console said the same thing three months running: every page anyone
 * clicked was something you have to DO. Nobody clicked a page that states a
 * fact, because Google states the fact itself. A drawn corner is not something
 * an answer box can finish for you.
 *
 * EVERYTHING IS DRAWN HERE, IN CODE
 * ---------------------------------
 * There are no photographs and no downloaded diagrams. Every scene is built from
 * rectangles, circles and paths by draw() below, out of the tiny description in
 * each scenario's "sc" field — so a new situation costs four or five lines of
 * data, not a new image. Road signs come from js/driving/signs.js, the same 80
 * original drawings the rest of the site uses.
 *
 * The bird's-eye view is not strictly orthographic: the traffic light and the
 * people are drawn as you would recognise them, not as you would see them from a
 * helicopter. A learner needs to know instantly what they are looking at, and a
 * top-down traffic light is a grey rectangle.
 *
 * WHAT IT COUNTS
 * --------------
 * Right answers, the running percentage, and the current streak, shown together
 * at the top and updated on every tap, because "7 / 10 · 70%" is the number
 * somebody studying for a test actually wants. After ten scenes there is a
 * result card with the percentage in large type. The best percentage is kept in
 * this browser only, in localStorage, and never sent anywhere.
 */
(function () {
  "use strict";

  var mount = document.getElementById("dg-scene");
  if (!mount || typeof CQ_SCENES === "undefined") return;

  var FR = /(^|\/)fr\//.test(location.pathname);
  var SRC = window.CQ_SCENE_SRC || {};
  var SIGNS = window.CQ_SIGNS || {};
  var ROUND = 10;
  var KEY = "cq-dg-best";

  var W = FR ? {
    you: "VOUS",
    right: "bonnes",
    pct: "de réussite",
    streak: "d'affilée",
    correct: "Bonne réponse",
    wrong: "Pas tout à fait",
    answer: "La bonne réponse :",
    next: "Situation suivante →",
    seeResult: "Voir mon résultat →",
    source: "Source :",
    done: "Vous avez terminé les 10 situations",
    scored: "Vous avez eu %1 sur %2",
    passed: "C'est au-dessus de la barre des 80 % du G1.",
    failed: "Le vrai G1 demande 80 %. Encore un peu de pratique.",
    bestEver: "Votre meilleur résultat : %1 %",
    another: "Essayer 10 autres",
    challenge: "Défier un ami",
    copied: "Copié. Collez-le à un ami.",
    shareMsg: "J'ai eu %1 % au jeu de situations de conduite de Canada Quiz. Pouvez-vous faire mieux ?",
    missed: "Les situations manquées",
    ofTen: "Situation %1 sur %2"
  } : {
    you: "YOU",
    right: "right",
    pct: "correct",
    streak: "in a row",
    correct: "Correct",
    wrong: "Not quite",
    answer: "The right answer:",
    next: "Next situation →",
    seeResult: "See my result →",
    source: "Source:",
    done: "You finished all 10 situations",
    scored: "You got %1 out of %2",
    passed: "That is above the 80% the G1 asks for.",
    failed: "The real G1 needs 80%. A little more practice.",
    bestEver: "Your best so far: %1%",
    another: "Try another 10",
    challenge: "Challenge a friend",
    copied: "Copied. Paste it to a friend.",
    shareMsg: "I got %1% on the Canada Quiz driving situations game. Can you beat it?",
    missed: "The situations you missed",
    ofTen: "Situation %1 of %2"
  };

  function T(k) {
    var s = W[k];
    for (var i = 1; i < arguments.length; i++) {
      s = s.replace("%" + i, arguments[i]);
    }
    return s;
  }

  function el(id) { return document.getElementById(id); }
  function txt(e, s) { e.textContent = s; return e; }

  /* =====================================================================
     THE DRAWING
     =====================================================================
     One 420 x 320 picture. Everything below is measured against these, so
     changing a lane width is one number and not twenty.
  */
  var V = { w: 420, h: 320 };
  var C = {                       // the crossroads
    hTop: 120, hBot: 210,         // the road that crosses
    vL: 165, vR: 255,             // the road you are on
    mine: 232, onc: 188,          // your lane centre, the oncoming lane centre
    west: 143, east: 188,         // the lane coming from your right, from your left
    stopLine: 216
  };
  var R = { l: 150, r: 270, mine: 240, other: 180 };   // a plain two-way road

  var COL = {
    ground: "#e8ebee", grass: "#cfe0cb", road: "#787f88",
    line: "#f2c744", dash: "#ffffff", kerb: "#cdd3da",
    you: "#2b6cb0", other: "#b8453b", other2: "#3f4a5a", bus: "#f2c113",
    dark: "#22262c"
  };

  function rect(x, y, w, h, fill, extra) {
    return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h +
      '" fill="' + fill + '"' + (extra || "") + "/>";
  }

  /* A car seen from above, pointing up, centred on 0,0. */
  function carShape(fill) {
    return '<rect x="-14" y="-25" width="28" height="50" rx="7" fill="' + fill + '"/>' +
      '<path d="M-10,-15 L10,-15 L7.5,-4 L-7.5,-4 Z" fill="#d6e8f7" opacity=".95"/>' +
      '<rect x="-9" y="9" width="18" height="8" rx="3" fill="#000" opacity=".2"/>' +
      '<circle cx="-9" cy="-22" r="2.6" fill="#fff6cf"/>' +
      '<circle cx="9" cy="-22" r="2.6" fill="#fff6cf"/>';
  }
  var DIR = { n: 0, e: 90, s: 180, w: 270 };
  function car(x, y, dir, fill, spin) {
    return '<g transform="translate(' + x + ',' + y + ') rotate(' +
      (DIR[dir] + (spin || 0)) + ')">' + carShape(fill || COL.other) + "</g>";
  }

  /* Your car, with a ring and a label, because in a picture full of cars the
     learner must never have to work out which one is theirs. */
  function mineCar(x, y, spin) {
    return '<g transform="translate(' + x + ',' + y + ')">' +
      '<ellipse cx="0" cy="0" rx="23" ry="33" fill="#2b6cb0" opacity=".16"/>' +
      '<g transform="rotate(' + (spin || 0) + ')">' + carShape(COL.you) + "</g>" +
      '<text x="0" y="44" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"' +
      ' font-size="13" font-weight="bold" fill="#1a3a5c" stroke="#ffffff"' +
      ' stroke-width="3.5" paint-order="stroke">' + W.you + "</text></g>";
  }

  /* A school bus, with the upper red lamps lit and the stop arm out. */
  function schoolBus(x, y, dir) {
    var b = '<rect x="-19" y="-39" width="38" height="78" rx="6" fill="' + COL.bus +
      '" stroke="#8a6c00" stroke-width="1.5"/>' +
      '<rect x="-14" y="-32" width="28" height="13" rx="3" fill="#cfe3f5"/>' +
      '<rect x="-14" y="-6" width="9" height="16" rx="2" fill="#cfe3f5"/>' +
      '<rect x="5" y="-6" width="9" height="16" rx="2" fill="#cfe3f5"/>' +
      '<rect x="-14" y="18" width="28" height="12" rx="3" fill="#cfe3f5"/>' +
      // the four upper red lamps, lit
      '<circle cx="-14" cy="-36" r="6" fill="#e63946" opacity=".3"/>' +
      '<circle cx="14" cy="-36" r="6" fill="#e63946" opacity=".3"/>' +
      '<circle cx="-14" cy="36" r="6" fill="#e63946" opacity=".3"/>' +
      '<circle cx="14" cy="36" r="6" fill="#e63946" opacity=".3"/>' +
      '<circle cx="-14" cy="-36" r="3.2" fill="#e63946"/>' +
      '<circle cx="14" cy="-36" r="3.2" fill="#e63946"/>' +
      '<circle cx="-14" cy="36" r="3.2" fill="#e63946"/>' +
      '<circle cx="14" cy="36" r="3.2" fill="#e63946"/>' +
      // the stop arm, swung out on the bus's left
      '<g transform="translate(-34,0)">' +
      '<rect x="8" y="-2" width="10" height="4" fill="#9a9a9a"/>' +
      '<polygon points="-4,-6 4,-11 12,-6 12,6 4,11 -4,6" fill="#d02128" stroke="#ffffff" stroke-width="1.6"/>' +
      "</g>";
    return '<g transform="translate(' + x + ',' + y + ') rotate(' + DIR[dir] + ')">' + b + "</g>";
  }

  /* Flashing roof lamps — one drawing, two colour pairs. */
  function lamps() {
    return '<circle cx="-7" cy="-4" r="7" fill="#e63946" opacity=".3"/>' +
      '<circle cx="7" cy="-4" r="7" fill="#2b6cb0" opacity=".3"/>' +
      '<circle cx="-7" cy="-4" r="3.4" fill="#e63946"/>' +
      '<circle cx="7" cy="-4" r="3.4" fill="#2b6cb0"/>';
  }
  function fireTruck(x, y, dir) {
    return '<g transform="translate(' + x + ',' + y + ') rotate(' + DIR[dir] + ')">' +
      '<rect x="-17" y="-29" width="34" height="58" rx="5" fill="#c8252c"/>' +
      '<rect x="-13" y="-24" width="26" height="11" rx="3" fill="#cfe3f5"/>' +
      '<rect x="-17" y="2" width="34" height="6" fill="#ffffff"/>' +
      lamps() + "</g>";
  }
  function policeCar(x, y, dir) {
    return '<g transform="translate(' + x + ',' + y + ') rotate(' + DIR[dir] + ')">' +
      '<rect x="-14" y="-25" width="28" height="50" rx="7" fill="#f4f6f8" stroke="#9aa3ad" stroke-width="1.5"/>' +
      '<path d="M-10,-15 L10,-15 L7.5,-4 L-7.5,-4 Z" fill="#d6e8f7"/>' +
      '<rect x="-14" y="6" width="28" height="11" fill="#22262c"/>' +
      lamps() + "</g>";
  }

  /* A person, drawn the way a person is recognised rather than from directly
     overhead. Legibility beats geometry in a 40-pixel figure. */
  function person(x, y, flip) {
    return '<g transform="translate(' + x + ',' + y + ')' +
      (flip ? " scale(-1,1)" : "") + '">' +
      '<circle cx="0" cy="-17" r="6" fill="#2f3640"/>' +
      '<path d="M0,-11 L0,3" stroke="#2f3640" stroke-width="7" stroke-linecap="round"/>' +
      '<path d="M0,-8 L-8,-1 M0,-8 L8,-2" stroke="#2f3640" stroke-width="4.5" stroke-linecap="round"/>' +
      '<path d="M0,2 L-6,16 M0,2 L7,15" stroke="#2f3640" stroke-width="5.5" stroke-linecap="round"/>' +
      "</g>";
  }
  function cyclist(x, y, k) {
    return '<g transform="translate(' + x + ',' + y + ') scale(' + (k || 1) + ')">' +
      '<circle cx="0" cy="-14" r="10" fill="none" stroke="#2f3640" stroke-width="2.6"/>' +
      '<circle cx="0" cy="14" r="10" fill="none" stroke="#2f3640" stroke-width="2.6"/>' +
      '<path d="M0,-14 L0,14" stroke="#2f3640" stroke-width="2.6"/>' +
      '<circle cx="0" cy="-2" r="5.5" fill="#2a9d8f"/>' +
      '<circle cx="0" cy="-12" r="4.5" fill="#2f3640"/>' +
      "</g>";
  }

  /* The signal head. Drawn upright, as the driver sees it, hanging over the far
     side of the intersection. */
  function signal(x, y, state) {
    function lamp(cy, on, col) {
      return '<circle cx="0" cy="' + cy + '" r="7.5" fill="' + (on ? col : "#3a4049") +
        '"' + (on ? ' stroke="#ffffff" stroke-width="1.2"' : "") + "/>" +
        (on ? '<circle cx="0" cy="' + cy + '" r="12" fill="' + col + '" opacity=".22"/>' : "");
    }
    var red = state === "red" || state === "flashRed";
    var amb = state === "amber" || state === "flashAmber";
    var grn = state === "green" || state === "arrow";
    var head = '<rect x="-13" y="-29" width="26" height="58" rx="5" fill="' + COL.dark + '"/>' +
      lamp(-18, red, "#e63946") + lamp(0, amb, "#f4a52a") + lamp(18, grn, "#2a9d8f");
    var arrow = state === "arrow"
      ? '<g transform="translate(-30,0)"><rect x="-12" y="-13" width="24" height="26" rx="5" fill="' + COL.dark + '"/>' +
      '<circle cx="0" cy="0" r="11" fill="#2a9d8f" opacity=".22"/>' +
      '<path d="M5,-7 L-3,0 L5,7 Z" fill="#2a9d8f"/><rect x="3" y="-2.2" width="7" height="4.4" fill="#2a9d8f"/></g>'
      : "";
    var flash = (state === "flashRed" || state === "flashAmber")
      ? '<text x="0" y="44" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"' +
      ' font-size="11" font-weight="bold" fill="#5f6b7a" stroke="#ffffff" stroke-width="3"' +
      ' paint-order="stroke">' + (FR ? "clignotant" : "flashing") + "</text>"
      : "";
    return '<g transform="translate(' + x + ',' + y + ')">' + head + arrow + flash + "</g>";
  }

  /* A sign from js/driving/signs.js, placed on a post. The drawings are whole
     <svg> elements with their own viewBox, so a nested svg with x/y/width/height
     scales one without touching the artwork. */
  function sign(key, x, y, size) {
    var s = SIGNS[key];
    if (!s) return "";
    var n = size || 44;
    /* WHY THE WRAPPER IS THROWN AWAY
       The first version nested the sign's own <svg> inside the scene and gave it
       x/y/width/height. Every sign came out the full width of the picture: a
       STOP sign three hundred pixels across, covering the car it was meant to
       stand beside. Each drawing is 100 x 100 in its own coordinates, so taking
       the contents out and scaling them by n/100 in a <g> is exact, and cannot
       be reinterpreted by the parser. */
    var inner = s.replace(/^[\s\S]*?<svg[^>]*>/, "").replace(/<\/svg>\s*$/, "");
    return '<rect x="' + (x - 2.5) + '" y="' + (y - 2) + '" width="5" height="18" fill="#8a9099"/>' +
      '<g transform="translate(' + (x - n / 2) + ',' + (y - n) + ') scale(' + (n / 100) + ')">' +
      inner + '</g>';
  }

  function crosswalk(x, y, w, h, vertical) {
    var o = "", i;
    if (vertical) {
      for (i = 0; i < h; i += 11) o += rect(x, y + i, w, 6, "#ffffff", ' opacity=".85"');
    } else {
      for (i = 0; i < w; i += 11) o += rect(x + i, y, 6, h, "#ffffff", ' opacity=".85"');
    }
    return o;
  }

  function dashes(x, y, len, vertical, col) {
    var o = "", i;
    for (i = 0; i < len; i += 26) {
      o += vertical ? rect(x - 2, y + i, 4, 14, col || COL.dash)
                    : rect(x + i, y - 2, 14, 4, col || COL.dash);
    }
    return o;
  }

  /* The path you intend to take, so "turning left" is visible and not just
     stated in the question. */
  function intent(kind) {
    var d, head;
    if (kind === "left") {
      d = "M232,250 L232,178 Q232,143 190,143 L128,143";
      head = '<polygon points="112,143 130,135 130,151" fill="#2b6cb0"/>';
    } else if (kind === "right") {
      d = "M232,250 L232,196 Q232,188 258,188 L330,188";
      head = '<polygon points="346,188 328,180 328,196" fill="#2b6cb0"/>';
    } else {
      d = "M232,250 L232,80";
      head = '<polygon points="232,62 224,80 240,80" fill="#2b6cb0"/>';
    }
    return '<path d="' + d + '" fill="none" stroke="#2b6cb0" stroke-width="4"' +
      ' stroke-dasharray="10 8" stroke-linecap="round" opacity=".75"/>' + head;
  }

  /* ---- the four backdrops ---- */
  function crossRoads() {
    return rect(0, 0, V.w, V.h, COL.ground) +
      rect(0, C.hTop, V.w, C.hBot - C.hTop, COL.road) +
      rect(C.vL, 0, C.vR - C.vL, V.h, COL.road) +
      // centre lines, stopping short of the intersection
      dashes(C.vL - 1 + 45, 0, C.hTop - 10, true, COL.line) +
      dashes(C.vL - 1 + 45, C.hBot + 10, V.h - C.hBot - 10, true, COL.line) +
      dashes(0, (C.hTop + C.hBot) / 2, C.vL - 10, false, COL.line) +
      dashes(C.vR + 10, (C.hTop + C.hBot) / 2, V.w - C.vR - 10, false, COL.line) +
      rect(C.vL, C.stopLine, C.vR - C.vL - 45, 5, "#ffffff", ' opacity=".9"');
  }
  function straightRoad(twoLane) {
    var l = twoLane ? 130 : R.l, r = twoLane ? 300 : R.r;
    var o = rect(0, 0, V.w, V.h, COL.grass) + rect(l, 0, r - l, V.h, COL.road);
    o += twoLane
      ? dashes(215, 0, V.h, true, COL.dash) + rect(r, 0, 34, V.h, "#b9a98e")
      : dashes(210, 0, V.h, true, COL.line);
    return o;
  }
  function dividedRoad() {
    return rect(0, 0, V.w, V.h, COL.grass) +
      rect(95, 0, 80, V.h, COL.road) + rect(245, 0, 80, V.h, COL.road) +
      rect(175, 0, 70, V.h, COL.grass) +
      rect(203, 0, 14, V.h, "#c3cfbe") +
      dashes(135, 0, V.h, true, COL.dash) + dashes(285, 0, V.h, true, COL.dash);
  }
  function roundabout() {
    var cx = 210, cy = 158;
    return rect(0, 0, V.w, V.h, COL.grass) +
      rect(cx - 40, 0, 80, V.h, COL.road) + rect(0, cy - 40, V.w, 80, COL.road) +
      '<circle cx="' + cx + '" cy="' + cy + '" r="104" fill="' + COL.road + '"/>' +
      '<circle cx="' + cx + '" cy="' + cy + '" r="46" fill="' + COL.grass +
      '" stroke="#ffffff" stroke-width="3"/>' +
      '<circle cx="' + cx + '" cy="' + cy + '" r="104" fill="none" stroke="#ffffff"' +
      ' stroke-width="3" opacity=".55"/>' +
      // the counter-clockwise arrows that a roundabout sign shows
      '<path d="M' + cx + ',' + (cy - 74) + ' A74,74 0 0 0 ' + (cx - 74) + ',' + cy +
      '" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="9 8" opacity=".8"/>' +
      '<polygon points="' + (cx - 74) + ',' + (cy + 14) + ' ' + (cx - 82) + ',' + (cy - 6) +
      ' ' + (cx - 66) + ',' + (cy - 6) + '" fill="#ffffff" opacity=".9"/>';
  }

  function draw(sc) {
    var o = "", mineY = (sc.you && sc.you.y) || 268, i;

    if (sc.kind === "cross") {
      o += crossRoads();
      o += crosswalk(C.vR + 4, C.hTop + 6, 16, C.hBot - C.hTop - 12, true);
      if (sc.light) {
        o += '<rect x="290" y="96" width="5" height="30" fill="#8a9099"/>';
        o += signal(292, 74, sc.light);
      }
      if (sc.signs) {
        o += sign(sc.signs[0], C.vR + 24, C.stopLine + 30);
        o += sign(sc.signs[0], C.vL - 24, C.hTop - 16);
      }
      if (sc.path) o += intent(sc.path);
      if (sc.cars) {
        for (i = 0; i < sc.cars.length; i++) {
          var a = sc.cars[i].at;
          if (a === "right") o += car(348, C.west, "w", COL.other);
          else if (a === "left") o += car(72, C.east, "e", COL.other2);
          else if (a === "onc") o += car(C.onc, 62, "s", COL.other);
          else if (a === "block") o += car(186, C.west, "w", COL.other2);
          else if (a === "block2") o += car(248, C.west, "w", COL.other);
          else if (a === "block3") o += car(310, C.west, "w", COL.other2);
        }
      }
      if (sc.bike === "onc") o += cyclist(C.onc, 88);
      if (sc.ped === "right") o += person(C.vR + 12, C.east - 4);
      if (sc.behind) o += car(C.mine, mineY + 74, "n", COL.other2);
      if (sc.emerg === "behind") o += fireTruck(C.mine, 292, "n");
      o += mineCar(C.mine, mineY);

    } else if (sc.kind === "road") {
      o += straightRoad(sc.twoLane);
      if (sc.fog) {
        o += '<defs><linearGradient id="dgfog" x1="0" y1="0" x2="0" y2="1">' +
          '<stop offset="0" stop-color="#eef2f5" stop-opacity=".95"/>' +
          '<stop offset=".62" stop-color="#eef2f5" stop-opacity=".62"/>' +
          '<stop offset="1" stop-color="#eef2f5" stop-opacity=".28"/></linearGradient></defs>';
        o += rect(0, 0, V.w, V.h, "url(#dgfog)");
      }
      if (sc.snow) {
        o += rect(0, 0, V.w, V.h, "#ffffff", ' opacity=".26"');
        for (i = 0; i < 26; i++) {
          o += '<circle cx="' + (17 * i % V.w) + '" cy="' + ((43 * i) % V.h) +
            '" r="' + (2 + (i % 3)) + '" fill="#ffffff" opacity=".85"/>';
        }
      }
      if (sc.ice) {
        o += '<ellipse cx="210" cy="150" rx="62" ry="30" fill="#171d22" opacity=".38"/>' +
          '<ellipse cx="210" cy="150" rx="62" ry="30" fill="none" stroke="#dbe9f2"' +
          ' stroke-width="1.6" opacity=".5"/>' +
          '<path d="M168,140 H236" stroke="#ffffff" stroke-width="4" opacity=".32"' +
          ' stroke-linecap="round"/>' +
          '<path d="M182,160 H248" stroke="#ffffff" stroke-width="3" opacity=".22"' +
          ' stroke-linecap="round"/>';
      }
      if (sc.tracks) {
        o += rect(0, 78, V.w, 26, "#8a7a63") +
          rect(0, 84, V.w, 4, "#b9bfc6") + rect(0, 96, V.w, 4, "#b9bfc6");
        for (i = 0; i < V.w; i += 20) o += rect(i, 78, 9, 26, "#6d5f4c", ' opacity=".55"');
      }
      if (sc.ped === "cross") {
        o += crosswalk(R.l + 4, 168, R.r - R.l - 8, 18);
        o += person(206, 176);
      }
      if (sc.sign) o += sign(sc.sign, R.r + 34, 158, 50);
      if (sc.bus === "ahead") o += schoolBus(R.mine, 118, "n");
      if (sc.bus === "onc") o += schoolBus(R.other, 112, "s");
      if (sc.bike === "ahead") o += cyclist(R.mine + 16, 152, 1.5);
      if (sc.police) o += policeCar(314, 146, "n");
      if (sc.cars) {
        for (i = 0; i < sc.cars.length; i++) {
          if (sc.cars[i].at === "ahead") {
            o += car(sc.twoLane ? 262 : R.mine, sc.fog ? 150 : 140, "n", COL.other);
          }
        }
      }
      o += mineCar(sc.twoLane ? 262 : R.mine, mineY, sc.skid ? 20 : 0);
      if (sc.skid) {
        o += '<path d="M250,316 Q244,282 232,258" fill="none" stroke="#4d545c"' +
          ' stroke-width="8" stroke-linecap="round" opacity=".5"/>' +
          '<path d="M264,318 Q258,288 246,266" fill="none" stroke="#4d545c"' +
          ' stroke-width="8" stroke-linecap="round" opacity=".35"/>';
      }

    } else if (sc.kind === "divided") {
      o += dividedRoad();
      if (sc.bus === "onc") o += schoolBus(135, 116, "s");
      o += mineCar(285, (sc.you && sc.you.y) || 250);

    } else if (sc.kind === "round") {
      o += roundabout();
      o += sign("warn-roundabout", 330, 268, 46);
      if (sc.cars) {
        for (i = 0; i < sc.cars.length; i++) {
          if (sc.cars[i].at === "in") o += car(210, 54, "e", COL.other);
        }
      }
      if (sc.inside) {
        o += '<path d="M244,220 Q290,196 296,158 Q300,112 262,92" fill="none"' +
          ' stroke="#2b6cb0" stroke-width="4" stroke-dasharray="10 8" opacity=".7"/>';
        o += mineCar(290, 186, 300);
      } else {
        o += mineCar(232, 288);
      }
    }

    return '<svg viewBox="0 0 ' + V.w + " " + V.h + '" role="img" ' +
      'preserveAspectRatio="xMidYMid meet" aria-label="' +
      (FR ? "Situation de conduite dessinée" : "A drawn driving situation") +
      '">' + o + "</svg>";
  }

  /* One drawing function, made available by name, so a scene can be shown
     outside the game — and so every scene can be rendered side by side and
     LOOKED AT before shipping. A picture is the one thing a gate cannot check:
     the railway-crossing sign on this site was wrong for weeks because nobody
     rendered it and looked. */
  window.CQDriveScene = { draw: draw, scenes: CQ_SCENES };

  /* =====================================================================
     THE GAME
     ===================================================================== */
  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1)), t = a[i];
      a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  var qs = [], cur = 0, score = 0, streak = 0, bestStreak = 0, answered = false;
  var missed = [], order = [], best = 0;

  try { best = parseInt(localStorage.getItem(KEY), 10) || 0; } catch (e) { best = 0; }

  function pct() { return cur === 0 ? 0 : Math.round(score / cur * 100); }

  function bar() {
    var b = el("dg-bar");
    b.innerHTML = "";
    function pill(big, small, tone) {
      var d = document.createElement("div");
      d.className = "dg-pill" + (tone ? " " + tone : "");
      d.setAttribute("data-no-i18n", "");
      var s1 = document.createElement("strong");
      s1.textContent = big;
      var s2 = document.createElement("span");
      s2.textContent = small;
      d.appendChild(s1); d.appendChild(s2);
      b.appendChild(d);
    }
    pill(score + " / " + qs.length, W.right, "");
    pill(pct() + "%", W.pct, pct() >= 80 ? "good" : (cur >= 3 && pct() < 60 ? "bad" : ""));
    if (streak > 1) pill(String(streak), W.streak, "good");
  }

  function show() {
    var s = qs[cur];
    answered = false;
    mount.innerHTML = draw(s.sc);
    txt(el("dg-count"), T("ofTen", cur + 1, qs.length));
    txt(el("dg-q"), s.q[FR ? "fr" : "en"]);
    el("dg-fb").innerHTML = "";
    el("dg-fb").className = "dg-fb";
    el("dg-next").innerHTML = "";

    var box = el("dg-opts");
    box.innerHTML = "";
    order = shuffle([0, 1, 2, 3]);
    order.forEach(function (idx) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "dg-opt";
      b.setAttribute("data-no-i18n", "");
      b.textContent = s.a[idx][FR ? "fr" : "en"];
      b.onclick = function () { answer(idx, b); };
      box.appendChild(b);
    });
    bar();
  }

  function answer(idx, btn) {
    if (answered) return;
    answered = true;
    var s = qs[cur], win = idx === s.c;
    cur++;

    var all = el("dg-opts").querySelectorAll(".dg-opt");
    for (var i = 0; i < all.length; i++) {
      all[i].disabled = true;
      if (order[i] === s.c) all[i].classList.add("right");
    }
    if (!win) {
      btn.classList.add("wrong");
      missed.push(s);
    } else {
      score++; streak++;
      if (streak > bestStreak) bestStreak = streak;
    }
    if (!win) streak = 0;

    var fb = el("dg-fb");
    fb.className = "dg-fb " + (win ? "ok" : "no");
    var h = document.createElement("p");
    h.className = "dg-verdict";
    h.setAttribute("data-no-i18n", "");
    h.textContent = (win ? "✓ " : "✗ ") + (win ? W.correct : W.wrong);
    fb.appendChild(h);
    var p = document.createElement("p");
    p.className = "dg-why";
    p.setAttribute("data-no-i18n", "");
    p.textContent = s.why[FR ? "fr" : "en"];
    fb.appendChild(p);
    var src = SRC[s.s];
    if (src) {
      var sp = document.createElement("p");
      sp.className = "dg-src";
      sp.setAttribute("data-no-i18n", "");
      sp.appendChild(document.createTextNode(W.source + " "));
      var a = document.createElement("a");
      a.href = src.u;
      a.rel = "nofollow noopener";
      a.target = "_blank";
      a.textContent = src[FR ? "fr" : "en"];
      sp.appendChild(a);
      fb.appendChild(sp);
    }
    bar();

    var nb = document.createElement("button");
    nb.type = "button";
    nb.className = "btn";
    nb.setAttribute("data-no-i18n", "");
    nb.textContent = cur >= qs.length ? W.seeResult : W.next;
    nb.onclick = function () { if (cur >= qs.length) end(); else show(); };
    el("dg-next").appendChild(nb);
    /* Focus the Next button so a keyboard or a screen reader lands on it — but
       NOT the scroll that normally comes with focus. On a phone that scroll
       jumped the page down to the button and pushed the picture off the top of
       the screen, which is the one thing on the page you want to still be able
       to see while you read why you were wrong. */
    try { nb.focus({ preventScroll: true }); } catch (e) { nb.focus(); }
  }

  function end() {
    var p = pct();
    if (p > best) {
      best = p;
      try { localStorage.setItem(KEY, String(best)); } catch (e) {}
    }
    mount.innerHTML = "";
    el("dg-opts").innerHTML = "";
    el("dg-next").innerHTML = "";
    txt(el("dg-count"), "");
    txt(el("dg-q"), "");

    var fb = el("dg-fb");
    fb.className = "dg-fb " + (p >= 80 ? "ok" : "no");
    fb.innerHTML = "";

    function add(tag, cls, s) {
      var e = document.createElement(tag);
      e.className = cls;
      e.setAttribute("data-no-i18n", "");
      e.textContent = s;
      fb.appendChild(e);
      return e;
    }
    add("p", "dg-big", p + "%");
    add("p", "dg-verdict", T("scored", score, qs.length));
    add("p", "dg-why", p >= 80 ? W.passed : W.failed);
    add("p", "dg-src", T("bestEver", best));

    var row = document.createElement("div");
    row.className = "center";
    row.style.marginTop = "12px";

    var again = document.createElement("button");
    again.type = "button";
    again.className = "btn";
    again.setAttribute("data-no-i18n", "");
    again.textContent = W.another;
    again.onclick = start;
    row.appendChild(again);

    var share = document.createElement("button");
    share.type = "button";
    share.className = "btn btn-ghost";
    share.setAttribute("data-no-i18n", "");
    share.textContent = W.challenge;
    share.onclick = function () {
      var msg = T("shareMsg", p) + " " + location.href;
      function done() { share.textContent = W.copied; }
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(msg).then(done, fallback);
        } else { fallback(); }
      } catch (e) { fallback(); }
      function fallback() {
        var t = document.createElement("textarea");
        t.value = msg;
        t.setAttribute("readonly", "");
        t.style.position = "fixed";
        t.style.left = "-9999px";
        document.body.appendChild(t);
        t.select();
        try { document.execCommand("copy"); done(); } catch (e2) {}
        document.body.removeChild(t);
      }
    };
    row.appendChild(share);
    fb.appendChild(row);

    /* The scenes you got wrong, drawn again with the right answer under them.
       Reading "you missed question 4" teaches nothing; seeing the corner again
       with the rule beside it does. */
    if (missed.length) {
      var h = document.createElement("h3");
      h.className = "dg-missed-h";
      h.setAttribute("data-no-i18n", "");
      h.textContent = W.missed;
      fb.appendChild(h);
      missed.forEach(function (s) {
        var w = document.createElement("div");
        w.className = "dg-missed";
        w.setAttribute("data-no-i18n", "");
        var pic = document.createElement("div");
        pic.className = "dg-missed-pic";
        pic.innerHTML = draw(s.sc);
        w.appendChild(pic);
        var side = document.createElement("div");
        var q = document.createElement("p");
        q.className = "dg-missed-q";
        q.textContent = s.q[FR ? "fr" : "en"];
        side.appendChild(q);
        var ans = document.createElement("p");
        ans.className = "dg-missed-a";
        ans.textContent = W.answer + " " + s.a[s.c][FR ? "fr" : "en"];
        side.appendChild(ans);
        var why = document.createElement("p");
        why.className = "dg-why";
        why.textContent = s.why[FR ? "fr" : "en"];
        side.appendChild(why);
        w.appendChild(side);
        fb.appendChild(w);
      });
    }
  }

  /* A fresh ten every time, drawn from all 26 — so "Try another 10" is a new
     round and not the same round shuffled, which is the quiet reason nobody
     plays a game twice. */
  var started = false;

  function start() {
    var again = started;
    started = true;
    qs = shuffle(CQ_SCENES).slice(0, Math.min(ROUND, CQ_SCENES.length));
    cur = 0; score = 0; streak = 0; bestStreak = 0; missed = [];
    show();
    /* Scroll to the top of the game only when the player asked for another ten.
       Doing it on the first load would scroll past the heading that tells a new
       visitor what this is. */
    var w = document.getElementById("dg-wrap");
    if (again && w && w.scrollIntoView) w.scrollIntoView({ block: "start" });
  }

  document.addEventListener("keydown", function (e) {
    if (!answered) return;
    if (e.key === "Enter" || e.key === " ") {
      var b = el("dg-next").querySelector("button");
      if (b) { e.preventDefault(); b.click(); }
    }
  });

  start();
}());
