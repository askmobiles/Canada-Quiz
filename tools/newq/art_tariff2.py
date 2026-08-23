#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article 2 of 3 — when a tariff goes on, who actually gains?

Written from a Canadian point of view and written against nobody. That is not a
softening: it is easier to be accurate when you are not trying to score. No
individual official is named on this page. Governments and departments are
named, because they are the ones who publish.

The rule this page is built on: quote what is claimed, print what was
measured, and where the measurements disagree say so instead of picking a
winner. Two Federal Reserve banks genuinely do not agree with each other about
the inflation question, and pretending otherwise would be dishonest. An earlier
draft called it three by conscripting a Harvard paper into the Federal Reserve,
which is the kind of small false precision this site exists not to commit.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="did-us-tariffs-on-canada-work.html",
    section="Trade",
    title=T("Tariffs Between Canada and the USA — Who Actually Gains?",
            "Les tarifs entre le Canada et les États-Unis — qui y gagne vraiment ?"),
    desc=T("A Canadian look at who a tariff actually costs and who it actually "
           "helps: the revenue, the refunds, the jobs on both sides of the border, "
           "and why the smaller country feels it more.",
           "Un regard canadien sur ce qu'un tarif coûte réellement et sur qui il aide "
           "réellement : les recettes, les remboursements, les emplois des deux côtés "
           "de la frontière, et pourquoi le plus petit pays le ressent davantage."),
    h1=T("\U0001F3ED When a tariff goes on, who actually gains?",
         "\U0001F3ED Quand un tarif est imposé, qui y gagne vraiment ?"),
    hero=T("A tariff is not a payment from one country to another. It is a tax paid "
           "at the border by the company bringing the goods in — and that changes the "
           "answer to who gains completely.",
           "Un tarif n'est pas un paiement d'un pays à un autre. C'est une taxe payée "
           "à la frontière par l'entreprise qui fait entrer la marchandise — et cela "
           "change complètement la réponse à la question de savoir qui y gagne."),
    checked=T("Last checked 22 August 2026 — this page covers a fast-moving situation",
              "Dernière vérification le 22 août 2026 — cette page traite d'une "
              "situation qui évolue vite"),
)

a.callout(T(
    "<strong>How is this page written?</strong> This is a Canadian site and this page "
    "is written for Canadians. It is not written against anyone. Tariffs are a "
    "decision governments make, and every country has made that decision at some "
    "point, Canada included. What this page does is look at what the numbers did "
    "afterwards. We name sources, not culprits, and where two good sources disagree we "
    "print both and leave the judgement to you. All dollar figures on this page are "
    "American dollars unless we say otherwise.",
    "<strong>Comment cette page est-elle écrite ?</strong> Ceci est un site canadien et "
    "cette page est écrite pour les Canadiens. Elle n'est écrite contre personne. Les "
    "tarifs sont une décision que prennent les gouvernements, et chaque pays l'a prise "
    "à un moment ou à un autre, le Canada compris. Ce que fait cette page, c'est "
    "regarder ce que les chiffres ont donné ensuite. Nous nommons des sources, pas des "
    "coupables, et là où deux bonnes sources divergent, nous imprimons les deux et "
    "vous laissons juger. Tous les montants sur cette page sont en dollars américains, "
    "sauf indication contraire."))

a.h2(T("The short answer", "La réponse courte"))
a.p(T(
    "Neither country came out ahead, and Canada felt it more. That is the honest "
    "summary of two years of numbers, and the rest of this page is the working behind "
    "it.",
    "Ni l'un ni l'autre des deux pays n'en est sorti gagnant, et le Canada l'a "
    "davantage ressenti. C'est le résumé honnête de deux années de chiffres, et le "
    "reste de cette page en est la démonstration."))
a.p(T(
    "Start with the thing most people have backwards. A tariff is not money one "
    "country pays another. It is a tax collected at the border from the company doing "
    "the importing — an American company, when the goods are Canadian. Whether the "
    "exporter ends up carrying that cost depends on whether the buyer can find the "
    "same thing somewhere else. The Federal Reserve Bank of New York measured this "
    "across detailed trade data and found that in 2025 about 90 percent of the cost "
    "was carried by American firms and their customers.",
    "Commençons par ce que la plupart des gens ont à l'envers. Un tarif n'est pas de "
    "l'argent qu'un pays verse à un autre. C'est une taxe perçue à la frontière auprès "
    "de l'entreprise importatrice — une entreprise américaine, quand la marchandise "
    "est canadienne. Que l'exportateur finisse par en porter le coût dépend de la "
    "capacité de l'acheteur à trouver la même chose ailleurs. La Banque fédérale de "
    "réserve de New York a mesuré cela à partir de données commerciales détaillées et "
    "a conclu qu'en 2025, environ 90 pour cent du coût avait été porté par des "
    "entreprises américaines et leurs clients."))
