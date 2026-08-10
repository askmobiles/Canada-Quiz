#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write sw.js from tools/sw_template.js.

The version string is a hash of everything the service worker precaches, so a
build that changes nothing produces the same sw.js and returning visitors are
not made to re-download anything; a build that changes something produces a new
one, the browser notices, and js/pwa.js offers the visitor a Refresh button.

Run this LAST in the pipeline — after rewrite_pages.py and build_fr.py — so the
stamped asset names it precaches are the ones the pages actually ask for.
"""
import hashlib, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import asset_ver

# The app shell: what a visitor needs for the site to feel alive with no
# signal. Deliberately small — the rest fills in as they play.
SHELL_PAGES = [
    "index.html", "games.html", "quizzes.html", "offline.html",
    "citizenship.html", "driving-test.html", "daily.html",
]
SHELL_ASSETS = [
    "css/style.css", "js/site.js", "js/game-fullscreen.js", "js/endcard.js",
    "js/tv-mode.js", "js/pwa.js",
    "brand/logo-horizontal-white.svg", "brand/favicon.svg",
    "brand/icon-192.png", "brand/icon-512.png", "brand/apple-touch-icon.png",
    "site.webmanifest",
]


def main():
    precache = []
    for p in SHELL_PAGES:
        if os.path.exists(os.path.join(ROOT, p)):
            precache.append(p)
    for a in SHELL_ASSETS:
        full = os.path.join(ROOT, a)
        if not os.path.exists(full):
            print("  !! missing from the shell:", a)
            continue
        if a.endswith((".css", ".js")):
            precache.append("%s?v=%s" % (a, asset_ver.ver(a)))
        else:
            precache.append(a)

    h = hashlib.sha1()
    for p in precache:
        h.update(p.encode("utf-8"))
        full = os.path.join(ROOT, p.split("?")[0])
        if os.path.exists(full):
            with open(full, "rb") as f:
                h.update(hashlib.sha1(f.read()).digest())
    version = h.hexdigest()[:12]

    tpl = io.open(os.path.join(ROOT, "tools", "sw_template.js"), encoding="utf-8").read()
    out = (tpl.replace("__VERSION__", version)
              .replace("__PRECACHE__", json.dumps(precache, indent=2)))

    path = os.path.join(ROOT, "sw.js")
    old = io.open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    if old == out:
        print("sw.js unchanged (version %s, %d files precached)" % (version, len(precache)))
        return
    io.open(path, "w", encoding="utf-8").write(out)
    print("wrote sw.js — version %s, %d files precached" % (version, len(precache)))


main()
