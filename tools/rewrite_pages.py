#!/usr/bin/env python3
"""
Canada Quiz — rewrite_pages.py

Makes every English page use:
  * the SAME header and footer (drawn by js/site.js)
  * the new brand logo and favicon
  * the language button (EN <-> FR)

Run it from the site folder:   python3 tools/rewrite_pages.py
It only touches the .html files in the site root.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://canada-quiz.com/"

NAV = [
    ("index.html",       "Home"),
    ("quizzes.html",     "Quizzes"),
    ("games.html",       "Family Games"),
    ("citizenship.html", "Citizenship"),
    ("daily.html",       "Daily"),
    ("blog.html",        "Blog"),
]
FOOTER_LINKS = [
    ("index.html",   "Home"),
    ("about.html",   "About"),
    ("contact.html", "Contact"),
    ("privacy.html", "Privacy Policy"),
    ("terms.html",   "Terms &amp; Conditions"),
]
BRAND      = "Canada Quiz &amp; Family Fun Games"
FOOTER_TAG = "Free quizzes, family games and citizenship practice — no signup, no ads in your face."
COPYRIGHT  = "© 2026 Canada Quiz &amp; Family Fun Games. All rights reserved."
DISCLAIMER = "Unofficial practice site. Not affiliated with the Government of Canada."


def header_html(page):
    links = "\n      ".join(
        '<a href="%s"%s>%s</a>' % (h, ' class="on" aria-current="page"' if h == page else "", l)
        for h, l in NAV
    )
    return (
        '<header class="site-header">\n'
        '  <div class="container">\n'
        '    <a class="brand" href="index.html" aria-label="%s">'
        '<img src="brand/logo-horizontal-white.svg" alt="%s" class="brand-logo" width="230" height="55"></a>\n'
        '    <nav class="nav" aria-label="Main">\n'
        '      %s\n'
        '      <button type="button" class="lang-btn" data-no-i18n data-set-lang="fr" '
        'aria-label="Passer en français" title="Passer en français">'
        '<span aria-hidden="true">🌐</span> FR</button>\n'
        '    </nav>\n'
        '  </div>\n'
        '</header>' % (BRAND, BRAND, links)
    )


def footer_html():
    links = " · ".join('<a href="%s">%s</a>' % (h, l) for h, l in FOOTER_LINKS)
    return (
        '<footer class="site-footer">\n'
        '  <div class="container center">\n'
        '    <img src="brand/logo-horizontal-white.svg" alt="%s" class="footer-logo" width="200" height="48">\n'
        '    <p>%s</p>\n'
        '    <div class="footer-links">%s</div>\n'
        '    <p class="muted" style="color:#b4a9cc;font-size:12px">%s</p>\n'
        '    <p class="muted" style="color:#b4a9cc;font-size:12.5px">%s</p>\n'
        '  </div>\n'
        '</footer>' % (BRAND, FOOTER_TAG, links, COPYRIGHT, DISCLAIMER)
    )


ICON_BLOCK = (
    '<link rel="icon" href="brand/favicon.svg" type="image/svg+xml">\n'
    '<link rel="apple-touch-icon" href="brand/apple-touch-icon.png">\n'
    '<link rel="manifest" href="site.webmanifest">'
)

# these <link> tags always sit alone on their own line, so match line-by-line
# (the old favicon was an inline SVG full of ">" characters)
OLD_ICON = re.compile(r'^[ \t]*<link rel="icon"[^\n]*\n', re.M)
OLD_APPLE = re.compile(r'^[ \t]*<link rel="apple-touch-icon"[^\n]*\n', re.M)
OLD_MANIFEST = re.compile(r'^[ \t]*<link rel="manifest"[^\n]*\n', re.M)
HEADER_RE = re.compile(r'<header class="site-header">.*?</header>', re.S)
FOOTER_RE = re.compile(r'<footer class="site-footer">.*?</footer>', re.S)
HREFLANG_RE = re.compile(r'^[ \t]*<link rel="alternate" hreflang=[^\n]*\n', re.M)
CANON_RE = re.compile(r'^[ \t]*<link rel="canonical"[^\n]*\n', re.M)


def main():
    files = sorted(f for f in glob.glob(os.path.join(ROOT, "*.html")))
    changed = 0
    for path in files:
        page = os.path.basename(path)
        s = open(path, encoding="utf-8").read()
        orig = s

        # --- head: icons, canonical, hreflang -------------------------------
        s = OLD_ICON.sub("", s)
        s = OLD_APPLE.sub("", s)
        s = OLD_MANIFEST.sub("", s)
        s = HREFLANG_RE.sub("", s)
        s = CANON_RE.sub("", s)

        head_add = (
            ICON_BLOCK + "\n"
            + '<link rel="canonical" href="%s%s">\n' % (SITE, page)
            + '<link rel="alternate" hreflang="en" href="%s%s">\n' % (SITE, page)
            + '<link rel="alternate" hreflang="fr" href="%sfr/%s">\n' % (SITE, page)
            + '<link rel="alternate" hreflang="x-default" href="%s%s">\n' % (SITE, page)
        )
        if "</head>" not in s:
            print("!! no </head> in", page); continue
        s = s.replace("</head>", head_add + "</head>", 1)

        # --- header / footer ------------------------------------------------
        if not HEADER_RE.search(s):
            print("!! no header in", page)
        s = HEADER_RE.sub(lambda m: header_html(page), s, count=1)
        if not FOOTER_RE.search(s):
            print("!! no footer in", page)
        s = FOOTER_RE.sub(lambda m: footer_html(), s, count=1)

        # --- site.js --------------------------------------------------------
        s = re.sub(r'[ \t]*<script src="js/site\.js"></script>\n?', "", s)
        if '<script src="js/analytics.js"></script>' in s:
            s = s.replace('<script src="js/analytics.js"></script>',
                          '<script src="js/site.js"></script>\n'
                          '  <script src="js/analytics.js"></script>', 1)
        else:
            s = s.replace("</body>", '  <script src="js/site.js"></script>\n</body>', 1)

        if s != orig:
            open(path, "w", encoding="utf-8").write(s)
            changed += 1
    print("rewritten:", changed, "of", len(files))


if __name__ == "__main__":
    main()
