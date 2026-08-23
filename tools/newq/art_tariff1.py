#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article 1 of 3 — what the US tariffs did to Canada, sector by sector.

Sources are in the project note research/tariffs-canada-usa-20260822.md.
Rules followed here, deliberately:
  * merchandise figures are never mixed with goods-and-services figures
  * where two official sources disagree, both are printed and named
  * nothing is blamed on anyone; the page reports what happened
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, link, flush_pairs

a = Article(
    slug="us-tariffs-and-canada-explained.html",
    section="Trade",
    title=T("What the Tariffs Did to Canada — Sector by Sector",
            "Ce que les tarifs ont fait au Canada — secteur par secteur"),
    desc=T("What the 2025 and 2026 United States tariffs actually did to Canadian "
           "exports and jobs, sector by sector, with the official numbers and the "
           "places the numbers disagree.",
           "Ce que les tarifs américains de 2025 et 2026 ont réellement fait aux "
           "exportations et aux emplois canadiens, secteur par secteur, avec les "
           "chiffres officiels et les endroits où ils divergent."),
    h1=T("\U0001F4C9 What the tariffs did to Canada, sector by sector",
         "\U0001F4C9 Ce que les tarifs ont fait au Canada, secteur par secteur"),
    hero=T("Steel exports fell by half. Copper went up 40 percent. The two facts are "
           "in the same year, in the same country, under the same tariffs. Here is "
           "the whole picture, with the official numbers and without the guessing.",
           "Les exportations d'acier ont chuté de moitié. Le cuivre a augmenté de "
           "40 pour cent. Les deux faits datent de la même année, dans le même pays, "
           "sous les mêmes tarifs. Voici le portrait complet, avec les chiffres "
           "officiels et sans devinettes."),
    checked=T("Last checked 22 August 2026 — this page covers a fast-moving situation",
              "Dernière vérification le 22 août 2026 — cette page traite d'une "
              "situation qui évolue vite"),
)

a.callout(T(
    "<strong>Where things stand today.</strong> Talks between Canada and the United "
    "States ended without a deal in the early hours of Saturday 22 August 2026, and a "
    "United States tariff of 50 percent came into force the same morning. It covers "
    "roughly 20 billion American dollars of Canadian goods — American and Canadian "
    "news outlets have given figures from 20 to 28 billion, so treat the exact number "
    "as unsettled — which is about 5 percent of everything Canada sells to the United "
    "States. It was made under Section 338 of the Tariff Act of 1930, a provision no "
    "president had used before. Vehicles, alcohol, dairy, "
    "furniture, clothing, cosmetics and hockey equipment are on the list. Energy, "
    "potash, fish and critical minerals are exempt. The Government of Canada has said "
    "it will match it dollar for dollar; the list of what Canada will tax had not been "
    "published when this page was written.",
    "<strong>Où en sont les choses aujourd'hui.</strong> Les pourparlers entre le "
    "Canada et les États-Unis se sont terminés sans entente aux petites heures du "
    "samedi 22 août 2026, et un tarif américain de 50 pour cent est entré en vigueur "
    "le matin même. Il vise environ 20 milliards de dollars américains de produits "
    "canadiens — les médias américains et canadiens donnent des chiffres allant de 20 "
    "à 28 milliards, alors considérez le montant exact comme incertain — soit environ "
    "5 pour cent de tout ce que le Canada vend aux États-Unis. Il a été pris en vertu "
    "de l'article 338 de la Loi tarifaire de 1930, une disposition qu'aucun président "
    "n'avait utilisée auparavant. Les véhicules, l'alcool, les produits laitiers, les meubles, les "
    "vêtements, les cosmétiques et l'équipement de hockey figurent sur la liste. "
    "L'énergie, la potasse, le poisson et les minéraux critiques en sont exemptés. Le "
    "gouvernement du Canada a dit qu'il répliquerait dollar pour dollar; la liste de "
    "ce que le Canada taxera n'était pas publiée au moment d'écrire cette page."))

