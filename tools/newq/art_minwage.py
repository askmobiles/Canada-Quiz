#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Article — minimum wage in Canada: why each province sets its own, and what
happens when it rises.

Sources: the three research notes in the private project —
  research/minimum-wage-rates-and-jurisdiction-20260828.md
  research/minimum-wage-compression-evidence-20260828.md
  research/minimum-wage-who-gains-who-loses-20260828.md

WHAT THIS PAGE DELIBERATELY DOES NOT DO
---------------------------------------
Minimum wage is one of the most politicised topics in Canadian economics and
both camps overclaim. Every one of these was avoided on purpose:

  * No verdict on whether minimum wage increases are good or bad. The page
    reports what has been measured and names what is disputed.
  * The Bank of Canada's 60,000 figure NEVER appears without its 30,000-140,000
    range AND its finding that total labour income would rise. Stripping those
    is the single most common misuse of that source.
  * Economists are NOT presented as agreeing. Neumark and Shirley's own line —
    that economists disagree about what the literature even says — is quoted.
  * The 2018 jump from 6.5% to 10.4% of employees at minimum wage is labelled
    as a policy artifact of Ontario's increase, not as economic deterioration.
  * No "for every $1 raise a worker keeps $X" figure, because no Canadian
    source computes it for minimum wage increases specifically.
  * The 2017 FAO of Ontario job-loss estimate is NOT used — it could not be
    verified against the FAO document itself.
  * The relative-versus-absolute distinction is stated in both directions and
    left standing, because that is what the data supports. The middle did not
    lose purchasing power; it lost distance from the floor. Resolving that
    either way would be editorialising.
  * Think tanks are named with their orientation attached, in both directions.

The constitutional quotations are limited to the statute text, which was read
directly. Haldane's words in Snider and Beetz J.'s in Montcalm are NOT quoted,
because the law reports could not be read directly — the holdings are described
instead.

NOTE ON DATES IN THE TABLE: no <sup> markup. T() refuses a pair whose two
languages carry different tag counts, and "1er" needs no tag anyway.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artlib import Article, T, bar_chart, out_link, flush_pairs

a = Article(
    slug="minimum-wage-in-canada-explained.html",
    section="Money",
    title=T("Minimum Wage in Canada — Why Every Province Sets Its Own",
            "Le salaire minimum au Canada — pourquoi chaque province fixe le sien"),
    desc=T("Canada has fourteen minimum wages, not one, and they move to fourteen "
           "different formulas. Here is why the constitution puts them there, what "
           "happened to Canadian pay after the big increases, and what the evidence "
           "does and does not settle.",
           "Le Canada compte quatorze salaires minimums, et non un seul, qui suivent "
           "quatorze formules différentes. Voici pourquoi la Constitution en décide "
           "ainsi, ce qui est arrivé à la rémunération au Canada après les fortes "
           "hausses, et ce que les données tranchent ou ne tranchent pas."),
    h1=T("💰 Minimum wage in Canada, explained",
         "💰 Le salaire minimum au Canada, expliqué"),
    hero=T("Fourteen governments set fourteen rates using fourteen different rules. "
           "One has not moved since 2018. What follows is what the official record "
           "shows about how the system works and what happens when the floor rises.",
           "Quatorze gouvernements fixent quatorze taux selon quatorze règles "
           "différentes. L'un d'eux n'a pas bougé depuis 2018. Voici ce que les "
           "documents officiels révèlent sur le fonctionnement du système et sur ce "
           "qui se produit quand le plancher monte."),
    checked=T("Last checked 28 August 2026 — rates change on fixed dates through the "
              "year and several will move before this page is checked again",
              "Dernière vérification le 28 août 2026 — les taux changent à dates fixes "
              "au cours de l'année et plusieurs bougeront avant la prochaine "
              "vérification de cette page"),
)

# ------------------------------------------------------------------ 1
a.h2(T("There is no such thing as the Canadian minimum wage",
       "Le salaire minimum canadien n'existe pas"))
a.p(T(
    "There are fourteen of them. Ten provinces, three territories, and one federal rate "
    "that covers a small slice of workers. On the same day in the same country, the "
    "lowest legal hourly pay ranges from $15.00 to $19.75.",
    "Il y en a quatorze. Dix provinces, trois territoires et un taux fédéral qui vise "
    "une petite tranche de travailleurs. Le même jour, dans le même pays, la "
    "rémunération horaire légale la plus basse va de 15,00 $ à 19,75 $."))
a.p(T(
    "That gap is not an accident or an oversight. It is the direct result of a decision "
    "made about how Canada would be governed, and confirmed by a court in 1925.",
    "Cet écart n'est ni un accident ni un oubli. Il découle directement d'une décision "
    "sur la manière dont le Canada serait gouverné, confirmée par un tribunal en 1925."))

a.h3(T("What every jurisdiction pays right now",
       "Ce que verse chaque administration en ce moment"))
a.table(
    [T("Where", "Où"), T("Rate", "Taux"), T("Since", "Depuis"),
     T("How it changes", "Comment il change")],
    [
        [T("Nunavut", "Nunavut"), "$19.75", T("1 Sep 2025", "1er sept. 2025"),
         T("Iqaluit prices and Nunavut wages", "Prix à Iqaluit et salaires au Nunavut")],
        [T("Yukon", "Yukon"), "$18.51", T("1 Apr 2026", "1er avr. 2026"),
         T("Whitehorse prices", "Prix à Whitehorse")],
        [T("British Columbia", "Colombie-Britannique"), "$18.25",
         T("1 Jun 2026", "1er juin 2026"),
         T("British Columbia prices", "Prix en Colombie-Britannique")],
        [T("Federal workers", "Travailleurs fédéraux"), "$18.15",
         T("1 Apr 2026", "1er avr. 2026"),
         T("National prices", "Prix à l'échelle nationale")],
        [T("Ontario", "Ontario"), "$17.60", T("1 Oct 2025", "1er oct. 2025"),
         T("Ontario prices — rises to $17.95 on 1 October 2026",
           "Prix en Ontario — passe à 17,95 $ le 1er octobre 2026")],
        [T("Prince Edward Island", "Île-du-Prince-Édouard"), "$17.00",
         T("1 Apr 2026", "1er avr. 2026"),
         T("Government decision, no formula", "Décision du gouvernement, sans formule")],
        [T("Northwest Territories", "Territoires du Nord-Ouest"), "$16.95",
         T("1 Sep 2025", "1er sept. 2025"),
         T("Yellowknife prices and territorial wages",
           "Prix à Yellowknife et salaires territoriaux")],
        [T("Nova Scotia", "Nouvelle-Écosse"), "$16.75",
         T("1 Apr 2026", "1er avr. 2026"),
         T("Prices plus one percentage point", "Prix plus un point de pourcentage")],
        [T("Quebec", "Québec"), "$16.60", T("1 May 2026", "1er mai 2026"),
         T("Aims at half the average wage", "Vise la moitié du salaire moyen")],
        [T("Newfoundland and Labrador", "Terre-Neuve-et-Labrador"), "$16.35",
         T("1 Apr 2026", "1er avr. 2026"),
         T("National prices", "Prix à l'échelle nationale")],
        [T("Manitoba", "Manitoba"), "$16.00", T("1 Oct 2025", "1er oct. 2025"),
         T("Manitoba prices", "Prix au Manitoba")],
        [T("New Brunswick", "Nouveau-Brunswick"), "$15.90",
         T("1 Apr 2026", "1er avr. 2026"),
         T("New Brunswick prices", "Prix au Nouveau-Brunswick")],
        [T("Saskatchewan", "Saskatchewan"), "$15.35",
         T("1 Oct 2025", "1er oct. 2025"),
         T("Half prices, half average wages", "Moitié prix, moitié salaires moyens")],
        [T("Alberta", "Alberta"), "$15.00", T("1 Oct 2018", "1er oct. 2018"),
         T("Government decision, no formula", "Décision du gouvernement, sans formule")],
    ])
