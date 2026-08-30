#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuilds which-canadian-city-quiz.html — the best-ranking page on the site.

WHY THIS PAGE AND NOT ANOTHER
-----------------------------
Search Console, three months to 29 Aug 2026: this page sat at average position
**11.5 with a 50% click-through rate** — by far the best on the site — on
**475 words**. It is the one page that is already close to page one, and it was
the thinnest thing we had. Everything here follows from that: keep the exact
phrase that is ranking, and give the page enough substance to deserve the click.

WHAT CHANGED
------------
  * 7 cities -> **13**, one from every region including the North. The extra
    six are also the ones nobody else builds pages for.
  * 7 questions -> **10**, adding language, size of place, and water.
  * The result now carries **real figures** for the city you land on:
    population, average two-bedroom rent, vacancy rate, and how you get around.
  * A **comparison table of all thirteen** — crawlable, and the thing a person
    actually wants after they get a result.
  * An **explanatory section**: what rent really differs by, what a vacancy
    rate tells you that a rent does not, and the documented shift in where
    newcomers are settling. That last one is the most distinctive thing on the
    page; no competing quiz has it.

EVERY NUMBER IS SOURCED. See research/canadian-cities-facts-20260830.md in the
private project for the full working, including what could not be verified.

  * Population — Statistics Canada, estimate for 1 July 2025, Table
    17-10-0148-01, released 14 January 2026.
  * Rent and vacancy — CMHC Rental Market Report, Fall 2025, released
    11 December 2025, from the October 2025 survey. ONE survey for all of
    them. National figures: 3.1% vacancy, $1,550 average two-bedroom.
  * Settlement shift — Statistics Canada, The Daily, 14 January 2026.

TWO HONEST GAPS, BOTH DELIBERATE
--------------------------------
1. **Halifax has no two-bedroom rent figure.** CMHC's published tables gave
   more than one value for it in the same survey. The page says so in one
   sentence instead of printing a number we cannot stand behind. Halifax's
   vacancy rate is published, because that one is clean.
2. **There are no temperature or snowfall numbers anywhere on this page.**
   Environment and Climate Change Canada's 1991-2020 normals could not be
   reached from the build environment (the data pages redirect non-browser
   clients, the bulk files are robots-blocked, and the cached encyclopaedia
   copies here are stale and unit-garbled). Winter is therefore described in
   words that are true without a figure. Do not let anyone "helpfully" fill
   those numbers in from memory later.

Whitehorse is a census agglomeration, not a CMA, and is not a CMHC featured
centre, so its row carries a city population and no rent. That is stated.

THIS SCRIPT OWNS THE PAGEDOC BLOCK ON THIS PAGE
-----------------------------------------------
`tools/build_content.py` writes the <!--PAGEDOC--> block on most pages from
`tools/page_content.json`, and it runs early in the pipeline. This page's entry
has therefore been **deleted from page_content.json**: the block here carries a
table, an id, source links and section headings that that file's schema cannot
express, and if the entry came back, the next build would quietly replace a
thousand words with the old three hundred. If you ever see the short "Seven
practical questions" text return to this page, that is what happened.

RUN
---
    python3 tools/newq/build_citypick.py            # rebuild the page
    python3 tools/newq/build_citypick.py --sim      # scoring balance only

