#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article — how Canada licenses drivers, and what the records show.

Sources: the three research notes in the private project —
  research/driver-licensing-canada-20260830.md
  research/collision-data-canada-20260830.md
  research/driver-behaviour-and-the-city-claim-20260830.md

WHAT THIS PAGE DELIBERATELY DOES NOT DO
---------------------------------------
The owner's instruction, 30 August 2026: **"not point anyone fall only the
information."** No one is blamed. Every one of these was avoided on purpose:

  * NO city is named as having bad drivers. Not one.
  * The "bad drivers in [that city]" stereotype is **not raised and not
    rebutted**. Rebutting it would put it in front of readers who had not
    thought of it. The section on why cities cannot be ranked does the work
    quietly and on the evidence.
  * NO group of drivers is identified by origin, age or community. The
    ICES study of 4.2 million Ontarians (recent immigrants, 39% lower crash
    risk) is in the research file and is deliberately NOT used here, because
    using it would require raising the claim it answers.
  * The Auditor General's road-test-centre finding is used for what it shows
    about TEST CENTRES; the municipality named in that audit is not.
  * Insurance is barely touched — it is the owner's next article.
  * No commercial "worst drivers" ranking is cited. They measure one insurer's
    customers.

OTHER ACCURACY GUARDS
  * The five-year window (2019–2023) shows deaths RISING only because it starts
    at a pandemic-depressed base. The page shows the long run instead and says
    why. This is the single easiest way to mislead on this subject.
  * "MELT began after the Humboldt Broncos crash" is FALSE — Ontario's took
    effect 1 July 2017, nine months before. The page does not make that claim.
  * Territorial rates swing on single-digit counts; Yukon is shown with that
    caveat attached, never as a bare ranking.
  * The Saskatchewan training results are SGI's own evaluation, verified as
    adequately conducted by the Provincial Auditor — not independently
    reproduced. Said plainly.
  * Contributing-factor percentages sum past 100% and rest on a subset of
    provinces. Said plainly.
  * Nunavut: "not stated in the Driver's Manual", never "has no graduated
    licensing".
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, flush_pairs

a = Article(
    slug="driving-tests-across-canada-explained.html",
    section="Driving",
    title=T("Driving Tests Across Canada — How Each Province Licenses Drivers",
            "Les examens de conduite au Canada — comment chaque province délivre les permis"),
    desc=T("Canada has thirteen licensing systems, not one. The fastest route to a full "
           "licence takes 16 months; the slowest takes five years. What each province "
           "tests, what the audits found, and what the collision records actually show.",
           "Le Canada compte treize régimes de permis, et non un seul. La voie la plus "
           "rapide vers un permis complet prend 16 mois ; la plus lente, cinq ans. Ce que "
           "chaque province évalue, ce que les vérifications ont révélé et ce que montrent "
           "réellement les données sur les collisions."),
    h1=T("🚗 How Canada licenses drivers, and why it differs so much",
         "🚗 Comment le Canada délivre les permis de conduire, et pourquoi cela varie autant"),
    hero=T("Everyone has an opinion about other people's driving. Very little of it is "
           "written down. Here is what the licensing rules, the government audits and the "
           "collision records actually say.",
           "Tout le monde a une opinion sur la conduite des autres. Très peu de choses sont "
           "pourtant consignées. Voici ce que disent réellement les règles de délivrance des "
           "permis, les vérifications gouvernementales et les données sur les collisions."),
    checked=T("Last checked 30 August 2026 — licensing rules change, and two of the rules "
              "below change in October 2026",
              "Dernière vérification le 30 août 2026 — les règles changent, et deux de celles "
              "présentées ici changent en octobre 2026"),
)

# ------------------------------------------------------------------ 1
a.h2(T("There is no Canadian driver's licence",
       "Il n'existe pas de permis de conduire canadien"))
a.p(T(
    "There are thirteen. Each province and territory writes its own rules, sets its own "
    "tests and decides how long a new driver must wait. A licence earned in one is "
    "honoured in all the others, but the work behind it is not the same.",
    "Il y en a treize. Chaque province et territoire établit ses propres règles, conçoit "
    "ses propres examens et décide du temps d'attente imposé aux nouveaux conducteurs. Un "
    "permis obtenu dans l'une est reconnu partout ailleurs, mais le travail qu'il a exigé "
    "n'est pas le même."))
a.p(T(
    "The clearest way to see the difference is the minimum time from a first learner "
    "permit to a full, unrestricted licence.",
    "La façon la plus claire de voir la différence est le temps minimal entre le premier "
    "permis d'apprenti et un permis complet, sans restrictions."))

a.h3(T("Minimum time to a full licence",
       "Temps minimal pour obtenir un permis complet"))
a.table(
    [T("Where", "Où"), T("Standard", "Norme"), T("With a driving course", "Avec un cours de conduite")],
    [
        [T("Nova Scotia", "Nouvelle-Écosse"),
         T("36 months — and about 5 years before every restriction lifts",
           "36 mois — et environ 5 ans avant la levée de toutes les restrictions"),
         T("33 months", "33 mois")],
        [T("British Columbia", "Colombie-Britannique"), T("36 months", "36 mois"),
         T("30 months", "30 mois")],
        [T("Quebec", "Québec"), T("36 months", "36 mois"),
         T("training is required of everyone", "la formation est obligatoire pour tous")],
        [T("Alberta", "Alberta"), T("36 months", "36 mois"),
         T("no reduction offered", "aucune réduction offerte")],
        [T("Prince Edward Island", "Île-du-Prince-Édouard"), T("36 months", "36 mois"),
         T("about 33 months", "environ 33 mois")],
        [T("Saskatchewan", "Saskatchewan"), T("27 months", "27 mois"),
         T("training is required", "la formation est obligatoire")],
        [T("Manitoba", "Manitoba"), T("24 months", "24 mois"),
         T("no reduction offered", "aucune réduction offerte")],
        [T("New Brunswick", "Nouveau-Brunswick"), T("24 months", "24 mois"),
         T("20 months", "20 mois")],
        [T("Newfoundland and Labrador", "Terre-Neuve-et-Labrador"), T("24 months", "24 mois"),
         T("20 months", "20 mois")],
        [T("Yukon", "Yukon"), T("24 months", "24 mois"),
         T("no reduction offered", "aucune réduction offerte")],
        [T("Northwest Territories", "Territoires du Nord-Ouest"), T("24 months", "24 mois"),
         T("none stated", "aucune mentionnée")],
        [T("<strong>Ontario</strong>", "<strong>Ontario</strong>"),
         T("<strong>20 months</strong>", "<strong>20 mois</strong>"),
         T("<strong>16 months</strong>", "<strong>16 mois</strong>")],
        [T("Nunavut", "Nunavut"),
         T("no waiting period is stated in the territory's driver's manual",
           "aucun délai n'est indiqué dans le manuel du conducteur du territoire"),
         T("—", "—")],
    ])
