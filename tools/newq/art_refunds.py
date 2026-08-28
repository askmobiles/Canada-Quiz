#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article 4 — who actually gets the tariff money back.

Sources: the research notes.

Two numbers on this page were deliberately left off because they could not be
confirmed: the size of the goods list covered by the 8 September 2026 Canadian
measures (Al Jazeera reported about 28 billion, Bloomberg about 20, and the
Prime Minister's own remarks gave no figure), and the "95 percent domestically
borne" line often attributed to the Congressional Budget Office, which could
not be found as a sentence in the CBO's own document.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="who-gets-the-tariff-money-back.html",
    section="Trade",
    title=T("Tariff Refunds — Who Actually Gets the Money Back?",
            "Remboursements de tarifs — qui récupère vraiment l'argent ?"),
    desc=T("American courts ordered about 166 billion dollars of tariffs returned. "
           "About 100 billion has gone back — to the companies that filed the import "
           "papers, not to the shoppers who paid the higher prices. How that works, "
           "and what Canada does with its own counter-tariff money.",
           "Les tribunaux américains ont ordonné le remboursement d'environ 166 "
           "milliards de dollars de tarifs. Une centaine de milliards sont repartis — "
           "vers les entreprises qui ont rempli les formulaires d'importation, pas vers "
           "les consommateurs qui ont payé plus cher. Comment cela fonctionne, et ce que "
           "le Canada fait de l'argent de ses propres contre-tarifs."),
    h1=T("\U0001F4B5 A hundred billion dollars went back. Who got it?",
         "\U0001F4B5 Cent milliards de dollars sont repartis. Qui les a reçus ?"),
    hero=T("A tariff is collected at the border from the company bringing the goods in. "
           "So when a court orders it refunded, that company is the one holding the "
           "receipt — and the shopper who paid the higher shelf price is not a party to "
           "the transaction at all.",
           "Un tarif est perçu à la frontière auprès de l'entreprise qui fait entrer la "
           "marchandise. Quand un tribunal en ordonne le remboursement, c'est donc cette "
           "entreprise qui détient le reçu — et le consommateur qui a payé le prix plus "
           "élevé en magasin n'est pas partie à la transaction."),
    checked=T("Last checked 24 August 2026 — this page covers a fast-moving situation",
              "Dernière vérification le 24 août 2026 — cette page traite d'une "
              "situation qui évolue vite"),
)

a.callout(T(
    "<strong>A note on the dollars.</strong> The first half of this page is in American "
    "dollars, because it describes money collected and returned by the United States. "
    "The Canadian half says so where it starts, and is in Canadian dollars from there on.",
    "<strong>Une note sur les dollars.</strong> La première moitié de cette page est en "
    "dollars américains, parce qu'elle décrit de l'argent perçu et remboursé par les "
    "États-Unis. La partie canadienne l'indique au moment où elle commence, et emploie "
    "des dollars canadiens à partir de là."))

# ------------------------------------------------------------------ 1
a.h2(T("The short answer", "La réponse courte"))
a.p(T(
    "The refund cheque goes to the importer of record — the company whose name is on "
    "the customs entry. Most of the money, by value, has gone to large American "
    "retailers, manufacturers and shipping companies. It does not go to the customer who "
    "paid the higher price, and there is no process by which it could.",
    "Le chèque de remboursement va à l'importateur officiel — l'entreprise dont le nom "
    "figure sur la déclaration en douane. L'essentiel de l'argent, en valeur, est allé à "
    "de grands détaillants, fabricants et transporteurs américains. Il ne va pas au client "
    "qui a payé plus cher, et aucun mécanisme ne permettrait qu'il en soit autrement."))
a.p(T(
    "That is not a loophole that somebody forgot to close. It follows from how the tax "
    "is written. American customs law treats the duty as owed by the importer, so the "
    "importer is the person the government owes it back to. Everything between the "
    "importer and the shopper — the wholesale price, the shelf price, the shipping "
    "surcharge — is private contract, and the customs service can see none of it. An "
    "importer may name someone else to receive the payment, but nothing gives a customer "
    "a claim of their own.",
    "Ce n'est pas une faille que quelqu'un aurait oublié de refermer. Cela découle de la "
    "façon dont la taxe est rédigée. Le droit douanier américain considère que le droit "
    "est dû par l'importateur, donc l'importateur est la personne à qui l'État le doit en "
    "retour. Tout ce qui se trouve entre l'importateur et le consommateur — le prix de "
    "gros, le prix en magasin, les frais de transport — relève du contrat privé, et le "
    "service des douanes n'en voit rien. Un importateur peut désigner quelqu'un d'autre "
    "pour recevoir le paiement, mais rien ne donne au client un droit qui lui soit "
    "propre."))

# ------------------------------------------------------------------ 2
a.p(T(
    "How much of the cost actually fell on American households in the first place is a "
    "separate question, and the research on it does not agree. Researchers at the Federal "
    "Reserve Bank of New York put about 90 percent of the 2025 burden on American firms and "
    "their customers. The Congressional Budget Office's mechanism gets to a similar place. "
    "Caroline Freund at the University of California, San Diego, working from "
    "trade-weighted data across the 50 largest American trading partners, found foreign "
    "exporters absorbing 40 to 50 percent, with the largest supplier of a given product "
    "absorbing up to 70 percent. Studies of what reached the shelf are lower again — "
    "around a quarter of the tariff after seven months, with a slower indirect channel "
    "running nine to twelve. So the honest range for "
    "how much American buyers carried runs from about half to nearly all, and where a "
    "particular product sits depends on whether the buyer had anywhere else to go.",
    "Quelle part du coût est réellement retombée sur les ménages américains au départ est "
    "une autre question, et les recherches ne s'accordent pas. Des chercheurs de la Banque "
    "fédérale de réserve de New York attribuent environ 90 pour cent du fardeau de 2025 aux "
    "entreprises américaines et à leurs clients.Le mécanisme décrit par le Bureau du budget du "
    "Congrès aboutit à un résultat semblable. Caroline Freund, de l'Université de "
    "Californie à San Diego, à partir de données pondérées par les échanges pour les 50 "
    "principaux partenaires commerciaux américains, conclut que les exportateurs étrangers "
    "ont absorbé de 40 à 50 pour cent, le principal fournisseur d'un produit donné "
    "absorbant jusqu'à 70 pour cent. Les études sur ce qui s'est rendu en magasin donnent "
    "encore moins — environ le quart du tarif après sept mois, avec un canal indirect plus "
    "lent qui s'étale sur neuf à douze mois. La fourchette "
    "honnête pour la part portée par les acheteurs américains va donc d'environ la moitié "
    "à la quasi-totalité, et la position d'un produit donné dépend de l'existence d'une "
    "autre source d'approvisionnement."))

