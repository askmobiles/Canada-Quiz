"""canada-quiz.com — build one province or territory's four driving pages.

Run:  python3 tools/newq/build_prov.py tools/newq/prov/nl.json

What it does, in order:

 1. writes the four English pages (the French twins are generated later by
    tools/build_fr.py — never hand-write a page in fr/);
 2. registers every hand-written English string with its French partner in
    tools/extra_fr.json, at the same moment the English is emitted, so the two
    can never drift apart;
 3. adds the four pages to tools/site_map.json (the footer, all-pages.html and
    sitemap.xml all read that one file) with French labels for the labels too;
 4. merges the four tools/page_content.json entries;
 5. puts the province's card into the grid on driving-test.html through
    prov_card.place_card, which deletes the "Coming soon" placeholder itself and
    refuses to finish if the province ends up listed twice;
 6. adds the province to the DRIVE map in tools/make_quiz_ld.py and to PROV in
    tools/related_links.py.

It does NOT run the site pipeline. Do that afterwards, in this order:

    python3 tools/make_quiz_ld.py
    python3 tools/build_content.py
    python3 tools/make_dict.py
    python3 tools/split_fr.py
    python3 tools/rewrite_pages.py
    python3 tools/build_fr.py
    python3 tools/newq/fr_qbank.py      # NOT OPTIONAL — see that file's docstring
    python3 tools/related_links.py
    python3 tools/build_sitemap.py
    python3 tools/build_sw.py
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import qbank          # noqa: E402
import prov_card      # noqa: E402
import frsafe         # noqa: E402

PAIRS = {}            # english -> french, everything this build hand-writes


def P(d):
    """Register an EN/FR pair and return the English. This is the whole trick:
    the French is written at the same moment as the English, in the same file,
    so it cannot be forgotten and cannot drift."""
    en, fr = d["en"], d["fr"]
    if en.strip() and fr.strip() and en != fr:
        PAIRS[en] = fr
    return en


HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="stylesheet" href="css/style.css">
<meta name="theme-color" content="#c8102e">
<meta name="google-adsense-account" content="ca-pub-7256851069341390">
</head>
<body class="qmode-study">

<header class="site-header"></header>

<main class="container">
"""

TAIL = """</main>

<footer class="site-footer"></footer>

  <script src="js/driving/signs.js"></script>
  <script src="js/driving/%(code)s.js"></script>
  <script src="js/driving-engine.js"></script>
  <script>
    CQDrive.%(call)s;
  </script>
</body>
</html>
"""


def esc_attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def section(sec):
    """A <section class="panel"> of prose. Whole sentences only — never bold a
    word inside a sentence, or build_fr.py can never look the sentence up."""
    out = ['  <section class="panel">', "    <h2>%s</h2>" % P(sec["h2"])]
    for p in sec.get("paras", []):
        out.append("    <p>%s</p>" % P(p))
    if sec.get("list"):
        out.append("    <ul>")
        for li in sec["list"]:
            out.append("      <li>%s</li>" % P(li))
        out.append("    </ul>")
    out.append("  </section>\n")
    return "\n".join(out)


def cards(items):
    out = ['  <div class="grid">']
    for c in items:
        out.append('    <div class="card %s">' % c["accent"])
        out.append('      <div class="emoji">%s</div>' % c["emoji"])
        out.append("      <h3>%s</h3>" % P(c["h3"]))
        out.append("      <p>%s</p>" % P(c["p"]))
        out.append('      <a class="btn %s" href="%s">%s</a>'
                   % (c["btn"], c["href"], P(c["cta"])))
        out.append("    </div>")
    out.append("  </div>\n")
    return "\n".join(out)


def official(d):
    return ('  <section class="panel">\n'
            "    <h2>%s</h2>\n"
            "    <p>%s</p>\n"
            '    <div class="disclaimer" style="text-align:left">%s</div>\n'
            "  </section>\n" % (P(d["official"]["h2"]), P(d["official"]["p"]),
                                P(d["disclaimer"])))


def files_of(d):
    s, c = d["slug"], d["cls"]
    return {
        "practice": "%s-%s-practice-test.html" % (s, c),
        "mock": "%s-%s-mock-test.html" % (s, c),
        "signs": "%s-road-signs.html" % s,
        "rules": "%s-rules-of-the-road.html" % s,
    }


