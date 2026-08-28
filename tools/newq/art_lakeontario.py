#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article — the human history of Lake Ontario.

Source: research/lake-ontario-20260828.md in the private project notes.
Government of Canada, Crown agencies, national and public museums, provincial
heritage agencies, municipal governments, public universities and First Nation
government publications only. Commercial and crowd-edited reference sites were
excluded by the research rule and none is cited here.

Two findings shape the page. The first is that the governments do not agree
about what the lake's name means, or about what the 1641 record actually named.
The second is quieter: no permitted source publishes an Indigenous-language name
for this lake at all. Governments that publish the acreage of an 1805 treaty to
the single acre do not publish that.

Deliberately kept off the page because no official source in the research
supports them:
  * any Indigenous-language name for the lake, including the forms that
    circulate online, and any French colonial name for it;
  * which specific Iroquoian language "Ontario" comes from;
  * that Brule was the first European to see Lake Ontario, and any dated
    account of Champlain crossing it in 1615;
  * Fort Niagara's construction date and its 1759 siege, and any detail of the
    American yard at Sackets Harbor — both are in New York State and no
    permitted Canadian source covers them;
  * any wording quoted from the 1783 Treaty of Paris for the Great Lakes
    segment;
  * a death toll for the Rideau Canal beyond "hundreds", the canal's total
    construction cost, and any death toll at all for the Welland Canal;
  * the number of people moved for the Seaway, the number of buildings moved,
    and the inundation date;
  * Lake Ontario's water volume and its retention time;
  * peak lake levels in metres for 2017 and 2019, and any damage figure;
  * census populations for the Hamilton, Oshawa, St. Catharines-Niagara and
    Kingston metropolitan areas, and the Toronto CMA Indigenous total;
  * a count of First Nations, Metis or Tribal communities in the basin;
  * the number of people served by Toronto's four water plants.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="lake-ontario-history-and-people.html",
    section="History",
    title=T("Lake Ontario: The People, The Nations, The History",
            "Le lac Ontario : les peuples, les nations, l'histoire"),
    desc=T("Governments disagree about what the lake's name means, and none of them "
           "publishes a name for it in any Indigenous language. A plain, sourced history of "
           "the people of Lake Ontario — the Wendat, the Neutral, the Haudenosaunee, the "
           "Mississauga, the treaties, the towns, the canals and the fish.",
           "Les gouvernements ne s'entendent pas sur le sens du nom du lac, et aucun ne "
           "publie de nom pour ce lac dans une langue autochtone. Une histoire simple et "
           "sourcée des peuples du lac Ontario — les Wendats, les Neutres, les Haudenosaunee, "
           "les Mississaugas, les traités, les villes, les canaux et les poissons."),
    h1=T("\U0001F30A Lake Ontario: the people, the nations, the history",
         "\U0001F30A Le lac Ontario : les peuples, les nations, l'histoire"),
    hero=T("Eleven million people live around this lake today. The nations who lived on both "
           "of its shores were there for thousands of years before the border was drawn "
           "through the middle of it. This page follows the dates, the treaties, the "
           "settlements and the disagreements — and it stops where the official record stops.",
           "Onze millions de personnes vivent aujourd'hui autour de ce lac. Les nations qui "
           "habitaient ses deux rives y étaient depuis des milliers d'années avant qu'on ne "
           "trace une frontière au milieu de l'eau. Cette page suit les dates, les traités, "
           "les règlements et les désaccords — et elle s'arrête là où s'arrête le dossier "
           "officiel."),
    checked=T("Last checked 28 August 2026 — every figure here is attributed to the body "
              "that published it",
              "Dernière vérification le 28 août 2026 — chaque chiffre présenté ici est "
              "attribué à l'organisme qui l'a publié"),
)

# ------------------------------------------------------------------ 1
a.h2(T("Start with the name, because the governments disagree with each other",
       "Commençons par le nom, parce que les gouvernements ne s'entendent pas entre eux"))
a.p(T(
    "Four official pages explain where the name Ontario comes from. They do not say the same "
    "thing, and the difference is not small.",
    "Quatre pages officielles expliquent d'où vient le nom Ontario. Elles ne disent pas la "
    "même chose, et l'écart n'est pas mince."))
a.ul([
    T("Natural Resources Canada, on its official origin-of-names page dated 8 January 2025, "
      "writes that Ontario acquired its name from the Iroquois word kanadario, which "
      "translates into \"sparkling\" water.",
      "Ressources naturelles Canada, sur sa page officielle sur l'origine des noms datée du "
      "8 janvier 2025, écrit que l'Ontario tire son nom du mot iroquois kanadario, qui se "
      "traduit par eau « scintillante »."),
    T("Canadian Heritage, on its provincial symbols page dated 15 August 2017, gives the same "
      "reading: the word Ontario comes from the Iroquois word kanadario, meaning \"sparkling\" "
      "water.",
      "Patrimoine canadien, sur sa page des symboles provinciaux datée du 15 août 2017, donne "
      "la même lecture : le mot Ontario vient du mot iroquois kanadario, qui signifie eau "
      "« scintillante »."),
    T("The Government of Ontario, on its About Ontario page last modified 2 October 2025, "
      "gives that reading too.",
      "Le gouvernement de l'Ontario, sur sa page À propos de l'Ontario modifiée pour la "
      "dernière fois le 2 octobre 2025, donne aussi cette lecture."),
    T("Immigration, Refugees and Citizenship Canada, on a fact sheet dated 16 October 2017, "
      "gives a different meaning: the word Ontario is believed to come from the Iroquoian for "
      "\"vast body of water.\" Note that IRCC hedges with believed, and the other three do not "
      "hedge at all.",
      "Immigration, Réfugiés et Citoyenneté Canada, sur une fiche datée du 16 octobre 2017, "
      "donne un sens différent : on croit que le mot Ontario vient de l'iroquoien et signifie "
      "« vaste étendue d'eau ». Notez qu'IRCC nuance avec on croit, et que les trois autres "
      "ne nuancent pas du tout."),
])
a.p(T(
    "There is a second disagreement underneath the first, and it is about what was named in "
    "1641. Natural Resources Canada writes that the earliest recording of the name Ontario was "
    "in 1641, where it was used to describe a mass of land on the north shore of the "
    "easternmost part of the Great Lakes. That is land, not water. Immigration, Refugees and "
    "Citizenship Canada writes that the lake itself was first referred to by this name in the "
    "Jesuit Relations documents around 1641. Same year, same record, two different things "
    "being named.",
    "Un second désaccord se cache sous le premier, et il porte sur ce qui a été nommé en 1641. "
    "Ressources naturelles Canada écrit que la plus ancienne mention du nom Ontario date de "
    "1641, où il servait à décrire une masse de terre sur la rive nord de la partie la plus à "
    "l'est des Grands Lacs. C'est de la terre, pas de l'eau. Immigration, Réfugiés et "
    "Citoyenneté Canada écrit que le lac lui-même a été désigné pour la première fois par ce "
    "nom dans les documents des Relations des jésuites vers 1641. Même année, même document, "
    "deux choses différentes nommées."))
a.callout(T(
    "<strong>Not one of these sources says which language the word comes from.</strong> They "
    "write Iroquois or Iroquoian and stop. Iroquoian is a family of languages, not a language: "
    "Wendat, Kanyen'keha (Mohawk), Seneca, Onondaga, Cayuga and Oneida all belong to it. The "
    "spelling the pages print, kanadario, is a French-era transcription rather than a modern "
    "spelling in any of those writing systems. This page cannot tell you which language it "
    "came from, because no official source says.",
    "<strong>Aucune de ces sources ne dit de quelle langue vient le mot.</strong> Elles "
    "écrivent iroquois ou iroquoien, et s'arrêtent là. L'iroquoien est une famille de langues, "
    "et non une langue : le wendat, le kanyen'keha (mohawk), le seneca, l'onondaga, le cayuga "
    "et l'oneida en font tous partie. L'orthographe imprimée sur ces pages, kanadario, est une "
    "transcription de l'époque française plutôt qu'une graphie moderne dans l'un de ces "
    "systèmes d'écriture. Cette page ne peut pas vous dire de quelle langue le mot vient, "
    "parce qu'aucune source officielle ne le dit."))
a.p(T(
    "One more detail is worth noticing. On the very same Natural Resources Canada page, the "
    "name Canada is introduced with a hedge: it likely comes from the Huron-Iroquois word "
    "kanata, meaning village or settlement. Ontario gets no likely. The department is more "
    "confident about the harder claim than about the easier one.",
    "Un dernier détail mérite d'être remarqué. Sur cette même page de Ressources naturelles "
    "Canada, le nom Canada est présenté avec une nuance : il vient probablement du mot "
    "huron-iroquois kanata, qui signifie village ou peuplement. Ontario n'a droit à aucun "
    "probablement. Le ministère est plus sûr de l'affirmation la plus difficile que de la plus "
    "facile."))
a.p(T(
    "And a word about Toronto, because the two names are often mixed together. Natural "
    "Resources Canada says Toronto derives from an Iroquois term meaning \"where there are "
    "trees in water\" in reference to a weir for catching fish, and that Toronto gradually "
    "came to refer to a larger region that includes the site of the present city. The fish "
    "weir was at the narrows at Lake Simcoe, at the far end of a portage trail, not on the "
    "Lake Ontario shore. The name travelled south along the trail.",
    "Et un mot sur Toronto, parce que les deux noms sont souvent confondus. Ressources "
    "naturelles Canada indique que Toronto vient d'un terme iroquois signifiant « là où il y a "
    "des arbres dans l'eau », en référence à une pêcherie faite de pieux, et que Toronto en "
    "est venu peu à peu à désigner une région plus vaste comprenant l'emplacement de la ville "
    "actuelle. Cette pêcherie se trouvait au détroit du lac Simcoe, à l'autre bout d'un "
    "sentier de portage, et non sur la rive du lac Ontario. Le nom a voyagé vers le sud le "
    "long du sentier."))

# ------------------------------------------------------------------ 2
a.h2(T("The name that no government publishes",
       "Le nom qu'aucun gouvernement ne publie"))
a.p(T(
    "Here is the finding underneath the disagreement, and it took more searching to establish "
    "than any fact on this page. No permitted source publishes a name for Lake Ontario in any "
    "Indigenous language, attached to a nation and a language.",
    "Voici le constat qui se cache sous ce désaccord, et il a demandé plus de recherche que "
    "n'importe quel fait de cette page. Aucune source autorisée ne publie de nom du lac "
    "Ontario dans une langue autochtone, rattaché à une nation et à une langue."))
a.p(T(
    "The places looked at were the ones that would hold it: the geographical names pages and "
    "database of Natural Resources Canada, which is the federal names authority; the Ontario "
    "Geographic Names Board's own policy page, which is the provincial statutory authority; "
    "Parks Canada's designation records; the Ontario Heritage Trust; the Canadian Museum of "
    "History; Crown-Indigenous Relations and Northern Affairs Canada; Library and Archives "
    "Canada; and the websites of the First Nations of this lake themselves — the Mississaugas "
    "of the Credit, Six Nations of the Grand River, the Mohawks of the Bay of Quinte, "
    "Alderville, and the Huron-Wendat Nation at Wendake.",
    "Les endroits consultés sont ceux qui devraient le contenir : les pages et la base de "
    "données des noms géographiques de Ressources naturelles Canada, l'autorité fédérale en "
    "matière de noms ; la page de politique de la Commission de toponymie de l'Ontario, "
    "l'autorité provinciale prévue par la loi ; les fiches de désignation de Parcs Canada ; la "
    "Fiducie du patrimoine ontarien ; le Musée canadien de l'histoire ; Relations "
    "Couronne-Autochtones et Affaires du Nord Canada ; Bibliothèque et Archives Canada ; et "
    "les sites des Premières Nations de ce lac elles-mêmes — les Mississaugas of the Credit, "
    "les Six Nations of the Grand River, les Mohawks of the Bay of Quinte, Alderville et la "
    "Nation huronne-wendat à Wendake."))
a.p(T(
    "Ontario's own naming policy makes the silence stranger. The province publishes that it "
    "maintains approximately 60,000 official geographic names in English, French and "
    "Indigenous languages, and that for an Indigenous name without a standard orthography the "
    "Board shall seek a local Band Council Resolution as to the orthography of each geographic "
    "name to be approved. The machinery for publishing an Indigenous name exists and is "
    "described in detail. That same page says nothing at all about the origin or the meaning "
    "of the name of Lake Ontario.",
    "La politique de dénomination de l'Ontario rend ce silence encore plus étrange. La "
    "province publie qu'elle tient environ 60 000 noms géographiques officiels en anglais, en "
    "français et en langues autochtones, et que, pour un nom autochtone sans orthographe "
    "normalisée, la Commission doit demander une résolution du conseil de bande local quant à "
    "l'orthographe de chaque nom géographique à approuver. Le mécanisme pour publier un nom "
    "autochtone existe et il est décrit en détail. Cette même page ne dit rien du tout sur "
    "l'origine ni sur le sens du nom du lac Ontario."))
a.callout(T(
    "<strong>Read this carefully, because it is an absence and not a claim.</strong> This page "
    "is not saying that the nations of this lake have no name for it. Of course they do, and "
    "always did. What can be said, and all that can be said, is narrower: the governments that "
    "publish the acreage of an 1805 treaty to the single acre, and the exact date a plaque was "
    "unveiled, do not publish a Wendat, Haudenosaunee or Anishinaabe name for this water. "
    "Several spellings circulate online. None of them was found on a government, museum, "
    "university or First Nation source, so none of them is printed here.",
    "<strong>Lisez ceci attentivement, car il s'agit d'une absence et non d'une "
    "affirmation.</strong> Cette page ne dit pas que les nations de ce lac n'ont pas de nom "
    "pour lui. Bien sûr qu'elles en ont un, et depuis toujours. Ce qu'on peut dire, et tout ce "
    "qu'on peut dire, est plus étroit : les gouvernements qui publient la superficie d'un "
    "traité de 1805 à l'acre près, et la date exacte du dévoilement d'une plaque, ne publient "
    "aucun nom wendat, haudenosaunee ou anishinaabe pour cette eau. Plusieurs graphies "
    "circulent en ligne. Aucune n'a été trouvée sur une source gouvernementale, muséale, "
    "universitaire ou d'une Première Nation ; aucune n'est donc imprimée ici."))
a.p(T(
    "The French historical names are missing in the same way. The names often attached to this "
    "lake in older French writing were not found on any permitted page either. Library and "
    "Archives Canada holds and describes Champlain's 1632 map of New France, and its page "
    "discusses what the map speculates about a frozen ocean to the north, but it does not say "
    "how the lake is labelled. What the French record does document, plainly and with dates, "
    "is the forts they built on the lake and the officials they named them after.",
    "Les noms historiques français manquent de la même façon. Les noms souvent attachés à ce "
    "lac dans les écrits français anciens n'ont été trouvés sur aucune page autorisée non "
    "plus. Bibliothèque et Archives Canada conserve et décrit la carte de la Nouvelle-France "
    "dressée par Champlain en 1632, et sa page traite de ce que la carte suppose au sujet d'un "
    "océan glacial au nord, mais elle ne dit pas comment le lac y est désigné. Ce que le "
    "dossier français documente clairement, avec des dates, ce sont les forts que les Français "
    "ont bâtis sur le lac et les fonctionnaires dont ils leur ont donné le nom."))

# ------------------------------------------------------------------ 3
a.h2(T("How to read the plaques quoted on this page",
       "Comment lire les plaques citées dans cette page"))
a.p(T(
    "Much of what follows is quoted from bronze plaques put up by the Government of Canada "
    "over the last hundred years. They are useful because they are dated, official and "
    "precise. They are also, in several cases, written in language the government itself no "
    "longer stands behind.",
    "Une grande partie de ce qui suit est citée de plaques de bronze installées par le "
    "gouvernement du Canada au cours du dernier siècle. Elles sont utiles parce qu'elles sont "
    "datées, officielles et précises. Elles sont aussi, dans plusieurs cas, rédigées dans une "
    "langue que le gouvernement lui-même ne défend plus."))
a.p(T(
    "Parks Canada has flagged seven of the designations quoted on this page for review, "
    "because of what it calls outdated language or terminology, absence of a significant layer "
    "of history, factual errors, controversial beliefs and behaviour, or significant new "
    "knowledge. The seven are the Toronto Carrying Place, the Carrying Place of the Bay of "
    "Quinte, Étienne Brûlé, Samuel de Champlain, the Six Nations event, Thayendanega (Joseph "
    "Brant), and the Wyandot (Hurons) event.",
    "Parcs Canada a signalé sept des désignations citées dans cette page comme devant être "
    "révisées, en raison de ce qu'il appelle un langage ou une terminologie désuets, l'absence "
    "d'un pan important de l'histoire, des erreurs factuelles, des croyances et des "
    "comportements controversés, ou des connaissances nouvelles importantes. Les sept sont le "
    "passage de Toronto, le passage de la baie de Quinte, Étienne Brûlé, Samuel de Champlain, "
    "l'événement des Six Nations, Thayendanega (Joseph Brant) et l'événement des Wyandots "
    "(Hurons)."))
a.callout(T(
    "<strong>Every plaque quotation on this page is what the Canadian state said at the time "
    "it said it, and is dated for that reason.</strong> It is not a current official statement "
    "of fact, and where Parks Canada has marked a designation for review this page says so at "
    "the point of quotation.",
    "<strong>Chaque citation de plaque dans cette page est ce que l'État canadien a dit au "
    "moment où il l'a dit, et elle est datée pour cette raison.</strong> Ce n'est pas une "
    "déclaration officielle actuelle, et lorsque Parcs Canada a signalé une désignation comme "
    "devant être révisée, cette page le mentionne à l'endroit même de la citation."))

# ------------------------------------------------------------------ 4
a.h2(T("The lake is younger than the people",
       "Le lac est plus jeune que les gens"))
a.p(T(
    "Parks Canada's geology page for Rouge National Urban Park, dated 1 April 2026, sets the "
    "ceiling on every claim about how long people have been on this shore. About 20,000 years "
    "ago the Laurentide Ice Sheet reached its maximum size, and the ice over what is now "
    "Toronto was approximately one kilometre thick. The ice began retreating 14,000 years ago, "
    "and by about 13,000 years ago it had disappeared from the Lake Ontario basin.",
    "La page de géologie de Parcs Canada pour le parc urbain national de la Rouge, datée du "
    "1er avril 2026, fixe la limite de toute affirmation sur la durée de la présence humaine "
    "sur cette rive. Il y a environ 20 000 ans, l'Inlandsis laurentidien atteignait sa taille "
    "maximale, et la glace au-dessus de l'actuelle Toronto avait environ un kilomètre "
    "d'épaisseur. La glace a commencé à reculer il y a 14 000 ans et, il y a environ "
    "13 000 ans, elle avait disparu du bassin du lac Ontario."))
a.p(T(
    "What followed was not this lake. Glacial Lake Iroquois, which Parks Canada calls a larger "
    "predecessor of Lake Ontario, stood 60 metres higher than Lake Ontario, and its shoreline "
    "was located 4 to 15 km further inland — it runs through the area of the Toronto Zoo and "
    "the former Beare Road landfill. About 12,000 years ago the ice in the St. Lawrence Valley "
    "broke up, the lake drained, and levels fell to 20 metres below modern-day levels, forming "
    "a smaller lake known as Lake Admiralty. Only by about 8,000 years ago, as the land in the "
    "east rebounded and raised the outlet, did the lake take the shape it has now.",
    "Ce qui a suivi n'était pas ce lac-ci. Le lac glaciaire Iroquois, que Parcs Canada appelle "
    "un prédécesseur plus vaste du lac Ontario, se trouvait 60 mètres plus haut que le lac "
    "Ontario, et son rivage était situé de 4 à 15 km plus loin à l'intérieur des terres — il "
    "passe par le secteur du zoo de Toronto et de l'ancien dépotoir du chemin Beare. Il y a "
    "environ 12 000 ans, la glace de la vallée du Saint-Laurent s'est rompue, le lac s'est "
    "vidé et les niveaux sont tombés à 20 mètres sous les niveaux actuels, formant un lac plus "
    "petit appelé lac Admiralty. Ce n'est qu'il y a environ 8 000 ans, quand les terres de "
    "l'est se sont relevées et ont haussé l'exutoire, que le lac a pris sa forme actuelle."))
a.callout(T(
    "<strong>The present shoreline is roughly 8,000 years old, and that matters for the "
    "history.</strong> Anything older than that sits under water or well inland of today's "
    "beach. When the earliest coastal record looks thin, the reason is partly that the "
    "earliest coast is drowned — not that nobody was living on it.",
    "<strong>Le rivage actuel a environ 8 000 ans, et cela compte pour l'histoire.</strong> "
    "Tout ce qui est plus ancien se trouve sous l'eau ou bien à l'intérieur des terres par "
    "rapport à la plage d'aujourd'hui. Si les traces côtières les plus anciennes semblent "
    "rares, c'est en partie parce que la côte la plus ancienne est noyée — et non parce que "
    "personne n'y vivait."))
a.p(T(
    "How long people have been here is given three different ways, and the sources should be "
    "read side by side rather than merged. The Ontario Heritage Trust writes that Indigenous "
    "peoples have been here for more than 10,000 years, naming the Anishinaabek, Haudenosaunee, "
    "Cree and Wendat peoples. The Trust's article on the archaeology of southwestern Ontario "
    "puts the earliest human presence at 11,000 years, with repeated campsite visits between "
    "11,000 and 10,400 years ago near Parkhill and Thedford. The University of Toronto "
    "Libraries' research guide says Toronto has been a site of human activity for 15,000 "
    "years, which is hard to square with Parks Canada's date for ice leaving the basin, and is "
    "printed here with that caution attached.",
    "La durée de la présence humaine ici est donnée de trois façons différentes, et il faut "
    "lire les sources côte à côte plutôt que de les fondre ensemble. La Fiducie du patrimoine "
    "ontarien écrit que les peuples autochtones sont ici depuis plus de 10 000 ans, en nommant "
    "les Anishinaabeks, les Haudenosaunee, les Cris et les Wendats. L'article de la Fiducie "
    "sur l'archéologie du sud-ouest de l'Ontario situe la plus ancienne présence humaine à "
    "11 000 ans, avec des séjours répétés dans des campements entre 11 000 et 10 400 ans avant "
    "aujourd'hui, près de Parkhill et de Thedford. Le guide de recherche des bibliothèques de "
    "l'Université de Toronto indique que Toronto est un lieu d'activité humaine depuis "
    "15 000 ans, ce qui se concilie mal avec la date de Parcs Canada pour le retrait des "
    "glaces du bassin, et ce chiffre est imprimé ici avec cette mise en garde."))
a.p(T(
    "One dated point on the shore itself settles the question better than any round number. At "
    "Bead Hill, in Scarborough, inside what is now Rouge National Urban Park, Parks Canada "
    "records an Archaic period campsite dating from roughly 3000 BCE — a directly dated "
    "occupation on the Lake Ontario shore, five thousand years old, on the same headland where "
    "a Seneca village would stand much later.",
    "Un point daté sur la rive elle-même règle la question mieux que n'importe quel chiffre "
    "rond. À Bead Hill, à Scarborough, dans ce qui est aujourd'hui le parc urbain national de "
    "la Rouge, Parcs Canada consigne un campement de la période archaïque datant d'environ "
    "3000 av. J.-C. — une occupation datée directement sur la rive du lac Ontario, vieille de "
    "cinq mille ans, sur la même pointe où se dressera bien plus tard un village seneca."))
