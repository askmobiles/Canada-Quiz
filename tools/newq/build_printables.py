#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds printable-quizzes.html — worksheet sheets teachers and parents can print.

WHY THIS PAGE EXISTS
--------------------
Search Console, 3 months to 29 Aug 2026: 15 clicks, 1,460 impressions, average
position 43.5, and almost no inbound links. The measured blocker is not thin
content (games repeat 0.1% of their sentences, quizzes 2.7%) — it is that
nobody has linked to the site.

Teachers and librarians link to free printables. A worksheet that needs no
account, no email and carries no watermark is genuinely uncommon; most
printable-worksheet sites gate it or sell it. This page is built to be the kind
of thing a school board resource list or a settlement agency links to.

It also satisfies the owner's own rule (29 Aug 2026): it is a TOOL, not simple
information. A worksheet cannot be answered in a search snippet.

HOW IT WORKS
------------
No PDF library and no server. The browser's own print dialog does the work, and
"Save as PDF" is a print destination on every modern browser. The page reuses
the three question banks already on the site:

    js/fun-questions.js          225 Canada questions
    js/citizenship-questions.js  319 citizenship practice questions
    js/gk-questions.js           405 general knowledge (9 subjects x 3 levels)

FRENCH — WHY IT WORKS FOR FREE
------------------------------
site.js loads its French chunks by looking at which question scripts a page
carries (see loadFrench(), js/site.js), and a MutationObserver translates any
node added to the DOM afterwards. Because this page includes all three banks,
the French build automatically fetches the gk, cit and fun chunks and
translates each generated worksheet as it appears. No new dictionary work is
needed for the questions — only for this page's own UI text, registered below
through T().

PRINT RULES
-----------
  * the answer key always starts on a new sheet of paper, so a teacher can
    photocopy the questions without copying the answers
  * header, navigation, footer, controls and ads are hidden when printing
  * no background colours — they waste toner and many school printers drop them
  * the site name and the unofficial notice stay on the sheet, so a photocopy
    handed to thirty children still says where it came from
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "printable-quizzes.html"

