#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article 3 of 3 — how Canada rebuilds.

The rule this page is built on: say "excluding gold" every single time
diversification is praised, because Global Affairs Canada itself does, and
because leaving it out is how "Canada fully replaced the American market" gets
printed as a fact when it is not one. Announced money and money that reached a
person are kept in separate paragraphs. Targets are never written as results.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="how-canada-rebuilds-its-economy.html",
    section="Trade",
    title=T("How Canada Rebuilds Its Economy Under Tariffs",
            "Comment le Canada rebâtit son économie sous les tarifs"),
    desc=T("New customers, internal trade, ports and pipelines: what Canada has "
           "actually done since 2025, what reached people, what is only a target, "
           "and what economists say is realistic.",
           "Nouveaux clients, commerce intérieur, ports et pipelines : ce que le "
           "Canada a réellement fait depuis 2025, ce qui s'est rendu aux gens, ce qui "
           "n'est qu'une cible, et ce que les économistes jugent réaliste."),
    h1=T("\U0001F341 How Canada rebuilds — new customers, old barriers",
         "\U0001F341 Comment le Canada se rebâtit — nouveaux clients, vieilles barrières"),
    hero=T("Canada sold 29 billion dollars more to the rest of the world in 2025. Take "
           "the gold out and it was 16 billion, against 32 billion lost in the United "
           "States. That one subtraction is the difference between a good news story "
           "and an honest one.",
           "Le Canada a vendu 29 milliards de dollars de plus au reste du monde en "
           "2025. Retirez l'or et il en reste 16 milliards, contre 32 milliards perdus "
           "aux États-Unis. Cette seule soustraction sépare une bonne nouvelle d'une "
           "nouvelle honnête."),
    checked=T("Last checked 22 August 2026 — this page covers a fast-moving situation",
              "Dernière vérification le 22 août 2026 — cette page traite d'une "
              "situation qui évolue vite"),
)

a.callout(T(
    "<strong>How this page is written.</strong> This is the Canadian half of the "
    "story, written for Canadians, and written against nobody. It is about what can be "
    "built here rather than about what happened to us. All dollar figures are Canadian "
    "dollars. We also keep two things apart that are often mixed together: money a "
    "government has announced over several years, and money that has actually reached "
    "a worker or a business. Both matter, but they are not the same thing, and only "
    "one of them can be counted yet.",
    "<strong>Comment cette page est écrite.</strong> Voici la moitié canadienne de "
    "l'histoire, écrite pour les Canadiens, et écrite contre personne. Elle porte sur "
    "ce qui peut être bâti ici plutôt que sur ce qui nous est arrivé. Tous les montants "
    "sont en dollars canadiens. Nous distinguons aussi deux choses souvent confondues : "
    "l'argent qu'un gouvernement a annoncé sur plusieurs années, et l'argent qui s'est "
    "réellement rendu à un travailleur ou à une entreprise. Les deux comptent, mais ce "
    "n'est pas la même chose, et une seule des deux est déjà mesurable."))

a.h2(T("Did Canada find other customers? Yes — and here is the catch",
       "Le Canada a-t-il trouvé d'autres clients? Oui — avec une réserve"))
a.p(T(
    "In 2025 Canada's merchandise exports to the United States fell by 30.7 billion "
    "dollars, and merchandise exports to everywhere else rose by 29.1 billion. Put "
    "like that, the new customers almost exactly replaced the old one, and a great "
    "many headlines said so.",
    "En 2025, les exportations canadiennes de marchandises vers les États-Unis ont "
    "reculé de 30,7 milliards de dollars, et les exportations vers tous les autres "
    "pays ont augmenté de 29,1 milliards. Dit ainsi, les nouveaux clients ont presque "
    "exactement remplacé l'ancien, et bien des manchettes l'ont écrit."))
a.p(T(
    "Global Affairs Canada published the same figures with the gold taken out, and the "
    "picture changes. Excluding gold, exports to the United States fell 32.0 billion "
    "and exports elsewhere rose 16.4 billion. Nearly 44 percent of the apparent gain "
    "was gold. In plain terms, the new customers replaced about half of what was lost, "
    "not all of it.",
    "Affaires mondiales Canada a publié les mêmes chiffres en retirant l'or, et le "
    "portrait change. Hors or, les exportations vers les États-Unis ont reculé de 32,0 "
    "milliards et les exportations ailleurs ont augmenté de 16,4 milliards. Près de 44 "
    "pour cent du gain apparent était de l'or. En clair, les nouveaux clients ont "
    "remplacé environ la moitié de ce qui a été perdu, pas la totalité."))

