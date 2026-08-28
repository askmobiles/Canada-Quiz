#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article — why big infrastructure projects take so long and cost so much.

Source: the research notes
notes, plus the research notes for the historical
counterweight only.

This page deliberately does NOT argue a thesis. The research file's section 11B
lists ten framings that would turn it into an opinion piece, and each one was
avoided on purpose:

  * The premise is TESTED, not assumed. StatCan's historical railway tables
    start at 1946 and the Infrastructure Construction Price Index starts at
    reference year 2019, so the like-for-like comparison readers want does not
    exist in official data. The page says so instead of manufacturing one.
  * No real-terms 1885-versus-today cost figure appears anywhere on the page,
    because no official source publishes one. Any such number would be the
    writer's own arithmetic.
  * "Canada is the slowest country in the world" is not claimed. The only
    rigorous comparison located puts Toronto at 18.8 years of pre-construction
    against London's 18.4.
  * The Trans Mountain escalation is NOT apportioned between causes. The PBO
    does not attribute the $12.8 billion, so neither does this page.
  * The absence of regulatory review and Indigenous consultation from the
    Canadian audit record is stated as an absence in that record — not as a
    claim that review costs nothing.
  * The counterweight is concrete and unsoftened, and the page ends on the
    trade-off rather than on a verdict.

Overlap with art_mpo.py (the Building Canada Act, section 6(1), the eighteen
referred projects, the jobs and investment figures) is handled by a link, not
by repetition. Only what is new since that page was written appears here.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="why-big-projects-take-so-long.html",
    section="Government",
    title=T("Why Big Projects in Canada Take So Long — What the Records Show",
            "Pourquoi les grands projets prennent autant de temps au Canada — ce que "
            "disent les documents"),
    desc=T("Canada built a railway to the Pacific in the 1880s and now takes ten years to "
           "approve a pipeline. Is that a fair comparison? A plain look at what official "
           "records, auditors and researchers actually measured — and at what nobody has "
           "measured at all.",
           "Le Canada a bâti un chemin de fer jusqu'au Pacifique dans les années 1880 et met "
           "aujourd'hui dix ans à autoriser un oléoduc. La comparaison est-elle juste ? Un "
           "regard simple sur ce que les documents officiels, les vérificateurs et les "
           "chercheurs ont réellement mesuré — et sur ce que personne n'a mesuré."),
    h1=T("⏳ Why big projects in Canada take so long, and cost so much",
         "⏳ Pourquoi les grands projets prennent autant de temps et coûtent autant au "
         "Canada"),
    hero=T("Almost everyone has an answer to this question. Very little of it is written "
           "down in an official record. Here is what is written down, what is disputed, and "
           "where the evidence simply runs out.",
           "Presque tout le monde a une réponse à cette question. Très peu de chose est "
           "pourtant consignée dans un document officiel. Voici ce qui l'est, ce qui est "
           "contesté, et l'endroit où la preuve s'arrête tout simplement."),
    checked=T("Last checked 27 August 2026 — several figures on this page are from live "
              "government pages and will move",
              "Dernière vérification le 27 août 2026 — plusieurs chiffres de cette page "
              "proviennent de pages gouvernementales vivantes et changeront"),
)

# ------------------------------------------------------------------ 1
a.h2(T("First, is the premise even true?", "D'abord, la prémisse est-elle vraie ?"))
a.p(T(
    "The story people tell is short. Canada built a railway across the continent in the "
    "1880s. Today a single pipeline takes ten years to approve and a single subway line "
    "costs more than the whole railway did. Something has gone wrong.",
    "L'histoire que l'on raconte est courte. Le Canada a bâti un chemin de fer d'un océan à "
    "l'autre dans les années 1880. Aujourd'hui, un seul oléoduc met dix ans à être autorisé "
    "et une seule ligne de métro coûte plus cher que tout le chemin de fer. Quelque chose "
    "s'est détraqué."))
a.p(T(
    "Before testing the explanations, it is worth testing the comparison. It turns out that "
    "the number everyone wants — what a 19th-century project cost in today's money, next to "
    "what a modern one costs — does not exist in any official Canadian source.",
    "Avant de vérifier les explications, il vaut la peine de vérifier la comparaison. Il se "
    "trouve que le chiffre que tout le monde veut — ce qu'un projet du 19e siècle coûtait en "
    "argent d'aujourd'hui, à côté de ce que coûte un projet moderne — n'existe dans aucune "
    "source officielle canadienne."))
a.callout(T(
    "<strong>The comparison people want has never been published.</strong> Statistics "
    "Canada's historical railway tables carry figures only from 1946 onward. Its "
    "Infrastructure Construction Price Index, which tracks the cost of roads, bridges and "
    "water systems, begins at reference year 2019. Neither reaches the 1880s. No Government "
    "of Canada, Statistics Canada or auditor's publication located for this page expresses "
    "a 19th-century project's cost in modern dollars beside a modern one. Any sentence of "
    "the form \"the railway cost X in today's money\" is somebody's own arithmetic, not a "
    "sourced fact — so you will not find one here.",
    "<strong>La comparaison que l'on veut n'a jamais été publiée.</strong> Les tableaux "
    "historiques de Statistique Canada sur les chemins de fer ne portent que sur 1946 et les "
    "années suivantes. Son Indice des prix de la construction d'infrastructures, qui suit le "
    "coût des routes, des ponts et des réseaux d'eau, commence à l'année de référence 2019. "
    "Ni l'un ni l'autre ne remonte aux années 1880. Aucune publication du gouvernement du "
    "Canada, de Statistique Canada ou d'un vérificateur repérée pour cette page n'exprime le "
    "coût d'un projet du 19e siècle en dollars d'aujourd'hui à côté d'un projet moderne. "
    "Toute phrase du genre « le chemin de fer a coûté X en argent d'aujourd'hui » est un "
    "calcul personnel, pas un fait attesté — vous n'en trouverez donc pas ici."))
a.p(T(
    "What official data does support is narrower. Non-residential building construction "
    "costs rose 3.6 percent over the year to the first quarter of 2026, on Statistics "
    "Canada's fifteen-city composite. Labour productivity in residential construction fell "
    "37.3 percent between 2001 and 2023, while the business sector as a whole grew 12.5 "
    "percent. Both are real measurements. Neither is about bridges, pipelines or transit, "
    "and the second one is housing, which is a different industry with different firms.",
    "Ce que les données officielles appuient est plus étroit. Les coûts de construction des "
    "bâtiments non résidentiels ont augmenté de 3,6 pour cent sur un an au premier trimestre "
    "de 2026, selon le composite de quinze villes de Statistique Canada. La productivité du "
    "travail dans la construction résidentielle a chuté de 37,3 pour cent entre 2001 et "
    "2023, alors que l'ensemble du secteur des entreprises progressait de 12,5 pour cent. "
    "Ce sont deux mesures réelles. Aucune ne porte sur les ponts, les oléoducs ou le "
    "transport collectif, et la seconde porte sur le logement, qui est une autre industrie "
    "avec d'autres entreprises."))
a.p(T(
    "So the honest starting point is this. Costs are rising, and that is measured. Projects "
    "do take a long time, and that is documented case by case. But \"slower and more "
    "expensive than a century ago, in real terms\" is not something any official Canadian "
    "source has established. That gap is not a detail. It is the most interesting fact in "
    "the whole subject.",
    "Le point de départ honnête est donc le suivant. Les coûts montent, et c'est mesuré. Les "
    "projets prennent effectivement beaucoup de temps, et c'est documenté cas par cas. Mais "
    "« plus lent et plus cher qu'il y a un siècle, en termes réels » n'est établi par aucune "
    "source officielle canadienne. Cette lacune n'est pas un détail. C'est le fait le plus "
    "intéressant de tout le sujet."))

# ------------------------------------------------------------------ 2
a.h2(T("Canada is not unusually slow", "Le Canada n'est pas exceptionnellement lent"))
a.p(T(
    "The strongest comparison available is not a government one. A peer-reviewed study by "
    "Shoshanna Saxe, Matti Siemiatycki, Daniel Durrant and colleagues, published in the "
    "European Journal of Transport and Infrastructure Research in 2021, looked at 26 large "
    "transport projects built between 2000 and 2018 — sixteen in Toronto over 500 million "
    "dollars, ten in London over 500 million pounds.",
    "La meilleure comparaison disponible n'est pas gouvernementale. Une étude évaluée par "
    "les pairs de Shoshanna Saxe, Matti Siemiatycki, Daniel Durrant et leurs collègues, "
    "publiée dans l'European Journal of Transport and Infrastructure Research en 2021, a "
    "examiné 26 grands projets de transport réalisés entre 2000 et 2018 — seize à Toronto de "
    "plus de 500 millions de dollars, dix à Londres de plus de 500 millions de livres."))
a.callout(T(
    "<strong>Toronto 18.8 years. London 18.4 years.</strong> That is the average time from "
    "the first idea to the start of construction, in the two cities, on the study's own "
    "measurement. In both cities, the authors found, more than half of that time on average "
    "was spent in political rather than technical processes.",
    "<strong>Toronto : 18,8 ans. Londres : 18,4 ans.</strong> C'est le temps moyen entre la "
    "première idée et le début des travaux, dans les deux villes, selon la mesure de "
    "l'étude. Dans les deux villes, ont constaté les auteurs, plus de la moitié de ce temps "
    "était en moyenne consacrée à des processus politiques plutôt que techniques."))
