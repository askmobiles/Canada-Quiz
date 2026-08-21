"""canada-quiz.com — write the printed question bank into every driving page.

READ THIS BEFORE TOUCHING THE FRENCH DRIVING PAGES.

tools/build_fr.py builds every French page by translating the English page one
text node at a time through js/i18n-fr.js. That works for prose, because every
sentence we hand-write is registered as an EN/FR pair. It does NOT work for the
driving question banks, and it never did:

  * a driving question's French does not live in the dictionary at all. It lives
    inside js/driving/<code>.js as `fr:{q,a,e}` beside the English, which is what
    makes a half-English French quiz structurally impossible while you are
    playing;
  * so when build_fr.py meets a printed bank of 170 questions, it finds no key
    for any of them and leaves all 170 in English.

Until now something outside the repository put the French bank back afterwards.
It was not in tools/, so the first full rebuild in a fresh container silently
turned twenty-four French driving pages back into English — 434 English
sentences on fr/ontario-g1-practice-test.html alone. Nothing crashed and nothing
was reported. This file is that missing step, now in the repository where the
rest of the build can see it.

    RUN IT AFTER build_fr.py, EVERY TIME. It is not optional.

It writes the English block too, so a page's two languages are always generated
from the same bank by the same code and cannot drift apart. (The first six
provinces were written before the printed bank put the correct answer first, so
their English and French keys were in different orders. Running this once puts
all thirteen on the same footing.)

python3 tools/newq/fr_qbank.py            # every driving page, English and French
python3 tools/newq/fr_qbank.py --check    # report, change nothing (exit 1 if stale)
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import qbank  # noqa: E402

BLOCK = re.compile(r"<!--QBANK-->(.*?)<!--/QBANK-->", re.S)
BANK_SRC = re.compile(r'<script src="(?:\.\./)?js/driving/([a-z]{2})\.js')


def kind_of(name):
    if name.endswith("-road-signs.html"):
        return "signs"
    if name.endswith("-rules-of-the-road.html"):
        return "rules"
    if name.endswith("-practice-test.html"):
        return "practice"
    return None            # the mock test carries no bank, by design


def pages():
    """Every page that (a) loads a province bank and (b) prints one."""
    out = []
    for lang, folder in (("en", ROOT), ("fr", os.path.join(ROOT, "fr"))):
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".html"):
                continue
            path = os.path.join(folder, name)
            html = open(path, encoding="utf-8").read()
            m = BANK_SRC.search(html)
            k = kind_of(name)
            if m and k and BLOCK.search(html):
                out.append((path, ("fr/" if lang == "fr" else "") + name, m.group(1), k, lang))
    return out


def run(check_only=False):
    changed, stale, seen = 0, [], 0
    for path, label, code, kind, lang in pages():
        seen += 1
        html = open(path, encoding="utf-8").read()
        want = "<!--QBANK-->\n" + qbank.block(code, kind, lang) + "<!--/QBANK-->"
        m = BLOCK.search(html)
        if m.group(0).strip() == want.strip():
            continue
        stale.append(label)
        if not check_only:
            open(path, "w", encoding="utf-8").write(html[:m.start()] + want + html[m.end():])
            changed += 1
    if check_only:
        for s in stale:
            print("printed question bank is stale on " + s)
        print("fr_qbank --check: %d pages, %d stale" % (seen, len(stale)))
        return 1 if stale else 0
    print("fr_qbank: %d driving pages carry a printed bank, %d rewritten" % (seen, changed))
    return 0


if __name__ == "__main__":
    sys.exit(run("--check" in sys.argv))