a.p(T(
    "So on the American side the ledger has real entries on both lines. Customs "
    "revenue more than doubled, then about 100 billion dollars of it went back out "
    "after the Supreme Court ruling in February 2026. Steel output rose 5.7 percent "
    "and one aluminium smelter came back to full capacity with 150 jobs. Against that, "
    "manufacturing employment across the country is 62,000 lower than in January 2025, "
    "and two independent estimates put the cost to an average household between 840 "
    "and 1,100 dollars a year.",
    "Du côté américain, le bilan comporte donc de vraies entrées dans les deux "
    "colonnes. Les recettes douanières ont plus que doublé, puis environ 100 milliards "
    "de dollars sont ressortis après la décision de la Cour suprême en février 2026. "
    "La production d'acier a augmenté de 5,7 pour cent et une fonderie d'aluminium est "
    "revenue à pleine capacité avec 150 emplois. En regard, l'emploi manufacturier à "
    "l'échelle du pays est inférieur de 62 000 à celui de janvier 2025, et deux "
    "estimations indépendantes chiffrent le coût pour un ménage moyen entre 840 et "
    "1 100 dollars par année."))
a.p(T(
    "On the Canadian side the dollar losses are smaller, because Canada is a smaller "
    "country. Measured against the size of the place, they are much larger.",
    "Du côté canadien, les pertes en dollars sont plus petites, parce que le Canada "
    "est un plus petit pays. Rapportées à la taille du pays, elles sont beaucoup plus "
    "grandes."))
a.p(T(
    "Statistics Canada worked out that in 2024, 15.9 percent of Canada's whole economy "
    "was the making of things sold to the United States, and that this accounted for "
    "more than 2.5 million Canadian jobs. Nothing on the American side is anywhere "
    "near that exposed to Canada.",
    "Statistique Canada a calculé qu'en 2024, 15,9 pour cent de toute l'économie "
    "canadienne consistait à fabriquer ce qui est vendu aux États-Unis, et que cela "
    "représentait plus de 2,5 millions d'emplois canadiens. Rien du côté américain "
    "n'est aussi exposé au Canada."))
a.p(T(
    "Before any of this began, the Peterson Institute modelled a 25 percent tariff "
    "with matching retaliation. It put the peak cost at about 0.5 percent of American "
    "output against about 2.3 percent of Canadian output — four to five times heavier "
    "here. That was a projection rather than a measurement.",
    "Avant même que tout cela commence, le Peterson Institute a modélisé un tarif de "
    "25 pour cent avec riposte équivalente. Il a chiffré le coût maximal à environ 0,5 "
    "pour cent de la production américaine contre environ 2,3 pour cent de la "
    "production canadienne — quatre à cinq fois plus lourd ici. C'était une projection "
    "et non une mesure."))
a.p(T(
    "The direction has held up. Canada's economy stood still for a full year: the "
    "level of output was roughly unchanged from the first quarter of 2025 to the first "
    "quarter of 2026, in the Bank of Canada's own words. The American economy grew 2.1 "
    "percent over 2025.",
    "La direction s'est confirmée. L'économie canadienne a fait du surplace pendant une "
    "année entière : le niveau de production est resté à peu près inchangé entre le "
    "premier trimestre de 2025 et le premier trimestre de 2026, selon les mots mêmes "
    "de la Banque du Canada. L'économie américaine a crû de 2,1 pour cent en 2025."))
a.p(T(
    "So if the question is which country comes out ahead, the answer is neither. If "
    "the question is which one feels it more, the answer is Canada.",
    "Donc si la question est de savoir quel pays en sort gagnant, la réponse est : ni "
    "l'un ni l'autre. Si la question est de savoir lequel le ressent davantage, la "
    "réponse est : le Canada."))

a.callout(T(
    "<strong>So, plainly.</strong> A tariff between two countries this closely joined "
    "does not move money from one to the other. It makes the same goods cost more on "
    "both sides of the line, protects a small number of plants narrowly, and spreads a "
    "small cost across a great many people. On the numbers so far it has cost both "
    "countries and gained neither very much — and Canada, being the smaller and far "
    "more dependent partner, has carried more of it. That is not a complaint about "
    "anybody. It is what happens when two economies that were built into each other "
    "put a tax between them.",
    "<strong>En clair.</strong> Un tarif entre deux pays aussi étroitement liés ne "
    "déplace pas d'argent de l'un vers l'autre. Il rend les mêmes marchandises plus "
    "chères des deux côtés de la ligne, protège étroitement un petit nombre d'usines, "
    "et répartit un petit coût sur un très grand nombre de gens. Selon les chiffres "
    "obtenus jusqu'ici, il a coûté aux deux pays et n'a beaucoup rapporté à aucun — et "
    "le Canada, partenaire plus petit et bien plus dépendant, en a porté davantage. Ce "
    "n'est pas une plainte contre qui que ce soit. C'est ce qui arrive quand deux "
    "économies bâties l'une dans l'autre mettent une taxe entre elles."))

a.h2(T("The money came in, and then a lot of it went back out",
       "L'argent est entré, puis une bonne partie est ressortie"))
a.p(T(
    "American customs duties from every country went from 77 billion dollars in the "
    "2024 fiscal year to 195 billion in 2025. That is a real and very large increase, "
    "and it is the strongest single fact in favour of the policy.",
    "Les droits de douane américains, tous pays confondus, sont passés de 77 milliards "
    "de dollars pour l'exercice 2024 à 195 milliards pour 2025. C'est une hausse "
    "réelle et très importante, et c'est le fait le plus solide en faveur de la "
    "politique."))
