"""canada-quiz.com — no driving page may talk about another province's rules.

This exists because of a real, live error. The Quebec and Manitoba page sets
were cloned from the British Columbia set, and the clone substituted the hero,
the title and the question banks but not the prose in the body. The result was a
Quebec page headed "What the real BC knowledge test looks like", telling readers
the test has 50 questions with a pass mark of 40. Publishing a wrong pass mark
to learner drivers is the worst mistake this site can make, and it was live.

The audit reads every driving page, English and French, and reports any mention
of a jurisdiction other than its own — except on the pages that compare
provinces on purpose, and except where the other province's name appears in a
question's wrong answer, which is legitimate.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# filename prefix -> (page-owner key, every spelling that means that jurisdiction)
PROVS = {
    "ontario":       ["Ontario", "DriveTest", "G1", "G2"],
    "bc":            ["British Columbia", "Colombie-Britannique", "ICBC", "C.-B."],
    "alberta":       ["Alberta"],
    "quebec":        ["Quebec", "Québec", "SAAQ"],
    "manitoba":      ["Manitoba", "Manitoba Public Insurance", "MPI"],
    "saskatchewan":  ["Saskatchewan", "SGI", "Sask."],
    "nova-scotia":   ["Nova Scotia", "Nouvelle-Écosse", "Access Nova Scotia", "N.-É."],
    "new-brunswick": ["New Brunswick", "Nouveau-Brunswick", "Service New Brunswick", "N.-B."],
    "newfoundland":  ["Newfoundland", "Terre-Neuve", "Labrador", "Motor Registration Division"],
    "pei":           ["Prince Edward Island", "Île-du-Prince-Édouard", "Access PEI", "Î.-P.-É."],
    "yukon":         ["Yukon"],
    "nwt":           ["Northwest Territories", "Territoires du Nord-Ouest"],
    "nunavut":       ["Nunavut"],
}

# Pages that name other jurisdictions on purpose.
COMPARISON_PAGES = {
    "driving-test.html",
    "canada-driving-test-by-province.html",
    "beginner-driver-education-ontario.html",
    "ontario-g1-study-guide.html",
    "all-pages.html",
}

TAG = re.compile(r"<[^>]+>")
WRONG_OPTION = re.compile(r'<li>(?!<)(.*?)</li>')


def owner(name):
    for pfx in sorted(PROVS, key=len, reverse=True):
        if name.startswith(pfx + "-"):
            return pfx
    return None


def pages():
    out = []
    for base in (ROOT, os.path.join(ROOT, "fr")):
        for f in sorted(os.listdir(base)):
            if not f.endswith(".html") or f in COMPARISON_PAGES:
                continue
            if owner(f):
                out.append(os.path.join(base, f))
    return out


def check(path):
    name = os.path.basename(path)
    mine = owner(name)
    html = open(path, encoding="utf-8").read()

    # The printed question bank legitimately names other provinces: a rival province
    # can be a wrong answer, and an explanation may say "this differs from Ontario".
    # The fault this audit exists to catch is mis-cloned PROSE — BC's pass mark sitting
    # under a Quebec heading — so the bank is not what we read.
    body = re.sub(r"<!--QBANK-->.*?<!--/QBANK-->", " ", html, flags=re.S)
    body = WRONG_OPTION.sub(" ", body)
    # …and the shared footer / header, which list every page on the site.
    body = re.sub(r"<footer\b.*?</footer>", " ", body, flags=re.S)
    body = re.sub(r"<header\b.*?</header>", " ", body, flags=re.S)
    body = re.sub(r'<nav class="also">.*?</nav>', " ", body, flags=re.S)
    # "More to explore" and "You might also like" are cross-links on purpose.
    body = re.sub(r'<(p|nav|div|section)[^>]*class="[^"]*pd-rel[^"]*".*?</\1>', " ", body, flags=re.S)
    body = re.sub(r"<!--LD-->.*?<!--/LD-->", " ", body, flags=re.S)
    # Cross-links to other provinces' pages are deliberate; drop hrefs.
    body = re.sub(r'href="[^"]*"', " ", body)
    text = TAG.sub(" ", body)

    hits = []
    for pfx, words in PROVS.items():
        if pfx == mine:
            continue
        for w in words:
            if re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(w), text):
                hits.append(w)
    return sorted(set(hits))


def run():
    problems, n = [], 0
    for p in pages():
        n += 1
        hits = check(p)
        if hits:
            rel = os.path.relpath(p, ROOT)
            problems.append("%s mentions %s" % (rel, ", ".join(hits)))
    return n, problems


if __name__ == "__main__":
    n, found = run()
    for p in found:
        print(p)
    print("province_audit: %d pages, %d problem(s)" % (n, len(found)))
    sys.exit(1 if found else 0)
