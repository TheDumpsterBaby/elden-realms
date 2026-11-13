"""W3 Greywater Fens -- the March, levels 40-45.

A marsh west of the Hollow Wood. Its villages have drowned, their people risen
from the black water; grey lights lure travellers off the causeways. The walled
town on stilts (working name Stilthold) still holds out -- the stronghold --
ringing its bell against the dark. In the deepest mere sleeps the Drowned Lord.
"""

ZONE = {
    'num': 202, 'name': 'Greywater Fens', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'fen_edge', 'name': 'The Edge of the Fens', 'sector': 'field',
         'desc': """The ground turns soft underfoot where the Hollow Wood ends, and the trees
         give way to reeds taller than a man.  Mist lies low over brown water.  A
         causeway of logs and packed earth leads out into the marsh, and from
         somewhere out in the mist a bell tolls, slow and steady.""",
         'exits': {'e': {'to': '@20124', 'back_desc': 'Downhill to the west, the track runs into the mists of the Greywater Fens.'}, 'w': 'causeway1'}},
        {'id': 'causeway1', 'name': 'The Log Causeway', 'sector': 'field',
         'desc': """Logs laid side by side make a road across the marsh, slick with green slime.
         Some have rotted through and you step over the gaps into black water.  On
         both sides the reeds hiss, and pale lights drift among them, just out of
         reach.""",
         'exits': {'w': 'causeway2', 'n': 'reed_maze', 's': 'drowned_village_e'},
         'mobs': [('grey_light', 2)]},
        {'id': 'reed_maze', 'name': 'Among the Tall Reeds', 'sector': 'water',
         'desc': """You wade off the causeway into reeds that close over your head.  The water is
         waist deep and cold, and the mud sucks at your boots.  Every direction looks
         the same.  A grey light bobs ahead, beckoning, always a few steps further.""",
         'exits': {'n': 'heron_mere', 'w': 'hag_hut'},
         'mobs': [('marsh_leech', 2), ('grey_light', 1)]},
        {'id': 'heron_mere', 'name': 'The Heron Mere', 'sector': 'water',
         'desc': """An open pool of still black water ringed by reeds.  Herons stand in the
         shallows, grey and motionless, but they do not fish; they watch you, every
         one, and their eyes are milky white.  Beneath the surface something long
         turns over and is gone.""",
         'mobs': [('grey_heron', 3)]},
        {'id': 'hag_hut', 'name': 'The Fen Hag\'s Hut', 'sector': 'inside', 'flags': 'd',
         'desc': """A hut of reeds and mud squats on a hummock above the water.  Inside, bundles
         of herbs and dead things hang from the roof, and a cauldron bubbles with
         something grey.  Little figures made of reeds and hair stand along a shelf,
         each wearing a scrap of clothing from someone who went missing.""",
         'extras': {'figures reeds shelf': 'Dozens of little reed people. One wears a scrap of Stilthold militia blue.'},
         'mobs': [('fen_hag', 1)]},
        {'id': 'drowned_village_e', 'name': 'The Drowned Village, East End', 'sector': 'water',
         'desc': """Roofs poke out of the water like the backs of whales.  This was a village of
         eel-fishers before the marsh rose in a single night and swallowed it.  The
         water is clear enough here to see the streets below, and the people still
         walking in them.""",
         'exits': {'w': 'drowned_square', 'd': 'drowned_street'},
         'mobs': [('drowned_villager', 2)]},
        {'id': 'drowned_street', 'name': 'Beneath the Water, a Drowned Street', 'sector': 'underwater', 'flags': 'a',
         'desc': """You sink into the cold water and walk the drowned street.  Doors hang open.
         Weed grows from the windows.  Drowned villagers go about their old tasks in
         slow motion, mending nets that rot as they mend them, and they turn their
         white faces toward you as you pass.""",
         'mobs': [('drowned_villager', 2), ('drowned_fisher', 1)]},
        {'id': 'drowned_square', 'name': 'The Drowned Square', 'sector': 'water',
         'desc': """The village square lies under a fathom of water, but its chapel spire rises
         above the surface, and someone has tied a rope ladder to it.  Grey-scaled
         things nest on the roofs around the square, hissing, and the water below
         them boils with eels.""",
         'exits': {'u': 'spire', 'n': 'causeway3'},
         'mobs': [('fen_eel_swarm', 2)]},
        {'id': 'spire', 'name': 'Atop the Drowned Spire', 'sector': 'inside',
         'desc': """You climb the ladder to the little belfry of the drowned chapel.  The bell is
         gone.  Someone has made a nest up here of sacking and stolen clothes, and
         left a heap of shiny things: buttons, rings, a soldier's badge.  The
         creature that made it is coming back.  You can hear it climbing.""",
         'mobs': [('marsh_harpy', 1)]},
        {'id': 'causeway2', 'name': 'The Causeway, Bones in the Mud', 'sector': 'field',
         'desc': """The causeway is lined with stakes, and on each stake is a skull, facing
         outward.  The Stilthold militia put them there as a warning to the things in
         the marsh.  The things in the marsh have replied by adding skulls of their
         own, in Stilthold blue.""",
         'exits': {'w': 'stilthold_gate'},
         'mobs': [('bog_wight', 1)]},
        {'id': 'stilthold_gate', 'name': 'The Gate of Stilthold', 'sector': 'city', 'flags': 'c',
         'desc': """A town rises from the marsh on a forest of tarred stilts, its timber walls
         studded with iron spikes.  A drawbridge of planks hangs over the causeway,
         let down only for the living.  A great bronze bell hangs in a tower above
         the gate, and a guard rings it every hundred heartbeats.""",
         'exits': {'u': 'stilt_walk', 'w': 'causeway3'},
         'mobs': [('stilt_militia', 2)]},
        {'id': 'stilt_walk', 'name': 'Stilthold, the Plank Walk', 'sector': 'city', 'flags': 'c',
         'desc': """Walkways of planks link the houses of Stilthold high above the water, swaying
         gently on their ropes.  Children are tied to their mothers with cords so
         that they cannot fall.  Lamps burn in every window, day and night, because
         the grey lights fear true flame.""",
         'exits': {'n': 'reeve_hall', 'w': 'inn', 's': 'healers', 'u': 'bell_tower'},
         'mobs': [('stilthold_townsfolk', 2)]},
        {'id': 'reeve_hall', 'name': 'Stilthold, the Reeve\'s Hall', 'sector': 'inside', 'flags': 'cde',
         'desc': """A long hall on the highest stilts, where the reeve holds council beneath a
         roof of reed thatch.  Maps of the marsh are spread on the table, and every
         drowned village is marked with a black stone.  There are more black stones
         than there are villages left.""",
         'mobs': [('reeve', 1)]},
        {'id': 'inn', 'name': 'Stilthold, the Last Lantern Inn', 'sector': 'inside', 'flags': 'cde',
         'desc': """A smoky common room where militia and eel-fishers drink in silence.  The
         landlady keeps a lantern burning on every table.  Above the bar hangs a
         stuffed fen eel as long as a boat, and beneath it a list of the inn's
         regulars who did not come back from the marsh.""",
         'objs': [('stilt_rainbarrel', 1)],
         'mobs': [('landlady', 1)]},
        {'id': 'healers', 'name': 'Stilthold, the House of Lamps', 'sector': 'inside', 'flags': 'cde',
         'desc': """A healer's house where leech-bitten and fever-sick lie on cots beneath a
         hundred small oil lamps.  The healer here burns the grey from wounds with a
         hot iron; it is the only cure that works.  The smell of scorched flesh never
         leaves the room.""",
         'mobs': [('lamp_healer', 1)]},
        {'id': 'bell_tower', 'name': 'Stilthold, the Bell Tower', 'sector': 'inside', 'flags': 'ce',
         'desc': """At the top of the tower the great bronze bell swings and tolls, and the
         ringer counts under his breath.  From here the whole marsh is spread out
         below: the drowned villages, the meres, and far to the west the black water
         of the Deep Mere, where the mist never lifts.""",
         'extras': {'deep mere west mist': 'The Deep Mere. The Stilthold folk say the old Fen-King sleeps beneath it, and that he has begun to dream again.'},
         'mobs': [('bell_ringer', 1)]},
        {'id': 'causeway3', 'name': 'The West Causeway', 'sector': 'field',
         'desc': """Beyond Stilthold the causeway runs west in poorer repair, half sunk in places.
         The marsh grows darker and the water blacker.  Bloated shapes float face
         down in the channels on either side, and not all of them stay floating
         when you pass.""",
         'exits': {'w': 'sunken_road', 'n': 'bog_field'},
         'mobs': [('bog_wight', 2)]},
        {'id': 'bog_field', 'name': 'The Bog of the Fallen', 'sector': 'water',
         'desc': """A wide bog where a company of Stilthold militia was lost chasing the grey
         lights.  Their spears still stand upright in the mud where they sank.
         Sometimes on still nights the spears move, as the men beneath them try to
         climb out.""",
         'exits': {'n': 'leech_pool'},
         'mobs': [('bog_wight', 2), ('drowned_militia', 1)]},
        {'id': 'leech_pool', 'name': 'The Leech Pool', 'sector': 'water',
         'desc': """A pool of warm, red-tinged water steaming slightly in the cold air.  Things
         ripple beneath the surface, long and fat.  On the bank lies the body of a
         deer drained white and dry as paper.  The water is the colour it is
         because of what lives in it.""",
         'mobs': [('marsh_leech', 2), ('leech_queen', 1)]},
        {'id': 'sunken_road', 'name': 'The Sunken Road', 'sector': 'water',
         'desc': """The causeway sinks below the water here, and you wade knee deep along its
         line, feeling for the logs with your feet.  Mist closes in until you
         cannot see your hands.  Voices call to you from the mist, using the names
         of people you have lost.""",
         'exits': {'w': 'fen_kings_way', 's': 'barrow_isle'},
         'mobs': [('grey_light', 2), ('mist_wraith', 1)]},
        {'id': 'barrow_isle', 'name': 'The Barrow Isle', 'sector': 'hills',
         'desc': """A low island rises from the marsh, crowned with a grassy barrow ringed with
         stones.  The old fen-folk buried their kings' servants here.  The barrow
         door has been dug open from the inside, and the earth around it is
         churned and wet.""",
         'exits': {'d': 'barrow_inside'},
         'mobs': [('barrow_servant', 2)]},
        {'id': 'barrow_inside', 'name': 'Inside the Barrow', 'sector': 'inside', 'flags': 'ad',
         'desc': """A passage of mossy stone leads into the mound, lined with niches where the
         dead lie in rotted finery.  Water drips everywhere.  At the end of the
         passage, a wight in a crown of tarnished bronze sits on a stone chair,
         its servants kneeling around it.""",
         'mobs': [('barrow_steward', 1), ('barrow_servant', 1)]},
        {'id': 'fen_kings_way', 'name': 'The Fen-King\'s Way', 'sector': 'field',
         'desc': """An ancient road of carved stone rises out of the water, leading west toward
         the Deep Mere.  Statues of crowned men line it, their faces worn away by
         centuries of rain, their hands held out as if offering something.  Each
         one has been hung with drowned flowers.""",
         'exits': {'w': 'deep_mere_shore', 'n': 'west_fens'},
         'mobs': [('drowned_knight', 1)]},
        {'id': 'deep_mere_shore', 'name': 'The Shore of the Deep Mere', 'sector': 'field',
         'desc': """The road ends at a stone jetty on the shore of a lake of black, motionless
         water.  The mist here is thick and cold and smells of iron.  A causeway of
         carved stone runs out into the mere, half submerged, toward a ruined tower
         rising from the water at its centre.""",
         'exits': {'w': 'mere_causeway'},
         'mobs': [('drowned_knight', 1), ('grey_light', 1)]},
        {'id': 'mere_causeway', 'name': 'The Causeway Across the Mere', 'sector': 'water',
         'desc': """You wade along the submerged stones, the black water around your thighs and
         rising.  The bottom drops away on either side into darkness.  Pale faces
         rise to just beneath the surface and drift alongside you, watching,
         patient.""",
         'exits': {'w': 'drowned_tower'},
         'mobs': [('drowned_villager', 2)]},
        {'id': 'drowned_tower', 'name': 'The Drowned Tower', 'sector': 'inside', 'flags': 'd',
         'desc': """The tower's lower floors are flooded.  Its walls are carved with the history
         of the fen-kings, ending in a carving of the marsh rising over a crowned
         figure who opens his arms to a darkness in the west.  A stair leads down
         into the black water.""",
         'exits': {'d': 'kings_hall'},
         'mobs': [('drowned_knight', 2)]},
        {'id': 'kings_hall', 'name': 'The Hall Beneath the Mere', 'sector': 'underwater', 'flags': 'a',
         'desc': """A drowned throne room deep beneath the mere, its pillars wrapped in weed.
         Grey light glows from nowhere.  On the throne sits the Drowned Lord, last of
         the fen-kings, who made a pact with the West to save his kingdom and
         drowned it instead.  He rises.""",
         'mobs': [('drowned_lord', 1)]},
        {'id': 'west_fens', 'name': 'The Western Fens', 'sector': 'field',
         'desc': """The marsh gives way to firmer ground as you go west.  The reeds thin, and
         the land rises toward a grey, open plain.  Broken banners lie half buried in
         the mud, and the wind brings a smell of old iron and older death from the
         battlefield ahead.""",
         'mobs': [('bog_wight', 1)]},
    ],
    'mobs': [
        {'id': 'grey_light', 'aliases': 'light grey wisp', 'short': 'a grey light', 'role': 'standard', 'level': 41,
         'long': 'A pale grey light bobs above the water, beckoning.', 'flags': 'f', 'align': -800, 'attack': 'blast',
         'desc': 'A cold glow with something almost like a face inside it. It leads travellers into the deep water and feeds on their drowning.'},
        {'id': 'marsh_leech', 'aliases': 'leech marsh', 'short': 'a giant marsh leech', 'role': 'standard', 'level': 40,
         'long': 'A leech as long as your arm rises from the water, sucker gaping.', 'flags': 'f', 'align': -300, 'attack': 'bite',
         'desc': 'Slick, black and blind, it can drain a man in an hour.'},
        {'id': 'grey_heron', 'aliases': 'heron grey', 'short': 'a milky-eyed heron', 'role': 'standard', 'level': 40,
         'long': 'A grey heron with milky eyes stands in the shallows, watching you.', 'flags': 'f', 'align': -500, 'attack': 'pierce',
         'desc': 'Its beak is long and sharp as a spear, and it no longer eats fish.'},
        {'id': 'fen_hag', 'aliases': 'hag fen', 'short': 'the fen hag', 'role': 'champion', 'level': 44,
         'long': 'A bent old woman with green-grey skin stirs her cauldron, grinning.', 'flags': 'bfl', 'align': -900, 'sex': 2,
         'desc': 'She has lived in the marsh for three hundred years, and she was wicked long before the West came. Now she has a patron, and she is delighted.',
         'equip': [('hag_ladle', 'wield', 100)], 'carry': [('hag_charm', 100)]},
        {'id': 'drowned_villager', 'aliases': 'drowned villager', 'short': 'a drowned villager', 'role': 'standard', 'level': 41,
         'long': 'A drowned villager turns a white, bloated face toward you.', 'flags': 'f', 'align': -800, 'attack': 'claw',
         'desc': 'Weed in its hair, eels in its ribs. It drowned when the marsh rose, and the darkness walked it again.'},
        {'id': 'drowned_fisher', 'aliases': 'fisher drowned', 'short': 'a drowned eel-fisher', 'role': 'elite', 'level': 43,
         'long': 'A drowned eel-fisher swings a rotting net toward you.', 'flags': 'f', 'align': -800, 'sex': 1,
         'desc': 'Big and broad, his net weighted with stones. He still knows how to catch things.',
         'equip': [('eel_spear', 'wield', 100)]},
        {'id': 'fen_eel_swarm', 'aliases': 'eels swarm eel', 'short': 'a boiling swarm of fen eels', 'role': 'standard', 'level': 42,
         'long': 'The water boils with grey eels, all teeth.', 'flags': 'f', 'align': -300, 'attack': 'bite',
         'desc': 'Hundreds of eels, fat on the drowned. They strip a body in minutes.'},
        {'id': 'marsh_harpy', 'aliases': 'harpy marsh', 'short': 'a marsh harpy', 'role': 'elite', 'level': 44,
         'long': 'A harpy with grey wings and a drowned woman\'s face screeches at you.', 'flags': 'bfl', 'align': -800, 'sex': 2, 'attack': 'claw',
         'desc': 'She collects shiny things from the drowned. She would like your eyes for her nest.',
         'carry': [('soldiers_badge', 100)]},
        {'id': 'bog_wight', 'aliases': 'wight bog', 'short': 'a bog wight', 'role': 'standard', 'level': 42,
         'long': 'A bog wight, its skin tanned dark as leather by the peat, rises from the mud.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Preserved for centuries in the bog, it has awakened hungry. Its touch steals warmth.'},
        {'id': 'stilt_militia', 'aliases': 'militia stilthold guard', 'short': 'a Stilthold militiaman', 'role': 'elite', 'level': 44,
         'long': 'A Stilthold militiaman in faded blue watches the marsh, a torch in one hand.', 'flags': 'bm', 'align': 600, 'sex': 1,
         'desc': 'Every man and woman in Stilthold serves on the wall. This one has served for twenty years, since he was twelve.',
         'equip': [('stilt_trident', 'wield', 100)]},
        {'id': 'stilthold_townsfolk', 'aliases': 'townsfolk townsman', 'short': 'a Stilthold townsman', 'role': 'harmless', 'level': 40,
         'long': 'A Stilthold townsman trims a lamp wick with careful hands.', 'flags': 'g', 'align': 500,
         'desc': 'Lamps are life in Stilthold. Everyone carries one, everyone tends one.'},
        {'id': 'reeve', 'aliases': 'reeve', 'short': 'the Reeve of Stilthold', 'role': 'champion', 'level': 45,
         'long': 'The Reeve of Stilthold studies the map of black stones.', 'flags': 'b', 'align': 700, 'sex': 2,
         'desc': 'A stout grey-haired woman with an eel-fisher\'s hands. She has held Stilthold together through two winters of the dark. She will not hold a third without help.',
         'equip': [('reeve_hammer', 'wield', 100)]},
        {'id': 'landlady', 'aliases': 'landlady', 'short': 'the landlady', 'role': 'harmless', 'level': 40,
         'long': 'The landlady wipes the bar and keeps one eye on the lanterns.', 'flags': 'b', 'align': 500, 'sex': 2,
         'desc': 'Kind eyes in a hard face. She feeds the militia on credit and has stopped keeping the tally.',
         'carry': [('eel_pie', 100)]},
        {'id': 'lamp_healer', 'aliases': 'healer lamp', 'short': 'the lamp healer', 'role': 'harmless', 'level': 42,
         'long': 'The lamp healer heats an iron in a brazier, face set.', 'flags': 'b', 'align': 900, 'sex': 1,
         'desc': 'The only cure for the grey is fire. He hates every moment of it, and does not stop.',
         'carry': [('burn_salve', 100)]},
        {'id': 'bell_ringer', 'aliases': 'ringer bell', 'short': 'the bell ringer', 'role': 'harmless', 'level': 40,
         'long': 'The bell ringer hauls the rope, counting under his breath.', 'flags': 'b', 'align': 400, 'sex': 1,
         'desc': 'If the bell stops, the grey lights come over the walls. He has not slept a full night in a year.'},
        {'id': 'drowned_militia', 'aliases': 'militia drowned', 'short': 'a drowned militiaman', 'role': 'elite', 'level': 43,
         'long': 'A drowned militiaman in rotted blue drags himself out of the bog.', 'flags': 'f', 'align': -800, 'sex': 1,
         'desc': 'One of the lost company. His spear is still in his hand.',
         'equip': [('stilt_trident', 'wield', 60)]},
        {'id': 'leech_queen', 'aliases': 'queen leech', 'short': 'the leech queen', 'role': 'champion', 'level': 44,
         'long': 'A leech the size of a boat heaves itself out of the red water.', 'flags': 'bfl', 'align': -500, 'attack': 'bite',
         'desc': 'Swollen and ancient, her body pulses with stolen blood.',
         'carry': [('leech_hide', 100)]},
        {'id': 'mist_wraith', 'aliases': 'wraith mist', 'short': 'a mist wraith', 'role': 'elite', 'level': 44,
         'long': 'The mist thickens into a shape with your mother\'s voice.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'It speaks with the voices of the dead you remember. It knows your name.'},
        {'id': 'barrow_servant', 'aliases': 'servant barrow', 'short': 'a barrow servant', 'role': 'standard', 'level': 43,
         'long': 'A skeleton in rotted livery shuffles toward you.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Buried alive with its king a thousand years ago, to serve him in death. It is still serving.'},
        {'id': 'barrow_steward', 'aliases': 'steward barrow wight crowned', 'short': 'the barrow steward', 'role': 'champion', 'level': 44,
         'long': 'A crowned wight rises from its stone chair.', 'flags': 'bfl', 'align': -1000,
         'desc': 'Steward to the fen-kings, he rules their servants in death. The Drowned Lord\'s return has woken him.',
         'equip': [('bronze_crown', 'head', 100), ('barrow_blade', 'wield', 100)]},
        {'id': 'drowned_knight', 'aliases': 'knight drowned', 'short': 'a drowned knight', 'role': 'elite', 'level': 45,
         'long': 'A knight in weed-hung armour stands guard, water pouring from his visor.', 'flags': 'f', 'align': -900, 'sex': 1,
         'desc': 'A knight of the old fen-kingdom, drowned with his lord. His sword is green with age and still sharp.',
         'equip': [('fen_knight_sword', 'wield', 80), ('weedhung_mail', 'body', 30)]},
        {'id': 'drowned_lord', 'aliases': 'lord drowned fen-king king', 'short': 'the Drowned Lord', 'role': 'boss', 'level': 45,
         'long': 'The Drowned Lord rises from his throne, black water streaming from his crown.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'Last of the fen-kings. When the West first reached the marsh he bargained with it for his kingdom\'s survival, and the price was the kingdom. He drowned it in a night, and he has been Nu\'Groth\'s willing servant ever since.',
         'equip': [('drowned_crown', 'head', 100), ('tide_blade', 'wield', 100)], 'carry': [('mere_pearl', 100)]},
    ],
    'objs': [
        {'id': 'stilt_rainbarrel', 'kind': 'fountain', 'aliases': 'barrel rain', 'short': 'a rain barrel',
         'long': 'A rain barrel of clean water stands by the bar.', 'liquid': 0},
        {'id': 'hag_ladle', 'kind': 'weapon', 'level': 43, 'attack': 'bludgeon', 'aliases': 'ladle hag iron',
         'short': 'the hag\'s iron ladle', 'long': 'A heavy iron ladle lies here.'},
        {'id': 'hag_charm', 'kind': 'worn', 'slot': 'neck', 'level': 44, 'aliases': 'charm hag reed',
         'short': 'a reed charm on a cord', 'long': 'A charm of knotted reeds and hair lies here.', 'affects': [('save_spell', -3), ('wis', 1)]},
        {'id': 'eel_spear', 'kind': 'weapon', 'level': 42, 'attack': 'pierce', 'aliases': 'spear eel',
         'short': 'an eel spear', 'long': 'A barbed eel spear lies here.'},
        {'id': 'soldiers_badge', 'kind': 'treasure', 'level': 40, 'aliases': 'badge soldier', 'short': 'a soldier\'s badge',
         'long': 'A tarnished soldier\'s badge lies here.', 'weight': 1, 'cost': 80,
         'extras': {'badge': 'A Midgaard tower badge, engraved: CORPORAL VESS, 2ND PATROL.'}},
        {'id': 'stilt_trident', 'kind': 'weapon', 'level': 44, 'attack': 'pierce', 'aliases': 'trident stilthold',
         'short': 'a Stilthold trident', 'long': 'A three-pronged militia trident lies here.'},
        {'id': 'reeve_hammer', 'kind': 'weapon', 'level': 45, 'attack': 'pound', 'aliases': 'hammer reeve',
         'short': 'the Reeve\'s hammer', 'long': 'A heavy shipwright\'s hammer lies here.', 'affects': [('hitroll', 2)]},
        {'id': 'eel_pie', 'kind': 'food', 'hours': 12, 'aliases': 'pie eel', 'short': 'an eel pie', 'long': 'An eel pie sits here.', 'weight': 1, 'cost': 15},
        {'id': 'burn_salve', 'kind': 'potion', 'level': 42, 'spells': [15, 43], 'spell_level': 40,
         'aliases': 'salve burn jar', 'short': 'a jar of burn salve', 'long': 'A small jar of salve lies here.', 'weight': 1},
        {'id': 'leech_hide', 'kind': 'armor', 'slot': 'body', 'level': 45, 'aliases': 'hide leech',
         'short': 'a coat of leech hide', 'long': 'A slick black coat of leech hide lies here.', 'affects': [('hit', 30)]},
        {'id': 'bronze_crown', 'kind': 'armor', 'slot': 'head', 'level': 45, 'aliases': 'crown bronze',
         'short': 'a tarnished bronze crown', 'long': 'A crown of tarnished bronze lies here.', 'affects': [('cha', 2), ('save_para', -2)]},
        {'id': 'barrow_blade', 'kind': 'weapon', 'level': 45, 'attack': 'slash', 'aliases': 'blade barrow bronze',
         'short': 'a bronze barrow blade', 'long': 'An ancient bronze blade lies here.', 'affects': [('hitroll', 2), ('damroll', 1)]},
        {'id': 'fen_knight_sword', 'kind': 'weapon', 'level': 45, 'attack': 'slash', 'aliases': 'sword knight fen green',
         'short': 'a green-bronze knight\'s sword', 'long': 'A knight\'s sword green with age lies here.'},
        {'id': 'weedhung_mail', 'kind': 'armor', 'slot': 'body', 'level': 45, 'aliases': 'mail weed',
         'short': 'weed-hung mail', 'long': 'A coat of mail hung with weed lies here.'},
        {'id': 'drowned_crown', 'kind': 'armor', 'slot': 'head', 'level': 46, 'aliases': 'crown drowned black',
         'short': 'the Drowned Crown', 'long': 'A crown of black iron, always wet, lies here.', 'affects': [('hit', 35), ('wis', 1), ('save_spell', -2)]},
        {'id': 'tide_blade', 'kind': 'weapon', 'level': 46, 'attack': 'slash', 'aliases': 'blade tide',
         'short': 'the Tide Blade', 'long': 'A sword that drips water endlessly lies here.', 'affects': [('hitroll', 3), ('damroll', 3)]},
        {'id': 'mere_pearl', 'kind': 'worn', 'slot': 'finger', 'level': 45, 'aliases': 'pearl ring mere',
         'short': 'a ring set with a black pearl', 'long': 'A ring set with a black pearl lies here.', 'affects': [('mana', 40), ('int', 1)]},
    ],
}