a.p(T(
    "Then, on 20 February 2026, the United States Supreme Court struck down the "
    "tariffs that had been imposed under emergency economic powers, including those on "
    "Canada. About 100 billion dollars had been refunded to importers by the middle of "
    "2026, out of 166 billion collected under that law, and the Congressional Budget "
    "Office expects most of that 166 billion to go back. In July 2026 alone, the United "
    "States collected about 26 billion in customs duties and paid out about 36 billion "
    "in refunds, so the month came in net negative — the Congressional Budget Office "
    "puts it at around 9 billion. The Congressional Budget Office now "
    "expects 2026 collections to land about 250 billion below its own February "
    "forecast.",
    "Puis, le 20 février 2026, la Cour suprême des États-Unis a invalidé les tarifs "
    "imposés en vertu des pouvoirs économiques d'urgence, y compris ceux visant le "
    "Canada. Environ 100 milliards de dollars avaient été remboursés aux importateurs "
    "au milieu de 2026, sur les 166 milliards perçus sous cette loi, et le Bureau du "
    "budget du Congrès s'attend à ce que la majeure partie de ces 166 milliards soit "
    "rendue. Pour le seul "
    "mois de juillet 2026, les États-Unis ont perçu environ 26 milliards en droits de "
    "douane et versé environ 36 milliards en remboursements : le mois s'est soldé en "
    "négatif net — le Bureau du budget du Congrès l'évalue à environ 9 milliards. Le Bureau du budget du Congrès s'attend désormais à ce que les "
    "recettes de 2026 soient inférieures d'environ 250 milliards à sa propre "
    "prévision de février."))
a.p(T(
    "The tariffs on steel, aluminium, copper, vehicles and lumber were not affected by "
    "the ruling, because they rest on a different law about national security. Those "
    "are still in force, and so is the new 50 percent measure that took effect on 22 "
    "August 2026.",
    "Les tarifs sur l'acier, l'aluminium, le cuivre, les véhicules et le bois n'ont "
    "pas été touchés par la décision, parce qu'ils reposent sur une autre loi portant "
    "sur la sécurité nationale. Ils demeurent en vigueur, tout comme la nouvelle "
    "mesure de 50 pour cent entrée en vigueur le 22 août 2026."))

a.h2(T("Who actually pays a tariff", "Qui paie réellement un tarif"))
a.p(T(
    "Legally this part is not in dispute. A tariff is paid to United States Customs "
    "and Border Protection by the American company importing the goods. The economic "
    "question is whether that company gets the money back by squeezing the foreign "
    "seller, or passes it on to American customers.",
    "Sur le plan juridique, ce point n'est pas contesté. Un tarif est versé au service "
    "des douanes américain par l'entreprise américaine qui importe la marchandise. La "
    "question économique est de savoir si cette entreprise récupère l'argent en "
    "serrant le vendeur étranger, ou le refile aux clients américains."))
a.p(T(
    "The Federal Reserve Bank of New York looked at this in February 2026 using "
    "detailed tariff-code data, and found that American firms and consumers bore about "
    "90 percent of the burden in 2025. Several independent research teams reached "
    "close to the same answer. Where economists disagree is on speed: one study finds "
    "the cost fully passed through to prices after about seven months, while Cavallo, "
    "Llamas and Vazquez at Harvard find it still incomplete at six months, with a "
    "cumulative effect on consumer prices of about 0.8 of a percentage point by early "
    "2026.",
    "La Banque fédérale de réserve de New York s'est penchée là-dessus en février 2026 "
    "à partir de données détaillées par code tarifaire, et a conclu que les "
    "entreprises et les consommateurs américains avaient supporté environ 90 pour cent "
    "du fardeau en 2025. Plusieurs équipes de recherche indépendantes sont arrivées à "
    "peu près au même résultat. Là où les économistes divergent, c'est sur la "
    "vitesse : une étude trouve le coût entièrement répercuté sur les prix après "
    "environ sept mois, tandis que Cavallo, Llamas et Vazquez, de Harvard, le trouvent "
    "encore incomplet à six mois, avec un effet cumulatif sur les prix à la "
    "consommation d'environ 0,8 point de pourcentage au début de 2026."))

a.h2(T("Did the protected industries actually gain?",
       "Les industries protégées ont-elles réellement gagné ?"))

a.h3(T("Steel: more tonnes, much higher prices, flat jobs",
       "Acier : plus de tonnes, des prix bien plus élevés, l'emploi stable"))
a.p(T(
    "American raw steel production is up 5.7 percent so far in 2026 against the same "
    "weeks of 2025. Capacity use rose from 77.0 percent to 78.9 percent — real "
    "improvement, but still short of the 80 percent that the policy itself names as "
    "the target. Prices rose far more than output. American hot-rolled coil was "
    "1,201.50 dollars a tonne on 26 May 2026, up 31 percent since the rate doubled to "
    "50 percent in June 2025 and 58 percent since January 2025. Southeast Asian coil was 571 "
    "dollars the same day. Producer prices for steel mill products rose 13.3 percent "
    "in a year, which is a cost paid by every American factory that buys steel rather "
    "than makes it.",
    "La production américaine d'acier brut est en hausse de 5,7 pour cent depuis le "
    "début de 2026 par rapport aux mêmes semaines de 2025. Le taux d'utilisation est "
    "passé de 77,0 à 78,9 pour cent — une amélioration réelle, mais toujours sous les "
    "80 pour cent que la politique elle-même fixe comme cible. Les prix ont monté bien "
    "plus que la production. La bobine laminée à chaud américaine valait 1 201,50 "
    "dollars la tonne le 26 mai 2026, en hausse de 31 pour cent depuis le doublement du "
    "taux à 50 pour cent en juin 2025 et de 58 pour cent depuis janvier 2025. La bobine "
    "d'Asie du Sud-Est valait 571 dollars le même jour. Les prix à la production des "
    "produits d'aciérie ont grimpé de 13,3 pour cent en un an, un coût payé par chaque "
    "usine américaine qui achète de l'acier au lieu d'en fabriquer."))