a.callout(T(
    "<strong>Ontario is the fastest route to a full licence in Canada.</strong> Sixteen "
    "months with a driving course, against thirty-six months in five other provinces — "
    "less than half. Nova Scotia is at the other end: about five years before the last "
    "condition comes off.",
    "<strong>L'Ontario offre la voie la plus rapide vers un permis complet au "
    "Canada.</strong> Seize mois avec un cours de conduite, contre trente-six mois dans "
    "cinq autres provinces — moins de la moitié. La Nouvelle-Écosse se situe à l'autre "
    "extrémité : environ cinq ans avant que la dernière condition ne tombe."))

# ------------------------------------------------------------------ 2
a.h2(T("What the tests actually ask", "Ce que les examens demandent réellement"))
a.h3(T("Two road tests, soon in only one place",
       "Deux examens sur route, bientôt à un seul endroit"))
a.p(T(
    "Most of Canada asks a new driver to pass one road test. Ontario and British Columbia "
    "ask for two — one to leave the learner stage, another to leave the novice stage. "
    "Alberta dropped its second test in April 2023, and British Columbia replaces its "
    "second test with a driving-record check in October 2026.",
    "La plupart du Canada exige un seul examen sur route. L'Ontario et la "
    "Colombie-Britannique en exigent deux — un pour quitter l'étape d'apprenti, un autre "
    "pour quitter l'étape de conducteur novice. L'Alberta a supprimé son second examen en "
    "avril 2023, et la Colombie-Britannique remplacera le sien par une vérification du "
    "dossier de conduite en octobre 2026."))
a.callout(T(
    "After October 2026, <strong>Ontario will be the only place in Canada that tests a new "
    "driver twice</strong> — while also being the fastest place to finish. Those two facts "
    "pull in opposite directions.",
    "Après octobre 2026, <strong>l'Ontario sera le seul endroit au Canada à évaluer un "
    "nouveau conducteur deux fois</strong> — tout en étant l'endroit où l'on termine le "
    "plus vite. Ces deux faits tirent en sens contraire."))

a.h3(T("Almost nowhere counts your practice hours",
       "Presque nulle part on ne compte vos heures de pratique"))
a.p(T(
    "Yukon is the only jurisdiction whose licensing page states a required number of hours "
    "behind the wheel before the road test: fifty. Ontario asks a new driver to declare "
    "that they have driven on highways, but sets no hour count. Everywhere else, a learner "
    "can arrive at the test having driven very little.",
    "Le Yukon est la seule administration dont la page sur les permis indique un nombre "
    "d'heures de conduite exigé avant l'examen sur route : cinquante. L'Ontario demande au "
    "nouveau conducteur de déclarer qu'il a conduit sur l'autoroute, mais sans fixer de "
    "nombre d'heures. Partout ailleurs, un apprenti peut se présenter à l'examen après "
    "avoir très peu conduit."))
a.p(T(
    "Where hour figures do appear — ten in-car hours in Prince Edward Island and Nova "
    "Scotia, six in Saskatchewan — they are hours inside a paid course, not practice a "
    "learner has to log. Most American states and Australia require between fifty and a "
    "hundred and twenty supervised hours. Canada, with one exception, does not ask.",
    "Là où des chiffres apparaissent — dix heures en voiture à l'Île-du-Prince-Édouard et "
    "en Nouvelle-Écosse, six en Saskatchewan — il s'agit d'heures comprises dans un cours "
    "payant, et non de pratique que l'apprenti doit consigner. La plupart des États "
    "américains et l'Australie exigent entre cinquante et cent vingt heures supervisées. "
    "Le Canada, à une exception près, ne le demande pas."))

a.h3(T("The written test is not the same test",
       "L'examen théorique n'est pas le même partout"))
a.p(T(
    "Newfoundland and Labrador requires 85 per cent to pass, the highest published mark in "
    "the country. Alberta requires 83 per cent, Ontario and British Columbia 80. Quebec "
    "splits its test into three sections and requires 75 per cent in each, so a candidate "
    "cannot pass by being strong on signs and weak on the rules. Several jurisdictions do "
    "not publish a pass mark at all.",
    "Terre-Neuve-et-Labrador exige 85 pour cent, la note de passage publiée la plus élevée "
    "au pays. L'Alberta exige 83 pour cent, l'Ontario et la Colombie-Britannique 80. Le "
    "Québec divise son examen en trois sections et exige 75 pour cent à chacune, de sorte "
    "qu'on ne peut réussir en étant fort sur les panneaux et faible sur le code. Plusieurs "
    "administrations ne publient aucune note de passage."))

a.h3(T("Novice rules range from strict to almost none",
       "Les règles pour les novices vont de sévères à presque inexistantes"))