a.callout(T(
    "<strong>Alberta has not raised its minimum wage since 1 October 2018.</strong> Eight "
    "years without a change. It is now $3.15 an hour below the federal rate and $4.75 "
    "below Nunavut. Alberta and Prince Edward Island are the only two jurisdictions with "
    "no formula at all — the rate moves when a government decides it moves.",
    "<strong>L'Alberta n'a pas augmenté son salaire minimum depuis le 1er octobre "
    "2018.</strong> Huit ans sans changement. Il se situe maintenant 3,15 $ l'heure sous "
    "le taux fédéral et 4,75 $ sous celui du Nunavut. L'Alberta et "
    "l'Île-du-Prince-Édouard sont les deux seules administrations sans aucune formule — "
    "le taux bouge quand un gouvernement décide qu'il bouge."))
a.p(T(
    "Ten of the fourteen now adjust automatically. But look at the right-hand column "
    "again: they adjust to different things. Some follow national prices, some their own "
    "province's, and three follow the price of living in one city — Whitehorse, "
    "Yellowknife, Iqaluit. Nova Scotia adds a full percentage point on top. Quebec aims "
    "at a target ratio to the average wage instead. Saskatchewan splits the difference "
    "between prices and wages.",
    "Dix des quatorze s'ajustent maintenant automatiquement. Mais regardez de nouveau la "
    "colonne de droite : ils ne s'ajustent pas à la même chose. Certains suivent les prix "
    "nationaux, d'autres ceux de leur province, et trois suivent le coût de la vie dans "
    "une seule ville — Whitehorse, Yellowknife, Iqaluit. La Nouvelle-Écosse ajoute un "
    "point de pourcentage complet. Le Québec vise plutôt un rapport cible avec le salaire "
    "moyen. La Saskatchewan partage la différence entre les prix et les salaires."))
a.p(T(
    "One rate of inflation therefore produces fourteen different answers, and the gaps "
    "between provinces widen or narrow every year without anyone deciding that they "
    "should.",
    "Un seul taux d'inflation produit donc quatorze réponses différentes, et les écarts "
    "entre les provinces se creusent ou se resserrent chaque année sans que personne ne "
    "l'ait décidé."))

# ------------------------------------------------------------------ 2
a.h2(T("Why Ottawa cannot simply set one national rate",
       "Pourquoi Ottawa ne peut pas simplement fixer un taux national"))
a.p(T(
    "The answer is in section 92 of the Constitution Act, 1867, the list of subjects on "
    "which the provinces — not Parliament — may make law. One item on that list is short "
    "enough to quote in full.",
    "La réponse se trouve à l'article 92 de la Loi constitutionnelle de 1867, la liste "
    "des sujets sur lesquels les provinces — et non le Parlement — peuvent légiférer. Un "
    "élément de cette liste est assez court pour être cité en entier."))
a.callout(T(
    "Section 92(13): <strong>“Property and Civil Rights in the Province.”</strong>",
    "Article 92(13) : <strong>« La propriété et les droits civils dans la "
    "province. »</strong>"))
a.p(T(
    "Six words. Courts have read them to cover the contract between an employer and an "
    "employee, and a minimum wage is a term of that contract. So it belongs to the "
    "provinces.",
    "Quelques mots à peine. Les tribunaux y ont vu le contrat entre un employeur et un "
    "employé, et le salaire minimum est une clause de ce contrat. Il relève donc des "
    "provinces."))
a.p(T(
    "That reading was settled in 1925. Parliament had passed a law requiring cooling-off "
    "periods before strikes in mines, transport and utilities. In Toronto Electric "
    "Commissioners v Snider, the Judicial Committee of the Privy Council — then Canada's "
    "highest court — struck it down. Labour legislation of that kind was in substance "
    "about property and civil rights in the province, and Parliament had no business "
    "making it.",
    "Cette interprétation a été fixée en 1925. Le Parlement avait adopté une loi imposant "
    "des périodes de réflexion avant les grèves dans les mines, les transports et les "
    "services publics. Dans l'affaire Toronto Electric Commissioners c. Snider, le Comité "
    "judiciaire du Conseil privé — alors le plus haut tribunal du Canada — l'a invalidée. "
    "Une loi du travail de ce genre portait au fond sur la propriété et les droits civils "
    "dans la province, et le Parlement n'avait pas à l'adopter."))
a.p(T(
    "The consequence still holds a century later. A national minimum wage covering every "
    "Canadian worker would require either the agreement of all thirteen provinces and "
    "territories or an amendment to the constitution. Neither is a small thing.",
    "La conséquence tient toujours un siècle plus tard. Un salaire minimum national "
    "visant tous les travailleurs canadiens exigerait soit l'accord des treize provinces "
    "et territoires, soit une modification de la Constitution. Ni l'un ni l'autre n'est "
    "une mince affaire."))

a.h3(T("The rule in one sentence", "La règle en une phrase"))
a.p(T(
    "In 1979 the Supreme Court of Canada decided a case about exactly this. A "
    "construction company building runways at Mirabel airport argued that because "
    "aviation is federal and the land was federal, Quebec's minimum wage law did not "
    "reach it. The Court disagreed: paying construction workers is too far removed from "
    "flying aircraft to be part of the federal subject.",
    "En 1979, la Cour suprême du Canada a tranché une affaire portant exactement "
    "là-dessus. Une entreprise de construction qui bâtissait des pistes à l'aéroport de "
    "Mirabel soutenait que, l'aviation étant fédérale et le terrain aussi, la loi "
    "québécoise sur le salaire minimum ne l'atteignait pas. La Cour n'a pas été de cet "
    "avis : payer des ouvriers de la construction est trop éloigné du transport aérien "
    "pour relever du champ fédéral."))