a.h2(T("How the refund came about", "D'où vient le remboursement"))
a.p(T(
    "On 20 February 2026 the Supreme Court of the United States decided two cases "
    "together and held that the emergency-powers statute the tariffs had been built on "
    "did not authorise them. The vote was six to three. The majority did not address "
    "refunds at all, and the trade courts have had to work out who gets the money back.",
    "Le 20 février 2026, la Cour suprême des États-Unis a tranché deux affaires "
    "ensemble et jugé que la loi sur les pouvoirs d'urgence sur laquelle les tarifs "
    "reposaient ne les autorisait pas. Le vote était de six contre trois. La majorité "
    "n'a pas abordé du tout la question des remboursements, et ce sont les tribunaux du "
    "commerce qui ont dû déterminer qui récupère l'argent."))
a.p(T(
    "The Court of International Trade then ordered the customs service to refund roughly "
    "165 billion dollars across more than 53 million import entries filed by over "
    "330,000 importers — the court's order figure, slightly below the total actually "
    "collected. Interest runs from the day each deposit was made to the day the "
    "entry is settled, at rates set quarterly — five percent on corporate refunds and six "
    "percent on non-corporate ones in the second quarter of 2026.",
    "Le Tribunal du commerce international a ensuite ordonné au service des douanes de "
    "rembourser environ 165 milliards de dollars répartis sur plus de 53 millions de "
    "déclarations d'importation déposées par plus de 330 000 importateurs — le chiffre de "
    "l'ordonnance du tribunal, légèrement inférieur au total réellement perçu. Des intérêts "
    "courent du jour de chaque dépôt jusqu'à la liquidation de la déclaration, à des taux "
    "fixés trimestriellement — cinq pour cent sur les remboursements aux sociétés et six "
    "pour cent sur les autres au deuxième trimestre de 2026."))
a.p(T(
    "One thing to be clear about, because it is widely misunderstood: the ruling did not "
    "end tariffs on Canada. The steel, aluminium and copper tariffs rest on a different "
    "statute and were untouched. Fifty percent remains on the core articles. What was "
    "struck down was one particular legal basis, and the refunds cover only the duties "
    "collected under it.",
    "Un point à clarifier, parce qu'il est souvent mal compris : la décision n'a pas mis "
    "fin aux tarifs visant le Canada. Les tarifs sur l'acier, l'aluminium et le cuivre "
    "reposent sur une autre loi et n'ont pas été touchés. Cinquante pour cent demeure sur "
    "les articles principaux. Ce qui a été invalidé, c'est un fondement juridique "
    "particulier, et les remboursements ne couvrent que les droits perçus sur cette base."))

# ------------------------------------------------------------------ 3
a.h2(T("What has actually been paid back", "Ce qui a réellement été remboursé"))
a.fig(bar_chart(
    T("Collected, accepted and paid — billions of US dollars",
      "Perçu, accepté et versé — en milliards de dollars américains"),
    [(T("Collected under the struck-down authority",
        "Perçu en vertu du pouvoir invalidé"), 166),
     (T("Accepted through the refund portal",
        "Accepté par le portail de remboursement"), 128.7),
     (T("Actually paid out by 31 July 2026",
        "Réellement versé au 31 juillet 2026"), 100)],
    colours=["blue", "purple", "green"]))
a.p(T(
    "The customs service built a new online system for this and opened it in stages "
    "through the spring and summer of 2026. Refunds are not automatic. An importer has to come "
    "forward, upload evidence of its entries and be registered for electronic payment; "
    "an importer that never registers gets nothing. Of the declarations submitted, about "
    "30 percent failed validation, and a further 1.6 billion dollars could not be sent "
    "because the bank details were wrong.",
    "Le service des douanes a créé un nouveau système en ligne pour cela et l'a ouvert "
    "par étapes au printemps et à l'été 2026. Les remboursements ne sont pas automatiques. "
    "L'importateur doit se manifester, téléverser la preuve de ses déclarations et être "
    "inscrit au paiement électronique ; un importateur qui ne s'inscrit jamais ne reçoit "
    "rien. Parmi les déclarations soumises, environ 30 pour cent ont échoué à la "
    "validation, et 1,6 milliard de dollars supplémentaires n'ont pu être envoyés parce "
    "que les coordonnées bancaires étaient erronées."))
a.p(T(
    "About 11.4 billion dollars is stuck on a separate question — entries that were "
    "already finally settled before the ruling — pending a jurisdictional appeal. One law "
    "firm puts the contested exposure on finally-settled entries at potentially over 30 "
    "billion. Separately, the government's notices of appeal filed in June 2026 argue that "
    "the refund orders should benefit only the importers who actually sued, rather than "
    "everyone. Neither appeal is decided.",
    "Environ 11,4 milliards de dollars sont bloqués sur une question distincte — des "
    "déclarations déjà définitivement liquidées avant la décision — en attente d'un appel "
    "sur la compétence. Un cabinet d'avocats chiffre l'exposition contestée sur les "
    "déclarations définitivement liquidées à potentiellement plus de 30 milliards. Par "
    "ailleurs, les avis d'appel déposés par le gouvernement en juin 2026 soutiennent que "
    "les ordonnances de remboursement ne devraient profiter qu'aux importateurs qui ont "
    "eux-mêmes poursuivi, et non à tout le monde. Ni l'un ni l'autre appel n'est tranché."))

# ------------------------------------------------------------------ 4
a.h2(T("Where the money landed", "Où l'argent a abouti"))
a.p(T(
    "American public companies report these refunds in their quarterly results, which is "
    "how the amounts are known. These are the figures disclosed in quarterly results "
    "between April and August 2026.",
    "Les sociétés américaines cotées déclarent ces remboursements dans leurs résultats "
    "trimestriels, et c'est ainsi que les montants sont connus. Voici les chiffres "
    "divulgués dans les résultats trimestriels entre avril et août 2026."))
