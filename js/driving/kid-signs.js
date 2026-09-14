/* The signs a child actually meets, in a child's words.
   ------------------------------------------------------------------
   Twenty-eight of the eighty signs, chosen for the walk to school and the ride
   in the back seat rather than for a licence. Nothing here is about driving:
   a seven-year-old will not merge or park, but they will cross a road, wait at
   a light and stand at a railway line.

   Each sign carries a short NAME a child would say out loud and one line of
   WHAT IT TELLS YOU. The line matters more than the name — a child who can say
   "it means look both ways and walk, do not run" has understood the sign, and
   can explain it to a grown-up at dinner, which is the whole point.

   The grown-up names live in CQ_SIGN_META and are not repeated here.

   Both languages sit in this file rather than in the dictionary, because a
   script builds these strings after the page loads and build_fr.py never sees
   a string that does not exist until somebody taps. Same reason as
   js/word-banks.js. The French is written for a child too, not translated
   word for word from the English. */
window.CQ_KID_SIGNS = [
  { id: "stop",
    en: ["Stop", "Every car must stop here. Not slow down — stop."],
    fr: ["Arrêt", "Chaque auto doit s'arrêter ici. Pas ralentir — s'arrêter."] },

  { id: "yield",
    en: ["Let them go first", "The cars already on the road go before you do."],
    fr: ["Laissez passer", "Les autos déjà sur la route passent avant vous."] },

  { id: "ped-crossover",
    en: ["Crossing for people", "Point, wait for the cars to stop, then walk across."],
    fr: ["Passage pour piétons", "Pointez, attendez que les autos arrêtent, puis traversez."] },

  { id: "warn-pedestrian",
    en: ["People cross ahead", "Drivers are being told that people walk across here."],
    fr: ["Des gens traversent", "Ce panneau dit aux conducteurs que des gens traversent ici."] },

  { id: "warn-school-zone",
    en: ["School zone", "A school is close. Cars must go slowly and watch for children."],
    fr: ["Zone scolaire", "Une école est proche. Les autos roulent lentement et surveillent les enfants."] },

  { id: "warn-school-crossing",
    en: ["Children cross here", "This is where children are meant to cross the road."],
    fr: ["Les enfants traversent ici", "C'est ici que les enfants doivent traverser la rue."] },

  { id: "warn-school-bus",
    en: ["School bus stops ahead", "A school bus picks children up just ahead."],
    fr: ["Arrêt d'autobus scolaire", "Un autobus scolaire prend des enfants juste devant."] },

  { id: "stop-school-bus",
    en: ["Stop for the bus", "When the bus flashes its red lights, every car must stop."],
    fr: ["Arrêtez pour l'autobus", "Quand l'autobus clignote en rouge, toutes les autos doivent arrêter."] },

  { id: "warn-playground",
    en: ["Playground near", "Children play close by, so a ball or a child may come out."],
    fr: ["Terrain de jeu", "Des enfants jouent tout près : un ballon ou un enfant peut surgir."] },

  { id: "warn-railway",
    en: ["Train crossing ahead", "A train track crosses the road soon. Look and listen."],
    fr: ["Passage à niveau", "Une voie ferrée traverse la route bientôt. Regardez et écoutez."] },

  { id: "warn-crossbuck",
    en: ["Train track here", "The big white X means the track is right here. A train always wins."],
    fr: ["Voie ferrée ici", "Le grand X blanc veut dire que la voie est ici. Un train gagne toujours."] },

  { id: "warn-bicycle",
    en: ["Bikes on the road", "People on bikes share this road, so drivers must look for them."],
    fr: ["Des vélos sur la route", "Des cyclistes partagent la route : les conducteurs doivent les voir."] },

  { id: "warn-deer",
    en: ["Deer may cross", "Deer live near this road and can jump out, often at night."],
    fr: ["Attention aux cerfs", "Des cerfs vivent près de la route et peuvent bondir, surtout le soir."] },

  { id: "warn-moose",
    en: ["Moose may cross", "A moose is taller than a car, so this is a serious warning."],
    fr: ["Attention aux orignaux", "Un orignal est plus grand qu'une auto : l'avertissement est sérieux."] },

  { id: "no-bicycles",
    en: ["No bikes", "You may not ride a bike here. Walk it instead."],
    fr: ["Vélos interdits", "On ne peut pas rouler à vélo ici. Marchez à côté du vélo."] },

  { id: "no-pedestrians",
    en: ["No walking here", "It is not safe to walk on this road. Find another way."],
    fr: ["Interdit aux piétons", "Ce n'est pas sécuritaire de marcher ici. Prenez un autre chemin."] },

  { id: "no-entry",
    en: ["Do not go in", "Cars must not drive into this road. It is the wrong way."],
    fr: ["Accès interdit", "Les autos ne doivent pas entrer ici. C'est le mauvais sens."] },

  { id: "one-way",
    en: ["One way only", "Cars go one way here, so look that way first."],
    fr: ["Sens unique", "Les autos vont dans un seul sens : regardez de ce côté d'abord."] },

  { id: "speed-50",
    en: ["Fifty is the fastest", "No car may go faster than 50 on this road."],
    fr: ["Cinquante au maximum", "Aucune auto ne peut dépasser 50 sur cette route."] },

  { id: "light-red",
    en: ["Red light", "Cars stop. If you are walking, wait for your own signal."],
    fr: ["Feu rouge", "Les autos arrêtent. À pied, attendez votre propre signal."] },

  { id: "light-amber",
    en: ["Yellow light", "The light is about to turn red. Cars should be stopping."],
    fr: ["Feu jaune", "Le feu va passer au rouge. Les autos devraient arrêter."] },

  { id: "light-green",
    en: ["Green light", "Cars may go — but they still have to look for people crossing."],
    fr: ["Feu vert", "Les autos peuvent avancer, mais elles doivent quand même regarder les piétons."] },

  { id: "mark-crosswalk",
    en: ["White stripes to cross", "These painted stripes are the safe place to walk across."],
    fr: ["Bandes blanches pour traverser", "Ces bandes peintes sont l'endroit sûr pour traverser."] },

  { id: "mark-stop-line",
    en: ["The stop line", "Cars must stop behind this thick white line, not on top of it."],
    fr: ["La ligne d'arrêt", "Les autos doivent arrêter derrière cette ligne blanche, pas dessus."] },

  { id: "info-hospital",
    en: ["Hospital this way", "A blue sign points the way to help if someone is hurt."],
    fr: ["Hôpital par ici", "Un panneau bleu indique le chemin de l'aide si quelqu'un est blessé."] },

  { id: "warn-signal-ahead",
    en: ["Traffic lights ahead", "Lights are coming up, even if you cannot see them yet."],
    fr: ["Feux de circulation devant", "Des feux arrivent, même si on ne les voit pas encore."] },

  { id: "community-safety-zone",
    en: ["Extra careful zone", "Fines are doubled here because people get hurt on this stretch."],
    fr: ["Zone de prudence", "Les amendes sont doublées ici parce que des gens y sont blessés."] },

  { id: "no-parking",
    en: ["No parking", "Cars may not be left here. It would block the view."],
    fr: ["Stationnement interdit", "On ne peut pas laisser une auto ici : cela bloque la vue."] }
];