a.callout(T(
    "<strong>How is this page written?</strong> This is a Canadian site and this page "
    "is written for Canadians — what happened here, to industries and towns here. It "
    "is not written against anyone. Tariffs are a decision governments make, Canada "
    "included, and this page looks at what the numbers did afterwards rather than at "
    "who deserves the blame. Canadian figures are in Canadian dollars, because that is "
    "how Statistics Canada and Global Affairs Canada publish them; American figures "
    "are marked where they appear. Mixing the two silently is one of the commonest "
    "ways a trade story goes wrong.",
    "<strong>Comment cette page est-elle écrite ?</strong> Ceci est un site canadien et "
    "cette page est écrite pour les Canadiens — ce qui s'est passé ici, pour des "
    "industries et des villes d'ici. Elle n'est écrite contre personne. Les tarifs "
    "sont une décision que prennent les gouvernements, le Canada compris, et cette "
    "page regarde ce que les chiffres ont donné ensuite plutôt que de chercher un "
    "coupable. Les chiffres canadiens sont en dollars canadiens, parce que c'est ainsi "
    "que Statistique Canada et Affaires mondiales Canada les publient; les chiffres "
    "américains sont indiqués là où ils apparaissent. Mélanger les deux en silence est "
    "l'une des façons les plus courantes de rater un reportage sur le commerce."))

a.h2(T("The short answer", "La réponse courte"))
a.p(T(
    "Canadian exports to the United States fell hard in 2025 and have been climbing "
    "back through 2026. The share of Canadian goods going south dropped from about "
    "76 percent to about 69 and a half percent — the lowest in decades. The damage "
    "was not spread evenly. A few industries were hit very hard indeed, most of the "
    "economy barely felt it directly, and one industry actually grew.",
    "Les exportations canadiennes vers les États-Unis ont fortement chuté en 2025 et "
    "remontent depuis le début de 2026. La part des produits canadiens qui prennent "
    "la route du sud est passée d'environ 76 pour cent à environ 69,5 pour cent — le "
    "creux de plusieurs décennies. Les dégâts n'ont pas été répartis également. "
    "Quelques industries ont été très durement touchées, la majeure partie de "
    "l'économie l'a à peine senti directement, et une industrie a même grandi."))
a.p(T(
    "The Bank of Canada put a size on it in April 2026: the industries actually hit "
    "by the tariffs are about 1 percent of what Canada produces and about 1 percent "
    "of the people who work — but about 15 percent of what Canada exports. That is "
    "the shape of the thing. A small number of towns and industries carried almost "
    "all of the pain.",
    "La Banque du Canada en a chiffré l'ampleur en avril 2026 : les industries "
    "réellement touchées par les tarifs représentent environ 1 pour cent de ce que "
    "le Canada produit et environ 1 pour cent des personnes qui travaillent — mais "
    "environ 15 pour cent de ce que le Canada exporte. Voilà la forme de la chose. "
    "Un petit nombre de villes et d'industries ont porté presque toute la douleur."))