a.p(T(
    "Sixteen of the 26 projects had a gestation period of more than ten years. The authors "
    "note that this long phase is not filled with time spent radically innovating; it "
    "reflects, in their words, the fragmented and often fractious ways that communities make "
    "decisions and allocate scarce resources. Professor Saxe put it more simply in her "
    "university's summary: the biggest contributor to delay is the time required for local "
    "or provincial authorities to decide.",
    "Seize des 26 projets ont eu une période de gestation de plus de dix ans. Les auteurs "
    "notent que cette longue phase n'est pas remplie d'innovation radicale ; elle reflète, "
    "selon leurs mots, les façons fragmentées et souvent conflictuelles dont les "
    "collectivités prennent des décisions et répartissent des ressources rares. La "
    "professeure Saxe l'a dit plus simplement dans le résumé de son université : le principal "
    "facteur de retard est le temps qu'il faut aux autorités locales ou provinciales pour "
    "décider."))
a.p(T(
    "This matters for every explanation that follows. London has no Canadian constitution, "
    "no section 35, no Impact Assessment Act and no Canadian provinces — and it takes almost "
    "exactly as long. No government source located for this page states that Canada builds "
    "more slowly than comparable countries. The only comparative evidence found points the "
    "other way.",
    "Cela compte pour toutes les explications qui suivent. Londres n'a pas de constitution "
    "canadienne, pas d'article 35, pas de Loi sur l'évaluation d'impact et pas de provinces "
    "canadiennes — et il y faut presque exactement autant de temps. Aucune source "
    "gouvernementale repérée pour cette page n'affirme que le Canada bâtit plus lentement que "
    "des pays comparables. La seule preuve comparative trouvée va dans l'autre sens."))

# ------------------------------------------------------------------ 3
a.h2(T("Canada is expensive, though", "Le Canada est cher, en revanche"))
a.p(T(
    "Slow and expensive are two different claims, and the evidence points differently on "
    "each. On cost, a January 2025 study by the University of Toronto's School of Cities, "
    "produced with Metrolinx, ranks Canada ninth in the world for transit construction cost "
    "per kilometre.",
    "Lent et cher sont deux affirmations différentes, et la preuve ne pointe pas dans la même "
    "direction pour chacune. Sur le coût, une étude de janvier 2025 de la School of Cities "
    "de l'Université de Toronto, réalisée avec Metrolinx, classe le Canada au neuvième rang "
    "mondial pour le coût de construction du transport collectif par kilomètre."))
a.fig(bar_chart(
    T("Transit construction cost per kilometre, millions of dollars",
      "Coût de construction du transport collectif par kilomètre, en millions de dollars"),
    [(T("Canada", "Canada"), 377),
     (T("Global average", "Moyenne mondiale"), 242)]))
a.p(T(
    "The study's four named drivers are worth listing, because none of them is a permit. "
    "They are overbuilding and overdesign; the loss of in-house expertise, with 25 to 30 "
    "percent of Metrolinx capital project positions filled by consultants; risk management "
    "practice, where contingency and escalation make up about a third of Metrolinx budgets "
    "against caps of 7 to 12 percent in low-cost places; and external constraints such as "
    "political micromanagement and limited competition, which the authors say need deeper "
    "analysis.",
    "Les quatre facteurs nommés par l'étude méritent d'être énumérés, car aucun n'est un "
    "permis. Ce sont la surconstruction et la surconception ; la perte d'expertise interne, "
    "avec 25 à 30 pour cent des postes de projets d'immobilisations de Metrolinx occupés par "
    "des consultants ; les pratiques de gestion du risque, où les provisions et "
    "l'indexation représentent environ le tiers des budgets de Metrolinx contre des plafonds "
    "de 7 à 12 pour cent dans les endroits peu coûteux ; et des contraintes externes comme "
    "la microgestion politique et la concurrence limitée, dont les auteurs disent qu'elles "
    "exigent une analyse plus poussée."))
a.p(T(
    "The same study makes the sharpest then-and-now comparison anyone has published. It "
    "quotes the Ontario Line at over one billion dollars per kilometre and describes that as "
    "roughly ten times the inflation-adjusted per-kilometre cost of Toronto's original 1954 "
    "Yonge subway. That figure belongs to the university, not to a government, and it "
    "compares 1954 with today — not 1885.",
    "La même étude établit la comparaison passé-présent la plus nette jamais publiée. Elle "
    "chiffre la ligne Ontario à plus d'un milliard de dollars par kilomètre et décrit cela "
    "comme environ dix fois le coût par kilomètre, corrigé de l'inflation, du métro original "
    "de la rue Yonge à Toronto en 1954. Ce chiffre appartient à l'université, pas à un "
    "gouvernement, et il compare 1954 à aujourd'hui — pas 1885."))

# ------------------------------------------------------------------ 4
a.h2(T("The usual explanation, checked against the record",
       "L'explication habituelle, confrontée aux documents"))
a.p(T(
    "The explanation you hear most often is environmental review and Indigenous "
    "consultation. It is worth checking against what the responsible bodies actually "
    "publish, because the numbers are smaller than most people expect.",
    "L'explication qu'on entend le plus souvent est l'évaluation environnementale et la "
    "consultation des peuples autochtones. Il vaut la peine de la confronter à ce que les "
    "organismes responsables publient réellement, car les chiffres sont plus petits que ce "
    "que la plupart des gens croient."))
a.ul([
    T("<strong>Federal impact assessment touches very few projects.</strong> The Impact "
      "Assessment Agency of Canada's own page states that only about eight major projects "
      "per year enter the federal impact assessment process. Most building in Canada is "
      "approved by provinces and municipalities, not by Ottawa.",
      "<strong>L'évaluation d'impact fédérale touche très peu de projets.</strong> La page "
      "de l'Agence d'évaluation d'impact du Canada indique qu'environ huit grands projets "
      "par année seulement entrent dans le processus fédéral d'évaluation d'impact. La "
      "plupart des chantiers au Canada sont autorisés par les provinces et les "
      "municipalités, pas par Ottawa."),
    T("<strong>The Agency's own reported processing time is short.</strong> Its 2024-25 "
      "departmental results report gives an average processing time of 91 days across 15 "
      "completed projects. Seven of those received early decisions that no full assessment "
      "was required, so this is not the length of a full assessment.",
      "<strong>Le temps de traitement que l'Agence déclare est court.</strong> Son rapport "
      "sur les résultats ministériels de 2024-2025 donne un temps de traitement moyen de 91 "
      "jours pour 15 projets terminés. Sept d'entre eux ont fait l'objet d'une décision "
      "hâtive selon laquelle aucune évaluation complète n'était requise ; ce n'est donc pas "
      "la durée d'une évaluation complète."),
    T("<strong>Full assessments can still be very long.</strong> Roberts Bank Terminal 2 in "
      "British Columbia was referred to a review panel in January 2014 and approved in April "
      "2023 — nine years and three months. The longest single gap in that file, from August "
      "2020 to September 2021, was the government waiting for information from the company. "
      "It was assessed under the older 2012 law, not the current one.",
      "<strong>Les évaluations complètes peuvent tout de même être très longues.</strong> Le "
      "terminal 2 de Roberts Bank, en Colombie-Britannique, a été renvoyé à une commission "
      "d'examen en janvier 2014 et approuvé en avril 2023 — neuf ans et trois mois. Le plus "
      "long intervalle du dossier, d'août 2020 à septembre 2021, correspond au gouvernement "
      "qui attendait des renseignements de l'entreprise. Le projet a été évalué sous "
      "l'ancienne loi de 2012, pas sous l'actuelle."),
    T("<strong>The Agency says it cannot stop the clock itself.</strong> In its own words, "
      "by law it cannot pause an assessment once it has started — only the project proponent "
      "can. The Agency also says plainly that federal impact assessments have often taken "
      "longer than it would like.",
      "<strong>L'Agence dit ne pas pouvoir arrêter l'horloge elle-même.</strong> Selon ses "
      "propres mots, la loi ne lui permet pas d'interrompre une évaluation une fois "
      "commencée — seul le promoteur du projet le peut. L'Agence dit aussi franchement que "
      "les évaluations d'impact fédérales ont souvent pris plus de temps qu'elle ne le "
      "voudrait."),
])
a.callout(T(
    "<strong>The finding this page is built on.</strong> In the Canadian audits and public "
    "inquiries read for this article — the Auditor General of Canada on the Champlain Bridge, "
    "on shipbuilding and on federal infrastructure spending, the Auditor General of Ontario "
    "on Metrolinx, the Muskrat Falls Commission of Inquiry, and a House of Commons committee "
    "on the Canada Infrastructure Bank — regulatory review and Indigenous consultation are "
    "not named as a primary cost driver. Read that carefully. It is an absence in the audit "
    "record, not a finding that review is free, and not a claim that approvals never delay "
    "anything. The Auditor General of Ontario did name City of Toronto permit approvals and "
    "transit agency design rejections among the causes of delay on the Eglinton Crosstown.",
    "<strong>Le constat qui fonde cette page.</strong> Dans les vérifications et enquêtes "
    "publiques canadiennes lues pour cet article — le vérificateur général du Canada sur le "
    "pont Champlain, sur la construction navale et sur les dépenses fédérales "
    "d'infrastructure, la vérificatrice générale de l'Ontario sur Metrolinx, la Commission "
    "d'enquête sur Muskrat Falls et un comité de la Chambre des communes sur la Banque de "
    "l'infrastructure du Canada — l'examen réglementaire et la consultation des peuples "
    "autochtones ne sont pas nommés comme cause première des coûts. Lisez cela attentivement. "
    "C'est une absence dans les documents de vérification, non un constat selon lequel "
    "l'examen ne coûte rien, ni une affirmation que les autorisations ne retardent jamais "
    "rien. La vérificatrice générale de l'Ontario a bel et bien nommé les permis de la Ville "
    "de Toronto et les rejets de conception par l'agence de transport parmi les causes de "
    "retard du projet Eglinton Crosstown."))

