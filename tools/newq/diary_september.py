#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adds the twenty-six missing September notes to tools/newq/diary_data.json.

WHY
---
The diary was written during July and August 2026 and it shows. Measured on
25 August 2026: July had a note on 31 days of 31, August on 30 of 31, and every
other month was nearly empty — 282 of 365 days had nothing at all. September had
four. In a week, most visitors would have landed on the "nothing is written for
this date yet" message instead of a note.

SOURCES
-------
Every one of these twenty-six is sourced to a government body, a Crown agency, a
national or provincial museum, a provincial heritage agency, a municipal
government, or a public university. None of them cites the encyclopedia that 83
of the existing 149 notes cite, and which the site is not supposed to name at
all. This batch is what the rest of the diary should look like after that is
cleaned up.

DATES
-----
Six of these are events where sources put the anniversary on either of two days.
In each case the body text says what happened when, so a reader who has seen the
other date is not left thinking the page is wrong: Gouzenko walked out on the
evening of the 5th and was granted protection on the 7th; Marilyn Bell entered
the water on the 8th and finished on the 9th; the Noronic docked on the evening
of the 16th and burned at half past one in the morning of the 17th.

    python3 tools/newq/diary_september.py           # add them
    python3 tools/newq/diary_september.py --check   # report, change nothing

Then rebuild:
    python3 tools/newq/build_diary.py
    ... the usual pipeline ...
    python3 tools/newq/build_diary.py --fr
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "tools", "newq", "diary_data.json")

