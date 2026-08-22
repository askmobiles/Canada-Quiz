#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Makes every sideways-scrolling table reachable from a keyboard.

A wide table on a phone lives inside <div class="cq-scroll">, which scrolls
horizontally. A div that scrolls but cannot be focused is unusable with a
keyboard: there is no way to reach it, so there is no way to scroll it. axe
reports this as scrollable-region-focusable, severity serious, and it was
sitting on eleven pages of this site.

The fix is three attributes: tabindex="0" so it can be reached, role="region"
so a screen reader announces it, and an aria-label so the announcement says
something useful. The label is registered with its French, like every other
visible string.

    python3 tools/newq/fix_scroll_a11y.py

Run it BEFORE build_fr.py. It is safe to run twice.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LABEL = T("Table — scroll sideways to see all of it",
          "Tableau — faites défiler latéralement pour tout voir")

BARE = re.compile(r'<div class="cq-scroll">')
NEW = ('<div class="cq-scroll" tabindex="0" role="region" aria-label="%s">' % LABEL)


def main():
    touched = 0
    fixed = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        s = open(path, encoding="utf-8").read()
        n = len(BARE.findall(s))
        if not n:
            continue
        s2 = BARE.sub(NEW, s)
        if s2 != s:
            open(path, "w", encoding="utf-8").write(s2)
            touched += 1
            fixed += n
            print("  %s — %d wrapper(s)" % (os.path.basename(path), n))
    print("fix_scroll_a11y: %d wrapper(s) fixed across %d page(s)" % (fixed, touched))
    flush_pairs()


if __name__ == "__main__":
    main()