a.table(
    [T("Company", "Entreprise"), T("Tariff refund reported", "Remboursement déclaré")],
    [["Walmart", "$2.9B"],
     ["Apple", "$2.2B"],
     ["Ford", "$1.3B"],
     ["Target", "$994M"],
     ["FedEx", "$800M"],
     ["Home Depot", "$730M"],
     ["Nike", T("$684M (receivable; $986M expected in total)",
                "684 M$ (à recevoir ; 986 M$ attendus au total)")],
     ["Amazon", "$640M"],
     ["General Motors", "$500M"],
     ["Stellantis", T("€400M (about $467M)", "400 M€ (environ 467 M$)")],
     ["TJX", "$331M"],
     ["Ross", "$253M"],
     ["Lowe's", "$80M"],
     [T("Ace Hardware", "Ace Hardware"), "$11.8M"]],
    label=T("Tariff refunds reported by company — scroll sideways to see all of it",
            "Remboursements de tarifs déclarés par entreprise — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "The size of these numbers relative to the businesses is worth pausing on. At Target, "
    "1.65 dollars of the quarter's 4.11 dollars of earnings per share came from tariff "
    "refunds — forty percent of the profit — and the company raised its guidance for the "
    "year. At Apple the refunds added eleven cents to earnings per share. At PepsiCo they "
    "were worth about a full percentage point of the year's earnings growth. At "
    "Caterpillar they pushed the operating margin above guidance.",
    "L'ampleur de ces chiffres par rapport aux entreprises mérite qu'on s'y arrête. Chez "
    "Target, 1,65 $ des 4,11 $ de bénéfice par action du trimestre provenaient de "
    "remboursements de tarifs — quarante pour cent du profit — et l'entreprise a relevé "
    "ses prévisions annuelles. Chez Apple, les remboursements ont ajouté onze cents au "
    "bénéfice par action. Chez PepsiCo, ils valaient environ un point de pourcentage "
    "complet de la croissance des bénéfices de l'année. Chez Caterpillar, ils ont poussé "
    "la marge d'exploitation au-dessus des prévisions."))
a.p(T(
    "The money is also concentrated. Approved refunds covered about 60 percent of the "
    "total owed but only about 30 percent of the import entries — which the Cato "
    "Institute reads as a strong sign that the money has gone mainly to large importers, "
    "in big, high-value shipments. A Minnesota baby-products company that "
    "had halved its staff and lost half its revenue received 50,000 dollars, against "
    "140,000 dollars of credit-card debt it had taken on. Its owner said it did not "
    "recover her losses.",
    "L'argent est aussi concentré. Les remboursements approuvés couvraient environ 60 "
    "pour cent du total dû mais seulement environ 30 pour cent des déclarations "
    "d'importation — ce que le Cato Institute interprète comme un fort indice que l'argent "
    "est allé surtout à de grands importateurs, dans de grosses expéditions de forte "
    "valeur. Une entreprise de produits pour bébés du Minnesota, qui avait réduit "
    "son personnel de moitié et perdu la moitié de son chiffre d'affaires, a reçu 50 000 "
    "dollars, contre 140 000 dollars de dettes de carte de crédit contractées. Sa "
    "propriétaire a dit que cela ne compensait pas ses pertes."))

# ------------------------------------------------------------------ 5
a.h2(T("What the companies say they will do with it",
       "Ce que les entreprises disent vouloir en faire"))
a.p(T(
    "One company is sending it back across the board. FedEx began returning refunds to its "
    "customers in August 2026. Amazon says it passes money back in the narrower set of "
    "circumstances where it had charged a specific import fee to a specific customer.",
    "Une entreprise le renvoie de façon générale. FedEx a commencé à rembourser ses clients "
    "en août 2026. Amazon dit remettre l'argent dans l'ensemble plus restreint de cas où "
    "elle avait facturé des frais d'importation précis à un client précis."))
a.p(T(
    "The rest describe other uses. Walmart says the intent was to deploy much of it back "
    "into price. Target says it will invest in price. Home Depot says it will offset "
    "other rising costs, including energy. Lowe's says the same. TJX is putting 112 "
    "million of its 331 million into employee bonuses. Apple says it will reinvest in the "
    "United States. None of those are refunds to customers, and none of them are hidden — "
    "the companies said so plainly.",
    "Les autres décrivent d'autres usages. Walmart dit que l'intention était d'en "
    "réinjecter une bonne part dans les prix. Target dit qu'elle investira dans les prix. "
    "Home Depot dit compenser d'autres hausses de coûts, dont l'énergie. Lowe's dit la "
    "même chose. TJX consacre 112 millions de ses 331 millions à des primes aux employés. "
    "Apple dit qu'elle réinvestira aux États-Unis. Aucune de ces réponses n'est un "
    "remboursement aux clients, et aucune n'est cachée — les entreprises l'ont dit "
    "clairement."))
a.p(T(
    "A tariff consultant quoted by CNN estimates that 15 to 20 percent of the refunds "
    "will reach consumers, through lower prices or direct rebates. That is one "
    "practitioner's estimate, not a measurement, and it should be read as one.",
    "Un consultant en tarifs cité par CNN estime que 15 à 20 pour cent des "
    "remboursements atteindront les consommateurs, par des baisses de prix ou des "
    "remises directes. C'est l'estimation d'un praticien, pas une mesure, et il faut la "
    "lire comme telle."))
a.p(T(
    "There is also litigation. A proposed class action filed in Oregon in May 2026 argues "
    "that a company that raised prices to cover a tariff and then collected the refund "
    "has recovered the same cost twice. Similar suits have been filed against other large "
    "retailers. Trade lawyers quoted in the American press describe the legal ground as "
    "shaky. None has been decided.",
    "Il y a aussi des poursuites. Un recours collectif proposé déposé en Oregon en mai "
    "2026 soutient qu'une entreprise ayant augmenté ses prix pour couvrir un tarif, puis "
    "encaissé le remboursement, a récupéré deux fois le même coût. Des poursuites "
    "semblables visent d'autres grands détaillants. Des avocats spécialisés en commerce "
    "cités dans la presse américaine décrivent le fondement juridique comme fragile. "
    "Aucune n'a été tranchée."))

# ------------------------------------------------------------------ 6
a.h2(T("Do prices come back down when a tariff comes off?",
       "Les prix redescendent-ils quand un tarif est retiré ?"))
a.p(T(
    "This is the question underneath the refund question, and it has been studied for "
    "thirty-five years under the name economists gave it in 1991: rockets and feathers. "
    "Prices go up like a rocket and come down like a feather.",
    "C'est la question qui se cache derrière celle des remboursements, et elle est "
    "étudiée depuis trente-cinq ans sous le nom que les économistes lui ont donné en "
    "1991 : fusées et plumes. Les prix montent comme une fusée et redescendent comme une "
    "plume."))