a.callout(T(
    "The test is <strong>what the employer's business is</strong> — not where the work "
    "happens, and not who the client is. The contractor building an airport is covered by "
    "the province. The airline flying out of it is covered by Ottawa.",
    "Le critère est <strong>la nature de l'entreprise de l'employeur</strong> — non le "
    "lieu du travail, ni l'identité du client. L'entrepreneur qui construit un aéroport "
    "relève de la province. La compagnie aérienne qui en décolle relève d'Ottawa."))

a.h3(T("So who does Ottawa cover?", "Qui relève donc d'Ottawa ?"))
a.p(T(
    "Banks. Airlines and airports. Railways, trucking and buses that cross a border. "
    "Telephone, internet and cable. Radio and television. Ports, ferries, canals and "
    "pipelines that cross a border. Postal and courier services. Uranium and atomic "
    "energy. The federal public service. And every private employer in Yukon, the "
    "Northwest Territories and Nunavut.",
    "Les banques. Les compagnies aériennes et les aéroports. Les chemins de fer, le "
    "camionnage et les autobus qui franchissent une frontière. Le téléphone, Internet et "
    "le câble. La radio et la télévision. Les ports, les traversiers, les canaux et les "
    "pipelines qui franchissent une frontière. Les services postaux et de messagerie. "
    "L'uranium et l'énergie atomique. La fonction publique fédérale. Et tout employeur "
    "privé au Yukon, dans les Territoires du Nord-Ouest et au Nunavut."))
a.p(T(
    "That is about 18,500 employers and 955,000 people — roughly six per cent of the "
    "Canadian workforce. Put the other way: about 94 workers in every 100 get their "
    "minimum wage from a province or territory, not from Ottawa.",
    "Cela représente environ 18 500 employeurs et 955 000 personnes — à peu près six "
    "pour cent de la main-d'oeuvre canadienne. Autrement dit : environ 94 travailleurs "
    "sur 100 tiennent leur salaire minimum d'une province ou d'un territoire, et non "
    "d'Ottawa."))
a.p(T(
    "And when the province pays better, the province wins. The Canada Labour Code says "
    "so directly: where the provincial rate is higher, the employer must pay the higher "
    "one. The federal minimum is a floor beneath a floor. Today it binds only in Alberta, "
    "Saskatchewan and New Brunswick.",
    "Et quand la province paie mieux, c'est la province qui l'emporte. Le Code canadien "
    "du travail le dit directement : lorsque le taux provincial est plus élevé, "
    "l'employeur doit verser le plus élevé des deux. Le minimum fédéral est un plancher "
    "sous un plancher. Aujourd'hui, il ne s'applique réellement qu'en Alberta, en "
    "Saskatchewan et au Nouveau-Brunswick."))

a.h3(T("The decade Ottawa forgot its own minimum wage",
       "La décennie où Ottawa a oublié son propre salaire minimum"))
a.p(T(
    "The federal rate has a strange history that is worth knowing, because it shows what "
    "happens to a wage floor that nobody indexes.",
    "Le taux fédéral a une histoire étrange qui mérite d'être connue, car elle montre ce "
    "qui arrive à un plancher salarial que personne n'indexe."))
a.p(T(
    "In 1986 it reached $4.00 an hour. Then it stayed at $4.00 for the next ten years. It "
    "was never repealed; it was simply never updated. By the mid-1990s provincial rates "
    "averaged about $5.95, which meant a federally regulated worker was legally entitled "
    "to less than someone doing identical work next door.",
    "En 1986, il a atteint 4,00 $ l'heure. Puis il est resté à 4,00 $ pendant dix ans. Il "
    "n'a jamais été abrogé ; il n'a simplement jamais été mis à jour. Au milieu des "
    "années 1990, les taux provinciaux se situaient en moyenne autour de 5,95 $, si bien "
    "qu'un travailleur sous réglementation fédérale avait légalement droit à moins que "
    "son voisin faisant exactement le même travail."))
a.p(T(
    "Parliament fixed it in 1996 by abolishing the federal number altogether and pointing "
    "the law at whatever the province charged. For twenty-five years there was no federal "
    "minimum wage as such. It came back on 29 December 2021 at $15.00, indexed to "
    "inflation every 1 April. It has since risen to $18.15 — a cumulative increase of "
    "21 per cent in four years.",
    "Le Parlement a corrigé la situation en 1996 en supprimant purement et simplement le "
    "chiffre fédéral et en renvoyant la loi au taux provincial en vigueur. Pendant "
    "vingt-cinq ans, il n'y a pas eu de salaire minimum fédéral comme tel. Il est revenu "
    "le 29 décembre 2021 à 15,00 $, indexé à l'inflation chaque 1er avril. Il a depuis "
    "atteint 18,15 $ — une hausse cumulative de 21 pour cent en quatre ans."))

# ------------------------------------------------------------------ 3
a.h2(T("What happened to Canadian pay after the big increases",
       "Ce qui est arrivé à la rémunération au Canada après les fortes hausses"))
a.p(T(
    "Between 2017 and 2018 several provinces raised their minimum wage sharply. Ontario "
    "went from $11.60 to $14.00 on a single day. The effect on the shape of Canadian pay "
    "shows up clearly in Statistics Canada's wage data, and it is not the effect most "
    "people expect.",
    "Entre 2017 et 2018, plusieurs provinces ont fortement relevé leur salaire minimum. "
    "L'Ontario est passé de 11,60 $ à 14,00 $ en une seule journée. L'effet sur la forme "
    "de la rémunération au Canada ressort clairement des données salariales de "
    "Statistique Canada, et ce n'est pas celui auquel la plupart des gens s'attendent."))
a.p(T(
    "Over twenty-five years, adjusted for inflation, the bottom tenth of Canadian wages "
    "grew fastest and the middle grew slowest.",
    "Sur vingt-cinq ans, une fois l'inflation prise en compte, le dixième inférieur des "
    "salaires canadiens a crû le plus vite et le milieu, le plus lentement."))
a.fig(bar_chart(
    T("Real growth in hourly wages, 1997 to 2022",
      "Croissance réelle des salaires horaires, de 1997 à 2022"),
    [(T("Bottom tenth", "Dixième inférieur"), 33.2),
     (T("Top tenth", "Dixième supérieur"), 21.6),
     (T("Middle", "Milieu"), 15.3)],
    unit="%"),
    T("Statistics Canada, wages by decile, in 2022 dollars.",
      "Statistique Canada, salaires par décile, en dollars de 2022."))