a.h2(T("How we got here, in dates", "Comment nous en sommes arrivés là, en dates"))
a.table(
    [T("Date", "Date"), T("What happened", "Ce qui s'est passé")],
    [
        [T("4 Mar 2025", "4 mars 2025"),
         T("25 percent on Canadian goods that do not comply with CUSMA, 10 percent on energy. Canada replies on 30 billion dollars of American goods.",
           "25 pour cent sur les produits canadiens non conformes à l'ACEUM, 10 pour cent sur l'énergie. Le Canada réplique sur 30 milliards de dollars de produits américains.")],
        [T("12 Mar 2025", "12 mars 2025"),
         T("25 percent on steel and aluminium. Canada replies on 12.6 billion of steel, 3 billion of aluminium and 14.2 billion of other goods.",
           "25 pour cent sur l'acier et l'aluminium. Le Canada réplique sur 12,6 milliards d'acier, 3 milliards d'aluminium et 14,2 milliards d'autres produits.")],
        [T("3 Apr 2025", "3 avril 2025"),
         T("25 percent on vehicles and parts. Canada matches it on 9 April.",
           "25 pour cent sur les véhicules et les pièces. Le Canada fait de même le 9 avril.")],
        [T("4 Jun 2025", "4 juin 2025"),
         T("Steel and aluminium doubled from 25 to 50 percent.",
           "L'acier et l'aluminium doublent, de 25 à 50 pour cent.")],
        [T("1 Aug 2025", "1 août 2025"),
         T("50 percent on semi-finished copper. Raw ore, cathode and scrap are exempt — that exemption turns out to matter enormously.",
           "50 pour cent sur le cuivre semi-fini. Le minerai brut, la cathode et la ferraille sont exemptés — cette exemption s'avérera énorme.")],
        [T("1 Aug 2025", "1 août 2025"),
         T("The general rate on Canadian goods outside CUSMA rises from 25 to 35 percent.",
           "Le taux général sur les produits canadiens hors ACEUM passe de 25 à 35 pour cent.")],
        [T("1 Sep 2025", "1 sept. 2025"),
         T("Canada lifts its counter-tariffs on about 44 billion dollars of American goods, keeping only steel, aluminium and autos.",
           "Le Canada lève ses contre-tarifs sur environ 44 milliards de dollars de produits américains, ne gardant que l'acier, l'aluminium et l'automobile.")],
        [T("14 Oct 2025", "14 oct. 2025"),
         T("10 percent on softwood lumber, 25 percent on cabinets and furniture.",
           "10 pour cent sur le bois d'œuvre, 25 pour cent sur les armoires et les meubles.")],
        [T("20 Feb 2026", "20 févr. 2026"),
         T("The United States Supreme Court strikes down the emergency-powers tariffs. About 100 billion American dollars is refunded to importers over the months that follow. The steel, aluminium, auto, lumber and copper tariffs are untouched, because they rest on a different law.",
           "La Cour suprême des États-Unis invalide les tarifs pris en vertu des pouvoirs d'urgence. Environ 100 milliards de dollars américains sont remboursés aux importateurs au cours des mois suivants. Les tarifs sur l'acier, l'aluminium, l'automobile, le bois et le cuivre demeurent, car ils reposent sur une autre loi.")],
        [T("22 Aug 2026", "22 août 2026"),
         T("Talks fail. A 50 percent tariff takes effect on about 20 billion American dollars of Canadian goods. This one is written so that CUSMA does not shield goods from it.",
           "Les pourparlers échouent. Un tarif de 50 pour cent frappe environ 20 milliards de dollars américains de produits canadiens. Celui-ci est rédigé de façon que l'ACEUM ne protège pas les marchandises.")],
    ])

a.h2(T("The number that surprises people", "Le chiffre qui surprend"))
a.p(T(
    "The headline rates were 25, then 35, then 50 percent. The rate the United States "
    "actually collected on Canadian goods, averaged across everything Canada sold, "
    "went from 0.1 percent in 2024 to 2.4 percent in 2025 and 3.2 percent in February "
    "2026. Those figures come from United States Census Bureau trade data.",
    "Les taux annoncés étaient de 25, puis 35, puis 50 pour cent. Le taux que les "
    "États-Unis ont réellement perçu sur les produits canadiens, en moyenne sur tout "
    "ce que le Canada a vendu, est passé de 0,1 pour cent en 2024 à 2,4 pour cent en "
    "2025 et 3,2 pour cent en février 2026. Ces chiffres proviennent des données "
    "commerciales du Bureau du recensement des États-Unis."))