a.p(T(
    "Farming came later, and the Canadian Museum of History is careful about when. It writes "
    "that corn, squash and sunflower farming marked a veritable food revolution that began in "
    "the early 14th century, and that the corn grown was Northern Flint, which matures "
    "quickly, in about 100 days or so — a variety that can finish a season this far north. The "
    "museum also records that scholars are split on when Iroquoian village life begins: some "
    "believe it can be seen starting in the fifth century of the common era, while others "
    "believe these peoples can only truly be dated to the 14th century. Ontario, for its part, "
    "publishes that over 80% of all archaeological sites in the province were inhabited by "
    "Indigenous peoples, including villages, longhouses, campsites, and portage areas.",
    "L'agriculture est venue plus tard, et le Musée canadien de l'histoire est prudent quant à "
    "la date. Il écrit que la culture du maïs, de la courge et du tournesol a marqué une "
    "véritable révolution alimentaire qui a commencé au début du XIVe siècle, et que le maïs "
    "cultivé était le Northern Flint, qui mûrit vite, en une centaine de jours environ — une "
    "variété capable de boucler une saison aussi loin au nord. Le musée consigne aussi que les "
    "spécialistes sont divisés sur le début de la vie villageoise iroquoienne : certains "
    "croient qu'on peut la voir apparaître dès le Ve siècle de notre ère, tandis que d'autres "
    "estiment qu'on ne peut vraiment dater l'établissement de ces peuples qu'au XIVe siècle. "
    "L'Ontario, de son côté, publie que plus de 80 % de tous les sites archéologiques de la "
    "province ont été habités par des peuples autochtones, y compris des villages, des maisons "
    "longues, des campements et des aires de portage."))

# ------------------------------------------------------------------ 5
a.h2(T("The north shore in four phases, not two",
       "La rive nord en quatre phases, et non en deux"))
a.p(T(
    "The usual short version of this history has two chapters: Indigenous peoples, then "
    "Europeans. The official record does not support that shape. Within about two hundred "
    "years the north shore of Lake Ontario was held by four different groups of nations in "
    "turn, and each transition is dated and designated. Getting this sequence wrong is the "
    "most common error in writing about the Toronto area.",
    "La version courte habituelle de cette histoire compte deux chapitres : les peuples "
    "autochtones, puis les Européens. Le dossier officiel ne soutient pas cette forme. En "
    "environ deux cents ans, la rive nord du lac Ontario a été tenue tour à tour par quatre "
    "groupes de nations différents, et chaque transition est datée et désignée. Se tromper sur "
    "cette séquence est l'erreur la plus courante dans les écrits sur la région de Toronto."))
a.table(
    [T("When", "Quand"), T("Who", "Qui"), T("What the record shows", "Ce que montre le dossier")],
    [[T("To about 1600", "Jusque vers 1600"),
      T("Ancestral Wendat", "Wendats ancestraux"),
      T("Large palisaded villages on the north shore, including the Jean-Baptiste Lainé site, "
        "abandoned sometime before A.D. 1600.",
        "De grands villages palissadés sur la rive nord, dont le site Jean-Baptiste-Lainé, "
        "abandonné avant l'an 1600.")],
     [T("About 1550 to 1651", "Vers 1550 à 1651"),
      T("Neutral / Attiwandaron", "Neutres / Attiwandarons"),
      T("At the western end of the lake, in the Hamilton area, after moving east from the "
        "Thames around 1550.",
        "À l'extrémité ouest du lac, dans la région de Hamilton, après un déplacement vers "
        "l'est depuis la Thames vers 1550.")],
     [T("To 1649 and 1650", "Jusqu'en 1649 et 1650"),
      T("Wendat, in Huronia", "Wendats, en Huronie"),
      T("Consolidated north of the lake, near Georgian Bay, until the attacks of 1649 and the "
        "dispersal of 1650.",
        "Regroupés au nord du lac, près de la baie Georgienne, jusqu'aux attaques de 1649 et à "
        "la dispersion de 1650.")],
     [T("About 1665 to about 1688", "Vers 1665 à vers 1688"),
      T("Haudenosaunee, mainly Seneca", "Haudenosaunee, surtout Senecas"),
      T("Villages at Ganatsekwyagon on the Rouge and Teiaiagon on the Humber, both dated, both "
        "designated.",
        "Des villages à Ganatsekwyagon sur la Rouge et à Teiaiagon sur la Humber, tous deux "
        "datés et désignés.")],
     [T("From the early 1700s", "À partir du début des années 1700"),
      T("Mississauga (Anishinaabe)", "Mississaugas (Anishinaabes)"),
      T("Settling on the lower Humber and along the north shore, in the Nation's own account "
        "as the result of their own campaign.",
        "Établis sur le cours inférieur de la Humber et le long de la rive nord, selon le "
        "récit de la Nation elle-même, à l'issue de leur propre campagne.")]],
    label=T("Who held the north shore of Lake Ontario, and when — scroll sideways to see all "
            "of it",
            "Qui occupait la rive nord du lac Ontario, et quand — faites défiler latéralement "
            "pour tout voir"))

a.h3(T("The Wendat village at Jean-Baptiste Lainé",
       "Le village wendat de Jean-Baptiste-Lainé"))
a.p(T(
    "North of the lake at Whitchurch-Stouffville, ancestral Wendat families built and lived in "
    "one of the largest villages ever excavated in this part of the country. The Ontario "
    "Heritage Trust's background paper puts its population at an estimated 1,700 people, on a "
    "three-hectare settlement whose early phase covered 2.9 hectares, surrounded by a "
    "palisade, a ditch and an embankment as protection. It was occupied in the early 16th "
    "century and abandoned sometime before A.D. 1600.",
    "Au nord du lac, à Whitchurch-Stouffville, des familles wendates ancestrales ont bâti et "
    "habité l'un des plus grands villages jamais fouillés dans cette partie du pays. Le "
    "document d'information de la Fiducie du patrimoine ontarien en estime la population à "
    "1 700 personnes, sur un établissement de trois hectares dont la phase initiale couvrait "
    "2,9 hectares, entouré d'une palissade, d'un fossé et d'un remblai en guise de protection. "
    "Il a été occupé au début du XVIe siècle et abandonné avant l'an 1600."))
a.p(T(
    "The Trust's own material carries two counts of the longhouses, and both are printed here "
    "because the Trust prints both. The excavation revealed 98 longhouses across the site's "
    "phases; the plaque, which is the conservative public figure, says more than 50 longhouses.",
    "Les documents de la Fiducie donnent deux décomptes des maisons longues, et les deux sont "
    "imprimés ici parce que la Fiducie imprime les deux. La fouille a révélé 98 maisons "
    "longues au fil des phases du site ; la plaque, qui retient le chiffre prudent destiné au "
    "public, indique plus de 50 maisons longues."))
a.callout(T(
    "<strong>Among the finds was a fragment of a Basque iron tool.</strong> European metal "
    "reached this inland village before any European did. The trade networks of the Great "
    "Lakes were already carrying goods hundreds of kilometres inland while the people who made "
    "those goods were still on the coast.",
    "<strong>Parmi les objets trouvés se trouvait un fragment d'outil de fer basque.</strong> "
    "Le métal européen a atteint ce village de l'intérieur avant tout Européen. Les réseaux "
    "d'échange des Grands Lacs transportaient déjà des marchandises à des centaines de "
    "kilomètres à l'intérieur des terres alors que ceux qui les fabriquaient étaient encore "
    "sur la côte."))
a.p(T(
    "The people who lived there were ancestral Wendat, and the Trust records that descendants "
    "of this community would become members of the Huron-Wendat Confederacy by 1615. The site "
    "was renamed in 2012 after Jean-Baptiste Lainé, an esteemed Huron-Wendat veteran who "
    "fought during the Second World War; older writing calls it the Mantle site. The plaque was "
    "unveiled on 25 August 2017 at Wendat Village Public School in Whitchurch-Stouffville, and "
    "it opens by saying that in the 16th century, prior to the arrival of Europeans, a village "
    "was founded on this site by the Huron-Wendat, and closes by calling the site significant "
    "to our understanding of Huron-Wendat socio-economic and political history.",
    "Les gens qui y vivaient étaient des Wendats ancestraux, et la Fiducie consigne que des "
    "descendants de cette communauté allaient devenir membres de la Confédération "
    "huronne-wendate en 1615. Le site a été renommé en 2012 en l'honneur de Jean-Baptiste "
    "Lainé, un vétéran huron-wendat estimé qui a combattu pendant la Seconde Guerre mondiale ; "
    "les écrits plus anciens l'appellent le site Mantle. La plaque a été dévoilée le 25 août "
    "2017 à l'école publique Wendat Village, à Whitchurch-Stouffville, et elle commence en "
    "disant qu'au XVIe siècle, avant l'arrivée des Européens, un village a été fondé sur ce "
    "site par les Hurons-Wendats, et se termine en qualifiant le site d'important pour notre "
    "compréhension de l'histoire socioéconomique et politique huronne-wendate."))

a.h3(T("The Neutral, at the western end, who are usually left out",
       "Les Neutres, à l'extrémité ouest, qu'on oublie d'habitude"))
a.p(T(
    "Lake Ontario histories tend to jump from the Wendat to the Haudenosaunee and skip the "
    "nation that held the head of the lake. The Attiwandaron — called the Neutral Iroquois, or "
    "la nation Neutre, by 17th-century French writers — were Iroquoian-speaking and were not "
    "part of the Haudenosaunee Confederacy.",
    "Les histoires du lac Ontario ont tendance à sauter des Wendats aux Haudenosaunee et à "
    "omettre la nation qui tenait la tête du lac. Les Attiwandarons — que les auteurs français "
    "du XVIIe siècle appelaient les Iroquois neutres, ou la nation Neutre — parlaient une "
    "langue iroquoienne et ne faisaient pas partie de la Confédération haudenosaunee."))
a.p(T(
    "Two designated sites hold their story with dates. At Southwold Earthworks, a national "
    "historic site designated on 25 May 1923, the village is dated to approximately A.D. "
    "1450-1550, several hundred people lived there, and the place is marked by a double ring "
    "of low earthen mounds that surround the site — a feature rare in southern Ontario. At the "
    "Norton Attawandaron site on the Thames at London, occupied around 1400, the record "
    "describes nine longhouses, a palisade, a sweat lodge, hearths and storage and refuse pits, "
    "and roughly 500 to 1,000 inhabitants.",
    "Deux sites désignés portent leur histoire avec des dates. Aux Earthworks de Southwold, "
    "lieu historique national désigné le 25 mai 1923, le village est daté d'environ 1450-1550, "
    "plusieurs centaines de personnes y vivaient, et l'endroit est marqué par un double anneau "
    "de basses buttes de terre qui entourent le site — une caractéristique rare dans le sud de "
    "l'Ontario. Au site Norton Attawandaron, sur la Thames à London, occupé vers 1400, le "
    "dossier décrit neuf maisons longues, une palissade, une hutte de sudation, des foyers, "
    "des fosses de stockage et de rebut, et environ 500 à 1 000 habitants."))
a.p(T(
    "The movement matters more than either site on its own. The federal register records that "
    "around 1550 they relocated eastward to the Hamilton area, later becoming part of the "
    "Neutral Confederacy. That places the Neutral at the western end of Lake Ontario for the "
    "whole century before contact — the head of the lake, where Hamilton and Burlington stand "
    "now.",
    "Le déplacement importe plus que chacun des sites pris séparément. Le registre fédéral "
    "consigne que, vers 1550, ils se sont déplacés vers l'est jusqu'à la région de Hamilton, "
    "avant de faire partie de la Confédération neutre. Cela situe les Neutres à l'extrémité "
    "ouest du lac Ontario pendant tout le siècle qui a précédé le contact — la tête du lac, là "
    "où se trouvent aujourd'hui Hamilton et Burlington."))
a.p(T(
    "Their ending is recorded in one hard sentence. The register states that the Neutral were "
    "dispersed or incorporated into the Five Nations Iroquois during the years 1647 to 1651, "
    "with no distinct descendant population remaining today. That is the government's wording, "
    "and it should not be softened.",
    "Leur fin est consignée en une phrase dure. Le registre indique que les Neutres ont été "
    "dispersés ou incorporés aux Iroquois des Cinq-Nations entre 1647 et 1651, sans population "
    "descendante distincte subsistant aujourd'hui. C'est la formulation du gouvernement, et "
    "elle ne doit pas être adoucie."))

a.h3(T("Huronia, and the year everything changed",
       "La Huronie, et l'année où tout a changé"))
a.p(T(
    "By the early 17th century the Wendat had consolidated north of the lake, in Huronia near "
    "Georgian Bay, and they were the hinge of the northern trade. Two pressures broke that "
    "position, and the Canadian Museum of History names both. During the smallpox epidemics of "
    "1634 to 1640 the Hurons lost between a half to two-thirds of their total population, "
    "creating generational imbalances that weakened their ability to resist Iroquois attacks. "
    "Parks Canada adds that intensified Iroquois attacks, along with social divisions and "
    "internal conflicts caused by conversions to Christianity, destabilised Huronia from "
    "inside as well.",
    "Au début du XVIIe siècle, les Wendats s'étaient regroupés au nord du lac, en Huronie près "
    "de la baie Georgienne, et ils étaient la charnière du commerce nordique. Deux pressions "
    "ont brisé cette position, et le Musée canadien de l'histoire nomme les deux. Pendant les "
    "épidémies de variole de 1634 à 1640, les Hurons ont perdu entre la moitié et les deux "
    "tiers de leur population totale, ce qui a créé des déséquilibres entre les générations et "
    "affaibli leur capacité de résister aux attaques iroquoises. Parcs Canada ajoute que "
    "l'intensification des attaques iroquoises, avec les divisions sociales et les conflits "
    "internes causés par les conversions au christianisme, a aussi déstabilisé la Huronie de "
    "l'intérieur."))
a.p(T(
    "Parks Canada dates the attacks precisely. On 16 March 1649 the Five Nations Iroquois "
    "attacked the mission of St. Ignace II, capturing the Jesuits Brebeuf and Lalemant, then "
    "attacked Saint-Louis the same morning, and returned to St. Ignace II where the two priests "
    "were killed the following day. In the winter of 1648-49 the Jesuits had already abandoned "
    "and burned Sainte-Marie and moved with Wendat converts to Christian Island. Parks Canada "
    "writes that the raids triggered the abandonment of Huronia by 1650.",
    "Parcs Canada date les attaques avec précision. Le 16 mars 1649, les Iroquois des "
    "Cinq-Nations ont attaqué la mission Saint-Ignace II, capturant les jésuites Brébeuf et "
    "Lalemant, puis ont attaqué Saint-Louis le même matin, et sont revenus à Saint-Ignace II, "
    "où les deux prêtres ont été tués le lendemain. À l'hiver 1648-1649, les jésuites avaient "
    "déjà abandonné et incendié Sainte-Marie et étaient partis avec des convertis wendats vers "
    "l'île Christian. Parcs Canada écrit que les raids ont provoqué l'abandon de la Huronie "
    "en 1650."))
a.callout(T(
    "<strong>The dispersal was not a disappearance, and the Wendat are not a past-tense "
    "people.</strong> Parks Canada's own 1997 designation is called the Dispersal of "
    "Huron-Wendat from Huronia, and its plaque at Wendake, Quebec, records that devastated by "
    "famine, conflict, and contagious diseases from Europe, they dispersed from their ancestral "
    "lands in 1650 — and that roughly 150 survivors, predominantly Attigeoniongnahak, "
    "re-established their community near the Kabir Kouba Falls in 1697. The Huron-Wendat "
    "Nation is at Wendake today. Wyandot and Wyandotte communities continue in the United "
    "States.",
    "<strong>La dispersion n'a pas été une disparition, et les Wendats ne sont pas un peuple au "
    "passé.</strong> La désignation de 1997 de Parcs Canada s'intitule elle-même Dispersion "
    "des Hurons-Wendats de la Huronie, et sa plaque à Wendake, au Québec, consigne que, "
    "dévastés par la famine, les conflits et les maladies contagieuses venues d'Europe, ils se "
    "sont dispersés de leurs terres ancestrales en 1650 — et qu'environ 150 survivants, "
    "principalement des Attigeoniongnahaks, ont rétabli leur communauté près des chutes Kabir "
    "Kouba en 1697. La Nation huronne-wendate est à Wendake aujourd'hui. Des communautés "
    "wyandotes se perpétuent aux États-Unis."))
a.p(T(
    "One plaque from that period shows why old commemorative text needs a date attached. The "
    "Wyandot (Hurons) national historic event, designated on 26 May 1953, carries a plaque at "
    "Amherstburg reading that this area was once the home of the Wyandot, remnants of the "
    "Huron, Neutrals, and Petuns who were dispersed by the Iroquois in the 1640s. It records "
    "that survivors resettled near Detroit and took the Wyandot name, allied with the British "
    "in the Revolution, that many remained neutral in 1812, and that by the 1840s some "
    "relocated to Kansas. Parks Canada has flagged this designation for review.",
    "Une plaque de cette période montre pourquoi un texte commémoratif ancien a besoin d'une "
    "date. L'événement historique national des Wyandots (Hurons), désigné le 26 mai 1953, "
    "porte à Amherstburg une plaque indiquant que cette région fut jadis le foyer des "
    "Wyandots, restes des Hurons, des Neutres et des Pétuns dispersés par les Iroquois dans "
    "les années 1640. Elle consigne que des survivants se sont réinstallés près de Détroit et "
    "ont pris le nom de Wyandots, se sont alliés aux Britanniques pendant la Révolution, que "
    "beaucoup sont restés neutres en 1812, et que, dans les années 1840, certains sont partis "
    "au Kansas. Parcs Canada a signalé cette désignation comme devant être révisée."))

a.h3(T("Ganatsekwyagon and Teiaiagon: the Seneca villages on the north shore",
       "Ganatsekwyagon et Teiaiagon : les villages senecas de la rive nord"))
a.p(T(
    "The north shore was not empty after 1650. Two Seneca villages stood on it, both dated in "
    "official records, both designated, and both sitting where a river meets the lake at the "
    "foot of a portage route.",
    "La rive nord n'était pas vide après 1650. Deux villages senecas s'y dressaient, tous deux "
    "datés dans des dossiers officiels, tous deux désignés, et tous deux situés là où une "
    "rivière rejoint le lac, au pied d'une route de portage."))
a.p(T(
    "Ganatsekwyagon, at Bead Hill on the Rouge in Scarborough, is a national historic site "
    "designated on 22 November 1991. Parks Canada dates the village and its burial ground to "
    "circa 1665-1687 CE, when they were used by the Seneca, members of the Iroquois "
    "Confederacy. The site holds the historic Seneca village and an associated burial area, a "
    "tree-covered midden on the hillside, the Archaic campsite from roughly 3000 BCE, and "
    "further burials on the tip of the point. Survey has recovered numerous small artifacts "
    "such as glass beads, ceramic smoking pipes and European gunflints. It was found in the "
    "late 19th century and has never undergone large-scale excavations, which is exactly why it "
    "is so well preserved.",
    "Ganatsekwyagon, à Bead Hill sur la Rouge à Scarborough, est un lieu historique national "
    "désigné le 22 novembre 1991. Parcs Canada date le village et son aire de sépulture "
    "d'environ 1665-1687, lorsqu'ils étaient utilisés par les Senecas, membres de la "
    "Confédération iroquoise. Le site comprend le village seneca historique et une aire de "
    "sépulture associée, un dépotoir boisé sur le versant, le campement archaïque d'environ "
    "3000 av. J.-C., ainsi que d'autres sépultures à la pointe du promontoire. Les "
    "prospections ont livré de nombreux petits objets comme des perles de verre, des pipes en "
    "céramique et des pierres à fusil européennes. Le site a été repéré à la fin du XIXe "
    "siècle et n'a jamais fait l'objet de fouilles à grande échelle, ce qui explique justement "
    "son excellent état de conservation."))
a.p(T(
    "Teiaiagon stood on the Humber at what is now Baby Point in Toronto. The City of Toronto's "
    "December 2024 planning study, drawing on scholarship from 1981, records that the village "
    "was probably established shortly after 1673 and likely consisted of 20 to 30 longhouses "
    "that provided shelter for 500 to 800 people. Those numbers are a scholarly estimate rather "
    "than an excavation result, and the study says so itself: any account of what the village "
    "looked like requires synthesizing limited eyewitness accounts, preliminary archaeological "
    "work and anthropological data.",
    "Teiaiagon se dressait sur la Humber, à l'emplacement actuel de Baby Point à Toronto. "
    "L'étude d'urbanisme de la Ville de Toronto de décembre 2024, s'appuyant sur des travaux "
    "de 1981, consigne que le village a probablement été établi peu après 1673 et comptait "
    "vraisemblablement de 20 à 30 maisons longues abritant de 500 à 800 personnes. Ces "
    "chiffres sont une estimation savante et non un résultat de fouille, et l'étude le dit "
    "elle-même : toute description de l'aspect du village exige de synthétiser des témoignages "
    "oculaires limités, des travaux archéologiques préliminaires et des données "
    "anthropologiques."))
a.p(T(
    "The same study dates the ending: the specific Seneca presence at Teiaiagon ended in "
    "approximately 1688, as the Five Nations withdrew in response to increasing military "
    "actions by the French colonial government. That is the cause the record gives, and it is "
    "worth holding on to — the Haudenosaunee left the north shore under military pressure from "
    "New France, not because the land emptied itself.",
    "La même étude date la fin : la présence seneca proprement dite à Teiaiagon a pris fin vers "
    "1688, les Cinq-Nations s'étant retirées en réaction aux actions militaires croissantes du "
    "gouvernement colonial français. C'est la cause que donne le dossier, et il vaut la peine "
    "de la retenir : les Haudenosaunee ont quitté la rive nord sous la pression militaire de "
    "la Nouvelle-France, et non parce que le territoire se serait vidé de lui-même."))
a.p(T(
    "What happened to the village afterward is part of its history and not a footnote. David "
    "Boyle's survey in 1888 found stone gouges, a bird stone and a conical ring, and concluded "
    "there must have been at one time a considerable Indian population. During house "
    "construction between 1913 and the 1920s burials were frequently unearthed and received "
    "little consideration. Gas-line work in 1999 and again in 2006 disturbed burials containing "
    "brass rings, kettles and antler combs; those remains were later reburied along the Humber. "
    "The area is now the Teiaiagon-Baby Point Heritage Conservation District.",
    "Ce qui est arrivé au village par la suite fait partie de son histoire et n'est pas une "
    "note de bas de page. La prospection de David Boyle en 1888 a mis au jour des gouges de "
    "pierre, une pierre-oiseau et un anneau conique, et il en a conclu qu'il avait dû y avoir "
    "autrefois une population indienne considérable. Pendant la construction de maisons entre "
    "1913 et les années 1920, des sépultures ont été fréquemment mises au jour et n'ont reçu "
    "que peu d'égards. Des travaux de canalisation de gaz en 1999, puis en 2006, ont perturbé "
    "des sépultures contenant des anneaux de laiton, des chaudrons et des peignes en bois de "
    "cervidé ; ces restes ont ensuite été réinhumés le long de la Humber. Le secteur constitue "
    "aujourd'hui le district de conservation du patrimoine Teiaiagon-Baby Point."))

a.h3(T("The Mississauga, in the Nation's own words",
       "Les Mississaugas, dans les mots de la Nation elle-même"))
a.p(T(
    "For the fourth phase the best source is not a government at all. The Mississaugas of the "
    "Credit First Nation publish their own account, and in it they are the subject of the "
    "sentences.",
    "Pour la quatrième phase, la meilleure source n'est pas un gouvernement du tout. Les "
    "Mississaugas of the Credit First Nation publient leur propre récit, et ils y sont le "
    "sujet des phrases."))
a.p(T(
    "The Nation writes that its ancestors originated north of Lake Superior and the area around "
    "Georgian Bay, and relocated to Southern Ontario following conflicts with the Iroquois "
    "Confederacy in the mid-17th century. On what happened next, the Nation's wording is "
    "direct: after the Iroquois expelled the Huron in 1649-50, by the end of the 17th century "
    "the Mississaugas and their allies had succeeded in driving the Iroquois back into their "
    "homelands south of Lake Ontario.",
    "La Nation écrit que ses ancêtres sont originaires du nord du lac Supérieur et de la "
    "région de la baie Georgienne, et qu'ils se sont déplacés vers le sud de l'Ontario à la "
    "suite de conflits avec la Confédération iroquoise au milieu du XVIIe siècle. Sur la suite, "
    "la formulation de la Nation est directe : après que les Iroquois eurent chassé les Hurons "
    "en 1649-1650, à la fin du XVIIe siècle, les Mississaugas et leurs alliés avaient réussi à "
    "repousser les Iroquois vers leurs terres d'origine au sud du lac Ontario."))