a.p(T(
    "The middle grew least of the three. That single fact is behind a great deal of what "
    "people describe when they say the middle class is being squeezed.",
    "Le milieu a le moins progressé des trois. Ce seul fait explique une bonne part de ce "
    "que les gens décrivent lorsqu'ils parlent d'un étranglement de la classe moyenne."))

a.h3(T("The measurement that shows it most clearly",
       "La mesure qui le montre le plus clairement"))
a.p(T(
    "Divide the middle wage by the bottom-tenth wage and you get a number for how far "
    "apart the bottom and the middle are. Here is that number over time.",
    "Divisez le salaire médian par celui du dixième inférieur et vous obtenez une mesure "
    "de la distance entre le bas et le milieu. Voici ce nombre au fil du temps."))
a.table(
    [T("Year", "Année"), T("Middle divided by bottom tenth",
                           "Médian divisé par le dixième inférieur")],
    [["1997", "2.0"], ["2008", "2.0"], ["2017", "1.9"],
     [T("<strong>2018</strong>", "<strong>2018</strong>"),
      T("<strong>1.7</strong>", "<strong>1.7</strong>")],
     ["2022", "1.7"]])
a.p(T(
    "It sat at 2.0 for twenty years. Then it fell to 1.7 in a single year and stayed "
    "there. The distance between the bottom and the middle shrank by about 15 per cent, "
    "and it happened suddenly, in the year of the largest coordinated minimum wage "
    "increases in modern Canadian history.",
    "Il est resté à 2,0 pendant vingt ans. Puis il est tombé à 1,7 en une seule année et "
    "y est resté. La distance entre le bas et le milieu s'est réduite d'environ 15 pour "
    "cent, et cela s'est produit d'un coup, l'année des plus fortes hausses coordonnées "
    "du salaire minimum de l'histoire canadienne moderne."))
a.p(T(
    "A second measure agrees. The share of Canadian employees actually earning the "
    "minimum wage sat between 4 and 5 per cent through the 2000s, was 5.3 per cent in "
    "2008, and reached 10.4 per cent in 2018. One employee in ten was sitting exactly on "
    "the legal floor.",
    "Une seconde mesure va dans le même sens. La proportion d'employés gagnant réellement "
    "le salaire minimum oscillait entre 4 et 5 pour cent durant les années 2000, se "
    "situait à 5,3 pour cent en 2008 et a atteint 10,4 pour cent en 2018. Un employé sur "
    "dix se trouvait exactement sur le plancher légal."))
a.callout(T(
    "That 2018 jump is not the economy deteriorating. It is what happens mechanically "
    "when a government raises the floor above where a lot of people were already standing.",
    "Ce bond de 2018 ne traduit pas une détérioration de l'économie. C'est ce qui se "
    "produit mécaniquement lorsqu'un gouvernement relève le plancher au-dessus du niveau "
    "où beaucoup de gens se tenaient déjà."))

a.h3(T("Why the raise stops before it reaches the middle",
       "Pourquoi la hausse s'arrête avant d'atteindre le milieu"))
a.p(T(
    "When the minimum wage goes up, employers often lift the people just above it too, to "
    "keep some distance between a new hire and an experienced worker. The Bank of Canada "
    "measured how far up that ripple travels.",
    "Quand le salaire minimum augmente, les employeurs relèvent souvent aussi ceux qui se "
    "situent juste au-dessus, afin de garder un écart entre une nouvelle recrue et un "
    "employé expérimenté. La Banque du Canada a mesuré jusqu'où remonte cette ondulation."))
a.fig(bar_chart(
    T("How much a 1% minimum wage rise lifts each wage level",
      "Effet d'une hausse de 1 % du salaire minimum à chaque niveau salarial"),
    [(T("Very lowest paid", "Les moins bien payés"), 0.67),
     (T("Low paid", "Faiblement rémunérés"), 0.31),
     (T("Just above low paid", "Juste au-dessus"), 0.08),
     (T("The middle", "Le milieu"), 0.0)],
    unit="%"),
    T("Bank of Canada, 2017. Above the lowest fifteen per cent of wages the effect could "
      "not be measured at all.",
      "Banque du Canada, 2017. Au-dessus des quinze pour cent de salaires les plus bas, "
      "l'effet n'a pas pu être mesuré du tout."))
a.p(T(
    "Canadian researchers using thirty-seven years of data and 157 separate minimum wage "
    "changes found the same boundary: the ripple reaches about two dollars above the "
    "minimum, and then it stops.",
    "Des chercheurs canadiens, s'appuyant sur trente-sept ans de données et 157 hausses "
    "distinctes du salaire minimum, ont trouvé la même limite : l'ondulation atteint "
    "environ deux dollars au-dessus du minimum, puis s'arrête."))
a.callout(T(
    "<strong>This is the whole mechanism.</strong> Raising the floor lifts the floor and "
    "the few steps above it, and does nothing measurable higher up. So the floor climbs "
    "toward the middle while the middle stands still.",
    "<strong>C'est tout le mécanisme.</strong> Relever le plancher soulève le plancher et "
    "les quelques marches au-dessus, sans effet mesurable plus haut. Le plancher se "
    "rapproche donc du milieu pendant que le milieu ne bouge pas."))

a.h3(T("What that feels like from the middle",
       "Ce que cela donne vu du milieu"))
a.p(T(
    "Here is the part worth being careful about, because it is easy to state wrongly in "
    "either direction.",
    "Voici la partie qu'il faut manier avec soin, car il est facile de la formuler de "
    "travers dans un sens comme dans l'autre."))
a.p(T(
    "The middle did not lose purchasing power. The median hourly wage rose about 15 per "
    "cent in real terms over twenty-five years — slow, roughly half a per cent a year, "
    "but positive. Someone in the middle can buy slightly more than their equivalent "
    "could in 1997.",
    "Le milieu n'a pas perdu de pouvoir d'achat. Le salaire horaire médian a augmenté "
    "d'environ 15 pour cent en termes réels sur vingt-cinq ans — lentement, environ un "
    "demi pour cent par année, mais positivement. Une personne au milieu peut acheter un "
    "peu plus que son équivalent en 1997."))
a.p(T(
    "What the middle lost was distance. In 2008 someone earning well above the minimum "
    "had a comfortable gap between their pay and the legal floor. Today that gap is much "
    "narrower, even though their real wage is slightly higher. Being closer to the bottom "
    "without having moved down is a real change, and it is what people are describing "
    "when they say they feel further behind than the numbers suggest.",
    "Ce que le milieu a perdu, c'est la distance. En 2008, une personne gagnant nettement "
    "plus que le minimum disposait d'un écart confortable entre sa paie et le plancher "
    "légal. Aujourd'hui, cet écart est bien plus mince, même si son salaire réel est "
    "légèrement supérieur. Se retrouver plus près du bas sans avoir reculé est un "
    "changement réel, et c'est ce que les gens décrivent quand ils disent se sentir plus "
    "distancés que ne le laissent croire les chiffres."))