a.p(T(
    "The reason is CUSMA, the free trade agreement. About 85 percent of what Canada "
    "sells to the United States qualifies under it and crosses free. Canada still "
    "faces the lowest average tariff of any major American trading partner, at 5.2 "
    "percent, according to the federal Spring Economic Update of April 2026. That is "
    "why the country as a whole stalled rather than crashed — and also why the "
    "industries outside that shield were hit so hard.",
    "La raison, c'est l'ACEUM, l'accord de libre-échange. Environ 85 pour cent de ce "
    "que le Canada vend aux États-Unis y est admissible et traverse la frontière sans "
    "droits. Le Canada fait toujours face au tarif moyen le plus bas de tous les "
    "grands partenaires commerciaux américains, soit 5,2 pour cent, selon la Mise à "
    "jour économique du printemps 2026. Voilà pourquoi le pays dans son ensemble a "
    "stagné plutôt que de s'effondrer — et aussi pourquoi les industries hors de ce "
    "bouclier ont été si durement frappées."))

a.fig(bar_chart(
    T("Share of Canadian goods exports going to the United States, per cent",
      "Part des exportations canadiennes de marchandises vers les États-Unis, en pour cent"),
    [(T("2024", "2024"), 75.9),
     (T("2025", "2025"), 71.7),
     (T("June 2026", "juin 2026"), 69.5)],
    unit="%", colours=["blue", "blue", "red"]),
    T("Statistics Canada and Global Affairs Canada. The 2026 figure is for June alone.",
      "Statistique Canada et Affaires mondiales Canada. Le chiffre de 2026 vise le seul mois de juin."))

a.h2(T("Sector by sector", "Secteur par secteur"))
a.p(T(
    "These are the Bank of Canada's own findings after one full year of tariffs, "
    "published on 29 April 2026, with the 2026 figures from Global Affairs Canada "
    "added beside them.",
    "Voici les constats de la Banque du Canada après une année complète de tarifs, "
    "publiés le 29 avril 2026, auxquels s'ajoutent les chiffres de 2026 d'Affaires "
    "mondiales Canada."))
a.table(
    [T("Industry", "Industrie"), T("What happened", "Ce qui s'est passé")],
    [
        [T("Steel", "Acier"),
         T("The worst hit of all. Exports fell by half. Algoma Steel in Sault Ste. Marie issued 1,000 layoff notices — about a third of its workforce — effective 23 March 2026.",
           "Le plus durement touché. Les exportations ont chuté de moitié. Algoma Steel, à Sault-Sainte-Marie, a envoyé 1 000 avis de licenciement — environ le tiers de son personnel — en vigueur le 23 mars 2026.")],
        [T("Aluminium", "Aluminium"),
         T("Down 50 percent against 2024 at the low point in July 2025, then more than half of that loss won back. But the recovered sales went to Europe at thinner profit margins, so the tonnes came back before the money did.",
           "En baisse de 50 pour cent par rapport à 2024 au creux de juillet 2025, puis plus de la moitié de cette perte récupérée. Mais les ventes retrouvées sont parties vers l'Europe à des marges plus minces : les tonnes sont revenues avant l'argent.")],
        [T("Vehicles and parts", "Véhicules et pièces"),
         T("Slightly below 2024 by the spring of 2026, and down 10.7 percent again in the first half of 2026. Employment held up better than expected. General Motors cut the third shift at Oshawa from 2 February 2026 — the company counted about 500 jobs, the union Unifor counted more than 1,000 once suppliers were included.",
           "Légèrement sous le niveau de 2024 au printemps 2026, puis en baisse de 10,7 pour cent au premier semestre de 2026. L'emploi a mieux tenu que prévu. General Motors a supprimé le troisième quart de travail à Oshawa à partir du 2 février 2026 — l'entreprise comptait environ 500 emplois, le syndicat Unifor plus de 1 000 en incluant les fournisseurs.")],
        [T("Softwood lumber", "Bois d'œuvre"),
         T("About 20 percent below 2024 by February 2026. In the first half of 2026 the volume sold to the United States fell 13 percent and the value fell 29 percent, because the price fell too.",
           "Environ 20 pour cent sous le niveau de 2024 en février 2026. Au premier semestre de 2026, le volume vendu aux États-Unis a baissé de 13 pour cent et la valeur de 29 pour cent, parce que le prix a aussi chuté.")],
        [T("Copper", "Cuivre"),
         T("Up 40 percent above its 2024 average, despite a 50 percent tariff. The tariff covers pipe, wire, rod and sheet; it does not cover ore, concentrate, cathode or scrap, and the industry moved towards the lines that were not taxed. Separately, Statistics Canada recorded copper ore and concentrate exports at a record 934 million dollars in June 2026, on higher shipments to Japan, China, Finland and South Korea.",
           "En hausse de 40 pour cent au-dessus de sa moyenne de 2024, malgré un tarif de 50 pour cent. Le tarif vise les tuyaux, les fils, les barres et les tôles; il ne vise ni le minerai, ni le concentré, ni la cathode, ni la ferraille, et l'industrie s'est tournée vers les produits non taxés. Par ailleurs, Statistique Canada a enregistré des exportations de minerai et de concentré de cuivre à un record de 934 millions de dollars en juin 2026, grâce à des livraisons accrues vers le Japon, la Chine, la Finlande et la Corée du Sud.")],
        [T("Energy", "Énergie"),
         T("Never really tariffed. The 10 percent energy tariff came under the emergency powers the Supreme Court struck down, and energy is exempt from the August 2026 measure. Energy exports are up 31.4 percent so far in 2026. Canada sold 126.1 billion dollars of crude oil, 15.5 billion of refined products, 12.5 billion of natural gas and 3.3 billion of electricity to the United States in 2025.",
           "Jamais vraiment tarifée. Le tarif de 10 pour cent sur l'énergie relevait des pouvoirs d'urgence invalidés par la Cour suprême, et l'énergie est exemptée de la mesure d'août 2026. Les exportations d'énergie sont en hausse de 31,4 pour cent depuis le début de 2026. Le Canada a vendu aux États-Unis 126,1 milliards de dollars de pétrole brut, 15,5 milliards de produits raffinés, 12,5 milliards de gaz naturel et 3,3 milliards d'électricité en 2025.")],
    ])