# ------------------------------------------------------------------ 5
a.h2(T("What the auditors actually blame", "Ce que les vérificateurs reprochent réellement"))
a.p(T(
    "Here is what five official Canadian examinations found when they looked at projects "
    "that went badly. The wording in the last column is theirs, not ours.",
    "Voici ce que cinq examens officiels canadiens ont conclu en se penchant sur des projets "
    "qui ont mal tourné. Les mots de la dernière colonne sont les leurs, pas les nôtres."))
a.table(
    [T("Project", "Projet"), T("Who examined it", "Qui l'a examiné"),
     T("What they found", "Ce qu'ils ont conclu")],
    [[T("Replacing Montréal's Champlain Bridge",
        "Remplacement du pont Champlain de Montréal"),
      T("Auditor General of Canada, 2018", "Vérificateur général du Canada, 2018"),
      T("Infrastructure Canada did not plan the replacement in a cost-effective manner. The "
        "public-private model was chosen in 2011 before the analyses were finished, and the "
        "value-for-money work used imprecise estimates based on a design that was only 5 "
        "percent completed, where best practice recommends at least 30 percent. Over 500 "
        "million dollars in avoidable costs from 2015-16 onward.",
        "Infrastructure Canada n'a pas planifié le remplacement de façon rentable. Le modèle "
        "public-privé a été retenu en 2011 avant la fin des analyses, et l'analyse "
        "d'optimisation des ressources reposait sur des estimations imprécises fondées sur "
        "une conception achevée à 5 pour cent seulement, alors que les pratiques exemplaires "
        "recommandent au moins 30 pour cent. Plus de 500 millions de dollars de coûts "
        "évitables à partir de 2015-2016.")],
     [T("Muskrat Falls, Newfoundland and Labrador",
        "Muskrat Falls, Terre-Neuve-et-Labrador"),
      T("Provincial Commission of Inquiry, 2020",
        "Commission d'enquête provinciale, 2020"),
      T("The estimate was clearly influenced by optimism bias, strategic misrepresentation "
        "and political bias. Sanctioned at 6.2 billion dollars, reported at 10.1 billion. "
        "Contingency of 368 million was 6.7 percent of the base estimate, which the "
        "Commissioner called unreasonably low. The province had no capacity or strong "
        "inclination to effectively oversee the Crown corporation it had created.",
        "L'estimation a été clairement influencée par un biais d'optimisme, une "
        "présentation stratégiquement trompeuse et un biais politique. Approuvé à 6,2 "
        "milliards de dollars, déclaré à 10,1 milliards. Une provision de 368 millions "
        "représentait 6,7 pour cent de l'estimation de base, ce que le commissaire a qualifié "
        "de déraisonnablement faible. La province n'avait ni la capacité ni la volonté ferme "
        "de superviser efficacement la société d'État qu'elle avait créée.")],
     [T("Metrolinx light rail lines, Ontario",
        "Lignes de train léger de Metrolinx, Ontario"),
      T("Auditor General of Ontario, 2018 and 2020",
        "Vérificatrice générale de l'Ontario, 2018 et 2020"),
      T("436 million dollars in sunk and additional costs between 2009 and 2018. The "
        "contract did not fully transfer responsibility for the risks of delays and cost "
        "overruns to the private consortium, and about 563 million dollars of risk stayed "
        "with Metrolinx. 63 percent of 2,655 design submissions had issues. The contractor "
        "cited city permit delays and design approval rejections among the causes of delay.",
        "436 millions de dollars en coûts irrécupérables et supplémentaires entre 2009 et "
        "2018. Le contrat n'a pas transféré entièrement au consortium privé la "
        "responsabilité des risques de retard et de dépassement, et environ 563 millions de "
        "dollars de risque sont restés chez Metrolinx. 63 pour cent des 2 655 soumissions de "
        "conception présentaient des problèmes. L'entrepreneur a invoqué les retards de "
        "permis municipaux et les rejets d'approbation de conception parmi les causes de "
        "retard.")],
     [T("National Shipbuilding Strategy", "Stratégie nationale de construction navale"),
      T("Auditor General of Canada, 2021", "Vérificateur général du Canada, 2021"),
      T("The federal fleet renewal experienced many delays in design and construction. Only "
        "2 of the 4 ships scheduled to be delivered by January 2020 were delivered, and some "
        "vessels had already been retired before being replaced.",
        "Le renouvellement de la flotte fédérale a connu de nombreux retards de conception "
        "et de construction. Seuls 2 des 4 navires devant être livrés d'ici janvier 2020 "
        "l'ont été, et certains navires avaient déjà été retirés du service avant d'être "
        "remplacés.")],
     [T("Canada Infrastructure Bank", "Banque de l'infrastructure du Canada"),
      T("House of Commons transport committee, 2022",
        "Comité des transports de la Chambre des communes, 2022"),
      T("Thirteen projects publicly committed but only two finalised investments. Of 420 "
        "proposals received, 82 percent were rejected. About 3 percent of the 35 billion "
        "dollar capital budget had been disbursed and no project was fully completed.",
        "Treize projets annoncés publiquement mais seulement deux investissements finalisés. "
        "Sur 420 propositions reçues, 82 pour cent ont été rejetées. Environ 3 pour cent du "
        "budget d'immobilisations de 35 milliards de dollars avait été versé et aucun projet "
        "n'était entièrement terminé.")]],
    label=T("What five official Canadian examinations found — scroll sideways to see all of "
            "it",
            "Ce que cinq examens officiels canadiens ont conclu — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "The same words keep coming back: estimating failures, optimism bias, governance "
    "failure, scope change after the contract is signed, and risk that was supposed to move "
    "to the private partner and did not. To that list the University of Toronto study adds "
    "the most concrete of them all. Canadian projects typically go out to bid at 1 to 10 "
    "percent design completion. In Paris, Milan and Istanbul, designs are advanced to 30 to "
    "70 percent before procurement. Signing a contract before you know what you are building "
    "is a decision, and it is made long before any regulator sees the file.",
    "Les mêmes mots reviennent : erreurs d'estimation, biais d'optimisme, défaillance de "
    "gouvernance, changement de portée après la signature du contrat, et risque censé passer "
    "au partenaire privé mais qui n'y est pas passé. À cette liste, l'étude de l'Université "
    "de Toronto ajoute le plus concret de tous. Les projets canadiens vont généralement en "
    "appel d'offres avec une conception achevée à 1 à 10 pour cent. À Paris, à Milan et à "
    "Istanbul, les conceptions sont poussées de 30 à 70 pour cent avant l'approvisionnement. "
    "Signer un contrat avant de savoir ce qu'on bâtit est une décision, et elle est prise "
    "bien avant qu'un organisme de réglementation ne voie le dossier."))
a.p(T(
    "One more check is worth making. Professor Siemiatycki, in work presented to Queen's "
    "University's Institute of Intergovernmental Relations, reports that nine out of ten "
    "projects experience a cost overrun, that the average overrun is 28 percent across all "
    "project types and 45 percent for transit, and that the pattern has been unchanged for "
    "seventy years. If overruns predate most of the modern process, then the modern process "
    "cannot be the whole explanation for them.",
    "Une autre vérification vaut la peine. Le professeur Siemiatycki, dans des travaux "
    "présentés à l'Institut des relations intergouvernementales de l'Université Queen's, "
    "rapporte que neuf projets sur dix connaissent un dépassement de coûts, que le "
    "dépassement moyen est de 28 pour cent tous types confondus et de 45 pour cent pour le "
    "transport collectif, et que ce schéma est inchangé depuis soixante-dix ans. Si les "
    "dépassements précèdent l'essentiel du processus moderne, ce processus ne peut pas les "
    "expliquer à lui seul."))

# ------------------------------------------------------------------ 6
a.h2(T("One project, followed all the way through",
       "Un projet, suivi du début à la fin"))
a.p(T(
    "The Trans Mountain expansion is the most fully documented large project in Canada, "
    "because a regulator, a court, a parliamentary officer and the government all published "
    "on it. It is also unrepresentative: it is the most litigated project in the energy "
    "regulator's entire register, with more than sixteen separate court challenges. Read it "
    "as one detailed example, not as the average.",
    "L'agrandissement de Trans Mountain est le grand projet le mieux documenté au Canada, "
    "parce qu'un organisme de réglementation, un tribunal, un officier parlementaire et le "
    "gouvernement ont tous publié à son sujet. Il n'est pas non plus représentatif : c'est le "
    "projet le plus contesté en justice de tout le registre de l'organisme de réglementation "
    "de l'énergie, avec plus de seize recours distincts. Lisez-le comme un exemple détaillé, "
    "pas comme une moyenne."))
