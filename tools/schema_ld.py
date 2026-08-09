#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structured data (JSON-LD) for every page, in English and French.

Imported by BOTH tools/rewrite_pages.py (English) and tools/build_fr.py (French),
so the two can never drift. French pages get their own block with French URLs,
French text and inLanguage fr-CA — a translated page carrying English JSON-LD
with English URLs would be worse than none at all.

What each page gets:
  * WebSite + Organization           — home page only
  * BreadcrumbList                   — every page except the home page
  * WebPage                          — every page (name, description, language)
  * Quiz with real practice problems — every page listed in tools/quiz_ld.json

Blog articles already carry a hand-written Article block; we leave it alone and
add the breadcrumb and WebPage around it.

The whole block sits between MARK_OPEN and MARK_CLOSE so a rebuild replaces it
cleanly instead of stacking copies.
"""
import io, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://canada-quiz.com/"
BRAND = "Canada Quiz & Family Fun Games"
PUBLISHER = "ASK Egoods"
SOCIAL = SITE + "images/social-preview.png"

MARK_OPEN = "<!--LD-->"
MARK_CLOSE = "<!--/LD-->"
BLOCK_RE = re.compile(re.escape(MARK_OPEN) + r".*?" + re.escape(MARK_CLOSE) + r"\n?", re.S)

_quiz = json.load(io.open(os.path.join(ROOT, "tools", "quiz_ld.json"), encoding="utf-8"))


def _load_fr_dict():
    """The finished runtime dictionary from js/i18n-fr.js — the same one the
    browser uses. Reading the built file (rather than re-merging fr_base.json and
    extra_fr.json) guarantees the JSON-LD says exactly what the visitor sees.

    Build order matters: make_dict.py must run before rewrite_pages.py."""
    path = os.path.join(ROOT, "js", "i18n-fr.js")
    try:
        raw = io.open(path, encoding="utf-8").read()
    except OSError:
        return {}
    m = re.search(r"window\.CQ_FR\s*=\s*(\{.*\});\s*$", raw, re.S)
    if not m:
        return {}
    try:
        return json.loads(m.group(1))
    except ValueError:
        return {}


_fr = _load_fr_dict()


def _fr_of(text):
    """Translate one string the way js/site.js would, or None if we cannot."""
    t = re.sub(r"\s+", " ", (text or "")).strip()
    return _fr.get(t)
_site_map = json.load(io.open(os.path.join(ROOT, "tools", "site_map.json"), encoding="utf-8"))

# section title (English, French) keyed by page filename, from the site map
SECTION_FR = {
    "Quizzes": "Quiz",
    "Driving Test Practice": "Pratique de l'examen de conduite",
    "Brain & Puzzle Games": "Jeux de réflexion et casse-tête",
    "Action & Classic Games": "Jeux d'action et classiques",
    "Party Games": "Jeux de groupe",
    "Blog": "Blogue",
    "The Site": "Le site",
}

# The landing page each section crumb points at. Google's breadcrumb spec
# requires an "item" URL on every element EXCEPT the last one; Search Console
# reported 'Missing field "item"' on 8 Aug 2026 because the middle crumb
# ("Blog", "Driving Test Practice", …) was a bare name with nowhere to go.
SECTION_PAGE = {
    "Quizzes": "quizzes.html",
    "Driving Test Practice": "driving-test.html",
    "Brain & Puzzle Games": "games.html",
    "Action & Classic Games": "games.html",
    "Party Games": "games.html",
    "Blog": "blog.html",
    "The Site": "about.html",
}

_section = {}
for _g in _site_map["groups"]:
    _title = _g["title"].replace("&amp;", "&")
    for _l in _g["links"]:
        _section.setdefault(_l[0], (_title, SECTION_FR.get(_title, _title)))

HOME_NAME = {
    "en": BRAND,
    "fr": "Canada Quiz et jeux amusants en famille",
}


def _txt(s):
    """Collapse whitespace and drop HTML entities that would break the JSON."""
    s = re.sub(r"\s+", " ", s or "").strip()
    return (s.replace("&amp;", "&").replace("&mdash;", "—")
             .replace("&nbsp;", " ").replace("&#39;", "'").replace("&quot;", '"'))


def _page_meta(html):
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    return _txt(t.group(1) if t else ""), _txt(d.group(1) if d else "")


def _url(page, lang):
    """/  and  /fr/  are the home pages — never /index.html."""
    if page == "index.html":
        return SITE if lang == "en" else SITE + "fr/"
    return (SITE if lang == "en" else SITE + "fr/") + page


def build(page, html, lang="en"):
    """Return the full JSON-LD block (with markers) for one page."""
    lang_tag = "en-CA" if lang == "en" else "fr-CA"
    name, desc = _page_meta(html)
    url = _url(page, lang)
    home = _url("index.html", lang)
    nodes = []

    org = {"@type": "Organization", "name": PUBLISHER, "url": SITE}

    if page == "index.html":
        nodes.append({
            "@type": "WebSite",
            "@id": home + "#website",
            "url": home,
            "name": HOME_NAME[lang],
            "description": desc,
            "inLanguage": lang_tag,
            "publisher": org,
        })
        nodes.append(dict(org, **{"@id": SITE + "#org", "logo": SITE + "brand/logo-icon-512.png"}))
    else:
        crumbs = [{"@type": "ListItem", "position": 1,
                   "name": "Home" if lang == "en" else "Accueil", "item": home}]
        sec = _section.get(page)
        landing = SECTION_PAGE.get(sec[0]) if sec else None
        # On the section's own landing page (blog.html inside "Blog") the middle
        # crumb would just repeat the last one, so skip it there.
        if sec and landing != page:
            crumb = {"@type": "ListItem", "position": 2,
                     "name": sec[0] if lang == "en" else sec[1]}
            if landing:
                crumb["item"] = _url(landing, lang)
            crumbs.append(crumb)
        crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1,
                       "name": name.split(" — ")[0].split(" | ")[0] or page,
                       "item": url})
        nodes.append({"@type": "BreadcrumbList", "itemListElement": crumbs})

    nodes.append({
        "@type": "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": name,
        "description": desc,
        "inLanguage": lang_tag,
        "isPartOf": {"@id": home + "#website"} if page == "index.html"
                    else {"@type": "WebSite", "url": _url("index.html", lang),
                          "name": HOME_NAME[lang]},
        "publisher": org,
        "primaryImageOfPage": {"@type": "ImageObject", "url": SOCIAL},
    })

    qs = _quiz.get(page)
    if qs:
        parts = []
        for q in qs:
            if lang == "fr" and q.get("fr"):
                qtext, opts = q["fr"]["q"], q["fr"]["o"]
            elif lang == "fr":
                # Citizenship and the general banks carry no inline French — the
                # site translates them in the browser from js/i18n-fr.js. Look the
                # strings up the same way. If ANY of the five is missing we skip the
                # question entirely; half-French structured data is worse than none.
                qtext = _fr_of(q["q"])
                opts = [_fr_of(o) for o in q["o"]]
                if not qtext or not all(opts):
                    continue
            else:
                qtext, opts = q["q"], q["o"]
            correct = opts[q["a"]]
            parts.append({
                "@type": "Question",
                "eduQuestionType": "Multiple choice",
                "name": qtext,
                "text": qtext,
                "acceptedAnswer": {"@type": "Answer", "text": correct},
                "suggestedAnswer": [{"@type": "Answer", "text": o}
                                    for i, o in enumerate(opts) if i != q["a"]],
            })
        if parts:
            nodes.append({
                "@type": "Quiz",
                "name": name,
                "url": url,
                "inLanguage": lang_tag,
                "about": {"@type": "Thing", "name": "Canada" if lang == "en" else "Canada"},
                "educationalLevel": "beginner",
                "isAccessibleForFree": True,
                "hasPart": parts,
            })

    data = {"@context": "https://schema.org", "@graph": nodes}
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return '%s<script type="application/ld+json">%s</script>%s\n' % (
        MARK_OPEN, payload, MARK_CLOSE)


def inject(page, html, lang="en"):
    """Replace any existing generated block, then insert before </head>."""
    html = BLOCK_RE.sub("", html)
    if "</head>" not in html:
        return html
    return html.replace("</head>", build(page, html, lang) + "</head>", 1)
