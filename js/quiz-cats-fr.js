/* canada-quiz.com — French names for the quiz topic cards.
 *
 * Found 29 September 2026 while testing the Back button: eight of the nine
 * multi-topic quiz pages printed their topic cards in ENGLISH on the French
 * side of the site. About fifty cards. fr/money-quiz.html offered "Canadian
 * Money" and "Saving & Spending"; fr/canada-quiz.html offered "History: 1700s"
 * and "Famous Canadians". Only gk-quiz was right, because it alone runs its
 * subject names through its own T() helper.
 *
 * Why every check missed it: these names are not words in the page. They are
 * the KEYS of each page's BANK object, and the cards are built from them at
 * run time. tools/newq/frbody.py reads the markup, so there was no English in
 * the markup for it to find. Same shape of blind spot as the image-metadata
 * rule in the project notes — a check that cannot see the format the content
 * is in is not a check.
 *
 * Why the keys are not simply translated: they are also the lookup handles
 * into BANK and part of the localStorage key that remembers which questions a
 * player has already seen (LSKEY + name). Renaming them would throw away every
 * player's progress and break the lookups. So the keys stay exactly as they
 * are and only what the reader sees is swapped, here, after the cards exist.
 *
 * The alternative was to register all fifty through T() and the site
 * dictionary, and call window.CQ.translateNode on each card. That is more in
 * the grain of the rest of the site, but the dictionary arrives asynchronously
 * and these cards are built at run time, so the ordering is a race. An explicit
 * map is duller and cannot break anything that already works.
 *
 * Load this BEFORE js/quiz-back.js: that file takes a topic's address slug from
 * the heading the card prints, so the French pages get French slugs
 * (#argent-canadien) rather than English ones.
 */
(function () {
  "use strict";

  if (!/(^|\/)fr\/[^\/]*$/.test(location.pathname)) return;

  /* English key -> what a French reader sees.
     House style follows gk-quiz's own SUBJ_FR: "et" rather than "&", and
     sentence case rather than Title Case. */
  var FR = {
    /* money-quiz */
    "Canadian Money": "Argent canadien",
    "Saving & Spending": "Épargner et dépenser",
    "Banks & Interest": "Banques et intérêts",
    "Earning & Jobs": "Revenus et emplois",
    "Smart Shopping": "Achats intelligents",
    "Needs vs Wants": "Besoins et désirs",

    /* canada-quiz */
    "History: 1700s": "Histoire : les années 1700",
    "History: 1800s": "Histoire : les années 1800",
    "History: 1900s": "Histoire : les années 1900",
    "Culture & Food": "Culture et cuisine",
    "Geography": "Géographie",
    "Famous Canadians": "Canadiens célèbres",
    "Hockey & Sports": "Hockey et sports",
    "Canadian Inventions": "Inventions canadiennes",

    /* ai-quiz */
    "How Computers Work": "Le fonctionnement des ordinateurs",
    "Artificial Intelligence": "Intelligence artificielle",
    "The Internet": "Internet",
    "Robots & Machines": "Robots et machines",
    "Coding Basics": "Bases de la programmation",
    "Staying Safe Online": "La sécurité en ligne",

    /* body-quiz */
    "Bones & Muscles": "Os et muscles",
    "Heart & Blood": "Cœur et sang",
    "Brain & Senses": "Cerveau et sens",
    "Food & Nutrition": "Alimentation et nutrition",
    "Germs & Staying Well": "Microbes et bonne santé",
    "Sleep, Exercise & Growing": "Sommeil, exercice et croissance",

    /* earth-quiz */
    "Our Planet Earth": "Notre planète Terre",
    "Weather & Climate": "Météo et climat",
    "Oceans & Water": "Océans et eau",
    "Forests & Wildlife": "Forêts et faune",
    "Recycling & Waste": "Recyclage et déchets",
    "Energy & Saving Power": "Énergie et économie d'énergie",

    /* entertainment-quiz */
    "Movies & TV": "Cinéma et télévision",
    "Music": "Musique",
    "Sports": "Sports",
    "Food Around the World": "Cuisines du monde",
    "Video Games": "Jeux vidéo",
    "Books & Cartoons": "Livres et dessins animés",

    /* science-quiz */
    "Space & Planets": "Espace et planètes",
    "Animals & Nature": "Animaux et nature",
    "The Human Body": "Le corps humain",
    "How Things Work": "Le fonctionnement des choses",
    "Weather & Earth": "Météo et Terre",
    "Numbers & Math": "Nombres et mathématiques",

    /* world-quiz */
    "Flags of the World": "Drapeaux du monde",
    "Capital Cities": "Capitales",
    "Famous Landmarks": "Monuments célèbres",
    "World Geography": "Géographie mondiale",
    "Countries & Cultures": "Pays et cultures",
    "Rivers, Mountains & Oceans": "Fleuves, montagnes et océans"
  };

  var root = document.getElementById("start-screen")
          || document.getElementById("start");

  var busy = false;

  function swap() {
    if (busy) return 0;
    busy = true;
    var done = 0;
    var box = root || document;
    Array.prototype.forEach.call(box.querySelectorAll(".card h3"), function (h) {
      var en = h.textContent.trim();
      /* The "!== en" is not tidiness, it is the whole reason fr/gk-quiz.html
         does not hang. Some names are the same word in both languages —
         "Sports" and "Music" — and gk-quiz prints a subject called Sports.
         Writing textContent replaces the text node even when the string is
         identical, which is a childList mutation, which wakes the observer
         below, which calls this again, forever. The page froze solid: no
         DOMContentLoaded, no scripts, nothing. Found 29 September 2026. */
      if (FR[en] && FR[en] !== en) { h.textContent = FR[en]; done++; }
    });
    /* the aria-label the button carries names the topic too */
    Array.prototype.forEach.call(box.querySelectorAll(".card button[aria-label]"),
      function (b) {
        var lab = b.getAttribute("aria-label");
        for (var en in FR) {
          if (FR.hasOwnProperty(en) && FR[en] !== en && lab.indexOf(en) !== -1) {
            b.setAttribute("aria-label", lab.split(en).join(FR[en]));
            break;
          }
        }
      });
    busy = false;
    return done;
  }

  /* The cards are built by each page's own script, and on some pages that
     happens after a question bank loads, so keep looking for a short while
     rather than giving up on the first empty pass. */
  function run(tries) {
    if (swap() > 0) return;
    if (tries > 0) setTimeout(function () { run(tries - 1); }, 120);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { run(16); });
  } else {
    run(16);
  }

  /* a page that rebuilds its card list (gk-quiz does, when the difficulty
     changes) gets the swap again without needing to know about this file */
  if (window.MutationObserver && root) {
    new MutationObserver(function () { swap(); })
      .observe(root, { childList: true, subtree: true });
  }
})();
