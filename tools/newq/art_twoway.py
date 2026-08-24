#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article 5 — what the two countries actually sell each other, both directions.

Sources: research/counter-tariff-revenue-and-import-composition-20260823.md,
research/two-way-dependence-canada-usa-20260823.md and
research/tariff-refunds-who-gets-the-money-20260823.md in the private project
notes.

Two things were deliberately left off this page because they could not be
verified. There is no published measurement of how much of China's exports to
the United States is made by or for American companies; the US International
Trade Commission says the foreign-invested share is highest for the American
market but has never printed a number, so the page uses the San Francisco
Federal Reserve's 2010 study and dates it plainly instead. And the OECD's
trade-in-value-added country notes, which would settle the imported-content
question, are blocked to automated retrieval, so no figure from them appears.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="what-canada-and-the-usa-sell-each-other.html",
    section="Trade",
    title=T("What Canada Sells America, and What America Sells Canada",
            "Ce que le Canada vend à l'Amérique, et ce que l'Amérique vend au Canada"),
    desc=T("Half of what the United States buys from Canada is raw and processed "
           "materials. Five percent is consumer goods. From China it is almost exactly "
           "the other way round. Both directions of the relationship, sector by sector, "
           "in dollars and percentages.",
           "La moitié de ce que les États-Unis achètent au Canada, ce sont des matières "
           "premières et transformées. Cinq pour cent sont des biens de consommation. "
           "Avec la Chine, c'est presque exactement l'inverse. Les deux sens de la "
           "relation, secteur par secteur, en dollars et en pourcentages."),
    h1=T("\U0001F69B What the two countries actually sell each other",
         "\U0001F69B Ce que les deux pays se vendent réellement"),
    hero=T("Canada and China both sell a great deal to the United States, and the two "
           "trades are shaped very differently. Half of the Canadian trade is material "
           "American industry runs on. Half of the Chinese trade is what Americans put in "
           "a shopping cart. That difference changes what a tariff does in each case.",
           "Le Canada et la Chine vendent tous deux beaucoup aux États-Unis, et les deux "
           "échanges n'ont pas du tout la même forme. La moitié du commerce canadien, "
           "c'est la matière avec laquelle l'industrie américaine fonctionne. La moitié du "
           "commerce chinois, c'est ce que les Américains mettent dans un panier "
           "d'épicerie. Cette différence change ce qu'un tarif produit dans chaque cas."),
    checked=T("Last checked 24 August 2026 — every figure carries the year its source "
              "published it for",
              "Dernière vérification le 24 août 2026 — chaque chiffre porte l'année pour "
              "laquelle sa source l'a publié"),
)

a.callout(T(
    "<strong>A note on the dollars.</strong> Figures describing what the United States "
    "buys are in American dollars, because that is how the American agencies publish "
    "them. Figures describing Canadian exports and imports are in Canadian dollars. "
    "Nothing on this page has been converted, and the two are never added together. That is "
    "why the same trade flow appears twice at different sizes — 389 billion American "
    "dollars of Canadian goods bought, 564.6 billion Canadian dollars of goods sold. The "
    "gap is the exchange rate and the different counting rules of the two statistical "
    "systems, not a discrepancy.",
    "<strong>Une note sur les dollars.</strong> Les chiffres décrivant ce que les "
    "États-Unis achètent sont en dollars américains, parce que c'est ainsi que les "
    "organismes américains les publient. Ceux décrivant les exportations et importations "
    "canadiennes sont en dollars canadiens. Rien sur cette page n'a été converti, et les "
    "deux ne sont jamais additionnés. C'est pourquoi le même flux commercial apparaît deux "
    "fois avec des tailles différentes — 389 milliards de dollars américains de biens "
    "canadiens achetés, 564,6 milliards de dollars canadiens de biens vendus. L'écart tient "
    "au taux de change et aux règles de comptage différentes des deux systèmes "
    "statistiques, non à une contradiction."))

# ------------------------------------------------------------------ 1
a.h2(T("The short answer", "La réponse courte"))
a.p(T(
    "About half of what the United States buys from Canada is the raw and processed "
    "material its factories, refineries, farms and power grids consume in order to make "
    "something else. About half of what it buys from China is finished consumer goods. In "
    "2025 consumer goods were 4.8 percent of what the United States bought from Canada and "
    "46.1 percent of what it bought from China. Industrial supplies and materials ran the "
    "other way: 50.3 percent from Canada, 10.6 percent from China.",
    "Environ la moitié de ce que les États-Unis achètent au Canada, c'est la matière brute "
    "et transformée que leurs usines, raffineries, fermes et réseaux électriques "
    "consomment pour fabriquer autre chose. Environ la moitié de ce qu'ils achètent à la "
    "Chine, ce sont des biens de consommation finis. En 2025, les biens de consommation "
    "représentaient 4,8 pour cent de ce que les États-Unis achetaient au Canada et 46,1 "
    "pour cent de ce qu'ils achetaient à la Chine. Les fournitures et matières "
    "industrielles allaient dans l'autre sens : 50,3 pour cent pour le Canada, 10,6 pour "
    "cent pour la Chine."))
