#!/usr/bin/env python3
"""
Canada Quiz — build_fr.py

Makes the French half of the website AUTOMATICALLY.

You write ONE page in English.  This script reads it, swaps the English words
for French using js/i18n-fr.js, fixes the links, and saves the French twin in
the /fr/ folder.

    about.html      ->  fr/about.html
    citizenship.html -> fr/citizenship.html

Run it from the site folder, every time you add or change an English page:

    python3 tools/build_fr.py

Anything the games and quizzes print while you play is translated live in the
browser by js/site.js, using the same dictionary — so nothing is missed.
"""
import glob, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRDIR = os.path.join(ROOT, "fr")
SITE = "https://canada-quiz.com/"
ASSET_DIRS = ("css/", "js/", "images/", "brand/")
ASSET_FILES = ("site.webmanifest",)

SKIP_INSIDE = {"script", "style", "textarea", "pre", "code"}


# ----------------------------------------------------------------- dictionary
def load_dict():
    src = open(os.path.join(ROOT, "js", "i18n-fr.js"), encoding="utf-8").read()
    i = src.index("{")
    j = src.rindex("}")
    return json.loads(src[i:j + 1])


DICT = load_dict()


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def _upper1(s):
    return s[:1].upper() + s[1:]


def _lower1(s):
    return s[:1].lower() + s[1:]


def core(t):
    """one string, also trying a capital / small first letter"""
    for cand in (t, html.unescape(t)):
        hit = DICT.get(cand)
        if hit:
            return hit
        lc = _lower1(cand)
        if lc != cand and DICT.get(lc):
            return _upper1(DICT[lc])
        uc = _upper1(cand)
        if uc != cand and DICT.get(uc):
            return _lower1(DICT[uc])
    return None


def tr(raw):
    """English -> French, or None if we have no translation."""
    t = norm(raw)
    if len(t) < 2:
        return None
    hit = core(t)
    if hit:
        return hit
    # strip a leading emoji / arrow and trailing punctuation, then retry
    m = re.match(r"^([^A-Za-z0-9(]*)(.*?)([\s.:!?…]*)$", t)
    if m and m.group(2) and len(m.group(2)) > 1 and m.group(2) != t:
        inner = core(m.group(2))
        if inner:
            return m.group(1) + inner + m.group(3)
    return None


# ----------------------------------------------------------------- attributes
ATTR_TEXT = ("alt", "title", "placeholder", "aria-label")
ATTR_RE = re.compile(r'([\w:-]+)\s*=\s*"([^"]*)"')


def fix_tag(tag, page):
    name = re.match(r"</?\s*([\w-]+)", tag)
    tname = name.group(1).lower() if name else ""

    def repl(m):
        key, val = m.group(1), m.group(2)
        k = key.lower()

        # 1. asset paths need one level up, because we are inside /fr/
        if k in ("src", "href") and (val.startswith(ASSET_DIRS) or val in ASSET_FILES):
            # if a French twin of the picture exists (name-fr.svg), use it,
            # so pictures with words inside them read in French too
            base, ext = os.path.splitext(val)
            twin = base + "-fr" + ext
            if ext.lower() in (".svg", ".png", ".jpg", ".webp") and \
               os.path.exists(os.path.join(ROOT, twin)):
                return '%s="../%s"' % (key, twin)
            return '%s="../%s"' % (key, val)

        # 2. words the reader can see
        if k in ATTR_TEXT:
            f = tr(val)
            if f:
                return '%s="%s"' % (key, html.escape(f, quote=True))
            return m.group(0)

        # 3. <meta ... content="...">
        if k == "content" and tname == "meta":
            low = tag.lower()
            if ('name="description"' in low or 'property="og:title"' in low
                    or 'property="og:description"' in low or 'name="twitter:title"' in low
                    or 'name="twitter:description"' in low):
                f = tr(val)
                if f:
                    return '%s="%s"' % (key, html.escape(f, quote=True))
            if 'property="og:url"' in low or 'name="twitter:url"' in low:
                return '%s="%s"' % (key, val.replace(SITE, SITE + "fr/"))
            if 'property="og:locale"' in low:
                return '%s="fr_CA"' % key
            if 'property="og:image"' in low or 'name="twitter:image"' in low:
                return m.group(0)
        return m.group(0)

    return ATTR_RE.sub(repl, tag)


# ----------------------------------------------------------------- whole page
TOKEN = re.compile(r"<!--.*?-->|<[^>]*>|[^<]+", re.S)


def convert(src, page):
    out = []
    skip_depth = 0
    for tok in TOKEN.finditer(src):
        t = tok.group(0)

        if t.startswith("<!--"):
            out.append(t)
            continue

        if t.startswith("<"):
            m = re.match(r"<\s*(/?)\s*([\w-]+)", t)
            if m:
                closing, tname = m.group(1), m.group(2).lower()
                if tname in SKIP_INSIDE:
                    if closing:
                        skip_depth = max(0, skip_depth - 1)
                    elif not t.rstrip().endswith("/>"):
                        skip_depth += 1
            out.append(fix_tag(t, page))
            continue

        if skip_depth:
            out.append(t)
            continue

        f = tr(t)
        if f:
            # keep the original spacing/newlines around the words
            lead = t[:len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            out.append(lead + f + trail)
        else:
            out.append(t)

    s = "".join(out)

    # <html lang="fr"> and a marker so js/site.js knows this page is French
    s = re.sub(r"<html[^>]*>", '<html lang="fr" data-lang="fr">', s, count=1)

    # canonical + hreflang for the French URL
    s = re.sub(r'^[ \t]*<link rel="canonical"[^\n]*\n', "", s, flags=re.M)
    s = re.sub(r'^[ \t]*<link rel="alternate" hreflang=[^\n]*\n', "", s, flags=re.M)
    # /fr/ and /  are the real home-page URLs — never /fr/index.html or /index.html
    en_url = "" if page == "index.html" else page
    fr_url = "fr/" if page == "index.html" else "fr/" + page
    head = ('<link rel="canonical" href="%s%s">\n'
            '<link rel="alternate" hreflang="en" href="%s%s">\n'
            '<link rel="alternate" hreflang="fr" href="%s%s">\n'
            '<link rel="alternate" hreflang="x-default" href="%s%s">\n'
            % (SITE, fr_url, SITE, en_url, SITE, fr_url, SITE, en_url))
    s = s.replace("</head>", head + "</head>", 1)
    return s


def main():
    os.makedirs(FRDIR, exist_ok=True)
    pages = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "*.html")))
    for page in pages:
        src = open(os.path.join(ROOT, page), encoding="utf-8").read()
        open(os.path.join(FRDIR, page), "w", encoding="utf-8").write(convert(src, page))
    print("built %d French pages in /fr/" % len(pages))


if __name__ == "__main__":
    main()