a.callout(T(
    "<strong>That sentence is the whole point of this section.</strong> The north shore did not "
    "become Mississauga territory because it was empty and somebody filled it. The Nation's own "
    "published history describes a campaign they fought and won. The City of Toronto's planning "
    "study adds that the Mississauga are referenced in a number of documentary sources as "
    "settling on the lower Humber River in the early 1700s, and likely used the former "
    "Teiaiagon site seasonally or year-round.",
    "<strong>Cette phrase résume tout le propos de cette section.</strong> La rive nord n'est "
    "pas devenue territoire mississauga parce qu'elle était vide et que quelqu'un l'a remplie. "
    "L'histoire publiée par la Nation elle-même décrit une campagne qu'ils ont menée et "
    "gagnée. L'étude d'urbanisme de la Ville de Toronto ajoute que les Mississaugas sont "
    "mentionnés dans plusieurs sources documentaires comme s'établissant sur le cours "
    "inférieur de la rivière Humber au début des années 1700, et qu'ils ont probablement "
    "utilisé l'ancien site de Teiaiagon de façon saisonnière ou à l'année."))
a.p(T(
    "The Nation also publishes the extent of what it held: the Mississaugas occupied, "
    "controlled and exercised stewardship over approximately 3.9 million acres of southern "
    "Ontario, from the Rouge River Valley westward across to the headwaters of the Thames "
    "River, down to Long Point on Lake Erie, and back along the major water routes to the "
    "Rouge. Every treaty in the next section is a piece of that.",
    "La Nation publie aussi l'étendue de ce qu'elle détenait : les Mississaugas ont occupé, "
    "contrôlé et administré environ 3,9 millions d'acres du sud de l'Ontario, de la vallée de "
    "la rivière Rouge vers l'ouest jusqu'aux sources de la Thames, en descendant jusqu'à Long "
    "Point sur le lac Érié, puis en revenant vers la Rouge par les grandes voies d'eau. Chaque "
    "traité de la section suivante en est un morceau."))
a.p(T(
    "The century closed with a peace. Parks Canada records that on 4 August 1701 the governor "
    "of New France and Indigenous representatives signed the Great Peace of Montréal, ending "
    "nearly a century of conflict. It involved the Iroquois nations plus more than 30 other "
    "First Nations who were allied with the French, it ensured free access to vast hunting "
    "grounds and opened new fur-trading markets, and it brought peace from Acadia to Lake "
    "Superior and from the headwaters of the Ottawa River to the confluence of the Missouri and "
    "the Mississippi. Parks Canada says it shaped relations among these First Nations until the "
    "19th century.",
    "Le siècle s'est terminé sur une paix. Parcs Canada consigne que, le 4 août 1701, le "
    "gouverneur de la Nouvelle-France et des représentants autochtones ont signé la Grande "
    "Paix de Montréal, mettant fin à près d'un siècle de conflits. Elle réunissait les nations "
    "iroquoises et plus de 30 autres Premières Nations alliées des Français, elle a assuré le "
    "libre accès à de vastes territoires de chasse et ouvert de nouveaux marchés pour la "
    "traite des fourrures, et elle a apporté la paix de l'Acadie au lac Supérieur et des "
    "sources de la rivière des Outaouais au confluent du Missouri et du Mississippi. Parcs "
    "Canada indique qu'elle a façonné les relations entre ces Premières Nations jusqu'au "
    "XIXe siècle."))

# ------------------------------------------------------------------ 6
a.h2(T("The trails, the traders and the first forts",
       "Les sentiers, les traiteurs et les premiers forts"))
a.p(T(
    "Long before any fort, two portage routes linked Lake Ontario to the interior, and both "
    "are commemorated. The Toronto Carrying Place, a national historic event designated on 23 "
    "October 1969, was two alternate routes between Lake Simcoe and Lake Ontario: one ascended "
    "the Humber River to the Holland, while a lesser one began 40 kilometres to the east and "
    "followed the Rouge River. Parks Canada calls it an important trade route for the Indian "
    "nations and later the French — the dated wording of a 1969 designation, now flagged by "
    "Parks Canada for review. The Carrying Place of the Bay of Quinte, designated in 1929 and "
    "also flagged for review, was an isthmus at the western end of the Bay of Quinte, a "
    "portage between the lake and the route toward Lake Huron.",
    "Bien avant tout fort, deux routes de portage reliaient le lac Ontario à l'intérieur des "
    "terres, et les deux sont commémorées. Le passage de Toronto, événement historique "
    "national désigné le 23 octobre 1969, comptait deux tracés entre le lac Simcoe et le lac "
    "Ontario : l'un remontait la rivière Humber jusqu'à la Holland, tandis qu'un autre, moins "
    "important, commençait 40 kilomètres plus à l'est et suivait la rivière Rouge. Parcs "
    "Canada l'appelle une importante route commerciale pour les nations indiennes, puis pour "
    "les Français — la formulation datée d'une désignation de 1969, aujourd'hui signalée par "
    "Parcs Canada comme devant être révisée. Le passage de la baie de Quinte, désigné en 1929 "
    "et lui aussi signalé pour révision, était un isthme à l'extrémité ouest de la baie de "
    "Quinte, un portage entre le lac et la route vers le lac Huron."))
a.p(T(
    "Parks Canada's own page on Indigenous history for Rouge National Urban Park says only that "
    "Indigenous peoples used these paths since time immemorial. It gives no dates, names no "
    "nations and mentions no archaeology — inside a national urban park that contains Bead Hill.",
    "La page de Parcs Canada sur l'histoire autochtone du parc urbain national de la Rouge dit "
    "seulement que les peuples autochtones ont emprunté ces sentiers depuis des temps "
    "immémoriaux. Elle ne donne aucune date, ne nomme aucune nation et ne mentionne aucune "
    "archéologie — dans un parc urbain national qui contient pourtant Bead Hill."))

a.h3(T("Étienne Brûlé: what is documented, and what is only repeated",
       "Étienne Brûlé : ce qui est documenté et ce qui est seulement répété"))
a.p(T(
    "Brûlé is the name most often attached to the first European sight of this lake. The "
    "official record will not support that. The Canadian Museum of History hedges every "
    "sentence about him: he is believed to have made the voyage to Quebec in the company of "
    "Samuel de Champlain in 1608, and he appears to have been the first European to set eyes on "
    "the Ottawa Valley, Georgian Bay, Pennsylvania and four of the Great Lakes. The museum does "
    "not name Lake Ontario among them, and does not credit him with exploring it.",
    "Brûlé est le nom le plus souvent associé à la première vision européenne de ce lac. Le "
    "dossier officiel ne l'appuie pas. Le Musée canadien de l'histoire nuance chaque phrase à "
    "son sujet : on croit qu'il a fait le voyage vers Québec en compagnie de Samuel de "
    "Champlain en 1608, et il semble avoir été le premier Européen à voir la vallée de "
    "l'Outaouais, la baie Georgienne, la Pennsylvanie et quatre des Grands Lacs. Le musée ne "
    "nomme pas le lac Ontario parmi eux et ne lui attribue pas son exploration."))
a.p(T(
    "What is dated is narrower. The Ontario Heritage Trust records that Brûlé was sent to "
    "Wendat villages in 1610 to gather information and learn their language. Parks Canada's "
    "Carrying Place record says he travelled that trail in 1615. Parks Canada's plaque for him, "
    "from a designation made on 13 June 1984, calls him the first of a long line of adventurous "
    "young Canadians who adopted Indian ways, says he roamed over much of the Great Lakes "
    "basin, that Champlain sent him in 1610 to live with the Algonkin chief Iroquet, and that "
    "members of the Attignaouantan Huron killed him about 1633 — which the plaque attributes to "
    "his being an undisciplined and turbulant man who eventually alienated them. That is the "
    "plaque's spelling and the plaque's judgement, from 1984. Parks Canada has flagged this "
    "designation for review.",
    "Ce qui est daté est plus étroit. La Fiducie du patrimoine ontarien consigne que Brûlé a "
    "été envoyé dans des villages wendats en 1610 pour recueillir des renseignements et "
    "apprendre leur langue. La fiche de Parcs Canada sur le passage de Toronto indique qu'il a "
    "emprunté ce sentier en 1615. La plaque que Parcs Canada lui consacre, issue d'une "
    "désignation du 13 juin 1984, le qualifie de premier d'une longue lignée de jeunes "
    "Canadiens aventureux qui ont adopté les moeurs indiennes, dit qu'il a parcouru une bonne "
    "partie du bassin des Grands Lacs, que Champlain l'a envoyé en 1610 vivre avec le chef "
    "algonquin Iroquet, et que des membres des Hurons attignaouantans l'ont tué vers 1633 — ce "
    "que la plaque attribue au fait qu'il était un homme indiscipliné et turbulent qui a fini "
    "par se les aliéner. C'est l'orthographe de la plaque et le jugement de la plaque, en 1984. "
    "Parcs Canada a signalé cette désignation comme devant être révisée."))
a.callout(T(
    "<strong>The popular claim that Brûlé was the first European to see Lake Ontario is not "
    "supported by any source used here, so this page does not print it.</strong> The same goes "
    "for the story of Champlain crossing the lake in 1615 and joining an attack on a fortified "
    "Onondaga or Oneida village. It is the central 1615 story in popular accounts, and it does "
    "not appear in Parks Canada's Champlain record, in the Ontario Heritage Trust's article on "
    "the early French experience, or on the Canadian Museum of History pages consulted.",
    "<strong>L'affirmation répandue selon laquelle Brûlé aurait été le premier Européen à voir "
    "le lac Ontario n'est appuyée par aucune source utilisée ici ; cette page ne l'imprime donc "
    "pas.</strong> Il en va de même du récit de Champlain traversant le lac en 1615 et prenant "
    "part à une attaque contre un village fortifié onondaga ou oneida. C'est le récit central "
    "de 1615 dans les comptes rendus populaires, et il ne figure ni dans la fiche de Parcs "
    "Canada sur Champlain, ni dans l'article de la Fiducie du patrimoine ontarien sur les "
    "débuts de la présence française, ni dans les pages consultées du Musée canadien de "
    "l'histoire."))
a.p(T(
    "What Parks Canada does say about Champlain, in a designation made on 17 May 1929, is "
    "general: he helped colonise Acadia, established Quebec in 1608, formed important alliances "
    "with Aboriginal peoples, and travelled up the Ottawa River and as far west as the Great "
    "Lakes. The record contains no mention of 1615, of Lake Ontario, or of the Wendat country "
    "by name. This designation is also flagged for review. The Ontario Heritage Trust adds two "
    "dated facts: the French came to present-day Ontario as early as 1610, and Champlain "
    "wintered in Wendake in 1615-16.",
    "Ce que Parcs Canada dit de Champlain, dans une désignation du 17 mai 1929, reste général : "
    "il a contribué à coloniser l'Acadie, fondé Québec en 1608, formé d'importantes alliances "
    "avec les peuples autochtones et remonté la rivière des Outaouais jusqu'aux Grands Lacs "
    "vers l'ouest. La fiche ne mentionne ni 1615, ni le lac Ontario, ni le pays wendat par son "
    "nom. Cette désignation est elle aussi signalée pour révision. La Fiducie du patrimoine "
    "ontarien ajoute deux faits datés : les Français sont venus dans l'Ontario actuel dès 1610, "
    "et Champlain a hiverné en Wendake en 1615-1616."))

a.h3(T("Fort Frontenac, Fort Rouillé and the fur trade",
       "Le fort Frontenac, le fort Rouillé et la traite des fourrures"))
a.p(T(
    "The first European post on the lake's north shore was Fort Frontenac, at the mouth of the "
    "Cataraqui River where Kingston stands now. Parks Canada, in a designation made on 25 May "
    "1923, records that the Comte de Frontenac established it in 1673, that La Salle rebuilt "
    "the wooden fort in masonry with limestone walls and bastions in 1675, and that it was "
    "recognised as the key to the West, the base of LaSalle's explorations and a French outpost "
    "against Indigenous nations and the British. That is 1923 wording about a colonial "
    "position, and it reads like it.",
    "Le premier poste européen sur la rive nord du lac fut le fort Frontenac, à l'embouchure de "
    "la rivière Cataraqui, là où se trouve aujourd'hui Kingston. Parcs Canada, dans une "
    "désignation du 25 mai 1923, consigne que le comte de Frontenac l'a établi en 1673, que La "
    "Salle a reconstruit le fort de bois en maçonnerie, avec des murs de calcaire et des "
    "bastions, en 1675, et qu'il était reconnu comme la clé de l'Ouest, la base des "
    "explorations de La Salle et un avant-poste français face aux nations autochtones et aux "
    "Britanniques. C'est une formulation de 1923 sur une position coloniale, et cela se sent."))
a.p(T(
    "How the fort's first life ended is told two ways by two federal sources, and both are "
    "printed here. Parks Canada says the French ordered its destruction in 1689. The Department "
    "of National Defence's own history of the fort says that by the spring of 1688, most of the "
    "Fort Frontenac garrison had died of scurvy and within a year, this post was abandoned. The "
    "two can sit in sequence, but they are told as different causes. Both sources agree it was "
    "reoccupied in 1695, and Parks Canada adds that it was garrisoned to 1745 and captured by "
    "Colonel John Bradstreet in 1758; National Defence records that Bradstreet was sent with "
    "some 3,000 men and destroyed the French ships. Today the site is mostly archaeological, "
    "with parts of the north and west limestone curtain walls still visible in Kingston.",
    "La fin de la première vie du fort est racontée de deux façons par deux sources fédérales, "
    "et les deux sont imprimées ici. Parcs Canada dit que les Français en ont ordonné la "
    "destruction en 1689. L'histoire du fort publiée par le ministère de la Défense nationale "
    "indique qu'au printemps 1688, la majeure partie de la garnison du fort Frontenac était "
    "morte du scorbut et que, en moins d'un an, le poste a été abandonné. Les deux versions "
    "peuvent se suivre, mais elles sont racontées comme des causes différentes. Les deux "
    "sources s'accordent sur une réoccupation en 1695, et Parcs Canada ajoute que le fort a été "
    "gardé en garnison jusqu'en 1745 et pris par le colonel John Bradstreet en 1758 ; la "
    "Défense nationale consigne que Bradstreet a été envoyé avec quelque 3 000 hommes et qu'il "
    "a détruit les navires français. Aujourd'hui, le site est surtout archéologique, avec des "
    "parties des courtines de calcaire nord et ouest encore visibles à Kingston."))
a.p(T(
    "Further west, the Ontario Heritage Trust records Fort Rouillé, also called Fort Toronto, "
    "built in 1750-51 on the site now occupied by Exhibition Place in Toronto: a palisade with "
    "four bastions and five main buildings, put there to strengthen French control of the Great "
    "Lakes and to intercept Indigenous fur trade heading to the British post at Oswego. Its own "
    "garrison destroyed it in July 1759 after the fall of other French posts on the lake.",
    "Plus à l'ouest, la Fiducie du patrimoine ontarien consigne le fort Rouillé, aussi appelé "
    "fort Toronto, bâti en 1750-1751 à l'emplacement qu'occupe aujourd'hui la Place de "
    "l'Exposition à Toronto : une palissade à quatre bastions et cinq bâtiments principaux, "
    "installée là pour renforcer l'emprise française sur les Grands Lacs et intercepter la "
    "traite des fourrures autochtone qui se dirigeait vers le poste britannique d'Oswego. Sa "
    "propre garnison l'a détruit en juillet 1759, après la chute d'autres postes français sur "
    "le lac."))
a.p(T(
    "A French fort also stood at the mouth of the Niagara River, on what is now the American "
    "side. No permitted Canadian source consulted gives its construction date or the details of "
    "its 1759 siege, so this page names it without dates. What the Canadian record does hold "
    "for that river is a treaty: Crown-Indigenous Relations and Northern Affairs Canada records "
    "that in 1764 the Seneca negotiated a treaty with the British that granted the British "
    "unimpeded access to two miles on either side of the Niagara River.",
    "Un fort français se dressait aussi à l'embouchure de la rivière Niagara, du côté "
    "aujourd'hui américain. Aucune source canadienne autorisée consultée ne donne sa date de "
    "construction ni les détails du siège de 1759 ; cette page le nomme donc sans dates. Ce que "
    "le dossier canadien conserve pour cette rivière, c'est un traité : Relations "
    "Couronne-Autochtones et Affaires du Nord Canada consigne qu'en 1764, les Senecas ont "
    "négocié avec les Britanniques un traité leur accordant un accès sans entrave à deux milles "
    "de chaque côté de la rivière Niagara."))
a.p(T(
    "Behind the forts was the trade that paid for them. The Canadian Museum of History records "
    "that European beaver faced near extinction during the late sixteenth and early seventeenth "
    "centuries, which drove the demand for North American pelts; that roughly 15,000 or 12,000 "
    "beaver pelts a year moved at one pistole each in the early 17th century, with one year "
    "recorded as high as 22,000. The museum adds a caution that is worth keeping in mind for "
    "this whole article: Indigenous societies appear to have assimilated French goods into "
    "traditional cultural patterns, rather than simply being transformed by them.",
    "Derrière les forts, il y avait le commerce qui les payait. Le Musée canadien de l'histoire "
    "consigne que le castor européen a frôlé l'extinction à la fin du XVIe et au début du "
    "XVIIe siècle, ce qui a stimulé la demande de peaux nord-américaines ; qu'environ 15 000 ou "
    "12 000 peaux de castor par année s'échangeaient à une pistole chacune au début du XVIIe "
    "siècle, une année ayant atteint 22 000. Le musée ajoute une mise en garde à retenir pour "
    "tout cet article : les sociétés autochtones semblent avoir intégré les biens français à "
    "des schémas culturels traditionnels, plutôt que d'avoir simplement été transformées par "
    "eux."))

# ------------------------------------------------------------------ 7
a.h2(T("A line drawn through a lake",
       "Une ligne tracée au milieu d'un lac"))
a.p(T(
    "In 1783 the Treaty of Paris ended the American War of Independence and drew a boundary. "
    "The International Boundary Commission, the standing body that still maintains that line, "
    "describes it as running from the mouth of the St. Croix River in the Bay of Fundy westward "
    "to Lake of the Woods, then due west to the Mississippi and downstream. Through the Great "
    "Lakes, that meant a border drawn down the middle of the water.",
    "En 1783, le traité de Paris a mis fin à la guerre d'Indépendance américaine et a tracé une "
    "frontière. La Commission de la frontière internationale, l'organisme permanent qui "
    "entretient encore cette ligne, la décrit comme allant de l'embouchure de la rivière "
    "Sainte-Croix, dans la baie de Fundy, vers l'ouest jusqu'au lac des Bois, puis plein ouest "
    "jusqu'au Mississippi et vers l'aval. À travers les Grands Lacs, cela signifiait une "
    "frontière tracée au milieu de l'eau."))
a.p(T(
    "The Commission's public history summarises the boundary's endpoints but does not quote the "
    "1783 wording lake by lake, and no permitted source consulted quotes it either. So this "
    "page describes what the line did rather than putting quotation marks around treaty text it "
    "has not seen. What the line did is plain enough. It ran through a lake that Haudenosaunee "
    "people lived on from both sides, and it put those two sides into two different countries.",
    "L'histoire publique de la Commission résume les extrémités de la frontière, mais ne cite "
    "pas le texte de 1783 lac par lac, et aucune source autorisée consultée ne le cite non "
    "plus. Cette page décrit donc ce que la ligne a fait plutôt que de mettre entre guillemets "
    "un texte de traité qu'elle n'a pas vu. Ce que la ligne a fait est assez clair. Elle "
    "traversait un lac que des Haudenosaunee habitaient des deux côtés, et elle a placé ces "
    "deux côtés dans deux pays différents."))
a.p(T(
    "Later treaties finished the work. The Commission records that the Treaty of Ghent in 1814 "
    "appointed commissioners to determine island sovereignty and map the boundary; that the "
    "Webster-Ashburton Treaty of 1842 resolved the northeastern boundary and the undecided "
    "sections west of it; that the Treaty of 1908 provided for the more complete demarcation of "
    "the boundary from the Atlantic to the Pacific, with water boundaries marked by buoys, "
    "monuments, and ranges; and that a 1925 treaty made minor adjustments and created the "
    "standing Commission.",
    "Des traités ultérieurs ont achevé le travail. La Commission consigne que le traité de Gand "
    "de 1814 a nommé des commissaires chargés de déterminer la souveraineté sur les îles et de "
    "cartographier la frontière ; que le traité Webster-Ashburton de 1842 a réglé la frontière "
    "du nord-est et les sections restées indécises plus à l'ouest ; que le traité de 1908 a "
    "prévu une démarcation plus complète de la frontière, de l'Atlantique au Pacifique, les "
    "frontières en eau étant marquées par des bouées, des monuments et des alignements ; et "
    "qu'un traité de 1925 y a apporté des ajustements mineurs et créé la Commission "
    "permanente."))
a.p(T(
    "The division shows up in the numbers today. Environment and Climate Change Canada gives "
    "Lake Ontario a total surface area of 18,960 km². Statistics Canada, republishing figures "
    "from Natural Resources Canada's Atlas of Canada and a 1973 inventory of freshwater lakes, "
    "gives 10,000 km² as the area of the lake found in Canada, and an elevation of 75 m. Note "
    "the age of that underlying data if precision matters to you.",
    "La division se voit encore dans les chiffres. Environnement et Changement climatique "
    "Canada donne au lac Ontario une superficie totale de 18 960 km². Statistique Canada, qui "
    "republie des chiffres de l'Atlas du Canada de Ressources naturelles Canada et d'un "
    "inventaire des lacs d'eau douce de 1973, donne 10 000 km² comme superficie du lac située "
    "au Canada, et une altitude de 75 m. Notez l'âge de ces données de base si la précision "
    "vous importe."))

a.h3(T("The Haldimand Proclamation and Six Nations of the Grand River",
       "La proclamation Haldimand et les Six Nations de la rivière Grand"))
a.p(T(
    "Haudenosaunee people who had allied with Britain lost their homelands in New York when the "
    "boundary was drawn. Six Nations of the Grand River publishes the record of what was "
    "promised instead. The Haldimand Proclamation, dated 25 October 1784, granted six miles on "
    "each side of the River from Lake Erie to its source, with authority to take possession of "
    "and settle upon the banks of the Grand River. The Nation's own publication says the grant "
    "was made in partial recognition of the loss sustained by the Six Nations in the aftermath "
    "of their alliance with the British Crown during the American War of Independence.",
    "Des Haudenosaunee alliés de la Grande-Bretagne ont perdu leurs terres d'origine dans "
    "l'État de New York quand la frontière a été tracée. Les Six Nations de la rivière Grand "
    "publient le dossier de ce qui a été promis en échange. La proclamation Haldimand, datée du "
    "25 octobre 1784, accordait six milles de chaque côté de la rivière, du lac Érié jusqu'à sa "
    "source, avec l'autorisation de prendre possession des rives de la rivière Grand et de s'y "
    "établir. La publication de la Nation indique que la concession a été faite en "
    "reconnaissance partielle des pertes subies par les Six Nations à la suite de leur alliance "
    "avec la Couronne britannique pendant la guerre d'Indépendance américaine."))
a.p(T(
    "The same publication follows what happened to it: an original grant of approximately "
    "950,000 acres in 1784; the Simcoe Patent of 1793 confirming approximately 675,000 acres; a "
    "purported General Surrender document in 1841; an Order-in-Council in 1843 reserving "
    "specific lands; and a Land Claims Research Office established in 1974.",
    "La même publication suit ce qu'il en est advenu : une concession initiale d'environ "
    "950 000 acres en 1784 ; le brevet Simcoe de 1793 confirmant environ 675 000 acres ; un "
    "prétendu document de cession générale en 1841 ; un décret en 1843 réservant des terres "
    "précises ; et un bureau de recherche sur les revendications territoriales créé en 1974."))
a.fig(bar_chart(
    T("The Haldimand Tract, as Six Nations of the Grand River publishes it",
      "Le territoire Haldimand, tel que le publient les Six Nations de la rivière Grand"),
    [(T("Original grant, 1784", "Concession initiale, 1784"), 950.0),
     (T("Confirmed by the Simcoe Patent, 1793",
        "Confirmé par le brevet Simcoe, 1793"), 675.0),
     (T("Held as of March 2010", "Détenu en mars 2010"), 46.5)],
    unit=T(" thousand acres", " milliers d'acres")))