a.fig(bar_chart(
    T("2025: what was lost and what replaced it, in billions of dollars",
      "2025 : ce qui a été perdu et ce qui l'a remplacé, en milliards de dollars"),
    [(T("Lost in the United States, gold included", "Perdu aux États-Unis, or compris"), -30.7),
     (T("Gained elsewhere, gold included", "Gagné ailleurs, or compris"), 29.1),
     (T("Lost in the United States, gold excluded", "Perdu aux États-Unis, hors or"), -32.0),
     (T("Gained elsewhere, gold excluded", "Gagné ailleurs, hors or"), 16.4)],
    colours=["red", "green", "red", "blue"]),
    T("Global Affairs Canada, Quarterly Economic and Trade Report, Spring 2026. "
      "Merchandise trade only. Read the pairs together — the gold-included loss "
      "against the gold-included gain, and the same for gold excluded.",
      "Affaires mondiales Canada, Rapport économique et commercial trimestriel, "
      "printemps 2026. Commerce de marchandises seulement. Lisez les paires ensemble : "
      "la perte or compris avec le gain or compris, et de même hors or."))

a.p(T(
    "Where did the growth go? The United Kingdom was up 62 percent in 2025 and 81 "
    "percent again in the first half of 2026 — but London is the world's gold-trading "
    "hub, and Statistics Canada says directly that the surge is unwrought gold. In "
    "June 2026 Canada exported more to the United Kingdom, at 7.2 billion dollars, "
    "than to the entire European Union at 3.3 billion. That only makes sense as "
    "bullion. Meanwhile China rose 14.7 percent in 2025 and 34 percent so far in 2026, "
    "while Japan fell 2.8 percent, South Korea fell 7.2 percent and India fell 27 "
    "percent in the same year.",
    "Où la croissance est-elle allée? Le Royaume-Uni a bondi de 62 pour cent en 2025 "
    "et encore de 81 pour cent au premier semestre de 2026 — mais Londres est la plaque "
    "tournante mondiale du commerce de l'or, et Statistique Canada dit directement que "
    "la poussée vient de l'or non ouvré. En juin 2026, le Canada a exporté davantage "
    "vers le Royaume-Uni, à 7,2 milliards de dollars, que vers toute l'Union "
    "européenne, à 3,3 milliards. Cela ne s'explique que par les lingots. Pendant ce "
    "temps, la Chine a progressé de 14,7 pour cent en 2025 et de 34 pour cent depuis "
    "le début de 2026, tandis que le Japon reculait de 2,8 pour cent, la Corée du Sud "
    "de 7,2 pour cent et l'Inde de 27 pour cent la même année."))
a.p(T(
    "The softwood lumber industry gives the clearest single example of how hard "
    "replacement really is. In the first half of 2026, sales to China, Taiwan, Mexico, "
    "Pakistan, South Korea and Hong Kong all grew — and together they made up about 4 "
    "percent of the volume lost in the United States.",
    "L'industrie du bois d'œuvre offre l'exemple le plus net de la difficulté réelle "
    "du remplacement. Au premier semestre de 2026, les ventes vers la Chine, Taïwan, "
    "le Mexique, le Pakistan, la Corée du Sud et Hong Kong ont toutes augmenté — et "
    "ensemble, elles ont compensé environ 4 pour cent du volume perdu aux États-Unis."))
a.p(T(
    "None of which means nothing happened. Non-American markets took 32.8 percent of "
    "Canada's exports in 2025, the highest share since 1981. That is a genuine "
    "milestone. It just has gold in it, and the honest way to report it is to say both "
    "halves of the sentence.",
    "Rien de tout cela ne veut dire qu'il ne s'est rien passé. Les marchés non "
    "américains ont absorbé 32,8 pour cent des exportations canadiennes en 2025, la "
    "part la plus élevée depuis 1981. C'est un jalon véritable. Il contient simplement "
    "de l'or, et la façon honnête de le rapporter est de dire les deux moitiés de la "
    "phrase."))

a.h2(T("The support that actually reached people",
       "L'aide qui s'est réellement rendue aux gens"))
a.p(T(
    "Most of the money you read about in a budget is announced over five years. These "
    "are the numbers where somebody was actually helped, and they are the ones worth "
    "trusting. By March 2026 the Employment Insurance Work-Sharing programme covered "
    "more than 54,000 workers, and the government estimated it had helped prevent "
    "nearly 20,000 layoffs. More than 650,000 claims benefited from a temporary adjustment to "
    "the unemployment-rate rules by December 2025, and more than 165,000 claims got "
    "access to twenty extra weeks of benefits. Softwood lumber work-sharing grants of "
    "102.7 million dollars reached an estimated 26,000 workers, and steel workers on "
    "the programme had their replacement rate lifted from 55 to 70 percent.",
    "La majeure partie de l'argent dont parlent les budgets est annoncée sur cinq ans. "
    "Voici les chiffres où quelqu'un a réellement été aidé, et ce sont ceux auxquels il "
    "vaut la peine de se fier. En mars 2026, le programme de travail partagé de "
    "l'assurance-emploi couvrait plus de 54 000 travailleurs et le gouvernement "
    "estimait avoir contribué à éviter près de 20 000 mises à pied. Plus de 650 000 demandes ont "
    "profité d'un rajustement temporaire des règles du taux de chômage en date de "
    "décembre 2025, et plus de 165 000 demandes ont eu accès à vingt semaines de "
    "prestations supplémentaires. Des subventions de travail partagé de 102,7 millions "
    "de dollars pour le bois d'œuvre ont rejoint environ 26 000 travailleurs, et le "
    "taux de remplacement des sidérurgistes inscrits au programme est passé de 55 à 70 "
    "pour cent."))
