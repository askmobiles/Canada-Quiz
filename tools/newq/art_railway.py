#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article — how Canada built its first transcontinental railway.

Source: research/transcontinental-railway-20260827.md in the private project
notes. Government of Canada, Crown agencies, national and public museums,
provincial archives and heritage agencies, and public-university publications
only. Commercial and crowd-edited reference sites were excluded by the research
rule and none is cited here.

The finding this page leads with, because almost nothing else does: the railway
was LATE. The British Columbia Terms of Union required completion within ten
years of 20 July 1871 — by 20 July 1881. The last spike went in on 7 November
1885, over four years past that promise. The "built at astonishing speed" story
only works against the revised 1891 deadline that UBC's Chung Collection
timeline reports, and almost nobody says which deadline they mean.

Deliberately kept off the page because no official source in the research
supports them:
  * any total construction cost of the CPR (LAC gives public funds, loans and
    land, which is a different thing, and says so);
  * any total or peak workforce figure;
  * any single Chinese worker death toll — four official sources disagree and
    UBC states the exact number can never be known, so all four are printed;
  * any per-day track-laying record — the famous ones belong to the 1869 US
    Central Pacific race, a different railway;
  * the duration of the 1885 troop movement and the number or length of the
    gaps in the line north of Lake Superior;
  * any dollar figure for the Canadian Northern, the Grand Trunk Pacific or the
    National Transcontinental;
  * any money figure attached to the Pacific Scandal;
  * the 1880 syndicate membership beyond Donald Smith, whom official sources
    call a director and nothing more;
  * quantities of explosives, and totals of tunnels or bridges for the whole
    line;
  * a repeal date for the monopoly clause.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="how-canada-built-the-railway.html",
    section="History",
    title=T("How Canada Built Its First Railway Across the Country",
            "Comment le Canada a bâti son premier chemin de fer d'un océan à l'autre"),
    desc=T("The promise was ten years. The last spike went in more than four years late, "
           "at Craigellachie, and it was iron, not gold. A plain, sourced account of who "
           "planned the railway, who paid, who built it, who died, and what the official "
           "record still does not say.",
           "La promesse était de dix ans. Le dernier crampon a été planté avec plus de "
           "quatre ans de retard, à Craigellachie, et il était en fer, non en or. Un récit "
           "simple et sourcé de qui a planifié le chemin de fer, qui a payé, qui l'a bâti, "
           "qui y est mort, et de ce que le dossier officiel ne dit toujours pas."),
    h1=T("\U0001F682 How Canada built its first railway across the country",
         "\U0001F682 Comment le Canada a bâti son premier chemin de fer d'un océan à "
         "l'autre"),
    hero=T("Canada promised British Columbia a railway within ten years. It took more than "
           "fourteen. This page follows the dates, the money, the passes through the "
           "mountains and the people who did the work — and it stops where the official "
           "record stops.",
           "Le Canada a promis à la Colombie-Britannique un chemin de fer en dix ans. Il en "
           "a fallu plus de quatorze. Cette page suit les dates, l'argent, les cols de "
           "montagne et les gens qui ont fait le travail — et elle s'arrête là où s'arrête "
           "le dossier officiel."),
    checked=T("Last checked 27 August 2026 — every figure here is attributed to the body "
              "that published it",
              "Dernière vérification le 27 août 2026 — chaque chiffre présenté ici est "
              "attribué à l'organisme qui l'a publié"),
)

# ------------------------------------------------------------------ 1
a.h2(T("Start with the thing almost everybody gets wrong",
       "Commençons par ce que presque tout le monde se trompe"))
a.p(T(
    "The story usually told is that Canada built a railway across a continent at "
    "astonishing speed. Parks Canada records the promise itself: in 1871 Sir John A. "
    "Macdonald pledged to build the longest railway in the world within ten years. That is "
    "a quotation of a pledge, not a verified engineering fact, and it is worth reading as "
    "one.",
    "On raconte d'habitude que le Canada a bâti un chemin de fer d'un bout à l'autre d'un "
    "continent à une vitesse étonnante. Parcs Canada consigne la promesse elle-même : en "
    "1871, sir John A. Macdonald s'est engagé à bâtir le plus long chemin de fer du monde "
    "en dix ans. C'est la citation d'une promesse, non un fait technique vérifié, et il "
    "vaut mieux la lire ainsi."))
a.p(T(
    "The deadline was not a slogan. It was written into the constitutional document that "
    "brought British Columbia into Canada. The Terms of Union, clause 11, as reproduced by "
    "Justice Canada, bound Canada to the commencement of construction within two years of "
    "the union and to the completion of such railway within ten years from the date of the "
    "Union. The union took effect on 20 July 1871. So the two dates in the promise are "
    "start by 20 July 1873 and finish by 20 July 1881.",
    "L'échéance n'était pas un slogan. Elle était inscrite dans le document constitutionnel "
    "qui a fait entrer la Colombie-Britannique dans le Canada. Les Conditions de l'adhésion, "
    "clause 11, telles que reproduites par Justice Canada, obligeaient le Canada au "
    "commencement des travaux dans les deux ans suivant l'union et à l'achèvement de ce "
    "chemin de fer dans les dix ans à compter de la date de l'Union. L'union est entrée en "
    "vigueur le 20 juillet 1871. Les deux dates de la promesse sont donc : commencer avant "
    "le 20 juillet 1873 et terminer avant le 20 juillet 1881."))
a.callout(T(
    "<strong>The last spike was driven on 7 November 1885.</strong> Against the deadline "
    "written into the Terms of Union, that is over four years late. Regular transcontinental "
    "service began the following summer, which makes it close to five years late. The site "
    "worked that arithmetic out from two officially published dates; no single government "
    "page states the lateness as a figure.",
    "<strong>Le dernier crampon a été planté le 7 novembre 1885.</strong> Par rapport à "
    "l'échéance inscrite dans les Conditions de l'adhésion, c'est plus de quatre ans de "
    "retard. Le service transcontinental régulier a commencé l'été suivant, ce qui fait près "
    "de cinq ans de retard. Ce calcul a été fait ici à partir de deux dates publiées "
    "officiellement ; aucune page gouvernementale ne chiffre elle-même ce retard."))
a.p(T(
    "There is a second deadline, and this is where the two versions of the story come from. "
    "UBC Library's Chung Collection timeline says the 1881 date was pushed to 1891 as "
    "construction lagged, and describes 7 November 1885 as four years past the original "
    "deadline but well ahead of the revised 1891 deadline. Both readings are true. They "
    "measure against different promises. No federal source found in this research confirms "
    "the revised date, so it is attributed to UBC and left there.",
    "Il existe une seconde échéance, et c'est de là que viennent les deux versions du récit. "
    "La chronologie de la collection Chung de la bibliothèque de l'UBC indique que la date de "
    "1881 a été reportée à 1891 devant les retards, et décrit le 7 novembre 1885 comme quatre "
    "ans après l'échéance initiale, mais bien avant l'échéance révisée de 1891. Les deux "
    "lectures sont vraies. Elles se mesurent à des promesses différentes. Aucune source "
    "fédérale trouvée dans cette recherche ne confirme la date révisée ; elle est donc "
    "attribuée à l'UBC et rien de plus."))
a.p(T(
    "One more caution about speed. The often-repeated four years belongs only to the "
    "company's own stretch of the work, from the incorporation of the Canadian Pacific "
    "Railway Company on 16 February 1881 to the last spike in November 1885. Surveys began "
    "in 1871 and the government was letting construction contracts in the mid-1870s. Four "
    "years is not the length of the project.",
    "Une dernière mise en garde sur la vitesse. Les quatre ans souvent répétés ne valent que "
    "pour la portion des travaux menée par la compagnie, de la constitution de la Compagnie "
    "du chemin de fer Canadien du Pacifique le 16 février 1881 jusqu'au dernier crampon en "
    "novembre 1885. Les levés ont commencé en 1871 et le gouvernement accordait des contrats "
    "de construction dès le milieu des années 1870. Quatre ans, ce n'est pas la durée du "
    "projet."))

# ------------------------------------------------------------------ 2
a.h2(T("The last spike, correctly",
       "Le dernier crampon, correctement raconté"))
a.p(T(
    "Three details get mixed up almost every time this moment is described, and all three "
    "are settled by official sources.",
    "Trois détails sont presque toujours brouillés quand on raconte ce moment, et les trois "
    "sont tranchés par des sources officielles."))
a.ul([
    T("<strong>The place was Craigellachie, in Eagle Pass — not Rogers Pass.</strong> The "
      "Parks Canada plaque for the Eagle Pass national historic event reads that on 7 "
      "November 1885, Sir Donald Smith drove the last spike here, in the pass, at "
      "Craigellachie. Parks Canada puts Craigellachie 118 kilometres west of Rogers Pass. "
      "They are two different places in two different mountain ranges.",
      "<strong>Le lieu était Craigellachie, dans le col Eagle — et non le col Rogers.</strong> "
      "La plaque de Parcs Canada pour l'événement historique national du col Eagle indique "
      "que, le 7 novembre 1885, sir Donald Smith y a planté le dernier crampon, dans le col, "
      "à Craigellachie. Parcs Canada situe Craigellachie à 118 kilomètres à l'ouest du col "
      "Rogers. Ce sont deux endroits différents dans deux chaînes de montagnes différentes."),
    T("<strong>The spike was iron, not gold.</strong> Library and Archives Canada states it "
      "plainly: the last spike was made of iron, not the customary gold. A ceremonial spike "
      "does exist — the Governor General's, given to William Van Horne in 1885 and now in the "
      "Canadian Museum of History's collection — but it is not the one that went into the "
      "track at Craigellachie.",
      "<strong>Le crampon était en fer, non en or.</strong> Bibliothèque et Archives Canada "
      "le dit clairement : le dernier crampon était fait de fer, et non de l'or habituel. Un "
      "crampon de cérémonie existe bel et bien — celui du gouverneur général, remis à William "
      "Van Horne en 1885 et conservé aujourd'hui dans la collection du Musée canadien de "
      "l'histoire — mais ce n'est pas celui qui a été planté dans la voie à Craigellachie."),
    T("<strong>The spike did not open the line to the travelling public.</strong> A "
      "Parks Canada plaque at Port Moody records the first transcontinental train reaching "
      "the terminus the next day, 8 November 1885. The Montréal plaque records that the "
      "first regular transcontinental train departed from that place on 28 June 1886, and "
      "the Port Moody record gives first regular passenger service as 4 July 1886.",
      "<strong>Le crampon n'a pas ouvert la ligne au public voyageur.</strong> Une plaque de "
      "Parcs Canada à Port Moody consigne l'arrivée du premier train transcontinental au "
      "terminus le lendemain, le 8 novembre 1885. La plaque de Montréal indique que le "
      "premier train transcontinental régulier est parti de cet endroit le 28 juin 1886, et "
      "la fiche de Port Moody donne le 4 juillet 1886 comme début du premier service régulier "
      "de voyageurs."),
])
a.p(T(
    "Something else is missing from the famous photograph of that morning, and two "
    "governments say so. The Province of British Columbia writes that Chinese workers were "
    "left out of the national celebration surrounding the railway's completion, and that in "
    "the Craigellachie photograph all of the Chinese Canadian workers were cleared from view. "
    "Library and Archives Canada makes the same observation about the same picture.",
    "Il manque autre chose sur la célèbre photographie de ce matin-là, et deux gouvernements "
    "le disent. La Province de la Colombie-Britannique écrit que les travailleurs chinois ont "
    "été exclus de la célébration nationale entourant l'achèvement du chemin de fer, et que, "
    "sur la photographie de Craigellachie, tous les travailleurs sino-canadiens ont été "
    "écartés du champ. Bibliothèque et Archives Canada fait la même observation à propos de "
    "la même image."))

