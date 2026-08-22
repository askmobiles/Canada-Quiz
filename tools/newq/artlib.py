#!/usr/bin/env python3
"""
tools/newq/artlib.py — the long-article builder.

This file was written on 9 August 2026, lived in /root/newq/, and was lost when
that container was recycled. It is in the repository now, for the same reason
the province tools are. Nothing in here is secret.

WHAT IT IS FOR
--------------
A long article page (canada-usa-trade-history.html and its kind) is not a quiz
and not a driving page. It is one <article> of prose, tables, callouts and
drawn charts, with a source list at the bottom.

THE ONE RULE THAT MATTERS
-------------------------
Every visible string is written as an (English, French) PAIR through T().
T() returns the English and, in the same run, writes the pair into
tools/extra_fr.json. That is why the French twin cannot drift: there is no way
to add a sentence to the page without also adding its French.

THE FRAGMENT PROBLEM, AND WHY T() SPLITS
----------------------------------------
build_fr.py translates one TEXT NODE at a time. A sentence containing <strong>
is three text nodes, so a whole-sentence dictionary key never matches and the
paragraph silently ships in English. T() therefore splits BOTH languages on
tags and registers each fragment pair separately, and refuses the pair if the
two languages do not carry the same tags in the same order.

Keys are stored UNESCAPED — a real apostrophe, a real em dash — because
build_fr.py looks the raw text node up first and html.unescape() second.

USAGE
-----
    from artlib import Article, T
    a = Article(slug="my-page.html", ...)
    a.h2(T("A heading", "Un titre"))
    a.p(T("A paragraph.", "Un paragraphe."))
    a.build()

Then run the normal pipeline (see tools/newq/README.md).
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXTRA_FR = os.path.join(ROOT, "tools", "extra_fr.json")
SITE_MAP = os.path.join(ROOT, "tools", "site_map.json")
PAGE_CONTENT = os.path.join(ROOT, "tools", "page_content.json")

PAIRS = {}          # every pair collected this run
TAG = re.compile(r"(<[^>]+>)")


# --------------------------------------------------------------------- T()
def T(en, fr):
    """Register an (English, French) pair and return the English.

    Splits on tags so each text node gets its own dictionary key, which is the
    unit build_fr.py actually looks up.
    """
    ep, fp = TAG.split(en), TAG.split(fr)
    etags = [x for x in ep if x.startswith("<")]
    ftags = [x for x in fp if x.startswith("<")]
    if etags != ftags:
        raise SystemExit(
            "T(): the two languages carry different tags, so the French can "
            "never be looked up.\n  EN %r\n  FR %r" % (en, fr))
    etxt = [x for x in ep if not x.startswith("<")]
    ftxt = [x for x in fp if not x.startswith("<")]
    for a, b in zip(etxt, ftxt):
        if a.strip():
            if not b.strip():
                raise SystemExit("T(): English fragment %r has no French" % a)
            PAIRS[a] = b
            # also register the whitespace-trimmed form, because build_fr.py
            # normalises whitespace before looking a text node up
            if a.strip() != a:
                PAIRS[a.strip()] = b.strip()
    return en


def flush_pairs():
    """Merge everything T() collected into tools/extra_fr.json."""
    d = json.load(open(EXTRA_FR, encoding="utf-8"))
    before = len(d)
    changed = 0
    for k, v in PAIRS.items():
        if d.get(k) != v:
            d[k] = v
            changed += 1
    json.dump(d, open(EXTRA_FR, "w", encoding="utf-8"),
              ensure_ascii=False, indent=0, sort_keys=True)
    print("extra_fr.json %d -> %d entries (%d written)" % (before, len(d), changed))


# ------------------------------------------------------------------ helpers
def e(s):
    return html.escape(str(s), quote=True)


def link(url, label):
    """A whole phrase in its own element. NEVER link part of a sentence."""
    return '<a href="%s">%s</a>' % (e(url), label)


def out_link(url, label):
    return ('<a href="%s" target="_blank" rel="noopener nofollow">%s</a>'
            % (e(url), label))


# ------------------------------------------------------------------- charts
# Charts are HTML, not SVG, and that is a deliberate reversal.
#
# The first version drew inline SVG. SVG set to width:100% scales its own text
# with the box, so a 12px label inside a 720-wide viewBox came out at about six
# pixels on a phone — measured, not guessed — and about fourteen on a laptop.
# HTML text does not scale with a box. It is also real text, which means
# build_fr.py translates it like any other sentence and a screen reader reads
# it aloud instead of skipping it.
#
# Bars are drawn from the left in every case, with the sign carried by the
# number and the colour. A two-sided bar looks clever and reads badly on a
# 320-pixel screen.
BAR_COLOURS = {
    "red":    "linear-gradient(90deg,#e0566a,#c1121f)",
    "green":  "linear-gradient(90deg,#4cbfae,#1f7a6f)",
    "blue":   "linear-gradient(90deg,#6fb0f5,#1471df)",
    "purple": "linear-gradient(90deg,#a99add,#7361a8)",
    "orange": "linear-gradient(90deg,#f7a486,#e0693f)",
    "teal":   "linear-gradient(90deg,#5bc0be,#0e7490)",
}
BAR_ORDER = ["red", "green", "blue", "purple", "orange", "teal"]


def bar_chart(title, rows, unit="", colours=None):
    """rows: [(label, value), ...]. Values may be negative; the bar length uses
    the size of the number and the minus sign is shown in the value column."""
    top = max(abs(v) for _, v in rows) or 1
    out = ['<div class="cq-chart">', '<p class="cq-ct">%s</p>' % title]
    for i, (name, v) in enumerate(rows):
        col = (colours[i] if colours else BAR_ORDER[i % len(BAR_ORDER)])
        pct = abs(v) / top * 100.0
        # one decimal for everything if any value has one, so a column of
        # numbers lines up instead of reading 32 next to 29.1
        dec = 1 if any(abs(x - round(x)) > 1e-9 for _, x in rows) else 0
        shown = ("%.*f" % (dec, v)).replace("-", "\u2212")
        out.append(
            '<div class="cq-row">'
            '<span class="cq-name">%s</span>'
            '<span class="cq-track"><span class="cq-bar" style="width:%.1f%%;'
            'background:%s"></span></span>'
            '<span class="cq-val">%s%s</span>'
            "</div>" % (name, pct, BAR_COLOURS[col], e(shown), e(unit)))
    out.append("</div>")
    return "".join(out)


# ------------------------------------------------------------------ Article
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://canada-quiz.com/{slug}">
<meta property="og:image" content="https://canada-quiz.com/images/social-preview.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" href="brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="brand/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#c8102e">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Canada Quiz">
<meta name="google-adsense-account" content="ca-pub-7256851069341390">
<link rel="canonical" href="https://canada-quiz.com/{slug}">
<link rel="alternate" hreflang="en" href="https://canada-quiz.com/{slug}">
<link rel="alternate" hreflang="fr" href="https://canada-quiz.com/fr/{slug}">
<link rel="alternate" hreflang="x-default" href="https://canada-quiz.com/{slug}">
</head>
<body>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Canada Quiz &amp; Family Fun Games"><img src="brand/logo-horizontal-white.svg" alt="Canada Quiz &amp; Family Fun Games" class="brand-logo" width="230" height="55"></a>
    <nav class="nav" aria-label="Main navigation">
      <a href="index.html">Home</a>
      <a href="quizzes.html">Quizzes</a>
      <a href="games.html">Family Games</a>
      <a href="for-kids.html">For Kids</a>
      <a href="citizenship.html">Citizenship</a>
      <a href="driving-test.html">Driving Test</a>
      <a href="daily.html">Daily</a>
      <a href="blog.html">Blog</a>
      <button type="button" class="lang-btn" data-no-i18n data-set-lang="fr" aria-label="Passer en français" title="Passer en français"><span aria-hidden="true">\U0001F310</span> FR</button>
    </nav>
  </div>
</header>
<main class="container">
  <article class="panel" style="max-width:860px;margin:18px auto">
"""

