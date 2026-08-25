#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article 7 — the Major Projects Office and Canada's big projects.

Source: research/major-projects-office-20260824.md in the private project notes.

The finding this page is built on, and which almost no coverage leads with:
Schedule 1 of the Building Canada Act is empty. Eighteen projects have been
REFERRED to the office; none has been DESIGNATED under the Act, so the Act's
deeming provision has never been used. Verified 24 August 2026 against the
consolidated statute, whose own page stamp reads 20 August 2026. That will
change, probably in the autumn, so the page is dated in three places.

Four things were deliberately kept off the page: the names of the nine
transformative strategies (the government's complete list was not retrievable),
the court and filing date of the First Nations constitutional challenge (every
outlet carrying it blocked automated fetching, so only what three of them agree
on is stated), any methodology for the 337,000 jobs and the billions — none is
published, so the figures are attributed and never asserted — and any claim that
the office has sped anything up, which cannot be known until one project has
been through it.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="canada-major-projects-office-explained.html",
    section="Energy",
    title=T("Canada's Big Projects — What Is Built and What Is on Paper",
            "Les grands projets du Canada — ce qui est bâti et ce qui est sur papier"),
    desc=T("Eighteen projects, a new law, and a government figure of 337,000 jobs. A plain "
           "look at Canada's Major Projects Office: what it is, what it can actually do, "
           "what exists today, and what is still only promised.",
           "Dix-huit projets, une nouvelle loi et un chiffre gouvernemental de 337 000 "
           "emplois. Un regard simple sur le Bureau des grands projets du Canada : ce qu'il "
           "est, ce qu'il peut réellement faire, ce qui existe aujourd'hui et ce qui n'est "
           "encore que promis."),
    h1=T("\U0001F3D7️ Canada's big projects — what is built, and what is on paper",
         "\U0001F3D7️ Les grands projets du Canada — ce qui est bâti et ce qui est sur "
         "papier"),
    hero=T("A year ago Canada created an office to get large projects built faster, and gave "
           "it a law with unusual powers. Eighteen projects are now in its process. The "
           "powers have not yet been used on any of them.",
           "Il y a un an, le Canada a créé un bureau pour faire bâtir plus vite les grands "
           "projets, et lui a donné une loi aux pouvoirs inhabituels. Dix-huit projets sont "
           "maintenant dans son processus. Ces pouvoirs n'ont encore été utilisés sur "
           "aucun d'eux."),
    checked=T("Last checked 24 August 2026 — this page covers a fast-moving situation",
              "Dernière vérification le 24 août 2026 — cette page traite d'une situation "
              "qui évolue vite"),
)

# ------------------------------------------------------------------ 1
a.h2(T("The short answer", "La réponse courte"))
a.p(T(
    "The Major Projects Office opened on 29 August 2025. It does not build anything, pay for "
    "anything or regulate anything. It coordinates. In its own words, it works with the company "
    "or government behind a project, the provinces and territories, Indigenous Peoples and "
    "federal partners, to recommend the best course to complete project approvals and get "
    "these projects built faster. Its target is to cut that route from five years or more "
    "down to two.",
    "Le Bureau des grands projets a ouvert le 29 août 2025. Il ne construit rien, ne paie "
    "rien et ne réglemente rien. Il coordonne. Selon ses propres mots, il travaille avec "
    "l'entreprise ou le gouvernement qui porte un projet, les provinces et territoires, les "
    "peuples autochtones et les partenaires fédéraux, pour recommander la meilleure voie vers "
    "les autorisations et faire bâtir ces projets plus vite. Son objectif est de ramener cette "
    "voie de cinq ans ou plus à deux ans."))
a.p(T(
    "Eighteen projects and nine broader strategies are in that process. The government puts "
    "the whole list at 192 billion dollars of new investment, 337,000 jobs and a further 500 "
    "billion dollars of future private investment. Those are the government's figures, from "
    "its own page, and no method for arriving at them has been published.",
    "Dix-huit projets et neuf stratégies plus larges sont dans ce processus. Le gouvernement "
    "chiffre l'ensemble à 192 milliards de dollars de nouveaux investissements, 337 000 "
    "emplois et 500 milliards de dollars d'investissements privés futurs. Ce sont les "
    "chiffres du gouvernement, tirés de sa propre page, et aucune méthode pour y parvenir "
    "n'a été publiée."))
a.callout(T(
    "<strong>The fact underneath all of it.</strong> Being sent to the office is not the same "
    "as being approved under the new law. Eighteen projects have been sent. As of 24 August "
    "2026 the list of projects designated under the Building Canada Act — Schedule 1 of the "
    "Act itself — is <strong>empty</strong>. The law's main power has never been used. The "
    "government began the process for the first three projects on 24 June 2026 and is aiming "
    "at a decision in the autumn.",
    "<strong>Le fait qui sous-tend tout le reste.</strong> Être confié au bureau n'équivaut "
    "pas à être approuvé en vertu de la nouvelle loi. Dix-huit projets ont été confiés. Au 24 "
    "août 2026, la liste des projets désignés sous la Loi sur la construction du Canada — "
    "l'annexe 1 de la loi elle-même — est <strong>vide</strong>. Le principal pouvoir de la "
    "loi n'a jamais servi. Le gouvernement a lancé le processus pour les trois premiers "
    "projets le 24 juin 2026 et vise une décision à l'automne."))

