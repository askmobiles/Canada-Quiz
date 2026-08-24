#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registers the three articles of 24 August 2026 everywhere a page has to be listed.

Same job as art_register.py, different pages. A page that exists but is not
registered is invisible: no card on the blog, no line in all-pages.html, no
entry in the sitemap, and no French twin.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PAGES = [
    ("who-gets-the-tariff-money-back.html", "c-purple", "\U0001F4B5",
     T("Tariff Refunds — Who Actually Gets the Money Back?",
       "Remboursements de tarifs — qui récupère vraiment l'argent ?"),
     T("A hundred billion dollars of tariffs went back to American companies, not to the "
       "people who paid the higher prices. Why the law works that way, and what Canada "
       "does with its own counter-tariff money.",
       "Cent milliards de dollars de tarifs sont retournés à des entreprises américaines, "
       "et non aux gens qui ont payé plus cher. Pourquoi la loi fonctionne ainsi, et ce "
       "que le Canada fait de l'argent de ses propres contre-tarifs."),
     "Who Gets the Tariff Money Back?"),
    ("what-canada-and-the-usa-sell-each-other.html", "c-orange", "\U0001F69B",
     T("What Canada Sells America, and What America Sells Canada",
       "Ce que le Canada vend à l'Amérique, et ce que l'Amérique vend au Canada"),
     T("Half of what the United States buys from Canada is raw material. Five percent is "
       "consumer goods. From China it is almost exactly the other way round — and both "
       "directions of the relationship, sector by sector.",
       "La moitié de ce que les États-Unis achètent au Canada, ce sont des matières "
       "premières. Cinq pour cent sont des biens de consommation. Avec la Chine, c'est "
       "presque l'inverse — et les deux sens de la relation, secteur par secteur."),
     "What Canada and the USA Sell Each Other"),
    ("churchill-falls-gull-island-explained.html", "c-yellow", "⚡",
     T("Churchill Falls and Gull Island — What Was Actually Agreed",
       "Churchill Falls et Gull Island — ce qui a réellement été conclu"),
     T("A 70 billion dollar announcement, a contract that is not binding yet, and two "
       "recent Canadian dams that came in 82 percent over budget. What is settled and "
       "what is not.",
       "Une annonce de 70 milliards de dollars, un contrat qui n'est pas encore "
       "contraignant, et deux barrages canadiens récents dépassés de 82 pour cent. Ce qui "
       "est réglé et ce qui ne l'est pas."),
     "Churchill Falls and Gull Island"),
]
TAG_EN = T("Trade", "Commerce")
CTA = T("Read article →", "Lire l'article →")
TODAY = "2026-08-24"


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
