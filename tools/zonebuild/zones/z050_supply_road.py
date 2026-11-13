"""The Supply Road -- support ring, levels 12-20.

The caravan road from Midgaard's east gate to the older eastern lands. It is
the fort's lifeline, and everything that preys on a lifeline is here:
deserters, bandits, wolves. Reconnects Miden'Nir, New Thalos, Drow City and
the City of Thalos, which used to hang off the Great Eastern Desert.
"""

ZONE = {
    'num': 50, 'name': 'The Supply Road', 'builders': 'Claude', 'lifespan': 20,
    # Miden'Nir is reached only from the road now; its second entrance from
    # South Midgaard contradicted the map.
    'remove_exits': [(3127, 'w'), (3504, 'e'),
                     (5232, 'e'), (5234, 'n')],      # stock Thalos exits to a room 5233 that never existed
    'room_descs': {
        3053: """You stand outside Midgaard's east gate, where the fort turns its back on
        the war and faces the lands that feed it.  The gate towers are lit day and
        night, and soldiers count every wagon that passes.  The Supply Road runs east
        between deep ruts, a muddy lane leads north toward the Granary Fields, and
        the clang of hammers drifts up from the Ironworks to the south.""",
    },
    'rooms': [
        {'id': 'gate', 'name': 'The Supply Road Below the East Gate', 'sector': 'field',
         'desc': """The road leaves Midgaard's east gate and runs out across open country,
         churned to black mud by wagon wheels and the boots of marching columns.  A
         wooden board nailed to a post lists the day's convoys in chalk, half of
         them crossed out.  The fort's walls loom to the west.""",
         'exits': {'w': {'to': '@3053', 'back_desc': 'The Supply Road runs east into the countryside.'},
                   'e': 'ruts'},
         'extras': {'board post chalk': 'Convoy names, dates and destinations. Beside three of them someone has written a single word: LOST.'},
         'mobs': [('teamster', 2)]},
        {'id': 'ruts', 'name': 'The Supply Road, Rutted Stretch', 'sector': 'field',
         'desc': """Ruts as deep as a man's shin score the road, filled with brown water that
         never quite dries.  Broken spokes and a lost horseshoe lie in the verge.
         Fields stretch away on either side, empty of workers this far from the
         wall.""",
         'exits': {'e': 'milestone'},
         'mobs': [('carrion_crow', 2)]},
        {'id': 'milestone', 'name': 'The Supply Road, By a Milestone', 'sector': 'field',
         'desc': """A squat milestone of grey granite marks the first league from Midgaard.
         Generations of travellers have scratched names and prayers into it, and
         newer hands have added the names of the dead.  To the north the road
         widens into the yard of a caravan depot.""",
         'exits': {'e': 'watch_road', 'n': 'depot_yard'},
         'extras': {'milestone stone names prayers': 'MIDGAARD I LEAGUE. Below, hundreds of names. The freshest read: "Holt, Anna, the twins. Taken on the road. Pray for them."'}},
        {'id': 'depot_yard', 'name': 'The Caravan Depot Yard', 'sector': 'city', 'flags': 'c',
         'desc': """Wagons stand in rows inside a palisade of sharpened logs, their canvas
         covers patched and stained.  Teamsters argue over loads while soldiers in
         Midgaard's grey watch every crate.  Everything bound for the fort passes
         through this yard, and everything is counted twice.""",
         'exits': {'w': 'stables', 'e': 'storehouse', 'n': 'depot_office'},
         'mobs': [('caravan_guard', 3), ('teamster', 2)]},
        {'id': 'stables', 'name': 'The Depot Stables', 'sector': 'inside', 'flags': 'cd',
         'desc': """Long stalls hold the depot's oxen and draught horses, thin from short
         rations.  The smell of dung and wet straw is thick.  A farrier's anvil
         stands by the door, and a row of hooks holds harness waiting for repair.""",
         'mobs': [('stablehand', 1)]},
        {'id': 'storehouse', 'name': 'The Depot Storehouse', 'sector': 'inside', 'flags': 'cd',
         'desc': """Sacks of grain, barrels of salt pork and crates stamped with Midgaard's
         seal are stacked to the rafters.  A clerk's desk stands by the door with a
         ledger chained to it.  Rats scratch somewhere behind the sacks, and nobody
         bothers to chase them any more.""",
         'objs': [('ledger', 1)],
         'mobs': [('depot_clerk', 1)]},
        {'id': 'depot_office', 'name': "The Depot Master's Office", 'sector': 'inside', 'flags': 'cd',
         'desc': """A cramped room with a single shuttered window overlooking the yard.  Maps
         of the road are pinned to the walls, marked in red where convoys were
         attacked.  The marks cluster around the old bridge and the Wolf Wood, and
         there are more of them every week.""",
         'extras': {'maps map marks red': 'The road east from Midgaard, drawn carefully. Red crosses crowd the old bridge, the deserters\' camp, and the edge of the Wolf Wood.'},
         'mobs': [('depot_master', 1)]},
        {'id': 'watch_road', 'name': 'The Supply Road, Beneath the Watch Hill', 'sector': 'field',
         'desc': """The road skirts the foot of a steep grassy hill crowned with a signal
         tower.  A path of trodden earth climbs toward it.  From up there the
         garrison can see smoke from the Ironworks, the fort's walls, and anything
         moving on the road for leagues.""",
         'exits': {'u': 'watch_hill', 'e': 'gallows'}},
        {'id': 'watch_hill', 'name': 'The Watch Hill Signal Tower', 'sector': 'hills',
         'desc': """A stone tower stands on the hilltop beside a great iron basket of pitch
         and timber, ready to be lit.  The wind is constant up here.  Far to the
         west, beyond Midgaard, the horizon is smudged with a darkness that is
         not cloud and never moves.""",
         'extras': {'basket pitch beacon': 'If the beacon is lit, every soldier between here and the fort will march. It has been lit twice this year.',
                    'west horizon darkness': 'A low stain across the western sky, darker at the bottom. Looking at it too long makes your eyes ache.'},
         'mobs': [('signal_warden', 1)]},
        {'id': 'gallows', 'name': 'The Supply Road, Gallows Corner', 'sector': 'field',
         'desc': """The road bends around a gallows built where everyone must pass it.
         Three bodies turn slowly on their ropes, a placard hung around each neck.
         Crows have been at them.  A rough track leads south through a hedge toward
         a thin column of cookfire smoke.""",
         'exits': {'e': 'fork', 's': 'camp_edge'},
         'extras': {'placard placards bodies': 'Each placard reads DESERTER in black paint.'},
         'mobs': [('carrion_crow', 3)]},
        {'id': 'camp_edge', 'name': "The Edge of the Deserters' Camp", 'sector': 'forest',
         'desc': """Beyond the hedge, lean-tos of stolen canvas crouch among the trees.
         Men in torn Midgaard grey squat around low fires, their eyes on the road.
         Discarded armour lies everywhere, the fort's sigil scratched out of every
         piece.""",
         'exits': {'s': 'camp', 'e': 'camp_pickets'},
         'mobs': [('deserter', 3)]},
        {'id': 'camp_pickets', 'name': "The Deserters' Picket Line", 'sector': 'forest',
         'desc': """A line of sharpened stakes faces the road, built by men who still
         remember their drill.  A crude watch post overlooks the track, its lookout
         dozing on a stolen shield.  Empty wine jars are stacked behind it like
         ammunition.""",
         'mobs': [('deserter', 2), ('deserter_sergeant', 1)]},
        {'id': 'camp', 'name': "The Deserters' Camp", 'sector': 'forest',
         'desc': """The heart of the camp is a ring of tents around a fire pit.  Loot from
         raided wagons is piled carelessly: grain sacks, a smashed harp, a child's
         shoe.  The men here fled the wall, and they would rather kill than be
         dragged back to it.""",
         'exits': {'s': 'captain_tent'},
         'mobs': [('deserter', 3), ('deserter_sergeant', 1)]},
        {'id': 'captain_tent', 'name': "The Deserter Captain's Tent", 'sector': 'inside', 'flags': 'd',
         'desc': """A command tent, taken whole from the garrison.  A folding table holds a
         map of the road with the convoy times marked in a soldier's neat hand.
         Captured banners hang upside down.  Whoever leads here was once a good
         officer, which makes him far more dangerous.""",
         'mobs': [('deserter_captain', 1)]},
        {'id': 'fork', 'name': 'The Supply Road, The Thalos Fork', 'sector': 'field',
         'desc': """A paved spur breaks south from the road toward the white walls of Thalos,
         an old city that has shut its great gate to all but carts of tribute.  A
         weathered statue of a king points down the spur.  Somebody has knocked off
         its head.""",
         'exits': {'s': {'to': '@5200', 'back_desc': 'North of the gate the Supply Road runs east and west.'},
                   'e': 'burned_wagon'},
         'extras': {'statue king': 'A king in old-fashioned armour, one arm outstretched toward Thalos. The head lies in the ditch, face down.'}},
        {'id': 'burned_wagon', 'name': 'The Supply Road, The Burned Wagon', 'sector': 'field',
         'desc': """The blackened shell of a supply wagon lies on its side across the verge,
         its oxen long since butchered and eaten.  Arrows still stand in the
         charred boards.  Whoever drove it is not here, and nobody has come to
         bury them.""",
         'exits': {'e': 'bridge'},
         'extras': {'wagon arrows boards': 'Short black-fletched arrows, the kind bandits favour. A few are Midgaard militia shafts, fired back.'},
         'mobs': [('bandit', 2)]},
        {'id': 'bridge', 'name': 'The Supply Road, The Old Bridge', 'sector': 'field',
         'desc': """A humped stone bridge carries the road over a slow, brown river.  Its
         parapets are cracked and one has fallen into the water.  Muddy footprints
         lead off the road and down the bank to the dark space beneath the
         arch.""",
         'exits': {'d': 'under_bridge', 'e': 'wood_edge'},
         'extras': {'footprints prints bank': 'Many boots, coming and going, all heading under the bridge.'},
         'mobs': [('bandit', 2)]},
        {'id': 'under_bridge', 'name': 'Beneath the Old Bridge', 'sector': 'inside', 'flags': 'ad',
         'desc': """Under the arch the Dark River laps against a ledge of slick stone.  The wall
         here has been chiselled open into a low tunnel, hung with a filthy
         curtain.  Bones of small animals and a few that are not so small litter
         the ledge.""",
         'exits': {'e': 'tunnel',
                   'n': {'to': '@5671', 'desc': 'The Dark River flows away north into the hills.',
                         'back_desc': 'Downstream, the river passes under the arch of an old stone bridge.'}},
         'mobs': [('bandit_lookout', 1)]},
        {'id': 'tunnel', 'name': 'The Bandit Tunnel', 'sector': 'inside', 'flags': 'ad',
         'desc': """A cramped tunnel dug through earth and old foundation stones, shored up
         with timbers stolen from wagons.  Water drips constantly.  It opens ahead
         into a wider space lit by stolen lanterns, where voices argue over
         shares.""",
         'exits': {'e': 'cache_hall'},
         'mobs': [('bandit', 2)]},
        {'id': 'cache_hall', 'name': "The Bandits' Den", 'sector': 'inside', 'flags': 'd',
         'desc': """A cellar of some long-gone house, widened and held up with timbers.
         Bedrolls ring the walls and a table is covered in dice and coin.  An
         iron-bound door in the far wall is locked, and a heavier curtain hangs
         over an arch to the north.""",
         'exits': {'s': {'to': 'cache', 'door': 'door iron', 'key': 'cache_key', 'state': 'locked',
                         'desc': 'An iron-bound door, locked.'},
                   'n': 'lord_hall'},
         'mobs': [('bandit', 2), ('bandit_cutthroat', 2)]},
        {'id': 'cache', 'name': "The Bandits' Cache", 'sector': 'inside', 'flags': 'd',
         'desc': """Crates and sacks from a dozen stolen convoys fill this narrow room, much
         of it Midgaard's own seal.  The fort is going hungry so this can rot in a
         cellar.  A strongbox sits on a crate beneath a guttering candle.""",
         'objs': [('strongbox', 1, [('salt_pork', 3), ('grain_sack', 2), ('signet_ring', 1)])]},
        {'id': 'lord_hall', 'name': "The Bandit Lord's Hall", 'sector': 'inside', 'flags': 'd',
         'desc': """A long room furnished with the best of everything stolen: a carved
         chair, tapestries, a rug from somewhere far to the east.  The man who
         rules the road from here sits as if he were a lord in truth, and the
         fort's tithes pay for his wine.""",
         'mobs': [('bandit_lord', 1)]},
        {'id': 'wood_edge', 'name': 'The Supply Road, Edge of the Wolf Wood', 'sector': 'forest',
         'desc': """Dark pines crowd close on both sides of the road.  Claw marks score the
         bark at shoulder height, and a torn cloak hangs from a branch.  Convoys
         run this stretch at a gallop.  A narrow game trail slips north among the
         trees.""",
         'exits': {'n': 'wolf_trail', 'e': 'sinkhole'},
         'mobs': [('grey_wolf', 2)]},
        {'id': 'wolf_trail', 'name': 'The Wolf Wood, A Trampled Trail', 'sector': 'forest',
         'desc': """The trail winds between pines whose lowest branches are stripped bare.
         The ground is churned by many paws and stained in places.  Somewhere
         ahead, too close, a wolf howls and others answer from all around.""",
         'exits': {'n': 'wolf_den'},
         'mobs': [('grey_wolf', 3)]},
        {'id': 'wolf_den', 'name': 'The Wolf Wood, The Den', 'sector': 'forest',
         'desc': """A hollow beneath the roots of a fallen giant pine, strewn with bones
         gnawed white.  Some are cattle.  Some wear the scraps of teamsters'
         leather.  The pack has grown bold and huge, and its leader is larger
         than any wolf has a right to be.""",
         'mobs': [('wolf_matriarch', 1), ('grey_wolf', 2)]},
        {'id': 'sinkhole', 'name': 'The Supply Road, The Sinkhole', 'sector': 'field',
         'desc': """Beside the road the earth has fallen away into a ragged sinkhole, and a
         rope ladder has been pegged to its lip.  Cold air breathes up from below,
         smelling of stone and something sweet and rotten.  The ladder descends
         toward Drow City, and the road continues east.""",
         'exits': {'d': {'to': '@5100', 'back_desc': 'A rope ladder climbs to daylight and the Supply Road.'},
                   'e': 'hills_foot'},
         'extras': {'ladder rope': 'Well made, and recently replaced. Someone down there trades with the surface.'}},
        {'id': 'hills_foot', 'name': 'The Supply Road, Before the Hills', 'sector': 'hills',
         'desc': """The road begins to climb into rolling hills.  To the north, the southern
         gate of New Thalos rises above the slopes, its banners hanging limp.
         Merchants still come down that road with grain and steel for the fort,
         though fewer each season.""",
         'exits': {'n': {'to': '@5411', 'back_desc': 'South of the gate, the Supply Road winds through the hills.'},
                   'e': 'turning'},
         'mobs': [('caravan_guard', 1)]},
        {'id': 'turning', 'name': "The Supply Road, The Miden'Nir Turning", 'sector': 'hills',
         'desc': """Here the road ends at a crossroads shrine where three tracks meet.  The
         eastern track leads to Miden'Nir.  The shrine's lamp has been kept lit by
         someone, and offerings of bread and salt sit before a carving of a
         weeping woman.""",
         'exits': {'e': {'to': '@3503', 'back_desc': 'West, the Supply Road leads back toward Midgaard.'},
                   's': 'shrine', 'n': 'gate_path'},
         'extras': {'carving woman shrine lamp': 'The Mourning Mother, they call her. She is said to weep for every soul the West takes.'}},
        {'id': 'gate_path', 'name': "The Path to Miden'Nir's South Gate", 'sector': 'hills',
         'desc': """A narrow track climbs between hedges of thorn toward a squat stone gatehouse
         in Miden'Nir's outer wall.  The gate stands open, but the arrow slits above
         it are manned, and the guards watch every face that comes up from the
         road.""",
         'exits': {'e': {'to': '@3504', 'back_desc': 'West, a track runs down to the Supply Road crossroads.'}}},
        {'id': 'shrine', 'name': 'Beside the Roadside Shrine', 'sector': 'hills', 'flags': 'ce',
         'desc': """A small hollow behind the shrine is sheltered from the wind by a ring of
         standing stones.  Travellers rest here, and the stones are warm to the
         touch even on cold nights.  No beast has ever been seen to cross the
         ring.""",
         'mobs': [('shrine_keeper', 1)]},
    ],
    'mobs': [
        {'id': 'teamster', 'aliases': 'teamster driver', 'short': 'a weary teamster', 'role': 'harmless', 'level': 12,
         'long': 'A weary teamster checks the harness on his team.', 'flags': 'g', 'align': 300, 'sex': 1,
         'desc': 'A broad-shouldered man with mud to the knees and a whip coiled on his belt. He looks as though he has not slept properly in a month.'},
        {'id': 'carrion_crow', 'aliases': 'crow carrion', 'short': 'a carrion crow', 'role': 'harmless', 'level': 12,
         'long': 'A carrion crow watches you with one bright eye.', 'flags': 'g', 'align': 0, 'attack': 'bite',
         'desc': 'A big black crow, fat on the road\'s dead. It hops closer whenever you stop moving.'},
        {'id': 'caravan_guard', 'aliases': 'guard caravan soldier', 'short': 'a caravan guard', 'role': 'standard', 'level': 16,
         'long': 'A caravan guard in Midgaard grey keeps watch over the wagons.', 'flags': 'm', 'align': 500, 'sex': 1,
         'desc': 'A hard-faced soldier with a spear and a dented helm. Guarding wagons is supposed to be the easy duty. Nobody on this road believes that.',
         'equip': [('militia_spear', 'wield', 100), ('militia_shield', 'shield', 40)]},
        {'id': 'stablehand', 'aliases': 'stablehand boy', 'short': 'a stablehand', 'role': 'harmless', 'level': 12,
         'long': 'A stablehand forks straw into an empty stall.', 'flags': 'b', 'align': 200, 'sex': 1,
         'desc': 'A thin youth with straw in his hair. His older brothers all went west to the wall.'},
        {'id': 'depot_clerk', 'aliases': 'clerk depot', 'short': 'the depot clerk', 'role': 'harmless', 'level': 13,
         'long': 'The depot clerk scratches figures into a ledger.', 'flags': 'b', 'align': 100, 'sex': 2,
         'desc': 'An ink-stained woman with spectacles and no patience. Every sack that goes missing is a sack she has to explain.'},
        {'id': 'depot_master', 'aliases': 'master depot', 'short': 'the depot master', 'role': 'elite', 'level': 18,
         'long': 'The depot master studies the maps, jaw clenched.', 'flags': 'b', 'align': 400, 'sex': 1,
         'desc': 'A one-armed veteran of the wall, sent east when he could no longer hold a shield. He runs the depot like a battle, because to him it is one.'},
        {'id': 'signal_warden', 'aliases': 'warden signal', 'short': 'the signal warden', 'role': 'elite', 'level': 17,
         'long': 'The signal warden stares west, a torch ready in her hand.', 'flags': 'b', 'align': 400, 'sex': 2,
         'desc': 'A grey-haired woman wrapped in a wool cloak, her eyes never leaving the western horizon.',
         'carry': [('caravan_lantern', 60)]},
        {'id': 'deserter', 'aliases': 'deserter soldier', 'short': 'a deserter', 'role': 'standard', 'level': 14,
         'long': 'A deserter in torn grey glares at you, hand on his blade.', 'flags': 'fg', 'align': -300, 'sex': 1,
         'desc': 'He once stood on Midgaard\'s wall. Whatever he saw out there broke him, and now he would cut your throat for your boots.',
         'equip': [('notched_sword', 'wield', 70)]},
        {'id': 'deserter_sergeant', 'aliases': 'sergeant deserter', 'short': 'a deserter sergeant', 'role': 'elite', 'level': 17,
         'long': 'A deserter sergeant barks orders at the men around the fire.', 'flags': 'fl', 'align': -400, 'sex': 1,
         'desc': 'Thick-necked and scarred, he still wears his sergeant\'s braid. He took his squad with him when he ran.',
         'equip': [('notched_sword', 'wield', 100), ('deserter_mail', 'body', 35)]},
        {'id': 'deserter_captain', 'aliases': 'captain deserter', 'short': 'the deserter captain', 'role': 'champion', 'level': 18,
         'long': 'The deserter captain looks up from his map with cold, intelligent eyes.', 'flags': 'bl', 'align': -500, 'sex': 1,
         'desc': 'Lean, clean-shaven and calm, he wears a captain\'s cloak with the sigil cut away. He decided the fort was already lost, and that the living should take what they can.',
         'equip': [('captains_sabre', 'wield', 100), ('deserter_mail', 'body', 100), ('deserter_helm', 'head', 60)]},
        {'id': 'bandit', 'aliases': 'bandit robber', 'short': 'a road bandit', 'role': 'standard', 'level': 15,
         'long': 'A road bandit grins at you over a drawn knife.', 'flags': 'fg', 'align': -500, 'sex': 1,
         'desc': 'A ragged cutthroat in mismatched leathers. Business has never been better: the fort pays, the road bleeds, and nobody comes looking.',
         'equip': [('bandit_shortsword', 'wield', 60)]},
        {'id': 'bandit_lookout', 'aliases': 'lookout bandit', 'short': 'a bandit lookout', 'role': 'standard', 'level': 16,
         'long': 'A bandit lookout crouches by the curtain, crossbow across his knees.', 'flags': 'bf', 'align': -500, 'sex': 1,
         'desc': 'A wiry man with sharp eyes and a sharper knife. He whistles a warning the moment he sees you.'},
        {'id': 'bandit_cutthroat', 'aliases': 'cutthroat bandit', 'short': 'a bandit cutthroat', 'role': 'elite', 'level': 18,
         'long': 'A bandit cutthroat turns a long dagger slowly in his fingers.', 'flags': 'fl', 'align': -700, 'sex': 1,
         'desc': 'The lord\'s favourite killers. Quick, quiet and utterly without pity.',
         'equip': [('cutthroat_dagger', 'wield', 100)], 'carry': [('cache_key', 50)]},
        {'id': 'bandit_lord', 'aliases': 'lord bandit', 'short': 'the Bandit Lord', 'role': 'boss', 'level': 20,
         'long': 'The Bandit Lord lounges in his carved chair, a broadsword across his knees.', 'flags': 'bl', 'align': -800, 'sex': 1,
         'desc': 'Big, handsome and dressed like nobility, he styles himself Lord of the Road. Every convoy that reaches the fort does so because he allowed it.',
         'equip': [('lords_broadsword', 'wield', 100), ('signet_ring', 'finger', 100), ('deserter_mail', 'body', 100)],
         'carry': [('cache_key', 100)]},
        {'id': 'grey_wolf', 'aliases': 'wolf grey', 'short': 'a grey wolf', 'role': 'standard', 'level': 13,
         'long': 'A lean grey wolf circles you, hackles raised.', 'flags': 'fg', 'align': -100, 'attack': 'bite',
         'desc': 'Gaunt and bold, with a scar across its muzzle. Hunger has driven the wolves out of the hills and onto the road.',
         'carry': [('wolf_pelt', 25)]},
        {'id': 'wolf_matriarch', 'aliases': 'wolf matriarch dire', 'short': 'the dire wolf matriarch', 'role': 'champion', 'level': 17,
         'long': 'An enormous dire wolf rises from the bones, lips peeling back from yellow fangs.', 'flags': 'bfl', 'align': -300, 'attack': 'bite',
         'desc': 'Twice the size of any wolf in the pack, her fur matted with old blood. Something in the West has been feeding her strength.',
         'carry': [('matriarch_cloak', 100)]},
        {'id': 'shrine_keeper', 'aliases': 'keeper shrine old woman', 'short': 'the shrine keeper', 'role': 'harmless', 'level': 15,
         'long': 'An old woman tends the shrine lamp, murmuring prayers.', 'flags': 'b', 'align': 900, 'sex': 2,
         'desc': 'Her hands shake, but the lamp has never gone out. She asks every traveller their name, so she can pray for them if they do not come back.',
         'carry': [('road_ration', 100)]},
    ],
    'objs': [
        {'id': 'ledger', 'kind': 'other', 'fixed': True, 'aliases': 'ledger chained book', 'short': 'a chained ledger',
         'long': 'A heavy ledger is chained to the clerk\'s desk.',
         'extras': {'ledger chained book': 'Columns of figures. Grain received, grain sent west. Each week the second column is larger than the first.'}},
        {'id': 'strongbox', 'kind': 'container', 'fixed': True, 'capacity': 50, 'aliases': 'strongbox box iron',
         'short': 'an iron strongbox', 'long': 'An iron strongbox sits on a crate, its lid ajar.'},
        {'id': 'salt_pork', 'kind': 'food', 'hours': 16, 'aliases': 'pork salt slab', 'short': 'a slab of salt pork',
         'long': 'A slab of salt pork stamped with Midgaard\'s seal lies here.', 'weight': 2, 'cost': 20},
        {'id': 'grain_sack', 'kind': 'other', 'aliases': 'sack grain', 'short': 'a sack of the fort\'s grain',
         'long': 'A sack of grain stamped with Midgaard\'s seal lies here.', 'weight': 20, 'cost': 30},
        {'id': 'cache_key', 'kind': 'key', 'aliases': 'key iron cache', 'short': 'a heavy iron key',
         'long': 'A heavy iron key lies here.', 'weight': 1},
        {'id': 'road_ration', 'kind': 'food', 'hours': 10, 'aliases': 'ration bread road', 'short': 'a road ration',
         'long': 'A wrapped road ration has been left here.', 'weight': 1, 'cost': 8},
        {'id': 'caravan_lantern', 'kind': 'light', 'level': 12, 'hours': 48, 'aliases': 'lantern caravan',
         'short': 'a caravan lantern', 'long': 'A battered caravan lantern lies here.', 'weight': 3},
        {'id': 'militia_spear', 'kind': 'weapon', 'level': 15, 'attack': 'pierce', 'aliases': 'spear militia',
         'short': 'a militia spear', 'long': 'A plain militia spear lies here.'},
        {'id': 'militia_shield', 'kind': 'armor', 'slot': 'shield', 'level': 15, 'aliases': 'shield militia grey',
         'short': 'a grey militia shield', 'long': 'A round grey shield bearing Midgaard\'s tower lies here.'},
        {'id': 'notched_sword', 'kind': 'weapon', 'level': 14, 'attack': 'slash', 'aliases': 'sword notched',
         'short': 'a notched sword', 'long': 'A notched army sword lies here.'},
        {'id': 'deserter_mail', 'kind': 'armor', 'slot': 'body', 'level': 17, 'aliases': 'mail chain shirt',
         'short': 'a chain shirt with the sigil cut away', 'long': 'A chain shirt lies here, a hole cut where its sigil was.'},
        {'id': 'deserter_helm', 'kind': 'armor', 'slot': 'head', 'level': 18, 'aliases': 'helm helmet officer',
         'short': "an officer's helm", 'long': "An officer's plumed helm lies here.", 'affects': [('hitroll', 1)]},
        {'id': 'captains_sabre', 'kind': 'weapon', 'level': 19, 'attack': 'slash', 'aliases': 'sabre saber captain',
         'short': "a captain's sabre", 'long': "A fine captain's sabre lies here.", 'affects': [('hitroll', 1), ('damroll', 1)]},
        {'id': 'bandit_shortsword', 'kind': 'weapon', 'level': 15, 'attack': 'slash', 'aliases': 'shortsword sword short',
         'short': 'a bandit shortsword', 'long': 'A short, wicked blade lies here.'},
        {'id': 'cutthroat_dagger', 'kind': 'weapon', 'level': 18, 'attack': 'pierce', 'aliases': 'dagger long cutthroat',
         'short': "a cutthroat's long dagger", 'long': 'A long, thin dagger lies here.', 'affects': [('dex', 1)]},
        {'id': 'lords_broadsword', 'kind': 'weapon', 'level': 21, 'attack': 'slash', 'aliases': 'broadsword sword lord',
         'short': "the Bandit Lord's broadsword", 'long': 'A broadsword with a jewelled hilt lies here.',
         'affects': [('hitroll', 2), ('damroll', 2)]},
        {'id': 'signet_ring', 'kind': 'worn', 'slot': 'finger', 'level': 20, 'aliases': 'ring signet brass',
         'short': 'a brass signet ring', 'long': 'A heavy brass signet ring lies here.', 'affects': [('str', 1), ('hit', 10)]},
        {'id': 'wolf_pelt', 'kind': 'armor', 'slot': 'about', 'level': 13, 'aliases': 'pelt wolf',
         'short': 'a grey wolf pelt', 'long': 'A grey wolf pelt lies here.'},
        {'id': 'matriarch_cloak', 'kind': 'armor', 'slot': 'about', 'level': 18, 'aliases': 'cloak dire wolf fur',
         'short': "a cloak of dire wolf fur", 'long': 'A huge cloak of dark wolf fur lies here.', 'affects': [('con', 1), ('move', 15)]},
    ],
}
