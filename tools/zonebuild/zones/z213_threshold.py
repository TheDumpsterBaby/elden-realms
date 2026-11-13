"""W14 The Threshold -- the Blight, levels 95-100.

Beyond the Bastion's inner gate, reality thins. Distances lie, the sky is
broken, and the things that live here were never made at all. Nu\'Groth\'s
will presses on every room. The Keeper of the Threshold guards the last door.
"""

ZONE = {
    'num': 213, 'name': 'The Threshold', 'builders': 'Claude', 'lifespan': 25,
    'rooms': [
        {'id': 'glass_stair', 'name': 'The Stair of Glass', 'sector': 'inside',
         'desc': """Beyond the gate a stair of clear glass climbs into grey nothing.  There is no
         ground beneath it, no sky above, only a grey haze in every direction.  Each step
         rings like a bell.  When you look down through the glass you see the realm far
         below, very small, and darkness spreading east across it.""",
         'exits': {'e': {'to': '@21209', 'back_desc': 'Through the inner gate, a stair of glass climbs into grey nothing.'}, 'u': 'mirror_hall'},
         'mobs': [('unmade_thing', 1)]},
        {'id': 'mirror_hall', 'name': 'The Hall of Reflections', 'sector': 'inside',
         'desc': """A hall of mirrors with no walls, only mirrors, hanging in the grey.  Each mirror
         shows you, but wrong: older, younger, hollowed, kneeling, dead.  In one you are
         wearing grey and marching east.  The reflections watch you, and some of them step
         out of their frames.""",
         'exits': {'w': 'broken_sky', 'n': 'memory_garden'},
         'mobs': [('false_reflection', 2)]},
        {'id': 'memory_garden', 'name': 'The Garden of Lost Things', 'sector': 'field',
         'desc': """A garden of grey flowers where everything the West has ever taken lies scattered:
         toys, crowns, letters, wedding rings, a child\'s drawing of a house.  They are
         not real; they are memories, and they fade when you touch them.  Things that
         were never made wander among them, collecting.""",
         'mobs': [('unmade_thing', 2), ('memory_eater', 1)]},
        {'id': 'broken_sky', 'name': 'Beneath the Broken Sky', 'sector': 'field',
         'desc': """You stand on a plain of grey dust beneath a sky that has cracked like a plate.
         Through the cracks you can see something vast and dark moving, very far away,
         like a shape beneath ice.  Fragments of the sky fall slowly around you, and
         where they land the ground stops existing.""",
         'exits': {'w': 'drowning_dark', 's': 'unmade_field'},
         'mobs': [('sky_shard', 2)]},
        {'id': 'unmade_field', 'name': 'The Field of the Unmade', 'sector': 'field',
         'desc': """A field where Nu\'Groth tries out shapes before it sends them east.  Half-formed
         creatures stand frozen in mid-making: a wolf with a human face, a man made of
         hands, a horse with no head and too many legs.  Some of them are finished enough
         to move.""",
         'mobs': [('unmade_horror', 2)]},
        {'id': 'drowning_dark', 'name': 'The Drowning Dark', 'sector': 'inside', 'flags': 'a',
         'desc': """A darkness so complete it feels like water, pressing on your eyes and filling
         your mouth.  You cannot tell up from down.  Voices whisper from every side, the
         voices of everyone you have lost, telling you to stop, to rest, to let go.  It
         would be so easy.""",
         'exits': {'w': 'last_door'},
         'mobs': [('void_wraith', 2)]},
        {'id': 'last_door', 'name': 'Before the Last Door', 'sector': 'inside',
         'desc': """The darkness ends at a door standing alone in the grey, a plain wooden door like
         the door of any farmhouse in the realm.  It is the most frightening thing you
         have ever seen.  Before it stands the Keeper of the Threshold, who has waited
         here since before the first kingdom of men.""",
         'exits': {'w': 'beyond_door'},
         'mobs': [('threshold_keeper', 1)]},
        {'id': 'beyond_door', 'name': 'Beyond the Door', 'sector': 'inside',
         'desc': """Through the door is a long corridor of grey stone, perfectly ordinary, perfectly
         silent, leading west.  The pressure of Nu\'Groth\'s attention is overwhelming
         now, a weight on your mind like a mountain.  At the end of the corridor is a
         light that is not light.""",
         'mobs': [('void_wraith', 1)]},
    ],
    'mobs': [
        {'id': 'unmade_thing', 'aliases': 'thing unmade', 'short': 'an unmade thing', 'role': 'standard', 'level': 97,
         'long': 'Something that was never properly made drifts toward you, changing shape.', 'flags': 'f', 'align': -1000, 'attack': 'claw',
         'desc': 'It has not decided what it is yet. It would like to try being you.'},
        {'id': 'false_reflection', 'aliases': 'reflection false mirror', 'short': 'a false reflection', 'role': 'elite', 'level': 98,
         'long': 'Your own reflection steps out of a mirror, wearing grey, smiling.', 'flags': 'f', 'align': -1000,
         'desc': 'You, as Nu\'Groth would have you. It knows every move you know.',
         'equip': [('mirror_shard', 'wield', 100)]},
        {'id': 'memory_eater', 'aliases': 'eater memory', 'short': 'a memory eater', 'role': 'champion', 'level': 100,
         'long': 'A tall thin shape with a mouth where its face should be gathers up memories and eats them.', 'flags': 'bfl', 'align': -1000, 'attack': 'bite',
         'desc': 'It eats what the West takes, so that nothing is remembered. It would like to eat yours.',
         'carry': [('locket_memory', 100)]},
        {'id': 'sky_shard', 'aliases': 'shard sky', 'short': 'a falling sky shard', 'role': 'elite', 'level': 98,
         'long': 'A shard of broken sky drifts down toward you, edges sharp as nothing.', 'flags': 'f', 'align': -1000, 'attack': 'slash',
         'desc': 'Where it touches, things stop being.'},
        {'id': 'unmade_horror', 'aliases': 'horror unmade', 'short': 'an unmade horror', 'role': 'elite', 'level': 99,
         'long': 'A creature with too many hands and a wolf\'s head lurches out of its unfinished pose.', 'flags': 'f', 'align': -1000, 'attack': 'claw',
         'desc': 'A draft of something Nu\'Groth will send east next year.'},
        {'id': 'void_wraith', 'aliases': 'wraith void', 'short': 'a void wraith', 'role': 'elite', 'level': 99,
         'long': 'A shape of deeper darkness whispers your mother\'s name.', 'flags': 'f', 'align': -1000, 'attack': 'claw',
         'desc': 'It speaks with the voices of the dead and it pulls you down into the dark.'},
        {'id': 'threshold_keeper', 'aliases': 'keeper threshold', 'short': 'the Keeper of the Threshold', 'role': 'boss', 'level': 100,
         'long': 'The Keeper of the Threshold unfolds before the door, taller than the hall, made of grey light and old silence.', 'flags': 'bfl', 'align': -1000, 'aff': 'q',
         'desc': 'It guarded the door before Nu\'Groth came, and it guards it now for Nu\'Groth. It is very tired, and very patient, and it has never yet let anyone pass.',
         'carry': [('keeper_lantern', 100), ('threshold_mantle', 100)]},
    ],
    'objs': [
        {'id': 'mirror_shard', 'kind': 'weapon', 'level': 98, 'attack': 'slash', 'aliases': 'shard mirror',
         'short': 'a shard of mirror', 'long': 'A long shard of mirror lies here, reflecting someone who is not you.', 'affects': [('hitroll', 4)]},
        {'id': 'locket_memory', 'kind': 'worn', 'slot': 'neck', 'level': 100, 'aliases': 'locket memory',
         'short': 'a locket of remembered faces', 'long': 'A small silver locket lies here.', 'affects': [('wis', 3), ('int', 2), ('save_spell', -4)],
         'extras': {'locket': 'Inside, a tiny painting of faces you almost recognise. Holding it, you remember everyone you have lost, clearly, and it hurts, and it is good.'}},
        {'id': 'keeper_lantern', 'kind': 'light', 'level': 101, 'hours': -1, 'aliases': 'lantern keeper grey',
         'short': 'the Keeper\'s lantern', 'long': 'A lantern burning with grey light that shows true things lies here.', 'extra': 'a',
         'affects': [('hitroll', 4), ('damroll', 4), ('mana', 60)]},
        {'id': 'threshold_mantle', 'kind': 'armor', 'slot': 'about', 'level': 101, 'aliases': 'mantle threshold silence',
         'short': 'a mantle of old silence', 'long': 'A grey mantle that makes no sound lies here.', 'affects': [('hit', 90), ('dex', 2), ('save_para', -5)]},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
ZONE['rooms'] += [
    {'id': 'beneath_stair', 'name': 'Beneath the Stair of Glass', 'sector': 'inside',
     'desc': """You climb down off the side of the glass stair onto a web of grey threads strung
     across the nothing.  Spiders of glass work the web, and in it hang things they have
     caught: birds, souls, a whole regiment still in formation.""",
     'exits': {'u': 'glass_stair'},
     'mobs': [('glass_spider', 2)]},
    {'id': 'mirror_maze', 'name': 'The Maze of Mirrors', 'sector': 'inside',
     'desc': """South of the hall of reflections the mirrors close in into a maze where every
     turn shows you another self, each one more wrong than the last.  Some of them are
     walking the maze too, and they know the way better than you.""",
     'exits': {'n': 'mirror_hall', 's': 'shattered_mirror'},
     'mobs': [('false_reflection', 2)]},
    {'id': 'shattered_mirror', 'name': 'The Shattered Mirror', 'sector': 'inside',
     'desc': """At the heart of the maze stands a great mirror, shattered, and in every shard is the
     same face: not yours, not anyone's, a face made of all the faces the West has taken.
     It steps out of the frame wearing a crown of glass.""",
     'mobs': [('mirror_sovereign', 1)]},
    {'id': 'childhood_house', 'name': 'The House You Grew Up In', 'sector': 'inside',
     'desc': """North of the garden there is a door, and through it is the house you grew up in,
     exactly as you remember it: the table, the hearth, the smell of bread.  Someone is
     standing at the hearth with their back to you, and they are wearing your mother's
     face, and it does not fit.""",
     'exits': {'s': 'memory_garden'},
     'mobs': [('wearing_thing', 1)]},
    {'id': 'unfought_battle', 'name': 'A Battle That Never Happened', 'sector': 'field',
     'desc': """West of the garden lies a battlefield of a war that was never fought, between
     kingdoms that were never founded.  Nu\'Groth dreams it here, over and over, and the
     soldiers in it do not know they are not real.  Neither do their swords.""",
     'exits': {'e': 'memory_garden'},
     'mobs': [('unremembered_soldier', 3)]},
    {'id': 'making_pits', 'name': 'The Pits of Making', 'sector': 'field',
     'desc': """South of the field of the unmade, great pits are dug into the grey dust, and in each
     pit something vast is being made: a titan of stitched flesh and grey iron, as tall as
     a tower, nearly finished.  One of them has opened its eyes.""",
     'exits': {'n': 'unmade_field'},
     'mobs': [('unmade_horror', 1), ('half_made_titan', 1)]},
    {'id': 'shape_vats', 'name': 'The Vats of Shape', 'sector': 'inside',
     'desc': """West of the field of the unmade stand vats of grey matter that has not yet decided
     what it will be.  Shapes rise in it and sink again: a hand, a wing, a child's face.
     A tender with too many arms stirs them with long poles.""",
     'exits': {'e': 'unmade_field'},
     'mobs': [('shape_tender', 1)]},
    {'id': 'sky_crack', 'name': 'Through the Crack in the Sky', 'sector': 'field',
     'desc': """You climb a slope of fallen sky-fragments up into a crack in the broken sky, and
     stand on the edge of the world.  Beyond the crack there are no stars, only the vast
     dark shape moving, very close now.  Something that eats stars is feeding at the
     edge.""",
     'exits': {'s': 'broken_sky'},
     'mobs': [('sky_shard', 1), ('star_eater', 1)]},
    {'id': 'voice_well', 'name': 'The Well of Voices', 'sector': 'inside', 'flags': 'a',
     'desc': """North of the drowning dark a well drops away into the deepest dark of all, and out
     of it rise the voices of every person you have ever known, all speaking at once,
     calling you down.  Wraiths circle the well like gulls over a wreck.""",
     'exits': {'s': 'drowning_dark'},
     'mobs': [('void_wraith', 2)]},
    {'id': 'keepers_watch', 'name': "The Keeper's Long Watch", 'sector': 'inside',
     'desc': """A small bare room north of the door where the Keeper rested, in the ages before
     Nu\'Groth came, between those who tried to pass.  A chair, a cold lamp, a journal
     on the table.  Something of the Keeper is still here, an echo, keeping watch.""",
     'exits': {'s': 'last_door'},
     'mobs': [('keeper_echo', 1)], 'objs': [('keeper_journal', 1)]},
    {'id': 'grey_cells', 'name': 'The Grey Cells', 'sector': 'inside',
     'desc': """A row of cells north of the corridor, where Nu\'Groth keeps the heroes it means to
     remake.  They hang in the grey light, half themselves and half something else, and
     the finished ones are let out to guard the corridor.""",
     'exits': {'s': 'beyond_door'},
     'mobs': [('remade_hero', 2)]},
    {'id': 'listening_hall', 'name': 'The Hall of Listening', 'sector': 'inside',
     'desc': """South of the corridor is a hall of perfect silence, its walls lined with ears, huge
     and grey and listening.  This is how Nu\'Groth hears the east.  Every word spoken in
     Midgaard comes here.""",
     'exits': {'n': 'beyond_door'},
     'mobs': [('listening_thing', 1)]},
]
ZONE['mobs'] += [
    {'id': 'glass_spider', 'aliases': 'spider glass', 'short': 'a glass spider', 'role': 'elite', 'level': 97,
     'long': 'A spider of clear glass runs down a grey thread toward you.', 'flags': 'f', 'align': -800, 'attack': 'bite',
     'desc': 'You can see what it ate last through its body.'},
    {'id': 'mirror_sovereign', 'aliases': 'sovereign mirror', 'short': 'the Mirror Sovereign', 'role': 'champion', 'level': 100,
     'long': 'The Mirror Sovereign steps out of the shattered frame, a crown of glass on its stolen face.', 'flags': 'bfl', 'align': -1000,
     'desc': 'All the faces the West has taken, wearing one another.',
     'carry': [('mirror_crown', 100)]},
    {'id': 'wearing_thing', 'aliases': 'thing wearing face', 'short': 'something wearing a face', 'role': 'elite', 'level': 98,
     'long': 'The thing at the hearth turns around, and the face it is wearing smiles too wide.', 'flags': 'bfl', 'align': -1000, 'attack': 'claw',
     'desc': 'It wants you to come home.'},
    {'id': 'unremembered_soldier', 'aliases': 'soldier unremembered', 'short': 'an unremembered soldier', 'role': 'standard', 'level': 97,
     'long': 'A soldier of a kingdom that never was charges at you.', 'flags': 'f', 'align': -500,
     'desc': 'Dreamed by Nu\'Groth, and fully, terribly real while the dream lasts.'},
    {'id': 'half_made_titan', 'aliases': 'titan half made', 'short': 'a half-made titan', 'role': 'champion', 'level': 100,
     'long': 'A titan of stitched flesh and grey iron tears itself out of its pit.', 'flags': 'bfl', 'align': -1000, 'attack': 'crush',
     'desc': 'Meant to march east next year and step over Midgaard\'s wall.',
     'carry': [('titan_heart', 100)]},
    {'id': 'shape_tender', 'aliases': 'tender shape', 'short': 'a shape tender', 'role': 'elite', 'level': 99,
     'long': 'The many-armed shape tender drops its poles and reaches for you.', 'flags': 'bfl', 'align': -1000, 'attack': 'claw',
     'desc': 'It would like to see what shape you would be.'},
    {'id': 'star_eater', 'aliases': 'eater star', 'short': 'a star-eater', 'role': 'elite', 'level': 99,
     'long': 'A long dark shape at the edge of the sky turns its mouth from the stars to you.', 'flags': 'f', 'align': -1000, 'attack': 'bite',
     'desc': 'There used to be more stars.',
     'carry': [('star_shard', 30)]},
    {'id': 'keeper_echo', 'aliases': 'echo keeper', 'short': 'an echo of the Keeper', 'role': 'elite', 'level': 99,
     'long': 'A faint grey echo of the Keeper rises from the chair.', 'flags': 'bl', 'align': 0,
     'desc': 'What is left of the Keeper from before Nu\'Groth: tired, grieving, and still bound to the door.'},
    {'id': 'remade_hero', 'aliases': 'hero remade', 'short': 'a remade hero', 'role': 'elite', 'level': 100,
     'long': 'A hero of the east, remade in grey, steps out of a cell with a familiar sword.', 'flags': 'f', 'align': -1000,
     'desc': 'You may have known this one, once.',
     'carry': [('remade_greaves', 25)]},
    {'id': 'listening_thing', 'aliases': 'thing listening ear', 'short': 'the listening thing', 'role': 'champion', 'level': 100,
     'long': 'The walls of ears all turn toward you, and the listening thing rises from among them.', 'flags': 'bfl', 'align': -1000, 'attack': 'blast',
     'desc': 'It has heard every word you ever said in Midgaard. It knows your name.'},
]
ZONE['objs'] += [
    {'id': 'mirror_crown', 'kind': 'armor', 'slot': 'head', 'level': 100, 'aliases': 'crown mirror glass',
     'short': 'a crown of mirror-glass', 'long': 'A crown of mirror-glass lies here, reflecting faces.', 'affects': [('hitroll', 5), ('int', 2)]},
    {'id': 'titan_heart', 'kind': 'worn', 'slot': 'hold', 'level': 101, 'aliases': 'heart titan',
     'short': "a titan's iron heart", 'long': 'A great iron heart lies here, still beating.', 'affects': [('hit', 70)]},
    {'id': 'star_shard', 'kind': 'weapon', 'level': 99, 'attack': 'pierce', 'aliases': 'shard star',
     'short': 'a shard of a dead star', 'long': 'A sliver of cold white light lies here.', 'affects': [('hitroll', 4), ('damroll', 3)]},
    {'id': 'remade_greaves', 'kind': 'armor', 'slot': 'legs', 'level': 100, 'aliases': 'greaves remade grey',
     'short': 'a pair of remade greaves', 'long': 'A pair of grey greaves lies here.', 'affects': [('hit', 40)]},
    {'id': 'keeper_journal', 'kind': 'other', 'level': 1, 'aliases': 'journal keeper book', 'cost': 10,
     'short': "the Keeper's journal", 'long': "A thin journal lies open on the table.",
     'extras': {'journal': 'The last entry, in a hand that shakes: "It came to the door today and asked to pass. I said no, as I have said to all. It did not argue. It simply waited, and I am so tired, and it is so patient. If you read this, I am still at the door. Kill me if you can. I would like to rest."'}},
]
