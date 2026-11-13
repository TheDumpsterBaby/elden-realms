"""The Ironworks -- support ring, levels 8-15.

Forges and armouries south of Midgaard's east gate, running day and night to
arm the wall. The work is done by conscripted refugees under a cruel overseer,
and the ore comes from a mine that has broken into something hot and alive.
"""

ZONE = {
    'num': 62, 'name': 'The Ironworks', 'builders': 'Claude', 'lifespan': 15,
    'rooms': [
        {'id': 'road', 'name': 'The Cinder Road', 'sector': 'field',
         'desc': """A road paved with cinders and slag runs south from Midgaard's east gate.
         The ground is black and the air tastes of iron.  Ahead, chimneys belch
         smoke into a sky that never clears, and the ringing of a hundred hammers
         never stops, day or night.""",
         'exits': {'n': {'to': '@3053', 'back_desc': 'A cinder road leads south toward the Ironworks.'}, 's': 'gate'},
         'mobs': [('ore_carter', 1)]},
        {'id': 'gate', 'name': 'The Ironworks Gate', 'sector': 'city',
         'desc': """A gate of riveted iron plates stands in a wall of blackened brick.  Soldiers
         check everyone who enters, and everyone who leaves is searched, because
         every nail and buckle belongs to the war.  A board lists the quota:
         FIVE HUNDRED BLADES BY THE NEW MOON.""",
         'exits': {'s': 'yard'},
         'mobs': [('gate_guard', 2)]},
        {'id': 'yard', 'name': 'The Forge Yard', 'sector': 'city',
         'desc': """A wide yard of packed cinders between long brick forge-halls.  Barrows of
         ore and coal rumble past, pushed by thin men and women in chains.  Finished
         blades are stacked in racks to cool, and a wagon is being loaded with them
         for the wall.""",
         'exits': {'w': 'great_forge', 'e': 'armoury', 's': 'slag_lane', 'n': 'gate'},
         'mobs': [('conscript_labourer', 3), ('yard_overseer', 1)]},
        {'id': 'great_forge', 'name': 'The Great Forge', 'sector': 'inside', 'flags': 'd',
         'desc': """A hall of a dozen forges, each with its smith, each with its anvil ringing.
         The heat is a wall that stops your breath.  Sparks fly in sheets.  The
         smiths work stripped to the waist and burned all over, and none of them
         looks up from the steel.""",
         'exits': {'w': 'bellows', 'n': 'quench'},
         'mobs': [('smith', 3)]},
        {'id': 'bellows', 'name': 'The Bellows House', 'sector': 'inside', 'flags': 'd',
         'desc': """Great leather bellows, each as big as a cart, breathe air into the forges
         through clay pipes.  They are worked by conscripts walking in a treadwheel,
         round and round, hour after hour.  A man in the wheel stumbles and the
         overseer's whip cracks.""",
         'mobs': [('conscript_labourer', 2), ('whip_overseer', 1)]},
        {'id': 'quench', 'name': 'The Quenching Pools', 'sector': 'inside', 'flags': 'd',
         'desc': """Long stone troughs of oily water hiss and steam as glowing steel is plunged
         into them.  The water is black and scummed.  A tired apprentice fishes in it
         with tongs for a blade someone dropped, and comes up with something that is
         not a blade.""",
         'objs': [('quench_trough', 1)],
         'mobs': [('apprentice', 1)]},
        {'id': 'armoury', 'name': 'The Armoury', 'sector': 'inside', 'flags': 'd',
         'desc': """Racks of spears, swords, helms and shields fill a long hall, every piece
         stamped with Midgaard's tower.  Clerks count and recount them.  The
         armourer inspects each item and throws one in five on a pile of rejects;
         the rejects go to the wall anyway.""",
         'exits': {'e': 'weaponsmith', 's': 'office'},
         'mobs': [('armourer', 1), ('armoury_clerk', 1)]},
        {'id': 'weaponsmith', 'name': "The Master Weaponsmith's Workshop", 'sector': 'inside', 'flags': 'd',
         'desc': """A quieter room with a single forge, where the finest blades are made for
         officers and champions.  Tools hang in perfect order.  The master
         weaponsmith works slowly, folding steel, and every blade she makes has a
         name engraved on it before it leaves.""",
         'mobs': [('master_weaponsmith', 1)]},
        {'id': 'office', 'name': "The Overseer's Office", 'sector': 'inside', 'flags': 'd',
         'desc': """A brick room with barred windows overlooking the yard.  A desk holds the
         quota ledgers and the conscript rolls, with deaths marked in a neat column.
         A whip hangs on the wall beside a portrait of the overseer himself, in a
         uniform he never earned.""",
         'extras': {'rolls ledger deaths': 'Conscript rolls. Name, village, date taken, date died. The second date is filled in for nearly half the names.'},
         'mobs': [('chief_overseer', 1)]},
        {'id': 'slag_lane', 'name': 'Slag Lane', 'sector': 'city',
         'desc': """A lane between the forge-halls and a mountain of cooling slag that smokes
         and crackles.  The heat comes off it in waves.  The lane leads south toward
         the conscripts' huts and west toward the coal yard and the mine head.""",
         'exits': {'s': 'huts', 'w': 'coal_yard', 'e': 'slag_heap'}},
        {'id': 'slag_heap', 'name': 'On the Slag Heap', 'sector': 'hills',
         'desc': """You climb the slope of glassy black slag.  It is warm underfoot and in
         places glows dull red beneath the crust.  Scavengers pick through it for
         scraps of iron.  Near the top something has burrowed into the slag,
         leaving a hole that breathes heat.""",
         'mobs': [('slag_scavenger', 2), ('cinder_beetle', 2)]},
        {'id': 'huts', 'name': "The Conscripts' Huts", 'sector': 'city',
         'desc': """Rows of low turf huts, each holding twenty conscripts in a space for five.
         Refugees from the camps, taken for the work because they were strong
         enough to stand.  They sleep in their chains.  Some of them never wake,
         and the carts come for those each morning.""",
         'exits': {'e': 'hut_inside'},
         'mobs': [('conscript_labourer', 2)]},
        {'id': 'hut_inside', 'name': 'Inside a Conscript Hut', 'sector': 'inside', 'flags': 'd',
         'desc': """Darkness, the smell of unwashed bodies, and quiet voices that stop when you
         enter.  Someone has scratched a map of the Ironworks on the turf wall, with
         the guard posts marked and a route out drawn in charcoal.  They are
         planning to run, and they are watching to see what you will do.""",
         'extras': {'map wall charcoal': 'A careful map of the Ironworks. The route out runs through the mine, where the guards will not go any more.'},
         'mobs': [('conscript_ringleader', 1)]},
        {'id': 'coal_yard', 'name': 'The Coal Yard', 'sector': 'city',
         'desc': """Black hills of coal and charcoal fill a fenced yard, and black dust coats
         everything.  Conscripts shovel it into barrows with black faces and black
         hands, coughing black.  At the west end of the yard stands the wooden
         headframe of the mine.""",
         'exits': {'w': 'mine_head'},
         'mobs': [('conscript_labourer', 2)]},
        {'id': 'mine_head', 'name': 'The Mine Head', 'sector': 'city',
         'desc': """A great wheel of timber turns above the shaft, winding the cage up and down
         on a creaking rope.  A ladder runs down beside it.  The guards here stand
         well back from the shaft, and a fresh notice is nailed to the headframe:
         NO DESCENT BELOW THE THIRD LEVEL.""",
         'exits': {'d': 'mine_level1'},
         'mobs': [('mine_guard', 1)]},
        {'id': 'mine_level1', 'name': 'The First Level', 'sector': 'inside', 'flags': 'ad',
         'desc': """A gallery cut through dark rock, lit by smoking lamps.  Rails run along the
         floor for the ore carts.  Picks ring in side tunnels.  The rock is warm to
         the touch, much warmer than rock should be this close to the surface.""",
         'exits': {'d': 'mine_level2', 'e': 'side_drift'},
         'mobs': [('miner', 2)]},
        {'id': 'side_drift', 'name': 'An Abandoned Drift', 'sector': 'inside', 'flags': 'ad',
         'desc': """A side tunnel where the work stopped suddenly: tools dropped, a lamp still
         on its hook, a half-filled cart on the rails.  Scorch marks streak the walls
         as though something burning ran along them.  There are no bodies, only
         ash in the shape of men.""",
         'mobs': [('cinder_beetle', 2)]},
        {'id': 'mine_level2', 'name': 'The Second Level', 'sector': 'inside', 'flags': 'ad',
         'desc': """The heat is oppressive now and sweat runs into your eyes.  The rock here is
         veined with red that pulses slowly, like a heartbeat.  The miners on this
         level work in silence, quickly, glancing constantly at the shaft that leads
         further down.""",
         'exits': {'d': 'mine_level3'},
         'mobs': [('miner', 2), ('ash_wraith', 1)]},
        {'id': 'mine_level3', 'name': 'The Third Level', 'sector': 'inside', 'flags': 'ad',
         'desc': """The lowest working level.  Beyond a barricade of beams and carts, a passage
         leads on downward, glowing orange.  Burned handprints cover the barricade.
         Something on the other side has tried to get through it, and from the heat
         pouring over the top, it is still there.""",
         'exits': {'d': {'to': 'forge_cavern', 'door': 'barricade', 'state': 'closed',
                         'desc': 'A barricade of charred beams, wedged shut.'}},
         'mobs': [('ash_wraith', 2)]},
        {'id': 'forge_cavern', 'name': 'The Living Forge', 'sector': 'inside', 'flags': 'd',
         'desc': """A vast cavern where the rock has melted into lakes of glowing slag.  The
         miners broke into it chasing a rich seam of ore, and the seam was the edge
         of something.  In the heart of the cavern a shape of molten iron and black
         slag rises from the lake, shedding fire, and turns toward you.""",
         'mobs': [('molten_hulk', 1), ('cinder_beetle', 2)]},
    ],
    'mobs': [
        {'id': 'ore_carter', 'aliases': 'carter ore', 'short': 'an ore carter', 'role': 'harmless', 'level': 8,
         'long': 'An ore carter drives a creaking wagon toward the gate.', 'flags': 'g', 'align': 200, 'sex': 1,
         'desc': 'Black dust in every line of his face.'},
        {'id': 'gate_guard', 'aliases': 'guard gate soldier', 'short': 'an ironworks guard', 'role': 'standard', 'level': 12,
         'long': 'An ironworks guard searches a conscript at the gate.', 'flags': 'bm', 'align': 100, 'sex': 1,
         'desc': 'Thorough, unsmiling, and armed with a fresh-forged spear.',
         'equip': [('fresh_spear', 'wield', 100), ('iron_cap', 'head', 40)]},
        {'id': 'conscript_labourer', 'aliases': 'conscript labourer laborer', 'short': 'a chained conscript', 'role': 'harmless', 'level': 8,
         'long': 'A chained conscript pushes a barrow of ore, head down.', 'flags': 'g', 'align': 300,
         'desc': 'Taken from the camps because they could still stand. They will work until they cannot.'},
        {'id': 'yard_overseer', 'aliases': 'overseer yard', 'short': 'a yard overseer', 'role': 'standard', 'level': 13,
         'long': 'A yard overseer counts barrows, a cudgel tapping his leg.', 'flags': 'fg', 'align': -300, 'sex': 1,
         'desc': 'He hits the slow ones and the fast ones alike. It keeps them guessing.',
         'equip': [('overseer_cudgel', 'wield', 100)]},
        {'id': 'smith', 'aliases': 'smith blacksmith', 'short': 'a forge smith', 'role': 'standard', 'level': 12,
         'long': 'A forge smith hammers a glowing blade, sweat steaming off him.', 'flags': 'b', 'align': 200, 'sex': 1,
         'desc': 'Arms like oak and burns all over. He has made a thousand blades this year and will make a thousand more.',
         'equip': [('smith_hammer', 'wield', 100)]},
        {'id': 'whip_overseer', 'aliases': 'overseer whip', 'short': 'the treadwheel overseer', 'role': 'elite', 'level': 14,
         'long': 'An overseer cracks a whip at the conscripts in the treadwheel.', 'flags': 'bf', 'align': -500, 'sex': 2,
         'desc': 'She enjoys it. That is the worst part.',
         'equip': [('barbed_whip', 'wield', 100)]},
        {'id': 'apprentice', 'aliases': 'apprentice boy', 'short': 'a forge apprentice', 'role': 'harmless', 'level': 9,
         'long': 'An apprentice fishes in the quench trough with long tongs.', 'flags': 'b', 'align': 300, 'sex': 1,
         'desc': 'Twelve years old, burned on both arms, and proud of every scar.'},
        {'id': 'armourer', 'aliases': 'armourer armorer', 'short': 'the armourer', 'role': 'elite', 'level': 14,
         'long': 'The armourer turns a helm over in her hands, frowning at a flaw.', 'flags': 'b', 'align': 300, 'sex': 2,
         'desc': 'She knows every flaw in every piece that leaves this hall, and she knows that a flawed shield is better than none.'},
        {'id': 'armoury_clerk', 'aliases': 'clerk armoury', 'short': 'an armoury clerk', 'role': 'harmless', 'level': 9,
         'long': 'An armoury clerk counts spears with a weary sigh.', 'flags': 'b', 'align': 100, 'sex': 1,
         'desc': 'Four hundred and twelve. Four hundred and thirteen.'},
        {'id': 'master_weaponsmith', 'aliases': 'weaponsmith master', 'short': 'the master weaponsmith', 'role': 'champion', 'level': 14,
         'long': 'The master weaponsmith folds glowing steel with slow, perfect strokes.', 'flags': 'b', 'align': 500, 'sex': 2,
         'desc': 'Grey-haired and steady-handed, the finest smith in the realm. She names every blade after a soldier who fell on the wall, so they will be remembered in steel.',
         'equip': [('named_blade', 'wield', 100)]},
        {'id': 'chief_overseer', 'aliases': 'overseer chief', 'short': 'the chief overseer', 'role': 'champion', 'level': 13,
         'long': 'The chief overseer looks up from his ledgers with small, cold eyes.', 'flags': 'bl', 'align': -700, 'sex': 1,
         'desc': 'A soft, pale man in a borrowed uniform who has never been near the wall. He meets his quotas by working conscripts to death, and he is praised for it.',
         'equip': [('overseer_cudgel', 'wield', 100), ('quilted_coat', 'body', 100)], 'carry': [('chain_key', 100)]},
        {'id': 'slag_scavenger', 'aliases': 'scavenger slag', 'short': 'a slag scavenger', 'role': 'standard', 'level': 10,
         'long': 'A ragged scavenger digs through the slag with burned hands.', 'flags': 'f', 'align': -200,
         'desc': 'Too sick for the forges and too stubborn to die. She will fight you for a nail.',
         'equip': [('slag_pick', 'wield', 70)]},
        {'id': 'cinder_beetle', 'aliases': 'beetle cinder', 'short': 'a cinder beetle', 'role': 'standard', 'level': 12,
         'long': 'A beetle the size of a dog scuttles over the slag, its shell glowing red.', 'flags': 'f', 'align': -300, 'attack': 'bite',
         'desc': 'Its shell is a crust of cooling slag over a body of embers. It came up out of the mine, and there are more every week.'},
        {'id': 'conscript_ringleader', 'aliases': 'ringleader conscript', 'short': 'the conscript ringleader', 'role': 'elite', 'level': 13,
         'long': 'A lean woman in chains watches you from the dark, a sharpened bar in her hand.', 'flags': 'b', 'align': 400, 'sex': 2,
         'desc': 'She was a captain of militia in a village in the west. She will lead her people out of here or die trying.',
         'equip': [('sharpened_bar', 'wield', 100)]},
        {'id': 'mine_guard', 'aliases': 'guard mine', 'short': 'a mine guard', 'role': 'standard', 'level': 13,
         'long': 'A mine guard stands well back from the shaft.', 'flags': 'b', 'align': 100, 'sex': 1,
         'desc': 'He used to go down with the miners. He does not any more.',
         'equip': [('fresh_spear', 'wield', 100)]},
        {'id': 'miner', 'aliases': 'miner', 'short': 'a sweating miner', 'role': 'standard', 'level': 11,
         'long': 'A miner swings a pick at the warm rock.', 'flags': 'g', 'align': 100, 'sex': 1,
         'desc': 'Soaked in sweat, nervous, quick to swing his pick at anything that moves.',
         'equip': [('slag_pick', 'wield', 100)]},
        {'id': 'ash_wraith', 'aliases': 'wraith ash', 'short': 'an ash wraith', 'role': 'elite', 'level': 15,
         'long': 'A shape of drifting ash and embers rises in the shape of a man.', 'flags': 'f', 'align': -800, 'attack': 'blast',
         'desc': 'All that is left of a miner who met what lives below. It still carries the outline of a pick.'},
        {'id': 'molten_hulk', 'aliases': 'hulk molten slag', 'short': 'the Molten Hulk', 'role': 'champion', 'level': 15,
         'long': 'A towering shape of molten iron and black slag rises from the glowing lake.', 'flags': 'bfl', 'align': -900, 'attack': 'crush',
         'desc': 'The living heart of the forge beneath the earth, woken by the miners\' picks. It knows the West is coming, and it is eager to help it melt the fort\'s walls.',
         'carry': [('heartstone', 100), ('molten_maul', 100)]},
    ],
    'objs': [
        {'id': 'quench_trough', 'kind': 'container', 'fixed': True, 'capacity': 0, 'aliases': 'trough troughs quench',
         'short': 'a quenching trough', 'long': 'A long stone quenching trough steams here.'},
        {'id': 'fresh_spear', 'kind': 'weapon', 'level': 12, 'attack': 'pierce', 'aliases': 'spear fresh iron',
         'short': 'a freshly forged spear', 'long': 'A freshly forged iron spear lies here.'},
        {'id': 'iron_cap', 'kind': 'armor', 'slot': 'head', 'level': 12, 'aliases': 'cap iron helm',
         'short': 'an iron cap', 'long': 'A plain iron cap lies here.'},
        {'id': 'overseer_cudgel', 'kind': 'weapon', 'level': 13, 'attack': 'bludgeon', 'aliases': 'cudgel iron-shod',
         'short': 'an iron-shod cudgel', 'long': 'An iron-shod cudgel lies here.'},
        {'id': 'smith_hammer', 'kind': 'weapon', 'level': 12, 'attack': 'pound', 'aliases': 'hammer smith',
         'short': "a smith's hammer", 'long': "A heavy smith's hammer lies here."},
        {'id': 'barbed_whip', 'kind': 'weapon', 'level': 14, 'attack': 'whip', 'aliases': 'whip barbed',
         'short': 'a barbed whip', 'long': 'A whip with iron barbs lies coiled here.', 'affects': [('hitroll', 1)]},
        {'id': 'named_blade', 'kind': 'weapon', 'level': 16, 'attack': 'slash', 'aliases': 'blade sword named',
         'short': 'a named blade', 'long': 'A fine sword with a name engraved on it lies here.',
         'affects': [('hitroll', 2), ('damroll', 1)],
         'extras': {'name engraved blade': 'Engraved along the fuller: FOR ROSIN OF THE THIRD COMPANY, WHO HELD THE GATE.'}},
        {'id': 'quilted_coat', 'kind': 'armor', 'slot': 'body', 'level': 13, 'aliases': 'coat quilted',
         'short': 'a quilted officer\'s coat', 'long': 'A quilted coat with brass buttons lies here.'},
        {'id': 'chain_key', 'kind': 'key', 'aliases': 'key chain', 'short': 'a key to the conscripts\' chains',
         'long': 'A small iron key lies here.', 'weight': 1},
        {'id': 'slag_pick', 'kind': 'weapon', 'level': 11, 'attack': 'pierce', 'aliases': 'pick mining',
         'short': 'a mining pick', 'long': 'A mining pick lies here.'},
        {'id': 'sharpened_bar', 'kind': 'weapon', 'level': 13, 'attack': 'pierce', 'aliases': 'bar sharpened iron',
         'short': 'a sharpened iron bar', 'long': 'An iron bar ground to a point lies here.'},
        {'id': 'heartstone', 'kind': 'worn', 'slot': 'hold', 'level': 15, 'aliases': 'heartstone stone heart',
         'short': 'a heartstone', 'long': 'A fist-sized stone glowing with inner heat lies here.',
         'affects': [('str', 1), ('hit', 20), ('damroll', 1)]},
        {'id': 'molten_maul', 'kind': 'weapon', 'level': 16, 'attack': 'crush', 'aliases': 'maul molten black', 'two_handed': True,
         'short': 'a maul of black slag', 'long': 'A heavy maul of black slag, still warm, lies here.',
         'affects': [('damroll', 2), ('hitroll', 1)]},
    ],
}
