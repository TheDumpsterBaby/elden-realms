"""The Hospice of the Last Rites -- support ring, levels 10-18.

The Temple's house of healing for the wounded from the wall, and below it the
catacombs where Midgaard's dead are laid. Since the greyblight came, the dead
do not always stay down. Joins the Temple altar (west) to the Refugee Camps
(south).
"""

ZONE = {
    'num': 63, 'name': 'The Hospice of the Last Rites', 'builders': 'Claude', 'lifespan': 15,
    'rooms': [
        {'id': 'passage', 'name': 'The Passage to the Hospice', 'sector': 'inside', 'flags': 'cde',
         'desc': """A vaulted stone passage leads east from the Temple altar, its walls carved
         with the names of healers who died tending the wounded.  The air smells of
         lye and incense.  Through the far arch you can hear coughing, prayers and,
         now and then, a scream.""",
         'exits': {'w': {'to': '@3054', 'back_desc': 'An arched passage leads east to the Hospice of the Last Rites.'},
                   'e': 'cloister_w'},
         'extras': {'names walls carved': 'Hundreds of names, each followed by a date. The dates grow closer together toward the end of the passage.'}},
        {'id': 'cloister_w', 'name': 'The West Cloister', 'sector': 'inside', 'flags': 'c',
         'desc': """A covered walk runs around a small garden of medicinal herbs, gone to seed
         for lack of hands to tend it.  Wounded men sit along the walls in the weak
         sun, wrapped in blankets.  Sisters in white move among them with bowls of
         broth and clean bandages.""",
         'exits': {'e': 'garth', 'n': 'chapel', 's': 'infirmary'},
         'mobs': [('wounded_soldier', 2), ('nursing_sister', 1)]},
        {'id': 'garth', 'name': 'The Herb Garden', 'sector': 'field', 'flags': 'c',
         'desc': """Beds of herbs fill the cloister garth, bordered by low box hedges: feverfew,
         comfrey, poppy, and rows of plants you do not recognise.  A stone basin of
         clear water stands in the middle, the only clean water you have seen
         outside the Temple.""",
         'exits': {'e': 'cloister_e'},
         'objs': [('holy_basin', 1)],
         'mobs': [('herb_sister', 1)]},
        {'id': 'cloister_e', 'name': 'The East Cloister', 'sector': 'inside', 'flags': 'c',
         'desc': """The eastern walk of the cloister looks onto the infirmary windows and the
         bell tower.  A door leads to the apothecary, and a broad stair descends to
         the mortuary, where the stretcher-bearers bring those who could not be
         saved.""",
         'exits': {'n': 'bell_tower', 'e': 'apothecary', 'd': 'mortuary', 's': 'gate'},
         'mobs': [('orderly', 1)]},
        {'id': 'gate', 'name': 'The Hospice Gate', 'sector': 'inside', 'flags': 'c',
         'desc': """The hospice's southern gate stands open at the top of the hill.  Below, the
         Refugee Camps spread out in a grey haze of smoke.  Stretcher-bearers come
         and go without rest, and a sister at the gate decides who is carried in and
         who is turned away.""",
         'exits': {'s': {'to': '@6103', 'back_desc': 'Up the slope stands the gate of the Hospice of the Last Rites.'}},
         'mobs': [('gate_sister', 1)]},
        {'id': 'chapel', 'name': 'The Chapel of the Last Rites', 'sector': 'inside', 'flags': 'cde',
         'desc': """A plain chapel lit by banks of candles.  Bodies lie on biers before the
         altar, wrapped in white, waiting for the rites to be spoken over them so
         that they will rest.  A priest moves from bier to bier, his voice hoarse,
         his hands never still.""",
         'mobs': [('rite_priest', 1)]},
        {'id': 'infirmary', 'name': 'The Long Infirmary', 'sector': 'inside', 'flags': 'c',
         'desc': """A long hall lined with beds, every one of them full.  Men missing limbs,
         men with wounds that will not close, men who stare at the ceiling and
         whisper about the West.  The smell of blood and vinegar is overpowering.
         A door at the end leads to the surgery.""",
         'exits': {'e': 'surgery'},
         'mobs': [('wounded_soldier', 3), ('nursing_sister', 2)]},
        {'id': 'surgery', 'name': 'The Surgery', 'sector': 'inside', 'flags': 'c',
         'desc': """A stone table stained dark, a tray of saws and knives, a bucket you do not
         look into.  The physician's leather apron hangs on a peg beside a list of
         names: those who must lose a limb tomorrow.  The list is long, and the
         physician has not slept.""",
         'exits': {'e': 'study'},
         'mobs': [('physician', 1)]},
        {'id': 'study', 'name': "The Physician's Study", 'sector': 'inside', 'flags': 'c',
         'desc': """Books on anatomy and herb lore crowd the shelves, and the desk is buried in
         notes.  A jar on the desk holds a sample of grey, soft grain beside a
         sketch of a blotched human arm.  Across the top of the notes is written,
         and underlined three times: IT IS NOT A DISEASE.""",
         'extras': {'notes jar grain sketch': 'The greyblight spreads from the grain to the flesh. It does not kill; it replaces. The victim is not dead when they rise. They are listening. To what?'}},
        {'id': 'bell_tower', 'name': 'The Foot of the Bell Tower', 'sector': 'inside', 'flags': 'c',
         'desc': """A narrow tower rises into darkness, its walls slick with damp.  A bell rope
         hangs down the centre.  The hospice bell is rung once for every death, and
         the rope is frayed nearly through.""",
         'exits': {'u': 'belfry'},
         'mobs': [('bell_ringer', 1)]},
        {'id': 'belfry', 'name': 'The Belfry', 'sector': 'inside',
         'desc': """A great bronze bell hangs among pigeon-fouled beams.  Through the louvres
         you can see the fort, the camps and the fields, and far to the west, the
         stain on the horizon.  Up here the bell hums faintly by itself, as if
         something far away were striking it.""",
         'mobs': [('belfry_bat', 3)]},
        {'id': 'apothecary', 'name': 'The Apothecary', 'sector': 'inside', 'flags': 'c',
         'desc': """Shelves of jars and bottles climb the walls, most of them empty.  Bundles of
         herbs hang drying from the beams.  The apothecary works at a bench with a
         mortar and pestle, grinding poppy for men who will die whether she grinds
         it or not.""",
         'mobs': [('apothecary', 1)]},
        {'id': 'mortuary', 'name': 'The Mortuary', 'sector': 'inside', 'flags': 'd',
         'desc': """A cold, low vault where the dead are washed and wrapped.  Stone slabs hold
         shrouded bodies, and more lie on the floor between them.  Some of the
         shrouds have grey stains spreading through the linen.  A heavy door in the
         east wall is chained and padlocked.""",
         'exits': {'e': {'to': 'crypt_stair', 'door': 'door chained', 'key': 'crypt_key', 'state': 'locked',
                         'desc': 'A heavy door, chained and padlocked. Scratches cover the inside of it.'},
                   'n': 'sexton_room'},
         'mobs': [('mortuary_sister', 1), ('shrouded_dead', 2)]},
        {'id': 'sexton_room', 'name': "The Sexton's Room", 'sector': 'inside', 'flags': 'd',
         'desc': """A cramped room beside the mortuary where the sexton lives and keeps the
         keys to the catacombs.  A cot, a bottle, a lantern, and a heavy iron ring
         of keys on a nail.  The sexton has started drinking before noon, and he
         keeps a mattock within reach of his cot.""",
         'mobs': [('sexton', 1)]},
        {'id': 'crypt_stair', 'name': 'The Catacomb Stair', 'sector': 'inside', 'flags': 'ad',
         'desc': """Worn steps spiral down into the earth beneath the hospice.  The walls are
         lined with niches, each holding a skull.  The air grows colder with every
         step, and from below comes a sound like many people breathing in their
         sleep.""",
         'exits': {'d': 'catacomb_hall'}},
        {'id': 'catacomb_hall', 'name': 'The Hall of Niches', 'sector': 'inside', 'flags': 'ad',
         'desc': """A long gallery cut from the rock, its walls lined floor to ceiling with burial
         niches.  Many niches are empty.  Their occupants have climbed out and lie
         on the floor, or stand facing the western wall, swaying.""",
         'exits': {'n': 'ossuary', 's': 'flooded', 'e': 'deep_catacomb'},
         'mobs': [('risen_dead', 3)]},
        {'id': 'ossuary', 'name': 'The Ossuary', 'sector': 'inside', 'flags': 'ad',
         'desc': """Bones are stacked in patterns along every wall: femurs in rows, skulls in
         arches, ribs in fans.  Generations of Midgaard's dead are arranged here.
         Tonight the bones are moving, clicking softly as they try to remember how
         they fit together.""",
         'mobs': [('bone_swarm', 2), ('ossuary_guardian', 1)]},
        {'id': 'flooded', 'name': 'The Flooded Catacomb', 'sector': 'swim', 'flags': 'ad',
         'desc': """Black water has seeped up through the floor and stands waist deep between
         the niches.  It is very cold.  Things float in it.  Every now and then the
         surface ripples outward from something moving beneath it.""",
         'mobs': [('drowned_dead', 2)]},
        {'id': 'deep_catacomb', 'name': 'The Deep Catacomb', 'sector': 'inside', 'flags': 'ad',
         'desc': """The oldest part of the catacombs, carved before Midgaard had walls.  The
         niches here hold abbots and abbesses of the hospice, laid out in their
         robes with their hands folded.  Many of the robes are empty.  A sealed
         door at the end has been broken open from the inside.""",
         'exits': {'e': 'abbess_tomb'},
         'mobs': [('risen_monk', 2)]},
        {'id': 'abbess_tomb', 'name': 'The Tomb of the Abbess', 'sector': 'inside', 'flags': 'ad',
         'desc': """A round vault with a marble sarcophagus at its centre, its lid cast aside and
         cracked in two.  The walls are scored with spirals scratched into the stone
         by fingernails.  The Abbess who founded the hospice rose first, and the
         others rose because she called them.""",
         'mobs': [('unquiet_abbess', 1)]},
    ],
    'mobs': [
        {'id': 'wounded_soldier', 'aliases': 'soldier wounded', 'short': 'a wounded soldier', 'role': 'harmless', 'level': 10,
         'long': 'A wounded soldier sits wrapped in a blanket, staring at nothing.', 'flags': 'b', 'align': 400, 'sex': 1,
         'desc': 'His bandages are clean, but the eyes above them have seen the West, and they have not come back from it.'},
        {'id': 'nursing_sister', 'aliases': 'sister nursing nurse', 'short': 'a nursing sister', 'role': 'harmless', 'level': 11,
         'long': 'A nursing sister in white changes a bandage with quick, sure hands.', 'flags': 'g', 'align': 900, 'sex': 2,
         'desc': 'Her white robe is spattered red to the elbows. She hums as she works so the men will not hear her crying.'},
        {'id': 'herb_sister', 'aliases': 'sister herb', 'short': 'the herb sister', 'role': 'harmless', 'level': 12,
         'long': 'An elderly sister kneels among the herb beds, weeding.', 'flags': 'b', 'align': 900, 'sex': 2,
         'desc': 'She has tended this garden for forty years. She talks to the plants and swears they listen.',
         'carry': [('comfrey_poultice', 100)]},
        {'id': 'orderly', 'aliases': 'orderly', 'short': 'an orderly', 'role': 'standard', 'level': 13,
         'long': 'An orderly carries a covered bucket toward the stairs.', 'flags': 'gm', 'align': 300, 'sex': 1,
         'desc': 'A big, slow, gentle man who does the work nobody else will do.'},
        {'id': 'gate_sister', 'aliases': 'sister gate', 'short': 'the gate sister', 'role': 'elite', 'level': 14,
         'long': 'A stern sister at the gate judges every stretcher with a glance.', 'flags': 'b', 'align': 700, 'sex': 2,
         'desc': 'She chooses who lives. There are not enough beds. She has made her peace with that, or tells herself she has.'},
        {'id': 'rite_priest', 'aliases': 'priest rite', 'short': 'the priest of the last rites', 'role': 'elite', 'level': 16,
         'long': 'A hoarse priest speaks the last rites over a shrouded body.', 'flags': 'b', 'align': 1000, 'sex': 1,
         'desc': 'If the rites are not spoken, the dead do not rest. Since the greyblight came, even the rites are not always enough.'},
        {'id': 'physician', 'aliases': 'physician doctor', 'short': 'the physician', 'role': 'elite', 'level': 15,
         'long': 'The physician scrubs blood from his hands, his face grey with fatigue.', 'flags': 'b', 'align': 600, 'sex': 1,
         'desc': 'The finest surgeon in Midgaard, and the only one left. He has cut off more limbs this year than in the rest of his life together.',
         'equip': [('bone_saw', 'wield', 100)]},
        {'id': 'bell_ringer', 'aliases': 'ringer bell', 'short': 'the bell-ringer', 'role': 'harmless', 'level': 12,
         'long': 'The bell-ringer sits by the rope, waiting for the next death.', 'flags': 'b', 'align': 300, 'sex': 1,
         'desc': 'Deaf in one ear from the bell. He rang it forty-one times yesterday.'},
        {'id': 'belfry_bat', 'aliases': 'bat belfry', 'short': 'a belfry bat', 'role': 'standard', 'level': 11,
         'long': 'A bat with a wingspan like a cloak hangs from the beams.', 'flags': 'f', 'align': -200, 'attack': 'bite',
         'desc': 'Far too large for a bat. The humming of the bell seems to have drawn it here and made it grow.'},
        {'id': 'apothecary', 'aliases': 'apothecary woman', 'short': 'the apothecary', 'role': 'harmless', 'level': 13,
         'long': 'The apothecary grinds poppy seed at her bench.', 'flags': 'b', 'align': 600, 'sex': 2,
         'desc': 'Sharp-tongued, quick-handed, and running out of everything.',
         'carry': [('poppy_draught', 100)]},
        {'id': 'mortuary_sister', 'aliases': 'sister mortuary', 'short': 'the mortuary sister', 'role': 'elite', 'level': 15,
         'long': 'A sister washes a body, a heavy mace hanging at her belt.', 'flags': 'b', 'align': 800, 'sex': 2,
         'desc': 'She washes the dead with great tenderness, and she keeps the mace close for the ones that sit up.',
         'equip': [('mortuary_mace', 'wield', 100)]},
        {'id': 'shrouded_dead', 'aliases': 'dead shrouded corpse', 'short': 'a shrouded corpse', 'role': 'standard', 'level': 13,
         'long': 'A shrouded corpse sits up slowly on its slab.', 'flags': 'f', 'align': -700, 'attack': 'claw',
         'desc': 'Grey stains spread through the linen. Beneath the shroud something turns its head toward the west.'},
        {'id': 'sexton', 'aliases': 'sexton drunk', 'short': 'the sexton', 'role': 'champion', 'level': 16,
         'long': 'The sexton sits on his cot with a bottle and a mattock.', 'flags': 'bl', 'align': 0, 'sex': 1,
         'desc': 'He keeps the keys to the catacombs. He has been down there since the dead began to walk, and he will not go down again for anyone, and he does not like anyone asking.',
         'equip': [('sexton_mattock', 'wield', 100)], 'carry': [('crypt_key', 100)]},
        {'id': 'risen_dead', 'aliases': 'dead risen corpse', 'short': 'a risen corpse', 'role': 'standard', 'level': 15,
         'long': 'A risen corpse in rotting grave-clothes sways, facing the western wall.', 'flags': 'f', 'align': -800, 'attack': 'claw',
         'desc': 'Midgaard\'s honoured dead, risen. Its skin is grey and its eyes are fixed on the West.'},
        {'id': 'bone_swarm', 'aliases': 'bones swarm', 'short': 'a clattering swarm of bones', 'role': 'standard', 'level': 14,
         'long': 'A whirling swarm of loose bones clatters through the air.', 'flags': 'f', 'align': -800, 'attack': 'crush',
         'desc': 'Hundreds of small bones, finger joints and vertebrae, spinning together as if a storm were trapped in them.'},
        {'id': 'ossuary_guardian', 'aliases': 'guardian ossuary skeleton', 'short': 'an ossuary guardian', 'role': 'elite', 'level': 17,
         'long': 'A tall skeleton assembled from many bodies rises with a clatter.', 'flags': 'bf', 'align': -900, 'attack': 'crush',
         'desc': 'Too many ribs, too many arms, a skull from a giant. The bones put themselves together into something new.',
         'carry': [('bone_amulet', 50)]},
        {'id': 'drowned_dead', 'aliases': 'drowned dead corpse', 'short': 'a drowned corpse', 'role': 'standard', 'level': 16,
         'long': 'A bloated corpse rises from the black water.', 'flags': 'f', 'align': -800, 'attack': 'claw',
         'desc': 'Swollen and white, water running from its mouth, it reaches for you with fingers that have no nails.'},
        {'id': 'risen_monk', 'aliases': 'monk risen abbot', 'short': 'a risen abbot', 'role': 'elite', 'level': 17,
         'long': 'A risen abbot in mouldering robes chants in a dead language.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Once a holy man who healed the sick. Now he chants the falling note of the Grey Choir, and his hands are cold as the grave.',
         'equip': [('abbots_rosary', 'neck', 40)]},
        {'id': 'unquiet_abbess', 'aliases': 'abbess unquiet', 'short': 'the Unquiet Abbess', 'role': 'champion', 'level': 18,
         'long': 'The Unquiet Abbess rises from her broken tomb, grey light burning in her eyes.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'She founded the hospice four hundred years ago and gave her life to healing. The West has reached down into her grave and given her a new purpose: to raise every soul the hospice could not save, and march them to the wall.',
         'equip': [('abbess_crook', 'wield', 100), ('abbess_veil', 'head', 100)], 'carry': [('crypt_key', 100)]},
    ],
    'objs': [
        {'id': 'holy_basin', 'kind': 'fountain', 'aliases': 'basin stone water', 'short': 'a stone basin',
         'long': 'A stone basin of clear water stands among the herbs.', 'liquid': 0},
        {'id': 'comfrey_poultice', 'kind': 'potion', 'level': 12, 'spells': [16, 0, 0], 'spell_level': 12,
         'aliases': 'poultice comfrey', 'short': 'a comfrey poultice', 'long': 'A comfrey poultice wrapped in linen lies here.', 'weight': 1},
        {'id': 'poppy_draught', 'kind': 'potion', 'level': 14, 'spells': [15, 0, 0], 'spell_level': 14,
         'aliases': 'draught poppy vial', 'short': 'a vial of poppy draught', 'long': 'A small vial of cloudy liquid lies here.', 'weight': 1},
        {'id': 'bone_saw', 'kind': 'weapon', 'level': 15, 'attack': 'slash', 'aliases': 'saw bone', 'short': "a surgeon's bone saw",
         'long': "A surgeon's bone saw lies here."},
        {'id': 'mortuary_mace', 'kind': 'weapon', 'level': 15, 'attack': 'bludgeon', 'aliases': 'mace mortuary',
         'short': "a sister's mace", 'long': 'A plain iron mace lies here.', 'extra': 'i', 'affects': [('hitroll', 1)]},
        {'id': 'sexton_mattock', 'kind': 'weapon', 'level': 16, 'attack': 'crush', 'aliases': 'mattock', 'two_handed': True,
         'short': "the sexton's mattock", 'long': 'A heavy grave-digging mattock lies here.', 'affects': [('damroll', 2)]},
        {'id': 'crypt_key', 'kind': 'key', 'aliases': 'key crypt iron ring', 'short': 'a ring of crypt keys',
         'long': 'A heavy iron ring of keys lies here.', 'weight': 1},
        {'id': 'bone_amulet', 'kind': 'worn', 'slot': 'neck', 'level': 16, 'aliases': 'amulet bone',
         'short': 'an amulet of knucklebones', 'long': 'An amulet of strung knucklebones lies here.', 'affects': [('con', 1), ('save_para', -2)]},
        {'id': 'abbots_rosary', 'kind': 'worn', 'slot': 'neck', 'level': 17, 'aliases': 'rosary beads',
         'short': "an abbot's rosary", 'long': 'A rosary of black beads lies here.', 'affects': [('wis', 1), ('mana', 20)]},
        {'id': 'abbess_crook', 'kind': 'weapon', 'level': 19, 'attack': 'bludgeon', 'aliases': 'crook abbess silver',
         'short': "the Abbess's silver crook", 'long': 'A tarnished silver crook lies here.',
         'affects': [('hitroll', 2), ('damroll', 2), ('wis', 1)]},
        {'id': 'abbess_veil', 'kind': 'armor', 'slot': 'head', 'level': 19, 'aliases': 'veil abbess',
         'short': "the Abbess's grave veil", 'long': 'A veil of yellowed lace lies here.',
         'affects': [('save_spell', -2), ('mana', 30)]},
    ],
}
