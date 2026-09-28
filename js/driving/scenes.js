/* canada-quiz.com — "What Would You Do?" driving scenarios.
 *
 * WHY THIS FILE EXISTS
 * --------------------
 * Every driving page on this site asks questions in words: "What must you do
 * when a school bus has its red lights flashing?" That is how the written test
 * works, and it is worth practising. But it is not how driving works. On the
 * road you do not read a sentence — you LOOK at a corner and decide.
 *
 * So this bank is different. Each entry carries a SCENE: a bird's-eye drawing
 * of a real situation, with your car, the other cars, the sign or the light, the
 * pedestrian, the bus. The learner looks at the picture, picks what to do, and
 * finds out. js/driving-game.js draws the scene from the small description in
 * the "sc" field; nothing here is a photograph and nothing is copied.
 *
 * WHERE THE ANSWERS COME FROM
 * ---------------------------
 * Every one of the 35 situations is checked against the Official MTO Driver's
 * Handbook on ontario.ca, and each carries the chapter it came from in "s", so
 * a learner who does not believe an answer can go and read the rule. The
 * handbook's own words appear in the explanation wherever they are short enough
 * to quote.
 *
 * This is practice for the written G1 knowledge test and for understanding the
 * rules. It is not a road test, and passing it is not a licence.
 *
 * BOTH LANGUAGES LIVE HERE
 * ------------------------
 * Like every province bank, each string is stored in English and French side by
 * side, so the French page is built from French and never translated after the
 * fact. The drawing carries no words at all, which is why one scene serves both.
 */
