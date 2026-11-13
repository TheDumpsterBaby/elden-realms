"""W10 The Shattered Peaks -- the Blight, levels 75-80.

A mountain range split open by some ancient blow. Beneath it lies a great
dwarven hold (working name Durhold) whose clans fell to the West and now forge
the grey iron its armies wear. Wyverns nest on the broken cliffs; in the
deepest hall the Forge-King has fused with his own furnace.
"""

ZONE = {
    'num': 209, 'name': 'The Shattered Peaks', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'mountain_path', 'name': 'The Mountain Path', 'sector': 'mountain',
         'desc': """A path climbs from the barrow-lands into the mountains, cut into the rock by
         dwarven hands long ago.  The peaks above are split and jagged, as if something
         vast struck them from the sky.  Cold wind howls down the path, carrying the
         distant ring of hammers from deep inside the stone.""",
         'exits': {'e': {'to': '@20816', 'back_desc': 'A path climbs west into the Shattered Peaks.'}, 'u': 'split_pass'},
         'mobs': [('grey_dwarf_scout', 1)]},
        {'id': 'split_pass', 'name': 'The Split Pass', 'sector': 'mountain',
         'desc': """The path enters a cleft where a whole mountain has been split in two, its halves
         standing apart like the pages of a book.  The cliffs on either side rise sheer
         for a thousand feet.  High above, dark shapes circle against the grey sky,
         screaming.""",
         'exits': {'w': 'chasm_bridge', 'n': 'wyvern_ledges'},
         'mobs': [('rock_horror', 1)]},
        {'id': 'wyvern_ledges', 'name': 'The Wyvern Ledges', 'sector': 'mountain',
         'desc': """A narrow ledge climbs the face of the split mountain toward a line of caves.  The
         rock is white with droppings and littered with bones: goats, dwarves, a
         horse.  Wyverns perch on every outcrop, grey-scaled and barb-tailed, and they
         have seen you.""",
         'exits': {'u': 'wyvern_eyrie'},
         'mobs': [('grey_wyvern', 2)]},
        {'id': 'wyvern_eyrie', 'name': 'The Iron Eyrie', 'sector': 'mountain',
         'desc': """A great cave high on the cliff, its mouth ringed with broken iron.  A wyvern
         larger than any other sleeps on a hoard of armour and weapons stolen from the
         dwarves.  Its scales have grown over with grey iron where the West\'s smiths
         armoured it.""",
         'mobs': [('iron_wyvern', 1)]},
        {'id': 'chasm_bridge', 'name': 'The Bridge over the Abyss', 'sector': 'mountain',
         'desc': """A stone bridge with no rail spans a chasm so deep that its bottom is lost in
         darkness.  Hot air rises from below, smelling of sulphur.  Halfway across, the
         bridge is cracked through, and the crack widens a little every time someone
         crosses.""",
         'exits': {'w': 'hold_gate', 'd': 'abyss_ledge'},
         'mobs': [('rock_horror', 1)]},
        {'id': 'abyss_ledge', 'name': 'A Ledge in the Abyss', 'sector': 'mountain', 'flags': 'a',
         'desc': """You climb down onto a narrow ledge below the bridge.  The heat is intense and the
         rock trembles.  Far below, a red glow pulses like a heartbeat.  Something lives
         on this ledge: a nest of bones and slag, and claw marks deep in the stone.""",
         'mobs': [('magma_crawler', 2)]},
        {'id': 'hold_gate', 'name': 'The Gate of Durhold', 'sector': 'mountain',
         'desc': """A gate of black iron fifty feet high is set into the mountain\'s face, carved
         with kings and anvils.  One leaf hangs broken.  The dwarves who guarded it
         stand in their places still, grey-skinned, grey-bearded, their eyes black,
         and they raise their axes as you approach.""",
         'exits': {'w': 'great_hall'},
         'mobs': [('grey_dwarf_warrior', 2)]},
        {'id': 'great_hall', 'name': 'The Great Hall of Durhold', 'sector': 'inside', 'flags': 'd',
         'desc': """A hall carved from the living rock, so vast its roof is lost in darkness.  Great
         pillars carved as dwarven kings hold up the mountain.  The tables where a
         thousand dwarves feasted are overturned and covered with grey dust.  The ring
         of hammers is very loud here.""",
         'exits': {'w': 'forge_halls', 'n': 'barracks', 's': 'mine_shaft'},
         'mobs': [('grey_dwarf_warrior', 2), ('grey_dwarf_thane', 1)]},
        {'id': 'barracks', 'name': 'The Clan Barracks', 'sector': 'inside', 'flags': 'd',
         'desc': """Long halls of stone bunks where the warriors of the clans slept.  They are full
         again, with grey dwarves lying in them with open eyes, waiting to be called.
         Their weapons lie beside them, newly forged, the metal grey and dull.""",
         'mobs': [('grey_dwarf_warrior', 3)]},
        {'id': 'forge_halls', 'name': 'The Forge Halls', 'sector': 'inside', 'flags': 'd',
         'desc': """A hall of a hundred forges, all burning.  Grey dwarves beat out armour and
         blades in grey iron, stacking them in racks for the West\'s armies.  They work
         without speaking, without pausing.  Iron golems carry the finished pieces down
         a ramp toward the deep.""",
         'exits': {'w': 'deep_ramp'},
         'mobs': [('grey_dwarf_smith', 2), ('iron_golem', 1)]},
        {'id': 'mine_shaft', 'name': 'The Great Shaft', 'sector': 'inside', 'flags': 'ad',
         'desc': """A shaft drops into the mountain\'s heart, with a stair spiralling down its walls.
         The dwarves dug too deep here, the legends said, and woke something.  Grey
         iron ore glistens in the walls.  It is warm to the touch, and it pulses.""",
         'exits': {'d': 'living_vein'},
         'mobs': [('rock_horror', 2)]},
        {'id': 'living_vein', 'name': 'The Living Vein', 'sector': 'inside', 'flags': 'ad',
         'desc': """At the bottom of the shaft, a vein of grey ore as wide as a river runs through the
         rock, and it is alive: it moves, slowly, like a muscle, and it whispers.  The
         dwarves mined it to make their iron.  The iron carries its whisper into everyone
         who wears it.""",
         'extras': {'vein ore grey': 'The ore whispers in the voice of Nu\'Groth. Every blade and helm forged from it carries a little of that voice to its wearer.'},
         'mobs': [('ore_elemental', 2)]},
        {'id': 'deep_ramp', 'name': 'The Deep Ramp', 'sector': 'inside', 'flags': 'd',
         'desc': """A broad ramp descends into the depths of the hold, worn smooth by iron carts.  The
         heat grows with every step.  Statues of the dwarven kings line it, and every one
         has had its face struck off and replaced with a grey iron mask.""",
         'exits': {'d': 'kings_forge', 'w': 'treasury'},
         'mobs': [('iron_golem', 1), ('grey_dwarf_thane', 1)]},
        {'id': 'treasury', 'name': 'The Plundered Treasury', 'sector': 'inside', 'flags': 'd',
         'desc': """The treasury of Durhold, its great vault door torn open.  Most of the gold is
         gone, melted for the West.  What remains is heaped carelessly: crowns, cups,
         ancient armour.  An iron golem stands guard over it, very old, very large.""",
         'mobs': [('vault_golem', 1)]},
        {'id': 'kings_forge', 'name': 'The Forge of the King', 'sector': 'inside', 'flags': 'd',
         'desc': """The deepest hall of Durhold, a cavern around a forge as big as a house, burning
         with grey fire.  The Forge-King stands in the fire itself, his body fused with
         the furnace, his beard a cascade of molten iron.  He forges with his bare hands,
         and every blade he makes is a blade for Nu\'Groth.""",
         'exits': {'w': 'deep_tunnel'},
         'mobs': [('forge_king', 1)]},
        {'id': 'deep_tunnel', 'name': 'The Western Tunnel', 'sector': 'inside', 'flags': 'ad',
         'desc': """Behind the king\'s forge a tunnel leads west through the roots of the mountains,
         long and dark and dripping.  The air grows cold and wet.  Far ahead, you hear
         water: the slow lap of a vast underground sea against a stone shore.""",
         'mobs': [('magma_crawler', 1)]},
    ],
    'mobs': [
        {'id': 'grey_dwarf_scout', 'aliases': 'dwarf scout grey', 'short': 'a grey dwarf scout', 'role': 'standard', 'level': 76,
         'long': 'A grey dwarf scout crouches behind a rock, crossbow levelled.', 'flags': 'f', 'align': -900, 'sex': 1,
         'desc': 'Black-eyed and silent. The clans fell to the West a hundred years ago, and their scouts still watch the passes.',
         'equip': [('grey_crossbow', 'wield', 80)]},
        {'id': 'rock_horror', 'aliases': 'horror rock', 'short': 'a rock horror', 'role': 'standard', 'level': 77,
         'long': 'A boulder unfolds into a creature of stone and grey iron.', 'flags': 'f', 'align': -800, 'attack': 'crush',
         'desc': 'Born from the living vein, it is stone with a grey iron heart.'},
        {'id': 'grey_wyvern', 'aliases': 'wyvern grey', 'short': 'a grey wyvern', 'role': 'elite', 'level': 78,
         'long': 'A grey wyvern drops from the cliff, its barbed tail raised.', 'flags': 'f', 'align': -600, 'attack': 'sting',
         'desc': 'Lean and screaming, its sting carries a venom that turns the blood to grey sludge.'},
        {'id': 'iron_wyvern', 'aliases': 'wyvern iron', 'short': 'the Iron Wyvern', 'role': 'champion', 'level': 80,
         'long': 'A huge wyvern armoured in grey iron rises from its hoard, screaming.', 'flags': 'bfl', 'align': -800, 'attack': 'sting',
         'desc': 'The West\'s smiths armoured it with plates bolted to its scales, and it guards the pass for them.',
         'carry': [('wyvern_barb', 100), ('iron_scale_bracers', 100)]},
        {'id': 'magma_crawler', 'aliases': 'crawler magma', 'short': 'a magma crawler', 'role': 'elite', 'level': 78,
         'long': 'A thing like a centipede made of cooling lava crawls out of a crack.', 'flags': 'f', 'align': -700, 'attack': 'bite',
         'desc': 'It glows red where its plates part.'},
        {'id': 'grey_dwarf_warrior', 'aliases': 'dwarf warrior grey', 'short': 'a grey dwarf warrior', 'role': 'standard', 'level': 78,
         'long': 'A grey dwarf warrior raises a grey iron axe.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'Clad head to foot in grey iron that whispers. He does not remember his clan or his name.',
         'equip': [('grey_dwarf_axe', 'wield', 70), ('grey_dwarf_mail', 'body', 25)]},
        {'id': 'grey_dwarf_thane', 'aliases': 'thane dwarf grey', 'short': 'a grey thane', 'role': 'elite', 'level': 80,
         'long': 'A grey thane in a horned helm surveys the hall.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'A lord of one of the fallen clans, still leading his warriors, now for the West.',
         'equip': [('thane_hammer', 'wield', 100), ('horned_helm', 'head', 40)]},
        {'id': 'grey_dwarf_smith', 'aliases': 'smith dwarf grey', 'short': 'a grey dwarf smith', 'role': 'standard', 'level': 77,
         'long': 'A grey dwarf smith beats grey iron on an anvil.', 'flags': 'f', 'align': -900, 'sex': 1,
         'desc': 'The finest smiths in the world once. Now they make armour for the dead.',
         'equip': [('smith_hammer', 'wield', 100)]},
        {'id': 'iron_golem', 'aliases': 'golem iron', 'short': 'an iron golem', 'role': 'elite', 'level': 79,
         'long': 'An iron golem carries a load of armour, steam hissing from its joints.', 'flags': 'f', 'align': -500, 'attack': 'pound',
         'desc': 'Built by the dwarves to work the forges. The West\'s iron has given it a will, and the will is not kind.'},
        {'id': 'ore_elemental', 'aliases': 'elemental ore', 'short': 'an ore elemental', 'role': 'elite', 'level': 79,
         'long': 'A mass of living grey ore pulls itself out of the vein.', 'flags': 'f', 'align': -900, 'attack': 'crush',
         'desc': 'A piece of the vein itself, whispering.'},
        {'id': 'vault_golem', 'aliases': 'golem vault', 'short': 'the vault golem', 'role': 'champion', 'level': 80,
         'long': 'An ancient iron golem twice your height stands guard over the treasury.', 'flags': 'bfl', 'align': 0, 'attack': 'pound',
         'desc': 'It was built to guard the treasury of Durhold before the West came, and it still does, against everyone.',
         'carry': [('durhold_crown', 100)]},
        {'id': 'forge_king', 'aliases': 'king forge forge-king', 'short': 'the Forge-King', 'role': 'boss', 'level': 80,
         'long': 'The Forge-King turns in the heart of his furnace, his beard a river of molten iron.', 'flags': 'bfl', 'align': -1000, 'sex': 1, 'attack': 'pound',
         'desc': 'Last king of Durhold, who dug too deep and found the living vein, and heard the voice in it, and listened. He has become one with his forge, and every blade the West carries was born in his hands.',
         'carry': [('forge_heart', 100), ('kingsforge_hammer', 100)]},
    ],
    'objs': [
        {'id': 'grey_crossbow', 'kind': 'weapon', 'level': 76, 'attack': 'pierce', 'aliases': 'crossbow grey',
         'short': 'a grey iron crossbow', 'long': 'A heavy grey iron crossbow lies here.'},
        {'id': 'wyvern_barb', 'kind': 'weapon', 'level': 80, 'attack': 'pierce', 'aliases': 'barb wyvern dagger',
         'short': 'a wyvern-barb dagger', 'long': 'A dagger made from a wyvern\'s barb lies here.', 'affects': [('hitroll', 4), ('damroll', 3)]},
        {'id': 'iron_scale_bracers', 'kind': 'armor', 'slot': 'arms', 'level': 80, 'aliases': 'bracers iron scale',
         'short': 'iron-scale vambraces', 'long': 'A pair of vambraces of iron-plated scales lies here.', 'affects': [('hit', 40), ('str', 1)]},
        {'id': 'grey_dwarf_axe', 'kind': 'weapon', 'level': 78, 'attack': 'slash', 'aliases': 'axe dwarf grey',
         'short': 'a grey dwarven axe', 'long': 'A grey iron dwarven axe lies here.'},
        {'id': 'grey_dwarf_mail', 'kind': 'armor', 'slot': 'body', 'level': 78, 'aliases': 'mail dwarf grey',
         'short': 'grey dwarven mail', 'long': 'A coat of grey dwarven mail lies here, whispering.'},
        {'id': 'thane_hammer', 'kind': 'weapon', 'level': 80, 'attack': 'pound', 'aliases': 'hammer thane',
         'short': 'a thane\'s warhammer', 'long': 'A rune-carved warhammer lies here.', 'affects': [('damroll', 3)]},
        {'id': 'horned_helm', 'kind': 'armor', 'slot': 'head', 'level': 80, 'aliases': 'helm horned',
         'short': 'a horned dwarven helm', 'long': 'A horned dwarven helm lies here.', 'affects': [('hit', 30)]},
        {'id': 'smith_hammer', 'kind': 'weapon', 'level': 77, 'attack': 'pound', 'aliases': 'hammer smith',
         'short': 'a dwarven smith\'s hammer', 'long': 'A dwarven smith\'s hammer lies here.'},
        {'id': 'durhold_crown', 'kind': 'armor', 'slot': 'head', 'level': 81, 'aliases': 'crown durhold',
         'short': 'the crown of Durhold', 'long': 'A heavy crown of red gold, untouched by grey, lies here.',
         'affects': [('hit', 50), ('con', 2), ('save_spell', -3)]},
        {'id': 'forge_heart', 'kind': 'worn', 'slot': 'hold', 'level': 82, 'aliases': 'heart forge',
         'short': 'the heart of the forge', 'long': 'A lump of grey iron, still glowing, beats slowly here.',
         'affects': [('str', 3), ('damroll', 3), ('hit', 40)]},
        {'id': 'kingsforge_hammer', 'kind': 'weapon', 'level': 82, 'attack': 'pound', 'aliases': 'hammer kingsforge', 'two_handed': True,
         'short': 'the hammer of the Forge-King', 'long': 'A great forge hammer, still warm, lies here.',
         'affects': [('hitroll', 4), ('damroll', 6)]},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
ZONE['rooms'] += [
    {'id': 'storm_summit', 'name': 'The Storm Summit', 'sector': 'mountain',
     'desc': """Above the wyvern eyrie the mountain ends in a summit of shattered stone where grey
     lightning strikes without pause.  The air tastes of iron.  A giant crouches among the
     rocks, frost in its beard, and it is not a giant of the mountains any more.""",
     'exits': {'d': 'wyvern_eyrie', 'w': 'sky_shrine'},
     'mobs': [('frost_giant', 2)]},
    {'id': 'sky_shrine', 'name': 'The Shrine of the Old Sky', 'sector': 'inside',
     'desc': """A small round shrine on the summit, open to the storm, where the dwarves once
     prayed to the sky.  The altar has been split by lightning, and a grey priest kneels at
     it, praying now to something else.""",
     'mobs': [('sky_priest', 1)]},
    {'id': 'abyss_floor', 'name': 'The Floor of the Chasm', 'sector': 'inside', 'flags': 'a',
     'desc': """The bottom of the chasm, a mile below the bridge.  It is utterly dark, and the
     floor is a field of broken bodies, everything that ever fell from the bridge above.
     Something large moves among them, feeding.""",
     'exits': {'u': 'abyss_ledge', 'w': 'fire_river'},
     'mobs': [('chasm_horror', 1)]},
    {'id': 'fire_river', 'name': 'The River of Fire', 'sector': 'inside',
     'desc': """A river of molten rock runs through the roots of the mountain, lighting the cavern
     red.  The heat is terrible.  Shapes of living fire rise from it and walk on its
     banks.""",
     'mobs': [('magma_crawler', 1), ('fire_elemental', 2)]},
    {'id': 'grey_armoury', 'name': 'The Grey Armoury', 'sector': 'inside',
     'desc': """Behind the barracks lies the armoury of the grey dwarves, rack upon rack of grey
     iron weapons and armour waiting to be sent east to the legions.  Every blade hums
     faintly with the voice of Nu\'Groth.""",
     'exits': {'s': 'barracks'},
     'mobs': [('armoury_warden', 1)]},
    {'id': 'crystal_cavern', 'name': 'The Crystal Cavern', 'sector': 'inside',
     'desc': """West of the living vein the ore gives way to a cavern of grey crystal that grows
     as you watch, spreading across the walls like frost.  Figures of crystal stand in it,
     dwarves who stood too long and were grown over.""",
     'exits': {'e': 'living_vein', 'w': 'heart_mountain'},
     'mobs': [('crystal_golem', 2)]},
    {'id': 'heart_mountain', 'name': 'The Heart of the Mountain', 'sector': 'inside',
     'desc': """At the centre of the crystal is the heart of the mountain: a vast slow-beating
     stone, the spirit the dwarves once worshipped.  The grey has reached it.  Its beat is
     wrong, and it has woken, and it is in pain.""",
     'mobs': [('mountain_heart', 1)]},
    {'id': 'slave_pens', 'name': 'The Slave Pens', 'sector': 'inside',
     'desc': """Iron cages line the tunnel, full of dwarves and men taken in raids on the east,
     worked in the mines until they hollow.  A driver walks the cages with a whip.""",
     'exits': {'s': 'deep_tunnel'},
     'mobs': [('slave_driver', 1), ('chained_slave', 2)]},
    {'id': 'ore_road', 'name': 'The Ore Road', 'sector': 'inside',
     'desc': """A wide tunnel with iron rails where carts of grey ore rumble toward the forges.
     Hollowed haulers push them without rest.""",
     'exits': {'n': 'deep_tunnel'},
     'mobs': [('ore_hauler', 2), ('grey_dwarf_warrior', 1)]},
    {'id': 'grey_anvil_hall', 'name': 'The Anvil of Grey Iron', 'sector': 'inside',
     'desc': """North of the king's forge stands the great anvil where the first grey iron was
     beaten, an anvil of black stone the size of a house.  A spirit of the forge burns
     above it, still working, still shaping.""",
     'exits': {'s': 'kings_forge'},
     'mobs': [('forge_spirit', 1)], 'objs': [('grey_anvil', 1)]},
]
ZONE['mobs'] += [
    {'id': 'frost_giant', 'aliases': 'giant frost grey', 'short': 'a grey frost giant', 'role': 'elite', 'level': 79,
     'long': 'A grey frost giant rises from the rocks, lightning crackling in its beard.', 'flags': 'f', 'align': -800, 'attack': 'crush',
     'desc': 'A giant of the peaks, taken by the grey.'},
    {'id': 'sky_priest', 'aliases': 'priest sky grey', 'short': 'the fallen sky-priest', 'role': 'elite', 'level': 79,
     'long': 'The fallen sky-priest turns from the split altar, eyes white with lightning.', 'flags': 'bfl', 'align': -900,
     'desc': 'The last dwarf priest of the old sky. He prays to the West now, and the West answers with lightning.',
     'carry': [('sky_amulet', 70)]},
    {'id': 'chasm_horror', 'aliases': 'horror chasm', 'short': 'the chasm horror', 'role': 'champion', 'level': 80,
     'long': 'Something enormous and pale rises from the heap of bodies.', 'flags': 'bfl', 'align': -1000, 'attack': 'bite',
     'desc': 'It has eaten everything that fell for a thousand years, and grown very large.'},
    {'id': 'fire_elemental', 'aliases': 'elemental fire', 'short': 'a fire elemental', 'role': 'elite', 'level': 79,
     'long': 'A shape of living fire rises from the molten river.', 'flags': 'f', 'align': -500, 'attack': 'blast',
     'desc': 'The mountain\'s fire, given a shape.'},
    {'id': 'armoury_warden', 'aliases': 'warden armoury dwarf', 'short': 'the armoury warden', 'role': 'elite', 'level': 80,
     'long': 'The grey dwarf armoury warden hefts a shield as tall as he is.', 'flags': 'bfl', 'align': -900,
     'desc': 'A grey dwarf veteran set to guard the arms of the legions.',
     'equip': [('grey_shield', 'shield', 60)]},
    {'id': 'crystal_golem', 'aliases': 'golem crystal', 'short': 'a crystal golem', 'role': 'elite', 'level': 79,
     'long': 'A dwarf-shaped figure of grey crystal cracks free of the wall and lurches toward you.', 'flags': 'f', 'align': -800, 'attack': 'crush',
     'desc': 'A dwarf grown over by the crystal, and moving still.',
     'carry': [('living_crystal', 25)]},
    {'id': 'mountain_heart', 'aliases': 'heart mountain spirit', 'short': 'the Heart of the Mountain', 'role': 'champion', 'level': 80,
     'long': 'The Heart of the Mountain pulses, and the whole cavern shudders toward you.', 'flags': 'bfl', 'align': -500, 'attack': 'crush',
     'desc': 'The spirit of the peaks, which the dwarves loved, poisoned by the grey and maddened by it. Killing it would be a mercy.',
     'carry': [('heartstone_ring', 100)]},
    {'id': 'slave_driver', 'aliases': 'driver slave', 'short': 'a slave driver', 'role': 'elite', 'level': 78,
     'long': 'A grey dwarf slave driver cracks his whip and comes at you.', 'flags': 'bf', 'align': -1000,
     'desc': 'A cruel grey dwarf who works slaves until they hollow.',
     'equip': [('slaver_whip', 'wield', 50)]},
    {'id': 'chained_slave', 'aliases': 'slave chained', 'short': 'a chained slave', 'role': 'harmless', 'level': 70,
     'long': 'A chained slave stares at you through the bars, too tired to hope.', 'flags': 'b', 'align': 300,
     'desc': 'A man from the east, taken in a raid. He has forgotten his name.'},
    {'id': 'ore_hauler', 'aliases': 'hauler ore hollowed', 'short': 'a hollowed ore hauler', 'role': 'standard', 'level': 77,
     'long': 'A hollowed hauler leaves its cart and turns toward you.', 'flags': 'f', 'align': -700, 'attack': 'punch',
     'desc': 'A slave worked hollow, pushing ore for ever.'},
    {'id': 'forge_spirit', 'aliases': 'spirit forge', 'short': 'the spirit of the forge', 'role': 'champion', 'level': 80,
     'long': 'The spirit of the forge turns from the anvil, a hammer of fire in its hand.', 'flags': 'bfl', 'align': -800, 'attack': 'pound',
     'desc': 'The fire that beat the first grey iron, still beating it.'},
]
ZONE['objs'] += [
    {'id': 'sky_amulet', 'kind': 'worn', 'slot': 'neck', 'level': 80, 'aliases': 'amulet sky storm',
     'short': 'an amulet of the old sky', 'long': 'An amulet that crackles with lightning lies here.', 'affects': [('wis', 2), ('save_spell', -3)]},
    {'id': 'grey_shield', 'kind': 'armor', 'slot': 'shield', 'level': 80, 'aliases': 'shield grey iron tower',
     'short': 'a grey iron tower shield', 'long': 'A tall shield of grey iron lies here.', 'affects': [('hit', 30)]},
    {'id': 'living_crystal', 'kind': 'worn', 'slot': 'hold', 'level': 79, 'aliases': 'crystal living grey',
     'short': 'a shard of living crystal', 'long': 'A shard of grey crystal lies here, slowly growing.', 'affects': [('mana', 40)]},
    {'id': 'heartstone_ring', 'kind': 'worn', 'slot': 'finger', 'level': 81, 'aliases': 'ring heartstone',
     'short': 'a ring of heartstone', 'long': 'A warm stone ring lies here, faintly beating.', 'affects': [('str', 2), ('hit', 25)]},
    {'id': 'slaver_whip', 'kind': 'weapon', 'level': 78, 'attack': 'whip', 'aliases': 'whip slaver',
     'short': "a slaver's whip", 'long': "A long slaver's whip lies here.", 'affects': [('hitroll', 2)]},
    {'id': 'grey_anvil', 'kind': 'other', 'level': 1, 'fixed': True, 'weight': 5000, 'aliases': 'anvil grey black great',
     'short': 'the anvil of grey iron', 'long': 'A vast anvil of black stone stands here, ringing faintly.',
     'extras': {'anvil': 'The first grey iron was beaten on this anvil, and Nu\'Groth\'s voice was hammered into it. If you put your ear to the stone, you can hear it still.'}},
]