# ------------------------------------------------------------------ 3
a.h2(T("The dates, in order", "Les dates, dans l'ordre"))
a.table(
    [T("Date", "Date"), T("What happened", "Ce qui s'est passé")],
    [[T("20 July 1871", "20 juillet 1871"),
      T("British Columbia enters Confederation. The Terms of Union require construction to "
        "start within two years and the railway to be finished within ten.",
        "La Colombie-Britannique entre dans la Confédération. Les Conditions de l'adhésion "
        "exigent que les travaux commencent dans les deux ans et que le chemin de fer soit "
        "achevé dans les dix ans.")],
     [T("April 1871", "Avril 1871"),
      T("Sandford Fleming is appointed Chief Engineer. About 21 survey parties, nearly 800 "
        "men, take the field in the first year.",
        "Sandford Fleming est nommé ingénieur en chef. Environ 21 équipes de levés, soit près "
        "de 800 hommes, sont sur le terrain la première année.")],
     [T("2 April 1872", "2 avril 1872"),
      T("An Order in Council adopts the Yellow Head Pass as the crossing of the Rockies. The "
        "planned route is 2,730 miles.",
        "Un décret adopte le col Yellow Head comme passage des Rocheuses. Le tracé prévu fait "
        "2 730 milles.")],
     [T("2 April 1873", "2 avril 1873"),
      T("Mr Huntington moves his resolution in Parliament. The Pacific Scandal begins.",
        "M. Huntington dépose sa résolution au Parlement. Le scandale du Pacifique commence.")],
     [T("5 February 1873", "5 février 1873"),
      T("The Allan charter is signed: a land grant of 50,000,000 acres and a subsidy of "
        "$30,300,000.",
        "La charte Allan est signée : une concession de terres de 50 000 000 d'acres et une "
        "subvention de 30 300 000 $.")],
     [T("14 August 1873", "14 août 1873"),
      T("A Royal Commission is issued under the Great Seal — Charles Dewey Day as chairman, "
        "with Antoine Polette and James Robert Gowan.",
        "Une commission royale est établie sous le grand sceau — Charles Dewey Day à la "
        "présidence, avec Antoine Polette et James Robert Gowan.")],
     [T("23 October 1873", "23 octobre 1873"),
      T("The Allan company surrenders its charter, unable to make the financial arrangements.",
        "La compagnie Allan remet sa charte, incapable de conclure les arrangements "
        "financiers.")],
     [T("31 December 1879", "31 décembre 1879"),
      T("$14,287,824 has been charged to the railway account since April 1871, before any "
        "company existed to build it.",
        "14 287 824 $ ont été imputés au compte du chemin de fer depuis avril 1871, avant "
        "même qu'une compagnie existe pour le bâtir.")],
     [T("October 1880", "Octobre 1880"),
      T("The new contract: a $25 million subsidy, 25 million acres, a 20-year tax exemption "
        "and a 20-year monopoly clause.",
        "Le nouveau contrat : une subvention de 25 millions de dollars, 25 millions d'acres, "
        "une exemption de taxes de 20 ans et une clause de monopole de 20 ans.")],
     [T("16 February 1881", "16 février 1881"),
      T("The Canadian Pacific Railway Company is incorporated to take over construction.",
        "La Compagnie du chemin de fer Canadien du Pacifique est constituée pour reprendre "
        "les travaux.")],
     [T("1881", "1881"),
      T("The company adopts the Kicking Horse Pass instead of the surveyed Yellowhead route. "
        "Major Rogers searches the Selkirks with his Shuswap guides.",
        "La compagnie adopte le col Kicking Horse plutôt que le tracé levé du Yellowhead. Le "
        "major Rogers explore les Selkirk avec ses guides shuswap.")],
     [T("December 1881", "Décembre 1881"),
      T("The whole section between Winnipeg and Brandon is operational.",
        "Toute la section entre Winnipeg et Brandon est en service.")],
     [T("1882", "1882"),
      T("Van Horne becomes general manager. UBC records 500 miles of prairie track built that "
        "year alone.",
        "Van Horne devient directeur général. L'UBC consigne 500 milles de voie construits "
        "dans les Prairies cette seule année.")],
     [T("18 August 1883", "18 août 1883"),
      T("The prairie section of the railway is completed.",
        "La section des Prairies du chemin de fer est achevée.")],
     [T("1884", "1884"),
      T("The first train to attempt the Big Hill derails. Three workers are killed.",
        "Le premier train à s'attaquer à la Grande Côte déraille. Trois travailleurs sont "
        "tués.")],
     [T("1885", "1885"),
      T("The Chinese Immigration Act imposes a duty of $50 on every Chinese person seeking "
        "entry into Canada.",
        "La Loi de l'immigration chinoise impose un droit de 50 $ à toute personne chinoise "
        "qui cherche à entrer au Canada.")],
     [T("Fall 1885", "Automne 1885"),
      T("The line through Rogers Pass is completed.",
        "La ligne qui traverse le col Rogers est achevée.")],
     [T("7 November 1885", "7 novembre 1885"),
      T("The last spike is driven at Craigellachie, in Eagle Pass, British Columbia.",
        "Le dernier crampon est planté à Craigellachie, dans le col Eagle, en "
        "Colombie-Britannique.")],
     [T("8 November 1885", "8 novembre 1885"),
      T("The first transcontinental train reaches the terminus at Port Moody.",
        "Le premier train transcontinental atteint le terminus de Port Moody.")],
     [T("28 June 1886", "28 juin 1886"),
      T("The first regular transcontinental train departs from Montréal.",
        "Le premier train transcontinental régulier part de Montréal.")],
     [T("4 July 1886", "4 juillet 1886"),
      T("First regular passenger service at Port Moody, per the Parks Canada record.",
        "Premier service régulier de voyageurs à Port Moody, selon la fiche de Parcs Canada.")],
     [T("July 1886", "Juillet 1886"),
      T("The company repays all of its government loans, according to UBC's timeline.",
        "La compagnie rembourse tous ses prêts gouvernementaux, selon la chronologie de "
        "l'UBC.")]],
    label=T("The main dates of the first transcontinental railway — scroll sideways to see "
            "all of it",
            "Les principales dates du premier chemin de fer transcontinental — faites défiler "
            "latéralement pour tout voir"))

# ------------------------------------------------------------------ 4
a.h2(T("What it cost — and the number nobody publishes",
       "Ce qu'il a coûté — et le chiffre que personne ne publie"))
a.p(T(
    "Start with the deal that was actually carried out. The Manitoba Historic Resources "
    "Branch, quoting the October 1880 contract, sets out four things the government gave.",
    "Commençons par l'entente qui a réellement été exécutée. La Direction des ressources "
    "historiques du Manitoba, citant le contrat d'octobre 1880, expose quatre choses que le "
    "gouvernement a accordées."))
a.ul([
    T("<strong>A cash subsidy of twenty-five million dollars.</strong>",
      "<strong>Une subvention en argent de vingt-cinq millions de dollars.</strong>"),
    T("<strong>A grant of twenty-five million acres of land.</strong> Library and Archives "
      "Canada describes the same grant in metric units, as 10.4 million hectares of the best "
      "Prairie land. These are one grant in two units, not two grants.",
      "<strong>Une concession de vingt-cinq millions d'acres de terres.</strong> Bibliothèque "
      "et Archives Canada décrit la même concession en unités métriques, soit 10,4 millions "
      "d'hectares des meilleures terres des Prairies. Il s'agit d'une seule concession en "
      "deux unités, non de deux concessions."),
    T("<strong>Exemption from taxes on that land for twenty years.</strong>",
      "<strong>Une exemption de taxes sur ces terres pendant vingt ans.</strong>"),
    T("<strong>A twenty-year monopoly.</strong> In the contract's terms, no charters were to "
      "be granted for twenty years to any competitors seeking to build within fifteen miles "
      "of the international boundary. This is the clause that produced Manitoba's long fight "
      "with Ottawa in the 1880s. The sources gathered here document the clause but do not say "
      "when or how it ended, so this page does not say either.",
      "<strong>Un monopole de vingt ans.</strong> Selon les termes du contrat, aucune charte "
      "ne devait être accordée pendant vingt ans à des concurrents qui voudraient bâtir à "
      "moins de quinze milles de la frontière internationale. C'est la clause qui a provoqué "
      "la longue bataille du Manitoba avec Ottawa dans les années 1880. Les sources "
      "rassemblées ici attestent la clause mais ne disent pas quand ni comment elle a pris "
      "fin ; cette page ne le dit donc pas non plus."),
])
a.p(T(
    "Now compare it with the bargain that collapsed. The 1882 Royal Commission quotes the "
    "charter signed on 5 February 1873 by a company headed by Sir Hugh Allan, which bound "
    "itself to build the railway within ten years of 20 July 1871 in return for a land grant "
    "of 50,000,000 acres and a subsidy of $30,300,000. That is twice the land and more cash "
    "than the deal that was eventually signed. The larger numbers belong to the arrangement "
    "that fell apart in the Pacific Scandal, and they are often quoted as though they were "
    "the CPR's terms. They were not.",
    "Comparons maintenant avec l'entente qui s'est effondrée. La commission royale de 1882 "
    "cite la charte signée le 5 février 1873 par une compagnie dirigée par sir Hugh Allan, "
    "qui s'engageait à bâtir le chemin de fer dans les dix ans du 20 juillet 1871 en échange "
    "d'une concession de terres de 50 000 000 d'acres et d'une subvention de 30 300 000 $. "
    "C'est le double des terres et plus d'argent que l'entente finalement signée. Les chiffres "
    "les plus élevés appartiennent à l'arrangement qui s'est écroulé dans le scandale du "
    "Pacifique, et on les cite souvent comme s'ils étaient les conditions du Canadien "
    "Pacifique. Ils ne l'étaient pas."))
a.fig(bar_chart(
    T("Published dollar figures, in millions — none of them is a total construction cost",
      "Chiffres en dollars publiés, en millions — aucun n'est un coût total de construction"),
    [(T("1880 contract subsidy", "Subvention du contrat de 1880"), 25.0),
     (T("1873 Allan charter subsidy, never paid",
        "Subvention de la charte Allan de 1873, jamais versée"), 30.3),
     (T("Government spending on the railway account to 31 December 1879",
        "Dépenses de l'État au compte du chemin de fer jusqu'au 31 décembre 1879"), 14.3),
     (T("Public funds, Library and Archives Canada's estimate",
        "Fonds publics, estimation de Bibliothèque et Archives Canada"), 63.5),
     (T("Government loans, Library and Archives Canada",
        "Prêts gouvernementaux, Bibliothèque et Archives Canada"), 35.0)]))
a.callout(T(
    "<strong>No official source gives a total construction cost for the Canadian Pacific "
    "Railway.</strong> Not the Government of Canada, not a Crown agency, not a national "
    "museum, not a provincial archive, not a public university — none of the sources gathered "
    "for this page states one. Library and Archives Canada gives an estimated $63.5 million "
    "in public funds, government loans of $35 million, and 10.4 million hectares of land, and "
    "presents those as the price to the public rather than as what the railway cost to build. "
    "Any single total you see quoted elsewhere did not come from these sources.",
    "<strong>Aucune source officielle ne donne de coût total de construction pour le chemin de "
    "fer Canadien du Pacifique.</strong> Ni le gouvernement du Canada, ni un organisme de la "
    "Couronne, ni un musée national, ni des archives provinciales, ni une université publique "
    "— aucune des sources réunies pour cette page n'en énonce un. Bibliothèque et Archives "
    "Canada donne une estimation de 63,5 millions de dollars en fonds publics, des prêts "
    "gouvernementaux de 35 millions de dollars et 10,4 millions d'hectares de terres, et "
    "présente cela comme le prix payé par le public plutôt que comme le coût de construction "
    "du chemin de fer. Tout total unique cité ailleurs ne vient pas de ces sources."))
