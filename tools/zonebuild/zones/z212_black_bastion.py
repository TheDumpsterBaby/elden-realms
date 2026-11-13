"""W13 The Black Bastion -- the Blight, levels 90-95.

Nu\'Groth\'s outer fortress, built into and out of a black cliff that rises into
the clouds. Its war-forges arm the West, its pens breed its beasts, its prison
holds the heroes of the living, and its generals plan the fall of Midgaard.
The Iron Herald commands them all. Its inner gate leads to the Threshold.
"""

ZONE = {
    'num': 212, 'name': 'The Black Bastion', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'outer_gate', 'name': 'The Outer Gate of the Bastion', 'sector': 'city',
         'desc': """A gate a hundred feet high, of black iron studded with skulls, stands open in the
         fortress wall.  Its towers are lost in mist.  An endless column of grey soldiers
         marches out through it, east, toward the living.  Nobody stops you as you walk in
         against the stream; nobody has ever walked in before.""",
         'exits': {'e': {'to': '@21111', 'back_desc': 'West, the gate of the Black Bastion stands open in the cliff.'}, 'w': 'killing_yard'},
         'mobs': [('bastion_legionary', 2)]},
        {'id': 'killing_yard', 'name': 'The Killing Yard', 'sector': 'city',
         'desc': """A vast yard of black flagstones inside the gate, ringed by walls with archers on
         every merlon.  Grey legions drill here in silence, thousands at a time.  The
         flagstones are stained in patterns, the marks of every test the Bastion\'s
         soldiers must pass.""",
         'exits': {'w': 'inner_court', 'n': 'war_forge', 's': 'beast_pens'},
         'mobs': [('bastion_legionary', 2), ('legion_centurion', 1)]},
        {'id': 'war_forge', 'name': 'The War-Forge', 'sector': 'inside', 'flags': 'd',
         'desc': """A forge so large it has its own weather: hot winds, a rain of sparks, a thunder of
         hammers.  Grey iron from the Shattered Peaks is forged here into the armour of the
         dread legions.  The Forge-General oversees it from a platform of black iron, and
         every blade is tested on a prisoner.""",
         'mobs': [('forge_general', 1), ('forge_thrall', 2)]},
        {'id': 'beast_pens', 'name': 'The Beast Pens', 'sector': 'inside', 'flags': 'd',
         'desc': """Cages of black iron hold the war-beasts of the West: dread hounds, wyverns, things
         that have no names.  The air stinks of musk and blood.  The Beastmaster walks among
         the cages with a whip of chains, and the beasts flinch from him.""",
         'mobs': [('beastmaster', 1), ('war_beast', 2)]},
        {'id': 'inner_court', 'name': 'The Inner Court', 'sector': 'city',
         'desc': """A courtyard of black stone at the heart of the Bastion, overlooked by a tower that
         rises out of sight.  Statues of Nu\'Groth\'s generals stand around it, each one a
         monument to a kingdom destroyed.  The newest plinth stands empty, waiting.  Its
         inscription reads MIDGAARD.""",
         'exits': {'w': 'war_room', 'n': 'prison', 's': 'dark_chapel', 'u': 'herald_tower'},
         'extras': {'plinth inscription midgaard': 'An empty plinth of black stone. Carved in its face: MIDGAARD. Beneath: TO BE RAISED IN THE SPRING.'},
         'mobs': [('dread_guard', 2)]},
        {'id': 'prison', 'name': 'The Prison of Heroes', 'sector': 'inside', 'flags': 'ad',
         'desc': """Cells line a long black gallery, and in each one is a hero of the living: a
         paladin, a queen, a wizard, a knight, all taken alive in battle.  They are not
         hollowed.  They are kept, and every day the Warden of Chains asks each of them
         to kneel.  Most of them still refuse.""",
         'mobs': [('warden_of_chains', 1), ('captive_hero', 2)]},
        {'id': 'dark_chapel', 'name': 'The Chapel of the West', 'sector': 'inside', 'flags': 'ad',
         'desc': """A chapel with no altar, only a window facing west, filled with a darkness that
         moves.  Nu\'Groth\'s priests kneel before it, faces pressed to the floor.  The
         darkness in the window looks back at you, and for a moment you feel the full
         weight of its attention, and your knees begin to bend.""",
         'extras': {'window darkness west': 'You look into the darkness and something vast looks back. It does not hate you. It does not think of you at all. That is worse.'},
         'mobs': [('void_priest', 2)]},
        {'id': 'war_room', 'name': 'The War Room', 'sector': 'inside', 'flags': 'd',
         'desc': """A great hall around a table carved as a map of the whole realm.  Grey figures
         representing armies are placed upon it: the Last Light encircled, the fens
         overrun, the Marches burning, Midgaard surrounded.  The generals of the West
         stand around the table, moving the pieces, and they look up as one.""",
         'exits': {'w': 'inner_gate'},
         'extras': {'table map pieces': 'The whole realm in black stone. The grey armies have already been placed around Midgaard. The plan is finished; only the marching remains.'},
         'mobs': [('dread_general', 2)]},
        {'id': 'herald_tower', 'name': 'The Herald\'s Tower', 'sector': 'inside', 'flags': 'd',
         'desc': """At the top of the tower, in a hall open to the sky on the western side, stands the
         Iron Herald, voice and general of Nu\'Groth, armoured in black iron fused to its
         body.  It was the first and greatest of Nu\'Groth\'s champions, and it speaks with
         Nu\'Groth\'s voice.""",
         'mobs': [('iron_herald', 1)]},
        {'id': 'inner_gate', 'name': 'The Inner Gate', 'sector': 'city',
         'desc': """At the western end of the Bastion a narrow gate of black stone opens onto nothing:
         a grey haze, a sense of distance that does not match the space.  The air ripples
         like heat.  The soldiers do not use this gate.  Beyond it, Nu\'Groth\'s will is
         felt in every breath.""",
         'mobs': [('dread_guard', 1)]},
    ],
    'mobs': [
        {'id': 'bastion_legionary', 'aliases': 'legionary bastion', 'short': 'a Bastion legionary', 'role': 'standard', 'level': 92,
         'long': 'A legionary in black iron marches past, eyes burning grey.', 'flags': 'f', 'align': -1000,
         'desc': 'The elite of the West\'s armies, armoured in grey iron from the Shattered Peaks.',
         'equip': [('legion_blade', 'wield', 60), ('legion_plate', 'body', 25)]},
        {'id': 'legion_centurion', 'aliases': 'centurion legion', 'short': 'a legion centurion', 'role': 'elite', 'level': 94,
         'long': 'A centurion in a crested helm drills the ranks with a black staff.', 'flags': 'f', 'align': -1000,
         'desc': 'It has drilled ten thousand soldiers for the march on Midgaard.',
         'equip': [('centurion_staff', 'wield', 100)]},
        {'id': 'forge_general', 'aliases': 'general forge', 'short': 'the Forge-General', 'role': 'champion', 'level': 95,
         'long': 'The Forge-General turns from the platform, a red-hot blade in each hand.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'Master of the war-forges, who arms every legion the West sends east. Its arms are black iron to the shoulder.',
         'carry': [('forge_general_gauntlets', 100)]},
        {'id': 'forge_thrall', 'aliases': 'thrall forge', 'short': 'a forge thrall', 'role': 'standard', 'level': 91,
         'long': 'A forge thrall hammers grey iron, burned all over.', 'flags': 'f', 'align': -800,
         'desc': 'Hollowed smiths from a dozen fallen kingdoms.',
         'equip': [('forge_hammer', 'wield', 70)]},
        {'id': 'beastmaster', 'aliases': 'beastmaster master beast', 'short': 'the Beastmaster', 'role': 'champion', 'level': 95,
         'long': 'The Beastmaster cracks a whip of chains, and every beast in the pens cowers.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'She breeds the war-beasts of the West from things captured and things made. She has wanted to see what is inside a hero for a long time.',
         'equip': [('chain_whip', 'wield', 100)]},
        {'id': 'war_beast', 'aliases': 'beast war', 'short': 'a war-beast', 'role': 'elite', 'level': 93,
         'long': 'A war-beast with too many eyes throws itself against its cage.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Part hound, part wyvern, part something else.'},
        {'id': 'dread_guard', 'aliases': 'guard dread', 'short': 'a dread guard', 'role': 'elite', 'level': 94,
         'long': 'A dread guard in black plate stands motionless, a glaive in hand.', 'flags': 'f', 'align': -1000,
         'desc': 'The Herald\'s own guard. They have not moved in a hundred years except to kill.',
         'equip': [('dread_glaive', 'wield', 80)]},
        {'id': 'warden_of_chains', 'aliases': 'warden chains', 'short': 'the Warden of Chains', 'role': 'champion', 'level': 95,
         'long': 'The Warden of Chains turns from a cell, chains rattling around its body.', 'flags': 'bfl', 'align': -1000,
         'desc': 'Wrapped in the chains of every prisoner it has broken. It asks you to kneel. It asks very politely.',
         'carry': [('prison_keys', 100), ('chain_mantle', 100)]},
        {'id': 'captive_hero', 'aliases': 'hero captive prisoner', 'short': 'a captive hero', 'role': 'harmless', 'level': 90,
         'long': 'A captive hero in rags grips the bars of a cell.', 'flags': 'b', 'align': 900,
         'desc': 'A legend of the living, taken alive. They have not knelt. They will not kneel. They ask you, if you can, to tell Midgaard that they did not kneel.'},
        {'id': 'void_priest', 'aliases': 'priest void', 'short': 'a void priest', 'role': 'elite', 'level': 94,
         'long': 'A priest of Nu\'Groth rises from the floor, its face a smooth blank.', 'flags': 'f', 'align': -1000,
         'desc': 'It has stared into the western window so long that its face has worn away.',
         'equip': [('void_rod', 'wield', 100)]},
        {'id': 'dread_general', 'aliases': 'general dread', 'short': 'a dread general', 'role': 'champion', 'level': 95,
         'long': 'A dread general looks up from the war table, grey fire in its eyes.', 'flags': 'f', 'align': -1000,
         'desc': 'Each of the generals has destroyed a kingdom. Each has been promised Midgaard.',
         'equip': [('general_sword', 'wield', 100), ('general_plate', 'body', 30)]},
        {'id': 'iron_herald', 'aliases': 'herald iron', 'short': 'the Iron Herald', 'role': 'boss', 'level': 95,
         'long': 'The Iron Herald turns from the western sky, and when it speaks, Nu\'Groth speaks through it.', 'flags': 'bfl', 'align': -1000,
         'desc': 'The first champion of Nu\'Groth, so old that no one remembers what it was before. Its armour has grown into its flesh, and its voice is the voice of the West. "You have come so far," it says. "It changes nothing."',
         'equip': [('herald_blade', 'wield', 100), ('herald_plate', 'body', 100)], 'carry': [('herald_sigil', 100)]},
    ],
    'objs': [
        {'id': 'legion_blade', 'kind': 'weapon', 'level': 92, 'attack': 'slash', 'aliases': 'blade legion',
         'short': 'a legion blade', 'long': 'A grey iron legion blade lies here.'},
        {'id': 'legion_plate', 'kind': 'armor', 'slot': 'body', 'level': 92, 'aliases': 'plate legion',
         'short': 'legion plate', 'long': 'A suit of grey iron legion plate lies here.'},
        {'id': 'centurion_staff', 'kind': 'weapon', 'level': 94, 'attack': 'bludgeon', 'aliases': 'staff centurion black',
         'short': 'a centurion\'s black staff', 'long': 'A black iron staff lies here.', 'affects': [('hitroll', 3)]},
        {'id': 'forge_general_gauntlets', 'kind': 'armor', 'slot': 'hands', 'level': 96, 'aliases': 'gauntlets forge general',
         'short': 'the Forge-General\'s gauntlets', 'long': 'A pair of black iron gauntlets, still warm, lies here.',
         'affects': [('str', 2), ('damroll', 4)]},
        {'id': 'forge_hammer', 'kind': 'weapon', 'level': 91, 'attack': 'pound', 'aliases': 'hammer forge',
         'short': 'a forge hammer', 'long': 'A heavy forge hammer lies here.'},
        {'id': 'chain_whip', 'kind': 'weapon', 'level': 96, 'attack': 'whip', 'aliases': 'whip chain',
         'short': 'a whip of chains', 'long': 'A whip of linked black chains lies here.', 'affects': [('hitroll', 4), ('damroll', 4)]},
        {'id': 'dread_glaive', 'kind': 'weapon', 'level': 94, 'attack': 'slash', 'aliases': 'glaive dread', 'two_handed': True,
         'short': 'a dread glaive', 'long': 'A black glaive lies here.', 'affects': [('damroll', 3)]},
        {'id': 'prison_keys', 'kind': 'key', 'aliases': 'keys prison ring', 'short': 'a ring of black keys',
         'long': 'A ring of black iron keys lies here.', 'weight': 1},
        {'id': 'chain_mantle', 'kind': 'armor', 'slot': 'about', 'level': 96, 'aliases': 'mantle chain',
         'short': 'a mantle of broken chains', 'long': 'A mantle of broken chains lies here.', 'affects': [('hit', 60), ('save_para', -4)]},
        {'id': 'void_rod', 'kind': 'weapon', 'level': 94, 'attack': 'bludgeon', 'aliases': 'rod void',
         'short': 'a void rod', 'long': 'A rod of black glass that swallows the light lies here.', 'affects': [('mana', 60), ('int', 1)]},
        {'id': 'general_sword', 'kind': 'weapon', 'level': 95, 'attack': 'slash', 'aliases': 'sword general',
         'short': 'a dread general\'s sword', 'long': 'A long black sword lies here.', 'affects': [('hitroll', 4), ('damroll', 3)]},
        {'id': 'general_plate', 'kind': 'armor', 'slot': 'body', 'level': 95, 'aliases': 'plate general',
         'short': 'a dread general\'s plate', 'long': 'A suit of black plate lies here.', 'affects': [('hit', 50)]},
        {'id': 'herald_blade', 'kind': 'weapon', 'level': 98, 'attack': 'slash', 'aliases': 'blade herald',
         'short': 'the Herald\'s blade', 'long': 'A sword of black iron that hums with a voice lies here.',
         'affects': [('hitroll', 6), ('damroll', 6)]},
        {'id': 'herald_plate', 'kind': 'armor', 'slot': 'body', 'level': 98, 'aliases': 'plate herald',
         'short': 'the Herald\'s plate', 'long': 'A suit of black plate, warm as flesh, lies here.',
         'affects': [('hit', 80), ('con', 2), ('save_spell', -4)]},
        {'id': 'herald_sigil', 'kind': 'worn', 'slot': 'finger', 'level': 96, 'aliases': 'sigil herald ring',
         'short': 'the Herald\'s sigil ring', 'long': 'A ring of black iron bearing a spiral lies here.',
         'affects': [('str', 2), ('dex', 2), ('hitroll', 2)]},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
ZONE['rooms'] += [
    {'id': 'north_rampart', 'name': 'The North Rampart', 'sector': 'city',
     'desc': """A wall walk along the Bastion's northern rampart, wide enough for four to march
     abreast.  Black-fletched archers line the battlements, and the stone is pocked with
     the scars of a siege that ended before Midgaard had a wall.""",
     'exits': {'s': 'outer_gate', 'w': 'siege_engines'},
     'mobs': [('bastion_archer', 2)]},
    {'id': 'siege_engines', 'name': 'The Siege Engines', 'sector': 'city',
     'desc': """Great engines of black timber and grey iron stand in a row on a platform behind the
     rampart: trebuchets, bolt-throwers, a ram as long as a ship.  They are being made
     ready to roll east.  Crews of hollowed men work them under a master's eye.""",
     'mobs': [('siege_crew', 2), ('engine_master', 1)]},
    {'id': 'south_rampart', 'name': 'The South Rampart', 'sector': 'city',
     'desc': """The southern rampart of the Bastion looks down over the burnt siegeworks and the
     edge of the Weeping Forest.  Archers watch the treeline, and every so often loose a
     black arrow at something moving there.""",
     'exits': {'n': 'outer_gate', 'w': 'gibbet_walk'},
     'mobs': [('bastion_archer', 2)]},
    {'id': 'gibbet_walk', 'name': 'The Gibbet Walk', 'sector': 'city',
     'desc': """A stretch of wall hung with iron gibbets, each holding a body: heroes of the east
     who came this far.  Their names are painted on the cages in the Bastion's script.
     Grey crows sit on the cages and argue over what is left.""",
     'mobs': [('gibbet_crow', 3)]},
    {'id': 'smelting_pits', 'name': 'The Smelting Pits', 'sector': 'inside',
     'desc': """North of the war-forge, pits of molten grey iron glow in the dark, and thralls
     carry crucibles along narrow walkways above them.  When a thrall falls, nobody stops
     working.  Something made of slag rises from the deepest pit.""",
     'exits': {'s': 'war_forge'},
     'mobs': [('forge_thrall', 2), ('slag_elemental', 1)]},
    {'id': 'drake_stalls', 'name': 'The Drake Stalls', 'sector': 'inside',
     'desc': """South of the beast pens, vaulted stalls hold the Bastion's war-drakes, grey and
     wingless, bred for pulling engines and breaking walls.  Each stall is scorched black
     inside.""",
     'exits': {'n': 'beast_pens', 'w': 'brood_pen'},
     'mobs': [('grey_drake', 2)]},
    {'id': 'brood_pen', 'name': 'The Brood Pen', 'sector': 'inside',
     'desc': """A vast pen strewn with broken eggshell and bones, where the drakes are bred.  The
     brood-mother lies coiled around her clutch, larger than any of her children, and she
     opens one eye as you enter.""",
     'mobs': [('drake_broodmother', 1)]},
    {'id': 'oubliette', 'name': 'The Oubliette', 'sector': 'inside', 'flags': 'a',
     'desc': """A pit beneath the prison where prisoners are dropped and forgotten.  It is utterly
     dark.  The forgotten are still down here, those who did not die, and they have been
     alone in the dark so long they have forgotten what they were.""",
     'exits': {'s': 'prison'},
     'mobs': [('forgotten_prisoner', 3)]},
    {'id': 'question_hall', 'name': 'The Hall of Questions', 'sector': 'inside',
     'desc': """A long hall of chains and tables where the Bastion's inquisitor asks prisoners
     about the east: its roads, its walls, its weak places.  A map of Midgaard is pinned
     to the wall.  It is very accurate.""",
     'exits': {'e': 'prison'},
     'mobs': [('inquisitor', 1)],
     'extras': {'map midgaard': 'A map of Midgaard drawn in a careful hand, every gate and tower marked, every street named. The west gate is circled. Someone inside the fort has been telling them everything.'}},
    {'id': 'void_altar', 'name': 'The Altar of the Void', 'sector': 'inside',
     'desc': """Below the dark chapel, an altar stands over a hole in the floor that has no
     bottom and gives off a cold grey light.  Acolytes kneel around it, feeding it
     offerings that drop into the light and are not heard to land.""",
     'exits': {'n': 'dark_chapel'},
     'mobs': [('void_acolyte', 2)]},
    {'id': 'tower_top', 'name': "The Top of the Herald's Tower", 'sector': 'mountain',
     'desc': """The roof of the herald's tower, high above the Bastion, swept by a wind that never
     stops.  From here you can see west into the Threshold, where the land thins into grey
     nothing.  Harpies roost on the tower's horns.""",
     'exits': {'d': 'herald_tower'},
     'mobs': [('storm_harpy', 2)]},
    {'id': 'map_vault', 'name': 'The Map Vault', 'sector': 'inside',
     'desc': """North of the war room, a vault of shelves full of rolled maps: every road, river
     and wall in the east, gathered over centuries by spies and the tortured.  A staff
     officer sits at a table, updating them.""",
     'exits': {'s': 'war_room'},
     'mobs': [('staff_officer', 1)], 'objs': [('war_map', 1)]},
    {'id': 'officers_quarters', 'name': "The Officers' Quarters", 'sector': 'inside',
     'desc': """Plain stone rooms behind the inner gate where the Bastion's dread officers sleep,
     if they sleep.  Their armour stands on racks by their beds, and some of the armour is
     standing by itself.""",
     'exits': {'s': 'inner_gate'},
     'mobs': [('dread_officer', 2)]},
    {'id': 'legion_barracks', 'name': 'The Legion Barracks', 'sector': 'inside',
     'desc': """A long hall of iron bunks where the legion musters.  There are bunks enough for ten
     thousand, and most of them are empty, because most of the legion is already marching
     east.""",
     'exits': {'n': 'inner_gate'},
     'mobs': [('bastion_legionary', 3)]},
]
ZONE['mobs'] += [
    {'id': 'bastion_archer', 'aliases': 'archer bastion', 'short': 'a Bastion archer', 'role': 'standard', 'level': 92,
     'long': 'A Bastion archer turns from the battlements and draws a black arrow.', 'flags': 'f', 'align': -1000, 'attack': 'pierce',
     'desc': 'A hollowed bowman of the Bastion, who never misses and never tires.',
     'carry': [('archer_bracer', 20)]},
    {'id': 'siege_crew', 'aliases': 'crew siege thrall', 'short': 'a siege crewman', 'role': 'standard', 'level': 91,
     'long': 'A hollowed siege crewman drops his rope and comes at you.', 'flags': 'f', 'align': -800, 'attack': 'punch',
     'desc': 'A thrall worked hollow at the engines.'},
    {'id': 'engine_master', 'aliases': 'master engine', 'short': 'the engine master', 'role': 'elite', 'level': 94,
     'long': 'The engine master looks up from his plans, a hammer in his iron hand.', 'flags': 'bfl', 'align': -1000, 'attack': 'pound',
     'desc': 'The engineer who builds the engines that will break Midgaard\'s wall.'},
    {'id': 'gibbet_crow', 'aliases': 'crow gibbet grey', 'short': 'a gibbet crow', 'role': 'standard', 'level': 92,
     'long': 'A grey crow as big as a dog flaps down from a gibbet.', 'flags': 'f', 'align': -600, 'attack': 'pierce',
     'desc': 'Fat on heroes.'},
    {'id': 'slag_elemental', 'aliases': 'elemental slag', 'short': 'a slag elemental', 'role': 'elite', 'level': 94,
     'long': 'A shape of molten slag heaves itself out of the pit.', 'flags': 'f', 'align': -800, 'attack': 'crush',
     'desc': 'The waste of the grey iron, given a shape and a temper.'},
    {'id': 'grey_drake', 'aliases': 'drake grey war', 'short': 'a grey war-drake', 'role': 'elite', 'level': 94,
     'long': 'A wingless grey war-drake lunges against its chain.', 'flags': 'f', 'align': -700, 'attack': 'bite',
     'desc': 'Bred to pull engines and break walls.'},
    {'id': 'drake_broodmother', 'aliases': 'broodmother drake mother', 'short': 'the drake brood-mother', 'role': 'champion', 'level': 95,
     'long': 'The drake brood-mother uncoils from her clutch, fire in her throat.', 'flags': 'bfl', 'align': -800, 'attack': 'bite', 'sex': 2,
     'desc': 'The mother of every war-drake in the Bastion, huge and ancient.',
     'carry': [('drake_scale_mail', 100)]},
    {'id': 'forgotten_prisoner', 'aliases': 'prisoner forgotten', 'short': 'a forgotten prisoner', 'role': 'standard', 'level': 91,
     'long': 'A pale thing that was a prisoner crawls toward your light.', 'flags': 'f', 'align': -300, 'attack': 'claw',
     'desc': 'Alone in the dark so long that it has forgotten everything but hunger.'},
    {'id': 'inquisitor', 'aliases': 'inquisitor', 'short': 'the Inquisitor', 'role': 'champion', 'level': 95,
     'long': 'The Inquisitor sets down a hot iron and smiles at you.', 'flags': 'bfl', 'align': -1000, 'attack': 'stab',
     'desc': 'The Bastion\'s questioner. Everyone answers him in the end.',
     'carry': [('inquisitor_brand', 100)]},
    {'id': 'void_acolyte', 'aliases': 'acolyte void', 'short': 'a void acolyte', 'role': 'standard', 'level': 93,
     'long': 'A void acolyte rises from the altar, grey light pouring from its mouth.', 'flags': 'f', 'align': -1000, 'attack': 'blast',
     'desc': 'A priest of the hole in the floor.',
     'carry': [('void_censer', 20)]},
    {'id': 'storm_harpy', 'aliases': 'harpy storm', 'short': 'a storm harpy', 'role': 'elite', 'level': 93,
     'long': 'A storm harpy shrieks and dives from the tower\'s horn.', 'flags': 'f', 'align': -900, 'attack': 'claw', 'sex': 2,
     'desc': 'A grey-winged hag of the high winds.'},
    {'id': 'staff_officer', 'aliases': 'officer staff', 'short': 'a staff officer', 'role': 'elite', 'level': 93,
     'long': 'A staff officer in black looks up from the maps and draws his sword.', 'flags': 'bfl', 'align': -1000,
     'desc': 'He knows the east better than anyone living in it.'},
    {'id': 'dread_officer', 'aliases': 'officer dread', 'short': 'a dread officer', 'role': 'elite', 'level': 94,
     'long': 'A dread officer rises from his bunk, already armoured.', 'flags': 'f', 'align': -1000,
     'desc': 'An officer of the legion, dead and tireless.'},
]
ZONE['objs'] += [
    {'id': 'archer_bracer', 'kind': 'armor', 'slot': 'wrist', 'level': 92, 'aliases': 'bracer archer black',
     'short': "a black archer's bracer", 'long': "A black leather archer's bracer lies here.", 'affects': [('hitroll', 2)]},
    {'id': 'drake_scale_mail', 'kind': 'armor', 'slot': 'body', 'level': 96, 'aliases': 'mail drake scale',
     'short': 'a coat of drake-scale mail', 'long': 'A coat of grey drake scales lies here.', 'affects': [('hit', 40), ('dex', 1)]},
    {'id': 'inquisitor_brand', 'kind': 'weapon', 'level': 94, 'attack': 'stab', 'aliases': 'brand iron inquisitor',
     'short': "the Inquisitor's brand", 'long': 'A long iron brand, still hot, lies here.', 'affects': [('hitroll', 4), ('damroll', 2)]},
    {'id': 'void_censer', 'kind': 'worn', 'slot': 'hold', 'level': 93, 'aliases': 'censer void',
     'short': 'a void censer', 'long': 'A censer leaking grey light lies here.', 'affects': [('mana', 40)]},
    {'id': 'war_map', 'kind': 'other', 'level': 90, 'aliases': 'map war campaign', 'cost': 2000,
     'short': 'a campaign map of the east', 'long': 'A rolled campaign map lies here.',
     'extras': {'map campaign': 'The Bastion\'s plan for the east: the legions to march through the march, the engines to break the west gate of Midgaard, and a note in the margin, "the sappers will be under the wall by midwinter."'}},
]