a.p(T(
    "One more figure makes it concrete. A wage of $15.00 an hour in 2008 needed to be "
    "$21.15 by 2024 simply to buy the same things. Anyone whose pay went from $15.00 to "
    "somewhere in the eighteens over that period took a real pay cut of about a tenth, "
    "while the legal minimum beneath them rose by more than 40 per cent in real terms.",
    "Un dernier chiffre rend la chose concrète. Un salaire de 15,00 $ l'heure en 2008 "
    "devait atteindre 21,15 $ en 2024 pour acheter les mêmes choses. Toute personne dont "
    "la paie est passée de 15,00 $ à un peu plus de 18 $ durant cette période a subi une "
    "baisse réelle d'environ un dixième, alors que le minimum légal sous elle augmentait "
    "de plus de 40 pour cent en termes réels."))
a.p(T(
    "This is also, quietly, an employer's problem. In a small business the cost of the "
    "bottom of the payroll rose far faster than the market rate for the experienced staff "
    "above it. The compression happens inside the payroll, not only in the statistics.",
    "C'est aussi, discrètement, un problème d'employeur. Dans une petite entreprise, le "
    "coût du bas de la masse salariale a augmenté bien plus vite que le taux du marché "
    "pour le personnel expérimenté au-dessus. La compression se produit à l'intérieur de "
    "la masse salariale, et pas seulement dans les statistiques."))

# ------------------------------------------------------------------ 4
a.h2(T("Who actually earns the minimum wage",
       "Qui gagne réellement le salaire minimum"))
a.p(T(
    "Two confident stories get told about this, and Statistics Canada contradicts both.",
    "Deux récits assurés circulent à ce sujet, et Statistique Canada les contredit tous "
    "les deux."))
a.p(T(
    "The first is that it is mostly teenagers with summer jobs. In 2018, 52 per cent of "
    "minimum wage workers were aged 15 to 24 — so just under half were 25 or older. "
    "Measured in the first quarter of the year, when students are in school rather than "
    "working, the under-25 share was 43 per cent, meaning a clear majority were adults. "
    "About one in three was a student.",
    "Le premier veut qu'il s'agisse surtout d'adolescents avec un emploi d'été. En 2018, "
    "52 pour cent des salariés au minimum avaient de 15 à 24 ans — donc un peu moins de "
    "la moitié avaient 25 ans ou plus. Mesurée au premier trimestre, quand les étudiants "
    "sont à l'école plutôt qu'au travail, la part des moins de 25 ans tombait à 43 pour "
    "cent, ce qui signifie qu'une nette majorité étaient des adultes. Environ un sur "
    "trois était étudiant."))
a.p(T(
    "The second is that it is mostly people supporting families. About one minimum wage "
    "worker in six is the main or only earner in their household. That is a great many "
    "people, and it is not most of them.",
    "Le second veut qu'il s'agisse surtout de personnes faisant vivre une famille. Environ "
    "un salarié au minimum sur six est le soutien principal ou unique de son ménage. Cela "
    "représente beaucoup de monde, mais pas la majorité."))
a.p(T(
    "What the data shows instead is a workforce split by age in a way that matters. Fewer "
    "than one in five minimum wage workers under 25 works full time. About two-thirds of "
    "the older ones do. The young worker on minimum wage is typically part-time; the "
    "older one is typically full-time, and depending on it.",
    "Ce que montrent plutôt les données, c'est une main-d'oeuvre divisée par l'âge d'une "
    "manière qui compte. Moins d'un salarié au minimum de moins de 25 ans sur cinq "
    "travaille à temps plein. Environ les deux tiers des plus âgés, oui. Le jeune au "
    "salaire minimum est généralement à temps partiel ; le plus âgé est généralement à "
    "temps plein, et en dépend."))
a.ul([
    T("Retail accounts for about a third of all minimum wage workers, and restaurants and "
      "hotels for about a quarter — nearly three in five between them",
      "Le commerce de détail représente environ le tiers de tous les salariés au minimum, "
      "et la restauration et l'hébergement environ le quart — près de trois sur cinq à "
      "eux deux"),
    T("Women are about 59 per cent of minimum wage workers",
      "Les femmes représentent environ 59 pour cent des salariés au minimum"),
    T("About 35 per cent hold a college or university credential, up from 23 per cent in "
      "1998",
      "Environ 35 pour cent détiennent un diplôme collégial ou universitaire, contre "
      "23 pour cent en 1998"),
    T("In 2024, 18.5 per cent of all Canadian employees earned less than $20.00 an hour — "
      "including 62 per cent of everyone working in restaurants and hotels",
      "En 2024, 18,5 pour cent de tous les employés canadiens gagnaient moins de 20,00 $ "
      "l'heure — dont 62 pour cent des personnes travaillant dans la restauration et "
      "l'hébergement"),
])

# ------------------------------------------------------------------ 5
a.h2(T("Does raising it cost jobs? Economists genuinely disagree",
       "Les hausses coûtent-elles des emplois ? Les économistes sont réellement divisés"))
a.p(T(
    "This is the oldest argument in the subject and it is not settled. It is worth being "
    "blunt about how unsettled it is.",
    "C'est le plus vieux débat du domaine, et il n'est pas tranché. Il vaut la peine de "
    "dire franchement à quel point il ne l'est pas."))
a.p(T(
    "Two economists who have spent careers on the question wrote in 2021 that summaries "
    "of the research range from “it is now well-established that higher minimum wages do "
    "not reduce employment” to “most evidence points to adverse employment effects.” "
    "Their point was that specialists cannot agree on what their own literature says.",
    "Deux économistes qui ont consacré leur carrière à cette question écrivaient en 2021 "
    "que les synthèses de la recherche vont de « il est désormais bien établi que des "
    "salaires minimums plus élevés ne réduisent pas l'emploi » à « la plupart des données "
    "indiquent des effets négatifs sur l'emploi ». Leur propos était que les spécialistes "
    "n'arrivent pas à s'entendre sur ce que dit leur propre littérature."))
