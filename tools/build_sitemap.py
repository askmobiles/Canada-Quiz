#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Canada Quiz — build_sitemap.py

Writes sitemap.xml from the pages that ACTUALLY exist on disk.

Why this file exists (29 Jul 2026): sitemap.xml used to be kept by hand.
tag.html was added to the site in a different session and nobody remembered to
edit the sitemap, so Google never learned the page existed.  Now the sitemap
is generated, so a page can never be silently left out again.

Run it last, after rewrite_pages.py and build_fr.py:

    python3 tools/make_dict.py
    python3 tools/rewrite_pages.py
    python3 tools/build_fr.py
    python3 tools/build_sitemap.py
"""
import io, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://canada-quiz.com/"
OUT = os.path.join(ROOT, "sitemap.xml")

# Pages that must never be listed (thank-you pages, redirects, drafts).
SKIP = {"404.html", "google-verify.html"}

# How often each kind of page really changes.
DAILY = {"daily.html"}
MONTHLY_EXACT = {"about.html", "contact.html", "privacy.html", "terms.html"}


def freq_for(name):
    if name in DAILY:
        return "daily"
    if name in MONTHLY_EXACT:
        return "monthly"
    # blog articles are the long-tail evergreen pages
    if name in BLOG:
        return "monthly"
    return "weekly"


def load_blog():
    """Blog article filenames come from site_map.json so there is one list."""
    p = os.path.join(ROOT, "tools", "site_map.json")
    m = json.load(io.open(p, encoding="utf-8"))
    for g in m["groups"]:
        if "Blog" in g["title"]:
            return {l[0] for l in g["links"] if l[0] != "blog.html"}
    return set()


BLOG = load_blog()


def url(loc, en, fr):
    return (
        '  <url><loc>%s%s</loc><changefreq>%s</changefreq>'
        '<xhtml:link rel="alternate" hreflang="en" href="%s%s"/>'
        '<xhtml:link rel="alternate" hreflang="fr" href="%s%s"/>'
        '<xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/></url>'
        % (SITE, loc, freq_for(os.path.basename(en) or "index.html"),
           SITE, en, SITE, fr, SITE, en)
    )


def main():
    pages = sorted(
        f for f in os.listdir(ROOT)
        if f.endswith(".html") and f not in SKIP
    )

    rows = [url("", "", "fr/index.html")]          # the bare domain
    for f in pages:
        rows.append(url(f, f, "fr/" + f))
    for f in pages:
        if os.path.exists(os.path.join(ROOT, "fr", f)):
            rows.append(url("fr/" + f, f, "fr/" + f))
        else:
            print("  !! no French twin for %s — left out of the sitemap" % f)

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    io.open(OUT, "w", encoding="utf-8").write(xml)
    print("wrote sitemap.xml — %d URLs (%d English pages + %d French + home)"
          % (len(rows), len(pages), len(rows) - len(pages) - 1))


if __name__ == "__main__":
    main()