a.callout(T(
    "<strong>One thing worth keeping straight.</strong> Canada's canola, pork and pea "
    "growers had a hard two years as well, but that came from Chinese tariffs, not "
    "American ones. China put 100 percent on canola meal and oil in March 2025, and "
    "from August 2025 canola seed faced about 85 percent all in — a 75.8 percent "
    "anti-dumping deposit on top of the standard duty. Much of that was unwound by an "
    "agreement announced on 16 January 2026, although the 100 percent tariff on canola "
    "oil is still there. It is a separate story and it belongs in a separate column.",
    "<strong>Une chose à ne pas confondre.</strong> Les producteurs canadiens de "
    "canola, de porc et de pois ont eux aussi vécu deux années difficiles, mais cela "
    "venait des tarifs chinois, non américains. La Chine a imposé 100 pour cent sur le "
    "tourteau et l'huile de canola en mars 2025, et à partir d'août 2025 la graine de "
    "canola faisait face à environ 85 pour cent au total — un dépôt antidumping de "
    "75,8 pour cent s'ajoutant au droit habituel. L'essentiel a été dénoué par une "
    "entente annoncée le 16 janvier 2026, même si le tarif de 100 pour cent sur "
    "l'huile de canola demeure. C'est une autre histoire, et elle appartient à une "
    "autre colonne."))

a.h2(T("Jobs", "Les emplois"))
a.p(T(
    "Manufacturing is where this shows up. Statistics Canada's payroll survey counted "
    "1.5 million manufacturing employees in December 2025, down 40,600 in a year, and "
    "Ontario alone lost 27,200 of them. The Labour Force Survey, which is a different "
    "count on a wider base, shows manufacturing employment down 61,000 from its "
    "January 2025 peak, a fall of 3.2 percent — a decline Statistics Canada describes "
    "as coinciding with a period of tariff-related uncertainty for the sector. Note "
    "the careful wording: coinciding, not caused by.",
    "C'est dans la fabrication que cela se voit. L'enquête sur la rémunération de "
    "Statistique Canada comptait 1,5 million de salariés en fabrication en décembre "
    "2025, soit 40 600 de moins en un an, et l'Ontario à lui seul en a perdu 27 200. "
    "L'Enquête sur la population active, un dénombrement différent sur une base plus "
    "large, montre un recul de 61 000 emplois manufacturiers depuis le sommet de "
    "janvier 2025, une baisse de 3,2 pour cent — un recul que Statistique Canada "
    "décrit comme coïncidant avec une période d'incertitude liée aux tarifs pour le "
    "secteur. Notez la formulation prudente : coïncidant, non causé par."))