FOOT = """  </article>
<!--PAGEDOC-->
</main>
<footer class="site-footer">
  <div class="container center">
    <img src="brand/logo-horizontal-white.svg" alt="Canada Quiz &amp; Family Fun Games" class="footer-logo" width="200" height="48">
    <p>Free quizzes, family games and citizenship practice — no signup, no ads in your face.</p>
    <div class="footer-links"><a href="index.html">Home</a> · <a href="about.html">About</a> · <a href="contact.html">Contact</a> · <a href="sources.html">Sources</a> · <a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms &amp; Conditions</a></div>
    <div class="footer-sections"><a href="quizzes.html">All Quizzes</a> · <a href="citizenship.html">Citizenship Test Practice</a> · <a href="driving-test.html">Driving Test Practice</a> · <a href="canada-driving-test-by-province.html">Driving Tests by Province</a> · <a href="games.html">Family Games</a> · <a href="for-kids.html">For Kids</a> · <a href="canada-quiz.html">Canada Quiz</a> · <a href="gk-quiz.html">General Knowledge</a> · <a href="blog.html">Blog</a> · <a href="daily.html">Daily Quiz</a></div>
    <p class="muted" style="color:#b4a9cc;font-size:12px">© 2026 Canada Quiz &amp; Family Fun Games. All rights reserved.</p>
    <p class="muted" style="color:#b4a9cc;font-size:12.5px">Unofficial practice site. Not affiliated with the Government of Canada.</p>
  </div>
</footer>
  <script src="js/site.js"></script>
  <script src="js/analytics.js"></script>
  <script src="js/ads.js" defer></script>
  <script src="js/pwa.js" defer></script>
</body>
</html>
"""