N = [
 (9, 2, 1998, "disaster", "Transportation Safety Board of Canada, Swissair 111 investigation report",
  "Swissair 111 goes down off Peggy's Cove",
  "A flight from New York to Geneva caught fire in the ceiling above the cockpit. The crew turned for Halifax, but the aircraft came down in the sea about five nautical miles from Peggy's Cove, Nova Scotia. All 229 people on board died. Fishermen and people from the villages nearby put out in their own boats to search.",
  "Le vol Swissair 111 s'abîme près de Peggy's Cove",
  "Un vol de New York vers Genève a pris feu dans le plafond au-dessus du poste de pilotage. L'équipage a mis le cap sur Halifax, mais l'appareil est tombé en mer à environ cinq milles marins de Peggy's Cove, en Nouvelle-Écosse. Les 229 personnes à bord ont péri. Des pêcheurs et des gens des villages voisins ont pris la mer dans leurs propres bateaux pour chercher."),

 (9, 4, 1984, "law", "House of Commons of Canada, Procedure and Practice, Appendix 12",
  "The largest win in a federal election",
  "Canadians voted in a federal general election. The Progressive Conservatives won 211 seats in the House of Commons. No party has ever won more in a Canadian federal election. The Liberals, who had governed for most of the previous twenty years, were reduced to 40 seats.",
  "La plus grande victoire d'une élection fédérale",
  "Les Canadiens ont voté à une élection générale fédérale. Les progressistes-conservateurs ont remporté 211 sièges à la Chambre des communes. Aucun parti n'en a jamais obtenu davantage à une élection fédérale canadienne. Les libéraux, au pouvoir pendant la majeure partie des vingt années précédentes, sont tombés à 40 sièges."),

 (9, 5, 1945, "people", "Library and Archives Canada",
  "A clerk walks out of the Soviet embassy",
  "Igor Gouzenko was a young cipher clerk at the Soviet embassy in Ottawa. On the evening of 5 September he walked out with documents hidden on him and went first to the Ottawa Journal, which turned him away. Canada granted him protection on 7 September. They showed that the Soviet Union was running a spy network inside Canada, including a member of Parliament. Many people date the beginning of the Cold War to that walk.",
  "Un commis quitte l'ambassade soviétique",
  "Igor Gouzenko était un jeune chiffreur à l'ambassade soviétique à Ottawa. Le soir du 5 septembre, il est sorti avec des documents cachés sur lui et s'est d'abord rendu au journal Ottawa Journal, qui l'a éconduit. Le Canada lui a accordé sa protection le 7 septembre. Ils montraient que l'Union soviétique dirigeait un réseau d'espions au Canada, dont un député. Beaucoup situent le début de la guerre froide à cette sortie."),

 (9, 6, 1775, "war", "Parks Canada, Battle of September 6th, 1775 National Historic Site",
  "An ambush beside the Richelieu",
  "American forces invading Canada landed near Fort Saint-Jean, in what is now Saint-Jean-sur-Richelieu, Quebec. About a hundred Mohawk and allied Indigenous fighters ambushed them beside a creek. The Americans were pushed back and withdrew to Île aux Noix. The place is a national historic site today.",
  "Une embuscade au bord du Richelieu",
  "Des forces américaines qui envahissaient le Canada ont débarqué près du fort Saint-Jean, dans l'actuelle Saint-Jean-sur-Richelieu, au Québec. Une centaine de combattants mohawks et alliés leur ont tendu une embuscade au bord d'un ruisseau. Les Américains ont été repoussés et se sont retirés à l'île aux Noix. L'endroit est aujourd'hui un lieu historique national."),

 (9, 7, 1850, "treaty", "Crown-Indigenous Relations and Northern Affairs Canada, Treaty Texts",
  "The Robinson-Superior Treaty",
  "Ojibwe leaders from the Lake Superior country, led by Chief Peau de Chat, signed a treaty with the Crown at Sault Ste. Marie. It covered the Lake Superior shore from Batchewana Bay to the Pigeon River. The Crown promised yearly payments and the continued right to hunt and fish. Two days later the Lake Huron bands signed a companion treaty.",
  "Le Traité Robinson-Supérieur",
  "Des chefs ojibwés du pays du lac Supérieur, menés par le chef Peau de Chat, ont signé un traité avec la Couronne à Sault-Sainte-Marie. Il couvrait la rive du lac Supérieur, de la baie Batchewana à la rivière aux Pigeons. La Couronne promettait des versements annuels et le maintien du droit de chasser et de pêcher. Deux jours plus tard, les bandes du lac Huron ont signé un traité jumeau."),

 (9, 9, 1954, "sport", "Parks Canada, The Crossing of Lake Ontario by Marilyn Bell National Historic Event",
  "Marilyn Bell crosses Lake Ontario",
  "Marilyn Bell was sixteen years old and from Toronto. She entered the water late on 8 September and swam 51.5 kilometres through cold water, high winds and eels, reaching Toronto on the evening of the 9th after almost twenty-one hours. She was the first person ever to swim the lake.",
  "Marilyn Bell traverse le lac Ontario",
  "Marilyn Bell avait seize ans et venait de Toronto. Elle est entrée dans l'eau tard le 8 septembre et a nagé 51,5 kilomètres dans une eau froide, par grands vents et parmi les anguilles, atteignant Toronto le soir du 9 après près de vingt et une heures. Elle a été la première personne à traverser le lac à la nage."),

 (9, 10, 1939, "war", "Veterans Affairs Canada, chronology of the Second World War",
  "Canada declares war",
  "Britain had declared war on Germany on 3 September. Canada did not follow automatically. Parliament was recalled, it debated, and it voted. Canada declared war on 10 September 1939 — the first time the country declared war on another by its own decision.",
  "Le Canada déclare la guerre",
  "La Grande-Bretagne avait déclaré la guerre à l'Allemagne le 3 septembre. Le Canada n'a pas suivi automatiquement. Le Parlement a été rappelé, il a débattu et il a voté. Le Canada a déclaré la guerre le 10 septembre 1939 — la première fois que le pays déclarait la guerre à un autre de sa propre décision."),

 (9, 11, 2001, "people", "Town of Gander",
  "Gander takes in the world",
  "After the attacks in the United States, the United States closed its airspace. Canada grounded its own flights but opened its airports to aircraft already over the Atlantic. Thirty-four airliners and four military aircraft landed at Gander, Newfoundland, carrying about 6,600 passengers and crew. The town's population was 9,651, so it grew by almost seventy per cent in a few hours. People opened schools, halls and their own homes.",
  "Gander accueille le monde",
  "Après les attentats aux États-Unis, les États-Unis ont fermé leur espace aérien. Le Canada a cloué ses propres vols au sol, mais a ouvert ses aéroports aux appareils déjà au-dessus de l'Atlantique. Trente-quatre avions de ligne et quatre appareils militaires se sont posés à Gander, à Terre-Neuve, avec environ 6 600 passagers et membres d'équipage. La population de la ville était de 9 651 personnes : elle a donc grimpé de près de soixante-dix pour cent en quelques heures. Les gens ont ouvert les écoles, les salles et leurs propres maisons."),

 (9, 12, 1945, "law", "Ontario Heritage Trust, provincial plaque, The Windsor-Ford Strike of 1945",
  "The Windsor Ford strike begins",
  "Talks between Ford of Canada and the United Auto Workers broke down, and ten thousand members of Local 200 walked out in Windsor, Ontario. At one point strikers parked about two thousand cars and trucks around the powerhouse to block it. The strike lasted ninety-nine days and led to the Rand Formula, which shaped union rights in Canada for decades.",
  "La grève de Ford à Windsor commence",
  "Les négociations entre Ford du Canada et les Travailleurs unis de l'automobile ont échoué, et dix mille membres de la section locale 200 ont débrayé à Windsor, en Ontario. À un moment, les grévistes ont garé environ deux mille voitures et camions autour de la centrale électrique de l'usine pour la bloquer. La grève a duré quatre-vingt-dix-neuf jours et a mené à la formule Rand, qui a façonné les droits syndicaux au Canada pendant des décennies."),

 (9, 14, 1926, "law", "House of Commons of Canada, Procedure and Practice, Appendix 12",
  "An election about the Governor General",
  "Earlier that year the Governor General had refused the Prime Minister's request to call an election. The Prime Minister made that refusal the main issue of the campaign that followed. On 14 September voters gave his party 116 of the 245 seats — short of a majority — and he governed with the support of Liberal-Progressive members. The House of Commons' own Procedure and Practice records that no Governor General has refused such a request since.",
  "Une élection au sujet du gouverneur général",
  "Plus tôt cette année-là, le gouverneur général avait refusé au premier ministre sa demande de déclencher des élections. Le premier ministre a fait de ce refus l'enjeu principal de la campagne qui a suivi. Le 14 septembre, les électeurs ont donné 116 des 245 sièges à son parti — pas une majorité — et il a gouverné avec l'appui de députés libéraux-progressistes. La Procédure et les usages de la Chambre des communes indique qu'aucun gouverneur général n'a refusé une telle demande depuis."),

 (9, 15, 1874, "treaty", "Crown-Indigenous Relations and Northern Affairs Canada, Treaty Texts",
  "Treaty No. 4 is signed",
  "Cree and Saulteaux leaders and Crown officials signed Treaty No. 4 at the Qu'Appelle Lakes, near Fort Qu'Appelle in what is now Saskatchewan. Other bands signed later at Fort Ellice, Swan Lake and Fort Pelly. The treaty covers most of southern Saskatchewan and parts of Manitoba and Alberta.",
  "Le Traité no 4 est signé",
  "Des chefs cris et saulteaux et des représentants de la Couronne ont signé le Traité no 4 aux lacs Qu'Appelle, près de Fort Qu'Appelle, dans l'actuelle Saskatchewan. D'autres bandes l'ont signé plus tard à Fort Ellice, à Swan Lake et à Fort Pelly. Le traité couvre la majeure partie du sud de la Saskatchewan et des parties du Manitoba et de l'Alberta."),

 (9, 16, 1987, "science", "Environment and Climate Change Canada",
  "The Montreal Protocol is signed",
  "Countries met in Montreal and agreed to start cutting back the chemicals that were destroying the ozone layer high above the Earth. Canada signed on 16 September 1987 along with twenty-three others. It became the first treaty in United Nations history that every country ratified, and Montreal still hosts the fund that helps poorer countries phase the chemicals out.",
  "Le Protocole de Montréal est signé",
  "Des pays se sont réunis à Montréal et ont convenu de commencer à réduire les produits chimiques qui détruisaient la couche d'ozone, très haut au-dessus de la Terre. Le Canada a signé le 16 septembre 1987, avec vingt-trois autres. Il est devenu le premier traité de l'histoire des Nations Unies à être ratifié par tous les pays, et Montréal accueille toujours le fonds qui aide les pays plus pauvres à éliminer ces produits."),

 (9, 17, 1949, "disaster", "Ontario Heritage Trust, provincial plaque, The Noronic Disaster",
  "Fire on the Noronic",
  "The cruise ship Noronic was tied up overnight in Toronto harbour with 524 passengers aboard. At half past one in the morning a passenger saw smoke coming from a locked closet. The fire spread before the crew could wake everyone. People climbed down ropes or jumped into the water, and 119 died. The inquiry that followed brought in much stricter fire rules on ships.",
  "L'incendie du Noronic",
  "Le paquebot Noronic était amarré pour la nuit dans le port de Toronto avec 524 passagers à bord. À une heure et demie du matin, un passager a vu de la fumée sortir d'un placard verrouillé. Le feu s'est propagé avant que l'équipage puisse réveiller tout le monde. Des gens sont descendus le long de cordages ou ont sauté à l'eau, et 119 personnes sont mortes. L'enquête qui a suivi a imposé des règles anti-incendie beaucoup plus strictes à bord des navires."),

 (9, 18, 1759, "war", "Parks Canada, Siege of Quebec 1759 National Historic Event",
  "The siege of Quebec ends",
  "British ships and troops had besieged Quebec since 26 June. Five days after the battle on the Plains of Abraham, the city's defenders gave up and the articles of capitulation were agreed. New France was formally handed to Britain four years later, by the Treaty of Paris.",
  "Le siège de Québec prend fin",
  "Des navires et des troupes britanniques assiégeaient Québec depuis le 26 juin. Cinq jours après la bataille des plaines d'Abraham, les défenseurs de la ville ont capitulé et les articles de la capitulation ont été convenus. La Nouvelle-France a été officiellement cédée à la Grande-Bretagne quatre ans plus tard, par le traité de Paris."),

 (9, 19, 2022, "people", "Department of National Defence",
  "A day of mourning for the Queen",
  "Queen Elizabeth II had been Canada's head of state for seventy years. Canada held a one-time National Day of Mourning on the day of her state funeral in London. A national ceremony was held at Christ Church Cathedral in Ottawa and shown on television.",
  "Une journée de deuil pour la reine",
  "La reine Elizabeth II avait été chef d'État du Canada pendant soixante-dix ans. Le Canada a tenu une Journée nationale de deuil, unique, le jour de ses funérailles nationales à Londres. Une cérémonie nationale a eu lieu à la cathédrale Christ Church, à Ottawa, et a été télédiffusée."),

 (9, 20, 1917, "law", "Elections Canada, A History of the Vote in Canada",
  "The first women get the federal vote",
  "In one day Parliament passed two election laws. Together they gave the federal vote to nurses serving overseas and to close female relatives of soldiers — the first time women could vote in a Canadian federal election. The same laws took the vote away from many recent immigrants. Most women aged twenty-one and over received the federal vote the following year, though property rules and other restrictions still applied to some.",
  "Les premières femmes obtiennent le droit de vote fédéral",
  "En une seule journée, le Parlement a adopté deux lois électorales. Ensemble, elles ont donné le droit de vote fédéral aux infirmières servant outre-mer et aux proches parentes de soldats — la première fois que des femmes pouvaient voter à une élection fédérale canadienne. Les mêmes lois ont retiré le droit de vote à de nombreux immigrants récents. La plupart des femmes de vingt et un ans et plus ont obtenu le vote fédéral l'année suivante, même si des règles de propriété et d'autres restrictions s'appliquaient encore à certaines."),

 (9, 21, 2010, "disaster", "Government of Newfoundland and Labrador",
  "Hurricane Igor cuts off the outports",
  "Hurricane Igor swept across Newfoundland with heavy rain and high winds. Roads and bridges washed out in nearly two hundred communities, with more than a hundred breaches in the roads. Over ninety communities were cut off, some for as long as ten days. More than a thousand members of the Canadian Armed Forces were sent to rebuild bridges and bring in water and supplies.",
  "L'ouragan Igor isole les villages côtiers",
  "L'ouragan Igor a balayé Terre-Neuve avec de fortes pluies et des vents violents. Des routes et des ponts ont été emportés dans près de deux cents localités, avec plus de cent brèches dans les routes. Plus de quatre-vingt-dix localités ont été coupées du reste, certaines jusqu'à dix jours. Plus de mille membres des Forces armées canadiennes ont été envoyés reconstruire des ponts et acheminer eau et provisions."),

 (9, 22, 1988, "law", "Canadian Museum for Human Rights",
  "The apology to Japanese Canadians",
  "During the Second World War Canada forced some 23,000 Japanese Canadians from their homes on the west coast and took their property. On 22 September 1988 the Prime Minister apologised in the House of Commons. The settlement gave 21,000 dollars to each surviving person, pardons for those wrongly imprisoned, citizenship for those wrongly deported, and 24 million dollars towards what became the Canadian Race Relations Foundation.",
  "Les excuses aux Canadiens d'origine japonaise",
  "Pendant la Seconde Guerre mondiale, le Canada a chassé quelque 23 000 Canadiens d'origine japonaise de leurs maisons de la côte Ouest et a saisi leurs biens. Le 22 septembre 1988, le premier ministre a présenté des excuses à la Chambre des communes. L'entente accordait 21 000 dollars à chaque survivant, le pardon à ceux qui avaient été emprisonnés à tort, la citoyenneté à ceux qui avaient été expulsés à tort, et 24 millions de dollars pour ce qui est devenu la Fondation canadienne des relations raciales."),

 (9, 23, 1908, "build", "University of Alberta",
  "A university opens in four rented rooms",
  "Alberta had been a province for three years. The new University of Alberta opened to forty-five students in four rented rooms on the top floor of a school in Strathcona, now part of Edmonton. It had no campus buildings of its own yet. It is one of Canada's largest universities today.",
  "Une université ouvre dans quatre pièces louées",
  "L'Alberta était une province depuis trois ans. La nouvelle Université de l'Alberta a ouvert ses portes à quarante-cinq étudiants dans quatre pièces louées au dernier étage d'une école de Strathcona, aujourd'hui un quartier d'Edmonton. Elle n'avait encore aucun bâtiment à elle. C'est aujourd'hui l'une des plus grandes universités du Canada."),

 (9, 24, 1875, "treaty", "Crown-Indigenous Relations and Northern Affairs Canada, Treaty Texts",
  "Treaty No. 5 at Norway House",
  "Treaty No. 5 was signed in two places. Saulteaux and Swampy Cree leaders signed at Berens River on 20 September and at Norway House on the 24th. The treaty covered about a hundred thousand square miles around Lake Winnipeg, in what is now Manitoba and Saskatchewan. More northern communities joined it in later years.",
  "Le Traité no 5 à Norway House",
  "Le Traité no 5 a été signé à deux endroits. Des chefs saulteaux et cris des marais l'ont signé à Berens River le 20 septembre et à Norway House le 24. Le traité couvrait environ cent mille milles carrés autour du lac Winnipeg, dans les actuels Manitoba et Saskatchewan. D'autres communautés du Nord y ont adhéré dans les années suivantes."),

 (9, 25, 1975, "culture", "Ontario Heritage Trust, provincial plaque background paper",
  "The Franco-Ontarian flag is raised",
  "The green and white Franco-Ontarian flag was raised for the first time at the University of Sudbury. On the green half it carries a white lily for the French-speaking world; on the white half, a green trillium, Ontario's flower. Ontario later made it an official provincial emblem, and since 2010 the province has marked Franco-Ontarian Day every 25 September.",
  "Le drapeau franco-ontarien est hissé",
  "Le drapeau franco-ontarien, vert et blanc, a été hissé pour la première fois à l'Université de Sudbury. Sur la moitié verte, il porte une fleur de lys blanche pour la francophonie ; sur la moitié blanche, un trille vert, la fleur de l'Ontario. L'Ontario en a plus tard fait un emblème provincial officiel, et depuis 2010 la province souligne le Jour des Franco-Ontariens chaque 25 septembre."),

 (9, 26, 1968, "people", "Assemblee nationale du Quebec, biography of Daniel Johnson",
  "A premier dies at Manic-5",
  "Daniel Johnson was the Premier of Quebec. He travelled north to the great hydro dam on the Manicouagan River, which was about to be opened. He died there, aged fifty-three. The dam carries his name today.",
  "Un premier ministre meurt à Manic-5",
  "Daniel Johnson était premier ministre du Québec. Il s'était rendu dans le Nord, au grand barrage hydroélectrique de la rivière Manicouagan, qui allait être inauguré. Il y est mort, à cinquante-trois ans. Le barrage porte aujourd'hui son nom."),

 (9, 27, 1918, "war", "Veterans Affairs Canada, The Last Hundred Days",
  "Crossing the Canal du Nord",
  "In the last months of the First World War the Canadian Corps faced a dry canal bed in northern France that the Germans had turned into a strong defence. Canadian engineers and soldiers crossed at a narrow point and pushed through. Veterans Affairs Canada calls the attack a stunning success. Two Canadians won the Victoria Cross for what they did that day, and two more for actions that began on it.",
  "La traversée du canal du Nord",
  "Dans les derniers mois de la Première Guerre mondiale, le Corps canadien s'est trouvé devant le lit asséché d'un canal, dans le nord de la France, que les Allemands avaient transformé en solide défense. Des ingénieurs et des soldats canadiens l'ont traversé à un point étroit et ont percé. Anciens Combattants Canada qualifie l'attaque de succès éclatant. Deux Canadiens ont mérité la Croix de Victoria pour ce qu'ils ont fait ce jour-là, et deux autres pour des actions commencées ce jour-là."),

 (9, 28, 1972, "sport", "Canadian Museum of History",
  "Henderson scores for Canada",
  "Canada and the Soviet Union played the last game of the eight-game Summit Series in Moscow. With thirty-four seconds left, Paul Henderson scored to win the game and the series. Schools and workplaces across the country stopped so people could watch. The Canadian Museum of History calls it the most famous goal in Canadian hockey.",
  "Henderson marque pour le Canada",
  "Le Canada et l'Union soviétique disputaient le dernier match de la Série du siècle, à Moscou. À trente-quatre secondes de la fin, Paul Henderson a marqué et remporté le match et la série. Partout au pays, écoles et lieux de travail se sont arrêtés pour regarder. Le Musée canadien de l'histoire le décrit comme le but le plus célèbre du hockey canadien."),

 (9, 29, 1962, "science", "Canadian Space Agency",
  "Canada's first satellite",
  "Alouette-1 was launched on 29 September 1962. The Canadian Space Agency calls Canada the third country to design and build its own satellite, after the Soviet Union and the United States. It studied the ionosphere, the electric layer high in the atmosphere that bends radio signals. It was built to last a year and sent back useful data for ten.",
  "Le premier satellite canadien",
  "Alouette-1 a été lancé le 29 septembre 1962. L'Agence spatiale canadienne présente le Canada comme le troisième pays à concevoir et construire son propre satellite, après l'Union soviétique et les États-Unis. Il étudiait l'ionosphère, la couche électrique très haute dans l'atmosphère qui dévie les signaux radio. Conçu pour durer un an, il a transmis des données utiles pendant dix ans."),

 (9, 30, 2021, "people", "Crown-Indigenous Relations and Northern Affairs Canada",
  "The first Truth and Reconciliation Day",
  "Canada held the first National Day for Truth and Reconciliation. The day honours the children who died at residential schools, the survivors, and their families and communities. It falls on the same date as Orange Shirt Day, and many people wear orange. It is now a federal statutory holiday.",
  "La première Journée de la vérité et de la réconciliation",
  "Le Canada a tenu la première Journée nationale de la vérité et de la réconciliation. La journée honore les enfants morts dans les pensionnats, les survivants, ainsi que leurs familles et leurs communautés. Elle tombe à la même date que la Journée du chandail orange, et beaucoup de gens portent de l'orange. C'est maintenant un jour férié fédéral."),
]


