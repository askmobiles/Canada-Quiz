#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article — how Canada's cities and towns actually work.

Sources: the research notes and, for everything about
census subdivision types, the research notes, which
supersedes the per-type numbers in the first file.

The finding the page is built on: nobody in Canada publishes how many
municipalities the country has. Statistics Canada publishes 5,161 census
subdivisions, its own dictionary says that unit is municipalities "or areas
treated as municipal equivalents for statistical purposes", and it classifies
those units into 57 types. At least 1,592 of the 5,161 are clearly not
municipalities. The provinces publish their own counts; twelve of them do,
Manitoba does not, and the twelve add to 3,334 — which is arithmetic, not an
official national total, and is labelled that way everywhere it appears.

Deliberately kept off the page:
  * Municipal revenue, spending, property tax shares, the education levy, the
    federal community-building fund and the infrastructure renewal gap. Cut on
    the owner's instruction — this page is about what municipalities are, how
    they are counted and how they are governed, not what they cost.
  * Any total number of Ontario strong-mayor municipalities. The increments are
    published (2, then 26, then 169); the running total is not, and the
    arithmetic 2 + 26 + 169 = 197 assumes no overlap and no double-counting of
    the two "169" announcements. The research file marks it unsafe.
  * 5,161 minus 1,592 as "the number of municipalities". The status of about
    twenty of the 57 types is not published by anyone, so that subtraction is
    meaningless and the page says so.
  * Any assertion that New Brunswick parishes ceased to be census subdivisions
    after the 2023 reform. The boundary-file series is circumstantial evidence;
    no Statistics Canada sentence says it, so the page does not either.
  * Any speculation about why the boundary-file count rose from 5,028 in 2024
    to 5,054 in 2025. Not established; listed as a thing nobody publishes.
  * Largest/smallest municipality by province for NL, PEI, NB and the three
    territories — not sourced in the research and not filled in from memory.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="how-canadas-cities-and-towns-work.html",
    section="Government",
    title=T("How Canada's Cities and Towns Work — The Numbers Nobody Publishes",
            "Comment fonctionnent les villes et villages du Canada — les chiffres que "
            "personne ne publie"),
    desc=T("Canada does not publish how many municipalities it has. What a census subdivision "
           "really is, the 57 types Statistics Canada counts, which of them are not "
           "municipalities at all, and who actually runs your town.",
           "Le Canada ne publie pas le nombre de ses municipalités. Ce qu'est vraiment une "
           "subdivision de recensement, les 57 types que compte Statistique Canada, ceux qui ne "
           "sont pas des municipalités, et qui dirige réellement votre municipalité."),
    h1=T("\U0001F3E0 How Canada's cities and towns work",
         "\U0001F3E0 Comment fonctionnent les villes et villages du Canada"),
    hero=T("Your municipality plows your street, runs your library and inspects your basement "
           "renovation. It is also the level of government Canada counts least well. Nobody "
           "publishes how many there are, and the number everyone quotes counts something else.",
           "Votre municipalité déneige votre rue, gère votre bibliothèque et inspecte vos "
           "rénovations. C'est aussi le palier de gouvernement que le Canada dénombre le moins "
           "bien. Personne n'en publie le nombre, et le chiffre que tout le monde cite compte "
           "autre chose."),
    checked=T("Last checked 27 August 2026 — every figure here carries its own source and "
              "reference year",
              "Dernière vérification le 27 août 2026 — chaque chiffre ici porte sa propre "
              "source et son année de référence"),
)

# ------------------------------------------------------------------ 1
a.h2(T("The number nobody publishes", "Le chiffre que personne ne publie"))
a.p(T(
    "Start with the simplest question anyone asks about local government: how many "
    "municipalities does Canada have? There is no official answer. No federal department, no "
    "agency and no national association publishes one. This is not an oversight that somebody "
    "will fix. It is a consequence of how the country is built: municipalities are created by "
    "provincial law, so counting them is nobody's federal job.",
    "Commençons par la question la plus simple qu'on pose sur le gouvernement local : combien "
    "le Canada compte-t-il de municipalités ? Il n'y a pas de réponse officielle. Aucun "
    "ministère fédéral, aucun organisme et aucune association nationale n'en publie une. Ce "
    "n'est pas un oubli que quelqu'un corrigera. C'est une conséquence de la façon dont le "
    "pays est bâti : les municipalités sont créées par une loi provinciale, alors les "
    "dénombrer n'est le travail d'aucune instance fédérale."))
a.p(T(
    "The number you will see quoted almost everywhere is about 5,000, and it comes from "
    "Statistics Canada. In the 2021 Census there were 5,161 census subdivisions in Canada. "
    "Statistics Canada does often call these municipalities in plain language — one of its own "
    "table titles reads \"Canada and census subdivisions (municipalities)\" — but its Census "
    "Dictionary is the authoritative text, and the dictionary says something more careful.",
    "Le nombre que vous verrez cité presque partout est d'environ 5 000, et il vient de "
    "Statistique Canada. Au Recensement de 2021, il y avait 5 161 subdivisions de recensement "
    "au Canada. Statistique Canada appelle souvent ces unités des municipalités en langage "
    "courant — le titre d'un de ses propres tableaux se lit « Canada et subdivisions de "
    "recensement (municipalités) » — mais son Dictionnaire du recensement fait foi, et le "
    "dictionnaire dit quelque chose de plus prudent."))
a.p(T(
    "The 5,161 is real, it is well documented, and it does not mean what almost everyone takes "
    "it to mean. The rest of this section is about what it actually counts, because that turns "
    "out to be the most interesting thing on the page.",
    "Le chiffre de 5 161 est réel, il est bien documenté, et il ne veut pas dire ce que presque "
    "tout le monde croit. La suite de cette section porte sur ce qu'il compte réellement, car "
    "c'est là le point le plus intéressant de cette page."))

# ------------------------------------------------------------------ 2
a.h2(T("What a census subdivision actually is",
       "Ce qu'est réellement une subdivision de recensement"))
a.p(T(
    "Statistics Canada is precise about this, and almost nobody reads the precision. Here is "
    "the definition in full, from the Census Dictionary.",
    "Statistique Canada est précis là-dessus, et presque personne ne lit cette précision. Voici "
    "la définition au complet, tirée du Dictionnaire du recensement."))
a.callout(T(
    "<strong>The definition, word for word.</strong> A census subdivision is \"the general term "
    "for municipalities (as determined by provincial/territorial legislation) or areas treated "
    "as municipal equivalents for statistical purposes (e.g. Indian reserves, Indian "
    "settlements and unorganized territories).\"",
    "<strong>La définition, mot pour mot.</strong> Une subdivision de recensement est le "
    "« terme général qui désigne les municipalités (telles qu'elles sont définies par les lois "
    "provinciales ou territoriales) ou les régions considérées comme des équivalents municipaux "
    "à des fins statistiques (par exemple, les réserves indiennes, les établissements indiens "
    "et les territoires non organisés) »."))
a.p(T(
    "Read the middle of that sentence again: municipalities, or areas treated as municipal "
    "equivalents for statistical purposes. The three examples are the dictionary's own. A "
    "census subdivision is not a synonym for a municipality. It is municipalities plus a set of "
    "statistical stand-ins, and the stand-ins are not a rounding error.",
    "Relisez le milieu de cette phrase : les municipalités, ou les régions considérées comme des "
    "équivalents municipaux à des fins statistiques. Les trois exemples sont ceux du "
    "dictionnaire lui-même. Une subdivision de recensement n'est pas un synonyme de "
    "municipalité. Ce sont les municipalités plus un ensemble de substituts statistiques, et ces "
    "substituts ne sont pas une erreur d'arrondi."))
a.p(T(
    "The same page says how many kinds there are, and the number is startling: \"Census "
    "subdivisions (CSDs) are classified into 57 types according to official designations "
    "adopted by provincial, territorial or federal authorities.\" Fifty-seven types, for one "
    "country. Two of them were not designated by any authority at all — Statistics Canada "
    "created them itself and says so, describing \"subdivision of unorganized\" in Newfoundland "
    "and Labrador and \"subdivision of county municipality\" in Nova Scotia as \"geographic "
    "areas created as equivalents for municipalities by Statistics Canada.\"",
    "La même page indique combien il existe de sortes de subdivisions, et le nombre surprend : "
    "« les subdivisions de recensement (SDR) sont classées en 57 types selon les désignations "
    "officielles adoptées par les autorités provinciales, territoriales ou fédérales ». "
    "Cinquante-sept types, pour un seul pays. Deux d'entre eux n'ont été désignés par aucune "
    "autorité — Statistique Canada les a créés lui-même et le dit, décrivant la « subdivision "
    "non organisée » de Terre-Neuve-et-Labrador et la « subdivision de municipalité de comté » "
    "de la Nouvelle-Écosse comme des « régions géographiques créées par Statistique Canada à "
    "titre d'équivalents des municipalités »."))
a.p(T(
    "Why count places that have no council at all? Because the census map has to cover every "
    "square metre of Canada without gaps, and every place has to sit inside exactly one census "
    "subdivision. Somewhere with no municipal government still has to be somewhere. That is a "
    "mapping convention, and it tells you nothing about who governs the ground.",
    "Pourquoi compter des lieux qui n'ont aucun conseil ? Parce que la carte du recensement doit "
    "couvrir chaque mètre carré du Canada sans trou, et que chaque lieu doit se trouver dans une "
    "subdivision de recensement et une seule. Un endroit sans gouvernement municipal doit quand "
    "même se trouver quelque part. C'est une convention cartographique, et elle ne dit rien de "
    "qui gouverne ce territoire."))
a.p(T(
    "Here are the types that are clearly not municipalities, with the official type code "
    "Statistics Canada uses for each one and the count from the 2021 Census.",
    "Voici les types qui ne sont manifestement pas des municipalités, avec le code de type "
    "officiel qu'emploie Statistique Canada pour chacun et le décompte du Recensement de 2021."))