a.p(T(
    "Two smaller money facts are worth keeping. Canada also agreed, under the same clause 11 "
    "of the Terms of Union, to pay British Columbia the sum of 100,000 dollars per annum, in "
    "half-yearly payments in advance, for the belt of land along the line — what later "
    "statute calls the Railway Belt and the Peace River Block. And the cost of the railway "
    "measured against the size of the government or the economy of the day cannot be given "
    "here: no official source states it, and Statistics Canada's Historical Statistics of "
    "Canada carries railway series only from 1946 onward in its second edition.",
    "Deux faits financiers plus modestes méritent d'être retenus. Le Canada s'est aussi "
    "engagé, en vertu de la même clause 11 des Conditions de l'adhésion, à payer à la "
    "Colombie-Britannique la somme de 100 000 dollars par année, en versements semestriels "
    "d'avance, pour la bande de terres le long du tracé — ce qu'une loi ultérieure appelle la "
    "ceinture du chemin de fer et le bloc de la rivière la Paix. Et le coût du chemin de fer "
    "rapporté à la taille de l'État ou de l'économie de l'époque ne peut pas être donné ici : "
    "aucune source officielle ne l'énonce, et les Statistiques historiques du Canada de "
    "Statistique Canada ne contiennent de séries ferroviaires qu'à partir de 1946 dans leur "
    "deuxième édition."))

# ------------------------------------------------------------------ 5
a.h2(T("The Pacific Scandal", "Le scandale du Pacifique"))
a.p(T(
    "On 2 April 1873 a member of Parliament, Mr Huntington, moved a resolution about the "
    "Canadian Pacific Railway. A Royal Commission followed under the Great Seal on 14 August "
    "1873, chaired by Charles Dewey Day with Antoine Polette and James Robert Gowan. Library "
    "and Archives Canada holds its records; Government of Canada Publications, which holds "
    "the printed report, describes the inquiry as specifically addressing bribery allegations "
    "regarding construction contracts.",
    "Le 2 avril 1873, un député, M. Huntington, a déposé une résolution au sujet du chemin de "
    "fer Canadien du Pacifique. Une commission royale a suivi, établie sous le grand sceau le "
    "14 août 1873, présidée par Charles Dewey Day avec Antoine Polette et James Robert Gowan. "
    "Bibliothèque et Archives Canada en conserve les archives ; Publications du gouvernement "
    "du Canada, qui conserve le rapport imprimé, décrit l'enquête comme portant "
    "spécifiquement sur des allégations de pots-de-vin concernant des contrats de "
    "construction."))
a.p(T(
    "What it did to the project is recorded in the government's own words, quoted in the 1882 "
    "Royal Commission report and dated 23 October 1873. The Canadian Pacific Company, to whom "
    "a charter had been granted, had been unable to make the financial agreements necessary "
    "for the construction of that great undertaking; they had therefore executed a surrender "
    "of their charter, which had been accepted. The railway went back to government hands. "
    "Contracts were let piecemeal — the commission records Sifton and Ward taking the "
    "45 miles from Fort William to Shebandowan in April 1875 for $406,194 — and by the end of "
    "1879 the railway account had absorbed $14,287,824 without a company in place to finish "
    "the line.",
    "Ce que cela a fait au projet est consigné dans les mots mêmes du gouvernement, cités dans "
    "le rapport de la commission royale de 1882 et datés du 23 octobre 1873. La Compagnie du "
    "Pacifique canadien, à qui une charte avait été accordée, n'avait pu conclure les "
    "arrangements financiers nécessaires à la construction de cette grande entreprise ; elle "
    "avait donc remis sa charte, qui avait été acceptée. Le chemin de fer est retourné aux "
    "mains de l'État. Les contrats ont été accordés au coup par coup — la commission consigne "
    "que Sifton et Ward ont obtenu les 45 milles de Fort William à Shebandowan en avril 1875 "
    "pour 406 194 $ — et, à la fin de 1879, le compte du chemin de fer avait absorbé "
    "14 287 824 $ sans qu'une compagnie soit en place pour achever la ligne."))
a.p(T(
    "Beyond that, the official record is thin. No Government of Canada page located in this "
    "research narrates the scandal in detail; Parks Canada mentions only, on its page for Sir "
    "John A. Macdonald, that his nation-building efforts included the Pacific Scandal. The "
    "sums of money said to have passed from Sir Hugh Allan to the governing party's campaign "
    "are widely repeated, but none of the official sources used here states one, so none is "
    "printed here.",
    "Au-delà de cela, le dossier officiel est mince. Aucune page du gouvernement du Canada "
    "trouvée dans cette recherche ne raconte le scandale en détail ; Parcs Canada mentionne "
    "seulement, dans sa page sur sir John A. Macdonald, que ses efforts d'édification du pays "
    "ont compris le scandale du Pacifique. Les sommes d'argent qui seraient passées de sir "
    "Hugh Allan à la caisse électorale du parti au pouvoir sont largement répétées, mais "
    "aucune des sources officielles utilisées ici n'en énonce ; aucune n'est donc imprimée "
    "ici."))

# ------------------------------------------------------------------ 6
a.h2(T("The people who built it", "Les gens qui l'ont bâti"))
a.p(T(
    "Parks Canada describes the workforce this way: railway employees and contractors "
    "included Aboriginal people, new immigrants from many Asian and European countries, "
    "American contractors and people from the new country of Canada. The Canadian Museum of "
    "History says the project required many thousands of workers to complete the "
    "5,000-kilometre track. Statistics Canada, writing about the word navvy, says railway "
    "workers around 1885 earned about a dollar a day.",
    "Parcs Canada décrit ainsi la main-d'oeuvre : les employés et les entrepreneurs du chemin "
    "de fer comprenaient des Autochtones, de nouveaux immigrants venus de nombreux pays "
    "d'Asie et d'Europe, des entrepreneurs américains et des gens du nouveau pays qu'était le "
    "Canada. Le Musée canadien de l'histoire indique que le projet a exigé plusieurs milliers "
    "de travailleurs pour achever les 5 000 kilomètres de voie. Statistique Canada, en "
    "écrivant sur le mot navvy, indique que les travailleurs du rail gagnaient environ un "
    "dollar par jour vers 1885."))
a.p(T(
    "There is no published total. No official source found in this research gives a total or "
    "a peak workforce for the whole project. The figures that do exist are for the British "
    "Columbia section, and they count different things.",
    "Il n'existe aucun total publié. Aucune source officielle trouvée dans cette recherche ne "
    "donne un effectif total ou maximal pour l'ensemble du projet. Les chiffres qui existent "
    "portent sur la section de la Colombie-Britannique, et ils comptent des choses "
    "différentes."))
a.h3(T("How many Chinese workers", "Combien de travailleurs chinois"))
a.p(T(
    "Counts range from about 7,000 to over 17,000, and the spread is mostly about what is "
    "being counted — arrivals in Canada, arrivals in British Columbia, or men on the job at "
    "one moment.",
    "Les décomptes vont d'environ 7 000 à plus de 17 000, et l'écart tient surtout à ce que "
    "l'on compte — les arrivées au Canada, les arrivées en Colombie-Britannique ou les hommes "
    "au travail à un moment donné."))
a.ul([
    T("Canadian Heritage gives two numbers on one page: over 17,000 Chinese immigrants "
      "arrived between 1881 and 1884 to build the railway and later to maintain it, and about "
      "7,000 Chinese workers arrived in British Columbia during construction from 1880 to "
      "1885. These measure different things and should not be merged.",
      "Patrimoine canadien donne deux chiffres sur une même page : plus de 17 000 immigrants "
      "chinois sont arrivés entre 1881 et 1884 pour bâtir le chemin de fer et, plus tard, "
      "l'entretenir, et environ 7 000 travailleurs chinois sont arrivés en "
      "Colombie-Britannique pendant la construction, de 1880 à 1885. Ces chiffres mesurent des "
      "choses différentes et ne doivent pas être additionnés."),
    T("The same Canadian Heritage page says about 3,500 Chinese workers were on hand at any "
      "single point of time, forming three-quarters of the total railway workforce in the "
      "province.",
      "La même page de Patrimoine canadien indique qu'environ 3 500 travailleurs chinois "
      "étaient présents à un moment donné, formant les trois quarts de l'effectif ferroviaire "
      "total de la province."),
    T("Library and Archives Canada, the Canadian Museum of History, the Canadian Museum of "
      "Immigration at Pier 21 and the 2006 address by the Prime Minister all give a figure of "
      "about 15,000, worded variously as approximately, an estimated, and over.",
      "Bibliothèque et Archives Canada, le Musée canadien de l'histoire, le Musée canadien de "
      "l'immigration du Quai 21 et l'allocution du premier ministre de 2006 donnent tous un "
      "chiffre d'environ 15 000, formulé tour à tour comme approximativement, estimé et plus "
      "de."),
    T("The Province of British Columbia states that of the 9,000 railway workers at the end "
      "of 1882, 6,500 were Chinese Canadians, brought by ship from both California and China.",
      "La Province de la Colombie-Britannique indique que, sur les 9 000 travailleurs du "
      "chemin de fer à la fin de 1882, 6 500 étaient des Canadiens d'origine chinoise, amenés "
      "par bateau de Californie et de Chine."),
    T("The Parks Canada plaque, unveiled for a designation made in 1977, says only that "
      "contractor Andrew Onderdonk brought thousands of labourers from China, and that about "
      "three-quarters of the men who worked between the Pacific and Craigellachie were "
      "Chinese.",
      "La plaque de Parcs Canada, dévoilée pour une désignation faite en 1977, dit seulement "
      "que l'entrepreneur Andrew Onderdonk a fait venir des milliers d'ouvriers de Chine, et "
      "qu'environ les trois quarts des hommes qui ont travaillé entre le Pacifique et "
      "Craigellachie étaient chinois."),
])
a.h3(T("What they were paid", "Ce qu'ils étaient payés"))
a.callout(T(
    "<strong>This is the Province of British Columbia's own figure, on its own website.</strong> "
    "Chinese labourers received $1.00 a day, and from this $1.00 they had to pay for their "
    "food and gear. White workers were paid $1.50 to $2.50 per day and did not have to pay "
    "for provisions. The Parks Canada plaque puts the same gap more briefly: although "
    "considered excellent workers, they received only a dollar a day, half the pay of a white "
    "worker.",
    "<strong>Voici le chiffre de la Province de la Colombie-Britannique elle-même, sur son "
    "propre site.</strong> Les ouvriers chinois recevaient 1,00 $ par jour et, sur ce 1,00 $, "
    "ils devaient payer leur nourriture et leur équipement. Les travailleurs blancs étaient "
    "payés de 1,50 $ à 2,50 $ par jour et n'avaient pas à payer leurs vivres. La plaque de "
    "Parcs Canada exprime le même écart plus brièvement : bien que considérés comme "
    "d'excellents travailleurs, ils ne recevaient qu'un dollar par jour, la moitié du salaire "
    "d'un travailleur blanc."))
a.p(T(
    "The work was also allocated by race. The Province of British Columbia states that Chinese "
    "workers were given the most dangerous tasks, such as handling the explosive "
    "nitroglycerin used to break up solid rock. Library and Archives Canada says the same of "
    "explosives work. UBC Library records that they were assigned dangerous tasks such as "
    "tunnelling with dynamite, and that Canadian authorities of the day described them as "
    "living machines.",
    "Le travail était aussi réparti selon la race. La Province de la Colombie-Britannique "
    "indique que l'on confiait aux travailleurs chinois les tâches les plus dangereuses, comme "
    "la manipulation de la nitroglycérine explosive servant à faire éclater la roche massive. "
    "Bibliothèque et Archives Canada dit la même chose du travail aux explosifs. La "
    "bibliothèque de l'UBC consigne qu'on leur assignait des tâches dangereuses comme le "
    "percement de tunnels à la dynamite, et que les autorités canadiennes de l'époque les "
    "décrivaient comme des machines vivantes."))
a.h3(T("How many died — five official answers",
       "Combien sont morts — cinq réponses officielles"))
a.p(T(
    "This is the most contested figure in the whole subject, and the disagreement is between "
    "government sources, not between government and outsiders. Every one of the statements "
    "below is official. They are printed together because picking one of them would be a "
    "choice this page has no basis to make.",
    "C'est le chiffre le plus contesté de tout le sujet, et le désaccord oppose des sources "
    "gouvernementales entre elles, non le gouvernement à des tiers. Chacune des déclarations "
    "ci-dessous est officielle. Elles sont imprimées ensemble parce qu'en choisir une seule "
    "serait un choix que cette page n'a aucun moyen de justifier."))