a.callout(T(
    "<strong>Six Nations gives its current holdings as approximately 46,500 acres as of March "
    "2010, which it calls roughly 4.9% of the original grant.</strong> The same publication "
    "also cites a figure of approximately 45,482.951 acres as of 1995. The two do not sit "
    "comfortably together, since the later date carries the larger number, and both are printed "
    "here with their stated dates rather than choosing one.",
    "<strong>Les Six Nations donnent leurs avoirs actuels comme étant d'environ 46 500 acres en "
    "mars 2010, ce qu'elles qualifient d'environ 4,9 % de la concession initiale.</strong> La "
    "même publication cite aussi un chiffre d'environ 45 482,951 acres en 1995. Les deux "
    "s'accordent mal, puisque la date la plus récente porte le chiffre le plus élevé, et les "
    "deux sont imprimés ici avec les dates indiquées plutôt que d'en choisir un."))
a.p(T(
    "Six Nations describes itself as unifying all Haudenosaunee peoples under the Great Tree of "
    "Peace, as the only First Nation community that includes all six Haudenosaunee nations, and "
    "as the most populous First Nation in Canada. On the Haldimand grant it writes that for "
    "their loyalty they were promised lands under the Treaty of Haldimand, and that their "
    "current territory is only a fraction of the promised area. A federal open-government "
    "record from 2025 confirms that the Haldimand Tract litigation is live.",
    "Les Six Nations se décrivent comme unissant tous les peuples haudenosaunee sous le Grand "
    "Arbre de la Paix, comme la seule communauté des Premières Nations qui réunit les six "
    "nations haudenosaunee, et comme la Première Nation la plus peuplée du Canada. Au sujet de "
    "la concession Haldimand, elles écrivent que, pour leur loyauté, on leur avait promis des "
    "terres en vertu du traité Haldimand, et que leur territoire actuel n'est qu'une fraction "
    "de la superficie promise. Un document du gouvernement ouvert fédéral de 2025 confirme que "
    "le litige sur le territoire Haldimand est toujours en cours."))
a.p(T(
    "Two Parks Canada plaques belong here, and both need their dates. The Six Nations national "
    "historic event, designated on 16 May 1930, commemorates the loyal services and unswerving "
    "fidelity of the Six Nations of Iroquois Indians to the British Empire across the Seven "
    "Years War, the American Revolution and the defence of Upper Canada in 1812-14 and 1837-38. "
    "That framing is entirely imperial, and Parks Canada has flagged it for review. The plaque "
    "for Thayendanega, Joseph Brant, designated on 29 May 1972, calls him this celebrated "
    "Mohawk chief of Canajoharie Castle and Johnson Hall, lists the Battle of Lake George in "
    "1755, the Niagara expedition of 1759 and Pontiac's Uprising in 1763, says that in the "
    "Revolution he and his Mohawks actively supported the British, that his effort afterward to "
    "build a new social and economic order to protect the Indian way of life was thwarted at "
    "the Sandusky Council, that he led his people north and they settled on the Grand River, "
    "and that he died at Wellington Square, now Burlington, Ontario. That designation is "
    "flagged for review as well.",
    "Deux plaques de Parcs Canada trouvent ici leur place, et les deux ont besoin de leur date. "
    "L'événement historique national des Six Nations, désigné le 16 mai 1930, commémore les "
    "loyaux services et la fidélité inébranlable des Six Nations des Indiens iroquois envers "
    "l'Empire britannique, à travers la guerre de Sept Ans, la Révolution américaine et la "
    "défense du Haut-Canada en 1812-1814 et en 1837-1838. Ce cadrage est entièrement impérial, "
    "et Parcs Canada l'a signalé pour révision. La plaque de Thayendanega, Joseph Brant, "
    "désigné le 29 mai 1972, le qualifie de célèbre chef mohawk de Canajoharie Castle et de "
    "Johnson Hall, énumère la bataille du lac George en 1755, l'expédition de Niagara de 1759 "
    "et le soulèvement de Pontiac en 1763, indique que, pendant la Révolution, lui et ses "
    "Mohawks ont activement soutenu les Britanniques, que son effort ultérieur pour bâtir un "
    "nouvel ordre social et économique protégeant le mode de vie indien a été contrecarré au "
    "conseil de Sandusky, qu'il a mené son peuple vers le nord et qu'ils se sont établis sur la "
    "rivière Grand, et qu'il est mort à Wellington Square, aujourd'hui Burlington, en Ontario. "
    "Cette désignation est elle aussi signalée pour révision."))

a.h3(T("Tyendinaga, on the Bay of Quinte",
       "Tyendinaga, sur la baie de Quinte"))
a.p(T(
    "Not everyone went to the Grand River. Parks Canada's Coming of the Mohawks event, "
    "designated on 17 May 1929 with a plaque on Tyendinaga Mohawk Territory at Deseronto, "
    "records that a group of around 100 people led by John Deserontyon and other chiefs settled "
    "the Bay of Quinte in 1784, after leaving their lands in northern New York in 1777 and "
    "joining British forces at Montréal. The plaque notes that despite their service their "
    "interests were overlooked in the peace negotiations, that Britain granted them replacement "
    "lands near the Bay of Quinte, and that their descendants live there today.",
    "Tout le monde n'est pas allé à la rivière Grand. L'événement Arrivée des Mohawks de Parcs "
    "Canada, désigné le 17 mai 1929 avec une plaque sur le territoire mohawk de Tyendinaga, à "
    "Deseronto, consigne qu'un groupe d'une centaine de personnes mené par John Deserontyon et "
    "d'autres chefs s'est établi sur la baie de Quinte en 1784, après avoir quitté ses terres "
    "du nord de l'État de New York en 1777 et rejoint les forces britanniques à Montréal. La "
    "plaque note que, malgré leurs services, leurs intérêts ont été négligés dans les "
    "négociations de paix, que la Grande-Bretagne leur a accordé des terres de remplacement "
    "près de la baie de Quinte, et que leurs descendants y vivent aujourd'hui."))
a.p(T(
    "That grant has its own long dispute. Crown-Indigenous Relations and Northern Affairs "
    "Canada records that the Simcoe Deed of 1793 granted the Mohawk Tract; that in 1837 the "
    "Culbertson Tract, of 923.4 acres, was unlawfully alienated; that the specific claim was "
    "filed in 1995 and accepted for negotiation in November 2003; that negotiations resumed in "
    "2017; and that the membership ratified a partial settlement on 4 November 2021. The "
    "partial agreement covers 299.43 acres, with the remaining 623.4 acres still under "
    "negotiation, and compensation of $30,974,864. The same federal release states that the "
    "original Mohawk Tract has diminished to less than one-third of its 1793 size.",
    "Cette concession a son propre long litige. Relations Couronne-Autochtones et Affaires du "
    "Nord Canada consigne que l'acte Simcoe de 1793 a accordé le territoire mohawk ; qu'en "
    "1837, le territoire Culbertson, de 923,4 acres, a été aliéné illégalement ; que la "
    "revendication particulière a été déposée en 1995 et acceptée aux fins de négociation en "
    "novembre 2003 ; que les négociations ont repris en 2017 ; et que les membres ont ratifié "
    "un règlement partiel le 4 novembre 2021. L'entente partielle porte sur 299,43 acres, les "
    "623,4 acres restants demeurant en négociation, avec une indemnité de 30 974 864 $. Le même "
    "communiqué fédéral indique que le territoire mohawk d'origine a été réduit à moins du "
    "tiers de sa taille de 1793."))
a.p(T(
    "The acreages in that release do not add up: 299.43 plus 623.4 makes 922.83, against a "
    "stated tract of 923.4 acres. The figures are quoted here as the government publishes them, "
    "and they are not summed.",
    "Les superficies de ce communiqué ne s'additionnent pas : 299,43 plus 623,4 donne 922,83, "
    "alors que le territoire est décrit comme faisant 923,4 acres. Les chiffres sont cités ici "
    "tels que le gouvernement les publie, et ils ne sont pas additionnés."))

# ------------------------------------------------------------------ 8
a.h2(T("The Toronto Purchase, and three different acreages",
       "L'achat de Toronto, et trois superficies différentes"))
a.p(T(
    "The land that Toronto stands on came to the Crown through a transaction so badly made that "
    "the Crown's own officials doubted it, and it took more than two hundred years to settle.",
    "Le terrain sur lequel Toronto est bâtie est passé à la Couronne par une transaction si mal "
    "faite que les propres fonctionnaires de la Couronne en doutaient, et il a fallu plus de "
    "deux cents ans pour la régler."))
a.p(T(
    "The Mississaugas of the Credit First Nation describe the beginning in their own words. Sir "
    "John Johnson met the Mississaugas at the Bay of Quinte in 1787, and there the Mississaugas "
    "of the Credit purportedly sold the lands of the Toronto Purchase Treaty. The Nation's word "
    "is purportedly, and it is doing real work.",
    "Les Mississaugas of the Credit First Nation décrivent le début dans leurs propres mots. "
    "Sir John Johnson a rencontré les Mississaugas à la baie de Quinte en 1787, et là, les "
    "Mississaugas of the Credit auraient prétendument vendu les terres du traité de l'achat de "
    "Toronto. Le mot employé par la Nation est prétendument, et il porte un vrai poids."))
a.p(T(
    "The defects are on the record, in the Nation's account and in Canada's own treaty research "
    "report. The deed was found blank, with no description of the land. The chiefs' marks were "
    "written on separate pieces of paper and then affixed to the blank deed. A survey attempt "
    "in 1788 met Mississauga opposition indicating that there had been no clear delineation of "
    "land boundaries. Crown administrators questioned the treaty's legality and worried that "
    "settlers, and even York, the capital, lacked clear title. Canada's research report quotes "
    "the record directly: it does not contain a description of the lands to be sold, but simply "
    "leaves blank spaces which evidently were to be filled in later after proper surveys could "
    "determine an accurate description. It also quotes Lord Dorchester, who wrote that the "
    "blank deed, not being filled up, is of no validity, or may be applied to a land they "
    "possess; no fraud has been committed or seems to have been intended.",
    "Les vices sont au dossier, dans le récit de la Nation et dans le propre rapport de "
    "recherche du Canada sur les traités. L'acte a été trouvé en blanc, sans description des "
    "terres. Les marques des chefs avaient été tracées sur des feuilles séparées, puis apposées "
    "sur l'acte vierge. Une tentative d'arpentage en 1788 s'est heurtée à l'opposition des "
    "Mississaugas, signe qu'aucune délimitation claire des limites n'avait été faite. Des "
    "administrateurs de la Couronne mettaient en doute la légalité du traité et craignaient que "
    "les colons, et même York, la capitale, n'aient pas de titre clair. Le rapport de recherche "
    "du Canada cite le dossier directement : il ne contient aucune description des terres à "
    "vendre, mais laisse simplement des espaces vides qui devaient manifestement être remplis "
    "plus tard, une fois que des arpentages en bonne et due forme auraient permis d'établir une "
    "description exacte. Il cite aussi lord Dorchester, qui écrivait que l'acte en blanc, "
    "n'étant pas rempli, est sans validité, ou pourrait s'appliquer à une terre qu'ils "
    "possèdent ; aucune fraude n'a été commise et il ne semble pas qu'il y en ait eu "
    "l'intention."))
a.p(T(
    "The same report names people on both sides, which is the way this should be told. At "
    "Toronto in August 1788 Colonel John Butler proposed that they surrender the land between "
    "Toronto and the Bay of Quinte, as far back as Lake La Clay, meaning Simcoe, and the Rice "
    "Lake. The surveyor Aitken feared to run his survey more than 2 3/4 miles inland, because "
    "Chief Wabikane cautioned him against crossing the stream located at that point. No valid "
    "deed came out of it, and uncertainty persisted about the boundaries and about which groups "
    "had been paid.",
    "Le même rapport nomme des personnes des deux côtés, et c'est ainsi qu'il faut raconter "
    "cela. À Toronto, en août 1788, le colonel John Butler a proposé qu'ils cèdent les terres "
    "entre Toronto et la baie de Quinte, jusqu'au lac La Clay, c'est-à-dire le lac Simcoe, et "
    "au lac Rice. L'arpenteur Aitken n'a pas osé pousser son levé à plus de 2 3/4 milles à "
    "l'intérieur des terres, parce que le chef Wabikane l'avait averti de ne pas franchir le "
    "ruisseau situé à cet endroit. Aucun acte valide n'en est sorti, et l'incertitude a persisté "
    "sur les limites et sur les groupes qui avaient été payés."))
a.p(T(
    "The attempted fix came on 1 August 1805. The Nation writes that the Crown purchased "
    "250,830 acres of land for the sum of 10 shillings, and that the Mississaugas retained "
    "exclusive fishing rights on Etobicoke Creek. Canada's published treaty text for Toronto "
    "Purchase No. 13 gives the same date, gives the consideration as ten shillings of good and "
    "lawful money, and says it ratified an earlier 1787 agreement that lacked a proper "
    "description.",
    "La tentative de correction est venue le 1er août 1805. La Nation écrit que la Couronne a "
    "acheté 250 830 acres de terres pour la somme de 10 shillings, et que les Mississaugas ont "
    "conservé des droits de pêche exclusifs sur le ruisseau Etobicoke. Le texte de traité publié "
    "par le Canada pour l'achat de Toronto no 13 donne la même date, fixe la contrepartie à dix "
    "shillings de bonne et légale monnaie, et indique qu'il ratifiait une entente antérieure de "
    "1787 dépourvue de description en bonne et due forme."))
a.p(T(
    "The acreage, however, is published three different ways by three official bodies. All "
    "three are printed below, because picking one would be a choice this page has no basis to "
    "make.",
    "La superficie, en revanche, est publiée de trois façons différentes par trois organismes "
    "officiels. Les trois sont imprimées ci-dessous, parce qu'en choisir une serait un choix "
    "que cette page n'a aucun moyen de justifier."))
a.table(
    [T("Who publishes it", "Qui la publie"), T("Acreage", "Superficie"),
     T("Date of the page", "Date de la page")],
    [[T("Crown-Indigenous Relations and Northern Affairs Canada, treaty text",
        "Relations Couronne-Autochtones et Affaires du Nord Canada, texte du traité"),
      T("Two hundred and fifty thousand, eight hundred and eight acres — 250,808",
        "Deux cent cinquante mille huit cent huit acres — 250 808"),
      T("Page dated 7 March 2016", "Page datée du 7 mars 2016")],
     [T("Mississaugas of the Credit First Nation",
        "Mississaugas of the Credit First Nation"),
      T("250,830 acres", "250 830 acres"),
      T("The Nation's treaty page", "La page du traité de la Nation")],
     [T("Government of Ontario, treaties and reserves map",
        "Gouvernement de l'Ontario, carte des traités et des réserves"),
      T("Approximately 250,800 acres", "Environ 250 800 acres"),
      T("Page updated 23 April 2024", "Page mise à jour le 23 avril 2024")]],
    label=T("Three official acreages for the same 1805 treaty — scroll sideways to see all of "
            "it",
            "Trois superficies officielles pour le même traité de 1805 — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "The spread is 22 acres between the highest and the lowest. It is small against a quarter "
    "of a million, and it is not small if you are trying to describe exactly what changed hands "
    "under a deed that was blank when the marks went on it.",
    "L'écart est de 22 acres entre le chiffre le plus élevé et le plus bas. C'est peu par "
    "rapport à un quart de million, et ce n'est pas peu si l'on cherche à décrire exactement ce "
    "qui a changé de mains en vertu d'un acte qui était vierge quand les marques y ont été "
    "apposées."))
a.h3(T("How it was settled, two centuries later",
       "Comment l'affaire a été réglée, deux siècles plus tard"))
a.p(T(
    "The Mississaugas of the Credit filed a claim in 1998. They disputed the Crown's "
    "acquisition of additional lands, including the Toronto Islands, and challenged the payment "
    "as unreasonable. The Nation writes that in 2010 the Government of Canada settled the "
    "Toronto Purchase Claim and the Brant Tract Claim for compensation of $145 million, at that "
    "time the largest claims settlement in Canadian history. The federal announcement gives the "
    "same amount, a ratification vote on 29 May 2010, a settlement finalised on 8 October 2010, "
    "and a membership of approximately 1,842. It also states plainly that this financial "
    "settlement does not include a land component: it was compensation for inadequate payment "
    "at the time, not a return of land.",
    "Les Mississaugas of the Credit ont déposé une revendication en 1998. Ils contestaient "
    "l'acquisition par la Couronne de terres supplémentaires, dont les îles de Toronto, et "
    "jugeaient le paiement déraisonnable. La Nation écrit qu'en 2010, le gouvernement du Canada "
    "a réglé la revendication de l'achat de Toronto et celle du territoire Brant pour une "
    "indemnité de 145 millions de dollars, alors le plus important règlement de revendication "
    "de l'histoire du Canada. Le communiqué fédéral donne le même montant, un vote de "
    "ratification le 29 mai 2010, un règlement finalisé le 8 octobre 2010 et un effectif "
    "d'environ 1 842 membres. Il précise aussi clairement que ce règlement financier ne "
    "comporte pas de volet foncier : il s'agissait d'une indemnité pour un paiement insuffisant "
    "à l'époque, et non d'une restitution de terres."))
a.p(T(
    "Chief Bryan LaForme is quoted in that release: the First Nation membership has charted our "
    "path and we will now move toward a brighter future for our people. The treaty lands "
    "include Etobicoke, Toronto, North York, York and Vaughan.",
    "Le chef Bryan LaForme est cité dans ce communiqué : les membres de la Première Nation ont "
    "tracé notre voie et nous avancerons maintenant vers un avenir meilleur pour notre peuple. "
    "Les terres visées par le traité comprennent Etobicoke, Toronto, North York, York et "
    "Vaughan."))

# ------------------------------------------------------------------ 9
a.h2(T("The other treaties on this shore, and what came of them",
       "Les autres traités de cette rive, et ce qu'ils sont devenus"))
a.p(T(
    "Ontario publishes that the province is covered by more than 40 treaties and other land "
    "agreements. Crown-Indigenous Relations and Northern Affairs Canada sets out the sequence: "
    "after the 1763 Treaty of Paris Britain sought peaceful relations; the first major cession "
    "was the 1764 Seneca treaty on the Niagara River; between 1783 and 1812 fifteen "
    "land-surrender treaties were concluded with Anishinaabe peoples; and after 1812 surrenders "
    "accelerated across the remaining lands of Upper Canada.",
    "L'Ontario publie que la province est visée par plus de 40 traités et autres accords "
    "fonciers. Relations Couronne-Autochtones et Affaires du Nord Canada en expose la séquence : "
    "après le traité de Paris de 1763, la Grande-Bretagne a cherché des relations pacifiques ; "
    "la première grande cession fut le traité seneca de 1764 sur la rivière Niagara ; entre 1783 "
    "et 1812, quinze traités de cession territoriale ont été conclus avec des peuples "
    "anishinaabes ; et après 1812, les cessions se sont accélérées sur les terres restantes du "
    "Haut-Canada."))
a.ul([
    T("Crawford's Purchases, dated 1783 by Ontario, covering the eastern end of the lake.",
      "Les achats Crawford, datés de 1783 par l'Ontario, couvrant l'extrémité est du lac."),
    T("The Johnson-Butler Purchase of 1788, covering the north shore from the eastern boundary "
      "of the Toronto Purchase east to the Bay of Quinte. Ontario explains its informal name, "
      "the Gunshot Treaty: it covered land as far back from the lake as a person could hear a "
      "gunshot.",
      "L'achat Johnson-Butler de 1788, couvrant la rive nord depuis la limite est de l'achat de "
      "Toronto jusqu'à la baie de Quinte. L'Ontario explique son nom informel, le traité du "
      "coup de fusil : il visait les terres s'étendant, à partir du lac, aussi loin qu'une "
      "personne pouvait entendre un coup de fusil."),
    T("The Between the Lakes Purchase, 7 December 1792, for a consideration of five shillings "
      "per chief, clarifying an existing 1784 purchase of the tract between Lake Ontario and "
      "Lake Erie.",
      "L'achat Between the Lakes, le 7 décembre 1792, pour une contrepartie de cinq shillings "
      "par chef, précisant un achat existant de 1784 portant sur le territoire entre le lac "
      "Ontario et le lac Érié."),
    T("The Head of the Lake Treaty, 5 and 6 September 1806: one thousand pounds of lawful money "
      "of Upper Canada for eighty-five thousand acres, with fishery reserves kept on the Credit "
      "River, Twelve Mile Creek, Sixteen Mile Creek and the Etobicoke River.",
      "Le traité de la tête du lac, les 5 et 6 septembre 1806 : mille livres de monnaie légale "
      "du Haut-Canada pour quatre-vingt-cinq mille acres, avec des réserves de pêche conservées "
      "sur la rivière Credit, le ruisseau Twelve Mile, le ruisseau Sixteen Mile et la rivière "
      "Etobicoke."),
])
a.p(T(
    "The Mississaugas of the Credit list their own treaties in one place: the Mississaugas "
    "Treaty at Niagara of 1781, Between the Lakes Treaty No. 3 of 1792, Brant Tract Treaty No. "
    "8 of 1797, Toronto Purchase Treaty No. 13 of 1805, Head of the Lake Treaty No. 14 of 1806, "
    "Ajetance Treaty No. 19 of 1818, Treaties Nos. 22 and 23 of 1820, and the Rouge Tract "
    "Settlement of 2025.",
    "Les Mississaugas of the Credit énumèrent leurs propres traités en un seul endroit : le "
    "traité des Mississaugas à Niagara de 1781, le traité Between the Lakes no 3 de 1792, le "
    "traité du territoire Brant no 8 de 1797, le traité de l'achat de Toronto no 13 de 1805, le "
    "traité de la tête du lac no 14 de 1806, le traité Ajetance no 19 de 1818, les traités "
    "nos 22 et 23 de 1820, et le règlement du territoire de la Rouge de 2025."))

a.h3(T("The Williams Treaties of 1923, and the apology of 2018",
       "Les traités Williams de 1923 et les excuses de 2018"))
a.p(T(
    "The two Williams Treaties were signed on 31 October and 21 November 1923, covering lands "
    "between Georgian Bay and the Ottawa River and along the shore of Lake Ontario and the "
    "lands up to Lake Simcoe. Ontario says they cover approximately 52,000 km². Canada's own "
    "treaty research report describes three parcels totalling 12,944,400 acres.",
    "Les deux traités Williams ont été signés le 31 octobre et le 21 novembre 1923, couvrant "
    "des terres entre la baie Georgienne et la rivière des Outaouais ainsi que le long de la "
    "rive du lac Ontario et jusqu'au lac Simcoe. L'Ontario indique qu'ils couvrent environ "
    "52 000 km². Le rapport de recherche du Canada sur les traités décrit trois parcelles "
    "totalisant 12 944 400 acres."))
a.p(T(
    "That report is unusually blunt about what happened. The Commission's report of 10 October "
    "1923 found the claims not only valid, but also far more extensive than had been supposed. "
    "It recommended compensation of $700,000.00, with an initial cash allocation of $30,000.00 "
    "and a suggested payment of $15.00 per head for roughly 1,350 claimants. The report then "
    "records the actual outcome: the Province offered only $500,000, and that amount was "
    "accepted in the final agreements.",
    "Ce rapport est d'une franchise inhabituelle sur ce qui s'est passé. Le rapport de la "
    "commission du 10 octobre 1923 a conclu que les revendications étaient non seulement "
    "valides, mais aussi bien plus vastes qu'on ne l'avait cru. Il recommandait une indemnité de "
    "700 000,00 $, avec une première attribution en argent de 30 000,00 $ et un versement "
    "suggéré de 15,00 $ par personne pour environ 1 350 ayants droit. Le rapport consigne "
    "ensuite le résultat réel : la province n'a offert que 500 000 $, et ce montant a été "
    "accepté dans les ententes finales."))
