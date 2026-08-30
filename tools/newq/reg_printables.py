#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registers printable-quizzes.html and links to it from the pages that matter.

Not a blog article, so no blog card. It belongs with the Quizzes group.

The internal links are the point of the second half of this script. A page
nothing links to is a page Google treats as unimportant, and internal linking is
one of the few ranking levers that costs nothing and carries no risk. This page
is linked from Quizzes, Citizenship, For Kids and the home page, which are the
four places a teacher or parent would actually be standing when they want a
worksheet.

Writes after every successful replacement.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "printable-quizzes.html"
SHORT = "Printable Quiz Sheets"
TODAY = "2026-08-29"


def reg_site_map():
    p = os.path.join(ROOT, "tools", "site_map.json")
    d = json.load(io.open(p, encoding="utf-8"))
    grp = next(g for g in d["groups"] if g["title"] == "Quizzes")
    if SLUG in {l[0] for l in grp["links"]}:
        print("site_map.json: already listed")
    else:
        grp["links"].append([SLUG, SHORT])
        grp["links"].sort(key=lambda l: l[1].lower())
        json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("site_map.json: added, Quizzes group now %d links" % len(grp["links"]))


def reg_published():
    p = os.path.join(ROOT, "tools", "published.json")
    d = json.load(io.open(p, encoding="utf-8"))
    d.setdefault(SLUG, TODAY)
    json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False,
              indent=1, sort_keys=True)
    print("published.json: %d pages" % len(d))


def reg_all_pages():
    p = os.path.join(ROOT, "all-pages.html")
    s = io.open(p, encoding="utf-8").read()
    if '<a href="%s">' % SLUG in s:
        print("all-pages.html: already listed")
        return
    marker = '<a href="province-quiz.html">'
    if marker not in s:
        sys.exit("all-pages.html: anchor NOT FOUND")
    i = s.index(marker)
    ls = s.rindex("\n", 0, i) + 1
    indent = s[ls:i]
    s = s[:ls] + '%s<a href="%s">%s</a>\n' % (indent, SLUG, SHORT) + s[ls:]
    io.open(p, "w", encoding="utf-8").write(s)
    print("all-pages.html: link added")


LINK = T("Printable quiz sheets", "Feuilles de questionnaire &agrave; imprimer")
BLURB = T("Free worksheets with an answer key &mdash; print or save as PDF, no signup.",
          "Feuilles gratuites avec corrig&eacute; &mdash; imprimez ou enregistrez en PDF, "
          "sans inscription.")

BLOCK = ('    <p class="pd-rel" style="margin-top:18px">'
         '<a href="%s"><strong>%s</strong></a> &mdash; %s</p>\n' % (SLUG, LINK, BLURB))

# (file, anchor to insert the block BEFORE)
LINKS_IN = [
    ("quizzes.html", "</main>"),
    ("citizenship.html", "</main>"),
    ("for-kids.html", "</main>"),
]


def reg_internal_links():
    for name, anchor in LINKS_IN:
        p = os.path.join(ROOT, name)
        s = io.open(p, encoding="utf-8").read()
        if 'href="%s"' % SLUG in s:
            print("%s: already links to it" % name)
            continue
        if s.count(anchor) < 1:
            print("%s: anchor NOT FOUND, skipped" % name)
            continue
        i = s.rindex(anchor)
        s = s[:i] + BLOCK + s[i:]
        io.open(p, "w", encoding="utf-8").write(s)   # write after every hit
        print("%s: link added" % name)


if __name__ == "__main__":
    reg_site_map()
    reg_published()
    reg_all_pages()
    reg_internal_links()
    flush_pairs()