then the normal pipeline: make_dict.py, build_fr.py, fr_qbank.py,
build_diary.py --fr, asset_ver.py, split_fr.py.
"""
import io
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import T, flush_pairs, e

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGE = os.path.join(ROOT, "which-canadian-city-quiz.html")

# --------------------------------------------------------------------------
# THE THIRTEEN
# --------------------------------------------------------------------------
# ne/nf  name in each language
# de/df  the character of the place, in one honest sentence
# pop    Statistics Canada estimate, 1 July 2025 (Whitehorse: 2021 Census city)
# rent   CMHC average two-bedroom, October 2025 survey. None = not published.
# vac    CMHC vacancy rate, same survey. None = not surveyed.
# tre/trf  how you get around, today
CITIES = [
    ("toronto", "🏙️", "Toronto", "Toronto",
     "You want everything within reach and you accept the crowd that comes with "
     "it. Something is always open, something is always on, and you will pay for "
     "the privilege of being in the middle of it.",
     "Vous voulez tout à portée de main et vous acceptez la foule qui vient avec. "
     "Il y a toujours quelque chose d'ouvert, toujours quelque chose à faire, et vous "
     "paierez pour être au cœur de tout cela.",
     "7,108,874", "7 108 874", "$2,034", "2 034 $", "3.0%", "3,0 %",
     "Subway and two new light rail lines",
     "Métro et deux nouvelles lignes de train léger"),

    ("montreal", "🥐", "Montreal", "Montréal",
     "Old streets, a festival most weekends, and rent that is low for a city of "
     "four and a half million. You want a place with style and noise, and you do "
     "not mind switching languages mid-sentence.",
     "Des rues anciennes, un festival presque chaque fin de semaine, et un loyer "
     "bas pour une ville de quatre millions et demi d'habitants. Vous voulez un "
     "endroit avec du style et du bruit, et changer de langue en pleine phrase ne "
     "vous dérange pas.",
     "4,597,837", "4 597 837", "$1,346", "1 346 $", "2.9%", "2,9 %",
     "Métro and the REM light rail",
     "Métro et le REM"),

    ("vancouver", "🏔️", "Vancouver", "Vancouver",
     "Mountains on one side, ocean on the other, rain in between, and the highest "
     "rent in the country. You will trade a great deal for a mild winter and a "
     "trail that starts where the bus stops.",
     "Les montagnes d'un côté, l'océan de l'autre, la pluie entre les deux, et le "
     "loyer le plus élevé au pays. Vous échangeriez beaucoup contre un hiver doux "
     "et un sentier qui commence au terminus d'autobus.",
     "3,088,036", "3 088 036", "$2,363", "2 363 $", "3.7%", "3,7 %",
     "SkyTrain", "SkyTrain"),

    ("calgary", "🤠", "Calgary", "Calgary",
     "Wide streets, big sky, cold that is dry and bright rather than damp, and "
     "the Rockies a little over an hour away. It also has the easiest rental "
     "market of any big Canadian city right now.",
     "Des rues larges, un grand ciel, un froid sec et lumineux plutôt qu'humide, "
     "et les Rocheuses à un peu plus d'une heure. C'est aussi le marché locatif le "
     "plus facile des grandes villes canadiennes en ce moment.",
     "1,836,012", "1 836 012", "$1,914", "1 914 $", "5.0%", "5,0 %",
     "CTrain light rail", "Train léger CTrain"),

    ("ottawa", "🍁", "Ottawa", "Ottawa",
     "A capital that behaves like a mid-size city: a canal you skate on, real "
     "winter, both official languages in ordinary use, and a share of new "
     "arrivals that has doubled in five years.",
     "Une capitale qui se comporte comme une ville de taille moyenne : un canal "
     "où l'on patine, un vrai hiver, les deux langues officielles d'usage courant, "
     "et une part de nouveaux arrivants qui a doublé en cinq ans.",
     "1,700,014", "1 700 014", "$1,926", "1 926 $", "3.0%", "3,0 %",
     "O-Train light rail", "Train léger O-Train"),

    ("edmonton", "🎭", "Edmonton", "Edmonton",
     "The northernmost big city in Canada, built along a river valley you can "
     "disappear into, with a summer of back-to-back festivals and a winter that "
     "earns them. It is also the fastest-growing large city in the country.",
     "La plus nordique des grandes villes canadiennes, bâtie le long d'une vallée "
     "fluviale où l'on peut disparaître, avec un été de festivals sans relâche et un "
     "hiver qui les fait mériter. C'est aussi la grande ville qui croît le plus vite "
     "au pays.",
     "1,692,385", "1 692 385", "$1,603", "1 603 $", "3.8%", "3,8 %",
     "Light rail, with a west line being built",
     "Train léger, avec une ligne ouest en construction"),

    ("winnipeg", "🌾", "Winnipeg", "Winnipeg",
     "Real winters, real summers, and rent that runs almost a quarter below "
     "Toronto's. You value substance over shine and minus thirty does not "
     "frighten you.",
     "De vrais hivers, de vrais étés, et un loyer inférieur de près d'un quart à "
     "celui de Toronto. Vous préférez le solide au brillant et moins trente ne "
     "vous fait pas peur.",
     "951,758", "951 758", "$1,571", "1 571 $", "2.8%", "2,8 %",
     "Buses, with one rapid transit corridor",
     "Autobus, avec un corridor de transport rapide"),

    ("quebec", "⚜️", "Quebec City", "Québec",
     "The lowest rent of the thirteen cities here, inside the only "
     "walled city north of Mexico, in French, under a great deal of snow. A "
     "tramway is being built through the middle of it.",
     "Le loyer le plus bas des treize villes présentées ici, dans la seule "
     "ville fortifiée au nord du Mexique, en français, sous beaucoup de neige. Un "
     "tramway est en construction en plein centre.",
     "903,607", "903 607", "$1,276", "1 276 $", "2.4%", "2,4 %",
     "Buses; a tramway is under construction",
     "Autobus ; un tramway est en construction"),

    ("halifax", "⚓", "Halifax", "Halifax",
     "A harbour, a short walk to most of what you need, and a slower gear than "
     "anywhere bigger. You would rather know your neighbours than have a hundred "
     "restaurants to choose between.",
     "Un port, tout à distance de marche ou presque, et un rythme plus lent que "
     "partout ailleurs de plus grand. Vous préférez connaître vos voisins qu'avoir "
     "cent restaurants au choix.",
     "544,834", "544 834", None, None, "2.6%", "2,6 %",
     "Buses and harbour ferries", "Autobus et traversiers du port"),

    ("victoria", "🌷", "Victoria", "Victoria",
     "The mildest winter in Canada, gardens in February, an island between you "
     "and the rest of the country, and rent to match. Small, pretty, and further "
     "from everything than it looks on a map.",
     "L'hiver le plus doux du Canada, des jardins en février, une île entre vous et "
     "le reste du pays, et un loyer en conséquence. Petite, jolie, et plus loin de "
     "tout qu'il n'y paraît sur une carte.",
     "445,090", "445 090", "$2,120", "2 120 $", "3.3%", "3,3 %",
     "Buses only", "Autobus seulement"),

    ("saskatoon", "🌉", "Saskatoon", "Saskatoon",
     "A river through the middle of it, prairie in every direction, and a city "
     "small enough to cross in twenty minutes. Rent sits almost exactly at the "
     "national average, and rapid transit stations are going in.",
     "Une rivière en plein milieu, la prairie dans toutes les directions, et une "
     "ville assez petite pour la traverser en vingt minutes. Le loyer se situe "
     "presque exactement à la moyenne nationale, et des stations de transport "
     "rapide sont en chantier.",
     "378,475", "378 475", "$1,548", "1 548 $", "3.3%", "3,3 %",
     "Buses; rapid transit stations being built",
     "Autobus ; des stations de transport rapide en construction"),

    ("stjohns", "🎣", "St. John's", "Saint-Jean",
     "Coloured houses up a steep hill, weather that changes four times before "
     "lunch, and strangers who talk to you in the queue. It also has one of the "
     "tightest rental markets in the country, so start looking early.",
     "Des maisons colorées sur une côte raide, un temps qui change quatre fois "
     "avant midi, et des inconnus qui vous parlent dans la file. C'est aussi l'un des "
     "marchés locatifs les plus serrés du pays : commencez à chercher tôt.",
     "243,478", "243 478", "$1,348", "1 348 $", "2.1%", "2,1 %",
     "Buses only", "Autobus seulement"),

    ("whitehorse", "🐺", "Whitehorse", "Whitehorse",
     "Twenty-eight thousand people, mountains at the end of the street, daylight "
     "a June where it hardly gets dark and a December where it hardly gets light. "
     "You are not looking for a city at all.",
     "Vingt-huit mille habitants, des montagnes au bout de la rue, une lumière qui "
     "un juin où il ne fait presque pas nuit et un décembre où il ne fait presque "
     "pas jour. Ce n'est pas une ville que vous cherchez.",
     "28,201", "28 201", None, None, None, None,
     "Buses; most people drive", "Autobus ; la plupart des gens conduisent"),
]

KEYS = [c[0] for c in CITIES]

# --------------------------------------------------------------------------
# THE TEN QUESTIONS
# --------------------------------------------------------------------------
# Scores were not guessed. Run with --sim: 200,000 random play-throughs, and
# every one of the thirteen has to be reachable and none may run away with it.
QUESTIONS = [
    ("What kind of winter can you actually live with?",
     "Quel genre d'hiver pouvez-vous vraiment supporter ?", [
        ("Cold and snowy — that is what winter is",
         "Froid et neigeux — c'est ça, l'hiver",
         {"winnipeg": 3, "edmonton": 2, "ottawa": 2, "quebec": 1}),
        ("Grey and rainy, but mild",
         "Gris et pluvieux, mais doux",
         {"vancouver": 2, "victoria": 3}),
        ("Cold, but dry and bright",
         "Froid, mais sec et lumineux",
         {"calgary": 2, "saskatoon": 2, "whitehorse": 2}),
        ("Windy and wet, straight off the ocean",
         "Venteux et humide, droit de l'océan",
         {"stjohns": 3, "halifax": 2}),
     ]),

    ("How big should the place be?",
     "À quel point l'endroit doit-il être grand ?", [
        ("As big as it gets",
         "Aussi grand que possible",
         {"toronto": 3, "montreal": 1}),
        ("Big, but you can still cross it in half an hour",
         "Grand, mais traçable en une demi-heure",
         {"ottawa": 3, "edmonton": 2, "calgary": 2, "winnipeg": 2, "quebec": 1}),
        ("Small enough to keep running into people you know",
         "Assez petit pour croiser sans cesse des gens que vous connaissez",
         {"halifax": 2, "victoria": 2, "saskatoon": 2, "stjohns": 2}),
        ("Genuinely small, and that is the whole point",
         "Vraiment petit, et c'est tout l'intérêt",
         {"whitehorse": 3}),
     ]),

    ("How much does the rent decide?",
     "Le loyer décide-t-il de tout ?", [
        ("Everything. Cheapest wins",
         "De tout. Le moins cher gagne",
         {"quebec": 2, "montreal": 1, "saskatoon": 1, "stjohns": 1, "winnipeg": 1}),
        ("It matters, but so does the city",
         "Il compte, mais la ville aussi",
         {"montreal": 2, "winnipeg": 2, "edmonton": 1, "halifax": 1}),
        ("I will pay for the location",
         "Je paierai pour l'emplacement",
         {"toronto": 2, "vancouver": 3, "victoria": 1}),
        ("I would rather buy than rent",
         "Je préfère acheter que louer",
         {"calgary": 3, "edmonton": 2, "saskatoon": 1, "winnipeg": 1}),
     ]),

    ("Pick a way to get to work:",
     "Choisissez une façon d'aller au travail :", [
        ("Subway, métro or SkyTrain",
         "Métro ou SkyTrain",
         {"toronto": 2, "montreal": 2, "vancouver": 2}),
        ("Bike, most of the year",
         "À vélo, presque toute l'année",
         {"victoria": 2, "montreal": 1, "ottawa": 1, "saskatoon": 1}),
        ("Drive, and park without thinking about it",
         "En auto, et se garer sans y penser",
         {"calgary": 2, "saskatoon": 2, "winnipeg": 2, "edmonton": 1, "whitehorse": 1}),
        ("Walk it in twenty minutes",
         "À pied, en vingt minutes",
         {"halifax": 2, "stjohns": 2, "quebec": 1}),
     ]),

    ("How far away should real wilderness be?",
     "À quelle distance devrait se trouver la vraie nature ?", [
        ("About an hour by car",
         "À une heure de route environ",
         {"calgary": 2, "edmonton": 2, "ottawa": 2}),
        ("Where the bus route ends",
         "Là où la ligne d'autobus se termine",
         {"vancouver": 2, "whitehorse": 2}),
        ("A weekend away is fine",
         "Une fin de semaine, c'est correct",
         {"toronto": 2, "montreal": 1, "winnipeg": 1}),
        ("I would rather have the ocean at the end of the street",
         "Je préfère l'océan au bout de la rue",
         {"halifax": 2, "stjohns": 2, "victoria": 1}),
     ]),

    ("What do you want to hear around you?",
     "Qu'aimeriez-vous entendre autour de vous ?", [
        ("English, mostly",
         "De l'anglais, surtout",
         {"calgary": 1, "edmonton": 1, "winnipeg": 1, "saskatoon": 1,
          "halifax": 1, "stjohns": 1, "victoria": 1, "whitehorse": 1}),
        ("French, mostly",
         "Du français, surtout",
         {"quebec": 3}),
        ("Both, all day long",
         "Les deux, toute la journée",
         {"montreal": 3, "ottawa": 3}),
        ("Every language at once",
         "Toutes les langues à la fois",
         {"toronto": 2, "vancouver": 2}),
     ]),

    ("A stranger starts talking to you in the queue.",
     "Un inconnu vous adresse la parole dans la file.", [
        ("Wonderful. Tell me everything",
         "Merveilleux. Racontez-moi tout",
         {"stjohns": 2, "halifax": 1, "whitehorse": 1}),
        ("In a shop, fine. On the train, no",
         "Dans un magasin, d'accord. Dans le train, non",
         {"toronto": 1, "calgary": 1, "ottawa": 1, "vancouver": 1}),
        ("Only if we are both freezing",
         "Seulement si nous gelons tous les deux",
         {"winnipeg": 2, "saskatoon": 1, "edmonton": 2}),
        ("It depends which language they open with",
         "Ça dépend de la langue qu'il emploie",
         {"montreal": 2, "quebec": 2}),
     ]),

    ("Water, please. What kind?",
     "De l'eau, oui. Mais laquelle ?", [
        ("An ocean you can smell from the front door",
         "Un océan que l'on sent depuis le pas de la porte",
         {"halifax": 2, "stjohns": 2, "victoria": 2}),
        ("A river running through the middle of town",
         "Une rivière en plein milieu de la ville",
         {"saskatoon": 3, "edmonton": 2, "winnipeg": 2, "ottawa": 2}),
        ("A lake big enough to look like the sea",
         "Un lac assez grand pour ressembler à la mer",
         {"toronto": 2, "ottawa": 1, "quebec": 1}),
        ("Mountains will do, thank you",
         "Les montagnes feront l'affaire, merci",
         {"vancouver": 2, "calgary": 2, "whitehorse": 2}),
     ]),

    ("Your ideal Saturday:",
     "Votre samedi idéal :", [
        ("A gallery, then dinner somewhere new",
         "Une galerie, puis un souper dans un nouvel endroit",
         {"toronto": 2, "montreal": 2, "ottawa": 2}),
        ("On a trail before lunch",
         "Sur un sentier avant midi",
         {"vancouver": 2, "calgary": 1, "whitehorse": 2}),
        ("A market, a park, and no plans at all",
         "Un marché, un parc, et aucun plan",
         {"winnipeg": 1, "saskatoon": 1, "edmonton": 2, "quebec": 2}),
        ("A walk along the water and a pub after",
         "Une marche au bord de l'eau, puis un pub",
         {"halifax": 2, "stjohns": 1, "victoria": 1}),
     ]),

    ("What do you want more of?",
     "De quoi voulez-vous plus ?", [
        ("Choices",
         "De choix",
         {"toronto": 2, "montreal": 1}),
        ("Space",
         "D'espace",
         {"saskatoon": 3, "calgary": 1, "winnipeg": 1, "whitehorse": 2, "edmonton": 1}),
        ("Beauty out of the window",
         "De beauté par la fenêtre",
         {"vancouver": 2, "victoria": 2, "quebec": 2, "stjohns": 1}),
        ("Time",
         "De temps",
         {"halifax": 2, "winnipeg": 1, "edmonton": 1, "victoria": 1}),
     ]),
]


# --------------------------------------------------------------------------
def simulate(n=200000):
    """Every city must be reachable, and none may swallow the quiz.

    This is the check that scoring by hand always needs and rarely gets. A
    personality quiz where two of the thirteen answers are unreachable is
    broken, and nothing else in the pipeline would ever notice.
    """
    random.seed(7)
    wins = dict((k, 0) for k in KEYS)
    for _ in range(n):
        s = dict((k, 0.0) for k in KEYS)
        for _q, _qf, opts in QUESTIONS:
            _e, _f, sc = random.choice(opts)
            for k, v in sc.items():
                s[k] += v
        for k in KEYS:                      # same jitter the page uses
            s[k] += random.random() * 0.001
        wins[max(KEYS, key=lambda k: s[k])] += 1

    order = sorted(KEYS, key=lambda k: -wins[k])
    print("%d random play-throughs" % n)
    worst = None
    for k in order:
        pct = 100.0 * wins[k] / n
        print("  %-11s %6.2f%%  %s" % (k, pct, "#" * int(pct)))
        worst = pct
    print("\nhighest %.2f%%  lowest %.2f%%  (even split would be %.2f%%)"
          % (100.0 * wins[order[0]] / n, worst, 100.0 / len(KEYS)))
    dead = [k for k in KEYS if wins[k] == 0]
    if dead:
        sys.exit("UNREACHABLE RESULT(S): %s" % ", ".join(dead))
    return wins


# --------------------------------------------------------------------------
def js_payload():
    R = {}
    for (k, emoji, ne, nf, de, df, pop, popf, rent, rentf,
         vac, vacf, tre, trf) in CITIES:
        R[k] = {"e": emoji, "ne": ne, "nf": nf, "de": de, "df": df,
                "pe": pop, "pf": popf, "re": rent, "rf": rentf,
                "ve": vac, "vf": vacf, "te": tre, "tf": trf}
    Q = []
    for en, fr, opts in QUESTIONS:
        Q.append({"en": en, "fr": fr,
                  "a": [{"en": a, "fr": b, "s": s} for a, b, s in opts]})
    return (json.dumps(R, ensure_ascii=False, indent=1, sort_keys=False),
            json.dumps(Q, ensure_ascii=False, indent=1))


SCRIPT = """<script>
(function(){
  var FR=/\\/fr\\//.test(location.pathname);
  function T(en,fr){ return FR?fr:en; }
  function $(id){ return document.getElementById(id); }

  var R=%(R)s;
  var Q=%(Q)s;

  var idx=0, scores={}, keys=[];
  for (var k in R) keys.push(k);

  function start(){
    idx=0; scores={};
    for (var i=0;i<keys.length;i++) scores[keys[i]]=0;
    $('start').style.display='none';
    $('result').style.display='none';
    $('quiz').style.display='block';
    show();
    window.scrollTo(0,0);
  }

  function show(){
    var q=Q[idx];
    $('counter').textContent=T('Question ','Question ')+(idx+1)+T(' of ',' sur ')+Q.length;
    $('bar').style.width=(idx/Q.length*100)+'%%';
    $('qtext').textContent=FR?q.fr:q.en;
    var box=$('opts'); box.innerHTML='';
    q.a.forEach(function(opt){
      var b=document.createElement('button');
      b.type='button';
      b.className='option';
      b.textContent=FR?opt.fr:opt.en;
      b.addEventListener('click',function(){
        for(var kk in opt.s) scores[kk]+=opt.s[kk];
        idx++;
        if(idx<Q.length){ show(); window.scrollTo(0,0); } else result();
      });
      box.appendChild(b);
    });
  }

  /* A row of the result panel. Left cell is a label, right cell a figure, and
     each is its own text node so the French dictionary can find it. */
  function fact(label, value){
    if(!value) return null;
    var row=document.createElement('div');
    row.className='cf-row';
    var a=document.createElement('span'); a.className='cf-k'; a.textContent=label;
    var b=document.createElement('span'); b.className='cf-v'; b.textContent=value;
    row.appendChild(a); row.appendChild(b);
    return row;
  }

  function result(){
    $('quiz').style.display='none';
    $('result').style.display='block';
    /* a hair of jitter, so a tie is not always broken the same way */
    var j={};
    for(var i=0;i<keys.length;i++) j[keys[i]]=scores[keys[i]]+Math.random()*0.001;
    var order=keys.slice().sort(function(a,b){ return j[b]-j[a]; });
    var best=R[order[0]], second=R[order[1]];
    $('r-emoji').textContent=best.e;
    $('r-lead').textContent=T('The city that fits you best is\\u2026',
                              'La ville qui vous convient le mieux est\\u2026');
    $('r-name').textContent=FR?best.nf:best.ne;
    $('r-desc').textContent=FR?best.df:best.de;

    var f=$('r-facts'); f.innerHTML='';
    var rows=[
      fact(T('People in the metro area','Population de la r\\u00e9gion m\\u00e9tropolitaine'),
           FR?best.pf:best.pe),
      fact(T('Average two-bedroom rent','Loyer moyen d\\u0027un deux chambres'),
           FR?best.rf:best.re),
      fact(T('Rental vacancy rate','Taux d\\u0027inoccupation des logements'),
           FR?best.vf:best.ve),
      fact(T('Getting around','Se d\\u00e9placer'), FR?best.tf:best.te)
    ];
    for(var n=0;n<rows.length;n++) if(rows[n]) f.appendChild(rows[n]);

    $('r-second').textContent=second
      ? T('Runner-up: ','Deuxi\\u00e8me : ')+(FR?second.nf:second.ne)
      : '';
    window.scrollTo(0,0);
  }

  function labels(){
    $('startBtn').textContent=T('Start the quiz','Commencer le quiz');
    $('againBtn').textContent=T('Try again','Recommencer');
    $('moreLink').textContent=T('Compare all thirteen',
                                'Comparer les treize');
  }

  $('startBtn').addEventListener('click',start);
  $('againBtn').addEventListener('click',start);
  labels();
})();
</script>"""


# --------------------------------------------------------------------------
def start_panel():
    return """  <section id="start" class="panel center">
    <div style="font-size:46px">🏙️</div>
    <h1>%(h1)s</h1>
    <p class="muted" style="max-width:600px;margin:0 auto">%(lead)s</p>
    <details class="howto"><summary>📖 %(howto)s</summary><p>%(howtop)s</p></details>
    <p style="margin-top:18px"><button class="btn btn-lg" type="button" id="startBtn">%(btn)s</button></p>
  </section>""" % {
        "h1": T("Which Canadian City Should You Live In?",
                "Dans quelle ville canadienne devriez-vous vivre ?"),
        "lead": T("Ten questions about winter, rent, language and how far you want "
                  "the wilderness to be — and one of thirteen Canadian cities at the "
                  "end, with what it actually costs to live there.",
                  "Dix questions sur l'hiver, le loyer, la langue et la distance qui "
                  "vous sépare de la nature — et l'une des treize villes canadiennes "
                  "à la fin, avec ce qu'il en coûte vraiment pour y vivre."),
        "howto": T("How to play", "Comment jouer"),
        "howtop": T("Tap the choice that feels most like you. There are ten "
                    "questions, no right answers and nothing to study. At the end "
                    "you get one city, the figures that go with it, the city that "
                    "came second, and a button to run the whole thing again.",
                    "Touchez le choix qui vous ressemble le plus. Il y a dix "
                    "questions, aucune bonne réponse et rien à réviser. À la fin, vous "
                    "obtenez une ville, les chiffres qui l'accompagnent, la ville "
                    "arrivée deuxième, et un bouton pour tout recommencer."),
        "btn": T("Start the quiz", "Commencer le quiz"),
    }


def result_panel():
    return """  <section id="result" class="panel center" style="display:none" data-no-i18n>
    <div class="result-big" id="r-emoji">🏙️</div>
    <p class="muted" id="r-lead"></p>
    <h2 id="r-name" style="color:var(--red);font-size:clamp(1.8rem,6vw,2.8rem);font-weight:800;margin:0"></h2>
    <p id="r-desc" style="max-width:560px;margin:0 auto 16px"></p>
    <div id="r-facts" class="cf-facts"></div>
    <p class="muted" id="r-second" style="font-size:14px"></p>
    <div>
      <button class="btn btn-lg" type="button" id="againBtn"></button>
      <a class="btn btn-ghost btn-lg" href="#compare" id="moreLink"></a>
    </div>
  </section>"""


# the result panel needs a few rules of its own; everything else is site CSS
FACT_CSS = """<style>
.cf-facts{max-width:460px;margin:0 auto 14px;text-align:left}
.cf-row{display:flex;justify-content:space-between;gap:12px;padding:7px 2px;
  border-bottom:1px solid #e6e1d8;font-size:15px}
.cf-row:last-child{border-bottom:none}
.cf-k{color:#5c5546}
.cf-v{font-weight:700;text-align:right}
</style>"""


# --------------------------------------------------------------------------
def compare_table():
    """All thirteen in one table. This is the part a person wants after the
    result, and the part a search engine can read without running the quiz."""
    head = [T("City", "Ville"),
            T("People (2025)", "Population (2025)"),
            T("Two-bedroom rent", "Loyer, deux chambres"),
            T("Vacancy rate", "Taux d'inoccupation"),
            T("Getting around", "Se déplacer")]
    rows = []
    for (k, emoji, ne, nf, de, df, pop, popf, rent, rentf,
         vac, vacf, tre, trf) in CITIES:
        rows.append([
            T(ne, nf),
            T(pop, popf),
            T(rent, rentf) if rent else T("not published", "non publié"),
            T(vac, vacf) if vac else T("not surveyed", "non recensé"),
            T(tre, trf),
        ])
    th = "".join("<th>%s</th>" % x for x in head)
    tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r)
                 for r in rows)
    label = T("Table of thirteen Canadian cities — scroll sideways to see all of it",
              "Tableau de treize villes canadiennes — faites défiler latéralement "
              "pour tout voir")
    return ('<div class="cq-scroll" tabindex="0" role="region" aria-label="%s">'
            '<table class="cq-table"><thead><tr>%s</tr></thead>'
            "<tbody>%s</tbody></table></div>" % (e(label), th, tr))


def pagedoc():
    P = []
    a = P.append

    a('<section class="pagedoc" id="compare">')

    a("  <h2>%s</h2>" % T("All thirteen cities, side by side",
                          "Les treize villes, côte à côte"))
    a("  <p>%s</p>" % T(
        "Population figures are Statistics Canada's estimates for the census "
        "metropolitan area on 1 July 2025. Rents and vacancy rates are from one "
        "survey — CMHC's Rental Market Survey of October 2025 — so the columns "
        "can be compared with each other. The rent shown is the average for a "
        "two-bedroom purpose-built apartment, which is a different and usually "
        "cheaper thing than a condominium or a house.",
        "Les chiffres de population sont les estimations de Statistique Canada "
        "pour la région métropolitaine de recensement au 1er juillet 2025. Les "
        "loyers et les taux d'inoccupation proviennent d'une seule enquête — "
        "l'Enquête sur les logements locatifs de la SCHL d'octobre 2025 — de sorte "
        "que les colonnes sont comparables entre elles. Le loyer indiqué est la "
        "moyenne d'un appartement de deux chambres construit pour la location, ce "
        "qui n'est pas la même chose qu'un condo ou une maison, et coûte "
        "généralement moins cher."))
    a("  " + compare_table())
    a("  <p class=\"muted\" style=\"font-size:13.5px\">%s</p>" % T(
        "Two gaps, left open on purpose. Halifax has no rent figure here because "
        "CMHC's published tables gave more than one two-bedroom value for it in "
        "the same survey, and a wrong number is worse than a blank. Whitehorse is "
        "not one of the centres CMHC surveys, and it is a town rather than a "
        "metropolitan area, so its population is the 2021 census count for the "
        "city itself.",
        "Deux trous, laissés ouverts volontairement. Halifax n'a pas de loyer ici "
        "parce que les tableaux publiés de la SCHL donnaient plus d'une valeur "
        "pour un deux chambres dans la même enquête, et un chiffre erroné vaut "
        "moins qu'une case vide. Whitehorse ne fait pas partie des centres "
        "recensés par la SCHL, et c'est une ville et non une région "
        "métropolitaine : sa population est donc le recensement de 2021 pour la "
        "ville elle-même."))

    a("  <h2>%s</h2>" % T("How people actually choose a Canadian city",
                          "Comment on choisit vraiment une ville canadienne"))
    a("  <p>%s</p>" % T(
        "A quiz is a good way to start the argument and a poor way to end it. "
        "What follows is what the numbers say about the choice, which is not "
        "always what the conversation says.",
        "Un quiz est une bonne façon de lancer la discussion et une mauvaise "
        "façon de la conclure. Ce qui suit, c'est ce que disent les chiffres sur "
        "ce choix, et ce n'est pas toujours ce que dit la conversation."))

    a("  <h3>%s</h3>" % T("The rent gap is wider than most people expect",
                          "L'écart de loyer est plus grand qu'on ne le croit"))
    a("  <p>%s</p>" % T(
        "In the same month, the average two-bedroom apartment cost $2,363 in "
        "Vancouver and $1,276 in Quebec City. That is a difference of about "
        "$1,087 every month, or roughly $13,000 a year, for the same size of "
        "home in the same country. Toronto and Victoria sit near the top with "
        "Vancouver; Quebec City, Montreal and St. John's sit near the bottom.",
        "Le même mois, l'appartement moyen de deux chambres coûtait 2 363 $ à "
        "Vancouver et 1 276 $ à Québec. C'est une différence d'environ 1 087 $ par "
        "mois, soit à peu près 13 000 $ par année, pour un logement de même taille "
        "dans le même pays. Toronto et Victoria se situent près du sommet avec "
        "Vancouver ; Québec, Montréal et Saint-Jean près du bas."))
    a("  <p>%s</p>" % T(
        "The national average that October was $1,550. Four of the eleven cities "
        "here with a published figure came in below it, and Winnipeg was only "
        "$21 above. That is worth saying plainly, because the conversation about "
        "housing in Canada is largely a conversation about three cities, and ten "
        "of the thirteen here are not those three.",
        "La moyenne nationale ce mois d'octobre était de 1 550 $. Quatre des onze "
        "villes dont le loyer est publié ici se situaient en dessous, et Winnipeg "
        "n'était que de 21 $ au-dessus. Cela mérite d'être dit clairement, car la "
        "conversation sur le logement au Canada porte surtout sur trois villes, et "
        "dix des treize présentées ici ne sont pas celles-là."))

    a("  <h3>%s</h3>" % T("The vacancy rate tells you something the rent does not",
                          "Le taux d'inoccupation dit ce que le loyer ne dit pas"))
    a("  <p>%s</p>" % T(
        "The vacancy rate is the share of purpose-built rental apartments "
        "standing empty and available. It is a measure of how hard it is to find "
        "a place at all, which is a separate question from what a place costs. "
        "Below about three per cent, a renter is competing for what is left; "
        "above it, a landlord is competing for tenants.",
        "Le taux d'inoccupation est la part des appartements construits pour la "
        "location qui sont vides et disponibles. Il mesure la difficulté à trouver "
        "un logement, ce qui est une question distincte de son prix. Sous environ "
        "trois pour cent, c'est le locataire qui se bat pour ce qui reste ; "
        "au-dessus, c'est le propriétaire qui cherche des locataires."))
    a("  <p>%s</p>" % T(
        "In October 2025 the national rate was 3.1 per cent. St. John's was the "
        "tightest market on this list at 2.1 per cent, followed by Quebec City "
        "at 2.4 and Halifax at 2.6. Quebec City has the lowest rent of the "
        "thirteen and St. John's the third lowest, so cheap and hard to find are "
        "not opposites. Calgary was the loosest by a "
        "distance at 5.0 per cent, which is the highest of any large Canadian "
        "city and the reason its rent stopped rising that year.",
        "En octobre 2025, le taux national était de 3,1 pour cent. Saint-Jean "
        "était le marché le plus serré de cette liste à 2,1 pour cent, suivi de "
        "Québec à 2,4 et de Halifax à 2,6. Québec affiche le loyer le plus bas "
        "des treize et Saint-Jean le troisième plus bas : bon marché et difficile "
        "à trouver ne sont pas des contraires. Calgary était de loin le marché le "
        "plus détendu, à 5,0 pour "
        "cent, le taux le plus élevé des grandes villes canadiennes et la raison "
        "pour laquelle son loyer a cessé de monter cette année-là."))
    a("  <p>%s</p>" % T(
        "Read the two columns together. A cheap city with a two per cent vacancy "
        "rate is cheap for the people already in it.",
        "Lisez les deux colonnes ensemble. Une ville bon marché avec un taux "
        "d'inoccupation de deux pour cent est bon marché pour ceux qui y sont "
        "déjà."))

    a("  <h3>%s</h3>" % T("Where newcomers are going has genuinely shifted",
                          "L'endroit où s'installent les nouveaux arrivants a vraiment changé"))
    a("  <p>%s</p>" % T(
        "For decades the answer to “where do people who move to Canada settle” "
        "was Toronto, Montreal or Vancouver. Statistics Canada's subprovincial "
        "estimates published in January 2026 show that changing quickly.",
        "Pendant des décennies, la réponse à « où s'installent les gens qui "
        "immigrent au Canada ? » était Toronto, Montréal ou Vancouver. Les "
        "estimations infraprovinciales de Statistique Canada publiées en janvier "
        "2026 montrent que cela change rapidement."))
    a("  <ul><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ul>" % (
        T("Over the five years to July 2025, the share of Ontario's new "
          "immigrants settling in the Toronto area fell from 76.1 per cent to "
          "60.5 per cent.",
          "Au cours des cinq années jusqu'en juillet 2025, la part des nouveaux "
          "immigrants de l'Ontario s'installant dans la région de Toronto est "
          "passée de 76,1 pour cent à 60,5 pour cent."),
        T("Over the same period, the share of Quebec's new immigrants settling "
          "in the Montreal area fell from 83.1 per cent to 65.3 per cent.",
          "Sur la même période, la part des nouveaux immigrants du Québec "
          "s'installant dans la région de Montréal est passée de 83,1 pour cent à "
          "65,3 pour cent."),
        T("Quebec City's share of the province's immigrants more than doubled, "
          "from 6.7 per cent to 14.7 per cent, and Ottawa–Gatineau's share of "
          "Ontario's roughly doubled, from 6.4 per cent to 12.5 per cent.",
          "La part des immigrants de la province qui s'installent à Québec a plus "
          "que doublé, de 6,7 pour cent à 14,7 pour cent, et celle "
          "d'Ottawa–Gatineau en Ontario a environ doublé, de 6,4 pour cent à "
          "12,5 pour cent."),
        T("The fastest-growing metropolitan areas in the country that year were "
          "Edmonton, Moncton and Calgary, each at close to three per cent.",
          "Les régions métropolitaines qui ont crû le plus vite au pays cette "
          "année-là étaient Edmonton, Moncton et Calgary, chacune près de trois "
          "pour cent."),
    ))
    a("  <p>%s</p>" % T(
        "If you are choosing a first Canadian city, this matters more than it "
        "sounds. The mid-size cities on this list are no longer places you go "
        "instead of the community you were expecting to find.",
        "Si vous choisissez une première ville canadienne, cela compte plus qu'il "
        "n'y paraît. Les villes de taille moyenne de cette liste ne sont plus des "
        "endroits où l'on va à défaut de la communauté que l'on espérait trouver."))

    a("  <h3>%s</h3>" % T("Can you live there without a car?",
                          "Peut-on y vivre sans voiture ?"))
    a("  <p>%s</p>" % T(
        "Six of the thirteen have a rail system you could plan a life around: "
        "Toronto, Montreal and Vancouver on a large scale, and Calgary, Ottawa "
        "and Edmonton on a smaller one. Quebec City is building a tramway, "
        "Saskatoon is building rapid transit stations, and Winnipeg runs a "
        "dedicated busway. Halifax and St. John's are walkable in their older "
        "parts and bus-only beyond them. In Whitehorse, almost everyone drives.",
        "Six des treize disposent d'un réseau ferroviaire autour duquel on peut "
        "organiser sa vie : Toronto, Montréal et Vancouver à grande échelle, et "
        "Calgary, Ottawa et Edmonton à plus petite. Québec construit un tramway, "
        "Saskatoon construit des stations de transport rapide, et Winnipeg "
        "exploite un corridor réservé aux autobus. Halifax et Saint-Jean se "
        "parcourent à pied dans leurs quartiers anciens et en autobus au-delà. À "
        "Whitehorse, presque tout le monde conduit."))
    a("  <p>%s</p>" % T(
        "A car costs money the rent table does not show. In a city where you can "
        "manage without one, a higher rent is not always the more expensive "
        "choice.",
        "Une voiture coûte de l'argent que le tableau des loyers ne montre pas. "
        "Dans une ville où l'on peut s'en passer, un loyer plus élevé n'est pas "
        "toujours le choix le plus coûteux."))

    a("  <h3>%s</h3>" % T("Winter, honestly",
                          "L'hiver, honnêtement"))
    a("  <p>%s</p>" % T(
        "People get winter wrong in both directions. The prairie cities are "
        "colder than newcomers imagine, and the cold is dry and often sunny, "
        "which is easier to dress for than the number suggests. The coastal "
        "cities are milder than the reputation of the country implies — "
        "Victoria and Vancouver rarely hold snow — and they are wet in a way "
        "that wears on people who expected mild to mean pleasant.",
        "On se trompe sur l'hiver dans les deux sens. Les villes des Prairies "
        "sont plus froides que ne l'imaginent les nouveaux arrivants, et ce froid "
        "est sec et souvent ensoleillé, ce qui se vêt plus facilement que le "
        "chiffre ne le laisse croire. Les villes côtières sont plus douces que la "
        "réputation du pays ne le suggère — Victoria et Vancouver gardent "
        "rarement la neige — et elles sont humides d'une façon qui use ceux qui "
        "croyaient que doux voulait dire agréable."))
    a("  <p>%s</p>" % T(
        "The thing that decides whether a person can live with a Canadian winter "
        "is usually not how cold it gets. It is how long it lasts, and how much "
        "daylight there is while it does.",
        "Ce qui détermine si l'on peut vivre un hiver canadien, ce n'est "
        "généralement pas l'intensité du froid. C'est sa durée, et la quantité de "
        "lumière du jour pendant ce temps."))

    a("  <h3>%s</h3>" % T("What a quiz cannot weigh",
                          "Ce qu'un quiz ne peut pas peser"))
    a("  <p>%s</p>" % T(
        "Work is usually the real answer, and it does not appear in any of the "
        "ten questions. Neither does family, nor whether your qualifications are "
        "recognised in that province, nor immigration status, nor whether you "
        "can find a place at all in a city with a two per cent vacancy rate. "
        "Treat the result as a conversation starter. The table above is the part "
        "worth keeping.",
        "Le travail est généralement la vraie réponse, et il n'apparaît dans "
        "aucune des dix questions. Pas plus que la famille, ni la reconnaissance "
        "de vos diplômes dans cette province, ni le statut d'immigration, ni la "
        "possibilité même de trouver un logement dans une ville où le taux "
        "d'inoccupation est de deux pour cent. Prenez le résultat comme un point "
        "de départ de discussion. C'est le tableau ci-dessus qui vaut la peine "
        "d'être gardé."))

    a("  <h2>%s</h2>" % T("Common questions", "Questions fréquentes"))
    a("  <h3>%s</h3>" % T("Should I actually move because of this?",
                          "Devrais-je vraiment déménager à cause de ceci ?"))
    a("  <p>%s</p>" % T(
        "No. It is a game with real figures attached. Moving depends on work, "
        "family, immigration status and housing you can actually get, and the "
        "quiz asks about none of them.",
        "Non. C'est un jeu accompagné de vrais chiffres. Déménager dépend du "
        "travail, de la famille, du statut d'immigration et d'un logement que "
        "l'on peut réellement obtenir, et le quiz ne pose de question sur aucun "
        "de ces points."))
    a("  <h3>%s</h3>" % T("Why is my city not one of the answers?",
                          "Pourquoi ma ville ne fait-elle pas partie des réponses ?"))
    a("  <p>%s</p>" % T(
        "Thirteen results keep it quick. They were chosen to cover every region "
        "of the country — Pacific coast, prairie, central Canada, Quebec, "
        "Atlantic and the North — rather than to rank anywhere.",
        "Treize résultats, c'est ce qui garde le jeu rapide. Ils ont été choisis "
        "pour couvrir chaque région du pays — la côte du Pacifique, les Prairies, "
        "le centre du Canada, le Québec, l'Atlantique et le Nord — et non pour "
        "classer qui que ce soit."))
    a("  <h3>%s</h3>" % T("How current are the rent figures?",
                          "À quand remontent les chiffres des loyers ?"))
    a("  <p>%s</p>" % T(
        "They are from CMHC's rental market survey of October 2025, published in "
        "December 2025, which is the most recent full survey of every centre. "
        "CMHC runs it once a year, so these are the numbers until the next one.",
        "Ils proviennent de l'enquête sur les logements locatifs de la SCHL "
        "d'octobre 2025, publiée en décembre 2025, la plus récente enquête "
        "complète couvrant tous les centres. La SCHL la mène une fois par année : "
        "ce sont donc les chiffres en vigueur jusqu'à la prochaine."))
    a("  <h3>%s</h3>" % T("How long does the quiz take?",
                          "Combien de temps dure le quiz ?"))
    a("  <p>%s</p>" % T("About two minutes.", "Environ deux minutes."))
    a("  <h3>%s</h3>" % T("Can I get a different city?",
                          "Puis-je obtenir une autre ville ?"))
    a("  <p>%s</p>" % T(
        "Yes. Change two or three answers and the totals move, which is half the "
        "reason to run it twice.",
        "Oui. Changez deux ou trois réponses et les totaux bougent, ce qui est la "
        "moitié de la raison de le refaire."))

    a("  <h2>%s</h2>" % T("Where these numbers come from", "D'où viennent ces chiffres"))
    a('  <ul class="cq-sources">')
    a('    <li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260114/dq260114a-eng.htm" '
      'target="_blank" rel="noopener nofollow">%s</a></li>' % T(
          "Statistics Canada — Canada's population estimates: Subprovincial "
          "areas, 2025 (14 January 2026)",
          "Statistique Canada — Estimations de la population du Canada : régions "
          "infraprovinciales, 2025 (14 janvier 2026)"))
    a('    <li><a href="https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/market-reports/rental-market-reports-major-centres" '
      'target="_blank" rel="noopener nofollow">%s</a></li>' % T(
          "Canada Mortgage and Housing Corporation — Rental Market Report, from "
          "the October 2025 survey",
          "Société canadienne d'hypothèques et de logement — Rapport sur le marché "
          "locatif, enquête d'octobre 2025"))
    a("  </ul>")

    a("  <h2>%s</h2>" % T("More to explore", "À découvrir aussi"))
    a('  <p class="pd-rel">'
      '<a href="canadas-biggest-cities.html">%s</a> · '
      '<a href="province-quiz.html">%s</a> · '
      '<a href="canada-map.html">%s</a> · '
      '<a href="canada-provinces-and-territories-explained.html">%s</a> · '
      '<a href="quizzes.html">%s</a></p>' % (
          T("Read about Canada's biggest cities",
            "Lire sur les plus grandes villes du Canada"),
          T("Find out which province matches your personality",
            "Découvrir quelle province correspond à votre personnalité"),
          T("Explore the map of Canada", "Explorer la carte du Canada"),
          T("Read about the provinces and territories",
            "Lire sur les provinces et territoires"),
          T("See every quiz on the site in one place",
            "Voir tous les quiz du site au même endroit")))
    a("  <h2>%s</h2>" % T("You might also like", "Vous aimerez peut-être aussi"))
    a('  <nav class="also"><p><a href="canada-geography-coast-to-coast.html">'
      '🗺️ %s</a></p></nav>' % T("Canada's Geography, Coast to Coast",
                                "La géographie du Canada, d'un océan à l'autre"))
    a("</section>")
    return "\n".join(P)


# --------------------------------------------------------------------------
# Both of these go through T(): the French page looks its title and its meta
# description up in the same dictionary as everything else, and fr_gap.py fails
# the build if either is left in English. That is exactly what happened on the
# first run of this script.
TITLE = T("Which Canadian City Should You Live In? Quiz | Canada Quiz",
          "Dans quelle ville canadienne devriez-vous vivre ? Quiz | Canada Quiz")
DESC = T("Ten questions and thirteen Canadian cities, each with its real "
         "population, average two-bedroom rent and vacancy rate. Free, no "
         "signup, works on a phone.",
         "Dix questions et treize villes canadiennes, chacune avec sa population "
         "réelle, son loyer moyen pour un deux chambres et son taux "
         "d'inoccupation. Gratuit, sans inscription, fonctionne sur téléphone.")


def rewrite(txt):
    def sub1(pattern, repl, what, flags=0):
        new, n = re.subn(pattern, lambda m: repl, txt, count=1, flags=flags)
        if n != 1:
            sys.exit("could not replace %s (%d matches)" % (what, n))
        print("  replaced %s" % what)
        return new

    # ---- head -------------------------------------------------------------
    txt = sub1(r"<title>.*?</title>", "<title>%s</title>" % e(TITLE), "<title>")
    txt = sub1(r'<meta name="description" content="[^"]*">',
               '<meta name="description" content="%s">' % e(DESC),
               "meta description")
    # both the WebPage name and description inside the JSON-LD graph
    txt = re.sub(r'"name":"Which Canadian City Should You Live In\? \| Canada Quiz"',
                 '"name":%s' % json.dumps(TITLE), txt)
    txt = re.sub(r'"description":"Seven questions[^"]*"',
                 '"description":%s' % json.dumps(DESC), txt)
    if '"description":%s' % json.dumps(DESC) not in txt:
        sys.exit("JSON-LD description not replaced")
    print("  replaced JSON-LD name and description")

    # the little stylesheet the result panel needs, once, before </head>
    if "cf-facts" not in txt:
        txt = txt.replace("</head>", FACT_CSS + "\n</head>", 1)
        print("  added result-panel CSS")

    # ---- body -------------------------------------------------------------
    txt = sub1(r'  <section id="start".*?\n  </section>', start_panel(),
               "start panel", re.S)
    txt = sub1(r'  <section id="result".*?\n  </section>', result_panel(),
               "result panel", re.S)
    txt = sub1(r"<!--PAGEDOC-->.*?<!--/PAGEDOC-->",
               "<!--PAGEDOC-->\n" + pagedoc() + "\n<!--/PAGEDOC-->",
               "page documentation", re.S)

    R, Q = js_payload()
    txt = sub1(r"<script>\n\(function\(\)\{.*?\n</script>",
               SCRIPT % {"R": R, "Q": Q}, "quiz script", re.S)
    return txt


def main():
    if "--sim" in sys.argv:
        simulate()
        return

    print("checking the scoring is playable before touching the page")
    simulate(60000)
    print("")

    txt = io.open(PAGE, encoding="utf-8").read()
    txt = rewrite(txt)
    io.open(PAGE, "w", encoding="utf-8").write(txt)

    prose = re.sub(r"<script.*?</script>|<style.*?</style>", " ", txt, flags=re.S)
    words = len(re.sub(r"<[^>]+>", " ", prose).split())
    print("\nwrote which-canadian-city-quiz.html — about %d words of page text, "
          "%d cities, %d questions" % (words, len(CITIES), len(QUESTIONS)))
    flush_pairs()


if __name__ == "__main__":
    main()
