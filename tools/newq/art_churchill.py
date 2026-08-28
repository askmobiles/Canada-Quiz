#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article 6 — the Churchill Falls and Gull Island agreement of 17 August 2026.

Source: the research notes
notes, which lists sixteen things that could not be established and the sources
that blocked automated retrieval.

Four figures were deliberately kept off this page or attributed rather than
asserted: the 14,000 MW headline, which does not sum from the named components;
the "largest clean energy investment in North American history" claim, which no
independent source verifies; the 23,000 jobs and $31 billion GDP figures, which
come from one government release with no published methodology; and a Muskrat
Falls overrun of 105 percent, which requires a baseline that could not be
confirmed. The Commission of Inquiry's own baseline gives 82 percent, and that
is what the page uses.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="churchill-falls-gull-island-explained.html",
    section="Energy",
    title=T("Churchill Falls and Gull Island — What Was Actually Agreed",
            "Churchill Falls et Gull Island — ce qui a réellement été conclu"),
    desc=T("A plain explanation of the 17 August 2026 Churchill Falls and Gull Island "
           "agreement: what it covers, what it costs, when anything gets built, whether "
           "it is binding yet, who objects, and what Canada's recent megaprojects "
           "suggest about the budget.",
           "Une explication simple de l'entente du 17 août 2026 sur Churchill Falls et "
           "Gull Island : ce qu'elle couvre, ce qu'elle coûte, quand quelque chose sera "
           "construit, si elle est déjà contraignante, qui s'y oppose, et ce que les "
           "récents mégaprojets canadiens laissent présager du budget."),
    h1=T("⚡ Churchill Falls and Gull Island, explained",
         "⚡ Churchill Falls et Gull Island, expliqués"),
    hero=T("Newfoundland and Labrador and Quebec have agreed to terminate and replace the "
           "1969 Churchill Falls contract and build a great deal more. Nothing is under "
           "construction, the binding contracts are not signed, and the first new dam is a "
           "decade away. Here is what is settled and what is not.",
           "Terre-Neuve-et-Labrador et le Québec ont convenu de résilier et de remplacer le "
           "contrat de Churchill Falls de 1969 et de construire beaucoup plus. Rien n'est "
           "en chantier, les contrats contraignants ne sont pas signés, et le premier "
           "nouveau barrage est à une décennie de distance. Voici ce qui est réglé et ce "
           "qui ne l'est pas."),
    checked=T("Last checked 24 August 2026 — this page covers a fast-moving situation",
              "Dernière vérification le 24 août 2026 — cette page traite d'une situation "
              "qui évolue vite"),
)

# ------------------------------------------------------------------ 1
a.h2(T("The short answer", "La réponse courte"))
a.p(T(
    "On 17 August 2026 in St. John's, the federal government, Quebec, Newfoundland and "
    "Labrador and the two provincial utilities announced an agreement to terminate and "
    "replace the 1969 Churchill Falls contract fifteen years before its 2041 expiry, "
    "upgrade the existing station, build a new dam at Gull Island, study a large wind "
    "project in Labrador, and run more than 660 kilometres of new transmission line. The "
    "federal government put up to 10 billion dollars behind it. Ottawa puts the "
    "construction value of the whole package at nearly 70 billion dollars.",
    "Le 17 août 2026, à St. John's, le gouvernement fédéral, le Québec, "
    "Terre-Neuve-et-Labrador et les deux sociétés d'État provinciales ont annoncé une "
    "entente pour résilier et remplacer le contrat de Churchill Falls de 1969 quinze ans "
    "avant son échéance de 2041, moderniser la centrale existante, construire un nouveau "
    "barrage à Gull Island, étudier un grand projet éolien au Labrador et déployer plus de "
    "660 kilomètres de nouvelles lignes de transport. Le gouvernement fédéral y engage "
    "jusqu'à 10 milliards de dollars. Ottawa chiffre la valeur de construction de "
    "l'ensemble à près de 70 milliards de dollars."))
a.p(T(
    "Three things are worth knowing before any of the numbers. The binding contracts do "
    "not exist yet and are targeted for 31 December 2026. The 1969 contract stays in force "
    "until they are signed. And the second-largest component of the original December 2024 "
    "plan — a 1,100 megawatt new powerhouse at Churchill Falls — has been taken out of this "
    "agreement and sent back to feasibility study. That last point is itself contested: the "
    "federal natural resources release still lists a Churchill Falls expansion of up to "
    "2,500 megawatts as part of the package, while VOCM reported the same day that it had "
    "been removed and that no commercial arrangements are in place for it.",
    "Trois choses méritent d'être sues avant tout chiffre. Les contrats contraignants "
    "n'existent pas encore et sont visés pour le 31 décembre 2026. Le contrat de 1969 "
    "demeure en vigueur jusqu'à leur signature. Et la deuxième composante en importance du "
    "plan initial de décembre 2024 — une nouvelle centrale de 1 100 mégawatts à Churchill "
    "Falls — a été retirée de cette entente et renvoyée à une étude de faisabilité. Ce "
    "dernier point est lui-même contesté : le communiqué fédéral des ressources naturelles "
    "mentionne toujours un agrandissement de Churchill Falls pouvant atteindre 2 500 "
    "mégawatts dans l'ensemble, tandis que VOCM rapportait le même jour qu'il avait été "
    "retiré et qu'aucune entente commerciale n'est en place à son sujet."))

# ------------------------------------------------------------------ 2
a.h2(T("Is it a deal yet? The sources disagree",
       "Est-ce déjà une entente ? Les sources ne s'accordent pas"))
a.p(T(
    "The document is called the Definitive Cooperation and Implementation Agreement, and "
    "it is between Newfoundland and Labrador Hydro and Hydro-Québec. The two utilities and "
    "the two governments describe its legal status differently, and the difference matters "
    "enough to print rather than resolve.",
    "Le document s'appelle l'Entente définitive de coopération et de mise en œuvre, et il "
    "lie Newfoundland and Labrador Hydro et Hydro-Québec. Les deux sociétés d'État et les "
    "deux gouvernements en décrivent le statut juridique différemment, et l'écart mérite "
    "d'être imprimé plutôt que tranché."))
