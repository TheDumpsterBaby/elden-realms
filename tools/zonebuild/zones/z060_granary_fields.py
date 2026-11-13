"""The Granary Fields -- support ring, levels 3-10.

The farms north of Midgaard's east gate that feed the garrison, worked under
military requisition. The first sign that the West reaches even here: a rot is
spreading through the stored grain, and the rats grow fat and strange on it.
"""

ZONE = {
    'num': 60, 'name': 'The Granary Fields', 'builders': 'Claude', 'lifespan': 15,
    'rooms': [
        {'id': 'lane', 'name': 'A Muddy Lane North of the East Gate', 'sector': 'field',
         'desc': """A lane of trampled mud leads north from Midgaard's east gate between low
         stone walls.  Carts heavy with sacks creak past toward the fort, each one
         escorted by a soldier with a tally board.  Beyond the walls, fields of grey
         wheat ripple in the wind.""",
         'exits': {'s': {'to': '@3053', 'back_desc': 'A muddy lane leads north toward the Granary Fields.'}, 'n': 'lane_north'},
         'mobs': [('farmhand', 2)]},
        {'id': 'lane_north', 'name': 'The Lane, Between the Walls', 'sector': 'field',
         'desc': """The lane narrows between dry-stone walls furred with lichen.  A wooden
         sign nailed to a post reads BY ORDER OF THE GARRISON: ALL GRAIN TO THE FORT.
         Someone has carved a crude skull beneath the words.""",
         'exits': {'n': 'crossroads'},
         'extras': {'sign post skull': 'BY ORDER OF THE GARRISON: ALL GRAIN TO THE FORT. HOARDERS WILL HANG. Below, a carved skull with grain spilling from its mouth.'}},
        {'id': 'crossroads', 'name': 'The Field Crossroads', 'sector': 'field',
         'desc': """Four tracks meet around a stone trough where carters water their oxen.
         To the west stands a requisition post flying Midgaard's grey banner, the
         farmhouse and its barn lie to the north, the mill wheel turns slowly to the
         east, and wheat stretches away in every direction.""",
         'exits': {'w': 'post', 'n': 'farm_yard', 'e': 'millrace', 'u': 'trough_wall'},
         'objs': [('trough', 1)],
         'mobs': [('ox', 2)]},
        {'id': 'trough_wall', 'name': 'On Top of the Field Wall', 'sector': 'field',
         'desc': """From the top of the old wall you can see the whole valley: grey fields,
         the dark bulk of the granary, the fort's towers to the south.  To the
         west, beyond the walls of Midgaard, the sky is stained a sickly brown that
         the farmers will not talk about.""",
         'extras': {'west sky stain': 'A smudge of brown and black low on the western horizon. The farmhands call it the Weather and spit when they say it.'}},
        {'id': 'post', 'name': 'The Requisition Post', 'sector': 'inside', 'flags': 'd',
         'desc': """A timber hut with a counter across its front where farmers hand over
         their harvest.  A soldier weighs each sack on a great iron scale while a
         clerk writes in a ledger.  Nobody is paid.  A list of hoarders hangs
         beside the door, and some names have been crossed through in red.""",
         'extras': {'list hoarders names': 'A list of farm families who held back grain. The crossed-out names are the ones who were hanged.'},
         'mobs': [('requisition_officer', 1), ('requisition_soldier', 2)]},
        {'id': 'farm_yard', 'name': 'The Farmhouse Yard', 'sector': 'field',
         'desc': """A yard of packed earth between a long stone farmhouse and a sagging barn.
         Chickens scratch in the dirt, and a dog on a chain watches you without
         barking.  The farmhouse windows are boarded, and a child's face appears at
         a crack and vanishes.""",
         'exits': {'s': 'crossroads', 'w': 'farmhouse', 'n': 'barn', 'e': 'well'},
         'mobs': [('chained_dog', 1), ('chicken', 3)]},
        {'id': 'farmhouse', 'name': 'Inside the Farmhouse', 'sector': 'inside', 'flags': 'd',
         'desc': """A single long room smelling of woodsmoke and boiled turnips.  A family of
         six shares one table and almost no food.  The father's chair is empty; his
         boots stand by the door where he left them the day he was taken west for
         the wall.""",
         'mobs': [('farmwife', 1), ('farm_child', 2)]},
        {'id': 'barn', 'name': 'The Sagging Barn', 'sector': 'inside', 'flags': 'd',
         'desc': """Tools hang on pegs and broken harness lies in heaps.  The air is thick
         with dust and the smell of wet hay.  Something has been at the feed bins:
         the wood is gnawed through and grain lies scattered, grey and furred with
         mould.""",
         'exits': {'u': 'loft'},
         'objs': [('pitchfork', 1)],
         'mobs': [('field_rat', 3)]},
        {'id': 'loft', 'name': 'The Barn Loft', 'sector': 'inside', 'flags': 'd',
         'desc': """Hay is piled high under the roof beams.  Pigeons shift and mutter in the
         rafters.  A hollow has been made in the hay, with a blanket and a stub of
         candle; someone has been hiding up here, and recently.""",
         'mobs': [('runaway_conscript', 1)]},
        {'id': 'well', 'name': 'The Farm Well', 'sector': 'field',
         'desc': """A stone well with a bucket on a frayed rope.  The water at the bottom is
         dark and smells faintly of rot.  The farmers still drink it, because there
         is nothing else, and because the soldiers drink the clean water from the
         fort's cisterns.""",
         'exits': {'e': 'wheat_east'},
         'objs': [('farm_well', 1)]},
        {'id': 'wheat_east', 'name': 'The Eastern Wheatfield', 'sector': 'field',
         'desc': """Wheat stands chest high, its ears grey instead of gold.  When you push
         through it the stalks crumble into dust that catches in your throat.  The
         reapers who should be working here have gone west to the wall, and the
         harvest is rotting where it stands.""",
         'exits': {'n': 'scarecrow_field', 'e': 'hedge'},
         'mobs': [('field_rat', 2), ('crow', 2)]},
        {'id': 'scarecrow_field', 'name': 'The Scarecrow Field', 'sector': 'field',
         'desc': """A ring of scarecrows stands in the middle of the field, more than any farm
         would need.  They are dressed in old Midgaard uniforms.  Up close their
         sackcloth faces are stained dark, and the straw that sticks out of their
         sleeves moves when there is no wind.""",
         'exits': {'w': 'wheat_north'},
         'extras': {'scarecrows uniforms faces': 'The uniforms are real. One still has a name stitched inside the collar: BRANNIC, 3RD COMPANY.'},
         'mobs': [('scarecrow', 3)]},
        {'id': 'wheat_north', 'name': 'The Northern Wheatfield', 'sector': 'field',
         'desc': """The wheat is flattened here in a wide spiral, as if something large lay
         down in it and turned around many times.  At the centre of the spiral the
         earth is bare and black.  Nothing has grown back.""",
         'exits': {'w': 'orchard'},
         'mobs': [('crow', 2)]},
        {'id': 'orchard', 'name': 'The Old Orchard', 'sector': 'forest',
         'desc': """Gnarled apple trees grow in crooked rows, their branches heavy with small,
         hard fruit.  Many apples have fallen and rotted in the grass, and wasps
         drone over them.  A path leads deeper among the trees, where they grow
         closer together.""",
         'exits': {'n': 'orchard_deep', 's': 'barn_back'},
         'objs': [('apple', 3)],
         'mobs': [('wasp_swarm', 1)]},
        {'id': 'barn_back', 'name': 'Behind the Barn', 'sector': 'field',
         'desc': """A muddy strip between the back of the barn and the orchard fence, where
         the farm's rubbish is thrown.  Broken pots, bones and a smashed cradle lie
         in the nettles.  The barn's back wall has a hole gnawed through its base,
         wide enough for a cat.  Or a very large rat.""",
         'exits': {'w': {'to': 'barn', 'desc': 'A rat hole has been gnawed into the barn wall, and the rotten boards beside it give way to a push.'}},
         'mobs': [('field_rat', 2)]},
        {'id': 'orchard_deep', 'name': 'Deep in the Orchard', 'sector': 'forest',
         'desc': """The trees grow wild here and the light turns green and dim.  In a clearing
         an old apple tree has been hung with ribbons, bones and little dolls of
         twisted straw.  Someone has been leaving offerings, and the offerings are
         not to any god the Temple would name.""",
         'extras': {'dolls ribbons bones offerings': 'The straw dolls each have a single grey grain of wheat pushed into the head where the face should be.'},
         'mobs': [('hedge_witch', 1)]},
        {'id': 'millrace', 'name': 'The Millrace', 'sector': 'field',
         'desc': """A channel of fast brown water runs beside the track toward a great timber
         mill.  Its wheel groans as it turns.  Grey scum collects against the
         sluice gate, and dead fish turn slowly in an eddy, their eyes milky and
         white.""",
         'exits': {'e': 'mill', 'n': 'granary_yard'}},
        {'id': 'mill', 'name': 'The Mill Floor', 'sector': 'inside', 'flags': 'd',
         'desc': """Great millstones grind with a sound like distant thunder, and flour hangs
         in the air in drifting sheets.  The flour is the colour of ash.  A miller
         white with dust works the stones with a fixed and frantic attention,
         talking to nobody you can see.""",
         'exits': {'u': 'mill_loft'},
         'mobs': [('mad_miller', 1)]},
        {'id': 'mill_loft', 'name': 'The Mill Loft', 'sector': 'inside', 'flags': 'd',
         'desc': """Sacks of grain wait to be fed down the chute to the stones.  Several have
         split, and the grain inside is grey and soft, and it moves.  Pale grubs as
         long as a finger squirm through it and drop through the chute into the
         flour below.""",
         'mobs': [('rotgrub', 3)]},
        {'id': 'granary_yard', 'name': 'The Granary Yard', 'sector': 'field',
         'desc': """The great granary rises above the yard, a windowless barn of grey stone
         raised on squat pillars against damp and vermin.  The pillars have not
         stopped the vermin.  Soldiers guard the doors, but they stand well back
         from them and do not like the sounds inside.""",
         'exits': {'n': {'to': 'granary', 'door': 'doors door', 'state': 'closed', 'desc': 'The granary doors, barred from outside.'}},
         'mobs': [('granary_guard', 2)]},
        {'id': 'granary', 'name': 'Inside the Great Granary', 'sector': 'inside', 'flags': 'ad',
         'desc': """Mountains of grain rise into the darkness, the stores that keep the fort
         alive through winter.  The smell hits first: sweet, wet rot.  The grain
         shifts and whispers on its own, and in the gloom, small red eyes watch from
         every slope of it.""",
         'exits': {'d': 'cellar'},
         'mobs': [('blight_rat', 3)]},
        {'id': 'cellar', 'name': 'The Granary Undercroft', 'sector': 'inside', 'flags': 'ad',
         'desc': """Between the pillars beneath the granary, grain has leaked through the floor
         into heaps black with mould.  Tunnels lead off into the earth, wide
         enough to crawl through, their mouths ringed with grey slime.""",
         'exits': {'n': 'tunnels'},
         'mobs': [('blight_rat', 2), ('rotgrub', 2)]},
        {'id': 'tunnels', 'name': 'The Rat Tunnels', 'sector': 'inside', 'flags': 'ad',
         'desc': """You crawl on hands and knees through tunnels lined with packed grain and
         filth.  The walls are warm, and pulse faintly under your palms.  Ahead the
         tunnel opens into a chamber filled with a wet chittering, like a thousand
         teeth on wood.""",
         'exits': {'n': 'nest'},
         'mobs': [('blight_rat', 2)]},
        {'id': 'nest', 'name': 'The Heart of the Rot', 'sector': 'inside', 'flags': 'ad',
         'desc': """A chamber hollowed out of the earth beneath the granary, its floor a
         living carpet of rats.  At its centre writhes a knot of them, dozens of
         rats fused at the tails into a single heaving mass, and it is larger than
         a man.  Grey grain spills from its many mouths.""",
         'mobs': [('rat_king', 1)]},
        {'id': 'hedge', 'name': 'The Eastern Hedge', 'sector': 'field',
         'desc': """A thick hawthorn hedge marks the edge of the Granary Fields.  A gap has been
         hacked through it, and beyond the gap the smoke of hundreds of cookfires
         rises from the Refugee Camps.  A soldier's warning has been painted on a
         board: NO REFUGEES PAST THIS HEDGE.""",
         'mobs': [('hedge_sentry', 1)]},
    ],
    'mobs': [
        {'id': 'farmhand', 'aliases': 'farmhand worker', 'short': 'a gaunt farmhand', 'role': 'harmless', 'level': 3,
         'long': 'A gaunt farmhand trudges past with a sack on his back.', 'flags': 'g', 'align': 300, 'sex': 1,
         'desc': 'Too old or too young for the wall, he does the work of three men on half a ration.'},
        {'id': 'ox', 'aliases': 'ox oxen', 'short': 'a draught ox', 'role': 'standard', 'level': 4,
         'long': 'A draught ox drinks from the trough.', 'flags': 'b', 'align': 0, 'attack': 'crush',
         'desc': 'A huge, patient beast with its ribs showing.'},
        {'id': 'requisition_officer', 'aliases': 'officer requisition', 'short': 'the requisition officer', 'role': 'elite', 'level': 10,
         'long': 'The requisition officer watches the scale with narrowed eyes.', 'flags': 'b', 'align': 0, 'sex': 2,
         'desc': 'A severe woman in a clean grey uniform. She has hanged hoarders and she would do it again; the fort must eat.',
         'equip': [('officers_baton', 'wield', 100)]},
        {'id': 'requisition_soldier', 'aliases': 'soldier requisition', 'short': 'a requisition soldier', 'role': 'standard', 'level': 7,
         'long': 'A requisition soldier leans on his spear.', 'flags': 'm', 'align': 100, 'sex': 1,
         'desc': 'A bored young soldier, relieved to be guarding sacks instead of the wall.',
         'equip': [('short_spear', 'wield', 80)]},
        {'id': 'chained_dog', 'aliases': 'dog chained hound', 'short': 'a chained farm dog', 'role': 'standard', 'level': 4,
         'long': 'A farm dog on a chain watches you without barking.', 'flags': 'b', 'align': 0, 'attack': 'bite',
         'desc': 'A scarred brindle hound. It stopped barking a long time ago; there was no point.'},
        {'id': 'chicken', 'aliases': 'chicken hen', 'short': 'a scrawny hen', 'role': 'harmless', 'level': 1,
         'long': 'A scrawny hen scratches in the dirt.', 'flags': 'b', 'align': 0, 'attack': 'bite',
         'desc': 'There is hardly any meat on her. That is the only reason she is still alive.'},
        {'id': 'farmwife', 'aliases': 'farmwife woman mother', 'short': 'the farmwife', 'role': 'harmless', 'level': 5,
         'long': 'A hollow-eyed farmwife stirs a pot of thin soup.', 'flags': 'b', 'align': 500, 'sex': 2,
         'desc': 'She was handsome once. Now she counts turnips at night and listens for soldiers at the door.',
         'carry': [('turnip_soup', 100)]},
        {'id': 'farm_child', 'aliases': 'child farm', 'short': 'a farm child', 'role': 'harmless', 'level': 1,
         'long': 'A farm child stares at you from behind the table.', 'flags': 'b', 'align': 600,
         'desc': 'Thin, silent and watchful. Children do not play much in the Granary Fields any more.'},
        {'id': 'field_rat', 'aliases': 'rat field', 'short': 'a field rat', 'role': 'standard', 'level': 3,
         'long': 'A field rat as big as a cat scurries through the grain.', 'flags': 'fg', 'align': -100, 'attack': 'bite',
         'desc': 'Too big, too bold, and its fur is patchy and grey with mould.'},
        {'id': 'runaway_conscript', 'aliases': 'conscript runaway boy', 'short': 'a runaway conscript', 'role': 'standard', 'level': 5,
         'long': 'A boy in a too-big uniform cowers in the hay.', 'flags': 'b', 'align': 200, 'sex': 1,
         'desc': 'He ran from his first march west. If the requisition soldiers find him, he will hang beside the hoarders.',
         'equip': [('rusty_shortsword', 'wield', 100)]},
        {'id': 'crow', 'aliases': 'crow', 'short': 'a crow', 'role': 'harmless', 'level': 2,
         'long': 'A crow picks at the grey wheat.', 'flags': 'g', 'align': 0, 'attack': 'bite',
         'desc': 'Even the crows look thin.'},
        {'id': 'scarecrow', 'aliases': 'scarecrow straw', 'short': 'a scarecrow in a soldier\'s uniform', 'role': 'elite', 'level': 8,
         'long': 'A scarecrow in an old Midgaard uniform turns its sackcloth head toward you.', 'flags': 'bf', 'align': -600, 'attack': 'claw',
         'desc': 'Straw and rags and a soldier\'s coat, stitched together around something that was once a man. It does not breathe.',
         'carry': [('straw_hat', 30)]},
        {'id': 'wasp_swarm', 'aliases': 'wasps swarm', 'short': 'a swarm of wasps', 'role': 'standard', 'level': 6,
         'long': 'A swarm of wasps drones angrily over the rotting apples.', 'flags': 'bf', 'align': 0, 'attack': 'sting',
         'desc': 'Hundreds of fat yellow wasps, drunk on rotten fruit and furious about it.'},
        {'id': 'hedge_witch', 'aliases': 'witch hedge old woman', 'short': 'the hedge witch', 'role': 'champion', 'level': 8,
         'long': 'An old woman in a shawl of grey feathers ties a straw doll to the tree.', 'flags': 'bl', 'align': -700, 'sex': 2,
         'desc': 'She smiles with too many teeth. She says the Weather in the west is coming for everyone, and that the clever ones are making friends with it early.',
         'equip': [('witch_sickle', 'wield', 100)], 'carry': [('straw_doll', 100)]},
        {'id': 'mad_miller', 'aliases': 'miller mad', 'short': 'the miller', 'role': 'elite', 'level': 9,
         'long': 'The miller works the stones, muttering to someone who is not there.', 'flags': 'b', 'align': -200, 'sex': 1,
         'desc': 'White with grey flour from head to foot. His eyes are bloodshot and he has not slept. "It whispers in the grain," he tells you. "It says it is hungry."',
         'equip': [('miller_cleaver', 'wield', 100)]},
        {'id': 'rotgrub', 'aliases': 'rotgrub grub', 'short': 'a pale rotgrub', 'role': 'standard', 'level': 5,
         'long': 'A pale grub as long as your hand burrows through the grain.', 'flags': 'f', 'align': -300, 'attack': 'bite',
         'desc': 'A soft, eyeless thing with a ring of tiny teeth. Where it has eaten, the grain turns grey.'},
        {'id': 'granary_guard', 'aliases': 'guard granary soldier', 'short': 'a granary guard', 'role': 'standard', 'level': 8,
         'long': 'A granary guard stands well back from the doors, sweating.', 'flags': 'bm', 'align': 200, 'sex': 1,
         'desc': 'He has heard the sounds inside at night. He has asked for a transfer to the wall.',
         'equip': [('short_spear', 'wield', 100)]},
        {'id': 'blight_rat', 'aliases': 'rat blight grey', 'short': 'a blight rat', 'role': 'standard', 'level': 7,
         'long': 'A grey rat with weeping eyes hisses from the grain.', 'flags': 'fl', 'align': -500, 'attack': 'bite',
         'desc': 'Swollen and hairless in patches, its bite leaves wounds that turn grey at the edges.'},
        {'id': 'rat_king', 'aliases': 'king rat mass knot', 'short': 'the Rat King', 'role': 'champion', 'level': 10,
         'long': 'A writhing knot of fused rats, larger than a man, heaves itself toward you.', 'flags': 'bfl', 'align': -900, 'attack': 'bite',
         'desc': 'Dozens of rats bound at the tails into one creature, every mouth chewing, every eye red. The rot that is eating the fort\'s grain begins here, and something far to the west is feeding it.',
         'carry': [('rat_crown', 100), ('grey_grain', 100)]},
        {'id': 'hedge_sentry', 'aliases': 'sentry hedge soldier', 'short': 'a hedge sentry', 'role': 'standard', 'level': 9,
         'long': 'A sentry stands by the gap in the hedge, watching the camps.', 'flags': 'b', 'align': 100, 'sex': 2,
         'desc': 'Her orders are to keep the refugees out of the fields. She lets the children through when no one is looking.',
         'equip': [('short_spear', 'wield', 100)]},
    ],
    'objs': [
        {'id': 'trough', 'kind': 'fountain', 'aliases': 'trough stone', 'short': 'a stone trough',
         'long': 'A stone trough of brackish water stands by the crossroads.', 'liquid': 0},
        {'id': 'farm_well', 'kind': 'fountain', 'aliases': 'well', 'short': 'the farm well',
         'long': 'A stone well stands here, its water dark.', 'liquid': 0},
        {'id': 'pitchfork', 'kind': 'weapon', 'level': 4, 'attack': 'pierce', 'aliases': 'pitchfork fork',
         'short': 'a pitchfork', 'long': 'A pitchfork leans against the wall.', 'weight': 6},
        {'id': 'apple', 'kind': 'food', 'hours': 3, 'aliases': 'apple', 'short': 'a small hard apple',
         'long': 'A small, hard apple lies in the grass.', 'weight': 1, 'cost': 2},
        {'id': 'turnip_soup', 'kind': 'food', 'hours': 4, 'aliases': 'soup bowl turnip', 'short': 'a bowl of turnip soup',
         'long': 'A bowl of thin turnip soup sits here.', 'weight': 1, 'cost': 3},
        {'id': 'officers_baton', 'kind': 'weapon', 'level': 10, 'attack': 'bludgeon', 'aliases': 'baton officer',
         'short': "an officer's baton", 'long': "A black officer's baton lies here.", 'affects': [('hitroll', 1)]},
        {'id': 'short_spear', 'kind': 'weapon', 'level': 7, 'attack': 'pierce', 'aliases': 'spear short',
         'short': 'a short spear', 'long': 'A short spear lies here.'},
        {'id': 'rusty_shortsword', 'kind': 'weapon', 'level': 5, 'attack': 'slash', 'aliases': 'shortsword sword rusty',
         'short': 'a rusty shortsword', 'long': 'A rusty shortsword lies here.'},
        {'id': 'straw_hat', 'kind': 'armor', 'slot': 'head', 'level': 5, 'aliases': 'hat straw',
         'short': 'a battered straw hat', 'long': 'A battered straw hat lies here.'},
        {'id': 'witch_sickle', 'kind': 'weapon', 'level': 9, 'attack': 'slash', 'aliases': 'sickle witch black',
         'short': 'a black iron sickle', 'long': 'A sickle of black iron lies here.', 'affects': [('damroll', 1)]},
        {'id': 'straw_doll', 'kind': 'worn', 'slot': 'neck', 'level': 8, 'aliases': 'doll straw',
         'short': 'a straw doll on a cord', 'long': 'A small straw doll on a cord lies here.',
         'affects': [('wis', 1), ('save_spell', -1)],
         'extras': {'doll straw grain': 'A grey grain of wheat is pressed into its head. It is faintly warm.'}},
        {'id': 'miller_cleaver', 'kind': 'weapon', 'level': 9, 'attack': 'slash', 'aliases': 'cleaver miller',
         'short': "the miller's cleaver", 'long': 'A heavy cleaver dusted with grey flour lies here.'},
        {'id': 'rat_crown', 'kind': 'armor', 'slot': 'head', 'level': 11, 'aliases': 'crown rat bone',
         'short': 'a crown of rat bones', 'long': 'A crude crown woven from tiny bones lies here.',
         'affects': [('dex', 1), ('hit', 10)]},
        {'id': 'grey_grain', 'kind': 'treasure', 'level': 10, 'aliases': 'grain grey handful', 'short': 'a handful of grey grain',
         'long': 'A handful of grey grain lies here, stirring faintly.', 'weight': 1, 'cost': 1,
         'extras': {'grain grey': 'Each grain is soft and warm. Held close to the ear, it seems to whisper. The physicians at the Hospice would want to see this.'}},
    ],
}
