"""canada-quiz.com — find English left in a French page's headline slots.

The body copy of every page goes through tools/page_content.json, which always
carries an "en" and an "fr". The headline slots do not: the <title>, the meta
description, the <h1>, the hero paragraph and every hand-written card heading
are typed straight into the English page and rely on the dictionary. Until this
script existed, nothing checked them, and 59 strings across 23 pages had
silently stayed English on the French site.

Method: compare each French page with its English twin in the same slot. If the
two are byte-identical, longer than a few characters, and contain a word that
only turns up in English prose, it was never translated.

Exit code is non-zero when anything is found, so a build can refuse to ship.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Words that appear in English prose and effectively never inside real French.
ENGLISH_ONLY = re.compile(
    r"\b(the|and|with|your|you|for|from|what|which|when|where|how|about|"
    r"free|test|questions|answer|road|rules|signs|practice|driving|licence|"
    r"before|after|every|there|their|this|that|must|should|would|can|will)\b", re.I)

SLOTS = [
    ("title", re.compile(r"<title>(.*?)</title>", re.S)),
    ("description", re.compile(r'<meta name="description" content="(.*?)"', re.S)),
    ("h1", re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)),
]
MULTI = [
    ("h2", re.compile(r"<h2[^>]*>(.*?)</h2>", re.S)),
    ("h3", re.compile(r"<h3[^>]*>(.*?)</h3>", re.S)),
    ("hero p", re.compile(r'<section class="hero">.*?<p[^>]*>(.*?)</p>', re.S)),
    ("card p", re.compile(r'<div class="card[^"]*">.*?<p[^>]*>(.*?)</p>', re.S)),
    ("pill", re.compile(r'<span class="pill">(.*?)</span>', re.S)),
    ("btn", re.compile(r'<a class="btn[^"]*"[^>]*>(.*?)</a>', re.S)),
]


def _clean(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def compare(pages=None):
    problems = []
    names = pages or sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    for name in names:
        en_path = os.path.join(ROOT, name)
        fr_path = os.path.join(ROOT, "fr", name)
        if not (os.path.exists(en_path) and os.path.exists(fr_path)):
            continue
        en = open(en_path, encoding="utf-8").read()
        fr = open(fr_path, encoding="utf-8").read()
        for label, pat in SLOTS:
            a, b = pat.search(en), pat.search(fr)
            if not (a and b):
                continue
            ta, tb = _clean(a.group(1)), _clean(b.group(1))
            if ta and ta == tb and len(ta) > 12 and ENGLISH_ONLY.search(ta):
                problems.append("%s [%s] never translated: %s" % (name, label, ta[:100]))
        for label, pat in MULTI:
            for ta, tb in zip((_clean(x) for x in pat.findall(en)),
                              (_clean(x) for x in pat.findall(fr))):
                if ta and ta == tb and len(ta) > 12 and ENGLISH_ONLY.search(ta):
                    problems.append("%s [%s] never translated: %s" % (name, label, ta[:100]))
    return problems


if __name__ == "__main__":
    found = compare(sys.argv[1:] or None)
    for p in found:
        print(p)
    print("fr_gap: %d problem(s)" % len(found))
    sys.exit(1 if found else 0)