a.table(
    [T("Source", "Source"), T("How it describes the agreement", "Comment elle décrit l'entente")],
    [[T("Hydro-Québec", "Hydro-Québec"),
      T("A binding agreement signed 17 August 2026",
        "Une entente contraignante signée le 17 août 2026")],
     [T("Government of Newfoundland and Labrador", "Gouvernement de Terre-Neuve-et-Labrador"),
      T("The parties will now work to implement final binding agreements — which is to say "
        "binding agreements do not yet exist",
        "Les parties travailleront maintenant à mettre en œuvre des ententes contraignantes "
        "définitives — autrement dit, il n'existe pas encore d'entente contraignante")],
     [T("Waterpower Canada, in a legal and technical summary",
        "Waterpower Canada, dans un résumé juridique et technique"),
      T("A framework agreement whose provisions are mostly expressly non-binding, with "
        "long-form definitive agreements targeted for 31 December 2026",
        "Une entente-cadre dont les dispositions sont pour la plupart expressément non "
        "contraignantes, les ententes définitives détaillées étant visées pour le 31 "
        "décembre 2026")],
     [T("VOCM and APTN News", "VOCM et APTN News"),
      T("Not yet binding", "Pas encore contraignante")]],
    label=T("How each source describes the agreement — scroll sideways to see all of it",
            "Comment chaque source décrit l'entente — faites défiler latéralement pour "
            "tout voir"))
a.p(T(
    "The agreement itself terminates no later than 31 March 2027 unless it is extended. So "
    "the fair description is a signed framework, some parts binding and most not, with a "
    "deadline. The full text has not been published, and no journalist has read it in full.",
    "L'entente elle-même prend fin au plus tard le 31 mars 2027, sauf prolongation. La "
    "description juste est donc celle d'un cadre signé, dont certaines parties sont "
    "contraignantes et la plupart ne le sont pas, assorti d'une échéance. Le texte "
    "intégral n'a pas été publié, et aucun journaliste ne l'a lu en entier."))

# ------------------------------------------------------------------ 3
a.h2(T("What would get built, and where", "Ce qui serait construit, et où"))
a.p(T(
    "Everything is on the Churchill River in Labrador, except the transmission that "
    "carries the power out and the wind project, whose location has not been announced.",
    "Tout se trouve sur le fleuve Churchill au Labrador, sauf les lignes de transport qui "
    "évacuent l'électricité et le projet éolien, dont l'emplacement n'a pas été annoncé."))
a.fig(bar_chart(
    T("Generating capacity, in megawatts",
      "Puissance de production, en mégawatts"),
    [(T("Churchill Falls today", "Churchill Falls aujourd'hui"), 5428),
     (T("Gull Island, proposed", "Gull Island, proposé"), 2700),
     (T("Labrador wind, feasibility study only",
        "Éolien du Labrador, étude de faisabilité seulement"), 2000),
     (T("Churchill Falls turbine upgrades", "Modernisation des turbines de Churchill Falls"), 1275),
     (T("Muskrat Falls, built 2020 — not part of this agreement",
        "Muskrat Falls, construit en 2020 — hors de cette entente"), 824)],
    colours=["blue", "green", "teal", "purple", "orange"]))
a.p(T(
    "Churchill Falls has eleven turbines and a rated capacity of 5,428 megawatts, "
    "producing over 34 terawatt-hours a year. The upgrade "
    "would replace turbines one unit per year for more output from the same water. Gull "
    "Island would be a new dam of 2,700 megawatts producing about 12 terawatt-hours, owned "
    "60 percent by Newfoundland and Labrador Hydro and 40 percent by Hydro-Québec. The "
    "transmission includes a new 735-kilovolt line to Labrador City, where the existing "
    "line is running at maximum capacity.",
    "Churchill Falls compte onze turbines et une puissance nominale de 5 428 mégawatts, "
    "produisant plus de 34 térawattheures par an. "
    "La modernisation remplacerait les turbines au rythme d'une par année, pour tirer plus "
    "d'électricité de la même eau. Gull Island serait un nouveau barrage de 2 700 "
    "mégawatts produisant environ 12 térawattheures, détenu à 60 pour cent par Newfoundland "
    "and Labrador Hydro et à 40 pour cent par Hydro-Québec. Le transport comprend une "
    "nouvelle ligne de 735 kilovolts vers Labrador City, où la ligne existante fonctionne "
    "à pleine capacité."))
a.callout(T(
    "<strong>About the 14,000 megawatt headline.</strong> The federal release says the "
    "projects will generate 14,000 megawatts, nearly tripling Churchill Falls. That figure "
    "includes the existing station. Add the three new components to what Churchill Falls "
    "already produces and the total is about 11,400 megawatts. Reaching 14,000 would "
    "require counting the Churchill Falls expansion that has been removed from this "
    "agreement, or Muskrat Falls, or both. No published source reconciles it, so it is "
    "printed here as a government figure rather than as an established one.",
    "<strong>À propos du chiffre de 14 000 mégawatts.</strong> Le communiqué fédéral "
    "indique que les projets produiront 14 000 mégawatts, presque le triple de Churchill "
    "Falls. Ce chiffre inclut la centrale existante. En additionnant les trois nouvelles "
    "composantes à ce que Churchill Falls produit déjà, on obtient environ 11 400 "
    "mégawatts. Atteindre 14 000 exigerait de compter l'agrandissement de Churchill Falls "
    "retiré de cette entente, ou Muskrat Falls, ou les deux. Aucune source publiée ne le "
    "réconcilie ; il est donc présenté ici comme un chiffre gouvernemental et non comme un "
    "chiffre établi."))

# ------------------------------------------------------------------ 4
a.h2(T("When", "Quand"))
a.p(T(
    "The power contract would run 50 years, to 2077. Gull Island is given an in-service "
    "date of 2036 or 2037. No construction start date has been published for any "
    "component, and no schedule at all has been published for the wind project.",
    "Le contrat d'électricité durerait 50 ans, jusqu'en 2077. Gull Island est annoncé pour "
    "une mise en service en 2036 ou 2037. Aucune date de début de construction n'a été "
    "publiée pour quelque composante que ce soit, et aucun calendrier n'a été publié pour "
    "le projet éolien."))
a.p(T(
    "The environmental assessment question is unusual and worth understanding. Gull Island "
    "went through a full federal and provincial environmental assessment that finished in "
    "2011, and was released in 2012. The joint review panel recommended putting an expiry "
    "date on that release, so that a long delay would trigger a fresh review. Both "
    "governments declined. As a result, a legal analysis by East Coast Environmental Law "
    "concludes that provincial law arguably does not require a new assessment, and that "
    "the federal Impact Assessment Act does not require fresh assessment of a project "
    "already assessed but never begun. So the accurate answer to whether the environmental "
    "process has started is that it finished fifteen years ago, on a different configuration of "
    "the project, and may not have to happen again.",
    "La question de l'évaluation environnementale est inhabituelle et mérite qu'on la "
    "comprenne. Gull Island a fait l'objet d'une évaluation environnementale fédérale et "
    "provinciale complète, terminée en 2011 et libérée en 2012. La commission d'examen "
    "conjoint avait recommandé d'assortir cette libération d'une date d'expiration, afin "
    "qu'un long délai déclenche un nouvel examen. Les deux gouvernements ont refusé. En "
    "conséquence, une analyse juridique d'East Coast Environmental Law conclut que la loi "
    "provinciale n'exige sans doute pas de nouvelle évaluation, et que la Loi fédérale sur "
    "l'évaluation d'impact n'en exige pas pour un projet déjà évalué mais jamais amorcé. "
    "La réponse exacte à la question de savoir si le processus environnemental a commencé "
    "est donc qu'il s'est terminé il y a quinze ans, sur une configuration différente du "
    "projet, et qu'il pourrait ne pas avoir à recommencer."))
