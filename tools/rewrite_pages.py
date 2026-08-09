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
import glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import private_pages
import schema_ld
import asset_ver

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://canada-quiz.com/"

# ---------------------------------------------------------------------------
# CACHE STAMP — bump this EVERY time css/style.css, js/site.js or js/analytics.js
# changes, then re-run this script + build_fr.py.
#
# Why: browsers keep a saved copy of the stylesheet. If the file changes but the
# web address stays the same, returning visitors keep the OLD stylesheet and the
# new page looks broken. Changing ?v=... makes it a new address, so everyone gets
# the fresh file. (This bit us on 27 Jul 2026 — new hero HTML + old cached CSS.)
# ---------------------------------------------------------------------------
# Kept only so old build notes still resolve; the real stamps are per-file
# hashes from tools/asset_ver.py. Nothing in this script reads this value.
ASSET_VER = "per-file-hash"

# The full A-to-Z page list shown at the bottom of every page.
# Add a new page to tools/site_map.json and re-run this script.
SITE_MAP = json.load(open(os.path.join(ROOT, "tools", "site_map.json"), encoding="utf-8"))

NAV = [
    ("index.html",       "Home"),
    ("quizzes.html",     "Quizzes"),
    ("games.html",       "Family Games"),
    ("citizenship.html", "Citizenship"),
    ("driving-test.html",  "Driving Test"),
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
        '    <nav class="nav" aria-label="Main navigation">\n'
        '      %s\n'
        '      <button type="button" class="lang-btn" data-no-i18n data-set-lang="fr" '
        'aria-label="Passer en français" title="Passer en français">'
        '<span aria-hidden="true">🌐</span> FR</button>\n'
        '    </nav>\n'
        '  </div>\n'
        '</header>' % (BRAND, BRAND, links)
    )


def footer_map_html():
    """The full A-to-Z list of every page, grouped, at the bottom of the site."""
    total = sum(len(g["links"]) for g in SITE_MAP["groups"])
    cols = []
    for g in SITE_MAP["groups"]:
        items = "\n        ".join('<a href="%s">%s</a>' % (h, l) for h, l in g["links"])
        cols.append('      <div class="footer-map-col">\n'
                    '        <div class="fm-h">%s</div>\n'
                    '        %s\n'
                    '      </div>' % (g["title"], items))
    return ('    <details class="footer-map">\n'
            '      <summary>All pages <span class="fm-count">(%d)</span></summary>\n'
            '      <div class="footer-map-cols">\n'
            '%s\n'
            '      </div>\n'
            '    </details>' % (total, "\n".join(cols)))


