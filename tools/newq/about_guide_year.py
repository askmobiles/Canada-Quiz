#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""About page — name the edition of the study guide, and put the correction
invitation back in place of the review promise that was removed.

Owner's instruction, 29 August 2026:

    "A is ok and if the yer of that book is available we add to"
    "No need to say who build no one need this information"

So the paragraph now says three true, checkable things and nothing else:

  * which guide the questions come from, and WHICH EDITION
  * what the practice test format is
  * that a reader who finds a mistake should report it and it will be fixed

It does NOT say who writes them, who reviews them, or that anyone checks them
on a schedule. See claude/decision-no-maker-named-no-review-promised.md.

EDITION, verified 29 August 2026 from the Government of Canada's own page at
canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/
discover-canada.html —

    "© Her Majesty the Queen in Right of Canada, represented by the Minister of
     Citizenship and Immigration Canada, 2012"
    Catalogue number Ci1-11/2012E   ISBN 978-1-100-20116-0
    Page last modified 2025-02-14

The 2012 edition is the one the government still serves, which is why the
wording is "the one the government still publishes" rather than "the latest" —
the latter would be a claim about editions that may not stay true.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OLD = ('    <p>Our practice questions are written based on the official '
       '<em>Discover Canada</em> study guide published by Immigration, Refugees and '
       'Citizenship Canada. Each question includes an explanation, because '
       'understanding the answer matters more than memorizing it. The practice test '
       'follows the real format — 20 questions, with 15 correct needed to pass — so '
       'the experience feels close to the real thing.</p>')

NEW = "    <p>%s</p>" % T(
    "Our practice questions are written from the official <em>Discover Canada</em> "
    "study guide published by Immigration, Refugees and Citizenship Canada — the 2012 "
    "edition, which is the one the government still publishes. Each question includes "
    "an explanation, because understanding the answer matters more than memorizing it. "
    "The practice test follows the real format — 20 questions, with 15 correct needed "
    "to pass — so the experience feels close to the real thing. If you spot a question "
    "that is wrong or out of date, tell us and we will fix it.",

    "Nos questions d'entraînement sont rédigées à partir du guide d'étude officiel "
    "<em>Discover Canada</em> publié par Immigration, Réfugiés et Citoyenneté Canada — "
    "l'édition de 2012, celle que le gouvernement publie toujours. Chaque question "
    "comprend une explication, car comprendre la réponse compte plus que la mémoriser. "
    "Le test pratique suit le format réel — 20 questions, dont 15 bonnes réponses pour "
    "réussir — de sorte que l'expérience se rapproche du vrai examen. Si vous repérez "
    "une question erronée ou périmée, dites-le-nous et nous la corrigerons.")


def main():
    path = os.path.join(ROOT, "about.html")
    txt = io.open(path, encoding="utf-8").read()
    if "the 2012 edition" in txt:
        print("about.html: already done, skipped")
    else:
        if OLD not in txt:
            sys.exit("about.html: NOT FOUND\n  %r" % OLD[:110])
        if txt.count(OLD) != 1:
            sys.exit("about.html: NOT UNIQUE (%d times)" % txt.count(OLD))
        txt = txt.replace(OLD, NEW)
        io.open(path, "w", encoding="utf-8").write(txt)   # write after the hit
        print("about.html: guide edition named, correction invitation restored")
    flush_pairs()


if __name__ == "__main__":
    main()
