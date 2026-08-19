#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Push internal links INTO the pages that were not receiving any.

THE PROBLEM
-----------
An August 2026 crawl found 108 of 348 pages with only one or two internal links
pointing at them. The site already had a "More to explore" block (class pd-rel)
on 274 pages, but it points *outward* to hubs — games.html, canada-quiz.html —
so the hubs got richer and the deep pages stayed invisible. 86 of the 108
starved pages already carried that block. More of the same would not have helped.

THE APPROACH
------------
Work backwards. For each starved page, find the pages most related to it and add
a link there, so the starved page gains inbound links from relevant neighbours.

Relatedness is scored on shared filename and title vocabulary, section
(driving / citizenship / kids / games / articles) and, for driving pages, the
province — an Ontario G1 page should point at other Ontario pages, not at
Saskatchewan. Hubs are never used as sources; they already link everywhere.

Blocks are written as <nav class="also"> so this never collides with pd-rel,
which tools/build_content.py owns and regenerates.

French pages only ever link to French pages.
"""
import io, os, re, glob
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUBS = {"index.html", "games.html", "quizzes.html", "for-kids.html", "blog.html",
        "all-pages.html", "daily.html", "driving-test.html", "citizenship.html",
        "about.html", "contact.html", "privacy.html", "terms.html", "sources.html",
        "offline.html", "tag.html", "top-answers.html", "canada-map.html"}
STOP = {"the","and","for","with","your","you","a","of","in","to","is","it","on","canada",
        "canadian","quiz","test","html","free","fr","les","des","une","un","la","le","du",
        "pour","avec","que","qui","est","au","aux"}
MAX_PER_SOURCE = 5     # keep blocks readable
WANT_INBOUND    = 4    # aim to bring every starved page up to this
PROV = ["ontario","alberta","bc","quebec","manitoba","saskatchewan","nova-scotia","new-brunswick"]

def toks(name):
    return {t for t in re.split(r"[^a-z0-9]+", name.lower()) if t and t not in STOP and len(t) > 2}

def section(f):
    b = os.path.basename(f)
    if re.search(r"(g1|class-5|class-7|class-7l|road-signs|rules-of-the-road|driving|licence|winter-tires)", b): return "driving"
    if re.search(r"citizen", b): return "citizenship"
    if re.search(r"for-kids", b): return "kids"
    if re.search(r"quiz", b): return "quiz"
    return "other"

def province(f):
    b = os.path.basename(f)
    for p in PROV:
        if b.startswith(p): return p
    return None

def load(lang):
    pat = "fr/*.html" if lang == "fr" else "*.html"
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, pat))):
        rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
        if os.path.basename(rel) in ("offline.html",): continue
        out.append(rel)
    return out

def title_of(d):
    """Anchor text. Prefer the H1 — page titles carry marketing tails like
    "| Family Games" that make ugly, unhelpful link text. Fall back to the
    title, minus anything after a pipe, when the H1 is too short to stand alone."""
    import html as _h
    h = re.search(r"<h1[^>]*>(.*?)</h1>", d, re.S)
    if h:
        t = re.sub(r"\s+", " ", _h.unescape(re.sub(r"<[^>]+>", "", h.group(1)))).strip()
        letters = re.sub(r"[^A-Za-zÀ-ÿ]", "", t)
        if len(letters) >= 8:
            return t
    m = re.search(r"<title>(.*?)</title>", d, re.S)
    t = _h.unescape(m.group(1).strip()) if m else ""
    t = t.split("|")[0]
    return re.sub(r"\s+", " ", t).strip()

def main():
    changed = 0
    report = []
    for lang in ("en", "fr"):
        pages = load(lang)
        text  = {f: io.open(os.path.join(ROOT, f), encoding="utf-8").read() for f in pages}
        title = {f: title_of(text[f]) for f in pages}
        tok   = {f: toks(os.path.basename(f)) | toks(title[f]) for f in pages}

        inbound = Counter()
        links   = defaultdict(set)
        for f in pages:
            for h in re.findall(r'href="([^"#?]+\.html)"', text[f]):
                if h.startswith("http"): continue
                t = os.path.normpath(os.path.join(os.path.dirname(f), h)).replace(os.sep, "/")
                inbound[t] += 1
                links[f].add(t)

        starved = [f for f in pages if inbound[f] <= 2 and os.path.basename(f) not in HUBS]
        additions = defaultdict(list)   # source -> [target]
        used = Counter()

        for tgt in starved:
            need = WANT_INBOUND - inbound[tgt]
            scored = []
            for src in pages:
                if src == tgt: continue
                if os.path.basename(src) in HUBS: continue
                if tgt in links[src]: continue
                if used[src] >= MAX_PER_SOURCE: continue
                s = len(tok[src] & tok[tgt]) * 2
                if section(src) == section(tgt) and section(tgt) != "other": s += 3
                if province(src) and province(src) == province(tgt): s += 4
                if s <= 0: continue
                s -= inbound[src] * 0.05      # prefer quieter sources
                scored.append((s, src))
            scored.sort(reverse=True)
            for _, src in scored[:max(need, 0)]:
                additions[src].append(tgt)
                used[src] += 1
                inbound[tgt] += 1

        for src, tgts in additions.items():
            d = text[src]
            i = d.find("</section>\n<!--/PAGEDOC-->")
            if i == -1:
                i = d.find("<!--/PAGEDOC-->")
                if i == -1: continue
            heading = "Vous aimerez peut-être aussi" if lang == "fr" else "You might also like"
            items = []
            for t in tgts:
                href = os.path.basename(t)
                items.append('<a href="%s">%s</a>' % (href, title[t]))
            block = ('  <h2>%s</h2>\n  <nav class="also"><p>%s</p></nav>\n'
                     % (heading, " · ".join(items)))
            d = d[:i] + block + d[i:]
            io.open(os.path.join(ROOT, src), "w", encoding="utf-8").write(d)
            changed += 1
        report.append((lang, len(starved), sum(len(v) for v in additions.values()), len(additions)))

    for lang, starved, added, srcs in report:
        print("  %s: %d starved pages, %d new links added across %d source pages"
              % (lang, starved, added, srcs))
    print("  files rewritten:", changed)

main()