a.p(T(
    "In the other direction, Canada is the more exposed of the two partners. Statistics "
    "Canada calculates that in 2024, 15.9 percent of Canada's whole economy was the "
    "production of exports destined for the United States, accounting for more than 2.5 "
    "million jobs. No American agency publishes the same calculation in reverse, so there "
    "is no exact number to set beside it — but in 2024 two-way trade was about two thirds "
    "of Canada's economy and about a quarter of the American one, and that ratio is the "
    "shape of the thing.",
    "Dans l'autre sens, le Canada est le plus exposé des deux partenaires. Statistique "
    "Canada calcule qu'en 2024, 15,9 pour cent de l'économie canadienne entière était la "
    "production d'exportations destinées aux États-Unis, ce qui représentait plus de 2,5 "
    "millions d'emplois. Aucun organisme américain ne publie le calcul inverse, il n'y a "
    "donc aucun chiffre exact à placer à côté — mais en 2024 le commerce bilatéral "
    "représentait environ les deux tiers de l'économie canadienne et environ le quart de "
    "l'économie américaine, et ce rapport donne la forme de la chose."))

# ------------------------------------------------------------------ 2
a.h2(T("What the United States buys, and from whom",
       "Ce que les États-Unis achètent, et à qui"))
a.p(T(
    "American trade statistics sort imports into a handful of end-use categories — what "
    "the goods are for, rather than what they are made of. Setting the two countries side "
    "by side in those categories is the clearest single picture of the difference.",
    "Les statistiques commerciales américaines classent les importations en quelques "
    "catégories d'utilisation finale — à quoi les biens servent, plutôt que de quoi ils "
    "sont faits. Placer les deux pays côte à côte dans ces catégories donne l'image la "
    "plus claire de la différence."))
a.fig(bar_chart(
    T("What the United States buys from Canada, 2025 — share of goods imports, percent",
      "Ce que les États-Unis achètent au Canada, 2025 — part des importations de biens, "
      "en pourcentage"),
    [(T("Industrial supplies and materials", "Fournitures et matières industrielles"), 50.3),
     (T("Vehicles, parts and engines", "Véhicules, pièces et moteurs"), 13.6),
     (T("Capital goods", "Biens d'équipement"), 13.5),
     (T("Food, feeds and beverages", "Aliments, fourrages et boissons"), 10.4),
     (T("Other merchandise", "Autres marchandises"), 5.0),
     (T("Consumer goods", "Biens de consommation"), 4.8),
     (T("Non-monetary gold", "Or non monétaire"), 2.4)],
    unit="%"))
a.fig(bar_chart(
    T("What the United States buys from China, 2025 — share of goods imports, percent",
      "Ce que les États-Unis achètent à la Chine, 2025 — part des importations de biens, "
      "en pourcentage"),
    [(T("Consumer goods", "Biens de consommation"), 46.1),
     (T("Capital goods", "Biens d'équipement"), 32.5),
     (T("Industrial supplies and materials", "Fournitures et matières industrielles"), 10.6),
     (T("Vehicles, parts and engines", "Véhicules, pièces et moteurs"), 5.2),
     (T("Other merchandise", "Autres marchandises"), 4.7),
     (T("Food, feeds and beverages", "Aliments, fourrages et boissons"), 1.3)],
    unit="%"),
    caption=T("The six categories sum to 100.4 percent because of rounding in the source "
              "data.",
              "Les six catégories totalisent 100,4 pour cent en raison des arrondis dans "
              "les données sources."))
a.p(T(
    "In dollars, on the same basis as the two charts: the United States bought 389 billion "
    "of goods from Canada in 2025 and 308 billion from China. Of the Canadian total, 195.9 "
    "billion was industrial supplies and materials and only 18.8 billion was consumer "
    "goods. Of the Chinese total, 141.9 billion was consumer goods and 32.7 billion was "
    "industrial supplies. About 111 billion of what the United States bought from Canada "
    "was energy — roughly 57 percent of the industrial-supplies category, though that "
    "comparison crosses two slightly different statistical bases and should be treated as "
    "approximate.",
    "En dollars, sur la même base que les deux graphiques : les États-Unis ont acheté pour "
    "389 milliards de biens au Canada en 2025 et pour 308 milliards à la Chine. Du total "
    "canadien, 195,9 milliards étaient des fournitures et matières industrielles et "
    "seulement 18,8 milliards des biens de consommation. Du total chinois, 141,9 milliards "
    "étaient des biens de consommation et 32,7 milliards des fournitures industrielles. "
    "Environ 111 milliards de ce que les États-Unis ont acheté au Canada était de "
    "l'énergie — soit à peu près 57 pour cent de la catégorie des fournitures "
    "industrielles, une comparaison qui croise toutefois deux bases statistiques "
    "légèrement différentes et qu'il faut tenir pour approximative."))
a.callout(T(
    "<strong>One qualification, because the simple version overshoots.</strong> Capital "
    "goods — machinery, computers, semiconductors, industrial equipment — are 32.5 "
    "percent of what the United States buys from China, and those are inputs and "
    "equipment for American producers too, not shopping-mall goods. Adding them to "
    "industrial supplies puts about 43 percent of imports from China in the "
    "inputs-and-equipment column. So the accurate sentence is not that Canada sells "
    "inputs and China sells consumer goods. It is that about half of what the United "
    "States buys from Canada is raw and processed materials, and about half of what it "
    "buys from China is finished consumer goods.",
    "<strong>Une nuance, parce que la version simple va trop loin.</strong> Les biens "
    "d'équipement — machinerie, ordinateurs, semi-conducteurs, équipement industriel — "
    "représentent 32,5 pour cent de ce que les États-Unis achètent à la Chine, et ce sont "
    "eux aussi des intrants et de l'équipement pour les producteurs américains, pas des "
    "articles de centre commercial. En les ajoutant aux fournitures industrielles, environ "
    "43 pour cent des importations en provenance de Chine se retrouvent dans la colonne "
    "des intrants et de l'équipement. La phrase exacte n'est donc pas que le Canada vend "
    "des intrants et la Chine des biens de consommation. C'est qu'environ la moitié de ce "
    "que les États-Unis achètent au Canada est de la matière brute et transformée, et "
    "qu'environ la moitié de ce qu'ils achètent à la Chine est du produit fini de "
    "consommation."))
