#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages that belong to Eesan, not to visitors.

Imported by rewrite_pages.py, build_fr.py and build_sitemap.py. A page listed
here is:
  * left exactly as hand-written — no shared header, footer or scripts,
  * never given a French twin,
  * never put in sitemap.xml,
  * never given ads or analytics, so opening it does not pollute the stats.

Keep this list tiny. Everything else on a public site should be public.
"""
PRIVATE = {
    "my-stats.html",
}
