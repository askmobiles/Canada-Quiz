/* Rights and Respect — ten everyday Canadian situations, drawn.
   ==================================================================
   WHERE EVERY ANSWER COMES FROM

   Two official sources, and nothing else:

     The rights and freedoms the Charter protects (Department of Justice) —
       "Everyone in Canada is free to practise any religion or no religion at
       all"; equality means "treated with the same respect, dignity and
       consideration, regardless of personal characteristics"; "English and
       French are the official languages of the country and have equality of
       status"; Canadians "can live or work anywhere within Canada"; every
       Canadian citizen has the right to vote and to run for office.

     Discover Canada, the official citizenship study guide — the
       responsibilities it lists by name: obeying the law, taking
       responsibility for oneself and one's family, serving on a jury, voting
       in elections, helping others in the community, and protecting and
       enjoying our heritage and environment.

   ONE THING KEPT HONEST

   The Charter binds governments, not children in a schoolyard. A child who
   will not pass the ball is not breaking the Constitution, and telling a
   ten-year-old otherwise would be teaching them something false they would
   later have to unlearn. So the wording throughout is what Canada PROMISES and
   what Canadians DO — "the rule Canada lives by", "one of the responsibilities
   Canada asks of everyone" — never "that is illegal". Where a real legal fact
   exists it is stated exactly: you vote at eighteen, both languages are
   official, you may live anywhere in the country.

   HOW THE PICTURES WORK

   Plain scenes: a schoolyard, a classroom, a park, a winter street. Figures are
   drawn simply and equally — different skin tones and, where the situation is
   about religion, different head coverings, all drawn with the same care and
   none of them a caricature. Nothing in a drawing may state its own answer.

   draw() TAKES THE LANGUAGE. Words inside a picture are invisible to
   build_fr.py and to the runtime translator alike, so the French page happily
   showed an English removal van until somebody looked at a screenshot. Any
   scene with words in it must branch on fr.

   Both languages are in this file, because a script writes these onto the page
   after it loads and build_fr.py never sees a string that does not exist yet. */