a.table(
    [T("When", "Quand"), T("What happened", "Ce qui s'est passé")],
    [[T("16 December 2013", "16 décembre 2013"),
      T("The company files its application. Cost estimate 5.4 billion dollars, in service "
        "December 2019.",
        "L'entreprise dépose sa demande. Estimation de coût : 5,4 milliards de dollars, mise "
        "en service en décembre 2019.")],
     [T("November 2016", "Novembre 2016"),
      T("Cabinet directs the regulator to issue a certificate. The estimate is now 7.4 "
        "billion dollars.",
        "Le Cabinet ordonne à l'organisme de réglementation de délivrer un certificat. "
        "L'estimation est maintenant de 7,4 milliards de dollars.")],
     [T("31 August 2018", "31 août 2018"),
      T("The Government of Canada buys the pipeline and the expansion for 4.4 billion "
        "dollars, net of adjustments.",
        "Le gouvernement du Canada achète l'oléoduc et l'agrandissement pour 4,4 milliards "
        "de dollars, déduction faite des ajustements.")],
     [T("30 August 2018", "30 août 2018"),
      T("The Federal Court of Appeal quashes the approval on two grounds: the regulator "
        "wrongly excluded marine shipping impacts, and Canada failed to properly execute its "
        "legal duty to consult with Indigenous peoples.",
        "La Cour d'appel fédérale annule l'approbation pour deux motifs : l'organisme de "
        "réglementation a écarté à tort les effets du transport maritime, et le Canada n'a "
        "pas exécuté correctement son obligation légale de consulter les peuples "
        "autochtones.")],
     [T("18 June 2019", "18 juin 2019"),
      T("After renewed consultations, the government approves the project again, subject to "
        "156 binding conditions.",
        "Après de nouvelles consultations, le gouvernement approuve de nouveau le projet, "
        "sous réserve de 156 conditions contraignantes.")],
     [T("2 July 2020", "2 juillet 2020"),
      T("The Supreme Court of Canada refuses leave to appeal, leaving the renewed "
        "consultations standing. Litigation ends here.",
        "La Cour suprême du Canada refuse l'autorisation d'appel, laissant en place les "
        "nouvelles consultations. Les recours judiciaires prennent fin ici.")],
     [T("2022 and 2024", "2022 et 2024"),
      T("The Parliamentary Budget Officer records estimates of 21.4 billion dollars and then "
        "34.2 billion dollars — an increase of 12.8 billion in two years, years after the "
        "litigation ended.",
        "Le directeur parlementaire du budget consigne des estimations de 21,4 milliards de "
        "dollars puis de 34,2 milliards — une hausse de 12,8 milliards en deux ans, des "
        "années après la fin des recours.")],
     [T("30 April 2024", "30 avril 2024"),
      T("The Canada Energy Regulator issues the final authorisation to operate.",
        "La Régie de l'énergie du Canada délivre l'autorisation finale d'exploitation.")]],
    label=T("Trans Mountain expansion, application to final authorisation — scroll sideways "
            "to see all of it",
            "Agrandissement de Trans Mountain, de la demande à l'autorisation finale — "
            "faites défiler latéralement pour tout voir"))
a.p(T(
    "Application to final authorisation to operate: 16 December 2013 to 30 April 2024. Ten "
    "years and four and a half months. Cost estimate at application 5.4 billion dollars; "
    "cost estimate in 2024, 34.2 billion.",
    "De la demande à l'autorisation finale d'exploitation : du 16 décembre 2013 au 30 avril "
    "2024. Dix ans et quatre mois et demi. Estimation de coût au dépôt de la demande : 5,4 "
    "milliards de dollars ; estimation de coût en 2024 : 34,2 milliards."))
a.callout(T(
    "<strong>Nobody official has said what caused that increase.</strong> The Parliamentary "
    "Budget Officer's 2024 report does not identify specific causes for the 12.8 billion "
    "dollar escalation, and no official source located apportions the increase between court "
    "delay, consultation, scope, materials, labour or interest. Note also the shape of the "
    "timeline: the estimate rose from 5.4 to 7.4 billion before the 2018 court ruling, and "
    "from 21.4 to 34.2 billion years after all litigation had ended. Anyone telling you the "
    "court case cost a specific number of billions is telling you something no published "
    "source supports.",
    "<strong>Aucune source officielle n'a dit ce qui a causé cette hausse.</strong> Le "
    "rapport de 2024 du directeur parlementaire du budget ne relève pas de causes précises "
    "pour l'escalade de 12,8 milliards de dollars, et aucune source officielle repérée ne "
    "répartit la hausse entre les délais judiciaires, la consultation, la portée, les "
    "matériaux, la main-d'oeuvre ou les intérêts. Notez aussi la forme du calendrier : "
    "l'estimation est passée de 5,4 à 7,4 milliards avant la décision judiciaire de 2018, et "
    "de 21,4 à 34,2 milliards des années après la fin de tous les recours. Quiconque vous "
    "affirme que le procès a coûté un nombre précis de milliards vous dit une chose "
    "qu'aucune source publiée n'appuie."))

# ------------------------------------------------------------------ 7
a.h2(T("The legal layer that did not exist in 1885",
       "La couche juridique qui n'existait pas en 1885"))
a.p(T(
    "Something real did change, and it is not a matter of opinion. A modern project must "
    "satisfy a set of laws that a 19th-century railway builder never faced. Here is the "
    "layer, with the date each part of it arrived and what it asks for.",
    "Quelque chose a réellement changé, et ce n'est pas une question d'opinion. Un projet "
    "moderne doit satisfaire un ensemble de lois qu'un bâtisseur de chemin de fer du 19e "
    "siècle n'a jamais connues. Voici cette couche, avec la date d'arrivée de chaque élément "
    "et ce qu'il exige."))
a.table(
    [T("Since", "Depuis"), T("What it is", "De quoi il s'agit"),
     T("What it requires, and why it exists",
       "Ce qu'il exige, et pourquoi il existe")],
    [[T("1868", "1868"), T("Fisheries Act", "Loi sur les pêches"),
      T("One of Canada's oldest statutes. Its pollution provisions forbid putting harmful "
        "substances into water where fish live, and its habitat provisions were added later. "
        "Work in or near water usually needs an authorisation from the federal fisheries "
        "department.",
        "L'une des plus anciennes lois du Canada. Ses dispositions sur la pollution "
        "interdisent de rejeter des substances nocives dans des eaux fréquentées par le "
        "poisson, et ses dispositions sur l'habitat ont été ajoutées plus tard. Les travaux "
        "dans l'eau ou à proximité exigent habituellement une autorisation du ministère "
        "fédéral des pêches.")],
     [T("1882", "1882"), T("Navigable waters protection",
                           "Protection des eaux navigables"),
      T("Three years before the last spike. It protects the public right to travel by water. "
        "Renamed the Canadian Navigable Waters Act in 2019; major works likely to interfere "
        "substantially with navigation need Transport Canada approval.",
        "Trois ans avant le dernier crampon. Elle protège le droit public de circuler par "
        "voie d'eau. Rebaptisée Loi sur les eaux navigables canadiennes en 2019 ; les "
        "ouvrages majeurs susceptibles de gêner sensiblement la navigation exigent "
        "l'approbation de Transports Canada.")],
     [T("1973 and 1995", "1973 et 1995"),
      T("Federal environmental assessment", "Évaluation environnementale fédérale"),
      T("There was no federal environmental assessment of any kind before 1973, and no "
        "statute in force until 1995. Today the Impact Assessment Act sets legislated time "
        "limits: 180 days for the planning phase, 300 days for an agency-led assessment, up "
        "to 600 days for a review panel.",
        "Il n'existait aucune évaluation environnementale fédérale avant 1973, et aucune loi "
        "en vigueur avant 1995. Aujourd'hui, la Loi sur l'évaluation d'impact fixe des "
        "délais légaux : 180 jours pour la phase préparatoire, 300 jours pour une évaluation "
        "menée par l'Agence, jusqu'à 600 jours pour une commission d'examen.")],
     [T("1976 and 1979", "1976 et 1979"),
      T("Occupational health and safety", "Santé et sécurité au travail"),
      T("Ontario's Occupational Health and Safety Act came into force in 1979, after the Ham "
        "Commission of 1976 into the health and safety of workers in mines. It created the "
        "internal responsibility system and a worker's right to refuse unsafe work.",
        "La Loi sur la santé et la sécurité au travail de l'Ontario est entrée en vigueur en "
        "1979, après la commission Ham de 1976 sur la santé et la sécurité des mineurs. Elle "
        "a créé le système de responsabilité interne et le droit du travailleur de refuser un "
        "travail dangereux.")],
     [T("2002", "2002"), T("Species at Risk Act", "Loi sur les espèces en péril"),
      T("Activities that would affect a listed species need a permit under section 73. "
        "Before 2002 there was no federal statute of this kind.",
        "Les activités touchant une espèce inscrite exigent un permis en vertu de l'article "
        "73. Avant 2002, il n'existait aucune loi fédérale de ce genre.")],
     [T("2004", "2004"),
      T("The constitutional duty to consult",
        "L'obligation constitutionnelle de consulter"),
      T("Section 35 of the Constitution Act, 1982 recognises and affirms existing Aboriginal "
        "and treaty rights. In Haida Nation in 2004 the Supreme Court held that the Crown "
        "must consult even where rights are claimed but not yet proven. Before that trilogy "
        "of cases, consultation was owed only after rights had been proven through lengthy "
        "litigation. The Library of Parliament explains the duty flows from the honour of "
        "the Crown and cannot be removed by legislation.",
        "L'article 35 de la Loi constitutionnelle de 1982 reconnaît et confirme les droits "
        "ancestraux et issus de traités existants. Dans l'arrêt Nation haïda de 2004, la Cour "
        "suprême a jugé que la Couronne doit consulter même lorsque les droits sont "
        "revendiqués sans être encore prouvés. Avant cette trilogie, la consultation n'était "
        "due qu'une fois les droits prouvés au terme de longs litiges. La Bibliothèque du "
        "Parlement explique que l'obligation découle de l'honneur de la Couronne et ne peut "
        "être écartée par une loi.")],
     [T("Modern law", "Droit moderne"), T("Expropriation", "Expropriation"),
      T("The federal Expropriation Act sets out notice, publication in the Canada Gazette, a "
        "30-day window to object, a public hearing if anyone objects, a hearing officer's "
        "report within 30 days, and a written compensation offer with an appraisal within 90 "
        "days. The railway did not use this route: in 1881 Canada granted land instead, an "
        "area Library and Archives Canada describes as the size of England.",
        "La Loi sur l'expropriation fédérale prévoit un avis, une publication dans la Gazette "
        "du Canada, un délai de 30 jours pour s'opposer, une audience publique en cas "
        "d'opposition, un rapport de l'agent d'audience dans les 30 jours, et une offre "
        "écrite d'indemnité accompagnée d'une évaluation dans les 90 jours. Le chemin de fer "
        "n'a pas emprunté cette voie : en 1881, le Canada a plutôt concédé des terres, une "
        "superficie que Bibliothèque et Archives Canada décrit comme équivalente à celle de "
        "l'Angleterre.")],
     [T("Local", "Local"), T("Municipal permits and zoning",
                             "Permis municipaux et zonage"),
      T("Approvals from cities and towns sit on top of everything federal. Canada Mortgage "
        "and Housing Corporation publishes an approval delay index in which Greater Toronto "
        "and Greater Vancouver take almost four times as long as the fastest regions. That "
        "index measures housing, not major infrastructure, and it is an index rather than a "
        "number of months.",
        "Les autorisations des villes s'ajoutent à tout ce qui est fédéral. La Société "
        "canadienne d'hypothèques et de logement publie un indice des délais d'approbation "
        "où le Grand Toronto et le Grand Vancouver prennent près de quatre fois plus de temps "
        "que les régions les plus rapides. Cet indice mesure le logement, pas les grandes "
        "infrastructures, et c'est un indice plutôt qu'un nombre de mois.")]],
    label=T("The legal layer, and when each part arrived — scroll sideways to see all of it",
            "La couche juridique, et l'arrivée de chacun de ses éléments — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "One correction is worth making here. It is not true that nothing was regulated in 1885. "
    "The Fisheries Act dates from 1868 and navigable waters protection from 1882. There were "
    "fewer rules, and they protected different things.",
    "Une correction s'impose ici. Il est faux de dire que rien n'était réglementé en 1885. La "
    "Loi sur les pêches date de 1868 et la protection des eaux navigables de 1882. Il y avait "
    "moins de règles, et elles protégeaient autre chose."))