# ------------------------------------------------------------------ 2
a.h2(T("The eighteen projects", "Les dix-huit projets"))
a.p(T(
    "This is the full list the office publishes, with its own categories. It gives no dollar "
    "value, no timeline and no stage for any of them. The dollar figures come from the "
    "announcement releases instead; the stages are not published anywhere.",
    "Voici la liste complète que publie le bureau, avec ses propres catégories. Elle ne donne "
    "pour aucun d'eux de valeur en dollars, d'échéancier ni d'étape. Les montants viennent "
    "plutôt des communiqués d'annonce ; les étapes ne sont publiées nulle part."))
a.fig(bar_chart(
    T("Where the eighteen projects are", "Où se trouvent les dix-huit projets"),
    [(T("British Columbia", "Colombie-Britannique"), 5),
     (T("Northwest Territories", "Territoires du Nord-Ouest"), 3),
     (T("Ontario", "Ontario"), 3),
     (T("Nunavut", "Nunavut"), 2),
     (T("Quebec", "Québec"), 2),
     (T("Alberta to British Columbia", "De l'Alberta à la Colombie-Britannique"), 1),
     (T("New Brunswick", "Nouveau-Brunswick"), 1),
     (T("Saskatchewan", "Saskatchewan"), 1)]))
a.p(T(
    "Five of the eighteen are in the Northwest Territories and Nunavut. None is in Yukon.",
    "Cinq des dix-huit se trouvent dans les Territoires du Nord-Ouest et au Nunavut. Aucun "
    "n'est au Yukon."))