a.table(
    [T("Code", "Code"),
     T("Census subdivision type", "Type de subdivision de recensement"),
     T("Census subdivisions, 2021", "Subdivisions de recensement, 2021"),
     T("What it actually is", "De quoi il s'agit réellement")],
    [[T("IRI", "IRI"),
      T("Indian reserve", "Réserve indienne"),
      T("992", "992"),
      T("Federal land set apart for the use and benefit of a First Nation. Named in the "
        "dictionary's own definition as a municipal equivalent, not a municipality.",
        "Terre fédérale mise de côté à l'usage et au profit d'une Première Nation. Nommée dans "
        "la définition même du dictionnaire comme un équivalent municipal, non comme une "
        "municipalité.")],
     [T("S-É", "S-É"),
      T("Indian settlement", "Établissement indien"),
      T("21", "21"),
      T("The second of the dictionary's three examples of an area treated as a municipal "
        "equivalent for statistical purposes.",
        "Le deuxième des trois exemples que donne le dictionnaire d'une région considérée comme "
        "un équivalent municipal à des fins statistiques.")],
     [T("NO", "NO"),
      T("Unorganized", "Non organisé"),
      T("138", "138"),
      T("Territory with no municipal government. The third example in the dictionary's own "
        "definition.",
        "Territoire sans gouvernement municipal. Le troisième exemple de la définition même du "
        "dictionnaire.")],
     [T("SNO", "SNO"),
      T("Subdivision of unorganized, Newfoundland and Labrador",
        "Subdivision de territoire non organisé, Terre-Neuve-et-Labrador"),
      T("92", "92"),
      T("Created as an equivalent for municipalities by Statistics Canada itself. No province "
        "designated it.",
        "Créée par Statistique Canada lui-même à titre d'équivalent des municipalités. Aucune "
        "province ne l'a désignée.")],
     [T("SC", "SC"),
      T("Subdivision of county municipality, Nova Scotia",
        "Subdivision de municipalité de comté, Nouvelle-Écosse"),
      T("28", "28"),
      T("The other type Statistics Canada created itself, for the same statistical reason.",
        "L'autre type que Statistique Canada a créé lui-même, pour la même raison statistique.")],
     [T("RDA", "RDA"),
      T("Regional district electoral area, British Columbia",
        "Secteur électoral de district régional, Colombie-Britannique"),
      T("160", "160"),
      T("The unincorporated rural parts of British Columbia. They elect a director to a regional "
        "district board and have no council of their own.",
        "Les parties rurales non constituées en municipalité de la Colombie-Britannique. Elles "
        "élisent un administrateur au conseil d'un district régional et n'ont pas de conseil "
        "propre.")],
     [T("P", "P"),
      T("Parish, New Brunswick", "Paroisse, Nouveau-Brunswick"),
      T("142", "142"),
      T("The territory outside any incorporated local government, as it stood for the 2021 "
        "Census. New Brunswick reorganised its local governance in 2023.",
        "Le territoire situé en dehors de tout gouvernement local constitué, tel qu'il existait "
        "au Recensement de 2021. Le Nouveau-Brunswick a réorganisé sa gouvernance locale en "
        "2023.")],
     [T("IGD", "IGD"),
      T("Indian government district", "District de gouvernement indien"),
      T("2", "2"),
      T("Indigenous government land in British Columbia.",
        "Terres de gouvernement autochtone en Colombie-Britannique.")],
     [T("TC", "TC"),
      T("Terres réservées aux Cris", "Terres réservées aux Cris"),
      T("9", "9"),
      T("Land reserved for the Cree in Quebec.", "Terres réservées aux Cris au Québec.")],
     [T("TK", "TK"),
      T("Terres réservées aux Naskapis", "Terres réservées aux Naskapis"),
      T("1", "1"),
      T("Land reserved for the Naskapi in Quebec.", "Terres réservées aux Naskapis au Québec.")],
     [T("NL", "NL"),
      T("Nisga'a land", "Terres nisga'a"),
      T("1", "1"),
      T("Territory transferred to the Nisga'a Nation under its treaty.",
        "Territoire transféré à la Nation nisga'a en vertu de son traité.")],
     [T("TWL", "TWL"),
      T("Tsawwassen Lands", "Terres tsawwassen"),
      T("1", "1"),
      T("Territory transferred to the Tsawwassen First Nation under its treaty.",
        "Territoire transféré à la Première Nation tsawwassen en vertu de son traité.")],
     [T("TAL", "TAL"),
      T("Tla'amin Lands", "Terres tla'amin"),
      T("1", "1"),
      T("Territory transferred to the Tla'amin Nation under its treaty.",
        "Territoire transféré à la Nation tla'amin en vertu de son traité.")],
     [T("SG", "SG"),
      T("Self-government, Yukon", "Autonomie gouvernementale, Yukon"),
      T("4", "4"),
      T("Land of self-governing First Nations in Yukon.",
        "Terres de Premières Nations autonomes au Yukon.")],
     [T("FD", "FD"),
      T("Fire District, Prince Edward Island",
        "District d'incendie, Île-du-Prince-Édouard"),
      T("35", "35"),
      T("Listed here because it is often assumed to be a municipality. Whether it is one is not "
        "established: no official source found for this page says either way.",
        "Inscrit ici parce qu'on le prend souvent pour une municipalité. Sa nature n'est pas "
        "établie : aucune source officielle trouvée pour cette page ne tranche la question.")]],
    label=T("Census subdivision types that are not municipalities — scroll sideways to see all "
            "of it",
            "Types de subdivisions de recensement qui ne sont pas des municipalités — faites "
            "défiler latéralement pour tout voir"))
a.callout(T(
    "<strong>A type code that trips people up.</strong> Prince Edward Island's fire districts "
    "carry the code FD. PE is a different code altogether: it is Quebec's \"Paroisse "
    "(municipalité de)\", and there were 139 of those in the 2021 Census, all in Quebec. They "
    "are a different thing entirely.",
    "<strong>Un code de type qui induit en erreur.</strong> Les districts d'incendie de "
    "l'Île-du-Prince-Édouard portent le code FD. PE est un code tout autre : il désigne la "
    "« Paroisse (municipalité de) » du Québec, dont on comptait 139 au Recensement de 2021, "
    "toutes au Québec. C'est une chose entièrement différente."))
a.p(T(
    "Add the first fourteen rows of that table together and you get 1,592 census subdivisions "
    "that are clearly not municipalities, which is about 31 per cent of the 5,161. That "
    "addition is ours, not Statistics Canada's — the agency publishes no subtotal of census "
    "subdivisions that are not municipalities. And 1,592 is a floor, not a total: the 35 fire "
    "districts are deliberately left out of it, and so is every other type whose status we could "
    "not settle from an official source.",
    "Additionnez les quatorze premières lignes de ce tableau et vous obtenez 1 592 subdivisions "
    "de recensement qui ne sont manifestement pas des municipalités, soit environ 31 pour cent "
    "des 5 161. Cette addition est la nôtre, pas celle de Statistique Canada — l'organisme ne "
    "publie aucun sous-total des subdivisions de recensement qui ne sont pas des municipalités. "
    "Et 1 592 est un plancher, pas un total : les 35 districts d'incendie en sont volontairement "
    "exclus, comme tout autre type dont nous n'avons pu établir la nature à partir d'une source "
    "officielle."))
a.p(T(
    "Now the part that matters most, and it is a warning. Do not subtract. 5,161 minus 1,592 is "
    "not the number of municipalities in Canada, and anyone who prints that difference has "
    "invented a statistic. Statistics Canada does not publish, type by type, which of its 57 "
    "types are municipalities and which are not, and for about twenty of the 57 no official "
    "source found for this page settles it either way. The honest sentence is this one: 5,161 is "
    "the number of census subdivisions, at least 1,592 of them are not municipalities, and the "
    "count you actually wanted is not published by anybody.",
    "Voici maintenant l'essentiel, et c'est une mise en garde. Ne soustrayez pas. 5 161 moins "
    "1 592 n'est pas le nombre de municipalités du Canada, et quiconque publie cette différence "
    "invente une statistique. Statistique Canada ne publie pas, type par type, lesquels de ses "
    "57 types sont des municipalités et lesquels ne le sont pas, et pour une vingtaine des 57 "
    "aucune source officielle trouvée pour cette page ne tranche la question. La phrase honnête "
    "est celle-ci : 5 161 est le nombre de subdivisions de recensement, au moins 1 592 d'entre "
    "elles ne sont pas des municipalités, et le décompte que vous cherchiez vraiment n'est "
    "publié par personne."))

# ------------------------------------------------------------------ 3
a.h2(T("Reserves are governed — just not by a municipal council",
       "Les réserves sont gouvernées — mais pas par un conseil municipal"))
a.p(T(
    "992 of the 5,161 census subdivisions are Indian reserves and another 21 are Indian "
    "settlements. That is 1,013 entries on the list, by our own addition, and it is the part "
    "most often waved away in a footnote. It deserves better than a footnote, because the reason "
    "a reserve is not a municipality has nothing to do with size or remoteness. It is governed "
    "under a different legal order.",
    "Sur les 5 161 subdivisions de recensement, 992 sont des réserves indiennes et 21 autres "
    "sont des établissements indiens. Cela fait 1 013 entrées de la liste, selon notre propre "
    "addition, et c'est la partie qu'on évacue le plus souvent en note de bas de page. Elle "
    "mérite mieux, car si une réserve n'est pas une municipalité, ce n'est ni une question de "
    "taille ni d'éloignement. Elle relève d'un ordre juridique différent."))
a.p(T(
    "They appear in the census subdivision list for the mapping reason given above: the "
    "geography has to cover all of Canada without gaps. Treating a reserve as a municipal "
    "equivalent for statistical purposes — the dictionary's own phrase — is a convention of that "
    "map and says nothing about legal status.",
    "Elles figurent dans la liste des subdivisions de recensement pour la raison cartographique "
    "déjà donnée : la géographie doit couvrir tout le Canada sans trou. Considérer une réserve "
    "comme un équivalent municipal à des fins statistiques — l'expression est celle du "
    "dictionnaire — est une convention de cette carte et ne dit rien du statut juridique."))
a.p(T(
    "They are not municipalities because they are not created by provincial or territorial "
    "municipal legislation at all. A reserve is federal land, and the federal statute that "
    "defines it is the Indian Act.",
    "Ce ne sont pas des municipalités parce qu'elles ne sont pas créées par une loi municipale "
    "provinciale ou territoriale. Une réserve est une terre fédérale, et la loi fédérale qui la "
    "définit est la Loi sur les Indiens."))
