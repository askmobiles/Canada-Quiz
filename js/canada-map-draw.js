/* Draws the shapes in js/canada-map-svg.js into an <svg> that is already on the
   page, and leaves everything else alone.

   The <svg> element itself stays in the HTML of each page, not in here, for one
   reason: its aria-label is the only word on a map, and a label written in the
   page is a text node the French build can translate. A label built by a script
   is a string the French build never sees — which is exactly how the word banks
   in the puzzle games ended up English on French pages. */
(function () {
  function esc(v) { return String(v).replace(/"/g, "&quot;"); }

  /* Rebuilds the inside of an <svg>: the United States behind, the thirteen
     provinces and territories in one group, the water in front, and an empty
     group for labels a page may want to add. Same shape on every map. */
  function inner(opts) {
    opts = opts || {};
    var m = window.CQMapSVG, out = "";
    var cls = opts.placeClass || "cm-p";
    out += '<path class="' + esc(opts.usaClass || "cm-usa") + '" d="' + m.usa + '"></path>';
    out += '<g id="' + esc(opts.shapesId || "cm-shapes") + '">';
    m.places.forEach(function (p) {
      out += '<path class="' + esc(cls) + '"' +
             (opts.idPrefix ? ' id="' + esc(opts.idPrefix + p.id) + '"' : "") +
             ' data-id="' + esc(p.id) + '" fill="' + esc(p.fill) + '" d="' + p.d + '"></path>';
    });
    /* Prince Edward Island is too small to hit with a finger. It gets an
       invisible oval on top so a thumb lands on the island and not the sea. */
    m.hit.forEach(function (h) {
      out += '<ellipse class="' + esc(opts.hitClass || "cm-hit") + '" data-id="' + esc(h["data-id"]) +
             '" cx="' + esc(h.cx) + '" cy="' + esc(h.cy) + '" rx="' + esc(h.rx) + '" ry="' + esc(h.ry) + '"></ellipse>';
    });
    out += "</g>";
    out += '<g id="' + esc(opts.watersId || "cm-waters") + '"><path class="' +
           esc(opts.waterClass || "cm-water") + '" d="' + m.water + '"></path></g>';
    out += '<g id="' + esc(opts.labelsId || "cm-labels") + '" class="' + esc(opts.labelsClass || "cm-hide") + '"></g>';
    return out;
  }

  function draw(svg, opts) {
    if (!svg) return false;
    svg.setAttribute("viewBox", window.CQMapSVG.viewBox);
    svg.innerHTML = inner(opts);
    return true;
  }

  window.CQMap = { inner: inner, draw: draw };
})();