a.table(
    [T("Who says it", "Qui le dit"), T("What it says", "Ce qui est dit")],
    [[T("Parks Canada", "Parcs Canada"),
      T("\"Hundreds of Chinese died from accidents or illness, for the work was dangerous and "
        "living conditions poor.\"",
        "« Des centaines de Chinois sont morts d'accidents ou de maladie, car le travail était "
        "dangereux et les conditions de vie mauvaises. »")],
     [T("Library and Archives Canada", "Bibliothèque et Archives Canada"),
      T("\"It is estimated that the number of Chinese workers who died is between 600 and "
        "800.\"",
        "« On estime que le nombre de travailleurs chinois morts se situe entre 600 et 800. »")],
     [T("Prime Minister of Canada, 22 June 2006",
        "Premier ministre du Canada, 22 juin 2006"),
      T("\"Tragically, some one thousand Chinese labourers died building the CPR.\"",
        "« Tragiquement, quelque mille ouvriers chinois sont morts en bâtissant le Canadien "
        "Pacifique. »")],
     [T("Canadian Heritage", "Patrimoine canadien"),
      T("\"The death count of Chinese workers over the entire construction period has been "
        "estimated to be between 600 and 2,200 workers.\"",
        "« On a estimé le nombre de travailleurs chinois morts sur l'ensemble de la période de "
        "construction entre 600 et 2 200 travailleurs. »")],
     [T("Province of British Columbia", "Province de la Colombie-Britannique"),
      T("\"Hundreds of Chinese Canadians working on the railway died from accidents, winter "
        "cold, illness and malnutrition.\"",
        "« Des centaines de Canadiens d'origine chinoise qui travaillaient au chemin de fer "
        "sont morts d'accidents, du froid de l'hiver, de maladie et de malnutrition. »")],
     [T("Andrew Onderdonk, the contractor, quoted by the Canadian Museum of History",
        "Andrew Onderdonk, l'entrepreneur, cité par le Musée canadien de l'histoire"),
      T("Three Chinese workers died for every kilometre of track laid in the Fraser Canyon "
        "alone.",
        "Trois travailleurs chinois sont morts pour chaque kilomètre de voie posée dans le "
        "seul canyon du Fraser.")],
     [T("UBC Library", "Bibliothèque de l'UBC"),
      T("\"The exact number of lives lost will never be known, as the CPR omitted Chinese "
        "workers from their official accident reports.\"",
        "« Le nombre exact de vies perdues ne sera jamais connu, car le Canadien Pacifique a "
        "exclu les travailleurs chinois de ses rapports d'accident officiels. »")]],
    label=T("What official sources say about Chinese worker deaths on the railway — scroll "
            "sideways to see all of it",
            "Ce que disent les sources officielles sur la mort de travailleurs chinois au "
            "chemin de fer — faites défiler latéralement pour tout voir"))
a.p(T(
    "That last line is the reason for all the others. The company kept the record, and the "
    "company left these men out of it. The defensible published range therefore runs from "
    "hundreds at the low end to 2,200 at the high end, with the Government of Canada's own "
    "two most-quoted figures being 600 to 800 and some one thousand. A page that prints a "
    "single number is not being more precise. It is choosing.",
    "Cette dernière ligne explique toutes les autres. La compagnie tenait le registre, et la "
    "compagnie a laissé ces hommes en dehors. La fourchette publiée défendable va donc de "
    "centaines au bas de l'échelle à 2 200 au haut, les deux chiffres les plus cités du "
    "gouvernement du Canada lui-même étant de 600 à 800 et quelque mille. Une page qui "
    "imprime un seul nombre n'est pas plus précise. Elle choisit."))
a.p(T(
    "Two other groups appear in the record without numbers. Parks Canada confirms Aboriginal "
    "people were employed on the railway, but no official source found here gives a figure "
    "for Indigenous workers, and BC Archives holds a photograph captioned as the first First "
    "Nations man employed on the Canadian Pacific Railway, taken after the railway was "
    "finished and the man was unemployed. And no official source gives a death toll for "
    "non-Chinese workers either; only individual incidents are documented.",
    "Deux autres groupes figurent au dossier sans chiffres. Parcs Canada confirme que des "
    "Autochtones ont été employés au chemin de fer, mais aucune source officielle trouvée ici "
    "ne donne de nombre pour les travailleurs autochtones, et les archives de la "
    "Colombie-Britannique conservent une photographie légendée comme celle du premier homme "
    "des Premières Nations employé au chemin de fer Canadien du Pacifique, prise après "
    "l'achèvement du chemin de fer, alors que l'homme était sans emploi. Et aucune source "
    "officielle ne donne non plus de bilan de morts pour les travailleurs non chinois ; seuls "
    "des incidents isolés sont documentés."))
a.h3(T("Then came the head tax", "Puis vint la taxe d'entrée"))
a.p(T(
    "The Chinese Immigration Act was passed in 1885 — the same year as the last spike, as the "
    "work in British Columbia was winding down. A Royal Commission on Chinese Immigration had "
    "sat through the summer of 1884 under J.A. Chapleau and J.H. Gray, heard 51 witnesses, "
    "found that the Chinese were judged by unfair standards and subject to sweeping "
    "generalizations about their character and habits, rejected outright exclusion, and "
    "recommended a $10 duty. Parliament imposed $50. The Province of British Columbia writes "
    "that almost immediately upon completion of the CPR, pressure from the provincial "
    "legislature led to the enactment of the Act.",
    "La Loi de l'immigration chinoise a été adoptée en 1885 — la même année que le dernier "
    "crampon, alors que les travaux en Colombie-Britannique tiraient à leur fin. Une "
    "commission royale sur l'immigration chinoise avait siégé pendant l'été 1884 sous "
    "J.A. Chapleau et J.H. Gray, entendu 51 témoins, conclu que les Chinois étaient jugés "
    "selon des critères injustes et soumis à des généralisations grossières sur leur caractère "
    "et leurs habitudes, rejeté l'exclusion pure et simple et recommandé un droit de 10 $. Le "
    "Parlement a imposé 50 $. La Province de la Colombie-Britannique écrit que, presque "
    "immédiatement après l'achèvement du Canadien Pacifique, la pression de l'assemblée "
    "législative provinciale a mené à l'adoption de la loi."))
a.p(T(
    "The tax rose to $100 and then to $500 — the equivalent of two years' wages, in the words "
    "of the 2006 address — and stayed in place until 1923. The sources disagree slightly on "
    "the first increase: Pier 21 and the 2006 address say 1900, while the Province of British "
    "Columbia says 1901. British Columbia also states that the province received "
    "approximately 40 per cent of the $23 million total nominal tax revenue collected, and "
    "that over 97,000 Chinese immigrants came to Canada during the head tax years. In 1923 "
    "the tax was replaced by the exclusion Act, in force for 24 years and repealed on 14 May "
    "1947.",
    "La taxe est passée à 100 $, puis à 500 $ — l'équivalent de deux années de salaire, selon "
    "les mots de l'allocution de 2006 — et est restée en vigueur jusqu'en 1923. Les sources "
    "divergent légèrement sur la première hausse : le Quai 21 et l'allocution de 2006 disent "
    "1900, tandis que la Province de la Colombie-Britannique dit 1901. La "
    "Colombie-Britannique indique aussi que la province a reçu environ 40 pour cent des "
    "23 millions de dollars de recettes fiscales nominales totales perçues, et que plus de "
    "97 000 immigrants chinois sont venus au Canada pendant les années de la taxe d'entrée. En "
    "1923, la taxe a été remplacée par la loi d'exclusion, en vigueur pendant 24 ans et "
    "abrogée le 14 mai 1947."))
a.p(T(
    "On 22 June 2006 the Prime Minister rose in the House of Commons and said that on behalf "
    "of all Canadians and the Government of Canada, the government offered a full apology to "
    "Chinese Canadians for the head tax and expressed its deepest sorrow for the subsequent "
    "exclusion of Chinese immigrants. Redress followed: $20,000 to living head tax payers and "
    "to living spouses of deceased payers, a $24 million community historical recognition "
    "program and a $10 million national one. Read the apology for what it says. It was an "
    "apology for the head tax and the exclusion. The railway appears in that speech as "
    "context, not as the thing being apologised for.",
    "Le 22 juin 2006, le premier ministre s'est levé à la Chambre des communes et a déclaré "
    "qu'au nom de tous les Canadiens et du gouvernement du Canada, le gouvernement présentait "
    "des excuses complètes aux Canadiens d'origine chinoise pour la taxe d'entrée et "
    "exprimait ses plus profonds regrets pour l'exclusion subséquente des immigrants chinois. "
    "Une réparation a suivi : 20 000 $ aux payeurs de la taxe encore vivants et aux conjoints "
    "survivants des payeurs décédés, un programme communautaire de reconnaissance historique "
    "de 24 millions de dollars et un programme national de 10 millions. Il faut lire ces "
    "excuses pour ce qu'elles disent. C'étaient des excuses pour la taxe d'entrée et "
    "l'exclusion. Le chemin de fer figure dans ce discours comme contexte, non comme l'objet "
    "des excuses."))

# ------------------------------------------------------------------ 7
a.h2(T("Who planned it", "Qui l'a planifié"))
a.h3(T("Sandford Fleming and the surveys", "Sandford Fleming et les levés"))
a.p(T(
    "Fleming was appointed Chief Engineer in April 1871 and told to find whether a railway was "
    "practicable between the seat of Government and the Pacific coast, and where the best "
    "route could be had. The 1882 Royal Commission records what that meant in the first year: "
    "about 21 survey parties, nearly 800 men, each party expected to cover about seventy-five "
    "miles per season. Parks Canada puts the whole reconnaissance effort at 74,000 kilometres, "
    "or 46,000 miles, of surveys across more than a dozen passes, all of them done on foot and "
    "horseback.",
    "Fleming a été nommé ingénieur en chef en avril 1871 et chargé de déterminer si un chemin "
    "de fer était réalisable entre le siège du gouvernement et la côte du Pacifique, et où se "
    "trouvait le meilleur tracé. La commission royale de 1882 consigne ce que cela a signifié "
    "la première année : environ 21 équipes de levés, près de 800 hommes, chaque équipe devant "
    "couvrir environ soixante-quinze milles par saison. Parcs Canada chiffre l'ensemble de "
    "l'effort de reconnaissance à 74 000 kilomètres, ou 46 000 milles, de levés à travers plus "
    "d'une douzaine de cols, tous faits à pied et à cheval."))
a.p(T(
    "By April 1872 Fleming's report found no serious engineering difficulty between Ottawa and "
    "Lake Superior, and an Order in Council of 2 April 1872 adopted the Yellow Head Pass for "
    "the Rockies on a planned route of 2,730 miles. Parks Canada, on its plaque for him, "
    "records that he was survey and construction engineer for the Intercolonial Railway and "
    "the Canadian Pacific from 1871 to 1880, and that he championed standard time.",
    "En avril 1872, le rapport de Fleming concluait qu'il n'existait aucune difficulté "
    "technique sérieuse entre Ottawa et le lac Supérieur, et un décret du 2 avril 1872 a "
    "adopté le col Yellow Head pour les Rocheuses, sur un tracé prévu de 2 730 milles. Parcs "
    "Canada, sur la plaque qui lui est consacrée, consigne qu'il a été ingénieur des levés et "
    "de la construction pour le chemin de fer Intercolonial et pour le Canadien Pacifique de "
    "1871 à 1880, et qu'il a défendu l'heure normale."))