a.p(T(
    "In the Northwest Territories a learner may not drive between 11 p.m. and 6 a.m., may "
    "carry no passenger at all besides the supervisor, and the supervisor must also be at "
    "zero blood alcohol. In Alberta a probationary driver has no curfew and no passenger "
    "limit, and a learner permit can be held from the age of fourteen — the youngest in "
    "Canada. Both are called graduated licensing.",
    "Dans les Territoires du Nord-Ouest, un apprenti ne peut conduire entre 23 h et 6 h, ne "
    "peut transporter aucun passager hormis l'accompagnateur, et cet accompagnateur doit "
    "lui aussi avoir une alcoolémie nulle. En Alberta, un conducteur probatoire n'a ni "
    "couvre-feu ni limite de passagers, et le permis d'apprenti peut être obtenu dès "
    "quatorze ans — le plus jeune âge au Canada. Les deux régimes s'appellent « accès "
    "graduel à la conduite »."))

# ------------------------------------------------------------------ 3
a.h2(T("Training: required in four provinces, discounted in the rest",
       "La formation : obligatoire dans quatre provinces, escomptée ailleurs"))
a.p(T(
    "Quebec, Saskatchewan, Prince Edward Island and Nova Scotia require driver training. "
    "In Quebec a course must be completed before the learner's licence is even issued. In "
    "Nova Scotia a course is required at the other end, to leave the novice stage.",
    "Le Québec, la Saskatchewan, l'Île-du-Prince-Édouard et la Nouvelle-Écosse exigent une "
    "formation à la conduite. Au Québec, un cours doit être terminé avant même la "
    "délivrance du permis d'apprenti. En Nouvelle-Écosse, un cours est exigé à l'autre "
    "bout, pour quitter l'étape de novice."))
a.p(T(
    "Everywhere else the course is optional, and the incentive to take it is time: four "
    "months off in Ontario, New Brunswick and Newfoundland and Labrador, six months in "
    "British Columbia, ninety days in Prince Edward Island. Alberta, Manitoba and Yukon "
    "offer neither a requirement nor a discount.",
    "Partout ailleurs, le cours est facultatif et l'incitatif est le temps : quatre mois de "
    "moins en Ontario, au Nouveau-Brunswick et à Terre-Neuve-et-Labrador, six mois en "
    "Colombie-Britannique, quatre-vingt-dix jours à l'Île-du-Prince-Édouard. L'Alberta, le "
    "Manitoba et le Yukon n'offrent ni obligation ni réduction."))
a.p(T(
    "In 2023 Ontario's Auditor General examined what happens to the drivers who take the "
    "discount. The finding is worth reading twice.",
    "En 2023, la vérificatrice générale de l'Ontario a examiné ce qu'il advient des "
    "conducteurs qui profitent de cette réduction. La conclusion mérite d'être lue deux "
    "fois."))
a.fig(bar_chart(
    T("Collision rate of new Ontario drivers who took the same course",
      "Taux de collision des nouveaux conducteurs ontariens ayant suivi le même cours"),
    [(T("Used it to shorten the wait", "L'ont utilisé pour raccourcir l'attente"), 4.8),
     (T("Took it without shortening", "L'ont suivi sans raccourcir l'attente"), 3.7)],
    unit="%"),
    T("Auditor General of Ontario, 2023.",
      "Vérificatrice générale de l'Ontario, 2023."))
a.callout(T(
    "<strong>Two groups took the same course.</strong> The ones who used it to cut four "
    "months off their wait went on to crash about 30 per cent more often than the ones who "
    "served the full time. The audit reports that difference. It does not establish what "
    "caused it — drivers in a hurry to be licensed may differ in other ways as well.",
    "<strong>Deux groupes ont suivi le même cours.</strong> Ceux qui s'en sont servis pour "
    "retrancher quatre mois d'attente ont eu environ 30 pour cent plus de collisions que "
    "ceux qui ont respecté le délai complet. La vérification rapporte cet écart. Elle n'en "
    "établit pas la cause — les conducteurs pressés d'obtenir leur permis peuvent aussi "
    "différer par d'autres aspects."))
a.p(T(
    "The same audit sent fourteen people to driving schools as ordinary customers. Eleven "
    "of the fourteen received their certificate without being given the required in-car "
    "hours. Auditors also found instructors teaching students the specific routes used on "
    "the road test, and videos of real road tests posted on social media by people "
    "describing themselves as instructors.",
    "La même vérification a envoyé quatorze personnes dans des écoles de conduite comme "
    "clients ordinaires. Onze des quatorze ont reçu leur attestation sans avoir suivi les "
    "heures de conduite exigées. Les vérificateurs ont aussi constaté que des moniteurs "
    "enseignaient les trajets précis utilisés lors de l'examen, et que des vidéos "
    "d'examens réels étaient publiées sur les réseaux sociaux par des personnes se "
    "présentant comme moniteurs."))

# ------------------------------------------------------------------ 4
a.h2(T("What happens after you pass: almost nothing",
       "Ce qui arrive après la réussite : presque rien"))
a.p(T(
    "This is the part of the system people rarely think about. Once the last road test is "
    "behind you, no province asks you to demonstrate that you can still drive. A licence "
    "obtained at eighteen is renewed by mail, by payment and by a photograph for decades.",
    "C'est la partie du système à laquelle on pense rarement. Une fois le dernier examen "
    "réussi, aucune province ne vous demande de démontrer que vous savez encore conduire. "
    "Un permis obtenu à dix-huit ans se renouvelle par la poste, par un paiement et par une "
    "photo, pendant des décennies."))
a.p(T(
    "The exceptions are medical rather than practical. Ontario brings drivers back at "
    "eighty for a vision screen and a short in-class exercise. Quebec asks for a "
    "self-declaration at seventy-five and a medical at eighty. British Columbia, Alberta, "
    "Newfoundland and Labrador and Nunavut require medical reports at seventy-five or "
    "eighty and every two years after. None of these is a driving test.",
    "Les exceptions sont médicales plutôt que pratiques. L'Ontario convoque les conducteurs "
    "à quatre-vingts ans pour un examen de la vue et un court exercice en classe. Le Québec "
    "demande une autodéclaration à soixante-quinze ans et un examen médical à quatre-vingts. "
    "La Colombie-Britannique, l'Alberta, Terre-Neuve-et-Labrador et le Nunavut exigent des "
    "rapports médicaux à soixante-quinze ou quatre-vingts ans, puis tous les deux ans. "
    "Aucun de ces contrôles n'est un examen de conduite."))
