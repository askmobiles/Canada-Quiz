#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fixes the general-knowledge question counts, which contradicted each other.

WHAT WAS WRONG
--------------
gk-quiz.html showed three different totals on one page:

    meta description + JSON-LD  "855 questions"
    intro paragraph             "Nine subjects, three levels, 855 questions"
    crawlable bank heading      "All 1080 general knowledge questions"
    About section               "the largest quiz on the site: 405 questions"

WHAT IS ACTUALLY TRUE — counted, not assumed
--------------------------------------------
Two different things were being given one name.

  * ``js/gk-questions.js`` holds **405** questions: 9 subjects x 3 levels x 15,
    all unique. That is what the interactive quiz can serve.
  * The printed bank on the page holds **1,080 blocks / 1,078 unique
    questions** — two are printed twice. Of those, **673 are readable but
    cannot be played**, because they are not in the JavaScript bank and carry
    no difficulty level.

So 855 was never right. 1,080 counted the duplicates. 405 was right about the
quiz and wrong as a page total.

WHAT THIS SCRIPT DOES
---------------------
  1. Removes the two duplicated questions from the printed bank, keeping the
     first appearance of each. Duplicate content on one page helps nobody.
  2. Recomputes each subject's "N questions" label from what is actually there
     rather than trusting the hard-coded 120.
  3. Rewrites every count on the page so the two numbers are named for what
     they are: the quiz plays 405 levelled questions, the written bank runs to
     1,078.

The honest fix is NOT to pick one number. It is to stop using one word for two
things.

STILL OPEN, and worth more than this fix: 673 questions are on the page but
unplayable. Rebuilding the playable bank needs a difficulty level for each of
them, and the printed HTML carries no level — the bank is grouped by subject
only. That data would have to come from wherever the 1,080 were generated.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(ROOT, "gk-quiz.html")

PLAYABLE = 405     # js/gk-questions.js — verified by counting


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).strip()


def main():
    txt = io.open(P, encoding="utf-8").read()

    # ---- 1. drop duplicated questions, keeping the first of each -----------
    seen = set()
    removed = []

    def drop(m):
        block = m.group(0)
        qm = re.search(r'class="qb-q"[^>]*>(.*?)</p>', block, re.S)
        if not qm:
            return block
        q = strip_tags(qm.group(1))
        if q in seen:
            removed.append(q)
            return ""
        seen.add(q)
        return block

    txt = re.sub(r'<li class="qb-item">.*?</li>\n(?=<li class="qb-item">|</ol>)',
                 drop, txt, flags=re.S)
    print("removed %d duplicate question(s):" % len(removed))
    for q in removed:
        print("   %s" % q[:70])

    # ---- 2. recount each subject from what is now present ------------------
    def relabel(m):
        head, body = m.group(1), m.group(2)
        n = len(re.findall(r'class="qb-q"', body))
        head = re.sub(r'(<span class="qb-acc-n">)\d+( questions?</span>)',
                      lambda mm: "%s%d%s" % (mm.group(1), n, mm.group(2)), head)
        return head + body

    txt = re.sub(r'(<summary>.*?</summary>\n)(<ol class="qb">.*?</ol>)',
                 relabel, txt, flags=re.S)

    total = len(re.findall(r'class="qb-q"', txt))
    print("printed bank now holds %d questions" % total)

    # ---- 3. rewrite every count --------------------------------------------
    edits = [
        # meta description
        ('content="Free general knowledge quiz with 855 questions in three levels: '
         'easy for kids, medium, and hard for adults."',
         'content="Free general knowledge quiz in three levels: easy for kids, medium, '
         'and hard for adults. %d questions written out in full with every answer '
         'explained."' % total),
        # the same sentence inside the JSON-LD graph
        ('"description":"Free general knowledge quiz with 855 questions in three levels: '
         'easy for kids, medium, and hard for adults."',
         '"description":"Free general knowledge quiz in three levels: easy for kids, '
         'medium, and hard for adults. %d questions written out in full with every '
         'answer explained."' % total),
        # intro paragraph
        ("Nine subjects, three levels, 855 questions.",
         T("Nine subjects, three levels.",
           "Neuf sujets, trois niveaux.")),
        # crawlable bank heading
        ("<h2>All 1080 general knowledge questions, with every answer explained</h2>",
         "<h2>%s</h2>" % T(
             "All %d general knowledge questions, with every answer explained" % total,
             "Les %d questions de culture g&eacute;n&eacute;rale, avec chaque r&eacute;ponse "
             "expliqu&eacute;e" % total)),
        # About — name the two numbers for what they are
        ("The General Knowledge Quiz is the largest quiz on the site: 405 questions "
         "arranged into nine subjects and three difficulty levels. You choose a level "
         "first, then a subject, and answer ten questions with a short explanation after "
         "each one.",
         T("The General Knowledge Quiz is the largest quiz on the site. You choose a "
           "level first, then a subject, and answer ten questions with a short "
           "explanation after each one. The quiz draws on %d questions sorted into nine "
           "subjects and three difficulty levels, and the written bank further down this "
           "page runs to %d." % (PLAYABLE, total),
           "Le questionnaire de culture g&eacute;n&eacute;rale est le plus vaste du site. "
           "Vous choisissez d'abord un niveau, puis un sujet, et r&eacute;pondez &agrave; "
           "dix questions suivies d'une courte explication. Le questionnaire puise dans "
           "%d questions r&eacute;parties en neuf sujets et trois niveaux de "
           "difficult&eacute;, et la banque &eacute;crite plus bas sur cette page en "
           "compte %d." % (PLAYABLE, total))),
        # About — the bullet that explained the arithmetic
        ("Every subject holds fifteen questions at each of the three levels, which is how "
         "the total reaches 405.",
         T("Every subject holds fifteen questions at each of the three levels, which is "
           "how the quiz reaches %d. The written bank below is larger again." % PLAYABLE,
           "Chaque sujet compte quinze questions &agrave; chacun des trois niveaux, ce "
           "qui porte le questionnaire &agrave; %d. La banque &eacute;crite ci-dessous "
           "est encore plus vaste." % PLAYABLE)),
    ]

    for old, new in edits:
        if old not in txt:
            if new in txt:
                print("  already done, skipped: %s..." % old[:55])
                continue
            sys.exit("NOT FOUND:\n  %r" % old[:110])
        if txt.count(old) != 1:
            sys.exit("NOT UNIQUE (%d): %r" % (txt.count(old), old[:80]))
        txt = txt.replace(old, new)
        io.open(P, "w", encoding="utf-8").write(txt)   # write after EVERY hit
        print("  fixed: %s..." % old[:55])

    print("\n855 -> gone. 1080 -> %d. 405 kept, but now named as the playable set."
          % total)
    flush_pairs()


if __name__ == "__main__":
    main()