a.p(T(
    "What has started instead is federal coordination: the Labrador corridor has been "
    "referred to the federal Major Projects Office for coordinated financing and "
    "accelerated permitting. Separately, the Newfoundland and Labrador House of Assembly "
    "reconvenes on 14 September 2026 to debate the agreement. That debate replaces a "
    "referendum the provincial government had previously promised and has now cancelled; "
    "the premier gave the partnership with Ottawa and the American tariffs as his reasons. "
    "Whether the House will hold a binding vote had not been settled when this page was "
    "written.",
    "Ce qui a commencé, c'est plutôt la coordination fédérale : le corridor du Labrador a "
    "été confié au Bureau fédéral des grands projets pour un financement coordonné et une "
    "délivrance accélérée des permis. Par ailleurs, la Chambre d'assemblée de "
    "Terre-Neuve-et-Labrador se réunit de nouveau le 14 septembre 2026 pour débattre de "
    "l'entente. Ce débat remplace un référendum que le gouvernement provincial avait promis "
    "et qu'il a maintenant annulé ; le premier ministre a invoqué le partenariat avec Ottawa "
    "et les tarifs américains. La tenue d'un vote contraignant à la Chambre n'était pas "
    "réglée au moment d'écrire cette page."))

# ------------------------------------------------------------------ 5
a.h2(T("What it costs — and why two very different numbers are both right",
       "Ce que cela coûte — et pourquoi deux chiffres très différents sont tous deux "
       "justes"))
a.p(T(
    "The federal government says 10 billion dollars. Newfoundland and Labrador says 3.5 "
    "billion. Those look like a contradiction and are not.",
    "Le gouvernement fédéral parle de 10 milliards de dollars. Terre-Neuve-et-Labrador "
    "parle de 3,5 milliards. Cela ressemble à une contradiction et n'en est pas une."))
a.p(T(
    "The 10 billion is the face value of the federal instruments — loan guarantees, an "
    "equity stake of up to 40 percent in the wind project, and financing — deployed over "
    "roughly fifteen years. A loan guarantee's face value is the amount guaranteed, and it "
    "costs the government nothing at all unless it is called.",
    "Les 10 milliards représentent la valeur nominale des instruments fédéraux — garanties "
    "de prêt, participation pouvant aller jusqu'à 40 pour cent dans le projet éolien, et "
    "financement — déployés sur une quinzaine d'années. La valeur nominale d'une garantie "
    "de prêt est le montant garanti, et elle ne coûte rien du tout à l'État tant qu'elle "
    "n'est pas appelée."))
a.p(T(
    "The 3.5 billion is a present value: what those instruments are worth, in 2026 dollars, "
    "to Newfoundland and Labrador specifically. The province itemises it as 1 billion for "
    "the federal equity stake in the wind project, 1 billion toward the Labrador West "
    "transmission line and 1.5 billion of value in support for Gull Island, Churchill Falls "
    "and transmission. A ten-billion-dollar envelope of guarantees and equity producing "
    "three and a half billion dollars of present-day benefit to one province is ordinary "
    "arithmetic. Neither figure is a cash grant. One caution: Waterpower Canada's summary "
    "of the deal attributes the same 3.5 billion present value to Hydro-Québec development "
    "payments rather than to federal support. The provincial government's own release "
    "attributes it to Ottawa, and that disagreement has not been resolved publicly.",
    "Les 3,5 milliards sont une valeur actualisée : ce que valent ces instruments, en "
    "dollars de 2026, pour Terre-Neuve-et-Labrador en particulier. La province les détaille "
    "ainsi : 1 milliard pour la participation fédérale dans le projet éolien, 1 milliard "
    "pour la ligne de transport de l'ouest du Labrador et 1,5 milliard de valeur en soutien "
    "à Gull Island, Churchill Falls et au transport. Une enveloppe de dix milliards en "
    "garanties et en capital produisant trois milliards et demi de bénéfice actuel pour une "
    "province, c'est de l'arithmétique ordinaire. Ni l'un ni l'autre de ces chiffres n'est "
    "une subvention en argent. Une mise en garde : le résumé de l'entente par Waterpower "
    "Canada attribue la même valeur actualisée de 3,5 milliards à des paiements de "
    "développement d'Hydro-Québec plutôt qu'à un soutien fédéral. Le communiqué du "
    "gouvernement provincial l'attribue à Ottawa, et ce désaccord n'a pas été résolu "
    "publiquement."))
a.p(T(
    "The near-70-billion-dollar figure is different again. It is an estimate of what the "
    "whole package would cost to build, for projects that have not been designed, costed "
    "in detail or sanctioned. No breakdown by component has been published. It is a "
    "planning estimate, not a budget — which brings us to the next question.",
    "Le chiffre de près de 70 milliards de dollars est encore autre chose. C'est une "
    "estimation de ce que l'ensemble coûterait à construire, pour des projets qui n'ont pas "
    "été conçus, chiffrés en détail ni approuvés. Aucune ventilation par composante n'a été "
    "publiée. C'est une estimation de planification, pas un budget — ce qui nous amène à la "
    "question suivante."))

# ------------------------------------------------------------------ 6
a.h2(T("Does a project like this come in on budget?",
       "Un projet de ce genre respecte-t-il son budget ?"))
a.p(T(
    "Canada has three recent large energy projects that can be checked against their own "
    "approved budgets. Two saw their costs grow by about 82 percent. The third came in "
    "under budget.",
    "Le Canada compte trois grands projets énergétiques récents qu'on peut comparer à leur "
    "propre budget approuvé. Deux ont vu leurs coûts croître d'environ 82 pour cent. Le "
    "troisième est resté sous le budget."))
a.fig(bar_chart(
    T("Cost growth against approved budget, percent",
      "Croissance des coûts par rapport au budget approuvé, en pourcentage"),
    [(T("Muskrat Falls, Newfoundland and Labrador", "Muskrat Falls, Terre-Neuve-et-Labrador"), 82.4),
     (T("Site C, British Columbia", "Site C, Colombie-Britannique"), 82.3),
     (T("Darlington refurbishment, Ontario", "Réfection de Darlington, Ontario"), -1.2)],
    unit="%", colours=["red", "red", "green"]),
    caption=T("Site C's figure is the growth in its approved budget. No final audited total "
              "has been published for it.",
              "Le chiffre de Site C correspond à la croissance de son budget approuvé. "
              "Aucun total final vérifié n'a été publié pour ce projet."))