a.p(T(
    "The national unemployment rate tells a gentler story than the headlines did. It "
    "was 6.4 percent before the tariffs, peaked at 7.1 percent in August and September "
    "2025, and was back to 6.4 percent in July 2026.",
    "Le taux de chômage national raconte une histoire plus douce que les manchettes. "
    "Il était de 6,4 pour cent avant les tarifs, a culminé à 7,1 pour cent en août et "
    "septembre 2025, et était revenu à 6,4 pour cent en juillet 2026."))
a.p(T(
    "The Institute for Research on Public Policy identified the communities where more "
    "than 5 percent of the workforce is in a tariff-exposed industry, and those are "
    "the places where a single plant decision changes a town: Fort McMurray and Cold "
    "Lake in Alberta, Fort Nelson in British Columbia, Ingersoll, Windsor and Sault "
    "Ste. Marie in Ontario, and Sept-Îles in Quebec.",
    "L'Institut de recherche en politiques publiques a repéré les collectivités où "
    "plus de 5 pour cent de la main-d'œuvre travaille dans une industrie exposée aux "
    "tarifs, et ce sont les endroits où une seule décision d'usine change une ville : "
    "Fort McMurray et Cold Lake en Alberta, Fort Nelson en Colombie-Britannique, "
    "Ingersoll, Windsor et Sault-Sainte-Marie en Ontario, et Sept-Îles au Québec."))

a.h2(T("The economy as a whole", "L'économie dans son ensemble"))
a.p(T(
    "Real gross domestic product fell 0.2 percent in the last quarter of 2025 and was "
    "flat in the first quarter of 2026. The Bank of Canada's own summary in July 2026 "
    "was that the level of gross domestic product was roughly unchanged from the first "
    "quarter of 2025 to the first quarter of 2026 — a full year of standing still.",
    "Le produit intérieur brut réel a reculé de 0,2 pour cent au dernier trimestre de "
    "2025 et n'a pas bougé au premier trimestre de 2026. Le résumé de la Banque du "
    "Canada en juillet 2026 était que le niveau du produit intérieur brut était à peu "
    "près inchangé entre le premier trimestre de 2025 et le premier trimestre de "
    "2026 — une année entière de surplace."))
a.p(T(
    "Was that a recession? Statistics Canada never said so, and the federal Spring "
    "Economic Update said Canada avoided one and grew 1.7 percent in 2025. Some "
    "commentators called it a technical recession on an annualised basis. The honest "
    "description is that the economy stalled rather than shrank.",
    "Était-ce une récession ? Statistique Canada ne l'a jamais dit, et la Mise à jour "
    "économique du printemps a affirmé que le Canada l'avait évitée et avait crû de "
    "1,7 pour cent en 2025. Certains commentateurs ont parlé d'une récession technique "
    "sur une base annualisée. La description honnête est que l'économie a stagné "
    "plutôt que reculé."))

a.h2(T("And then it started coming back", "Puis c'est reparti"))
a.p(T(
    "This is the part that gets left out. Exports to the United States are up 4.6 "
    "percent so far in 2026, and June was the fifth month in a row that they rose. "
    "Canada's trade surplus with the United States was 10 billion dollars in June 2026.",
    "C'est la partie qu'on oublie. Les exportations vers les États-Unis sont en hausse "
    "de 4,6 pour cent depuis le début de 2026, et juin a été le cinquième mois de "
    "hausse consécutif. L'excédent commercial du Canada avec les États-Unis s'est "
    "établi à 10 milliards de dollars en juin 2026."))