a.p(T(
    "One claim that comes up often is that much of what China ships to the United States "
    "is made in China by or for American companies. It may well be true, but no agency "
    "publishes a number for it. The US International Trade Commission has written that "
    "the share of Chinese trade conducted by foreign-invested firms is highest for exports "
    "to the United States — and has never put a figure on it. What has been measured, by "
    "the Federal Reserve Bank of San Francisco using 2010 data, is that of every dollar an "
    "American spends on an item labelled made in China, about 55 cents goes to Americans "
    "for shipping, wholesaling and selling it. That study is fifteen years old, and should "
    "be read with its date attached.",
    "Une affirmation revient souvent : une bonne part de ce que la Chine expédie aux "
    "États-Unis serait fabriquée en Chine par ou pour des entreprises américaines. C'est "
    "peut-être vrai, mais aucun organisme n'en publie le chiffre. La Commission du "
    "commerce international des États-Unis a écrit que la part du commerce chinois réalisée "
    "par des entreprises à capitaux étrangers est la plus élevée pour les exportations vers "
    "les États-Unis — sans jamais avancer de chiffre. Ce qui a été mesuré, par la Banque "
    "fédérale de réserve de San Francisco à partir de données de 2010, c'est que sur chaque "
    "dollar qu'un Américain dépense pour un article étiqueté fabriqué en Chine, environ 55 "
    "cents vont à des Américains pour le transport, la distribution et la vente. Cette "
    "étude a quinze ans et doit être lue avec sa date."))

# ------------------------------------------------------------------ 3
a.h2(T("The things that are hard to buy anywhere else",
       "Ce qui est difficile à acheter ailleurs"))
a.p(T(
    "A share of imports is one measure of importance. A more useful one is whether there "
    "is anywhere else to go. On several Canadian products there is not, at least not "
    "within a few years.",
    "Une part des importations est une mesure de l'importance. Une mesure plus utile est "
    "de savoir s'il existe une autre source. Pour plusieurs produits canadiens, il n'y en "
    "a pas, du moins pas avant plusieurs années."))
a.table(
    [T("Product", "Produit"),
     T("Canada's place in American supply", "La place du Canada dans l'approvisionnement américain"),
     T("How quickly it could be replaced", "À quelle vitesse cela pourrait être remplacé")],
    [[T("Potash", "Potasse"),
      T("79 percent of American imports on the 2021–24 average, or 88 percent on the trade "
        "commission's 2023–24 figure; the United States is 92 percent import-reliant",
        "79 pour cent des importations américaines sur la moyenne 2021-2024, ou 88 pour "
        "cent selon le chiffre 2023-2024 de la commission du commerce ; les États-Unis "
        "dépendent des importations à 92 pour cent"),
      T("The only other large sources are Russia and Belarus, both sanctioned. The one "
        "new American mine in development would take 42 months to build and cover about "
        "11 percent of consumption.",
        "Les seules autres grandes sources sont la Russie et le Bélarus, tous deux sous "
        "sanctions. La seule nouvelle mine américaine en développement demanderait 42 mois "
        "de construction et couvrirait environ 11 pour cent de la consommation.")],
     [T("Heavy crude oil", "Pétrole brut lourd"),
      T("3.9 million barrels a day in 2025; 73 percent of the crude run through Midwest "
        "refineries on 2024 data",
        "3,9 millions de barils par jour en 2025 ; 73 pour cent du brut traité par les "
        "raffineries du Midwest selon les données de 2024"),
      T("Those refineries hold cokers and hydrotreaters built for heavy sour crude. "
        "Mexican heavy exports have fallen to about 400,000 barrels a day and Venezuelan "
        "to about 100,000.",
        "Ces raffineries possèdent des cokeurs et des hydrotraiteurs conçus pour le brut "
        "lourd sulfureux. Les exportations lourdes mexicaines sont tombées à environ "
        "400 000 barils par jour et les vénézuéliennes à environ 100 000.")],
     [T("Aluminium", "Aluminium"),
      T("56 percent of American imports on the 2021–24 average; the United States is 60 "
        "percent import-reliant on the 2025 estimate",
        "56 pour cent des importations américaines sur la moyenne 2021-2024 ; les "
        "États-Unis dépendent des importations à 60 pour cent selon l'estimation de 2025"),
      T("Six primary smelters remain, from 33 in 1980. A smelter needs about 14,800 "
        "kilowatt-hours per tonne and long-term power near 40 dollars a megawatt-hour. "
        "New capacity is spoken of as end-of-decade.",
        "Il reste six fonderies primaires, contre 33 en 1980. Une fonderie exige environ "
        "14 800 kilowattheures par tonne et de l'électricité à long terme près de 40 "
        "dollars le mégawattheure. On parle de nouvelle capacité vers la fin de la "
        "décennie.")],
     [T("Uranium", "Uranium"),
      T("15.2 million pounds bought by American civilian reactors in 2025 — the largest "
        "single source, and roughly a third of everything they purchased",
        "15,2 millions de livres achetées par les réacteurs civils américains en 2025 — la "
        "première source, et environ le tiers de tous leurs achats"),

      T("American sources supplied under eight percent of what those reactors bought in "
        "2025 — Canada supplied more than four times as much. Domestic output is projected "
        "to rise six or seven times by 2030, which would still leave the country importing "
        "most of its fuel.",
        "Les sources américaines ont fourni moins de huit pour cent de ce que ces réacteurs "
        "ont acheté en 2025 — le Canada en a fourni plus de quatre fois plus. La production "
        "intérieure devrait être multipliée par six ou sept d'ici 2030, ce qui laisserait "
        "le pays importer la majeure partie de son combustible.")],
     [T("Softwood lumber", "Bois d'œuvre résineux"),
      T("12 billion board feet in 2024 — about 24 percent of American consumption",
        "12 milliards de pieds-planche en 2024 — environ 24 pour cent de la consommation "
        "américaine"),
      T("The timber exists on American federal land, but federal harvests average 1.4 "
        "billion board feet a year against the roughly 8 billion that would be needed — a "
        "450 percent increase, plus about 12,500 more forestry workers.",
        "Le bois existe sur les terres fédérales américaines, mais les récoltes fédérales "
        "moyennes sont de 1,4 milliard de pieds-planche par an contre les quelque 8 "
        "milliards nécessaires — une hausse de 450 pour cent, plus environ 12 500 "
        "travailleurs forestiers de plus.")],
     [T("Electricity", "Électricité"),
      T("Under 2 percent of American generation nationally — but, on 2023 data, 64 percent "
        "of Maine's supply and 13 percent of Minnesota's",
        "Moins de 2 pour cent de la production américaine à l'échelle nationale — mais, "
        "selon les données de 2023, 64 pour cent de l'approvisionnement du Maine et 13 pour "
        "cent de celui du Minnesota"),
      T("Replaceable in aggregate, not regionally. A new interconnection takes years: the "
        "Champlain Hudson line into New York City took three years to build and reached "
        "commercial operation in May 2026.",
        "Remplaçable dans l'ensemble, pas région par région. Une nouvelle interconnexion "
        "prend des années : la ligne Champlain Hudson vers New York a demandé trois ans de "
        "construction et est entrée en service commercial en mai 2026.")]],
    label=T("Canadian products and how easily they could be replaced — scroll sideways to "
            "see all of it",
            "Produits canadiens et facilité de remplacement — faites défiler latéralement "
            "pour tout voir"))