a.table(
    [T("Project", "Projet"), T("Where", "Où"), T("What it is", "De quoi il s'agit"),
     T("Behind it", "Qui le porte")],
    [[T("Arctic Economic and Security Corridor", "Corridor économique et de sécurité de l'Arctique"),
      T("Northwest Territories", "Territoires du Nord-Ouest"), T("Transport", "Transport"),
      T("Tłı̨chǫ Government, Dene First Nation and the territorial government",
        "Gouvernement tlicho, Première Nation dénée et gouvernement territorial")],
     [T("Canada Nickel's Crawford Project", "Projet Crawford de Canada Nickel"),
      T("Timmins, Ontario", "Timmins, Ontario"), T("Mining", "Mine"),
      T("Canada Nickel Company", "Canada Nickel Company")],
     [T("Contrecœur Container Terminal", "Terminal à conteneurs de Contrecœur"),
      T("Contrecœur, Quebec", "Contrecœur, Québec"), T("Industrial", "Industriel"),
      T("Montreal Port Authority", "Administration portuaire de Montréal")],
     [T("Darlington New Nuclear Project", "Projet nucléaire de Darlington"),
      T("Bowmanville, Ontario", "Bowmanville, Ontario"), T("Electricity", "Électricité"),
      T("Ontario Power Generation", "Ontario Power Generation")],
     [T("Deep Geological Repository", "Dépôt géologique en profondeur"),
      T("Wabigoon Lake / Ignace, Ontario", "Lac Wabigoon / Ignace, Ontario"),
      T("Electricity", "Électricité"),
      T("Nuclear Waste Management Organization",
        "Société de gestion des déchets nucléaires")],
     [T("Grays Bay Road and Port", "Route et port de Grays Bay"),
      T("Kitikmeot, Nunavut", "Kitikmeot, Nunavut"), T("Transport", "Transport"),
      T("West Kitikmeot Resources Corporation", "West Kitikmeot Resources Corporation")],
     [T("Iqaluit Nukkiksautiit Hydro", "Hydroélectricité Nukkiksautiit d'Iqaluit"),
      T("Iqaluit, Nunavut", "Iqaluit, Nunavut"), T("Electricity", "Électricité"),
      T("Nunavut Nukkiksautiit Corporation", "Nunavut Nukkiksautiit Corporation")],
     [T("Ksi Lisims LNG", "Ksi Lisims GNL"),
      T("Pearse Island, British Columbia", "Île Pearse, Colombie-Britannique"),
      T("Energy", "Énergie"),
      T("Western LNG, the Nisg̱a'a Nation and Rockies LNG Partners",
        "Western LNG, la Nation Nisga'a et Rockies LNG Partners")],
     [T("LNG Canada Phase 2", "LNG Canada phase 2"),
      T("Kitimat, British Columbia", "Kitimat, Colombie-Britannique"),
      T("Energy", "Énergie"), T("LNG Canada", "LNG Canada")],
     [T("Mackenzie Valley Highway", "Route de la vallée du Mackenzie"),
      T("Wrigley to Inuvik, NWT", "De Wrigley à Inuvik, T.N.-O."), T("Transport", "Transport"),
      T("Government of the Northwest Territories",
        "Gouvernement des Territoires du Nord-Ouest")],
     [T("McIlvenna Bay Foran Copper Mine", "Mine de cuivre Foran de McIlvenna Bay"),
      T("East-central Saskatchewan", "Centre-est de la Saskatchewan"), T("Mining", "Mine"),
      T("Foran Mining", "Foran Mining")],
     [T("North Coast Transmission Line", "Ligne de transport de la côte Nord"),
      T("Northwestern British Columbia", "Nord-ouest de la Colombie-Britannique"),
      T("Electricity", "Électricité"), T("BC Hydro", "BC Hydro")],
     [T("Northcliff Resources' Sisson Mine", "Mine Sisson de Northcliff Resources"),
      T("Sisson Brook, New Brunswick", "Sisson Brook, Nouveau-Brunswick"),
      T("Mining", "Mine"), T("Northcliff Resources", "Northcliff Resources")],
     [T("Nouveau Monde Graphite's Matawinie Mine",
        "Mine Matawinie de Nouveau Monde Graphite"),
      T("Saint-Michel-des-Saints, Quebec", "Saint-Michel-des-Saints, Québec"),
      T("Mining", "Mine"), T("Nouveau Monde Graphite", "Nouveau Monde Graphite")],
     [T("Red Chris Mine Expansion", "Agrandissement de la mine Red Chris"),
      T("Northwestern British Columbia", "Nord-ouest de la Colombie-Britannique"),
      T("Mining", "Mine"),
      T("Newmont Mining and Imperial Metals, with the Tahltan Nation",
        "Newmont Mining et Imperial Metals, avec la Nation Tahltan")],
     [T("Roberts Bank Terminal 2", "Terminal 2 de Roberts Bank"),
      T("Delta, British Columbia", "Delta, Colombie-Britannique"), T("Transport", "Transport"),
      T("Vancouver Fraser Port Authority",
        "Administration portuaire Vancouver Fraser")],
     [T("Taltson Hydro Expansion", "Agrandissement hydroélectrique de Taltson"),
      T("Great Slave Lake region, NWT", "Région du Grand lac des Esclaves, T.N.-O."),
      T("Electricity", "Électricité"),
      T("Government of the Northwest Territories",
        "Gouvernement des Territoires du Nord-Ouest")],
     [T("West Coast Oil Pipeline", "Oléoduc de la côte Ouest"),
      T("Alberta to British Columbia", "De l'Alberta à la Colombie-Britannique"),
      T("Energy", "Énergie"), T("Government of Alberta", "Gouvernement de l'Alberta")]],
    label=T("The eighteen projects referred to the Major Projects Office — scroll sideways to "
            "see all of it",
            "Les dix-huit projets confiés au Bureau des grands projets — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "Alongside them sit nine broader efforts the office calls transformative strategies, "
    "covering critical minerals, wind energy, infrastructure in the North, ports, and carbon "
    "capture and storage. We could not retrieve a page listing all nine names — the office's own "
    "link to a complete list did not load when it was checked on 24 August 2026. Two are "
    "known: the Atlantic Energy Strategy, referred in the autumn of 2025, and "
    "the Labrador Trough clean power, critical minerals and infrastructure corridor, referred "
    "on 17 August 2026 as part of the Churchill Falls and Gull Island agreement.",
    "À leurs côtés se trouvent neuf démarches plus larges que le bureau appelle stratégies "
    "transformatrices, portant sur les minéraux critiques, l'énergie éolienne, les "
    "infrastructures du Nord, les ports et le captage et stockage du carbone. Le gouvernement "
    "n'a pas pu récupérer de page énumérant les neuf noms — le lien du bureau vers une liste "
    "complète ne s'est pas chargé lors de la vérification du 24 août 2026. Deux sont "
    "connus : la Stratégie "
    "énergétique de l'Atlantique, confiée à l'automne 2025, et le corridor d'énergie propre, "
    "de minéraux critiques et d'infrastructures de la fosse du Labrador, confié le 17 août "
    "2026 dans le cadre de l'entente sur Churchill Falls et Gull Island."))

# ------------------------------------------------------------------ 3
a.h2(T("The law behind it, and the one sentence that matters",
       "La loi qui le sous-tend, et la phrase qui compte"))
a.p(T(
    "The office was created by the Building Canada Act, which came into force in June 2025. "
    "The Act's stated purpose is to enhance Canada's prosperity, national security, economic "
    "security, national defence and national autonomy by advancing projects in the national "
    "interest through an accelerated process.",
    "Le bureau a été créé par la Loi sur la construction du Canada, entrée en vigueur en juin "
    "2025. La loi dit avoir pour objet d'accroître la prospérité, la sécurité nationale, la "
    "sécurité économique, la défense nationale et l'autonomie nationale du Canada en faisant "
    "avancer par un processus accéléré les projets d'intérêt national."))