a.callout(T(
    "<strong>Indian Act, section 2, on the two words that matter.</strong> A reserve is \"a "
    "tract of land, the legal title to which is vested in Her Majesty, that has been set apart "
    "by Her Majesty for the use and benefit of a band.\" A band is a body of Indians for whose "
    "use and benefit in common such lands have been set apart, or for whom moneys are held by "
    "Her Majesty, or that has been declared a band by the Governor in Council.",
    "<strong>Loi sur les Indiens, article 2, sur les deux mots qui comptent.</strong> Une réserve "
    "est une « parcelle de terrain dont Sa Majesté est propriétaire et qu'elle a mise de côté à "
    "l'usage et au profit d'une bande ». Une bande est un groupe d'Indiens à l'usage et au "
    "profit communs desquels de telles terres ont été mises de côté, ou pour lesquels Sa Majesté "
    "détient des sommes d'argent, ou qui a été déclaré une bande par le gouverneur en conseil."))
a.p(T(
    "The government of a reserve is the chief and council of the First Nation, and Indigenous "
    "Services Canada sets out three ways a council is chosen.",
    "Le gouvernement d'une réserve est le chef et le conseil de la Première Nation, et Services "
    "aux Autochtones Canada énonce trois façons dont un conseil est choisi."))
a.ul([
    T("<strong>The Indian Act election system.</strong> Elections must be held every two years. "
      "The department says roughly 200 First Nations select their leadership this way.",
      "<strong>Le système électoral de la Loi sur les Indiens.</strong> Les élections doivent "
      "avoir lieu tous les deux ans. Le ministère indique qu'environ 200 Premières Nations "
      "choisissent ainsi leurs dirigeants."),
    T("<strong>Community or custom leadership selection.</strong> The rules are set by the First "
      "Nation itself, and the department notes that they are often documented in a community's "
      "election code.",
      "<strong>La sélection communautaire ou coutumière des dirigeants.</strong> Les règles sont "
      "fixées par la Première Nation elle-même, et le ministère précise qu'elles sont souvent "
      "consignées dans le code électoral de la communauté."),
    T("<strong>The First Nations Elections Act.</strong> This one is opt-in: a council can "
      "request to come under the act by adopting a band council resolution, and terms are four "
      "years.",
      "<strong>La Loi sur les élections au sein de premières nations.</strong> Celle-ci est "
      "facultative : un conseil peut demander d'y être assujetti en adoptant une résolution de "
      "conseil de bande, et les mandats sont de quatre ans."),
])
a.p(T(
    "A self-government agreement is a different and stronger arrangement again. A comparison "
    "published by Crown-Indigenous Relations and Northern Affairs Canada, on a page dated 2010, "
    "states the contrast plainly. Under the Indian Act, in its words, the band government is "
    "accountable to the Minister, core funding for the band is determined by the department, and "
    "land provided for the use and benefit of the band cannot be owned by the band or by "
    "individual members. A self-governing First Nation, again in its words, sets its own "
    "priorities with an election process defined by its Constitution, owns and manages its own "
    "land, and has the ability to tax its citizens and other residents.",
    "Une entente d'autonomie gouvernementale est un arrangement encore différent et plus fort. "
    "Une comparaison publiée par Relations Couronne-Autochtones et Affaires du Nord Canada, sur "
    "une page datée de 2010, énonce clairement le contraste. Sous le régime de la Loi sur les "
    "Indiens, selon ses termes, le gouvernement de la bande rend des comptes au ministre, le "
    "financement de base de la bande est déterminé par le ministère, et les terres fournies à "
    "l'usage et au profit de la bande ne peuvent appartenir ni à la bande ni à ses membres. Une "
    "Première Nation autonome, toujours selon ses termes, fixe ses propres priorités avec un "
    "processus électoral défini par sa Constitution, possède et gère ses propres terres, et a la "
    "capacité de taxer ses citoyens et les autres résidents."))
a.p(T(
    "So reserves and treaty lands appear in the census subdivision list because the map needs "
    "them there. The governments on them are First Nation governments, on a nation-to-nation "
    "footing with Canada, and not units of any province's municipal system. The same is true of "
    "the smaller types in the table above: Nisga'a land, Tsawwassen Lands, Tla'amin Lands, the "
    "Cree and Naskapi reserved lands in Quebec, and the four self-government census subdivisions "
    "in Yukon.",
    "Les réserves et les terres visées par des traités figurent donc dans la liste des "
    "subdivisions de recensement parce que la carte en a besoin. Les gouvernements qui s'y "
    "trouvent sont des gouvernements de Premières Nations, sur une base de nation à nation avec "
    "le Canada, et non des unités du système municipal d'une province. Il en va de même des "
    "types plus petits du tableau ci-dessus : les terres nisga'a, les terres tsawwassen, les "
    "terres tla'amin, les terres réservées aux Cris et aux Naskapis au Québec, et les quatre "
    "subdivisions de recensement d'autonomie gouvernementale du Yukon."))

# ------------------------------------------------------------------ 4
a.h2(T("Two more that are not municipalities",
       "Deux autres cas qui ne sont pas des municipalités"))
a.h3(T("New Brunswick parishes, and the date that matters",
       "Les paroisses du Nouveau-Brunswick, et la date qui compte"))
a.p(T(
    "In the 2021 Census there were 142 New Brunswick parishes counted as census subdivisions. "
    "They were not municipalities: a parish was the territory outside any incorporated local "
    "government. The figure belongs to the 2021 Census, whose boundaries are those in force on 1 "
    "January 2021, and that date is the whole point, because New Brunswick's local governance "
    "reform took effect on 1 January 2023 — two years after the census these numbers come from. "
    "Since the reform the province describes its structure as 77 local governments, 12 rural "
    "districts and an expanded mandate for regional service commissions, with one rural district "
    "in each of the province's 12 regions.",
    "Au Recensement de 2021, 142 paroisses du Nouveau-Brunswick étaient comptées comme "
    "subdivisions de recensement. Ce n'étaient pas des municipalités : une paroisse était le "
    "territoire situé en dehors de tout gouvernement local constitué. Le chiffre appartient au "
    "Recensement de 2021, dont les limites sont celles en vigueur le 1er janvier 2021, et cette "
    "date est tout l'enjeu, car la réforme de la gouvernance locale du Nouveau-Brunswick est "
    "entrée en vigueur le 1er janvier 2023 — deux ans après le recensement d'où viennent ces "
    "chiffres. Depuis la réforme, la province décrit sa structure comme 77 gouvernements locaux, "
    "12 districts ruraux et un mandat élargi pour les commissions de services régionaux, avec un "
    "district rural dans chacune des 12 régions de la province."))
a.p(T(
    "What we are not going to tell you is whether parishes are still census subdivisions today. "
    "Statistics Canada's annual boundary file count fell from 5,173 to 5,028 in the edition that "
    "first incorporated the New Brunswick changes, and that edition says so in a note. That is "
    "circumstantial and the direction is obvious, but no Statistics Canada sentence we found "
    "says that New Brunswick parishes ceased to be census subdivisions, so this page does not "
    "say it either.",
    "Ce que nous n'allons pas vous dire, c'est si les paroisses sont encore aujourd'hui des "
    "subdivisions de recensement. Le décompte du fichier annuel des limites de Statistique "
    "Canada est passé de 5 173 à 5 028 dans l'édition qui a intégré pour la première fois les "
    "changements du Nouveau-Brunswick, et cette édition le mentionne dans une note. C'est "
    "circonstanciel et la direction est évidente, mais aucune phrase de Statistique Canada que "
    "nous avons trouvée n'affirme que les paroisses du Nouveau-Brunswick ont cessé d'être des "
    "subdivisions de recensement, alors cette page ne l'affirme pas non plus."))
a.h3(T("British Columbia's regional district electoral areas",
       "Les secteurs électoraux des districts régionaux de la Colombie-Britannique"))
a.p(T(
    "A regional district electoral area is the rural, unincorporated part of British Columbia — "
    "land that is not inside any city, town, village or district municipality. There are 160 of "
    "them and they have no council of their own. Residents instead elect a single director, for "
    "a four-year term, to sit on the board of one of the province's 27 regional districts, and "
    "the regional district provides local services such as waterworks and fire protection to the "
    "unincorporated communities inside those areas. That unincorporated status is exactly why "
    "the 160 are census subdivisions and are not municipalities.",
    "Un secteur électoral de district régional est la partie rurale et non constituée en "
    "municipalité de la Colombie-Britannique — un territoire qui ne fait partie d'aucune cité, "
    "ville, village ni municipalité de district. Il y en a 160 et ils n'ont pas de conseil "
    "propre. Les résidents élisent plutôt un seul administrateur, pour un mandat de quatre ans, "
    "qui siège au conseil de l'un des 27 districts régionaux de la province, et le district "
    "régional fournit des services locaux comme l'aqueduc et la protection contre les incendies "
    "aux collectivités non constituées de ces secteurs. C'est précisément ce statut non "
    "constitué qui explique que les 160 soient des subdivisions de recensement sans être des "
    "municipalités."))

# ------------------------------------------------------------------ 5
a.h2(T("There is a newer number, and it is not the same number",
       "Il existe un chiffre plus récent, et ce n'est pas le même"))
a.p(T(
    "Separately from the census, Statistics Canada publishes an annual Census Subdivision "
    "Boundary File with a current count. The most recent edition states it plainly: the 2025 "
    "file \"portrays the boundaries of all 5,054 CSDs (census subdivisions), which combined, "
    "cover all of Canada\", with a geographic reference date of 1 January 2025.",
    "Indépendamment du recensement, Statistique Canada publie un fichier annuel des limites des "
    "subdivisions de recensement accompagné d'un décompte à jour. L'édition la plus récente le "
    "dit clairement : le fichier de 2025 « représente les limites de l'ensemble des 5 054 SDR "
    "(subdivisions de recensement) qui, réunies, couvrent tout le Canada », avec une date de "
    "référence géographique au 1er janvier 2025."))
a.p(T(
    "The series runs 5,173 census subdivisions as of 1 January 2023, 5,028 as of 1 January 2024, "
    "and 5,054 as of 1 January 2025. This is a different product from the census, with a "
    "different reference date, and the two must not be blurred together. Why the count rose by "
    "26 between the 2024 and 2025 editions is not explained in the guides, and we are not going "
    "to guess.",
    "La série indique 5 173 subdivisions de recensement au 1er janvier 2023, 5 028 au 1er "
    "janvier 2024 et 5 054 au 1er janvier 2025. Il s'agit d'un produit différent du recensement, "
    "avec une date de référence différente, et il ne faut pas confondre les deux. La raison pour "
    "laquelle le décompte a augmenté de 26 entre les éditions de 2024 et de 2025 n'est pas "
    "expliquée dans les guides, et nous n'allons pas la deviner."))