def footer_html():
    links = " · ".join('<a href="%s">%s</a>' % (h, l) for h, l in FOOTER_LINKS)
    return (
        '<footer class="site-footer">\n'
        '  <div class="container center">\n'
        '    <img src="brand/logo-horizontal-white.svg" alt="%s" class="footer-logo" width="200" height="48">\n'
        '    <p>%s</p>\n'
        '    <div class="footer-links">%s</div>\n'
        '%s\n'
        '    <p class="muted" style="color:#b4a9cc;font-size:12px">%s</p>\n'
        '    <p class="muted" style="color:#b4a9cc;font-size:12.5px">%s</p>\n'
        '  </div>\n'
        '</footer>' % (BRAND, FOOTER_TAG, links, footer_map_html(), COPYRIGHT, DISCLAIMER)
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

# The old AdSense tag that used to sit in <head>. It is now loaded late by
# js/ads.js instead, so the page draws first and the ads follow. See js/ads.js.
ADS_HEAD_RE = re.compile(
    r'^[ \t]*<script[^>]*pagead2\.googlesyndication\.com[^>]*>\s*</script>[ \t]*\n?', re.M)
ADS_TAIL_RE = re.compile(r'[ \t]*<script src="js/ads\.js(\?[^"]*)?"[^>]*></script>\n?')

# Pinch-zoom must never be switched off in the page source: blocking it locks
# out anyone who needs to enlarge the text (WCAG 1.4.4, and Lighthouse checks
# it). js/game-fullscreen.js still locks the viewport while a game is actually
# in play mode, and puts it back on the way out.
VIEWPORT_RE = re.compile(r'(<meta name="viewport" content=")([^"]*)(">)')


def fix_viewport(s):
    def repl(m):
        parts = [p.strip() for p in m.group(2).split(",")]
        parts = [p for p in parts
                 if not p.startswith("user-scalable")
                 and not p.startswith("maximum-scale")]
        return m.group(1) + ", ".join(parts) + m.group(3)
    return VIEWPORT_RE.sub(repl, s)



def main():
    # js/site.js loads js/i18n-fr.js itself, so that ?v= is written in here
    # first. Do it BEFORE site.js is hashed, or the pages would point at a
    # site.js whose bytes no longer match its own stamp.
    if asset_ver.stamp_i18n_into_site_js():
        print("js/site.js: dictionary stamp ->", asset_ver.ver("js/i18n-fr.js"))

    # private_pages.PRIVATE are hand-written owner-only pages: no shared
    # header/footer, no analytics, no ads. Left exactly as written.
    files = sorted(f for f in glob.glob(os.path.join(ROOT, "*.html"))
                   if os.path.basename(f) not in private_pages.PRIVATE)
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
        s = ADS_HEAD_RE.sub("", s)   # AdSense moves out of <head> (see js/ads.js)
        s = ADS_TAIL_RE.sub("", s)   # re-added below, so the ?v= stamp stays fresh

        # the home page lives at the bare URL, not at /index.html —
        # keeping them identical stops Google seeing two copies of the home page
        en_url = "" if page == "index.html" else page
        fr_url = "fr/" if page == "index.html" else "fr/" + page

        head_add = (
            ICON_BLOCK + "\n"
            + '<link rel="canonical" href="%s%s">\n' % (SITE, en_url)
            + '<link rel="alternate" hreflang="en" href="%s%s">\n' % (SITE, en_url)
            + '<link rel="alternate" hreflang="fr" href="%s%s">\n' % (SITE, fr_url)
            + '<link rel="alternate" hreflang="x-default" href="%s%s">\n' % (SITE, en_url)
        )
        s = fix_viewport(s)

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

        # --- the three site-wide scripts, on EVERY page, in a fixed order -----
        # site.js      draws the header/footer and runs the French dictionary
        # analytics.js visitor tracking — must be on every page or the numbers lie
        # ads.js       loads AdSense AFTER the page is readable
        #
        # These are stripped and re-added every build rather than left wherever
        # a page happened to have them. Before this, a page only got
        # analytics.js if its hand-written source already had the tag, so 100
        # of 218 pages — every driving test, every blog article — were
        # invisible in the stats. Adding a new page can no longer miss it.
        for _js in ("site", "analytics", "ads"):
            s = re.sub(r'[ \t]*<script src="js/%s\.js(\?[^"]*)?"[^>]*></script>\n?' % _js, "", s)
        s = s.replace(
            "</body>",
            '  <script src="js/site.js?v=%s"></script>\n'
            '  <script src="js/analytics.js?v=%s"></script>\n'
            '  <script src="js/ads.js?v=%s" defer></script>\n</body>'
            % (asset_ver.ver("js/site.js"),
               asset_ver.ver("js/analytics.js"),
               asset_ver.ver("js/ads.js")), 1)

        # --- cache stamp: A HASH OF EACH FILE, not one shared version --------
        # Each ?v= is the first 8 hex of that file's SHA-1 (tools/asset_ver.py).
        # Two things follow, and both matter:
        #   * editing one JS file rewrites only the pages that load it, instead
        #     of all 202 pages every single build;
        #   * a changed file can never keep a stale stamp, because the stamp IS
        #     the file. No more remembering to bump a constant by hand.
        s = re.sub(r'(<link rel="stylesheet" href="(css/[A-Za-z0-9_./-]+\.css))(\?[^"]*)?(")',
                   lambda m: '%s?v=%s%s' % (m.group(1), asset_ver.ver(m.group(2)), m.group(4)), s)

        s = re.sub(r'(<script src="(js/[A-Za-z0-9_./-]+\.js))(\?[^"]*)?(")',
                   lambda m: '%s?v=%s%s' % (m.group(1), asset_ver.ver(m.group(2)), m.group(4)), s)

        # --- structured data (JSON-LD) --------------------------------------
        # Regenerated every run from tools/schema_ld.py, so it always matches
        # the page's real title, description and question bank.
        s = schema_ld.inject(page, s, "en")

        if s != orig:
            open(path, "w", encoding="utf-8").write(s)
            changed += 1
    print("rewritten:", changed, "of", len(files))


if __name__ == "__main__":
    main()