(function () {
  "use strict";

  var INK = "#2b2d42", SKY = "#dbeeff", GRASS = "#a8d5ae", SNOW = "#eef4f8";

  function t(x, y, s, size, fill, weight, anchor) {
    return '<text x="' + x + '" y="' + y + '" font-family="Arial, Helvetica, sans-serif" font-size="' +
           (size || 13) + '" fill="' + (fill || INK) + '"' +
           (weight ? ' font-weight="' + weight + '"' : "") +
           (anchor ? ' text-anchor="' + anchor + '"' : "") + ">" + s + "</text>";
  }

  /* Sky above, ground below. Every scene starts here so they feel like one set. */
  function ground(groundFill, skyFill) {
    return '<rect x="0" y="0" width="500" height="300" fill="' + (skyFill || SKY) + '"/>' +
           '<rect x="0" y="214" width="500" height="86" fill="' + (groundFill || GRASS) + '"/>';
  }

  /* A child. One shape, changed by options, so no child in these scenes is
     drawn with more or less care than another.
       skin  shirt            the two colours
       o.hair   a simple cap of hair
       o.hijab  a headscarf          o.turban  a turban
       o.chair  a wheelchair instead of legs
       o.flip   facing the other way */
  function kid(x, y, skin, shirt, o) {
    o = o || {};
    var g = '<g transform="translate(' + x + ',' + y + ')' + (o.flip ? " scale(-1,1)" : "") + '">';
    if (o.chair) {
      g += '<circle cx="2" cy="16" r="15" fill="none" stroke="' + INK + '" stroke-width="3"/>';
      g += '<circle cx="2" cy="16" r="4" fill="' + INK + '"/>';
      g += '<circle cx="24" cy="26" r="6" fill="none" stroke="' + INK + '" stroke-width="2.5"/>';
      g += '<path d="M-8 -6 L14 -6 L14 10 L-8 10 Z" fill="' + shirt + '"/>';
      g += '<path d="M-10 -8 L-10 14" stroke="' + INK + '" stroke-width="3" stroke-linecap="round"/>';
      g += '<path d="M-4 -20 L12 -20 L14 -4 L-6 -4 Z" fill="' + shirt + '"/>';
    } else {
      g += '<path d="M-7 4 L-7 30" stroke="' + INK + '" stroke-width="5" stroke-linecap="round"/>';
      g += '<path d="M7 4 L7 30" stroke="' + INK + '" stroke-width="5" stroke-linecap="round"/>';
      g += '<path d="M-11 -22 L11 -22 L14 6 L-14 6 Z" fill="' + shirt + '"/>';
      g += '<path d="M-13 -18 L-20 2" stroke="' + shirt + '" stroke-width="6" stroke-linecap="round"/>';
      g += '<path d="M13 -18 L20 2" stroke="' + shirt + '" stroke-width="6" stroke-linecap="round"/>';
    }
    var hy = o.chair ? -30 : -34;
    g += '<circle cx="1" cy="' + hy + '" r="11" fill="' + skin + '" stroke="' + INK + '" stroke-width="2"/>';
    if (o.hijab) {
      g += '<path d="M-13 ' + (hy - 2) + ' a13 13 0 0 1 26 0 l2 16 l-30 0 Z" fill="' + o.hijab + '"/>';
      g += '<circle cx="1" cy="' + hy + '" r="8" fill="' + skin + '"/>';
    } else if (o.turban) {
      /* Taller than a cap, with a wrap line across it — the first version was a
         low dome and read as a red beanie, which is not the same thing at all.
         Found by drawing it and looking. */
      g += '<path d="M-13 ' + (hy + 1) + ' a13 18 0 0 1 26 0 Z" fill="' + o.turban + '"/>';
      g += '<path d="M-13 ' + (hy - 4) + ' q13 7 26 0" stroke="rgba(0,0,0,.22)" stroke-width="2.5" fill="none"/>';
      g += '<path d="M-12 ' + (hy + 1) + ' q12 5 24 0" stroke="rgba(0,0,0,.22)" stroke-width="2" fill="none"/>';
    } else if (o.hair !== false) {
      g += '<path d="M-11 ' + (hy - 2) + ' a11 11 0 0 1 22 0 Z" fill="' + (o.hair || "#3b2f2a") + '"/>';
    }
    return g + "</g>";
  }

  function maple(x, y, s) {
    s = s || 1;
    return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')">' +
           '<rect x="-5" y="0" width="10" height="34" rx="3" fill="#8a6a4a"/>' +
           '<circle cx="0" cy="-16" r="26" fill="#e07a3f"/>' +
           '<circle cx="-20" cy="-4" r="16" fill="#d9662f"/>' +
           '<circle cx="20" cy="-4" r="16" fill="#d9662f"/></g>';
  }

  function school(x, y) {
    return '<g transform="translate(' + x + ',' + y + ')">' +
           '<rect x="0" y="0" width="150" height="86" fill="#c9a227"/>' +
           '<polygon points="-10,0 75,-38 160,0" fill="#b5651d"/>' +
           '<rect x="60" y="40" width="30" height="46" fill="#8a6a4a"/>' +
           '<rect x="16" y="20" width="26" height="24" fill="#dff0f7"/>' +
           '<rect x="108" y="20" width="26" height="24" fill="#dff0f7"/>' +
           '<rect x="70" y="-52" width="4" height="30" fill="#6b7280"/>' +
           '<path d="M74 -50 h26 v17 h-26 Z" fill="#e63946"/></g>';
  }

  function ball(x, y) {
    return '<circle cx="' + x + '" cy="' + y + '" r="12" fill="#ffffff" stroke="' + INK + '" stroke-width="2"/>' +
           '<path d="M' + (x - 12) + ' ' + y + ' h24 M' + x + ' ' + (y - 12) + ' v24" stroke="' + INK + '" stroke-width="1.5"/>';
  }

  function bubble(x, y, w, h, lines, fill) {
    var g = '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h +
            '" rx="12" fill="' + (fill || "#ffffff") + '" stroke="' + INK + '" stroke-width="2"/>';
    g += '<path d="M' + (x + 18) + ' ' + (y + h) + ' l6 12 l12 -12 Z" fill="' + (fill || "#ffffff") +
         '" stroke="' + INK + '" stroke-width="2"/>';
    lines.forEach(function (s, i) { g += t(x + 12, y + 24 + i * 18, s, 13); });
    return g;
  }

  /* Some scenes are ABOUT a detail — a turban, a wheelchair — and a detail on a
     26-pixel figure is just a coloured blob. Those scenes are drawn closer. */
  function zoom(inner, s, x, y) {
    return '<g transform="translate(' + (x || 0) + ',' + (y || 0) + ') scale(' + s + ')">' +
           inner + "</g>";
  }

  window.CQ_RESPECT_SCENES = [

    /* 1 — two official languages, equality of status. */
    { id: "french",
      draw: function () {
        return ground() + school(300, 128) +
               kid(120, 214, "#8d5524", "#4895ef", {}) +
               kid(190, 214, "#f2c6a0", "#2a9d8f", { flip: true, hair: "#c98b3a" }) +
               bubble(60, 70, 200, 56, ["Bonjour ! Je m'appelle", "Chlo&eacute;."], "#fff8e1");
      },
      en: { q: "A new girl joins your class. She speaks French and is still learning English. What is true in Canada?",
            a: ["She should speak English at school, because this is Canada",
                "French and English are both official languages of Canada, with equal status",
                "She has to go to a different school"],
            c: 1,
            e: "Canada has two official languages and they have equal status. She is speaking one of them. Learning a few words of hers is a good way to make her welcome." },
      fr: { q: "Une nouvelle &eacute;l&egrave;ve arrive dans ta classe. Elle parle fran&ccedil;ais et apprend encore l'anglais. Qu'est-ce qui est vrai au Canada ?",
            a: ["Elle devrait parler anglais &agrave; l'&eacute;cole, puisqu'on est au Canada",
                "Le fran&ccedil;ais et l'anglais sont les deux langues officielles du Canada, &agrave; &eacute;galit&eacute;",
                "Elle doit aller dans une autre &eacute;cole"],
            c: 1,
            e: "Le Canada a deux langues officielles, &agrave; &eacute;galit&eacute; de statut. Elle en parle une. Apprendre quelques mots de sa langue est une belle fa&ccedil;on de l'accueillir." } },

    /* 2 — equality: same respect, dignity and consideration. */
    { id: "team",
      draw: function (fr) {
        return ground() + maple(440, 200, .8) +
               kid(140, 214, "#f2c6a0", "#e63946", {}) +
               kid(200, 214, "#c68642", "#ffb703", {}) +
               ball(172, 250) +
               kid(360, 214, "#5c3a21", "#8e7dbe", { flip: true }) +
               bubble(250, 62, 210, 56,
                      fr ? ["Tu ne peux pas jouer", "avec nous."]
                         : ["You cannot play", "with us."], "#fdf3f4");
      },
      en: { q: "Two children will not let another join the game because of the colour of his skin. What is the rule Canada lives by?",
            a: ["Everyone is treated with the same respect and dignity, whatever they look like",
                "It is their game, so they can choose who plays",
                "He should find children who look like him"],
            c: 0,
            e: "Equality in Canada means everyone is treated with the same respect, dignity and consideration, whoever they are. Leaving somebody out for how they look is the opposite of that — and worth telling a teacher about." },
      fr: { q: "Deux enfants refusent qu'un autre se joigne au jeu &agrave; cause de la couleur de sa peau. Quelle est la r&egrave;gle du Canada ?",
            a: ["Tout le monde est trait&eacute; avec le m&ecirc;me respect et la m&ecirc;me dignit&eacute;, peu importe son apparence",
                "C'est leur jeu, ils choisissent qui joue",
                "Il devrait trouver des enfants qui lui ressemblent"],
            c: 0,
            e: "L'&eacute;galit&eacute; au Canada, c'est que chacun soit trait&eacute; avec le m&ecirc;me respect, la m&ecirc;me dignit&eacute; et la m&ecirc;me consid&eacute;ration. Exclure quelqu'un pour son apparence en est le contraire, et cela vaut la peine d'en parler &agrave; un enseignant." } },

    /* 3 — freedom of conscience and religion, including none. */
    { id: "religion",
      draw: function (fr) {
        return ground() +
               zoom(kid(0, 0, "#c68642", "#2a9d8f", { hijab: "#8e7dbe" }) +
                    kid(78, 0, "#8d5524", "#4895ef", { turban: "#e63946" }) +
                    kid(156, 0, "#f2c6a0", "#ffb703", {}), 1.75, 90, 214) +
               bubble(250, 40, 240, 56,
                      fr ? ["Pourquoi ont-ils le droit", "de porter cela &agrave; l'&eacute;cole ?"]
                         : ["Why do they get to wear", "that at school?"], "#ffffff");
      },
      en: { q: "Three children in your class dress differently because of what their families believe. One wears a headscarf, one a turban, one wears nothing special. Who is allowed to?",
            a: ["Only the one wearing nothing special",
                "All of them — everyone in Canada is free to practise any religion, or no religion at all",
                "Only if the school gives permission"],
            c: 1,
            e: "Freedom of conscience and religion is one of Canada's fundamental freedoms. It covers following a religion and it covers following none — all three children are doing exactly what Canada allows." },
      fr: { q: "Trois enfants de ta classe s'habillent diff&eacute;remment selon les croyances de leur famille. L'un porte un foulard, l'autre un turban, l'autre rien de particulier. Qui en a le droit ?",
            a: ["Seulement celui qui ne porte rien de particulier",
                "Tous les trois : au Canada, chacun est libre de pratiquer une religion, ou aucune",
                "Seulement si l'&eacute;cole donne la permission"],
            c: 1,
            e: "La libert&eacute; de conscience et de religion est une des libert&eacute;s fondamentales du Canada. Elle couvre le fait de suivre une religion et celui de n'en suivre aucune : les trois enfants font exactement ce que le Canada permet." } },

    /* 4 — equality includes disability. The place changes, not the child. */
    { id: "wheelchair",
      draw: function (fr) {
        return ground("#cfd6dd") +
               '<rect x="250" y="120" width="200" height="94" fill="#b9c3cc"/>' +
               '<rect x="300" y="150" width="40" height="64" fill="#8a6a4a"/>' +
               '<path d="M250 214 l0 -10 l18 0 l0 -10 l18 0 l0 -10 l18 0" fill="none" stroke="' + INK + '" stroke-width="4"/>' +
               kid(120, 214, "#f2c6a0", "#4895ef", { chair: true }) +
               kid(190, 214, "#8d5524", "#e63946", {}) +
               bubble(60, 56, 230, 56,
                      fr ? ["La sortie de classe est", "en haut de cet escalier."]
                         : ["The class trip is up", "those steps."], "#ffffff");
      },
      en: { q: "The whole class is going on a trip, but the only way in is up a flight of steps, and one girl uses a wheelchair. What should happen?",
            a: ["She stays behind — it is nobody's fault",
                "Somebody carries her up",
                "The class finds a place everyone can get into, or asks for a ramp"],
            c: 2,
            e: "Equality covers disability too: the same respect, dignity and consideration. The thing that needs to change is the steps, not the child — and being carried is not the same as being included." },
      fr: { q: "Toute la classe part en sortie, mais la seule entr&eacute;e est en haut d'un escalier, et une &eacute;l&egrave;ve utilise un fauteuil roulant. Que devrait-il se passer ?",
            a: ["Elle reste &agrave; l'&eacute;cole : ce n'est la faute de personne",
                "Quelqu'un la porte jusqu'en haut",
                "La classe trouve un endroit accessible &agrave; tous, ou demande une rampe"],
            c: 2,
            e: "L'&eacute;galit&eacute; couvre aussi le handicap : m&ecirc;me respect, m&ecirc;me dignit&eacute;, m&ecirc;me consid&eacute;ration. Ce qui doit changer, c'est l'escalier, pas l'enfant — et &ecirc;tre port&eacute;e n'&eacute;quivaut pas &agrave; &ecirc;tre incluse." } },

    /* 5 — how decisions get made, and the real voting age. */
    { id: "vote",
      draw: function (fr) {
        return '<rect x="0" y="0" width="500" height="300" fill="#fdfbf7"/>' +
               '<rect x="0" y="238" width="500" height="62" fill="#d8c3a5"/>' +
               '<rect x="150" y="40" width="200" height="120" rx="6" fill="#2f4f4f"/>' +
               t(250, 88, fr ? "Sortie : parc ou mus&eacute;e ?" : "Trip: park or museum?",
                 17, "#ffffff", "bold", "middle") +
               t(250, 122, fr ? "Levez la main pour chacun" : "Hands up for each",
                 14, "#cfe3d8", null, "middle") +
               kid(110, 238, "#c68642", "#4895ef", {}) +
               kid(190, 238, "#f2c6a0", "#e63946", {}) +
               kid(310, 238, "#8d5524", "#2a9d8f", {}) +
               kid(390, 238, "#f6d5c0", "#ffb703", {});
      },
      en: { q: "The class cannot agree where to go, so the teacher asks everyone to put a hand up for one choice or the other. What is that called, and when can you do it for real?",
            a: ["Voting — and you can vote in a Canadian election at eighteen",
                "Voting — and you can vote in an election as soon as you are in high school",
                "It is not really voting, teachers just decide anyway"],
            c: 0,
            e: "That is a vote: everybody gets one, and the bigger number wins. In a real Canadian election every citizen may vote from the age of eighteen — and may run for office too." },
      fr: { q: "La classe n'arrive pas &agrave; se d&eacute;cider, alors l'enseignante demande de lever la main pour un choix ou l'autre. Comment cela s'appelle-t-il, et quand peux-tu le faire pour de vrai ?",
            a: ["Voter — et on peut voter &agrave; une &eacute;lection canadienne &agrave; dix-huit ans",
                "Voter — et on peut voter d&egrave;s l'&eacute;cole secondaire",
                "Ce n'est pas vraiment un vote, l'enseignant d&eacute;cide de toute fa&ccedil;on"],
            c: 0,
            e: "C'est un vote : chacun en a un, et le plus grand nombre l'emporte. &Agrave; une vraie &eacute;lection canadienne, tout citoyen peut voter &agrave; partir de dix-huit ans, et peut aussi se pr&eacute;senter." } },

    /* 6 — mobility rights. */
    { id: "moving",
      draw: function (fr) {
        return ground("#d8c3a5") + maple(60, 200, .7) +
               '<rect x="180" y="120" width="180" height="76" rx="8" fill="#4895ef"/>' +
               '<rect x="360" y="140" width="60" height="56" rx="6" fill="#2b6cb0"/>' +
               '<circle cx="220" cy="204" r="16" fill="' + INK + '"/><circle cx="220" cy="204" r="6" fill="#9aa4b2"/>' +
               '<circle cx="380" cy="204" r="16" fill="' + INK + '"/><circle cx="380" cy="204" r="6" fill="#9aa4b2"/>' +
               t(270, 166, fr ? "D&Eacute;M&Eacute;NAGEMENT" : "MOVING",
                 fr ? 15 : 20, "#ffffff", "bold", "middle") +
               kid(110, 214, "#f2c6a0", "#e63946", {}) +
               bubble(40, 44, 240, 56,
                      fr ? ["Nous d&eacute;m&eacute;nageons de", "Halifax &agrave; Calgary."]
                         : ["We are moving from", "Halifax to Calgary."], "#ffffff");
      },
      en: { q: "Your friend's family is moving from Nova Scotia to Alberta. Do they need permission to live in another province?",
            a: ["Yes, they must apply to the new province first",
                "No — Canadians can live and work anywhere in Canada",
                "Only if they are moving for a job"],
            c: 1,
            e: "Canadians can live or work anywhere within Canada, and can leave the country and come back. It is one of the rights the Charter protects, and it is why moving province is a moving truck and not a form." },
      fr: { q: "La famille de ton ami d&eacute;m&eacute;nage de la Nouvelle-&Eacute;cosse &agrave; l'Alberta. Faut-il une permission pour vivre dans une autre province ?",
            a: ["Oui, il faut d'abord faire une demande &agrave; la nouvelle province",
                "Non : les Canadiens peuvent vivre et travailler partout au Canada",
                "Seulement si c'est pour un emploi"],
            c: 1,
            e: "Les Canadiens peuvent vivre ou travailler partout au Canada, et quitter le pays puis y revenir. C'est un des droits que la Charte prot&egrave;ge, et c'est pourquoi changer de province demande un camion, pas un formulaire." } },

    /* 7 — freedom of expression, and the honest limit on it. */
    { id: "disagree",
      draw: function (fr) {
        return ground() + maple(430, 202, .75) +
               kid(150, 214, "#8d5524", "#2a9d8f", {}) +
               kid(300, 214, "#f2c6a0", "#4895ef", { flip: true }) +
               bubble(40, 46, 200, 56,
                      fr ? ["Le hockey, c'est plate.", "Vraiment plate."]
                         : ["Hockey is boring.", "Really boring."], "#ffffff") +
               bubble(270, 92, 190, 38,
                      fr ? ["Je ne suis pas d'accord !"]
                         : ["I completely disagree!"], "#e8f3ef");
      },
      en: { q: "A classmate says something you think is completely wrong. What does Canada let you do?",
            a: ["Make them stop saying it",
                "Say why you disagree — you both have freedom of expression",
                "Nothing, disagreeing is rude"],
            c: 1,
            e: "Freedom of thought, belief, opinion and expression belongs to both of you, so the answer to an opinion you dislike is your own opinion back. It does have limits: it does not cover hateful speech against a group of people." },
      fr: { q: "Un camarade dit quelque chose que tu trouves compl&egrave;tement faux. Que te permet le Canada ?",
            a: ["De l'emp&ecirc;cher de le dire",
                "De dire pourquoi tu n'es pas d'accord : vous avez tous les deux la libert&eacute; d'expression",
                "Rien, ce serait impoli de contredire"],
            c: 1,
            e: "La libert&eacute; de pens&eacute;e, de croyance, d'opinion et d'expression vous appartient &agrave; tous les deux : la r&eacute;ponse &agrave; une opinion qui d&eacute;pla&icirc;t est une autre opinion. Elle a une limite : elle ne couvre pas les propos haineux contre un groupe de personnes." } },

    /* 8 — a responsibility Discover Canada names: protect our environment. */
    { id: "litter",
      draw: function () {
        return ground() + maple(400, 196, .9) + maple(70, 204, .6) +
               '<rect x="210" y="156" width="46" height="58" rx="6" fill="#2a9d8f"/>' +
               '<rect x="204" y="146" width="58" height="12" rx="4" fill="#1d7a6e"/>' +
               '<rect x="150" y="238" width="18" height="12" rx="3" fill="#e63946"/>' +
               '<rect x="300" y="252" width="16" height="10" rx="3" fill="#ffb703"/>' +
               '<circle cx="262" cy="256" r="7" fill="#9aa4b2"/>' +
               kid(120, 214, "#c68642", "#8e7dbe", {});
      },
      en: { q: "You are in a park and there is litter on the grass. The bin is a few steps away and none of it is yours. What does Canada ask of you?",
            a: ["Nothing — you did not drop it",
                "Protecting and enjoying our heritage and environment is one of the responsibilities Canada asks of everyone",
                "Report whoever dropped it"],
            c: 1,
            e: "Protecting and enjoying our heritage and environment is listed as a responsibility of everyone in Canada, right alongside obeying the law and helping others. Nobody checks who dropped it." },
      fr: { q: "Tu es dans un parc et il y a des d&eacute;chets sur l'herbe. La poubelle est &agrave; quelques pas et rien n'est &agrave; toi. Que te demande le Canada ?",
            a: ["Rien : ce n'est pas toi qui les as jet&eacute;s",
                "Prot&eacute;ger et appr&eacute;cier notre patrimoine et notre environnement est une des responsabilit&eacute;s demand&eacute;es &agrave; tous",
                "Signaler celui qui les a jet&eacute;s"],
            c: 1,
            e: "Prot&eacute;ger et appr&eacute;cier notre patrimoine et notre environnement figure parmi les responsabilit&eacute;s de chacun au Canada, au m&ecirc;me titre que respecter la loi et aider les autres. Personne ne v&eacute;rifie qui a jet&eacute; quoi." } },

    /* 9 — helping others in the community, the Canadian winter version. */
    { id: "snow",
      draw: function () {
        return ground(SNOW, "#cddff0") +
               '<rect x="300" y="120" width="150" height="94" fill="#c98b8b"/>' +
               '<polygon points="290,120 375,80 460,120" fill="#8a5a5a"/>' +
               '<rect x="352" y="164" width="30" height="50" fill="#6b4f3a"/>' +
               '<rect x="240" y="214" width="230" height="22" fill="#ffffff"/>' +
               kid(150, 214, "#f2c6a0", "#e63946", {}) +
               '<path d="M160 190 l40 26" stroke="#8a6a4a" stroke-width="5" stroke-linecap="round"/>' +
               '<path d="M196 212 l22 0 l0 12 l-26 0 Z" fill="#9aa4b2"/>' +
               kid(400, 214, "#f6d5c0", "#8e7dbe", { flip: true, hair: "#d8d8d8" });
      },
      en: { q: "It snowed overnight. Your elderly neighbour's walk is buried and she cannot clear it herself. You have a shovel. What does Canada ask of you?",
            a: ["Nothing — it is her walk, not yours",
                "Helping others in the community is one of the responsibilities Canada asks of everyone",
                "Wait until somebody pays you to do it"],
            c: 1,
            e: "Helping others in the community is on the official list of what Canada asks of everyone here — not a law you can be fined for, but one of the things the country says being Canadian means." },
      fr: { q: "Il a neig&eacute; pendant la nuit. L'all&eacute;e de ta voisine &acirc;g&eacute;e est ensevelie et elle ne peut pas la d&eacute;neiger. Tu as une pelle. Que te demande le Canada ?",
            a: ["Rien : c'est son all&eacute;e, pas la tienne",
                "Aider les autres dans la communaut&eacute; est une des responsabilit&eacute;s demand&eacute;es &agrave; tous",
                "Attendre que quelqu'un te paie pour le faire"],
            c: 1,
            e: "Aider les autres dans sa communaut&eacute; figure sur la liste officielle de ce que le Canada demande &agrave; chacun : pas une loi qui peut vous valoir une amende, mais une des choses que le pays consid&egrave;re comme faire partie d'&ecirc;tre Canadien." } },

    /* 10 — belonging. Equality again, because it is the one worth twice. */
    { id: "belong",
      draw: function (fr) {
        return ground() + school(300, 128) +
               kid(120, 214, "#5c3a21", "#ffb703", {}) +
               kid(196, 214, "#f2c6a0", "#4895ef", { flip: true }) +
               bubble(40, 50, 240, 56,
                      fr ? ["Retourne d'o&ugrave;", "tu viens."]
                         : ["Go back to where", "you came from."], "#fdf3f4");
      },
      en: { q: "Somebody tells a boy in your class to go back where he came from. He was born here, and it would be just as wrong if he was not. What is true?",
            a: ["He has to prove he was born here",
                "Everyone in Canada is treated with the same respect and dignity, whether they were born here or came here",
                "It is only a joke if he laughs"],
            c: 1,
            e: "Canada is built out of people who came from somewhere else and people who were here first. Where somebody was born changes nothing about the respect they are owed — and this is worth telling an adult about, because the boy should not have to answer it alone." },
      fr: { q: "Quelqu'un dit &agrave; un gar&ccedil;on de ta classe de retourner d'o&ugrave; il vient. Il est n&eacute; ici, et ce serait tout aussi mal s'il ne l'&eacute;tait pas. Qu'est-ce qui est vrai ?",
            a: ["Il doit prouver qu'il est n&eacute; ici",
                "Au Canada, chacun est trait&eacute; avec le m&ecirc;me respect et la m&ecirc;me dignit&eacute;, qu'il soit n&eacute; ici ou venu d'ailleurs",
                "Ce n'est une blague que s'il en rit"],
            c: 1,
            e: "Le Canada est fait de gens venus d'ailleurs et de peuples qui &eacute;taient ici les premiers. L'endroit de naissance ne change rien au respect qui est d&ucirc; &agrave; une personne — et cela vaut la peine d'en parler &agrave; un adulte, car ce gar&ccedil;on ne devrait pas avoir &agrave; r&eacute;pondre seul." } }
  ];
}());