a.p(T(
    "As for the census itself, the 2026 Census was collected — collection began on 4 May 2026 — "
    "but nothing from it has been published. Statistics Canada's release schedule puts the 2026 "
    "geographic and reference products on 18 November 2026 and the population and dwelling "
    "counts on 10 February 2027. Until then, 5,161 remains the current census figure, and any "
    "page quoting a 2026 census subdivision count today is quoting something that does not exist "
    "yet.",
    "Quant au recensement lui-même, le Recensement de 2026 a été mené — la collecte a commencé "
    "le 4 mai 2026 — mais rien n'en a été publié. Le calendrier de diffusion de Statistique "
    "Canada fixe les produits géographiques et de référence de 2026 au 18 novembre 2026, et les "
    "chiffres de population et des logements au 10 février 2027. D'ici là, 5 161 demeure le "
    "chiffre courant du recensement, et toute page qui cite aujourd'hui un décompte de "
    "subdivisions de recensement de 2026 cite quelque chose qui n'existe pas encore."))

# ------------------------------------------------------------------ 6
a.h2(T("What each province says, and what the census counted",
       "Ce que dit chaque province, et ce qu'a compté le recensement"))
a.p(T(
    "The other way to count is to ask each province what it says. Twelve of the thirteen "
    "provinces and territories publish a count. Add those twelve together and you get 3,334. "
    "That number is arithmetic done here, on twelve official figures that use twelve different "
    "definitions and reference years between 2021 and 2026. It is a sum of provincial figures, "
    "not an official Canadian total, and it is incomplete, because Manitoba publishes no count "
    "at all.",
    "L'autre façon de compter est de demander à chaque province ce qu'elle dit. Douze des "
    "treize provinces et territoires publient un décompte. Additionnez ces douze chiffres et "
    "vous obtenez 3 334. Ce nombre est une addition faite ici, à partir de douze chiffres "
    "officiels qui reposent sur douze définitions différentes et sur des années de référence "
    "allant de 2021 à 2026. C'est une somme de chiffres provinciaux, pas un total canadien "
    "officiel, et elle est incomplète, parce que le Manitoba ne publie aucun décompte."))
a.p(T(
    "Manitoba is worth pausing on, because the silence is thorough. Its Municipal and Northern "
    "Relations department publishes a Municipal Officials Directory that lists every "
    "municipality one by one and states no total. Its annual report, its amalgamation page, its "
    "geoportal dataset and the provincial municipal association's directory all do the same. "
    "The only municipal-adjacent number Manitoba publishes is 48 Northern Affairs Communities, "
    "which are not municipalities.",
    "Le Manitoba mérite qu'on s'y arrête, car le silence y est complet. Son ministère des "
    "Relations avec les municipalités et le Nord publie un répertoire des élus municipaux qui "
    "énumère chaque municipalité une par une sans donner de total. Son rapport annuel, sa page "
    "sur les fusions, son jeu de données géospatiales et le répertoire de l'association "
    "municipale provinciale font tous de même. Le seul chiffre voisin que publie le Manitoba "
    "est celui de 48 collectivités des Affaires du Nord, qui ne sont pas des municipalités."))
a.p(T(
    "Two columns below, deliberately. The left is what the province itself publishes about its "
    "own municipalities. The right is what Statistics Canada counted as census subdivisions in "
    "the 2021 Census. They do not match anywhere in the country, and the gap is the whole story.",
    "Deux colonnes ci-dessous, délibérément. À gauche, ce que la province publie elle-même au "
    "sujet de ses propres municipalités. À droite, ce que Statistique Canada a compté comme "
    "subdivisions de recensement au Recensement de 2021. Les deux ne concordent nulle part au "
    "pays, et cet écart est toute l'histoire."))
a.table(
    [T("Province or territory", "Province ou territoire"),
     T("The province's own count", "Le décompte de la province elle-même"),
     T("Date of that figure", "Date de ce chiffre"),
     T("Census subdivisions, 2021", "Subdivisions de recensement, 2021")],
    [[T("Newfoundland and Labrador", "Terre-Neuve-et-Labrador"),
      T("275 municipalities", "275 municipalités"),
      T("Municipal Council Handbook, 2021", "Guide du conseil municipal, 2021"),
      T("372", "372")],
     [T("Prince Edward Island", "Île-du-Prince-Édouard"),
      T("57 municipalities — 2 cities, 10 towns, 45 rural municipalities",
        "57 municipalités — 2 cités, 10 villes, 45 municipalités rurales"),
      T("No date shown, retrieved August 2026",
        "Aucune date affichée, consulté en août 2026"),
      T("98", "98")],
     [T("Nova Scotia", "Nouvelle-Écosse"),
      T("49 municipalities, plus 21 villages that are not municipalities",
        "49 municipalités, plus 21 villages qui ne sont pas des municipalités"),
      T("Guide for New Municipal Councillors, November 2024",
        "Guide des nouveaux conseillers municipaux, novembre 2024"),
      T("95", "95")],
     [T("New Brunswick", "Nouveau-Brunswick"),
      T("77 local governments and 12 rural districts",
        "77 gouvernements locaux et 12 districts ruraux"),
      T("Structure in force 1 January 2023", "Structure en vigueur le 1er janvier 2023"),
      T("266 — 2021 boundaries, before the reform",
        "266 — limites de 2021, avant la réforme")],
     [T("Quebec", "Québec"),
      T("1,122 local municipalities", "1 122 municipalités locales"),
      T("Municipal organisation in Quebec, February 2026",
        "L'organisation municipale au Québec, février 2026"),
      T("1,282", "1 282")],
     [T("Ontario", "Ontario"),
      T("444 municipalities", "444 municipalités"),
      T("Updated 10 July 2025", "Mise à jour le 10 juillet 2025"),
      T("577", "577")],
     [T("Manitoba", "Manitoba"),
      T("Not published", "Non publié"),
      T("Checked across seven official sources, August 2026",
        "Vérifié auprès de sept sources officielles, août 2026"),
      T("239", "239")],
     [T("Saskatchewan", "Saskatchewan"),
      T("761 municipalities — 440 urban, 296 rural, 25 northern",
        "761 municipalités — 440 urbaines, 296 rurales, 25 nordiques"),
      T("No date shown, retrieved August 2026",
        "Aucune date affichée, consulté en août 2026"),
      T("951", "951")],
     [T("Alberta", "Alberta"),
      T("No single total published; the per-type counts add to 322",
        "Aucun total unique publié ; les décomptes par type totalisent 322"),
      T("Page metadata 27 July 2026", "Métadonnées de la page, 27 juillet 2026"),
      T("423", "423")],
     [T("British Columbia", "Colombie-Britannique"),
      T("161 municipalities and 27 regional districts",
        "161 municipalités et 27 districts régionaux"),
      T("Updated 1 May 2025", "Mise à jour le 1er mai 2025"),
      T("751", "751")],
     [T("Yukon", "Yukon"),
      T("8 municipalities", "8 municipalités"),
      T("News release, 14 April 2026", "Communiqué, 14 avril 2026"),
      T("35", "35")],
     [T("Northwest Territories", "Territoires du Nord-Ouest"),
      T("33 communities of all kinds", "33 collectivités de tous types"),
      T("No date shown, retrieved August 2026",
        "Aucune date affichée, consulté en août 2026"),
      T("41", "41")],
     [T("Nunavut", "Nunavut"),
      T("25 — 24 hamlets and 1 city", "25 — 24 hameaux et 1 cité"),
      T("Government business plan, May 2026",
        "Plan d'activités du gouvernement, mai 2026"),
      T("31", "31")],
     [T("Canada", "Canada"),
      T("No official total. The twelve published counts add to 3,334 — a sum, not an official "
        "figure",
        "Aucun total officiel. Les douze décomptes publiés totalisent 3 334 — une somme, pas "
        "un chiffre officiel"),
      T("Mixed, 2021 to 2026", "Variable, de 2021 à 2026"),
      T("5,161", "5 161")]],
    label=T("Municipal counts by province and territory — scroll sideways to see all of it",
            "Décomptes municipaux par province et territoire — faites défiler latéralement "
            "pour tout voir"))
a.p(T(
    "Four rows need a word of warning. New Brunswick rebuilt its entire local government "
    "structure on 1 January 2023, so the 2021 census figure of 266 describes a world that no "
    "longer exists. Alberta's 322 is itself a sum of the province's own per-type counts, not a "
    "figure Alberta publishes as a total. The Northwest Territories figure of 33 comes from the "
    "territorial department, while the NWT Association of Communities lists structures that add "
    "to 32 — one short, and neither source explains the difference. And Manitoba's row is "
    "simply empty, which is a finding rather than a gap.",
    "Quatre lignes méritent une mise en garde. Le Nouveau-Brunswick a refait toute sa "
    "structure de gouvernement local le 1er janvier 2023, si bien que le chiffre de 266 du "
    "recensement de 2021 décrit un monde qui n'existe plus. Le 322 de l'Alberta est lui-même "
    "une somme des décomptes par type publiés par la province, et non un total que l'Alberta "
    "publie. Le chiffre de 33 pour les Territoires du Nord-Ouest vient du ministère "
    "territorial, alors que l'Association des collectivités des T.N.-O. énumère des structures "
    "qui totalisent 32 — une de moins, et ni l'une ni l'autre source n'explique l'écart. Quant "
    "à la ligne du Manitoba, elle est tout simplement vide, ce qui est un constat et non une "
    "lacune."))
a.p(T(
    "The honest sentence is this. Under provincial definitions the real number is somewhere a "
    "little over 3,000 — but no government in Canada publishes that total, because no "
    "government is responsible for it.",
    "La phrase honnête est celle-ci. Selon les définitions provinciales, le nombre réel se "
    "situe un peu au-dessus de 3 000 — mais aucun gouvernement au Canada ne publie ce total, "
    "parce qu'aucun gouvernement n'en est responsable."))

# ------------------------------------------------------------------ 7
a.h2(T("Creatures of the province", "Des créatures de la province"))
a.p(T(
    "All of this follows from one constitutional fact. Municipalities are creatures of the "
    "province, and the federal government says so itself, in unusually plain language: municipal "
    "government is not a constitutional order of government, and municipalities are established "
    "by the provincial legislatures which delegate some of their powers to municipal governments.",
    "Tout cela découle d'un seul fait constitutionnel. Les municipalités sont des créatures de "
    "la province, et le gouvernement fédéral le dit lui-même, en des termes remarquablement "
    "simples : le gouvernement municipal n'est pas un ordre constitutionnel de gouvernement, et "
    "les municipalités sont créées par les législatures provinciales, qui leur délèguent "
    "certains de leurs pouvoirs."))