a.callout(T(
    "A driver can be tested once, at eighteen, and never assessed again. Habits formed in "
    "the first years are the habits of a lifetime, because nothing in the system ever asks "
    "about them again.",
    "Un conducteur peut être évalué une seule fois, à dix-huit ans, et ne plus jamais "
    "l'être. Les habitudes prises dans les premières années deviennent celles de toute une "
    "vie, car plus rien dans le système ne s'y intéresse ensuite."))

# ------------------------------------------------------------------ 5
a.h2(T("Commercial licences: what the 2026 audit found",
       "Les permis commerciaux : ce qu'a révélé la vérification de 2026"))
a.p(T(
    "Canada agreed a national minimum for entry-level truck training in 2021: 103.5 hours, "
    "made up of classroom time, yard work, time behind the wheel and air brake "
    "instruction. Provinces are free to require more, and they do.",
    "Le Canada a adopté en 2021 une norme minimale nationale de formation de base pour les "
    "camionneurs : 103,5 heures, réparties entre la classe, la cour, la conduite et la "
    "formation sur les freins pneumatiques. Les provinces peuvent en exiger davantage, et "
    "elles le font."))
a.fig(bar_chart(
    T("Required hours of entry-level truck training",
      "Heures de formation de base exigées pour le camionnage"),
    [(T("British Columbia", "Colombie-Britannique"), 140),
     (T("Alberta", "Alberta"), 125),
     (T("Saskatchewan / Manitoba", "Saskatchewan / Manitoba"), 121.5),
     (T("Northwest Territories", "Territoires du Nord-Ouest"), 113),
     (T("Newfoundland and Labrador", "Terre-Neuve-et-Labrador"), 112.5),
     (T("New Brunswick", "Nouveau-Brunswick"), 112),
     (T("Ontario", "Ontario"), 103.5)],
    unit="h"),
    T("Provincial requirements. Ontario sits exactly at the national minimum.",
      "Exigences provinciales. L'Ontario se situe exactement au minimum national."))
a.p(T(
    "British Columbia requires about 35 per cent more training than Ontario for the same "
    "class of licence, and that licence moves between provinces. The mix differs as much as "
    "the total: time actually behind the wheel ranges from 41 hours in one province to 57 "
    "in another.",
    "La Colombie-Britannique exige environ 35 pour cent plus de formation que l'Ontario "
    "pour la même catégorie de permis, et ce permis circule d'une province à l'autre. La "
    "composition varie autant que le total : le temps réellement passé au volant va de 41 "
    "heures dans une province à 57 dans une autre."))
a.p(T(
    "In May 2026 Ontario's Auditor General published a special report on large commercial "
    "truck driver licensing. Trucks were three per cent of vehicles on Ontario roads "
    "between 2019 and 2023, and twelve per cent of fatal collisions.",
    "En mai 2026, la vérificatrice générale de l'Ontario a publié un rapport spécial sur la "
    "délivrance des permis de camionneur. Entre 2019 et 2023, les camions représentaient "
    "trois pour cent des véhicules sur les routes ontariennes et douze pour cent des "
    "collisions mortelles."))
a.ul([
    T("Two colleges delivered only 57 and 78 per cent of the required hours. Students sent "
      "in by the auditors were never taught left turns at major intersections, reverse "
      "parking or emergency stopping",
      "Deux collèges n'ont donné que 57 et 78 pour cent des heures exigées. Les étudiants "
      "envoyés par les vérificateurs n'ont jamais appris les virages à gauche aux grandes "
      "intersections, le stationnement en marche arrière ni l'arrêt d'urgence"),
    T("Three colleges falsified or altered student training records",
      "Trois collèges ont falsifié ou modifié des dossiers de formation d'étudiants"),
    T("A quarter of the schools offering the training had never been inspected, and there "
      "was no policy requiring periodic inspection at all",
      "Le quart des écoles offrant la formation n'avaient jamais été inspectées, et aucune "
      "politique n'exigeait d'inspection périodique"),
    T("Seventeen schools that had never registered booked 3,227 examination appointments",
      "Dix-sept écoles jamais inscrites ont réservé 3 227 rendez-vous d'examen"),
    T("Twenty-nine test centres used expressways with speed limits below 100 km/h, and nine "
      "tested at only 50 to 70 km/h. Drivers tested on the easier routes went on to have a "
      "higher first-year collision rate",
      "Vingt-neuf centres d'examen utilisaient des voies rapides limitées à moins de "
      "100 km/h, et neuf évaluaient à seulement 50 à 70 km/h. Les conducteurs évalués sur "
      "les trajets les plus faciles ont ensuite connu un taux de collision plus élevé la "
      "première année"),
    T("Ontario sets no waiting period at all between holding an ordinary car licence and "
      "applying for a large truck licence",
      "L'Ontario n'impose aucun délai entre la détention d'un permis d'automobile ordinaire "
      "et la demande d'un permis de gros camion"),
])
a.p(T(
    "There is a counterweight, and it points the other way. Saskatchewan brought in "
    "mandatory truck training in March 2019 and evaluated it in 2024. Comparing drivers "
    "trained after the requirement with those trained before, the insurer reported 79 per "
    "cent fewer offence tickets, 71 per cent fewer at-fault collisions and 85 per cent "
    "fewer inspection failures. These are the insurer's own figures; the province's "
    "auditor confirmed the evaluation was properly carried out rather than repeating the "
    "measurement independently.",
    "Il existe un contrepoids, et il va dans l'autre sens. La Saskatchewan a rendu la "
    "formation obligatoire en mars 2019 et l'a évaluée en 2024. En comparant les "
    "conducteurs formés après l'exigence à ceux formés avant, l'assureur a signalé 79 pour "
    "cent moins de contraventions, 71 pour cent moins de collisions avec responsabilité et "
    "85 pour cent moins d'échecs à l'inspection. Ce sont les chiffres de l'assureur "
    "lui-même ; le vérificateur provincial a confirmé que l'évaluation avait été menée "
    "correctement, sans refaire la mesure de façon indépendante."))
