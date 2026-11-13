"""W11 The Drowned Kingdom -- the Blight, levels 80-85.

Beyond the roots of the Shattered Peaks lies a black sea in a cavern the size of
a country, and beneath it a kingdom the West sank whole. Its drowned court
still rules from the palace on the sea floor, and the Queen Beneath keeps the
black water for Nu\'Groth. A flooded stair rises to the surface in the west.
"""

ZONE = {
    'num': 210, 'name': 'The Drowned Kingdom', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'sea_shore', 'name': 'The Shore of the Black Sea', 'sector': 'field', 'flags': 'a',
         'desc': """The tunnel opens onto a beach of black sand at the edge of an underground sea.
         The cavern above is so vast that its roof is lost in darkness, and the water
         stretches away into the dark, still and black as oil.  Pale lights glimmer
         far out beneath the surface, in the shape of streets.""",
         'exits': {'e': {'to': '@20915', 'back_desc': 'West, the tunnel opens onto the shore of a black underground sea.'}, 'w': 'shallows'},
         'mobs': [('black_crab', 2)]},
        {'id': 'shallows', 'name': 'The Black Shallows', 'sector': 'water', 'flags': 'a',
         'desc': """You wade out into water as cold as death.  It closes over your waist, then your
         chest.  The black sand shelves away beneath you toward the lights.  Things brush
         against your legs in the dark, smooth and cold, and do not let go at once.""",
         'exits': {'w': 'sinking', 's': 'wreck_reef'},
         'mobs': [('black_eel', 2)]},
        {'id': 'wreck_reef', 'name': 'The Reef of Wrecks', 'sector': 'water', 'flags': 'a',
         'desc': """A reef of sunken boats rises out of the shallows: fishing skiffs, barges, a royal
         galley with a gilded prow.  They were dragged down when the kingdom sank, with
         their crews still aboard.  The crews are still aboard.""",
         'exits': {'d': 'galley_hold'},
         'mobs': [('drowned_sailor', 2)]},
        {'id': 'galley_hold', 'name': 'The Hold of the Royal Galley', 'sector': 'underwater', 'flags': 'a',
         'desc': """You dive into the galley\'s flooded hold.  Chests of the royal household float
         against the beams, and the rowers are still chained to their benches, pulling
         at oars that move only water.  The galley\'s captain sits at the stern in his
         finery, bloated and white, and turns his head.""",
         'mobs': [('galley_captain', 1), ('drowned_sailor', 1)]},
        {'id': 'sinking', 'name': 'Sinking into the Black', 'sector': 'underwater', 'flags': 'a',
         'desc': """The bottom falls away and you sink, down and down through black water, toward
         the drowned lights below.  Your ears ache.  Your lungs burn and then, strangely,
         stop burning, as if the water has decided to let you breathe it for now.""",
         'exits': {'d': 'outer_city'},
         'mobs': [('abyssal_jelly', 1)]},
        {'id': 'outer_city', 'name': 'The Outer City', 'sector': 'underwater', 'flags': 'a',
         'desc': """Streets of white stone run between drowned houses, lit by pale fungus that grows
         on every wall.  Drowned citizens walk them as if on dry land, going about errands
         a hundred years old, their hair drifting around their faces like weed.""",
         'exits': {'w': 'bone_coral', 'n': 'drowned_market', 's': 'temple_ruin'},
         'mobs': [('drowned_citizen', 3)]},
        {'id': 'drowned_market', 'name': 'The Drowned Market', 'sector': 'underwater', 'flags': 'a',
         'desc': """Stalls stand in a drowned square, their wares floating: fish that have been dead
         for a century, bolts of rotted silk, jars of black pearls.  The merchants call
         out their prices in bubbles.  Grey sharks circle overhead like vultures.""",
         'mobs': [('drowned_citizen', 2), ('grey_shark', 2)]},
        {'id': 'temple_ruin', 'name': 'The Temple of the Tides', 'sector': 'underwater', 'flags': 'a',
         'desc': """A temple to the sea god, its columns cracked, its dome caved in.  The god\'s statue
         lies face down on the floor, and over the altar hangs a grey spiral of woven
         weed.  Tide-priests in robes of kelp chant before it in voices like the deep
         sea.""",
         'exits': {'d': 'kraken_grotto'},
         'mobs': [('tide_priest', 2)]},
        {'id': 'kraken_grotto', 'name': 'The Kraken Grotto', 'sector': 'underwater', 'flags': 'a',
         'desc': """Beneath the temple, a cave opens into the sea floor.  It is full of bones, ships\'
         timbers and the rusting armour of a hundred knights.  Something vast fills the
         back of the cave, coil upon coil of grey arm as thick as a tree, and an eye opens
         in the dark.""",
         'mobs': [('grey_kraken', 1)]},
        {'id': 'bone_coral', 'name': 'The Avenue of Bone Coral', 'sector': 'underwater', 'flags': 'a',
         'desc': """A grand avenue leads toward the palace, lined with coral that has grown over the
         bodies of the kingdom\'s soldiers, standing where they drowned in ranks.  Their
         faces show through the coral, white and staring.  Abyssal knights patrol the
         avenue on the backs of great grey rays.""",
         'exits': {'w': 'palace_gate'},
         'mobs': [('abyssal_knight', 2)]},
        {'id': 'palace_gate', 'name': 'The Palace of Coral and Pearl', 'sector': 'underwater', 'flags': 'a',
         'desc': """The royal palace rises before you, its towers encrusted with pearl and coral, its
         windows glowing with pale light.  It was the most beautiful building in the world.
         It still is, in a way that makes you want to weep.  The gate stands open, guarded
         by knights of the drowned court.""",
         'exits': {'w': 'court_hall'},
         'mobs': [('abyssal_knight', 2)]},
        {'id': 'court_hall', 'name': 'The Hall of the Drowned Court', 'sector': 'underwater', 'flags': 'a',
         'desc': """A great hall where the drowned court still sits in session: lords and ladies in
         robes of rotted silk, a herald, a chancellor reading petitions from a scroll that
         dissolves as he reads.  They turn as one to look at you, a living thing in their
         hall.""",
         'exits': {'w': 'tide_chamber', 'n': 'royal_crypt'},
         'mobs': [('drowned_courtier', 3), ('drowned_chancellor', 1)]},
        {'id': 'royal_crypt', 'name': 'The Royal Crypt', 'sector': 'underwater', 'flags': 'a',
         'desc': """Beneath the hall lie the tombs of the kingdom\'s rulers, their lids cast aside.
         The kings and queens of a thousand years float above their coffins, wrapped in
         their burial robes, and they are the queen\'s honour guard now.""",
         'mobs': [('drowned_monarch', 2)]},
        {'id': 'tide_chamber', 'name': 'The Chamber of Tides', 'sector': 'underwater', 'flags': 'a',
         'desc': """A round chamber at the heart of the palace where a great pearl the size of a man
         turns slowly in the water, glowing grey.  It was the kingdom\'s heart once, the
         source of the tides.  Nu\'Groth poisoned it, and the kingdom sank.  Beyond it,
         through an arch of black pearl, is the throne room.""",
         'exits': {'w': 'throne_room'},
         'mobs': [('pearl_guardian', 1)]},
        {'id': 'throne_room', 'name': 'The Throne Beneath the Sea', 'sector': 'underwater', 'flags': 'a',
         'desc': """The queen\'s throne room, its walls of mother-of-pearl, its floor a mosaic of the
         kingdom as it was.  On a throne of black coral sits the Queen Beneath, crowned in
         pearls, her hair a cloud of black weed.  She chose to drown her people rather than
         see them hollowed.  The West drowned them anyway, and made her its keeper.""",
         'exits': {'u': 'flooded_stair'},
         'mobs': [('queen_beneath', 1)]},
        {'id': 'flooded_stair', 'name': 'The Flooded Stair', 'sector': 'underwater', 'flags': 'a',
         'desc': """Behind the throne, a stair of white stone spirals upward through the water, out of
         the palace and up through the roof of the cavern itself.  You climb.  The water
         grows lighter, grey instead of black, and at last your head breaks the surface into
         grey daylight and the smell of rotting leaves.""",
         'mobs': [('black_eel', 1)]},
    ],
    'mobs': [
        {'id': 'black_crab', 'aliases': 'crab black', 'short': 'a black crab', 'role': 'standard', 'level': 81,
         'long': 'A crab as big as a shield scuttles out of the black sand.', 'flags': 'f', 'align': -400, 'attack': 'claw',
         'desc': 'Its shell is black and its claws could take off a hand.'},
        {'id': 'black_eel', 'aliases': 'eel black', 'short': 'a black eel', 'role': 'standard', 'level': 82,
         'long': 'A black eel as long as a boat glides past, jaws open.', 'flags': 'f', 'align': -500, 'attack': 'bite',
         'desc': 'Smooth, cold, and very hungry.'},
        {'id': 'drowned_sailor', 'aliases': 'sailor drowned', 'short': 'a drowned sailor', 'role': 'standard', 'level': 82,
         'long': 'A drowned sailor climbs over the rail toward you.', 'flags': 'f', 'align': -900,
         'desc': 'Barnacles grow on his face. He still carries his cutlass.',
         'equip': [('barnacled_cutlass', 'wield', 70)]},
        {'id': 'galley_captain', 'aliases': 'captain galley', 'short': 'the galley captain', 'role': 'champion', 'level': 85,
         'long': 'The galley captain rises from his chair in the stern, bloated and white.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'He was carrying the royal family to safety when the kingdom sank. He has been sailing nowhere for a hundred years.',
         'equip': [('captains_rapier', 'wield', 100)], 'carry': [('admiral_coat', 100)]},
        {'id': 'abyssal_jelly', 'aliases': 'jelly abyssal', 'short': 'an abyssal jelly', 'role': 'elite', 'level': 83,
         'long': 'A pale jelly the size of a house drifts up out of the dark, trailing stinging threads.', 'flags': 'f', 'align': -500, 'attack': 'sting',
         'desc': 'Its threads hang down for fathoms, and anything they touch goes numb.'},
        {'id': 'drowned_citizen', 'aliases': 'citizen drowned', 'short': 'a drowned citizen', 'role': 'standard', 'level': 82,
         'long': 'A drowned citizen walks the street, hair drifting like weed.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Going about errands a hundred years old. It does not like to be interrupted.'},
        {'id': 'grey_shark', 'aliases': 'shark grey', 'short': 'a grey shark', 'role': 'elite', 'level': 84,
         'long': 'A grey shark as long as a wagon circles overhead.', 'flags': 'f', 'align': -600, 'attack': 'bite',
         'desc': 'Eyeless and grey. It hunts by the beat of your heart.'},
        {'id': 'tide_priest', 'aliases': 'priest tide', 'short': 'a tide-priest', 'role': 'elite', 'level': 84,
         'long': 'A tide-priest in robes of kelp chants before the grey spiral.', 'flags': 'f', 'align': -1000,
         'desc': 'They worshipped the sea god. Now they worship what drowned him.',
         'equip': [('coral_trident', 'wield', 100)]},
        {'id': 'grey_kraken', 'aliases': 'kraken grey', 'short': 'the grey kraken', 'role': 'champion', 'level': 85,
         'long': 'A vast grey kraken uncoils from the back of the grotto, arms reaching.', 'flags': 'bfl', 'align': -900, 'attack': 'crush',
         'desc': 'It pulled the kingdom\'s fleet down one ship at a time. It is still hungry.',
         'carry': [('kraken_beak', 100)]},
        {'id': 'abyssal_knight', 'aliases': 'knight abyssal', 'short': 'an abyssal knight', 'role': 'elite', 'level': 85,
         'long': 'An abyssal knight on a great grey ray levels a coral lance.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'The queen\'s knights, drowned in their armour, which has grown over with black coral.',
         'equip': [('coral_lance', 'wield', 80), ('coral_plate', 'body', 25)]},
        {'id': 'drowned_courtier', 'aliases': 'courtier drowned', 'short': 'a drowned courtier', 'role': 'standard', 'level': 83,
         'long': 'A drowned courtier in rotted silk turns to stare at you.', 'flags': 'f', 'align': -1000,
         'desc': 'Lords and ladies of a kingdom that ended a hundred years ago, still at court.'},
        {'id': 'drowned_chancellor', 'aliases': 'chancellor drowned', 'short': 'the drowned chancellor', 'role': 'elite', 'level': 85,
         'long': 'The drowned chancellor looks up from a dissolving scroll.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'He reads the petitions of the dead. One of them asks for you.',
         'carry': [('dissolving_scroll', 100)]},
        {'id': 'drowned_monarch', 'aliases': 'monarch drowned king queen', 'short': 'a drowned monarch', 'role': 'elite', 'level': 85,
         'long': 'A drowned monarch rises from an open coffin, crowned and robed.', 'flags': 'f', 'align': -1000,
         'desc': 'A ruler of the kingdom from centuries ago, woken to serve the last queen.',
         'carry': [('pearl_circlet', 30)]},
        {'id': 'pearl_guardian', 'aliases': 'guardian pearl', 'short': 'the pearl guardian', 'role': 'champion', 'level': 85,
         'long': 'A shape of living water and grey light rises from the great pearl.', 'flags': 'bfl', 'align': -1000, 'attack': 'blast',
         'desc': 'The spirit of the kingdom\'s heart, poisoned. It will not let anyone near the queen.'},
        {'id': 'queen_beneath', 'aliases': 'queen beneath', 'short': 'the Queen Beneath', 'role': 'boss', 'level': 85,
         'long': 'The Queen Beneath rises from her coral throne, her hair a cloud of black weed.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'She drowned her kingdom to save it from the West. The West made her its keeper of the black sea, and gave her back her people as drowned things, and she has hated it every day for a hundred years while she served it perfectly.',
         'equip': [('pearl_crown', 'head', 100), ('tide_scepter', 'wield', 100)], 'carry': [('black_pearl', 100)]},
    ],
    'objs': [
        {'id': 'barnacled_cutlass', 'kind': 'weapon', 'level': 82, 'attack': 'slash', 'aliases': 'cutlass barnacled',
         'short': 'a barnacled cutlass', 'long': 'A cutlass crusted with barnacles lies here.'},
        {'id': 'captains_rapier', 'kind': 'weapon', 'level': 85, 'attack': 'pierce', 'aliases': 'rapier captain',
         'short': 'a sea captain\'s rapier', 'long': 'A rapier with a gilded basket hilt lies here.', 'affects': [('hitroll', 4), ('dex', 1)]},
        {'id': 'admiral_coat', 'kind': 'armor', 'slot': 'about', 'level': 85, 'aliases': 'coat admiral',
         'short': 'a drowned admiral\'s coat', 'long': 'A heavy blue coat with gold braid lies here, still damp.', 'affects': [('hit', 50), ('move', 40)]},
        {'id': 'coral_trident', 'kind': 'weapon', 'level': 84, 'attack': 'pierce', 'aliases': 'trident coral',
         'short': 'a coral trident', 'long': 'A trident of black coral lies here.', 'affects': [('mana', 40)]},
        {'id': 'kraken_beak', 'kind': 'weapon', 'level': 86, 'attack': 'pierce', 'aliases': 'beak kraken dagger',
         'short': 'a kraken-beak dagger', 'long': 'A dagger carved from a kraken\'s beak lies here.', 'affects': [('hitroll', 4), ('damroll', 4)]},
        {'id': 'coral_lance', 'kind': 'weapon', 'level': 85, 'attack': 'pierce', 'aliases': 'lance coral',
         'short': 'a coral lance', 'long': 'A long lance of black coral lies here.', 'affects': [('damroll', 2)]},
        {'id': 'coral_plate', 'kind': 'armor', 'slot': 'body', 'level': 85, 'aliases': 'plate coral',
         'short': 'coral-grown plate', 'long': 'A suit of plate grown over with black coral lies here.', 'affects': [('hit', 40)]},
        {'id': 'dissolving_scroll', 'kind': 'note', 'aliases': 'scroll dissolving petition', 'short': 'a dissolving petition',
         'long': 'A scroll that is slowly dissolving lies here.', 'weight': 1,
         'extras': {'scroll petition': 'A petition to the queen from a fisherman, a hundred years old: PLEASE, MAJESTY, LET US GO UP. Granted, it says at the bottom, in a hand that shakes. Never.'}},
        {'id': 'pearl_circlet', 'kind': 'armor', 'slot': 'head', 'level': 85, 'aliases': 'circlet pearl',
         'short': 'a pearl circlet', 'long': 'A circlet of grey pearls lies here.', 'affects': [('wis', 2), ('mana', 40)]},
        {'id': 'pearl_crown', 'kind': 'armor', 'slot': 'head', 'level': 87, 'aliases': 'crown pearl',
         'short': 'the pearl crown of the Queen Beneath', 'long': 'A crown of black and white pearls lies here.',
         'affects': [('hit', 70), ('wis', 2), ('save_spell', -4)]},
        {'id': 'tide_scepter', 'kind': 'weapon', 'level': 87, 'attack': 'bludgeon', 'aliases': 'scepter sceptre tide',
         'short': 'the sceptre of tides', 'long': 'A sceptre of mother-of-pearl, cold and wet, lies here.',
         'affects': [('hitroll', 5), ('damroll', 5), ('mana', 50)]},
        {'id': 'black_pearl', 'kind': 'worn', 'slot': 'neck', 'level': 86, 'aliases': 'pearl black pendant',
         'short': 'a black pearl pendant', 'long': 'A black pearl on a silver chain lies here.', 'affects': [('int', 2), ('con', 2)]},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
ZONE['rooms'] += [
    {'id': 'sunken_fleet', 'name': 'The Sunken Fleet', 'sector': 'underwater',
     'desc': """Beyond the galley lies the whole fleet of the drowned kingdom, a hundred ships
     resting upright on the sea floor in their battle line, sails still set and swaying in
     the current.  Their crews stand at the rails, and turn their heads to watch you.""",
     'exits': {'e': 'galley_hold', 'w': 'admiral_cabin'},
     'mobs': [('drowned_marine', 3)]},
    {'id': 'admiral_cabin', 'name': "The Admiral's Cabin", 'sector': 'underwater',
     'desc': """The great stern cabin of the flagship.  Charts float in the water, and the
     admiral sits at his table with a spyglass to his eye, looking east, planning the
     attack he has been planning for three hundred years.""",
     'mobs': [('drowned_admiral', 1)]},
    {'id': 'drowned_library', 'name': 'The Drowned Library', 'sector': 'underwater',
     'desc': """North of the market stands the kingdom's great library, its shelves still full.
     The books have swollen and burst, and their ink has run out into the water in dark
     clouds that move against the current, and gather, and take shape.""",
     'exits': {'s': 'drowned_market'},
     'mobs': [('ink_horror', 1)]},
    {'id': 'ink_depths', 'name': 'The Ink-Black Depths', 'sector': 'underwater', 'flags': 'a',
     'desc': """West of the kraken's grotto the sea floor drops into a trench so deep and dark that
     your light is swallowed an arm's length away.  Small lights move in the black, lures
     dangling in front of mouths you cannot see.""",
     'exits': {'e': 'kraken_grotto'},
     'mobs': [('deep_angler', 2)]},
    {'id': 'mirror_pool_hall', 'name': 'The Hall of Drowned Mirrors', 'sector': 'underwater',
     'desc': """North of the royal crypt the queen's handmaidens kept her mirrors.  The glass is
     still bright under the water, and in each mirror a pale woman combs her hair.  When
     you pass, they put down their combs and step out.""",
     'exits': {'s': 'royal_crypt'},
     'mobs': [('drowned_handmaiden', 2)]},
    {'id': 'tide_gardens', 'name': 'The Tide Gardens', 'sector': 'underwater',
     'desc': """Above the throne room the queen's gardens grow: forests of black kelp that sway
     like dancers, grey coral shaped like hands, and anemones that close on anything that
     swims too near.  The kelp moves even when the water does not.""",
     'exits': {'s': 'flooded_stair', 'w': 'pearl_vault'},
     'mobs': [('kelp_strangler', 3)]},
    {'id': 'pearl_vault', 'name': 'The Pearl Vault', 'sector': 'underwater',
     'desc': """A domed vault of mother-of-pearl where the kingdom kept its treasure.  It is all
     still here, heaped on the floor, and coiled around it, sleeping, is a leviathan grown
     huge on three hundred years of guarding it.""",
     'mobs': [('pearl_leviathan', 1)]},
    {'id': 'whale_fall', 'name': 'The Whale-Fall', 'sector': 'underwater',
     'desc': """North of the sinking water the skeleton of a whale larger than a cathedral lies on
     the sea floor, its ribs arching overhead.  Eels by the thousand live in its bones, and
     they pour out of it like smoke when you come near.""",
     'exits': {'s': 'sinking'},
     'mobs': [('bone_eels', 2)]},
]
ZONE['mobs'] += [
    {'id': 'drowned_marine', 'aliases': 'marine drowned', 'short': 'a drowned marine', 'role': 'standard', 'level': 83,
     'long': 'A drowned marine climbs down from the rail of his ship, cutlass in hand.', 'flags': 'f', 'align': -800,
     'desc': 'A sailor of the drowned fleet, ready for a battle three hundred years late.',
     'equip': [('drowned_cutlass', 'wield', 15)]},
    {'id': 'drowned_admiral', 'aliases': 'admiral drowned', 'short': 'the Drowned Admiral', 'role': 'champion', 'level': 85,
     'long': 'The Drowned Admiral lowers his spyglass and draws his sword.', 'flags': 'bfl', 'align': -900,
     'desc': 'The admiral who led the kingdom\'s fleet against the West, and lost it, and still commands it.',
     'carry': [('admiral_spyglass', 100)]},
    {'id': 'ink_horror', 'aliases': 'horror ink', 'short': 'an ink horror', 'role': 'elite', 'level': 84,
     'long': 'A cloud of black ink gathers itself into a shape full of written words, and lunges.', 'flags': 'bfl', 'align': -900, 'attack': 'blast',
     'desc': 'Everything the drowned library ever knew, poured out and made hungry.',
     'carry': [('waterlogged_tome', 40)]},
    {'id': 'deep_angler', 'aliases': 'angler deep', 'short': 'a deep angler', 'role': 'elite', 'level': 84,
     'long': 'A light bobs in the darkness, and behind it opens a mouth full of needles.', 'flags': 'f', 'align': -500, 'attack': 'bite',
     'desc': 'A fish of the deep trench, all jaw and lure.'},
    {'id': 'drowned_handmaiden', 'aliases': 'handmaiden drowned', 'short': 'a drowned handmaiden', 'role': 'elite', 'level': 84,
     'long': 'A pale handmaiden steps out of her mirror, comb in hand.', 'flags': 'f', 'align': -800, 'sex': 2, 'attack': 'claw',
     'desc': 'One of the queen\'s maids, drowned with her mistress and still serving her.'},
    {'id': 'kelp_strangler', 'aliases': 'strangler kelp', 'short': 'a kelp strangler', 'role': 'standard', 'level': 83,
     'long': 'A mass of black kelp wraps around you and pulls.', 'flags': 'f', 'align': -500, 'attack': 'whip',
     'desc': 'The queen\'s garden, defending itself.'},
    {'id': 'pearl_leviathan', 'aliases': 'leviathan pearl', 'short': 'the pearl leviathan', 'role': 'champion', 'level': 85,
     'long': 'The pearl leviathan uncoils from its hoard, eyes like lamps.', 'flags': 'bfl', 'align': -600, 'attack': 'bite',
     'desc': 'A sea serpent the length of a ship, grown huge guarding the kingdom\'s treasure.',
     'carry': [('black_pearl', 100)]},
    {'id': 'bone_eels', 'aliases': 'eels bone swarm', 'short': 'a swarm of bone eels', 'role': 'standard', 'level': 82,
     'long': 'A swarm of white eels pours out of the whale\'s ribs.', 'flags': 'f', 'align': -500, 'attack': 'bite',
     'desc': 'Thousands of eels that live on the whale-fall, and on anything else that comes.'},
]
ZONE['objs'] += [
    {'id': 'drowned_cutlass', 'kind': 'weapon', 'level': 83, 'attack': 'slash', 'aliases': 'cutlass drowned',
     'short': 'a barnacled cutlass', 'long': 'A barnacled cutlass lies here.', 'affects': [('hitroll', 3)]},
    {'id': 'admiral_spyglass', 'kind': 'worn', 'slot': 'hold', 'level': 85, 'aliases': 'spyglass admiral',
     'short': "the Drowned Admiral's spyglass", 'long': 'A brass spyglass crusted with coral lies here.', 'affects': [('hitroll', 3), ('dex', 1)]},
    {'id': 'waterlogged_tome', 'kind': 'worn', 'slot': 'hold', 'level': 84, 'aliases': 'tome waterlogged book',
     'short': 'a waterlogged tome', 'long': 'A swollen book lies here, dripping ink.', 'affects': [('mana', 50), ('int', 1)]},
    {'id': 'black_pearl', 'kind': 'worn', 'slot': 'finger', 'level': 86, 'aliases': 'pearl black ring',
     'short': 'a ring set with a black pearl', 'long': 'A ring set with a black pearl lies here.', 'affects': [('hit', 30), ('save_spell', -3)]},
]