a.p(T(
    "The broadest measurement is Sam Peltzman's 2000 study of 242 products — 77 consumer "
    "goods and 165 producer goods. He found the asymmetry in more than two of every three "
    "markets he examined. On average the immediate response to a cost increase was at "
    "least twice the response to a cost decrease of the same size, and that difference was "
    "sustained for at least five to eight months. Later work for the American justice "
    "department found the same shape in fuel retailing: five days after a spot price "
    "change, stations had passed through 46 percent of an increase but only 24 percent of "
    "a decrease.",
    "La mesure la plus large est l'étude de Sam Peltzman de 2000 portant sur 242 produits "
    "— 77 biens de consommation et 165 biens de production. Il a trouvé l'asymétrie dans "
    "plus de deux marchés sur trois. En moyenne, la réaction immédiate à une hausse de "
    "coût était au moins le double de la réaction à une baisse de même ampleur, et cet "
    "écart se maintenait pendant au moins cinq à huit mois. Des travaux ultérieurs réalisés "
    "pour le ministère de la Justice américain ont trouvé la même forme dans la vente au "
    "détail de carburant : cinq jours après une variation du prix au comptant, les stations "
    "avaient répercuté 46 pour cent d'une hausse mais seulement 24 pour cent d'une "
    "baisse."))
a.p(T(
    "Days after the February 2026 ruling, Goldman Sachs told clients it would not "
    "expect companies to lower prices in response to tariff reductions nearly as quickly "
    "as they had raised them. That is the same finding, said in advance and in plain "
    "English by a market participant.",
    "Quelques jours après la décision de février 2026, Goldman Sachs a écrit à ses clients "
    "qu'elle ne s'attendait pas à ce que les entreprises baissent leurs prix en réponse "
    "aux réductions de tarifs aussi vite qu'elles les avaient augmentés. C'est le même "
    "constat, formulé à l'avance et en clair par un acteur du marché."))
a.p(T(
    "And the measurement since agrees. Five months after the ruling, the American "
    "consumer price index for July 2026 had core goods — the category most exposed to "
    "tariffs — still rising, at 0.8 percent over the year. Appliances were the one "
    "broadly tariff-exposed category showing an annual decline, and even there the "
    "monthly figure was up. Researchers at the Federal Reserve Bank of St. Louis describe "
    "what happened as the tariff effect on inflation levelling off, or even declining "
    "slightly — not reversing.",
    "Et les mesures depuis lors vont dans le même sens. Cinq mois après la décision, "
    "l'indice américain des prix à la consommation de juillet 2026 montrait des biens de "
    "base — la catégorie la plus exposée aux tarifs — encore en hausse, de 0,8 pour cent "
    "sur un an. Les électroménagers étaient la seule catégorie largement exposée aux "
    "tarifs à afficher une baisse annuelle, et même là le chiffre mensuel était en "
    "hausse. Des chercheurs de la Banque fédérale de réserve de Saint-Louis décrivent ce "
    "qui s'est passé comme un plafonnement de l'effet des tarifs sur l'inflation, voire un "
    "léger recul — non comme un renversement."))
a.callout(T(
    "<strong>The closest thing to an experiment, and what it does and does not show.</strong> "
    "When the United States put a safeguard tariff on washing machines in 2018, the price "
    "of washers rose about 12 percent — and the price of dryers, which were not tariffed at "
    "all, rose by the same amount. A pro-tariff research group has shown, from the "
    "published price index, that prices then fell through 2019 and 2020. But that happened "
    "while the tariff was still in force, as manufacturers built assembly plants inside the "
    "United States. So the episode tells us a great deal about what a tariff does going on, "
    "and almost nothing about what happens when one comes off. No peer-reviewed study has "
    "examined what happened to those prices when the safeguard finally expired in 2023.",
    "<strong>Ce qui ressemble le plus à une expérience, et ce que cela montre ou "
    "non.</strong> Quand les États-Unis ont imposé un tarif de sauvegarde sur les laveuses "
    "en 2018, leur prix a monté d'environ 12 pour cent — et celui des sécheuses, qui "
    "n'étaient pas visées, a monté d'autant. Un groupe de recherche favorable aux tarifs a "
    "montré, à partir de l'indice des prix publié, que les prix ont ensuite baissé en 2019 "
    "et 2020. Mais cela s'est produit alors que le tarif était toujours en vigueur, pendant "
    "que les fabricants construisaient des usines d'assemblage aux États-Unis. L'épisode "
    "nous apprend donc beaucoup sur l'effet d'un tarif qu'on impose, et presque rien sur ce "
    "qui se passe quand on le retire. Aucune étude évaluée par les pairs n'a examiné ce "
    "qu'il est advenu de ces prix lorsque la sauvegarde a finalement expiré en 2023."))

# ------------------------------------------------------------------ 7
a.h2(T("The Canadian half — and it came out differently",
       "La moitié canadienne — et le résultat a été différent"))
a.p(T(
    "Everything from here is in Canadian dollars. Canada put counter-tariffs on American "
    "goods in March and April 2025: 25 percent on about 30 billion dollars of consumer "
    "goods, then on a further 29.8 billion made up of 12.6 billion of steel, 3 billion of "
    "aluminium and 14.2 billion of tools, computers, servers, monitors and sports "
    "equipment, then on vehicles. On 1 September 2025 the 30 billion consumer tranche and "
    "the 14.2 billion tranche were both repealed. The steel, aluminium and automotive "
    "measures have been in force continuously since and were extended in June 2026.",
    "Tout ce qui suit est en dollars canadiens. Le Canada a imposé des contre-tarifs sur "
    "des produits américains en mars et avril 2025 : 25 pour cent sur environ 30 "
    "milliards de dollars de biens de consommation, puis sur 29,8 milliards "
    "supplémentaires composés de 12,6 milliards d'acier, 3 milliards d'aluminium et 14,2 "
    "milliards d'outils, d'ordinateurs, de serveurs, d'écrans et d'articles de sport, puis "
    "sur les véhicules. Le 1er septembre 2025, la tranche de 30 milliards visant les biens "
    "de consommation et celle de 14,2 milliards ont toutes deux été abrogées. Les mesures "
    "sur l'acier, l'aluminium et l'automobile sont en vigueur sans interruption depuis, et "
    "ont été prolongées en juin 2026."))
