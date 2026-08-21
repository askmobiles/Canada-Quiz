"""canada-quiz.com — stop a page shipping French that can never be looked up.

build_fr.py translates ONE TEXT NODE AT A TIME. So a sentence that contains
emphasis inside it is not one node, it is three, and a dictionary key holding
the whole sentence will never match. Translating the fragments separately does
not work either, because French word order is not English word order.

    <p>SGI splits the test into <strong>two parts</strong>. …</p>   BAD
    <p><strong>SGI splits the test into two parts.</strong> …</p>   FINE

The same trap catches a label and its value written in one node:

    <p>How the test is split: Two sections.</p>                     BAD
    <p><b>How the test is split:</b> Two sections.</p>              FINE (two nodes, two keys)

Do NOT run check() over the whole site. About forty older pages have their
fragments registered and working; unwrapping them once turned 86 untranslated
sentences into 272 before it was backed out. Run it over pages you are writing.
"""

import re

# <span> is deliberately excluded. The site uses it for chips and labels whose
# text is registered on its own — .pill, .qb-lab "Correct answer", .qb-acc-n
# "30 questions" — and those are fine. The trap is emphasis inside prose.
INLINE = ("strong", "b", "em", "i", "u", "mark")

# A block whose text we care about.
BLOCK = re.compile(r"<(p|li|h1|h2|h3|h4|figcaption|summary|td|th)\b[^>]*>(.*?)</\1>", re.S)
TAG = re.compile(r"<[^>]+>")


def _text(s):
    return re.sub(r"\s+", " ", TAG.sub("", s)).strip()


def check(html, where=""):
    """Return a list of problems. Empty list means the page is safe to translate."""
    problems = []
    for m in BLOCK.finditer(html):
        inner = m.group(2)
        whole = _text(inner)
        if not whole:
            continue
        for tag in INLINE:
            for em in re.finditer(r"<%s\b[^>]*>(.*?)</%s>" % (tag, tag), inner, re.S):
                part = _text(em.group(1))
                if not part or part == whole:
                    continue          # the emphasis wraps the whole sentence — fine
                if len(whole) - len(part) < 3:
                    continue          # only punctuation outside it — fine
                problems.append(
                    "%s: <%s> wraps only part of a sentence — "
                    "the whole node can never be looked up: %r inside %r"
                    % (where, tag, part[:60], whole[:90]))
    return problems


def unwrap_partial_strong(html):
    """Promote emphasis that covers only part of a sentence to cover nothing.

    Safe, blunt and deliberate: it is better to lose a bold word than to ship a
    French page that quietly stays English.
    """
    def fix(m):
        inner = m.group(2)
        whole = _text(inner)
        out = inner
        for tag in ("strong", "b", "em", "i"):
            for em in re.finditer(r"<%s\b[^>]*>(.*?)</%s>" % (tag, tag), inner, re.S):
                part = _text(em.group(1))
                if part and part != whole and len(whole) - len(part) >= 3:
                    out = out.replace(em.group(0), em.group(1))
        return m.group(0).replace(inner, out)

    return BLOCK.sub(fix, html)