class Article(object):
    def __init__(self, slug, title, desc, h1, hero, checked, section="History"):
        self.slug = slug
        self.title = title
        self.desc = desc
        self.h1 = h1
        self.hero = hero
        self.checked = checked
        self.section = section
        self.body = []

    # ---- blocks
    def h2(self, t):
        self.body.append("    <h2>%s</h2>" % t)

    def h3(self, t):
        self.body.append("    <h3>%s</h3>" % t)

    def p(self, t):
        self.body.append("    <p>%s</p>" % t)

    def callout(self, t):
        self.body.append('    <div class="cq-callout">%s</div>' % t)

    def ul(self, items):
        li = "".join("<li>%s</li>" % x for x in items)
        self.body.append("    <ul>%s</ul>" % li)

    def table(self, head, rows, label=None):
        """A wide table scrolls sideways on a phone. The wrapper therefore needs
        tabindex and a role, or a keyboard user can never scroll it — axe calls
        that scrollable-region-focusable, and it is a real failure, not a
        technicality."""
        th = "".join("<th>%s</th>" % x for x in head)
        tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r)
                     for r in rows)
        if label is None:
            label = T("Table — scroll sideways to see all of it",
                      "Tableau — faites défiler latéralement pour tout voir")
        self.body.append(
            '    <div class="cq-scroll" tabindex="0" role="region" aria-label="%s">'
            '<table class="cq-table">'
            "<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>"
            % (e(label), th, tr))

    def fig(self, svg, caption=None):
        cap = ("<figcaption>%s</figcaption>" % caption) if caption else ""
        self.body.append('    <figure class="cq-fig">%s%s</figure>' % (svg, cap))

    def sources(self, heading, items):
        li = "".join("<li>%s</li>" % x for x in items)
        self.body.append("    <h2>%s</h2>" % heading)
        self.body.append('    <ul class="cq-sources">%s</ul>' % li)

    def disclaimer(self, t):
        self.body.append(
            '    <hr style="border:none;border-top:1px solid #e6e1d8;margin:24px 0">')
        self.body.append('    <p class="muted" style="font-size:13px">%s</p>' % t)

    # ---- output
    def render(self):
        head = HEAD.format(title=e(self.title), desc=e(self.desc), slug=self.slug)
        top = [
            '    <p class="muted" style="margin:0 0 4px"><a href="blog.html">%s</a> · %s</p>'
            % (T("← Blog", "← Blogue"), self.section),
            '    <h1 style="margin:.2em 0 .3em">%s</h1>' % self.h1,
            '    <p class="muted" style="font-size:15px;margin:0 0 6px">%s</p>' % self.hero,
            '    <p class="muted" style="font-size:13px;margin:0 0 18px">%s</p>' % self.checked,
        ]
        return head + "\n".join(top + self.body) + "\n" + FOOT

    def build(self):
        path = os.path.join(ROOT, self.slug)
        open(path, "w", encoding="utf-8").write(self.render())
        print("wrote %s (%d blocks)" % (self.slug, len(self.body)))