a.p(T(
    "That repeal created something rare: a natural experiment on Canadian soil, with a "
    "central bank watching. Bank of Canada researchers measured it. About one quarter of "
    "the 25 percent counter-tariff reached consumer prices, adding roughly 0.3 percentage "
    "points to inflation. Then, when the tariffs came off on 1 September 2025, prices fell "
    "back quickly toward those of comparable goods that had never been tariffed. For "
    "groceries and appliances the reversal was nearly complete within three months.",
    "Cette abrogation a créé quelque chose de rare : une expérience naturelle en sol "
    "canadien, sous l'œil d'une banque centrale. Des chercheurs de la Banque du Canada "
    "l'ont mesurée. Environ le quart du contre-tarif de 25 pour cent s'est rendu aux prix "
    "à la consommation, ajoutant à peu près 0,3 point de pourcentage à l'inflation. Puis, "
    "quand les tarifs ont été retirés le 1er septembre 2025, les prix sont redescendus "
    "rapidement vers ceux de biens comparables qui n'avaient jamais été tarifés. Pour "
    "l'épicerie et les électroménagers, le retour était presque complet en trois mois."))
a.p(T(
    "So the feather fell faster here than the literature would predict. Two things are "
    "worth saying about that and neither is a boast. The Canadian counter-tariffs were "
    "smaller and shorter-lived than the American ones, and they were removed cleanly on a "
    "single date rather than partially unwound through a court process. Both make a "
    "reversal easier to see and easier to make.",
    "La plume est donc tombée plus vite ici que la littérature ne le laissait prévoir. "
    "Deux choses méritent d'être dites, et aucune n'est un motif de fierté. Les "
    "contre-tarifs canadiens étaient plus petits et plus courts que les tarifs "
    "américains, et ils ont été retirés d'un seul coup à une date unique plutôt que "
    "démêlés partiellement par un processus judiciaire. Les deux rendent un retour en "
    "arrière plus facile à voir et plus facile à réaliser."))

# ------------------------------------------------------------------ 8
a.h2(T("Where Canada's counter-tariff money goes",
       "Où va l'argent des contre-tarifs canadiens"))
a.fig(bar_chart(
    T("Canadian counter-tariff revenue — billions of Canadian dollars",
      "Recettes des contre-tarifs canadiens — en milliards de dollars canadiens"),
    [(T("Projected in a 2025 election platform",
        "Projeté dans une plateforme électorale de 2025"), 20.0),
     (T("Forecast in Budget 2025", "Prévu dans le budget de 2025"), 4.4),
     (T("Reported by the Department of Finance to CBC News",
        "Communiqué par le ministère des Finances à CBC News"), 3.0)],
    colours=["purple", "blue", "green"]))
a.p(T(
    "The Department of Finance told CBC News that the counter-tariffs collected about 3 "
    "billion dollars before most of them were withdrawn, and that this figure is already "
    "net of amounts collected and then given back to affected industries. It is a "
    "departmental statement rather than a published table. What is published: total "
    "customs duties for the 2025-26 fiscal year came in at 10.24 billion against 6.21 "
    "billion the year before, an increase of 65 percent that the department attributes to "
    "the countermeasures.",
    "Le ministère des Finances a indiqué à CBC News que les contre-tarifs ont rapporté "
    "environ 3 milliards de dollars avant que la plupart ne soient retirés, et que ce "
    "chiffre est déjà net des sommes perçues puis restituées aux industries touchées. "
    "C'est une déclaration ministérielle, non un tableau publié. Ce qui est publié : le "
    "total des droits de douane pour l'exercice 2025-2026 s'est établi à 10,24 milliards "
    "contre 6,21 milliards l'année précédente, une hausse de 65 pour cent que le ministère "
    "attribue aux contre-mesures."))
a.h3(T("Is the money set aside for the sectors that were hit?",
       "L'argent est-il réservé aux secteurs touchés ?"))
a.p(T(
    "Not in law, and this is the honest distinction. Canada's counter-tariffs are "
    "surtaxes made by order under the Customs Tariff and collected by the border agency "
    "as customs duties. Under the Financial Administration Act all public money is "
    "deposited to the credit of the Receiver General — the Consolidated Revenue Fund. "
    "Setting revenue aside for a purpose requires a statute that says so, and no such "
    "statute or special-purpose account exists for this money. The surtax orders "
    "themselves contain no allocation provision.",
    "Pas en droit, et c'est là la distinction honnête. Les contre-tarifs canadiens sont "
    "des surtaxes établies par décret en vertu du Tarif des douanes et perçues par "
    "l'agence frontalière comme des droits de douane. Selon la Loi sur la gestion des "
    "finances publiques, tous les fonds publics sont déposés au crédit du receveur "
    "général — le Trésor. Réserver des recettes à une fin exige une loi qui le prévoit, et "
    "aucune loi ni aucun compte à fin déterminée n'existe pour cet argent. Les décrets de "
    "surtaxe eux-mêmes ne contiennent aucune disposition d'affectation."))
a.p(T(
    "There is one explicit commitment on the record. On 3 April 2025, announcing the "
    "counter-tariff on vehicles, the Prime Minister said that every single dollar raised "
    "from those tariffs would go directly to support Canadian auto workers. That sentence "
    "is about the auto measure specifically. The four main Department of Finance "
    "counter-tariff announcements and Budget 2025 contain no equivalent statement, and "
    "Budget 2025 books the expected tariff revenue and the support programs as separate "
    "items with no stated link.",
    "Il existe un engagement explicite au dossier. Le 3 avril 2025, en annonçant le "
    "contre-tarif sur les véhicules, le premier ministre a déclaré que chaque dollar "
    "perçu grâce à ces tarifs irait directement au soutien des travailleurs canadiens de "
    "l'automobile. Cette phrase vise la mesure automobile en particulier. Les quatre "
    "principales annonces de contre-tarifs du ministère des Finances et le budget de 2025 "
    "ne contiennent aucune déclaration équivalente, et le budget de 2025 inscrit les "
    "recettes tarifaires attendues et les programmes de soutien comme des postes distincts "
    "sans lien énoncé."))
a.p(T(
    "There is also a mechanism that does return counter-tariff money to the party that "
    "paid it: remission. A remission order refunds the surtax to the importer. Broad "
    "remission for steel goods used in Canadian manufacturing and in food and beverage "
    "processing ended on 1 February 2026, except for motor-vehicle and aerospace uses, and "
    "remission for aluminium imports and for public health and security goods expired on 1 "
    "July 2026. Motor-vehicle remission continues. That is the Canadian mirror of the "
    "American process described above — same logic, same recipient, much smaller scale.",
    "Il existe aussi un mécanisme qui rend l'argent des contre-tarifs à celui qui l'a "
    "payé : la remise. Un décret de remise rembourse la surtaxe à l'importateur. La remise "
    "générale pour les produits d'acier utilisés dans la fabrication canadienne et dans la "
    "transformation des aliments et des boissons a pris fin le 1er février 2026, sauf pour "
    "les usages automobiles et aérospatiaux, et la remise pour les importations "
    "d'aluminium et les biens de santé et de sécurité publiques a expiré le 1er juillet "
    "2026. La remise automobile se poursuit. C'est le miroir canadien du processus "
    "américain décrit plus haut — même logique, même bénéficiaire, échelle beaucoup plus "
    "petite."))

