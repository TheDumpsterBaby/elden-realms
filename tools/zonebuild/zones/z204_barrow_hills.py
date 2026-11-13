"""W5 The Barrow Hills -- the March, levels 50-55.

Rolling grey hills studded with the burial mounds of an ancient people, now
breaking open one by one. A fortified monastery (working name the Monastery of
the Unsleeping Flame) is the stronghold: its monks keep vigil to hold the dead
down. Beneath the greatest mound, the first Barrow King is waking.
"""

ZONE = {
    'num': 204, 'name': 'The Barrow Hills', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'hill_road', 'name': 'The Hill Road', 'sector': 'hills',
         'desc': """The road from the battlefield climbs into hills of coarse grey grass.  Burial
         mounds rise on every slope, hundreds of them, ringed with standing stones.
         Many have been broken open, their stone doors cast down, and paths of
         trampled grass lead away from them in every direction.""",
         'exits': {'e': {'to': '@20318', 'back_desc': 'West, the road climbs into hills scattered with barrows.'}, 'w': 'crossing', 'n': 'open_barrow'},
         'mobs': [('barrow_wight', 1)]},
        {'id': 'open_barrow', 'name': 'A Broken Barrow', 'sector': 'hills',
         'desc': """A mound has been split open like a burst fruit.  Its stone door lies shattered
         in the grass, and the passage behind it gapes, breathing cold air.  Grave
         goods are scattered across the slope: bronze cups, beads, a little clay
         horse.  Whatever lay inside did not stop to take them.""",
         'exits': {'d': 'barrow_passage'},
         'mobs': [('barrow_wight', 2)]},
        {'id': 'barrow_passage', 'name': 'The Barrow Passage', 'sector': 'inside', 'flags': 'ad',
         'desc': """A passage of fitted stone slabs leads into the mound, so low you must stoop.
         The walls are carved with spirals, the ancient ones that the hill-folk made
         long before the West ever used the sign.  At the end lies an empty stone
         bed, and claw marks on the ceiling above it.""",
         'mobs': [('tomb_crawler', 2)]},
        {'id': 'crossing', 'name': 'The Crossing of Stones', 'sector': 'hills',
         'desc': """Four roads meet in a hollow between hills, marked by a cairn of white stones
         taller than a man.  Offerings have been left on it for centuries: coins,
         bread, little bone charms.  Someone has knocked the top off the cairn and
         painted the stones beneath it grey.""",
         'exits': {'w': 'monastery_road', 'n': 'robbers_camp', 's': 'ghoul_dell'},
         'mobs': [('barrow_wight', 1), ('ghoul_pack', 1)]},
        {'id': 'robbers_camp', 'name': 'The Grave Robbers\' Camp', 'sector': 'hills',
         'desc': """A camp of tents and dug-outs in the lee of a big barrow, where grave robbers
         came to loot the opened tombs.  Picks and shovels lie everywhere.  So do the
         robbers, or what is left of them, and some of what is left is still
         digging.""",
         'exits': {'n': 'great_dig'},
         'mobs': [('cursed_robber', 2)]},
        {'id': 'great_dig', 'name': 'The Great Dig', 'sector': 'hills',
         'desc': """The robbers drove a shaft straight down into the side of a huge mound,
         shoring it with timber.  A windlass stands over the shaft with a rope and
         bucket.  A sign scrawled on a plank by the windlass reads: DONT GO DOWN.
         Below that, in a different hand: SHE IS AWAKE.""",
         'exits': {'d': 'queen_tomb'},
         'mobs': [('cursed_robber', 1)]},
        {'id': 'queen_tomb', 'name': 'The Tomb of the Spiral Queen', 'sector': 'inside', 'flags': 'ad',
         'desc': """A round chamber beneath the mound, its walls lined with gold leaf and carved
         with a queen surrounded by kneeling figures.  Her stone coffin stands open.
         She sits on its edge, mummified and jewelled, combing her long dry hair, and
         she smiles at you with teeth like brown pegs.""",
         'mobs': [('spiral_queen', 1)]},
        {'id': 'ghoul_dell', 'name': 'The Ghoul Dell', 'sector': 'hills',
         'desc': """A deep dell between three barrows where the ghouls of the hills gather to feed.
         The grass is worn away to mud and bones.  The ghouls are pale and naked and
         move on all fours, and they have learned to hunt in packs like wolves.""",
         'exits': {'w': 'bone_hollow'},
         'mobs': [('ghoul_pack', 3)]},
        {'id': 'bone_hollow', 'name': 'The Bone Hollow', 'sector': 'hills',
         'desc': """At the end of the dell, the ghouls have piled the bones of their meals into a
         mound of their own, a mockery of the barrows around them.  On top of it sits
         the largest ghoul you have ever seen, cracking a thighbone and sucking out
         the marrow.""",
         'mobs': [('ghoul_patriarch', 1), ('ghoul_pack', 1)]},
        {'id': 'monastery_road', 'name': 'The Road to the Monastery', 'sector': 'hills',
         'desc': """A paved road climbs a steep hill toward a walled monastery, its stone walls
         lit by a ring of torches that never go out.  Bodies lie along the road,
         wrapped in white and laid in neat rows: the dead the monks have put to rest,
         awaiting burial in ground they have blessed.""",
         'exits': {'u': 'monastery_gate', 'w': 'western_downs'},
         'mobs': [('barrow_wight', 1)]},
        {'id': 'monastery_gate', 'name': 'The Gate of the Unsleeping Flame', 'sector': 'city', 'flags': 'c',
         'desc': """A great gate of oak bound with iron stands in the monastery wall, carved with a
         single open eye surrounded by flames.  Two monks in grey stand at it with
         staves, and above them on the wall more monks pace with torches, chanting.
         The chant never stops.""",
         'exits': {'w': 'courtyard'},
         'mobs': [('vigil_monk', 2)]},
        {'id': 'courtyard', 'name': 'The Monastery Courtyard', 'sector': 'city', 'flags': 'c',
         'desc': """A paved courtyard inside the walls, with a well in its centre and the
         monastery buildings around it.  Monks cross it quickly, always in pairs,
         always chanting.  Refugees from the hills huddle along the walls, given
         shelter here because the monks turn no living soul away.""",
         'exits': {'n': 'chapel', 's': 'refectory', 'w': 'cloister', 'u': 'wall_walk'},
         'objs': [('monastery_well', 1)],
         'mobs': [('vigil_monk', 1), ('hill_refugee', 2)]},
        {'id': 'wall_walk', 'name': 'The Wall Walk', 'sector': 'city', 'flags': 'c',
         'desc': """The top of the monastery wall, where monks walk the vigil in a ring that
         never breaks.  From here you can see the barrows stretching away in every
         direction, and the shapes moving among them.  Every so often a monk stops
         and hurls a torch down at something climbing the wall.""",
         'mobs': [('vigil_monk', 2)]},
        {'id': 'chapel', 'name': 'The Chapel of the Flame', 'sector': 'inside', 'flags': 'cde',
         'desc': """A tall chapel with no windows, lit by a single great flame that burns in a
         bronze bowl on the altar.  It has burned without fuel for six hundred years,
         the monks say, and while it burns the dead of the hills cannot pass the
         walls.  It is smaller than it used to be.""",
         'extras': {'flame bowl altar': 'A white flame, steady and silent. Its light seems to push against something you cannot see. At its edges, it flickers grey.'},
         'mobs': [('flame_keeper', 1)]},
        {'id': 'refectory', 'name': 'The Refectory', 'sector': 'inside', 'flags': 'cde',
         'desc': """Long tables where monks and refugees eat together in silence: barley bread,
         thin soup, water.  The monks give their own portions to the children.  A
         reader stands at a lectern reading aloud the names of the dead buried in
         the hills, one after another, as he has every day for forty years.""",
         'mobs': [('refectory_brother', 1), ('hill_refugee', 2)]},
        {'id': 'cloister', 'name': 'The Cloister of Graves', 'sector': 'inside', 'flags': 'c',
         'desc': """A cloister around a garth of graves, where the monks bury those they have put
         to rest.  Each grave has a small flame burning on it in a clay lamp.  An old
         monk tends the lamps, and every grave whose lamp goes out, he says, is a
         grave that will open.""",
         'exits': {'w': 'library', 'n': 'abbot_stair'},
         'mobs': [('lamp_tender', 1)]},
        {'id': 'library', 'name': 'The Library of the Dead', 'sector': 'inside', 'flags': 'cde',
         'desc': """Shelves of scrolls and books record every barrow in the hills: who lies in it,
         when they were buried, what rites keep them down.  A monk at a desk is copying
         one of them in great haste.  He tells you without looking up that the rites
         are failing, all of them, all at once.""",
         'extras': {'scrolls books shelves': 'Records of a thousand barrows. The newest scroll, unfinished: THE KING BENEATH THE GREAT MOUND STIRS. THE FLAME CANNOT HOLD HIM.'},
         'mobs': [('archivist_monk', 1)]},
        {'id': 'abbot_stair', 'name': 'The Abbot\'s Stair', 'sector': 'inside', 'flags': 'c',
         'desc': """A narrow stair spirals up inside the monastery's only tower.  The walls are
         painted with the faces of past abbots, each holding a flame.  The most
         recent portrait shows a hard-faced woman, and the paint is barely dry.""",
         'exits': {'u': 'abbot_room'}},
        {'id': 'abbot_room', 'name': 'The Abbot\'s Chamber', 'sector': 'inside', 'flags': 'cde',
         'desc': """A bare cell at the top of the tower: a cot, a desk, a window looking west.  The
         abbess of the monastery keeps the vigil here at night, watching the Great
         Mound on the western horizon, where a grey light has begun to burn.""",
         'extras': {'window west mound': 'The Great Mound, the largest barrow in the hills. A grey light leaks from it now, like dawn from under a door.'},
         'mobs': [('abbess_ulla', 1)]},
        {'id': 'western_downs', 'name': 'The Western Downs', 'sector': 'hills',
         'desc': """Beyond the monastery the hills grow higher and barer, and the barrows larger
         and older.  The wind moans over the grass.  Bones lie in the open, and
         shapes walk in the distance, some of them taller than any man.""",
         'exits': {'w': 'giants_barrow', 's': 'mound_avenue'},
         'mobs': [('barrow_wight', 2)]},
        {'id': 'giants_barrow', 'name': 'The Giant\'s Barrow', 'sector': 'hills',
         'desc': """An enormous long barrow lies along the ridge, its door large enough for a
         wagon.  The hill-folk buried their champions here, and their champions were
         not small.  The door is open.  Something inside is walking, and the ground
         shakes with each step.""",
         'exits': {'d': 'giant_hall'},
         'mobs': [('barrow_guardian', 1)]},
        {'id': 'giant_hall', 'name': 'The Hall of Champions', 'sector': 'inside', 'flags': 'ad',
         'desc': """A long hall beneath the barrow lined with stone biers, each one built for a
         man twice the height of a man.  The biers are empty.  At the far end, a
         giant skeleton in bronze armour rises from the last of them, picking up a
         sword as long as a cart.""",
         'mobs': [('bone_giant', 1), ('tomb_crawler', 1)]},
        {'id': 'mound_avenue', 'name': 'The Avenue of Stones', 'sector': 'hills',
         'desc': """A double row of standing stones leads west across the downs toward the Great
         Mound, each stone carved with a face.  The faces have been worn by wind and
         rain to blank ovals, but as you walk between them you feel them turn to
         watch you pass.""",
         'exits': {'w': 'great_mound'},
         'mobs': [('barrow_wight', 2), ('stone_watcher', 1)]},
        {'id': 'great_mound', 'name': 'Before the Great Mound', 'sector': 'hills',
         'desc': """The Great Mound rises before you, a hill made by hands, ringed by three circles
         of stones.  Its great stone door has been pushed outward from within and lies
         flat on the grass.  Grey light pours from the opening, and with it a cold that
         freezes the breath in your throat.""",
         'exits': {'d': 'kings_passage', 'w': 'west_ridge'},
         'mobs': [('barrow_lord_guard', 2)]},
        {'id': 'kings_passage', 'name': 'The King\'s Passage', 'sector': 'inside', 'flags': 'd',
         'desc': """A long passage of carved stone runs down into the heart of the mound, its walls
         lined with the bones of servants, horses and hounds buried to serve the king
         in death.  They are all awake.  They all turn toward you.""",
         'exits': {'d': 'kings_chamber'},
         'mobs': [('barrow_lord_guard', 2), ('tomb_crawler', 1)]},
        {'id': 'kings_chamber', 'name': 'The Chamber of the Barrow King', 'sector': 'inside', 'flags': 'd',
         'desc': """A great domed chamber at the heart of the mound, heaped with gold and bronze
         and bone.  On a throne of stone sits the Barrow King, first lord of the
         hill-folk, dead three thousand years.  Grey fire burns in his eye sockets.  He
         has heard the voice from the West, and he has answered it.""",
         'mobs': [('barrow_king', 1)]},
        {'id': 'west_ridge', 'name': 'The Western Ridge', 'sector': 'hills',
         'desc': """The barrow hills end at a long ridge.  Below it, a great river winds through a
         ruined valley, crossed by a broken bridge.  On the near bank stand the walls of
         a fortress, and from its single tower a banner still flies, faded but
         defiant.""",
         'mobs': [('barrow_wight', 1)]},
    ],
    'mobs': [
        {'id': 'barrow_wight', 'aliases': 'wight barrow', 'short': 'a barrow wight', 'role': 'standard', 'level': 52,
         'long': 'A barrow wight in rotted burial finery stalks between the mounds.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'An ancient dead noble of the hill-folk, gold torcs on its withered neck, grey fire in its eyes.'},
        {'id': 'tomb_crawler', 'aliases': 'crawler tomb', 'short': 'a tomb crawler', 'role': 'standard', 'level': 51,
         'long': 'A many-legged thing of bone and grave-wax crawls along the ceiling.', 'flags': 'f', 'align': -800, 'attack': 'bite',
         'desc': 'Made from the bones of a dozen burial-servants, fused together into something that scuttles.'},
        {'id': 'ghoul_pack', 'aliases': 'ghoul ghouls pack', 'short': 'a pack of hill ghouls', 'role': 'standard', 'level': 52,
         'long': 'A pack of pale ghouls lopes toward you on all fours.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Naked, hairless and grey, they hunt like wolves and their claws carry a numbing rot.'},
        {'id': 'cursed_robber', 'aliases': 'robber cursed grave', 'short': 'a cursed grave robber', 'role': 'standard', 'level': 53,
         'long': 'A grave robber with grey skin digs frantically with bleeding hands.', 'flags': 'f', 'align': -700, 'sex': 1,
         'desc': 'He came to loot the barrows. The barrows took him instead. He digs forever now, searching for something he cannot remember.',
         'equip': [('robbers_pick', 'wield', 80)]},
        {'id': 'spiral_queen', 'aliases': 'queen spiral mummy', 'short': 'the Spiral Queen', 'role': 'champion', 'level': 54,
         'long': 'A jewelled mummy sits on the edge of her coffin, combing her hair.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'A queen of the hill-folk, buried with a hundred servants. She remembers everything, and she is lonely, and she would like you to stay forever.',
         'equip': [('spiral_circlet', 'head', 100)], 'carry': [('queen_torc', 100)]},
        {'id': 'ghoul_patriarch', 'aliases': 'patriarch ghoul', 'short': 'the ghoul patriarch', 'role': 'champion', 'level': 54,
         'long': 'An enormous ghoul looks up from a thighbone, marrow dripping from its jaws.', 'flags': 'bfl', 'align': -1000, 'attack': 'claw',
         'desc': 'The father of every ghoul in the hills, swollen to the size of a bear on the dead of three thousand years.',
         'carry': [('ghoul_claw', 100)]},
        {'id': 'vigil_monk', 'aliases': 'monk vigil', 'short': 'a vigil monk', 'role': 'elite', 'level': 54,
         'long': 'A monk in grey chants steadily, a torch in one hand and a staff in the other.', 'flags': 'bm', 'align': 900, 'sex': 1,
         'desc': 'The monks keep the vigil in shifts. If the chant stops, the walls will not hold.',
         'equip': [('vigil_staff', 'wield', 100)]},
        {'id': 'hill_refugee', 'aliases': 'refugee hill', 'short': 'a refugee from the hills', 'role': 'harmless', 'level': 50,
         'long': 'A refugee from the hills huddles against the wall.', 'flags': 'b', 'align': 400,
         'desc': 'Shepherds and farmers from the hill villages, sheltered here when the barrows opened.'},
        {'id': 'flame_keeper', 'aliases': 'keeper flame', 'short': 'the keeper of the flame', 'role': 'champion', 'level': 55,
         'long': 'An old monk kneels before the flame, feeding it with prayer.', 'flags': 'b', 'align': 1000, 'sex': 1,
         'desc': 'He has knelt here for sixty years. The flame lives on his prayer, and he is very tired.',
         'carry': [('flame_candle', 100)]},
        {'id': 'refectory_brother', 'aliases': 'brother reader monk', 'short': 'the reading brother', 'role': 'harmless', 'level': 52,
         'long': 'A monk reads names aloud from a lectern.', 'flags': 'b', 'align': 800, 'sex': 1,
         'desc': 'Every name must be read so the dead remember who they were. If they remember, they rest.',
         'carry': [('barley_bread', 100)]},
        {'id': 'lamp_tender', 'aliases': 'tender lamp monk', 'short': 'the lamp tender', 'role': 'harmless', 'level': 52,
         'long': 'An old monk refills the grave lamps with careful hands.', 'flags': 'b', 'align': 900, 'sex': 1,
         'desc': 'He has lost count of the lamps. He has not lost count of the ones that went out.'},
        {'id': 'archivist_monk', 'aliases': 'archivist monk', 'short': 'the archivist', 'role': 'harmless', 'level': 53,
         'long': 'A monk copies a scroll in desperate haste.', 'flags': 'b', 'align': 800, 'sex': 1,
         'desc': 'Ink to the elbows. He is trying to copy every rite before the library burns, because he is sure that it will.',
         'carry': [('rite_scroll', 100)]},
        {'id': 'abbess_ulla', 'aliases': 'abbess', 'short': 'the Abbess of the Flame', 'role': 'champion', 'level': 55,
         'long': 'The Abbess stands at the window, watching the grey light in the west.', 'flags': 'b', 'align': 1000, 'sex': 2,
         'desc': 'A hard-faced woman in grey with a soldier\'s bearing. She was a knight before she was a monk. She knows the King beneath the Great Mound will come for the flame, and she means to meet him at the door.',
         'equip': [('abbess_mace', 'wield', 100)]},
        {'id': 'barrow_guardian', 'aliases': 'guardian barrow', 'short': 'a barrow guardian', 'role': 'elite', 'level': 55,
         'long': 'A huge skeleton in bronze stands in the barrow door, spear raised.', 'flags': 'bf', 'align': -900,
         'desc': 'A champion\'s bodyguard, buried at the door of his tomb. He has guarded it for three thousand years.',
         'equip': [('bronze_spear', 'wield', 100)]},
        {'id': 'bone_giant', 'aliases': 'giant bone', 'short': 'a bone giant', 'role': 'champion', 'level': 55,
         'long': 'A giant skeleton in bronze armour rises, a cart-length sword in its hands.', 'flags': 'bfl', 'align': -1000, 'attack': 'crush',
         'desc': 'A champion of the hill-folk, twice a man\'s height in life, and no smaller in death.',
         'carry': [('giant_bracer', 100)]},
        {'id': 'stone_watcher', 'aliases': 'watcher stone', 'short': 'a stone watcher', 'role': 'elite', 'level': 54,
         'long': 'A standing stone turns its blank face toward you and steps out of line.', 'flags': 'f', 'align': -700, 'attack': 'crush',
         'desc': 'The stones of the avenue guard the way to the king. The grey light has woken them.'},
        {'id': 'barrow_lord_guard', 'aliases': 'guard barrow lord', 'short': 'a barrow lord\'s huscarl', 'role': 'elite', 'level': 55,
         'long': 'A dead huscarl in a bronze mask raises an axe.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'The king\'s sworn warriors, buried with him to fight for him in death. They keep their oath.',
         'equip': [('bronze_axe', 'wield', 80)]},
        {'id': 'barrow_king', 'aliases': 'king barrow', 'short': 'the Barrow King', 'role': 'boss', 'level': 55,
         'long': 'The Barrow King rises from his stone throne, grey fire blazing in his eyes.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'First lord of the hill-folk, three thousand years dead, a tall withered shape in gold and bronze. In life he made the spiral the sign of his people. In death he has heard Nu\'Groth\'s voice and found it familiar, and he means to lead every dead thing in the hills against the monastery\'s flame.',
         'equip': [('barrow_crown', 'head', 100), ('kings_bronze_blade', 'wield', 100)], 'carry': [('kings_torc', 100)]},
    ],
    'objs': [
        {'id': 'monastery_well', 'kind': 'fountain', 'aliases': 'well', 'short': 'the monastery well',
         'long': 'A stone well stands in the courtyard.', 'liquid': 0},
        {'id': 'robbers_pick', 'kind': 'weapon', 'level': 52, 'attack': 'pierce', 'aliases': 'pick robber',
         'short': 'a grave robber\'s pick', 'long': 'A heavy pick lies here.'},
        {'id': 'spiral_circlet', 'kind': 'armor', 'slot': 'head', 'level': 55, 'aliases': 'circlet spiral gold',
         'short': 'a gold spiral circlet', 'long': 'A circlet of gold spirals lies here.', 'affects': [('int', 1), ('wis', 1), ('mana', 40)]},
        {'id': 'queen_torc', 'kind': 'worn', 'slot': 'neck', 'level': 55, 'aliases': 'torc queen gold',
         'short': 'a queen\'s gold torc', 'long': 'A heavy gold torc lies here.', 'affects': [('cha', 2), ('save_spell', -3)]},
        {'id': 'ghoul_claw', 'kind': 'weapon', 'level': 55, 'attack': 'claw', 'aliases': 'claw ghoul',
         'short': 'a ghoul patriarch\'s claw', 'long': 'A huge grey claw lies here.', 'affects': [('damroll', 3)]},
        {'id': 'vigil_staff', 'kind': 'weapon', 'level': 54, 'attack': 'bludgeon', 'aliases': 'staff vigil',
         'short': 'a vigil staff', 'long': 'An iron-shod staff lies here.', 'extra': 'i'},
        {'id': 'flame_candle', 'kind': 'light', 'level': 55, 'hours': -1, 'aliases': 'candle flame white',
         'short': 'a candle lit from the flame', 'long': 'A white candle burns here without melting.', 'extra': 'a',
         'affects': [('save_spell', -2)]},
        {'id': 'barley_bread', 'kind': 'food', 'hours': 12, 'aliases': 'bread barley', 'short': 'a loaf of barley bread',
         'long': 'A loaf of barley bread lies here.', 'weight': 1, 'cost': 10},
        {'id': 'rite_scroll', 'kind': 'note', 'aliases': 'scroll rite', 'short': 'a scroll of burial rites',
         'long': 'A scroll of burial rites lies here.', 'weight': 1,
         'extras': {'scroll rite': 'Rites to keep the dead asleep, copied in haste. The last line: NONE OF THIS WORKS ANY MORE.'}},
        {'id': 'abbess_mace', 'kind': 'weapon', 'level': 56, 'attack': 'bludgeon', 'aliases': 'mace abbess',
         'short': 'the Abbess\'s mace', 'long': 'A plain steel mace lies here.', 'extra': 'i', 'affects': [('hitroll', 3), ('damroll', 2)]},
        {'id': 'bronze_spear', 'kind': 'weapon', 'level': 55, 'attack': 'pierce', 'aliases': 'spear bronze',
         'short': 'a bronze spear', 'long': 'An ancient bronze spear lies here.'},
        {'id': 'giant_bracer', 'kind': 'armor', 'slot': 'wrist', 'level': 56, 'aliases': 'bracer giant bronze',
         'short': 'a giant\'s bronze bracer', 'long': 'An enormous bronze bracer lies here.', 'affects': [('str', 2), ('hit', 20)]},
        {'id': 'bronze_axe', 'kind': 'weapon', 'level': 55, 'attack': 'slash', 'aliases': 'axe bronze',
         'short': 'a bronze huscarl axe', 'long': 'A bronze axe lies here.', 'affects': [('damroll', 1)]},
        {'id': 'barrow_crown', 'kind': 'armor', 'slot': 'head', 'level': 57, 'aliases': 'crown barrow gold',
         'short': 'the Barrow King\'s crown', 'long': 'A crown of gold spirals, cold as ice, lies here.', 'affects': [('hit', 45), ('wis', 2), ('save_spell', -3)]},
        {'id': 'kings_bronze_blade', 'kind': 'weapon', 'level': 57, 'attack': 'slash', 'aliases': 'blade bronze king',
         'short': 'the Barrow King\'s blade', 'long': 'A long bronze sword patterned with spirals lies here.', 'affects': [('hitroll', 4), ('damroll', 4)]},
        {'id': 'kings_torc', 'kind': 'worn', 'slot': 'neck', 'level': 56, 'aliases': 'torc king',
         'short': 'the king\'s torc', 'long': 'A massive gold torc lies here.', 'affects': [('con', 2), ('str', 1)]},
    ],
}