a.p(T(
    "Newsprint belongs on that list but with a weaker source. The Columbia Journalism "
    "Review reported in March 2025 that Canada supplies about 80 percent of the newsprint "
    "used by American newspapers; no statistical agency publishes an equivalent figure. "
    "What is firmly measured is that nearly 90 percent of North American newsprint "
    "capacity has closed since 1997, and an industry association reported in 2018 that "
    "demand had already fallen 75 percent since 2000. That is a shrinking industry on both "
    "sides of the border, which is a different situation from the ones in the table.",
    "Le papier journal appartient à cette liste, mais avec une source plus faible. La "
    "Columbia Journalism Review a rapporté en mars 2025 que le Canada fournit environ 80 "
    "pour cent du papier journal utilisé par les quotidiens américains ; aucun organisme "
    "statistique ne publie de chiffre équivalent. Ce qui est solidement mesuré, c'est que "
    "près de 90 pour cent de la capacité nord-américaine de papier journal a fermé depuis "
    "1997, et une association sectorielle rapportait en 2018 que la demande avait déjà "
    "chuté de 75 pour cent depuis 2000. C'est une industrie en déclin des deux côtés de la "
    "frontière, ce qui est une situation différente de celles du tableau."))

# ------------------------------------------------------------------ 4
a.h2(T("Now the other direction", "Maintenant l'autre sens"))
a.p(T(
    "Canadian figures from here on, in Canadian dollars. In 2025 Canada sold 564.6 billion "
    "of merchandise to the United States out of 779.0 billion sold to the whole world — "
    "72.5 percent on the customs basis, 71.7 percent on the balance-of-payments basis. "
    "Both numbers are official and they measure slightly different things; that is normal "
    "and worth knowing when two sources appear to disagree.",
    "Chiffres canadiens à partir d'ici, en dollars canadiens. En 2025, le Canada a vendu "
    "564,6 milliards de marchandises aux États-Unis sur 779,0 milliards vendus au monde "
    "entier — 72,5 pour cent sur la base douanière, 71,7 pour cent sur la base de la "
    "balance des paiements. Les deux chiffres sont officiels et mesurent des choses "
    "légèrement différentes ; c'est normal et utile à savoir quand deux sources semblent "
    "se contredire."))
a.p(T(
    "Energy is the biggest block of it. Canadian energy exports to the United States were "
    "157.5 billion in 2025, which the energy regulator puts at 20.2 percent of everything "
    "Canada sells anywhere. And almost none of it has another buyer.",
    "L'énergie en est le plus gros bloc. Les exportations énergétiques canadiennes vers "
    "les États-Unis se sont élevées à 157,5 milliards en 2025, ce que la Régie de "
    "l'énergie chiffre à 20,2 pour cent de tout ce que le Canada vend où que ce soit. Et "
    "presque rien de cela n'a un autre acheteur."))