a.table(
    [T("Project", "Projet"), T("Approved budget", "Budget approuvé"),
     T("Final or current", "Final ou actuel"), T("Capacity", "Puissance")],
    [[T("Muskrat Falls, sanctioned late 2012", "Muskrat Falls, approuvé fin 2012"),
      "$7.4B", "$13.5B", "824 MW"],
     [T("Site C, approved December 2014", "Site C, approuvé en décembre 2014"),
      T("$8.775B including reserve", "8,775 G$ réserve comprise"),
      T("$16B approved; $14.9B spent to date", "16 G$ approuvés ; 14,9 G$ dépensés à ce jour"),
      "1,100 MW"],
     [T("Darlington refurbishment, completed February 2026",
        "Réfection de Darlington, achevée en février 2026"),
      "$12.8B", T("$12.65B — $150M under budget, four months early",
                  "12,65 G$ — 150 M$ sous le budget, quatre mois d'avance"),
      T("3,512 MW across four units", "3 512 MW répartis sur quatre tranches")]],
    label=T("Recent Canadian energy megaprojects against budget — scroll sideways to see "
            "all of it",
            "Mégaprojets énergétiques canadiens récents par rapport au budget — faites "
            "défiler latéralement pour tout voir"))
a.p(T(
    "The pattern in those three is not random. Muskrat Falls and Site C were greenfield "
    "dams — new structures on new ground, where the geology is only fully known once you "
    "dig. British Columbia Hydro's own review of Site C attributes 1.1 billion to "
    "foundation work on the right bank, 600 million to cracks on the left bank and 1.6 "
    "billion to pandemic delays. The utility acknowledged it should have been more "
    "proactive about low-probability, high-consequence risks, and that its contingency and "
    "project reserve were both insufficient when those risks materialised. Darlington was a "
    "refurbishment: an existing plant, a defined scope, four repetitions of the same job.",
    "Le schéma de ces trois projets n'est pas aléatoire. Muskrat Falls et Site C étaient "
    "des barrages en terrain vierge — de nouvelles structures sur un nouveau site, où la "
    "géologie n'est pleinement connue qu'une fois qu'on creuse. L'examen de Site C par BC "
    "Hydro elle-même attribue 1,1 milliard aux travaux de fondation de la rive droite, 600 "
    "millions à des fissures sur la rive gauche et 1,6 milliard aux retards de la pandémie. "
    "La société d'État a reconnu qu'elle aurait dû être plus proactive à l'égard des "
    "risques à faible probabilité et à forte conséquence, et que sa provision pour imprévus "
    "et sa réserve étaient toutes deux insuffisantes quand ces risques se sont matérialisés. "
    "Darlington était une réfection : une centrale existante, une portée définie, quatre "
    "répétitions du même travail."))
a.p(T(
    "Gull Island is a greenfield dam, on the same river and in the same province as Muskrat "
    "Falls, and the same provincial utility is building it. That is not a "
    "prediction. It is the closest comparison available, and it is the reason a "
    "70-billion-dollar planning estimate should be read as a starting point.",
    "Gull Island est un barrage en terrain vierge, sur le même fleuve et dans la même "
    "province que Muskrat Falls, et c'est la même société d'État provinciale qui le "
    "construit. Ce n'est pas une prédiction. C'est la comparaison la plus "
    "proche qui existe, et c'est pourquoi une estimation de planification de 70 milliards de "
    "dollars doit être lue comme un point de départ."))

# ------------------------------------------------------------------ 7
a.h2(T("Is it the largest clean energy investment in North American history?",
       "Est-ce le plus grand investissement en énergie propre de l'histoire de l'Amérique "
       "du Nord ?"))
a.p(T(
    "That is how the federal government describes it. No independent source has verified "
    "it, and no methodology has been published — there is no stated definition of what "
    "counts as one investment, and no inflation basis on which to compare an announcement "
    "made in 2026 with a project built in the 1970s.",
    "C'est ainsi que le gouvernement fédéral le décrit. Aucune source indépendante ne l'a "
    "vérifié, et aucune méthodologie n'a été publiée — il n'existe aucune définition "
    "énoncée de ce qui constitue un seul investissement, ni de base d'inflation permettant "
    "de comparer une annonce de 2026 à un projet construit dans les années 1970."))
a.p(T(
    "Inside Climate News, which questioned the claim, reported that the analysts it "
    "contacted could not immediately name a larger single North American project — which "
    "is weak support rather than confirmation — and pointed out that the American Inflation "
    "Reduction Act projected more than 350 billion American dollars of clean-energy "
    "spending, though much of it was later rolled back. Closer to home, Quebec's own James "
    "Bay complex has 15,244 megawatts installed across eleven stations, built from 1974. "
    "Nobody has published an inflation-adjusted comparison, so the question cannot be "
    "settled here either way.",
    "Inside Climate News, qui a mis la formule en doute, a rapporté que les analystes "
    "consultés n'ont pas pu nommer sur-le-champ un projet nord-américain unique plus grand "
    "— ce qui est un appui faible plutôt qu'une confirmation — et a souligné que l'Inflation "
    "Reduction Act américaine prévoyait plus de 350 milliards de dollars américains de "
    "dépenses en énergie propre, dont une bonne part a ensuite été annulée. Plus près de "
    "nous, le complexe québécois de la Baie-James compte 15 244 mégawatts installés dans "
    "onze centrales, construites à partir de 1974. Personne n'a publié de comparaison "
    "ajustée à l'inflation, alors la question ne peut être tranchée ici dans un sens ni "
    "dans l'autre."))

# ------------------------------------------------------------------ 8
a.h2(T("What Newfoundland and Labrador gets",
       "Ce que Terre-Neuve-et-Labrador obtient"))