a.h3(T("The syndicate of 1880", "Le syndicat de 1880"))
a.p(T(
    "The group of financiers who took the 1880 contract is usually named as George Stephen, "
    "Donald Smith and James J. Hill. That naming needs a caution rather than a footnote. Among "
    "the official Canadian sources gathered for this page, only Donald Smith is identified, "
    "and only as a director of the Canadian Pacific Railway — that is how the Government of "
    "Canada's own citizenship study guide describes him, and how the Canadian Museum of "
    "History describes him. No Parks Canada plaque or federal page found here names the full "
    "membership of the syndicate. Treat the other names as belonging to the general literature "
    "rather than to the official record used on this page.",
    "On nomme habituellement le groupe de financiers qui a obtenu le contrat de 1880 : George "
    "Stephen, Donald Smith et James J. Hill. Cette attribution appelle une mise en garde "
    "plutôt qu'une note de bas de page. Parmi les sources officielles canadiennes réunies pour "
    "cette page, seul Donald Smith est identifié, et seulement comme administrateur du chemin "
    "de fer Canadien du Pacifique — c'est ainsi que le décrit le guide d'étude de la "
    "citoyenneté du gouvernement du Canada, et ainsi que le décrit le Musée canadien de "
    "l'histoire. Aucune plaque de Parcs Canada ni page fédérale trouvée ici ne nomme "
    "l'ensemble des membres du syndicat. Il faut donc considérer les autres noms comme "
    "appartenant à la littérature générale plutôt qu'au dossier officiel utilisé ici."))
a.h3(T("William Cornelius Van Horne", "William Cornelius Van Horne"))
a.p(T(
    "Van Horne was born in Chelsea, Illinois, in 1843 and died in Montréal in 1915. His Parks "
    "Canada plaque, at Windsor Station in Montréal, calls him dynamic and imaginative, and "
    "sets out the sequence of his jobs: General Manager, Vice President, and then President of "
    "the Canadian Pacific Railway during its formative years. He became general manager in "
    "1882. Parks Canada's record gives his presidency as 1888 to 1899, so he was not the "
    "company's first president.",
    "Van Horne est né à Chelsea, en Illinois, en 1843 et mort à Montréal en 1915. Sa plaque de "
    "Parcs Canada, à la gare Windsor de Montréal, le qualifie de dynamique et imaginatif, et "
    "expose la suite de ses fonctions : directeur général, vice-président, puis président du "
    "chemin de fer Canadien du Pacifique pendant ses années de formation. Il est devenu "
    "directeur général en 1882. La fiche de Parcs Canada situe sa présidence de 1888 à 1899 ; "
    "il n'a donc pas été le premier président de la compagnie."))
a.p(T(
    "His method shows up in two places in the record. UBC's timeline states that under him, "
    "500 miles of track were built in the prairies in 1882 alone. And Parks Canada records his "
    "route thinking: he had decided a more direct Pacific route was necessary to reduce the "
    "costs of construction and operation. That decision is why the line goes where it goes "
    "through the mountains, and it is also why the Selkirks had to be crossed at all.",
    "Sa méthode apparaît à deux endroits dans le dossier. La chronologie de l'UBC indique que, "
    "sous sa direction, 500 milles de voie ont été construits dans les Prairies pour la seule "
    "année 1882. Et Parcs Canada consigne sa logique de tracé : il avait décidé qu'un trajet "
    "plus direct vers le Pacifique était nécessaire pour réduire les coûts de construction et "
    "d'exploitation. Cette décision explique pourquoi la ligne passe là où elle passe dans les "
    "montagnes, et pourquoi il a fallu traverser les Selkirk."))
a.h3(T("Major Rogers and Rogers Pass", "Le major Rogers et le col Rogers"))
a.p(T(
    "Parks Canada describes Albert Bowman Rogers as a Massachusetts-born railway surveyor with "
    "an engineering degree from Brown University who had taught at Yale, quick-tempered and "
    "experienced only in prairie surveying, and disliked by other engineers and by his workers. "
    "In the summer of 1881 he searched the western Selkirks with his Shuswap guides — Parks "
    "Canada names the guides, and any account that has him finding the pass alone is leaving "
    "them out. In 1882 he climbed to the summit from the east side and confirmed the pass he "
    "had spotted the year before. He received a $5,000 cheque and a permanent place in Canadian "
    "geography.",
    "Parcs Canada décrit Albert Bowman Rogers comme un arpenteur ferroviaire né au "
    "Massachusetts, diplômé en génie de l'Université Brown et ayant enseigné à Yale, "
    "soupe au lait et expérimenté uniquement en levés de prairie, mal aimé des autres "
    "ingénieurs et de ses propres travailleurs. À l'été 1881, il a exploré l'ouest des Selkirk "
    "avec ses guides shuswap — Parcs Canada nomme les guides, et tout récit qui lui fait "
    "trouver le col seul les laisse de côté. En 1882, il a gravi le sommet par le versant est "
    "et confirmé le col qu'il avait repéré l'année précédente. Il a reçu un chèque de 5 000 $ "
    "et une place permanente dans la géographie canadienne."))
a.p(T(
    "The pass where the last spike was driven has a different history again. Parks Canada "
    "records that Eagle Pass was noted in the summer of 1865 by Walter Moberly, assistant "
    "surveyor-general of British Columbia, who noted the flight of eagles through a break in "
    "the Gold Range. After 1881 it was chosen as the railway's route between the Columbia and "
    "Fraser drainage basins.",
    "Le col où le dernier crampon a été planté a encore une autre histoire. Parcs Canada "
    "consigne que le col Eagle a été remarqué à l'été 1865 par Walter Moberly, arpenteur "
    "général adjoint de la Colombie-Britannique, qui a noté le vol d'aigles à travers une "
    "brèche de la chaîne Gold. Après 1881, il a été retenu comme tracé du chemin de fer entre "
    "les bassins versants du Columbia et du Fraser."))

# ------------------------------------------------------------------ 8
a.h2(T("The land, and a shortcut worth correcting",
       "Les terres, et un raccourci qu'il faut corriger"))
a.p(T(
    "It is often said that the numbered treaties were signed to make way for the railway. The "
    "dates do not support it, and the government's own research says so.",
    "On dit souvent que les traités numérotés ont été signés pour faire place au chemin de "
    "fer. Les dates ne le confirment pas, et la recherche du gouvernement lui-même le dit."))
a.p(T(
    "Crown-Indigenous Relations and Northern Affairs Canada dates Treaty 4 to 1874 at Fort "
    "Qu'Appelle, Treaty 5 to 1875, Treaty 6 to 1876 on the North Saskatchewan River and "
    "Treaty 7 to 22 September 1877 at the Blackfoot Crossing of the Bow River. Main-line "
    "construction across the prairies belongs to a later period: the company was incorporated "
    "on 16 February 1881, and the prairie section was completed on 18 August 1883. The "
    "department's own Treaty Research Report on Treaty Four states it directly — at the time "
    "of that treaty, railway construction through the West had not yet begun.",
    "Relations Couronne-Autochtones et Affaires du Nord Canada date le Traité 4 de 1874 à Fort "
    "Qu'Appelle, le Traité 5 de 1875, le Traité 6 de 1876 sur la rivière Saskatchewan Nord et "
    "le Traité 7 du 22 septembre 1877 au passage des Pieds-Noirs de la rivière Bow. La "
    "construction de la ligne principale à travers les Prairies appartient à une période "
    "postérieure : la compagnie a été constituée le 16 février 1881 et la section des Prairies "
    "a été achevée le 18 août 1883. Le rapport de recherche du ministère sur le Traité Quatre "
    "le dit directement — à l'époque de ce traité, la construction ferroviaire dans l'Ouest "
    "n'avait pas encore commencé."))
a.p(T(
    "So what does the official record give as the reasons? CIRNAC lists establishing "
    "jurisdiction over Aboriginal lands after the acquisition of the Hudson's Bay Company "
    "charter, the opening of the North and access to valuable natural resources, and the "
    "disruption of a telegraph line that prompted the Treaty 6 negotiations. Its Treaty Four "
    "research report adds that the Crown wanted treaties because officials feared the "
    "possibility of Indian wars and the adverse effect such a threat would present to the "
    "settlement and development of the North-West, and that the purpose was to extinguish "
    "Indian title in order to clear any obstructions to the Crown's title. On the Indigenous "
    "side, the report says the big danger was Indian starvation, from the reduction in the "
    "numbers of buffalo and other animals.",
    "Que donne alors le dossier officiel comme raisons ? RCAANC énumère l'établissement de la "
    "compétence sur les terres autochtones après l'acquisition de la charte de la Compagnie de "
    "la Baie d'Hudson, l'ouverture du Nord et l'accès à de précieuses ressources naturelles, "
    "ainsi que la perturbation d'une ligne télégraphique qui a provoqué les négociations du "
    "Traité 6. Son rapport de recherche sur le Traité Quatre ajoute que la Couronne voulait "
    "des traités parce que les fonctionnaires craignaient la possibilité de guerres indiennes "
    "et l'effet néfaste d'une telle menace sur la colonisation et le développement du "
    "Nord-Ouest, et que l'objectif était d'éteindre le titre indien afin de lever tout "
    "obstacle au titre de la Couronne. Du côté autochtone, le rapport indique que le grand "
    "danger était la famine, causée par la diminution du nombre de bisons et d'autres "
    "animaux."))
a.callout(T(
    "<strong>Parks Canada says this about the bison, on its own page for Sir John A. "
    "Macdonald.</strong> His government used the disappearance of the bison to force First "
    "Nations to take treaty and settle on reserves. The same page records that his government "
    "founded a national system of Indian Residential Schools, which represented a policy of "
    "aggressive assimilation that the Truth and Reconciliation Commission of Canada described "
    "in 2015 as cultural genocide.",
    "<strong>Voici ce que dit Parcs Canada au sujet du bison, dans sa propre page consacrée à "
    "sir John A. Macdonald.</strong> Son gouvernement s'est servi de la disparition du bison "
    "pour forcer les Premières Nations à conclure des traités et à s'établir dans des "
    "réserves. La même page consigne que son gouvernement a fondé un système national de "
    "pensionnats indiens, qui représentait une politique d'assimilation agressive que la "
    "Commission de vérité et réconciliation du Canada a décrite en 2015 comme un génocide "
    "culturel."))
a.p(T(
    "One more correction while we are here. The texts of Treaties 4, 6 and 7 as published by "
    "CIRNAC contain no railway clause. Treaty 6 contains a general public-works clause, saying "
    "that such sections of the reserves as may at any time be required for public works or "
    "buildings, of what nature soever, may be appropriated for that purpose by Her Majesty's "
    "Government of the Dominion of Canada, due compensation being made for the value of any "
    "improvements thereon. That is a general clause. It should not be upgraded into a railway "
    "clause.",
    "Une correction de plus pendant que nous y sommes. Les textes des Traités 4, 6 et 7 tels "
    "que publiés par RCAANC ne contiennent aucune clause ferroviaire. Le Traité 6 contient une "
    "clause générale sur les travaux publics, portant que les parties des réserves qui "
    "pourraient en tout temps être requises pour des travaux ou des bâtiments publics, de "
    "quelque nature que ce soit, peuvent être affectées à cette fin par le gouvernement de Sa "
    "Majesté du Dominion du Canada, moyennant une juste compensation pour la valeur des "
    "améliorations qui s'y trouvent. C'est une clause générale. Il ne faut pas la transformer "
    "en clause ferroviaire."))
a.p(T(
    "None of which makes the railway innocent of what happened on the plains. Library and "
    "Archives Canada counts among the price of building it the displacement of Canada's First "
    "Nations, and gives one specific example: roughly 5,000 First Nations and Métis Nation "
    "peoples were expelled from the Cypress Hills of Saskatchewan in the 1880s during the "
    "construction phase. Parks Canada, writing about Batoche, lists railway policy among the "
    "grievances behind the discontent of 1885, and says that afterwards the Métis community "
    "survived but lost economic viability, with the railway's placement at Duck Lake "
    "signalling declining prosperity. The honest statement is that the treaties came first and "
    "the railway came into a West already being surveyed, policed and settled — and that both "
    "belonged to the same federal project.",
    "Rien de tout cela ne rend le chemin de fer innocent de ce qui s'est passé dans les "
    "plaines. Bibliothèque et Archives Canada compte parmi le prix de sa construction le "
    "déplacement des Premières Nations du Canada, et donne un exemple précis : environ 5 000 "
    "membres des Premières Nations et de la Nation métisse ont été expulsés des collines "
    "Cypress, en Saskatchewan, dans les années 1880, pendant la phase de construction. Parcs "
    "Canada, en écrivant sur Batoche, place la politique ferroviaire parmi les griefs à "
    "l'origine du mécontentement de 1885, et indique que, par la suite, la communauté métisse "
    "a survécu mais a perdu sa viabilité économique, l'emplacement du chemin de fer à Duck "
    "Lake annonçant le déclin de sa prospérité. L'énoncé honnête est que les traités sont "
    "venus d'abord et que le chemin de fer est arrivé dans un Ouest déjà arpenté, surveillé et "
    "colonisé — et que les deux appartenaient au même projet fédéral."))