a.callout(T(
    "Read together, the two reports say the same thing from opposite directions: "
    "<strong>training works when it is actually delivered, and the weak point is not the "
    "standard but whether anyone checks that it was taught.</strong>",
    "Lus ensemble, les deux rapports disent la même chose en sens inverse : <strong>la "
    "formation fonctionne quand elle est réellement donnée, et le point faible n'est pas la "
    "norme mais l'absence de vérification qu'elle a bien été enseignée.</strong>"))

# ------------------------------------------------------------------ 6
a.h2(T("The habits everyone complains about, measured",
       "Les habitudes dont tout le monde se plaint, mesurées"))
a.p(T(
    "Rolling through stop signs, turning without signalling, sliding through on the amber. "
    "Most of this is discussed and very little of it is counted. One Canadian study did "
    "count it.",
    "Franchir un arrêt sans s'immobiliser, tourner sans clignotant, passer sur le feu "
    "jaune. On en parle beaucoup et on le mesure très peu. Une étude canadienne l'a "
    "pourtant mesuré."))
a.p(T(
    "Researchers filmed five stop-controlled intersections in Montreal and measured the "
    "actual speed of 2,909 vehicles, rather than relying on an observer's judgement.",
    "Des chercheurs ont filmé cinq intersections avec arrêt obligatoire à Montréal et "
    "mesuré la vitesse réelle de 2 909 véhicules, plutôt que de s'en remettre au jugement "
    "d'un observateur."))
a.fig(bar_chart(
    T("What 2,909 drivers did at a stop sign",
      "Ce qu'ont fait 2 909 conducteurs à un panneau d'arrêt"),
    [(T("Slight rolling stop", "Ralentissement marqué sans arrêt"), 37),
     (T("Rolling stop", "Arrêt roulant"), 33),
     (T("Slowed but did not stop", "Ont ralenti sans s'arrêter"), 14),
     (T("Came to a complete stop", "Se sont immobilisés complètement"), 11),
     (T("Drove straight through", "Ont franchi sans ralentir"), 5)],
    unit="%"),
    T("Measured by vehicle speed, not by observation.",
      "Mesuré par la vitesse des véhicules, et non par observation."))
a.callout(T(
    "<strong>About one driver in nine came to a complete stop.</strong> Not one group of "
    "drivers, not one neighbourhood — the drivers who happened to arrive at five ordinary "
    "intersections.",
    "<strong>Environ un conducteur sur neuf s'est immobilisé complètement.</strong> Pas un "
    "groupe de conducteurs, pas un quartier — les conducteurs qui se sont présentés à cinq "
    "intersections ordinaires."))
a.p(T(
    "Signalling is different: it is complained about constantly and measured almost "
    "nowhere. Ontario's collision reports have no category for it, and neither does the "
    "national table. The figure quoted everywhere online comes from a single study of one "
    "American city, presented at an engineering conference, by an author who sells an "
    "automatic signalling product. It should not be repeated as a Canadian fact.",
    "Le clignotant, c'est autre chose : on s'en plaint constamment et on ne le mesure "
    "presque nulle part. Les rapports de collision de l'Ontario n'ont aucune catégorie pour "
    "cela, ni le tableau national. Le chiffre repris partout en ligne provient d'une seule "
    "étude portant sur une ville américaine, présentée dans un congrès d'ingénierie, par un "
    "auteur qui vend un dispositif de clignotant automatique. Il ne devrait pas être répété "
    "comme un fait canadien."))

a.h3(T("What actually goes wrong at intersections",
       "Ce qui ne va vraiment pas aux intersections"))
a.p(T(
    "Intersections account for about 27 per cent of Canadian road deaths and 41 per cent of "
    "serious injuries. The most common driver failure behind them is not aggression and not "
    "speed. It is looking without seeing — a driver checks, and does not register what is "
    "there. On-scene investigation puts it at about 44 per cent of intersection crashes, "
    "roughly six times more common there than anywhere else on the road.",
    "Les intersections représentent environ 27 pour cent des décès sur les routes "
    "canadiennes et 41 pour cent des blessures graves. La défaillance la plus fréquente "
    "n'est ni l'agressivité ni la vitesse. C'est regarder sans voir — le conducteur vérifie "
    "et n'enregistre pas ce qui s'y trouve. Les enquêtes sur les lieux l'estiment à environ "
    "44 pour cent des collisions aux intersections, soit à peu près six fois plus fréquent "
    "là qu'ailleurs sur la route."))

a.h3(T("The annoying behaviours are not the deadly ones",
       "Les comportements agaçants ne sont pas les comportements mortels"))
a.p(T(
    "Ontario records what each driver was doing in more than 270,000 collisions a year, and "
    "the pattern is not what most people assume.",
    "L'Ontario consigne ce que faisait chaque conducteur dans plus de 270 000 collisions "
    "par année, et le portrait n'est pas celui que l'on suppose."))
a.table(
    [T("Driver action", "Comportement du conducteur"),
     T("Share of all collisions", "Part de toutes les collisions"),
     T("Share of fatal collisions", "Part des collisions mortelles")],
    [[T("Following too closely", "Suivre de trop près"), "8.6%", "0.9%"],
     [T("Failing to yield right of way", "Refus de priorité"), "5.6%", "6.9%"],
     [T("Disobeying a traffic control", "Ne pas respecter un dispositif de contrôle"),
      "2.1%", "5.1%"]])