a.fig(bar_chart(
    T("American share of Canadian energy exports, 2025 — percent",
      "Part américaine des exportations énergétiques canadiennes, 2025 — en pourcentage"),
    [(T("Electricity", "Électricité"), 100),
     (T("Crude oil", "Pétrole brut"), 90.1),
     (T("Refined petroleum products", "Produits pétroliers raffinés"), 84.3)],
    unit="%", colours=["teal", "blue", "purple"]))
a.p(T(
    "Electricity is at 100 percent because Canada has no other electricity trading "
    "partner — there is nowhere else a wire goes. Natural gas is not on the chart because "
    "the regulator describes the American share as nearly all of 8.6 billion cubic feet a "
    "day rather than giving a percentage. Crude oil alone was 126.1 billion dollars.",
    "L'électricité est à 100 pour cent parce que le Canada n'a aucun autre partenaire "
    "commercial en électricité — il n'y a nulle part ailleurs où un fil se rende. Le gaz "
    "naturel ne figure pas au graphique parce que le régulateur décrit la part américaine "
    "comme la quasi-totalité de 8,6 milliards de pieds cubes par jour plutôt que d'en "
    "donner un pourcentage. Le pétrole brut seul valait 126,1 milliards de dollars."))
a.p(T(
    "For manufacturing, Statistics Canada publishes a value-added measure, which strips "
    "out the imported content inside a Canadian export and counts only the part actually "
    "made here. It is a model, not a headcount, and it is the right number to use — a "
    "gross-exports figure double-counts American parts that crossed the border twice.",
    "Pour la fabrication, Statistique Canada publie une mesure en valeur ajoutée, qui "
    "retranche le contenu importé à l'intérieur d'une exportation canadienne et ne compte "
    "que la part réellement produite ici. C'est un modèle, pas un dénombrement, et c'est "
    "le bon chiffre à utiliser — un chiffre d'exportations brutes compte deux fois les "
    "pièces américaines qui ont traversé la frontière deux fois."))
a.table(
    [T("Sector, 2024", "Secteur, 2024"),
     T("Share of the sector's value added that serves American demand",
       "Part de la valeur ajoutée du secteur qui sert la demande américaine"),
     T("Jobs", "Emplois")],
    [[T("Aluminium production", "Production d'aluminium"), "77.6%", T("about 12,000", "environ 12 000")],
     [T("Motor vehicle manufacturing", "Fabrication de véhicules automobiles"), "76.4%",
      T("about 27,000", "environ 27 000")],
     [T("Iron and steel mills", "Aciéries et usines sidérurgiques"), "67.0%",
      T("about 9,800", "environ 9 800")],
     [T("Manufacturing overall", "Ensemble de la fabrication"), "42.4%",
      T("about 694,000", "environ 694 000")],
     [T("The whole Canadian economy", "L'ensemble de l'économie canadienne"),
      T("15.9% of GDP", "15,9 % du PIB"),
      T("more than 2,500,000", "plus de 2 500 000")]],
    label=T("Canadian value added tied to American demand, 2024 — scroll sideways to see "
            "all of it",
            "Valeur ajoutée canadienne liée à la demande américaine, 2024 — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "Outside manufacturing, agriculture and seafood sent 61.7 percent of exports to the "
    "United States in 2024, worth 61.9 billion. Minerals and metals sent 46 percent in "
    "2025, worth 76.4 billion. Steel is the sector where the arithmetic runs least in "
    "Canada's favour: two thirds of the industry's value added serves American demand, "
    "while Canadian steel works out to only about three percent of what the United States "
    "consumes. "
    "Services are the exception that is rarely mentioned: just over half of Canadian "
    "services exports go to the United States, and Export Development Canada reports they "
    "grew 6 percent in 2025 while goods exports fell.",
    "Hors fabrication, l'agriculture et les produits de la mer ont dirigé 61,7 pour cent "
    "de leurs exportations vers les États-Unis en 2024, pour 61,9 milliards. Les minéraux "
    "et métaux, 46 pour cent en 2025, pour 76,4 milliards. L'acier est le secteur où "
    "l'arithmétique joue le moins en faveur du Canada : les deux tiers de la valeur ajoutée "
    "de l'industrie servent la demande américaine, alors que l'acier canadien ne représente, "
    "calcul fait, qu'environ trois pour cent de ce que consomment les États-Unis.Les "
    "services sont l'exception rarement mentionnée : un peu plus de la moitié des "
    "exportations canadiennes de services vont aux États-Unis, et Exportation et "
    "développement Canada rapporte qu'elles ont augmenté de 6 pour cent en 2025 pendant que "
    "les exportations de biens reculaient."))

# ------------------------------------------------------------------ 5
a.h2(T("What Canada buys from the United States",
       "Ce que le Canada achète aux États-Unis"))
a.p(T(
    "This is the half Canadians see least, and it is large. It is also the place where "
    "two official numbers differ by twelve percentage points, so it is worth taking a "
    "moment over.",
    "C'est la moitié que les Canadiens voient le moins, et elle est importante. C'est "
    "aussi l'endroit où deux chiffres officiels diffèrent de douze points de pourcentage, "
    "ce qui mérite qu'on s'y arrête."))