a.h3(T("What was announced for the affected sectors",
       "Ce qui a été annoncé pour les secteurs touchés"))
a.p(T(
    "The support is real and it is much larger than the counter-tariffs raised, which is "
    "possible precisely because the two are not linked. These are the named measures, "
    "with the dates they were announced. They should not be added together: several are "
    "top-ups of earlier ones, and they mix grants with loans and loan guarantees, which "
    "are not the same kind of money.",
    "Le soutien est réel et il dépasse largement ce que les contre-tarifs ont rapporté, "
    "ce qui est possible précisément parce que les deux ne sont pas liés. Voici les "
    "mesures nommées, avec leur date d'annonce. Il ne faut pas les additionner : "
    "plusieurs sont des bonifications de mesures antérieures, et elles mêlent "
    "subventions, prêts et garanties de prêt, qui ne sont pas de l'argent de même nature."))
a.table(
    [T("Announced", "Annoncé"), T("Measure", "Mesure"), T("Amount", "Montant")],
    [[T("7 March 2025", "7 mars 2025"),
      T("Trade Impact Program, through Export Development Canada",
        "Programme d'impact commercial, par Exportation et développement Canada"),
      T("$5B over two years", "5 G$ sur deux ans")],
     [T("7 March 2025", "7 mars 2025"),
      T("Business Development Bank of Canada loans",
        "Prêts de la Banque de développement du Canada"), "$500M"],
     [T("7 March 2025", "7 mars 2025"),
      T("Farm Credit Canada financing", "Financement de Financement agricole Canada"),
      "$1B"],
     [T("3 April 2025", "3 avril 2025"),
      T("Tax and GST/HST deferrals for businesses",
        "Reports d'impôt et de TPS/TVH pour les entreprises"),
      T("up to $40B in liquidity", "jusqu'à 40 G$ de liquidités")],
     [T("15 April 2025", "15 avril 2025"),
      T("Large Enterprise Tariff Loan facility established",
        "Création de la facilité de prêt tarifaire pour grandes entreprises"),
      T("facility later set at $10B", "facilité fixée plus tard à 10 G$")],
     [T("4 November 2025", "4 novembre 2025"),
      T("Strategic Response Fund", "Fonds de réponse stratégique"),
      T("$5B over six years", "5 G$ sur six ans")],
     [T("4 November 2025", "4 novembre 2025"),
      T("Regional Tariff Response Initiative",
        "Initiative régionale de réponse aux tarifs"),
      T("up to $1B over three years", "jusqu'à 1 G$ sur trois ans")],
     [T("4 November 2025", "4 novembre 2025"),
      T("Employment Insurance income supports",
        "Soutiens du revenu de l'assurance-emploi"),
      T("$3.7B over three years", "3,7 G$ sur trois ans")],
     [T("4 November 2025", "4 novembre 2025"),
      T("Employment Insurance Work-Sharing flexibilities",
        "Assouplissements du Travail partagé de l'assurance-emploi"),
      T("$370.5M over five years", "370,5 M$ sur cinq ans")],
     [T("4 November 2025", "4 novembre 2025"),
      T("Agriculture, fish and seafood measures",
        "Mesures pour l'agriculture, le poisson et les fruits de mer"),
      T("more than $639M over five years", "plus de 639 M$ sur cinq ans")],
     [T("26 November 2025", "26 novembre 2025"),
      T("Steel — Strategic Response Fund allocation",
        "Acier — affectation du Fonds de réponse stratégique"), "$1B"],
     [T("26 November 2025", "26 novembre 2025"),
      T("Softwood lumber — loan guarantees ($700M, plus a $500M top-up), tariff loans "
        "($500M), diversification ($500M) and Work-Sharing grants ($102.7M)",
        "Bois d'œuvre — garanties de prêt (700 M$, plus une bonification de 500 M$), prêts "
        "tarifaires (500 M$), diversification (500 M$) et subventions de Travail partagé "
        "(102,7 M$)"),
      T("five separate instruments", "cinq instruments distincts")],
     [T("4 May 2026", "4 mai 2026"),
      T("Business Development Bank program for metals and forestry",
        "Programme de la BDC pour les métaux et la foresterie"), "$1B"],
     [T("4 May 2026", "4 mai 2026"),
      T("Regional Tariff Response Initiative — additional funding",
        "Initiative régionale de réponse aux tarifs — financement supplémentaire"), "$500M"],
     [T("22 August 2026", "22 août 2026"),
      T("Package for workers and businesses hurt by the tariffs",
        "Ensemble pour les travailleurs et les entreprises touchés par les tarifs"),
      "$25B"]],
    label=T("Announced Canadian tariff-response support — scroll sideways to see all of it",
            "Soutien canadien annoncé en réponse aux tarifs — faites défiler "
            "latéralement pour tout voir"))
a.p(T(
    "The most recent of those was announced on 22 August 2026, after trade talks between "
    "the two countries ended without an agreement. Alongside it, new Canadian counter-"
    "tariffs were announced for the Tuesday after Labour Day — 8 September 2026 — "
    "concentrated in steel, dairy, appliances, agricultural equipment, pulp and paper and "
    "electronics, and including products already subject to American tariffs imposed under "
    "sections 232 and 338. The detailed list and the rates had not been published when "
    "this page was written.",
    "La plus récente a été annoncée le 22 août 2026, après l'échec des pourparlers "
    "commerciaux entre les deux pays. En parallèle, de nouveaux contre-tarifs canadiens "
    "ont été annoncés pour le mardi suivant la fête du Travail — le 8 septembre 2026 — "
    "concentrés dans l'acier, les produits laitiers, les électroménagers, la machinerie "
    "agricole, les pâtes et papiers et l'électronique, et visant aussi des produits déjà "
    "soumis à des tarifs américains imposés en vertu des articles 232 et 338. La liste "
    "détaillée et les taux n'étaient pas publiés au moment d'écrire cette page."))