# ------------------------------------------------------------------ 8
a.h2(T("Uncertainty about the law is itself a cost",
       "L'incertitude juridique est elle-même un coût"))
a.p(T(
    "Between 2019 and 2024 the central federal statute governing major project review was "
    "challenged, largely struck down and rewritten. This is documented entirely in official "
    "sources, and it is a different problem from any single permit taking too long.",
    "Entre 2019 et 2024, la principale loi fédérale régissant l'examen des grands projets a "
    "été contestée, largement invalidée puis réécrite. Tout cela est documenté dans des "
    "sources officielles, et c'est un problème différent de celui d'un permis qui tarde."))
a.ul([
    T("<strong>August 2019</strong> — the Impact Assessment Act comes into force.",
      "<strong>Août 2019</strong> — la Loi sur l'évaluation d'impact entre en vigueur."),
    T("<strong>September 2019 to 2022</strong> — Alberta petitions its Court of Appeal and "
      "wins there, four to one, in May 2022.",
      "<strong>De septembre 2019 à 2022</strong> — l'Alberta saisit sa Cour d'appel et "
      "obtient gain de cause, à quatre contre un, en mai 2022."),
    T("<strong>October 2023</strong> — the Supreme Court of Canada, five to two, finds most "
      "of the Act unconstitutional. The majority called the breadth of the definition of "
      "effects within federal jurisdiction astonishing, and said the Act gave "
      "decision-makers practically untrammelled power to regulate projects as projects. The "
      "parts covering federal lands and federally funded projects survived. Two justices "
      "dissented, arguing for cooperative federalism and a narrower reading of the statute.",
      "<strong>Octobre 2023</strong> — la Cour suprême du Canada, à cinq contre deux, juge "
      "l'essentiel de la loi inconstitutionnel. La majorité a qualifié d'étonnante l'ampleur "
      "de la définition des effets relevant de la compétence fédérale, et a dit que la loi "
      "conférait aux décideurs un pouvoir pratiquement sans entrave de réglementer les "
      "projets en tant que projets. Les parties visant les terres fédérales et les projets "
      "financés par le fédéral ont survécu. Deux juges étaient dissidents, plaidant pour le "
      "fédéralisme coopératif et une lecture plus étroite de la loi."),
    T("<strong>June 2024</strong> — Parliament rewrites the Act. Federal jurisdiction is "
      "narrowed to adverse effects within federal jurisdiction, requiring a non-negligible "
      "adverse change. The Impact Assessment Agency says the amended framework restores "
      "certainty and clarity. Alberta says it will monitor progress and take action as "
      "needed.",
      "<strong>Juin 2024</strong> — le Parlement réécrit la loi. La compétence fédérale est "
      "resserrée aux effets négatifs relevant de la compétence fédérale, exigeant un "
      "changement négatif non négligeable. L'Agence d'évaluation d'impact affirme que le "
      "cadre modifié rétablit la certitude et la clarté. L'Alberta dit qu'elle surveillera "
      "les progrès et agira au besoin."),
])
a.p(T(
    "For five years, a company deciding whether to spend billions of dollars could not be "
    "certain which government would review its project or under what rules. That is a real "
    "cost, and unlike most of the costs on this page it has a documented beginning and end.",
    "Pendant cinq ans, une entreprise qui décidait de dépenser des milliards ne pouvait pas "
    "savoir avec certitude quel gouvernement examinerait son projet ni selon quelles règles. "
    "C'est un coût réel et, contrairement à la plupart des coûts de cette page, il a un début "
    "et une fin documentés."))

# ------------------------------------------------------------------ 9
a.h2(T("What the fast way actually cost", "Ce que la manière rapide a réellement coûté"))
a.p(T(
    "Any comparison with the railway era has to include the other side of the ledger. All of "
    "the following comes from Parks Canada, from federal departments and from a Prime "
    "Minister speaking in the House of Commons.",
    "Toute comparaison avec l'époque du chemin de fer doit inclure l'autre colonne du grand "
    "livre. Tout ce qui suit provient de Parcs Canada, de ministères fédéraux et d'un premier "
    "ministre s'exprimant à la Chambre des communes."))
a.ul([
    T("<strong>The Québec Bridge, 29 August 1907</strong> — the south section of the frame "
      "collapsed, killing 76 workers, 33 of them Mohawk workers from the Kahnawake "
      "community. A second collapse on 11 September 1916 killed 13 more.",
      "<strong>Le pont de Québec, le 29 août 1907</strong> — la section sud de la charpente "
      "s'est effondrée, tuant 76 travailleurs, dont 33 travailleurs mohawks de la communauté "
      "de Kahnawake. Un second effondrement, le 11 septembre 1916, en a tué 13 autres."),
    T("<strong>Rogers Pass, 4 March 1910</strong> — 58 workers died in a single avalanche "
      "while clearing an earlier slide. Between 1885 and 1911 avalanches on that line killed "
      "more than 200 workers and passengers. The railway eventually abandoned the route for "
      "a tunnel.",
      "<strong>Le col Rogers, le 4 mars 1910</strong> — 58 travailleurs sont morts dans une "
      "seule avalanche pendant qu'ils dégageaient une coulée antérieure. Entre 1885 et 1911, "
      "les avalanches sur cette ligne ont tué plus de 200 travailleurs et passagers. Le "
      "chemin de fer a fini par abandonner ce tracé pour un tunnel."),
    T("<strong>Pay on the railway</strong> — Parks Canada records that Chinese workers, "
      "though considered excellent workers, received only a dollar a day, half the pay of a "
      "white worker, and that hundreds died from accidents or illness because the work was "
      "dangerous and living conditions poor. A Prime Minister said in 2006 that some one "
      "thousand Chinese labourers died building the railway. The exact number is not known.",
      "<strong>La paie sur le chemin de fer</strong> — Parcs Canada consigne que les "
      "travailleurs chinois, bien que considérés comme excellents, ne recevaient qu'un dollar "
      "par jour, la moitié de la paie d'un travailleur blanc, et que des centaines sont morts "
      "d'accidents ou de maladie parce que le travail était dangereux et les conditions de vie "
      "mauvaises. Un premier ministre a déclaré en 2006 que quelque mille ouvriers chinois "
      "sont morts en bâtissant le chemin de fer. Le nombre exact n'est pas connu."),
    T("<strong>The head tax, legislated in 1885</strong> — the same year the last spike was "
      "driven, Parliament imposed a duty of 50 dollars on Chinese people entering Canada. It "
      "rose to 100 dollars in 1900 and 500 dollars in 1903, which the Prime Minister's 2006 "
      "address described as the equivalent of two years' wages, before near-total exclusion "
      "in 1923. He called these race-based financial measures aimed solely at the Chinese, "
      "implemented with deliberation by the Canadian state.",
      "<strong>La taxe d'entrée, adoptée en 1885</strong> — l'année même où l'on a planté le "
      "dernier crampon, le Parlement a imposé un droit de 50 dollars aux personnes chinoises "
      "entrant au Canada. Il est passé à 100 dollars en 1900 et à 500 dollars en 1903, ce que "
      "le discours du premier ministre en 2006 a décrit comme l'équivalent de deux années de "
      "salaire, avant une exclusion presque totale en 1923. Il a qualifié ces mesures de "
      "mesures financières fondées sur la race, visant uniquement les Chinois, mises en "
      "oeuvre délibérément par l'État canadien."),
    T("<strong>The land</strong> — the Numbered Treaties of 1871 to 1921 were made, in the "
      "words of Crown-Indigenous Relations and Northern Affairs Canada, because Canada needed "
      "to secure Aboriginal land claims after acquiring the Hudson's Bay Company charter, and "
      "because officials feared American expansionism and saw western expansion as vital to "
      "Canada's economic future. Annuities were 3 to 5 dollars per person; reserves were 160 "
      "to 640 acres per family of five. The same department writes that the early treaties "
      "served as the vehicle by which the Department of Indian Affairs implemented existing "
      "and future assimilation policies.",
      "<strong>Les terres</strong> — les traités numérotés de 1871 à 1921 ont été conclus, "
      "selon les mots de Relations Couronne-Autochtones et Affaires du Nord Canada, parce que "
      "le Canada devait régler les revendications territoriales autochtones après "
      "l'acquisition de la charte de la Compagnie de la Baie d'Hudson, et parce que les "
      "responsables craignaient l'expansionnisme américain et voyaient l'expansion vers "
      "l'Ouest comme vitale pour l'avenir économique du Canada. Les annuités étaient de 3 à 5 "
      "dollars par personne ; les réserves, de 160 à 640 acres par famille de cinq. Le même "
      "ministère écrit que les premiers traités ont servi de véhicule par lequel le ministère "
      "des Affaires indiennes a mis en oeuvre les politiques d'assimilation existantes et "
      "futures."),
    T("<strong>And no law stood in the way of any of it.</strong> There was no occupational "
      "health and safety statute, no environmental assessment, and no duty to consult. Those "
      "arrived in 1979, 1973 and 2004 respectively.",
      "<strong>Et aucune loi ne s'y opposait.</strong> Il n'y avait ni loi sur la santé et la "
      "sécurité au travail, ni évaluation environnementale, ni obligation de consulter. Elles "
      "sont arrivées en 1979, en 1973 et en 2004 respectivement."),
])
a.p(T(
    "Against that, here is what the modern process buys, in countable things rather than "
    "principles. Roberts Bank Terminal 2 was approved subject to 370 legally binding "
    "conditions and a 150 million dollar financial guarantee, after the Agency consulted 48 "
    "Indigenous Nations and the port authority concluded benefit agreements with 26 of them. "
    "Trans Mountain carries 156 conditions and a lifecycle regulator that inspects and "
    "audits after approval. In a single quarter the Impact Assessment Agency reported 25 "
    "post-decision inspections, 1.9 million dollars of public and Indigenous participation "
    "funding and 1.8 million dollars of Indigenous capacity funding.",
    "En face, voici ce que le processus moderne achète, en choses dénombrables plutôt qu'en "
    "principes. Le terminal 2 de Roberts Bank a été approuvé sous réserve de 370 conditions "
    "juridiquement contraignantes et d'une garantie financière de 150 millions de dollars, "
    "après que l'Agence eut consulté 48 nations autochtones et que l'administration portuaire "
    "eut conclu des ententes sur les répercussions et les avantages avec 26 d'entre elles. "
    "Trans Mountain porte 156 conditions et relève d'un organisme de réglementation du cycle "
    "de vie qui inspecte et vérifie après l'approbation. En un seul trimestre, l'Agence "
    "d'évaluation d'impact a déclaré 25 inspections postérieures à la décision, 1,9 million "
    "de dollars de financement de la participation du public et des Autochtones et 1,8 "
    "million de dollars de financement des capacités autochtones."))