TITLE = "Printable Quiz Sheets — Free Canada Worksheets with Answer Key"
DESC = ("Free printable quiz worksheets about Canada, citizenship practice and general "
        "knowledge. Choose a topic, print or save as PDF, answer key included. No signup.")

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" href="brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="brand/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#c8102e">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Canada Quiz">
<meta name="google-adsense-account" content="ca-pub-7256851069341390">
<link rel="canonical" href="https://canada-quiz.com/printable-quizzes.html">
<link rel="alternate" hreflang="en" href="https://canada-quiz.com/printable-quizzes.html">
<link rel="alternate" hreflang="fr" href="https://canada-quiz.com/fr/printable-quizzes.html">
<link rel="alternate" hreflang="x-default" href="https://canada-quiz.com/printable-quizzes.html">
<style>
/* ---- on screen ---- */
.pw-controls{display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;
  background:#fff;border:1px solid #e6e1d8;border-radius:14px;padding:16px 18px;margin:18px 0}
.pw-field{display:flex;flex-direction:column;gap:5px}
.pw-field label{font-size:13px;font-weight:800;color:#5f6b7a}
.pw-field select{font:inherit;padding:9px 12px;border:2px solid #ded7cc;border-radius:10px;
  background:#fff;min-width:190px}
.pw-sheet{background:#fff;border:1px solid #e6e1d8;border-radius:14px;padding:26px 28px;margin-top:18px}
.pw-head{border-bottom:2px solid #2b2d42;padding-bottom:10px;margin-bottom:6px}
.pw-head h2{margin:0 0 4px;font-size:22px}
.pw-meta{display:flex;gap:26px;flex-wrap:wrap;font-size:14px;color:#2b2d42;margin:14px 0 4px}
.pw-q{margin:0 0 18px;break-inside:avoid;page-break-inside:avoid}
.pw-q p{margin:0 0 7px;font-weight:700}
.pw-opts{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:5px 18px}
.pw-opts li{font-size:15px}
.pw-key{margin-top:26px;border-top:2px solid #2b2d42;padding-top:14px}
.pw-key ol{padding-left:22px}
.pw-key li{margin-bottom:9px;font-size:14.5px}
.pw-note{font-size:12.5px;color:#5f6b7a;margin-top:20px;border-top:1px solid #e6e1d8;padding-top:10px}
@media (max-width:620px){.pw-opts{grid-template-columns:1fr}}

/* ---- on paper ---- */
@page{margin:16mm 14mm}
@media print{
  .site-header,.site-footer,.pw-controls,.pw-screen-only,.adbox,.ad-slot,
  .breadcrumbs,.pd-rel,nav{display:none!important}
  body{background:#fff!important;color:#000!important;font-size:12pt}
  main.container{max-width:none;padding:0;margin:0}
  .pw-sheet{border:0;border-radius:0;padding:0;margin:0;background:#fff!important;
    box-shadow:none!important}
  .pw-head h2{font-size:17pt}
  .pw-q{margin-bottom:15pt}
  .pw-opts li{font-size:11.5pt}
  /* the answer key always starts on its own sheet, so the questions can be
     photocopied without the answers */
  .pw-key{page-break-before:always;break-before:page;border-top:0;margin-top:0;padding-top:0}
  a[href]:after{content:""}
}
</style>
</head>
<body>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Canada Quiz &amp; Family Fun Games"><img src="brand/logo-horizontal-white.svg" alt="Canada Quiz &amp; Family Fun Games" class="brand-logo" width="230" height="55"></a>
    <nav class="nav" aria-label="Main navigation">
      <a href="index.html">Home</a>
      <a href="quizzes.html">Quizzes</a>
      <a href="games.html">Family Games</a>
      <a href="for-kids.html">For Kids</a>
      <a href="citizenship.html">Citizenship</a>
      <a href="driving-test.html">Driving Test</a>
      <a href="daily.html">Daily</a>
      <a href="blog.html">Blog</a>
      <button type="button" class="lang-btn" data-no-i18n data-set-lang="fr" aria-label="Passer en fran&ccedil;ais" title="Passer en fran&ccedil;ais"><span aria-hidden="true">&#127760;</span> FR</button>
    </nav>
  </div>
</header>

<main class="container">
''' % {"title": TITLE, "desc": DESC}

FOOT = '''</main>

<footer class="site-footer">
  <div class="container center">
    <img src="brand/logo-horizontal-white.svg" alt="Canada Quiz &amp; Family Fun Games" class="footer-logo" width="200" height="48">
    <p>Free quizzes, family games and citizenship practice &mdash; no signup, no ads in your face.</p>
    <div class="footer-links"><a href="index.html">Home</a> &middot; <a href="about.html">About</a> &middot; <a href="contact.html">Contact</a> &middot; <a href="sources.html">Sources</a> &middot; <a href="privacy.html">Privacy Policy</a> &middot; <a href="terms.html">Terms &amp; Conditions</a></div>
    <p class="footer-all"><a href="all-pages.html">Every page on the site</a></p>
    <p class="muted" style="color:#b4a9cc;font-size:12px">&copy; 2026 Canada Quiz &amp; Family Fun Games. All rights reserved.</p>
    <p class="muted" style="color:#b4a9cc;font-size:12.5px">Unofficial practice site. Not affiliated with the Government of Canada.</p>
  </div>
</footer>

<script src="js/fun-questions.js"></script>
<script src="js/citizenship-questions.js"></script>
<script src="js/gk-questions.js"></script>
<script src="js/printables.js"></script>
<script src="js/site.js"></script>
</body>
</html>
'''


def body():
    o = []
    a = o.append
    # Everything from the breadcrumb to the last intro line is screen-only. A
    # teacher photocopying a worksheet does not want the site's own heading and
    # instructions across the top of it — the sheet has to look like a sheet.
    a('    <div class="pw-screen-only">')
    a('    <p class="muted" style="margin:0 0 4px"><a href="quizzes.html">%s</a></p>'
      % T("&larr; Quizzes", "&larr; Questionnaires"))
    a('    <h1 style="margin:.2em 0 .3em">%s</h1>'
      % T("&#128462; Printable quiz sheets", "&#128462; Feuilles de questionnaire &agrave; imprimer"))
    a('    <p class="muted" style="font-size:15px;margin:0 0 6px">%s</p>' % T(
        "Pick a topic, choose how many questions, and print. The answer key prints on "
        "its own page so you can photocopy the questions on their own.",
        "Choisissez un sujet et un nombre de questions, puis imprimez. Le corrig&eacute; "
        "s'imprime sur une page distincte, ce qui permet de photocopier les questions "
        "seules."))
    a('    <p class="muted" style="font-size:13px;margin:0 0 18px">%s</p>' % T(
        "Free to use and to photocopy. No account, no email address, no watermark.",
        "Libre d'utilisation et de photocopie. Aucun compte, aucune adresse courriel, "
        "aucun filigrane."))
    a('    </div>')

    # ---- controls
    a('    <div class="pw-controls pw-screen-only">')
    a('      <div class="pw-field"><label for="pw-topic">%s</label>'
      % T("Topic", "Sujet"))
    a('        <select id="pw-topic"></select></div>')
    a('      <div class="pw-field"><label for="pw-level">%s</label>'
      % T("Level", "Niveau"))
    a('        <select id="pw-level"></select></div>')
    a('      <div class="pw-field"><label for="pw-count">%s</label>'
      % T("Questions", "Nombre de questions"))
    a('        <select id="pw-count">'
      '<option value="10">10</option><option value="15" selected>15</option>'
      '<option value="20">20</option><option value="25">25</option></select></div>')
    a('      <div class="pw-field"><button type="button" class="btn btn-lg" id="pw-make">%s</button></div>'
      % T("Make the sheet", "Cr&eacute;er la feuille"))
    a('      <div class="pw-field"><button type="button" class="btn btn-lg btn-ghost" id="pw-print">%s</button></div>'
      % T("Print", "Imprimer"))
    a('    </div>')

    a('    <div id="pw-out" aria-live="polite"></div>')

    # ---- for teachers
    a('    <div class="pw-screen-only">')
    a('    <h2>%s</h2>' % T("For teachers and tutors", "Pour le personnel enseignant et les tuteurs"))
    a('    <p>%s</p>' % T(
        "Every sheet is free to photocopy for a class. There is nothing to sign up for and "
        "nothing to pay, and no student ever needs an account, so no child's information is "
        "collected by this site at any point.",
        "Chaque feuille peut &ecirc;tre photocopi&eacute;e librement pour une classe. Il n'y "
        "a rien &agrave; cr&eacute;er comme compte ni rien &agrave; payer, et aucun &eacute;l&egrave;ve "
        "n'a besoin d'un compte : aucune information concernant un enfant n'est recueillie "
        "par ce site."))
    a('    <p>%s</p>' % T(
        "Pressing Print opens your browser's normal print window. Choosing &#8220;Save as "
        "PDF&#8221; as the destination gives you a file you can email or upload instead of "
        "printing on paper.",
        "Le bouton Imprimer ouvre la fen&ecirc;tre d'impression habituelle de votre "
        "navigateur. En choisissant &#171; Enregistrer au format PDF &#187; comme "
        "destination, vous obtenez un fichier &agrave; envoyer par courriel ou &agrave; "
        "d&eacute;poser en ligne plut&ocirc;t qu'une impression papier."))
    a('    <p>%s</p>' % T(
        "Each sheet is drawn fresh from the question banks, so pressing the button again "
        "gives a different set. That makes it easy to produce two versions of the same test, "
        "or a new one next term.",
        "Chaque feuille est tir&eacute;e au hasard des banques de questions : appuyer de "
        "nouveau sur le bouton donne un ensemble diff&eacute;rent. Il est donc facile de "
        "produire deux versions d'un m&ecirc;me test, ou une nouvelle feuille au trimestre "
        "suivant."))
    a('    <h2>%s</h2>' % T("What is on the sheets", "Ce que contiennent les feuilles"))
    a('    <ul><li>%s</li><li>%s</li><li>%s</li></ul>' % (
        T("<strong>Canada</strong> &mdash; food, hockey, animals, provinces, symbols and "
          "everyday facts about the country",
          "<strong>Canada</strong> &mdash; cuisine, hockey, animaux, provinces, "
          "symboles et faits du quotidien sur le pays"),
        T("<strong>Citizenship practice</strong> &mdash; questions in the style of the real "
          "test, written from the official guide <em>Discover Canada</em>, 2012 edition",
          "<strong>Pr&eacute;paration &agrave; la citoyennet&eacute;</strong> &mdash; des "
          "questions dans l'esprit du vrai examen, r&eacute;dig&eacute;es &agrave; partir "
          "du guide officiel <em>Discover Canada</em>, &eacute;dition de 2012"),
        T("<strong>General knowledge</strong> &mdash; geography, science, animals, history, "
          "sport, maths and more, at three levels",
          "<strong>Culture g&eacute;n&eacute;rale</strong> &mdash; g&eacute;ographie, "
          "sciences, animaux, histoire, sport, math&eacute;matiques et plus, &agrave; "
          "trois niveaux")))
    a('    <div class="disclaimer"><strong>%s</strong> %s</div>' % (
        T("Please note:", "&Agrave; noter :"),
        T("The citizenship sheets are practice only. This site is unofficial and is not "
          "affiliated with the Government of Canada. Always study the official "
          "<em>Discover Canada</em> guide for the real test.",
          "Les feuilles sur la citoyennet&eacute; servent uniquement &agrave; s'exercer. Ce "
          "site n'est pas officiel et n'a aucun lien avec le gouvernement du Canada. "
          "&Eacute;tudiez toujours le guide officiel <em>Discover Canada</em> pour le vrai "
          "examen.")))
    a('    </div>')
    return "\n".join(o) + "\n"


def js_strings():
    """Strings that only ever appear through js/printables.js.

    They never reach the HTML, so T() would not see them. Registering them here
    puts them in tools/extra_fr.json, which make_dict.py compiles into the
    runtime dictionary — and site.js's MutationObserver then translates each
    generated sheet on the French page. The return value is deliberately thrown
    away; the side effect on the dictionary is the point."""
    T("All levels", "Tous les niveaux")
    T("Easy", "Facile")
    T("Medium", "Moyen")
    T("Hard", "Difficile")
    T("Canada", "Canada")
    T("Citizenship practice", "Pr&eacute;paration &agrave; la citoyennet&eacute;")
    T("Printable quiz sheet from canada-quiz.com",
      "Feuille de questionnaire &agrave; imprimer, de canada-quiz.com")
    T("Name:", "Nom :")
    T("Date:", "Date :")
    T("Score:", "R&eacute;sultat :")
    T("Answer key", "Corrig&eacute;")
    T("canada-quiz.com — free to use and photocopy. Unofficial practice. "
      "Not affiliated with the Government of Canada.",
      "canada-quiz.com — libre d'utilisation et de photocopie. Exercice non officiel. "
      "Aucun lien avec le gouvernement du Canada.")


def main():
    io.open(os.path.join(ROOT, SLUG), "w", encoding="utf-8").write(HEAD + body() + FOOT)
    print("wrote %s" % SLUG)
    js_strings()
    flush_pairs()


if __name__ == "__main__":
    main()