a.h3(T("Aluminium: production fell, and one plant came back",
       "Aluminium : la production a baissé, et une usine est revenue"))
a.p(T(
    "This is the clearest single case, and it cuts both ways. According to the United "
    "States Geological Survey, American primary aluminium production fell from 676,000 "
    "tonnes in 2024 to an estimated 660,000 tonnes in 2025 — down, not up, despite the "
    "tariffs. Employment went from 29,900 to about 30,000, a gain of roughly a hundred "
    "people. The price rose 39 percent.",
    "C'est le cas le plus net, et il tranche dans les deux sens. Selon le Service "
    "géologique des États-Unis, la production américaine d'aluminium primaire est "
    "passée de 676 000 tonnes en 2024 à environ 660 000 tonnes en 2025 — en baisse, "
    "non en hausse, malgré les tarifs. L'emploi est passé de 29 900 à environ 30 000, "
    "un gain d'une centaine de personnes. Le prix a monté de 39 pour cent."))
a.p(T(
    "But one thing did happen that would not have happened otherwise. Century "
    "Aluminum's Mt. Holly smelter in South Carolina returned to full capacity in July "
    "2026 for the first time since 2015 — it had been running at half capacity, not "
    "closed. The restart is 50,000 tonnes a year, which the company says lifts "
    "American primary aluminium output by about 10 percent, along with 150 jobs and a "
    "50 million dollar investment. The company's chief executive credited the import "
    "tariffs with saving the plant. That is a genuine result and it deserves to be "
    "counted.",
    "Mais une chose s'est produite qui ne se serait pas produite autrement. La "
    "fonderie Mt. Holly de Century Aluminum, en Caroline du Sud, est revenue à pleine "
    "capacité en juillet 2026 pour la première fois depuis 2015 — elle tournait à "
    "moitié capacité, elle n'était pas fermée. La remise en route représente 50 000 "
    "tonnes par an, ce qui, selon l'entreprise, accroît la production américaine "
    "d'aluminium primaire d'environ 10 pour cent, avec 150 emplois et un "
    "investissement de 50 millions de dollars. Le chef de la direction a attribué aux "
    "tarifs le sauvetage de l'usine. C'est un résultat véritable et il mérite d'être "
    "compté."))

a.h3(T("Vehicles: billions absorbed, prices barely moved",
       "Véhicules : des milliards absorbés, des prix presque inchangés"))
a.p(T(
    "Carmakers have absorbed about 35.4 billion dollars in tariff costs since the "
    "measures began, with Ford, General Motors and Stellantis accounting for 6.5 "
    "billion between them in one year. Yet the price American families actually paid "
    "barely shifted: new vehicles were up 0.5 percent and used cars and trucks were "
    "down 1.9 percent in the year to July 2026. Both Ford and General Motors raised "
    "their 2026 guidance after receiving tariff refunds following the Supreme Court "
    "ruling.",
    "Les constructeurs ont absorbé environ 35,4 milliards de dollars en coûts "
    "tarifaires depuis le début des mesures, dont 6,5 milliards pour Ford, General "
    "Motors et Stellantis réunis en une seule année. Pourtant, le prix réellement payé "
    "par les familles américaines a à peine bougé : les véhicules neufs ont augmenté "
    "de 0,5 pour cent et les voitures et camions d'occasion ont baissé de 1,9 pour "
    "cent sur l'année se terminant en juillet 2026. Ford et General Motors ont tous "
    "deux relevé leurs prévisions pour 2026 après avoir reçu des remboursements à la "
    "suite de la décision de la Cour suprême."))

a.h3(T("Lumber and housing: the predicted spike did not arrive",
       "Bois et habitation : la flambée annoncée n'est pas venue"))
a.p(T(
    "American homebuilders estimated in April 2025 that tariff actions were adding "
    "about 10,900 dollars to the cost of a house. That was a survey of builders' own "
    "expectations, not a measurement, and it is now more than a year old. The "
    "measurement is less dramatic: framing lumber was 536.15 dollars per thousand "
    "board feet on 14 August 2026, unchanged from a year earlier, and futures were "
    "down 6.6 percent. American sawmills were running at only 64 percent of capacity "
    "in early 2025, so domestic supply did not rush in to replace the Canadian wood.",
    "Les constructeurs d'habitations américains estimaient en avril 2025 que les "
    "mesures tarifaires ajoutaient environ 10 900 dollars au coût d'une maison. "
    "C'était un sondage sur les attentes des constructeurs, non une mesure, et il date "
    "de plus d'un an. La mesure est moins spectaculaire : le bois de charpente valait "
    "536,15 dollars les mille pieds-planche le 14 août 2026, inchangé par rapport à un "
    "an plus tôt, et les contrats à terme étaient en baisse de 6,6 pour cent. Les "
    "scieries américaines ne tournaient qu'à 64 pour cent de leur capacité au début de "
    "2025 : l'offre intérieure ne s'est donc pas précipitée pour remplacer le bois "
    "canadien."))