a.p(T(
    "Ninety-five years later Canada settled it. Seven First Nations — Alderville, Beausoleil, "
    "the Chippewas of Georgina Island, Rama, Curve Lake, Hiawatha and the Mississaugas of "
    "Scugog Island — signed a settlement in August 2018 of $666 million from Canada and $444 "
    "million from Ontario, with federal and provincial apologies in November 2018. Each First "
    "Nation can acquire and apply to add up to 11,000 acres to their reserve land base, and the "
    "settlement includes recognition of pre-existing treaty harvesting rights in certain treaty "
    "areas. Canada's own explanation of why is worth quoting: the 1923 treaties were signed to "
    "try to deal with First Nations' complaints, but led to longstanding disputes about "
    "compensation, land and harvesting.",
    "Quatre-vingt-quinze ans plus tard, le Canada a réglé l'affaire. Sept Premières Nations — "
    "Alderville, Beausoleil, les Chippewas de l'île Georgina, Rama, Curve Lake, Hiawatha et les "
    "Mississaugas de l'île Scugog — ont signé en août 2018 un règlement de 666 millions de "
    "dollars du Canada et de 444 millions de dollars de l'Ontario, suivi d'excuses fédérales et "
    "provinciales en novembre 2018. Chaque Première Nation peut acquérir et demander d'ajouter "
    "jusqu'à 11 000 acres à son assise territoriale de réserve, et le règlement comprend la "
    "reconnaissance de droits de récolte issus de traités préexistants dans certaines zones "
    "visées. L'explication du Canada lui-même mérite d'être citée : les traités de 1923 ont été "
    "signés pour tenter de répondre aux plaintes des Premières Nations, mais ils ont mené à des "
    "différends de longue date sur l'indemnisation, les terres et la récolte."))

a.h3(T("The Rouge River Valley Tract, 2025",
       "Le territoire de la vallée de la Rouge, 2025"))
a.p(T(
    "The most recent chapter concerns the north shore directly. The Mississaugas of the Credit "
    "submitted a claim in 2015 over the southern portion of the lands allegedly ceded under the "
    "1788 Gunshot Treaty, running along the north shore of Lake Ontario from the Bay of Quinte "
    "to the eastern boundary of the 1787 Toronto Purchase. The Nation's core grievance is that "
    "it was excluded from the 1923 Williams Treaties negotiations over those lands, and were "
    "even unaware that part of their territory was under discussion.",
    "Le chapitre le plus récent touche directement la rive nord. Les Mississaugas of the Credit "
    "ont déposé une revendication en 2015 visant la portion sud des terres prétendument cédées "
    "en vertu du traité du coup de fusil de 1788, qui longe la rive nord du lac Ontario depuis "
    "la baie de Quinte jusqu'à la limite est de l'achat de Toronto de 1787. Le grief central de "
    "la Nation est qu'elle a été exclue des négociations des traités Williams de 1923 portant "
    "sur ces terres, et qu'elle ignorait même qu'une partie de son territoire était en "
    "discussion."))
a.p(T(
    "Negotiations with Canada began in 2022 and Ontario joined in 2024. On 8 March 2025 Canada "
    "and Ontario announced a settlement of $183.4 million — $108.4 million from Canada and $75 "
    "million from Ontario — covering a claim of 128,697 acres and a dispute spanning "
    "approximately 230 years. The membership is given as 2,693. Private property within the "
    "claim lands is not in dispute, the settlement being financial only, and Rouge National "
    "Urban Park within the claim area will remain a national park.",
    "Les négociations avec le Canada ont commencé en 2022 et l'Ontario s'y est joint en 2024. Le "
    "8 mars 2025, le Canada et l'Ontario ont annoncé un règlement de 183,4 millions de dollars "
    "— 108,4 millions du Canada et 75 millions de l'Ontario — portant sur une revendication de "
    "128 697 acres et un différend s'étendant sur environ 230 ans. L'effectif est donné comme "
    "étant de 2 693 membres. Les propriétés privées situées dans les terres visées ne sont pas "
    "en cause, le règlement étant strictement financier, et le parc urbain national de la Rouge "
    "compris dans la zone visée demeurera un parc national."))
a.callout(T(
    "<strong>The two sides describe the status of that settlement differently, and both "
    "statements are printed here.</strong> The Mississaugas of the Credit describe the "
    "settlement as finalized in 2025. The federal and provincial announcement of 8 March 2025 "
    "describes a proposed settlement, initialed by negotiators, meaning they are prepared to "
    "recommend it for ratification and signing, with a community vote to follow and final "
    "approval required from the First Nation, Ontario and Canada. No later federal release "
    "confirming ratification was found for this page.",
    "<strong>Les deux parties décrivent différemment l'état de ce règlement, et les deux "
    "déclarations sont imprimées ici.</strong> Les Mississaugas of the Credit décrivent le "
    "règlement comme finalisé en 2025. Le communiqué fédéral et provincial du 8 mars 2025 "
    "décrit un règlement proposé, paraphé par les négociateurs, ce qui signifie qu'ils sont "
    "prêts à le recommander pour ratification et signature, un vote communautaire devant suivre "
    "et l'approbation finale étant requise de la Première Nation, de l'Ontario et du Canada. "
    "Aucun communiqué fédéral ultérieur confirmant la ratification n'a été trouvé pour cette "
    "page."))

# ------------------------------------------------------------------ 10
a.h2(T("The towns on the lake", "Les villes du lac"))
a.h3(T("Kingston, at the eastern end", "Kingston, à l'extrémité est"))
a.p(T(
    "The Ontario Heritage Trust plaque for the Loyalist Landing at Cataraqui, 1784, gives the "
    "sequence in the government's own words. Following the end of the American Revolution in "
    "1783 Frederick Haldimand, Governor of Quebec, approved the resettlement of loyalist "
    "refugees in what is now southern Ontario. Favourable reports on the Cataracoui area led to "
    "its occupation by British forces in the spring of 1783 and to the commencement of surveys "
    "the following October. In June 1784 a party of Associated Loyalists from New York State "
    "under Captain Michael Grass, part of a flotilla travelling from Montréal, established a "
    "camp on Mississauga Point. Grass later recalled that he led the loyal band, pointed out to "
    "them the site of their future metropolis, and gained for persecuted principles a sanctuary "
    "and for himself and his followers a home.",
    "La plaque de la Fiducie du patrimoine ontarien sur le débarquement des loyalistes à "
    "Cataraqui, en 1784, donne la séquence dans les mots mêmes du gouvernement. Après la fin de "
    "la Révolution américaine en 1783, Frederick Haldimand, gouverneur de Québec, a approuvé la "
    "réinstallation de réfugiés loyalistes dans ce qui est aujourd'hui le sud de l'Ontario. Des "
    "rapports favorables sur la région de Cataracoui ont mené à son occupation par les forces "
    "britanniques au printemps 1783 et au début des arpentages en octobre suivant. En juin "
    "1784, un groupe de loyalistes associés venus de l'État de New York, sous le commandement "
    "du capitaine Michael Grass et faisant partie d'une flottille venue de Montréal, a établi "
    "un camp à la pointe Mississauga. Grass a raconté plus tard qu'il avait mené la troupe "
    "loyale, leur avait montré l'emplacement de leur future métropole, et avait gagné pour des "
    "principes persécutés un sanctuaire, et pour lui-même et les siens un foyer."))
a.p(T(
    "Notice the order of the dates on that plaque: British occupation in the spring of 1783, "
    "surveys from October 1783, the landing in June 1784. Ontario dates Crawford's Purchases, "
    "the land agreements with the Mississauga for that end of the lake, to 1783. The plaque "
    "does not say how many people were in the landing party, and no permitted source gives that "
    "number.",
    "Remarquez l'ordre des dates sur cette plaque : occupation britannique au printemps 1783, "
    "arpentages à partir d'octobre 1783, débarquement en juin 1784. L'Ontario date de 1783 les "
    "achats Crawford, les ententes foncières conclues avec les Mississaugas pour cette "
    "extrémité du lac. La plaque ne dit pas combien de personnes comptait le groupe débarqué, "
    "et aucune source autorisée ne donne ce nombre."))
a.h3(T("Niagara, York and Hamilton", "Niagara, York et Hamilton"))
a.p(T(
    "Parks Canada records that in 1778, Loyalist refugees began crossing from Fort Niagara to "
    "settle the west bank of the Niagara River, and that the settlement was formally established "
    "in 1779 as a supply depot for British Loyalist forces, originally known as Newark. It was "
    "the first capital of Upper Canada from 1792 to 1796. The town was destroyed by fire in "
    "1813, and citizens rebuilt, mainly in the British classical architectural tradition; the "
    "designated district today covers about 41 hectares with over 90 buildings from 1815 to "
    "1859.",
    "Parcs Canada consigne qu'en 1778, des réfugiés loyalistes ont commencé à traverser depuis "
    "le fort Niagara pour s'établir sur la rive ouest de la rivière Niagara, et que "
    "l'établissement a été officiellement fondé en 1779 comme dépôt d'approvisionnement des "
    "forces loyalistes britanniques, sous le nom de Newark. Ce fut la première capitale du "
    "Haut-Canada, de 1792 à 1796. La ville a été détruite par le feu en 1813, et les citoyens "
    "l'ont reconstruite surtout dans la tradition architecturale classique britannique ; le "
    "district désigné couvre aujourd'hui environ 41 hectares avec plus de 90 bâtiments "
    "construits entre 1815 et 1859."))
a.p(T(
    "York was a compromise, and the Ontario Heritage Trust's chapter on the founding of the "
    "capital says so. Simcoe's preferred capital was London on the Thames — he wrote on 20 "
    "September 1793 that this capital he proposed to be established at New London as marked on "
    "the map of the Thames. Recognising how exposed Newark was to American attack, he moved the "
    "capital to Toronto in August 1793 as a temporary measure pending London's development. The "
    "capital never moved to London. He renamed Toronto to York in August 1793 to mark the Duke "
    "of York's victory against the French at Famars, and the name reverted to Toronto in 1834. "
    "Lord Dorchester opposed the York plans as too remote, preferred to keep the naval arsenal "
    "at Kingston, and withheld military funding and approval.",
    "York fut un compromis, et le chapitre de la Fiducie du patrimoine ontarien sur la fondation "
    "de la capitale le dit. La capitale que préférait Simcoe était London, sur la Thames — il "
    "écrivait le 20 septembre 1793 qu'il proposait d'établir cette capitale à New London, comme "
    "l'indiquait la carte de la Thames. Conscient de la vulnérabilité de Newark à une attaque "
    "américaine, il a déplacé la capitale à Toronto en août 1793 à titre de mesure temporaire, "
    "en attendant le développement de London. La capitale n'a jamais été déplacée à London. Il "
    "a rebaptisé Toronto en York en août 1793 pour souligner la victoire du duc d'York contre "
    "les Français à Famars, et le nom est redevenu Toronto en 1834. Lord Dorchester s'opposait "
    "aux projets de York, qu'il jugeait trop éloignés, préférait garder l'arsenal naval à "
    "Kingston, et a retenu les fonds et l'approbation militaires."))
a.p(T(
    "By November 1793 there was a sawmill on the Humber River, two log barracks and possibly a "
    "stockade at Fort York; the Queen's Rangers then built 28 more log structures there and "
    "defensive works at Gibraltar Point. Yonge Street was begun in 1796. Parks Canada calls "
    "Fort York the primary defensive position in early York, established by Lieutenant-Governor "
    "John Graves Simcoe to garrison troops and encourage settlement. Why here at all? The "
    "harbour behind the Toronto Islands, then a peninsula, and the head of the Toronto Carrying "
    "Place — Parks Canada makes that causal claim itself, writing that the route contributed to "
    "the favourable position of the settlement which became Toronto.",
    "En novembre 1793, il y avait une scierie sur la rivière Humber, deux casernes en rondins et "
    "peut-être une palissade au fort York ; les Queen's Rangers y ont ensuite bâti 28 autres "
    "structures en rondins et des ouvrages défensifs à la pointe Gibraltar. La rue Yonge a été "
    "amorcée en 1796. Parcs Canada qualifie le fort York de principale position défensive du "
    "York des débuts, établie par le lieutenant-gouverneur John Graves Simcoe pour y loger des "
    "troupes et encourager la colonisation. Pourquoi ici ? Le havre abrité derrière les îles de "
    "Toronto, alors une presqu'île, et la tête du passage de Toronto — Parcs Canada formule "
    "lui-même ce lien de cause à effet, en écrivant que la route a contribué à la position "
    "avantageuse de l'établissement devenu Toronto."))
a.p(T(
    "At the head of the lake, the Ontario Heritage Trust plaque for George Hamilton, 1787-1836, "
    "records that in 1815 Hamilton acquired land here at the Head of the Lake, laid out a "
    "village plot and sold lots; that when the settlement was chosen as the administrative "
    "centre of the Gore District in 1816 he gave land for a court-house square; that he sat in "
    "the Assembly for the area from 1821 to 1830; and that the settlement was named in his "
    "honour and became a police village in 1833. The year usually printed for Hamilton's "
    "founding is 1816. The plaque supports 1815 for the survey and 1816 for the administrative "
    "designation, and both are given here.",
    "À la tête du lac, la plaque de la Fiducie du patrimoine ontarien sur George Hamilton, "
    "1787-1836, consigne qu'en 1815, Hamilton a acquis des terres ici, à la tête du lac, a tracé "
    "le plan d'un village et vendu des lots ; que, lorsque l'établissement a été choisi comme "
    "centre administratif du district de Gore en 1816, il a donné un terrain pour une place du "
    "palais de justice ; qu'il a siégé à l'Assemblée pour cette région de 1821 à 1830 ; et que "
    "l'établissement a été nommé en son honneur et est devenu un village policé en 1833. "
    "L'année habituellement imprimée pour la fondation de Hamilton est 1816. La plaque appuie "
    "1815 pour l'arpentage et 1816 pour la désignation administrative, et les deux sont données "
    "ici."))
a.h3(T("Two groups who arrived by water", "Deux groupes arrivés par l'eau"))
a.p(T(
    "Parks Canada's Underground Railroad national historic event, designated in 1925, describes "
    "a network dedicated to helping free and enslaved African Americans find freedom, with main "
    "crossing points at the Detroit and Niagara rivers, from the early 19th century to the "
    "American Civil War. By 1861 approximately 30,000 people had settled in present-day Ontario "
    "after travelling north from slave states such as Kentucky and Virginia. Parks Canada does "
    "not break that figure down by destination, so this page does not assign a share of it to "
    "any lakeside town.",
    "L'événement historique national du chemin de fer clandestin de Parcs Canada, désigné en "
    "1925, décrit un réseau voué à aider des Afro-Américains libres et asservis à trouver la "
    "liberté, avec des points de passage principaux aux rivières Détroit et Niagara, du début "
    "du XIXe siècle jusqu'à la guerre de Sécession. En 1861, environ 30 000 personnes s'étaient "
    "établies dans l'Ontario actuel après avoir voyagé vers le nord depuis des États "
    "esclavagistes comme le Kentucky et la Virginie. Parcs Canada ne ventile pas ce chiffre par "
    "destination ; cette page n'en attribue donc aucune part à une ville riveraine en "
    "particulier."))
a.p(T(
    "The Ontario Heritage Trust plaque on the typhus epidemic of 1847, at St. Mary's Cemetery in "
    "Kingston, records that approximately 90,000 emigrants left for Canada that year, mostly "
    "Irish famine refugees, and that nearly 16,000 died of typhus in transit or after arrival. "
    "In Kingston roughly 1,400 died. Temporary immigrant sheds were built near the waterfront, "
    "and care was given by the Sisters of the Religious Hospitallers of St. Joseph and the "
    "Female Benevolent Society. The remains were originally buried near the present general "
    "hospital and relocated to St. Mary's Cemetery in 1966.",
    "La plaque de la Fiducie du patrimoine ontarien sur l'épidémie de typhus de 1847, au "
    "cimetière St. Mary's de Kingston, consigne qu'environ 90 000 émigrants sont partis pour le "
    "Canada cette année-là, surtout des réfugiés de la famine irlandaise, et que près de 16 000 "
    "sont morts du typhus en route ou après leur arrivée. À Kingston, environ 1 400 sont morts. "
    "Des hangars temporaires pour immigrants ont été bâtis près du port, et les soins ont été "
    "donnés par les Religieuses hospitalières de Saint-Joseph et la Female Benevolent Society. "
    "Les dépouilles avaient d'abord été inhumées près de l'actuel hôpital général, puis "
    "transférées au cimetière St. Mary's en 1966."))

# ------------------------------------------------------------------ 11
a.h2(T("The War of 1812, and the shipbuilding race",
       "La guerre de 1812 et la course aux navires"))
a.p(T(
    "Control of Lake Ontario was, in Parks Canada's words, essential for the defence of the "
    "colony, and the war produced a virtual arms race as each side built larger and more heavily "
    "armed ships. The British side of that race is documented in detail, centred on the dockyard "
    "at Kingston.",
    "Le contrôle du lac Ontario était, selon les mots de Parcs Canada, essentiel à la défense de "
    "la colonie, et la guerre a produit une véritable course aux armements, chaque camp bâtissant "
    "des navires plus grands et plus lourdement armés. Le côté britannique de cette course est "
    "documenté en détail, autour du chantier naval de Kingston."))
a.p(T(
    "Parks Canada's Kingston Navy Yard national historic site, designated on 16 May 1928 at "
    "Point Frederick, records naval operations from 1789 to 1853 with the significant war period "
    "in 1813 and 1814. Its plaque reads that Commodore James Yeo, R.N., commanded a considerable "
    "squadron built in these yards, including the 112-gun St. Lawrence, and that these ships let "
    "the British hold Upper Canada and posed such a threat that American forces never felt "
    "strong enough to risk a direct attack. Kingston, unlike York and Newark, was never attacked.",
    "Le lieu historique national du chantier naval de Kingston, désigné par Parcs Canada le "
    "16 mai 1928 à la pointe Frederick, consigne des opérations navales de 1789 à 1853, la "
    "période de guerre importante étant 1813 et 1814. Sa plaque indique que le commodore James "
    "Yeo, de la Marine royale, a commandé une escadre considérable bâtie dans ces chantiers, "
    "dont le St. Lawrence de 112 canons, et que ces navires ont permis aux Britanniques de tenir "
    "le Haut-Canada et représentaient une menace telle que les forces américaines ne se sont "
    "jamais senties assez fortes pour risquer une attaque directe. Kingston, contrairement à "
    "York et à Newark, n'a jamais été attaquée."))
a.p(T(
    "The American yard was at Sackets Harbor, across the water in New York State. No permitted "
    "Canadian source consulted describes it in comparable detail — no ship names, no dates, no "
    "description of the yard — so this page names it as the other half of the race and stops "
    "there.",
    "Le chantier américain se trouvait à Sackets Harbor, de l'autre côté de l'eau, dans l'État "
    "de New York. Aucune source canadienne autorisée consultée ne le décrit avec autant de "
    "détails — ni noms de navires, ni dates, ni description du chantier — ; cette page le nomme "
    "donc comme l'autre moitié de la course et s'arrête là."))
a.p(T(
    "How the race ended is on the lake bottom. Parks Canada's War of 1812 Shipwrecks national "
    "historic site, designated on 7 July 2014 in Kingston Harbour, holds HMS Prince Regent, HMS "
    "Princess Charlotte and HMS St. Lawrence, which it calls the most powerful British warships "
    "built in Canada during the War of 1812. HMS St. Lawrence was the largest and most heavily "
    "armed freshwater warship of its era, comparable to Nelson's Victory. All three were "
    "abandoned after the Rush-Bagot agreement of 1817 limited armaments on the Great Lakes, and "
    "they became wrecks — physical evidence, in Parks Canada's phrase, of the naval arms race. "
    "The agreement also led to the navy yard's closure by mid-century; the Royal Military "
    "College took over the naval facilities by 1876.",
    "La fin de la course repose au fond du lac. Le lieu historique national des épaves de la "
    "guerre de 1812, désigné par Parcs Canada le 7 juillet 2014 dans le port de Kingston, "
    "renferme le HMS Prince Regent, le HMS Princess Charlotte et le HMS St. Lawrence, qu'il "
    "qualifie de navires de guerre britanniques les plus puissants bâtis au Canada pendant la "
    "guerre de 1812. Le HMS St. Lawrence était le plus grand et le plus lourdement armé des "
    "navires de guerre d'eau douce de son époque, comparable au Victory de Nelson. Les trois ont "
    "été abandonnés après que l'accord Rush-Bagot de 1817 eut limité les armements sur les "
    "Grands Lacs, et ils sont devenus des épaves — la preuve matérielle, selon la formule de "
    "Parcs Canada, de la course aux armements navals. L'accord a aussi mené à la fermeture du "
    "chantier naval au milieu du siècle ; le Collège militaire royal a repris les installations "
    "navales en 1876."))
a.p(T(
    "York was invaded twice in one year. On 27 April 1813 the town was occupied and public "
    "buildings including the Legislature were destroyed by fire — the Parliament buildings were "
    "burned to the ground, and the Canadian Armed Forces' commemoration says hundreds of "
    "combatants were killed or wounded. That federal page gives no casualty count beyond "
    "hundreds, and does not mention the magazine explosion, the death of the American general, "
    "or the length of the occupation, so none of those details appears here.",
    "York a été envahie deux fois en une seule année. Le 27 avril 1813, la ville a été occupée "
    "et des édifices publics, dont l'Assemblée législative, ont été détruits par le feu — les "
    "édifices du Parlement ont été rasés, et la commémoration des Forces armées canadiennes "
    "indique que des centaines de combattants ont été tués ou blessés. Cette page fédérale ne "
    "donne aucun bilan chiffré au-delà de centaines, et ne mentionne ni l'explosion de la "
    "poudrière, ni la mort du général américain, ni la durée de l'occupation ; aucun de ces "
    "détails ne figure donc ici."))
a.p(T(
    "The Ontario Heritage Trust plaque for the second invasion tells the rest. On the morning of "
    "31 July 1813 a U.S. invasion fleet appeared off York, after having withdrawn from a planned "
    "attack on British positions at Burlington Heights. That afternoon 300 American soldiers "
    "came ashore. Their landing was unopposed: there were no British regulars in town, and "
    "York's militia had withdrawn from further combat in return for its freedom during the "
    "invasion three months earlier. The invaders seized food and military supplies, then "
    "re-embarked; the next day they returned to investigate reports that stores were concealed "
    "up the Don River, and finding nothing, burned military installations on nearby Gibraltor "
    "Point before departing. Fort York itself was captured and burned in 1813 and rebuilt "
    "between 1813 and 1815, and seven of those buildings survive — the largest collection of War "
    "of 1812 buildings in Canada, on a 3.24-hectare site.",
    "La plaque de la Fiducie du patrimoine ontarien sur la seconde invasion raconte la suite. Au "
    "matin du 31 juillet 1813, une flotte d'invasion américaine est apparue au large de York, "
    "après avoir renoncé à une attaque prévue contre les positions britanniques de Burlington "
    "Heights. Cet après-midi-là, 300 soldats américains ont débarqué. Leur débarquement n'a "
    "rencontré aucune opposition : il n'y avait pas de réguliers britanniques en ville, et la "
    "milice de York s'était retirée de tout combat ultérieur en échange de sa liberté lors de "
    "l'invasion trois mois plus tôt. Les envahisseurs ont saisi des vivres et des fournitures "
    "militaires, puis se sont rembarqués ; le lendemain, ils sont revenus vérifier des rapports "
    "selon lesquels des réserves étaient cachées en amont de la rivière Don et, ne trouvant "
    "rien, ont incendié des installations militaires à la pointe Gibraltor avant de repartir. Le "
    "fort York lui-même a été pris et incendié en 1813, puis reconstruit entre 1813 et 1815, et "
    "sept de ces bâtiments subsistent — la plus grande collection de bâtiments de la guerre de "
    "1812 au Canada, sur un site de 3,24 hectares."))

# ------------------------------------------------------------------ 12
a.h2(T("The canals, and two corrections",
       "Les canaux, et deux corrections"))
a.h3(T("The Rideau Canal, built because of the border",
       "Le canal Rideau, bâti à cause de la frontière"))