# ------------------------------------------------------------------ 9
a.h2(T("1885, and the troops on the line", "1885, et les troupes sur la ligne"))
a.p(T(
    "The North-West Resistance ran from March to June 1885, while the railway was still "
    "unfinished. The Canadian War Museum's chronology says Ottawa responded by rushing 8,000 "
    "regular and militia troops, mainly by rail. The Department of National Defence puts the "
    "significance this way: the existence of telegraph lines and a near-complete rail link to "
    "Ottawa meant that information and troops could travel very rapidly to respond to the "
    "crisis — a contrast it draws with the Red River Expedition of 1870, which took months. "
    "Library and Archives Canada, describing the same year, calls it a partially completed "
    "Canadian Pacific Railroad.",
    "La Résistance du Nord-Ouest s'est déroulée de mars à juin 1885, alors que le chemin de "
    "fer n'était pas encore terminé. La chronologie du Musée canadien de la guerre indique "
    "qu'Ottawa a réagi en dépêchant en hâte 8 000 soldats réguliers et miliciens, "
    "principalement par train. Le ministère de la Défense nationale en expose ainsi la portée : "
    "l'existence de lignes télégraphiques et d'une liaison ferroviaire presque complète avec "
    "Ottawa faisait que l'information et les troupes pouvaient se déplacer très rapidement "
    "pour répondre à la crise — un contraste qu'il établit avec l'expédition de la rivière "
    "Rouge de 1870, qui avait pris des mois. Bibliothèque et Archives Canada, en décrivant la "
    "même année, parle d'un chemin de fer Canadien du Pacifique partiellement achevé."))
a.p(T(
    "Notice what those three official sources do and do not say. They agree the line was in "
    "use and not finished. None of them says how many days the journey took, and none says how "
    "many gaps there were north of Lake Superior or how long they were. Popular accounts are "
    "full of both figures. This page does not repeat them, because no official source in this "
    "research gives them.",
    "Remarquez ce que ces trois sources officielles disent et ne disent pas. Elles s'accordent "
    "sur le fait que la ligne était utilisée sans être terminée. Aucune ne dit combien de "
    "jours le trajet a pris, et aucune ne dit combien de brèches il y avait au nord du lac "
    "Supérieur ni quelle était leur longueur. Les récits populaires regorgent de ces deux "
    "chiffres. Cette page ne les répète pas, parce qu'aucune source officielle de cette "
    "recherche ne les donne."))
a.p(T(
    "The events themselves are documented. Parks Canada records five major engagements — Duck "
    "Lake, Fish Creek, Cut Knife Hill, Batoche and Frenchman's Butte — and the North-West "
    "Field Force of 800 troops under General Frederick Middleton. Batoche fell on 12 May 1885. "
    "Riel surrendered on 15 May, Poundmaker on 26 May and Big Bear on 4 July. Riel was hanged "
    "at Regina on 16 November 1885. On 27 November 1885, Parks Canada records, Fort Battleford "
    "was witness to the largest mass hanging in Canadian history, when eight Indigenous men "
    "were executed.",
    "Les événements eux-mêmes sont documentés. Parcs Canada consigne cinq engagements majeurs "
    "— Duck Lake, Fish Creek, Cut Knife Hill, Batoche et Frenchman's Butte — et le Corps de "
    "campagne du Nord-Ouest, fort de 800 soldats sous le général Frederick Middleton. Batoche "
    "est tombé le 12 mai 1885. Riel s'est rendu le 15 mai, Poundmaker le 26 mai et Big Bear le "
    "4 juillet. Riel a été pendu à Regina le 16 novembre 1885. Le 27 novembre 1885, consigne "
    "Parcs Canada, le fort Battleford a été témoin de la plus grande pendaison collective de "
    "l'histoire canadienne, lorsque huit hommes autochtones ont été exécutés."))

# ------------------------------------------------------------------ 10
a.h2(T("The engineering", "Le génie civil"))
a.h3(T("North of Lake Superior", "Au nord du lac Supérieur"))
a.p(T(
    "Fleming's 1872 report found no serious engineering difficulty between Ottawa and Lake "
    "Superior. That was a survey-stage judgement, made before anyone tried to build there. "
    "What the section actually took is one of the gaps in the official record: no government or "
    "Crown-agency page found in this research describes the muskeg, the rock cutting, the "
    "explosives used or the cost of the Canadian Shield section. The one concrete figure "
    "available is a contract — Sifton and Ward, Fort William to Shebandowan, 45 miles, approved "
    "3 April 1875, for $406,194.",
    "Le rapport de Fleming de 1872 ne trouvait aucune difficulté technique sérieuse entre "
    "Ottawa et le lac Supérieur. C'était un jugement d'étape de levé, porté avant que "
    "quiconque tente d'y construire. Ce que cette section a réellement exigé est l'une des "
    "lacunes du dossier officiel : aucune page gouvernementale ou d'organisme de la Couronne "
    "trouvée dans cette recherche ne décrit la fondrière, le percement de la roche, les "
    "explosifs utilisés ou le coût de la section du Bouclier canadien. Le seul chiffre concret "
    "disponible est un contrat — Sifton et Ward, de Fort William à Shebandowan, 45 milles, "
    "approuvé le 3 avril 1875, pour 406 194 $."))
a.h3(T("The Rockies, the Big Hill and the Spiral Tunnels",
       "Les Rocheuses, la Grande Côte et les tunnels en spirale"))
a.p(T(
    "In 1881 the company adopted the Kicking Horse Pass in place of the surveyed Yellowhead "
    "route. Canada's Historic Places calls that a pivotal shift that altered the location of "
    "the line across western Canada and dramatically affected the development of the West. The "
    "pass itself had been documented during the Palliser expedition of 1857 to 1860 and named "
    "after an incident in which the expedition surgeon, Dr James Hector, was struck by his "
    "horse.",
    "En 1881, la compagnie a adopté le col Kicking Horse à la place du tracé levé du "
    "Yellowhead. Lieux patrimoniaux du Canada qualifie ce changement de tournant qui a modifié "
    "l'emplacement de la ligne dans l'Ouest canadien et profondément influé sur le "
    "développement de l'Ouest. Le col lui-même avait été documenté pendant l'expédition "
    "Palliser de 1857 à 1860 et nommé à la suite d'un incident au cours duquel le chirurgien "
    "de l'expédition, le docteur James Hector, a été frappé par son cheval."))
a.p(T(
    "The price of that choice was the Big Hill. Parks Canada gives its grade as 4.5 percent and "
    "records what happened in 1884: the first train to attempt the hill derailed, tragically "
    "killing three workers. Three spur lines were created to divert runaway trains. The Big "
    "Hill was used for approximately 25 years before being abandoned.",
    "Le prix de ce choix a été la Grande Côte. Parcs Canada en donne la pente à 4,5 pour cent "
    "et consigne ce qui s'est passé en 1884 : le premier train à s'attaquer à la côte a "
    "déraillé, tuant tragiquement trois travailleurs. Trois voies d'évitement ont été créées "
    "pour dévier les trains emballés. La Grande Côte a servi pendant environ 25 ans avant "
    "d'être abandonnée."))
a.p(T(
    "The replacement was the Spiral Tunnels, designed by Assistant Chief Engineer "
    "J.E. Schwitzer on a Swiss model and completed in 1909 — a quarter-century after the last "
    "spike, which is why they are not part of the original construction story. Parks Canada "
    "gives the Lower Spiral Tunnel under Mount Ogden as 891 metres long, gaining 15 metres and "
    "spiralling left, and the Upper Spiral Tunnel under Cathedral Mountain as 991 metres, "
    "gaining 17 metres and spiralling right. They are in Yoho National Park, in British "
    "Columbia, not in Alberta. Between 25 and 30 trains pass through them daily today. UBC "
    "Library records the human cost of that work too: hundreds of workers, primarily Chinese, "
    "died from exposure to freezing temperatures, illness and violent accidents.",
    "Le remplacement a été les tunnels en spirale, conçus par l'ingénieur en chef adjoint "
    "J.E. Schwitzer sur un modèle suisse et achevés en 1909 — un quart de siècle après le "
    "dernier crampon, ce qui explique qu'ils ne fassent pas partie de la construction "
    "d'origine. Parcs Canada donne le tunnel en spirale inférieur, sous le mont Ogden, à 891 "
    "mètres de longueur, avec un gain de 15 mètres et une spirale vers la gauche, et le tunnel "
    "en spirale supérieur, sous la montagne Cathedral, à 991 mètres, avec un gain de 17 mètres "
    "et une spirale vers la droite. Ils se trouvent dans le parc national Yoho, en "
    "Colombie-Britannique, et non en Alberta. De 25 à 30 trains les traversent chaque jour "
    "aujourd'hui. La bibliothèque de l'UBC consigne aussi le coût humain de ces travaux : des "
    "centaines de travailleurs, principalement chinois, sont morts d'exposition au froid "
    "glacial, de maladie et d'accidents violents."))
a.h3(T("The Selkirks and Rogers Pass", "Les Selkirk et le col Rogers"))
a.p(T(
    "East of the pass Parks Canada counts eight major bridges, built under James Ross. Stoney "
    "Creek Bridge was the tallest bridge structure in the world at the time, and Mountain Creek "
    "Bridge required millions of board feet of lumber. The line through Rogers Pass was "
    "completed in the fall of 1885.",
    "À l'est du col, Parcs Canada dénombre huit grands ponts, bâtis sous la direction de James "
    "Ross. Le pont Stoney Creek était alors la plus haute structure de pont au monde, et le "
    "pont Mountain Creek a exigé des millions de pieds-planche de bois. La ligne traversant le "
    "col Rogers a été achevée à l'automne 1885."))
a.p(T(
    "Then the railway had to keep it open. An average of more than 12 metres, or 40 feet, of "
    "snow fell on this rail line every winter. The company built snowsheds on the model of the "
    "Central Pacific's at Donner Pass, over 6.5 kilometres of them in total, which Parks Canada "
    "says cost the railway a fortune to build and maintain. Rotary snow plows, invented in "
    "Ontario in 1885, were added to the rolling stock in 1888. It was not enough. Parks Canada "
    "records that between 1885 and 1911 deaths caused by avalanches totalled over 200, and that "
    "a single slide on 4 March 1910 killed 58 railway workers who were clearing snow from an "
    "earlier one. The Connaught Tunnel opened on 13 December 1916 — Parks Canada describes it "
    "as eight kilometres on one page and nine on another — and the surface line over the pass "
    "was abandoned in 1917.",
    "Ensuite, le chemin de fer devait la garder ouverte. En moyenne, plus de 12 mètres, ou 40 "
    "pieds, de neige tombaient sur cette ligne chaque hiver. La compagnie a bâti des "
    "paraneiges sur le modèle de ceux du Central Pacific au col Donner, plus de 6,5 kilomètres "
    "au total, dont Parcs Canada dit qu'ils ont coûté une fortune au chemin de fer à "
    "construire et à entretenir. Les chasse-neige rotatifs, inventés en Ontario en 1885, ont "
    "été ajoutés au matériel roulant en 1888. Cela n'a pas suffi. Parcs Canada consigne "
    "qu'entre 1885 et 1911 les morts causées par les avalanches ont dépassé 200, et qu'une "
    "seule coulée, le 4 mars 1910, a tué 58 travailleurs du rail qui déblayaient la neige "
    "d'une avalanche précédente. Le tunnel Connaught a ouvert le 13 décembre 1916 — Parcs "
    "Canada le décrit comme long de huit kilomètres sur une page et de neuf sur une autre — et "
    "la ligne de surface franchissant le col a été abandonnée en 1917."))
