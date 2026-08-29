#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adds the Facebook and X links to about.html and contact.html only.

Deliberately NOT in the site-wide footer, at the owner's instruction. Kids' game
pages and quiz pages stay clean.

Two rules held here:

  * Plain <a> tags. No Facebook SDK, no X widget, no follow buttons. Those load
    third-party tracking on every page that carries them, which would break the
    no-signup, nothing-collected promise the site is built on — and would be
    setting Meta cookies for a child doing a quiz.

  * The link row is its own element, and the sentence above it carries no link.
    build_fr.py translates one text node at a time, so a link in the middle of a
    sentence splits the node and the French can never be looked up.

"Facebook" and "X" are proper nouns and pass through make_dict.py untranslated.

Writes after every successful replacement, so a later failure never leaves a
file half-edited.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

FB = "https://www.facebook.com/CanadaQuizGames"
X = "https://x.com/CanadaQuiz"

H2 = T("Find us online", "Nous trouver en ligne")
LINE = T("Canada Quiz has been on Facebook and X since 2011.",
         "Canada Quiz est présent sur Facebook et X depuis 2011.")

BLOCK = (
    '    <h2>%s</h2>\n'
    '    <p>%s</p>\n'
    '    <p style="font-size:17px;font-weight:700">'
    '<a href="%s" target="_blank" rel="noopener">Facebook</a>'
    ' &middot; '
    '<a href="%s" target="_blank" rel="noopener">X</a></p>\n'
) % (H2, LINE, FB, X)

# (file, anchor the block is inserted BEFORE)
EDITS = [
    ("about.html", '    <div class="center" style="margin-top:18px">\n'),
    ("contact.html", "    <h2>Published by</h2>\n"),
]


def main():
    for name, anchor in EDITS:
        path = os.path.join(ROOT, name)
        txt = io.open(path, encoding="utf-8").read()
        if FB in txt:
            print("%s: already has the links, skipped" % name)
            continue
        if anchor not in txt:
            sys.exit("%s: anchor NOT FOUND -- %r" % (name, anchor))
        if txt.count(anchor) != 1:
            sys.exit("%s: anchor NOT UNIQUE (%d times)" % (name, txt.count(anchor)))
        txt = txt.replace(anchor, BLOCK + "\n" + anchor)
        io.open(path, "w", encoding="utf-8").write(txt)   # write after every hit
        print("%s: social block added" % name)
    flush_pairs()


if __name__ == "__main__":
    main()