a.callout(T(
    "<strong>Constitution Act, 1867, section 92(8), in full:</strong> \"Municipal Institutions "
    "in the Province.\" Six words. That is the entire constitutional basis of every city hall "
    "in Canada.",
    "<strong>Loi constitutionnelle de 1867, paragraphe 92(8), au complet :</strong> « Les "
    "institutions municipales dans la province. » Sept mots. C'est là tout le fondement "
    "constitutionnel de chaque hôtel de ville au Canada."))
a.p(T(
    "That is why there is no federal count, and it is also why there are 57 census subdivision "
    "types. Each province and territory names and shapes its own municipal forms, and none of "
    "them ever had to agree with the others.",
    "Voilà pourquoi il n'existe aucun décompte fédéral, et voilà aussi pourquoi il existe 57 "
    "types de subdivisions de recensement. Chaque province et territoire nomme et façonne ses "
    "propres formes municipales, et aucun n'a jamais eu à s'entendre avec les autres."))

# ------------------------------------------------------------------ 8
a.h2(T("The same word means different things in different provinces",
       "Le même mot ne veut pas dire la même chose d'une province à l'autre"))
a.p(T(
    "This is the single most useful thing to understand about Canadian local government. There "
    "is no national vocabulary. A city in Saskatchewan can be smaller than a village in "
    "Ontario. The word tells you which provincial statute applies, not how big the place is or "
    "what it does.",
    "C'est la chose la plus utile à comprendre au sujet du gouvernement local canadien. Il "
    "n'existe pas de vocabulaire national. Une cité en Saskatchewan peut être plus petite "
    "qu'un village en Ontario. Le mot vous dit quelle loi provinciale s'applique, non la "
    "taille de l'endroit ni ce qu'il fait."))
a.ul([
    T("<strong>Township</strong> is an Ontario word. British Columbia has a Township of "
      "Langley, but the province states plainly that it is legally a district municipality.",
      "<strong>Canton (township)</strong> est un mot ontarien. La Colombie-Britannique a un "
      "Township of Langley, mais la province indique clairement qu'il s'agit en droit d'une "
      "municipalité de district."),
    T("<strong>Rural municipality</strong> is a Prairie word. Saskatchewan has 296 of them and "
      "Manitoba uses the term too; no Atlantic province does.",
      "<strong>Municipalité rurale</strong> est un mot des Prairies. La Saskatchewan en compte "
      "296 et le Manitoba emploie aussi le terme ; aucune province de l'Atlantique ne le fait."),
    T("<strong>County</strong> means opposite things in two provinces. A Nova Scotia county "
      "municipality is an ordinary municipality with a council. An Ontario county is an upper "
      "tier sitting above other municipalities.",
      "<strong>Comté</strong> désigne des choses opposées dans deux provinces. Une "
      "municipalité de comté en Nouvelle-Écosse est une municipalité ordinaire dotée d'un "
      "conseil. Un comté ontarien est un palier supérieur qui chapeaute d'autres "
      "municipalités."),
    T("<strong>District municipality</strong> in British Columbia is an ordinary municipality "
      "that happens to cover a lot of ground. It is not a district in the Ontario sense.",
      "<strong>Municipalité de district</strong> en Colombie-Britannique est une municipalité "
      "ordinaire qui couvre simplement un grand territoire. Ce n'est pas un district au sens "
      "ontarien."),
    T("<strong>Resort village and northern hamlet</strong> exist in Saskatchewan and nowhere "
      "else. Alberta has summer villages, which no other province has either.",
      "<strong>Village de villégiature et hameau nordique</strong> existent en Saskatchewan et "
      "nulle part ailleurs. L'Alberta a des villages d'été, qu'aucune autre province n'a non "
      "plus."),
    T("<strong>Local government</strong> is what New Brunswick calls its municipalities since "
      "the 2023 reform. The province does not use the word municipality for them any more.",
      "<strong>Gouvernement local</strong> est le nom que le Nouveau-Brunswick donne à ses "
      "municipalités depuis la réforme de 2023. La province n'emploie plus le mot municipalité "
      "pour les désigner."),
])
a.p(T(
    "Above the municipality, the picture is just as uneven. Canada has no uniform second tier. "
    "Ontario has upper-tier counties, united counties and regional municipalities, and the "
    "province states that all municipalities in northern Ontario are single-tier. Quebec's "
    "upper tier is the regional county municipality, the MRC, and there are 87 of them, plus 11 "
    "agglomerations and 2 metropolitan communities. British Columbia has 27 regional districts, "
    "which are unusual in that a regional district is a federation of its member "
    "municipalities, electoral areas and in some cases Treaty First Nations, each with a seat "
    "on the board. Every other province and territory has no upper-tier municipal government at "
    "all.",
    "Au-dessus de la municipalité, le portrait est tout aussi inégal. Le Canada n'a pas de "
    "deuxième palier uniforme. L'Ontario a des comtés, des comtés unis et des municipalités "
    "régionales de palier supérieur, et la province précise que toutes les municipalités du "
    "Nord ontarien sont à palier unique. Au Québec, le palier supérieur est la municipalité "
    "régionale de comté, la MRC, et il y en a 87, en plus de 11 agglomérations et de 2 "
    "communautés métropolitaines. La Colombie-Britannique compte 27 districts régionaux, "
    "singuliers en ceci qu'un district régional est une fédération de ses municipalités "
    "membres, de ses secteurs électoraux et, dans certains cas, de Premières Nations "
    "signataires de traités, chacun ayant un siège au conseil. Toutes les autres provinces et "
    "tous les autres territoires n'ont aucun gouvernement municipal de palier supérieur."))
a.callout(T(
    "<strong>Census divisions are not regional governments.</strong> Canada had 293 census "
    "divisions in the 2021 Census. In Quebec, Ontario and British Columbia they largely line up "
    "with real upper-tier governments. In Newfoundland, Manitoba, Saskatchewan and Alberta they "
    "are statistical constructs with no government attached at all.",
    "<strong>Les divisions de recensement ne sont pas des gouvernements régionaux.</strong> Le "
    "Canada comptait 293 divisions de recensement au Recensement de 2021. Au Québec, en "
    "Ontario et en Colombie-Britannique, elles correspondent en grande partie à de véritables "
    "gouvernements de palier supérieur. À Terre-Neuve, au Manitoba, en Saskatchewan et en "
    "Alberta, ce sont des constructions statistiques auxquelles aucun gouvernement n'est "
    "rattaché."))

# ------------------------------------------------------------------ 9
a.h2(T("Mayors — nobody counts them either",
       "Les maires — personne ne les compte non plus"))
a.p(T(
    "There is no official national count of Canadian mayors. Statistics Canada does not collect "
    "counts of elected municipal officials by title. Elections Canada has no municipal role. "
    "The Federation of Canadian Municipalities, the closest thing to a national municipal body, "
    "publishes only its own membership — almost 2,000 municipalities, which it says represent "
    "more than 90 percent of all Canadians — and does not count mayors.",
    "Il n'existe aucun décompte national officiel des maires canadiens. Statistique Canada ne "
    "recueille pas de décomptes d'élus municipaux par titre. Élections Canada n'a aucun rôle "
    "municipal. La Fédération canadienne des municipalités, ce qui se rapproche le plus d'un "
    "organisme municipal national, ne publie que son propre effectif — près de 2 000 "
    "municipalités, qui représentent selon elle plus de 90 pour cent de tous les Canadiens — "
    "et ne compte pas les maires."))
a.p(T(
    "One government in Canada does publish a hard number, and it is Quebec, because Quebec is "
    "the only province whose municipal elections are administered through a provincial "
    "ministry. For the general municipal elections of 2 November 2025 the ministry reported "
    "1,091 mayoral positions, 6,795 councillor positions, 21 regional county municipality "
    "prefects elected by universal suffrage, and 7,907 elective positions in total. It also "
    "reported that 568 mayors and 4,039 councillors were elected without opposition — 4,607 "
    "acclamations.",
    "Un seul gouvernement au Canada publie un chiffre ferme, et c'est le Québec, parce que "
    "c'est la seule province dont les élections municipales sont administrées par un ministère "
    "provincial. Pour les élections générales municipales du 2 novembre 2025, le ministère a "
    "fait état de 1 091 postes de maire, de 6 795 postes de conseiller, de 21 préfets de "
    "municipalité régionale de comté élus au suffrage universel et de 7 907 postes électifs au "
    "total. Il a aussi rapporté que 568 maires et 4 039 conseillers ont été élus sans "
    "opposition — 4 607 élections par acclamation."))
a.p(T(
    "Note that 1,091 is smaller than Quebec's 1,122 local municipalities, because the northern, "
    "Cree and Naskapi villages and some municipalities under particular regimes do not vote in "
    "the general municipal elections.",
    "Notez que 1 091 est inférieur aux 1 122 municipalités locales du Québec, parce que les "
    "villages nordiques, cris et naskapi ainsi que certaines municipalités à régime "
    "particulier ne votent pas aux élections générales municipales."))
a.p(T(
    "The other reason no one can produce a national figure is that the head of a Canadian "
    "council is not always called a mayor. Nova Scotia's own guide explains the difference "
    "plainly: a warden has a similar position to a mayor but is elected to the position by "
    "fellow councillors instead of directly by the voters. Rural municipalities in Manitoba, "
    "Saskatchewan and Alberta are headed by a reeve. Ontario upper-tier councils are headed by a "
    "warden or a chair. British Columbia regional district boards have a chair. Several "
    "Northwest Territories communities are headed by a chief. Quebec MRCs have a prefect. "
    "Alberta says its chief elected official can be a mayor, a reeve or an improvement district "
    "chairperson.",
    "L'autre raison pour laquelle personne ne peut produire un chiffre national, c'est que la "
    "personne qui dirige un conseil canadien ne s'appelle pas toujours maire. Le guide de la "
    "Nouvelle-Écosse explique clairement la différence : un préfet occupe une position "
    "semblable à celle d'un maire, mais il est élu à ce poste par ses collègues conseillers "
    "plutôt que directement par les électeurs. Les municipalités rurales du Manitoba, de la "
    "Saskatchewan et de l'Alberta sont dirigées par un reeve. Les conseils de palier supérieur "
    "de l'Ontario sont dirigés par un warden ou un président. Les conseils de districts "
    "régionaux de la Colombie-Britannique ont un président. Plusieurs collectivités des "
    "Territoires du Nord-Ouest sont dirigées par un chef. Les MRC du Québec ont un préfet. "
    "L'Alberta indique que son premier élu peut être un maire, un reeve ou un président de "
    "district d'amélioration."))