a.p(T(
    "The announced side is larger. Budget 2025, tabled on 4 November 2025, put 16.5 "
    "billion dollars over five years into its tariff-response chapter, including 3.7 "
    "billion in income support and 570 million for retraining up to 66,000 workers. "
    "Separately there is a 10 billion dollar loan facility for large employers — its "
    "first loan was 400 million federal dollars plus 100 million from Ontario to Algoma "
    "Steel — a 5 billion dollar Strategic Response Fund, and roughly 1.5 billion "
    "through the regional development agencies. How much of that has actually been "
    "spent is not published, and we are not going to guess.",
    "Le côté annoncé est plus imposant. Le budget de 2025, déposé le 4 novembre 2025, "
    "a consacré 16,5 milliards de dollars sur cinq ans à son chapitre de réponse aux "
    "tarifs, dont 3,7 milliards en soutien du revenu et 570 millions pour le recyclage "
    "professionnel de jusqu'à 66 000 travailleurs. S'y ajoutent une facilité de prêt de "
    "10 milliards de dollars pour les grands employeurs — dont le premier prêt a été de "
    "400 millions du fédéral plus 100 millions de l'Ontario à Algoma Steel —, un Fonds "
    "de réponse stratégique de 5 milliards, et environ 1,5 milliard par les agences de "
    "développement régional. Quelle part a réellement été dépensée n'est pas publiée, "
    "et nous n'allons pas le deviner."))
a.p(T(
    "One number is worth noticing because it moved so far. The government first "
    "projected 20 billion dollars of counter-tariff revenue for the year. Budget 2025 "
    "revised that down to 4.4 billion, and the Department of Finance has reported over "
    "3 billion actually collected from counter-tariffs before most of them were "
    "dropped. A wider measure, all customs import duties, came to 9.506 billion "
    "between April 2025 and February 2026, up 84 percent on the year before — but that "
    "figure includes the ordinary tariff base as well, so it is not the counter-tariff "
    "total. The gap between the first projection and what was collected is itself part "
    "of the story: Canada lifted most of its counter-tariffs on 1 September 2025, so it "
    "stopped collecting them.",
    "Un chiffre mérite d'être remarqué parce qu'il a beaucoup bougé. Le gouvernement a "
    "d'abord prévu 20 milliards de dollars de recettes de contre-tarifs pour l'année. "
    "Le budget de 2025 a ramené cela à 4,4 milliards, et le ministère des Finances a "
    "fait état de plus de 3 milliards réellement perçus en contre-tarifs avant que la "
    "plupart soient levés. Une mesure plus large, l'ensemble des droits de douane à "
    "l'importation, a atteint 9,506 milliards entre avril 2025 et février 2026, en "
    "hausse de 84 pour cent sur un an — mais ce chiffre comprend aussi les droits "
    "ordinaires, ce n'est donc pas le total des contre-tarifs. L'écart entre la "
    "première prévision et ce qui a été perçu fait lui aussi partie de l'histoire : le Canada a levé la plupart de ses "
    "contre-tarifs le 1er septembre 2025 et a donc cessé de les percevoir."))

a.h2(T("Selling to each other: the biggest lever Canada actually controls",
       "Se vendre entre nous : le plus grand levier que le Canada contrôle vraiment"))
a.p(T(
    "Canada trades roughly half a trillion dollars a year across its own provincial "
    "borders, and it has always been harder than it should be. Statistics Canada found "
    "that trade within a province is 53 percent stronger than trade across a provincial "
    "border — the difference you would expect if there were a 6.9 percent tariff "
    "between provinces. That is where the famous line about an internal seven percent "
    "tariff comes from. It is Statistics Canada's number, not the International "
    "Monetary Fund's, and it is worth attributing correctly.",
    "Le Canada échange environ un demi-billion de dollars par année d'une province à "
    "l'autre, et cela a toujours été plus difficile que ce ne devrait l'être. "
    "Statistique Canada a constaté que le commerce à l'intérieur d'une province est 53 "
    "pour cent plus fort que le commerce entre provinces — l'écart qu'on attendrait "
    "s'il existait un tarif de 6,9 pour cent entre les provinces. C'est de là que vient "
    "la fameuse phrase sur un tarif intérieur de sept pour cent. C'est un chiffre de "
    "Statistique Canada, non du Fonds monétaire international, et il vaut la peine de "
    "l'attribuer correctement."))
