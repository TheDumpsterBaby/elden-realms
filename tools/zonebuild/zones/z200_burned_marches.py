"""W1 The Burned Marches -- the March, levels 30-35.

Farmland beyond Midgaard's west gate, torched in the first raids. A chain of
three watchtowers still holds (the stronghold), but between them the Hollowed
-- people emptied out by the darkness -- wander the ashes, and raiders in the
Nu\'Groth\'s service camp in the ruins of Ashford.
"""

ZONE = {
    'num': 200, 'name': 'The Burned Marches', 'builders': 'Claude', 'lifespan': 20,
    'room_descs': {
        3052: """You stand outside Midgaard's west gate, between two squat towers joined by
        a footbridge high above the heavy wooden doors.  Soldiers on the wall watch
        the west without blinking.  Beyond the gate the road runs out into the
        Burned Marches, a grey country of ash and blackened stubble that was
        farmland a year ago.  This is where the war begins.""",
    },
    'rooms': [
        {'id': 'road_gate', 'name': 'The West Road Beyond the Gate', 'sector': 'field',
         'desc': """The road leaves the shadow of the west gate and runs out across a plain of
         ash.  Burned fields stretch to the horizon on both sides, the stubble black
         and brittle.  A wooden sign hangs from a post, its paint blistered:
         MIDGAARD.  TURN BACK.""",
         'exits': {'e': {'to': '@3052', 'back_desc': 'The west road runs out into the Burned Marches.'}, 'w': 'road_ash'},
         'mobs': [('blight_crow', 2)]},
        {'id': 'road_ash', 'name': 'The West Road, Ash Plain', 'sector': 'field',
         'desc': """Ash drifts across the road like grey snow, piling against the stones of
         an old field wall.  Every step raises a cloud of it.  The wind carries a
         smell of burned grain and older, worse things, and somewhere a dog is
         howling.""",
         'exits': {'w': 'tower1_foot', 'n': 'field_n1', 's': 'field_s1'}},
        {'id': 'tower1_foot', 'name': 'The Foot of the First Watchtower', 'sector': 'field', 'flags': 'c',
         'desc': """A square stone tower stands beside the road, ringed by a ditch and a palisade
         of stakes.  Midgaard's grey banner hangs from its top.  Soldiers on the
         parapet watch every shadow on the plain, and the gate in the palisade
         opens only for the living.""",
         'exits': {'u': 'tower1_hall', 'w': 'road_mid'},
         'mobs': [('tower_watchman', 2)]},
        {'id': 'tower1_hall', 'name': 'The First Watchtower, Guardroom', 'sector': 'inside', 'flags': 'cde',
         'desc': """A low guardroom with arrow slits facing west, warm from a brazier.  Weapons
         hang ready on the walls.  Off-duty soldiers sleep in their armour on straw
         pallets, and a surgeon has set up a table in the corner for the wounded
         who make it back from the plain.""",
         'exits': {'u': 'tower1_top'},
         'objs': [('water_barrel', 1)],
         'mobs': [('tower_surgeon', 1), ('tower_watchman', 1)]},
        {'id': 'tower1_top', 'name': 'The First Watchtower, Parapet', 'sector': 'inside', 'flags': 'ce',
         'desc': """The wind tears at you on the tower top.  From here you can see the other two
         towers marching west along the road, the black ruins of Ashford to the
         south, and beyond everything a dark line of forest on the western horizon.
         Signal fires stand ready in iron baskets.""",
         'extras': {'forest horizon line': 'The Hollow Wood. The watchmen say it has gone quiet. Nothing has come out of it for weeks, and that frightens them more than raiders do.'},
         'mobs': [('tower_captain', 1)]},
        {'id': 'field_n1', 'name': 'Burned Fields North of the Road', 'sector': 'field',
         'desc': """Charred stubble crunches underfoot.  A plough lies abandoned in a furrow,
         its handles burned away.  Here and there a figure stands motionless in the
         middle of a field, facing west, and does not turn when you call to it.""",
         'exits': {'n': 'farmstead', 'w': 'field_n2'},
         'mobs': [('hollowed_villager', 2)]},
        {'id': 'farmstead', 'name': 'A Burned Farmstead', 'sector': 'field',
         'desc': """The walls of a farmhouse stand roofless around a yard of ash.  The well has
         been choked with rubble.  On the door, still hanging by one hinge, someone
         has carved the grey spiral of the Choir, and under it, in a child's hand,
         the word SORRY.""",
         'exits': {'w': 'barn_ruin'},
         'mobs': [('hollowed_villager', 1), ('carrion_hound', 2)]},
        {'id': 'barn_ruin', 'name': 'The Collapsed Barn', 'sector': 'field',
         'desc': """Fallen beams lie criss-crossed over the remains of the animals that were
         shut in when the barn burned.  The smell has never quite gone.  Something
         has been digging under the beams, and the digging is recent.""",
         'mobs': [('carrion_hound', 2), ('ash_ghoul', 1)]},
        {'id': 'field_n2', 'name': 'The Field of Scarecrows', 'sector': 'field',
         'desc': """The raiders have planted the dead of the farms on poles across this field,
         facing east toward Midgaard, as a message.  Crows have taken their eyes.
         The poles creak in the wind, and one of the dead is still moving.""",
         'exits': {'w': 'hanging_tree'},
         'mobs': [('blight_crow', 3), ('hollowed_militia', 1)]},
        {'id': 'hanging_tree', 'name': 'The Hanging Oak', 'sector': 'field',
         'desc': """A huge oak, the only tree for leagues that did not burn, stands alone on a
         rise.  Its branches are heavy with hanged men and women, villagers who
         refused to join the raiders.  The rope burns on the bark are deep.  The
         grass beneath it has turned grey.""",
         'exits': {'s': 'road_mid2'},
         'extras': {'oak tree hanged': 'Dozens of bodies. The newest wear Midgaard grey: a patrol that never came back.'},
         'mobs': [('hanged_wraith', 1)]},
        {'id': 'road_mid', 'name': 'The West Road, Between the Towers', 'sector': 'field',
         'desc': """The road runs straight between the first and second towers.  Patrols ride it
         twice a day, and the verges are littered with what they leave behind:
         broken arrows, a dead horse, a soldier's boot with the foot still in it.""",
         'exits': {'w': 'road_mid2', 's': 'ashford_lane'},
         'mobs': [('hollowed_militia', 2)]},
        {'id': 'road_mid2', 'name': 'The West Road, The Dead Patrol', 'sector': 'field',
         'desc': """A patrol died here.  Their bodies have been arranged around the road in a
         circle, kneeling, facing west, their hands bound behind them.  Their
         horses lie where they fell.  Ash has been rubbed into their eyes.""",
         'exits': {'w': 'tower2_foot'},
         'mobs': [('ash_ghoul', 2)]},
        {'id': 'tower2_foot', 'name': 'The Foot of the Second Watchtower', 'sector': 'field', 'flags': 'c',
         'desc': """The second tower is battered.  Its palisade has been burned and rebuilt,
         and scorch marks climb its walls.  The soldiers here are fewer and grimmer
         than at the first tower, and the ditch around it is full of raider
         bodies.""",
         'exits': {'u': 'tower2_hall', 'w': 'road_west'},
         'mobs': [('tower_watchman', 2)]},
        {'id': 'tower2_hall', 'name': 'The Second Watchtower, Barracks', 'sector': 'inside', 'flags': 'cde',
         'desc': """Bunks line the walls of a crowded room smelling of sweat and smoke.  A
         quartermaster hands out arrows and hard bread from a locked chest.  On the
         wall someone has kept a tally of raids, in groups of five scratched into
         the plaster.  There are a great many groups of five.""",
         'objs': [('water_barrel', 1)],
         'mobs': [('tower_quartermaster', 1)]},
        {'id': 'field_s1', 'name': 'The South Ditch', 'sector': 'field',
         'desc': """A drainage ditch runs south from the road, choked with ash and worse.
         Soldiers threw the dead of the first raids in here when there was no time
         to bury them.  The ditch is not as full as it was, and there are tracks
         leading out of it.""",
         'exits': {'s': 'ashford_gate'},
         'mobs': [('ash_ghoul', 2)]},
        {'id': 'ashford_lane', 'name': 'The Lane to Ashford', 'sector': 'field',
         'desc': """A lane runs south between burned hedges toward the black shell of a village.
         Wagon tracks in the ash lead into it, recent ones, heavy with loot.
         Smoke still rises from one of the chimneys, and it is not from a
         hearth.""",
         'exits': {}},
        {'id': 'ashford_gate', 'name': 'The East End of Ashford', 'sector': 'city',
         'desc': """The first houses of Ashford are blackened shells.  A child's cart lies
         overturned in the street, and a dog's skeleton is still chained to a
         doorpost.  The raiders' painted sign hangs over the road: a grey hand,
         open, palm out.""",
         'exits': {'w': 'ashford_square', 's': 'pen'},
         'mobs': [('raider', 2)]},
        {'id': 'ashford_square', 'name': 'Ashford Square', 'sector': 'city',
         'desc': """The village square is a ring of burned houses around a cracked fountain.
         The raiders have made it their camp: tents of stolen cloth, a cookfire,
         piles of loot.  The villagers who were not hanged or hollowed are kept in
         a pen of hurdles at the east end of the village.""",
         'exits': {'w': 'chapel_ashford', 's': 'mill_ashford', 'n': 'ashford_lane'},
         'objs': [('cracked_fountain', 1)],
         'mobs': [('raider', 3), ('raider_outrider', 1)]},
        {'id': 'pen', 'name': 'The Prisoners\' Pen', 'sector': 'city',
         'desc': """A pen of wattle hurdles holds a dozen villagers, filthy and silent.  The
         raiders feed them ash and water.  Every day one of them is taken to the
         chapel and comes back hollowed.  The ones left beg you, in whispers, to
         kill them before it is their turn.""",
         'mobs': [('captive_villager', 3), ('raider_jailer', 1)]},
        {'id': 'chapel_ashford', 'name': 'The Chapel of Ashford', 'sector': 'inside', 'flags': 'd',
         'desc': """The village chapel has been turned into something else.  The pews are
         gone, the altar painted grey, and a spiral of ash covers the floor.  At its
         centre is a chair with straps on the arms.  This is where the raiders'
         shaman empties people out.""",
         'exits': {'w': 'shaman_cell'},
         'mobs': [('raider_shaman', 1), ('hollowed_villager', 2)]},
        {'id': 'shaman_cell', 'name': 'The Sacristy', 'sector': 'inside', 'flags': 'ad',
         'desc': """A small dark room behind the altar.  Jars line the shelves, filled with a
         grey dust that stirs when you come near.  A book lies open on a table,
         written in a language that hurts to look at.  The shaman's bedroll lies in
         the corner beside a pile of children's shoes.""",
         'objs': [('ash_tome', 1)],
         'mobs': [('raider_shaman', 1)]},
        {'id': 'mill_ashford', 'name': 'The Burned Mill', 'sector': 'inside', 'flags': 'd',
         'desc': """The Ashford mill burned with the miller's family inside, and its great
         wheel stands still in a stream gone grey with ash.  The raiders use the
         ground floor as a storehouse.  Stairs climb to where the warlord has made
         his quarters.""",
         'exits': {'u': 'warlord_room', 'w': 'millstream'},
         'mobs': [('raider', 2)]},
        {'id': 'warlord_room', 'name': "The Warlord's Loft", 'sector': 'inside', 'flags': 'd',
         'desc': """Furs and stolen tapestries cover the floor of the mill loft.  A rack holds
         weapons taken from dead soldiers.  A crude map of the Marches is pinned to
         the wall, the watchtowers circled in charcoal and marked for burning.""",
         'extras': {'map charcoal towers': 'The three towers, each circled. Beside the second: SOON. Beside Midgaard: AFTER.'},
         'mobs': [('raider_warlord', 1)]},
        {'id': 'millstream', 'name': 'The Grey Millstream', 'sector': 'swim',
         'desc': """A stream that once turned the mill wheel runs thick and grey with ash.
         Bodies have caught against the sluice gate.  Downstream the water vanishes
         into a culvert under the road, and something large has been dragged
         through it recently.""",
         'exits': {'w': 'culvert'},
         'mobs': [('drowned_hollow', 2)]},
        {'id': 'culvert', 'name': 'The Culvert Beneath the Road', 'sector': 'inside', 'flags': 'ad',
         'desc': """A stone tunnel carries the stream under the road.  You wade through cold
         grey water in the dark.  Bones crunch underfoot.  Halfway through, a side
         passage has been dug into the earth, and it smells of a carrion den.""",
         'exits': {'n': 'hound_den', 'u': {'to': 'road_west', 'desc': 'Iron rungs set in the stone climb up to the bridge.'}},
         'mobs': [('carrion_hound', 2)]},
        {'id': 'hound_den', 'name': 'The Carrion Den', 'sector': 'inside', 'flags': 'ad',
         'desc': """A cave dug into the earth under the road, carpeted with bones and rotting
         hides.  The raiders' hounds breed here, gorging on the dead of the
         Marches.  They have grown huge on it, and the largest of them watches you
         from the back of the den with eyes like coals.""",
         'mobs': [('hound_alpha', 1), ('carrion_hound', 2)]},
        {'id': 'road_west', 'name': 'The West Road, Burned Crossing', 'sector': 'field',
         'desc': """The road crosses the grey stream on a bridge of scorched timber.  Below it,
         the culvert mouth gapes in the bank.  Ahead, the third and last watchtower
         stands on a mound, and beyond it the land darkens toward the forest.""",
         'exits': {'w': 'tower3_foot'},
         'mobs': [('hollowed_militia', 2), ('blight_crow', 2)]},
        {'id': 'tower3_foot', 'name': 'The Foot of the Last Watchtower', 'sector': 'hills', 'flags': 'c',
         'desc': """The last tower stands on a mound, the westernmost post of the Burned
         Marches.  Half its palisade is gone.  The garrison here is the smallest
         and the most scarred, and they have stopped counting the raids.  Beyond
         the mound, the road runs on into the dark of the Hollow Wood.""",
         'exits': {'u': 'tower3_hall', 'w': 'wood_edge', 's': 'reaver_trail'},
         'mobs': [('tower_watchman', 2)]},
        {'id': 'tower3_hall', 'name': 'The Last Watchtower, Command Room', 'sector': 'inside', 'flags': 'cde',
         'desc': """A cramped room at the top of the tower, maps on every wall.  The commander
         of the Marches sleeps here in a chair, when she sleeps at all.  A shrine to
         the fallen stands in the corner, its candles guttering, a pile of
         identity tags at its foot.""",
         'objs': [('water_barrel', 1)],
         'mobs': [('marches_commander', 1)]},
        {'id': 'wood_edge', 'name': 'Where the Marches Meet the Wood', 'sector': 'forest',
         'desc': """Burned stubble gives way to the first trees of the Hollow Wood.  They are
         black and leafless at the edge, scorched by the fires, but further in they
         are untouched and very still.  No birds sing.  The road runs on between
         them into the gloom.""",
         'mobs': [('hollowed_villager', 2)]},
        {'id': 'reaver_trail', 'name': 'The Reaver\'s Trail', 'sector': 'field',
         'desc': """A trail of ash and blood leads south from the tower mound across the burned
         fields, toward a ring of standing stones on a low hill.  Hollowed men
         stand along it like sentries, all facing the same way.  The raiders say
         the Reaver waits at the stones.""",
         'exits': {'s': 'stone_ring'},
         'mobs': [('hollowed_militia', 2)]},
        {'id': 'stone_ring', 'name': 'The Ring of Stones', 'sector': 'hills',
         'desc': """A ring of ancient standing stones crowns the hill, each stone smeared with
         grey ash in the shape of a spiral.  A bonfire of bones burns at the centre.
         The Reaver of Ashford stands beside it, the first of the West's champions
         to come within sight of Midgaard's walls.""",
         'mobs': [('reaver', 1)]},
    ],
    'mobs': [
        {'id': 'blight_crow', 'aliases': 'crow blight', 'short': 'a blight crow', 'role': 'standard', 'level': 30,
         'long': 'A blight crow with grey, featherless patches watches you hungrily.', 'flags': 'f', 'align': -400, 'attack': 'bite',
         'desc': 'A crow as big as a hawk, its beak stained black. The dead of the Marches have fed it well, and it has grown bold.'},
        {'id': 'tower_watchman', 'aliases': 'watchman soldier', 'short': 'a tower watchman', 'role': 'elite', 'level': 34,
         'long': 'A tower watchman stands at the palisade, crossbow ready.', 'flags': 'bm', 'align': 600, 'sex': 1,
         'desc': 'Hollow-cheeked and steady-eyed, he has seen everything the Marches can show and stayed at his post anyway.',
         'equip': [('watch_crossbow', 'wield', 100), ('watch_helm', 'head', 40)]},
        {'id': 'tower_surgeon', 'aliases': 'surgeon', 'short': 'the tower surgeon', 'role': 'harmless', 'level': 32,
         'long': 'A surgeon stitches a soldier\'s arm by the light of the brazier.', 'flags': 'b', 'align': 800, 'sex': 2,
         'desc': 'She came west with the first garrison and refused every order to go back.',
         'carry': [('field_dressing', 100)]},
        {'id': 'tower_captain', 'aliases': 'captain tower', 'short': 'the tower captain', 'role': 'champion', 'level': 35,
         'long': 'The tower captain watches the west from the parapet.', 'flags': 'b', 'align': 700, 'sex': 1,
         'desc': 'A big grey-bearded man with a voice like gravel. He has held this tower for a year with half the men he was promised.',
         'equip': [('captain_blade', 'wield', 100)]},
        {'id': 'tower_quartermaster', 'aliases': 'quartermaster', 'short': 'the quartermaster', 'role': 'elite', 'level': 33,
         'long': 'The quartermaster counts arrows into a chest.', 'flags': 'b', 'align': 400, 'sex': 1,
         'desc': 'A sour old soldier with one eye, guarding the last of the tower\'s supplies like a dragon.',
         'carry': [('hard_bread', 100), ('field_dressing', 100)]},
        {'id': 'marches_commander', 'aliases': 'commander marches', 'short': 'the Commander of the Marches', 'role': 'champion', 'level': 35,
         'long': 'The Commander of the Marches looks up from her maps with red-rimmed eyes.', 'flags': 'b', 'align': 800, 'sex': 2,
         'desc': 'She commands three towers, a hundred soldiers and a country of ash. She has written to Midgaard for more men eleven times. She has stopped writing.',
         'equip': [('commander_sword', 'wield', 100)]},
        {'id': 'hollowed_villager', 'aliases': 'hollowed villager', 'short': 'a hollowed villager', 'role': 'standard', 'level': 30,
         'long': 'A hollowed villager stands motionless, facing west.', 'flags': 'f', 'align': -700, 'attack': 'claw',
         'desc': 'There is no one behind the eyes. The darkness took whatever was inside and left the body walking, and it walks toward whatever the darkness wants.'},
        {'id': 'hollowed_militia', 'aliases': 'hollowed militia soldier', 'short': 'a hollowed militiaman', 'role': 'standard', 'level': 32,
         'long': 'A hollowed militiaman shambles along, a rusted spear in his hand.', 'flags': 'f', 'align': -700,
         'desc': 'He still wears the tabard of a village watch. He still carries his spear. He still knows how to use it, and nothing else.',
         'equip': [('rusted_spear', 'wield', 80)]},
        {'id': 'carrion_hound', 'aliases': 'hound carrion', 'short': 'a carrion hound', 'role': 'standard', 'level': 31,
         'long': 'A carrion hound with a bloated belly snarls over a corpse.', 'flags': 'f', 'align': -500, 'attack': 'bite',
         'desc': 'The raiders\' hounds have gorged on the dead of the Marches and grown big as ponies, mangy and yellow-eyed.',
         'carry': [('hound_hide', 20)]},
        {'id': 'ash_ghoul', 'aliases': 'ghoul ash', 'short': 'an ash ghoul', 'role': 'standard', 'level': 33,
         'long': 'An ash ghoul crawls out of the grey drifts.', 'flags': 'f', 'align': -800, 'attack': 'claw',
         'desc': 'A corpse dusted grey with ash, too long dead to walk upright. It moves on all fours, quick and hungry.'},
        {'id': 'hanged_wraith', 'aliases': 'wraith hanged', 'short': 'a hanged wraith', 'role': 'elite', 'level': 35,
         'long': 'A wraith with a noose around its neck drifts down from the oak.', 'flags': 'bf', 'align': -900, 'attack': 'claw',
         'desc': 'The spirits of the hanged have run together under the oak into something cold and furious, its face many faces.',
         'carry': [('hangmans_noose', 60)]},
        {'id': 'raider', 'aliases': 'raider grey', 'short': 'a grey-handed raider', 'role': 'standard', 'level': 34,
         'long': 'A raider with a grey hand painted on his chest sharpens an axe.', 'flags': 'f', 'align': -800, 'sex': 1,
         'desc': 'Once a farmer or a herdsman from the far west, now a servant of the darkness. He fights with a zealot\'s joy and dies smiling.',
         'equip': [('raider_axe', 'wield', 70), ('raider_leathers', 'body', 30)]},
        {'id': 'raider_outrider', 'aliases': 'outrider raider', 'short': 'a raider outrider', 'role': 'elite', 'level': 35,
         'long': 'A raider outrider in a wolf-skin cloak watches you over a drawn bow.', 'flags': 'fl', 'align': -800, 'sex': 2,
         'desc': 'The raiders\' scouts ride ahead of every attack, and they leave no witnesses.',
         'equip': [('outrider_bow', 'wield', 100), ('wolfskin_cloak', 'about', 40)]},
        {'id': 'captive_villager', 'aliases': 'captive villager prisoner', 'short': 'a captive villager', 'role': 'harmless', 'level': 30,
         'long': 'A captive villager huddles in the pen, eyes on the chapel.', 'flags': 'b', 'align': 500,
         'desc': 'Starved and filthy. Tomorrow, or the day after, it will be her turn in the chair.'},
        {'id': 'raider_jailer', 'aliases': 'jailer raider', 'short': 'the raider jailer', 'role': 'elite', 'level': 35,
         'long': 'A fat raider jailer leans on the pen, a whip in his belt.', 'flags': 'bf', 'align': -800, 'sex': 1,
         'desc': 'He chooses who goes to the chapel each day. He takes bribes, and then he chooses them anyway.',
         'equip': [('raider_axe', 'wield', 100)], 'carry': [('pen_key', 100)]},
        {'id': 'raider_shaman', 'aliases': 'shaman raider', 'short': 'a raider shaman', 'role': 'elite', 'level': 35,
         'long': 'A raider shaman with ash-grey skin chants over a strapped chair.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'His eyes are black from lid to lid. He hollows people with Nu\'Groth\'s words and a grey dust breathed into their mouths.',
         'equip': [('ash_staff', 'wield', 100)]},
        {'id': 'raider_warlord', 'aliases': 'warlord raider', 'short': 'the raider warlord', 'role': 'champion', 'level': 35,
         'long': 'The raider warlord rises from his furs, reaching for a great axe.', 'flags': 'bfl', 'align': -900, 'sex': 1,
         'desc': 'A giant of a man with a grey hand tattooed across his whole face. He has burned eleven villages and he means to burn the twelfth inside Midgaard\'s walls.',
         'equip': [('warlord_axe', 'wield', 100), ('raider_leathers', 'body', 100)]},
        {'id': 'drowned_hollow', 'aliases': 'drowned hollow corpse', 'short': 'a drowned hollow', 'role': 'standard', 'level': 32,
         'long': 'A bloated grey corpse lurches up out of the stream.', 'flags': 'f', 'align': -700, 'attack': 'claw',
         'desc': 'Thrown in the millstream with the other dead. The darkness walked it out again.'},
        {'id': 'hound_alpha', 'aliases': 'alpha hound carrion', 'short': 'the carrion alpha', 'role': 'champion', 'level': 34,
         'long': 'An enormous carrion hound rises from a heap of bones, eyes glowing like coals.', 'flags': 'bfl', 'align': -700, 'attack': 'bite',
         'desc': 'The sire of the pack, big as a bull, its hide scarred and patched with grey. It has eaten a hundred dead and wants a living meal.',
         'carry': [('alpha_fang', 100)]},
        {'id': 'reaver', 'aliases': 'reaver ashford', 'short': 'the Reaver of Ashford', 'role': 'boss', 'level': 35,
         'long': 'The Reaver of Ashford turns from the bone fire, a great black blade in his hands.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'Once the lord of Ashford, he opened his gates to the darkness to save his people and was rewarded by being made its herald. Grey fire burns in his empty helm, and he has sworn to hang every soldier of the towers from the oak.',
         'equip': [('reaver_blade', 'wield', 100), ('reaver_helm', 'head', 100), ('blackened_plate', 'body', 100)]},
    ],
    'objs': [
        {'id': 'water_barrel', 'kind': 'fountain', 'aliases': 'barrel water', 'short': 'a water barrel',
         'long': 'A barrel of clean water stands by the wall.', 'liquid': 0},
        {'id': 'cracked_fountain', 'kind': 'fountain', 'aliases': 'fountain cracked', 'short': 'a cracked fountain',
         'long': 'A cracked stone fountain dribbles grey water.', 'liquid': 0},
        {'id': 'ash_tome', 'kind': 'other', 'fixed': True, 'aliases': 'book tome', 'short': 'an open book of grey pages',
         'long': 'A book lies open on the table, its pages grey.',
         'extras': {'book tome pages': 'The words crawl when you look at them. One phrase repeats, in a hundred hands: THE WALL IS ALREADY FALLEN. IT HAS ONLY NOT NOTICED.'}},
        {'id': 'field_dressing', 'kind': 'potion', 'level': 32, 'spells': [15], 'spell_level': 30,
         'aliases': 'dressing field bandage', 'short': 'a field dressing', 'long': 'A rolled field dressing lies here.', 'weight': 1},
        {'id': 'hard_bread', 'kind': 'food', 'hours': 12, 'aliases': 'bread hard', 'short': 'a hard loaf of army bread',
         'long': 'A hard loaf of army bread lies here.', 'weight': 1, 'cost': 10},
        {'id': 'watch_crossbow', 'kind': 'weapon', 'level': 33, 'attack': 'pierce', 'aliases': 'crossbow watch',
         'short': 'a watchman\'s crossbow', 'long': 'A heavy crossbow lies here.'},
        {'id': 'watch_helm', 'kind': 'armor', 'slot': 'head', 'level': 33, 'aliases': 'helm watch',
         'short': 'a dented watch helm', 'long': 'A dented grey helm lies here.'},
        {'id': 'captain_blade', 'kind': 'weapon', 'level': 35, 'attack': 'slash', 'aliases': 'blade captain',
         'short': 'a captain\'s longsword', 'long': 'A plain, well-kept longsword lies here.', 'affects': [('hitroll', 2)]},
        {'id': 'commander_sword', 'kind': 'weapon', 'level': 36, 'attack': 'slash', 'aliases': 'sword commander',
         'short': 'the Commander\'s sword', 'long': 'A sword with a worn leather grip lies here.', 'affects': [('hitroll', 2), ('damroll', 2)]},
        {'id': 'rusted_spear', 'kind': 'weapon', 'level': 31, 'attack': 'pierce', 'aliases': 'spear rusted',
         'short': 'a rusted militia spear', 'long': 'A rusted spear lies here.'},
        {'id': 'hound_hide', 'kind': 'armor', 'slot': 'about', 'level': 31, 'aliases': 'hide hound',
         'short': 'a mangy hound hide', 'long': 'A mangy hound hide lies here.'},
        {'id': 'hangmans_noose', 'kind': 'worn', 'slot': 'neck', 'level': 35, 'aliases': 'noose hangman',
         'short': 'a hangman\'s noose', 'long': 'A frayed noose lies coiled here.', 'affects': [('save_para', -3), ('con', 1)]},
        {'id': 'raider_axe', 'kind': 'weapon', 'level': 34, 'attack': 'slash', 'aliases': 'axe raider',
         'short': 'a raider\'s axe', 'long': 'A notched axe with a grey hand painted on the haft lies here.'},
        {'id': 'raider_leathers', 'kind': 'armor', 'slot': 'body', 'level': 34, 'aliases': 'leathers raider',
         'short': 'raider leathers', 'long': 'A set of patched raider leathers lies here.'},
        {'id': 'outrider_bow', 'kind': 'weapon', 'level': 35, 'attack': 'pierce', 'aliases': 'bow outrider',
         'short': 'an outrider\'s horn bow', 'long': 'A short horn bow lies here.', 'affects': [('dex', 1)]},
        {'id': 'wolfskin_cloak', 'kind': 'armor', 'slot': 'about', 'level': 35, 'aliases': 'cloak wolfskin',
         'short': 'a wolf-skin cloak', 'long': 'A wolf-skin cloak lies here.', 'affects': [('move', 20)]},
        {'id': 'pen_key', 'kind': 'key', 'aliases': 'key pen', 'short': 'a crude iron key', 'long': 'A crude iron key lies here.', 'weight': 1},
        {'id': 'ash_staff', 'kind': 'weapon', 'level': 35, 'attack': 'bludgeon', 'aliases': 'staff ash',
         'short': 'a staff of ash-grey wood', 'long': 'A staff of grey wood lies here.', 'affects': [('mana', 30), ('int', 1)]},
        {'id': 'warlord_axe', 'kind': 'weapon', 'level': 36, 'attack': 'slash', 'aliases': 'axe great warlord', 'two_handed': True,
         'short': 'the warlord\'s great axe', 'long': 'A huge double-bitted axe lies here.', 'affects': [('damroll', 3)]},
        {'id': 'alpha_fang', 'kind': 'worn', 'slot': 'neck', 'level': 35, 'aliases': 'fang alpha necklace',
         'short': 'a necklace of carrion fangs', 'long': 'A necklace of yellow fangs lies here.', 'affects': [('str', 1), ('hitroll', 1)]},
        {'id': 'reaver_blade', 'kind': 'weapon', 'level': 37, 'attack': 'slash', 'aliases': 'blade reaver black',
         'short': 'the Reaver\'s black blade', 'long': 'A greatsword of black iron lies here, smoking faintly.', 'two_handed': True,
         'affects': [('hitroll', 3), ('damroll', 3)]},
        {'id': 'reaver_helm', 'kind': 'armor', 'slot': 'head', 'level': 37, 'aliases': 'helm reaver empty',
         'short': 'the Reaver\'s empty helm', 'long': 'A blackened helm, grey embers glowing inside it, lies here.',
         'affects': [('hit', 25), ('save_spell', -2)]},
        {'id': 'blackened_plate', 'kind': 'armor', 'slot': 'body', 'level': 36, 'aliases': 'plate blackened breastplate',
         'short': 'a blackened breastplate', 'long': 'A breastplate scorched black lies here.', 'affects': [('con', 1)]},
    ],
}