a.p(T(
    "So the best that can honestly be said is this: most of Canada's roughly 3,300-plus "
    "municipalities are headed by someone titled mayor, but several hundred are headed by a "
    "reeve, a warden, a chair or a chief instead, and the split is published for exactly one "
    "province.",
    "Le mieux qu'on puisse dire honnêtement est ceci : la plupart des quelque 3 300 et plus "
    "municipalités du Canada sont dirigées par une personne portant le titre de maire, mais "
    "plusieurs centaines le sont par un reeve, un warden, un président ou un chef, et la "
    "répartition n'est publiée que pour une seule province."))

# ------------------------------------------------------------------ 10
a.h2(T("Amalgamation — how the map was redrawn",
       "Les fusions — comment la carte a été redessinée"))
a.p(T(
    "Canada has spent thirty years merging municipalities together, and two provinces did it on "
    "a scale that changed the map. If you are wondering why the counts above look unstable, this "
    "is a large part of the answer.",
    "Le Canada a passé trente ans à fusionner des municipalités, et deux provinces l'ont fait à "
    "une échelle qui a changé la carte. Si vous vous demandez pourquoi les décomptes ci-dessus "
    "paraissent instables, c'est en grande partie l'explication."))
a.ul([
    T("<strong>Ontario went from 815 municipalities to 445 between 1996 and 2004</strong>, a "
      "reduction of more than 40 per cent, and to 444 in January 2009. That era created the "
      "City of Toronto in 1998, and Ottawa, Hamilton, Greater Sudbury, Chatham-Kent, Kawartha "
      "Lakes, Haldimand and Norfolk.",
      "<strong>L'Ontario est passé de 815 municipalités à 445 entre 1996 et 2004</strong>, une "
      "réduction de plus de 40 pour cent, puis à 444 en janvier 2009. Cette époque a créé la "
      "Ville de Toronto en 1998, ainsi qu'Ottawa, Hamilton, le Grand Sudbury, Chatham-Kent, "
      "Kawartha Lakes, Haldimand et Norfolk."),
    T("<strong>New Brunswick collapsed 340 entities into 89 on 1 January 2023.</strong> Before "
      "the reform the province had 104 local governments and 236 local service districts, which "
      "its own green paper described as 340 entities to govern fewer than 800,000 people. After "
      "it: 77 local governments and 12 rural districts, with 12 regional service commissions "
      "delivering shared services.",
      "<strong>Le Nouveau-Brunswick a ramené 340 entités à 89 le 1er janvier 2023.</strong> "
      "Avant la réforme, la province comptait 104 gouvernements locaux et 236 districts de "
      "services locaux, ce que son propre livre vert décrivait comme 340 entités pour "
      "gouverner moins de 800 000 personnes. Après : 77 gouvernements locaux et 12 districts "
      "ruraux, avec 12 commissions de services régionaux qui offrent des services partagés."),
])
a.p(T(
    "Ontario's own restructuring page is worth reading for what it does not claim. The stated "
    "reasons for restructuring are to accommodate future growth, to combine resources and build "
    "capacity, and to realign a boundary. New Brunswick's reform is recent enough that no "
    "outcome evaluation of it exists yet.",
    "La page ontarienne sur la restructuration vaut le détour pour ce qu'elle ne prétend pas. "
    "Les raisons invoquées pour restructurer sont d'accueillir la croissance future, de "
    "regrouper les ressources et de bâtir des capacités, et de redéfinir une limite. La réforme "
    "du Nouveau-Brunswick est assez récente pour qu'aucune évaluation de ses résultats n'existe "
    "encore."))

# ------------------------------------------------------------------ 11
a.h2(T("Terms and elections", "Mandats et élections"))
a.p(T(
    "Municipal terms and election dates are set province by province, and the pattern has mostly "
    "converged on four-year terms and a fixed date — but not everywhere, and not always.",
    "Les mandats municipaux et les dates d'élection sont fixés province par province, et le "
    "modèle a largement convergé vers des mandats de quatre ans à date fixe — mais pas partout, "
    "et pas depuis toujours."))
a.p(T(
    "The fixed dates differ. Nova Scotia votes on the third Saturday in October, British "
    "Columbia on the third Saturday in October as well, Ontario on the fourth Monday in "
    "October, Manitoba on the fourth Wednesday in October, and Quebec on the first Sunday in "
    "November. Saskatchewan is more complicated than a single date: general elections for each "
    "office are held every four years, but rural municipalities elect selected divisions every "
    "two years while each member still serves a four-year term. New Brunswick's local "
    "governments and rural districts voted on 11 May 2026, nowhere near the autumn.",
    "Les dates fixes diffèrent. La Nouvelle-Écosse vote le troisième samedi d'octobre, la "
    "Colombie-Britannique le troisième samedi d'octobre elle aussi, l'Ontario le quatrième "
    "lundi d'octobre, le Manitoba le quatrième mercredi d'octobre, et le Québec le premier "
    "dimanche de novembre. La Saskatchewan est plus complexe qu'une date unique : les élections "
    "générales pour chaque poste ont lieu tous les quatre ans, mais les municipalités rurales "
    "élisent certaines divisions tous les deux ans alors que chaque membre siège quand même "
    "quatre ans. Les gouvernements locaux et les districts ruraux du Nouveau-Brunswick ont voté "
    "le 11 mai 2026, loin de l'automne."))
a.p(T(
    "Two places deserve to be named, because a table that reads \"four years, October, "
    "everywhere\" is wrong about both.",
    "Deux endroits méritent d'être nommés, parce qu'un tableau qui dirait « quatre ans, "
    "octobre, partout » serait faux dans les deux cas."))
a.ul([
    T("<strong>Yukon moved from three-year terms to four-year terms.</strong> Municipal and "
      "local advisory council elections are now held every four years. The 2021 election was "
      "under the old three-year term; October 2024 was the first election of the four-year era. "
      "The territory consulted first, and reported that 62.4 per cent of the 149 respondents "
      "supported a four-year term while 34.2 per cent did not.",
      "<strong>Le Yukon est passé de mandats de trois ans à des mandats de quatre ans.</strong> "
      "Les élections municipales et celles des conseils consultatifs locaux ont désormais lieu "
      "tous les quatre ans. L'élection de 2021 s'est tenue sous l'ancien mandat de trois ans ; "
      "celle d'octobre 2024 a été la première de l'ère des quatre ans. Le territoire a d'abord "
      "consulté et a rapporté que 62,4 pour cent des 149 répondants appuyaient un mandat de "
      "quatre ans tandis que 34,2 pour cent s'y opposaient."),
    T("<strong>The Northwest Territories has no common term length and no common election "
      "day.</strong> Terms run two, three or four years depending on which statute governs the "
      "community: Tlicho community governments serve four years, while charter communities and "
      "hamlets serve two or three. Elections are not synchronised — in 2025 alone, the Tlicho "
      "voted on 9 June, Fort Good Hope on 21 July, and seven hamlets on 8 December.",
      "<strong>Les Territoires du Nord-Ouest n'ont ni durée de mandat commune ni jour "
      "d'élection commun.</strong> Les mandats durent deux, trois ou quatre ans selon la loi "
      "qui régit la collectivité : les gouvernements communautaires tlichos siègent quatre ans, "
      "tandis que les collectivités à charte et les hameaux siègent deux ou trois ans. Les "
      "élections ne sont pas synchronisées — pour la seule année 2025, les Tlichos ont voté le "
      "9 juin, Fort Good Hope le 21 juillet, et sept hameaux le 8 décembre."),
])
a.p(T(
    "One more thing worth knowing before you vote: council sizes are set in law and they are "
    "small. British Columbia states that each municipal council consists of a mayor and between "
    "four and ten councillors depending on population. In Nunavut a council normally has eight "
    "councillors plus a mayor. In Prince Edward Island, elected councils typically include a "
    "mayor and six councillors.",
    "Une dernière chose à savoir avant d'aller voter : la taille des conseils est fixée par la "
    "loi et elle est modeste. La Colombie-Britannique précise que chaque conseil municipal se "
    "compose d'un maire et de quatre à dix conseillers selon la population. Au Nunavut, un "
    "conseil compte normalement huit conseillers en plus du maire. À l'Île-du-Prince-Édouard, "
    "les conseils élus comprennent habituellement un maire et six conseillers."))

# ------------------------------------------------------------------ 12
a.h2(T("Strong mayor powers in Ontario", "Les pouvoirs de maire fort en Ontario"))
a.p(T(
    "The default across Canada is that a mayor has no veto. A Canadian mayor is one vote on "
    "council. Alberta's official statement of the chief elected official's role contains no "
    "veto, and neither do the provincial guides for British Columbia, Nova Scotia, Saskatchewan "
    "or Manitoba. A Canadian mayor's real power is setting the agenda, influencing "
    "appointments, and being the only member elected by the whole municipality.",
    "Par défaut au Canada, un maire n'a pas de droit de veto. Un maire canadien est une voix au "
    "conseil. L'énoncé officiel du rôle du premier élu en Alberta ne prévoit aucun veto, pas "
    "plus que les guides provinciaux de la Colombie-Britannique, de la Nouvelle-Écosse, de la "
    "Saskatchewan ou du Manitoba. Le véritable pouvoir d'un maire canadien est de fixer l'ordre "
    "du jour, d'influencer les nominations et d'être le seul membre élu par toute la "
    "municipalité."))
a.p(T(
    "Ontario is the exception, and it is genuinely unusual in Canada. The Strong Mayors, "
    "Building Homes Act, 2022 received royal assent on 8 September 2022, and the Better "
    "Municipal Governance Act, 2022 followed on 8 December 2022. Here is what the powers "
    "actually are, from Ontario's own councillor's guide.",
    "L'Ontario fait exception, et c'est réellement inhabituel au Canada. La Loi de 2022 sur le "
    "renforcement des pouvoirs des maires pour la construction de logements a reçu la sanction "
    "royale le 8 septembre 2022, et la Loi de 2022 visant à améliorer la gouvernance municipale "
    "a suivi le 8 décembre 2022. Voici en quoi consistent réellement ces pouvoirs, selon le "
    "guide du conseiller municipal de l'Ontario lui-même."))