a.p(T(
    "To see why this matters in the province, you have to know what the 1969 contract did. "
    "Churchill Falls sells Hydro-Québec roughly 31 billion kilowatt-hours a year at a price "
    "set in 1969, at about three tenths of a cent per kilowatt-hour, declining in stages "
    "over the life of the contract, with no adjustment for inflation. It ran for 40 years "
    "from the station's completion, and a renewal clause extended it automatically for a "
    "further 25 — to 2041 — at a lower price still. That clause is the famous part: the "
    "original letter of intent had provided for the renewal terms to be negotiated and "
    "agreed by both sides. "
    "The province's attempts to get out of it failed in the 1970s, again in 1980, and most "
    "recently at the Supreme Court of Canada in 2018. Today the arrangement is widely "
    "reported as returning less than 20 million dollars a year to the provincial treasury.",
    "Pour comprendre pourquoi cela compte dans la province, il faut savoir ce qu'a fait le "
    "contrat de 1969. Churchill Falls vend à Hydro-Québec environ 31 milliards de "
    "kilowattheures par an à un prix fixé en 1969, soit environ trois dixièmes de cent le "
    "kilowattheure, décroissant par paliers sur la durée du contrat, sans ajustement à "
    "l'inflation. Il courait sur 40 ans à partir de l'achèvement de la centrale, et une "
    "clause de renouvellement l'a prolongé automatiquement de 25 ans de plus — jusqu'en "
    "2041 — à un prix encore plus bas. C'est cette clause qui est célèbre : la lettre "
    "d'intention originale prévoyait "
    "que les conditions de renouvellement soient négociées et convenues par les deux "
    "parties.Les tentatives de la province pour s'en "
    "sortir ont échoué dans les années 1970, de nouveau en 1980, et plus récemment devant "
    "la Cour suprême du Canada en 2018. Aujourd'hui, on rapporte largement que l'entente "
    "rapporte moins de 20 millions de dollars par an au trésor provincial."))
a.p(T(
    "Against that, here is what the province says the new agreement gives it.",
    "En regard, voici ce que la province dit obtenir de la nouvelle entente."))
a.ul([
    T("<strong>Guaranteed transmission through Quebec — 985 megawatts</strong>, sold at "
      "export market prices at Newfoundland and Labrador Hydro's sole discretion, without "
      "needing approval from Hydro-Québec or the Churchill Falls corporation's board. This "
      "is the structural change. The 1969 contract never provided it, and without it the "
      "province's power had exactly one possible buyer.",
      "<strong>Un accès de transport garanti à travers le Québec — 985 mégawatts</strong>, "
      "vendus aux prix du marché d'exportation à la seule discrétion de Newfoundland and "
      "Labrador Hydro, sans avoir besoin de l'approbation d'Hydro-Québec ni du conseil de "
      "la société de Churchill Falls. C'est là le changement structurel. Le contrat de 1969 "
      "ne le prévoyait pas, et sans lui l'électricité de la province n'avait exactement "
      "qu'un acheteur possible."),
    T("<strong>Up to 2,750 megawatts kept for the province</strong> — 2,350 from Churchill "
      "Falls and Gull Island plus 400 from the wind project, against 1,990 under the "
      "December 2024 memorandum.",
      "<strong>Jusqu'à 2 750 mégawatts conservés pour la province</strong> — 2 350 de "
      "Churchill Falls et Gull Island plus 400 du projet éolien, contre 1 990 dans le "
      "protocole de décembre 2024."),
    T("<strong>60 percent of the Gull Island joint venture</strong>, and a 3.9 billion "
      "dollar Gull Island option payment retained.",
      "<strong>60 pour cent de la coentreprise de Gull Island</strong>, et le maintien "
      "d'un paiement d'option de 3,9 milliards de dollars sur Gull Island."),
    T("<strong>A rebate for households</strong> — 15 percent on the first 2,000 "
      "kilowatt-hours a month, which CBC reported at about 351 dollars a year for an "
      "average home.",
      "<strong>Un rabais pour les ménages</strong> — 15 pour cent sur les 2 000 premiers "
      "kilowattheures par mois, ce que CBC chiffre à environ 351 dollars par an pour un "
      "foyer moyen."),
    T("<strong>49 billion dollars in 2026 present value, or 273 billion nominal</strong>, "
      "over the life of the agreements — up from 36 billion in 2024 present value and 225 "
      "billion nominal in the December 2024 memorandum.",
      "<strong>49 milliards de dollars en valeur actualisée de 2026, ou 273 milliards en "
      "valeur nominale</strong>, sur la durée des ententes — en hausse par rapport à 36 "
      "milliards en valeur actualisée de 2024 et 225 milliards en valeur nominale dans le "
      "protocole de décembre 2024."),
])
a.h3(T("The price — four numbers are in circulation",
       "Le prix — quatre chiffres circulent"))
a.p(T(
    "This is where reporting has been genuinely confusing, and it is worth setting the "
    "figures side by side rather than picking one.",
    "C'est ici que la couverture a été réellement confuse, et il vaut mieux placer les "
    "chiffres côte à côte plutôt que d'en choisir un."))
a.table(
    [T("Figure", "Chiffre"), T("What it appears to measure", "Ce qu'il semble mesurer"),
     T("Where it comes from", "D'où il vient")],
    [[T("1.8 cents per kilowatt-hour in 2027, rising to 11.5 cents by 2041",
        "1,8 cent le kilowattheure en 2027, montant à 11,5 cents en 2041"),
      T("The contract price schedule", "Le barème du prix contractuel"),
      T("CBC and the Financial Post", "CBC et le Financial Post")],
     [T("7.4 cents per kilowatt-hour from 2027",
        "7,4 cents le kilowattheure à partir de 2027"),
      T("An effective or all-in price including other value",
        "Un prix effectif ou tout compris incluant d'autres éléments de valeur"),
      "NTV"],
     [T("6 cents per kilowatt-hour", "6 cents le kilowattheure"),
      T("Hydro-Québec's own cost of supply — not the price paid to Newfoundland and Labrador",
        "Le coût d'approvisionnement d'Hydro-Québec — pas le prix versé à "
        "Terre-Neuve-et-Labrador"),
      T("Hydro-Québec", "Hydro-Québec")],
     [T("5.9 cents per kilowatt-hour", "5,9 cents le kilowattheure"),
      T("The December 2024 memorandum figure, now superseded",
        "Le chiffre du protocole de décembre 2024, maintenant remplacé"),
      T("Government of Newfoundland and Labrador, 2024",
        "Gouvernement de Terre-Neuve-et-Labrador, 2024")]],
    label=T("Prices reported for the new agreement — scroll sideways to see all of it",
            "Prix rapportés pour la nouvelle entente — faites défiler latéralement pour "
            "tout voir"))
a.p(T(
    "For scale, Hydro-Québec averaged 14.5 cents a kilowatt-hour on its external sales in "
    "2025 — different markets and different contracts, so not a like-for-like comparison, "
    "but a useful marker.",
    "Pour donner l'échelle, Hydro-Québec a obtenu en moyenne 14,5 cents le kilowattheure "
    "sur ses ventes externes en 2025 — des marchés et des contrats différents, donc pas une "
    "comparaison directe, mais un repère utile."))
