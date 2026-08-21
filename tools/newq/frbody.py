"""canada-quiz.com — read a French page on its own and find English sentences.

fr_gap.py compares slots between the twins. This one does not compare anything:
it reads the French page by itself and asks of every sentence in <main>, "is
this English?" That catches what a structural comparison cannot — a paragraph
that has no English counterpart in the same position, a list item that drifted,
a sentence someone edited in English inside an otherwise French page.

It is what found the 86 English sentences on 11 August.

Scoring: a sentence is called English when it contains several words that only
occur in English prose and none of the French function words. Names, numbers,
URLs, code and the sign artwork are ignored.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

EN = re.compile(r"\b(the|and|with|your|you|for|from|what|which|when|where|how|about|"
                r"this|that|there|their|must|should|would|will|can|not|are|is|was|"
                r"have|has|before|after|every|each|only|also|than|then|because)\b", re.I)
FR = re.compile(r"\b(le|la|les|un|une|des|du|de|et|ou|vous|votre|vos|qui|que|quoi|"
                r"pour|dans|avec|sur|sous|est|sont|être|avoir|ne|pas|plus|moins|"
                r"si|quand|comme|mais|donc|car|au|aux|ce|cette|ces|il|elle|on|"
                r"doit|devez|peut|pouvez|faut|selon|entre|chaque|tout|toute)\b", re.I)

SKIP_INSIDE = re.compile(r"<(script|style|svg|code|pre)\b.*?</\1>", re.S)
TAG = re.compile(r"<[^>]+>")


def sentences(main):
    text = TAG.sub(" ", SKIP_INSIDE.sub(" ", main))
    text = re.sub(r"&[a-zA-Z#0-9]+;", " ", text)
    for raw in re.split(r"(?<=[.!?])\s+|\n", text):
        s = re.sub(r"\s+", " ", raw).strip()
        if len(s) >= 30:
            yield s


def check_page(path):
    html = open(path, encoding="utf-8").read()
    m = re.search(r"<main\b.*?</main>", html, re.S)
    if not m:
        return []
    bad = []
    for s in sentences(m.group(0)):
        en = len(set(w.lower() for w in EN.findall(s)))
        fr = len(set(w.lower() for w in FR.findall(s)))
        if en >= 3 and fr == 0:
            bad.append(s[:120])
    return bad


def run(names=None):
    problems = []
    frdir = os.path.join(ROOT, "fr")
    names = names or sorted(f for f in os.listdir(frdir) if f.endswith(".html"))
    for n in names:
        p = os.path.join(frdir, os.path.basename(n))
        if not os.path.exists(p):
            continue
        for s in check_page(p):
            problems.append("fr/%s: %s" % (os.path.basename(n), s))
    return problems


if __name__ == "__main__":
    found = run(sys.argv[1:] or None)
    for p in found:
        print(p)
    print("frbody: %d English sentence(s) in French pages" % len(found))
    sys.exit(1 if found else 0)