a.ul([
    T("<strong>The budget.</strong> The head of council must propose the municipality's budget "
      "each year by February 1, and can initiate and prepare in-year budget amendments. This is "
      "the largest of the powers and the least discussed — in a strong-mayor municipality the "
      "budget is the mayor's document, not the council's.",
      "<strong>Le budget.</strong> Le président du conseil doit proposer le budget de la "
      "municipalité chaque année d'ici le 1er février, et peut lancer et préparer des "
      "modifications budgétaires en cours d'exercice. C'est le plus important de ces pouvoirs et "
      "le moins discuté — dans une municipalité à maire fort, le budget est le document du "
      "maire, pas celui du conseil."),
    T("<strong>The veto, which is narrow.</strong> The head of council can choose to veto "
      "certain by-laws if they are of the opinion that all or part of the by-law could "
      "potentially interfere with a provincial priority. It must be exercised within 14 days, "
      "with written reasons filed with the clerk. It is not a general veto.",
      "<strong>Le veto, qui est étroit.</strong> Le président du conseil peut choisir "
      "d'opposer son veto à certains règlements s'il est d'avis que tout ou partie du règlement "
      "pourrait nuire à une priorité provinciale. Il doit être exercé dans les 14 jours, avec "
      "des motifs écrits déposés auprès du greffier. Ce n'est pas un veto général."),
    T("<strong>The override.</strong> Council may override the veto if two-thirds of all "
      "council members vote to override it.",
      "<strong>Le renversement.</strong> Le conseil peut renverser le veto si les deux tiers de "
      "tous ses membres votent en ce sens."),
    T("<strong>The one-third rule, added by the second Act.</strong> The head of council may "
      "propose a by-law advancing a prescribed provincial priority, and it passes if more than "
      "one third of the members of council vote for it. In plain words: certain by-laws can "
      "become law with the support of barely a third of the elected council.",
      "<strong>La règle du tiers, ajoutée par la seconde loi.</strong> Le président du conseil "
      "peut proposer un règlement qui fait avancer une priorité provinciale prescrite, et ce "
      "règlement est adopté si plus du tiers des membres du conseil votent pour. En clair : "
      "certains règlements peuvent devenir loi avec l'appui d'à peine un tiers du conseil élu."),
    T("<strong>Hiring, but not everyone.</strong> The head of council can hire municipal "
      "division heads and has authority over the chief administrative officer — but not over "
      "statutory officers such as the clerk, treasurer, chief building official, medical officer "
      "of health, police chief or fire chief.",
      "<strong>L'embauche, mais pas de tout le monde.</strong> Le président du conseil peut "
      "embaucher les chefs de division municipaux et a autorité sur le directeur général — mais "
      "pas sur les titulaires de charges prévues par la loi comme le greffier, le trésorier, le "
      "chef du service du bâtiment, le médecin hygiéniste, le chef de police ou le chef des "
      "pompiers."),
    T("<strong>Committees and the agenda.</strong> Power to create and dissolve committees and "
      "appoint their chairs and vice-chairs, including of local boards, and to bring matters "
      "forward for council consideration where they relate to provincial priorities.",
      "<strong>Les comités et l'ordre du jour.</strong> Le pouvoir de créer et de dissoudre des "
      "comités et d'en nommer les présidents et vice-présidents, y compris ceux de conseils "
      "locaux, et de soumettre des questions à l'examen du conseil lorsqu'elles se rapportent "
      "aux priorités provinciales."),
])
a.p(T(
    "The prescribed provincial priorities are specific and there are only two of them: building "
    "1.5 million new homes by 31 December 2031, and constructing and maintaining infrastructure "
    "to support housing, including transit, roads, utilities and servicing. The veto applies "
    "only to by-laws the mayor judges could interfere with those. A description of an "
    "unrestricted mayoral veto is wrong.",
    "Les priorités provinciales prescrites sont précises et il n'y en a que deux : construire "
    "1,5 million de nouveaux logements d'ici le 31 décembre 2031, et construire et entretenir "
    "les infrastructures nécessaires au logement, y compris le transport en commun, les routes, "
    "les services publics et la viabilisation. Le veto ne s'applique qu'aux règlements que le "
    "maire juge susceptibles d'y nuire. Décrire un veto municipal illimité est inexact."))
a.p(T(
    "As for how far the powers now reach: they came into force for Toronto and Ottawa, "
    "Ontario's two largest municipalities, for the 2022 to 2026 council term. They were "
    "extended to additional municipal councils in 26 municipalities on 1 July 2023, and to "
    "another 169 municipalities as of 1 May 2025. The province does not publish a running "
    "total, and we are not going to invent one by adding the announcements together — the "
    "regulation that lists the designated municipalities is the only place a true total exists.",
    "Quant à leur portée actuelle : ces pouvoirs sont entrés en vigueur pour Toronto et Ottawa, "
    "les deux plus grandes municipalités de l'Ontario, pour le mandat de conseil de 2022 à "
    "2026. Ils ont été étendus à des conseils municipaux supplémentaires dans 26 municipalités "
    "le 1er juillet 2023, puis à 169 autres municipalités à compter du 1er mai 2025. La "
    "province ne publie pas de total courant, et nous n'allons pas en inventer un en "
    "additionnant les annonces — le règlement qui énumère les municipalités désignées est le "
    "seul endroit où un véritable total existe."))
a.p(T(
    "One further development is worth watching. Under the Better Regional Governance Act, 2026, "
    "introduced on 2 April 2026 and affecting Durham, Halton, Muskoka, Niagara, Peel, Simcoe, "
    "Waterloo and York, Ontario proposes to let the Minister appoint the heads of council of "
    "upper-tier municipalities and to give those appointed chairs strong mayor powers. No "
    "upper-tier municipalities are being dissolved.",
    "Un autre développement mérite d'être suivi. En vertu de la Loi de 2026 sur l'amélioration "
    "de la gouvernance régionale, déposée le 2 avril 2026 et touchant Durham, Halton, Muskoka, "
    "Niagara, Peel, Simcoe, Waterloo et York, l'Ontario propose de permettre au ministre de "
    "nommer les présidents des conseils de municipalités de palier supérieur et d'accorder à "
    "ces présidents nommés les pouvoirs de maire fort. Aucune municipalité de palier supérieur "
    "n'est dissoute."))

# ------------------------------------------------------------------ 13
a.h2(T("What the government does not publish",
       "Ce que le gouvernement ne publie pas"))
a.p(T(
    "These are findings, not gaps in our research. Each one was looked for and each one is "
    "genuinely absent from the official record.",
    "Ce sont des constats, non des lacunes de notre recherche. Chacun a été cherché et chacun "
    "est réellement absent du dossier officiel."))
a.ul([
    T("<strong>A national count of municipalities, and a national count of mayors.</strong> "
      "Neither exists. Statistics Canada counts census subdivisions; the Federation of Canadian "
      "Municipalities publishes only its own membership.",
      "<strong>Un décompte national des municipalités, et un décompte national des "
      "maires.</strong> Ni l'un ni l'autre n'existe. Statistique Canada compte des subdivisions "
      "de recensement ; la Fédération canadienne des municipalités ne publie que son propre "
      "effectif."),
    T("<strong>Which of the 57 census subdivision types are municipalities.</strong> Statistics "
      "Canada classifies census subdivisions into 57 types and publishes no municipality flag "
      "for any of them. Five types are settled by the agency's own wording; the rest have to be "
      "checked against provincial statutes one at a time.",
      "<strong>Lesquels des 57 types de subdivisions de recensement sont des "
      "municipalités.</strong> Statistique Canada classe les subdivisions de recensement en 57 "
      "types et ne publie aucun indicateur de statut municipal pour aucun d'entre eux. Cinq "
      "types sont tranchés par les mots mêmes de l'organisme ; les autres doivent être vérifiés "
      "un à un dans les lois provinciales."),
    T("<strong>A subtotal of census subdivisions that are not municipalities.</strong> No such "
      "figure is published. The 1,592 on this page is our own addition of the types that are "
      "clearly not municipalities, and it is a floor.",
      "<strong>Un sous-total des subdivisions de recensement qui ne sont pas des "
      "municipalités.</strong> Aucun chiffre de ce genre n'est publié. Le 1 592 de cette page "
      "est notre propre addition des types qui ne sont manifestement pas des municipalités, et "
      "c'est un plancher."),
    T("<strong>A statement that New Brunswick parishes stopped being census "
      "subdivisions.</strong> The boundary-file count fell by 145 in the edition that loaded the "
      "2023 New Brunswick reform, but no sentence anywhere says what happened to the parishes.",
      "<strong>Une déclaration selon laquelle les paroisses du Nouveau-Brunswick ont cessé "
      "d'être des subdivisions de recensement.</strong> Le décompte du fichier des limites a "
      "chuté de 145 dans l'édition qui a intégré la réforme néo-brunswickoise de 2023, mais "
      "aucune phrase nulle part ne dit ce qu'il est advenu des paroisses."),
    T("<strong>Why the boundary-file count rose from 5,028 to 5,054.</strong> The 2025 guide "
      "gives the new figure and no explanation of the increase.",
      "<strong>Pourquoi le décompte du fichier des limites est passé de 5 028 à 5 054.</strong> "
      "Le guide de 2025 donne le nouveau chiffre sans expliquer la hausse."),
    T("<strong>How many First Nations use each leadership selection route.</strong> Indigenous "
      "Services Canada gives roughly 200 for the Indian Act election system and no count at all "
      "for custom selection or for the First Nations Elections Act.",
      "<strong>Combien de Premières Nations utilisent chaque mode de sélection des "
      "dirigeants.</strong> Services aux Autochtones Canada avance environ 200 pour le système "
      "électoral de la Loi sur les Indiens et aucun décompte pour la sélection coutumière ni "
      "pour la Loi sur les élections au sein de premières nations."),
    T("<strong>The total number of Ontario municipalities with strong mayor powers.</strong> "
      "The increments are announced one at a time; no running total is published.",
      "<strong>Le nombre total de municipalités ontariennes dotées de pouvoirs de maire "
      "fort.</strong> Les ajouts sont annoncés un à un ; aucun total courant n'est publié."),
    T("<strong>Manitoba's number of municipalities.</strong> Seven official sources were "
      "checked and none states a total.",
      "<strong>Le nombre de municipalités du Manitoba.</strong> Sept sources officielles ont "
      "été vérifiées et aucune n'énonce de total."),
])
a.p(T(
    "None of this makes local government unknowable. It does mean that anyone quoting a single "
    "confident national number about Canadian municipalities is either quoting the census "
    "subdivision count without its definition, or doing arithmetic and not saying so.",
    "Rien de tout cela ne rend le gouvernement local impossible à connaître. Cela signifie "
    "cependant que quiconque cite un seul chiffre national assuré au sujet des municipalités "
    "canadiennes cite soit le décompte des subdivisions de recensement sans sa définition, soit "
    "le résultat d'une addition sans le dire."))

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("canada-major-projects-office-explained.html",
         T("Canada's big projects — what is built, and what is on paper",
           "Les grands projets du Canada — ce qui est bâti et ce qui est sur papier")),
    link("how-canada-rebuilds-its-economy.html",
         T("How Canada rebuilds — new customers, old barriers",
           "Comment le Canada se rebâtit — nouveaux clients, vieilles barrières")),
])