a.p(T(
    "Cabinet may add a project to Schedule 1 of the Act. In deciding, it may consider whether "
    "the project would strengthen Canada's autonomy, resilience and security; provide economic "
    "or other benefits to Canada; have a high likelihood of successful execution; advance the "
    "interests "
    "of Indigenous peoples; and contribute to clean growth and Canada's climate objectives. "
    "Before recommending it, the minister must consult Indigenous peoples whose rights under "
    "section 35 of the Constitution Act, 1982 may be adversely affected.",
    "Le Cabinet peut ajouter un projet à l'annexe 1 de la loi. Pour en décider, il peut "
    "examiner si le projet renforcerait l'autonomie, la résilience et la sécurité du Canada ; "
    "procurerait au Canada des avantages économiques ou autres ; aurait une forte probabilité de "
    "réalisation ; ferait progresser les intérêts des peuples autochtones ; et contribuerait à "
    "une croissance propre et aux objectifs climatiques du Canada. Avant de le recommander, le "
    "ministre doit consulter les peuples autochtones dont les droits reconnus par l'article 35 "
    "de la Loi constitutionnelle de 1982 pourraient être lésés."))
a.p(T(
    "What listing then does is set out in one sentence, and it is worth reading in full rather "
    "than in summary.",
    "Ce que l'inscription produit ensuite tient en une phrase, et il vaut mieux la lire en "
    "entier plutôt qu'en résumé."))
a.callout(T(
    "<strong>Building Canada Act, section 6(1):</strong> \"Every determination and finding "
    "that has to be made and every opinion that has to be formed in order for an authorization "
    "to be granted in respect of a national interest project is deemed to be made or formed, "
    "as the case may be, in favour of permitting the project.\"",
    "<strong>Loi sur la construction du Canada, paragraphe 6(1) :</strong> « Toute décision, "
    "conclusion ou opinion devant être rendue, tirée ou formée pour qu'une autorisation soit "
    "accordée à l'égard d'un projet d'intérêt national est réputée l'avoir été en faveur de "
    "l'autorisation du projet. »"))
a.p(T(
    "It does not cancel the review. It fixes the answer to the question of whether a project "
    "may go ahead, and moves the work onto the conditions it must meet. The government adds "
    "that listing does not change Canada's obligation to see through the impact assessment and "
    "regulatory processes set out in modern treaties, and does not affect safety and other "
    "matters decided under the Nuclear Safety and Control Act.",
    "Elle n'annule pas l'examen. Elle fixe la réponse à la question de savoir si un projet peut "
    "aller de l'avant, et reporte le travail sur les conditions qu'il doit respecter. Le "
    "gouvernement ajoute que l'inscription ne change rien à l'obligation du Canada de mener à "
    "terme les processus d'évaluation d'impact et de réglementation prévus dans les traités "
    "modernes, et n'a pas d'effet sur la sûreté et les autres questions tranchées en vertu de "
    "la Loi sur la sûreté et la réglementation nucléaires."))
a.p(T(
    "Three limits are written into the Act itself, and they are easy to miss. No project can be "
    "added after five years. Conditions cannot be amended after five years. And the documents "
    "a listed project receives expire if it has not substantially started within five years. "
    "This is a window, not a permanent regime.",
    "Trois limites sont inscrites dans la loi elle-même, et elles passent facilement inaperçues. "
    "Aucun projet ne peut être ajouté après cinq ans. Les conditions ne peuvent être modifiées "
    "après cinq ans. Et les documents que reçoit un projet inscrit expirent s'il n'a pas "
    "véritablement commencé dans les cinq ans. C'est une fenêtre, pas un régime permanent."))

# ------------------------------------------------------------------ 4
a.h2(T("Sent to the office is not the same as approved under the law",
       "Être confié au bureau n'équivaut pas à être approuvé par la loi"))
a.p(T(
    "This distinction is blurred almost everywhere, and it decides how much has actually "
    "happened.",
    "Cette distinction est brouillée presque partout, et c'est elle qui détermine ce qui s'est "
    "réellement passé."))