a.p(T(
    "Two International Monetary Fund estimates are often merged, and they should not "
    "be. A 2019 paper found that fully freeing internal trade in goods could raise "
    "output per person by about 4 percent. A January 2026 assessment found that "
    "removing all internal barriers could raise real gross domestic product by about 7 "
    "percent, worth roughly 210 billion dollars — but four fifths of that gain comes "
    "from services, not goods. The federal government's own headline is up to 200 "
    "billion dollars, or about 5,100 dollars per person.",
    "Deux estimations du Fonds monétaire international sont souvent fusionnées, et "
    "elles ne devraient pas l'être. Une étude de 2019 concluait que la libéralisation "
    "complète du commerce intérieur des biens pourrait accroître la production par "
    "personne d'environ 4 pour cent. Une évaluation de janvier 2026 concluait que "
    "l'élimination de toutes les barrières intérieures pourrait accroître le produit "
    "intérieur brut réel d'environ 7 pour cent, soit à peu près 210 milliards de "
    "dollars — mais les quatre cinquièmes de ce gain viennent des services, non des "
    "biens. Le chiffre mis de l'avant par le gouvernement fédéral est de jusqu'à 200 "
    "milliards de dollars, ou environ 5 100 dollars par personne."))
a.p(T(
    "Not everyone believes those numbers. Marc Lee of the Canadian Centre for Policy "
    "Alternatives argued in February 2025 that the studies behind them do not measure "
    "barriers at all — they infer barriers from trade patterns, assume every province "
    "would otherwise buy in the same proportions despite real differences in what each "
    "one makes, and borrow trade sensitivities from the Canada-United States border for "
    "provinces that share a currency and have no customs posts. He notes that the "
    "sectors where barriers genuinely exist are only about 6.7 percent of the economy. "
    "That criticism is worth reading before treating 200 billion dollars as money "
    "sitting on a table.",
    "Tout le monde ne croit pas ces chiffres. Marc Lee, du Centre canadien de "
    "politiques alternatives, soutenait en février 2025 que les études sur lesquelles "
    "ils reposent ne mesurent pas les barrières du tout — elles les déduisent des flux "
    "commerciaux, supposent que chaque province achèterait autrement dans les mêmes "
    "proportions malgré des différences réelles de production, et empruntent des "
    "sensibilités commerciales de la frontière canado-américaine pour des provinces qui "
    "partagent une monnaie et n'ont aucun poste de douane. Il rappelle que les secteurs "
    "où des barrières existent vraiment ne représentent qu'environ 6,7 pour cent de "
    "l'économie. Cette critique mérite d'être lue avant de traiter 200 milliards de "
    "dollars comme de l'argent posé sur une table."))
a.p(T(
    "What has actually changed is real but partial. The One Canadian Economy Act "
    "received Royal Assent on 26 June 2025 and its free trade and labour mobility part "
    "came into force on 1 January 2026. All 53 federal exceptions to the Canadian Free "
    "Trade Agreement are gone; 94 of the 296 exceptions overall have been removed. All "
    "fourteen governments signed a mutual recognition agreement on the sale of goods in "
    "November 2025 — but it excludes food, drink, alcohol, tobacco, cannabis, plants "
    "and live animals, which is a large hole in a country that grows a great deal.",
    "Ce qui a réellement changé est vrai mais partiel. La Loi sur une économie "
    "canadienne unifiée a reçu la sanction royale le 26 juin 2025 et sa partie sur le "
    "libre-échange et la mobilité de la main-d'œuvre est entrée en vigueur le 1er "
    "janvier 2026. Les 53 exceptions fédérales à l'Accord de libre-échange canadien ont "
    "toutes disparu; 94 des 296 exceptions au total ont été retirées. Les quatorze "
    "gouvernements ont signé une entente de reconnaissance mutuelle sur la vente de "
    "biens en novembre 2025 — mais elle exclut les aliments, les boissons, l'alcool, le "
    "tabac, le cannabis, les plantes et les animaux vivants, ce qui fait un grand trou "
    "dans un pays qui cultive beaucoup."))

a.h2(T("Buy Canadian, honestly assessed",
       "Achetons canadien, évalué honnêtement"))
