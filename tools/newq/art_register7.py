#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registers the driving-tests article everywhere a page has to be listed."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PAGES = [
    ("driving-tests-across-canada-explained.html", "c-blue", "\U0001F697",
     T("Driving Tests Across Canada — How Each Province Licenses Drivers",
       "Les examens de conduite au Canada — comment chaque province délivre les permis"),
     T("Canada has thirteen licensing systems, not one. The fastest route to a full licence "
       "takes 16 months; the slowest takes about five years. What each province tests, what "
       "the government audits found, and what the collision records actually show.",
       "Le Canada compte treize régimes de permis, et non un seul. La voie la plus rapide "
       "vers un permis complet prend 16 mois ; la plus lente, environ cinq ans. Ce que "
       "chaque province évalue, ce que les vérifications gouvernementales ont révélé et ce "
       "que montrent réellement les données sur les collisions."),
     "Driving Tests Across Canada — How Each Province Licenses Drivers"),
]
TAG_EN = T("Driving", "Conduite")
CTA = T("Read article \u2192", "Lire l'article \u2192")
TODAY = "2026-08-28"


def reg_site_map():
    p = os.path.join(ROOT, "tools", "site_map.json")
    d = json.load(open(p, encoding="utf-8"))
    grp = next(g for g in d["groups"] if g["title"] == "Blog")
    have = {l[0] for l in grp["links"]}
    added = 0
    for slug, _, _, _, _, short in PAGES:
        if slug not in have:
            grp["links"].append([slug, short])
            added += 1
    grp["links"].sort(key=lambda l: l[1].lower())
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("site_map.json: %d added, Blog group now %d links" % (added, len(grp["links"])))


def reg_published():
    p = os.path.join(ROOT, "tools", "published.json")
    d = json.load(open(p, encoding="utf-8"))
    for slug, _, _, _, _, _ in PAGES:
        d.setdefault(slug, TODAY)
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False,
              indent=1, sort_keys=True)
    print("published.json: %d pages" % len(d))


CARD = ('    <a class="card %s" href="%s" style="text-decoration:none;color:inherit">\n'
        '      <div class="emoji">%s</div>\n'
        '      <span class="tag" style="display:inline-block;font-size:11px;'
        'font-weight:800;text-transform:uppercase;padding:3px 9px;border-radius:999px;'
        'background:#eef3ff;color:#3a6ea5;margin-bottom:6px">%s</span>\n'
        '      <h3>%s</h3>\n'
        '      <p>%s</p>\n'
        '      <span class="btn btn-%s">%s</span>\n'
        '    </a>\n')


def reg_blog_cards():
    p = os.path.join(ROOT, "blog.html")
    s = open(p, encoding="utf-8").read()
    anchor = '<div class="grid">\n'
    if anchor not in s:
        raise SystemExit("blog.html: could not find the grid")
    cards = ""
    for slug, cls, emoji, title, blurb, _ in PAGES:
        if 'href="%s"' % slug in s:
            print("blog.html: %s already carded, skipped" % slug)
            continue
        cards += CARD % (cls, slug, emoji, TAG_EN, title, blurb,
                         cls.split("-")[1], CTA)
    if not cards:
        return
    s = s.replace(anchor, anchor + cards, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("blog.html: %d card(s) added at the top of the grid" % cards.count("<a class"))


def reg_all_pages():
    p = os.path.join(ROOT, "all-pages.html")
    s = open(p, encoding="utf-8").read()
    marker = '<a href="canada-usa-trade-history.html">'
    i = s.index(marker)
    line_start = s.rindex("\n", 0, i) + 1
    indent = s[line_start:i]
    add = ""
    for slug, _, _, _, _, short in PAGES:
        if '<a href="%s">' % slug in s:
            print("all-pages.html: %s already listed, skipped" % slug)
            continue
        add += '%s<a href="%s">%s</a>\n' % (indent, slug, short)
    if not add:
        return
    s = s[:line_start] + add + s[line_start:]
    open(p, "w", encoding="utf-8").write(s)
    print("all-pages.html: %d link(s) added" % add.count("<a "))


if __name__ == "__main__":
    reg_site_map()
    reg_published()
    reg_blog_cards()
    reg_all_pages()
    flush_pairs()
