"""canada-quiz.com — render the static <!--QBANK--> block for a driving page.

Why this exists
---------------
Every driving page carries its whole question bank as static HTML between
``<!--QBANK-->`` and ``<!--/QBANK-->``. That is not decoration: the quiz itself
is built by JavaScript, so without this block a crawler sees an empty page, and
"low value content" is exactly what AdSense rejected this site for once already.

Half of every driving bank asks what a sign means. Printing those questions
without the picture would be a page of nothing, so each sign question renders
its own SVG with the sign's name as both the caption and the alt text.

The markup here is byte-for-byte what the eight live provinces already carry —
verified against nova-scotia-road-signs.html, nova-scotia-rules-of-the-road.html
and nova-scotia-class-7-practice-test.html before this module was written.

Escaping rule (checked, not guessed): only ``&``, ``<`` and ``>`` are escaped.
Apostrophes stay literal. Escaping them produces a dictionary key that will
never match, and the French twin silently reverts to English.
"""

import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

# Every visible string of the block, in both languages. The French page is not
# translated from the English one by the dictionary — its questions live inside
# js/driving/<code>.js as fr:{…} and are written straight out here. That is the
# whole reason fr_qbank.py exists; see the note at the top of that file.
W = {
    "en": {
        "intro": ("This is the whole question bank from the test above, written out so you can "
                  "read straight through it. The right answer is marked, and every question has "
                  "a short explanation of why it is the right one."),
        "open": "Open all", "close": "Close all",
        "correct": "Correct answer",
        "showall": "Show all %d questions",
        "count": "%d questions",
        "h2_practice": "All %d practice questions, with every answer explained",
        "h2_signs": "All %d road sign questions, with every answer explained",
        "h2_rules": "All %d rules of the road questions, with every answer explained",
        "sec_signs": "Road signs", "sec_rules": "Rules of the road",
    },
    "fr": {
        "intro": ("Voici toute la banque de questions du test ci-dessus, écrite au complet pour "
                  "que vous puissiez la lire d'un bout à l'autre. La bonne réponse est indiquée, "
                  "et chaque question est accompagnée d'une courte explication."),
        "open": "Tout ouvrir", "close": "Tout fermer",
        "correct": "Bonne réponse",
        "showall": "Afficher les %d questions",
        "count": "%d questions",
        "h2_practice": "Les %d questions pratiques, avec chaque réponse expliquée",
        "h2_signs": "Les %d questions sur les panneaux, avec chaque réponse expliquée",
        "h2_rules": "Les %d questions sur le code de la route, avec chaque réponse expliquée",
        "sec_signs": "Panneaux routiers", "sec_rules": "Code de la route",
    },
}


def tools(lang):
    return ('<div class="qb-tools"><button type="button" class="qb-openall" '
            'data-open="%s" data-close="%s">%s</button></div>'
            % (W[lang]["open"], W[lang]["close"], W[lang]["open"]))


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def load(code):
    """Return (questions, province, signs, meta) for one province code."""
    out = subprocess.run(
        ["node", os.path.join(HERE, "dumpbank.js"), code],
        capture_output=True, text=True, check=True)
    d = json.loads(out.stdout)
    return d["questions"], d["province"], d["signs"], d["meta"]


def figure(sign, signs, meta, lang="en"):
    """The sign picture, with the sign's own name as caption and in the alt text.

    The drawing itself is never translated — a stop sign in Alberta really says
    STOP. Only the caption and the alt text change language.
    """
    en = meta[sign][lang]
    svg = signs[sign]
    if 'aria-label="' in svg:
        i = svg.index('aria-label="') + len('aria-label="')
        j = svg.index('"', i)
        have = svg[i:j]
        # "Stop — Stop sign" reads well; "Watch for deer — Watch for deer" does not.
        if have.strip().lower() != en.strip().lower():
            svg = svg[:i] + en + " — " + svg[i:j] + svg[j:]
        else:
            svg = svg[:i] + en + svg[j:]
    elif 'role="img"' in svg:
        # Some of the older drawings carry role="img" and no label at all, which
        # axe-core reports as svg-img-alt: a screen reader announces "image" and
        # nothing else. Give it the sign's own name.
        svg = svg.replace('role="img"', 'role="img" aria-label="%s"' % en, 1)
    return '<figure class="qb-sign">%s<figcaption>%s</figcaption></figure>' % (svg, en)


def item(q, signs, meta, lang="en"):
    """One <li> of the printed bank. Correct option first, the rest in their own order."""
    t = q[lang]
    rest = [o for i, o in enumerate(t["a"]) if i != q["c"]]
    opts = ('<ul class="qb-o"><li class="qb-ok">%s<span class="qb-lab">%s</span></li>'
            % (esc(t["a"][q["c"]]), W[lang]["correct"])
            + "".join("<li>%s</li>" % esc(o) for o in rest) + "</ul>")
    body = ('<p class="qb-q">%s</p>\n%s\n<p class="qb-e">%s</p>'
            % (esc(t["q"]), opts, esc(t["e"])))
    if q.get("sec") == "signs":
        return ('<li class="qb-item qb-haspic">\n%s<div class="qb-body">%s</div>\n</li>'
                % (figure(q["sign"], signs, meta, lang), body))
    return '<li class="qb-item">\n%s\n</li>' % body


def _solo(title, qs, signs, meta, lang):
    return (
        '<section class="panel qbank">\n<h2>%s</h2>\n<p>%s</p>\n%s\n'
        '<details class="qb-acc qb-acc-solo">\n'
        '<summary><span class="qb-acc-t">%s</span></summary>\n'
        '<ol class="qb">\n%s\n</ol>\n</details>\n</section>\n'
        % (title, W[lang]["intro"], tools(lang), W[lang]["showall"] % len(qs),
           "\n".join(item(q, signs, meta, lang) for q in qs)))


def _grouped(title, groups, signs, meta, lang):
    parts = []
    for label, qs in groups:
        parts.append(
            '<details class="qb-acc">\n'
            '<summary><h3 class="qb-acc-t">%s</h3><span class="qb-acc-n">%s</span></summary>\n'
            '<ol class="qb">\n%s\n</ol>\n</details>'
            % (label, W[lang]["count"] % len(qs),
               "\n".join(item(q, signs, meta, lang) for q in qs)))
    return ('<section class="panel qbank">\n<h2>%s</h2>\n<p>%s</p>\n%s\n%s\n</section>\n'
            % (title, W[lang]["intro"], tools(lang), "\n".join(parts)))


def block(code, kind, lang="en"):
    """Build the QBANK block. kind is 'practice', 'signs' or 'rules'.

    The mock-test page deliberately carries no bank: it is the timed exam page,
    and body.quiz-live .qbank{display:none} would hide it anyway.
    """
    qs, prov, signs, meta = load(code)
    w = W[lang]
    sg = [q for q in qs if q.get("sec") == "signs"]
    ru = [q for q in qs if q.get("sec") == "rules"]

    if kind == "signs":
        return _solo(w["h2_signs"] % len(sg), sg, signs, meta, lang)
    if kind == "rules":
        return _solo(w["h2_rules"] % len(ru), ru, signs, meta, lang)
    if kind == "practice":
        names = {s["id"]: s["name"][lang] for s in prov["sections"]}
        groups = [(names.get("signs", w["sec_signs"]), sg),
                  (names.get("rules", w["sec_rules"]), ru)]
        return _grouped(w["h2_practice"] % len(qs), groups, signs, meta, lang)
    raise ValueError("unknown kind %r" % kind)


if __name__ == "__main__":
    import sys
    print(block(sys.argv[1], sys.argv[2])[:2000])