a.p(T(
    "David Vardy, a former chair of the Newfoundland and Labrador Public Utilities Board, "
    "has questioned whether measuring the new deal against the 1969 contract sets the bar "
    "too low, and argues fairness should be judged by economic rent. On the escalation "
    "formula he says the province needed electric power markets, not the consumer price "
    "index. François Bouffard, an engineering professor at McGill, takes a more positive "
    "view, saying the parties made the pie bigger and noting that the province's allocation "
    "rises from 525 to 1,630 megawatts — a third set of allocation figures, different again "
    "from the ones the two governments published.",
    "David Vardy, ancien président du Board of Commissioners of Public Utilities de "
    "Terre-Neuve-et-Labrador, se demande si mesurer la nouvelle entente à l'aune du contrat "
    "de 1969 ne place pas la barre trop bas, et soutient que l'équité devrait se juger par "
    "la rente économique. Sur la formule d'indexation, il dit que la province avait besoin "
    "des marchés de l'électricité, pas de l'indice des prix à la consommation. François "
    "Bouffard, professeur de génie à McGill, est plus positif et estime que les parties ont "
    "agrandi le gâteau, en notant que l'allocation de la province passe de 525 à 1 630 "
    "mégawatts — un troisième jeu de chiffres d'allocation, encore différent de ceux "
    "publiés par les deux gouvernements."))

# ------------------------------------------------------------------ 9
a.h2(T("What Quebec gets", "Ce que le Québec obtient"))
a.p(T(
    "6,915 megawatts of firm supply locked in to 2077, potentially 8,515 including wind, "
    "with a further 3,850 under study. Hydro-Québec puts its own cost of that supply at "
    "about 6 cents a kilowatt-hour against roughly 17 cents for the alternatives it would "
    "otherwise need after 2035. It also takes 40 percent of Gull Island. Quebec's demand is "
    "growing quickly, and this is a large block of firm power secured for half a century.",
    "6 915 mégawatts d'approvisionnement ferme jusqu'en 2077, potentiellement 8 515 en "
    "incluant l'éolien, avec 3 850 de plus à l'étude. Hydro-Québec chiffre son propre coût "
    "pour cet approvisionnement à environ 6 cents le kilowattheure contre environ 17 cents "
    "pour les solutions de rechange dont elle aurait autrement besoin après 2035. Elle "
    "obtient aussi 40 pour cent de Gull Island. La demande québécoise croît rapidement, et "
    "il s'agit d'un gros bloc d'électricité ferme sécurisé pour un demi-siècle."))
a.p(T(
    "For the country as a whole rather than for either province, the federal release also "
    "puts 23,000 jobs in the construction phase and a 31 billion dollar contribution to "
    "Canada's economy through the early 2040s. Those two figures come from that release "
    "alone. No methodology, no modelling assumptions and no "
    "third-party assessment have been published for either, so they are attributed here "
    "rather than stated.",
    "Pour l'ensemble du pays plutôt que pour l'une ou l'autre province, le communiqué "
    "fédéral avance également 23 000 emplois en phase de construction et une contribution "
    "de 31 milliards de dollars à l'économie canadienne jusqu'au début des années 2040. Ces "
    "deux chiffres proviennent uniquement de ce communiqué. Aucune "
    "méthodologie, aucune hypothèse de modélisation et aucune évaluation indépendante n'ont "
    "été publiées pour l'un ou l'autre ; ils sont donc attribués ici plutôt qu'affirmés."))

# ------------------------------------------------------------------ 10
a.h2(T("Who has not agreed", "Qui n'a pas donné son accord"))
a.h3(T("Two Innu nations in Quebec object, and one is in court",
       "Deux nations innues au Québec s'y opposent, et l'une est devant les tribunaux"))
a.p(T(
    "On the day of the announcement, Innu Takuaikan Uashat mak Mani-utenam and "
    "Matimekush–Lac John issued a joint statement rejecting it. Their stated position is "
    "that Churchill Falls was built and is being operated illegally in Nitassinan, their "
    "territory. Chief Pako Vachon of Matimekush–Lac John said the mistakes of the past "
    "must not be repeated, and that it is time their ancestral rights and title to the "
    "territory were recognised and respected; he added that any agreement about projects on "
    "Nitassinan requires their participation and consent. Chief Jonathan Shetush of Uashat "
    "mak Mani-utenam said the Innu continue to fight in court so that any development there "
    "respects their rights.",
    "Le jour de l'annonce, Innu Takuaikan Uashat mak Mani-utenam et Matimekush–Lac John ont "
    "publié une déclaration conjointe la rejetant. Leur position déclarée est que Churchill "
    "Falls a été construit et est exploité illégalement dans le Nitassinan, leur "
    "territoire. Le chef Pako Vachon de Matimekush–Lac John a déclaré que les erreurs du "
    "passé ne doivent pas se répéter et qu'il est grand temps que leurs droits ancestraux "
    "et leur titre sur ce territoire soient reconnus et respectés ; il a ajouté que toute "
    "entente concernant des projets sur le Nitassinan exige leur participation et leur "
    "consentement. Le chef Jonathan Shetush d'Uashat mak Mani-utenam a dit que les Innus "
    "continuent de se battre devant les tribunaux pour que tout développement là-bas "
    "respecte leurs droits."))
a.p(T(
    "The litigation is real and active. A claim filed by Uashat mak Mani-utenam in Quebec "
    "Superior Court on 20 January 2024 against Hydro-Québec and the Churchill Falls "
    "corporation seeks 2.2 billion dollars plus 200 million in punitive damages and 200 "
    "million from the corporation, together with recognition of ancestral title, an "
    "injunction requiring consent in any renegotiation of the contract expiring in 2041, and "
    "an annual share of the station's profits. Some coverage cites a 4 billion dollar "
    "figure; the difference between the two has not been explained publicly. In November "
    "2025 the court allowed the action to proceed. That ruling has been appealed, and the "
    "appeal was still pending in August 2026. Nothing has been tried on the merits.",
    "Le litige est réel et actif. Une demande déposée par Uashat mak Mani-utenam le 20 "
    "janvier 2024 devant la Cour supérieure du Québec contre Hydro-Québec et la société de "
    "Churchill Falls réclame 2,2 milliards de dollars, plus 200 millions en dommages "
    "punitifs et 200 millions de la société, ainsi que la reconnaissance du titre "
    "ancestral, une injonction exigeant le consentement dans toute renégociation du contrat "
    "venant à échéance en 2041, et une part annuelle des profits de la centrale. Certaines "
    "couvertures citent un chiffre de 4 milliards ; l'écart entre les deux n'a pas été "
    "expliqué publiquement. En novembre 2025, le tribunal a permis à l'action de suivre son "
    "cours. Ce jugement a été porté en appel, et l'appel était toujours pendant en août "
    "2026. Rien n'a été jugé au fond."))