a.p(T(
    "The Buy Canadian policy took effect on 16 December 2025 for strategic purchases "
    "above 25 million dollars, and the threshold was lowered to 5 million on 15 June "
    "2026. Canadian suppliers get a 10 percent reduction applied to their financial "
    "proposal, or a quarter of the evaluation score for Canadian content, and steel, "
    "aluminium and wood must be made or processed in Canada.",
    "La politique Achetons canadien est entrée en vigueur le 16 décembre 2025 pour les "
    "achats stratégiques de plus de 25 millions de dollars, et le seuil a été abaissé à "
    "5 millions le 15 juin 2026. Les fournisseurs canadiens bénéficient d'une réduction "
    "de 10 pour cent appliquée à leur proposition financière, ou du quart de la note "
    "d'évaluation pour le contenu canadien, et l'acier, l'aluminium et le bois doivent "
    "être fabriqués ou transformés au Canada."))
a.p(T(
    "Its real reach is smaller than it sounds. Writing in Policy Options in June 2026, "
    "Noah Fry pointed out that the policy applied to 3.6 billion dollars of purchases "
    "and that the added cost was at most about 62 million dollars on 249 million of "
    "contracts, because Canada's own trade agreements forbid discriminating across most "
    "of the rest of government buying. It is a useful tool with a narrow handle.",
    "Sa portée réelle est plus modeste qu'il n'y paraît. Dans Options politiques en "
    "juin 2026, Noah Fry soulignait que la politique s'était appliquée à 3,6 milliards "
    "de dollars d'achats et que le coût supplémentaire atteignait au plus environ 62 "
    "millions de dollars sur 249 millions de contrats, parce que les propres accords "
    "commerciaux du Canada interdisent la discrimination dans la majeure partie du "
    "reste des achats publics. C'est un outil utile, mais au manche étroit."))

a.h2(T("Getting it to the ship", "Le faire monter à bord du navire"))
a.p(T(
    "This is the part of the diversification argument that is physical rather than "
    "political, and it is the strongest objection to the whole plan. Charles Lammam of "
    "the C.D. Howe Institute pointed out in July 2026 that the largest container ships "
    "Canada's ports can handle carry about 15,000 containers, while the newest vessels "
    "carry more than 20,000, so some Canada-bound cargo goes through American ports "
    "instead. Canada's "
    "world ranking for total ship capacity fell from sixth in 2016 to twenty-third in "
    "2023. Vancouver handles 42 percent of Canada's container traffic and ranks 375th "
    "out of 400 on the World Bank's port performance index; Halifax is the exception at "
    "29th. Water transport carries 54 percent of the value of what Canada exports.",
    "C'est la partie de l'argument sur la diversification qui est physique plutôt que "
    "politique, et c'est la plus forte objection à tout le plan. Charles Lammam, de "
    "l'Institut C.D. Howe, signalait en juillet 2026 que les plus grands "
    "porte-conteneurs que le Canada peut accueillir transportent environ 15 000 "
    "conteneurs alors que les navires les plus récents en portent plus de 20 000 : une "
    "partie du fret destiné au Canada passe donc par des ports américains. Le rang "
    "mondial du Canada pour la capacité totale des navires est passé du sixième en 2016 "
    "au vingt-troisième en 2023. Vancouver traite 42 pour cent du trafic conteneurisé "
    "canadien et se classe 375e sur 400 à l'indice de performance portuaire de la "
    "Banque mondiale; Halifax fait exception, au 29e rang. Le transport maritime porte "
    "54 pour cent de la valeur de ce que le Canada exporte."))
a.p(T(
    "The Fraser Institute made the same point from a different angle in June 2026: "
    "Canada's dependence on the American market fell modestly between 1999 and 2011 and "
    "then stayed flat all the way through 2024. The highways, the railways and the "
    "pipelines were built to run north to south. Changing that is a matter of concrete "
    "and steel, and it takes years.",
    "L'Institut Fraser a fait la même remarque sous un autre angle en juin 2026 : la "
    "dépendance du Canada au marché américain a modestement baissé entre 1999 et 2011, "
    "puis est restée stable jusqu'en 2024. Les autoroutes, les chemins de fer et les "
    "pipelines ont été construits pour aller du nord au sud. Changer cela est une "
    "affaire de béton et d'acier, et cela demande des années."))

a.h2(T("New deals, new pipes, new ports",
       "Nouvelles ententes, nouveaux tuyaux, nouveaux ports"))