a.p(T(
    "Those are the two columns. The 1880s are not a control group for a modern experiment: "
    "they were a different society, with different accounting, and much of what made the "
    "railway fast is precisely what modern law was written to prevent. Weighing the speed "
    "against the protections is a judgement, and it belongs to you rather than to this page.",
    "Voilà les deux colonnes. Les années 1880 ne sont pas un groupe témoin pour une "
    "expérience moderne : c'était une autre société, avec une autre comptabilité, et une "
    "grande partie de ce qui rendait le chemin de fer rapide est précisément ce que le droit "
    "moderne a été écrit pour empêcher. Mettre en balance la vitesse et les protections est "
    "un jugement, et il vous appartient plutôt qu'à cette page."))
a.callout(T(
    "Professor Saxe, whose study found Toronto and London almost level, framed the trade-off "
    "this way: \"Consultation and consideration before we invest billions of dollars is "
    "important. But there is also an opportunity cost to not acting.\"",
    "La professeure Saxe, dont l'étude a trouvé Toronto et Londres presque à égalité, a "
    "formulé le compromis ainsi : « La consultation et la réflexion avant d'investir des "
    "milliards de dollars sont importantes. Mais ne pas agir a aussi un coût "
    "d'opportunité. »"))

# ------------------------------------------------------------------ 10
a.h2(T("What Canada is doing about it now", "Ce que le Canada fait maintenant"))
a.p(T(
    "Canada's answer so far is the Building Canada Act and the Major Projects Office, which "
    "opened in August 2025 with a target of cutting federal approval time from five years or "
    "more down to two. We have a separate page on what that office is, what the law lets it "
    "do and what it has actually achieved.",
    "La réponse du Canada jusqu'ici est la Loi sur la construction du Canada et le Bureau des "
    "grands projets, ouvert en août 2025 avec l'objectif de ramener le délai d'approbation "
    "fédérale de cinq ans ou plus à deux ans. Nous avons une page distincte sur ce qu'est ce "
    "bureau, sur ce que la loi lui permet de faire et sur ce qu'il a réellement accompli."))
a.ul([
    link("canada-major-projects-office-explained.html",
         T("Canada's big projects — what is built, and what is on paper",
           "Les grands projets du Canada — ce qui est bâti et ce qui est sur papier")),
])
a.p(T(
    "Three things are worth adding here, checked on 27 August 2026. First, Schedule 1 of the "
    "Building Canada Act — the list of designated national interest projects — is still "
    "empty. The consolidated statute shows only the column headings. Being referred to the "
    "office is not the same as being designated under the law.",
    "Trois éléments méritent d'être ajoutés ici, vérifiés le 27 août 2026. D'abord, l'annexe "
    "1 de la Loi sur la construction du Canada — la liste des projets désignés d'intérêt "
    "national — est toujours vide. La loi codifiée n'affiche que les en-têtes de colonnes. "
    "Être confié au bureau n'équivaut pas à être désigné par la loi."))
a.p(T(
    "Second, the first concrete step toward listing anything appeared in a supplement to the "
    "Canada Gazette on 1 August 2026. It gives notice that cabinet may add the West Coast "
    "Oil Pipeline to Schedule 1 — a line of about 1,250 kilometres from Bruderheim, Alberta "
    "to a deepwater port near Delta, British Columbia, with a capacity of one million barrels "
    "a day, proposed by Trans Mountain Corporation, the Alberta Petroleum Marketing "
    "Commission and Pembina Pipeline Corporation. Public input closes on 18 September 2026.",
    "Ensuite, le premier pas concret vers l'inscription de quoi que ce soit est paru dans un "
    "supplément de la Gazette du Canada le 1er août 2026. Il donne avis que le Cabinet "
    "pourrait ajouter l'oléoduc de la côte Ouest à l'annexe 1 — une conduite d'environ 1 250 "
    "kilomètres reliant Bruderheim, en Alberta, à un port en eau profonde près de Delta, en "
    "Colombie-Britannique, d'une capacité d'un million de barils par jour, proposée par Trans "
    "Mountain Corporation, l'Alberta Petroleum Marketing Commission et Pembina Pipeline "
    "Corporation. La période de commentaires du public se termine le 18 septembre 2026."))
a.p(T(
    "Third, the energy regulator has published what its own reviews take. For large pipeline "
    "projects of more than 40 kilometres, deciding whether an application is complete takes "
    "144 to 286 days, and the hearing phase takes 374 to 451 days. For small projects under "
    "40 kilometres, the average time from application to decision fell from 144 days in "
    "2019-20 to 111 days in 2024-25. Those are the regulator's figures, from a briefing "
    "binder prepared for a House of Commons committee in June 2026.",
    "Enfin, l'organisme de réglementation de l'énergie a publié la durée de ses propres "
    "examens. Pour les grands projets d'oléoducs de plus de 40 kilomètres, déterminer si une "
    "demande est complète prend de 144 à 286 jours, et la phase d'audience de 374 à 451 "
    "jours. Pour les petits projets de moins de 40 kilomètres, le délai moyen entre la "
    "demande et la décision est passé de 144 jours en 2019-2020 à 111 jours en 2024-2025. Ce "
    "sont les chiffres de l'organisme, tirés d'un cahier d'information préparé pour un comité "
    "de la Chambre des communes en juin 2026."))

# ------------------------------------------------------------------ 11
a.h2(T("What is genuinely contested", "Ce qui est réellement contesté"))
a.p(T(
    "These are live disagreements between serious people, and this page does not resolve "
    "them. Each position is given with the body that holds it.",
    "Ce sont des désaccords bien vivants entre gens sérieux, et cette page ne les tranche "
    "pas. Chaque position est présentée avec l'organisme qui la défend."))