a.p(T(
    "Statistics Canada counts imports two ways. By country of origin — where the goods "
    "were grown, mined or made — the United States supplied 46.2 percent of Canada's "
    "imports in 2025, the lowest share on record in data going back to 1946. By balance of "
    "payments, which captures goods that merely reached Canada through American ports and "
    "warehouses, the share is 58.8 percent. Neither is wrong. They answer different "
    "questions, and the gap between them is foreign-made goods arriving by way of the "
    "United States.",
    "Statistique Canada compte les importations de deux façons. Par pays d'origine — où "
    "les biens ont été cultivés, extraits ou fabriqués — les États-Unis ont fourni 46,2 "
    "pour cent des importations canadiennes en 2025, la part la plus faible jamais "
    "enregistrée dans des données remontant à 1946. Par la balance des paiements, qui "
    "englobe les biens qui n'ont fait que transiter par des ports et entrepôts américains, "
    "la part est de 58,8 pour cent. Aucune n'est fausse. Elles répondent à des questions "
    "différentes, et l'écart entre elles, ce sont des biens de fabrication étrangère "
    "arrivés via les États-Unis."))
a.p(T(
    "Underneath the percentages, three facts are worth having.",
    "Sous les pourcentages, trois faits méritent d'être retenus."))
a.ul([
    T("<strong>Canada runs an automotive trade deficit with the United States.</strong> "
      "Two-way automotive trade was 152 billion dollars in 2024 — 75 billion of Canadian "
      "exports against 77 billion of imports. Canada bought nearly 30 billion dollars of "
      "American auto parts in 2024 alone.",
      "<strong>Le Canada affiche un déficit commercial automobile avec les États-Unis.</strong> "
      "Le commerce automobile bilatéral s'élevait à 152 milliards de dollars en 2024 — 75 "
      "milliards d'exportations canadiennes contre 77 milliards d'importations. Le Canada a "
      "acheté près de 30 milliards de dollars de pièces automobiles américaines pour la "
      "seule année 2024."),
    T("<strong>Imports from the United States were 15.4 percent of every input Canadian "
      "industry used in 2022</strong>, on Statistics Canada's input-output model — not "
      "just what Canadians buy at the till, but the parts, chemicals, machinery and "
      "materials that go into Canadian production.",
      "<strong>Les importations en provenance des États-Unis représentaient 15,4 pour cent "
      "de chaque intrant utilisé par l'industrie canadienne en 2022</strong>, selon le "
      "modèle entrées-sorties de Statistique Canada — pas seulement ce que les Canadiens "
      "achètent en magasin, mais les pièces, produits chimiques, machines et matériaux qui "
      "entrent dans la production canadienne."),
    T("<strong>A Canadian-assembled vehicle is about half American by value</strong>, on "
      "the federal industry department's own estimate. Which is why a tariff on Canadian "
      "vehicles falls partly on American-made content.",
      "<strong>Un véhicule assemblé au Canada est américain à environ la moitié de sa "
      "valeur</strong>, selon l'estimation du ministère fédéral de l'industrie lui-même. "
      "C'est pourquoi un tarif sur les véhicules canadiens frappe en partie du contenu "
      "fabriqué aux États-Unis."),
])
a.p(T(
    "On the country-of-origin basis, Canada's imports from the United States fell 4.2 "
    "percent in 2025, or 15.8 billion dollars. The largest declines were motor vehicles and parts, down 5.2 billion, and "
    "metal and non-metallic mineral products, down 3.2 billion. Canada's total merchandise "
    "imports from everywhere rose 2.8 percent — but prices accounted for the entire "
    "increase, and volumes were flat for a second straight year.",
    "Sur la base du pays d'origine, les importations canadiennes en provenance des "
    "États-Unis ont reculé de 4,2 pour cent en 2025, soit 15,8 milliards de dollars. Les "
    "baisses les plus fortes touchaient les "
    "véhicules automobiles et pièces, en baisse de 5,2 milliards, et les produits "
    "métalliques et minéraux non métalliques, en baisse de 3,2 milliards. Les importations "
    "totales de marchandises du Canada, toutes provenances, ont augmenté de 2,8 pour cent "
    "— mais les prix expliquent la totalité de la hausse, et les volumes sont restés plats "
    "pour une deuxième année de suite."))

# ------------------------------------------------------------------ 6
a.h2(T("What this adds up to", "Ce que cela donne au total"))
a.p(T(
    "Two things are true at once and they pull in opposite directions.",
    "Deux choses sont vraies en même temps et tirent en sens opposés."))
a.p(T(
    "Canada holds real weight in a handful of American supply chains, and it is the kind "
    "of weight that cannot be shopped around quickly — a refinery built for heavy crude, a "
    "reactor fuelled on Canadian uranium, a fertiliser season with no second potash "
    "supplier, a state that draws most of its power across the border. In those places a "
    "tariff on Canadian goods is a tax on an input with no near substitute. How much of "
    "that lands on the American buyer rather than the Canadian seller is disputed: "
    "estimates of the American share range from about half to about ninety percent, and "
    "one study finds that the dominant supplier of a product absorbs the most — which "
    "would mean Canada absorbing more, not less, in exactly these categories.",
    "Le Canada pèse réellement dans une poignée de chaînes d'approvisionnement "
    "américaines, et c'est un poids qu'on ne peut pas remplacer rapidement — une "
    "raffinerie conçue pour le brut lourd, un réacteur alimenté à l'uranium canadien, une "
    "saison d'engrais sans deuxième fournisseur de potasse, un État qui tire la majeure "
    "partie de son électricité de l'autre côté de la frontière. À ces endroits, un tarif "
    "sur des biens canadiens est une taxe sur un intrant sans substitut proche. La part qui "
    "retombe sur l'acheteur américain plutôt que sur le vendeur canadien est contestée : "
    "les estimations de la part américaine vont d'environ la moitié à environ quatre-vingt-"
    "dix pour cent, et une étude conclut que le fournisseur dominant d'un produit en "
    "absorbe le plus — ce qui voudrait dire que le Canada en absorbe davantage, et non "
    "moins, précisément dans ces catégories."),)
