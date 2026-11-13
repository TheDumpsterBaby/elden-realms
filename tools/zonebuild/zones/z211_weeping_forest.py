"""W12 The Weeping Forest -- the Blight, levels 85-90.

Above the Drowned Kingdom grows a forest of trees that are part flesh, with
bark that whispers and sap that bleeds. The land itself is hostile here: roots
grasp, fruit screams, and the paths move. At its heart stands the Weeping
Mother, grown from the first grove Nu\'Groth ever corrupted.
"""

ZONE = {
    'num': 211, 'name': 'The Weeping Forest', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'pool_edge', 'name': 'The Weeping Pool', 'sector': 'forest',
         'desc': """You climb out of a pool of grey water into a forest that should not exist.  The
         trees have bark like skin, pale and veined, and their branches end in fingers.
         Sap runs down them like tears.  All around you, very softly, the trees are
         weeping.""",
         'exits': {'d': {'to': '@21015', 'back_desc': 'Above, grey daylight shows through the surface of a pool.'}, 'w': 'skin_trees'},
         'mobs': [('grasping_root', 1)]},
        {'id': 'skin_trees', 'name': 'Among the Skin Trees', 'sector': 'forest',
         'desc': """The trunks are warm to the touch, and they flinch.  Faces push out of the bark,
         eyes closed, mouths moving.  They are the people the forest has taken, absorbed
         into the wood, still alive.  They whisper to you to cut them free, or to cut them
         down, or to join them.""",
         'exits': {'w': 'path_shifting', 'n': 'fruit_grove', 's': 'blood_stream'},
         'mobs': [('bark_stalker', 2)]},
        {'id': 'fruit_grove', 'name': 'The Grove of Screaming Fruit', 'sector': 'forest',
         'desc': """Heavy fruit hangs from these trees, swollen and red, each one the size of a head.
         When the wind moves them, they scream.  The ground is covered in burst fruit and
         the seeds inside them, which are teeth, and which have begun to put down
         roots.""",
         'exits': {'n': 'hanged_glade'},
         'mobs': [('fruit_swarm', 2)]},
        {'id': 'hanged_glade', 'name': 'The Glade of the Hanged Knight', 'sector': 'forest',
         'desc': """A knight in silver armour hangs from a great tree by vines grown through his
         arms and legs, his armour pierced by branches.  He has hung here for years, and
         he is not dead; the tree feeds on him and keeps him alive.  His eyes open, and
         he begs you to kill him.  The tree does not want you to.""",
         'mobs': [('weeping_knight', 1)]},
        {'id': 'blood_stream', 'name': 'The Stream of Sap', 'sector': 'water',
         'desc': """A stream of thick red sap flows slowly through the forest, warm and stinking of
         iron.  Things drown in it: deer, birds, a man still clutching a lantern.  The sap
         clings to your legs and does not want to let go.""",
         'exits': {'w': 'thorn_hollow'},
         'mobs': [('sap_ooze', 2)]},
        {'id': 'thorn_hollow', 'name': 'The Thorn Hollow', 'sector': 'forest',
         'desc': """A hollow overgrown with black thorns as long as swords, wet with red sap.  Wolves
         with thorns growing from their spines lie among them like hounds in a kennel.  At
         the centre of the hollow, a woman of thorns and bark sits weaving thorn into new
         shapes.""",
         'mobs': [('thorn_wolf', 2), ('thornmother', 1)]},
        {'id': 'path_shifting', 'name': 'The Shifting Path', 'sector': 'forest',
         'desc': """A path runs between the trees, but it will not stay still.  When you look away
         and look back, it bends in a new direction.  The trees lean in.  Roots move
         under the leaf litter like snakes.  The forest is herding you, and it knows
         where it wants you to go.""",
         'exits': {'w': 'whisper_wood', 'n': 'banshee_glade'},
         'mobs': [('grasping_root', 2)]},
        {'id': 'banshee_glade', 'name': 'The Glade of Mourning', 'sector': 'forest',
         'desc': """A glade of white trees, their bark smooth and pale as bone.  Women in white walk
         among them, wringing their hands, their faces hidden by their hair.  They are
         weeping for everyone the forest has taken, and their weeping is a sound that
         stops hearts.""",
         'mobs': [('weeping_maiden', 2)]},
        {'id': 'whisper_wood', 'name': 'The Whispering Wood', 'sector': 'forest',
         'desc': """The whispering is loud here, a thousand voices in the bark, all speaking at once,
         all saying the same thing: come closer, come closer, it is warm inside, it does
         not hurt for long.  You find you have taken a step toward a tree without
         deciding to.""",
         'exits': {'w': 'heart_grove', 's': 'root_maze'},
         'mobs': [('bark_stalker', 1), ('whisper_shade', 1)]},
        {'id': 'root_maze', 'name': 'The Root Maze', 'sector': 'forest', 'flags': 'a',
         'desc': """You descend into a maze of tunnels beneath the forest floor, walled with roots as
         thick as a man.  They pulse.  They are veins.  The whole forest is one creature,
         and you are inside its body, and somewhere ahead is its heart, beating.""",
         'mobs': [('root_horror', 2)]},
        {'id': 'heart_grove', 'name': 'The Heart Grove', 'sector': 'forest',
         'desc': """The trees part around a vast clearing.  In its centre stands the Weeping Mother,
         a tree larger than a castle, its bark a mass of faces, its branches hung with
         sleeping people wrapped in bark like cocoons.  This was the first grove the
         Nu\'Groth reached, long ago, and every tree in the forest grew from her seed.""",
         'exits': {'w': 'forest_end'},
         'mobs': [('weeping_mother', 1)]},
        {'id': 'forest_end', 'name': 'The Edge of the Forest', 'sector': 'forest',
         'desc': """The trees end abruptly at the foot of a black cliff that rises into the clouds.
         Built into the cliff, and out of it, is a fortress of black stone so vast that its
         walls are lost in the mist above.  War-horns sound from its towers.  This is the
         Nu\'Groth\'s outer fortress, and its gate is open.""",
         'mobs': [('grasping_root', 1)]},
    ],
    'mobs': [
        {'id': 'grasping_root', 'aliases': 'root grasping roots', 'short': 'a grasping root', 'role': 'elite', 'level': 87,
         'long': 'A thick root bursts out of the ground and lashes toward you.', 'flags': 'bf', 'align': -800, 'attack': 'whip',
         'desc': 'The forest reaching for you. It wants to pull you down into the earth.'},
        {'id': 'bark_stalker', 'aliases': 'stalker bark', 'short': 'a bark stalker', 'role': 'standard', 'level': 87,
         'long': 'A figure of pale bark and sap steps out of a tree trunk.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Someone the forest absorbed, now sent out to bring more.'},
        {'id': 'fruit_swarm', 'aliases': 'fruit swarm screaming', 'short': 'a swarm of screaming fruit', 'role': 'standard', 'level': 86,
         'long': 'A cluster of red fruit drops from the branches, splitting open into mouths full of teeth.', 'flags': 'f', 'align': -800, 'attack': 'bite',
         'desc': 'They scream as they bite.'},
        {'id': 'weeping_knight', 'aliases': 'knight weeping silver', 'short': 'the Weeping Knight', 'role': 'champion', 'level': 90,
         'long': 'A knight in silver armour, pierced by branches, tears himself free of the tree with a scream.', 'flags': 'bfl', 'align': -500, 'sex': 1,
         'desc': 'A paladin who came west to destroy the forest twenty years ago. It caught him and has fed on him ever since. When he fights, the tree fights through him.',
         'equip': [('silver_sword', 'wield', 100), ('pierced_plate', 'body', 100)]},
        {'id': 'sap_ooze', 'aliases': 'ooze sap', 'short': 'a sap ooze', 'role': 'standard', 'level': 87,
         'long': 'A mass of red sap rises from the stream and flows toward you.', 'flags': 'f', 'align': -700, 'attack': 'crush',
         'desc': 'It smothers and dissolves.'},
        {'id': 'thorn_wolf', 'aliases': 'wolf thorn', 'short': 'a thorn wolf', 'role': 'elite', 'level': 88,
         'long': 'A wolf with black thorns growing from its spine rises, snarling.', 'flags': 'f', 'align': -800, 'attack': 'bite',
         'desc': 'The forest\'s hounds, grown rather than born.'},
        {'id': 'thornmother', 'aliases': 'thornmother thorn mother', 'short': 'the Thornmother', 'role': 'champion', 'level': 90,
         'long': 'A woman of thorns and bark rises from her weaving, thorns bristling.', 'flags': 'bfl', 'align': -1000, 'sex': 2, 'attack': 'pierce',
         'desc': 'Sister to the grey dryad of the Hollow Wood, and far older. She grows the forest\'s soldiers from thorn.',
         'carry': [('thorn_crown', 100)]},
        {'id': 'weeping_maiden', 'aliases': 'maiden weeping banshee', 'short': 'a weeping maiden', 'role': 'elite', 'level': 89,
         'long': 'A woman in white lifts her face from her hands, and her weeping becomes a scream.', 'flags': 'f', 'align': -900, 'sex': 2, 'attack': 'blast',
         'desc': 'She mourns everyone the forest has taken. Her grief can kill.'},
        {'id': 'whisper_shade', 'aliases': 'shade whisper', 'short': 'a whisper shade', 'role': 'elite', 'level': 89,
         'long': 'A shadow detaches from the bark, whispering your name.', 'flags': 'f', 'align': -1000, 'attack': 'claw',
         'desc': 'The forest\'s voice given shape. It knows what you fear.'},
        {'id': 'root_horror', 'aliases': 'horror root', 'short': 'a root horror', 'role': 'elite', 'level': 89,
         'long': 'A knot of roots tears itself out of the tunnel wall and lunges.', 'flags': 'f', 'align': -900, 'attack': 'crush',
         'desc': 'Part of the forest\'s body, defending it.'},
        {'id': 'weeping_mother', 'aliases': 'mother weeping tree', 'short': 'the Weeping Mother', 'role': 'boss', 'level': 90,
         'long': 'The Weeping Mother stirs, a thousand faces in her bark opening their eyes at once.', 'flags': 'bfl', 'align': -1000, 'sex': 2, 'attack': 'crush',
         'desc': 'The first grove Nu\'Groth reached, ages ago, when the West was still green. Everything in this forest grew from her. She weeps without ceasing for what she has become, and she will make you part of her.',
         'carry': [('mother_seed', 100), ('heartwood_bow', 100)]},
    ],
    'objs': [
        {'id': 'silver_sword', 'kind': 'weapon', 'level': 90, 'attack': 'slash', 'aliases': 'sword silver paladin',
         'short': 'a paladin\'s silver sword', 'long': 'A silver sword, tarnished and wrapped in vines, lies here.', 'extra': 'i',
         'affects': [('hitroll', 5), ('damroll', 4)]},
        {'id': 'pierced_plate', 'kind': 'armor', 'slot': 'body', 'level': 90, 'aliases': 'plate pierced silver',
         'short': 'pierced silver plate', 'long': 'A suit of silver plate, holed by branches, lies here.', 'affects': [('hit', 50), ('save_spell', -3)]},
        {'id': 'thorn_crown', 'kind': 'armor', 'slot': 'head', 'level': 90, 'aliases': 'crown thorn',
         'short': 'a crown of black thorns', 'long': 'A crown of black thorns lies here.', 'affects': [('str', 2), ('damroll', 3)]},
        {'id': 'mother_seed', 'kind': 'worn', 'slot': 'neck', 'level': 92, 'aliases': 'seed mother',
         'short': 'a seed of the Weeping Mother', 'long': 'A seed the size of a fist, warm and faintly pulsing, lies here.',
         'affects': [('hit', 60), ('con', 2), ('wis', 2)]},
        {'id': 'heartwood_bow', 'kind': 'weapon', 'level': 92, 'attack': 'pierce', 'aliases': 'bow heartwood', 'two_handed': True,
         'short': 'a bow of weeping heartwood', 'long': 'A pale bow that drips sap like tears lies here.',
         'affects': [('hitroll', 6), ('damroll', 5)]},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
ZONE['rooms'] += [
    {'id': 'misted_pools', 'name': 'The Misted Pools', 'sector': 'forest',
     'desc': """North of the weeping pool a chain of small grey pools lies among the roots, mist
     rising from them in slow coils.  Lights drift in the mist, soft and inviting, and the
     bones at the edges of the pools show where people followed them.""",
     'exits': {'s': 'pool_edge'},
     'mobs': [('pool_wisp', 2)]},
    {'id': 'drowned_saplings', 'name': 'The Drowned Saplings', 'sector': 'forest',
     'desc': """South of the pool, young skin-trees grow from the flooded ground, thin and pale,
     their faces still small, still crying like infants.  Red sap pools between them.""",
     'exits': {'n': 'pool_edge'},
     'mobs': [('sap_ooze', 2)]},
    {'id': 'dead_orchard', 'name': 'The Orchard of the Dead', 'sector': 'forest',
     'desc': """West of the screaming fruit is an orchard in neat rows, planted by someone: every
     tree hung with bodies instead of fruit, swinging gently.  A tall figure in a straw hat
     walks between the rows with a scythe, harvesting.""",
     'exits': {'e': 'fruit_grove'},
     'mobs': [('fruit_swarm', 1), ('orchard_keeper', 1)]},
    {'id': 'knights_camp', 'name': "The Lost Knights' Camp", 'sector': 'forest',
     'desc': """North of the hanged knight lie the remains of his company's camp: rusted tents,
     a cold fire-pit, and his squires, grown into the trees around the clearing up to
     their waists.  They still hold their spears.  Their lord's banner hangs from a branch,
     rotting.""",
     'exits': {'s': 'hanged_glade'},
     'mobs': [('bound_squire', 2)], 'objs': [('paladin_banner', 1)]},
    {'id': 'white_lake', 'name': 'The White Lake', 'sector': 'water',
     'desc': """Beyond the glade of mourning lies a still lake of milk-white water, its shores
     lined with bone-white trees.  A woman stands in the shallows with her back to you,
     singing a lament, and the water around her is rippling with her grief.""",
     'exits': {'s': 'banshee_glade'},
     'mobs': [('lake_banshee', 1)]},
    {'id': 'thorn_kennels', 'name': 'The Thorn Kennels', 'sector': 'forest',
     'desc': """West of the thorn hollow, cages of woven thorn hold the litters of the thorn
     wolves.  The pups are already thorned, and they hurl themselves at the bars when you
     come near.""",
     'exits': {'e': 'thorn_hollow'},
     'mobs': [('thorn_wolf', 1), ('thorn_pup', 3)]},
    {'id': 'root_heart', 'name': 'The Root-Heart', 'sector': 'inside', 'flags': 'a',
     'desc': """Below the root maze the tunnels open into a hollow where all the forest's roots
     meet in a single knot as big as a house, beating slowly.  Each beat pushes red sap
     out through the veins of the forest.  Something stands guard before it.""",
     'exits': {'u': 'root_maze'},
     'mobs': [('vein_guardian', 1)]},
    {'id': 'buried_village', 'name': 'The Buried Village', 'sector': 'inside', 'flags': 'a',
     'desc': """West of the root maze, the roots have grown through a whole village and pulled it
     underground.  Houses hang in the root-walls, doors open, and their people sit inside
     at their tables, roots grown through their chairs and into their backs.""",
     'exits': {'e': 'root_maze'},
     'mobs': [('absorbed_villager', 3)]},
    {'id': 'cocoon_hall', 'name': 'The Hall of Cocoons', 'sector': 'forest',
     'desc': """North of the Mother the forest has made a hall of hanging cocoons, each with a
     sleeper inside, each sleeper slowly turning into wood.  A tender moves among them,
     checking, adjusting, humming a lullaby.""",
     'exits': {'s': 'heart_grove'},
     'mobs': [('cocoon_sleeper', 2), ('cocoon_tender', 1)]},
    {'id': 'seed_pits', 'name': 'The Seed Pits', 'sector': 'forest',
     'desc': """South of the Mother the earth is pocked with pits where her seeds fall and sprout.
     What grows from them is not trees.""",
     'exits': {'n': 'heart_grove'},
     'mobs': [('seed_horror', 2)]},
    {'id': 'cliff_path', 'name': 'The Cliff Path', 'sector': 'mountain',
     'desc': """A narrow path climbs the black cliff north of the forest's edge toward the
     Bastion's outer walls.  The Bastion's scouts use it to watch the forest, and they are
     watching you.""",
     'exits': {'s': 'forest_end'},
     'mobs': [('bastion_scout', 2)]},
    {'id': 'burnt_siegeworks', 'name': 'The Burnt Siegeworks', 'sector': 'field',
     'desc': """South of the forest's edge lie the burned remains of siege engines, trebuchets and
     towers that an eastern army built to break the Black Bastion, long ago.  It never got
     to use them.  Its soldiers walk among the wreckage still, grey and transparent,
     loading engines that are not there.""",
     'exits': {'n': 'forest_end'},
     'mobs': [('siege_ghost', 2)]},
]
ZONE['mobs'] += [
    {'id': 'pool_wisp', 'aliases': 'wisp pool light', 'short': 'a pool wisp', 'role': 'standard', 'level': 87,
     'long': 'A soft light drifts out of the mist, and behind it, teeth.', 'flags': 'f', 'align': -800, 'attack': 'blast',
     'desc': 'A lure of the forest, leading travellers into the pools.'},
    {'id': 'orchard_keeper', 'aliases': 'keeper orchard scarecrow', 'short': 'the orchard keeper', 'role': 'elite', 'level': 88,
     'long': 'The orchard keeper turns, a scarecrow of bark and straw with a scythe.', 'flags': 'bfl', 'align': -900, 'attack': 'slash',
     'desc': 'It tends the orchard and harvests what grows there.',
     'carry': [('orchard_scythe', 40)]},
    {'id': 'bound_squire', 'aliases': 'squire bound', 'short': 'a tree-bound squire', 'role': 'standard', 'level': 88,
     'long': 'A squire grown into a tree up to his waist levels his spear at you.', 'flags': 'bf', 'align': -500, 'attack': 'pierce',
     'desc': 'He followed his lord west. He followed him into the forest. He is still following.'},
    {'id': 'lake_banshee', 'aliases': 'banshee lake woman', 'short': 'the banshee of the white lake', 'role': 'champion', 'level': 90,
     'long': 'The banshee of the white lake turns, and her lament becomes a scream.', 'flags': 'bfl', 'align': -1000, 'sex': 2, 'attack': 'blast',
     'desc': 'The first of the weeping maidens, the paladin\'s bride, who followed him west and found him hanging.',
     'carry': [('wedding_veil', 100)]},
    {'id': 'thorn_pup', 'aliases': 'pup thorn wolf', 'short': 'a thorn wolf pup', 'role': 'standard', 'level': 86,
     'long': 'A thorned wolf pup hurls itself at you.', 'flags': 'f', 'align': -700, 'attack': 'bite',
     'desc': 'Small, savage and already spiked.'},
    {'id': 'vein_guardian', 'aliases': 'guardian vein', 'short': 'the vein guardian', 'role': 'champion', 'level': 90,
     'long': 'The vein guardian tears itself from the root-heart, a giant of knotted root and sap.', 'flags': 'bfl', 'align': -900, 'attack': 'crush',
     'desc': 'The forest\'s heart, defending itself.',
     'carry': [('heartwood_shield', 100)]},
    {'id': 'absorbed_villager', 'aliases': 'villager absorbed', 'short': 'an absorbed villager', 'role': 'standard', 'level': 87,
     'long': 'A villager rises from her table, roots tearing from her back.', 'flags': 'f', 'align': -700, 'attack': 'claw',
     'desc': 'Pulled under with her house, and part of the forest now.'},
    {'id': 'cocoon_sleeper', 'aliases': 'sleeper cocoon', 'short': 'a cocoon sleeper', 'role': 'standard', 'level': 88,
     'long': 'A cocoon splits, and a half-wooden thing climbs out.', 'flags': 'f', 'align': -800, 'attack': 'claw',
     'desc': 'Halfway to becoming a tree, and angry to be woken.'},
    {'id': 'cocoon_tender', 'aliases': 'tender cocoon', 'short': 'a cocoon tender', 'role': 'elite', 'level': 89,
     'long': 'A many-armed tender stops humming and turns toward you.', 'flags': 'bfl', 'align': -900, 'attack': 'claw',
     'desc': 'It cares for the sleepers, and it would like to care for you.',
     'carry': [('cocoon_silk', 40)]},
    {'id': 'seed_horror', 'aliases': 'horror seed', 'short': 'a seed horror', 'role': 'elite', 'level': 89,
     'long': 'Something sprouted from the Mother\'s seed heaves itself out of a pit.', 'flags': 'f', 'align': -1000, 'attack': 'crush',
     'desc': 'A child of the Weeping Mother, grown wrong.'},
    {'id': 'bastion_scout', 'aliases': 'scout bastion', 'short': 'a Bastion scout', 'role': 'elite', 'level': 89,
     'long': 'A Bastion scout in black leather draws two curved knives.', 'flags': 'f', 'align': -1000, 'attack': 'slash',
     'desc': 'One of the Bastion\'s eyes, sent to watch the forest for anything coming west.'},
    {'id': 'siege_ghost', 'aliases': 'ghost siege soldier', 'short': 'a siege ghost', 'role': 'elite', 'level': 89,
     'long': 'A grey soldier looks up from loading an engine that is not there.', 'flags': 'f', 'align': -500, 'attack': 'hit',
     'desc': 'A soldier of the eastern army that came to break the Bastion. He does not know he failed.'},
]
ZONE['objs'] += [
    {'id': 'orchard_scythe', 'kind': 'weapon', 'level': 88, 'attack': 'slash', 'two_handed': True, 'aliases': 'scythe orchard',
     'short': "the orchard keeper's scythe", 'long': 'A long scythe with a bark handle lies here.', 'affects': [('damroll', 4)]},
    {'id': 'paladin_banner', 'kind': 'treasure', 'level': 85, 'aliases': 'banner paladin rotting',
     'short': "a paladin's rotting banner", 'long': "A paladin's rotting banner hangs from a branch.", 'cost': 6000,
     'extras': {'banner': 'A silver sword on blue, the arms of the knight who hangs in the glade. Bring it east and someone in Midgaard will weep for it.'}},
    {'id': 'wedding_veil', 'kind': 'worn', 'slot': 'about', 'level': 90, 'aliases': 'veil wedding white',
     'short': 'a white wedding veil', 'long': 'A white wedding veil lies here, wet with tears.', 'affects': [('wis', 2), ('mana', 50), ('save_spell', -3)]},
    {'id': 'heartwood_shield', 'kind': 'armor', 'slot': 'shield', 'level': 91, 'aliases': 'shield heartwood',
     'short': 'a heartwood shield', 'long': 'A shield of living heartwood lies here, faintly pulsing.', 'affects': [('hit', 40)]},
    {'id': 'cocoon_silk', 'kind': 'armor', 'slot': 'about', 'level': 89, 'aliases': 'silk cocoon cloak',
     'short': 'a cloak of cocoon silk', 'long': 'A grey cloak of cocoon silk lies here.', 'affects': [('hit', 30), ('save_spell', -2)]},
]
