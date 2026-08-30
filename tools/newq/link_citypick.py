#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Points four related pages at the rebuilt city quiz.

The page was already ranking at position 11.5 with nothing linking to it except
the quiz index and two sibling personality quizzes. Internal links are the one
part of ranking that costs nothing and is entirely within our control, so the
four pages that are genuinely about the same subject now point at it.

Each link is added to the page's existing "More to explore" line, not dropped
into the middle of a sentence, because a link that is a whole phrase in its own
element is the only kind build_fr.py can translate cleanly.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LABEL = T("Find out which Canadian city fits you",
          "Découvrir quelle ville canadienne vous convient")
LINK = ' · <a href="which-canadian-city-quiz.html">%s</a>' % LABEL

PAGES = [
    "canada-map.html",
    "province-quiz.html",
    "canada-provinces-and-territories-explained.html",
    "canada-geography-coast-to-coast.html",
]


def main():
    for name in PAGES:
        p = os.path.join(ROOT, name)
        txt = io.open(p, encoding="utf-8").read()
        if "which-canadian-city-quiz.html" in txt:
            print("  already linked, skipped: %s" % name)
            continue
        marker = '<p class="pd-rel">'
        i = txt.find(marker)
        if i < 0:
            sys.exit("%s has no More-to-explore line" % name)
        j = txt.find("</p>", i)
        txt = txt[:j] + LINK + txt[j:]
        io.open(p, "w", encoding="utf-8").write(txt)
        print("  linked: %s" % name)
    flush_pairs()


if __name__ == "__main__":
    main()