a.ul([
    T("<strong>Referral</strong> means the office assesses the project and helps coordinate it "
      "through the existing federal system. Eighteen projects are here.",
      "<strong>Le renvoi</strong> signifie que le bureau évalue le projet et aide à le "
      "coordonner dans le système fédéral existant. Dix-huit projets en sont là."),
    T("<strong>Designation</strong> means cabinet has listed the project in Schedule 1 and the "
      "sentence above switches on. As of 24 August 2026, no project has been designated.",
      "<strong>La désignation</strong> signifie que le Cabinet a inscrit le projet à l'annexe 1 "
      "et que la phrase ci-dessus prend effet. Au 24 août 2026, aucun projet n'a été désigné."),
])
a.p(T(
    "The process for the first three began on 24 June 2026 — the Mackenzie Valley Highway, "
    "Grays Bay Road and Port, and the Deep Geological Repository. Consultations with affected "
    "Indigenous rights holders, provinces and territories were to start in the following weeks, "
    "with a decision aimed at the autumn of 2026. A notice must appear in the Canada Gazette "
    "thirty days before any Order in Council. In August 2026 the federal government also moved "
    "to begin the same process for the Alberta-backed West Coast oil pipeline.",
    "Le processus pour les trois premiers a commencé le 24 juin 2026 — la route de la vallée du "
    "Mackenzie, la route et le port de Grays Bay, et le dépôt géologique en profondeur. Les "
    "consultations avec les détenteurs de droits autochtones touchés, les provinces et les "
    "territoires devaient s'amorcer dans les semaines suivantes, avec une décision visée pour "
    "l'automne 2026. Un avis doit paraître dans la Gazette du Canada trente jours avant tout "
    "décret. En août 2026, le gouvernement fédéral a aussi entrepris la même démarche pour "
    "l'oléoduc de la côte Ouest appuyé par l'Alberta."))

# ------------------------------------------------------------------ 5
a.h2(T("What benefit exists today", "Quel avantage existe aujourd'hui"))
a.p(T(
    "Honestly: the office is a year old, and large projects take a decade. Nothing has been "
    "built because of it, and nothing could have been.",
    "Honnêtement : le bureau a un an, et les grands projets prennent une décennie. Rien n'a été "
    "bâti grâce à lui, et rien n'aurait pu l'être."))
a.p(T(
    "At least one thing on the list is genuinely under construction. The Darlington New "
    "Nuclear Project is the clearest case — described as the G7's first small modular reactor, "
    "with shaft excavation completed in early 2026. But it was approved for construction in "
    "May 2025, months before the office opened. The office did not cause it.",
    "Au moins une chose sur la liste est réellement en construction. Le projet nucléaire de "
    "Darlington en est le cas le plus net — décrit comme le premier petit réacteur modulaire du "
    "G7, dont l'excavation du puits s'est achevée au début de 2026. Mais sa construction a été "
    "approuvée en mai 2025, des mois avant l'ouverture du bureau. Le bureau n'en est pas la "
    "cause."))
a.p(T(
    "A law firm reviewing the second group of projects in November 2025 made the same point: "
    "many of them had already been approved under the ordinary federal processes. The firm's "
    "argument was that the office may be adding streamlining to projects that did not need it "
    "in order to proceed.",
    "Un cabinet d'avocats qui examinait le deuxième groupe de projets en novembre 2025 a fait "
    "le même constat : plusieurs avaient déjà été approuvés par les processus fédéraux "
    "ordinaires. Son argument était que le bureau ajoute peut-être de l'accélération à des "
    "projets qui n'en avaient pas besoin pour aller de l'avant."))
a.p(T(
    "So the fair summary of the first year is this. The office has a list, a process and a "
    "target. What it does not have is a single completed case, and the "
    "two-year promise cannot be judged until one project has gone all the way through. The "
    "first will not be listed before the autumn.",
    "Le résumé juste de la première année est donc le suivant. Le bureau a une liste, un "
    "processus et une cible. Ce qu'il n'a pas, c'est un seul dossier mené à "
    "terme, et la promesse des deux ans ne pourra être jugée qu'une fois qu'un projet aura "
    "parcouru tout le chemin. Le premier ne sera pas inscrit avant l'automne."))

# ------------------------------------------------------------------ 6
a.h2(T("What benefit is promised", "Quel avantage est promis"))
a.p(T(
    "The figures below all come from government announcements. None carries a published "
    "method, and none has been checked by an independent body. They are given here as claims, "
    "with the date each was made or last checked, because they move.",
    "Les chiffres ci-dessous proviennent tous d'annonces gouvernementales. Aucun n'est "
    "accompagné d'une méthode publiée, et aucun n'a été vérifié par un organisme indépendant. "
    "Ils sont présentés ici comme des affirmations, avec la date à laquelle chacun a été "
    "avancé ou vérifié pour la dernière fois, parce qu'ils changent."))
