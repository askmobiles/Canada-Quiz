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

    python3 tools/make_samples.py    # only when a question bank changed
    python3 tools/make_quiz_ld.py    # only when a question bank changed

Cache stamps are per-file hashes now (tools/asset_ver.py) — there is no
ASSET_VER to bump by hand any more.
    python3 tools/build_content.py
    python3 tools/make_dict.py
    python3 tools/rewrite_pages.py
    python3 tools/build_fr.py
    python3 tools/build_sitemap.py
"""
import datetime, hashlib, io, json, os, re

import private_pages

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://canada-quiz.com/"
OUT = os.path.join(ROOT, "sitemap.xml")


# ---------------------------------------------------------------------------
# <lastmod> — Google uses this to decide what is worth re-crawling. It ignores
# <changefreq> entirely.
#
# The date must be HONEST. Every build rewrites all 202 pages (the ?v= cache
# stamp changes), so a plain file timestamp would tell Google "everything
# changed" every single time, and it would stop trusting the dates.
#
# So we hash the part of the page a reader actually sees — <main> plus the
# title and description — and keep the date in tools/lastmod.json. The date
# only moves when that hash moves.
# ---------------------------------------------------------------------------
LASTMOD_DB = os.path.join(ROOT, "tools", "lastmod.json")
MAIN_RE = re.compile(r"<main.*?</main>", re.S)
TITLE_RE = re.compile(r"<title>.*?</title>", re.S)
DESC_RE = re.compile(r'<meta name="description"[^>]*>', re.S)


def content_hash(path):
    try:
        s = io.open(path, encoding="utf-8").read()
    except OSError:
        return None
    parts = MAIN_RE.findall(s) + TITLE_RE.findall(s) + DESC_RE.findall(s)
    body = "".join(parts) or s
    # the cache stamp changes on every build and is not real content
    body = re.sub(r"\?v=[0-9a-z]+", "", body)
    return hashlib.sha1(body.encode("utf-8")).hexdigest()


def load_lastmod():
    try:
        return json.load(io.open(LASTMOD_DB, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_lastmod(db):
    json.dump(db, io.open(LASTMOD_DB, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)


DB = load_lastmod()
TODAY = datetime.date.today().isoformat()
_moved = []


def lastmod_for(relpath):
    """relpath is like "games.html" or "fr/games.html"."""
    h = content_hash(os.path.join(ROOT, relpath))
    if h is None:
        return None
    rec = DB.get(relpath)
    if not rec or rec.get("hash") != h:
        DB[relpath] = {"hash": h, "date": TODAY}
        if rec:
            _moved.append(relpath)
        return TODAY
    return rec["date"]


# Pages that must never be listed (thank-you pages, redirects, drafts).
SKIP = {"404.html", "google-verify.html"} | private_pages.PRIVATE

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
    # loc is the URL path: "" is the home page, "fr/" the French home page.
    # Map it back to the file that actually sits on disk.
    lm = lastmod_for("index.html" if loc == "" else
                     "fr/index.html" if loc == "fr/" else loc)
    lm_tag = "<lastmod>%s</lastmod>" % lm if lm else ""
    # NOTE: % binds tighter than +, so the whole template must be built FIRST
    # and formatted after. Formatting mid-concatenation only fills the last
    # literal and raises "not all arguments converted".
    template = ('  <url><loc>%s%s</loc>' + lm_tag +
                '<changefreq>%s</changefreq>'
                '<xhtml:link rel="alternate" hreflang="en" href="%s%s"/>'
                '<xhtml:link rel="alternate" hreflang="fr" href="%s%s"/>'
                '<xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/></url>')
    return template % (SITE, loc, freq_for(os.path.basename(en) or "index.html"),
                       SITE, en, SITE, fr, SITE, en)


def main():
    pages = sorted(
        f for f in os.listdir(ROOT)
        if f.endswith(".html") and f not in SKIP
    )

    # the home page is listed ONCE, at the bare URL — /index.html is the same
    # page and listing both makes Google report a duplicate
    rows = [url("", "", "fr/")]                    # https://canada-quiz.com/
    rows.append(url("fr/", "", "fr/"))             # https://canada-quiz.com/fr/
    for f in pages:
        if f == "index.html":
            continue
        rows.append(url(f, f, "fr/" + f))
    for f in pages:
        if f == "index.html":
            continue
        if os.path.exists(os.path.join(ROOT, "fr", f)):
            rows.append(url("fr/" + f, f, "fr/" + f))
        else:
            print("  !! no French twin for %s — left out of the sitemap" % f)

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    io.open(OUT, "w", encoding="utf-8").write(xml)
    save_lastmod(DB)
    print("wrote sitemap.xml — %d URLs (%d English pages + %d French + home)"
          % (len(rows), len(pages), len(rows) - len(pages) - 1))
    if _moved:
        print("  lastmod moved to %s on %d page(s)" % (TODAY, len(_moved)))


if __name__ == "__main__":
    main()
