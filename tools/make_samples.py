#!/usr/bin/env python3
"""
make_samples.py — turns /root/banks.json (dumped from the live pages by
/tmp/dumpbanks.js in a headless browser) into tools/samples.json:
five real questions per quiz page, with the correct answer and explanation,
spread across that page's categories.

Every one of these strings is already a key in the French dictionary,
so printing them as static text costs nothing in translation work.
"""
import io, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANKS = sys.argv[1] if len(sys.argv) > 1 else "/root/banks.json"
OUT = os.path.join(ROOT, "tools", "samples.json")
N = 5

def norm(it):
    """Return {q, a, e} from any of the four question shapes used on the site."""
    q = it.get("q") or it.get("question")
    opts = it.get("o") or it.get("options")
    ai = it.get("a") if "a" in it else it.get("answer")
    e = it.get("e") or it.get("explain") or ""
    if q is None or not opts or ai is None:
        return None
    try:
        a = opts[int(ai)]
    except Exception:
        return None
    return {"q": q, "a": a, "e": e}

def pick(items, n):
    """Deterministic spread across the list."""
    items = [x for x in items if x]
    if len(items) <= n:
        return items
    step = len(items) / float(n)
    return [items[int(i * step)] for i in range(n)]

def main():
    banks = json.load(io.open(BANKS, encoding="utf-8"))
    out = {}
    for page, data in sorted(banks.items()):
        chosen = []
        if "GK_BANK" in data:
            cats = list(data["GK_BANK"].items())
            per = max(1, N // max(1, len(cats)))
            flat = []
            for name, c in cats:
                for lvl in ("easy", "medium", "hard"):
                    flat.extend(c.get(lvl, []))
            chosen = pick([norm(x) for x in flat], N)
        elif "BANK" in data:
            cats = list(data["BANK"].items())
            # one question from each of the first N categories, then top up
            for name, c in cats[:N]:
                qs = c.get("q") if isinstance(c, dict) else c
                if isinstance(qs, list) and qs:
                    v = norm(qs[len(qs) // 2])
                    if v:
                        chosen.append(v)
            if len(chosen) < N:
                flat = []
                for name, c in cats:
                    qs = c.get("q") if isinstance(c, dict) else c
                    if isinstance(qs, list):
                        flat.extend(qs)
                for v in pick([norm(x) for x in flat], N * 2):
                    if v and v["q"] not in [c["q"] for c in chosen]:
                        chosen.append(v)
                    if len(chosen) >= N:
                        break
        else:
            for key in ("FUN_QUESTIONS", "TRIVIA", "QUESTIONS"):
                if key in data:
                    chosen = pick([norm(x) for x in data[key]], N)
                    break
        chosen = [c for c in chosen if c][:N]
        if chosen:
            out[page] = chosen

    json.dump(out, io.open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)
    for p, v in sorted(out.items()):
        print("%-26s %d samples  (%d with explanation)"
              % (p, len(v), sum(1 for x in v if x["e"])))

if __name__ == "__main__":
    main()