a.table(
    [T("When", "Quand"), T("What was said", "Ce qui a été dit")],
    [[T("11 September 2025", "11 septembre 2025"),
      T("The first five projects would put more than $60 billion into the economy",
        "Les cinq premiers projets injecteraient plus de 60 milliards de dollars dans "
        "l'économie")],
     [T("13 November 2025", "13 novembre 2025"),
      T("The next six were worth over $56 billion and 68,000 jobs",
        "Les six suivants valaient plus de 56 milliards de dollars et 68 000 emplois")],
     [T("24 June 2026", "24 juin 2026"),
      T("16 projects and 7 strategies, more than $135 billion combined",
        "16 projets et 7 stratégies, plus de 135 milliards de dollars au total")],
     [T("Checked 24 August 2026", "Vérifié le 24 août 2026"),
      T("18 projects and 9 strategies, $192 billion of new investment, 337,000 jobs, and "
        "$500 billion of future private sector investment",
        "18 projets et 9 stratégies, 192 milliards de dollars de nouveaux investissements, "
        "337 000 emplois et 500 milliards de dollars d'investissements privés futurs")]],
    label=T("What the government has said the list is worth — scroll sideways to see all of it",
            "Ce que le gouvernement a dit de la valeur de la liste — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "A few individual projects do have published numbers, and they are more useful than the "
    "totals because you can picture them. Darlington's first reactor is meant to power 300,000 "
    "homes and sustain 3,700 jobs a year, and 18,000 during construction over 65 years. "
    "Contrecœur would "
    "raise the Port of Montréal's capacity by about 60 percent. Red Chris would raise Canada's "
    "annual copper production by over 15 percent. McIlvenna Bay is put at 400 jobs.",
    "Quelques projets pris individuellement ont des chiffres publiés, et ils sont plus utiles "
    "que les totaux parce qu'on peut se les représenter. Le premier réacteur de Darlington "
    "doit alimenter 300 000 foyers et soutenir 3 700 emplois par an, et 18 000 pendant la "
    "construction sur 65 ans. Contrecœur augmenterait d'environ 60 pour cent la capacité du port de "
    "Montréal. Red Chris augmenterait de plus de 15 pour cent la production annuelle de cuivre "
    "du Canada. McIlvenna Bay est chiffré à 400 emplois."))
a.p(T(
    "Read them the way you would read any projection about something not yet built. Canada's "
    "recent record on large energy projects is mixed. Muskrat Falls was sanctioned at 7.4 "
    "billion dollars and came in around 13.5 billion, about 82 percent over. Site C's approved "
    "budget rose from 8.775 billion including its reserve to 16 billion, also about 82 "
    "percent, and no final audited total has been published. The Darlington refurbishment "
    "finished 150 million under a 12.8 billion dollar budget and four months early.",
    "Lisez-les comme vous liriez toute projection sur quelque chose qui n'est pas encore bâti. "
    "Le bilan récent du Canada en matière de grands projets énergétiques est mitigé. Muskrat "
    "Falls a été approuvé à 7,4 milliards de dollars et a coûté environ 13,5 milliards, soit "
    "environ 82 pour cent de plus. Le budget approuvé de Site C est passé de 8,775 milliards, "
    "réserve comprise, à 16 milliards, soit également environ 82 pour cent, et aucun total "
    "final vérifié n'a été publié. La réfection de Darlington s'est terminée 150 millions sous "
    "un budget de 12,8 milliards de dollars et quatre mois plus tôt que prévu."))

# ------------------------------------------------------------------ 7
a.h2(T("Who objects, and to what", "Qui s'y oppose, et à quoi"))
a.p(T(
    "The law is being challenged in court. Nine First Nations in Ontario launched a "
    "constitutional challenge against the federal Bill C-5, which contains the Building Canada "
    "Act, together with Ontario's own Bill 5. Five more First Nations later joined, and the "
    "group also sought an injunction.",
    "La loi est contestée devant les tribunaux. Neuf Premières Nations de l'Ontario ont lancé "
    "une contestation constitutionnelle contre le projet de loi fédéral C-5, qui contient la "
    "Loi sur la construction du Canada, ainsi que contre le projet de loi 5 de l'Ontario. Cinq "
    "autres Premières Nations s'y sont ensuite jointes, et le groupe a aussi demandé une "
    "injonction."))
a.p(T(
    "The objection is to how decisions get made, not to development itself. Ontario Regional "
    "Chief Abram Benedict put it this way in June 2025:",
    "L'objection porte sur la façon dont les décisions sont prises, non sur le développement "
    "lui-même. Le chef régional de l'Ontario Abram Benedict l'a exprimé ainsi en juin 2025 :"))
a.callout(T(
    "\"We are not anti-development, and our communities want to be prosperous, but we won't "
    "accept laws that silence our voices, or that destroy our environment and ways of life.\"",
    "« Nous ne sommes pas contre le développement, et nos communautés veulent prospérer, mais "
    "nous n'accepterons pas des lois qui font taire nos voix, ou qui détruisent notre "
    "environnement et nos modes de vie. »"))
a.p(T(
    "Grand Council Treaty #3 Ogichidaa Francis Kavanaugh, the same day: \"Canada claims to be a "
    "nation of laws, we have proven time and time again that Canada cannot just run roughshod "
    "over our rights.\" Temagami Chief Shelly Moore-Frappier: \"Bill C-5 is not "
    "reconciliation—it's a betrayal of it.\" The stated concerns are that cabinet can "
    "fast-track projects without meaningful consultation, that treaty rights and environmental "
    "protections are weakened, and that the bill itself passed with only two days of committee "
    "debate.",
    "L'Ogichidaa du Grand Conseil du Traité no 3, Francis Kavanaugh, le même jour : « Le Canada "
    "se dit un pays de lois ; nous avons prouvé maintes et maintes fois que le Canada ne peut "
    "pas simplement piétiner nos droits. » La cheffe de Temagami, Shelly Moore-Frappier : « Le "
    "projet de loi C-5 n'est pas la réconciliation, c'en est une trahison. » Les préoccupations "
    "exprimées sont que le Cabinet peut accélérer des "
    "projets sans consultation véritable, que les droits issus de traités et les protections "
    "environnementales sont affaiblis, et que le projet de loi lui-même a été adopté après "
    "seulement deux jours de débat en comité."))
