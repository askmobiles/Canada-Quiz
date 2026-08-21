#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build tools/quiz_ld.json — a few real multiple-choice questions per quiz page.

These feed the Quiz / Practice-problem structured data that tools/schema_ld.py
injects into every page. Google can show these as practice-problem rich results,
which is one of the few things that helps a brand-new site get crawled.

Run this whenever a question bank changes, alongside tools/make_samples.py.
Output: {page: [{"q": ..., "o": [4 options], "a": index, "fr": {...} or null}]}
"""
import io, json, os, re, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tools", "quiz_ld.json")
PER_PAGE = 3


def clean(t):
    return re.sub(r"\s+", " ", t).strip()


def usable(q, opts):
    return len(opts) == 4 and len(set(opts)) == 4 and len(q) >= 12 and q.endswith("?")


# ---------------------------------------------------------------- inline banks
INLINE_PAGES = ["canada-quiz.html", "world-quiz.html", "science-quiz.html",
                "entertainment-quiz.html", "daily.html", "money-quiz.html",
                "earth-quiz.html", "body-quiz.html", "ai-quiz.html",
                "trivia-showdown.html"]

INLINE_RE = re.compile(
    r'q:"((?:[^"\\]|\\.)*)"\s*,\s*(?:o|options):\[(.*?)\]\s*,\s*(?:a|answer):(\d)', re.S)


def from_inline(page):
    s = io.open(os.path.join(ROOT, page), encoding="utf-8").read()
    items = []
    for m in INLINE_RE.finditer(s):
        q = clean(m.group(1))
        opts = [clean(o) for o in re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(2))]
        if not usable(q, opts):
            continue
        items.append({"q": q, "o": opts, "a": int(m.group(3)), "fr": None})
        if len(items) >= PER_PAGE:
            break
    return items


# ------------------------------------------------------- banks loaded from JS
NODE = r"""
const fs = require('fs'), vm = require('vm');
function load(file, expr) {
  const c = { console }; c.window = c; c.globalThis = c; vm.createContext(c);
  return vm.runInContext(fs.readFileSync(file, 'utf8') + '\n;(' + expr + ')', c, { filename: file });
}
const ROOT = process.argv[2];   // argv[0]=node, argv[1]=this script
const out = {};

// citizenship: English only, French comes from the runtime dictionary
const cit = load(ROOT + '/js/citizenship-questions.js', 'CITIZENSHIP_QUESTIONS');
out['citizenship.html'] = cit.slice(0, 60)
  .filter(q => q.q.endsWith('?') && new Set(q.options).size === 4)
  .slice(0, 3).map(q => ({ q: q.q, o: q.options, a: q.answer, fr: null }));

// general knowledge
const gk = load(ROOT + '/js/gk-questions.js', 'GK_BANK');
let flat = [];
for (const cat of Object.values(gk))
  for (const arr of Object.values(cat)) if (Array.isArray(arr)) flat = flat.concat(arr);
out['gk-quiz.html'] = flat.filter(q => q.q.endsWith('?') && new Set(q.o).size === 4)
  .slice(0, 3).map(q => ({ q: q.q, o: q.o, a: q.a, fr: null }));

// fun Canada
const fun = load(ROOT + '/js/fun-questions.js', 'FUN_QUESTIONS');
out['fun-quiz.html'] = fun.filter(q => q.q.endsWith('?') && new Set(q.options).size === 4)
  .slice(0, 3).map(q => ({ q: q.q, o: q.options, a: q.answer, fr: null }));

// driving — these carry their own French inline
const DRIVE = {
  sk: ['saskatchewan-class-7-practice-test.html', 'saskatchewan-class-7-mock-test.html', 'saskatchewan-rules-of-the-road.html'],
  ns: ['nova-scotia-class-7-practice-test.html', 'nova-scotia-class-7-mock-test.html', 'nova-scotia-rules-of-the-road.html'],
  nb: ['new-brunswick-class-7-practice-test.html', 'new-brunswick-class-7-mock-test.html', 'new-brunswick-rules-of-the-road.html'],
  nu: ['nunavut-class-7-practice-test.html', 'nunavut-class-7-mock-test.html', 'nunavut-rules-of-the-road.html'],
  nt: ['nwt-class-7-practice-test.html', 'nwt-class-7-mock-test.html', 'nwt-rules-of-the-road.html'],
  yt: ['yukon-class-7-practice-test.html', 'yukon-class-7-mock-test.html', 'yukon-rules-of-the-road.html'],
  pe: ['pei-class-7-practice-test.html', 'pei-class-7-mock-test.html', 'pei-rules-of-the-road.html'],
  nl: ['newfoundland-class-5-practice-test.html', 'newfoundland-class-5-mock-test.html', 'newfoundland-rules-of-the-road.html'],
  on: ['ontario-g1-practice-test.html', 'ontario-g1-mock-test.html', 'ontario-g1-rules-of-the-road.html'],
  bc: ['bc-class-7l-practice-test.html', 'bc-class-7l-mock-test.html', 'bc-rules-of-the-road.html'],
  ab: ['alberta-class-7-practice-test.html', 'alberta-class-7-mock-test.html', 'alberta-rules-of-the-road.html'],
  qc: ['quebec-class-5-practice-test.html', 'quebec-class-5-mock-test.html', 'quebec-rules-of-the-road.html'],
  mb: ['manitoba-class-5-practice-test.html', 'manitoba-class-5-mock-test.html', 'manitoba-rules-of-the-road.html']
};
for (const [prov, pages] of Object.entries(DRIVE)) {
  const Q = load(ROOT + '/js/driving/' + prov + '.js', 'CQ_DRIVE_Q');
  // rules questions read well without their sign image
  const pool = Q.filter(q => q.sec === 'rules' && q.en.q.endsWith('?') && new Set(q.en.a).size === 4);
  for (let i = 0; i < pages.length; i++) {
    out[pages[i]] = pool.slice(i * 3, i * 3 + 3).map(q => ({
      q: q.en.q, o: q.en.a, a: q.c,
      fr: { q: q.fr.q, o: q.fr.a }
    }));
  }
}
process.stdout.write(JSON.stringify(out));
"""


def from_js():
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
        fh.write(NODE)
        path = fh.name
    try:
        raw = subprocess.check_output(["node", path, ROOT], text=True)
    finally:
        os.unlink(path)
    return json.loads(raw)


def main():
    out = {}
    for p in INLINE_PAGES:
        items = from_inline(p)
        if items:
            out[p] = items
    for page, items in from_js().items():
        if items:
            out[page] = items
    json.dump(out, io.open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote tools/quiz_ld.json — %d pages, %d questions"
          % (len(out), sum(len(v) for v in out.values())))
    thin = [p for p, v in out.items() if len(v) < PER_PAGE]
    if thin:
        print("  (fewer than %d questions: %s)" % (PER_PAGE, ", ".join(thin)))


if __name__ == "__main__":
    main()
