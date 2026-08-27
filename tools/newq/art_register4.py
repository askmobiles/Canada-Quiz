#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registers the three 27 August articles everywhere a page has to be listed."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PAGES = [
    ("how-canadas-cities-and-towns-work.html", "c-green", "\U0001F3E2",
     T("How Canada's Cities and Towns Work",
       "Comment fonctionnent les villes et villages du Canada"),
     T("Canada does not publish how many municipalities it has. Where your property tax "
       "goes, who your mayor is, and why the rules change at every provincial border.",
       "Le Canada ne publie pas le nombre de ses municipalités. Où va votre taxe "
       "foncière, qui est votre maire, et pourquoi les règles changent à chaque "
       "frontière provinciale."),
     "How Canada's Cities and Towns Work"),
    ("how-canada-built-the-railway.html", "c-red", "\U0001F682",
     T("How Canada Built the Railway",
       "Comment le Canada a bâti le chemin de fer"),
     T("It was over four years late, the last spike was iron, and government sources "
       "still disagree about how many workers died. The transcontinental railway, "
       "as the records actually describe it.",
       "Il avait plus de quatre ans de retard, le dernier crampon était en fer, et les "
       "sources gouvernementales ne s'entendent toujours pas sur le nombre de "
       "travailleurs morts. Le chemin de fer transcontinental, tel que les archives le "
       "décrivent vraiment."),
     "How Canada Built the Railway"),
    ("why-big-projects-take-so-long.html", "c-purple", "\U0001F6A7",
     T("Why Big Projects Take So Long",
       "Pourquoi les grands projets prennent autant de temps"),
     T("Toronto averages 18.8 years before construction starts. London averages 18.4. "
       "What Canada's own auditors actually blame for the cost of building — and it is "
       "not what most people think.",
       "Toronto compte en moyenne 18,8 ans avant le début des travaux. Londres, 18,4. "
       "Ce que les vérificateurs du Canada blâment réellement pour le coût de la "
       "construction — et ce n'est pas ce que la plupart des gens croient."),
     "Why Big Projects Take So Long"),
]
TAG_EN = T("Canada", "Canada")
CTA = T("Read article \u2192", "Lire l'article \u2192")
TODAY = "2026-08-27"


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