a.p(T(
    "At the same time, several of the eighteen projects have Indigenous governments or nations "
    "as proponents or partners — the Arctic corridor with the Tłı̨chǫ Government and the Dene "
    "First Nation, Ksi Lisims LNG with the Nisg̱a'a Nation, Iqaluit Nukkiksautiit, McIlvenna Bay "
    "with the Peter Ballantyne Cree Nation, and Red Chris with the Tahltan Nation. Both things "
    "are true at once, and a page that reported only one of them would be misleading.",
    "En même temps, plusieurs des dix-huit projets ont des gouvernements ou des nations "
    "autochtones comme promoteurs ou partenaires — le corridor de l'Arctique avec le "
    "gouvernement tlicho et la Première Nation dénée, Ksi Lisims GNL avec la Nation Nisga'a, "
    "Nukkiksautiit d'Iqaluit, McIlvenna Bay avec la Nation crie de Peter Ballantyne, et Red "
    "Chris avec la Nation Tahltan. Les deux choses sont vraies en même temps, et une page qui "
    "n'en rapporterait qu'une seule induirait en erreur."))

# ------------------------------------------------------------------ 8
a.h2(T("What to watch", "À surveiller"))
a.ul([
    T("<strong>Autumn 2026</strong> — the first decision on listing the Mackenzie Valley "
      "Highway, Grays Bay Road and Port, and the Deep Geological Repository. Watch the Canada "
      "Gazette: a notice must appear thirty days before the Order in Council.",
      "<strong>Automne 2026</strong> — la première décision sur l'inscription de la route de la "
      "vallée du Mackenzie, de la route et du port de Grays Bay et du dépôt géologique en "
      "profondeur. Surveillez la Gazette du Canada : un avis doit paraître trente jours avant "
      "le décret."),
    T("<strong>The West Coast oil pipeline</strong>, which the federal government moved to list "
      "in August 2026.",
      "<strong>L'oléoduc de la côte Ouest</strong>, que le gouvernement fédéral a entrepris "
      "d'inscrire en août 2026."),
    T("<strong>The court challenge</strong>, which could change what the Act can do.",
      "<strong>La contestation judiciaire</strong>, qui pourrait modifier ce que la loi peut "
      "faire."),
    T("<strong>The first completed case</strong> — until one project goes from referral to "
      "final federal approval, the two-year target is a promise and not a result.",
      "<strong>Le premier dossier mené à terme</strong> — tant qu'un projet ne sera pas passé "
      "du renvoi à l'approbation fédérale finale, la cible de deux ans reste une promesse et "
      "non un résultat."),
    T("<strong>The five-year window closing</strong> — no project can be added to the list "
      "more than five years after the Act was enacted.",
      "<strong>La fermeture de la fenêtre de cinq ans</strong> — aucun projet ne peut être "
      "ajouté à la liste plus de cinq ans après l'adoption de la loi."),
])

a.h2(T("What is not known", "Ce qu'on ne sait pas"))
a.ul([
    T("How the 337,000 jobs, the 192 billion and the 500 billion were calculated. No method is "
      "published for any of them.",
      "Comment les 337 000 emplois, les 192 milliards et les 500 milliards ont été calculés. "
      "Aucune méthode n'est publiée pour l'un ou l'autre."),
    T("The names of all nine transformative strategies. The government describes the areas they "
      "cover but does not publish the nine together.",
      "Les noms des neuf stratégies transformatrices. Le gouvernement décrit les domaines "
      "qu'elles couvrent mais ne publie pas les neuf ensemble."),
    T("What stage each project is at. The office's own project list gives no stages, no dollar "
      "values and no timelines.",
      "L'étape où en est chaque projet. La liste de projets du bureau ne donne ni étapes, ni "
      "montants, ni échéanciers."),
    T("Whether the office has made anything faster. Nothing has finished its process, so there "
      "is nothing yet to measure.",
      "Si le bureau a accéléré quoi que ce soit. Rien n'a terminé son processus, il n'y a donc "
      "encore rien à mesurer."),
])

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("churchill-falls-gull-island-explained.html",
         T("Churchill Falls and Gull Island — what was actually agreed",
           "Churchill Falls et Gull Island — ce qui a réellement été conclu")),
    link("how-canada-rebuilds-its-economy.html",
         T("How Canada rebuilds — new customers, old barriers",
           "Comment le Canada se rebâtit — nouveaux clients, vieilles barrières")),
    link("what-canada-and-the-usa-sell-each-other.html",
         T("What Canada sells America, and what America sells Canada",
           "Ce que le Canada vend à l'Amérique, et ce que l'Amérique vend au Canada")),
])