(function () {
  "use strict";

  /* The handbook chapters, named once. */
  var SRC = {
    inter: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/driving-through-intersections",
      en: "Driver's Handbook — Driving through intersections",
      fr: "Guide du conducteur — Traverser les intersections"
    },
    lights: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/traffic-lights",
      en: "Driver's Handbook — Traffic lights",
      fr: "Guide du conducteur — Les feux de circulation"
    },
    signs: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/signs",
      en: "Driver's Handbook — Signs",
      fr: "Guide du conducteur — Les panneaux"
    },
    share: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/sharing-road-other-road-users",
      en: "Driver's Handbook — Sharing the road with other road users",
      fr: "Guide du conducteur — Partager la route"
    },
    dirs: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/changing-directions",
      en: "Driver's Handbook — Changing directions",
      fr: "Guide du conducteur — Changer de direction"
    },
    weather: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/driving-night-and-bad-weather",
      en: "Driver's Handbook — Driving at night and in bad weather",
      fr: "Guide du conducteur — Conduire la nuit et par mauvais temps"
    },
    stopping: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/stopping",
      en: "Driver's Handbook — Stopping",
      fr: "Guide du conducteur — L'arrêt"
    },
    marks: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/pavement-markings",
      en: "Driver's Handbook — Pavement markings",
      fr: "Guide du conducteur — Les marques sur la chaussée"
    },
    passing: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/changing-positions",
      en: "Driver's Handbook — Changing positions",
      fr: "Guide du conducteur — Changer de position"
    },
    parking: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/parking-along-roadways",
      en: "Driver's Handbook — Parking along roadways",
      fr: "Guide du conducteur — Le stationnement en bordure de route"
    },
    freeway: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/freeway-driving",
      en: "Driver's Handbook — Freeway driving",
      fr: "Guide du conducteur — La conduite sur autoroute"
    },
    situations: {
      u: "https://www.ontario.ca/document/official-mto-drivers-handbook/dealing-particular-situations",
      en: "Driver's Handbook — Dealing with particular situations",
      fr: "Guide du conducteur — Faire face à des situations particulières"
    },
    emerg: {
      u: "https://www.ontario.ca/page/driving-near-emergency-vehicles",
      en: "Ontario — Driving near emergency vehicles",
      fr: "Ontario — Conduire près des véhicules d'urgence"
    }
  };

  window.CQ_SCENE_SRC = SRC;

  window.CQ_SCENES = [

  /* ---------- who goes first ---------------------------------------- */
  {
    id: "allway-right",
    sc: { kind: "cross", signs: ["stop"], cars: [{ at: "right" }] },
    q: {
      en: "You and the other car reach this all-way stop at the same moment. Both of you have stopped. What now?",
      fr: "L'autre voiture et vous arrivez à cet arrêt toutes directions en même temps. Vous avez tous les deux immobilisé. Que faire ?"
    },
    a: [
      { en: "Let the car on your right go first", fr: "Laissez passer la voiture à votre droite" },
      { en: "Go first — the other car must yield to you", fr: "Passez d'abord — l'autre voiture doit vous céder le passage" },
      { en: "Go first if you are going straight through", fr: "Passez d'abord si vous allez tout droit" },
      { en: "Both of you edge forward together, slowly", fr: "Avancez tous les deux lentement en même temps" }
    ],
    c: 0,
    why: {
      en: "When two vehicles reach an all-way stop at the same time, “the vehicle on the left must yield to the vehicle on the right.” You are the one on the left.",
      fr: "Quand deux véhicules arrivent en même temps à un arrêt toutes directions, le véhicule de gauche doit céder le passage à celui de droite. Vous êtes celui de gauche."
    },
    s: "inter"
  },
  {
    id: "uncontrolled-right",
    sc: { kind: "cross", cars: [{ at: "right" }] },
    q: {
      en: "No signs. No lights. A car is arriving from your right at the same time as you. What do you do?",
      fr: "Aucun panneau. Aucun feu. Une voiture arrive de votre droite en même temps que vous. Que faites-vous ?"
    },
    a: [
      { en: "Slow down and let the car on your right go first", fr: "Ralentissez et laissez passer la voiture à votre droite" },
      { en: "Keep your speed — the bigger road always wins", fr: "Gardez votre vitesse — la route la plus large a toujours priorité" },
      { en: "Sound your horn and carry on through", fr: "Klaxonnez et continuez votre chemin" },
      { en: "Go first, because you are on the through street", fr: "Passez d'abord, car vous êtes sur la rue principale" }
    ],
    c: 0,
    why: {
      en: "At an intersection with no signs and no lights, “the vehicle approaching from the right has the right-of-way.”",
      fr: "À une intersection sans panneau ni feu, le véhicule qui arrive de la droite a la priorité."
    },
    s: "inter"
  },
  {
    id: "yield-sign",
    sc: { kind: "cross", signs: ["yield"], cars: [{ at: "left" }] },
    q: {
      en: "You face a yield sign and a car is already coming through the intersection. What do you do?",
      fr: "Vous faites face à un panneau « Cédez » et une voiture traverse déjà l'intersection. Que faites-vous ?"
    },
    a: [
      { en: "Let the traffic in the intersection go first", fr: "Laissez passer d'abord la circulation dans l'intersection" },
      { en: "Stop completely, every time, like a stop sign", fr: "Immobilisez-vous complètement, chaque fois, comme à un arrêt" },
      { en: "Speed up to get through before the other car", fr: "Accélérez pour passer avant l'autre voiture" },
      { en: "Nothing — a yield sign is only a warning", fr: "Rien — le panneau « Cédez » est seulement un avertissement" }
    ],
    c: 0,
    why: {
      en: "A yield sign “means you must let traffic in the intersection or close to it go first.” You slow, and you stop if that is what it takes.",
      fr: "Le panneau « Cédez » signifie que vous devez laisser passer d'abord la circulation qui est dans l'intersection ou tout près. Vous ralentissez, et vous arrêtez s'il le faut."
    },
    s: "signs"
  },
  {
    id: "blocked-intersection",
    sc: { kind: "cross", light: "green", cars: [{ at: "block" }, { at: "block2" }, { at: "block3" }] },
    q: {
      en: "Your light is green, but the traffic ahead has the intersection completely blocked. What do you do?",
      fr: "Votre feu est vert, mais la circulation devant bloque complètement l'intersection. Que faites-vous ?"
    },
    a: [
      { en: "Stop before you enter and wait until the traffic ahead moves on", fr: "Arrêtez avant d'y entrer et attendez que la circulation avance" },
      { en: "Move in anyway — a green light is your right of way", fr: "Entrez quand même — le feu vert vous donne priorité" },
      { en: "Enter halfway so nobody takes your place", fr: "Avancez à moitié pour que personne ne prenne votre place" },
      { en: "Turn right instead, whether or not you signalled", fr: "Tournez à droite à la place, avec ou sans clignotant" }
    ],
    c: 0,
    why: {
      en: "“When you approach an intersection on a main road, and the intersection is blocked with traffic, stop before entering the intersection and wait until the traffic ahead moves on.” A green light is permission, not a place to sit.",
      fr: "Si l'intersection est bloquée par la circulation, arrêtez avant d'y entrer et attendez que la circulation avance. Le feu vert est une permission, pas une place pour rester coincé."
    },
    s: "inter"
  },

  /* ---------- the lights -------------------------------------------- */
  {
    id: "amber-far",
    sc: { kind: "cross", light: "amber", you: { y: 292 } },
    q: {
      en: "The light turns yellow while you are still well back from the line. What do you do?",
      fr: "Le feu passe au jaune alors que vous êtes encore loin de la ligne. Que faites-vous ?"
    },
    a: [
      { en: "Stop — you can stop safely from here", fr: "Arrêtez — vous pouvez le faire sans danger d'ici" },
      { en: "Speed up to beat the red", fr: "Accélérez pour passer avant le rouge" },
      { en: "Keep the same speed and carry on through", fr: "Gardez la même vitesse et continuez" },
      { en: "Stop only if a police car is watching", fr: "Arrêtez seulement si une voiture de police vous observe" }
    ],
    c: 0,
    why: {
      en: "“A yellow — or amber — light means the red light is about to appear. You must stop if you can do so safely.” From this far back, you can.",
      fr: "Le feu jaune annonce le rouge. Vous devez arrêter si vous pouvez le faire sans danger. D'aussi loin, vous pouvez."
    },
    s: "lights"
  },
  {
    id: "amber-close",
    sc: { kind: "cross", light: "amber", you: { y: 232 }, behind: true },
    q: {
      en: "The light turns yellow just as your front wheels reach the line, with a car close behind you. What do you do?",
      fr: "Le feu passe au jaune au moment où vos roues avant atteignent la ligne, une voiture juste derrière vous. Que faites-vous ?"
    },
    a: [
      { en: "Carry on through with caution — you can no longer stop safely", fr: "Continuez avec prudence — vous ne pouvez plus arrêter sans danger" },
      { en: "Brake hard and stop on the line", fr: "Freinez fort et arrêtez sur la ligne" },
      { en: "Stop in the middle of the intersection", fr: "Arrêtez au milieu de l'intersection" },
      { en: "Reverse back behind the line", fr: "Reculez derrière la ligne" }
    ],
    c: 0,
    why: {
      en: "The rule has two halves: “You must stop if you can do so safely; otherwise, go with caution.” Slamming the brakes on the line with a car behind you is not stopping safely.",
      fr: "La règle a deux parties : vous devez arrêter si vous pouvez le faire sans danger, sinon passez avec prudence. Freiner brusquement sur la ligne avec une voiture derrière n'est pas sans danger."
    },
    s: "lights"
  },
  {
    id: "green-left",
    sc: { kind: "cross", light: "green", cars: [{ at: "onc" }], path: "left" },
    q: {
      en: "Green light, and you want to turn left. A car is coming straight at you from the other side. What do you do?",
      fr: "Feu vert, et vous voulez tourner à gauche. Une voiture arrive tout droit en face. Que faites-vous ?"
    },
    a: [
      { en: "Wait for the oncoming car to pass, then turn", fr: "Attendez que la voiture arrive et passe, puis tournez" },
      { en: "Turn now — a green light gives you the right of way", fr: "Tournez maintenant — le feu vert vous donne priorité" },
      { en: "Turn quickly in front of it before it arrives", fr: "Tournez vite devant elle avant qu'elle arrive" },
      { en: "Flash your headlights so it stops for you", fr: "Faites des appels de phares pour qu'elle s'arrête" }
    ],
    c: 0,
    why: {
      en: "A plain green light lets you turn left only after yielding: “you must wait for approaching traffic to pass or turn and for pedestrians in or approaching your path to cross.”",
      fr: "Un feu vert ordinaire permet de tourner à gauche seulement après avoir cédé : vous devez attendre que la circulation qui approche passe ou tourne, et que les piétons traversent."
    },
    s: "inter"
  },
  {
    id: "advance-green",
    sc: { kind: "cross", light: "arrow", path: "left" },
    q: {
      en: "You want to turn left and you face a green left arrow beside the green light. What does it mean?",
      fr: "Vous voulez tourner à gauche et vous voyez une flèche verte à gauche à côté du feu vert. Qu'est-ce que cela veut dire ?"
    },
    a: [
      { en: "You may turn left now — oncoming traffic is being held", fr: "Vous pouvez tourner à gauche maintenant — la circulation en face est retenue" },
      { en: "You must turn left; going straight is not allowed", fr: "Vous devez tourner à gauche ; aller tout droit est interdit" },
      { en: "The arrow is only a suggestion to move into the left lane", fr: "La flèche suggère seulement de vous placer dans la voie de gauche" },
      { en: "You may turn left but must still yield to oncoming cars", fr: "Vous pouvez tourner à gauche mais devez encore céder aux voitures en face" }
    ],
    c: 0,
    why: {
      en: "“When you face a flashing green light or a left-pointing green arrow and a green light, you may turn left, go straight ahead or turn right from the proper lane.” The oncoming side is stopped. Pedestrians still come first.",
      fr: "Avec une flèche verte vers la gauche et un feu vert, vous pouvez tourner à gauche, aller tout droit ou tourner à droite depuis la bonne voie. La circulation en face est arrêtée. Les piétons passent toujours avant."
    },
    s: "lights"
  },
  {
    id: "green-right-ped",
    sc: { kind: "cross", light: "green", ped: "right", path: "right" },
    q: {
      en: "Green light, you are turning right, and somebody steps into the crosswalk you are about to cross. What do you do?",
      fr: "Feu vert, vous tournez à droite, et quelqu'un s'engage dans le passage que vous allez traverser. Que faites-vous ?"
    },
    a: [
      { en: "Wait for them to finish crossing", fr: "Attendez qu'ils finissent de traverser" },
      { en: "Turn behind them while they are still walking", fr: "Tournez derrière eux pendant qu'ils marchent encore" },
      { en: "Turn in front of them — you have a green light", fr: "Tournez devant eux — vous avez le feu vert" },
      { en: "Edge forward until they hurry up", fr: "Avancez petit à petit pour qu'ils se pressent" }
    ],
    c: 0,
    why: {
      en: "“When turning left or right you must yield the right-of-way to pedestrians crossing the intersection.” The whole crossing, not the half you want.",
      fr: "En tournant à gauche ou à droite, vous devez céder le passage aux piétons qui traversent l'intersection. Tout le passage, pas seulement la moitié qui vous arrange."
    },
    s: "lights"
  },
  {
    id: "red-right",
    sc: { kind: "cross", light: "red", path: "right" },
    q: {
      en: "Red light, you want to turn right, and there is no sign forbidding it. What do you do?",
      fr: "Feu rouge, vous voulez tourner à droite, et aucun panneau ne l'interdit. Que faites-vous ?"
    },
    a: [
      { en: "Come to a complete stop first, then turn when the way is clear", fr: "Immobilisez-vous complètement d'abord, puis tournez quand la voie est libre" },
      { en: "Slow right down, then roll around the corner", fr: "Ralentissez beaucoup, puis tournez sans arrêter" },
      { en: "Wait for the green — right on red is not allowed in Ontario", fr: "Attendez le vert — le virage à droite au rouge est interdit en Ontario" },
      { en: "Turn at once if no car is coming", fr: "Tournez tout de suite si aucune voiture n'arrive" }
    ],
    c: 0,
    why: {
      en: "“You may turn right on a red light only after coming to a complete stop and waiting until the way is clear.” Both halves matter: the full stop, and the clear way.",
      fr: "Vous pouvez tourner à droite au feu rouge seulement après un arrêt complet et une fois la voie libre. Les deux parties comptent."
    },
    s: "lights"
  },
  {
    id: "flashing-red",
    sc: { kind: "cross", light: "flashRed" },
    q: {
      en: "The light above your lane is a red light flashing on and off. What do you do?",
      fr: "Le feu au-dessus de votre voie est un feu rouge clignotant. Que faites-vous ?"
    },
    a: [
      { en: "Come to a complete stop, then go when it is safe", fr: "Immobilisez-vous complètement, puis avancez quand c'est sécuritaire" },
      { en: "Slow down and drive through with caution", fr: "Ralentissez et traversez avec prudence" },
      { en: "Treat it as a broken light and carry on", fr: "Considérez-le comme un feu en panne et continuez" },
      { en: "Stop and wait until it turns green", fr: "Arrêtez et attendez qu'il passe au vert" }
    ],
    c: 0,
    why: {
      en: "“You must come to a complete stop at a flashing red light. Move through the intersection only when it is safe.” It behaves like a stop sign.",
      fr: "Vous devez vous immobiliser complètement à un feu rouge clignotant, puis traverser seulement quand c'est sécuritaire. Il se comporte comme un arrêt."
    },
    s: "lights"
  },
  {
    id: "flashing-amber",
    sc: { kind: "cross", light: "flashAmber" },
    q: {
      en: "The light above your lane is a yellow light flashing on and off. What do you do?",
      fr: "Le feu au-dessus de votre voie est un feu jaune clignotant. Que faites-vous ?"
    },
    a: [
      { en: "Drive through with caution", fr: "Traversez avec prudence" },
      { en: "Come to a complete stop first", fr: "Immobilisez-vous complètement d'abord" },
      { en: "Stop and wait for a green light", fr: "Arrêtez et attendez le feu vert" },
      { en: "Carry on at full speed — yellow flashing means go", fr: "Continuez à pleine vitesse — le jaune clignotant veut dire « allez »" }
    ],
    c: 0,
    why: {
      en: "“A flashing yellow light means you should drive with caution when approaching and moving through the intersection.” Caution, not a stop — and not full speed either.",
      fr: "Un feu jaune clignotant signifie qu'il faut conduire avec prudence en approchant et en traversant l'intersection. De la prudence, pas un arrêt — et pas la pleine vitesse."
    },
    s: "lights"
  },

  /* ---------- the school bus ---------------------------------------- */
  {
    id: "bus-behind",
    sc: { kind: "road", bus: "ahead", you: { y: 262 } },
    q: {
      en: "You are following this school bus and its upper red lights start flashing. What do you do?",
      fr: "Vous suivez cet autobus scolaire et ses feux rouges supérieurs se mettent à clignoter. Que faites-vous ?"
    },
    a: [
      { en: "Stop at least 20 metres behind the bus and wait", fr: "Arrêtez à au moins 20 mètres derrière l'autobus et attendez" },
      { en: "Pass on the left, slowly and carefully", fr: "Dépassez à gauche, lentement et prudemment" },
      { en: "Slow to walking speed and keep rolling past", fr: "Ralentissez au pas et continuez à avancer" },
      { en: "Stop only if you can see children on the road", fr: "Arrêtez seulement si vous voyez des enfants sur la route" }
    ],
    c: 0,
    why: {
      en: "“You must stop whether you are behind or approaching the bus” and “stop at least 20 metres away.” Wait for the lights to stop flashing before you move.",
      fr: "Vous devez arrêter, que vous soyez derrière l'autobus ou que vous l'approchiez, à au moins 20 mètres. Attendez la fin du clignotement avant de repartir."
    },
    s: "share"
  },
  {
    id: "bus-oncoming",
    sc: { kind: "road", bus: "onc", you: { y: 262 } },
    q: {
      en: "On this two-way road with no median, a school bus coming the other way has its red lights flashing. What do you do?",
      fr: "Sur cette route à double sens sans terre-plein, un autobus scolaire venant en sens inverse a ses feux rouges clignotants. Que faites-vous ?"
    },
    a: [
      { en: "Stop — traffic must stop from both directions here", fr: "Arrêtez — la circulation doit s'arrêter dans les deux sens ici" },
      { en: "Carry on — the bus is not in your lane", fr: "Continuez — l'autobus n'est pas dans votre voie" },
      { en: "Slow down but keep moving", fr: "Ralentissez mais continuez d'avancer" },
      { en: "Move over to the shoulder and keep going", fr: "Déplacez-vous sur l'accotement et continuez" }
    ],
    c: 0,
    why: {
      en: "“You must stop whether you are behind or approaching the bus.” On a road with no median, oncoming traffic stops too — children may be crossing to your side.",
      fr: "Vous devez arrêter, que vous soyez derrière l'autobus ou que vous l'approchiez. Sans terre-plein, la circulation en sens inverse arrête aussi — des enfants peuvent traverser vers votre côté."
    },
    s: "share"
  },
  {
    id: "bus-divided",
    sc: { kind: "divided", bus: "onc", you: { y: 250 } },
    q: {
      en: "A school bus on the far side of a median has its red lights flashing. You are going the other way. What do you do?",
      fr: "Un autobus scolaire de l'autre côté d'un terre-plein a ses feux rouges clignotants. Vous allez en sens inverse. Que faites-vous ?"
    },
    a: [
      { en: "Carry on — with a median between you, only traffic behind the bus must stop", fr: "Continuez — avec un terre-plein entre vous, seule la circulation derrière l'autobus doit arrêter" },
      { en: "Stop, exactly as on any other road", fr: "Arrêtez, exactement comme sur toute autre route" },
      { en: "Stop only if you can see the driver", fr: "Arrêtez seulement si vous voyez le conducteur" },
      { en: "Cross the median and stop behind the bus", fr: "Traversez le terre-plein et arrêtez derrière l'autobus" }
    ],
    c: 0,
    why: {
      en: "This is the one exception: on divided highways with median strips, only vehicles approaching from the rear must stop. A median is a real barrier, not a painted line — if it is only paint, you stop.",
      fr: "C'est la seule exception : sur une route divisée par un terre-plein, seuls les véhicules qui approchent par l'arrière doivent arrêter. Un terre-plein est une vraie séparation, pas une ligne peinte — si c'est de la peinture, vous arrêtez."
    },
    s: "share"
  },

  /* ---------- people outside cars ----------------------------------- */
  {
    id: "ped-crossover",
    sc: { kind: "road", sign: "ped-crossover", ped: "cross", you: { y: 262 } },
    q: {
      en: "Somebody is stepping onto a pedestrian crossover ahead of you. What do you do?",
      fr: "Quelqu'un s'engage sur un passage pour piétons devant vous. Que faites-vous ?"
    },
    a: [
      { en: "Stop and let them cross the whole road before you go", fr: "Arrêtez et laissez-les traverser toute la chaussée avant de repartir" },
      { en: "Go once they pass the middle of the road", fr: "Repartez dès qu'ils ont dépassé le milieu de la chaussée" },
      { en: "Drive slowly around behind them", fr: "Passez lentement derrière eux" },
      { en: "Carry on if they have not stepped off the curb yet", fr: "Continuez s'ils n'ont pas encore quitté le trottoir" }
    ],
    c: 0,
    why: {
      en: "“Drivers, including cyclists, must stop and yield the whole roadway at pedestrian crossovers, school crossings and other locations where there is a crossing guard.” The whole roadway — you wait until they are off the road.",
      fr: "Les conducteurs, y compris les cyclistes, doivent arrêter et céder toute la chaussée aux passages pour piétons, aux passages scolaires et là où il y a un brigadier. Toute la chaussée — vous attendez qu'ils l'aient quittée."
    },
    s: "share"
  },
  {
    id: "cyclist-pass",
    sc: { kind: "road", bike: "ahead", you: { y: 262 } },
    q: {
      en: "A cyclist is riding along the right edge ahead of you and you want to pass. What do you do?",
      fr: "Un cycliste roule au bord droit devant vous et vous voulez le dépasser. Que faites-vous ?"
    },
    a: [
      { en: "Pass only when you can leave at least one metre of space", fr: "Dépassez seulement quand vous pouvez laisser au moins un mètre d'espace" },
      { en: "Pass close but slowly, staying in your lane", fr: "Dépassez de près mais lentement, en restant dans votre voie" },
      { en: "Sound your horn and pass", fr: "Klaxonnez et dépassez" },
      { en: "Follow right behind until the cyclist turns off", fr: "Suivez juste derrière jusqu'à ce que le cycliste tourne" }
    ],
    c: 0,
    why: {
      en: "“When passing a cyclist, drivers of motor vehicles must maintain a minimum distance of one metre, where practical.” If the lane is too narrow for that, you wait.",
      fr: "En dépassant un cycliste, il faut garder au moins un mètre de distance, dans la mesure du possible. Si la voie est trop étroite pour cela, vous attendez."
    },
    s: "share"
  },
  {
    id: "cyclist-left-turn",
    sc: { kind: "cross", light: "green", bike: "onc", path: "left" },
    q: {
      en: "You are turning left at this green light and a cyclist is coming straight towards you. What do you do?",
      fr: "Vous tournez à gauche à ce feu vert et un cycliste vient droit vers vous. Que faites-vous ?"
    },
    a: [
      { en: "Stop and wait for the bicycle to pass, then turn", fr: "Arrêtez et attendez que le vélo passe, puis tournez" },
      { en: "Turn in front of the bicycle — a car has priority", fr: "Tournez devant le vélo — une voiture a priorité" },
      { en: "Turn wide around behind the bicycle", fr: "Tournez large derrière le vélo" },
      { en: "Carry on and let the cyclist steer around you", fr: "Continuez et laissez le cycliste vous contourner" }
    ],
    c: 0,
    why: {
      en: "A bicycle coming the other way is oncoming traffic: “you must stop and wait for oncoming bicycles to pass before turning.” Bikes are easy to misjudge — they arrive faster than they look.",
      fr: "Un vélo qui vient en sens inverse fait partie de la circulation venant en face : vous devez arrêter et attendre qu'il passe avant de tourner. On sous-estime facilement leur vitesse."
    },
    s: "share"
  },

  /* ---------- emergency vehicles ------------------------------------ */
  {
    id: "emerg-behind",
    sc: { kind: "cross", emerg: "behind", you: { y: 226 } },
    q: {
      en: "A fire truck is behind you with its lights and siren on, and you are almost at an intersection. What do you do?",
      fr: "Un camion d'incendie est derrière vous, gyrophares et sirène en marche, et vous êtes presque à une intersection. Que faites-vous ?"
    },
    a: [
      { en: "Signal, move to the right side of the road clear of the intersection, and stop", fr: "Signalez, rangez-vous à droite hors de l'intersection, puis arrêtez" },
      { en: "Stop right where you are, in the intersection", fr: "Arrêtez sur place, dans l'intersection" },
      { en: "Speed up to get out of its way", fr: "Accélérez pour vous écarter de son chemin" },
      { en: "Pull to the left, because it will pass on the right", fr: "Rangez-vous à gauche, car il passera à droite" }
    ],
    c: 0,
    why: {
      en: "The steps are: “Slow down. Signal. Move to the right side of the road, clear of any intersection. Stop.” Stopping inside the intersection blocks the very route the truck needs.",
      fr: "Les étapes sont : ralentir, signaler, se ranger à droite hors de toute intersection, arrêter. Arrêter dans l'intersection bloque justement le passage dont le camion a besoin."
    },
    s: "emerg"
  },
  {
    id: "emerg-shoulder",
    sc: { kind: "road", twoLane: true, police: true, you: { y: 268 } },
    q: {
      en: "A police car is stopped on the right shoulder with its lights flashing. There are two lanes your way. What do you do?",
      fr: "Une voiture de police est arrêtée sur l'accotement de droite, gyrophares allumés. Il y a deux voies dans votre sens. Que faites-vous ?"
    },
    a: [
      { en: "Slow down and, if it is safe, move over to leave a lane of space", fr: "Ralentissez et, si c'est sécuritaire, changez de voie pour laisser une voie d'espace" },
      { en: "Keep your speed — it is stopped, so it is not in your way", fr: "Gardez votre vitesse — elle est arrêtée, donc elle ne vous gêne pas" },
      { en: "Stop behind it and wait", fr: "Arrêtez derrière elle et attendez" },
      { en: "Move over only if an officer waves you across", fr: "Changez de voie seulement si un agent vous fait signe" }
    ],
    c: 0,
    why: {
      en: "“You can be charged if you don’t slow down or move over for emergency vehicles or tow trucks that are stopped with sirens or lights flashing,” and “if a road has two or more lanes, you must leave a lane of space” when it is safe to do so.",
      fr: "Vous pouvez recevoir une contravention si vous ne ralentissez pas ou ne changez pas de voie pour un véhicule d'urgence ou une dépanneuse arrêtée avec gyrophares ou sirène. Sur une route à deux voies ou plus, il faut laisser une voie d'espace quand c'est sécuritaire."
    },
    s: "emerg"
  },

  /* ---------- roundabouts ------------------------------------------- */
  {
    id: "round-entry",
    sc: { kind: "round", cars: [{ at: "in" }] },
    q: {
      en: "You are at the entrance to this roundabout and a car is already going around it. What do you do?",
      fr: "Vous êtes à l'entrée de ce carrefour giratoire et une voiture y circule déjà. Que faites-vous ?"
    },
    a: [
      { en: "Yield — wait for the car already in the roundabout", fr: "Cédez le passage — attendez la voiture déjà dans le giratoire" },
      { en: "Enter first, because you are on its right", fr: "Entrez d'abord, car vous êtes à sa droite" },
      { en: "Stop completely and wait until the roundabout is empty", fr: "Arrêtez complètement et attendez que le giratoire soit vide" },
      { en: "Enter and go clockwise to keep out of its way", fr: "Entrez et tournez dans le sens des aiguilles pour l'éviter" }
    ],
    c: 0,
    why: {
      en: "“Traffic in the roundabout has the right-of-way.” You yield on entry, and “once in the roundabout, always keep to the right of the central island and travel in a counter-clockwise direction.”",
      fr: "La circulation dans le giratoire a la priorité. Vous cédez le passage à l'entrée puis, à l'intérieur, vous restez à droite de l'îlot central et circulez dans le sens antihoraire."
    },
    s: "dirs"
  },
  {
    id: "round-signal",
    sc: { kind: "round", inside: true },
    q: {
      en: "You are going around this roundabout and you want the next exit but one. When do you signal right?",
      fr: "Vous circulez dans ce giratoire et vous voulez la sortie suivant la prochaine. Quand signalez-vous à droite ?"
    },
    a: [
      { en: "Once you have passed the exit before the one you want", fr: "Une fois passée la sortie qui précède celle que vous voulez" },
      { en: "Before you enter the roundabout", fr: "Avant d'entrer dans le giratoire" },
      { en: "As you leave the exit, once you are out", fr: "En quittant la sortie, une fois dehors" },
      { en: "Not at all — signals are not used in roundabouts", fr: "Jamais — on n'utilise pas les clignotants dans un giratoire" }
    ],
    c: 0,
    why: {
      en: "“Once you have passed the exit before the one you want, use your right-turn signal.” Signalling any earlier tells the driver waiting at that exit that you are coming out there, and they may pull in front of you.",
      fr: "Une fois passée la sortie précédant la vôtre, mettez votre clignotant droit. Plus tôt, vous dites au conducteur qui attend à cette sortie que vous sortez là — et il peut s'engager devant vous."
    },
    s: "dirs"
  },

  /* ---------- the railway ------------------------------------------- */
  {
    id: "railway-ahead",
    sc: { kind: "road", sign: "warn-railway", tracks: true, you: { y: 268 } },
    q: {
      en: "You see this sign at the roadside. What does it tell you to do?",
      fr: "Vous voyez ce panneau au bord de la route. Que vous dit-il de faire ?"
    },
    a: [
      { en: "Slow down, look both ways for a train and be ready to stop", fr: "Ralentir, regarder des deux côtés s'il vient un train et être prêt à arrêter" },
      { en: "Stop completely every time, train or no train", fr: "Arrêter complètement chaque fois, qu'il y ait un train ou non" },
      { en: "Speed up to clear the tracks quickly", fr: "Accélérer pour franchir la voie rapidement" },
      { en: "Nothing — the flashing lights will warn you if a train is coming", fr: "Rien — les feux clignotants vous avertiront s'il vient un train" }
    ],
    c: 0,
    why: {
      en: "“A railway crossing sign is X-shaped with a white background and red outline. It warns that railway tracks cross the road. Watch for this sign. Slow down and look both ways for trains. Be prepared to stop.” Not every crossing has lights or gates.",
      fr: "Le panneau de passage à niveau, en forme de X blanc bordé de rouge, avertit qu'une voie ferrée croise la route : ralentir, regarder des deux côtés, être prêt à arrêter. Tous les passages à niveau n'ont pas de feux ni de barrières."
    },
    s: "signs"
  },

  /* ---------- weather ---------------------------------------------- */
  {
    id: "fog",
    sc: { kind: "road", fog: true, cars: [{ at: "ahead" }], you: { y: 262 } },
    q: {
      en: "You drive into thick fog. What do you do with your lights and your following distance?",
      fr: "Vous entrez dans un brouillard épais. Que faites-vous de vos phares et de votre distance de suivi ?"
    },
    a: [
      { en: "Low beams, and leave more space than usual", fr: "Feux de croisement, et laissez plus d'espace que d'habitude" },
      { en: "High beams, to see as far as possible", fr: "Feux de route, pour voir le plus loin possible" },
      { en: "Hazard lights, and stay close to the car ahead", fr: "Feux de détresse, et restez près de la voiture devant" },
      { en: "No lights at all, so you are not dazzled", fr: "Aucun phare, pour ne pas être aveuglé" }
    ],
    c: 0,
    why: {
      en: "“Use your low-beam headlights. High beams reflect off the moisture droplets in the fog, making it harder to see.” And “increase your following distance — you will need extra distance to brake safely.”",
      fr: "Utilisez vos feux de croisement : les feux de route se reflètent sur les gouttelettes et nuisent à la visibilité. Et augmentez votre distance de suivi : il vous faudra plus d'espace pour freiner."
    },
    s: "weather"
  },
  {
    id: "skid",
    sc: { kind: "road", snow: true, skid: true, you: { y: 250 } },
    q: {
      en: "On a snowy road the back of your car starts to slide sideways. What do you do?",
      fr: "Sur une route enneigée, l'arrière de votre voiture commence à glisser de côté. Que faites-vous ?"
    },
    a: [
      { en: "Ease off the accelerator or brake and keep steering where you want to go", fr: "Relâchez l'accélérateur ou le frein et continuez à diriger où vous voulez aller" },
      { en: "Brake as hard as you can", fr: "Freinez aussi fort que possible" },
      { en: "Steer the opposite way to the skid and hold it", fr: "Braquez du côté opposé au dérapage et maintenez" },
      { en: "Accelerate to straighten the car out", fr: "Accélérez pour redresser la voiture" }
    ],
    c: 0,
    why: {
      en: "“Ease off on the accelerator or brake… Continue to steer in the direction you wish to go.” The best move is earlier still: “avoid sudden steering, braking or accelerating that could cause a skid.”",
      fr: "Relâchez l'accélérateur ou le frein et continuez à diriger vers où vous voulez aller. Mieux encore, plus tôt : évitez les coups de volant, de frein ou d'accélérateur qui causent les dérapages."
    },
    s: "weather"
  },
  {
    id: "black-ice",
    sc: { kind: "road", ice: true, you: { y: 262 } },
    q: {
      en: "The road ahead looks like wet, shiny black asphalt, but the temperature is below freezing. What is it likely to be?",
      fr: "La chaussée devant semble noire, mouillée et luisante, mais il fait sous zéro. Qu'est-ce probablement ?"
    },
    a: [
      { en: "Black ice — slow down early and make no sudden moves", fr: "De la glace noire — ralentissez tôt et évitez tout geste brusque" },
      { en: "Fresh asphalt, which grips better than usual", fr: "De l'asphalte neuf, qui adhère mieux que d'habitude" },
      { en: "Rain, which is safe at any speed", fr: "De la pluie, sans danger à n'importe quelle vitesse" },
      { en: "Oil from traffic, which only matters on corners", fr: "De l'huile, qui ne compte que dans les virages" }
    ],
    c: 0,
    why: {
      en: "“If the road ahead looks like black and shiny asphalt, be suspicious. It may be covered by a thin layer of ice known as black ice.” Bridges, shaded spots and overpasses freeze first.",
      fr: "Si la chaussée semble noire et luisante, soyez méfiant : elle peut être couverte d'une mince couche de glace, la glace noire. Les ponts, les zones ombragées et les viaducs gèlent en premier."
    },
    s: "weather"
  },

  /* ---------- school zones, guards and work zones ------------------- */
  {
    id: "school-crossing-guard",
    sc: { kind: "road", sign: "warn-school-crossing", ped: "cross", you: { y: 262 } },
    q: {
      en: "The school crossing is marked and a crossing guard is still standing out in the road. The last child has just reached the far sidewalk. What do you do?",
      fr: "Le passage scolaire est marqué et un brigadier se tient encore sur la chaussée. Le dernier enfant vient d'atteindre le trottoir d'en face. Que faites-vous ?"
    },
    a: [
      { en: "Stay stopped until the guard is off the road too", fr: "Restez immobilisé jusqu'à ce que le brigadier ait lui aussi quitté la chaussée" },
      { en: "Go now — the children are across", fr: "Avancez maintenant : les enfants sont passés" },
      { en: "Edge forward slowly past the guard", fr: "Avancez doucement en dépassant le brigadier" },
      { en: "Go around the guard on the far side of the road", fr: "Contournez le brigadier par l'autre côté de la chaussée" }
    ],
    c: 0,
    why: {
      en: "You must stop before the crossing and “remain stopped until all people, including the school crossing guard, have cleared the entire roadway.” The guard is a person on the road, not a signal. Not stopping properly carries three demerit points.",
      fr: "Vous devez vous arrêter avant le passage et rester immobilisé jusqu'à ce que toutes les personnes, y compris le brigadier scolaire, aient complètement quitté la chaussée. Le brigadier est une personne sur la route, pas un feu. Ne pas s'arrêter correctement vaut trois points d'inaptitude."
    },
    s: "stopping"
  },
  {
    id: "community-safety-zone",
    sc: { kind: "road", sign: "community-safety-zone", you: { y: 262 } },
    q: {
      en: "You pass this sign. What has just changed for you as a driver?",
      fr: "Vous passez devant ce panneau. Qu'est-ce qui vient de changer pour vous comme conducteur ?"
    },
    a: [
      { en: "Nothing about the rules, but fines for breaking them go up here", fr: "Rien dans les règles, mais les amendes y sont plus élevées" },
      { en: "The speed limit automatically drops to 40 km/h", fr: "La limite de vitesse passe automatiquement à 40 km/h" },
      { en: "It only applies during school hours", fr: "Cela ne s'applique que pendant les heures d'école" },
      { en: "It is a warning sign with no legal effect", fr: "C'est un panneau d'avertissement sans effet juridique" }
    ],
    c: 0,
    why: {
      en: "The sign marks somewhere “the community has identified that there is a special risk to pedestrians,” and “traffic related offences committed within the zone are subject to increased fines.” The speed limit is whatever is posted — the sign does not change it by itself.",
      fr: "Le panneau signale un endroit où la communauté a jugé qu'il existe un risque particulier pour les piétons, et les infractions routières commises dans la zone entraînent des amendes plus élevées. La limite de vitesse reste celle qui est affichée : le panneau ne la change pas à lui seul."
    },
    s: "signs"
  },
  {
    id: "construction-flagger",
    sc: { kind: "road", sign: "temp-flagger", you: { y: 262 } },
    q: {
      en: "A traffic-control person in the work zone ahead is holding a STOP paddle towards you. What do you do?",
      fr: "Dans la zone de travaux devant vous, un signaleur brandit une palette ARRÊT dans votre direction. Que faites-vous ?"
    },
    a: [
      { en: "Stop, and wait until they signal you through", fr: "Arrêtez-vous et attendez son signal pour repartir" },
      { en: "Slow to a crawl and keep rolling past", fr: "Ralentissez au pas et continuez à rouler" },
      { en: "Obey the posted signs but treat the flagger as advisory", fr: "Obéissez aux panneaux, mais considérez le signaleur comme facultatif" },
      { en: "Change lanes and go around the closed section yourself", fr: "Changez de voie et contournez vous-même la section fermée" }
    ],
    c: 0,
    why: {
      en: "“It is also an offence to disobey STOP or SLOW signs displayed by a traffic-control person or firefighter.” The handbook also says plainly: in a construction zone, do not change lanes. Speeding fines are doubled where workers are present.",
      fr: "Désobéir aux panneaux ARRÊT ou LENTEMENT d'un signaleur ou d'un pompier est une infraction. Le guide dit aussi clairement de ne pas changer de voie dans une zone de travaux. Les amendes pour excès de vitesse y sont doublées lorsque des travailleurs sont présents."
    },
    s: "situations"
  },

  /* ---------- passing, merging and lane discipline ------------------ */
  {
    id: "solid-yellow-line",
    sc: { kind: "road", centre: "solid", cars: [{ at: "ahead" }], you: { y: 268 } },
    q: {
      en: "You are behind a slower car on a two-lane road. The centre line is solid yellow on your side, and the road ahead looks empty. Can you pass?",
      fr: "Vous suivez une voiture plus lente sur une route à deux voies. La ligne centrale est jaune continue de votre côté et la route devant paraît vide. Pouvez-vous dépasser ?"
    },
    a: [
      { en: "No — a solid line on your side means passing is unsafe here", fr: "Non : une ligne continue de votre côté signifie qu'il est dangereux de dépasser ici" },
      { en: "Yes, if you can see far enough and nothing is coming", fr: "Oui, si vous voyez assez loin et que rien n'arrive" },
      { en: "Yes, because the car ahead is unusually slow", fr: "Oui, parce que la voiture devant est particulièrement lente" },
      { en: "Only if the line is solid on both sides", fr: "Seulement si la ligne est continue des deux côtés" }
    ],
    c: 0,
    why: {
      en: "“A solid line at the left of your lane means it is unsafe to pass.” An empty-looking road is not the test — the line is there because of what you cannot see, such as a hill crest or a curve.",
      fr: "Une ligne continue à gauche de votre voie signifie qu'il est dangereux de dépasser. Une route qui paraît vide n'est pas le critère : la ligne est là à cause de ce que vous ne voyez pas, comme un sommet de côte ou une courbe."
    },
    s: "marks"
  },
  {
    id: "broken-yellow-line",
    sc: { kind: "road", centre: "broken", cars: [{ at: "ahead" }], you: { y: 262 } },
    q: {
      en: "Same road, but now the centre line is broken yellow on your side. You may pass. What must you do first?",
      fr: "Même route, mais la ligne centrale est maintenant jaune discontinue de votre côté. Vous pouvez dépasser. Que devez-vous faire d'abord ?"
    },
    a: [
      { en: "Signal, and check the way is clear both ahead and behind", fr: "Signalez, et vérifiez que la voie est libre devant et derrière" },
      { en: "Just go — a broken line means passing is always allowed", fr: "Allez-y : une ligne discontinue autorise toujours le dépassement" },
      { en: "Check ahead only, since you are moving left", fr: "Vérifiez seulement devant, puisque vous vous déplacez à gauche" },
      { en: "Pull out first, then signal so you do not confuse the driver ahead", fr: "Déboîtez d'abord, puis signalez pour ne pas troubler le conducteur devant" }
    ],
    c: 0,
    why: {
      en: "“A broken line at the left of your lane means you may pass if the way is clear.” The handbook asks you to “use your left-turn signal… and check that the way is clear ahead and behind before moving into the passing lane.” Passing is also banned within 30 metres of a pedestrian crossover, or of a bridge, viaduct or tunnel.",
      fr: "Une ligne discontinue à gauche de votre voie signifie que vous pouvez dépasser si la voie est libre. Le guide demande d'utiliser le clignotant gauche et de vérifier que la voie est libre devant et derrière avant de vous déporter. Le dépassement est aussi interdit à moins de 30 mètres d'un passage pour piétons, d'un pont, d'un viaduc ou d'un tunnel."
    },
    s: "passing"
  },
  {
    id: "being-passed",
    sc: { kind: "road", twoLane: true, behind: true, you: { y: 250 } },
    q: {
      en: "You are at the speed limit. A car comes up fast behind you and pulls out to pass. What do you do?",
      fr: "Vous roulez à la limite de vitesse. Une voiture arrive vite derrière vous et déboîte pour vous dépasser. Que faites-vous ?"
    },
    a: [
      { en: "Move closer to the right of your lane and let them by", fr: "Serrez à droite dans votre voie et laissez-la passer" },
      { en: "Hold your position — you are already at the limit", fr: "Gardez votre position : vous êtes déjà à la limite" },
      { en: "Tap the brakes to warn them off", fr: "Touchez les freins pour la dissuader" },
      { en: "Speed up so they give up on passing", fr: "Accélérez pour qu'elle renonce à dépasser" }
    ],
    c: 0,
    why: {
      en: "“When faster traffic wants to pass you, move to the right and let it pass in safety.” If they have pulled into the oncoming lane, watch that lane and move closer to your right. And the handbook is blunt about the last option: “do not speed up when another driver is trying to pass you. It is unlawful and dangerous.”",
      fr: "Quand une circulation plus rapide veut vous dépasser, serrez à droite et laissez-la passer en sécurité. Si elle s'est engagée dans la voie inverse, surveillez cette voie et rapprochez-vous de votre droite. Le guide est net sur la dernière réponse : n'accélérez pas quand un autre conducteur tente de vous dépasser, c'est illégal et dangereux."
    },
    s: "passing"
  },

  /* ---------- the country road -------------------------------------- */
  {
    id: "crossbuck-no-lights",
    sc: { kind: "road", sign: "warn-crossbuck", tracks: true, you: { y: 268 } },
    q: {
      en: "A railway crossing with the X sign, but no lights and no gates. What does the law ask of you here?",
      fr: "Un passage à niveau avec le panneau en X, mais sans feux ni barrières. Qu'exige la loi de vous ici ?"
    },
    a: [
      { en: "Slow down, look and listen both ways, cross only when sure", fr: "Ralentir, regarder et écouter des deux côtés, et ne traverser qu'une fois certain" },
      { en: "Come to a full stop, the way a school bus must", fr: "Faire un arrêt complet, comme doit le faire un autobus scolaire" },
      { en: "Keep your speed — no lights means the line is not in use", fr: "Garder votre vitesse : sans feux, la ligne n'est pas en service" },
      { en: "Sound your horn and cross without slowing", fr: "Klaxonner et traverser sans ralentir" }
    ],
    c: 0,
    why: {
      en: "“Slow down, listen and look both ways to make sure the way is clear before crossing the tracks.” A full stop is required of school buses, not of cars. If a train is coming, stop at least five metres from the nearest rail — and never try to beat it, because a train can take up to two kilometres to stop.",
      fr: "Ralentissez, écoutez et regardez des deux côtés pour vous assurer que la voie est libre avant de traverser. L'arrêt complet est exigé des autobus scolaires, pas des voitures. Si un train arrive, arrêtez-vous à au moins cinq mètres du rail le plus proche — et n'essayez jamais de le devancer : un train peut mettre jusqu'à deux kilomètres à s'arrêter."
    },
    s: "stopping"
  },
  {
    id: "deer-dusk",
    sc: { kind: "road", sign: "warn-deer", you: { y: 262 } },
    q: {
      en: "Dusk on a country road. A deer is standing at the edge of the pavement, watching you come. What do you do?",
      fr: "Au crépuscule sur une route de campagne. Un chevreuil se tient au bord de la chaussée et vous regarde approcher. Que faites-vous ?"
    },
    a: [
      { en: "Slow down, sound your horn, and be ready to stop", fr: "Ralentir, klaxonner et être prêt à vous arrêter" },
      { en: "Steer around it into the other lane", fr: "Le contourner en passant dans l'autre voie" },
      { en: "Keep your speed and flash your high beams to scare it", fr: "Garder votre vitesse et faire des appels de phares pour l'effrayer" },
      { en: "Pull onto the shoulder to let it decide", fr: "Vous ranger sur l'accotement pour la laisser décider" }
    ],
    c: 0,
    why: {
      en: "“Slow down and sound your horn.” The handbook warns against the other three: “don't try to drive around the animal,” because “animal movements are unpredictable,” and do not park on the shoulder, since other drivers may be watching the animal instead of you. Watch for more — where there is one, there are often others.",
      fr: "Ralentissez et klaxonnez. Le guide déconseille les trois autres réponses : n'essayez pas de contourner l'animal, car ses mouvements sont imprévisibles, et ne vous arrêtez pas sur l'accotement, d'autres conducteurs pouvant regarder l'animal plutôt que vous. Surveillez les suivants : là où il y en a un, il y en a souvent d'autres."
    },
    s: "situations"
  },
  {
    id: "slow-moving-vehicle",
    sc: { kind: "road", sign: "slow-vehicle", centre: "broken", cars: [{ at: "ahead" }], you: { y: 268 } },
    q: {
      en: "A vehicle ahead carries the orange and red triangle, and you are coming up to the crest of a hill. What do you do?",
      fr: "Le véhicule devant vous porte le triangle orange et rouge, et vous approchez du sommet d'une côte. Que faites-vous ?"
    },
    a: [
      { en: "Stay well back and wait until you can see far enough to pass", fr: "Restez bien en retrait et attendez de voir assez loin pour dépasser" },
      { en: "Pass on the hill — it will pull over for you", fr: "Dépassez dans la côte : il se rangera pour vous" },
      { en: "Pass on the right shoulder to avoid the centre line", fr: "Dépassez par l'accotement de droite pour éviter la ligne centrale" },
      { en: "Follow close behind, ready to pull out the moment it straightens", fr: "Collez-le de près, prêt à déboîter dès que la route se redresse" }
    ],
    c: 0,
    why: {
      en: "The triangle means the vehicle travels at 40 km/h or less: “stay well back and do not pass until it is safe to do so.” And the handbook is specific about where it is not safe — “don't attempt to pass when approaching the crest of a hill or on a curve where your vision of oncoming traffic is obstructed.”",
      fr: "Le triangle signifie que le véhicule roule à 40 km/h ou moins : restez bien en retrait et ne dépassez pas avant qu'il soit sûr de le faire. Le guide précise où ce n'est pas sûr : n'essayez pas de dépasser à l'approche d'un sommet de côte ou dans une courbe où votre vue de la circulation venant en sens inverse est masquée."
    },
    s: "share"
  }

];
}());
