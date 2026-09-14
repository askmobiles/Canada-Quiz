/* Word banks and in-game messages for Word Search and Word Groups.
   ------------------------------------------------------------------
   WHY THIS FILE EXISTS

   Both games used to keep their words inside the page's own inline <script>.
   That is the one place a string can never reach the French side:
   build_fr.py translates one text node at a time and leaves script contents
   alone, and split_fr.py scans a fixed list of .js FILES, not inline blocks.
   So every French visitor got a French page with an English word bank.

   Putting the banks in the dictionary would not fix it either, because a word
   bank is not a translation. A French grid needs French words that fit a
   French grid — CHIEN, not the French for DOG placed letter by letter into an
   English-shaped puzzle — and a French sorting puzzle needs categories a
   French speaker would actually group, like "Petits fruits".

   So both languages live here, side by side, and the page picks by its own
   lang attribute. Nothing to register, nothing to compile, and a rebuild
   cannot quietly drop one side.

   Grid letters are A-Z with no accents, which is how French word searches are
   normally printed. Messages carry their real accents and the space before
   ? ! ; that French typography needs. */
(function () {
  var tag = (document.documentElement.getAttribute("lang") || "en").toLowerCase();
  var fr = tag.indexOf("fr") === 0;

  var EN = {
    /* 3 levels, 15 words each, variety of topics */
    search: {
      Easy: ["DOG", "CAT", "SUN", "MOON", "STAR", "TREE", "FISH", "BIRD", "CAKE",
             "BALL", "FROG", "LION", "BEAR", "SNOW", "RAIN"],
      Medium: ["PLANET", "GUITAR", "ROCKET", "CASTLE", "JUNGLE", "PENGUIN", "VOLCANO",
               "DIAMOND", "TURTLE", "MARKET", "ISLAND", "RAINBOW", "PYRAMID",
               "DOLPHIN", "GARDEN"],
      Hard: ["ELEPHANT", "DINOSAUR", "MOUNTAIN", "ASTRONAUT", "CHOCOLATE", "KANGAROO",
             "HURRICANE", "ORCHESTRA", "PINEAPPLE", "SUBMARINE", "WATERFALL",
             "BUTTERFLY", "TELESCOPE", "CROCODILE", "HELICOPTER"]
    },
    groups: [
      [["Canadian animals", "Beaver", "Moose", "Loon", "Caribou"], ["Provinces", "Ontario", "Alberta", "Quebec", "Manitoba"], ["Winter things", "Snow", "Ice", "Toque", "Mittens"], ["Fruits", "Apple", "Banana", "Cherry", "Grape"]],
      [["Hockey words", "Puck", "Stick", "Goal", "Rink"], ["Colours", "Red", "Blue", "Green", "Yellow"], ["Canadian foods", "Poutine", "Nanaimo", "BeaverTail", "Butter tart"], ["Body parts", "Arm", "Leg", "Head", "Hand"]],
      [["Oceans", "Atlantic", "Pacific", "Arctic", "Indian"], ["Trees", "Maple", "Pine", "Oak", "Birch"], ["Weather", "Rain", "Wind", "Fog", "Storm"], ["Instruments", "Guitar", "Drums", "Piano", "Flute"]],
      [["Canadian cities", "Toronto", "Calgary", "Halifax", "Regina"], ["Farm animals", "Cow", "Pig", "Sheep", "Goat"], ["Shapes", "Circle", "Square", "Triangle", "Star"], ["Drinks", "Water", "Juice", "Milk", "Tea"]],
      [["In space", "Sun", "Moon", "Star", "Planet"], ["Sports", "Soccer", "Tennis", "Golf", "Boxing"], ["Kitchen", "Fork", "Spoon", "Plate", "Cup"], ["Birds", "Eagle", "Robin", "Owl", "Duck"]],
      [["Time", "Hour", "Minute", "Second", "Day"], ["Canadian coins", "Penny", "Nickel", "Dime", "Loonie"], ["Bugs", "Ant", "Bee", "Fly", "Moth"], ["Clothes", "Shirt", "Pants", "Hat", "Shoes"]],
      [["Reptiles", "Snake", "Lizard", "Turtle", "Gecko"], ["Canada symbols", "Flag", "Anthem", "Maple", "Poppy"], ["Vehicles", "Car", "Bus", "Train", "Truck"], ["Vegetables", "Carrot", "Potato", "Onion", "Pea"]],
      [["Continents", "Asia", "Africa", "Europe", "Australia"], ["Metals", "Gold", "Silver", "Iron", "Copper"], ["Feelings", "Happy", "Sad", "Angry", "Scared"], ["Berries", "Blueberry", "Strawberry", "Raspberry", "Cranberry"]]
    ],
    msg: {
      allFound: "🎉 You found them all! Try a new puzzle!",
      pickFour: "Pick exactly 4 words",
      solved: "🎉 You solved it! Great job!",
      groupFound: "Nice! Group found.",
      oneAway: "So close — one away!",
      notGroup: "Not a group. Try again!",
      outOfTries: "😅 Out of tries! Here were the groups."
    }
  };

  var FR = {
    search: {
      Easy: ["CHAT", "CHIEN", "LUNE", "ARBRE", "OURS", "LION", "NEIGE", "PLUIE",
             "POMME", "FLEUR", "BALLE", "SOLEIL", "OISEAU", "GATEAU", "ETOILE"],
      Medium: ["PLANETE", "GUITARE", "CHATEAU", "JUNGLE", "MANCHOT", "VOLCAN",
               "DIAMANT", "TORTUE", "MARCHE", "JARDIN", "DAUPHIN", "CASTOR",
               "ERABLE", "BALEINE", "RENARD"],
      Hard: ["ELEPHANT", "DINOSAURE", "MONTAGNE", "ASTRONAUTE", "CHOCOLAT",
             "KANGOUROU", "ORCHESTRE", "TELESCOPE", "CROCODILE", "HELICOPTERE",
             "PAPILLON", "AVALANCHE", "TERRITOIRE", "GLACIER", "CARIBOU"]
    },
    groups: [
      [["Animaux du Canada", "Castor", "Orignal", "Huard", "Caribou"], ["Provinces", "Ontario", "Alberta", "Quebec", "Manitoba"], ["L'hiver", "Neige", "Glace", "Tuque", "Mitaines"], ["Fruits", "Pomme", "Banane", "Cerise", "Raisin"]],
      [["Le hockey", "Rondelle", "Baton", "But", "Patinoire"], ["Couleurs", "Rouge", "Bleu", "Vert", "Jaune"], ["Mets canadiens", "Poutine", "Nanaimo", "Tourtiere", "Tire d'erable"], ["Le corps", "Bras", "Jambe", "Tete", "Main"]],
      [["Oceans", "Atlantique", "Pacifique", "Arctique", "Indien"], ["Arbres", "Erable", "Pin", "Chene", "Bouleau"], ["Le temps qu'il fait", "Pluie", "Vent", "Brouillard", "Orage"], ["Instruments", "Guitare", "Batterie", "Piano", "Flute"]],
      [["Villes canadiennes", "Toronto", "Calgary", "Halifax", "Regina"], ["Animaux de la ferme", "Vache", "Cochon", "Mouton", "Chevre"], ["Formes", "Cercle", "Carre", "Triangle", "Etoile"], ["Boissons", "Eau", "Jus", "Lait", "The"]],
      [["Dans l'espace", "Soleil", "Lune", "Etoile", "Planete"], ["Sports", "Soccer", "Tennis", "Golf", "Boxe"], ["La cuisine", "Fourchette", "Cuillere", "Assiette", "Tasse"], ["Oiseaux", "Aigle", "Merle", "Hibou", "Canard"]],
      [["Le temps qui passe", "Heure", "Minute", "Seconde", "Jour"], ["Pieces canadiennes", "Cent", "Cinq cents", "Dix cents", "Huard"], ["Insectes", "Fourmi", "Abeille", "Mouche", "Papillon"], ["Vetements", "Chemise", "Pantalon", "Chapeau", "Souliers"]],
      [["Reptiles", "Serpent", "Lezard", "Tortue", "Gecko"], ["Symboles du Canada", "Drapeau", "Hymne", "Erable", "Coquelicot"], ["Vehicules", "Auto", "Autobus", "Train", "Camion"], ["Legumes", "Carotte", "Patate", "Oignon", "Pois"]],
      [["Continents", "Asie", "Afrique", "Europe", "Australie"], ["Metaux", "Or", "Argent", "Fer", "Cuivre"], ["Emotions", "Heureux", "Triste", "Fache", "Effraye"], ["Petits fruits", "Bleuet", "Fraise", "Framboise", "Canneberge"]]
    ],
    msg: {
      allFound: "🎉 Vous les avez tous trouvés ! Essayez une nouvelle grille !",
      pickFour: "Choisissez exactement 4 mots",
      solved: "🎉 Vous avez tout trouvé ! Bravo !",
      groupFound: "Bien joué ! Groupe trouvé.",
      oneAway: "Tout près — il en manque un !",
      notGroup: "Ce n'est pas un groupe. Réessayez !",
      outOfTries: "😅 Plus d'essais ! Voici les groupes."
    }
  };

  window.CQWB = fr ? FR : EN;
})();