a.p(T(
    "And Canada is far more concentrated. One customer takes about seven tenths of what "
    "the country sells, nine tenths of its oil and all of its exported electricity. "
    "Fifteen point nine percent of the economy and more than two and a half million jobs "
    "sit on that one relationship. Leverage in a few products does not offset exposure across the "
    "whole economy, and it would not even if every tariff came off tomorrow morning. That "
    "is the argument for ports, pipelines to other coasts, open provincial borders and "
    "other buyers — and it is an argument about the next twenty years, not about this "
    "year's trade file.",
    "Et le Canada est bien plus concentré. Un seul client absorbe environ les sept dixièmes "
    "de ce que le pays vend, les neuf dixièmes de son pétrole et la totalité de son "
    "électricité exportée. Quinze virgule neuf pour cent de l'économie et plus de deux "
    "millions et demi d'emplois reposent sur cette seule relation. Un rapport de force sur quelques "
    "produits ne compense pas une exposition à l'échelle de toute l'économie, et ce serait "
    "encore vrai si tous les tarifs tombaient demain matin. C'est l'argument en faveur des "
    "ports, des pipelines vers d'autres côtes, de l'ouverture des frontières provinciales "
    "et d'autres acheteurs — et c'est un argument sur les vingt prochaines années, pas sur "
    "le dossier commercial de cette année."))

a.h2(T("What could not be checked", "Ce qui n'a pas pu être vérifié"))
a.ul([
    T("The share of Canada's imports of machinery, food or consumer goods that comes from "
      "the United States. That needs a Statistics Canada table that could not be queried, "
      "so no category-level import share is printed here.",
      "La part des importations canadiennes de machinerie, d'aliments ou de biens de "
      "consommation qui provient des États-Unis. Cela exige un tableau de Statistique "
      "Canada qui n'a pas pu être interrogé, alors aucune part d'importation par catégorie "
      "n'est indiquée ici."),
    T("The American share of Canadian aerospace and machinery exports. The industry reports "
      "give a total but not the destination split.",
      "La part américaine des exportations canadiennes en aérospatiale et en machinerie. "
      "Les rapports sectoriels donnent un total mais pas la répartition par destination."),
    T("How much of a Chinese-made good is American-owned or American-designed. No agency "
      "publishes it.",
      "Quelle part d'un bien fabriqué en Chine appartient à des intérêts américains ou est "
      "de conception américaine. Aucun organisme ne le publie."),
])

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("who-gets-the-tariff-money-back.html",
         T("A hundred billion dollars went back. Who got it?",
           "Cent milliards de dollars sont repartis. Qui les a reçus ?")),
    link("did-us-tariffs-on-canada-work.html",
         T("When a tariff goes on, who actually gains?",
           "Quand un tarif est imposé, qui y gagne vraiment ?")),
    link("how-canada-rebuilds-its-economy.html",
         T("How Canada rebuilds — new customers, old barriers",
           "Comment le Canada se rebâtit — nouveaux clients, vieilles barrières")),
])