a.p(T(
    "Following too closely is the most common improper action on the road and almost never "
    "appears in a fatal collision. Running a light or a sign is the reverse. The behaviour "
    "that irritates a driver in traffic and the behaviour that kills someone are largely "
    "not the same behaviour.",
    "Suivre de trop près est le comportement fautif le plus courant et n'apparaît presque "
    "jamais dans une collision mortelle. Brûler un feu ou un panneau, c'est l'inverse. Le "
    "comportement qui agace dans la circulation et celui qui tue une personne ne sont "
    "généralement pas le même."))
a.p(T(
    "One more number belongs here, because it is the simplest of all: of the drivers killed "
    "on Canadian roads in 2023, 32.6 per cent were not wearing a seatbelt.",
    "Un dernier chiffre a sa place ici, car il est le plus simple de tous : parmi les "
    "conducteurs tués sur les routes canadiennes en 2023, 32,6 pour cent ne portaient pas "
    "leur ceinture."))

# ------------------------------------------------------------------ 7
a.h2(T("Where crashes actually happen", "Où se produisent réellement les collisions"))
a.p(T(
    "It is natural to assume the busiest roads are the most dangerous. The national record "
    "says the opposite, at least where dying is concerned.",
    "Il est naturel de supposer que les routes les plus achalandées sont les plus "
    "dangereuses. Les données nationales disent le contraire, du moins pour ce qui est de "
    "mourir."))
a.table(
    [T("", ""), T("Fatal collisions", "Collisions mortelles"),
     T("Injury collisions", "Collisions avec blessures")],
    [[T("Urban roads", "Routes urbaines"), "799", "65,834"],
     [T("Rural roads", "Routes rurales"), "<strong>932</strong>", "22,051"]])
a.callout(T(
    "<strong>Rural roads produce 53 per cent of Canada's fatal collisions but only 25 per "
    "cent of the injury collisions.</strong> A rural crash is roughly three and a half "
    "times more likely to kill someone. Higher speeds, no separation between directions, "
    "and a longer wait for an ambulance.",
    "<strong>Les routes rurales causent 53 pour cent des collisions mortelles au Canada, "
    "mais seulement 25 pour cent des collisions avec blessures.</strong> Une collision en "
    "milieu rural risque environ trois fois et demie plus de tuer. Vitesses plus élevées, "
    "aucune séparation entre les sens de circulation, et une ambulance plus longue à "
    "arriver."))
a.p(T(
    "That single fact explains most of the difference between provinces. The jurisdictions "
    "with the highest death rates are the most rural; the lowest are the most urban.",
    "Ce seul fait explique l'essentiel des écarts entre provinces. Les administrations où "
    "le taux de décès est le plus élevé sont les plus rurales ; les plus faibles sont les "
    "plus urbaines."))
a.table(
    [T("Province or territory", "Province ou territoire"),
     T("Road deaths per 100,000 people, 2023", "Décès sur la route par 100 000 habitants, 2023")],
    [[T("New Brunswick", "Nouveau-Brunswick"), "8.5"],
     [T("Prince Edward Island", "Île-du-Prince-Édouard"), "8.1"],
     [T("Newfoundland and Labrador", "Terre-Neuve-et-Labrador"), "7.8"],
     [T("Saskatchewan", "Saskatchewan"), "7.6"],
     [T("Alberta", "Alberta"), "6.4"],
     [T("British Columbia", "Colombie-Britannique"), "5.5"],
     [T("Manitoba", "Manitoba"), "5.4"],
     [T("Nova Scotia", "Nouvelle-Écosse"), "5.3"],
     [T("<strong>Canada</strong>", "<strong>Canada</strong>"), "<strong>4.9</strong>"],
     [T("Quebec", "Québec"), "4.3"],
     [T("<strong>Ontario</strong>", "<strong>Ontario</strong>"), "<strong>3.9</strong>"]])
a.p(T(
    "Ontario has the lowest road death rate of any province, and New Brunswick's is more "
    "than double it. The territories are left out of the table on purpose: their counts are "
    "small enough that a handful of collisions moves the rate enormously, and Yukon's went "
    "from 4.6 to 19.8 in a single year.",
    "L'Ontario affiche le taux de décès routiers le plus bas de toutes les provinces, et "
    "celui du Nouveau-Brunswick est plus du double. Les territoires sont volontairement "
    "exclus du tableau : leurs effectifs sont si faibles qu'une poignée de collisions "
    "déplace énormément le taux, et celui du Yukon est passé de 4,6 à 19,8 en une seule "
    "année."))

a.h3(T("Is it getting worse? It depends entirely on the window",
       "Est-ce que cela empire ? Tout dépend de la période choisie"))
a.p(T(
    "Take the last five years and road deaths appear to be climbing: 1,756 in 2019 and "
    "1,964 in 2023. But 2019 sits right before the pandemic, and traffic collapsed in 2020. "
    "Any five-year window starting there is measuring a recovery, not a trend.",
    "Prenez les cinq dernières années et les décès semblent grimper : 1 756 en 2019 et "
    "1 964 en 2023. Mais 2019 précède immédiatement la pandémie, et la circulation s'est "
    "effondrée en 2020. Toute période de cinq ans commençant là mesure une reprise, et non "
    "une tendance."))
a.p(T(
    "Step back and the picture reverses completely. Canadian roads killed 5,933 people in "
    "1979, at a rate of 24.5 per 100,000. In 2023 they killed 1,964, at 4.9. Deaths fell by "
    "about two thirds while the population grew by nearly half, so the death rate is down "
    "around 80 per cent.",
    "Prenez du recul et le portrait s'inverse complètement. Les routes canadiennes ont tué "
    "5 933 personnes en 1979, soit un taux de 24,5 par 100 000. En 2023, elles en ont tué "
    "1 964, à 4,9. Les décès ont chuté d'environ deux tiers alors que la population "
    "augmentait de près de la moitié : le taux de mortalité a donc baissé d'environ 80 pour "
    "cent."))