a.p(T(
    "The modern argument began in 1994, when two American economists compared fast-food "
    "restaurants on either side of the New Jersey border after that state raised its "
    "minimum wage, and found employment had not fallen. A large 2019 study of 138 "
    "American minimum wage increases found the total number of low-wage jobs essentially "
    "unchanged five years later. Against that, a 2021 review concluded there is a clear "
    "preponderance of negative estimates, strongest for teenagers and the least educated.",
    "Le débat moderne a commencé en 1994, quand deux économistes américains ont comparé "
    "des restaurants-minute de part et d'autre de la frontière du New Jersey après une "
    "hausse du salaire minimum dans cet État, et n'ont constaté aucune baisse de "
    "l'emploi. Une vaste étude de 2019 portant sur 138 hausses américaines a conclu que "
    "le nombre total d'emplois faiblement rémunérés était pratiquement inchangé cinq ans "
    "plus tard. À l'opposé, une revue de 2021 conclut à une nette prépondérance "
    "d'estimations négatives, plus marquées chez les adolescents et les moins scolarisés."))

a.h3(T("The Canadian finding worth remembering",
       "La conclusion canadienne à retenir"))
a.p(T(
    "Canada is unusually good ground for studying this, because thirteen governments "
    "change their rates independently — more than 140 changes between 1979 and 2008 "
    "alone. Canadian research tends to find measurable effects on youth employment. But "
    "the most interesting Canadian result is subtler than that.",
    "Le Canada est un terrain d'étude particulièrement riche, car treize gouvernements "
    "modifient leurs taux de façon indépendante — plus de 140 changements entre 1979 et "
    "2008 seulement. La recherche canadienne tend à relever des effets mesurables sur "
    "l'emploi des jeunes. Mais le résultat canadien le plus intéressant est plus subtil."))
a.callout(T(
    "Studying thirty years of Canadian data, researchers found that higher minimum wages "
    "meant <strong>fewer people were hired, and fewer people were laid off</strong>. A "
    "10 per cent increase cut the layoff rate by about 4 per cent. Their summary: jobs in "
    "higher minimum wage regimes are <strong>more stable, but harder to get</strong>.",
    "En étudiant trente ans de données canadiennes, des chercheurs ont constaté qu'un "
    "salaire minimum plus élevé signifiait <strong>moins d'embauches et moins de "
    "licenciements</strong>. Une hausse de 10 pour cent réduisait le taux de licenciement "
    "d'environ 4 pour cent. Leur conclusion : dans les régimes à salaire minimum élevé, "
    "les emplois sont <strong>plus stables, mais plus difficiles à obtenir</strong>."))
a.p(T(
    "That explains something the headline numbers hide. Total employment can look "
    "unchanged while the effect lands hard on one identifiable group — the people trying "
    "to get their first job.",
    "Cela explique une chose que les chiffres globaux masquent. L'emploi total peut "
    "sembler inchangé alors que l'effet frappe durement un groupe bien identifiable : "
    "les personnes qui cherchent leur premier emploi."))
a.p(T(
    "Before the 2018 increases, the Bank of Canada projected that employment would end up "
    "about 60,000 lower than it otherwise would have been by 2019. Three things belong "
    "with that number every time it is used: it was a projection rather than a "
    "measurement, the Bank's own range ran from 30,000 to 140,000, and the same analysis "
    "concluded that total labour income would rise. Quoting the 60,000 alone misrepresents "
    "what the Bank found.",
    "Avant les hausses de 2018, la Banque du Canada prévoyait que l'emploi serait "
    "d'environ 60 000 postes inférieur, en 2019, à ce qu'il aurait autrement été. Trois "
    "précisions accompagnent ce chiffre chaque fois qu'on l'emploie : il s'agissait d'une "
    "projection et non d'une mesure, la fourchette de la Banque allait de 30 000 à "
    "140 000, et la même analyse concluait que le revenu du travail total augmenterait. "
    "Citer les 60 000 seuls déforme ce que la Banque a constaté."))

# ------------------------------------------------------------------ 6
a.h2(T("Does it make everything more expensive?",
       "Est-ce que cela renchérit tout ?"))
a.p(T(
    "Partly, and the honest answer depends entirely on whether you mean the whole economy "
    "or the shop in front of you.",
    "En partie, et la réponse honnête dépend entièrement de ce dont on parle : de "
    "l'ensemble de l'économie ou du commerce devant vous."))
a.p(T(
    "Across the economy the effect is small. The Bank of Canada estimated that the 2018 "
    "increases — the largest coordinated rise in modern Canadian history — added about "
    "0.1 percentage points to inflation. Inflation that year ran around 2.3 per cent, so "
    "the increases account for roughly a twentieth of it. A survey of the international "
    "research found that a 10 per cent rise in the minimum wage raises overall prices by "
    "no more than 0.4 per cent.",
    "À l'échelle de l'économie, l'effet est faible. La Banque du Canada a estimé que les "
    "hausses de 2018 — la plus forte progression coordonnée de l'histoire canadienne "
    "moderne — avaient ajouté environ 0,1 point de pourcentage à l'inflation. Celle-ci "
    "s'est établie cette année-là autour de 2,3 pour cent : les hausses en expliquent "
    "donc environ un vingtième. Une synthèse de la recherche internationale conclut "
    "qu'une hausse de 10 pour cent du salaire minimum renchérit l'ensemble des prix d'au "
    "plus 0,4 pour cent."))
a.p(T(
    "In one particular corner of the economy the effect is much larger. The same survey "
    "found restaurant prices rising by up to about 1.5 per cent for the same 10 per cent "
    "increase — roughly ten to thirty times the economy-wide figure. In a business where "
    "wages are most of the cost, a wage increase shows up on the menu quickly.",
    "Dans un coin précis de l'économie, l'effet est bien plus important. La même synthèse "
    "relève des prix de restaurant en hausse d'environ 1,5 pour cent pour cette même "
    "hausse de 10 pour cent — soit dix à trente fois le chiffre de l'ensemble de "
    "l'économie. Dans une entreprise où les salaires représentent l'essentiel des coûts, "
    "une hausse salariale se retrouve vite sur le menu."))
a.callout(T(
    "Both things are true at once. A restaurant owner who says the minimum wage pushed "
    "their prices up is describing their own accounts accurately. It does not follow that "
    "the minimum wage is why groceries, rent or fuel cost what they do — those are driven "
    "by forces the research does not connect to the wage floor.",
    "Les deux choses sont vraies à la fois. Un restaurateur qui affirme que le salaire "
    "minimum a poussé ses prix à la hausse décrit exactement ses propres livres. Il ne "
    "s'ensuit pas que le salaire minimum explique le prix de l'épicerie, du loyer ou du "
    "carburant — ceux-là obéissent à des forces que la recherche ne rattache pas au "
    "plancher salarial."))

# ------------------------------------------------------------------ 7
a.h2(T("Does the money reach the people who need it?",
       "L'argent atteint-il ceux qui en ont besoin ?"))