a.h2(T("What it cost", "Ce que cela a coûté"))
a.p(T(
    "American manufacturing employment stood at 12,611,000 in July 2026, which is "
    "62,000 lower than in January 2025. It had been 93,000 lower in December 2025 "
    "before a partial recovery. The Cato Institute, looking at the same figures in "
    "January 2026, described the pattern as concentrated benefits and dispersed costs: "
    "primary metals was one of the few sectors adding jobs, while machinery, computers "
    "and transport equipment lost the most. Cato also cautioned, fairly, that "
    "employment data alone cannot prove what caused what.",
    "L'emploi manufacturier américain s'élevait à 12 611 000 en juillet 2026, soit "
    "62 000 de moins qu'en janvier 2025. Le creux était de 93 000 en décembre 2025, "
    "avant une reprise partielle. L'Institut Cato, examinant les mêmes chiffres en "
    "janvier 2026, a décrit le phénomène comme des avantages concentrés et des coûts "
    "dispersés : les métaux primaires figuraient parmi les rares secteurs à créer des "
    "emplois, tandis que la machinerie, l'informatique et le matériel de transport en "
    "perdaient le plus. Cato a aussi prévenu, à juste titre, que les seules données "
    "sur l'emploi ne peuvent pas prouver ce qui a causé quoi."))
a.p(T(
    "American farmers took a measurable hit from Canada's reply. The United States "
    "Department of Agriculture found that American exports to Canada of the targeted "
    "farm products fell by nearly 440 million dollars between March and June 2025 "
    "compared with the same months of 2024. Canada lifted those particular "
    "counter-tariffs on 1 September 2025.",
    "Les agriculteurs américains ont subi un coup mesurable de la riposte canadienne. "
    "Le Département de l'Agriculture des États-Unis a constaté que les exportations "
    "américaines vers le Canada des produits agricoles visés avaient reculé de près de "
    "440 millions de dollars entre mars et juin 2025 par rapport aux mêmes mois de "
    "2024. Le Canada a levé ces contre-tarifs précis le 1er septembre 2025."))
a.p(T(
    "For households, two independent estimates put the cost between 840 and 1,100 "
    "dollars a year. The Budget Lab at Yale estimated the consumer price level about "
    "0.7 percent higher and roughly 1,100 dollars per household; the Tax Foundation "
    "estimated 1,000 dollars in 2025 and 840 in 2026. The Tax Foundation also scores "
    "the tariffs at 0.4 percent lower "
    "American gross domestic product in the long run and 345,000 fewer full-time jobs. "
    "Those last figures are model projections, not measurements.",
    "Pour les ménages, deux estimations indépendantes situent le coût entre 840 et "
    "1 100 dollars par année. Le Budget Lab de Yale évalue le niveau des prix à la "
    "consommation à environ 0,7 pour cent de plus, soit à peu près 1 100 dollars par "
    "ménage; la Tax Foundation évalue 1 000 dollars en 2025 et 840 en 2026. La Tax "
    "Foundation chiffre aussi les tarifs à "
    "0,4 pour cent de produit intérieur brut américain en moins à long terme et "
    "345 000 emplois à temps plein en moins. Ces derniers chiffres sont des "
    "projections de modèle, non des mesures."))

a.callout(T(
    "<strong>Two Federal Reserve banks do not agree with each other.</strong> The "
    "Minneapolis Fed found in April 2026 that inflation by product category was "
    "actually negatively correlated with tariff exposure — the categories most exposed "
    "showed the least inflation — and concluded that tariffs cannot explain rising "
    "goods inflation. The St. Louis Fed found in August 2026 that tariffs did explain a "
    "large share through February 2026 but that other factors have been the main "
    "drivers since March. We are not going to referee this. It is a live disagreement "
    "among serious people inside the same central bank system, and anyone quoting one "
    "of them as settled fact is leaving out the other.",
    "<strong>Deux banques de la Réserve fédérale ne s'entendent pas entre elles.</strong> "
    "La Fed de Minneapolis a constaté en avril 2026 que l'inflation par catégorie de "
    "produits était en fait négativement corrélée à l'exposition aux tarifs — les "
    "catégories les plus exposées affichaient le moins d'inflation — et en a conclu "
    "que les tarifs ne peuvent pas expliquer la hausse des prix des biens. La Fed de "
    "Saint-Louis a constaté en août 2026 que les tarifs en expliquaient une large part "
    "jusqu'en février 2026, mais que d'autres facteurs dominent depuis mars. Nous "
    "n'allons pas arbitrer. C'est un désaccord vivant entre gens sérieux au sein du "
    "même système de banque centrale, et quiconque cite l'une des deux comme un fait "
    "établi laisse l'autre de côté."))

a.h2(T("Why a neighbour is a different case",
       "Pourquoi un voisin, c'est un cas différent"))
a.p(T(
    "A tariff on a distant supplier and a tariff on the country next door do not work "
    "the same way, because the country next door is inside the supply chain rather "
    "than at the end of it. Canada and Mexico together account for close to half of "
    "all American imports and exports of vehicles and parts, and supply nearly 40 "
    "percent of American imports of steel mill products. A 2019 academic study found "
    "that 74 percent of the foreign value in vehicles imported from Mexico was itself "
    "American-made. A tariff on those vehicles therefore falls partly on American-made "
    "content.",
    "Un tarif sur un fournisseur lointain et un tarif sur le pays voisin ne "
    "fonctionnent pas de la même façon, parce que le pays voisin se trouve à "
    "l'intérieur de la chaîne d'approvisionnement plutôt qu'à son extrémité. Le Canada "
    "et le Mexique représentent ensemble près de la moitié de toutes les importations "
    "et exportations américaines de véhicules et de pièces, et fournissent près de 40 "
    "pour cent des importations américaines de produits d'aciérie. Une étude "
    "universitaire de 2019 a trouvé que 74 pour cent de la valeur étrangère des "
    "véhicules importés du Mexique était elle-même de fabrication américaine. Un tarif "
    "sur ces véhicules frappe donc en partie du contenu de fabrication américaine."))
