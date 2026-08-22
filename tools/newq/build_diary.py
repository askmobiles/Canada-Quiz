#!/usr/bin/env python3
"""
build_diary.py — builds the Canada Diary page from tools/newq/diary_data.json.

Two passes, exactly like the driving pages:

  python3 tools/newq/build_diary.py          # writes the ENGLISH block into
                                             # canada-diary.html, and does the
                                             # registrations
  python3 tools/newq/build_diary.py --fr     # writes the FRENCH block into
                                             # fr/canada-diary.html
                                             # RUN THIS AFTER build_fr.py.

Why the second pass is not optional
-----------------------------------
build_fr.py translates one text node at a time through the dictionary. A diary
note's French is NOT in the dictionary — it lives beside its English in
diary_data.json. Without --fr the French page ships 131 notes in English, which
is exactly what happened to twenty-four driving pages on 20 August.

  python3 tools/newq/build_diary.py --check  # reports stale/missing without
                                             # changing anything

Why every note is printed into the HTML
---------------------------------------
The pickers filter with CSS over notes that are already in the page. Nothing is
fetched or inserted by JavaScript. If the notes only appeared after a tap,
Google would index one day and ignore the other hundred and thirty.
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "tools", "newq", "diary_data.json")
PAGE = "canada-diary.html"

MON = {
    "en": ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"],
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
           "août", "septembre", "octobre", "novembre", "décembre"],
}
ERA_LABEL = {
    "en": ["Before Canada", "1867 – 1899", "1900 – 1949", "1950 – 1999", "2000 – today"],
    "fr": ["Avant le Canada", "1867 – 1899", "1900 – 1949", "1950 – 1999", "2000 à aujourd'hui"],
}
LONG_AGO = {"en": "Thousands of years ago", "fr": "Il y a des milliers d'années"},
UPCOMING = {"en": "Not yet", "fr": "À venir"}


# A small colour icon per note, so a reader scrolling can see at a glance what
# kind of thing each one is. Decorative only — it never carries a fact.
# The glyph sits in a FIXED box with overflow:hidden, because you cannot control
# which font a reader's machine substitutes. That is the hero-badge lesson.
TOPIC = {
    "war":     ("\u2694\ufe0f", "War and the people in it",   "Guerre et ceux qui l'ont faite"),
    "treaty":  ("\U0001FAB6", "Treaties and Indigenous history", "Trait\u00e9s et histoire autochtone"),
    "law":     ("\u2696\ufe0f", "Law, rights and government",  "Lois, droits et gouvernement"),
    "disaster":("\U0001F525", "Disaster",                      "Catastrophe"),
    "explore": ("\U0001F9ED", "Exploration and gold",          "Exploration et or"),
    "land":    ("\U0001F341", "The land and the map",          "Le territoire et la carte"),
    "build":   ("\U0001F682", "Built things",                  "Ce qui a \u00e9t\u00e9 b\u00e2ti"),
    "sport":   ("\U0001F3C5", "Sport",                         "Sport"),
    "people":  ("\U0001F464", "People",                        "Personnes"),
    "sea":     ("\u2693", "The sea",                           "La mer"),
    "culture": ("\U0001F3AD", "Culture and stories",           "Culture et r\u00e9cits"),
    "science": ("\U0001F4A1", "Discoveries",                   "D\u00e9couvertes"),
}

MARK_OPEN = "<!--DIARY-->"
MARK_CLOSE = "<!--/DIARY-->"


def e(s):
    return html.escape(str(s), quote=True)


def when(n, lang):
    y, m, d = n["y"], n.get("m"), n.get("d")
    if y < 0:
        return "Thousands of years ago" if lang == "en" else "Il y a des milliers d'années"
    if y == 1000:
        return "About the year 1000" if lang == "en" else "Vers l'an 1000"
    if m and d:
        return ("%s %d, %d" % (MON[lang][m - 1], d, y)) if lang == "en" \
            else ("%d %s %d" % (d, MON[lang][m - 1], y))
    if m:
        return "%s %d" % (MON[lang][m - 1], y)
    return str(y)


def anchor(n):
    """A stable id so a note can be linked, shared and cited by a teacher."""
    if n.get("m") and n.get("d"):
        return "d-%04d-%02d-%02d" % (n["y"], n["m"], n["d"])
    if n.get("m"):
        return "d-%04d-%02d" % (n["y"], n["m"])
    if n["y"] < 0:
        return "d-precontact"
    return "d-%04d" % n["y"]


def iso(n):
    if n.get("m") and n.get("d"):
        return "%04d-%02d-%02d" % (n["y"], n["m"], n["d"])
    if n.get("m"):
        return "%04d-%02d" % (n["y"], n["m"])
    return "%04d" % n["y"] if n["y"] > 0 else ""


def note_html(n, lang):
    title, body = n[lang]
    cls = "dnote fut" if n.get("future") else "dnote e%d" % n["era"]
    dt = iso(n)
    timeattr = ' datetime="%s"' % dt if dt else ""
    tag = ('<span class="dtag">%s</span>' % e(UPCOMING[lang])) if n.get("future") else ""
    link = ""
    if n.get("link"):
        # A whole phrase in its own element. NEVER link part of a sentence:
        # build_fr.py matches one text node at a time and a split sentence can
        # never be looked up again.
        label = "Read more on this" if lang == "en" else "En lire plus à ce sujet"
        href = n["link"] if lang == "en" else n["link"]
        link = '\n      <p class="dmore"><a href="%s">%s</a></p>' % (e(href), e(label))
    topic = n.get("topic", "land")
    glyph, label_en, label_fr = TOPIC.get(topic, TOPIC["land"])
    label = label_en if lang == "en" else label_fr
    icon = ('<span class="dicon t-%s" title="%s"><span aria-hidden="true">%s</span>'
            '<span class="sr-only">%s</span></span>' % (topic, e(label), glyph, e(label)))
    tpl = (
        '\n    <article class="%s" id="%s" data-era="%d"%s%s>'
        '\n      ' + icon.replace('%', '%%') +
        '\n      <time class="dwhen"%s>%s</time>%s'
        '\n      <h2 class="dtitle">%s</h2>'
        '\n      <p class="dbody">%s</p>%s'
        '\n      <p class="dsrc">%s %s</p>'
        '\n    </article>')
    return (tpl
        % (cls, anchor(n), n["era"],
           ' data-m="%d"' % n["m"] if n.get("m") else "",
           ' data-d="%d"' % n["d"] if n.get("d") else "",
           timeattr, e(when(n, lang)), tag,
           e(title), e(body), link,
           "—" if lang == "en" else "—", e(n["src"])))


def block(notes, lang):
    """Every note, in order, printed into the page. CSS does the filtering."""
    notes = sorted(notes, key=lambda n: (n["y"], n.get("m") or 0, n.get("d") or 0))
    out = [MARK_OPEN, '\n  <div class="dlist" id="dlist">']
    era = None
    for n in notes:
        if n["era"] != era:
            era = n["era"]
            out.append('\n    <h2 class="dera" data-era="%d">%s</h2>'
                       % (era, e(ERA_LABEL[lang][era])))
        out.append(note_html(n, lang))
    out.append('\n  </div>\n')
    out.append(MARK_CLOSE)
    return "".join(out)


def splice(path, new_block):
    src = open(path, encoding="utf-8").read()
    if MARK_OPEN not in src:
        raise SystemExit("%s has no %s marker" % (path, MARK_OPEN))
    out = re.sub(re.escape(MARK_OPEN) + r".*?" + re.escape(MARK_CLOSE),
                 lambda _: new_block, src, flags=re.S)
    if out != src:
        open(path, "w", encoding="utf-8").write(out)
        return True
    return False


def main():
    notes = json.load(open(DATA, encoding="utf-8"))

    # every note must carry a source and both languages, or it does not ship
    bad = [n for n in notes
           if not n.get("src") or not n.get("en") or not n.get("fr")
           or len(n["en"]) != 2 or len(n["fr"]) != 2]
    if bad:
        raise SystemExit("%d note(s) missing a source or a language: %s"
                         % (len(bad), [n.get("en", ["?"])[0] for n in bad[:5]]))

    # a wrong era puts a note on the wrong paper. Canada begins 1 July 1867.
    def want(n):
        y, m = n["y"], n.get("m") or 1
        if y < 1867 or (y == 1867 and m < 7):
            return 0
        return 1 if y < 1900 else 2 if y < 1950 else 3 if y < 2000 else 4
    wrong = [(n["en"][0], n["era"], want(n)) for n in notes if n["era"] != want(n)]
    if wrong:
        raise SystemExit("era does not match the year: %s" % wrong[:5])

    fr = "--fr" in sys.argv
    check = "--check" in sys.argv
    lang = "fr" if fr else "en"
    path = os.path.join(ROOT, "fr", PAGE) if fr else os.path.join(ROOT, PAGE)

    if check:
        src = open(path, encoding="utf-8").read()
        want_block = block(notes, lang)
        print("%s: %s" % (path, "up to date" if want_block in src else "STALE"))
        return

    changed = splice(path, block(notes, lang))
    print("%s %s (%d notes, %s)"
          % ("wrote" if changed else "unchanged", path, len(notes), lang))


if __name__ == "__main__":
    main()
