# tools/newq — the province build and French audit tools

These used to live outside the repository, in `/root/newq/`. That folder does
not survive a fresh cloud container, so on 15, 16 and 17 August three scheduled
build nights had to be skipped: the site source could be cloned from GitHub, but
the tools that build a province could not. Worse, on 20 August a full rebuild
without them silently turned twenty-four French driving pages back into English,
because the step that writes the French question bank was one of the missing
files.

They are in the repository now. Nothing in here is secret and nothing in here is
large.

## What each file does

| File | Why it exists |
|---|---|
| `guide_data.py` | The verified facts for all thirteen jurisdictions — what each government publishes about its written test, and, just as important, what it does not. Read this before writing a single question. |
| `build_prov.py` | Builds one province's four English pages from a JSON content file, registers every hand-written string with its French, and does all six registrations (site map, page content, landing card, Quiz JSON-LD, internal linking). |
| `prov/<code>.json` | One jurisdiction's page copy, every string as an `{en, fr}` pair. The French is written beside the English so it cannot drift. |
| `qbank.py` | Renders the printed `<!--QBANK-->` block from a bank, in either language. Byte-for-byte identical to what the eight earlier provinces already carried — that was verified against the live pages before this module was trusted. |
| `fr_qbank.py` | **Run this after `build_fr.py`, every time.** It writes the question bank into every driving page, English and French. Without it the French pages ship in English. |
| `build_diary.py --fr` | **Run this after `build_fr.py`, every time, for the same reason.** A diary note's French lives beside its English in `diary_data.json`, not in the dictionary, so `build_fr.py` overwrites `fr/canada-diary.html` with 149 English notes. This happened on 24 August 2026, in a build that followed this README exactly as it was then written, and was caught only by `frbody.py`. |
| `artlib.py` | The long-article builder — `Article`, `T(en, fr)`, `bar_chart`, `table`. Every visible string is written as an (English, French) pair through `T()`, which registers the pair into `tools/extra_fr.json` in the same run, so a long article's French twin cannot drift. |
| `dumpbank.js` | Dumps one bank as JSON so the Python tools never have to parse JavaScript. |
| `prov_card.py` | Puts a province's card into the grid on `driving-test.html`. It deletes the "Coming soon" placeholder itself and refuses to finish if the province ends up listed twice — which is exactly what went wrong with Saskatchewan. |
| `build_index.py` | Keeps `all-pages.html` honest: the page count, the question count and the driving list. |
| `frsafe.py` | Refuses a page that bolds part of a sentence, because `build_fr.py` translates one text node at a time and such a sentence can never be looked up. |
| `fr_gap.py` | English left in a French page's headline slots — title, description, H1, hero, card headings. Must be 0 new. |
| `frbody.py` | English sentences anywhere in a French `<main>`. Must be 0. |
| `province_audit.py` | No driving page may describe another province's rules. A Quebec page once carried British Columbia's pass mark, live. |

## Adding a province or territory

1. Research it from official sources only, and write down what the government
   does **not** publish. That list is as important as the facts.
2. Write `js/driving/<code>.js`: the bilingual bank plus `window.CQ_PROVINCE`.
   Leave `CQ_PROVINCE` out and the pages load and render nothing.
3. Write `tools/newq/prov/<code>.json`, copying the shape of `nl.json`.
4. `python3 tools/newq/build_prov.py tools/newq/prov/<code>.json`
5. Run the pipeline:

```
python3 tools/make_quiz_ld.py
python3 tools/build_content.py
python3 tools/make_dict.py
python3 tools/split_fr.py
python3 tools/rewrite_pages.py
python3 tools/build_fr.py
python3 tools/newq/fr_qbank.py          # NOT OPTIONAL
python3 tools/newq/build_diary.py --fr  # NOT OPTIONAL
python3 tools/newq/build_index.py
python3 tools/related_links.py
python3 tools/build_sitemap.py
python3 tools/build_sw.py
python3 tools/asset_ver.py
```

Both "NOT OPTIONAL" lines exist for the same reason. `build_fr.py` translates one text
node at a time through the dictionary, and both the driving question banks and the diary
notes carry their own French beside their English in a data file rather than in the
dictionary. Skip either line and that content silently reverts to English on the French
pages, with nothing failing and nothing warning you.

6. Verify:

```
python3 tools/newq/fr_gap.py
python3 tools/newq/frbody.py            # MUST be 0 — this is the check that catches it
python3 tools/newq/province_audit.py
python3 tools/newq/fr_qbank.py --check
python3 tools/newq/build_diary.py --check
```

Then play the quiz through in English and in French, and run axe-core at both
1350×940 and 412×900. A layout that changes with screen size can change its
accessibility with it.

## The rule that matters more than any of this

These pages tell newcomers how a government test works. **Never publish a
figure no official source supports.** Where a government publishes nothing, say
so on the page. Six of the thirteen publish no question count at all, and
several commercial sites state one anyway without citing anybody. Not being one
of those sites is the whole reason this site is worth reading.