# ------------------------------------------------------------------ 9
a.h2(T("What is not known", "Ce qu'on ne sait pas"))
a.p(T(
    "How much of the announced Canadian support has actually been paid out. No government "
    "source found publishes disbursement figures for any of these programs — only "
    "announced and committed amounts. How many firms were approved, how many workers were "
    "covered, how many jobs were kept: none of that is published either.",
    "Quelle part du soutien canadien annoncé a réellement été versée. Aucune source "
    "gouvernementale trouvée ne publie de chiffres de décaissement pour ces programmes — "
    "seulement des montants annoncés et engagés. Combien d'entreprises ont été "
    "approuvées, combien de travailleurs ont été couverts, combien d'emplois ont été "
    "conservés : rien de cela n'est publié non plus."))
a.p(T(
    "Nor has any independent body assessed it. The Parliamentary Budget Officer has not "
    "costed the counter-tariff revenue or the support programs. The Auditor General has "
    "not audited them. What does exist is the Bank of Canada research on who bore the "
    "counter-tariffs, and Export Development Canada's account of the damage: 32,161 "
    "manufacturing jobs lost between January 2025 and "
    "January 2026, and the American share of Canada's goods exports down from 76 percent "
    "in 2024 to 72 percent in 2025.",
    "Aucun organisme indépendant ne l'a évalué non plus. Le directeur parlementaire du "
    "budget n'a chiffré ni les recettes des contre-tarifs ni les programmes de soutien. "
    "La vérificatrice générale ne les a pas vérifiés. Ce qui existe, ce sont les travaux "
    "de la Banque du Canada sur qui a porté les contre-tarifs, et le bilan des dommages "
    "dressé par Exportation et développement Canada : 32 161 emplois manufacturiers perdus "
    "entre janvier 2025 et janvier 2026, et "
    "la part américaine des exportations canadiennes de biens passée de 76 pour cent en "
    "2024 à 72 pour cent en 2025."))

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("did-us-tariffs-on-canada-work.html",
         T("When a tariff goes on, who actually gains?",
           "Quand un tarif est imposé, qui y gagne vraiment ?")),
    link("what-canada-and-the-usa-sell-each-other.html",
         T("What Canada sells America, and what America sells Canada",
           "Ce que le Canada vend à l'Amérique, et ce que l'Amérique vend au Canada")),
    link("us-tariffs-and-canada-explained.html",
         T("What the tariffs did to Canada, sector by sector",
           "Ce que les tarifs ont fait au Canada, secteur par secteur")),
])

