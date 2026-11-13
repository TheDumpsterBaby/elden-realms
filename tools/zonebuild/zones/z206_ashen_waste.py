"""W7 The Ashen Waste -- the Blight, levels 60-65.

Where the Blight begins: a grey dead land where nothing grows, swept by ash
storms. A petrified forest, plains of fused glass, a dead lake, a tribe of
hollowed ash-eaters, and beneath it all the Ashen Wyrm. No refuge.
"""

ZONE = {
    'num': 206, 'name': 'The Ashen Waste', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'waste_edge', 'name': 'The Threshold of the Waste', 'sector': 'field',
         'desc': """The last grey grass gives out and the ground turns to ash, fine and deep as
         snow.  The sky is the colour of slate and the sun is a dull coin behind it.
         There is no sound at all.  Every step leaves a print that the wind fills in
         behind you within moments.""",
         'exits': {'e': {'to': '@20524', 'back_desc': 'West, the dead ground gives way to the Ashen Waste.'}, 'w': 'ash_dunes'},
         'mobs': [('ash_drifter', 1)]},
        {'id': 'ash_dunes', 'name': 'The Ash Dunes', 'sector': 'field',
         'desc': """Dunes of grey ash roll away to the horizon, rippled by the wind.  You sink to
         the ankle with every step.  Things are buried in the dunes: the top of a
         wagon wheel, the tip of a spire, a hand reaching up out of the ash, grey and
         perfectly still.""",
         'exits': {'w': 'glass_plain', 'n': 'petrified_edge', 's': 'caravan_wreck'},
         'mobs': [('ash_drifter', 2), ('blight_worm', 1)]},
        {'id': 'caravan_wreck', 'name': 'The Last Caravan', 'sector': 'field',
         'desc': """A caravan of a dozen wagons lies half buried in the ash, its oxen turned to
         grey stone in their traces.  The drivers sit on their benches, also stone,
         their faces frozen in the moment they looked west and saw what was coming.
         The cargo has been looted by something with claws.""",
         'exits': {'w': 'ash_eater_camp'},
         'extras': {'drivers stone faces': 'Each face is frozen mid-scream. They looked west, and the Blight looked back.'},
         'mobs': [('stone_scavenger', 2)]},
        {'id': 'ash_eater_camp', 'name': 'The Camp of the Ash-Eaters', 'sector': 'field',
         'desc': """Low shelters of bone and hide crouch in a hollow between dunes.  The tribe that
         lives here eats ash, because there is nothing else, and it has changed them:
         grey-skinned, black-eyed, their teeth worn to stumps.  They worship the thing
         beneath the dead lake.""",
         'exits': {'w': 'chief_hut', 's': 'ash_pit'},
         'mobs': [('ash_eater', 3)]},
        {'id': 'chief_hut', 'name': 'The Ash-Chief\'s Hut', 'sector': 'inside', 'flags': 'd',
         'desc': """A hut of whale-sized bones roofed with grey hide.  Inside, a fire of bones burns
         without smoke.  The ash-chief squats beside it, painted in white ash, a
         necklace of stone fingers around her throat.  Offerings for the Wyrm are
         heaped against the walls.""",
         'mobs': [('ash_chief', 1), ('ash_eater', 1)]},
        {'id': 'ash_pit', 'name': 'The Feeding Pit', 'sector': 'field',
         'desc': """A pit dug in the ash where the tribe throws its sacrifices for the Wyrm.  The
         bottom is out of sight, and warm air rises from it, smelling of embers.  Now
         and then the ash at the bottom heaves, and something vast turns over far
         below.""",
         'exits': {'d': 'worm_tunnel'},
         'mobs': [('ash_eater', 1)]},
        {'id': 'worm_tunnel', 'name': 'The Worm Tunnels', 'sector': 'inside', 'flags': 'ad',
         'desc': """A round tunnel bored through packed ash and stone, its walls glazed smooth by
         the heat of whatever made it.  It is wide enough for a wagon.  The air is
         hot and the walls tremble.  Smaller tunnels branch off in every direction,
         and things move in them.""",
         'exits': {'w': 'worm_nest', 'n': 'glazed_tunnel'},
         'mobs': [('blight_worm', 2)]},
        {'id': 'worm_nest', 'name': 'The Worm Nest', 'sector': 'inside', 'flags': 'ad',
         'desc': """A cavern full of eggs, each one the size of a man, ribbed and grey and warm.
         Worms the length of a horse coil among them, guarding.  The largest, its
         body ringed with plates of fused glass, rears up and opens a mouth lined with
         rows of teeth.""",
         'mobs': [('worm_mother', 1), ('blight_worm', 1)]},
        {'id': 'glazed_tunnel', 'name': 'The Glazed Tunnel', 'sector': 'inside', 'flags': 'ad',
         'desc': """The tunnel climbs, its walls glazed to black glass by enormous heat.  Your own
         reflection follows you in the walls, distorted.  Sometimes the reflection does
         not move when you do.  The tunnel climbs out onto the shore of the dead lake.""",
         'exits': {'u': 'lake_shore'},
         'mobs': [('glass_shade', 1)]},
        {'id': 'petrified_edge', 'name': 'The Edge of the Stone Forest', 'sector': 'forest',
         'desc': """A forest stands here, every tree turned to grey stone, every leaf, every bird
         on every branch.  The stone trees creak in the wind as though they still
         remember being wood.  A deer stands frozen mid-leap in a clearing, and its
         stone eyes follow you.""",
         'exits': {'w': 'stone_heart'},
         'mobs': [('stone_stalker', 2)]},
        {'id': 'stone_heart', 'name': 'The Heart of the Stone Forest', 'sector': 'forest',
         'desc': """In the heart of the petrified forest, a village of woodcutters was caught in the
         moment the Blight passed over it: a woman with a bucket, children chasing a
         dog, a man splitting logs, all grey stone.  Their stone faces are turned west,
         and all of them are weeping.""",
         'exits': {'w': 'gorgon_grove'},
         'extras': {'villagers stone faces weeping': 'Stone tears on stone cheeks. If you touch them, they are wet.'},
         'mobs': [('stone_stalker', 1)]},
        {'id': 'gorgon_grove', 'name': 'The Grove of Stone Eyes', 'sector': 'forest',
         'desc': """A grove where the stone trees grow in a ring around a pool of grey water.
         Figures of every kind stand frozen around the pool: soldiers, beasts, a
         knight on horseback.  The thing that made them lives in the pool, and it is
         rising, and you must not look at its face.""",
         'mobs': [('blight_basilisk', 1)]},
        {'id': 'glass_plain', 'name': 'The Glass Plain', 'sector': 'field',
         'desc': """The ash gives way to a plain of black glass, fused by some fire so hot it
         melted the earth itself.  It stretches for leagues, cracked and jagged.  The
         sun glares off it.  Shapes are trapped in the glass beneath your feet:
         people, horses, a whole marching column, frozen running.""",
         'exits': {'w': 'obelisks', 's': 'storm_flats'},
         'mobs': [('glass_shade', 2)]},
        {'id': 'storm_flats', 'name': 'The Storm Flats', 'sector': 'field',
         'desc': """A flat plain where the ash storms are born.  Pillars of whirling grey ash walk
         across it like giants, crackling with lightning.  When one passes close, the
         air is full of stinging grit and voices, the screaming of everyone the Blight
         has burned.""",
         'exits': {'w': 'lake_shore'},
         'mobs': [('ash_storm', 2)]},
        {'id': 'obelisks', 'name': 'The Bone Obelisks', 'sector': 'field',
         'desc': """A line of obelisks marches across the waste, each one built of fused bones and
         taller than a tower.  They mark the road the West's armies march east.
         Grey fire burns at the top of each, and as you pass beneath them, you feel
         them looking down at you.""",
         'exits': {'w': 'road_west', 's': 'lake_shore'},
         'mobs': [('obelisk_warden', 1), ('ash_drifter', 1)]},
        {'id': 'lake_shore', 'name': 'The Shore of the Dead Lake', 'sector': 'field',
         'desc': """A lake once lay here, wide and blue.  Now it is a basin of grey cracked mud
         and salt, ringed by the bleached skeletons of boats.  In the centre of the
         basin the ground has collapsed into a vast crater, and a column of black
         smoke rises from it, unmoving in the wind.""",
         'exits': {'w': 'lake_bed'},
         'mobs': [('ash_storm', 1)]},
        {'id': 'lake_bed', 'name': 'The Dead Lake Bed', 'sector': 'field',
         'desc': """You walk out across the cracked lake bed toward the crater.  The heat rises
         through your boots.  Bones of fish as big as boats lie half buried in the
         salt.  The crater's edge is close now, and you can hear breathing from it,
         slow and vast, like a bellows.""",
         'exits': {'d': 'wyrm_lair'},
         'mobs': [('blight_worm', 1), ('ash_drifter', 1)]},
        {'id': 'wyrm_lair', 'name': 'The Crater of the Ashen Wyrm', 'sector': 'inside',
         'desc': """You descend into the crater, a pit of glazed rock and hot ash a hundred paces
         across.  Coiled in its depths, its body as thick as a tower and grey as the
         waste, lies the Ashen Wyrm.  It burned the lake dry when it came, and the
         waste is its breath.  One eye opens, as big as a door, burning grey.""",
         'mobs': [('ashen_wyrm', 1)]},
        {'id': 'road_west', 'name': 'The Army Road', 'sector': 'field',
         'desc': """A road beaten flat by the march of countless feet runs west between the
         obelisks.  The ash on it is trodden hard as stone.  Ahead, on the horizon,
         rise the black walls and broken towers of a great city, and over it hangs a
         cloud of flies so thick it looks like smoke.""",
         'mobs': [('ash_drifter', 1)]},
    ],
    'mobs': [
        {'id': 'ash_drifter', 'aliases': 'drifter ash', 'short': 'an ash drifter', 'role': 'standard', 'level': 61,
         'long': 'A shape of drifting ash in the form of a man walks toward you against the wind.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Everyone the Blight burned in the waste walks here still, as grey ash held together by hatred.'},
        {'id': 'blight_worm', 'aliases': 'worm blight', 'short': 'a blight worm', 'role': 'standard', 'level': 63,
         'long': 'A grey worm as long as a wagon bursts up out of the ash.', 'flags': 'f', 'align': -600, 'attack': 'bite',
         'desc': 'Blind, armoured in grey rings, its mouth a funnel of teeth. It hunts by the vibration of footsteps.'},
        {'id': 'stone_scavenger', 'aliases': 'scavenger stone', 'short': 'a stone scavenger', 'role': 'standard', 'level': 62,
         'long': 'A lean grey beast with stone-crusted claws picks through the wreck.', 'flags': 'f', 'align': -500, 'attack': 'claw',
         'desc': 'Half lizard, half hound, its hide crusted with grey stone. It eats the stone dead.'},
        {'id': 'ash_eater', 'aliases': 'ash-eater eater ash tribesman', 'short': 'an ash-eater', 'role': 'standard', 'level': 62,
         'long': 'An ash-eater with black eyes and grey skin bares worn teeth at you.', 'flags': 'f', 'align': -800,
         'desc': 'The tribe ate the ash because there was nothing else, and the ash ate them back.',
         'equip': [('bone_club', 'wield', 70)]},
        {'id': 'ash_chief', 'aliases': 'chief ash', 'short': 'the ash-chief', 'role': 'champion', 'level': 65,
         'long': 'The ash-chief rises from the fire, stone fingers clicking at her throat.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'She speaks to the Wyrm, and it answers in her dreams. She feeds it her own people, and they thank her for it.',
         'equip': [('chief_spear', 'wield', 100)], 'carry': [('stone_finger_necklace', 100)]},
        {'id': 'worm_mother', 'aliases': 'mother worm', 'short': 'the worm mother', 'role': 'champion', 'level': 65,
         'long': 'A worm plated with fused glass rears over her eggs, mouth gaping.', 'flags': 'bfl', 'align': -700, 'attack': 'bite',
         'desc': 'The brood-mother of the waste\'s worms, armoured in glass from the fires.',
         'carry': [('glass_scale_shield', 100)]},
        {'id': 'glass_shade', 'aliases': 'shade glass', 'short': 'a glass shade', 'role': 'elite', 'level': 63,
         'long': 'A figure trapped in the glass tears itself free, its edges sharp as knives.', 'flags': 'f', 'align': -900, 'attack': 'slash',
         'desc': 'Someone who burned in the fire that made the glass, and became part of it.'},
        {'id': 'stone_stalker', 'aliases': 'stalker stone', 'short': 'a stone stalker', 'role': 'elite', 'level': 64,
         'long': 'A stone wolf steps down from its pedestal, grinding as it moves.', 'flags': 'f', 'align': -800, 'attack': 'bite',
         'desc': 'Turned to stone by the Blight, and then woken again by it, hungry and very hard to hurt.'},
        {'id': 'blight_basilisk', 'aliases': 'basilisk blight', 'short': 'the blight basilisk', 'role': 'champion', 'level': 65,
         'long': 'A huge grey lizard with too many legs rises from the pool, its eyes burning.', 'flags': 'bfl', 'align': -900, 'attack': 'bite',
         'desc': 'The thing that turns the living to stone. The Blight made it, and it made the forest.',
         'carry': [('basilisk_eye', 100)]},
        {'id': 'ash_storm', 'aliases': 'storm ash pillar', 'short': 'a walking ash storm', 'role': 'elite', 'level': 64,
         'long': 'A pillar of whirling ash and lightning bears down on you, screaming.', 'flags': 'f', 'align': -800, 'attack': 'blast',
         'desc': 'A storm with a will, full of the voices of the burned.'},
        {'id': 'obelisk_warden', 'aliases': 'warden obelisk', 'short': 'an obelisk warden', 'role': 'elite', 'level': 65,
         'long': 'A tall figure in bone armour stands at the foot of an obelisk, unmoving.', 'flags': 'bf', 'align': -1000,
         'desc': 'The wardens guard the army road. They do not sleep and they do not stop.',
         'equip': [('warden_pike', 'wield', 100)]},
        {'id': 'ashen_wyrm', 'aliases': 'wyrm ashen dragon', 'short': 'the Ashen Wyrm', 'role': 'boss', 'level': 65,
         'long': 'The Ashen Wyrm uncoils from the crater, grey fire leaking between its teeth.', 'flags': 'bfl', 'align': -1000, 'attack': 'blast',
         'desc': 'A serpent-dragon as long as a river, grey as the waste it made. It came from the West when the Blight was young and burned this country to ash with a single breath, and it sleeps here guarding the army road.',
         'carry': [('wyrm_heart', 100), ('wyrm_scale_mail', 100)]},
    ],
    'objs': [
        {'id': 'bone_club', 'kind': 'weapon', 'level': 62, 'attack': 'bludgeon', 'aliases': 'club bone',
         'short': 'a bone club', 'long': 'A heavy club of bone lies here.'},
        {'id': 'chief_spear', 'kind': 'weapon', 'level': 65, 'attack': 'pierce', 'aliases': 'spear chief glass',
         'short': 'a glass-tipped spear', 'long': 'A spear tipped with black glass lies here.', 'affects': [('hitroll', 3), ('damroll', 2)]},
        {'id': 'stone_finger_necklace', 'kind': 'worn', 'slot': 'neck', 'level': 65, 'aliases': 'necklace stone fingers',
         'short': 'a necklace of stone fingers', 'long': 'A necklace of grey stone fingers lies here.', 'affects': [('wis', 2), ('save_para', -4)]},
        {'id': 'glass_scale_shield', 'kind': 'armor', 'slot': 'shield', 'level': 65, 'aliases': 'shield glass scale',
         'short': 'a shield of glass scales', 'long': 'A shield of fused glass scales lies here.', 'affects': [('hit', 30)]},
        {'id': 'basilisk_eye', 'kind': 'worn', 'slot': 'hold', 'level': 65, 'aliases': 'eye basilisk',
         'short': 'a basilisk\'s eye', 'long': 'A grey eye, hard as stone, lies here, staring.', 'affects': [('int', 2), ('mana', 50)]},
        {'id': 'warden_pike', 'kind': 'weapon', 'level': 65, 'attack': 'pierce', 'aliases': 'pike warden bone', 'two_handed': True,
         'short': 'a bone pike', 'long': 'A long pike of fused bone lies here.', 'affects': [('damroll', 3)]},
        {'id': 'wyrm_heart', 'kind': 'worn', 'slot': 'hold', 'level': 67, 'aliases': 'heart wyrm ember',
         'short': 'the heart of the Ashen Wyrm', 'long': 'A grey ember the size of a fist, still beating, lies here.',
         'affects': [('str', 2), ('con', 2), ('hit', 50)]},
        {'id': 'wyrm_scale_mail', 'kind': 'armor', 'slot': 'body', 'level': 67, 'aliases': 'mail scale wyrm',
         'short': 'a coat of ashen wyrm scales', 'long': 'A coat of grey dragon scales lies here.', 'affects': [('hit', 40), ('save_spell', -3)]},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
# Appended, not inserted, so every existing vnum (and the W8 link) keeps its number.
ZONE['rooms'] += [
    {'id': 'glass_ruins', 'name': 'The Glass Ruins of Sarn', 'sector': 'field',
     'desc': """North of the glass plain rise the ruins of Sarn, a city that stood here when the
     waste was farmland.  Whatever came out of the West melted it where it stood.  Towers
     lean like candles left too near a fire, and the streets are rivers of black glass
     with shapes trapped inside them, people caught in mid-stride.""",
     'exits': {'s': 'glass_plain', 'w': 'glass_spire', 'n': 'glass_wells'},
     'mobs': [('glass_shade', 2)]},
    {'id': 'glass_spire', 'name': 'The Melted Spire', 'sector': 'inside',
     'desc': """Inside the tallest of Sarn's towers the stairs have run together into a smooth
     glass ramp that spirals up into darkness.  The walls are clear as water, and through
     them you see the waste outside bent and wrong.  Someone still lives here, at the top
     of the ramp, among books fused into bricks of glass.""",
     'mobs': [('glass_magister', 1)]},
    {'id': 'glass_wells', 'name': 'The Dry Wells of Sarn', 'sector': 'field',
     'desc': """A square of public wells, every one of them choked with ash.  Ropes still hang
     down into them, and when the wind blows the ropes sway as if something at the bottom
     were tugging.  Something is.""",
     'mobs': [('well_thing', 2)]},
    {'id': 'bone_dunes', 'name': 'The Bone Dunes', 'sector': 'field',
     'desc': """South of the storm flats the wind has heaped the ash into dunes, and the dunes are
     full of bones: cattle, horses, men, whole herds and armies, scoured white and stacked
     by the wind into shapes like waves.  Tall things stride along the dune crests on
     stilt-thin legs.""",
     'exits': {'n': 'storm_flats', 'w': 'sunken_shrine'},
     'mobs': [('dune_strider', 2)]},
    {'id': 'sunken_shrine', 'name': 'A Half-Buried Shrine', 'sector': 'inside',
     'desc': """The roof of a shrine pokes out of the ash, and you climb down through a broken
     window into its nave.  The god on the altar has had its face chiselled off, and a
     grey sun has been painted in its place.  A gaunt man in ash-grey rags preaches to an
     audience of skulls set in rows on the pews.""",
     'mobs': [('ash_prophet', 1)]},
    {'id': 'pilgrim_cairns', 'name': 'The Pilgrim Cairns', 'sector': 'field',
     'desc': """Beside the western road stand hundreds of small cairns, each topped with a grey
     stone.  Pilgrims from the east built them on their way west to give themselves to the
     Nu\'Groth, and some of them are still walking, grey-robed and barefoot, singing one
     long note.""",
     'exits': {'s': 'road_west'},
     'mobs': [('grey_pilgrim', 3)]},
    {'id': 'scorched_camp', 'name': 'A Scorched Army Camp', 'sector': 'field',
     'desc': """Rows of burned tents mark where the last army the east sent west made camp.  It got
     this far.  The tents are ash, the wagons are iron hoops, and the soldiers are still
     at their posts, black and cracked, their weapons in their hands.  Some of them turn
     their heads as you pass.""",
     'exits': {'n': 'road_west'},
     'mobs': [('ash_revenant', 2)], 'objs': [('scorched_standard', 1)]},
    {'id': 'salt_caves', 'name': 'The Salt Caves', 'sector': 'inside', 'flags': 'a',
     'desc': """Beneath the dry lake bed the old lake left caves of white salt that glitter in your
     light.  The air is so dry it cracks your lips.  Salt-crusted figures stand in the
     side passages, the dead of the lake, preserved and watching.""",
     'exits': {'n': 'lake_bed'},
     'mobs': [('salt_wight', 2)]},
]
ZONE['mobs'] += [
    {'id': 'glass_magister', 'aliases': 'magister glass mage', 'short': 'the Glass Magister', 'role': 'champion', 'level': 65,
     'long': 'The Glass Magister turns from his fused books, his skin clear as glass, his bones dark inside it.', 'flags': 'bfl', 'align': -900,
     'desc': 'The last mage of Sarn, who tried to bargain with the thing that melted his city. It let him live, and made him glass, and he has had a thousand years to regret it.',
     'carry': [('glass_staff', 100)]},
    {'id': 'well_thing', 'aliases': 'thing well rope', 'short': 'a thing from the well', 'role': 'standard', 'level': 63,
     'long': 'A long grey thing climbs out of a well, hand over hand up the rope.', 'flags': 'f', 'align': -900, 'attack': 'claw',
     'desc': 'It lived at the bottom of the wells when they ran dry. It is very thin and very hungry.'},
    {'id': 'dune_strider', 'aliases': 'strider dune', 'short': 'a dune strider', 'role': 'elite', 'level': 64,
     'long': 'A dune strider stalks along the crest on stilt-thin legs, twice the height of a man.', 'flags': 'f', 'align': -800, 'attack': 'pierce',
     'desc': 'A tall grey thing of bone and ash with a head like a heron. It spears its prey from above.'},
    {'id': 'ash_prophet', 'aliases': 'prophet ash', 'short': 'the ash prophet', 'role': 'standard', 'level': 63,
     'long': 'The ash prophet breaks off his sermon to the skulls and turns his burning eyes on you.', 'flags': 'bfl', 'align': -1000,
     'desc': 'A preacher of the grey sun who walked west to be taken and was found wanting. He has been preaching to the dead ever since.',
     'carry': [('ash_beads', 60)]},
    {'id': 'grey_pilgrim', 'aliases': 'pilgrim grey', 'short': 'a grey pilgrim', 'role': 'standard', 'level': 64,
     'long': 'A barefoot grey pilgrim walks west, singing, and turns to bless you with a knife.', 'flags': 'f', 'align': -800, 'attack': 'stab',
     'desc': 'Someone from the east who chose the West. Their feet are bloody and their eyes are happy.'},
    {'id': 'ash_revenant', 'aliases': 'revenant ash soldier', 'short': 'an ash revenant', 'role': 'elite', 'level': 65,
     'long': 'A burned soldier rises from his post, ash falling from his armour.', 'flags': 'f', 'align': -900,
     'desc': 'A soldier of the last army east, burned at his post and still standing his watch.',
     'equip': [('scorched_blade', 'wield', 40)]},
    {'id': 'salt_wight', 'aliases': 'wight salt', 'short': 'a salt wight', 'role': 'elite', 'level': 64,
     'long': 'A salt-crusted figure steps out of a side passage, crystals cracking at its joints.', 'flags': 'f', 'align': -900, 'attack': 'claw',
     'desc': 'One of the drowned of the dry lake, preserved in salt and given motion by the West.',
     'carry': [('salt_crown', 30)]},
]
ZONE['objs'] += [
    {'id': 'glass_staff', 'kind': 'weapon', 'level': 66, 'attack': 'bludgeon', 'two_handed': True, 'aliases': 'staff glass',
     'short': 'a staff of black glass', 'long': 'A staff of black glass lies here, something dark moving inside it.',
     'affects': [('mana', 40), ('int', 2)]},
    {'id': 'ash_beads', 'kind': 'worn', 'slot': 'neck', 'level': 63, 'aliases': 'beads prayer ash',
     'short': 'a string of ash prayer beads', 'long': 'A string of grey prayer beads lies here.', 'affects': [('wis', 1), ('save_spell', -2)]},
    {'id': 'scorched_blade', 'kind': 'weapon', 'level': 64, 'attack': 'slash', 'aliases': 'blade scorched sword',
     'short': 'a scorched sword', 'long': 'A blackened army sword lies here.', 'affects': [('hitroll', 3)]},
    {'id': 'salt_crown', 'kind': 'armor', 'slot': 'head', 'level': 64, 'aliases': 'crown salt',
     'short': 'a crown of salt crystal', 'long': 'A crown of white salt crystal lies here.', 'affects': [('hit', 25), ('con', 1)]},
    {'id': 'scorched_standard', 'kind': 'treasure', 'level': 60, 'aliases': 'standard banner scorched',
     'short': 'a scorched regimental standard', 'long': 'A scorched regimental standard leans against a burned wagon.', 'cost': 3000,
     'extras': {'standard banner': 'The banner of the Third of the East, burned to a rag. Midgaard would pay to have it home.'}},
]