a.p(T(
    "You will often read that a car part crosses the Canada-United States border six "
    "to eight times before a vehicle is finished. It is worth knowing where that comes "
    "from: a 2017 news report and, later, political speeches. It has never been "
    "established by a government or academic study. The best-documented single part "
    "anyone has actually followed — a capacitor inside a seat assembly, traced by NBC "
    "News — crossed four times. Four is still a remarkable number, and it makes the "
    "point without needing a bigger one.",
    "On lit souvent qu'une pièce d'auto traverse la frontière canado-américaine de six "
    "à huit fois avant qu'un véhicule soit terminé. Il vaut la peine de savoir d'où "
    "cela vient : d'un reportage de 2017 et, plus tard, de discours politiques. Cela "
    "n'a jamais été établi par une étude gouvernementale ou universitaire. La pièce la "
    "mieux documentée qu'on ait réellement suivie — un condensateur dans un ensemble "
    "de siège, retracé par NBC News — a traversé quatre fois. Quatre reste un chiffre "
    "remarquable, et il fait la démonstration sans qu'on ait besoin d'un plus grand."))
a.p(T(
    "Energy is the clearest illustration of all. Canada supplied 4.1 million barrels a "
    "day of crude oil to the United States in 2024, 62 percent of all American oil "
    "imports, and Midwest refineries take about 73 percent of their input from Canada. "
    "The Kansas City Fed declined to estimate who would pay a tariff on that, saying "
    "only that it would be split between Canadian producers, Midwest refiners and "
    "Midwest drivers depending on what each could substitute. In practice the question "
    "never got tested: the 10 percent energy tariff was struck down with the rest of "
    "the emergency measures, and energy is exempt from the August 2026 tariff as well.",
    "L'énergie en est l'illustration la plus nette. Le Canada a fourni 4,1 millions de "
    "barils de pétrole brut par jour aux États-Unis en 2024, soit 62 pour cent de "
    "toutes les importations pétrolières américaines, et les raffineries du Midwest "
    "tirent environ 73 pour cent de leur approvisionnement du Canada. La Fed de Kansas "
    "City a refusé d'estimer qui paierait un tarif là-dessus, se bornant à dire que "
    "ce serait partagé entre producteurs canadiens, raffineurs du Midwest et "
    "automobilistes du Midwest selon ce que chacun pouvait remplacer. En pratique, la "
    "question n'a jamais été mise à l'épreuve : le tarif de 10 pour cent sur l'énergie "
    "a été invalidé avec le reste des mesures d'urgence, et l'énergie est également "
    "exemptée du tarif d'août 2026."))

a.h2(T("What is claimed, and what has been measured",
       "Ce qui est affirmé, et ce qui a été mesuré"))
a.p(T(
    "The United States government has set out its own case, and it deserves to be "
    "read in its own words rather than summarised by someone who disagrees with it. A "
    "White House fact sheet of 20 July 2026 says that tariffs make America wealthier "
    "and stronger, that American manufacturing grew at its fastest rate in four years, "
    "and that trade policy has brought jobs back. On the trade with Canada "
    "specifically it points to American vehicle sales into Canada falling about 22 "
    "percent, or 5.6 billion dollars, and alcohol sales falling about 81 percent, or "
    "582 million dollars. On the smelter that came back to full capacity, the United "
    "States Commerce Department said that producing more aluminium at home reduces "
    "dependence on foreign supply chains.",
    "Le gouvernement des États-Unis a exposé son propre argumentaire, et il mérite "
    "d'être lu dans ses propres mots plutôt que résumé par quelqu'un qui n'est pas "
    "d'accord avec lui. Une fiche d'information de la Maison-Blanche du 20 juillet "
    "2026 affirme que les tarifs rendent l'Amérique plus riche et plus forte, que la "
    "fabrication américaine a connu sa plus forte croissance en quatre ans, et que la "
    "politique commerciale a ramené des emplois. Au sujet du commerce avec le Canada "
    "en particulier, elle relève une baisse d'environ 22 pour cent, soit 5,6 milliards "
    "de dollars, des ventes de véhicules américains au Canada, et une baisse d'environ "
    "81 pour cent, soit 582 millions de dollars, des ventes d'alcool. Au sujet de la "
    "fonderie revenue à pleine capacité, le Département du Commerce des États-Unis a "
    "dit que produire plus d'aluminium au pays réduit la dépendance aux chaînes "
    "d'approvisionnement étrangères."))
a.p(T(
    "Several of those claims are borne out. Customs revenue really did more than "
    "double. The smelter really did come back. Steel output really is up 5.7 percent. "
    "The American goods and services deficit with Canada really did narrow, from 39.4 "
    "billion dollars in 2024 to 27.3 billion in 2025.",
    "Plusieurs de ces affirmations se vérifient. Les recettes douanières ont bel et "
    "bien plus que doublé. La fonderie est bel et bien revenue. La production d'acier "
    "est bel et bien en hausse de 5,7 pour cent. Le déficit américain de biens et "
    "services avec le Canada s'est bel et bien resserré, passant de 39,4 milliards de "
    "dollars en 2024 à 27,3 milliards en 2025."))