def build_page(d, kind):
    f = files_of(d)
    pg = d["pages"][kind]
    body = []

    if kind == "practice":
        body.append('  <section class="hero">')
        body.append("    <h1>%s</h1>" % P(pg["h1"]))
        body.append("    <p>%s</p>" % P(pg["hero"]))
        body.append("    <p>" + " &nbsp; ".join(
            '<span class="pill">%s</span>' % P(x) for x in pg["pills"]) + "</p>")
        body.append("  </section>\n")
        body.append('  <div class="ad-slot"><span class="ad-label">Advertisement</span></div>\n')
        body.append('  <section class="panel">')
        body.append("    <h2>%s</h2>" % P(pg["startH2"]))
        body.append('    <p class="muted">%s</p>' % P(pg["startP"]))
        body.append('    <div id="drive-quick"></div>')
        body.append('    <p class="center" style="margin-top:16px">'
                    '<a class="btn btn-green btn-lg" href="%s">%s</a></p>'
                    % (f["mock"], P(pg["cta"])))
        body.append("  </section>\n")
        for s in pg.get("before", []):
            body.append(section(s))
        body.append(cards(pg["cards"]))
        for s in pg.get("after", []):
            body.append(section(s))
        body.append(official(d))
        body.append("<!--QBANK-->\n" + qbank.block(d["code"], "practice") + "<!--/QBANK-->")

    elif kind == "mock":
        body.append('  <section class="panel center">')
        body.append("    <h1>%s</h1>" % P(pg["h1"]))
        body.append('    <p class="muted" style="max-width:660px;margin:0 auto">%s</p>'
                    % P(pg["hero"]))
        body.append('    <details class="howto"><summary>📖 How to play</summary>'
                    "<p>%s</p></details>" % P(pg["howto"]))
        body.append("  </section>\n")
        body.append('  <div id="drive-mock"></div>\n')
        for s in pg.get("after", []):
            body.append(section(s))
        body.append(official(d))

    else:  # signs, rules
        body.append('  <section class="panel center">')
        body.append("    <h1>%s</h1>" % P(pg["h1"]))
        body.append('    <p class="muted" style="max-width:660px;margin:0 auto">%s</p>'
                    % P(pg["hero"]))
        body.append("  </section>\n")
        body.append('  <div class="ad-slot"><span class="ad-label">Advertisement</span></div>\n')
        body.append('  <div id="drive-%s"></div>\n' % kind)
        for s in pg.get("after", []):
            body.append(section(s))
        body.append(official(d))
        body.append("<!--QBANK-->\n" + qbank.block(d["code"], kind) + "<!--/QBANK-->")

    body.append("<!--PAGEDOC--><!--/PAGEDOC-->\n")

    call = {"practice": 'quickPractice("#drive-quick", 10)',
            "mock": 'mock("#drive-mock")',
            "signs": 'studySigns("#drive-signs")',
            "rules": 'studyRules("#drive-rules")'}[kind]

    html = (HEAD % {"title": P(pg["title"]), "desc": esc_attr(P(pg["desc"]))}
            + "\n".join(body)
            + TAIL % {"code": d["code"], "call": call})

    problems = frsafe.check(html, files_of(d)[kind])
    if problems:
        raise AssertionError("\n".join(problems))
    return html


def merge_json(path, update):
    data = json.load(open(path, encoding="utf-8"))
    update(data)
    json.dump(data, open(path, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)


def register(d):
    f = files_of(d)

    # --- site_map.json: the single source of truth for the footer, all-pages
    #     and sitemap.xml. A page that is not here is a page nobody can find.
    def sm(data):
        for g in data["groups"]:
            if g["title"] == "Driving Test Practice":
                have = {h for h, _ in g["links"]}
                for k, label in d["siteMap"].items():
                    if f[k] not in have:
                        g["links"].append([f[k], label])
                g["links"].sort(key=lambda x: x[1])
    merge_json(os.path.join(ROOT, "tools", "site_map.json"), sm)

    # the footer showed English page names on the French site once, because
    # these labels had no French pair. They are hand-written; nothing else
    # translates them.
    for k, label in d["siteMap"].items():
        PAIRS[label] = d["siteMapFr"][k]

    def pc(data):
        for name, entry in d["pageContent"].items():
            data[name] = entry
    merge_json(os.path.join(ROOT, "tools", "page_content.json"), pc)

    # --- the card on driving-test.html
    path = os.path.join(ROOT, "driving-test.html")
    html = open(path, encoding="utf-8").read()
    card = ('    <div class="card %s">\n'
            '      <div class="emoji">%s</div>\n'
            "      <h3>%s</h3>\n"
            "      <p>%s</p>\n"
            '      <a class="btn %s" href="%s">%s</a>\n'
            "    </div>"
            % (d["accent"], d["emoji"], P(d["card"]["h3"]), P(d["card"]["p"]),
               d["btn"], f["practice"], P(d["card"]["cta"])))
    html = prov_card.place_card(html, d["card"]["h3"]["en"], card, d["afterHref"])
    open(path, "w", encoding="utf-8").write(html)

    # --- Quiz JSON-LD: three pages per province get real practice problems
    path = os.path.join(ROOT, "tools", "make_quiz_ld.py")
    src = open(path, encoding="utf-8").read()
    line = "  %s: ['%s', '%s', '%s']" % (d["code"], f["practice"], f["mock"], f["rules"])
    if "\n" + line not in src:
        src = re.sub(r"(const DRIVE = \{\n)", r"\1" + line + ",\n", src, count=1)
        open(path, "w", encoding="utf-8").write(src)

    # --- internal linking: without this the new pages score no province bonus
    path = os.path.join(ROOT, "tools", "related_links.py")
    src = open(path, encoding="utf-8").read()
    m = re.search(r"^PROV = \[(.*?)\]$", src, re.M)
    items = [x.strip().strip('"') for x in m.group(1).split(",")]
    if d["slug"] not in items:
        items.append(d["slug"])
        src = (src[:m.start()] + "PROV = [" + ", ".join('"%s"' % i for i in items) + "]"
               + src[m.end():])
        open(path, "w", encoding="utf-8").write(src)


def main(cfg_path):
    d = json.load(open(cfg_path, encoding="utf-8"))
    f = files_of(d)
    for kind in ("practice", "mock", "signs", "rules"):
        html = build_page(d, kind)
        open(os.path.join(ROOT, f[kind]), "w", encoding="utf-8").write(html)
        print("wrote", f[kind], len(html), "bytes")
    register(d)

    # every hand-written English string on those pages, with its French
    path = os.path.join(ROOT, "tools", "extra_fr.json")
    extra = json.load(open(path, encoding="utf-8"))
    added = 0
    for en, fr in PAIRS.items():
        if en not in extra:
            extra[en] = fr
            added += 1
        elif extra[en] != fr:
            print("   kept existing French for:", en[:70])
    json.dump(extra, open(path, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)
    print("extra_fr.json: +%d pairs (%d total)" % (added, len(extra)))


if __name__ == "__main__":
    main(sys.argv[1])