a.p(T(
    "Canada signed a free trade agreement with Ecuador on 24 July 2026 and announced "
    "its first agreement with a Southeast Asian country, Indonesia, in September 2025. "
    "Talks with Mercosur and with the ten-nation Southeast Asian bloc are aiming at the "
    "end of 2026, and negotiations with India are at an early stage — the trade "
    "minister has said plainly that it is going to take some time. On 16 January 2026 "
    "Canada and China reached an arrangement that cut Chinese tariffs on canola seed "
    "from about 85 percent all in to roughly 15 percent, a market worth about 4 billion "
    "dollars, in exchange for Canada admitting 49,000 Chinese electric vehicles a year "
    "at a low rate, which is under 3 percent of the Canadian market.",
    "Le Canada a signé un accord de libre-échange avec l'Équateur le 24 juillet 2026 et "
    "annoncé sa première entente avec un pays d'Asie du Sud-Est, l'Indonésie, en "
    "septembre 2025. Les pourparlers avec le Mercosur et avec le bloc de dix pays "
    "d'Asie du Sud-Est visent la fin de 2026, et les négociations avec l'Inde n'en sont "
    "qu'à leurs débuts — le ministre du Commerce a dit franchement que cela prendrait "
    "du temps. Le 16 janvier 2026, le Canada et la Chine se sont entendus pour réduire "
    "les tarifs chinois sur la graine de canola d'environ 85 pour cent au total à quelque 15 "
    "pour cent, un marché d'environ 4 milliards de dollars, en échange de l'admission "
    "par le Canada de 49 000 véhicules électriques chinois par an à taux réduit, soit "
    "moins de 3 pour cent du marché canadien."))
a.p(T(
    "The physical projects are moving too. LNG Canada started up in June 2025 and "
    "shipped a million tonnes in April 2026, its first million-tonne month, with all of "
    "that month's cargoes going to Asia and more than half to South Korea. Trans "
    "Mountain moved 15.3 million barrels in 29 tankers in July 2026, the most since "
    "records began, with nearly three quarters going to the Asia-Pacific — and the "
    "Canada West Foundation calculates that it cut Canadian producers' reliance on the "
    "American market from 97 percent to 90 percent. Eighteen projects now sit with the "
    "federal Major Projects Office, from a Nunavut hydro project that is entirely "
    "Inuit-owned to container terminals in British Columbia and Quebec.",
    "Les projets physiques avancent aussi. LNG Canada a démarré en juin 2025 et a "
    "expédié un million de tonnes en avril 2026, son premier mois à un million de "
    "tonnes, toutes les cargaisons du mois partant vers l'Asie et plus de la moitié "
    "vers la Corée du Sud. Trans Mountain a acheminé 15,3 millions de barils dans 29 "
    "navires-citernes en juillet 2026, un sommet depuis le début du suivi, dont près "
    "des trois quarts vers l'Asie-Pacifique — et la Canada West Foundation calcule que "
    "cela a réduit la dépendance des producteurs canadiens au marché américain de 97 à "
    "90 pour cent. Dix-huit projets se trouvent maintenant au Bureau fédéral des grands "
    "projets, d'un projet hydroélectrique du Nunavut entièrement détenu par des Inuits "
    "à des terminaux à conteneurs en Colombie-Britannique et au Québec."))
a.p(T(
    "A West Coast oil pipeline of a million barrels a day was announced with Alberta on "
    "2 July 2026, paired with a carbon capture project. It is at the proposal stage: no "
    "cost and no construction timetable were given, and the job figures quoted with it "
    "are projections. It belongs in the plans column, not the results column.",
    "Un oléoduc vers la côte Ouest d'un million de barils par jour a été annoncé avec "
    "l'Alberta le 2 juillet 2026, jumelé à un projet de captage du carbone. Il en est "
    "au stade de la proposition : aucun coût ni calendrier de construction n'a été "
    "donné, et les chiffres d'emplois qui l'accompagnent sont des projections. Il "
    "appartient à la colonne des plans, non à celle des résultats."))

a.h2(T("What the economists actually expect",
       "Ce que les économistes attendent réellement"))
a.p(T(
    "The Bank of Canada's July 2026 forecast is 0.7 percent growth this year, rising to "
    "1.8 percent in 2027 and again in 2028. Its wording on exports is careful and worth "
    "quoting: exports remain on a lower path than before the tariffs were imposed. The "
    "Bank's Governor said export growth has resumed and is expected to keep "
    "strengthening, though along a lower path, helped partly by a weaker Canadian "
    "dollar, and that American trade policy continues to be a headwind.",
    "La prévision de juillet 2026 de la Banque du Canada est de 0,7 pour cent de "
    "croissance cette année, puis 1,8 pour cent en 2027 et de nouveau en 2028. Sa "
    "formulation sur les exportations est prudente et mérite d'être citée : les "
    "exportations demeurent sur une trajectoire plus basse qu'avant l'imposition des "
    "tarifs. Le gouverneur de la Banque a dit que la croissance des exportations a "
    "repris et devrait continuer de se renforcer, quoique sur une trajectoire plus "
    "basse, aidée en partie par un dollar canadien plus faible, et que la politique "
    "commerciale américaine reste un vent de face."))