a.p(T(
    "The Rideau Canal exists because of what happened on this lake in 1812. Parks Canada writes "
    "that the need to deal with the weakness of this water link to the Great Lakes became "
    "apparent when tensions between Great Britain and the United States led to war in 1812, and "
    "that the St. Lawrence route was vulnerable because much of the southern shore of the river "
    "was in American possession. Its World Heritage nomination puts it harder: the St. Lawrence "
    "was Britain's only military supply line to the colony, exceedingly slow and costly because "
    "of the rapids, and exposed to American attack for most of its length between Montréal and "
    "Lake Ontario. Planners, in the fall of 1814, turned their attention to the Rideau and "
    "Cataraqui rivers as a possible route.",
    "Le canal Rideau existe à cause de ce qui s'est passé sur ce lac en 1812. Parcs Canada écrit "
    "que la nécessité de corriger la faiblesse de cette liaison par eau vers les Grands Lacs est "
    "apparue quand les tensions entre la Grande-Bretagne et les États-Unis ont mené à la guerre "
    "en 1812, et que la route du Saint-Laurent était vulnérable parce qu'une bonne partie de la "
    "rive sud du fleuve était en possession américaine. Sa proposition d'inscription au "
    "patrimoine mondial le dit plus crûment : le Saint-Laurent était la seule ligne "
    "d'approvisionnement militaire de la Grande-Bretagne vers la colonie, extrêmement lente et "
    "coûteuse à cause des rapides, et exposée aux attaques américaines sur la majeure partie de "
    "son parcours entre Montréal et le lac Ontario. À l'automne 1814, les planificateurs se sont "
    "tournés vers les rivières Rideau et Cataraqui comme tracé possible."))
a.p(T(
    "Lieutenant-Colonel John By of the Royal Engineers arrived in 1826 and oversaw the project. "
    "Parks Canada's own two pages disagree slightly on when digging began: its culture and "
    "history page says work began in 1827, while the World Heritage nomination chapter counts "
    "twelve years from the autumn of 1814, which gives 1826. Both are Parks Canada, so this page "
    "gives the range 1826 to 1827. The canal opened in the summer of 1832, runs 202 km with "
    "forty-seven locks, and has been a UNESCO World Heritage Site since 2007.",
    "Le lieutenant-colonel John By, du génie royal, est arrivé en 1826 et a dirigé le projet. "
    "Les deux pages de Parcs Canada divergent légèrement sur le début des travaux : sa page de "
    "culture et d'histoire indique que les travaux ont commencé en 1827, tandis que le chapitre "
    "de la proposition d'inscription au patrimoine mondial compte douze ans depuis l'automne "
    "1814, ce qui donne 1826. Les deux viennent de Parcs Canada ; cette page donne donc la "
    "fourchette de 1826 à 1827. Le canal a été ouvert à l'été 1832, s'étend sur 202 km avec "
    "quarante-sept écluses, et est inscrit au patrimoine mondial de l'UNESCO depuis 2007."))
a.p(T(
    "The workers came from two main sources, French-Canadian settlers and Irish immigrants, and "
    "the nomination chapter counts more than 6,000 workers at multiple worksites.",
    "Les travailleurs venaient de deux sources principales, des colons canadiens-français et des "
    "immigrants irlandais, et le chapitre de la proposition d'inscription en compte plus de "
    "6 000 sur de multiples chantiers."))
a.callout(T(
    "<strong>Canada's published figure for the dead is hundreds, not a thousand.</strong> The "
    "number usually printed is about 1,000, and no source used here supports it. Parks Canada "
    "publishes no death toll at all; its wording is that new recruits were always needed to "
    "replace workers who died from malaria in the swamps. The federal commemoration of 2013, "
    "which unveiled plaques at the Ottawa and Jones Falls lockstations on 20 June that year, "
    "says only that hundreds paid with the ultimate sacrifice — their lives. It gives no number "
    "and no cause, and it records that the workers were the majority of whom were Irish "
    "immigrants or French Canadians. The canal's total construction cost is not published on "
    "any page used here either.",
    "<strong>Le chiffre publié par le Canada pour les morts est des centaines, et non un "
    "millier.</strong> Le nombre habituellement imprimé est d'environ 1 000, et aucune source "
    "utilisée ici ne l'appuie. Parcs Canada ne publie aucun bilan ; sa formulation est qu'il "
    "fallait sans cesse de nouvelles recrues pour remplacer les travailleurs morts de la malaria "
    "dans les marécages. La commémoration fédérale de 2013, qui a dévoilé des plaques aux "
    "écluses d'Ottawa et de Jones Falls le 20 juin de cette année-là, dit seulement que des "
    "centaines ont payé le sacrifice ultime — leur vie. Elle ne donne ni nombre ni cause, et "
    "elle consigne que les travailleurs étaient en majorité des immigrants irlandais ou des "
    "Canadiens français. Le coût total de construction du canal n'est publié sur aucune page "
    "utilisée ici non plus."))
a.h3(T("The Welland Canal, and a death toll that was never kept",
       "Le canal Welland, et un bilan qui n'a jamais été tenu"))
a.p(T(
    "Between Lake Ontario and Lake Erie the land rises past Niagara Falls, and four successive "
    "canals were built to climb it. Parks Canada's Welland Canal System national historic event, "
    "designated on 4 June 1924 with a plaque at the Lock 7 Viewing Centre in Thorold, records "
    "four canals built between 1824 and 1932, each larger and using the latest technologies, and "
    "calls the system an important navigation link between Lake Ontario and Lake Erie. The "
    "fourth canal, the Welland Ship Canal, is recognised as a major Canadian civil engineering "
    "achievement. The Seaway system today counts 8 Canadian locks on the Welland.",
    "Entre le lac Ontario et le lac Érié, le relief s'élève au-delà des chutes Niagara, et "
    "quatre canaux successifs ont été bâtis pour le franchir. L'événement historique national du "
    "réseau du canal Welland, désigné par Parcs Canada le 4 juin 1924 avec une plaque au centre "
    "d'observation de l'écluse 7 à Thorold, consigne quatre canaux bâtis entre 1824 et 1932, "
    "chacun plus grand et faisant appel aux technologies les plus récentes, et qualifie le "
    "réseau de lien de navigation important entre le lac Ontario et le lac Érié. Le quatrième "
    "canal, le canal maritime Welland, est reconnu comme une grande réalisation du génie civil "
    "canadien. Le réseau de la Voie maritime compte aujourd'hui 8 écluses canadiennes sur le "
    "Welland."))
a.callout(T(
    "<strong>Parks Canada states outright that the Welland Canal deaths were never recorded.</strong> "
    "Its wording is that thousands of labourers toiled in difficult and dangerous conditions, "
    "and that comprehensive casualty records are incomplete because there were no contemporary "
    "health and safety regulations. That is not a gap in this page's research. It is a gap in "
    "the record itself, and the government says so. No number is printed here, because there is "
    "no number to print.",
    "<strong>Parcs Canada affirme sans détour que les morts du canal Welland n'ont jamais été "
    "consignées.</strong> Sa formulation est que des milliers d'ouvriers ont peiné dans des "
    "conditions difficiles et dangereuses, et que les registres complets des victimes sont "
    "incomplets parce qu'il n'existait pas de règlements de santé et de sécurité à l'époque. Ce "
    "n'est pas une lacune de la recherche de cette page. C'est une lacune du dossier lui-même, "
    "et le gouvernement le dit. Aucun chiffre n'est imprimé ici, parce qu'il n'y a pas de "
    "chiffre à imprimer."))
a.h3(T("The St. Lawrence Seaway", "La Voie maritime du Saint-Laurent"))
a.p(T(
    "Parks Canada's Construction of the St. Lawrence Seaway national historic event, designated "
    "on 18 March 2004 with a plaque at Iroquois, Ontario, dates the construction to 1954-1959 "
    "and says it transformed shipping on the St. Lawrence River and opened Great Lakes ports to "
    "ocean shipping on the world's greatest inland waterway, alongside hydroelectric generation "
    "and water-level control, undertaken jointly by Canada and the United States. The Seaway "
    "opened to deep draft navigation in 1959. Between Montréal and Lake Ontario it has 7 locks, "
    "2 American and 5 Canadian, with a combined lockage time of five hours; the maximum vessel "
    "is 225.5 m long, 23.77 m wide, 8.08 m in draft and 35.5 m above the water.",
    "L'événement historique national de la construction de la Voie maritime du Saint-Laurent, "
    "désigné par Parcs Canada le 18 mars 2004 avec une plaque à Iroquois, en Ontario, date la "
    "construction de 1954 à 1959 et indique qu'elle a transformé la navigation sur le fleuve "
    "Saint-Laurent et ouvert les ports des Grands Lacs à la navigation océanique sur la plus "
    "grande voie navigable intérieure du monde, avec production hydroélectrique et régulation "
    "des niveaux d'eau, entreprise conjointement par le Canada et les États-Unis. La Voie "
    "maritime a été ouverte à la navigation de grand tirant d'eau en 1959. Entre Montréal et le "
    "lac Ontario, elle compte 7 écluses, 2 américaines et 5 canadiennes, avec une durée totale "
    "d'éclusage de cinq heures ; le navire maximal fait 225,5 m de long, 23,77 m de large, "
    "8,08 m de tirant d'eau et 35,5 m au-dessus de l'eau."))
a.callout(T(
    "<strong>The Lost Villages were on the St. Lawrence River below Lake Ontario, not on Lake "
    "Ontario.</strong> The International Joint Commission records that the project caused a "
    "dozen Ontario communities, now collectively known as the Lost Villages, to be flooded, and "
    "that several present-day communities such as Long Sault, Morrisburg and Iroquois, Ontario, "
    "contain houses and other structures moved from areas that were flooded. The Commission does "
    "not publish how many people were relocated, how many buildings were moved, or the date of "
    "the flooding, and Parks Canada's Seaway designation record does not mention the flooding at "
    "all.",
    "<strong>Les villages engloutis se trouvaient sur le fleuve Saint-Laurent, en aval du lac "
    "Ontario, et non sur le lac Ontario.</strong> La Commission mixte internationale consigne "
    "que le projet a entraîné l'inondation d'une douzaine de collectivités ontariennes, "
    "aujourd'hui connues collectivement sous le nom de villages engloutis, et que plusieurs "
    "collectivités actuelles comme Long Sault, Morrisburg et Iroquois, en Ontario, comptent des "
    "maisons et d'autres bâtiments déplacés depuis les zones inondées. La Commission ne publie "
    "ni le nombre de personnes relogées, ni le nombre de bâtiments déplacés, ni la date de "
    "l'inondation, et la fiche de désignation de Parcs Canada sur la Voie maritime ne mentionne "
    "pas du tout l'inondation."))
a.p(T(
    "One more silence deserves naming. The International Joint Commission's own page on the "
    "population of that reach notes that the Mohawk Nation of Akwesasne is primarily downstream "
    "of Lake St. Lawrence and that residents remain closely tied to it — and then says nothing "
    "about how the Seaway and the power project affected Akwesasne.",
    "Un autre silence mérite d'être nommé. La page de la Commission mixte internationale sur la "
    "population de ce tronçon signale que la Nation mohawk d'Akwesasne se trouve surtout en aval "
    "du lac Saint-Laurent et que ses résidents y restent étroitement liés — puis elle ne dit "
    "rien de la façon dont la Voie maritime et le projet hydroélectrique ont touché Akwesasne."))
a.p(T(
    "What the Seaway carries is published: since 1959, more than 2.5 billion tonnes of cargo "
    "estimated at $375 billion have moved to and from Canada, the United States and nearly fifty "
    "other nations. Ontario adds that Great Lakes shipping routes stimulate $15.9 billion in "
    "annual economic activity in Ontario and Quebec.",
    "Ce que transporte la Voie maritime est publié : depuis 1959, plus de 2,5 milliards de "
    "tonnes de marchandises évaluées à 375 milliards de dollars ont circulé à destination et en "
    "provenance du Canada, des États-Unis et de près de cinquante autres pays. L'Ontario ajoute "
    "que les routes maritimes des Grands Lacs stimulent 15,9 milliards de dollars d'activité "
    "économique annuelle en Ontario et au Québec."))

# ------------------------------------------------------------------ 13
a.h2(T("What was lost, and what came back",
       "Ce qui a été perdu, et ce qui est revenu"))
a.p(T(
    "Ontario publishes a dated history of the lake's fish, and it reads as a slow collapse. "
    "Declines in Lake Ontario Atlantic salmon stocks were first reported in 1835. Commercial "
    "yields fell each season from 1846 to 1850. By 1865 the species was on the verge of "
    "extinction. Ontario's causes are pollution, overexploitation, and dams blocking spawning "
    "streams, including the Dunnville Dam of 1827 on the Grand River, together with intensified "
    "commercial fishing.",
    "L'Ontario publie une histoire datée des poissons du lac, et elle se lit comme un lent "
    "effondrement. Les premiers signalements de déclin des stocks de saumon atlantique du lac "
    "Ontario datent de 1835. Les prises commerciales ont chuté chaque saison de 1846 à 1850. En "
    "1865, l'espèce était au bord de l'extinction. Les causes que donne l'Ontario sont la "
    "pollution, la surexploitation et les barrages bloquant les cours d'eau de fraie, dont le "
    "barrage de Dunnville de 1827 sur la rivière Grand, avec l'intensification de la pêche "
    "commerciale."))
a.callout(T(
    "<strong>Ontario says the last record of Atlantic salmon in Lake Ontario is 1897.</strong> "
    "The year commonly printed elsewhere is 1898, and no source used here supports it. Ontario "
    "dates the extirpation of the species from the lake to the 1890s.",
    "<strong>L'Ontario indique que la dernière mention de saumon atlantique dans le lac Ontario "
    "date de 1897.</strong> L'année couramment imprimée ailleurs est 1898, et aucune source "
    "utilisée ici ne l'appuie. L'Ontario situe la disparition de l'espèce dans le lac dans les "
    "années 1890."))
a.h3(T("The sea lamprey: two governments, two accounts",
       "La lamproie marine : deux gouvernements, deux récits"))
a.p(T(
    "How the sea lamprey reached and spread through the Great Lakes is told differently by "
    "Ontario and by Fisheries and Oceans Canada. Both are printed here.",
    "La façon dont la lamproie marine a atteint les Grands Lacs et s'y est répandue est racontée "
    "différemment par l'Ontario et par Pêches et Océans Canada. Les deux récits sont imprimés "
    "ici."))
a.table(
    [T("Who says it", "Qui le dit"), T("What it says", "Ce qui est dit")],
    [[T("Government of Ontario, fish management history",
        "Gouvernement de l'Ontario, histoire de la gestion des pêches"),
      T("\"1835: First reliable report of sea lamprey in Lake Ontario. It is believed that sea "
        "lamprey gained access to Lake Ontario via the Erie Canal.\" The same timeline then "
        "gives 1921 above Niagara Falls in Lake Erie, 1931 in Lake Huron and 1946 in Lake "
        "Superior.",
        "« 1835 : premier signalement fiable de la lamproie marine dans le lac Ontario. On "
        "croit que la lamproie marine a accédé au lac Ontario par le canal Érié. » La même "
        "chronologie donne ensuite 1921 au-dessus des chutes Niagara, dans le lac Érié, 1931 "
        "dans le lac Huron et 1946 dans le lac Supérieur.")],
     [T("Fisheries and Oceans Canada", "Pêches et Océans Canada"),
      T("Lampreys \"were first observed in Lake Ontario in the 1830s\", and \"when the Welland "
        "Canal (constructed to bypass the falls) was deepened in 1919, sea lampreys gained "
        "access to the rest of the Great Lakes. By 1938, they had invaded all of the Great "
        "Lakes.\"",
        "Les lamproies « ont été observées pour la première fois dans le lac Ontario dans les "
        "années 1830 » et, « lorsque le canal Welland (construit pour contourner les chutes) a "
        "été approfondi en 1919, les lamproies marines ont eu accès au reste des Grands Lacs. "
        "En 1938, elles avaient envahi tous les Grands Lacs. »")]],
    label=T("Two official accounts of the sea lamprey — scroll sideways to see all of it",
            "Deux récits officiels sur la lamproie marine — faites défiler latéralement pour "
            "tout voir"))
a.p(T(
    "The difference is not a detail. One account has the lamprey arriving by the Erie Canal and "
    "spreading upward by 1921; the other has the deepening of the Welland Canal in 1919 opening "
    "the upper lakes and the invasion complete by 1938. Note also that neither source says "
    "plainly whether the sea lamprey is native to Lake Ontario. Ontario hedges with it is "
    "believed, and this page keeps the hedge.",
    "La différence n'est pas un détail. Un récit fait arriver la lamproie par le canal Érié et "
    "la fait remonter vers 1921 ; l'autre fait de l'approfondissement du canal Welland en 1919 "
    "l'ouverture des lacs supérieurs, l'invasion étant achevée en 1938. Notez aussi qu'aucune "
    "des deux sources ne dit clairement si la lamproie marine est indigène du lac Ontario. "
    "L'Ontario nuance avec on croit, et cette page conserve la nuance."))
a.p(T(
    "Fisheries and Oceans Canada records that Canada and the United States created the Great "
    "Lakes Fishery Commission in 1955 to control sea lampreys, coordinate research, and improve "
    "the fishery, and that control using lampricides, barriers and traps has achieved a 90% "
    "reduction of sea lamprey populations in most areas. The department also publishes damage "
    "figures — a collapse from about 7 million kilograms of lake trout a year to about 136,000 "
    "kilograms by the early 1960s — but those are for lakes Huron and Superior, not Lake "
    "Ontario, and they are not transferred here.",
    "Pêches et Océans Canada consigne que le Canada et les États-Unis ont créé la Commission des "
    "pêcheries des Grands Lacs en 1955 pour lutter contre la lamproie marine, coordonner la "
    "recherche et améliorer la pêche, et que la lutte au moyen de lampricides, de barrières et "
    "de pièges a permis une réduction de 90 % des populations de lamproies marines dans la "
    "plupart des secteurs. Le ministère publie aussi des chiffres de dommages — un effondrement "
    "d'environ 7 millions de kilogrammes de touladi par année à environ 136 000 kilogrammes au "
    "début des années 1960 — mais ils concernent les lacs Huron et Supérieur, et non le lac "
    "Ontario, et ils ne sont pas transposés ici."))
a.p(T(
    "Stocking has a long and mixed history on this lake. Ontario records that chinook salmon "
    "were first stocked in the Ontario waters of Lake Ontario in 1874 and that the stocking "
    "program was discontinued in 1882, and that large-scale lake trout stocking, along with "
    "coho, kokanee, pink and chum salmon, ran from the 1950s to 1975. Ontario now runs a Lake "
    "Ontario Atlantic Salmon Restoration Program, and the Atlantic salmon of this lake have been "
    "the subject of a federal species-at-risk consultation.",
    "L'empoissonnement a une longue histoire, aux résultats mêlés, sur ce lac. L'Ontario "
    "consigne que le saumon quinnat a été introduit pour la première fois dans les eaux "
    "ontariennes du lac Ontario en 1874 et que le programme a été abandonné en 1882, et que "
    "l'empoissonnement à grande échelle en touladi, ainsi qu'en saumons coho, kokani, rose et "
    "kéta, s'est poursuivi des années 1950 à 1975. L'Ontario mène aujourd'hui un programme de "
    "rétablissement du saumon atlantique du lac Ontario, et le saumon atlantique de ce lac a "
    "fait l'objet d'une consultation fédérale sur les espèces en péril."))

a.h3(T("The agreement that changed the water",
       "L'accord qui a changé l'eau"))
a.p(T(
    "Environment and Climate Change Canada records the Great Lakes Water Quality Agreement as "
    "signed on 15 April 1972, revised in 1978, and amended by protocol in 1987 and again in "
    "2012. The current agreement addresses ten priority areas: Areas of Concern; Lakewide "
    "Management; Chemicals of Mutual Concern; Nutrients; Discharges from Vessels; Aquatic "
    "Invasive Species; Habitat and Species; Groundwater; Climate Change Impacts; and Science.",
    "Environnement et Changement climatique Canada consigne l'Accord relatif à la qualité de "
    "l'eau dans les Grands Lacs comme signé le 15 avril 1972, révisé en 1978, puis modifié par "
    "protocole en 1987 et de nouveau en 2012. L'accord actuel porte sur dix domaines "
    "prioritaires : les secteurs préoccupants ; la gestion à l'échelle du lac ; les produits "
    "chimiques sources de préoccupations mutuelles ; les éléments nutritifs ; les rejets des "
    "navires ; les espèces aquatiques envahissantes ; les habitats et les espèces ; les eaux "
    "souterraines ; les répercussions des changements climatiques ; et la science."))
a.p(T(
    "It is often said that the 1972 agreement was about phosphorus. The department's own page on "
    "the agreement does not say so, so this page does not either; nutrients are one of the ten "
    "current annexes, and that is what can be stated from the source.",
    "On dit souvent que l'accord de 1972 portait sur le phosphore. La page du ministère sur "
    "l'accord ne le dit pas ; cette page ne le dit donc pas non plus. Les éléments nutritifs "
    "sont l'une des dix annexes actuelles, et c'est ce que la source permet d'affirmer."))
a.p(T(
    "In 1987, 43 Areas of Concern were designated: 12 entirely in Canadian waters, 5 shared and "
    "26 entirely in American waters. Five of them are on Lake Ontario, and all five are still "
    "designated: Toronto and Region, assessed in 1989; Bay of Quinte, 1990; Hamilton Harbour, "
    "1992; the Niagara River, 1993; and Port Hope Harbour, 2003. The three Canadian Areas of "
    "Concern that have been delisted — Collingwood Harbour in 1994, Severn Sound in 2002 and "
    "Wheatley Harbour in 2010 — are not on this lake. Canada reports that as of March 2025, 76 "
    "of the 121 impaired beneficial uses identified in its 17 Areas of Concern have been "
    "restored.",
    "En 1987, 43 secteurs préoccupants ont été désignés : 12 entièrement en eaux canadiennes, 5 "
    "partagés et 26 entièrement en eaux américaines. Cinq d'entre eux se trouvent sur le lac "
    "Ontario, et les cinq sont toujours désignés : Toronto et sa région, évalué en 1989 ; la "
    "baie de Quinte, en 1990 ; le port de Hamilton, en 1992 ; la rivière Niagara, en 1993 ; et "
    "le port de Port Hope, en 2003. Les trois secteurs préoccupants canadiens radiés — le port "
    "de Collingwood en 1994, Severn Sound en 2002 et le port de Wheatley en 2010 — ne sont pas "
    "sur ce lac. Le Canada rapporte qu'en mars 2025, 76 des 121 utilisations bénéfiques altérées "
    "recensées dans ses 17 secteurs préoccupants avaient été rétablies."))
a.p(T(
    "Hamilton Harbour shows what industry left behind. Canada writes that water quality and "
    "environmental health were severely degraded there by intensive industrial and urban "
    "development, that the regional economy was dominated by the steel and iron industry, and "
    "that the harbour still supports one of the largest concentrations of heavy industry in "
    "Canada. Some sediment in the harbour is contaminated by metals, polychlorinated biphenyls "
    "and polycyclic aromatic hydrocarbons, from more than a century of industry.",
    "Le port de Hamilton montre ce que l'industrie a laissé derrière elle. Le Canada écrit que "
    "la qualité de l'eau et la santé environnementale y ont été gravement dégradées par un "
    "développement industriel et urbain intensif, que l'économie régionale était dominée par la "
    "sidérurgie, et que le port abrite encore l'une des plus fortes concentrations d'industrie "
    "lourde au Canada. Certains sédiments du port sont contaminés par des métaux, des biphényles "
    "polychlorés et des hydrocarbures aromatiques polycycliques, résultat de plus d'un siècle "
    "d'industrie."))
a.p(T(
    "Randle Reef is the largest contaminated sediment site of them all: about 615,000 cubic "
    "metres of sediment contaminated with polycyclic aromatic hydrocarbons, covering about 60 "
    "hectares, with contamination dating to the 1800s. The project began in 2015 and costs "
    "$138.9 million, funded one third by Canada, one third by Ontario, and one third jointly by "
    "the City of Hamilton, the City of Burlington, Halton Region, the Hamilton-Oshawa Port "
    "Authority and Stelco. Stage 1 built an engineered containment facility with 3,400 steel "
    "beams; a federal announcement in March 2022 confirmed all contaminated sediment removed or "
    "capped; Stage 3, a multi-layered environmental cap, is scheduled for completion in 2027. "
    "The work is not finished.",
    "Le récif Randle est le plus grand site de sédiments contaminés de tous : environ "
    "615 000 mètres cubes de sédiments contaminés par des hydrocarbures aromatiques "
    "polycycliques, sur environ 60 hectares, une contamination qui remonte aux années 1800. Le "
    "projet a commencé en 2015 et coûte 138,9 millions de dollars, financés pour un tiers par le "
    "Canada, un tiers par l'Ontario et un tiers conjointement par la Ville de Hamilton, la Ville "
    "de Burlington, la région de Halton, l'administration portuaire de Hamilton-Oshawa et "
    "Stelco. L'étape 1 a permis de construire une installation de confinement technique avec "
    "3 400 poutres d'acier ; un communiqué fédéral de mars 2022 a confirmé que tous les "
    "sédiments contaminés avaient été enlevés ou recouverts ; l'étape 3, un recouvrement "
    "environnemental multicouche, doit être achevée en 2027. Le travail n'est pas terminé."))
