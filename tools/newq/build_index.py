"""canada-quiz.com — keep all-pages.html honest.

all-pages.html is the full directory of the site: seven sections, every page
listed, and the number of questions beside every quiz. The footer only carries
seventeen links; this page carries them all, and it is the page a visitor lands
on when the menu does not have what they want.

Two things go stale the moment a page or a question is added, and both are
visible claims: the "N pages" and "N questions" chips at the top, and the
Driving Test Practice list. A page that says 172 pages while the footer says 193
is exactly the kind of small wrong number an AdSense reviewer treats as
careless, and it is the kind the owner spots on his phone.

What this does:
  * rebuilds the Driving Test Practice list from tools/site_map.json, so a new
    province cannot be left out, with each page's real question count read from
    js/driving/<code>.js;
  * recomputes both chips from what is actually on the page and on disk.

Every string it writes is registered in tools/extra_fr.json with its French, so
the French twin is right on the next build_fr run.

    python3 tools/newq/build_index.py
"""

import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

PAGE = os.path.join(ROOT, "all-pages.html")
LINK = re.compile(r'<a href="([^"]+)">(.*?)(?:<span class="idx-n">([^<]*)</span>)?\s*</a>')


def bank_counts():
    """questions per driving page, straight from the province's own bank"""
    out = {}
    for f in sorted(os.listdir(os.path.join(ROOT, "js", "driving"))):
        if not f.endswith(".js") or f == "signs.js":
            continue
        code = f[:-3]
        d = json.loads(subprocess.run(["node", os.path.join(HERE, "dumpbank.js"), code],
                                      capture_output=True, text=True, check=True).stdout)
        qs = d["questions"]
        sg = sum(1 for q in qs if q.get("sec") == "signs")
        ru = len(qs) - sg
        out[code] = {"practice": len(qs), "signs": sg, "rules": ru, "mock": len(qs)}
    return out



# Quizzes whose bank lives in its own JS file, so the count can be read from the
# source rather than trusted. The inline banks (canada-quiz, world-quiz and the
# rest) keep whatever number the page already carries — node /tmp/qcount.js is
# what refreshes those, because they can only be counted in a browser.
JS_BANKS = {
    "citizenship.html": ("js/citizenship-questions.js", "CITIZENSHIP_QUESTIONS"),
    "fun-quiz.html": ("js/fun-questions.js", "FUN_QUESTIONS"),
}


def js_bank_count(rel, global_name):
    """Length of a bank declared as `const NAME = [ … ]` in its own file."""
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        return None
    js = ('var window={};' + open(path, encoding="utf-8").read().replace("const " + global_name, "var " + global_name)
          + ';process.stdout.write(String(' + global_name + '.length))')
    out = subprocess.run(["node", "-e", js], capture_output=True, text=True)
    return int(out.stdout) if out.returncode == 0 and out.stdout.strip().isdigit() else None

def kind_of(name):
    if name.endswith("-road-signs.html"):
        return "signs"
    if name.endswith("-rules-of-the-road.html"):
        return "rules"
    if name.endswith("-mock-test.html"):
        return "mock"
    if name.endswith("-practice-test.html"):
        return "practice"
    return None


def code_of(name):
    """which bank does this page load"""
    p = os.path.join(ROOT, name)
    if not os.path.exists(p):
        return None
    m = re.search(r'<script src="js/driving/([a-z]{2})\.js', open(p, encoding="utf-8").read())
    return m.group(1) if m else None


def main():
    html = open(PAGE, encoding="utf-8").read()
    site_map = json.load(open(os.path.join(ROOT, "tools", "site_map.json"), encoding="utf-8"))
    counts = bank_counts()

    driving = next(g for g in site_map["groups"] if g["title"] == "Driving Test Practice")

    rows, pairs = [], {}
    for href, label in sorted(driving["links"], key=lambda x: x[1]):
        code, kind = code_of(href), kind_of(href)
        # only the practice page carries a count: it is the one page that holds
        # the whole bank. The mock draws from the same bank and the two study
        # pages are its halves, so counting them too would triple the site total.
        n = counts.get(code, {}).get(kind) if code and kind == "practice" else None
        if n:
            chip = "%d questions" % n
            rows.append('<a href="%s">%s <span class="idx-n">%s</span></a>' % (href, label, chip))
            pairs[chip] = "%d questions" % n
        else:
            rows.append('<a href="%s">%s</a>' % (href, label))

    # replace the whole Driving Test Practice column block
    m = re.search(r'(<h2>Driving Test Practice</h2>.*?<div class="idx-cols">)(.*?)(</div>)', html, re.S)
    if not m:
        print("!! could not find the Driving Test Practice list in all-pages.html")
        return 1
    html = html[:m.start(2)] + "\n      " + "\n      ".join(rows) + "\n    " + html[m.end(2):]

    # the JS-backed quiz counts, refreshed from their own source files
    for page, (rel, gname) in JS_BANKS.items():
        n = js_bank_count(rel, gname)
        if not n:
            continue
        pat = re.compile(r'(<a href="%s">[^<]*<span class="idx-n">)([\d,]+)( questions</span>)' % re.escape(page))
        m = pat.search(html)
        if m and m.group(2).replace(",", "") != str(n):
            print("  %s: %s -> %d questions" % (page, m.group(2), n))
            html = pat.sub(lambda mm: mm.group(1) + "{:,}".format(n) + mm.group(3), html, count=1)
            pairs["{:,} questions".format(n)] = "{:,} questions".format(n).replace(",", " ")

    # both chips, recomputed
    total_q = sum(int(x.replace(",", "")) for x in re.findall(r'<span class="idx-n">([\d,]+) questions</span>', html))
    listed = len(set(re.findall(r'<a href="([a-z0-9][a-z0-9./-]*\.html)"', re.search(
        r"<main.*?</main>", html, re.S).group(0))))
    old_pages = re.search(r'<span class="pill">([\d,]+) pages</span>', html).group(1)
    old_qs = re.search(r'<span class="pill">([\d,]+) questions</span>', html).group(1)
    html = html.replace('<span class="pill">%s pages</span>' % old_pages,
                        '<span class="pill">%d pages</span>' % listed, 1)
    html = html.replace('<span class="pill">%s questions</span>' % old_qs,
                        '<span class="pill">{:,} questions</span>'.format(total_q), 1)
    open(PAGE, "w", encoding="utf-8").write(html)

    pairs["%d pages" % listed] = "%d pages" % listed
    pairs["{:,} questions".format(total_q)] = "{:,} questions".format(total_q).replace(",", " ")
    p = os.path.join(ROOT, "tools", "extra_fr.json")
    extra = json.load(open(p, encoding="utf-8"))
    for k, v in pairs.items():
        extra.setdefault(k, v)
    json.dump(extra, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)

    print("all-pages.html: %d pages listed, %s questions, %d driving links"
          % (listed, "{:,}".format(total_q), len(rows)))
    print("  (%s pages -> %d, %s questions -> %s)" % (old_pages, listed, old_qs, "{:,}".format(total_q)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