a.p(T(
    "This is where the evidence is least comfortable for everyone, and it turns on a "
    "distinction that is easy to miss: a low-earning person is not the same thing as a "
    "low-income household.",
    "C'est ici que les données sont les moins confortables pour tout le monde, et tout "
    "repose sur une distinction facile à manquer : une personne faiblement rémunérée "
    "n'est pas la même chose qu'un ménage à faible revenu."))
a.p(T(
    "Ontario's Financial Accountability Office, a non-partisan officer of the provincial "
    "legislature, examined a rise to $15 an hour. It found that 86 per cent of the money "
    "would go to individuals earning $36,000 a year or less — well targeted by that "
    "measure. It also found that only about 10 per cent would reach individuals living in "
    "low-income families.",
    "Le Bureau de la responsabilité financière de l'Ontario, un poste non partisan "
    "relevant de l'Assemblée législative provinciale, a examiné une hausse à 15 $ "
    "l'heure. Il a conclu que 86 pour cent des sommes iraient à des personnes gagnant "
    "36 000 $ par année ou moins — bien ciblées selon cette mesure. Il a aussi conclu que "
    "10 pour cent seulement atteindraient des personnes vivant dans une famille à faible "
    "revenu."))
a.p(T(
    "The gap between those two numbers is the whole finding. A student earning $14,000 is "
    "a low-earning individual who may live in a comfortable household. Peer-reviewed "
    "Canadian work reaches the same place: about 30 per cent of the earnings gain reaches "
    "poor households, and researchers have called the minimum wage a blunt instrument for "
    "dealing with poverty.",
    "L'écart entre ces deux chiffres constitue toute la conclusion. Un étudiant gagnant "
    "14 000 $ est une personne faiblement rémunérée qui peut vivre dans un ménage aisé. "
    "Des travaux canadiens revus par les pairs aboutissent au même constat : environ "
    "30 pour cent du gain salarial atteint les ménages pauvres, et des chercheurs ont "
    "qualifié le salaire minimum d'instrument grossier pour lutter contre la pauvreté."))
a.p(T(
    "There is a serious answer to that. A labour economist at the University of British "
    "Columbia has argued that those studies measured increases too small to lift anyone "
    "over the poverty line — that they tested underpowered policy rather than an "
    "ineffective one. On that view the failure was in the size of the increases, not in "
    "the instrument.",
    "Il existe une réponse sérieuse à cela. Un économiste du travail de l'Université de "
    "la Colombie-Britannique soutient que ces études portaient sur des hausses trop "
    "faibles pour faire franchir à quiconque le seuil de pauvreté — qu'elles ont testé "
    "une politique sous-dimensionnée plutôt qu'une politique inefficace. Selon ce point "
    "de vue, l'échec tenait à l'ampleur des hausses, non à l'instrument."))

a.h3(T("And the raise is bigger than what you keep",
       "Et la hausse est plus grande que ce qu'il vous reste"))
a.p(T(
    "When low pay rises, some of it goes back. Income tax takes a share, and income-tested "
    "benefits such as the Canada Child Benefit and the Canada Workers Benefit reduce as "
    "earnings go up. Ontario's Financial Accountability Office calculated that income tax "
    "alone would absorb about 15 per cent of a $1.3 billion minimum wage increase, before "
    "any benefit reduction at all.",
    "Quand une faible rémunération augmente, une partie repart. L'impôt sur le revenu en "
    "prend une part, et les prestations fondées sur le revenu, comme l'Allocation "
    "canadienne pour enfants et l'Allocation canadienne pour les travailleurs, diminuent "
    "à mesure que les gains montent. Le Bureau de la responsabilité financière de "
    "l'Ontario a calculé que l'impôt sur le revenu absorberait à lui seul environ "
    "15 pour cent d'une hausse du salaire minimum de 1,3 milliard de dollars, avant toute "
    "réduction de prestation."))
a.p(T(
    "Add the benefit reductions and the effect gets much larger. Canadian research finds "
    "that families earning roughly $45,000 to $65,000 can lose more than half of every "
    "extra dollar they earn, once tax and withdrawn benefits are counted together. In "
    "some family situations it is considerably more than half.",
    "Ajoutez les réductions de prestations et l'effet grandit beaucoup. La recherche "
    "canadienne montre que les familles gagnant environ de 45 000 $ à 65 000 $ peuvent "
    "perdre plus de la moitié de chaque dollar supplémentaire gagné, une fois l'impôt et "
    "les prestations retirées comptés ensemble. Dans certaines situations familiales, "
    "c'est nettement plus de la moitié."))
a.p(T(
    "This is not a fault of minimum wage policy — it is how the tax and benefit system "
    "behaves at every income. But it means a headline raise and a raise in take-home pay "
    "are two different sizes, and the second is smaller.",
    "Ce n'est pas un défaut de la politique du salaire minimum — c'est le comportement du "
    "système d'impôt et de prestations à tous les niveaux de revenu. Mais cela signifie "
    "qu'une hausse annoncée et une hausse du salaire net sont deux grandeurs différentes, "
    "et que la seconde est plus petite."))

# ------------------------------------------------------------------ 8
a.h2(T("What the numbers settle, and what they leave open",
       "Ce que les chiffres tranchent et ce qu'ils laissent ouvert"))
a.p(T(
    "Three things are well established and not seriously disputed.",
    "Trois choses sont bien établies et ne sont pas sérieusement contestées."))
a.ul([
    T("The minimum wage has risen far faster than prices. In Ontario it went from $8.75 "
      "in 2008 to $17.95 in 2026, while prices rose about 44 per cent — a gain of roughly "
      "40 per cent in what that wage actually buys",
      "Le salaire minimum a augmenté bien plus vite que les prix. En Ontario, il est "
      "passé de 8,75 $ en 2008 à 17,95 $ en 2026, alors que les prix montaient d'environ "
      "44 pour cent — un gain d'à peu près 40 pour cent en pouvoir d'achat réel"),
    T("The gap between the lowest-paid and the middle has narrowed sharply, and the change "
      "happened in one year",
      "L'écart entre les moins bien payés et le milieu s'est nettement resserré, et le "
      "changement s'est produit en une seule année"),
    T("The lift does not travel far. Above roughly two dollars over the minimum, no effect "
      "on wages can be measured",
      "La hausse ne remonte pas loin. Au-delà d'environ deux dollars au-dessus du "
      "minimum, aucun effet sur les salaires n'est mesurable"),
])
a.p(T(
    "Three things are not settled, and anyone who tells you otherwise is choosing a side "
    "rather than reporting the evidence.",
    "Trois choses ne sont pas tranchées, et quiconque prétend le contraire choisit un "
    "camp plutôt que de rapporter les données."))