a.p(T(
    "That does not make Canada a leader. Measured against other wealthy countries, Canada "
    "sits around twentieth of thirty-four, at 4.8 deaths per 100,000. Norway is at 2.0, "
    "Sweden 2.2, the United Kingdom 2.5, Japan 2.6. Canada is well ahead of the United "
    "States and roughly two and a half times worse than the safest.",
    "Cela ne fait pas du Canada un chef de file. Comparé aux autres pays riches, le Canada "
    "se situe autour du vingtième rang sur trente-quatre, à 4,8 décès par 100 000. La "
    "Norvège est à 2,0, la Suède à 2,2, le Royaume-Uni à 2,5, le Japon à 2,6. Le Canada "
    "devance nettement les États-Unis et fait environ deux fois et demie moins bien que les "
    "plus sûrs."))

# ------------------------------------------------------------------ 8
a.h2(T("Why nobody can honestly rank Canadian cities by crashes",
       "Pourquoi personne ne peut honnêtement classer les villes canadiennes selon les collisions"))
a.p(T(
    "Lists of the worst places to drive in Canada appear every year. They cannot be built "
    "from the available data, and it is worth understanding why, because the reasons are "
    "not small.",
    "Des palmarès des pires endroits où conduire au Canada paraissent chaque année. Ils ne "
    "peuvent pas être construits à partir des données disponibles, et il vaut la peine de "
    "comprendre pourquoi, car les raisons ne sont pas mineures."))
a.ul([
    T("<strong>Cities count different collisions.</strong> Some publish only crashes where "
      "someone was killed or seriously hurt. Others include every fender-bender — and "
      "fender-benders are about 83 per cent of all reported collisions. That difference "
      "alone changes a city's number roughly six-fold",
      "<strong>Les villes ne comptent pas les mêmes collisions.</strong> Certaines ne "
      "publient que les collisions ayant fait un mort ou un blessé grave. D'autres incluent "
      "chaque accrochage — et les accrochages représentent environ 83 pour cent de toutes "
      "les collisions déclarées. Cette seule différence modifie le chiffre d'une ville "
      "d'environ six fois"),
    T("<strong>The reporting threshold differs by province and keeps moving.</strong> "
      "Quebec requires a report above $2,000 of damage; Ontario and Alberta now use $5,000. "
      "A minor collision that goes unrecorded in one province is a statistic in another",
      "<strong>Le seuil de déclaration varie d'une province à l'autre et change "
      "constamment.</strong> Le Québec exige une déclaration au-delà de 2 000 $ de dommages ; "
      "l'Ontario et l'Alberta utilisent maintenant 5 000 $. Une collision mineure non "
      "consignée dans une province devient une statistique dans une autre"),
    T("<strong>Some cities do not count their own highways.</strong> In Ontario the busiest "
      "freeways are policed by the provincial force, so those collisions never enter the "
      "city's figures. One major city excludes the highway network by rule; another "
      "includes it. They are not measuring the same roads",
      "<strong>Certaines villes ne comptent pas leurs propres autoroutes.</strong> En "
      "Ontario, les autoroutes les plus achalandées relèvent de la police provinciale : ces "
      "collisions n'entrent jamais dans les chiffres municipaux. Une grande ville exclut le "
      "réseau autoroutier par règle ; une autre l'inclut. Elles ne mesurent pas les mêmes "
      "routes"),
    T("<strong>The years do not line up.</strong> Among the largest cities, published "
      "collision data ends in 2020 in one, 2021 in another, 2022 in a third and 2023 in a "
      "fourth. There is no common five-year window to compare",
      "<strong>Les années ne concordent pas.</strong> Parmi les plus grandes villes, les "
      "données publiées s'arrêtent en 2020 dans l'une, 2021 dans une autre, 2022 dans une "
      "troisième et 2023 dans une quatrième. Il n'existe aucune période commune de cinq ans "
      "à comparer"),
])
a.callout(T(
    "The rankings that circulate are usually built from one insurance company's claims "
    "among its own customers, with no measure of how far those people drive. That is a "
    "picture of an insurer's business, not of a city's roads.",
    "Les palmarès qui circulent sont généralement bâtis à partir des réclamations d'une "
    "seule compagnie d'assurance auprès de ses propres clients, sans aucune mesure de la "
    "distance parcourue. C'est le portrait des affaires d'un assureur, non celui des routes "
    "d'une ville."))
a.p(T(
    "There is also a number nobody publishes at all. No province in Canada reports how many "
    "new driver's licences it issues in a year. They report how many licence holders exist, "
    "which is a different thing entirely — it cannot tell you how many people joined the "
    "road last year.",
    "Il existe aussi un chiffre que personne ne publie. Aucune province canadienne ne "
    "déclare combien de nouveaux permis de conduire elle délivre en un an. On publie le "
    "nombre de titulaires de permis, ce qui est tout autre chose — cela ne dit pas combien "
    "de personnes se sont ajoutées à la route l'an dernier."))

# ------------------------------------------------------------------ 9
a.h2(T("What the record adds up to", "Ce que révèle l'ensemble"))
a.p(T(
    "Nothing here supports the idea that one place produces worse drivers than another. "
    "What the record does show is a set of design choices, made differently in thirteen "
    "places, with measurable results.",
    "Rien ici n'appuie l'idée qu'un endroit produirait de moins bons conducteurs qu'un "
    "autre. Ce que les données montrent, ce sont des choix de conception, faits "
    "différemment à treize endroits, avec des résultats mesurables."))