a.p(T(
    "So the fair way to describe the last two years is a sharp shock in 2025 followed "
    "by a partial recovery in 2026, with a handful of industries and towns still "
    "carrying the damage. What the tariff that took effect on 22 August 2026 does to "
    "that recovery is not yet known, and anyone who tells you otherwise is guessing.",
    "La façon juste de décrire les deux dernières années est donc : un choc brutal en "
    "2025, suivi d'une reprise partielle en 2026, avec une poignée d'industries et de "
    "villes qui portent encore les dégâts. Ce que le tarif entré en vigueur le 22 août "
    "2026 fera à cette reprise n'est pas encore connu, et quiconque prétend le "
    "contraire devine."))

a.h2(T("Read next", "À lire ensuite"))
a.ul([
    link("did-us-tariffs-on-canada-work.html",
         T("When a tariff goes on, who actually gains?",
           "Quand un tarif est imposé, qui y gagne vraiment ?")),
    link("how-canada-rebuilds-its-economy.html",
         T("How Canada rebuilds — new customers, old barriers",
           "Comment le Canada se rebâtit — nouveaux clients, vieilles barrières")),
    link("canada-usa-trade-history.html",
         T("Canada and the United States: 170 years of trade, fights and deals",
           "Le Canada et les États-Unis : 170 ans de commerce, de disputes et d'ententes")),
])

a.sources(T("Where this came from", "D'où viennent ces chiffres"), [
    out_link("https://www150.statcan.gc.ca/n1/daily-quotidien/260804/dq260804a-eng.htm",
             T("Statistics Canada — Canadian international merchandise trade, June 2026",
               "Statistique Canada — Commerce international de marchandises du Canada, juin 2026")),
    out_link("https://www.bankofcanada.ca/publications/mpr/mpr-2026-04-29/in-focus-2/",
             T("Bank of Canada — One year later: assessing the impact of US trade restrictions",
               "Banque du Canada — Un an plus tard : évaluation des restrictions commerciales américaines")),
    out_link("https://international.canada.ca/en/global-affairs/corporate/reports/chief-economist/monthly/2026-06",
             T("Global Affairs Canada — Monthly trade report, June 2026",
               "Affaires mondiales Canada — Rapport mensuel sur le commerce, juin 2026")),
    out_link("https://www.statcan.gc.ca/o1/en/plus/9099-manufacturing-labour-2025-losses-down-line-amid-trade-headwinds",
             T("Statistics Canada — Manufacturing labour in 2025",
               "Statistique Canada — La main-d'œuvre manufacturière en 2025")),
    out_link("https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2026/market-snapshot-overview-of-2025-canada-us-energy-trade.html",
             T("Canada Energy Regulator — Overview of 2025 Canada-US energy trade",
               "Régie de l'énergie du Canada — Aperçu du commerce énergétique Canada-États-Unis en 2025")),
    out_link("https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs.html",
             T("Department of Finance Canada — Canada's response to US tariffs",
               "Ministère des Finances Canada — La réponse du Canada aux tarifs américains")),
    out_link("https://irpp.org/research-studies/reducing-canada-vulnerability-to-us-tariffs/",
             T("Institute for Research on Public Policy — Reducing Canada's vulnerability to US tariffs",
               "Institut de recherche en politiques publiques — Réduire la vulnérabilité du Canada aux tarifs américains")),
])

a.disclaimer(T(
    "This article is for general information and study. This site is unofficial and "
    "not affiliated with the Government of Canada. Trade figures are revised as new "
    "data arrives; every source we used is listed above and on our sources page.",
    "Cet article est fourni à titre d'information générale et d'étude. Ce site est non "
    "officiel et n'a aucun lien avec le gouvernement du Canada. Les données "
    "commerciales sont révisées à mesure que de nouveaux chiffres paraissent; toutes "
    "nos sources sont énumérées ci-dessus et sur notre page des sources."))

if __name__ == "__main__":
    a.build()
    flush_pairs()