a.p(T(
    "A separate case involving the same nation and the same utility, over a 2014 agreement "
    "relating to a different project, ended in January 2025 with the Quebec Superior Court "
    "ordering Hydro-Québec to pay 5 million dollars and finding it had acted in "
    "institutional bad faith, and breached the honour of the Crown. That case is not about "
    "Churchill Falls and should not be confused with the one above.",
    "Une affaire distincte impliquant la même nation et la même société d'État, au sujet "
    "d'une entente de 2014 relative à un autre projet, s'est conclue en janvier 2025 par "
    "une ordonnance de la Cour supérieure du Québec condamnant Hydro-Québec à payer 5 "
    "millions de dollars et concluant qu'elle avait agi de mauvaise foi institutionnelle et "
    "manqué à l'honneur de la Couronne. Cette affaire ne porte pas sur Churchill Falls et "
    "ne doit pas être confondue avec la précédente."))
a.h3(T("In Labrador", "Au Labrador"))
a.p(T(
    "The Innu Nation in Labrador has been cautiously positive rather than committed. Grand "
    "Chief Jodie Ashini said the agreement sounds really promising and noted the "
    "significance of it acknowledging that the projects fall within their land claim area, "
    "while saying the document had not yet been reviewed and needed to be taken to the "
    "community. The federal package speaks of co-investment opportunities and partial "
    "ownership of wind and transmission, but no signed impact-benefit or equity agreement "
    "was announced.",
    "La Nation innue au Labrador s'est montrée prudemment favorable plutôt qu'engagée. La "
    "grande cheffe Jodie Ashini a dit que l'entente semble très prometteuse et a souligné "
    "l'importance qu'elle reconnaisse que les projets se trouvent dans leur zone de "
    "revendication territoriale, tout en indiquant que le document n'avait pas encore été "
    "examiné et devait être porté à la communauté. Le volet fédéral évoque des occasions de "
    "coinvestissement et une propriété partielle de l'éolien et du transport, mais aucune "
    "entente signée sur les répercussions et les avantages ni sur une participation n'a été "
    "annoncée."))
a.p(T(
    "The NunatuKavut Community Council said the agreement is very significant for the "
    "province and the country, and that NunatuKavut Inuit rights and interests must be "
    "addressed and accommodated before any future development at Churchill Falls or Gull "
    "Island proceeds. It plans a major projects review office and is consulting its "
    "members.",
    "Le NunatuKavut Community Council a dit que l'entente est très importante pour la "
    "province et pour le pays, et que les droits et intérêts des Inuits du NunatuKavut "
    "doivent être pris en compte et accommodés avant que tout développement futur à "
    "Churchill Falls ou à Gull Island n'aille de l'avant. Il prévoit un bureau d'examen des "
    "grands projets et consulte ses membres."))
a.h3(T("In the legislature and at the ballot box",
       "À l'assemblée législative et aux urnes"))
a.p(T(
    "The Newfoundland and Labrador New Democratic Party has called the agreement "
    "aspirational, saying it relies on external factors including the Quebec election, and "
    "has asked for an independent oversight committee. Its leader also said opposition "
    "members were not briefed before the announcement and pointed to numerical "
    "discrepancies between the two provinces' figures that oversight staff could not "
    "explain.",
    "Le Nouveau Parti démocratique de Terre-Neuve-et-Labrador a qualifié l'entente "
    "d'aspirationnelle, affirmant qu'elle dépend de facteurs externes dont l'élection "
    "québécoise, et a demandé un comité de surveillance indépendant. Son chef a aussi dit "
    "que les députés de l'opposition n'avaient pas été informés avant l'annonce et a relevé "
    "des écarts de chiffres entre les deux provinces que le personnel de surveillance n'a "
    "pu expliquer."))
a.p(T(
    "And Quebec votes on 5 October 2026. Hydro-Québec is a provincial Crown corporation, so "
    "a change of government changes its shareholder — and both of the agreement's deadlines "
    "fall after the election. Views on how much this matters differ. Kelly Blidook, an "
    "associate professor at Memorial University, told one outlet that if the Parti "
    "Québécois, currently leading in the polls, does not support the arrangement then it "
    "will not happen. Other experts told CBC the election is unlikely to put the deal in "
    "jeopardy. The Parti Québécois leader has said his party would consider maintaining the "
    "agreement if it is beneficial for Quebec. Quebec's premier has said her government will "
    "implement it and has challenged its opponents to say where they would otherwise find "
    "the power, while also acknowledging publicly that its future turns on the election "
    "result.",
    "Et le Québec vote le 5 octobre 2026. Hydro-Québec est une société d'État provinciale, "
    "de sorte qu'un changement de gouvernement change son actionnaire — et les deux "
    "échéances de l'entente tombent après l'élection. Les avis divergent sur l'ampleur de "
    "cet enjeu. Kelly Blidook, professeur agrégé à l'Université Memorial, a déclaré à un "
    "média que si le Parti québécois, actuellement en tête des sondages, n'appuie pas "
    "l'arrangement, celui-ci ne se réalisera pas. D'autres experts ont dit à CBC que "
    "l'élection risque peu de compromettre l'entente. Le chef du Parti québécois a dit que "
    "son parti envisagerait de maintenir l'entente si elle est avantageuse pour le Québec. "
    "La première ministre du Québec a dit que son gouvernement la mettra en œuvre et a mis "
    "ses opposants au défi de dire où ils trouveraient autrement cette électricité, tout en "
    "reconnaissant publiquement que son avenir dépend du résultat de l'élection."))

# ------------------------------------------------------------------ 11
a.h2(T("What to watch", "À surveiller"))
a.ul([
    T("<strong>14 September 2026</strong> — the Newfoundland and Labrador House of "
      "Assembly reconvenes to debate the agreement.",
      "<strong>14 septembre 2026</strong> — la Chambre d'assemblée de "
      "Terre-Neuve-et-Labrador se réunit pour débattre de l'entente."),
    T("<strong>5 October 2026</strong> — the Quebec general election.",
      "<strong>5 octobre 2026</strong> — l'élection générale québécoise."),
    T("<strong>31 December 2026</strong> — the target for signing the long-form binding "
      "agreements.",
      "<strong>31 décembre 2026</strong> — la date visée pour la signature des ententes "
      "contraignantes détaillées."),
    T("<strong>31 March 2027</strong> — the date the framework agreement expires unless it "
      "is extended.",
      "<strong>31 mars 2027</strong> — la date d'expiration de l'entente-cadre, sauf "
      "prolongation."),
    T("<strong>The appeal in the Innu case</strong>, which has no hearing date published.",
      "<strong>L'appel dans l'affaire innue</strong>, dont aucune date d'audience n'est "
      "publiée."),
    T("<strong>Publication of the agreement itself</strong>, and of a breakdown of the "
      "federal 10 billion dollars by instrument. Neither exists yet.",
      "<strong>La publication de l'entente elle-même</strong>, et d'une ventilation des 10 "
      "milliards de dollars fédéraux par instrument. Ni l'une ni l'autre n'existe encore."),
])

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("how-canada-rebuilds-its-economy.html",
         T("How Canada rebuilds — new customers, old barriers",
           "Comment le Canada se rebâtit — nouveaux clients, vieilles barrières")),
    link("what-canada-and-the-usa-sell-each-other.html",
         T("What Canada sells America, and what America sells Canada",
           "Ce que le Canada vend à l'Amérique, et ce que l'Amérique vend au Canada")),
    link("canada-quiz.html",
         T("Try the Canada quiz", "Essayez le quiz sur le Canada")),
])