a.ul([
    T("Whether increases cost jobs overall, and how many",
      "La question de savoir si les hausses coûtent des emplois dans l'ensemble, et "
      "combien"),
    T("Whether the minimum wage is a reasonable tool for reducing poverty, or the wrong "
      "instrument aimed at the right problem",
      "La question de savoir si le salaire minimum est un outil raisonnable de réduction "
      "de la pauvreté, ou le mauvais instrument visé sur le bon problème"),
    T("Whether the compression of the last decade is a fairness gain, a squeeze on the "
      "middle, or both at once",
      "La question de savoir si la compression de la dernière décennie est un gain "
      "d'équité, un étranglement du milieu, ou les deux à la fois"),
])
a.p(T(
    "That last one is not really an economic question. The data can tell you that the "
    "bottom rose and the middle did not move much. Whether that is the system working or "
    "the system failing is a judgment about what a fair distance between the floor and "
    "the middle ought to be, and no dataset answers it.",
    "La dernière n'est pas vraiment une question économique. Les données peuvent vous "
    "dire que le bas a monté et que le milieu a peu bougé. Savoir si cela signifie que le "
    "système fonctionne ou qu'il échoue relève d'un jugement sur la distance juste entre "
    "le plancher et le milieu, et aucun ensemble de données n'y répond."))

# ------------------------------------------------------------------ sources
a.sources(T("Where this comes from", "D'où proviennent ces données"), [
    out_link("https://laws-lois.justice.gc.ca/eng/const/page-3.html",
             T("Constitution Act, 1867, section 92 — Justice Canada",
               "Loi constitutionnelle de 1867, article 92 — Justice Canada")),
    out_link("https://laws-lois.justice.gc.ca/eng/acts/L-2/section-178.html",
             T("Canada Labour Code, section 178 — Justice Canada",
               "Code canadien du travail, article 178 — Justice Canada")),
    out_link("https://www.canada.ca/en/services/jobs/workplace/federally-regulated-industries.html",
             T("Federally regulated industries and workplaces — Government of Canada",
               "Industries et lieux de travail sous réglementation fédérale — "
               "gouvernement du Canada")),
    out_link("https://www.canada.ca/en/employment-social-development/corporate/portfolio/labour/programs/labour-standards/reports/issue-paper-federal-minimum-wage.html",
             T("Issue paper on the federal minimum wage — Employment and Social "
               "Development Canada",
               "Document de réflexion sur le salaire minimum fédéral — Emploi et "
               "Développement social Canada")),
    out_link("https://www.canada.ca/en/employment-social-development/news/2026/03/government-of-canada-raises-the-federal-minimum-wage.html",
             T("Federal minimum wage rises to $18.15, March 2026 — Government of Canada",
               "Le salaire minimum fédéral passe à 18,15 $, mars 2026 — gouvernement du "
               "Canada")),
    out_link("https://news.ontario.ca/en/release/1007239/ontario-raising-minimum-wage-to-protect-workers-and-support-a-competitive-economy",
             T("Ontario minimum wage rising to $17.95, April 2026 — Government of Ontario",
               "Le salaire minimum de l'Ontario passe à 17,95 $, avril 2026 — "
               "gouvernement de l'Ontario")),
    out_link("https://www150.statcan.gc.ca/n1/pub/14-28-0001/2023001/article/00005-eng.htm",
             T("Wages by decile, 1997 to 2022 — Statistics Canada",
               "Salaires par décile, de 1997 à 2022 — Statistique Canada")),
    out_link("https://www150.statcan.gc.ca/n1/pub/14-28-0001/2025001/article/00002-eng.htm",
             T("Employees with low pay, 2024 — Statistics Canada",
               "Employés faiblement rémunérés, 2024 — Statistique Canada")),
    out_link("https://www150.statcan.gc.ca/n1/pub/75-004-m/75-004-m2019003-eng.htm",
             T("Minimum wage workers: 20 years of data — Statistics Canada",
               "Les travailleurs au salaire minimum : 20 ans de données — Statistique "
               "Canada")),
    out_link("https://www150.statcan.gc.ca/n1/pub/75-006-x/2018001/article/54974-eng.htm",
             T("Recent changes in the composition of minimum wage workers — Statistics "
               "Canada",
               "Changements récents dans la composition des travailleurs au salaire "
               "minimum — Statistique Canada")),
    out_link("https://www.bankofcanada.ca/2017/12/staff-analytical-note-2017-26/",
             T("The impacts of minimum wage increases on the Canadian economy — Bank of "
               "Canada",
               "Les effets des hausses du salaire minimum sur l'économie canadienne — "
               "Banque du Canada")),
    out_link("https://fao-on.org/en/report/lift-report-2019/",
             T("Comparing the LIFT credit to a minimum wage increase — Financial "
               "Accountability Office of Ontario",
               "Comparaison du crédit LIFT et d'une hausse du salaire minimum — Bureau de "
               "la responsabilité financière de l'Ontario")),
    out_link("https://www.nber.org/papers/w28388",
             T("Myth or measurement: what does the new minimum wage research say? — "
               "Neumark and Shirley",
               "Mythe ou mesure : que dit la nouvelle recherche sur le salaire minimum ? "
               "— Neumark et Shirley")),
    out_link("https://www.nber.org/papers/w25434",
             T("The effect of minimum wages on low-wage jobs — Cengiz, Dube, Lindner and "
               "Zipperer",
               "L'effet du salaire minimum sur les emplois faiblement rémunérés — Cengiz, "
               "Dube, Lindner et Zipperer")),
    out_link("https://clef.uwaterloo.ca/wp-content/uploads/2023/10/CLEF-059-2023.pdf",
             T("The minimum wage, turnover, and the shape of the wage distribution — "
               "Canadian Labour Economics Forum",
               "Le salaire minimum, la rotation et la forme de la distribution salariale "
               "— Canadian Labour Economics Forum")),
    out_link("https://cdhowe.org/publication/the-clawback-trap-how-canadas-benefit-system-can-undermine-work-and-saving/",
             T("The clawback trap — C.D. Howe Institute",
               "Le piège de la récupération — Institut C.D. Howe")),
])

a.disclaimer(T(
    "This page explains how minimum wage rules work in Canada. It is not legal or "
    "financial advice, and it is not affiliated with any government. Rates change on "
    "fixed dates through the year — always confirm the current rate with your province, "
    "territory, or the Government of Canada before relying on it.",
    "Cette page explique le fonctionnement des règles sur le salaire minimum au Canada. "
    "Il ne s'agit ni d'un avis juridique ni d'un conseil financier, et elle n'est "
    "affiliée à aucun gouvernement. Les taux changent à dates fixes au cours de "
    "l'année — vérifiez toujours le taux en vigueur auprès de votre province, de votre "
    "territoire ou du gouvernement du Canada avant de vous y fier."))

a.build()
flush_pairs()