a.p(T(
    "One material figure is worth quoting with its source attached, because it appears in "
    "exactly one official place. Library and Archives Canada says more than 30 million iron "
    "spikes were used to construct the Canadian Pacific Railway. Nothing else in this research "
    "corroborates it, and no official quantity of explosives, and no total for tunnels or "
    "bridges on the whole line, is published anywhere.",
    "Un chiffre de matériaux mérite d'être cité avec sa source, parce qu'il n'apparaît qu'à un "
    "seul endroit officiel. Bibliothèque et Archives Canada indique que plus de 30 millions de "
    "crampons de fer ont servi à construire le chemin de fer Canadien du Pacifique. Rien "
    "d'autre dans cette recherche ne le corrobore, et aucune quantité officielle d'explosifs, "
    "ni aucun total de tunnels ou de ponts pour l'ensemble de la ligne, n'est publié nulle "
    "part."))
a.p(T(
    "One lasting side effect. Parks Canada notes that Glacier and Yoho national parks were "
    "created in 1886 because of the railway, the country's second and third national parks "
    "after Banff in 1885.",
    "Un effet secondaire durable. Parcs Canada souligne que les parcs nationaux Glacier et "
    "Yoho ont été créés en 1886 grâce au chemin de fer, deuxième et troisième parcs nationaux "
    "du pays après Banff en 1885."))

# ------------------------------------------------------------------ 11
a.h2(T("The other transcontinentals, and how they ended",
       "Les autres transcontinentaux, et leur fin"))
a.p(T(
    "The Canadian Pacific was not the only line built across the country, and it was the only "
    "one that survived on its own. Between the 1890s and 1915 two more transcontinental "
    "systems were built, and both failed.",
    "Le Canadien Pacifique n'a pas été la seule ligne bâtie d'un bout à l'autre du pays, et il "
    "a été le seul à survivre par ses propres moyens. Entre les années 1890 et 1915, deux "
    "autres réseaux transcontinentaux ont été bâtis, et les deux ont échoué."))
a.p(T(
    "The Canadian Northern was the work of Sir William Mackenzie and Sir Donald Mann, both "
    "designated national historic persons in 1976. Manitoba's heritage study traces it from a "
    "first branch between Gladstone and Winnipegosis in 1897 to a line from Winnipeg to Port "
    "Arthur in 1902, and says that by 1910 it was competing successfully with the CPR across "
    "the prairies with significantly lower freight rates. The Canadian Transportation Agency "
    "gives its transcontinental construction as complete by 1915, and describes the company as "
    "struggling financially.",
    "Le Canadien du Nord a été l'oeuvre de sir William Mackenzie et de sir Donald Mann, tous "
    "deux désignés personnages d'importance historique nationale en 1976. L'étude patrimoniale "
    "du Manitoba en retrace le parcours, d'une première ligne secondaire entre Gladstone et "
    "Winnipegosis en 1897 jusqu'à une ligne de Winnipeg à Port Arthur en 1902, et indique qu'en "
    "1910 il concurrençait avec succès le Canadien Pacifique dans les Prairies grâce à des "
    "tarifs de fret nettement plus bas. L'Office des transports du Canada situe l'achèvement de "
    "sa construction transcontinentale en 1915 et décrit la compagnie comme en difficulté "
    "financière."))
a.p(T(
    "The second system came in two halves. The Grand Trunk Pacific built west, completing track "
    "from Winnipeg to Prince Rupert on 7 April 1914, to higher standards than its competitors, "
    "and using the Yellowhead Pass that Fleming's surveys had originally chosen. The National "
    "Transcontinental was the eastern half, built by the government from Winnipeg to Moncton "
    "and completed on 1 June 1915, then leased to the Grand Trunk Pacific. The Canadian "
    "Transportation Agency records the break in that arrangement bluntly: the Grand Trunk "
    "Pacific reneged on the 1915 deal to assume the National Transcontinental and offered the "
    "subsidiary to the government.",
    "Le second réseau est venu en deux moitiés. Le Grand Tronc Pacifique a construit vers "
    "l'ouest, achevant la voie de Winnipeg à Prince Rupert le 7 avril 1914, selon des normes "
    "plus élevées que ses concurrents, et empruntant le col Yellowhead que les levés de Fleming "
    "avaient d'abord retenu. Le Transcontinental National en était la moitié est, bâtie par "
    "l'État de Winnipeg à Moncton et achevée le 1er juin 1915, puis louée au Grand Tronc "
    "Pacifique. L'Office des transports du Canada consigne sans détour la rupture de cette "
    "entente : le Grand Tronc Pacifique est revenu sur l'accord de 1915 par lequel il devait "
    "reprendre le Transcontinental National et a offert la filiale au gouvernement."))
a.p(T(
    "A Royal Commission into railways and transportation was appointed in May 1916 — Alfred "
    "Holland Smith as chair, with Henry Lumley Drayton and William Mitchell Acworth — and "
    "reported in 1917 recommending that the lines be united into a single national railway. "
    "The Railway Act revision of 1919 incorporated the Canadian National Railways Company and "
    "brought in the Canadian Northern. The Grand Trunk Pacific was transferred to the Dominion "
    "in 1920. By 1923 the Grand Trunk and the Grand Trunk Pacific had been added and, in the "
    "Agency's words, the Canadian National Railways system was in operation. Through all of "
    "this the CPR was managed profitably compared to competitors and operated in the black.",
    "Une commission royale sur les chemins de fer et les transports a été nommée en mai 1916 — "
    "Alfred Holland Smith à la présidence, avec Henry Lumley Drayton et William Mitchell "
    "Acworth — et a recommandé en 1917 de réunir les lignes en un seul chemin de fer national. "
    "La révision de la Loi sur les chemins de fer de 1919 a constitué la Compagnie des chemins "
    "de fer nationaux du Canada et y a intégré le Canadien du Nord. Le Grand Tronc Pacifique a "
    "été transféré au Dominion en 1920. En 1923, le Grand Tronc et le Grand Tronc Pacifique "
    "s'y étaient ajoutés et, selon les mots de l'Office, le réseau des Chemins de fer "
    "nationaux du Canada était en exploitation. Pendant tout ce temps, le Canadien Pacifique "
    "était géré de façon rentable par rapport à ses concurrents et exploité de façon "
    "bénéficiaire."))
a.p(T(
    "What those two systems cost to build is not published. Dates for the Canadian Northern, "
    "the Grand Trunk Pacific and the National Transcontinental are officially available; dollar "
    "figures are not, on any accessible official page found in this research. The numbers may "
    "well be inside the printed 1917 Royal Commission report, which runs to six parts and could "
    "not be read in this session. Until it is read, this page states no cost for any of them.",
    "Ce que ces deux réseaux ont coûté à bâtir n'est pas publié. Les dates du Canadien du Nord, "
    "du Grand Tronc Pacifique et du Transcontinental National sont officiellement disponibles ; "
    "les montants en dollars ne le sont pas, sur aucune page officielle accessible trouvée dans "
    "cette recherche. Les chiffres se trouvent peut-être dans le rapport imprimé de la "
    "commission royale de 1917, qui compte six parties et n'a pas pu être lu dans le cadre de "
    "ce travail. Tant qu'il ne l'aura pas été, cette page n'énonce aucun coût pour l'un ou "
    "l'autre."))

# ------------------------------------------------------------------ 12
a.h2(T("What is not settled", "Ce qui n'est pas établi"))
a.p(T(
    "Other accounts of this railway carry single numbers where this page carries ranges or "
    "silence. Here is exactly why. Each item below is something no official source in this "
    "research states.",
    "D'autres récits de ce chemin de fer donnent des chiffres uniques là où cette page donne "
    "des fourchettes ou du silence. Voici précisément pourquoi. Chacun des éléments ci-dessous "
    "est une chose qu'aucune source officielle de cette recherche n'énonce."))
a.ul([
    T("<strong>A total construction cost for the Canadian Pacific Railway.</strong> Public "
      "funds, loans and land are published. A build cost is not.",
      "<strong>Un coût total de construction du chemin de fer Canadien du Pacifique.</strong> "
      "Les fonds publics, les prêts et les terres sont publiés. Un coût de construction ne "
      "l'est pas."),
    T("<strong>The cost measured against the economy or the federal budget of the day.</strong> "
      "Statistics Canada's historical railway series begin in 1946.",
      "<strong>Le coût rapporté à l'économie ou au budget fédéral de l'époque.</strong> Les "
      "séries ferroviaires historiques de Statistique Canada commencent en 1946."),
    T("<strong>A total or peak workforce for the project.</strong> The published figures are "
      "for the British Columbia section only.",
      "<strong>Un effectif total ou maximal pour le projet.</strong> Les chiffres publiés ne "
      "portent que sur la section de la Colombie-Britannique."),
    T("<strong>The number of Chinese workers who died.</strong> UBC Library states the exact "
      "number will never be known, because the company left them out of its accident reports.",
      "<strong>Le nombre de travailleurs chinois morts.</strong> La bibliothèque de l'UBC "
      "indique que le nombre exact ne sera jamais connu, parce que la compagnie les a exclus "
      "de ses rapports d'accident."),
    T("<strong>The number of Indigenous workers, and the number of non-Chinese workers who "
      "died.</strong> Only individual incidents are on the record.",
      "<strong>Le nombre de travailleurs autochtones, et le nombre de travailleurs non "
      "chinois morts.</strong> Seuls des incidents isolés figurent au dossier."),
    T("<strong>Any track-laying record in miles per day.</strong> The famous ones come from "
      "the 1869 race on the United States Central Pacific, which is a different railway.",
      "<strong>Tout record de pose de voie en milles par jour.</strong> Les records célèbres "
      "viennent de la course de 1869 sur le Central Pacific des États-Unis, qui est un autre "
      "chemin de fer."),
    T("<strong>Quantities of explosives, and totals of tunnels and bridges for the whole "
      "line.</strong> Only local counts exist.",
      "<strong>Les quantités d'explosifs, et les totaux de tunnels et de ponts pour "
      "l'ensemble de la ligne.</strong> Seuls des décomptes locaux existent."),
    T("<strong>How long the 1885 troop movement took, and how many gaps the line had north of "
      "Lake Superior.</strong> Three official sources describe the line as near-complete or "
      "partially completed and stop there.",
      "<strong>La durée du déplacement des troupes de 1885, et le nombre de brèches de la "
      "ligne au nord du lac Supérieur.</strong> Trois sources officielles décrivent la ligne "
      "comme presque complète ou partiellement achevée, et s'arrêtent là."),
    T("<strong>Construction costs for the Canadian Northern, the Grand Trunk Pacific and the "
      "National Transcontinental.</strong> Dates yes, dollars no.",
      "<strong>Les coûts de construction du Canadien du Nord, du Grand Tronc Pacifique et du "
      "Transcontinental National.</strong> Les dates, oui ; les dollars, non."),
    T("<strong>The full membership of the 1880 syndicate.</strong> Official sources name "
      "Donald Smith, and call him a director.",
      "<strong>La composition complète du syndicat de 1880.</strong> Les sources officielles "
      "nomment Donald Smith, et le qualifient d'administrateur."),
    T("<strong>The substance of the Pacific Scandal.</strong> No government narrative page "
      "tells it; the primary record is the 1873 commission report itself.",
      "<strong>Le fond du scandale du Pacifique.</strong> Aucune page narrative "
      "gouvernementale ne le raconte ; le document de base est le rapport même de la "
      "commission de 1873."),
    T("<strong>When and how the twenty-year monopoly clause ended.</strong> The clause is "
      "documented; its end is not.",
      "<strong>Quand et comment la clause de monopole de vingt ans a pris fin.</strong> La "
      "clause est documentée ; sa fin ne l'est pas."),
    T("<strong>Whether the 1871 promise was legally satisfied in 1885 or in 1886.</strong> No "
      "official source rules on it.",
      "<strong>Si la promesse de 1871 a été légalement satisfaite en 1885 ou en 1886.</strong> "
      "Aucune source officielle ne tranche."),
])