a.p(T(
    "Other measurements point the other way over the same period. Manufacturing "
    "employment across the United States is lower, not higher. Primary aluminium "
    "production fell rather than rose. Steel capacity use is still under the 80 "
    "percent the policy names as its own target. About 90 percent of the cost landed "
    "on American buyers. And the Supreme Court ruling has already sent about 100 "
    "billion dollars back out.",
    "D'autres mesures pointent dans l'autre sens sur la même période. L'emploi "
    "manufacturier à l'échelle des États-Unis est plus bas, non plus haut. La "
    "production d'aluminium primaire a reculé au lieu de progresser. Le taux "
    "d'utilisation de l'acier reste sous les 80 pour cent que la politique se donne "
    "elle-même comme cible. Environ 90 pour cent du coût est retombé sur les acheteurs "
    "américains. Et la décision de la Cour suprême a déjà fait ressortir environ 100 "
    "milliards de dollars."))
a.p(T(
    "Both of those paragraphs are true at once, and that is the whole difficulty. A "
    "policy this large does several things at the same time, some of them what it "
    "intended and some of them not. Anyone who can only see one of the two paragraphs "
    "is arguing rather than counting.",
    "Ces deux paragraphes sont vrais en même temps, et c'est là toute la difficulté. "
    "Une politique de cette ampleur fait plusieurs choses à la fois, certaines voulues "
    "et d'autres non. Quiconque ne voit qu'un seul des deux paragraphes est en train "
    "d'argumenter plutôt que de compter."))

a.h2(T("What nobody can tell you", "Ce que personne ne peut vous dire"))
a.p(T(
    "Four things are simply not published, and we would rather say so than invent "
    "them. Nobody knows how many dollars of duty were collected on Canadian goods "
    "specifically, because the United States Treasury does not break its customs "
    "receipts down by country. Nobody has measured the net effect on American gross "
    "domestic product after the fact — every figure you will see is a model "
    "projection. No study has documented American refiners or utilities actually "
    "paying tariff dollars on Canadian crude or electricity. And the effect of the "
    "copper tariff on American prices, production and jobs has not been measured at "
    "all.",
    "Quatre choses ne sont tout simplement pas publiées, et nous préférons le dire "
    "plutôt que de les inventer. Personne ne sait combien de dollars de droits ont été "
    "perçus sur les produits canadiens précisément, parce que le Trésor américain ne "
    "ventile pas ses recettes douanières par pays. Personne n'a mesuré après coup "
    "l'effet net sur le produit intérieur brut américain — tous les chiffres que vous "
    "verrez sont des projections de modèle. Aucune étude n'a documenté de raffineurs "
    "ou de services publics américains payant réellement des droits sur le brut ou "
    "l'électricité du Canada. Et l'effet du tarif sur le cuivre sur les prix, la "
    "production et l'emploi américains n'a pas été mesuré du tout."))

a.h2(T("What to take away", "Ce qu'il faut retenir"))
a.p(T(
    "Where the protection worked, it worked narrowly and it worked as designed: one "
    "smelter, 150 jobs, more steel tonnes, higher steel prices. Where it cost, it cost "
    "broadly and thinly: a little on every household bill, a lot on the factories "
    "that buy metal instead of making it, and a manufacturing workforce 62,000 smaller "
    "than in January 2025 — though nobody has established how much of that fall the "
    "tariffs caused, and the Cato Institute says so plainly. Whether that trade is "
    "worth making is a political judgement, not an arithmetic one, and it belongs to "
    "the people who vote in that country.",
    "Là où la protection a fonctionné, elle a fonctionné de façon étroite et comme "
    "prévu : une fonderie, 150 emplois, plus de tonnes d'acier, des prix de l'acier "
    "plus élevés. Là où elle a coûté, elle a coûté largement et diffusément : un peu "
    "sur chaque facture de ménage, beaucoup sur les usines qui achètent du métal au "
    "lieu d'en fabriquer, et une main-d'œuvre manufacturière plus petite de 62 000 "
    "personnes qu'en janvier 2025 — même si personne n'a établi quelle part de ce "
    "recul les tarifs ont causée, et l'Institut Cato le dit franchement. Savoir si "
    "l'échange en vaut la peine est un jugement politique, non une opération "
    "arithmétique, et il appartient aux gens qui votent dans ce pays."))