a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://www.supplychaindive.com/news/cbp-has-paid-100b-in-ieepa-tariff-refunds/827257/",
             T("Supply Chain Dive, reporting US Customs and Border Protection — 100 billion dollars paid in refunds",
               "Supply Chain Dive, citant le service américain des douanes — 100 milliards de dollars remboursés")),
    out_link("https://www.skadden.com/insights/publications/2026/03/tariff-refund-mechanism-takes-shape",
             T("Skadden — the tariff refund mechanism takes shape, March 2026",
               "Skadden — le mécanisme de remboursement des tarifs prend forme, mars 2026")),
    out_link("https://www.hklaw.com/en/insights/publications/2026/06/ieepa-tariff-refund-update-government-appeals",
             T("Holland & Knight — tariff refund update, government appeals, June 2026",
               "Holland & Knight — mise à jour sur les remboursements, appels du gouvernement, juin 2026")),
    out_link("https://www.bdo.com/insights/tax/ieepa-tariff-refunds-frequently-asked-questions",
             T("BDO — tariff refunds, frequently asked questions",
               "BDO — remboursements de tarifs, foire aux questions")),
    out_link("https://www.federalregister.gov/documents/2026/05/18/2026-09871/quarterly-irs-interest-rates-used-in-calculating-interest-on-overdue-accounts-and-refunds-of-customs",
             T("United States Federal Register — quarterly interest rates on customs refunds, May 2026",
               "Federal Register des États-Unis — taux d'intérêt trimestriels sur les remboursements de douane, mai 2026")),
    out_link("https://cepr.org/voxeu/columns/foreign-exporters-absorbed-nearly-half-2025-us-tariff-shock",
             T("Caroline Freund, CEPR — foreign exporters absorbed nearly half the 2025 tariff shock",
               "Caroline Freund, CEPR — les exportateurs étrangers ont absorbé près de la moitié du choc tarifaire de 2025")),
    out_link("https://www.nber.org/papers/w35561",
             T("Amiti, Heise and Weinstein — tariff pass-through to consumer prices, NBER working paper, 2026",
               "Amiti, Heise et Weinstein — la répercussion des tarifs sur les prix à la consommation, document de travail du NBER, 2026")),
    out_link("https://kesq.com/money/cnn-business-consumer/2026/08/22/tariffs-raised-prices-you-paid-but-most-businesses-wont-be-passing-tariffs-refunds-back-to-you/",
             T("CNN Business — most businesses will not pass tariff refunds back to customers, August 2026",
               "CNN Business — la plupart des entreprises ne remettront pas les remboursements aux clients, août 2026")),
    out_link("https://www.forbes.com/sites/alisondurkee/2026/08/21/americans-top-retailers-are-getting-billions-in-tariff-refunds-including-walmart-target-but-many-consumers-still-arent/",
             T("Forbes — America's top retailers are getting billions in tariff refunds, August 2026",
               "Forbes — les grands détaillants américains reçoivent des milliards en remboursements de tarifs, août 2026")),
    out_link("https://fortune.com/article/fortune-500-companies-billions-tariff-refunds-customers-08-19-2026/",
             T("Fortune — Fortune 500 companies and billions in tariff refunds, August 2026",
               "Fortune — les entreprises du Fortune 500 et des milliards en remboursements de tarifs, août 2026")),
    out_link("https://www.cbsnews.com/news/how-to-get-a-tariff-refund-ieepa/",
             T("CBS News — how tariff refunds work, and why consumers cannot claim one, August 2026",
               "CBS News — le fonctionnement des remboursements de tarifs, et pourquoi les consommateurs ne peuvent en réclamer, août 2026")),
    out_link("https://finance.yahoo.com/news/goldman-sachs-says-u-consumers-181838897.html",
             T("Goldman Sachs, via Yahoo Finance — on whether companies will lower prices, February 2026",
               "Goldman Sachs, via Yahoo Finance — les entreprises baisseront-elles leurs prix ?, février 2026")),
    out_link("https://ideas.repec.org/a/eee/eneeco/v13y1991i3p211-218.html",
             T("Robert W. Bacon — Rockets and feathers, Energy Economics, 1991",
               "Robert W. Bacon — Rockets and feathers, Energy Economics, 1991")),
    out_link("https://www.cbc.ca/news/politics/canada-collected-3-billion-u-s-counter-tariffs-9.6961968",
             T("CBC News — Canada collected about 3 billion dollars from counter-tariffs",
               "CBC News — le Canada a perçu environ 3 milliards de dollars grâce aux contre-tarifs")),
    out_link("https://laws-lois.justice.gc.ca/eng/acts/f-11/fulltext.html",
             T("Financial Administration Act — section 21, money received for a special purpose",
               "Loi sur la gestion des finances publiques — article 21, fonds reçus à une fin déterminée")),
    out_link("https://www.cbsa-asfc.gc.ca/publications/dm-md/d16/d16-1-1-eng.html",
             T("Canada Border Services Agency — Memorandum D16-1-1, application and collection of a surtax",
               "Agence des services frontaliers du Canada — Mémorandum D16-1-1, application et perception d'une surtaxe")),
    out_link("https://www.law.cornell.edu/uscode/text/19/1505",
             T("United States Code, Title 19 section 1505 — liquidation, refunds and interest",
               "Code des États-Unis, titre 19 article 1505 — liquidation, remboursements et intérêts")),
    out_link("https://www.ecfr.gov/current/title-19/chapter-I/part-24/section-24.36",
             T("United States Code of Federal Regulations, 19 CFR 24.36 — refunds of excess duties",
               "Code des règlements fédéraux des États-Unis, 19 CFR 24.36 — remboursement des droits excédentaires")),
    out_link("https://www.cbo.gov/publication/62704",
             T("Congressional Budget Office — the budgetary effects of tariff policy, July 2026",
               "Bureau du budget du Congrès — effets budgétaires de la politique tarifaire, juillet 2026")),
    out_link("https://www.cato.org/blog/ieepa-refunds-update-good-progress-still-ways-go",
             T("Cato Institute — refunds update, July 2026",
               "Cato Institute — mise à jour sur les remboursements, juillet 2026")),
    out_link("https://www.conference-board.org/research/policy-backgrounders/tariff-refunds-update",
             T("The Conference Board — tariff refunds update, August 2026",
               "The Conference Board — mise à jour sur les remboursements de tarifs, août 2026")),
    out_link("https://www.bls.gov/news.release/pdf/cpi.pdf",
             T("United States Bureau of Labor Statistics — Consumer Price Index, July 2026",
               "Bureau of Labor Statistics des États-Unis — Indice des prix à la consommation, juillet 2026")),
    out_link("https://www.stlouisfed.org/on-the-economy/2026/aug/tariff-effects-inflation-stabilize-recent-months",
             T("Federal Reserve Bank of St. Louis — tariff effects on inflation stabilise",
               "Banque fédérale de réserve de Saint-Louis — les effets des tarifs sur l'inflation se stabilisent")),
    out_link("https://libertystreeteconomics.newyorkfed.org/2026/07/more-tariff-pass-through-is-in-the-pipeline/",
             T("Federal Reserve Bank of New York — more tariff pass-through is in the pipeline",
               "Banque fédérale de réserve de New York — d'autres répercussions tarifaires sont à venir")),
    out_link("https://www.journals.uchicago.edu/doi/abs/10.1086/262126",
             T("Sam Peltzman — Prices Rise Faster than They Fall, Journal of Political Economy, 2000",
               "Sam Peltzman — Prices Rise Faster than They Fall, Journal of Political Economy, 2000")),
    out_link("https://www.justice.gov/sites/default/files/atr/legacy/2012/11/02/288447.pdf",
             T("Marc Remer — An Empirical Investigation of the Determinants of Asymmetric Pricing",
               "Marc Remer — An Empirical Investigation of the Determinants of Asymmetric Pricing")),
    out_link("https://www.aeaweb.org/articles?id=10.1257%2Faer.20190611",
             T("Flaaen, Hortacsu and Tintelnot — the price effects of the washing machine tariffs, American Economic Review, 2020",
               "Flaaen, Hortacsu et Tintelnot — les effets de prix des tarifs sur les laveuses, American Economic Review, 2020")),
    out_link("https://www.bankofcanada.ca/2026/05/sparks-at-bank-article-2026-13/",
             T("Bank of Canada — how Canada's counter-tariffs impacted consumer prices, May 2026",
               "Banque du Canada — l'effet des contre-tarifs canadiens sur les prix à la consommation, mai 2026")),
    out_link("https://www.canada.ca/en/department-finance/services/publications/fiscal-monitor/2026/03.html",
             T("Department of Finance Canada — The Fiscal Monitor, March 2026",
               "Ministère des Finances du Canada — La revue financière, mars 2026")),
    out_link("https://budget.canada.ca/2025/report-rapport/chap2-en.html",
             T("Government of Canada — Budget 2025, chapter 2",
               "Gouvernement du Canada — Budget de 2025, chapitre 2")),
    out_link("https://laws-lois.justice.gc.ca/eng/acts/f-11/fulltext.html",
             T("Financial Administration Act — section 17, public money and the Consolidated Revenue Fund",
               "Loi sur la gestion des finances publiques — article 17, fonds publics et Trésor")),
    out_link("https://gazette.gc.ca/rp-pr/p2/2025/2025-09-10/html/sor-dors181-eng.html",
             T("Canada Gazette — order repealing certain surtax orders, August 2025",
               "Gazette du Canada — décret abrogeant certains décrets de surtaxe, août 2025")),
    out_link("https://www.pm.gc.ca/en/news/news-releases/2025/04/03/canada-announces-new-countermeasures-response-tariffs-from-united-states",
             T("Prime Minister of Canada — new countermeasures, 3 April 2025",
               "Premier ministre du Canada — nouvelles contre-mesures, 3 avril 2025")),
    out_link("https://www.pm.gc.ca/en/news/speeches/2026/08/22/prime-minister-carney-delivers-remarks-canada-us-trade-negotiations",
             T("Prime Minister of Canada — remarks on Canada-US trade negotiations, 22 August 2026",
               "Premier ministre du Canada — allocution sur les négociations commerciales Canada-États-Unis, 22 août 2026")),
    out_link("https://www.edc.ca/en/article/us-tariffs-canada-trade-impact.html",
             T("Export Development Canada — one year later: how US tariffs reshaped Canada-US trade",
               "Exportation et développement Canada — un an plus tard : comment les tarifs américains ont remodelé le commerce Canada-États-Unis")),
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
