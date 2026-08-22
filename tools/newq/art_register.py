#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registers the three trade articles everywhere a new page has to be listed.

A page that exists but is not registered is invisible: no card on its landing
page, no line in all-pages.html, no entry in the sitemap, and no French twin.
That has happened before, which is why this is a script and not a checklist.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PAGES = [
    ("us-tariffs-and-canada-explained.html", "c-red", "\U0001F4C9",
     T("What the American Tariffs Did to Canada, Sector by Sector",
       "Ce que les tarifs américains ont fait au Canada, secteur par secteur"),
     T("Steel exports fell by half. Copper rose 40 percent. Same year, same country, "
       "same tariffs — the whole picture with the official numbers.",
       "Les exportations d'acier ont chuté de moitié. Le cuivre a monté de 40 pour "
       "cent. Même année, même pays, mêmes tarifs — le portrait complet avec les "
       "chiffres officiels."),
     "Canada and the USA: What the Tariffs Did"),
    ("did-us-tariffs-on-canada-work.html", "c-blue", "\U0001F3ED",
     T("Did Tariffs on Canada Pay Off for the United States?",
       "Les tarifs contre le Canada ont-ils rapporté aux États-Unis?"),
     T("One smelter reopened with 150 jobs. American manufacturing is down 62,000 "
       "jobs. Both are true, and three Federal Reserve banks disagree about why.",
       "Une fonderie a rouvert avec 150 emplois. La fabrication américaine a perdu "
       "62 000 emplois. Les deux sont vrais, et trois banques de la Réserve fédérale "
       "ne s'entendent pas sur la raison."),
     "Did the Tariffs Work for the USA?"),
    ("how-canada-rebuilds-its-economy.html", "c-green", "\U0001F341",
     T("How Canada Rebuilds — New Customers, Old Barriers",
       "Comment le Canada se rebâtit — nouveaux clients, vieilles barrières"),
     T("Canada sold 29 billion dollars more to the rest of the world. Take the gold "
       "out and it was 16 billion, against 32 billion lost. What that really means.",
       "Le Canada a vendu 29 milliards de dollars de plus au reste du monde. Retirez "
       "l'or et il en reste 16 milliards, contre 32 milliards perdus. Ce que cela veut "
       "vraiment dire."),
     "How Canada Rebuilds Its Economy"),
]
TAG_EN = T("Trade", "Commerce")
CTA = T("Read article →", "Lire l'article →")
TODAY = "2026-08-22"


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
    """New cards go at the TOP of the grid, because they are the newest thing."""
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
    print("blog.html: %d cards added at the top of the grid" % cards.count("<a class"))


def reg_all_pages():
    """all-pages.html is the full directory. A page missing from it is an orphan
    that only the sitemap knows about."""
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
    print("all-pages.html: %d links added" % add.count("<a "))


if __name__ == "__main__":
    reg_site_map()
    reg_published()
    reg_blog_cards()
    reg_all_pages()
    flush_pairs()