def era_for(y, m):
    if y < 1867 or (y == 1867 and m < 7):
        return 0
    return 1 if y < 1900 else 2 if y < 1950 else 3 if y < 2000 else 4


def main():
    check = "--check" in sys.argv
    notes = json.load(open(DATA, encoding="utf-8"))
    have = {(n.get("m"), n.get("d"), n.get("y")) for n in notes}
    taken = {(n.get("m"), n.get("d")) for n in notes if n.get("m") and n.get("d")}

    added, skipped = [], []
    for m, d, y, topic, src, en_t, en_b, fr_t, fr_b in N:
        if (m, d, y) in have:
            skipped.append((m, d, en_t))
            continue
        notes.append({
            "y": y, "era": era_for(y, m), "m": m, "d": d,
            "topic": topic, "src": src,
            "en": [en_t, en_b], "fr": [fr_t, fr_b],
        })
        added.append((m, d, en_t, (m, d) in taken))

    print("September notes to add: %d   already present: %d" % (len(added), len(skipped)))
    for m, d, t, clash in added:
        print("   %2d Sept  %s%s" % (d, t, "   (day already had a note)" if clash else ""))

    # the same guards build_diary.py applies, run here so a bad note never lands
    bad = [n for n in notes if not n.get("src") or len(n.get("en", [])) != 2
           or len(n.get("fr", [])) != 2]
    if bad:
        raise SystemExit("%d note(s) missing a source or a language" % len(bad))
    wrong = [n["en"][0] for n in notes if n["era"] != era_for(n["y"], n.get("m") or 1)]
    if wrong:
        raise SystemExit("wrong era on: %s" % wrong[:5])
    named = [n["en"][0] for n in notes if "ncyclopedia" in (n.get("src") or "")
             and n["en"][0] in [x[2] for x in added]]
    if named:
        raise SystemExit("a new note cites the encyclopedia: %s" % named)

    sept = sorted({n["d"] for n in notes if n.get("m") == 9})
    print("\nSeptember days with a note: %d of 30" % len(sept))
    missing = [d for d in range(1, 31) if d not in sept]
    print("still empty: %s" % (missing or "none"))

    if check:
        print("--check: nothing written")
        return
    json.dump(notes, open(DATA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nwrote %s — %d notes" % (DATA, len(notes)))


if __name__ == "__main__":
    main()