a.ul([
    T("One province lets a course shorten the waiting period, and its own auditor found "
      "that the drivers who took that option crashed more often afterwards than those who "
      "did not",
      "Une province permet à un cours de raccourcir le délai d'attente, et sa propre "
      "vérificatrice a constaté que les conducteurs ayant choisi cette option ont eu par "
      "la suite plus de collisions que les autres"),
    T("Training works where it is delivered and inspected, and one auditor found a quarter "
      "of schools had never been inspected at all",
      "La formation fonctionne là où elle est donnée et inspectée, et une vérification a "
      "constaté que le quart des écoles n'avaient jamais été inspectées"),
    T("A test taken on a slower road is an easier test, and the drivers who took it crashed "
      "more afterwards",
      "Un examen passé sur une route plus lente est un examen plus facile, et les "
      "conducteurs qui l'ont passé ont ensuite eu plus de collisions"),
    T("Almost no jurisdiction requires logged practice hours, and only one states a number",
      "Presque aucune administration n'exige d'heures de pratique consignées, et une seule "
      "indique un nombre"),
    T("After the last test, nobody is ever assessed again",
      "Après le dernier examen, plus personne n'est évalué"),
])
a.p(T(
    "And the habits people complain about are not the property of any group. At five "
    "ordinary intersections, about one driver in nine came to a complete stop. Whatever "
    "explains that, it is not a place on a map.",
    "Et les habitudes dont on se plaint n'appartiennent à aucun groupe. À cinq "
    "intersections ordinaires, environ un conducteur sur neuf s'est immobilisé "
    "complètement. Quelle qu'en soit l'explication, ce n'est pas un endroit sur une carte."))

# ------------------------------------------------------------------ sources
a.sources(T("Where this comes from", "D'où proviennent ces données"), [
    out_link("https://tc.canada.ca/en/road-transportation/statistics-data/canadian-motor-vehicle-traffic-collision-statistics/2023/canadian-motor-vehicle-traffic-collision-statistics-2023",
             T("Canadian Motor Vehicle Traffic Collision Statistics 2023 — Transport Canada",
               "Statistiques sur les collisions de la route au Canada 2023 — Transports Canada")),
    out_link("https://www.auditor.on.ca/en/content/specialreports/specialreports/en26/2026_CommTrucking_EN.pdf",
             T("Large Commercial Truck Driver Licensing, May 2026 — Auditor General of Ontario",
               "Délivrance des permis de camionneur, mai 2026 — vérificatrice générale de l'Ontario")),
    out_link("https://www.auditor.on.ca/en/content/annualreports/arreports/en23/AR_drivertraining_en23.pdf",
             T("Driver Training, 2023 — Auditor General of Ontario",
               "Formation des conducteurs, 2023 — vérificatrice générale de l'Ontario")),
    out_link("https://auditor.sk.ca/pub/publications/public_reports/2025/2025%20Report%20Volume%202/ch-23----saskatchewan-government-insurancelicensing-commercial-drivers.pdf",
             T("Licensing Commercial Drivers, 2025 — Provincial Auditor of Saskatchewan",
               "Délivrance des permis commerciaux, 2025 — vérificateur provincial de la Saskatchewan")),
    out_link("https://www.ccmta.ca/web/default/files/PDF/ELT_Standard_16_Update_2021_FINAL_English.pdf",
             T("National Safety Code Standard 16, entry-level truck training — CCMTA",
               "Norme 16 du Code canadien de sécurité, formation de base en camionnage — CCATM")),
    out_link("https://www.mdpi.com/2071-1050/13/3/1404",
             T("Driver behaviour at stop-controlled intersections in Montreal — Sustainability, 2021",
               "Comportement des conducteurs aux intersections avec arrêt à Montréal — Sustainability, 2021")),
    out_link("https://www.ontario.ca/page/get-g-drivers-licence-new-drivers",
             T("Get a G driver's licence: new drivers — Government of Ontario",
               "Obtenir un permis de conduire de catégorie G — gouvernement de l'Ontario")),
    out_link("https://icbc.com/driver-licensing/new-drivers/Graduated-licensing",
             T("Graduated licensing — ICBC, British Columbia",
               "Programme d'accès graduel — ICBC, Colombie-Britannique")),
    out_link("https://saaq.gouv.qc.ca/en/drivers-licences/obtaining-licence/passenger-vehicle-class-5",
             T("Obtaining a Class 5 licence — SAAQ, Quebec",
               "Obtenir un permis de classe 5 — SAAQ, Québec")),
    out_link("https://www.alberta.ca/class-5-drivers-licence",
             T("Class 5 driver's licence — Government of Alberta",
               "Permis de conduire de classe 5 — gouvernement de l'Alberta")),
    out_link("https://sgi.sk.ca/handbook/-/knowledge_base/drivers/graduated-driver-licensing-program",
             T("Graduated Driver Licensing — SGI, Saskatchewan",
               "Programme d'accès graduel — SGI, Saskatchewan")),
    out_link("https://www.gov.nl.ca/motorregistration/new-drivers/graduated-driver-licencing-program/",
             T("Graduated Driver Licensing — Newfoundland and Labrador",
               "Programme d'accès graduel — Terre-Neuve-et-Labrador")),
    out_link("https://www.itf-oecd.org/sites/default/files/docs/irtad-road-safety-annual-report-2024.pdf",
             T("Road Safety Annual Report 2024 — International Transport Forum",
               "Rapport annuel sur la sécurité routière 2024 — Forum international des transports")),
])

a.disclaimer(T(
    "This page explains how driver licensing works across Canada and what public records "
    "show. It is not legal advice and is not affiliated with any government. Licensing "
    "rules change — always confirm the current requirements with your own province or "
    "territory before relying on them.",
    "Cette page explique le fonctionnement de la délivrance des permis de conduire au "
    "Canada et ce que montrent les documents publics. Il ne s'agit pas d'un avis juridique "
    "et elle n'est affiliée à aucun gouvernement. Les règles changent — vérifiez toujours "
    "les exigences en vigueur auprès de votre province ou territoire avant de vous y fier."))

a.build()
flush_pairs()