a.table(
    [T("The question", "La question"), T("One position", "Une position"),
     T("The other", "L'autre")],
    [[T("Is regulation the main brake, or is it internal capability?",
        "La réglementation est-elle le principal frein, ou est-ce la capacité interne ?"),
      T("The Bank of Canada, reporting what firms told it, said companies are naturally wary "
        "of a regulatory approval process that can be both lengthy and unpredictable. The "
        "Government of Canada built the Building Canada Act around the same view, with a "
        "target of two years.",
        "La Banque du Canada, rapportant ce que les entreprises lui ont dit, a déclaré que "
        "les entreprises se méfient naturellement d'un processus d'approbation réglementaire "
        "qui peut être à la fois long et imprévisible. Le gouvernement du Canada a bâti la "
        "Loi sur la construction du Canada sur la même vision, avec une cible de deux ans."),
      T("The University of Toronto School of Cities names overbuilding, lost in-house "
        "expertise, contingency practice and bidding at 1 to 10 percent design — not "
        "permitting. The Impact Assessment Agency says only about eight major projects a year "
        "enter its process.",
        "La School of Cities de l'Université de Toronto nomme la surconstruction, la perte "
        "d'expertise interne, les pratiques de provisionnement et les appels d'offres à 1 à "
        "10 pour cent de conception — pas les autorisations. L'Agence d'évaluation d'impact "
        "dit qu'environ huit grands projets par année seulement entrent dans son processus.")],
     [T("Was the Impact Assessment Act a legitimate federal law?",
        "La Loi sur l'évaluation d'impact était-elle une loi fédérale légitime ?"),
      T("The Supreme Court majority, five to two, held that the designated projects scheme "
        "was unconstitutional. The Government of Alberta says the Act intruded into "
        "provincial jurisdiction and harmed its economy and regulatory certainty.",
        "La majorité de la Cour suprême, à cinq contre deux, a jugé inconstitutionnel le "
        "régime des projets désignés. Le gouvernement de l'Alberta affirme que la loi "
        "empiétait sur la compétence provinciale et a nui à son économie et à sa certitude "
        "réglementaire."),
      T("Two dissenting justices argued for cooperative federalism and a narrow reading that "
        "would have saved the Act. The Impact Assessment Agency says the 2024 amendments now "
        "anchor decisions in areas of clear federal jurisdiction and restore certainty and "
        "clarity.",
        "Deux juges dissidents ont plaidé pour le fédéralisme coopératif et une "
        "interprétation étroite qui aurait sauvé la loi. L'Agence d'évaluation d'impact dit "
        "que les modifications de 2024 ancrent désormais les décisions dans des domaines de "
        "compétence fédérale claire et rétablissent la certitude et la clarté.")],
     [T("Does the Building Canada Act speed things up or override rights?",
        "La Loi sur la construction du Canada accélère-t-elle les choses ou écarte-t-elle des "
        "droits ?"),
      T("Nine First Nations in Ontario launched a constitutional challenge to the federal "
        "Bill C-5 and Ontario's Bill 5, and five more later joined. Ontario Regional Chief "
        "Abram Benedict said in June 2025 that they are not anti-development and want their "
        "communities to prosper, but will not accept laws that silence their voices.",
        "Neuf Premières Nations de l'Ontario ont lancé une contestation constitutionnelle "
        "contre le projet de loi fédéral C-5 et le projet de loi 5 de l'Ontario, et cinq "
        "autres s'y sont jointes ensuite. Le chef régional de l'Ontario Abram Benedict a dit "
        "en juin 2025 qu'ils ne sont pas contre le développement et veulent que leurs "
        "communautés prospèrent, mais qu'ils n'accepteront pas des lois qui font taire leurs "
        "voix."),
      T("The Government of Canada says that listing a project under the Act does not alter "
        "Canada's obligation to see through the impact assessment and regulatory processes "
        "set out in modern treaties.",
        "Le gouvernement du Canada affirme que l'inscription d'un projet en vertu de la loi "
        "ne modifie en rien l'obligation du Canada de mener à terme les processus "
        "d'évaluation d'impact et de réglementation prévus dans les traités modernes.")],
     [T("Was the public-private model a saving or a cost?",
        "Le modèle public-privé était-il une économie ou un coût ?"),
      T("The Auditor General of Canada found the public-private decision came before the "
        "analysis, that the analysis had many flaws favouring that model, and that the "
        "problems were typical of Canadian projects of this kind.",
        "Le vérificateur général du Canada a conclu que la décision public-privé a précédé "
        "l'analyse, que l'analyse comportait de nombreuses faiblesses favorisant ce modèle et "
        "que les problèmes étaient typiques des projets canadiens de ce genre."),
      T("Governments that use the model point to on-time, on-budget delivery. Professor "
        "Siemiatycki's review of British Columbia's programme lists Abbotsford Hospital going "
        "from 211 to 355 million dollars, the Canada Line from 1.55 to 2 billion, and Golden "
        "Ears Bridge from 600 to 808 million.",
        "Les gouvernements qui l'utilisent invoquent des livraisons dans les délais et les "
        "budgets. L'examen du programme de la Colombie-Britannique par le professeur "
        "Siemiatycki relève que l'hôpital d'Abbotsford est passé de 211 à 355 millions de "
        "dollars, la Canada Line de 1,55 à 2 milliards, et le pont Golden Ears de 600 à 808 "
        "millions.")]],
    label=T("Four live disagreements, with each side attributed — scroll sideways to see all "
            "of it",
            "Quatre désaccords bien vivants, chaque camp étant attribué — faites défiler "
            "latéralement pour tout voir"))

# ------------------------------------------------------------------ 12
a.h2(T("What nobody has measured", "Ce que personne n'a mesuré"))
a.ul([
    T("Any official real-terms comparison of 19th-century and modern Canadian project costs. "
      "It does not exist.",
      "Toute comparaison officielle en termes réels entre les coûts de projets canadiens du "
      "19e siècle et d'aujourd'hui. Elle n'existe pas."),
    T("Any Statistics Canada or Infrastructure Canada measure of the average time to build a "
      "major project in Canada. There is no such number.",
      "Toute mesure de Statistique Canada ou d'Infrastructure Canada du temps moyen pour "
      "bâtir un grand projet au Canada. Ce chiffre n'existe pas."),
    T("How the Trans Mountain cost escalation divides between causes. The Parliamentary "
      "Budget Officer does not attribute it.",
      "La répartition de l'escalade des coûts de Trans Mountain entre ses causes. Le "
      "directeur parlementaire du budget ne l'attribue pas."),
    T("How often approvals outside the energy sector are challenged in court. The energy "
      "regulator keeps a register; there is no equivalent for transit, ports, highways or "
      "mines.",
      "La fréquence des contestations judiciaires d'autorisations en dehors du secteur de "
      "l'énergie. L'organisme de réglementation de l'énergie tient un registre ; il n'y a pas "
      "d'équivalent pour le transport collectif, les ports, les routes ou les mines."),
    T("What share of impact assessments meet the legislated time limits. The Agency's "
      "2024-25 results report does not publish that metric.",
      "La proportion d'évaluations d'impact qui respectent les délais prévus par la loi. Le "
      "rapport de résultats de 2024-2025 de l'Agence ne publie pas cette mesure."),
    T("Absolute municipal approval times by city, in months or days. The housing agency "
      "publishes an index, not durations.",
      "Les délais d'approbation municipaux absolus par ville, en mois ou en jours. "
      "L'organisme du logement publie un indice, pas des durées."),
    T("A national construction-sector fatality count assembled by a federal source. The "
      "federal report covers federally regulated industries only, and construction is mostly "
      "provincially regulated.",
      "Un décompte national des décès dans le secteur de la construction établi par une "
      "source fédérale. Le rapport fédéral ne couvre que les secteurs de compétence fédérale, "
      "et la construction relève surtout des provinces."),
])

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("canada-major-projects-office-explained.html",
         T("Canada's big projects — what is built, and what is on paper",
           "Les grands projets du Canada — ce qui est bâti et ce qui est sur papier")),
    link("churchill-falls-gull-island-explained.html",
         T("Churchill Falls and Gull Island — what was actually agreed",
           "Churchill Falls et Gull Island — ce qui a réellement été conclu")),
    link("how-canada-rebuilds-its-economy.html",
         T("How Canada rebuilds — new customers, old barriers",
           "Comment le Canada se rebâtit — nouveaux clients, vieilles barrières")),
])