a.h3(T("Where the lake stands now", "Où en est le lac aujourd'hui"))
a.p(T(
    "The binational State of the Great Lakes 2025 Report, published by Environment and Climate "
    "Change Canada and the United States Environmental Protection Agency, rates Lake Ontario "
    "overall as Fair, with the trend Unchanging. The category assessments are worth reading one "
    "by one.",
    "Le rapport binational sur l'état des Grands Lacs de 2025, publié par Environnement et "
    "Changement climatique Canada et l'Environmental Protection Agency des États-Unis, évalue le "
    "lac Ontario dans son ensemble comme passable, avec une tendance stable. Les évaluations par "
    "catégorie méritent d'être lues une à une."))
a.table(
    [T("Category", "Catégorie"), T("Status and trend", "État et tendance")],
    [[T("Drinking water", "Eau potable"),
      T("Good, Unchanging to Improving", "Bon, stable à en amélioration")],
     [T("Beaches", "Plages"), T("Good, Unchanging", "Bon, stable")],
     [T("Fish consumption", "Consommation de poisson"),
      T("Fair, Unchanging to Improving", "Passable, stable à en amélioration")],
     [T("Toxic chemicals", "Produits chimiques toxiques"),
      T("Fair, No Trend", "Passable, aucune tendance")],
     [T("Habitat and species", "Habitats et espèces"),
      T("Fair, Unchanging", "Passable, stable")],
     [T("Nutrients and algae", "Éléments nutritifs et algues"),
      T("Fair, Unchanging", "Passable, stable")],
     [T("Invasive species impacts", "Répercussions des espèces envahissantes"),
      T("Poor, No Trend", "Mauvais, aucune tendance")],
     [T("Watershed impacts", "Répercussions à l'échelle du bassin versant"),
      T("Fair, No Trend", "Passable, aucune tendance")],
     [T("Groundwater", "Eaux souterraines"),
      T("Fair, Undetermined", "Passable, indéterminée")]],
    label=T("Lake Ontario in the State of the Great Lakes 2025 Report — scroll sideways to see "
            "all of it",
            "Le lac Ontario dans le rapport sur l'état des Grands Lacs de 2025 — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "The report also records real recovery. Lake trout populations are Improving, due in part to "
    "successful sea lamprey control, and lake sturgeon populations are showing some signs of "
    "recovery with stocking programs leading to successful spawning in tributaries. Offshore "
    "phosphorus concentrations remain below established objectives.",
    "Le rapport consigne aussi de véritables rétablissements. Les populations de touladi sont en "
    "amélioration, en partie grâce au succès de la lutte contre la lamproie marine, et les "
    "populations d'esturgeon jaune montrent certains signes de rétablissement, les programmes "
    "d'empoissonnement menant à des fraies réussies dans les affluents. Les concentrations de "
    "phosphore au large demeurent sous les objectifs établis."))
a.callout(T(
    "<strong>Clearer water is not the same as healthier water, and the report explains why.</strong> "
    "Excessive growth of the alga Cladophora in localized nearshore areas, due in part to "
    "nutrient loading and increased water clarity caused by the filtering effects of invasive "
    "Dreissenid mussels, can degrade habitats and foul beaches. The mussels that made the lake "
    "look cleaner are part of what makes the beaches worse. Invasive species impacts are the one "
    "category rated Poor.",
    "<strong>Une eau plus claire n'est pas la même chose qu'une eau plus saine, et le rapport "
    "explique pourquoi.</strong> La croissance excessive de l'algue Cladophora dans certaines "
    "zones littorales, due en partie aux apports d'éléments nutritifs et à une transparence "
    "accrue de l'eau causée par la filtration des moules dreissenidés envahissantes, peut "
    "dégrader les habitats et souiller les plages. Les moules qui ont rendu le lac plus clair "
    "font partie de ce qui rend les plages plus sales. Les répercussions des espèces "
    "envahissantes sont la seule catégorie jugée mauvaise."))
a.p(T(
    "As of 2023, the same report counts 190 aquatic non-native species reported as established "
    "in the Great Lakes, of which 78 are considered invasive, and notes that no new aquatic "
    "non-native species suspected to have been introduced through ballast water has become "
    "established since 2006. An older Environment and Climate Change Canada page, dated 2017, "
    "still says more than 160 alien species; the 2025 figures are the current ones. That page "
    "does record that zebra mussels were first discovered in the Great Lakes around 1986 and "
    "have significantly changed the nature of the lake bottom, and that the round goby was "
    "introduced to the St. Clair River in 1990, probably through ballast water from ships "
    "originating from southern Europe, and has since colonized all five Great Lakes.",
    "En 2023, le même rapport recense 190 espèces aquatiques non indigènes signalées comme "
    "établies dans les Grands Lacs, dont 78 sont considérées comme envahissantes, et note "
    "qu'aucune nouvelle espèce aquatique non indigène soupçonnée d'avoir été introduite par les "
    "eaux de ballast ne s'y est établie depuis 2006. Une page plus ancienne d'Environnement et "
    "Changement climatique Canada, datée de 2017, parle encore de plus de 160 espèces exotiques ; "
    "les chiffres de 2025 sont les chiffres actuels. Cette page consigne néanmoins que les "
    "moules zébrées ont été découvertes pour la première fois dans les Grands Lacs vers 1986 et "
    "ont considérablement modifié la nature du fond des lacs, et que le gobie à taches noires a "
    "été introduit dans la rivière Sainte-Claire en 1990, probablement par les eaux de ballast "
    "de navires venus du sud de l'Europe, et qu'il a depuis colonisé les cinq Grands Lacs."))
a.p(T(
    "One recovery is worth ending on. Environment and Climate Change Canada records that "
    "monitoring in the 1970s alerted scientists to the fact that the eggs of fish-eating birds "
    "were becoming so thin that they would crack during incubation. After DDT was banned, levels "
    "declined by 10 times and the health of local birds improved; more broadly, since regulatory "
    "actions were taken against legacy persistent organic pollutants, levels in general have "
    "declined by about half, and in some indicator species, such as the herring gull, drastic "
    "reductions have occurred. The department does not publish exact percentage declines for "
    "individual contaminants, and none is invented here.",
    "Un rétablissement mérite de conclure. Environnement et Changement climatique Canada consigne "
    "que la surveillance des années 1970 a alerté les scientifiques sur le fait que les oeufs "
    "des oiseaux piscivores devenaient si minces qu'ils se fendaient pendant l'incubation. Après "
    "l'interdiction du DDT, les concentrations ont diminué de 10 fois et la santé des oiseaux "
    "locaux s'est améliorée ; plus largement, depuis que des mesures réglementaires ont visé les "
    "polluants organiques persistants hérités du passé, les concentrations ont généralement "
    "diminué de moitié environ, et chez certaines espèces indicatrices, comme le goéland "
    "argenté, des réductions spectaculaires ont eu lieu. Le ministère ne publie pas de baisses "
    "en pourcentage exact pour chaque contaminant, et aucune n'est inventée ici."))

# ------------------------------------------------------------------ 14
a.h2(T("The lake today", "Le lac aujourd'hui"))
a.p(T(
    "For a long time the governments published population figures for all five Great Lakes "
    "together and nothing for this lake by itself. The Lake Ontario Lakewide Action and "
    "Management Plan for 2018 to 2022, published by Environment and Climate Change Canada and "
    "the United States Environmental Protection Agency under the Great Lakes Water Quality "
    "Agreement, closes that gap.",
    "Pendant longtemps, les gouvernements ont publié des chiffres de population pour les cinq "
    "Grands Lacs ensemble, et rien pour ce lac seul. Le plan d'action et d'aménagement panlacustre "
    "du lac Ontario pour 2018-2022, publié par Environnement et Changement climatique Canada et "
    "l'Environmental Protection Agency des États-Unis en vertu de l'Accord relatif à la qualité "
    "de l'eau dans les Grands Lacs, comble cette lacune."))
a.fig(bar_chart(
    T("People in the Lake Ontario watershed, from the 2018-2022 Lakewide Plan",
      "Population du bassin versant du lac Ontario, selon le plan panlacustre 2018-2022"),
    [(T("The whole watershed", "L'ensemble du bassin versant"), 11.0),
     (T("Of them, in Ontario", "Dont, en Ontario"), 9.0),
     (T("Of them, in New York State", "Dont, dans l'État de New York"), 2.0)],
    unit=T(" million people", " millions de personnes")))
a.ul([
    T("The plan states that the Lake Ontario watershed is currently home to 11 million people, "
      "about 9 million Ontarians and 2 million New Yorkers.",
      "Le plan indique que le bassin versant du lac Ontario abrite actuellement 11 millions de "
      "personnes, soit environ 9 millions d'Ontariens et 2 millions de New-Yorkais."),
    T("It states that over 9 million New Yorkers and Ontarians get their drinking water from "
      "Lake Ontario.",
      "Il indique que plus de 9 millions de New-Yorkais et d'Ontariens tirent leur eau potable "
      "du lac Ontario."),
    T("And it states that of the 12.8 million people who live in the province, 49.2%, or 6.3 "
      "million people, draw their drinking water from the Lake.",
      "Et il indique que, sur les 12,8 millions de personnes qui vivent dans la province, "
      "49,2 %, soit 6,3 millions de personnes, tirent leur eau potable du lac."),
])
a.callout(T(
    "<strong>That 49.2% rests on an Ontario population of 12.8 million, which is out of "
    "date.</strong> Statistics Canada's 2021 Census counted 14,223,942 people in Ontario. The "
    "percentage and the 6.3 million are quoted here exactly as the 2021 plan document publishes "
    "them, and they are not silently recalculated against a newer population. If you need a "
    "current figure, it has not been published.",
    "<strong>Ce 49,2 % repose sur une population ontarienne de 12,8 millions, qui n'est plus à "
    "jour.</strong> Le Recensement de 2021 de Statistique Canada a dénombré 14 223 942 personnes "
    "en Ontario. Le pourcentage et les 6,3 millions sont cités ici exactement comme le document "
    "de planification de 2021 les publie, et ils ne sont pas recalculés en douce sur une "
    "population plus récente. Si vous avez besoin d'un chiffre actuel, il n'a pas été publié."))
a.p(T(
    "This also resolves a figure that looks contradictory at first. Ontario publishes that more "
    "than 80% of Ontarians get their drinking water from Lakes Superior, Huron, Erie and "
    "Ontario. That is across four lakes. Roughly half of Ontarians draw specifically from this "
    "one.",
    "Cela règle aussi un chiffre qui paraît contradictoire au premier abord. L'Ontario publie que "
    "plus de 80 % des Ontariens tirent leur eau potable des lacs Supérieur, Huron, Érié et "
    "Ontario. C'est pour quatre lacs. Environ la moitié des Ontariens s'approvisionnent "
    "précisément à celui-ci."))
a.p(T(
    "The same plan publishes the lake's dimensions, which the general government pages do not: a "
    "surface area of 18,960 km², an average depth of 86 metres and a maximum depth of 244 "
    "metres, with a shoreline length of 1,146 km. The surface area matches Environment and "
    "Climate Change Canada's own drainage basin page exactly. The lake's water volume and its "
    "retention time are not printed here — the volume figure in the document carries a unit "
    "error, and no retention time was found on any source used.",
    "Le même plan publie les dimensions du lac, que les pages gouvernementales générales ne "
    "donnent pas : une superficie de 18 960 km², une profondeur moyenne de 86 mètres et une "
    "profondeur maximale de 244 mètres, avec un littoral de 1 146 km. La superficie correspond "
    "exactement à la page d'Environnement et Changement climatique Canada sur le bassin de "
    "drainage. Le volume d'eau du lac et son temps de séjour ne sont pas imprimés ici — le "
    "chiffre de volume du document comporte une erreur d'unité, et aucun temps de séjour n'a été "
    "trouvé dans les sources utilisées."))
a.p(T(
    "Water levels have been the recent worry. The International Joint Commission records that "
    "record precipitation fell across the Lake Ontario and St. Lawrence River basin in 2017, and "
    "that in 2019 there was too much water entering Lake Ontario from a flooded Lake Erie, and "
    "nowhere for it to go but into a flooded St. Lawrence River, with record-high inflows from "
    "Lake Erie and a late, heavy snowmelt coupled with an extremely wet spring. Lake Ontario "
    "levels in 2019 eventually exceeded their record peak of 2017. Between November and May in "
    "2019 Toronto received 555.6 mm of precipitation, the fourth highest since 1938, and "
    "Watertown, New York, received 823.7 mm, the second highest since 1898. The Commission also "
    "states its own conclusion plainly: the high water levels were not caused by regulation of "
    "outflows or by Plan 2014. It publishes no peak level in metres and no damage figures, so "
    "neither appears here.",
    "Les niveaux d'eau ont été l'inquiétude récente. La Commission mixte internationale consigne "
    "qu'une pluviométrie record est tombée sur le bassin du lac Ontario et du fleuve "
    "Saint-Laurent en 2017, et qu'en 2019 il entrait trop d'eau dans le lac Ontario depuis un "
    "lac Érié en crue, sans autre issue qu'un Saint-Laurent lui-même en crue, avec des apports "
    "record du lac Érié et une fonte des neiges tardive et abondante conjuguée à un printemps "
    "extrêmement pluvieux. Les niveaux du lac Ontario ont fini par dépasser en 2019 leur pointe "
    "record de 2017. De novembre à mai en 2019, Toronto a reçu 555,6 mm de précipitations, le "
    "quatrième total le plus élevé depuis 1938, et Watertown, dans l'État de New York, 823,7 mm, "
    "le deuxième depuis 1898. La Commission énonce aussi clairement sa propre conclusion : les "
    "hauts niveaux d'eau n'ont pas été causés par la régulation des débits sortants ni par le "
    "Plan 2014. Elle ne publie aucune pointe en mètres ni aucun chiffre de dommages ; ni l'un ni "
    "l'autre ne figure donc ici."))
a.h3(T("The First Nations on the lake today",
       "Les Premières Nations du lac aujourd'hui"))
a.p(T(
    "Ontario's official First Nations and treaties map, last revised in April 2026, shows on or "
    "near Lake Ontario and its immediate watershed: the Mississaugas of the Credit; the "
    "Mississaugas of Scugog Island; Alderville; Hiawatha; Curve Lake; the Mohawks of the Bay of "
    "Quinte at Tyendinaga; Six Nations of the Grand River; the Chippewas of Georgina Island; and "
    "the Chippewas of Rama.",
    "La carte officielle des Premières Nations et des traités de l'Ontario, révisée pour la "
    "dernière fois en avril 2026, montre sur le lac Ontario ou son bassin immédiat, ou à "
    "proximité : les Mississaugas of the Credit ; les Mississaugas de l'île Scugog ; Alderville ; "
    "Hiawatha ; Curve Lake ; les Mohawks de la baie de Quinte à Tyendinaga ; les Six Nations de "
    "la rivière Grand ; les Chippewas de l'île Georgina ; et les Chippewas de Rama."))
a.p(T(
    "Alderville First Nation publishes its own history, and it is a history of holding on. The "
    "Mississauga Anishinabeg of the Ojibway Nation originally inhabited their traditional lands "
    "around the Bay of Quinte at Grape Island. After 1783 Loyalist arrivals created increased "
    "pressure on Mississauga lands, forcing land surrenders along the St. Lawrence and the Bay. "
    "By the 1820s many had converted to Methodism, and in 1826 they established a mission on "
    "Grape Island where people learned literacy and agriculture — which the Nation describes not "
    "as a replacement of their own ways but as a hybrid, or a mixed composition of traditional "
    "and western values. The Nation writes that the Mississauga maintained a hold on many of "
    "their traditions including the Ojibway language, and that as assimilation policies "
    "hardened, resistance strengthened, becoming the basis upon which the cultural survival of "
    "the people has been maintained.",
    "La Première Nation d'Alderville publie sa propre histoire, et c'est une histoire de "
    "ténacité. Les Mississaugas anishinabegs de la nation ojibwée habitaient à l'origine leurs "
    "terres traditionnelles autour de la baie de Quinte, à l'île Grape. Après 1783, l'arrivée "
    "des loyalistes a accru la pression sur les terres mississaugas, forçant des cessions le "
    "long du Saint-Laurent et de la baie. Dans les années 1820, beaucoup s'étaient convertis au "
    "méthodisme et, en 1826, ils ont établi une mission à l'île Grape où l'on apprenait à lire, "
    "à écrire et à cultiver — ce que la Nation décrit non pas comme le remplacement de ses "
    "propres façons de faire, mais comme un métissage, une composition mixte de valeurs "
    "traditionnelles et occidentales. La Nation écrit que les Mississaugas ont conservé "
    "beaucoup de leurs traditions, dont la langue ojibwée, et que, à mesure que les politiques "
    "d'assimilation se durcissaient, la résistance s'est renforcée, devenant le fondement sur "
    "lequel la survie culturelle du peuple s'est maintenue."))
a.p(T(
    "The City of Toronto's official land acknowledgement, adopted in February 2019, names the "
    "nations of this place: the land is the traditional territory of many nations including the "
    "Mississaugas of the Credit, the Anishnabeg, the Chippewa, the Haudenosaunee and the Wendat "
    "peoples, and is now home to many diverse First Nations, Inuit and Métis peoples. It also "
    "acknowledges that Toronto is covered by Treaty 13 with the Mississaugas of the Credit.",
    "La reconnaissance territoriale officielle de la Ville de Toronto, adoptée en février 2019, "
    "nomme les nations de ce lieu : la terre est le territoire traditionnel de nombreuses "
    "nations, dont les Mississaugas of the Credit, les Anishnabegs, les Chippewas, les "
    "Haudenosaunee et les peuples wendats, et elle abrite aujourd'hui de nombreux peuples "
    "divers des Premières Nations, inuits et métis. Elle reconnaît aussi que Toronto est visée "
    "par le traité 13 conclu avec les Mississaugas of the Credit."))
a.p(T(
    "The southern shore of this lake, in New York State, is Tuscarora, Seneca and other "
    "Haudenosaunee territory. No permitted Canadian source used for this page covers those "
    "nations, and rather than write as though the south shore were empty, this page names the "
    "omission.",
    "La rive sud de ce lac, dans l'État de New York, est un territoire tuscarora, seneca et "
    "d'autres nations haudenosaunee. Aucune source canadienne autorisée utilisée pour cette page "
    "ne traite de ces nations et, plutôt que d'écrire comme si la rive sud était vide, cette "
    "page nomme l'omission."))
a.h3(T("What sits on the shore now", "Ce qui se trouve sur la rive aujourd'hui"))
a.p(T(
    "Ontario Power Generation operates the Pickering and Darlington nuclear stations on the "
    "north shore, both drawing cooling water from Lake Ontario, and both regulated by the "
    "Canadian Nuclear Safety Commission. Toronto draws its drinking water from four Lake Ontario "
    "plants: R.C. Harris at 950 million litres a day, F.J. Horgan at 800 million, R.L. Clark at "
    "615 million and the Island plant at 440 million. The City does not publish how many people "
    "each plant serves, or where the intakes sit.",
    "Ontario Power Generation exploite les centrales nucléaires de Pickering et de Darlington sur "
    "la rive nord, toutes deux alimentées en eau de refroidissement par le lac Ontario et toutes "
    "deux réglementées par la Commission canadienne de sûreté nucléaire. Toronto puise son eau "
    "potable dans quatre usines du lac Ontario : R.C. Harris, à 950 millions de litres par jour, "
    "F.J. Horgan, à 800 millions, R.L. Clark, à 615 millions, et l'usine de l'île, à "
    "440 millions. La Ville ne publie pas combien de personnes chaque usine dessert, ni où se "
    "trouvent les prises d'eau."))
a.p(T(
    "The 2019 Canadian nearshore assessment for Lake Ontario, covering 17 regional units, "
    "concludes that overall, nearshore areas in Lake Ontario are under moderate stress, that "
    "western Lake Ontario is under far greater development pressure than the east, and that many "
    "of the regional units are under high stress due to the extensive construction of shoreline "
    "stabilizing structures. It records Cladophora fouling beaches from Burlington Beach to "
    "Humber Bay, and harmful cyanobacteria detected in Hamilton Harbour, the Bay of Quinte and "
    "the Kingston Basin, creating a concern to human and ecosystem health.",
    "L'évaluation canadienne de la zone littorale du lac Ontario de 2019, portant sur 17 unités "
    "régionales, conclut que, dans l'ensemble, les zones littorales du lac Ontario subissent un "
    "stress modéré, que l'ouest du lac Ontario subit une pression de développement bien plus "
    "forte que l'est, et que de nombreuses unités régionales subissent un stress élevé en raison "
    "de la construction massive d'ouvrages de stabilisation du rivage. Elle consigne que la "
    "Cladophora souille les plages de Burlington Beach à la baie Humber, et que des "
    "cyanobactéries nocives ont été détectées dans le port de Hamilton, la baie de Quinte et le "
    "bassin de Kingston, ce qui soulève des préoccupations pour la santé humaine et celle de "
    "l'écosystème."))

# ------------------------------------------------------------------ 15
a.h2(T("What is not settled", "Ce qui n'est pas réglé"))
a.p(T(
    "A page about a lake this old should end by saying what it cannot say. Each item below is a "
    "real gap or a real disagreement in the official record, not a shortcut taken here.",
    "Une page sur un lac aussi ancien devrait se terminer en disant ce qu'elle ne peut pas dire. "
    "Chaque point ci-dessous est une vraie lacune ou un vrai désaccord dans le dossier officiel, "
    "et non un raccourci pris ici."))