a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://www.pm.gc.ca/en/news/news-releases/2026/08/17/prime-minister-carney-announces-largest-clean-energy-investment-north",
             T("Prime Minister of Canada — announcement of 17 August 2026",
               "Premier ministre du Canada — annonce du 17 août 2026")),
    out_link("https://www.canada.ca/en/natural-resources-canada/news/2026/08/prime-minister-carney-announces-the-largest-clean-energy-investment-in-north-american-history.html",
             T("Natural Resources Canada — news release, 17 August 2026",
               "Ressources naturelles Canada — communiqué du 17 août 2026")),
    out_link("https://www.gov.nl.ca/releases/2026/exec/0817n01/",
             T("Government of Newfoundland and Labrador — news release, 17 August 2026",
               "Gouvernement de Terre-Neuve-et-Labrador — communiqué du 17 août 2026")),
    out_link("https://news.hydroquebec.com/news/press-releases/all-quebec/power-generation-labrador-hydro-quebec-secures-quebec-energy-future-competitive-cost.html",
             T("Hydro-Québec — press release, 17 August 2026",
               "Hydro-Québec — communiqué du 17 août 2026")),
    out_link("https://waterpowercanada.ca/learn/blog/all/churchill-falls-and-gull-island-what-this-landmark-agreement-means-for-canadas-energy-future/",
             T("Waterpower Canada — what the agreement means, 21 August 2026",
               "Waterpower Canada — ce que signifie l'entente, 21 août 2026")),
    out_link("https://nlhydro.com/about-us/our-electricity-system/our-generation-assets/",
             T("Newfoundland and Labrador Hydro — generation assets",
               "Newfoundland and Labrador Hydro — actifs de production")),
    out_link("https://www.heritage.nf.ca/articles/politics/churchill-falls.php",
             T("Newfoundland and Labrador Heritage — the 1969 Churchill Falls contract",
               "Newfoundland and Labrador Heritage — le contrat de Churchill Falls de 1969")),
    out_link("https://www.gov.nl.ca/releases/2024/exec/1212n02/",
             T("Government of Newfoundland and Labrador — memorandum of understanding, 12 December 2024",
               "Gouvernement de Terre-Neuve-et-Labrador — protocole d'entente du 12 décembre 2024")),
    out_link("https://www.canlii.org/en/ca/scc/doc/2018/2018scc46/2018scc46.html",
             T("Supreme Court of Canada — Churchill Falls (Labrador) Corp. v. Hydro-Québec, 2018 SCC 46",
               "Cour suprême du Canada — Churchill Falls (Labrador) Corp. c. Hydro-Québec, 2018 CSC 46")),
    out_link("https://www.aptnnews.ca/national-news/innu-in-quebec-reject-churchill-falls-deal-between-quebec-newfoundland-and-labrador/",
             T("APTN News — Innu in Quebec reject the Churchill Falls deal, 18 August 2026",
               "APTN News — les Innus du Québec rejettent l'entente de Churchill Falls, 18 août 2026")),
    out_link("https://nunatukavut.ca/nunatukavut-community-council-looks-forward-to-engagement-and-negotiations-on-churchill-falls-and-gull-island-developments/",
             T("NunatuKavut Community Council — statement, 19 August 2026",
               "NunatuKavut Community Council — déclaration du 19 août 2026")),
    out_link("https://insideclimatenews.org/news/17082026/canada-hydro-wind-power-investments/",
             T("Inside Climate News — Canada's hydro and wind announcement, 17 August 2026",
               "Inside Climate News — l'annonce canadienne sur l'hydroélectricité et l'éolien, 17 août 2026")),
    out_link("https://www.opg.com/news-resources/newsroom/our-stories/story/darlington-refurb-construction-completed-ahead-of-schedule-under-budget/",
             T("Ontario Power Generation — Darlington refurbishment completed, February 2026",
               "Ontario Power Generation — réfection de Darlington achevée, février 2026")),
    out_link("https://atlanticbusinessmagazine.ca/web-exclusives/muskrat-falls-and-the-price-of-failure/",
             T("Atlantic Business Magazine — Muskrat Falls and the price of failure",
               "Atlantic Business Magazine — Muskrat Falls et le prix de l'échec")),
    out_link("https://www.barchart.com/story/news/35875103/bc-hydro-says-it-should-have-been-more-proactive-as-site-c-costs-overflowed",
             T("Reporting on BC Hydro's lessons-learned report to the utilities commission on Site C, November 2025",
               "Reportage sur le rapport de BC Hydro à la régie sur les leçons tirées de Site C, novembre 2025")),
    out_link("https://www.electionsquebec.qc.ca/en/vote/current-and-upcoming-elections/",
             T("Élections Québec — current and upcoming elections",
               "Élections Québec — élections en cours et à venir")),
    out_link("https://vocm.com/2026/08/17/cf-deal-draft/",
             T("VOCM — reporting on the agreement, 17 August 2026",
               "VOCM — reportage sur l'entente, 17 août 2026")),
    out_link("https://energynow.ca/2026/08/more-money-more-power-but-how-good-is-the-new-churchill-falls-deal-for-newfoundland/",
             T("Financial Post via EnergyNow — how good is the new deal for Newfoundland?, 21 August 2026",
               "Financial Post via EnergyNow — l'entente est-elle bonne pour Terre-Neuve ?, 21 août 2026")),
])

a.disclaimer(T(
    "This article is for general information and study. "
    "This site is unofficial and not affiliated with the Government of Canada, the "
    "Government of Quebec or the Government of Newfoundland and Labrador. Every source "
    "used is listed above and on our sources page.",
    "Cet article est fourni à titre d'information générale et d'étude. Ce site est non "
    "officiel et n'a aucun lien avec le gouvernement du Canada, celui du Québec ni celui de "
    "Terre-Neuve-et-Labrador. Toutes les sources utilisées sont énumérées ci-dessus et sur "
    "notre page des sources."))

if __name__ == "__main__":
    a.build()
    flush_pairs()
