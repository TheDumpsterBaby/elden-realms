"""W15 The Seat of Nu\'Groth -- the endgame, level 100 and remort.

The source of all evil in the realm. Its name is not yet decided; until it is,
it is "Nu\'Groth". Built for a full group of remorted level-100
characters.
"""

ZONE = {
    'num': 214, 'name': 'The Seat of Nu\'Groth', 'builders': 'Claude', 'lifespan': 30,
    'rooms': [
        {'id': 'antechamber', 'name': 'The Antechamber of Light That Is Not Light', 'sector': 'inside',
         'desc': """The corridor opens into a vast space filled with a grey radiance that has no
         source and casts no shadows.  It is cold, and silent, and it goes on forever.
         Figures kneel in rows in the radiance, millions of them, every soul the West has
         ever taken, facing the same way.""",
         'exits': {'e': {'to': '@21307', 'back_desc': 'West, the corridor opens onto a radiance that is not light.'}, 'w': 'kneeling_host'},
         'mobs': [('taken_soul', 2)]},
        {'id': 'kneeling_host', 'name': 'Among the Kneeling Host', 'sector': 'inside',
         'desc': """You walk between the kneeling dead.  Kings and beggars, soldiers and children,
         the Reaver and the Bandit Lord, faces you passed on the road.  They do not look
         at you.  They look west, toward the heart of the radiance, where something waits
         that is too large to see.""",
         'exits': {'w': 'seat', 'n': 'chosen_hall', 's': 'unbecoming'},
         'mobs': [('taken_soul', 2), ('entity_herald', 1)]},
        {'id': 'chosen_hall', 'name': 'The Hall of the Chosen', 'sector': 'inside',
         'desc': """A hall where Nu\'Groth\'s greatest servants stand on pillars of grey light, those
         who were too valuable to send east: archmages, saints, conquerors, every one of
         them hollowed and remade.  They step down from their pillars as you enter.""",
         'mobs': [('chosen_servant', 2)]},
        {'id': 'unbecoming', 'name': 'The Place of Unbecoming', 'sector': 'inside',
         'desc': """Here the grey radiance thickens into a fog that unmakes whatever it touches.  Your
         hand, held out before you, goes faint at the edges.  Things that were once heroes
         drift in the fog, half unmade, reaching for you, wanting to share what is left of
         them.""",
         'mobs': [('unbecoming_shade', 2)]},
        {'id': 'seat', 'name': 'The Seat of Nu\'Groth', 'sector': 'inside',
         'desc': """At the heart of the radiance there is nothing, and the nothing is aware of you.  It
         has a shape only because your mind insists on giving it one: a vast dark figure
         seated on nothing, larger than mountains, closer than your own breath.  It has no
         face.  It is the source of all evil in the realm, and it has noticed you.""",
         'mobs': [('the_entity', 1)]},
    ],
    'mobs': [
        {'id': 'taken_soul', 'aliases': 'soul taken kneeling', 'short': 'a taken soul', 'role': 'elite', 'level': 100,
         'long': 'One of the kneeling host rises and turns toward you with empty eyes.', 'flags': 'f', 'align': -1000, 'attack': 'claw',
         'desc': 'Someone the West took, kept forever in the radiance.'},
        {'id': 'entity_herald', 'aliases': 'herald voice nugroth', 'short': 'a voice of Nu\'Groth', 'role': 'champion', 'level': 100,
         'long': 'A tall figure of grey light speaks with a voice like the whole sky.', 'flags': 'bfl', 'align': -1000, 'aff': 'h',
         'desc': 'One of Nu\'Groth\'s voices, given shape to speak to things too small to hear it directly.',
         'carry': [('voice_ring', 100)]},
        {'id': 'chosen_servant', 'aliases': 'servant chosen', 'short': 'a chosen servant', 'role': 'champion', 'level': 100,
         'long': 'A remade archmage steps down from its pillar of grey light.', 'flags': 'fl', 'align': -1000, 'aff': 'h',
         'desc': 'Too great to waste on the march east. Kept here, beside Nu\'Groth, forever.',
         'equip': [('chosen_blade', 'wield', 100)]},
        {'id': 'unbecoming_shade', 'aliases': 'shade unbecoming', 'short': 'an unbecoming shade', 'role': 'champion', 'level': 100,
         'long': 'A half-unmade hero drifts out of the fog, reaching for you.', 'flags': 'fl', 'align': -1000, 'attack': 'claw',
         'desc': 'Once a hero. Now less every moment, and desperate to take you with it.',
         'carry': [('unmade_relic', 60)]},
        {'id': 'the_entity', 'aliases': 'nugroth groth entity dark', 'short': 'Nu\'Groth', 'role': 'entity', 'level': 100,
         'long': 'Nu\'Groth turns the whole of its attention upon you.', 'flags': 'bfl', 'align': -1000, 'aff': 'hq',
         'desc': 'The source of all evil in the realm. It has no name that a mortal tongue can hold, and no shape except the one your mind gives it. It has been patient for longer than the world has had a sun. It does not hate you. It simply intends that you, and everything you love, become part of it.',
         'carry': [('heart_of_the_west', 100), ('crown_of_unbeing', 100)]},
    ],
    'objs': [
        {'id': 'voice_ring', 'kind': 'worn', 'slot': 'finger', 'level': 102, 'aliases': 'ring voice grey',
         'short': 'a ring of grey light', 'long': 'A ring of solid grey light lies here.', 'affects': [('cha', 3), ('mana', 80), ('save_spell', -4)]},
        {'id': 'chosen_blade', 'kind': 'weapon', 'level': 102, 'attack': 'slash', 'aliases': 'blade chosen',
         'short': 'a blade of the chosen', 'long': 'A blade of grey light that is heavy as iron lies here.', 'affects': [('hitroll', 6), ('damroll', 6)]},
        {'id': 'unmade_relic', 'kind': 'worn', 'slot': 'hold', 'level': 102, 'aliases': 'relic unmade',
         'short': 'a half-unmade relic', 'long': 'A relic that flickers between being and not being lies here.', 'affects': [('hit', 80), ('mana', 80)]},
        {'id': 'heart_of_the_west', 'kind': 'worn', 'slot': 'neck', 'level': 105, 'aliases': 'heart west darkness',
         'short': 'the Heart of the West', 'long': 'A shard of perfect darkness, cold beyond cold, lies here.',
         'affects': [('str', 3), ('dex', 3), ('con', 3), ('hit', 100), ('save_spell', -5)]},
        {'id': 'crown_of_unbeing', 'kind': 'armor', 'slot': 'head', 'level': 105, 'aliases': 'crown unbeing',
         'short': 'the Crown of Unbeing', 'long': 'A crown that is a hole in the world lies here.',
         'affects': [('hitroll', 6), ('damroll', 6), ('hit', 100), ('wis', 3)]},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
ZONE['rooms'] += [
    {'id': 'hall_of_names', 'name': 'The Hall of Unspoken Names', 'sector': 'inside',
     'desc': """North of the antechamber a hall of grey stone is carved floor to ceiling with
     names, every name of every soul the West has taken, and Nu\'Groth is slowly erasing
     them.  Something tall walks the hall with a chisel, and where it passes the names are
     gone.""",
     'exits': {'s': 'antechamber'},
     'mobs': [('name_eater', 1)]},
    {'id': 'river_of_souls', 'name': 'The River of Souls', 'sector': 'inside',
     'desc': """South of the antechamber runs a river of grey light, and in it drift souls, millions
     of them, carried west.  A ferryman poles a boat of bone along it, and he will take you
     across, for a price that is always the same.""",
     'exits': {'n': 'antechamber'},
     'mobs': [('soul_ferryman', 1)]},
    {'id': 'pillar_saints', 'name': 'The Pillar of Saints', 'sector': 'inside',
     'desc': """North of the hall of the chosen, a pillar of grey light holds the saints the West has
     taken: healers and martyrs, haloes gone grey.  The greatest of them stands on the
     pillar's foot, and the light around her head is the grey of ash.""",
     'exits': {'s': 'chosen_hall'},
     'mobs': [('fallen_saint', 1)]},
    {'id': 'pillar_conquerors', 'name': 'The Pillar of Conquerors', 'sector': 'inside',
     'desc': """West of the hall of the chosen, a pillar holds the conquerors: the warlords and
     emperors who thought they could bargain with the West.  The last and greatest of them
     steps down with an axe that has broken a hundred kingdoms.""",
     'exits': {'e': 'chosen_hall'},
     'mobs': [('fallen_conqueror', 1)]},
    {'id': 'deepest_fog', 'name': 'The Deepest Fog', 'sector': 'inside',
     'desc': """The fog of unbecoming is thickest here.  You can no longer see your own hands, and
     you are not entirely sure you still have them.  Shades drift past, nearly gone,
     reaching.""",
     'exits': {'n': 'unbecoming'},
     'mobs': [('unbecoming_shade', 2)]},
    {'id': 'first_hero', 'name': 'Where the First Hero Kneels', 'sector': 'inside',
     'desc': """West of the fog, alone, kneels the first hero who ever reached the Seat: a woman in
     armour older than any kingdom, her sword across her knees.  She has knelt here since
     the world was young.  She is not entirely unmade.  She is not entirely on your
     side.""",
     'exits': {'e': 'unbecoming'},
     'mobs': [('first_hero', 1)]},
    {'id': 'above_host', 'name': 'Above the Kneeling Host', 'sector': 'inside',
     'desc': """You rise above the host as if the radiance were water, and from here you can see
     them all, row on row to the edge of sight, facing west.  Some of them look up.""",
     'exits': {'d': 'kneeling_host'},
     'mobs': [('taken_soul', 2)]},
    {'id': 'beneath_host', 'name': 'Beneath the Host', 'sector': 'inside',
     'desc': """Beneath the host the radiance goes down into roots of grey light that run east,
     under the Threshold, under the Bastion, under the march, all the way to Midgaard.  This
     is how the West spreads.  Something guards the roots.""",
     'exits': {'u': 'kneeling_host'},
     'mobs': [('root_of_the_west', 1)]},
    {'id': 'left_hand', 'name': 'The Left Hand of Nu\'Groth', 'sector': 'inside',
     'desc': """North of the Seat the darkness takes the shape of a hand, vast, resting on nothing.
     Its fingers move.  It is the hand that takes.""",
     'exits': {'s': 'seat'},
     'mobs': [('left_hand', 1)]},
    {'id': 'right_hand', 'name': 'The Right Hand of Nu\'Groth', 'sector': 'inside',
     'desc': """South of the Seat the darkness takes the shape of a second hand, open, palm up.  It
     is the hand that offers.  What it offers is everything you have ever wanted, and it is
     not lying.""",
     'exits': {'n': 'seat'},
     'mobs': [('right_hand', 1)]},
]
ZONE['mobs'] += [
    {'id': 'name_eater', 'aliases': 'eater name chisel', 'short': 'the eraser of names', 'role': 'elite', 'level': 100,
     'long': 'A tall grey figure turns from the wall, chisel raised, and begins on your name.', 'flags': 'bfl', 'align': -1000, 'attack': 'stab',
     'desc': 'When it has erased every name, nobody will remember there was ever anyone else.'},
    {'id': 'soul_ferryman', 'aliases': 'ferryman soul', 'short': 'the ferryman of souls', 'role': 'champion', 'level': 100,
     'long': 'The ferryman of souls leans on his pole and holds out a bony hand for payment.', 'flags': 'bfl', 'align': -1000,
     'desc': 'He takes everyone west. He would like to take you.',
     'carry': [('ferryman_coin', 100)]},
    {'id': 'fallen_saint', 'aliases': 'saint fallen', 'short': 'the Fallen Saint', 'role': 'champion', 'level': 100,
     'long': 'The Fallen Saint opens her arms to you, her ash-grey halo burning.', 'flags': 'bfl', 'align': -1000, 'sex': 2, 'attack': 'blast',
     'desc': 'She healed a thousand thousand, and then she came west to heal the West.',
     'carry': [('saint_halo', 100)]},
    {'id': 'fallen_conqueror', 'aliases': 'conqueror fallen', 'short': 'the Fallen Conqueror', 'role': 'champion', 'level': 100,
     'long': 'The Fallen Conqueror steps down from his pillar, hefting an axe that broke a hundred kingdoms.', 'flags': 'bfl', 'align': -1000,
     'desc': 'He thought he could rule the West. It let him think so for a little while.',
     'equip': [('conqueror_axe', 'wield', 100)]},
    {'id': 'first_hero', 'aliases': 'hero first woman', 'short': 'the First Hero', 'role': 'champion', 'level': 100,
     'long': 'The First Hero rises from her knees and raises her ancient sword.', 'flags': 'bfl', 'align': 0, 'sex': 2,
     'desc': 'She reached the Seat before there were kingdoms, and she has knelt here ever since, neither taken nor free. She will test you, to see if you are the one she has waited for.',
     'carry': [('first_sword', 100)]},
    {'id': 'root_of_the_west', 'aliases': 'root west guardian', 'short': 'the Root of the West', 'role': 'elite', 'level': 100,
     'long': 'The roots of grey light knot together and rise into a shape.', 'flags': 'bfl', 'align': -1000, 'attack': 'whip',
     'desc': 'The part of Nu\'Groth that reaches east.'},
    {'id': 'left_hand', 'aliases': 'hand left', 'short': 'the Left Hand of Nu\'Groth', 'role': 'champion', 'level': 100,
     'long': 'The Left Hand of Nu\'Groth closes slowly around you.', 'flags': 'bfl', 'align': -1000, 'attack': 'crush',
     'desc': 'The hand that takes.',
     'carry': [('hand_gauntlets', 100)]},
    {'id': 'right_hand', 'aliases': 'hand right', 'short': 'the Right Hand of Nu\'Groth', 'role': 'champion', 'level': 100,
     'long': 'The Right Hand of Nu\'Groth opens, offering, and then strikes.', 'flags': 'bfl', 'align': -1000, 'attack': 'crush',
     'desc': 'The hand that offers.',
     'carry': [('hand_bracers', 100)]},
]
ZONE['objs'] += [
    {'id': 'ferryman_coin', 'kind': 'worn', 'slot': 'hold', 'level': 102, 'aliases': 'coin ferryman',
     'short': "the ferryman's coin", 'long': 'A coin of grey light lies here.', 'affects': [('save_spell', -4), ('mana', 60)]},
    {'id': 'saint_halo', 'kind': 'armor', 'slot': 'about', 'level': 102, 'aliases': 'halo saint ash',
     'short': 'an ash-grey halo', 'long': 'A ring of ash-grey light hangs in the air here.', 'affects': [('wis', 3), ('hit', 60)]},
    {'id': 'conqueror_axe', 'kind': 'weapon', 'level': 102, 'attack': 'slash', 'two_handed': True, 'aliases': 'axe conqueror',
     'short': "the Conqueror's axe", 'long': 'A huge black axe lies here.', 'affects': [('hitroll', 5), ('damroll', 7)]},
    {'id': 'first_sword', 'kind': 'weapon', 'level': 104, 'attack': 'slash', 'aliases': 'sword first hero ancient',
     'short': "the First Hero's sword", 'long': 'An ancient bronze sword, still bright, lies here.', 'extra': 'g',
     'affects': [('hitroll', 7), ('damroll', 7)]},
    {'id': 'hand_gauntlets', 'kind': 'armor', 'slot': 'hands', 'level': 103, 'aliases': 'gauntlets dark hand',
     'short': 'gauntlets of the taking hand', 'long': 'A pair of gauntlets of solid darkness lies here.', 'affects': [('str', 2), ('damroll', 4)]},
    {'id': 'hand_bracers', 'kind': 'armor', 'slot': 'wrist', 'level': 103, 'aliases': 'bracers offering hand',
     'short': 'bracers of the offering hand', 'long': 'A pair of dark bracers lies here.', 'affects': [('dex', 2), ('hitroll', 4)]},
]