a.p(T(
    "What is properly ours to say is the Canadian half. Much of what happens next will "
    "be decided outside Canada, and what is worth taking from two years of numbers is "
    "not resentment but the plain reading: one customer taking three quarters of what "
    "you sell is a wonderful arrangement right up until it is not. That is the argument "
    "for building the ports, opening the provincial borders and finding other buyers — "
    "and it would still be the argument if every tariff came off tomorrow morning.",
    "Ce qui nous revient de dire, c'est la moitié canadienne. Une grande partie de la "
    "suite se décidera hors du Canada, et ce qu'il faut retenir de deux années de "
    "chiffres n'est pas du ressentiment mais une lecture simple : un client "
    "qui prend les trois quarts de ce que vous vendez est un arrangement merveilleux "
    "jusqu'au jour où il ne l'est plus. C'est l'argument pour bâtir les ports, ouvrir "
    "les frontières provinciales et trouver d'autres acheteurs — et ce serait encore "
    "l'argument si tous les tarifs tombaient demain matin."))

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("us-tariffs-and-canada-explained.html",
         T("What the tariffs did to Canada, sector by sector",
           "Ce que les tarifs ont fait au Canada, secteur par secteur")),
    link("how-canada-rebuilds-its-economy.html",
         T("How Canada rebuilds — new customers, old barriers",
           "Comment le Canada se rebâtit — nouveaux clients, vieilles barrières")),
    link("canada-usa-trade-history.html",
         T("Canada and the United States: 170 years of trade, fights and deals",
           "Le Canada et les États-Unis : 170 ans de commerce, de disputes et d'ententes")),
])

a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://www.bea.gov/news/2026/gdp-second-estimate-4th-quarter-and-year-2025",
             T("United States Bureau of Economic Analysis — Gross domestic product, fourth quarter and year 2025",
               "Bureau of Economic Analysis des États-Unis — Produit intérieur brut, quatrième trimestre et année 2025")),
    out_link("https://www.bankofcanada.ca/publications/mpr/mpr-2026-07-15/overview/",
             T("Bank of Canada — Monetary Policy Report, July 2026",
               "Banque du Canada — Rapport sur la politique monétaire, juillet 2026")),
    out_link("https://statcan.gc.ca/en/topics-start/canada-united-states/trade",
             T("Statistics Canada — Focus on Canada and the United States: trade",
               "Statistique Canada — Le Canada et les États-Unis : le commerce")),
    out_link("https://www.piie.com/blogs/realtime-economics/2025/us-tariffs-canada-and-mexico-would-hurt-all-three-economies",
             T("Peterson Institute for International Economics — US tariffs on Canada and Mexico would hurt all three economies",
               "Peterson Institute for International Economics — Les tarifs américains sur le Canada et le Mexique nuiraient aux trois économies")),
    out_link("https://libertystreeteconomics.newyorkfed.org/2026/02/who-is-paying-for-the-2025-u-s-tariffs/",
             T("Federal Reserve Bank of New York — Who is paying for the 2025 US tariffs?",
               "Banque fédérale de réserve de New York — Qui paie les tarifs américains de 2025 ?")),
    out_link("https://www.minneapolisfed.org/article/2026/tariffs-cant-explain-rising-goods-inflation",
             T("Federal Reserve Bank of Minneapolis — Tariffs can't explain rising goods inflation",
               "Banque fédérale de réserve de Minneapolis — Les tarifs n'expliquent pas la hausse des prix des biens")),
    out_link("https://www.stlouisfed.org/on-the-economy/2026/aug/tariff-effects-inflation-stabilize-recent-months",
             T("Federal Reserve Bank of St. Louis — Tariff effects on inflation stabilize",
               "Banque fédérale de réserve de Saint-Louis — Les effets des tarifs sur l'inflation se stabilisent")),
    out_link("https://www.cbo.gov/system/files/2026-08/61983-2026-07-MBR.pdf",
             T("Congressional Budget Office — Monthly Budget Review, July 2026",
               "Bureau du budget du Congrès — Revue budgétaire mensuelle, juillet 2026")),
    out_link("https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-aluminum.pdf",
             T("United States Geological Survey — Mineral Commodity Summaries 2026, aluminium",
               "Service géologique des États-Unis — Sommaires des produits minéraux 2026, aluminium")),
    out_link("https://www.bls.gov/news.release/cpi.nr0.htm",
             T("United States Bureau of Labor Statistics — Consumer Price Index",
               "Bureau of Labor Statistics des États-Unis — Indice des prix à la consommation")),
    out_link("https://www.fas.usda.gov/data/canada-canada-removes-retaliatory-tariffs-usmca-compliant-products",
             T("United States Department of Agriculture — Canada removes retaliatory tariffs",
               "Département de l'Agriculture des États-Unis — Le Canada retire ses contre-tarifs")),
    out_link("https://budgetlab.yale.edu/research/state-us-tariffs",
             T("The Budget Lab at Yale — The state of US tariffs",
               "Le Budget Lab de Yale — L'état des tarifs américains")),
    out_link("https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/",
             T("Tax Foundation — Tariff tracker",
               "Tax Foundation — Suivi des tarifs")),
    out_link("https://www.kansascityfed.org/research/economic-bulletin/canadian-oil-important-for-midwest-gasoline-prices/",
             T("Federal Reserve Bank of Kansas City — Canadian oil and Midwest gasoline prices",
               "Banque fédérale de réserve de Kansas City — Le pétrole canadien et les prix de l'essence dans le Midwest")),
])

a.disclaimer(T(
    "This article is for general information and study. This site is unofficial and "
    "not affiliated with the Government of Canada or the Government of the United "
    "States. Where sources disagree we have said so rather than choosing one; every "
    "source we used is listed above and on our sources page.",
    "Cet article est fourni à titre d'information générale et d'étude. Ce site est non "
    "officiel et n'a aucun lien avec le gouvernement du Canada ni avec celui des "
    "États-Unis. Là où les sources divergent, nous l'avons dit plutôt que d'en choisir "
    "une; toutes nos sources sont énumérées ci-dessus et sur notre page des sources."))

if __name__ == "__main__":
    a.build()
    flush_pairs()
