#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Removes every claim about WHO makes the site, and every promise of human
review that the owner cannot personally stand behind.

His instruction, 29 August 2026:

    "I don't verify all. The thinks my self I trust you but I don't want to lie
     person verify"
    "Who mad this no need for anyone"

Two separate problems, both fixed here:

  1. HONESTY. "A person reads every question before it goes live" and "We review
     our questions against official materials" both promise a human checking
     routine. He does not check every question himself, so the site must not say
     someone does. The reader-reports-it route in "Found a mistake?" is the true
     safeguard and it stays.

  2. ANONYMITY. He has said more than once that the maker does not need naming —
     no ASK Egoods, no "small team", no "small group". The site speaks for
     itself.

What is NOT touched: the unofficial / not-affiliated-with-the-Government-of-
Canada notices. Those are honest, legally useful, and he has never asked for
them to go.

Writes after every successful replacement so a failure never leaves a file
half-edited.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------------------------------------------------------------- new wording
ABOUT_P = T(
    " study guide published by Immigration, Refugees and Citizenship Canada. Each "
    "question includes an explanation, because understanding the answer matters more "
    "than memorizing it. The practice test follows the real format — 20 questions, with "
    "15 correct needed to pass — so the experience feels close to the real thing.",
    " publié par Immigration, Réfugiés et Citoyenneté Canada. Chaque question comprend "
    "une explication, car comprendre la réponse compte plus que la mémoriser. Le test "
    "pratique suit le format réel — 20 questions, dont 15 bonnes réponses pour réussir — "
    "de sorte que l'expérience se rapproche du vrai examen.")

CONTACT_INDEP = T(
    "The site is an independent project with no connection to the Government of Canada. "
    "That distinction matters most when your question is about a real application rather "
    "than a page on this site.",
    "Le site est un projet indépendant sans lien avec le gouvernement du Canada. Cette "
    "distinction compte surtout lorsque votre question porte sur une véritable demande "
    "plutôt que sur une page de ce site.")

CONTACT_REPLY = T(
    "The page says replies usually arrive within a few business days. Weekends and "
    "holidays naturally stretch that a little.",
    "La page indique que les réponses arrivent habituellement en quelques jours "
    "ouvrables. Les fins de semaine et les jours fériés allongent naturellement ce "
    "délai.")

CONTACT_META = T(
    "Contact Canada Quiz &amp; Family Fun Games with questions, corrections or "
    "suggestions.",
    "Communiquez avec Canada Quiz &amp; Family Fun Games pour des questions, des "
    "corrections ou des suggestions.")

CONTACT_REL = T("Learn about this site and why it stays free",
                "En savoir plus sur ce site et sur les raisons de sa gratuité")

CIT_P = T(
    "The questions follow the subjects covered in the official Discover Canada study "
    "guide. This is unofficial practice, not from the Government of Canada, so keep "
    "reading the real guide beside it.",
    "Les questions suivent les sujets abordés dans le guide d'étude officiel Découvrir "
    "le Canada. Il s'agit d'un exercice non officiel, qui ne provient pas du "
    "gouvernement du Canada : gardez le vrai guide à portée de main.")

# ------------------------------------------------------- (file, old, new) list
EDITS = [
    # --- about.html: drop the human-review promise -------------------------
    ("about.html",
     " study guide published by Immigration, Refugees and Citizenship Canada. Each "
     "question includes an explanation, because understanding the answer matters more "
     "than memorizing it. The practice test follows the real format — 20 questions, "
     "with 15 correct needed to pass — so the experience feels close to the real "
     "thing. We review our questions against official materials and update them when "
     "those materials change.",
     ABOUT_P),

    # --- contact.html: meta description ------------------------------------
    ("contact.html",
     "Contact Canada Quiz &amp; Family Fun Games with questions, corrections or "
     "suggestions. Published by ASK Egoods.",
     CONTACT_META),

    # --- contact.html: the JSON-LD copy of the same sentence ----------------
    ("contact.html",
     "Contact Canada Quiz & Family Fun Games with questions, corrections or "
     "suggestions. Published by ASK Egoods.",
     "Contact Canada Quiz & Family Fun Games with questions, corrections or "
     "suggestions."),

    # --- contact.html: the Published by block -------------------------------
    ("contact.html",
     '    <h2>Published by</h2>\n'
     '    <p><strong>ASK Egoods</strong> — '
     '<a href="https://askegoods.com" rel="noopener">askegoods.com</a></p>\n\n',
     ""),

    # --- contact.html: prose ------------------------------------------------
    ("contact.html",
     "The site is published by ASK Egoods and is an independent project with no "
     "connection to the Government of Canada. That distinction matters most when your "
     "question is about a real application rather than a page on this site.",
     CONTACT_INDEP),

    ("contact.html",
     "    <li>The publisher is named openly as ASK Egoods, with a link through to its "
     "own website for anyone who wants to check.</li>\n",
     ""),

    ("contact.html",
     "The page says replies usually arrive within a few business days. It is a small "
     "team rather than a call centre, so weekends and holidays naturally stretch that "
     "a little.",
     CONTACT_REPLY),

    # --- contact.html: the whole "who publishes this" question --------------
    ("contact.html",
     "  <h3>Who actually publishes this website?</h3>\n"
     "  <p>ASK Egoods, named on this page with a link to its own site. The quizzes, "
     "the citizenship practice and the family games are built and maintained by the "
     "same small group.</p>\n",
     ""),

    ("contact.html",
     "Learn who builds this site and why it stays free",
     CONTACT_REL),

    # --- citizenship.html: drop "built by a small team" ---------------------
    ("citizenship.html",
     "The questions follow the subjects covered in the official Discover Canada study "
     "guide. This is unofficial practice built by a small team, not by the Government "
     "of Canada, so keep reading the real guide beside it.",
     CIT_P),
]


def main():
    for name, old, new in EDITS:
        path = os.path.join(ROOT, name)
        txt = io.open(path, encoding="utf-8").read()
        if old not in txt:
            if new and new in txt:
                print("%s: already done, skipped" % name)
                continue
            sys.exit("%s: NOT FOUND\n  %r" % (name, old[:90]))
        if txt.count(old) != 1:
            sys.exit("%s: NOT UNIQUE (%d times)\n  %r"
                     % (name, txt.count(old), old[:90]))
        txt = txt.replace(old, new)
        io.open(path, "w", encoding="utf-8").write(txt)   # write after EVERY hit
        print("%s: replaced %r..." % (name, old[:60]))
    flush_pairs()


if __name__ == "__main__":
    main()