a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://www.canada.ca/en/privy-council/major-projects-office.html",
             T("Government of Canada — the Major Projects Office",
               "Gouvernement du Canada — le Bureau des grands projets")),
    out_link("https://www.canada.ca/en/privy-council/major-projects-office/projects/national.html",
             T("Major Projects Office — projects referred to the office",
               "Bureau des grands projets — projets qui lui ont été confiés")),
    out_link("https://www.canada.ca/en/privy-council/major-projects-office/our-priorities/projects-transformative-strategies.html",
             T("Major Projects Office — projects and transformative strategies",
               "Bureau des grands projets — projets et stratégies transformatrices")),
    out_link("https://www.canada.ca/en/privy-council/major-projects-office/advancing-nation-building-projects/projects-designated-under-building-canada-act.html",
             T("Major Projects Office — how a project is designated under the Building Canada Act",
               "Bureau des grands projets — comment un projet est désigné sous la Loi sur la construction du Canada")),
    out_link("https://laws-lois.justice.gc.ca/eng/acts/B-9.89/page-1.html",
             T("Building Canada Act — purpose, factors and the effect of listing",
               "Loi sur la construction du Canada — objet, facteurs et effet de l'inscription")),
    out_link("https://laws-lois.justice.gc.ca/eng/acts/B-9.89/page-3.html",
             T("Building Canada Act — Schedule 1, the list of national interest projects",
               "Loi sur la construction du Canada — annexe 1, la liste des projets d'intérêt national")),
    out_link("https://www.pm.gc.ca/en/news/news-releases/2025/09/11/prime-minister-carney-announces-first-projects-be-reviewed-new",
             T("Prime Minister of Canada — first projects referred to the office, 11 September 2025",
               "Premier ministre du Canada — premiers projets confiés au bureau, 11 septembre 2025")),
    out_link("https://www.canada.ca/en/one-canadian-economy/news/2026/06/canada-initiates-process-to-list-major-projects-under-the-building-canada-act0.html",
             T("Government of Canada — process begun to list the first projects, 24 June 2026",
               "Gouvernement du Canada — lancement du processus d'inscription des premiers projets, 24 juin 2026")),
    out_link("https://www.pm.gc.ca/en/news/news-releases/2026/07/02/canada-and-alberta-advance-west-coast-pipeline-project-proposal-and",
             T("Prime Minister of Canada — Canada and Alberta advance the West Coast pipeline proposal, 2 July 2026",
               "Premier ministre du Canada — le Canada et l'Alberta font avancer le projet d'oléoduc de la côte Ouest, 2 juillet 2026")),
    out_link("https://www.bnnbloomberg.ca/business/politics/2026/08/04/federal-government-moves-to-list-alberta-backed-west-coast-pipeline-as-national-interest-project/",
             T("BNN Bloomberg — the federal government moves to list the West Coast pipeline, 4 August 2026",
               "BNN Bloomberg — le gouvernement fédéral entreprend d'inscrire l'oléoduc de la côte Ouest, 4 août 2026")),
    out_link("https://www.blakes.com/insights/second-tranche-of-projects-referred-to-canada-s-major-projects-office/",
             T("Blakes — second group of projects referred to the Major Projects Office",
               "Blakes — deuxième groupe de projets confiés au Bureau des grands projets")),
    out_link("https://www.blg.com/en/insights/2025/12/fast-tracking-canadas-future-recent-projects-announced-by-the-major-projects-office",
             T("BLG — recent projects announced by the Major Projects Office",
               "BLG — projets récents annoncés par le Bureau des grands projets")),
    out_link("https://www.opg.com/projects-services/projects/nuclear/smr/darlington-smr/",
             T("Ontario Power Generation — the Darlington small modular reactor project",
               "Ontario Power Generation — le projet de petit réacteur modulaire de Darlington")),
    out_link("https://www.cnsc-ccsn.gc.ca/eng/reactors/new-reactor-power-plant-projects/new-reactor-power-plant-facilities/darlington-new-nuclear-project/",
             T("Canadian Nuclear Safety Commission — the Darlington New Nuclear Project",
               "Commission canadienne de sûreté nucléaire — le projet nucléaire de Darlington")),
    out_link("https://chiefs-of-ontario.org/first-nations-leadership-united-in-opposition-to-liberal-governments-unprecedented-bill-c-5/",
             T("Chiefs of Ontario — First Nations leadership on Bill C-5, 19 June 2025",
               "Chiefs of Ontario — les dirigeants des Premières Nations sur le projet de loi C-5, 19 juin 2025")),
    out_link("https://www.cbc.ca/news/indigenous/ontario-challenge-bill-c5-9.7074134",
             T("CBC News — more First Nations join the legal challenge to Bill 5 and Bill C-5",
               "CBC News — d'autres Premières Nations se joignent à la contestation des projets de loi 5 et C-5")),
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
