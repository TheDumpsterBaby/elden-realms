"""W2 The Hollow Wood -- the March, levels 35-40.

An old forest west of the Burned Marches that has gone quiet and wrong. The
darkness is inside the trees now; the beasts are turning, the foresters are
hollowed, and at its heart the forest's ancient guardian has been made into
something terrible. No stronghold.
"""

ZONE = {
    'num': 201, 'name': 'The Hollow Wood', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'eaves', 'name': 'Under the Eaves of the Hollow Wood', 'sector': 'forest',
         'desc': """The burned trees of the Marches give way to living ones, tall and grey-barked,
         their branches knitting overhead.  The light turns dim and green.  It is
         very quiet; no birds, no insects, not even wind.  The road runs on west,
         narrowing to a track.""",
         'exits': {'e': {'to': '@20029', 'back_desc': 'The road runs on west under the eaves of the Hollow Wood.'}, 'w': 'track1'}},
        {'id': 'track1', 'name': 'The Forest Track', 'sector': 'forest',
         'desc': """The track winds between trunks so thick that three men could not link arms
         around them.  Moss hangs from the branches in grey curtains.  Your
         footsteps sound too loud, and you have the feeling, every few paces, that
         something has just stopped moving.""",
         'exits': {'w': 'track2', 'n': 'woodcutter_clearing', 's': 'fern_hollow'},
         'mobs': [('quiet_stalker', 1)]},
        {'id': 'woodcutter_clearing', 'name': "The Woodcutters' Clearing", 'sector': 'forest',
         'desc': """A clearing where woodcutters worked: stumps, stacked logs, a lean-to of
         bark.  Their axes are still buried in a half-felled tree.  The tree is
         bleeding a thick grey sap from the cut, and the sap has crept down the
         trunk and across the ground toward the lean-to.""",
         'exits': {'n': 'cutters_hut', 'w': 'sap_trees'},
         'mobs': [('hollow_forester', 2)]},
        {'id': 'cutters_hut', 'name': "The Woodcutters' Hut", 'sector': 'inside', 'flags': 'd',
         'desc': """A low hut of logs and turf.  Bunks for six men, a table with six bowls of
         porridge gone grey with mould, six pairs of boots by the door.  The men
         who wore them walk the wood now, still carrying their axes, still
         working.""",
         'extras': {'bowls porridge boots': 'The bowls were never finished. The spoons are still in them.'},
         'mobs': [('hollow_forester', 1)]},
        {'id': 'sap_trees', 'name': 'The Bleeding Grove', 'sector': 'forest',
         'desc': """Every tree in this grove weeps grey sap from cracks in its bark.  The sap
         pools between the roots and gives off a sweet, cloying smell.  Insects
         that land in it do not die; they twitch, and slowly turn grey, and walk
         away.""",
         'exits': {'w': 'dead_stream'},
         'mobs': [('sap_crawler', 3)]},
        {'id': 'fern_hollow', 'name': 'The Fern Hollow', 'sector': 'forest',
         'desc': """A dip in the forest floor filled with ferns taller than a man.  They close
         behind you as you push through, and the track is lost at once.  The ferns
         move against the stillness of the air, parting and closing as something
         low and quick passes through them.""",
         'exits': {'w': 'spider_thicket', 's': 'deer_run'},
         'mobs': [('thornback_boar', 1)]},
        {'id': 'deer_run', 'name': 'The Deer Run', 'sector': 'forest',
         'desc': """A narrow path beaten by deer runs between the trees.  The deer that made it
         are here: a herd standing among the trunks, perfectly still, all facing
         west.  Their eyes are milky grey.  When you come closer, every head turns
         toward you at once.""",
         'exits': {'w': 'stag_glade'},
         'mobs': [('hollow_deer', 3)]},
        {'id': 'stag_glade', 'name': 'The Glade of the Antlered Stones', 'sector': 'forest',
         'desc': """A glade ringed by old standing stones carved with antlers, where the people
         of the wood once worshipped the forest's guardian.  The carvings have been
         defaced, scratched over with grey spirals.  The grass in the glade is
         dead, and in its centre lies a huge stag's skull, freshly cleaned.""",
         'exits': {'n': 'old_way'},
         'extras': {'stones antlers carvings': 'The Antlered One, guardian of the wood. Under the spirals someone has scratched: HE HAS BEEN TAKEN.'},
         'mobs': [('hollow_deer', 2)]},
        {'id': 'track2', 'name': 'The Forest Track, Hanging Moss', 'sector': 'forest',
         'desc': """The moss hangs so thickly here that you push through it like curtains.  It
         is damp and cold and clings to your skin.  Things are tangled in it: a
         bird's skeleton, a child's mitten, a wooden charm on a string, turning
         slowly.""",
         'exits': {'w': 'track3', 'n': 'spider_thicket'},
         'mobs': [('moss_lurker', 1)]},
        {'id': 'spider_thicket', 'name': 'The Webbed Thicket', 'sector': 'forest',
         'desc': """Webs as thick as rope span the gaps between the trees, white and grey and
         heavy with wrapped shapes.  Some of the shapes are deer.  Some are not.
         The webs tremble constantly, though there is no wind, and the trembling
         grows stronger as you go deeper.""",
         'exits': {'w': 'brood_hollow'},
         'mobs': [('greyweb_spider', 3)]},
        {'id': 'brood_hollow', 'name': 'The Brood Hollow', 'sector': 'forest', 'flags': 'a',
         'desc': """Beneath a tangle of roots the webs form a domed chamber, dark as night.  Egg
         sacs the size of barrels hang from the roots, pulsing.  On the far side of
         the chamber, something huge shifts its many legs and the whole web sways.""",
         'mobs': [('brood_mother', 1), ('greyweb_spider', 2)]},
        {'id': 'track3', 'name': 'The Forest Track, Fallen Giant', 'sector': 'forest',
         'desc': """An enormous tree has fallen across the track, its roots torn out of the earth
         and standing higher than a house.  You climb over the trunk.  The hollow
         under the roots is full of bones, gnawed and stacked with unsettling care.""",
         'exits': {'w': 'forest_shrine', 'd': 'root_hollow'},
         'mobs': [('quiet_stalker', 1)]},
        {'id': 'root_hollow', 'name': 'Under the Roots', 'sector': 'inside', 'flags': 'ad',
         'desc': """You crawl into the pit beneath the fallen tree's roots.  The bones are piled
         in neat spirals, skulls at the centre of each.  This is a larder, and a
         shrine, and the creature that keeps it is coming back; you can hear it
         breathing in the passage behind the roots.""",
         'mobs': [('bone_keeper', 1)]},
        {'id': 'dead_stream', 'name': 'The Dead Stream', 'sector': 'swim',
         'desc': """A stream runs through the wood, clear as glass and utterly lifeless.  No
         weed grows in it, no fish swim in it, and the stones on its bed are bleached
         white.  The water is so cold it aches.  Grey sap drips into it from the
         trees on the bank.""",
         'exits': {'w': 'old_mill', 's': 'track3'},
         'mobs': [('stream_wight', 1)]},
        {'id': 'old_mill', 'name': 'The Forester\'s Mill', 'sector': 'inside', 'flags': 'd',
         'desc': """A small sawmill on the stream, its wheel still turning in the dead water.
         The saw blade runs back and forth on its own, cutting nothing.  Sawdust lies
         deep on the floor, grey, and footprints lead through it to a ladder.""",
         'exits': {'u': 'mill_loft'},
         'mobs': [('hollow_forester', 2)]},
        {'id': 'mill_loft', 'name': 'The Mill Loft', 'sector': 'inside', 'flags': 'd',
         'desc': """The forester who ran the mill lives up here still, after a fashion.  He has
         carved a hundred small figures of wood and set them all around the loft,
         facing west.  Each one is a person he knew.  He is carving another one now,
         and he does not look up.""",
         'mobs': [('mad_forester', 1)]},
        {'id': 'forest_shrine', 'name': 'The Wayside Shrine of the Wood', 'sector': 'forest',
         'desc': """A small roofed shrine stands beside the track, where travellers once left
         offerings for safe passage.  The offerings are rotted.  The carved figure
         inside, a robed woman with a lantern, has had its face chiselled off and
         replaced with a smooth grey stone.""",
         'exits': {'w': 'old_way', 'n': 'owl_tree'},
         'mobs': [('moss_lurker', 1)]},
        {'id': 'owl_tree', 'name': 'The Owl Tree', 'sector': 'forest',
         'desc': """A massive hollow oak stands alone in a ring of dead bracken.  Its trunk is
         split open like a door, and from inside come soft, low hoots, far too
         deep for any owl.  Pellets of fur and bone lie heaped around its roots,
         some of them the size of a man's head.""",
         'exits': {'u': 'owl_nest'},
         'mobs': [('grey_owl', 2)]},
        {'id': 'owl_nest', 'name': 'Inside the Hollow Oak', 'sector': 'forest', 'flags': 'a',
         'desc': """You climb up inside the hollow trunk into a great nest of branches and
         bones.  Eyes as big as plates open in the dark above you.  The owl that
         lives here is the size of a horse, its feathers grey and falling out in
         patches, its beak caked with old blood.""",
         'mobs': [('elder_owl', 1)]},
        {'id': 'old_way', 'name': 'The Old Way', 'sector': 'forest',
         'desc': """An ancient path paved with mossy stones runs west through the heart of the
         wood, older than the track and older than Midgaard.  The trees lean over
         it.  Here the silence is complete, a pressure in your ears, and the grey
         sap runs in rivulets between the paving stones.""",
         'exits': {'w': 'heart_approach'},
         'mobs': [('thornback_boar', 1), ('quiet_stalker', 1)]},
        {'id': 'heart_approach', 'name': 'The Approach to the Heartwood', 'sector': 'forest',
         'desc': """The trees grow closer and taller, and their bark has turned from grey to
         black.  Their roots break up through the paving.  Ahead, a wall of
         intertwined trunks forms a living barrier with a single dark opening, and
         from it comes a slow, deep sound, like breathing.""",
         'exits': {'w': 'heartwood', 'n': 'thorn_maze'},
         'mobs': [('heartwood_sentinel', 1)]},
        {'id': 'thorn_maze', 'name': 'The Thorn Maze', 'sector': 'forest',
         'desc': """Walls of black thorn rise higher than your head, and the paths between them
         twist back on themselves.  The thorns are long as daggers and wet with grey
         sap.  Torn cloth and old blood mark where others have tried to force a way
         through.""",
         'exits': {'n': 'thorn_heart', 'w': 'track_west'},
         'mobs': [('thornling', 3)]},
        {'id': 'thorn_heart', 'name': 'The Heart of the Thorns', 'sector': 'forest',
         'desc': """At the centre of the maze stands a tree that was once a woman, or a woman
         who was once a tree; her arms are branches and her hair is grey moss, and
         her face is twisted in endless pain.  The dryad of the Hollow Wood has
         been made the gardener of its thorns.""",
         'mobs': [('grey_dryad', 1)]},
        {'id': 'heartwood', 'name': 'The Heartwood', 'sector': 'forest', 'flags': 'a',
         'desc': """A vast chamber of living trees, their trunks fused into walls, their branches
         a roof so thick no light comes through.  In the centre stands the Antlered
         One, guardian of the wood for a thousand years: a stag-headed giant of root
         and bark.  The West has rotted it hollow, and grey fire burns in the cage of
         its ribs.""",
         'mobs': [('antlered_hollow', 1)]},
        {'id': 'track_west', 'name': 'The Western Edge of the Wood', 'sector': 'forest',
         'desc': """The trees thin out at last, and the track runs down a slope into low, wet
         ground.  The air changes, heavy with the smell of stagnant water and rot.
         Ahead, mist hangs over the Greywater Fens, and somewhere out in it a
         bell is tolling, slow and muffled.""",
         'mobs': [('hollow_deer', 1)]},
    ],
    'mobs': [
        {'id': 'quiet_stalker', 'aliases': 'stalker quiet', 'short': 'a quiet stalker', 'role': 'standard', 'level': 37,
         'long': 'Something grey and long-limbed freezes between the trunks, watching you.', 'flags': 'f', 'align': -700, 'attack': 'claw',
         'desc': 'Thin as a sapling, grey as bark, with too many joints in its arms. The wood went quiet when these came.'},
        {'id': 'hollow_forester', 'aliases': 'forester hollow woodcutter', 'short': 'a hollowed forester', 'role': 'standard', 'level': 36,
         'long': 'A hollowed forester chops at a tree that is not there.', 'flags': 'f', 'align': -700, 'sex': 1,
         'desc': 'Grey sap has crusted over his eyes and mouth. He still swings his axe, at trees, at air, at you.',
         'equip': [('forester_axe', 'wield', 80)]},
        {'id': 'sap_crawler', 'aliases': 'crawler sap insect', 'short': 'a sap crawler', 'role': 'standard', 'level': 35,
         'long': 'A beetle the size of a dog, crusted with grey sap, scuttles toward you.', 'flags': 'f', 'align': -500, 'attack': 'bite',
         'desc': 'It drank the grey sap and grew. It is still growing.'},
        {'id': 'thornback_boar', 'aliases': 'boar thornback', 'short': 'a thornback boar', 'role': 'elite', 'level': 38,
         'long': 'A huge boar with black thorns growing from its spine paws the ground.', 'flags': 'f', 'align': -500, 'attack': 'pierce',
         'desc': 'The thorns grow out through its hide. It is in constant pain, and it hates everything.',
         'carry': [('boar_tusk', 40)]},
        {'id': 'hollow_deer', 'aliases': 'deer hollow', 'short': 'a milky-eyed deer', 'role': 'standard', 'level': 35,
         'long': 'A deer with milky grey eyes stands perfectly still, facing west.', 'flags': 'f', 'align': -500, 'attack': 'pierce',
         'desc': 'Its flanks are sunken and its antlers are growing in strange, branching spirals.'},
        {'id': 'moss_lurker', 'aliases': 'lurker moss', 'short': 'a moss lurker', 'role': 'elite', 'level': 38,
         'long': 'A curtain of grey moss shifts and reaches for you.', 'flags': 'bf', 'align': -600, 'attack': 'whip',
         'desc': 'It looks like hanging moss until it moves. It wraps its prey and holds it until it stops struggling.'},
        {'id': 'greyweb_spider', 'aliases': 'spider greyweb', 'short': 'a greyweb spider', 'role': 'standard', 'level': 37,
         'long': 'A grey spider as big as a wolf picks its way along a web.', 'flags': 'f', 'align': -600, 'attack': 'bite',
         'desc': 'Its body is bloated and grey, its bite carries a venom that numbs and greys the flesh.'},
        {'id': 'brood_mother', 'aliases': 'brood mother spider', 'short': 'the Brood Mother', 'role': 'champion', 'level': 39,
         'long': 'A spider the size of a cart rises from her web, mandibles clicking.', 'flags': 'bfl', 'align': -800, 'attack': 'bite',
         'desc': 'Ancient and enormous, her abdomen swollen with eggs. The West has made her fertile beyond nature, and her children are spreading east.',
         'carry': [('spider_silk_cloak', 100)]},
        {'id': 'bone_keeper', 'aliases': 'keeper bone', 'short': 'the bone keeper', 'role': 'champion', 'level': 39,
         'long': 'A hunched thing of bark and bone crawls out of the passage behind the roots.', 'flags': 'bfl', 'align': -900, 'attack': 'claw',
         'desc': 'It collects bones and arranges them in spirals, an offering to the voice in the West. It wants yours for the centre of a new one.',
         'carry': [('bone_spiral_charm', 100)]},
        {'id': 'stream_wight', 'aliases': 'wight stream', 'short': 'a stream wight', 'role': 'elite', 'level': 38,
         'long': 'A pale shape rises from the clear, dead water.', 'flags': 'bf', 'align': -800, 'attack': 'claw',
         'desc': 'A drowned traveller, white as the bleached stones. The cold of the stream lives in its touch.'},
        {'id': 'mad_forester', 'aliases': 'forester mad', 'short': 'the mad forester', 'role': 'elite', 'level': 39,
         'long': 'The mad forester carves a small wooden figure, humming.', 'flags': 'b', 'align': -400, 'sex': 1,
         'desc': 'He is not hollowed, not yet; he carved and carved to hold on to himself. "Everyone is going west," he says. "I am making them so I remember."',
         'equip': [('carving_knife', 'wield', 100)], 'carry': [('wooden_figure', 100)]},
        {'id': 'grey_owl', 'aliases': 'owl grey', 'short': 'a grey owl', 'role': 'standard', 'level': 36,
         'long': 'A grey owl as big as an eagle watches from a branch, head turning.', 'flags': 'f', 'align': -400, 'attack': 'claw',
         'desc': 'Silent and huge, its feathers patchy. It hunts in daylight now.'},
        {'id': 'elder_owl', 'aliases': 'owl elder', 'short': 'the elder owl', 'role': 'champion', 'level': 39,
         'long': 'An owl the size of a horse spreads moulting grey wings above you.', 'flags': 'bfl', 'align': -600, 'attack': 'claw',
         'desc': 'The oldest creature in the wood after the Antlered One. It was wise once. Now it only hungers.',
         'carry': [('owl_feather_cap', 100)]},
        {'id': 'heartwood_sentinel', 'aliases': 'sentinel heartwood treant', 'short': 'a heartwood sentinel', 'role': 'elite', 'level': 40,
         'long': 'A tree beside the opening uproots itself and steps forward.', 'flags': 'bf', 'align': -700, 'attack': 'crush',
         'desc': 'A guardian of black wood, its bark split by grey cracks, its eyes knots of sap.'},
        {'id': 'thornling', 'aliases': 'thornling thorn', 'short': 'a thornling', 'role': 'standard', 'level': 38,
         'long': 'A small figure woven of black thorns unfolds from the hedge.', 'flags': 'f', 'align': -700, 'attack': 'pierce',
         'desc': 'The dryad grows them from the maze. They are all thorns and spite.'},
        {'id': 'grey_dryad', 'aliases': 'dryad grey', 'short': 'the grey dryad', 'role': 'champion', 'level': 40,
         'long': 'A dryad of black wood and grey moss twists toward you, weeping sap.', 'flags': 'bfl', 'align': -800, 'sex': 2, 'attack': 'whip',
         'desc': 'She was the wood\'s gentlest spirit. Now she grows thorns for the West, and every thorn costs her agony.',
         'carry': [('dryad_tear', 100)]},
        {'id': 'antlered_hollow', 'aliases': 'antlered hollow guardian stag', 'short': 'the Antlered Hollow', 'role': 'boss', 'level': 40,
         'long': 'The Antlered Hollow lowers its vast rotting crown toward you, grey fire blazing in its ribs.', 'flags': 'bfl', 'align': -1000, 'attack': 'pierce',
         'desc': 'For a thousand years the Antlered One kept the wood. Nu\'Groth reached into its heart and hollowed it, and now the whole forest obeys a guardian of rot. Its antlers scrape the roof of living trees.',
         'equip': [('antler_crown', 'head', 100)], 'carry': [('heartwood_staff', 100)]},
    ],
    'objs': [
        {'id': 'forester_axe', 'kind': 'weapon', 'level': 36, 'attack': 'slash', 'aliases': 'axe forester',
         'short': 'a forester\'s axe', 'long': 'A forester\'s axe crusted with grey sap lies here.'},
        {'id': 'boar_tusk', 'kind': 'weapon', 'level': 38, 'attack': 'pierce', 'aliases': 'tusk boar dagger',
         'short': 'a boar-tusk dagger', 'long': 'A dagger made from a huge tusk lies here.', 'affects': [('damroll', 1)]},
        {'id': 'spider_silk_cloak', 'kind': 'armor', 'slot': 'about', 'level': 40, 'aliases': 'cloak silk spider',
         'short': 'a cloak of grey spider silk', 'long': 'A shimmering cloak of grey silk lies here.', 'affects': [('dex', 2), ('save_para', -2)]},
        {'id': 'bone_spiral_charm', 'kind': 'worn', 'slot': 'wrist', 'level': 39, 'aliases': 'charm bone spiral bracelet',
         'short': 'a bracelet of spiralled bones', 'long': 'A bracelet of tiny spiralled bones lies here.', 'affects': [('hitroll', 2), ('hit', 15)]},
        {'id': 'carving_knife', 'kind': 'weapon', 'level': 38, 'attack': 'pierce', 'aliases': 'knife carving',
         'short': 'a carving knife', 'long': 'A small, very sharp carving knife lies here.'},
        {'id': 'wooden_figure', 'kind': 'treasure', 'level': 38, 'aliases': 'figure wooden carving', 'short': 'a small wooden figure',
         'long': 'A small carved figure of a person lies here.', 'weight': 1, 'cost': 50,
         'extras': {'figure wooden carving': 'A carefully carved woman with a basket. On the base: MARTA, WHO WENT WEST.'}},
        {'id': 'owl_feather_cap', 'kind': 'armor', 'slot': 'head', 'level': 40, 'aliases': 'cap feather owl',
         'short': 'a cap of grey owl feathers', 'long': 'A cap of grey feathers lies here.', 'affects': [('wis', 1), ('int', 1)]},
        {'id': 'dryad_tear', 'kind': 'worn', 'slot': 'neck', 'level': 40, 'aliases': 'tear dryad amber',
         'short': 'a dryad\'s tear', 'long': 'A drop of amber-grey sap, hard as glass, lies here.', 'affects': [('mana', 40), ('save_spell', -2)]},
        {'id': 'antler_crown', 'kind': 'armor', 'slot': 'head', 'level': 41, 'aliases': 'crown antler',
         'short': 'the antler crown', 'long': 'A crown of black antler lies here.', 'affects': [('str', 2), ('hit', 30)]},
        {'id': 'heartwood_staff', 'kind': 'weapon', 'level': 41, 'attack': 'bludgeon', 'aliases': 'staff heartwood', 'two_handed': True,
         'short': 'a staff of black heartwood', 'long': 'A staff of black heartwood, warm to the touch, lies here.',
         'affects': [('hitroll', 3), ('damroll', 3), ('mana', 25)]},
    ],
}