a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://www150.statcan.gc.ca/n1/pub/11-516-x/sectiont/4147444-eng.htm",
             T("Statistics Canada — Historical Statistics of Canada, railway tables from 1946",
               "Statistique Canada — Statistiques historiques du Canada, tableaux "
               "ferroviaires depuis 1946")),
    out_link("https://www150.statcan.gc.ca/n1/daily-quotidien/200302/dq200302d-info-eng.htm",
             T("Statistics Canada — Infrastructure Construction Price Index, reference year "
               "2019",
               "Statistique Canada — Indice des prix de la construction d'infrastructures, "
               "année de référence 2019")),
    out_link("https://www150.statcan.gc.ca/n1/daily-quotidien/260428/dq260428b-eng.htm",
             T("Statistics Canada — building construction price indexes, first quarter 2026",
               "Statistique Canada — indices des prix de la construction de bâtiments, "
               "premier trimestre de 2026")),
    out_link("https://www150.statcan.gc.ca/n1/pub/36-28-0001/2026002/article/00003-eng.htm",
             T("Statistics Canada and CMHC — labour productivity in residential "
               "construction, 2001 to 2023",
               "Statistique Canada et la SCHL — productivité du travail dans la construction "
               "résidentielle, de 2001 à 2023")),
    out_link("https://journals.open.tudelft.nl/ejtir/article/view/5515",
             T("Saxe, Dean, Raghav, Durrant and Siemiatycki — timelines of transport "
               "infrastructure delivery in Toronto and London, 2021",
               "Saxe, Dean, Raghav, Durrant et Siemiatycki — échéanciers de réalisation des "
               "infrastructures de transport à Toronto et à Londres, 2021")),
    out_link("https://schoolofcities.utoronto.ca/wp-content/uploads/2025/04/Understanding-the-Drivers-of-Transit-Construction-Costs-in-Canada_Feb-2025_FINAL.pdf",
             T("University of Toronto School of Cities with Metrolinx — drivers of transit "
               "construction costs in Canada, January 2025",
               "School of Cities de l'Université de Toronto avec Metrolinx — facteurs des "
               "coûts de construction du transport collectif au Canada, janvier 2025")),
    out_link("https://www.queensu.ca/iigr/sites/iirwww/files/uploaded_files/SiemiatyckiSOTF2015.pdf",
             T("Siemiatycki — infrastructure cost overruns and performance shortfalls",
               "Siemiatycki — dépassements de coûts et manques à gagner de performance des "
               "infrastructures")),
    out_link("https://www.canada.ca/en/impact-assessment-agency/corporate/our-impact/impact-assessments-that-work/truths-misconceptions-federal-impact-assessments-canada.html",
             T("Impact Assessment Agency of Canada — truths and misconceptions about federal "
               "impact assessments",
               "Agence d'évaluation d'impact du Canada — vérités et idées fausses sur les "
               "évaluations d'impact fédérales")),
    out_link("https://www.canada.ca/en/impact-assessment-agency/corporate/transparency/accountability-performance-financial-reporting/2024-2025-departmental-results-report/departmental-results-report.html",
             T("Impact Assessment Agency of Canada — 2024-25 departmental results report",
               "Agence d'évaluation d'impact du Canada — rapport sur les résultats "
               "ministériels de 2024-2025")),
    out_link("https://www.canada.ca/en/impact-assessment-agency/corporate/mandate/milestones-history-assessments.html",
             T("Impact Assessment Agency of Canada — milestones in the history of assessments",
               "Agence d'évaluation d'impact du Canada — jalons de l'histoire des "
               "évaluations")),
    out_link("https://www.canada.ca/en/impact-assessment-agency/news/2023/04/government-of-canada-approves-key-roberts-bank-terminal-2-project-in-british-columbia-subject-to-strict-conditions-to-protect-the-local-environment.html",
             T("Government of Canada — Roberts Bank Terminal 2 approval and its 370 "
               "conditions, April 2023",
               "Gouvernement du Canada — approbation du terminal 2 de Roberts Bank et ses 370 "
               "conditions, avril 2023")),
    out_link("https://lop.parl.ca/sites/PublicWebsite/default/en_CA/ResearchPublications/201917E",
             T("Library of Parliament — the duty to consult Indigenous peoples",
               "Bibliothèque du Parlement — l'obligation de consulter les peuples "
               "autochtones")),
    out_link("https://lop.parl.ca/sites/PublicWebsite/default/en_CA/ResearchPublications/202502E",
             T("Library of Parliament — the Constitution and the Impact Assessment Act",
               "Bibliothèque du Parlement — la Constitution et la Loi sur l'évaluation "
               "d'impact")),
    out_link("https://decisions.scc-csc.ca/scc-csc/scc-csc/en/item/20102/index.do",
             T("Supreme Court of Canada — Reference re Impact Assessment Act, 2023",
               "Cour suprême du Canada — Renvoi relatif à la Loi sur l'évaluation d'impact, "
               "2023")),
    out_link("https://www.canada.ca/en/impact-assessment-agency/news/media-room/amended-impact-assessment-act-now-in-force.html",
             T("Impact Assessment Agency of Canada — the amended Act in force, June 2024",
               "Agence d'évaluation d'impact du Canada — la loi modifiée en vigueur, juin "
               "2024")),
    out_link("https://www.alberta.ca/albertas-response-to-the-federal-impact-assessment-act",
             T("Government of Alberta — Alberta's response to the federal Impact Assessment "
               "Act",
               "Gouvernement de l'Alberta — la réponse de l'Alberta à la Loi fédérale sur "
               "l'évaluation d'impact")),
    out_link("https://www.ourcommons.ca/documentviewer/en/42-1/PACP/report-51/page-36",
             T("House of Commons Public Accounts Committee — the Auditor General's findings "
               "on the Champlain Bridge",
               "Comité des comptes publics de la Chambre des communes — les constats du "
               "vérificateur général sur le pont Champlain")),
    out_link("https://www.gov.nl.ca/em/files/Volume-1-Executive-Summary-Key-Findings-and-Recommendations.pdf",
             T("Commission of Inquiry — Muskrat Falls: A Misguided Project, March 2020",
               "Commission d'enquête — Muskrat Falls : un projet mal avisé, mars 2020")),
    out_link("https://www.auditor.on.ca/en/content/annualreports/arreports/en18/v1_307en18.pdf",
             T("Auditor General of Ontario — Metrolinx light rail construction, 2018",
               "Vérificatrice générale de l'Ontario — construction du train léger de "
               "Metrolinx, 2018")),
    out_link("https://www.canada.ca/en/auditor-general/our-work/audit-reports/parl-oag-202102-02-e.html",
             T("Auditor General of Canada — National Shipbuilding Strategy, February 2021",
               "Vérificateur général du Canada — Stratégie nationale de construction navale, "
               "février 2021")),
    out_link("https://www.ourcommons.ca/Content/Committee/441/TRAN/Reports/RP11664128/tranrp03/tranrp03-e.pdf",
             T("House of Commons transport committee — the Canada Infrastructure Bank, May "
               "2022",
               "Comité des transports de la Chambre des communes — la Banque de "
               "l'infrastructure du Canada, mai 2022")),
    out_link("https://www.pbo-dpb.ca/en/publications/RP-2425-021-S--trans-mountain-pipeline-2024-report--reseau-pipelines-trans-mountain-rapport-2024",
             T("Parliamentary Budget Officer — Trans Mountain pipeline, 2024 report",
               "Directeur parlementaire du budget — réseau de pipelines Trans Mountain, "
               "rapport de 2024")),
    out_link("https://www.cer-rec.gc.ca/en/about/news-room/news-releases/2024/cer-issues-final-authorization-for-trans-mountain-expansion-project-to-operate.html",
             T("Canada Energy Regulator — final authorisation for Trans Mountain to operate, "
               "April 2024",
               "Régie de l'énergie du Canada — autorisation finale d'exploitation de Trans "
               "Mountain, avril 2024")),
    out_link("https://decisions.fca-caf.gc.ca/fca-caf/decisions/en/343511/1/document.do",
             T("Federal Court of Appeal — Tsleil-Waututh Nation v. Canada, 2018",
               "Cour d'appel fédérale — Tsleil-Waututh Nation c. Canada, 2018")),
    out_link("https://www.cer-rec.gc.ca/en/about/who-we-are-what-we-do/governance/committee-natural-resources-RNNR-briefing-binder-2026/index.html",
             T("Canada Energy Regulator — briefing binder for the natural resources "
               "committee, June 2026",
               "Régie de l'énergie du Canada — cahier d'information pour le comité des "
               "ressources naturelles, juin 2026")),
    out_link("https://gazette.gc.ca/rp-pr/p1/2026/2026-08-01/html/sup1-eng.html",
             T("Canada Gazette — notice on listing the West Coast Oil Pipeline, 1 August 2026",
               "Gazette du Canada — avis sur l'inscription de l'oléoduc de la côte Ouest, 1er "
               "août 2026")),
    out_link("https://laws-lois.justice.gc.ca/eng/acts/B-9.89/page-3.html",
             T("Building Canada Act — Schedule 1, checked 27 August 2026",
               "Loi sur la construction du Canada — annexe 1, vérifiée le 27 août 2026")),
    out_link("https://www.bankofcanada.ca/2024/03/time-to-break-the-glass-fixing-canadas-productivity-problem/",
             T("Bank of Canada — Carolyn Rogers on Canada's productivity problem, March 2024",
               "Banque du Canada — Carolyn Rogers sur le problème de productivité du Canada, "
               "mars 2024")),
    out_link("https://www.cmhc-schl.gc.ca/observer/2023/approval-delays-linked-lower-housing-affordability",
             T("Canada Mortgage and Housing Corporation — approval delays and housing "
               "affordability, July 2023",
               "Société canadienne d'hypothèques et de logement — délais d'approbation et "
               "abordabilité du logement, juillet 2023")),
    out_link("https://www.canada.ca/en/housing-infrastructure-communities/news/2021/04/the-history-of-the-quebec-bridge.html",
             T("Housing, Infrastructure and Communities Canada — the history of the Québec "
               "Bridge",
               "Logement, Infrastructures et Collectivités Canada — l'histoire du pont de "
               "Québec")),
    out_link("https://parks.canada.ca/pn-np/bc/glacier/culture/histoire-history/neige-snow",
             T("Parks Canada — the snow war, avalanches at Rogers Pass",
               "Parcs Canada — la guerre de la neige, les avalanches du col Rogers")),
    out_link("https://parks.canada.ca/culture/designation/evenement-event/travailleurs-chinois-chinese-workers",
             T("Parks Canada — Chinese construction workers on the Canadian Pacific Railway",
               "Parcs Canada — les travailleurs chinois du chemin de fer Canadien "
               "Pacifique")),
    out_link("https://www.canada.ca/en/news/archive/2006/06/address-prime-minister-chinese-head-tax-redress.html",
             T("Prime Minister of Canada — address on the Chinese head tax redress, 22 June "
               "2006",
               "Premier ministre du Canada — allocution sur le dédommagement pour la taxe "
               "d'entrée chinoise, 22 juin 2006")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1360948213124/1544620003549",
             T("Crown-Indigenous Relations and Northern Affairs Canada — the Numbered "
               "Treaties, 1871 to 1921",
               "Relations Couronne-Autochtones et Affaires du Nord Canada — les traités "
               "numérotés, de 1871 à 1921")),
    out_link("https://www.ontario.ca/document/final-report-mining-health-safety-and-prevention-review/internal-responsibility-system",
             T("Government of Ontario — the Ham Commission and the internal responsibility "
               "system",
               "Gouvernement de l'Ontario — la commission Ham et le système de responsabilité "
               "interne")),
    out_link("https://laws-lois.justice.gc.ca/eng/acts/E-21/FullText.html",
             T("Expropriation Act — the federal expropriation process",
               "Loi sur l'expropriation — le processus fédéral d'expropriation")),
    out_link("https://www.collectionscanada.gc.ca/canadian-west/052920/05292073_e.html",
             T("Library and Archives Canada — the 1881 railway land grant",
               "Bibliothèque et Archives Canada — la concession de terres ferroviaires de "
               "1881")),
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
