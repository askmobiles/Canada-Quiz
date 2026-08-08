#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Per-file cache stamps.

WHY THIS EXISTS
---------------
The site used to carry one global stamp, ASSET_VER, on every css/js link. Two
problems came from that:

1. Every build changed the stamp on all 202 pages, so a one-line edit produced a
   202-file diff in GitHub Desktop. (Eesan asked about this more than once:
   "why evey time 135 page need to update?")

2. Worse — the stamp was bumped BY HAND. On 7 Aug 2026 three JS files were
   edited and the build ran without a bump. Every page kept its old ?v=, so a
   returning visitor would have been served the STALE cached JS and seen none of
   the new questions. The mistake was invisible until someone noticed
   "rewritten: 0 of 101".

Both go away if the stamp is a hash of the file's own contents:

  * editing js/gk-questions.js changes the stamp on that file only, so only the
    pages that load it are rewritten;
  * a changed file can never keep an old stamp, because the stamp IS the file.

The hash is the first 8 hex characters of the file's SHA-1 — plenty to tell
versions apart, and short enough to keep URLs readable.
"""
import hashlib, io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_cache = {}


def ver(rel):
    """Stamp for a site-root-relative asset path, e.g. "js/site.js".

    Returns "0" for a file that does not exist, so a typo shows up as ?v=0
    rather than crashing the build.
    """
    if rel in _cache:
        return _cache[rel]
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    try:
        with io.open(path, "rb") as fh:
            h = hashlib.sha1(fh.read()).hexdigest()[:8]
    except OSError:
        h = "0"
    _cache[rel] = h
    return h


def forget(rel=None):
    """Drop cached hashes. Call after rewriting an asset during the same build —
    js/site.js is rewritten with the dictionary stamp before it is itself hashed."""
    if rel is None:
        _cache.clear()
    else:
        _cache.pop(rel, None)


def stamp_i18n_into_site_js():
    """js/site.js loads js/i18n-fr.js by hand, so its ?v= cannot be stamped by
    the page rewriter. Write the dictionary's current hash into site.js first,
    THEN let site.js be hashed — order matters, or site.js carries a stale
    reference and its own hash is computed from the wrong bytes.

    Returns True when the file changed."""
    import re
    path = os.path.join(ROOT, "js", "site.js")
    src = io.open(path, encoding="utf-8").read()
    want = ver("js/i18n-fr.js")
    new = re.sub(r'("js/i18n-fr\.js\?v=)[^"]*(")', r"\g<1>%s\g<2>" % want, src)
    if new != src:
        io.open(path, "w", encoding="utf-8").write(new)
        forget("js/site.js")
        return True
    return False


if __name__ == "__main__":
    for f in ["css/style.css", "js/site.js", "js/i18n-fr.js", "js/ads.js",
              "js/analytics.js", "js/gk-questions.js", "js/citizenship-questions.js"]:
        print("%-34s %s" % (f, ver(f)))