# ------------------------------------------------------------------ 13
a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("how-canada-was-built.html",
         T("How every Canadian province was created",
           "Comment chaque province canadienne a été créée")),
    link("what-is-confederation.html",
         T("What is Confederation? Canada's beginning explained",
           "Qu'est-ce que la Confédération ? Les débuts du Canada expliqués")),
    link("indigenous-peoples-of-canada.html",
         T("Indigenous Peoples of Canada — First Nations, Inuit and Métis",
           "Les peuples autochtones du Canada — Premières Nations, Inuits et Métis")),
    link("the-railway-across-canada-for-kids.html",
         T("The railway that had to cross the mountains, for kids",
           "Le chemin de fer qui devait traverser les montagnes, pour les enfants")),
])

a.sources(T("Where this came from", "D'où vient tout ceci"), [
    out_link("https://justice.canada.ca/eng/rp-pr/csj-sjc/constitution/lawreg-loireg/p1t42.html",
             T("Justice Canada — British Columbia Terms of Union, clause 11",
               "Justice Canada — Conditions de l'adhésion de la Colombie-Britannique, clause 11")),
    out_link("https://justice.canada.ca/eng/rp-pr/csj-sjc/constitution/lawreg-loireg/p1t41.html",
             T("Justice Canada — the Province of British Columbia, Enactment No. 4",
               "Justice Canada — la province de la Colombie-Britannique, texte no 4")),
    out_link("https://epe.lac-bac.gc.ca/100/200/301/pco-bcp/commissions-ef/clark1882-eng/clark1882-v3-part1-eng.pdf?nodisclaimer=1",
             T("Report of the Canadian Pacific Railway Royal Commission, 1882, Volume III",
               "Rapport de la commission royale sur le chemin de fer Canadien du Pacifique, "
               "1882, volume III")),
    out_link("https://www.publications.gc.ca/pub?id=9.826326&sl=0",
             T("Government of Canada Publications — the 1873 Royal Commission on the Canadian "
               "Pacific Railway",
               "Publications du gouvernement du Canada — la commission royale de 1873 sur le "
               "chemin de fer Canadien du Pacifique")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1691",
             T("Parks Canada — Eagle Pass National Historic Event, where the last spike was "
               "driven",
               "Parcs Canada — événement historique national du col Eagle, où le dernier "
               "crampon a été planté")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1579",
             T("Parks Canada — Completion of the Canadian Pacific Railway, Port Moody",
               "Parcs Canada — achèvement du chemin de fer Canadien du Pacifique, Port Moody")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1621",
             T("Parks Canada — First Transcontinental Train, Montréal",
               "Parcs Canada — premier train transcontinental, Montréal")),
    out_link("https://www.collectionscanada.gc.ca/05/0529/052920/05292086_e.html",
             T("Library and Archives Canada — the last spike at Craigellachie, and the price "
               "of the railway",
               "Bibliothèque et Archives Canada — le dernier crampon à Craigellachie, et le "
               "prix du chemin de fer")),
    out_link("https://www.canada.ca/en/library-archives/collection/engage-learn/podcasts/treasures-revealed/episode-016.html",
             T("Library and Archives Canada — Treasures Revealed, episode 16, the last spike",
               "Bibliothèque et Archives Canada — Trésors révélés, épisode 16, le dernier "
               "crampon")),
    out_link("https://www.gov.mb.ca/chc/hrb/internal_reports/pdfs/railway_stations_full.pdf",
             T("Manitoba Historic Resources Branch — Railway Stations of Manitoba, a theme "
               "study",
               "Direction des ressources historiques du Manitoba — étude thématique sur les "
               "gares du Manitoba")),
    out_link("https://www2.gov.bc.ca/gov/content/governments/multiculturalism-anti-racism/chinese-legacy-bc/history/building-the-railway",
             T("Province of British Columbia — Building the Railway, wages and working "
               "conditions",
               "Province de la Colombie-Britannique — la construction du chemin de fer, "
               "salaires et conditions de travail")),
    out_link("https://www2.gov.bc.ca/gov/content/governments/multiculturalism-anti-racism/chinese-legacy-bc/history/discrimination/federal-head-tax",
             T("Province of British Columbia — the federal head tax",
               "Province de la Colombie-Britannique — la taxe d'entrée fédérale")),
    out_link("https://parks.canada.ca/culture/designation/evenement-event/travailleurs-chinois-chinese-workers",
             T("Parks Canada — Chinese Construction Workers on the Canadian Pacific Railway",
               "Parcs Canada — les travailleurs chinois de la construction du chemin de fer "
               "Canadien du Pacifique")),
    out_link("https://www.canada.ca/en/canadian-heritage/campaigns/asian-heritage-month/important-events.html",
             T("Canadian Heritage — significant events in the history of Asian communities in "
               "Canada",
               "Patrimoine canadien — événements marquants de l'histoire des communautés "
               "asiatiques au Canada")),
    out_link("https://www.canada.ca/en/news/archive/2006/06/address-prime-minister-chinese-head-tax-redress.html",
             T("Address by the Prime Minister on the Chinese head tax redress, 22 June 2006",
               "Allocution du premier ministre sur la réparation de la taxe d'entrée chinoise, "
               "22 juin 2006")),
    out_link("https://pier21.ca/research/immigration-history/royal-commission-on-chinese-immigration-1885",
             T("Canadian Museum of Immigration at Pier 21 — the 1885 Royal Commission on "
               "Chinese Immigration",
               "Musée canadien de l'immigration du Quai 21 — la commission royale de 1885 sur "
               "l'immigration chinoise")),
    out_link("https://gallery.library.ubc.ca/building-canadian-pacific/",
             T("UBC Library, Chung and Lind Gallery — Building Canadian Pacific",
               "Bibliothèque de l'UBC, galerie Chung et Lind — bâtir le Canadien Pacifique")),
    out_link("https://library-rbsc-2017.sites.olt.ubc.ca/files/2019/03/CPR-Timeline-Final.pdf",
             T("UBC Library, Chung Collection — Canadian Pacific Railway Company timeline",
               "Bibliothèque de l'UBC, collection Chung — chronologie de la Compagnie du "
               "chemin de fer Canadien du Pacifique")),
    out_link("https://www.historymuseum.ca/teachers-zone/history-box/colonial-canada/last-spike/",
             T("Canadian Museum of History — the Last Spike",
               "Musée canadien de l'histoire — le dernier crampon")),
    out_link("https://www.warmuseum.ca/cwm/exhibitions/chrono/1774northwest_e.html",
             T("Canadian War Museum — a chronology of Canadian military history, 1884 to 1885",
               "Musée canadien de la guerre — chronologie de l'histoire militaire canadienne, "
               "1884 à 1885")),
    out_link("https://www.canada.ca/en/department-national-defence/services/military-history/history-heritage/popular-books/aboriginal-people-canadian-military/transforming-relationships-1815-1902.html",
             T("Department of National Defence — Transforming Relationships, 1815 to 1902",
               "Ministère de la Défense nationale — transformation des relations, 1815 à 1902")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1360948213124/1544620003549",
             T("Crown-Indigenous Relations and Northern Affairs Canada — the numbered treaties, "
               "1871 to 1921",
               "Relations Couronne-Autochtones et Affaires du Nord Canada — les traités "
               "numérotés, 1871 à 1921")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1100100028685/1564413292885",
             T("CIRNAC — Treaty Research Report, Treaty Four, 1874",
               "RCAANC — rapport de recherche sur les traités, Traité Quatre, 1874")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1100100028710/1581292569426",
             T("CIRNAC — the text of Treaty No. 6",
               "RCAANC — le texte du Traité no 6")),
    out_link("https://parks.canada.ca/culture/designation/personnage-person/john-a-macdonald",
             T("Parks Canada — Sir John A. Macdonald National Historic Person",
               "Parcs Canada — sir John A. Macdonald, personnage d'importance historique "
               "nationale")),
    out_link("https://parks.canada.ca/lhn-nhs/sk/batoche/culture/histoire-history",
             T("Parks Canada — the history of Batoche National Historic Site",
               "Parcs Canada — l'histoire du lieu historique national de Batoche")),
    out_link("https://parks.canada.ca/lhn-nhs/sk/battleford/culture/histoire-history",
             T("Parks Canada — the history of Fort Battleford National Historic Site",
               "Parcs Canada — l'histoire du lieu historique national du Fort-Battleford")),
    out_link("https://parks.canada.ca/lhn-nhs/bc/rogers/decouvrir-discover/natcul4",
             T("Parks Canada — the Impenetrable Selkirks, Rogers Pass",
               "Parcs Canada — les Selkirk impénétrables, col Rogers")),
    out_link("https://parks.canada.ca/lhn-nhs/bc/rogers/decouvrir-discover/natcul5",
             T("Parks Canada — engineering marvels at Rogers Pass",
               "Parcs Canada — merveilles du génie au col Rogers")),
    out_link("https://parks.canada.ca/pn-np/bc/glacier/culture/histoire-history/neige-snow",
             T("Parks Canada — the Snow War, Glacier National Park",
               "Parcs Canada — la guerre de la neige, parc national des Glaciers")),
    out_link("https://parks.canada.ca/pn-np/bc/yoho/culture/kickinghorse/visit/spirale-spiral",
             T("Parks Canada — the Spiral Tunnels and the Big Hill",
               "Parcs Canada — les tunnels en spirale et la Grande Côte")),
    out_link("https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=10063",
             T("Canada's Historic Places — Kicking Horse Pass National Historic Site",
               "Lieux patrimoniaux du Canada — lieu historique national du col Kicking Horse")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1428",
             T("Parks Canada — Sir William Van Horne National Historic Person",
               "Parcs Canada — sir William Van Horne, personnage d'importance historique "
               "nationale")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1253&i=57955",
             T("Parks Canada — Sir Sandford Fleming National Historic Person",
               "Parcs Canada — sir Sandford Fleming, personnage d'importance historique "
               "nationale")),
    out_link("https://otc-cta.gc.ca/eng/publication/at-heart-transportation-a-moving-history",
             T("Canadian Transportation Agency — At the Heart of Transportation, a moving "
               "history",
               "Office des transports du Canada — au coeur des transports, une histoire en "
               "mouvement")),
    out_link("https://www.statcan.gc.ca/o1/en/plus/8309-who-are-navvies-who-work-upon-railway-today",
             T("Statistics Canada — who are the navvies who work upon the railway today",
               "Statistique Canada — qui sont les navvies qui travaillent au chemin de fer "
               "aujourd'hui")),
    out_link("https://www150.statcan.gc.ca/n1/pub/11-516-x/sectiont/4147444-eng.htm",
             T("Statistics Canada — Historical Statistics of Canada, transportation and "
               "communication",
               "Statistique Canada — Statistiques historiques du Canada, transports et "
               "communications")),
    out_link("https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/discover-canada/read-online/canadas-history.html",
             T("Immigration, Refugees and Citizenship Canada — Discover Canada, Canada's "
               "history",
               "Immigration, Réfugiés et Citoyenneté Canada — Découvrir le Canada, l'histoire "
               "du Canada")),
])

a.disclaimer(T(
    "This article is for general information and study. "
    "This site is unofficial and not affiliated with the Government of Canada or any "
    "provincial or territorial government. Every source used is listed above and on our "
    "sources page.",
    "Cet article est fourni à titre d'information générale et d'étude. Ce site est non "
    "officiel et n'a aucun lien avec le gouvernement du Canada ni avec aucun gouvernement "
    "provincial ou territorial. Toutes les sources utilisées sont énumérées ci-dessus et sur "
    "notre page des sources."))

if __name__ == "__main__":
    a.build()
    flush_pairs()
