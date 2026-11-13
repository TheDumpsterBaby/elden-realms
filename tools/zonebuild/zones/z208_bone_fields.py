"""W9 The Bone Fields -- the Blight, levels 70-75.

Graves without end, rolling over grey hills to every horizon: the dead of every
war the West has ever fought. Here the darkness raises its armies. A bone mill
grinds the unusable dead into the obelisks; legions muster in silent ranks; and
in the necropolis at the centre, the Gravelord commands it all.
"""

ZONE = {
    'num': 208, 'name': 'The Bone Fields', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'grave_road', 'name': 'The Road of Open Graves', 'sector': 'hills',
         'desc': """The road from Vel\'Morrow runs west between graves, rows upon rows of them on
         both sides, every one dug open from beneath.  Their headstones lean like bad
         teeth.  The names on them are in a hundred languages, from a hundred
         kingdoms the West has swallowed.""",
         'exits': {'e': {'to': '@20718', 'back_desc': 'West of the city, the road runs on between endless open graves.'}, 'w': 'grave_sea'},
         'mobs': [('bone_soldier', 2)]},
        {'id': 'grave_sea', 'name': 'The Sea of Graves', 'sector': 'hills',
         'desc': """Graves cover the grey hills from horizon to horizon like the waves of a frozen
         sea.  Here and there a skeletal hand reaches from the earth, or a skull turns
         to follow you.  Wind moans over the stones.  You could walk for days and
         never see the end of them.""",
         'exits': {'w': 'muster_field', 'n': 'mausoleum_row', 's': 'bone_mill'},
         'mobs': [('bone_soldier', 2), ('grave_crawler', 1)]},
        {'id': 'mausoleum_row', 'name': 'The Row of Mausoleums', 'sector': 'hills',
         'desc': """A row of great stone tombs for the kings and generals of fallen realms, each
         one carved with its owner\'s deeds.  The doors have been broken outward.
         Their occupants have been raised to lead the West\'s legions, and they took
         their grave goods with them.""",
         'exits': {'n': 'kings_tomb', 'w': 'charnel_house'},
         'mobs': [('dread_knight', 2)]},
        {'id': 'kings_tomb', 'name': 'The Tomb of a Forgotten King', 'sector': 'inside', 'flags': 'ad',
         'desc': """The largest mausoleum, its walls painted with a kingdom that no one remembers:
         blue rivers, white cities, a king with a sun on his shield.  The king himself
         sits on his sarcophagus, risen and armoured, waiting for the Gravelord\'s
         command to ride east.""",
         'mobs': [('risen_king', 1)]},
        {'id': 'charnel_house', 'name': 'The Charnel House', 'sector': 'inside', 'flags': 'd',
         'desc': """A long stone hall where bodies are sorted.  Grey servants strip the dead on
         long tables: the good bones to the legions, the broken ones to the mill, the
         flesh to the hounds.  The work never stops.  The piles never shrink.""",
         'mobs': [('charnel_servant', 3), ('bone_hound', 1)]},
        {'id': 'bone_mill', 'name': 'The Bone Mill', 'sector': 'inside', 'flags': 'd',
         'desc': """A great mill turned by hollowed slaves walking a wheel, its stones grinding
         bones to grey powder.  The powder is packed into moulds and fired into the
         blocks that build the obelisks of the army road.  The noise is a constant
         grinding crunch.""",
         'exits': {'s': 'bone_pits'},
         'mobs': [('mill_overseer', 1), ('hollowed_slave', 2)]},
        {'id': 'bone_pits', 'name': 'The Bone Pits', 'sector': 'field',
         'desc': """Pits as wide as lakes are filled with bones awaiting the mill.  They shift and
         slide and settle, and in places they have begun to assemble themselves,
         skull to spine to rib, into things that were never alive in any shape.""",
         'mobs': [('bone_horror', 2)]},
        {'id': 'muster_field', 'name': 'The Muster Field', 'sector': 'field',
         'desc': """A vast flat field where the risen legions stand in ranks, rank after rank of
         skeletons in rusting armour, utterly still, waiting.  There are tens of
         thousands of them.  When the order comes, they will march east, and nothing
         the living have can stop them.""",
         'exits': {'w': 'necropolis_gate', 's': 'titan_hollow'},
         'mobs': [('bone_soldier', 3), ('bone_captain', 1)]},
        {'id': 'titan_hollow', 'name': 'The Titan\'s Hollow', 'sector': 'hills',
         'desc': """A great hollow between hills where the bones of giants have been assembled into
         a titan taller than a tower, still being built.  Grey servants climb over it on
         ladders, binding bones with wire and black rope.  Its skull, a giant\'s skull
         as big as a house, turns toward you.""",
         'mobs': [('grave_titan', 1), ('charnel_servant', 1)]},
        {'id': 'necropolis_gate', 'name': 'The Gate of the Necropolis', 'sector': 'city',
         'desc': """At the heart of the Bone Fields stands a city built entirely of bone: walls of
         femurs, towers of skulls, gates of ribcages.  Grey fire burns in every empty
         eye socket.  Two dread knights on skeletal horses guard the gate.""",
         'exits': {'w': 'bone_street',
                   'n': {'to': 'west_hills', 'desc': 'A path skirts the bone walls and climbs toward the broken mountains.'}},
         'mobs': [('dread_knight', 2)]},
        {'id': 'bone_street', 'name': 'The Street of Skulls', 'sector': 'city',
         'desc': """A street paved with skulls, set close like cobbles, every one grinning up at
         you.  The buildings on either side are built of long bones, roofed with
         shoulder blades.  Bone-weavers sit in the doorways, working bones into new
         shapes with their hands.""",
         'exits': {'w': 'bone_temple', 'n': 'weaver_hall'},
         'mobs': [('bone_weaver', 2)]},
        {'id': 'weaver_hall', 'name': 'The Hall of Weavers', 'sector': 'inside', 'flags': 'd',
         'desc': """A great hall where the bone-weavers practice their art, making servants, beasts
         and engines from the dead.  Works hang half finished from the rafters.  At the
         centre, the Matron of the Weavers is shaping something huge out of the bones of
         a dragon.""",
         'mobs': [('weaver_matron', 1), ('bone_weaver', 1)]},
        {'id': 'bone_temple', 'name': 'The Temple of Bones', 'sector': 'inside', 'flags': 'd',
         'desc': """A temple whose pillars are spines and whose dome is a single colossal skull.
         Rows of skeletal priests kneel before an altar on which a grey flame burns.
         A stair behind the altar descends into the catacombs beneath the city.""",
         'exits': {'d': 'catacombs', 'w': 'sanctum_door'},
         'mobs': [('bone_priest', 2)]},
        {'id': 'catacombs', 'name': 'The Deep Catacombs', 'sector': 'inside', 'flags': 'ad',
         'desc': """Tunnels lined with bones run beneath the necropolis in every direction, deeper
         than anyone has mapped.  The dead here are the oldest, from before the first
         kingdoms of men.  They are restless, and they whisper in languages that died
         with them.""",
         'mobs': [('ancient_dead', 3)]},
        {'id': 'sanctum_door', 'name': 'Before the Sanctum', 'sector': 'inside', 'flags': 'd',
         'desc': """A door of fused black bone, carved with the face of the Gravelord, bars the
         way to his sanctum.  Before it stand his honour guard, the risen champions of
         a dozen fallen realms, each in the armour they died in.""",
         'exits': {'w': {'to': 'sanctum', 'door': 'door bone', 'state': 'closed', 'desc': 'A door of black bone carved with a skull-faced king.'}},
         'mobs': [('grave_champion', 2)]},
        {'id': 'sanctum', 'name': 'The Gravelord\'s Sanctum', 'sector': 'inside', 'flags': 'd',
         'desc': """A round chamber at the heart of the necropolis, its walls lined with the crowns
         of every king the West has buried.  In its centre, on a throne of skulls, sits
         the Gravelord, who raises the West\'s armies from the dead.  He was the first
         mortal to bow to Nu\'Groth, and he has been dead for longer than Midgaard has
         stood.""",
         'mobs': [('gravelord', 1)]},
        {'id': 'west_hills', 'name': 'The Western Barrow-Lands', 'sector': 'hills',
         'desc': """Beyond the necropolis the graves thin out at last, and the land rises toward a
         wall of broken mountains, their peaks split and jagged against the dark sky.
         A path climbs toward a great gate cut into the rock, and from it comes the
         distant ring of hammers.""",
         'mobs': [('bone_soldier', 1)]},
    ],
    'mobs': [
        {'id': 'bone_soldier', 'aliases': 'soldier bone skeleton', 'short': 'a bone soldier', 'role': 'standard', 'level': 72,
         'long': 'A skeleton in rusting armour raises its sword in silence.', 'flags': 'f', 'align': -1000,
         'desc': 'One of tens of thousands, from a kingdom no one remembers.',
         'equip': [('ancient_sword', 'wield', 60), ('ancient_shield', 'shield', 25)]},
        {'id': 'grave_crawler', 'aliases': 'crawler grave', 'short': 'a grave crawler', 'role': 'standard', 'level': 71,
         'long': 'A legless corpse drags itself out of a grave on its hands.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Not every corpse rises whole. These come anyway.'},
        {'id': 'dread_knight', 'aliases': 'knight dread', 'short': 'a dread knight', 'role': 'elite', 'level': 74,
         'long': 'A dread knight on a skeletal horse lowers a black lance.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'A great knight of some fallen realm, risen to command the West\'s cavalry.',
         'equip': [('dread_lance', 'wield', 80), ('dread_plate', 'body', 20)]},
        {'id': 'risen_king', 'aliases': 'king risen forgotten', 'short': 'a forgotten king', 'role': 'champion', 'level': 75,
         'long': 'A risen king with a sun on his shield rises from his sarcophagus.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'He ruled a kingdom of white cities and blue rivers that the West swallowed a thousand years ago. Now he waits to lead his people east, against people like him.',
         'equip': [('sun_shield', 'shield', 100), ('ancient_sword', 'wield', 100)]},
        {'id': 'charnel_servant', 'aliases': 'servant charnel', 'short': 'a charnel servant', 'role': 'standard', 'level': 71,
         'long': 'A grey servant strips a body on a stone table.', 'flags': 'f', 'align': -900,
         'desc': 'Hollowed, patient, tireless. It sorts the dead, and you are not yet dead.',
         'equip': [('flaying_knife', 'wield', 70)]},
        {'id': 'bone_hound', 'aliases': 'hound bone', 'short': 'a bone hound', 'role': 'elite', 'level': 73,
         'long': 'A hound of fused bones gnaws on scraps beneath the tables.', 'flags': 'f', 'align': -900, 'attack': 'bite',
         'desc': 'Built from the bones of a dozen wolves.'},
        {'id': 'mill_overseer', 'aliases': 'overseer mill', 'short': 'the mill overseer', 'role': 'elite', 'level': 74,
         'long': 'A tall grey figure drives the slaves at the mill wheel.', 'flags': 'bf', 'align': -1000,
         'desc': 'It has ground ten thousand dead to powder.',
         'equip': [('grey_whip', 'wield', 100)]},
        {'id': 'hollowed_slave', 'aliases': 'slave hollowed', 'short': 'a hollowed slave', 'role': 'standard', 'level': 70,
         'long': 'A hollowed slave walks the mill wheel, empty-eyed.', 'flags': 'f', 'align': -600,
         'desc': 'It will walk until it falls, and then it will be ground too.'},
        {'id': 'bone_horror', 'aliases': 'horror bone', 'short': 'a bone horror', 'role': 'elite', 'level': 74,
         'long': 'A shape of mismatched bones assembles itself and lurches toward you.', 'flags': 'f', 'align': -1000, 'attack': 'crush',
         'desc': 'Too many limbs, too many skulls, no plan at all.'},
        {'id': 'bone_captain', 'aliases': 'captain bone', 'short': 'a bone captain', 'role': 'elite', 'level': 75,
         'long': 'A skeletal captain in a plumed helm surveys the ranks.', 'flags': 'f', 'align': -1000,
         'desc': 'It commands a thousand dead, and they move when it moves.',
         'equip': [('captain_glaive', 'wield', 100)]},
        {'id': 'grave_titan', 'aliases': 'titan grave', 'short': 'the grave titan', 'role': 'champion', 'level': 75,
         'long': 'A titan of giant bones, taller than a tower, turns its house-sized skull toward you.', 'flags': 'bfl', 'align': -1000, 'attack': 'crush',
         'desc': 'Built to break city walls. When it is finished, it will walk east.',
         'carry': [('titan_knuckle', 100)]},
        {'id': 'bone_weaver', 'aliases': 'weaver bone', 'short': 'a bone-weaver', 'role': 'elite', 'level': 73,
         'long': 'A bone-weaver shapes a bone in its long grey fingers.', 'flags': 'f', 'align': -1000,
         'desc': 'They can make anything from the dead. They would like to make something from you.',
         'equip': [('weaver_awl', 'wield', 100)]},
        {'id': 'weaver_matron', 'aliases': 'matron weaver', 'short': 'the Matron of the Weavers', 'role': 'champion', 'level': 75,
         'long': 'The Matron of the Weavers turns from a half-built dragon of bones.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'The greatest of the bone-weavers, who built the bone engines of the Field of Broken Banners and the titan in the hollow. The dragon is her masterpiece.',
         'carry': [('weaver_shroud', 100)]},
        {'id': 'bone_priest', 'aliases': 'priest bone', 'short': 'a skeletal priest', 'role': 'elite', 'level': 74,
         'long': 'A skeletal priest kneels before the grey flame, chanting.', 'flags': 'f', 'align': -1000,
         'desc': 'They pray to Nu\'Groth for more dead to raise.',
         'equip': [('bone_rod', 'wield', 100)]},
        {'id': 'ancient_dead', 'aliases': 'dead ancient', 'short': 'one of the ancient dead', 'role': 'standard', 'level': 73,
         'long': 'A brown, withered corpse older than any kingdom rises, whispering.', 'flags': 'f', 'align': -1000, 'attack': 'claw',
         'desc': 'Dead since before the first city was built. It has forgotten everything except hunger.'},
        {'id': 'grave_champion', 'aliases': 'champion grave', 'short': 'a grave champion', 'role': 'elite', 'level': 75,
         'long': 'A risen champion in ancient armour bars the sanctum door.', 'flags': 'f', 'align': -1000,
         'desc': 'The greatest warriors of a dozen fallen realms, chosen for the Gravelord\'s guard.',
         'equip': [('champion_greatsword', 'wield', 100)]},
        {'id': 'gravelord', 'aliases': 'gravelord lord grave', 'short': 'the Gravelord', 'role': 'boss', 'level': 75,
         'long': 'The Gravelord rises from his throne of skulls, and every bone in the necropolis turns toward him.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'The first mortal to kneel to Nu\'Groth, rewarded with an eternity as lord of its dead. He has raised every army that has ever marched east, and he is raising the one that will take Midgaard.',
         'equip': [('gravelord_scythe', 'wield', 100), ('crown_of_kings', 'head', 100)], 'carry': [('phylactery', 100)]},
    ],
    'objs': [
        {'id': 'ancient_sword', 'kind': 'weapon', 'level': 72, 'attack': 'slash', 'aliases': 'sword ancient',
         'short': 'an ancient sword', 'long': 'An ancient sword of strange design lies here.'},
        {'id': 'ancient_shield', 'kind': 'armor', 'slot': 'shield', 'level': 72, 'aliases': 'shield ancient',
         'short': 'an ancient round shield', 'long': 'An ancient round shield lies here.'},
        {'id': 'dread_lance', 'kind': 'weapon', 'level': 74, 'attack': 'pierce', 'aliases': 'lance dread black',
         'short': 'a black lance', 'long': 'A long black lance lies here.', 'affects': [('hitroll', 2)]},
        {'id': 'dread_plate', 'kind': 'armor', 'slot': 'body', 'level': 74, 'aliases': 'plate dread black',
         'short': 'black dread plate', 'long': 'A suit of black plate lies here.', 'affects': [('hit', 30)]},
        {'id': 'sun_shield', 'kind': 'armor', 'slot': 'shield', 'level': 75, 'aliases': 'shield sun',
         'short': 'a shield bearing a faded sun', 'long': 'A shield bearing a faded golden sun lies here.', 'affects': [('save_spell', -3), ('hit', 30)]},
        {'id': 'flaying_knife', 'kind': 'weapon', 'level': 71, 'attack': 'slash', 'aliases': 'knife flaying',
         'short': 'a flaying knife', 'long': 'A curved flaying knife lies here.'},
        {'id': 'grey_whip', 'kind': 'weapon', 'level': 74, 'attack': 'whip', 'aliases': 'whip grey',
         'short': 'a whip of grey hide', 'long': 'A whip of grey hide lies coiled here.'},
        {'id': 'captain_glaive', 'kind': 'weapon', 'level': 75, 'attack': 'slash', 'aliases': 'glaive captain', 'two_handed': True,
         'short': 'a bone captain\'s glaive', 'long': 'A long glaive with a bone haft lies here.', 'affects': [('damroll', 3)]},
        {'id': 'titan_knuckle', 'kind': 'worn', 'slot': 'hold', 'level': 75, 'aliases': 'knuckle titan bone',
         'short': 'a giant\'s knucklebone', 'long': 'A knucklebone as big as a fist lies here.', 'affects': [('str', 3), ('hit', 40)]},
        {'id': 'weaver_awl', 'kind': 'weapon', 'level': 73, 'attack': 'pierce', 'aliases': 'awl weaver',
         'short': 'a bone-weaver\'s awl', 'long': 'A long bone awl lies here.'},
        {'id': 'weaver_shroud', 'kind': 'armor', 'slot': 'about', 'level': 76, 'aliases': 'shroud weaver',
         'short': 'the Matron\'s shroud', 'long': 'A grey shroud sewn with tiny bones lies here.', 'affects': [('int', 2), ('mana', 60), ('save_spell', -3)]},
        {'id': 'bone_rod', 'kind': 'weapon', 'level': 74, 'attack': 'bludgeon', 'aliases': 'rod bone',
         'short': 'a rod of fused bone', 'long': 'A rod of fused bone lies here.', 'affects': [('mana', 30)]},
        {'id': 'champion_greatsword', 'kind': 'weapon', 'level': 75, 'attack': 'slash', 'aliases': 'greatsword champion', 'two_handed': True,
         'short': 'a champion\'s greatsword', 'long': 'A huge ancient greatsword lies here.', 'affects': [('hitroll', 2), ('damroll', 3)]},
        {'id': 'gravelord_scythe', 'kind': 'weapon', 'level': 77, 'attack': 'slash', 'aliases': 'scythe gravelord', 'two_handed': True,
         'short': 'the Gravelord\'s scythe', 'long': 'A scythe whose blade is black glass and whose haft is a spine lies here.',
         'affects': [('hitroll', 5), ('damroll', 5)]},
        {'id': 'crown_of_kings', 'kind': 'armor', 'slot': 'head', 'level': 77, 'aliases': 'crown kings',
         'short': 'the crown of dead kings', 'long': 'A crown made from the fused crowns of many kings lies here.',
         'affects': [('hit', 60), ('wis', 2), ('save_spell', -4)]},
        {'id': 'phylactery', 'kind': 'treasure', 'level': 75, 'aliases': 'phylactery jar', 'short': 'the Gravelord\'s phylactery',
         'long': 'A small black jar, cold as the grave, lies here.', 'weight': 1, 'cost': 5000,
         'extras': {'phylactery jar': 'The Gravelord\'s death is kept here. While it exists, he will rise again. Something to take to Midgaard\'s priests.'}},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
ZONE['rooms'] += [
    {'id': 'ossuary_cliffs', 'name': 'The Ossuary Cliffs', 'sector': 'hills',
     'desc': """South of the bone pits the land drops away in white cliffs made entirely of
     packed bone, ground fine and set hard as chalk by centuries of rain.  The cliff face
     is riddled with holes, and great bald vultures sit in them, watching the mill.""",
     'exits': {'n': 'bone_pits', 'w': 'bone_caves'},
     'mobs': [('bone_vulture', 3)]},
    {'id': 'bone_caves', 'name': 'The Caves of Teeth', 'sector': 'inside', 'flags': 'a',
     'desc': """A cave cut into the bone cliffs, its walls studded with teeth, millions of them,
     pressed into the bone in spiralling patterns.  Someone is still adding to them: a
     thin grey figure crouches at the back of the cave with a sack, setting them one by
     one.""",
     'mobs': [('tooth_gatherer', 1)]},
    {'id': 'giant_graves', 'name': 'The Graves of Giants', 'sector': 'hills',
     'desc': """Beyond the titan's hollow lie the graves of the giants who fought for the east in
     the first war, each mound a hundred paces long.  The mounds have split open.  Rib
     cages like the frames of ships stand out of the earth, and some of them are
     breathing.""",
     'exits': {'n': 'titan_hollow'},
     'mobs': [('grave_giant', 2)]},
    {'id': 'deep_catacombs', 'name': 'The Deep Catacombs', 'sector': 'inside', 'flags': 'a',
     'desc': """The catacombs go down and down beneath the temple, older with every level, until
     the niches hold bones too large or too strange to have been men.  Ghasts squat in
     the niches, gnawing, and the stench of them is a physical thing.""",
     'exits': {'s': 'catacombs', 'n': 'forgotten_kings'},
     'mobs': [('catacomb_ghast', 2)]},
    {'id': 'forgotten_kings', 'name': 'The Hall of Forgotten Kings', 'sector': 'inside',
     'desc': """A long hall of thrones, each with a crowned skeleton seated on it, kings of
     kingdoms nobody remembers, all of them taken by the West in ages past.  At the end
     of the hall the oldest king rises from his throne, and his crown is the only thing
     about him that is not dust.""",
     'mobs': [('forgotten_king', 1)]},
    {'id': 'skull_tower', 'name': 'The Tower of Skulls', 'sector': 'inside',
     'desc': """A tower built of skulls mortared with grave-dirt stands on the western hills,
     every skull facing east.  Inside, a stair of thighbones spirals up past niches where
     skeletal sentinels stand guard.""",
     'exits': {'s': 'west_hills', 'u': 'skull_tower_top'},
     'mobs': [('skull_sentinel', 2)]},
    {'id': 'skull_tower_top', 'name': 'Atop the Tower of Skulls', 'sector': 'inside',
     'desc': """The top of the tower is a ring of skulls open to the sky.  From here the necromancer
     who raises the bone armies looks east over the fields, counting her soldiers.  There
     are a very great many of them.""",
     'mobs': [('bone_necromancer', 1)]},
    {'id': 'tomb_treasury', 'name': 'The Tomb Treasury', 'sector': 'inside',
     'desc': """Behind the risen king's tomb lies the treasure he was buried with: gold, jewels,
     the arms of his bodyguard.  He has no use for it now, but the thing that guards it
     does not know that.""",
     'exits': {'s': 'kings_tomb'},
     'mobs': [('tomb_guardian', 1)], 'objs': [('burial_gold', 1)]},
    {'id': 'silk_loft', 'name': 'The Bone-Silk Loft', 'sector': 'inside',
     'desc': """Above the weavers' hall, a loft hung with sheets of white silk spun from ground
     bone.  Spiders the size of dogs work the silk, and things wrapped in it hang from the
     rafters, some of them still moving.""",
     'exits': {'s': 'weaver_hall'},
     'mobs': [('bone_spider', 3)]},
]
ZONE['mobs'] += [
    {'id': 'bone_vulture', 'aliases': 'vulture bone bald', 'short': 'a bone vulture', 'role': 'standard', 'level': 72,
     'long': 'A bald vulture as big as a man drops from the cliff, wings spread.', 'flags': 'f', 'align': -500, 'attack': 'pierce',
     'desc': 'It has eaten nothing but the dead for a hundred years, and it is tired of waiting for you to die.'},
    {'id': 'tooth_gatherer', 'aliases': 'gatherer tooth', 'short': 'the tooth-gatherer', 'role': 'elite', 'level': 73,
     'long': 'The tooth-gatherer looks up from its work, its own mouth empty and grinning.', 'flags': 'bfl', 'align': -900,
     'desc': 'It collects the teeth of the dead and sets them in the walls. It would like yours.',
     'carry': [('tooth_necklace', 30)]},
    {'id': 'grave_giant', 'aliases': 'giant grave', 'short': 'a grave giant', 'role': 'elite', 'level': 74,
     'long': 'A giant skeleton heaves itself up out of its burst mound.', 'flags': 'f', 'align': -900, 'attack': 'crush',
     'desc': 'A giant who died for the east, now marching for the West.'},
    {'id': 'catacomb_ghast', 'aliases': 'ghast catacomb', 'short': 'a catacomb ghast', 'role': 'elite', 'level': 74,
     'long': 'A ghast drops out of a niche, jaws wide, reeking.', 'flags': 'f', 'align': -1000, 'attack': 'claw',
     'desc': 'A grey, long-limbed eater of the dead, and of the living when it can get them.'},
    {'id': 'forgotten_king', 'aliases': 'king forgotten oldest', 'short': 'the Forgotten King', 'role': 'champion', 'level': 75,
     'long': 'The Forgotten King rises from his throne, dust pouring from his robes.', 'flags': 'bfl', 'align': -1000,
     'desc': 'The first king the West ever took. Nobody remembers his name, not even him.',
     'carry': [('forgotten_crown', 100)]},
    {'id': 'skull_sentinel', 'aliases': 'sentinel skull skeleton', 'short': 'a skull sentinel', 'role': 'elite', 'level': 74,
     'long': 'A skeletal sentinel steps out of its niche, spear levelled.', 'flags': 'bf', 'align': -900, 'attack': 'pierce',
     'desc': 'A soldier of bone, set to guard the tower for ever.'},
    {'id': 'bone_necromancer', 'aliases': 'necromancer bone', 'short': 'the bone necromancer', 'role': 'champion', 'level': 75,
     'long': 'The bone necromancer turns from the parapet, her face a skull with living eyes.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
     'desc': 'The Gravelord\'s general, who raises the bone armies and sends them east. She was a priestess of Midgaard once.',
     'carry': [('necro_staff', 100)]},
    {'id': 'tomb_guardian', 'aliases': 'guardian tomb', 'short': 'the tomb guardian', 'role': 'elite', 'level': 75,
     'long': 'A tall armoured skeleton bars the way to the treasure.', 'flags': 'bf', 'align': -900,
     'desc': 'The risen king\'s bodyguard, buried alive with him so that he would guard the treasure for ever. He has.'},
    {'id': 'bone_spider', 'aliases': 'spider bone silk', 'short': 'a bone-silk spider', 'role': 'standard', 'level': 73,
     'long': 'A white spider the size of a dog drops on a thread of bone-silk.', 'flags': 'f', 'align': -700, 'attack': 'bite',
     'desc': 'It spins silk from ground bone, and wraps the living in it.',
     'carry': [('bone_silk_cloak', 15)]},
]
ZONE['objs'] += [
    {'id': 'tooth_necklace', 'kind': 'worn', 'slot': 'neck', 'level': 73, 'aliases': 'necklace teeth tooth',
     'short': 'a necklace of teeth', 'long': 'A necklace of human teeth lies here.', 'affects': [('damroll', 2)]},
    {'id': 'forgotten_crown', 'kind': 'armor', 'slot': 'head', 'level': 76, 'aliases': 'crown forgotten',
     'short': 'the crown of the Forgotten King', 'long': 'An ancient crown of dark gold lies here.', 'affects': [('hitroll', 3), ('hit', 30)]},
    {'id': 'necro_staff', 'kind': 'weapon', 'level': 76, 'attack': 'bludgeon', 'two_handed': True, 'aliases': 'staff bone necromancer',
     'short': "a necromancer's bone staff", 'long': 'A staff of fused bone lies here.', 'affects': [('mana', 50), ('int', 2)]},
    {'id': 'burial_gold', 'kind': 'treasure', 'level': 70, 'aliases': 'gold burial hoard',
     'short': 'a hoard of burial gold', 'long': 'A heap of ancient burial gold lies here.', 'cost': 5000},
    {'id': 'bone_silk_cloak', 'kind': 'armor', 'slot': 'about', 'level': 74, 'aliases': 'cloak bone silk',
     'short': 'a cloak of bone-silk', 'long': 'A white cloak of bone-silk lies here.', 'affects': [('dex', 1), ('hit', 20)]},
]
