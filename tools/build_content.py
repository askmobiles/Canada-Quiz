#!/usr/bin/env python3
"""
build_content.py — injects the written "page documentation" block into every
thin quiz / game / article page, and feeds its French into the dictionary.

Sources
  tools/page_content.json   hand-written EN + FR content, one entry per page
  tools/samples.json        auto-extracted sample questions (from tools/make_samples.py)

What it does
  1. builds an HTML block and writes it between <!--PAGEDOC--> markers,
     just before </main> on each English page
  2. merges every English -> French pair into tools/extra_fr.json
     (existing values always win, same rule as the rest of the build)

Run it BEFORE make_dict.py so the new French reaches js/i18n-fr.js:
    python3 tools/build_content.py
    python3 tools/make_dict.py
    python3 tools/rewrite_pages.py
    python3 tools/build_fr.py
    python3 tools/build_sitemap.py
"""
import io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")

CONTENT = os.path.join(TOOLS, "page_content.json")
SAMPLES = os.path.join(TOOLS, "samples.json")
EXTRA   = os.path.join(TOOLS, "extra_fr.json")

START = "<!--PAGEDOC-->"
END   = "<!--/PAGEDOC-->"

# Fixed section headings. These are the only strings shared across pages.
HEADINGS = {
    "about_quiz":  ("About this quiz",        "À propos de ce quiz"),
    "about_game":  ("About this game",        "À propos de ce jeu"),
    "about_page":  ("About this page",        "À propos de cette page"),
    "about_article": ("In short",             "En bref"),
    "inside_quiz": ("What's inside",          "Ce que contient ce quiz"),
    "inside_game": ("How it works",           "Comment ça marche"),
    "inside_page": ("What you'll find here",  "Ce que vous trouverez ici"),
    "inside_article": ("Key points",          "Points clés"),
    "samples":     ("Sample questions",       "Exemples de questions"),
    "facts_quiz":  ("Good to know",           "Bon à savoir"),
    "facts_game":  ("Tips for playing",       "Conseils pour jouer"),
    "facts_page":  ("Worth remembering",      "À retenir"),
    "facts_article": ("Worth remembering too", "À retenir également"),
    "faq":         ("Common questions",       "Questions fréquentes"),
    "related":     ("More to explore",        "À découvrir aussi"),
    "answer":      ("Answer:",                "Réponse :"),
}

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def load(path, default):
    if not os.path.exists(path):
        return default
    return json.load(io.open(path, encoding="utf-8"))

def build_block(page, entry, samples):
    kind = entry.get("kind", "quiz")           # quiz | game | page | article
    hk = {"quiz": "quiz", "game": "game", "page": "page",
          "article": "article"}.get(kind, "page")
    pairs = []                                  # (en, fr) to feed the dictionary

    def H(key):
        en, fr = HEADINGS[key]
        pairs.append((en, fr))
        return en

    out = ['<section class="pagedoc">']

    about = entry.get("about", [])
    if about:
        out.append("  <h2>%s</h2>" % esc(H("about_" + hk)))
        for p in about:
            pairs.append((p["en"], p["fr"]))
            out.append("  <p>%s</p>" % esc(p["en"]))

    inside = entry.get("inside", [])
    if inside:
        out.append("  <h2>%s</h2>" % esc(H("inside_" + hk)))
        out.append("  <ul>")
        for b in inside:
            pairs.append((b["en"], b["fr"]))
            out.append("    <li>%s</li>" % esc(b["en"]))
        out.append("  </ul>")

    sq = samples.get(page, [])
    # Pages carrying the full question bank already print every question with its
    # answer and explanation, so a five-question sample repeats content from the
    # same page. Skip it there; pages without a bank still get their samples.
    if sq:
        try:
            if "<!--QBANK-->" in io.open(os.path.join(ROOT, page), encoding="utf-8").read():
                sq = []
        except (OSError, IOError):
            pass
    if sq:
        out.append("  <h2>%s</h2>" % esc(H("samples")))
        out.append('  <ol class="sq-list">')
        for it in sq:
            out.append('    <li class="sq">')
            out.append('      <p class="sq-q">%s</p>' % esc(it["q"]))
            out.append('      <p class="sq-a"><strong>%s</strong> <span>%s</span></p>'
                       % (esc(H("answer")), esc(it["a"])))
            if it.get("e"):
                out.append('      <p class="sq-e">%s</p>' % esc(it["e"]))
            out.append("    </li>")
        out.append("  </ol>")

    facts = entry.get("facts", [])
    if facts:
        out.append("  <h2>%s</h2>" % esc(H("facts_" + hk)))
        out.append("  <ul>")
        for b in facts:
            pairs.append((b["en"], b["fr"]))
            out.append("    <li>%s</li>" % esc(b["en"]))
        out.append("  </ul>")

    faq = entry.get("faq", [])
    if faq:
        out.append("  <h2>%s</h2>" % esc(H("faq")))
        for item in faq:
            pairs.append((item["q"]["en"], item["q"]["fr"]))
            pairs.append((item["a"]["en"], item["a"]["fr"]))
            out.append("  <h3>%s</h3>" % esc(item["q"]["en"]))
            out.append("  <p>%s</p>" % esc(item["a"]["en"]))

    rel = entry.get("related", [])
    if rel:
        out.append("  <h2>%s</h2>" % esc(H("related")))
        links = []
        for href, label in rel:
            pairs.append((label["en"], label["fr"]))
            links.append('<a href="%s">%s</a>' % (href, esc(label["en"])))
        out.append('  <p class="pd-rel">%s</p>' % " · ".join(links))

    out.append("</section>")
    return "\n".join(out), pairs

def main():
    content = load(CONTENT, {})
    samples = load(SAMPLES, {})
    if not content:
        print("no tools/page_content.json — nothing to do")
        return

    extra = load(EXTRA, {})
    added = 0
    written = 0
    missing = []

    for page in sorted(content):
        path = os.path.join(ROOT, page)
        if not os.path.exists(path):
            missing.append(page)
            continue
        block, pairs = build_block(page, content[page], samples)
        wrapped = "%s\n%s\n%s" % (START, block, END)

        s = io.open(path, encoding="utf-8").read()
        if START in s and END in s:
            s = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: wrapped, s, flags=re.S)
        else:
            i = s.rfind("</main>")
            if i < 0:
                missing.append(page + " (no </main>)")
                continue
            s = s[:i] + wrapped + "\n" + s[i:]
        io.open(path, "w", encoding="utf-8").write(s)
        written += 1

        for en, fr in pairs:
            en = en.strip(); fr = fr.strip()
            if not en or not fr:
                continue
            if en not in extra:
                extra[en] = fr
                added += 1

    json.dump(extra, io.open(EXTRA, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)

    print("page content written into %d pages" % written)
    print("extra_fr.json: +%d new entries (now %d)" % (added, len(extra)))
    if missing:
        print("SKIPPED (not found): " + ", ".join(missing))

if __name__ == "__main__":
    main()