a.p(T(
    "Budget 2025 set the target: double what Canada sells outside the United States "
    "over a decade, about 300 billion dollars more trade by 2035. That is a target, and "
    "we should be careful never to report it as an achievement. Glen Hodgson of the "
    "C.D. Howe Institute is the optimist about diversification in general — much more "
    "diversified Canadian trade is indeed possible, he wrote in April 2026, and active "
    "public policy can help overcome gravity — though he was writing about the "
    "direction, not endorsing that particular target. The Fraser Institute and Charles "
    "Lammam both say the target is out of reach on today's infrastructure. Nobody publishes a figure for what share of the American market "
    "can realistically be replaced, and by when. Anyone who gives you one is guessing.",
    "Le budget de 2025 a fixé la cible : doubler ce que le Canada vend hors des "
    "États-Unis en une décennie, soit environ 300 milliards de dollars de commerce en "
    "plus d'ici 2035. C'est une cible, et il faut se garder de la présenter comme une "
    "réalisation. Glen Hodgson, de l'Institut C.D. Howe, est l'optimiste au sujet de la "
    "diversification en général — un commerce beaucoup plus diversifié est bel et bien "
    "possible, écrivait-il en avril 2026, et une politique publique active peut aider à "
    "vaincre la gravité — même s'il parlait de la direction à prendre et non de cette "
    "cible précise. L'Institut Fraser et Charles Lammam estiment tous deux que la cible "
    "est hors de portée avec les infrastructures actuelles. Personne ne publie de chiffre sur la part du marché "
    "américain qui peut réalistement être remplacée, ni sur l'échéance. Quiconque vous "
    "en donne un devine."))

a.h2(T("If you run a small business, this is the practical list",
       "Si vous dirigez une petite entreprise, voici la liste pratique"))
a.ul([
    T("Check whether your goods qualify under CUSMA first. About 85 percent of "
      "Canadian exports do, and qualifying is the single biggest thing most exporters "
      "can control.",
      "Vérifiez d'abord si vos marchandises sont admissibles sous l'ACEUM. Environ 85 "
      "pour cent des exportations canadiennes le sont, et l'admissibilité est la chose "
      "la plus importante que la plupart des exportateurs peuvent contrôler."),
    T("The Trade Commissioner Service runs a support line on 1-833-760-1167 for "
      "tariff-impact advice and help finding buyers in other markets.",
      "Le Service des délégués commerciaux offre une ligne d'aide au 1-833-760-1167 "
      "pour des conseils sur les effets des tarifs et pour trouver des acheteurs sur "
      "d'autres marchés."),
    T("If you import from the United States and pay a surtax, look at the Canada "
      "Border Services Agency's Duties Relief and Duty Drawback programmes, and at "
      "case-by-case remission through the Department of Finance.",
      "Si vous importez des États-Unis et payez une surtaxe, examinez les programmes "
      "d'exonération des droits et de drawback de l'Agence des services frontaliers du "
      "Canada, ainsi que la remise au cas par cas par le ministère des Finances."),
    T("The Business Development Bank of Canada lends up to 100,000 dollars to small "
      "businesses, with specific financing for steel, aluminium and copper firms.",
      "La Banque de développement du Canada prête jusqu'à 100 000 dollars aux petites "
      "entreprises, avec du financement précis pour les entreprises de l'acier, de "
      "l'aluminium et du cuivre."),
    T("The Regional Tariff Response Initiative runs through the regional development "
      "agency in your province, and Alberta, Ontario, British Columbia and Quebec each "
      "run their own programme as well.",
      "L'Initiative régionale de réponse aux tarifs passe par l'agence de développement "
      "régional de votre province, et l'Alberta, l'Ontario, la Colombie-Britannique et "
      "le Québec ont aussi chacun leur propre programme."),
    T("The Canada Tariff Finder and the Rules of Origin Facilitator are both free and "
      "will answer most of the questions people pay consultants for.",
      "Le Localisateur de tarifs du Canada et le Facilitateur des règles d'origine sont "
      "gratuits et répondent à la plupart des questions pour lesquelles les gens paient "
      "des consultants."),
])

a.h2(T("What to take away", "Ce qu'il faut retenir"))
a.p(T(
    "Canada has moved faster in eighteen months than at any point in recent memory: "
    "internal barriers coming down, a shelf of new agreements, gas leaving the west "
    "coast for the first time, and a support system the government estimates kept about "
    "20,000 people in their jobs. It has also not replaced the American market, and on "
    "the honest measure it has replaced about half of what it lost. Both of those "
    "sentences are true at the same time, and a country that can hold both in mind at "
    "once is better placed than one that can only hold one.",
    "Le Canada a avancé plus vite en dix-huit mois qu'à tout autre moment récent : des "
    "barrières intérieures qui tombent, une série de nouvelles ententes, du gaz qui "
    "quitte la côte Ouest pour la première fois, et un filet de soutien qui, selon les "
    "estimations du gouvernement, a gardé environ 20 000 personnes à l'emploi. Il n'a pas non plus "
    "remplacé le marché américain, et selon la mesure honnête il a remplacé environ la "
    "moitié de ce qu'il a perdu. Ces deux phrases sont vraies en même temps, et un pays "
    "capable de tenir les deux à l'esprit est mieux placé que celui qui n'en tient "
    "qu'une."))

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("us-tariffs-and-canada-explained.html",
         T("What the tariffs did to Canada, sector by sector",
           "Ce que les tarifs ont fait au Canada, secteur par secteur")),
    link("did-us-tariffs-on-canada-work.html",
         T("When a tariff goes on, who actually gains?",
           "Quand un tarif est imposé, qui y gagne vraiment?")),
    link("canada-usa-trade-history.html",
         T("Canada and the United States: 170 years of trade, fights and deals",
           "Le Canada et les États-Unis : 170 ans de commerce, de disputes et d'ententes")),
])