# ------------------------------------------------------------------ 14
a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://www12.statcan.gc.ca/census-recensement/2021/ref/dict/az/definition-eng.cfm?ID=geo012",
             T("Statistics Canada — Census Dictionary 2021, the definition of a census "
               "subdivision and the 57 types",
               "Statistique Canada — Dictionnaire du recensement de 2021, la définition d'une "
               "subdivision de recensement et les 57 types")),
    out_link("https://www12.statcan.gc.ca/census-recensement/2021/ref/dict/tab/index-eng.cfm?ID=T1_5",
             T("Statistics Canada — Table 1.5, census subdivision types by province and "
               "territory, 2021 Census",
               "Statistique Canada — tableau 1.5, types de subdivisions de recensement par "
               "province et territoire, Recensement de 2021")),
    out_link("https://www.statcan.gc.ca/en/subjects/standard/sgc/2021/tablef",
             T("Statistics Canada — standard abbreviations and titles for census subdivision "
               "types, 2021",
               "Statistique Canada — abréviations et titres normalisés des types de "
               "subdivisions de recensement, 2021")),
    out_link("https://www150.statcan.gc.ca/n1/pub/92-162-g/92-162-g2025001-eng.htm",
             T("Statistics Canada — Census Subdivision Boundary File reference guide, 2025, and "
               "the 5,054 count",
               "Statistique Canada — guide de référence du fichier des limites des subdivisions "
               "de recensement, 2025, et le décompte de 5 054")),
    out_link("https://www150.statcan.gc.ca/n1/pub/92-162-g/92-162-g2024001-eng.htm",
             T("Statistics Canada — Census Subdivision Boundary File reference guide, 2024, the "
               "edition that loaded the New Brunswick changes",
               "Statistique Canada — guide de référence du fichier des limites des subdivisions "
               "de recensement, 2024, l'édition qui a intégré les changements du "
               "Nouveau-Brunswick")),
    out_link("https://www150.statcan.gc.ca/n1/pub/92-162-g/92-162-g2023001-eng.htm",
             T("Statistics Canada — Census Subdivision Boundary File reference guide, 2023",
               "Statistique Canada — guide de référence du fichier des limites des subdivisions "
               "de recensement, 2023")),
    out_link("https://www12.statcan.gc.ca/census-recensement/releaseschedule-calendrierdediffusion/upcomingreleases-diffusionsavenir-eng.cfm",
             T("Statistics Canada — upcoming releases of the Census of Population",
               "Statistique Canada — prochaines diffusions du Recensement de la population")),
    out_link("https://laws-lois.justice.gc.ca/eng/acts/i-5/page-1.html",
             T("Justice Canada — Indian Act, section 2, the definitions of reserve, band and "
               "council of the band",
               "Justice Canada — Loi sur les Indiens, article 2, les définitions de réserve, de "
               "bande et de conseil de la bande")),
    out_link("https://www.sac-isc.gc.ca/eng/1323195944486/1565366893158",
             T("Indigenous Services Canada — leadership selection in First Nations",
               "Services aux Autochtones Canada — la sélection des dirigeants dans les Premières "
               "Nations")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1100100028429/1616789617763",
             T("Crown-Indigenous Relations and Northern Affairs Canada — differences between "
               "self-governing First Nations and Indian Act bands, a page dated 2010",
               "Relations Couronne-Autochtones et Affaires du Nord Canada — les différences "
               "entre les Premières Nations autonomes et les bandes visées par la Loi sur les "
               "Indiens, page datée de 2010")),
    out_link("https://laws-lois.justice.gc.ca/eng/const/page-3.html",
             T("Justice Canada — the Constitution Acts 1867 to 1982, section 92",
               "Justice Canada — les Lois constitutionnelles de 1867 à 1982, article 92")),
    out_link("https://www.canada.ca/en/intergovernmental-affairs/services/federation/distribution-legislative-powers.html",
             T("Intergovernmental Affairs — the constitutional distribution of legislative powers",
               "Affaires intergouvernementales — la répartition constitutionnelle des pouvoirs "
               "législatifs")),
    out_link("https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/affaires-municipales/publications/organisation_municipale/organisation_territoriale/BRO_organisation_municipale.pdf",
             T("Quebec — Municipal organisation in Quebec in 2026",
               "Québec — L'organisation municipale au Québec en 2026")),
    out_link("https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/affaires-municipales/publications/elections/RAP_elections_municipales_2025.pdf",
             T("Quebec — data on the 2025 general municipal elections, including 1,091 mayoral "
               "positions",
               "Québec — données relatives aux élections générales municipales de 2025, dont 1 "
               "091 postes de maire")),
    out_link("https://www.ontario.ca/page/list-ontario-municipalities",
             T("Ontario — the list of Ontario municipalities",
               "Ontario — la liste des municipalités de l'Ontario")),
    out_link("https://www.ontario.ca/document/ontario-municipal-councillors-guide/10-strong-mayor-powers-and-duties",
             T("Ontario — municipal councillor's guide, strong mayor powers and duties",
               "Ontario — guide du conseiller municipal, pouvoirs et fonctions de maire fort")),
    out_link("https://www.ontario.ca/page/municipal-restructuring",
             T("Ontario — municipal restructuring",
               "Ontario — la restructuration municipale")),
    out_link("https://www.amo.on.ca/how-local-government-works",
             T("Association of Municipalities of Ontario — how local government works, and the "
               "815 to 444 history",
               "Association des municipalités de l'Ontario — le fonctionnement du gouvernement "
               "local, et l'historique de 815 à 444")),
    out_link("https://www2.gnb.ca/content/gnb/en/corporate/promo/local-governance/structure.html",
             T("New Brunswick — local governance structure after the 2023 reform",
               "Nouveau-Brunswick — la structure de gouvernance locale après la réforme de 2023")),
    out_link("https://www2.gnb.ca/content/gnb/en/corporate/promo/local-governance/about.html",
             T("New Brunswick — about local governance reform and the 12 rural districts",
               "Nouveau-Brunswick — au sujet de la réforme de la gouvernance locale et des 12 "
               "districts ruraux")),
    out_link("https://www2.gnb.ca/content/dam/gnb/Corporate/Promo/localgovreform/local-governance-reform.pdf",
             T("New Brunswick — the local governance reform green paper, and the 340 entities "
               "before it",
               "Nouveau-Brunswick — le livre vert sur la réforme de la gouvernance locale, et "
               "les 340 entités qui la précédaient")),
    out_link("https://www.novascotia.ca/sites/default/files/documents/1-1414/guide-new-municipal-councillors-en.pdf",
             T("Nova Scotia — guide for new municipal councillors, mayors and wardens",
               "Nouvelle-Écosse — guide des nouveaux conseillers municipaux, maires et préfets")),
    out_link("https://www.alberta.ca/types-of-municipalities-in-alberta",
             T("Alberta — types of municipalities in Alberta",
               "Alberta — les types de municipalités en Alberta")),
    out_link("https://www2.gov.bc.ca/gov/content/governments/local-governments/facts-framework/systems",
             T("British Columbia — local government systems, 161 municipalities and 27 regional "
               "districts",
               "Colombie-Britannique — les systèmes de gouvernement local, 161 municipalités et "
               "27 districts régionaux")),
    out_link("https://www2.gov.bc.ca/gov/content/governments/local-governments/facts-framework/systems/regional-districts",
             T("British Columbia — regional districts and their electoral areas",
               "Colombie-Britannique — les districts régionaux et leurs secteurs électoraux")),
    out_link("https://www.saskatchewan.ca/government/government-structure/local-federal-and-other-governments/your-local-government/about-the-saskatchewan-municipal-system",
             T("Saskatchewan — about the Saskatchewan municipal system",
               "Saskatchewan — au sujet du système municipal de la Saskatchewan")),
    out_link("https://www.gov.mb.ca/mr/contactus/pubs/mod.pdf",
             T("Manitoba — the Municipal Officials Directory, which lists municipalities and "
               "states no total",
               "Manitoba — le répertoire des élus municipaux, qui énumère les municipalités "
               "sans donner de total")),
    out_link("https://yukon.ca/en/news/government-yukon-plans-move-forward-municipal-term-office-change-following-what-we-heard-report",
             T("Yukon — the move from three-year to four-year municipal terms",
               "Yukon — le passage de mandats municipaux de trois ans à quatre ans")),
    out_link("https://www.maca.gov.nt.ca/en/services/municipal-elections/election-dates",
             T("Northwest Territories — municipal election dates, which are not synchronised",
               "Territoires du Nord-Ouest — les dates des élections municipales, qui ne sont pas "
               "synchronisées")),
    out_link("https://www.gov.nu.ca/sites/default/files/documents/2026-05/2026-2030_Business_Plans_-_ENG.pdf",
             T("Nunavut — Government of Nunavut business plan 2026 to 2030",
               "Nunavut — plan d'activités du gouvernement du Nunavut 2026-2030")),
    out_link("https://www.gov.nl.ca/mca/files/Municipal-Council-Handbook-2021.pdf",
             T("Newfoundland and Labrador — Municipal Council Handbook",
               "Terre-Neuve-et-Labrador — Guide du conseil municipal")),
    out_link("https://peimunicipalities.princeedwardisland.ca/faqs",
             T("Prince Edward Island — municipalities frequently asked questions",
               "Île-du-Prince-Édouard — foire aux questions sur les municipalités")),
    out_link("https://fcm.ca/en/about-fcm",
             T("Federation of Canadian Municipalities — about FCM and its membership",
               "Fédération canadienne des municipalités — au sujet de la FCM et de son effectif")),
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