a.ul([
    T("<strong>What the name means.</strong> Three official sources say sparkling water and one "
      "says vast body of water, and only the last one hedges.",
      "<strong>Le sens du nom.</strong> Trois sources officielles disent eau scintillante et une "
      "dit vaste étendue d'eau, et seule la dernière nuance."),
    T("<strong>Which language it comes from.</strong> Every source stops at Iroquois or "
      "Iroquoian, which is a family of languages and not a language.",
      "<strong>La langue dont il vient.</strong> Chaque source s'arrête à iroquois ou iroquoien, "
      "qui est une famille de langues et non une langue."),
    T("<strong>What the 1641 record actually named.</strong> Natural Resources Canada says a "
      "mass of land; Immigration, Refugees and Citizenship Canada says the lake.",
      "<strong>Ce que le document de 1641 nommait réellement.</strong> Ressources naturelles "
      "Canada dit une masse de terre ; Immigration, Réfugiés et Citoyenneté Canada dit le lac."),
    T("<strong>The lake's name in any Indigenous language, and its French historical names.</strong> "
      "Not published by any source used here — the largest single gap on this page.",
      "<strong>Le nom du lac dans une langue autochtone, et ses noms historiques français.</strong> "
      "Non publiés par aucune source utilisée ici — la plus grande lacune de cette page."),
    T("<strong>How long people have been on this shore.</strong> More than 10,000 years, 11,000 "
      "years and 15,000 years are all published, and the last is hard to square with ice leaving "
      "the basin 13,000 years ago.",
      "<strong>Depuis combien de temps il y a des gens sur cette rive.</strong> Plus de "
      "10 000 ans, 11 000 ans et 15 000 ans sont tous publiés, et le dernier chiffre se concilie "
      "mal avec un retrait des glaces du bassin il y a 13 000 ans."),
    T("<strong>The Toronto Purchase acreage.</strong> 250,808, 250,830 and approximately 250,800 "
      "acres, from three official bodies, for the same treaty.",
      "<strong>La superficie de l'achat de Toronto.</strong> 250 808, 250 830 et environ "
      "250 800 acres, selon trois organismes officiels, pour le même traité."),
    T("<strong>Six Nations' remaining land.</strong> Approximately 46,500 acres as of March 2010 "
      "and approximately 45,482.951 acres as of 1995, both in the same publication.",
      "<strong>Les terres qui restent aux Six Nations.</strong> Environ 46 500 acres en mars "
      "2010 et environ 45 482,951 acres en 1995, les deux dans la même publication."),
    T("<strong>Whether the Rouge Tract settlement is final.</strong> The First Nation says "
      "finalized in 2025; Canada and Ontario in March 2025 described a proposed settlement "
      "awaiting a vote.",
      "<strong>Si le règlement du territoire de la Rouge est final.</strong> La Première Nation "
      "dit finalisé en 2025 ; le Canada et l'Ontario, en mars 2025, décrivaient un règlement "
      "proposé en attente d'un vote."),
    T("<strong>Fort Frontenac's end in 1688 or 1689.</strong> Parks Canada says the French "
      "ordered its destruction; National Defence says scurvy emptied the garrison first.",
      "<strong>La fin du fort Frontenac en 1688 ou en 1689.</strong> Parcs Canada dit que les "
      "Français en ont ordonné la destruction ; la Défense nationale dit que le scorbut a vidé "
      "la garnison d'abord."),
    T("<strong>How many died building the Rideau Canal.</strong> Canada's published word is "
      "hundreds. The often-printed figure of about a thousand has no official source.",
      "<strong>Combien de personnes sont mortes en bâtissant le canal Rideau.</strong> Le mot "
      "publié par le Canada est des centaines. Le chiffre souvent imprimé d'environ un millier "
      "n'a aucune source officielle."),
    T("<strong>How many died building the Welland Canal.</strong> Parks Canada states that the "
      "records were never kept, because there were no health and safety regulations. There is no "
      "number to find.",
      "<strong>Combien de personnes sont mortes en bâtissant le canal Welland.</strong> Parcs "
      "Canada affirme que les registres n'ont jamais été tenus, faute de règlements de santé et "
      "de sécurité. Il n'y a aucun chiffre à trouver."),
    T("<strong>How the sea lamprey arrived and spread.</strong> Ontario says the Erie Canal and "
      "1921; Fisheries and Oceans Canada says the deepened Welland Canal in 1919 and all five "
      "lakes by 1938.",
      "<strong>Comment la lamproie marine est arrivée et s'est répandue.</strong> L'Ontario dit "
      "le canal Érié et 1921 ; Pêches et Océans Canada dit l'approfondissement du canal Welland "
      "en 1919 et les cinq lacs envahis en 1938."),
    T("<strong>The Seaway's effect on Akwesasne, and the Lost Villages in numbers.</strong> "
      "Neither is published by the bodies that publish everything else about the project.",
      "<strong>Les effets de la Voie maritime sur Akwesasne, et les villages engloutis en "
      "chiffres.</strong> Ni l'un ni l'autre ne sont publiés par les organismes qui publient "
      "tout le reste sur ce projet."),
    T("<strong>Lake Ontario's water volume and retention time.</strong> Not printed here; the "
      "one published volume figure carries a unit error and no retention time was found.",
      "<strong>Le volume d'eau et le temps de séjour du lac Ontario.</strong> Non imprimés ici ; "
      "le seul chiffre de volume publié comporte une erreur d'unité et aucun temps de séjour n'a "
      "été trouvé."),
    T("<strong>A current count of who drinks from this lake.</strong> The 49.2% figure rests on "
      "an Ontario population of 12.8 million, and no newer lake-specific figure has been "
      "published.",
      "<strong>Un décompte actuel des personnes qui boivent l'eau de ce lac.</strong> Le chiffre "
      "de 49,2 % repose sur une population ontarienne de 12,8 millions, et aucun chiffre plus "
      "récent propre à ce lac n'a été publié."),
])

# ------------------------------------------------------------------ 16
a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("indigenous-peoples-of-canada.html",
         T("Indigenous Peoples of Canada — First Nations, Inuit and Métis",
           "Les peuples autochtones du Canada — Premières Nations, Inuits et Métis")),
    link("a-short-history-of-canada.html",
         T("A short history of Canada", "Une courte histoire du Canada")),
    link("how-canada-built-the-railway.html",
         T("How Canada built its first railway across the country",
           "Comment le Canada a bâti son premier chemin de fer d'un océan à l'autre")),
    link("canadas-biggest-cities.html",
         T("Canada's biggest cities", "Les plus grandes villes du Canada")),
    link("voyageurs-and-the-fur-trade-for-kids.html",
         T("The voyageurs and the fur trade, for kids",
           "Les voyageurs et la traite des fourrures, pour les enfants")),
])

a.sources(T("Where this came from", "D'où vient tout ceci"), [
    out_link("https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-canada/origin-names-canada-its-provinces-territories",
             T("Natural Resources Canada — origin of the names of Canada and its provinces and "
               "territories",
               "Ressources naturelles Canada — origine des noms du Canada et de ses provinces "
               "et territoires")),
    out_link("https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-canada/origin-names-canadas-provincial-territorial-capitals",
             T("Natural Resources Canada — origin of the names of Canada's provincial and "
               "territorial capitals",
               "Ressources naturelles Canada — origine des noms des capitales provinciales et "
               "territoriales du Canada")),
    out_link("https://www.canada.ca/en/canadian-heritage/services/provincial-territorial-symbols-canada/ontario.html",
             T("Canadian Heritage — Ontario, provincial and territorial symbols",
               "Patrimoine canadien — Ontario, symboles provinciaux et territoriaux")),
    out_link("https://www.canada.ca/en/immigration-refugees-citizenship/services/canadians/celebrate-being-canadian/teachers-corner/pin-symbol-province-territory/fact-sheet-ontario.html",
             T("Immigration, Refugees and Citizenship Canada — Ontario fact sheet",
               "Immigration, Réfugiés et Citoyenneté Canada — fiche d'information sur "
               "l'Ontario")),
    out_link("https://www.ontario.ca/page/about-ontario",
             T("Government of Ontario — About Ontario",
               "Gouvernement de l'Ontario — À propos de l'Ontario")),
    out_link("https://www.ontario.ca/page/geographic-names-ontario-language-principles-and-procedures",
             T("Government of Ontario — geographic names, language principles and procedures",
               "Gouvernement de l'Ontario — noms géographiques, principes et procédures "
               "linguistiques")),
    out_link("https://parks.canada.ca/pn-np/on/rouge/nature/environnement-environment/geo",
             T("Parks Canada — the geology of Rouge National Urban Park",
               "Parcs Canada — la géologie du parc urbain national de la Rouge")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=531",
             T("Parks Canada — Bead Hill National Historic Site, Ganatsekwyagon",
               "Parcs Canada — lieu historique national de Bead Hill, Ganatsekwyagon")),
    out_link("https://www.heritagetrust.on.ca/provincial-plaque-program/provincial-plaque-background-papers/jean-baptiste-laine-site",
             T("Ontario Heritage Trust — the Jean-Baptiste Lainé site background paper",
               "Fiducie du patrimoine ontarien — document d'information sur le site "
               "Jean-Baptiste-Lainé")),
    out_link("https://www.heritagetrust.on.ca/heritagematters/articles/the-archaeology-of-southwestern-ontario",
             T("Ontario Heritage Trust — the archaeology of southwestern Ontario",
               "Fiducie du patrimoine ontarien — l'archéologie du sud-ouest de l'Ontario")),
    out_link("https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=11706",
             T("Canada's Historic Places — Southwold Earthworks, the Attiwandaron village",
               "Lieux patrimoniaux du Canada — les Earthworks de Southwold, village "
               "attiwandaron")),
    out_link("https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=13721",
             T("Canada's Historic Places — the Norton Attawandaron site, London",
               "Lieux patrimoniaux du Canada — le site Norton Attawandaron, à London")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=11450",
             T("Parks Canada — Mission of St. Ignace II National Historic Site",
               "Parcs Canada — lieu historique national de la mission Saint-Ignace II")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1798",
             T("Parks Canada — Dispersal of Huron-Wendat from Huronia",
               "Parcs Canada — dispersion des Hurons-Wendats de la Huronie")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1175",
             T("Parks Canada — Wyandot (Hurons) National Historic Event, flagged for review",
               "Parcs Canada — événement historique national des Wyandots (Hurons), signalé "
               "pour révision")),
    out_link("https://www.toronto.ca/wp-content/uploads/2025/01/9473-CityPlanning-Teiaiagon-Baby-Point-History-and-Evolution-December-2024.pdf",
             T("City of Toronto — Teiaiagon and Baby Point, history and evolution, December 2024",
               "Ville de Toronto — Teiaiagon et Baby Point, histoire et évolution, décembre "
               "2024")),
    out_link("https://mncfn.ca/about-mncfn/treaty-lands-and-territory/",
             T("Mississaugas of the Credit First Nation — treaty lands and territory",
               "Mississaugas of the Credit First Nation — terres et territoire visés par les "
               "traités")),
    out_link("https://mncfn.ca/the-toronto-purchase-treaty-no-13-1805/",
             T("Mississaugas of the Credit First Nation — the Toronto Purchase, Treaty No. 13",
               "Mississaugas of the Credit First Nation — l'achat de Toronto, traité no 13")),
    out_link("https://mncfn.ca/treaty-lands-territory/rouge-claim/",
             T("Mississaugas of the Credit First Nation — the Rouge Tract settlement",
               "Mississaugas of the Credit First Nation — le règlement du territoire de la "
               "Rouge")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1937",
             T("Parks Canada — the Great Peace of Montréal, 1701",
               "Parcs Canada — la Grande Paix de Montréal, 1701")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1653",
             T("Parks Canada — the Toronto Carrying Place, flagged for review",
               "Parcs Canada — le passage de Toronto, signalé pour révision")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=358",
             T("Parks Canada — the Carrying Place of the Bay of Quinte, flagged for review",
               "Parcs Canada — le passage de la baie de Quinte, signalé pour révision")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1673",
             T("Parks Canada — Étienne Brûlé National Historic Person, flagged for review",
               "Parcs Canada — Étienne Brûlé, personnage d'importance historique nationale, "
               "signalé pour révision")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1250",
             T("Parks Canada — Samuel de Champlain National Historic Person, flagged for review",
               "Parcs Canada — Samuel de Champlain, personnage d'importance historique "
               "nationale, signalé pour révision")),
    out_link("https://www.historymuseum.ca/virtual-museum-of-new-france/the-explorers/etienne-brule-1615-1621/",
             T("Canadian Museum of History — Étienne Brûlé, 1615 to 1621",
               "Musée canadien de l'histoire — Étienne Brûlé, 1615 à 1621")),
    out_link("https://www.historymuseum.ca/virtual-museum-of-new-france/economic-activities/fur-trade/",
             T("Canadian Museum of History — the fur trade",
               "Musée canadien de l'histoire — la traite des fourrures")),
    out_link("https://www.historymuseum.ca/cmc/vmnf/premieres_nations/en/iroquoians/description.html",
             T("Canadian Museum of History — the Iroquoians",
               "Musée canadien de l'histoire — les Iroquoiens")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=392",
             T("Parks Canada — Fort Frontenac National Historic Site",
               "Parcs Canada — lieu historique national du Fort-Frontenac")),
    out_link("https://www.canada.ca/content/dam/dnd-mdn/migration/assets/FORCES_Internet/docs/en/training-establishments/ff-history-cacsc-eng.pdf",
             T("Department of National Defence — a history of Fort Frontenac",
               "Ministère de la Défense nationale — une histoire du fort Frontenac")),
    out_link("https://www.heritagetrust.on.ca/plaques/fort-rouille",
             T("Ontario Heritage Trust — the Fort Rouillé plaque",
               "Fiducie du patrimoine ontarien — la plaque du fort Rouillé")),
    out_link("https://www.internationalboundarycommission.org/en/about/history.php",
             T("International Boundary Commission — the history of the boundary",
               "Commission de la frontière internationale — l'histoire de la frontière")),
    out_link("https://www.sixnations.ca/LandsResources/SNLands-LandRightsBook-FINALyr2020.pdf",
             T("Six Nations of the Grand River — the Land Rights book, 2020",
               "Six Nations of the Grand River — le livre sur les droits fonciers, 2020")),
    out_link("https://www.sixnations.ca/who-we-are/",
             T("Six Nations of the Grand River — who we are",
               "Six Nations of the Grand River — qui nous sommes")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1242",
             T("Parks Canada — the Six Nations National Historic Event, flagged for review",
               "Parcs Canada — l'événement historique national des Six Nations, signalé pour "
               "révision")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1246",
             T("Parks Canada — Thayendanega, Joseph Brant, flagged for review",
               "Parcs Canada — Thayendanega, Joseph Brant, signalé pour révision")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1198",
             T("Parks Canada — the Coming of the Mohawks, Tyendinaga",
               "Parcs Canada — l'arrivée des Mohawks, Tyendinaga")),
    out_link("https://www.canada.ca/en/crown-indigenous-relations-northern-affairs/news/2022/10/mohawks-of-the-bay-of-quinte-and-canada-take-a-step-toward-reconciliation-with-partial-settlement-of-historic-claim.html",
             T("Crown-Indigenous Relations and Northern Affairs Canada — the Culbertson Tract "
               "partial settlement",
               "Relations Couronne-Autochtones et Affaires du Nord Canada — le règlement "
               "partiel du territoire Culbertson")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1370372152585/1581293792285",
             T("CIRNAC — treaty texts, Upper Canada land surrenders",
               "RCAANC — textes des traités, cessions de terres du Haut-Canada")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1100100029000/1564415701529",
             T("CIRNAC — treaty research report, the Williams Treaties, 1923",
               "RCAANC — rapport de recherche sur les traités, les traités Williams, 1923")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1360941656761/1544619778887",
             T("CIRNAC — Upper Canada land surrenders and the Williams Treaties",
               "RCAANC — cessions de terres du Haut-Canada et traités Williams")),
    out_link("https://www.rcaanc-cirnac.gc.ca/eng/1542370282768/1542370308434",
             T("CIRNAC — the Williams Treaties First Nations settlement agreement",
               "RCAANC — l'entente de règlement avec les Premières Nations des traités "
               "Williams")),
    out_link("https://www.canada.ca/en/news/archive/2010/10/canada-mississaugas-new-credit-first-nation-celebrate-historic-claim-settlement.html",
             T("Government of Canada — the 2010 Toronto Purchase and Brant Tract claim "
               "settlement",
               "Gouvernement du Canada — le règlement de 2010 des revendications de l'achat de "
               "Toronto et du territoire Brant")),
    out_link("https://www.canada.ca/en/crown-indigenous-relations-northern-affairs/news/2025/03/mississaugas-of-the-credit-first-nation-ontario-and-canada-announce-proposed-settlement-and-next-steps-on-rouge-river-valley-tract-claim.html",
             T("Canada and Ontario — the proposed Rouge River Valley Tract settlement, March "
               "2025",
               "Le Canada et l'Ontario — le règlement proposé du territoire de la vallée de la "
               "Rouge, mars 2025")),
    out_link("https://www.ontario.ca/page/map-ontario-treaties-and-reserves",
             T("Government of Ontario — the map of Ontario treaties and reserves",
               "Gouvernement de l'Ontario — la carte des traités et des réserves de l'Ontario")),
    out_link("https://www.heritagetrust.on.ca/plaques/loyalist-landing-at-cataraqui",
             T("Ontario Heritage Trust — the Loyalist Landing at Cataraqui, 1784",
               "Fiducie du patrimoine ontarien — le débarquement des loyalistes à Cataraqui, "
               "1784")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=11130",
             T("Parks Canada — Niagara-on-the-Lake National Historic Site",
               "Parcs Canada — lieu historique national de Niagara-on-the-Lake")),
    out_link("https://www.heritagetrust.on.ca/user_assets/documents/06-Chapter-1-A-New-Capital.pdf",
             T("Ontario Heritage Trust — Laying the Foundations for Upper Canada, a new capital",
               "Fiducie du patrimoine ontarien — les fondations du Haut-Canada, une nouvelle "
               "capitale")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=538",
             T("Parks Canada — Fort York National Historic Site",
               "Parcs Canada — lieu historique national du Fort-York")),
    out_link("https://www.heritagetrust.on.ca/plaques/george-hamilton-1787-1836",
             T("Ontario Heritage Trust — the George Hamilton plaque",
               "Fiducie du patrimoine ontarien — la plaque de George Hamilton")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1320",
             T("Parks Canada — the Underground Railroad National Historic Event",
               "Parcs Canada — l'événement historique national du chemin de fer clandestin")),
    out_link("https://www.heritagetrust.on.ca/plaques/typhus-epidemic-1847",
             T("Ontario Heritage Trust — the typhus epidemic of 1847, Kingston",
               "Fiducie du patrimoine ontarien — l'épidémie de typhus de 1847, Kingston")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=400",
             T("Parks Canada — the Kingston Navy Yard National Historic Site",
               "Parcs Canada — lieu historique national du chantier naval de Kingston")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=14212",
             T("Parks Canada — the War of 1812 Shipwrecks National Historic Site",
               "Parcs Canada — lieu historique national des épaves de la guerre de 1812")),
    out_link("https://www.canada.ca/en/news/archive/2013/04/canadian-armed-forces-commemorate-battle-york.html",
             T("Government of Canada — the Canadian Armed Forces commemorate the Battle of York",
               "Gouvernement du Canada — les Forces armées canadiennes commémorent la bataille "
               "d'York")),
    out_link("https://www.heritagetrust.on.ca/plaques/second-invasion-of-york-1813",
             T("Ontario Heritage Trust — the second invasion of York, 1813",
               "Fiducie du patrimoine ontarien — la seconde invasion d'York, 1813")),
    out_link("https://parks.canada.ca/lhn-nhs/on/rideau/histoire-history",
             T("Parks Canada — the Rideau Canal, culture and history",
               "Parcs Canada — le canal Rideau, culture et histoire")),
    out_link("https://parks.canada.ca/docs/r/on/rideau/whl-lhm/chap2/chap2b",
             T("Parks Canada — the Rideau Canal World Heritage nomination, history and "
               "development",
               "Parcs Canada — la proposition d'inscription du canal Rideau au patrimoine "
               "mondial, histoire et développement")),
    out_link("https://www.canada.ca/en/news/archive/2013/06/government-canada-commemorates-contributions-rideau-canal-construction-workers.html",
             T("Government of Canada — commemorating the Rideau Canal construction workers",
               "Gouvernement du Canada — commémoration des travailleurs de la construction du "
               "canal Rideau")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=1583",
             T("Parks Canada — the Welland Canal System National Historic Event",
               "Parcs Canada — l'événement historique national du réseau du canal Welland")),
    out_link("https://www.pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=10266",
             T("Parks Canada — the Construction of the St. Lawrence Seaway",
               "Parcs Canada — la construction de la Voie maritime du Saint-Laurent")),
    out_link("https://greatlakes-seaway.com/en/the-seaway/facts-figures/",
             T("Great Lakes St. Lawrence Seaway System — facts and figures",
               "Réseau Grands Lacs Voie maritime du Saint-Laurent — faits et chiffres")),
    out_link("https://ijc.org/en/loslrb/lake-st-lawrence/population",
             T("International Joint Commission — Lake St. Lawrence, local population and the "
               "Lost Villages",
               "Commission mixte internationale — le lac Saint-Laurent, la population locale et "
               "les villages engloutis")),
    out_link("https://ijc.org/en/loslrb/watershed/causes-2019-high-water-event",
             T("International Joint Commission — the causes of the 2019 high water event",
               "Commission mixte internationale — les causes de la crue de 2019")),
    out_link("https://www.ontario.ca/page/fish-management-history",
             T("Government of Ontario — fish management history",
               "Gouvernement de l'Ontario — histoire de la gestion des pêches")),
    out_link("https://www.dfo-mpo.gc.ca/species-especes/publications/ais-eae/lamprey-lamproie/index-eng.html",
             T("Fisheries and Oceans Canada — sea lamprey and the Great Lakes fishery",
               "Pêches et Océans Canada — la lamproie marine et la pêche des Grands Lacs")),
    out_link("https://www.canada.ca/en/environment-climate-change/corporate/international-affairs/partnerships-countries-regions/north-america/great-lakes-water-quality-agreement.html",
             T("Environment and Climate Change Canada — the Great Lakes Water Quality Agreement",
               "Environnement et Changement climatique Canada — l'Accord relatif à la qualité "
               "de l'eau dans les Grands Lacs")),
    out_link("https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/restoring-great-lakes-areas-concern.html",
             T("Environment and Climate Change Canada — restoring the Great Lakes Areas of "
               "Concern",
               "Environnement et Changement climatique Canada — la restauration des secteurs "
               "préoccupants des Grands Lacs")),
    out_link("https://www.canada.ca/en/canada-water-agency/freshwater-ecosystem-initiatives/great-lakes/great-lakes-protection/areas-concern/hamilton-harbour/randle-reef.html",
             T("Canada Water Agency — Randle Reef, Hamilton Harbour",
               "Agence de l'eau du Canada — le récif Randle, port de Hamilton")),
    out_link("https://binational.net/wp-content/uploads/2026/01/State-of-the-Great-Lakes-2025-Report.pdf",
             T("State of the Great Lakes 2025 Report, Canada and the United States",
               "Rapport sur l'état des Grands Lacs de 2025, Canada et États-Unis")),
    out_link("https://binational.net/wp-content/uploads/2021/03/FINAL-EN-2018-22-Lake-Ontario-LAMP-2021-01-13.pdf",
             T("Lake Ontario Lakewide Action and Management Plan, 2018 to 2022",
               "Plan d'action et d'aménagement panlacustre du lac Ontario, 2018 à 2022")),
    out_link("https://www.canada.ca/en/canada-water-agency/freshwater-ecosystem-initiatives/great-lakes/great-lakes-protection/taking-action-protect/nearshore-waters/lake-ontario-nearshore-assessment.html",
             T("Canada Water Agency — the Lake Ontario Canadian nearshore assessment, 2019",
               "Agence de l'eau du Canada — l'évaluation canadienne de la zone littorale du lac "
               "Ontario, 2019")),
    out_link("https://www.canada.ca/en/canada-water-agency/freshwater-ecosystem-initiatives/great-lakes/great-lakes-protection/maps/lake-ontario-drainage-basin.html",
             T("Canada Water Agency — the Lake Ontario drainage basin",
               "Agence de l'eau du Canada — le bassin de drainage du lac Ontario")),
    out_link("https://www150.statcan.gc.ca/n1/pub/11-402-x/2012000/chap/geo/tbl/tbl05-eng.htm",
             T("Statistics Canada — selected principal lakes, elevation and area",
               "Statistique Canada — principaux lacs choisis, altitude et superficie")),
    out_link("https://www150.statcan.gc.ca/n1/daily-quotidien/220209/dq220209a-eng.htm",
             T("Statistics Canada — 2021 Census population and dwelling counts",
               "Statistique Canada — chiffres de population et des logements du Recensement de "
               "2021")),
    out_link("https://www.ontario.ca/page/ontarios-great-lakes-strategy",
             T("Government of Ontario — Ontario's Great Lakes Strategy",
               "Gouvernement de l'Ontario — la stratégie ontarienne pour les Grands Lacs")),
    out_link("https://www.ontario.ca/files/2026-04/iafner-first-nations-and-treaties-map-en-2026-04-17.pdf",
             T("Government of Ontario — the First Nations and treaties map",
               "Gouvernement de l'Ontario — la carte des Premières Nations et des traités")),
    out_link("https://alderville.ca/alderville-first-nation/history/",
             T("Alderville First Nation — our history",
               "Première Nation d'Alderville — notre histoire")),
    out_link("https://www.toronto.ca/city-government/accessibility-human-rights/indigenous-affairs-office/land-acknowledgement/",
             T("City of Toronto — the land acknowledgement",
               "Ville de Toronto — la reconnaissance territoriale")),
    out_link("https://guides.library.utoronto.ca/Toronto",
             T("University of Toronto Libraries — the Indigenous history of Tkaronto",
               "Bibliothèques de l'Université de Toronto — l'histoire autochtone de Tkaronto")),
    out_link("https://www.toronto.ca/services-payments/water-environment/tap-water-in-toronto/fast-facts-about-the-citys-water-treatment-plants/",
             T("City of Toronto — fast facts about the city's water treatment plants",
               "Ville de Toronto — faits saillants sur les usines de traitement de l'eau de la "
               "ville")),
    out_link("https://www.opg.com/power-generation/our-power/nuclear/darlington-nuclear/",
             T("Ontario Power Generation — Darlington Nuclear",
               "Ontario Power Generation — la centrale nucléaire de Darlington")),
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