a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://international.canada.ca/en/global-affairs/corporate/reports/chief-economist/quarterly/spring-2026",
             T("Global Affairs Canada — Quarterly Economic and Trade Report, Spring 2026",
               "Affaires mondiales Canada — Rapport économique et commercial trimestriel, printemps 2026")),
    out_link("https://international.canada.ca/en/global-affairs/corporate/reports/chief-economist/state-trade/2026",
             T("Global Affairs Canada — State of Trade 2026",
               "Affaires mondiales Canada — Le point sur le commerce 2026")),
    out_link("https://budget.canada.ca/2025/report-rapport/chap2-en.html",
             T("Budget 2025 — Shifting from reliance to resilience",
               "Budget de 2025 — Passer de la dépendance à la résilience")),
    out_link("https://www.canada.ca/en/employment-social-development/news/2026/03/government-of-canada-extending-employment-insurance-temporary-measures-to-ensure-critical-income-support-continues-for-workers-impacted-by-tariffs.html",
             T("Employment and Social Development Canada — Extending Employment Insurance measures",
               "Emploi et Développement social Canada — Prolongation des mesures d'assurance-emploi")),
    out_link("https://www.statcan.gc.ca/en/blog/cs/trade_costs",
             T("Statistics Canada — The effect of provincial borders on trade",
               "Statistique Canada — L'effet des frontières provinciales sur le commerce")),
    out_link("https://www.canada.ca/en/intergovernmental-affairs/services/internal-trade/federal-investments-internal-trade.html",
             T("Intergovernmental Affairs Canada — Internal trade",
               "Affaires intergouvernementales Canada — Le commerce intérieur")),
    out_link("https://www.policyalternatives.ca/news-research/those-big-gdp-numbers-about-interprovincial-trade-barriers-are-wrong/",
             T("Canadian Centre for Policy Alternatives — Those big GDP numbers are wrong",
               "Centre canadien de politiques alternatives — Ces grands chiffres de PIB sont erronés")),
    out_link("https://cdhowe.org/publication/trade-diversification-ambitions-face-a-container-port-reality/",
             T("C.D. Howe Institute — Trade diversification ambitions face a container port reality",
               "Institut C.D. Howe — Les ambitions de diversification commerciale se heurtent à la réalité portuaire")),
    out_link("https://www.fraserinstitute.org/studies/opportunities-diversify-canadas-trade",
             T("Fraser Institute — Opportunities to diversify Canada's trade",
               "Institut Fraser — Occasions de diversifier le commerce du Canada")),
    out_link("https://www.bankofcanada.ca/publications/mpr/mpr-2026-07-15/canadian-outlook/",
             T("Bank of Canada — Monetary Policy Report, July 2026",
               "Banque du Canada — Rapport sur la politique monétaire, juillet 2026")),
    out_link("https://www.tradecommissioner.gc.ca/en/market-industry-info/search-country-region/country/canada-united-states-export/us-tariffs/supporting-exporters-through-tariff-challenges.html",
             T("Trade Commissioner Service — Supporting exporters through tariff challenges",
               "Service des délégués commerciaux — Soutenir les exportateurs face aux tarifs")),
])

a.disclaimer(T(
    "This article is for general information and study. This site is unofficial and "
    "not affiliated with the Government of Canada. It is not business, legal or "
    "financial advice; if a tariff affects your company, speak to the Trade "
    "Commissioner Service or a customs broker. Every source we used is listed above "
    "and on our sources page.",
    "Cet article est fourni à titre d'information générale et d'étude. Ce site est non "
    "officiel et n'a aucun lien avec le gouvernement du Canada. Il ne constitue pas un "
    "conseil commercial, juridique ou financier; si un tarif touche votre entreprise, "
    "parlez au Service des délégués commerciaux ou à un courtier en douane. Toutes nos "
    "sources sont énumérées ci-dessus et sur notre page des sources."))

if __name__ == "__main__":
    a.build()
    flush_pairs()
