#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split the French dictionary into per-engine chunks.

WHY THIS EXISTS
---------------
js/i18n-fr.js is 3.3 MB and every page under /fr/ downloaded all of it. That was
never necessary. The French pages are already French in their HTML — a scan of
fr/gk-quiz.html finds zero English dictionary keys in its static text. The
dictionary is only needed for text JavaScript injects after load: the header and
footer drawn by site.js, and quiz questions coming out of the question files.

Measured against the 3.3 MB dictionary:

    core (site.js, read-aloud, tv-mode, ...)   131 keys      3.2 KB
    gk-questions.js                           5245 keys    475.7 KB
    citizenship-questions.js                  1450 keys    131.7 KB
    fun-questions.js                          1323 keys     96.2 KB
    driving-engine.js                           18 keys      0.4 KB
    kids-quiz.js                                 2 keys      0.0 KB
    matched by no JavaScript at all          15925 keys   2680.3 KB   <- dropped

So a French driving page goes from 3,372 KB to 3.7 KB, and fr/gk-quiz.html — the
worst page on the site — from 3,372 KB to 479 KB.

Run this AFTER tools/make_dict.py, which writes js/i18n-fr.js. That file stays in
the repo as the source of truth; it is simply no longer served to visitors.

site.js decides which chunks to load by looking at which scripts the page
carries, so no page needs editing and a new quiz page picks up the right chunk
automatically.
"""
import io, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "js", "i18n-fr.js")

UI = ["site.js", "read-aloud.js", "tv-mode.js", "game-fullscreen.js",
      "endcard.js", "pwa.js", "ads.js", "analytics.js"]
CHUNKS = [("gk",     "gk-questions.js"),
          ("cit",    "citizenship-questions.js"),
          ("fun",    "fun-questions.js"),
          ("drive",  "driving-engine.js"),
          ("kids",   "kids-quiz.js")]

def load_dict():
    raw = io.open(SRC, encoding="utf-8").read()
    a = raw.find("{")
    b = raw.rstrip().rstrip(";").rfind("}") + 1
    return json.loads(raw[a:b])

def read(js):
    p = os.path.join(ROOT, "js", js)
    return io.open(p, encoding="utf-8").read() if os.path.exists(p) else ""

def write_chunk(name, mapping):
    path = os.path.join(ROOT, "js", "i18n-fr-%s.js" % name)
    body = json.dumps(mapping, ensure_ascii=False, separators=(",", ":"))
    out = ("/* Canada Quiz — French chunk '%s'. Built by tools/split_fr.py.\n"
           "   Do NOT edit by hand — edit tools/extra_fr.json and rebuild. */\n"
           "window.CQ_FR = Object.assign(window.CQ_FR || {}, %s);\n" % (name, body))
    old = io.open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    if old != out:
        io.open(path, "w", encoding="utf-8").write(out)
    return path, len(out)

def main():
    dic = load_dict()
    core = set()
    for js in UI:
        s = read(js)
        core |= {k for k in dic if len(k) > 2 and k in s}
    written = [write_chunk("core", {k: dic[k] for k in sorted(core)})]
    taken = set(core)
    for name, js in CHUNKS:
        s = read(js)
        keys = {k for k in dic if len(k) > 2 and k in s} - taken
        taken |= keys
        written.append(write_chunk(name, {k: dic[k] for k in sorted(keys)}))
    total = sum(n for _, n in written)
    print("wrote %d chunks, %.1f KB total (was %.1f KB on every French page)"
          % (len(written), total/1024.0, os.path.getsize(SRC)/1024.0))
    for p, n in written:
        print("  %-28s %8.1f KB" % (os.path.basename(p), n/1024.0))

main()