a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://www.usitc.gov/sites/default/files/publications/332/executive_briefings/ebot_potash.pdf",
             T("United States International Trade Commission — executive briefing on potash, November 2025",
               "Commission du commerce international des États-Unis — note sur la potasse, novembre 2025")),
    out_link("https://pubs.usgs.gov/publication/fs20253057/full",
             T("United States Geological Survey — Fact Sheet 2025-3057, uranium",
               "Service géologique des États-Unis — fiche 2025-3057, uranium")),
    out_link("https://www.mining.com/web/column-us-aluminum-smelters-vie-with-big-tech-for-scarce-power/",
             T("MINING.COM and Reuters — American aluminium smelters compete with data centres for power",
               "MINING.COM et Reuters — les fonderies d'aluminium américaines se disputent l'électricité avec les centres de données")),
    out_link("https://www.rbc.com/en/thought-leadership/the-trade-zone/washingtons-heavy-oil-dilemma/",
             T("RBC — Washington's heavy oil dilemma",
               "RBC — le dilemme du pétrole lourd à Washington")),
    out_link("https://www.cjr.org/analysis/tariffs-canada-newsprint.php",
             T("Columbia Journalism Review — tariffs, Canada and newsprint, March 2025",
               "Columbia Journalism Review — tarifs, Canada et papier journal, mars 2025")),
    out_link("https://www.emge.com/news/north-american-newsprint-market-capacity-closures-and-2026-outlook",
             T("EMGE — North American newsprint capacity closures and 2026 outlook",
               "EMGE — fermetures de capacité de papier journal en Amérique du Nord et perspectives 2026")),
    out_link("https://search.open.canada.ca/qpnotes/record/ic%2CIND-2025-QP-00004",
             T("Innovation, Science and Economic Development Canada — briefing note on the auto sector, May 2025",
               "Innovation, Sciences et Développement économique Canada — note d'information sur le secteur automobile, mai 2025")),
    out_link("https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-iron-steel.pdf",
             T("United States Geological Survey — Mineral Commodity Summaries 2026, iron and steel",
               "Service géologique des États-Unis — Sommaires des produits minéraux 2026, fer et acier")),
    out_link("https://www.census.gov/foreign-trade/balance/c1220.html",
             T("United States Census Bureau — trade in goods with Canada",
               "Bureau du recensement des États-Unis — commerce de biens avec le Canada")),
    out_link("https://www.census.gov/foreign-trade/balance/c5700.html",
             T("United States Census Bureau — trade in goods with China",
               "Bureau du recensement des États-Unis — commerce de biens avec la Chine")),
    out_link("https://usafacts.org/answers/what-is-the-value-of-us-trade/countries/canada/",
             T("USAFacts, from Bureau of Economic Analysis data — what the United States trades with Canada",
               "USAFacts, à partir des données du Bureau of Economic Analysis — ce que les États-Unis échangent avec le Canada")),
    out_link("https://usafacts.org/answers/what-is-the-value-of-us-trade/countries/china/",
             T("USAFacts, from Bureau of Economic Analysis data — what the United States trades with China",
               "USAFacts, à partir des données du Bureau of Economic Analysis — ce que les États-Unis échangent avec la Chine")),
    out_link("https://www.frbsf.org/research-and-insights/publications/economic-letter/2011/08/us-made-in-china/",
             T("Federal Reserve Bank of San Francisco — the US content of made in China, 2011",
               "Banque fédérale de réserve de San Francisco — le contenu américain du « fabriqué en Chine », 2011")),
    out_link("https://www150.statcan.gc.ca/n1/pub/13-605-x/2026001/article/00001-eng.htm",
             T("Statistics Canada — value added and jobs associated with exports to the United States, 2024",
               "Statistique Canada — valeur ajoutée et emplois associés aux exportations vers les États-Unis, 2024")),
    out_link("https://www150.statcan.gc.ca/n1/daily-quotidien/260219/dq260219a-eng.htm",
             T("Statistics Canada — Canadian international merchandise trade, December 2025",
               "Statistique Canada — Commerce international de marchandises du Canada, décembre 2025")),
    out_link("https://www.statcan.gc.ca/o1/en/app/7870-perspectives-country-attribution-canadian-international-merchandise-trade-statistics",
             T("Statistics Canada — perspectives on country attribution in merchandise trade statistics",
               "Statistique Canada — perspectives sur l'attribution par pays dans les statistiques du commerce de marchandises")),
    out_link("https://international.canada.ca/en/global-affairs/corporate/reports/chief-economist/annual/2025",
             T("Global Affairs Canada — highlights of Canada's merchandise trade performance, 2025",
               "Affaires mondiales Canada — faits saillants du commerce de marchandises du Canada, 2025")),
    out_link("https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2026/market-snapshot-overview-of-2025-canada-us-energy-trade.html",
             T("Canada Energy Regulator — overview of 2025 Canada-United States energy trade",
               "Régie de l'énergie du Canada — aperçu du commerce énergétique Canada-États-Unis en 2025")),
    out_link("https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-potash.pdf",
             T("United States Geological Survey — Mineral Commodity Summaries 2026, potash",
               "Service géologique des États-Unis — Sommaires des produits minéraux 2026, potasse")),
    out_link("https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-aluminum.pdf",
             T("United States Geological Survey — Mineral Commodity Summaries 2026, aluminium",
               "Service géologique des États-Unis — Sommaires des produits minéraux 2026, aluminium")),
    out_link("https://www.kansascityfed.org/research/economic-bulletin/canadian-oil-important-for-midwest-gasoline-prices/",
             T("Federal Reserve Bank of Kansas City — Canadian oil and Midwest gasoline prices",
               "Banque fédérale de réserve de Kansas City — le pétrole canadien et les prix de l'essence dans le Midwest")),
    out_link("https://www.eia.gov/uranium/marketing/",
             T("United States Energy Information Administration — Uranium Marketing Annual Report",
               "Administration américaine d'information sur l'énergie — rapport annuel sur la commercialisation de l'uranium")),
    out_link("https://www.eia.gov/todayinenergy/detail.php?id=67904",
             T("United States Energy Information Administration — Canada-United States energy trade in 2025",
               "Administration américaine d'information sur l'énergie — commerce énergétique Canada-États-Unis en 2025")),
    out_link("https://www.rbc.com/en/thought-leadership/energy/power-play-assessing-canadas-electricity-advantage-in-u-s-trade-talks/",
             T("RBC — assessing Canada's electricity advantage",
               "RBC — évaluer l'avantage électrique du Canada")),
    out_link("https://www.fastmarkets.com/insights/can-us-federal-land-offset-imported-canadian-forest-products/",
             T("Fastmarkets — can American federal land offset imported Canadian forest products?",
               "Fastmarkets — les terres fédérales américaines peuvent-elles remplacer les produits forestiers canadiens importés ?")),
    out_link("https://statcan.gc.ca/en/topics-start/canada-united-states/trade",
             T("Statistics Canada — focus on Canada and the United States: trade",
               "Statistique Canada — le Canada et les États-Unis : le commerce")),
])

a.disclaimer(T(
    "This article is for general information and study. "
    "This site is unofficial and not affiliated with the Government of Canada or the "
    "Government of the United States. Every source used is listed above and on our "
    "sources page.",
    "Cet article est fourni à titre d'information générale et d'étude. Ce site est non "
    "officiel et n'a aucun lien avec le gouvernement du Canada ni avec celui des "
    "États-Unis. Toutes les sources utilisées sont énumérées ci-dessus et sur notre page "
    "des sources."))

if __name__ == "__main__":
    a.build()
    flush_pairs()
