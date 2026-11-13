"""W8 Vel'Morrow, the Plague City -- the Blight, levels 65-70.

A great walled city that fell to the greyblight. Its people were not killed;
they were changed, and now serve Nu\'Groth. The Grey Choir that preaches in
Midgaard's refugee camps was born in this city's cathedral, and in the palace
the duchess has become the Mother of Flies. ("Vel'Morrow" is a working name.)
"""

ZONE = {
    'num': 207, 'name': "Vel'Morrow, the Plague City", 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'east_gate', 'name': 'The East Gate of Vel\'Morrow', 'sector': 'city',
         'desc': """The army road ends at a gate in black walls forty feet high.  The gate stands
         open, its doors torn from their hinges.  A cloud of flies hangs over the city
         so thick that the light comes through it brown.  The smell is beyond
         description.  Grey banners hang from every tower.""",
         'exits': {'e': {'to': '@20618', 'back_desc': 'The army road leads west to the black walls of Vel\'Morrow.'}, 'w': 'avenue'},
         'mobs': [('fly_swarm', 2)]},
        {'id': 'avenue', 'name': 'The Avenue of Lamps', 'sector': 'city',
         'desc': """A broad avenue once lit by a thousand lamps runs into the heart of the city.
         The lamp posts are hung with bodies now, wrapped in grey cocoons that
         twitch.  Grey figures walk the avenue in slow processions, ringing small
         bells, singing the Choir's long falling note.""",
         'exits': {'w': 'market', 'n': 'cathedral_steps', 's': 'plague_pits'},
         'mobs': [('plague_walker', 3)]},
        {'id': 'plague_pits', 'name': 'The Plague Pits', 'sector': 'city',
         'desc': """Great pits were dug in the city park when the plague began, to hold the dead.
         The pits are full, and the dead in them are not still; they writhe together
         into a single grey mass that heaves and breathes.  Corpse-carts still arrive
         to tip more into it.""",
         'exits': {'w': 'hospital'},
         'mobs': [('corpse_cart', 1), ('pit_mass', 1)]},
        {'id': 'hospital', 'name': 'The Hospital of Saint Orla', 'sector': 'inside', 'flags': 'd',
         'desc': """The city's great hospital, where the physicians fought the greyblight until
         they caught it themselves.  Wards of grey sleepers fill every hall, and the
         physicians still walk among them in their beaked masks, administering cures
         that are now the disease itself.""",
         'exits': {'d': 'sewer_e'},
         'mobs': [('plague_doctor', 2), ('grey_sleeper', 2)]},
        {'id': 'market', 'name': 'The Rot Market', 'sector': 'city',
         'desc': """The great market square is still busy.  Grey merchants sell grey goods to grey
         customers: rotting meat, bolts of cloth woven from hair, jars of whispering
         grain.  Coins change hands that are only discs of bone.  Nobody speaks.  The
         bells ring.""",
         'exits': {'w': 'noble_street', 'n': 'tannery'},
         'mobs': [('grey_merchant', 2), ('plague_walker', 2)]},
        {'id': 'tannery', 'name': 'The Flesh Tailor\'s Workshop', 'sector': 'inside', 'flags': 'd',
         'desc': """A tannery turned to a darker trade.  Hides hang drying on racks, and they are
         not animal hides.  Tables hold half-finished works: soldiers stitched from
         many bodies, a horse with too many legs.  The tailor works at the largest
         table, humming, needle flashing.""",
         'mobs': [('flesh_tailor', 1), ('stitched_soldier', 2)]},
        {'id': 'cathedral_steps', 'name': 'The Cathedral Steps', 'sector': 'city',
         'desc': """Wide steps climb to the great cathedral of Vel\'Morrow, its spires lost in the
         cloud of flies.  The saints on its facade have been chiselled away and replaced
         with spirals.  The Choir's note pours from the open doors, ten thousand voices,
         loud enough to shake the stones.""",
         'exits': {'n': 'nave'},
         'mobs': [('choir_zealot', 2)]},
        {'id': 'nave', 'name': 'The Nave of the Grey Choir', 'sector': 'inside', 'flags': 'd',
         'desc': """The cathedral's nave is packed with the faithful, standing shoulder to shoulder,
         mouths open in the endless note.  They face the altar, where a great spiral of
         grey stone has replaced the old god.  The Grey Choir was born here, and from
         here it sends its preachers east.""",
         'exits': {'n': 'chancel', 'd': 'crypt'},
         'mobs': [('choir_faithful', 3), ('choir_zealot', 1)]},
        {'id': 'chancel', 'name': 'The Chancel', 'sector': 'inside', 'flags': 'd',
         'desc': """Behind the altar, the Plague Bishop holds court on a throne of grey stone.  He
         was the city's bishop when the greyblight came, and he was the first to
         welcome it.  He conducts the Choir with a staff topped with a spiral, and the
         note bends to his will.""",
         'mobs': [('plague_bishop', 1)]},
        {'id': 'crypt', 'name': 'The Cathedral Crypt', 'sector': 'inside', 'flags': 'ad',
         'desc': """The crypt beneath the cathedral is full of grey cocoons hanging from the vaults
         like fruit.  Inside each one something is changing.  The cocoons split
         as you watch, and pale wet things climb out and unfold wings like a moth\'s.""",
         'mobs': [('grey_moth', 3)]},
        {'id': 'sewer_e', 'name': 'The Eastern Sewers', 'sector': 'inside', 'flags': 'ad',
         'desc': """A brick sewer runs beneath the city, its channel thick with grey sludge.  Rats
         swarm along the ledges in rivers.  The plague came up from here first, the
         physicians thought; it came from the grain stores, carried by the rats.""",
         'exits': {'w': 'sewer_w'},
         'mobs': [('plague_rat_swarm', 2)]},
        {'id': 'sewer_w', 'name': 'The Sewer Junction', 'sector': 'inside', 'flags': 'ad',
         'desc': """Several tunnels meet in a vaulted chamber where the sludge pools deep.  A nest
         of rats as big as dogs has been built here from rags and bones, and in its
         heart sits a rat the size of a bull, its fur fallen out, its skin a mass of
         grey sores.""",
         'exits': {'u': 'palace_cellars'},
         'mobs': [('plague_rat_swarm', 1), ('rat_lord', 1)]},
        {'id': 'noble_street', 'name': 'The Street of Lords', 'sector': 'city',
         'desc': """Grand houses line the street, their windows boarded from the inside.  The
         nobility of Vel\'Morrow locked themselves in when the plague came, and
         waited.  Their doors stand open now, and they walk the street in rotting
         silks, still proud, still cruel.""",
         'exits': {'w': 'palace_gate', 'n': 'manor'},
         'mobs': [('blighted_noble', 2)]},
        {'id': 'manor', 'name': 'A Lord\'s Manor', 'sector': 'inside', 'flags': 'd',
         'desc': """A great house of marble and gilt, its rooms still furnished, its tables still
         laid for a feast that rotted a year ago.  The lord of the house sits at the
         head of the table with his family, all of them grey, all of them eating
         something that is still moving.""",
         'mobs': [('blighted_noble', 2), ('grey_hound_noble', 1)]},
        {'id': 'palace_gate', 'name': 'The Palace Gate', 'sector': 'city',
         'desc': """The ducal palace rises behind a wall of white marble gone yellow and stained.
         Its gate is guarded by the duchess's household knights, grey and swollen in
         their armour, flies crawling in and out of their visors.  Through the bars you
         can see the palace, buzzing like a hive.""",
         'exits': {'w': 'palace_hall', 's': 'west_gate'},
         'mobs': [('plague_knight', 2)]},
        {'id': 'palace_cellars', 'name': 'The Palace Cellars', 'sector': 'inside', 'flags': 'ad',
         'desc': """Wine cellars beneath the palace, their racks smashed.  The floor is a carpet of
         maggots.  A stair leads up into the palace kitchens, and from above comes a
         buzzing so loud and deep it vibrates in your chest.""",
         'exits': {'u': 'palace_hall'},
         'mobs': [('maggot_mass', 1)]},
        {'id': 'palace_hall', 'name': 'The Great Hall of the Palace', 'sector': 'inside', 'flags': 'd',
         'desc': """A vast hall of marble columns, every surface crawling with flies.  The court of
         Vel\'Morrow stands frozen in a grey dance, swaying to music that is only the
         buzzing.  Doors of gilded bronze at the end of the hall stand open on the
         throne room.""",
         'exits': {'w': 'throne_room'},
         'mobs': [('grey_courtier', 3), ('plague_knight', 1)]},
        {'id': 'throne_room', 'name': 'The Throne Room of the Mother of Flies', 'sector': 'inside', 'flags': 'd',
         'desc': """The duchess of Vel\'Morrow sits on her throne, and she has grown.  She fills the
         dais, a vast bloated grey mass in the rags of a gown, her crown sunk into her
         swollen head, and from a thousand openings in her body pour the flies that
         blot out the sun.  She is the plague\'s heart.""",
         'mobs': [('mother_of_flies', 1)]},
        {'id': 'west_gate', 'name': 'The West Gate', 'sector': 'city',
         'desc': """The city's western gate opens onto a land of low grey hills.  The road beyond is
         lined with graves, endless rows of them, and every grave is open.  The wind
         from the west carries the sound of a vast army marching, very far away, and
         the clatter of bone.""",
         'mobs': [('plague_walker', 2)]},
    ],
    'mobs': [
        {'id': 'fly_swarm', 'aliases': 'flies swarm fly', 'short': 'a swarm of plague flies', 'role': 'standard', 'level': 66,
         'long': 'A swarm of fat grey flies boils toward you.', 'flags': 'f', 'align': -800, 'attack': 'sting',
         'desc': 'Each fly is the size of a thumb, and each carries the greyblight.'},
        {'id': 'plague_walker', 'aliases': 'walker plague', 'short': 'a plague walker', 'role': 'standard', 'level': 67,
         'long': 'A plague walker in grey rags rings a small bell, singing.', 'flags': 'f', 'align': -900,
         'desc': 'A citizen of Vel\'Morrow, changed. It sings the Choir\'s note and it wants you to sing too.'},
        {'id': 'corpse_cart', 'aliases': 'cart corpse', 'short': 'a corpse-cart', 'role': 'elite', 'level': 68,
         'long': 'A corpse-cart drawn by grey men creaks toward the pit.', 'flags': 'f', 'align': -900, 'attack': 'crush',
         'desc': 'The cart and the men who pull it have grown together into one thing.'},
        {'id': 'pit_mass', 'aliases': 'mass pit dead', 'short': 'the heaving pit mass', 'role': 'champion', 'level': 69,
         'long': 'The grey mass of the dead in the plague pit heaves and reaches for you with a hundred arms.', 'flags': 'bf', 'align': -1000, 'attack': 'claw',
         'desc': 'Thousands of the dead of Vel\'Morrow, run together into one breathing thing.'},
        {'id': 'plague_doctor', 'aliases': 'doctor plague physician', 'short': 'a plague doctor', 'role': 'elite', 'level': 68,
         'long': 'A plague doctor in a beaked mask raises a syringe of grey fluid.', 'flags': 'f', 'align': -800, 'sex': 1,
         'desc': 'Still trying to cure the sick. The cure is the disease now, and he does not know it.',
         'equip': [('grey_syringe', 'wield', 100)], 'carry': [('beaked_mask', 30)]},
        {'id': 'grey_sleeper', 'aliases': 'sleeper grey', 'short': 'a grey sleeper', 'role': 'standard', 'level': 66,
         'long': 'A grey sleeper sits up in its bed and opens black eyes.', 'flags': 'f', 'align': -800, 'attack': 'claw',
         'desc': 'Half changed, waking hungry.'},
        {'id': 'grey_merchant', 'aliases': 'merchant grey', 'short': 'a grey merchant', 'role': 'standard', 'level': 67,
         'long': 'A grey merchant holds out a jar of whispering grain.', 'flags': 'f', 'align': -800,
         'desc': 'He sells what the Choir wants spread. His prices are very reasonable.',
         'carry': [('grain_jar', 40)]},
        {'id': 'flesh_tailor', 'aliases': 'tailor flesh', 'short': 'the Flesh Tailor', 'role': 'champion', 'level': 70,
         'long': 'The Flesh Tailor looks up from her work, needle in hand, and smiles.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'Vel\'Morrow\'s finest seamstress once. Now she stitches soldiers for the West from the dead of the city, and she takes great pride in her work.',
         'equip': [('tailor_needle', 'wield', 100)], 'carry': [('stitched_gloves', 100)]},
        {'id': 'stitched_soldier', 'aliases': 'soldier stitched', 'short': 'a stitched soldier', 'role': 'elite', 'level': 69,
         'long': 'A soldier stitched together from many bodies lurches off the table.', 'flags': 'f', 'align': -1000,
         'desc': 'Four arms, two heads, and the strength of several men.'},
        {'id': 'choir_zealot', 'aliases': 'zealot choir', 'short': 'a Choir zealot', 'role': 'elite', 'level': 68,
         'long': 'A Choir zealot in grey robes swings a censer of grey smoke.', 'flags': 'f', 'align': -1000,
         'desc': 'The Choir\'s soldiers, who carry the note east with fire and blade.',
         'equip': [('zealot_flail', 'wield', 80)]},
        {'id': 'choir_faithful', 'aliases': 'faithful choir', 'short': 'one of the Choir faithful', 'role': 'standard', 'level': 66,
         'long': 'One of the Choir faithful turns from the altar, mouth still open in the note.', 'flags': 'f', 'align': -900,
         'desc': 'They have been singing for a year without stopping.'},
        {'id': 'plague_bishop', 'aliases': 'bishop plague', 'short': 'the Plague Bishop', 'role': 'champion', 'level': 70,
         'long': 'The Plague Bishop rises from his stone throne, raising a spiral staff.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'The founder of the Grey Choir, first to welcome the greyblight and the voice behind it. Every preacher in Midgaard\'s camps was ordained by his hand.',
         'equip': [('spiral_staff', 'wield', 100), ('bishop_mitre', 'head', 100)]},
        {'id': 'grey_moth', 'aliases': 'moth grey', 'short': 'a grey moth', 'role': 'standard', 'level': 68,
         'long': 'A moth the size of a man unfolds wet grey wings.', 'flags': 'f', 'align': -800, 'attack': 'claw',
         'desc': 'What the cocooned become. Its wings shed a dust that greys the flesh.'},
        {'id': 'plague_rat_swarm', 'aliases': 'rats swarm rat', 'short': 'a swarm of plague rats', 'role': 'standard', 'level': 67,
         'long': 'A river of grey rats pours along the ledge toward you.', 'flags': 'f', 'align': -600, 'attack': 'bite',
         'desc': 'The carriers of the plague, numberless and bold.'},
        {'id': 'rat_lord', 'aliases': 'lord rat', 'short': 'the rat lord', 'role': 'champion', 'level': 69,
         'long': 'A hairless rat the size of a bull rises from its nest.', 'flags': 'bfl', 'align': -900, 'attack': 'bite',
         'desc': 'Kin to the Rat King beneath Midgaard\'s granary, and far older. The plague spreads from its bite.',
         'carry': [('rat_lord_tail', 100)]},
        {'id': 'blighted_noble', 'aliases': 'noble blighted lord lady', 'short': 'a blighted noble', 'role': 'standard', 'level': 68,
         'long': 'A blighted noble in rotting silks looks down its nose at you.', 'flags': 'f', 'align': -1000,
         'desc': 'Proud in life, prouder in death, and hungrier.',
         'equip': [('rapier', 'wield', 70)]},
        {'id': 'grey_hound_noble', 'aliases': 'hound grey', 'short': 'a noble\'s grey hound', 'role': 'elite', 'level': 69,
         'long': 'A hunting hound with grey sores on its hide snarls by the table.', 'flags': 'f', 'align': -800, 'attack': 'bite',
         'desc': 'The lord\'s favourite, still loyal.'},
        {'id': 'plague_knight', 'aliases': 'knight plague', 'short': 'a plague knight', 'role': 'elite', 'level': 70,
         'long': 'A swollen grey knight stands guard, flies crawling from its visor.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'The duchess\'s household knights, sworn to her in life and bound to her in death.',
         'equip': [('plague_blade', 'wield', 80), ('swollen_plate', 'body', 30)]},
        {'id': 'maggot_mass', 'aliases': 'mass maggot maggots', 'short': 'a heaving mass of maggots', 'role': 'elite', 'level': 69,
         'long': 'The carpet of maggots rises into a heaving mound and rolls toward you.', 'flags': 'bf', 'align': -800, 'attack': 'bite',
         'desc': 'Millions of maggots moving as one.'},
        {'id': 'grey_courtier', 'aliases': 'courtier grey', 'short': 'a grey courtier', 'role': 'standard', 'level': 68,
         'long': 'A grey courtier sways in an endless dance.', 'flags': 'f', 'align': -1000,
         'desc': 'The court still dances for its duchess, as it danced on the night the plague came.'},
        {'id': 'mother_of_flies', 'aliases': 'mother flies duchess', 'short': 'the Mother of Flies', 'role': 'boss', 'level': 70,
         'long': 'The Mother of Flies heaves her vast bulk forward on the throne, and the air turns black with flies.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'Once the duchess of Vel\'Morrow, the most beautiful woman in the west. She opened her city to Nu\'Groth in exchange for eternal life, and she has it: a bloated, buzzing, endless life as the heart of the plague.',
         'carry': [('ducal_crown', 100), ('fly_mantle', 100)]},
    ],
    'objs': [
        {'id': 'grey_syringe', 'kind': 'weapon', 'level': 68, 'attack': 'pierce', 'aliases': 'syringe grey',
         'short': 'a syringe of grey fluid', 'long': 'A brass syringe of grey fluid lies here.'},
        {'id': 'beaked_mask', 'kind': 'armor', 'slot': 'head', 'level': 68, 'aliases': 'mask beaked',
         'short': 'a beaked plague mask', 'long': 'A beaked leather mask lies here.', 'affects': [('save_para', -4), ('con', 1)]},
        {'id': 'grain_jar', 'kind': 'treasure', 'level': 67, 'aliases': 'jar grain', 'short': 'a jar of whispering grain',
         'long': 'A jar of grey grain lies here, whispering.', 'weight': 2, 'cost': 50},
        {'id': 'tailor_needle', 'kind': 'weapon', 'level': 70, 'attack': 'pierce', 'aliases': 'needle tailor bone',
         'short': 'the Flesh Tailor\'s bone needle', 'long': 'A bone needle as long as a dagger lies here.', 'affects': [('hitroll', 4), ('dex', 1)]},
        {'id': 'stitched_gloves', 'kind': 'armor', 'slot': 'hands', 'level': 70, 'aliases': 'gloves stitched',
         'short': 'a pair of stitched gloves', 'long': 'A pair of finely stitched gloves lies here. You try not to think about what they are made of.',
         'affects': [('dex', 2), ('hitroll', 2)]},
        {'id': 'zealot_flail', 'kind': 'weapon', 'level': 68, 'attack': 'bludgeon', 'aliases': 'flail zealot',
         'short': 'a zealot\'s flail', 'long': 'A spiked flail lies here.'},
        {'id': 'spiral_staff', 'kind': 'weapon', 'level': 71, 'attack': 'bludgeon', 'aliases': 'staff spiral', 'two_handed': True,
         'short': 'the spiral staff', 'long': 'A staff topped with a grey stone spiral lies here.', 'affects': [('mana', 60), ('wis', 2), ('damroll', 3)]},
        {'id': 'bishop_mitre', 'kind': 'armor', 'slot': 'head', 'level': 70, 'aliases': 'mitre bishop',
         'short': 'a grey bishop\'s mitre', 'long': 'A tall grey mitre lies here.', 'affects': [('save_spell', -4), ('mana', 40)]},
        {'id': 'rat_lord_tail', 'kind': 'weapon', 'level': 69, 'attack': 'whip', 'aliases': 'tail rat whip',
         'short': 'a whip made from the rat lord\'s tail', 'long': 'A long, scaly whip lies here.', 'affects': [('damroll', 3)]},
        {'id': 'rapier', 'kind': 'weapon', 'level': 68, 'attack': 'pierce', 'aliases': 'rapier',
         'short': 'a noble\'s rapier', 'long': 'A slender rapier with a jewelled guard lies here.'},
        {'id': 'plague_blade', 'kind': 'weapon', 'level': 70, 'attack': 'slash', 'aliases': 'blade plague',
         'short': 'a plague knight\'s blade', 'long': 'A sword crusted with grey lies here.', 'affects': [('hitroll', 2)]},
        {'id': 'swollen_plate', 'kind': 'armor', 'slot': 'body', 'level': 70, 'aliases': 'plate swollen',
         'short': 'stretched plate armour', 'long': 'A suit of plate, warped as if something inside it swelled, lies here.'},
        {'id': 'ducal_crown', 'kind': 'armor', 'slot': 'head', 'level': 72, 'aliases': 'crown ducal',
         'short': 'the ducal crown of Vel\'Morrow', 'long': 'A crown of tarnished gold, sticky with something, lies here.',
         'affects': [('hit', 60), ('cha', 2), ('save_spell', -3)]},
        {'id': 'fly_mantle', 'kind': 'armor', 'slot': 'about', 'level': 72, 'aliases': 'mantle fly',
         'short': 'a mantle of iridescent wings', 'long': 'A mantle woven from thousands of fly wings lies here, shimmering.',
         'affects': [('dex', 2), ('move', 50), ('save_para', -3)]},
    ],
}

# ---------------------------------------------------------------- expansion (2026-11-13)
ZONE['rooms'] += [
    {'id': 'weavers_row', 'name': "Weavers' Row", 'sector': 'city',
     'desc': """A narrow street of weavers' shops south of the market.  The looms are still
     working: grey-skinned women sit at them weaving shrouds from thread spun out of
     their own hair, and the finished shrouds are stacked to the ceilings, waiting for a
     city's worth of dead.""",
     'exits': {'n': 'market', 's': 'orphanage'},
     'mobs': [('grey_weaver', 2)]},
    {'id': 'orphanage', 'name': 'The Orphanage of Saint Mera', 'sector': 'inside',
     'desc': """A long dormitory of tiny beds, each with a doll on its pillow.  The children of
     Vel'Morrow were brought here when their parents died, and the plague followed them.
     They are still here.  They play in the corners, grey and quiet, and when they see you
     they smile, all together, and get up.""",
     'mobs': [('grey_child', 4), ('matron_mera', 1)]},
    {'id': 'kings_garden', 'name': "The King's Plague Garden", 'sector': 'field',
     'desc': """The palace garden has run wild.  The roses are grey and swollen, and great pale
     flowers the size of shields have opened among the hedges, each with a body tangled in
     its roots.  The air is thick with spores that sting your eyes.""",
     'exits': {'s': 'palace_gate'},
     'mobs': [('corpse_flower', 2)]},
    {'id': 'bell_tower', 'name': 'The Cathedral Bell Tower', 'sector': 'inside',
     'desc': """A cold stone stair winds up inside the cathedral's bell tower.  Its walls are
     scratched with tally marks, one for every death the bell was rung for, until the
     ringer ran out of wall.  Something hunched sits on the stair above, holding a rope.""",
     'exits': {'e': 'cathedral_steps', 'u': 'belfry'},
     'mobs': [('bell_ringer', 1)]},
    {'id': 'belfry', 'name': 'The Belfry', 'sector': 'inside',
     'desc': """The great bell of Vel'Morrow hangs cracked in its frame, and carrion birds have
     nested in it by the hundred.  From here you can see the whole plague city spread
     beneath a yellow haze, and beyond its western wall, the white hills of bone.""",
     'mobs': [('carrion_flock', 2)]},
    {'id': 'ossuary', 'name': 'The Plague Ossuary', 'sector': 'inside', 'flags': 'a',
     'desc': """North of the crypt the dead were stacked when the graves were full: skulls in
     rows along the walls, long bones bundled like firewood, the whole city's dead sorted
     by size.  A figure in a beaked mask moves among them, still sorting.""",
     'exits': {'s': 'crypt'},
     'mobs': [('ossuary_keeper', 1)]},
    {'id': 'plague_cistern', 'name': 'The Plague Cistern', 'sector': 'water',
     'desc': """The sewer opens into the city's old cistern, where the plague first came into the
     water.  The bodies thrown in at the start of the sickness float here still, swollen
     to three times their size, and they bump gently against you as you wade.""",
     'exits': {'n': 'sewer_w'},
     'mobs': [('bloated_drowned', 2)]},
    {'id': 'quarantine', 'name': 'The Quarantine Ward', 'sector': 'inside',
     'desc': """A locked ward behind the hospital where the last of the sick were shut in and
     forgotten.  The door was nailed shut from the outside.  The patients are still in
     their beds, wrapped in grey sheets, and they sit up together when the door opens.""",
     'exits': {'n': 'hospital'},
     'mobs': [('quarantine_patient', 3), ('grey_sleeper', 1)]},
]
ZONE['mobs'] += [
    {'id': 'grey_weaver', 'aliases': 'weaver grey woman', 'short': 'a grey weaver', 'role': 'standard', 'level': 67,
     'long': 'A grey weaver rises from her loom, a shuttle sharp as a knife in her hand.', 'flags': 'f', 'align': -800, 'sex': 2, 'attack': 'stab',
     'desc': 'She weaves shrouds from her own hair, and she would like to measure you for one.'},
    {'id': 'grey_child', 'aliases': 'child grey orphan', 'short': 'a grey orphan', 'role': 'standard', 'level': 66,
     'long': 'A grey orphan smiles at you and reaches out its small hands.', 'flags': 'f', 'align': -900, 'attack': 'bite',
     'desc': 'A plague child, small and silent, with grey teeth and very strong hands.'},
    {'id': 'matron_mera', 'aliases': 'matron mera', 'short': 'Matron Mera', 'role': 'champion', 'level': 70,
     'long': 'Matron Mera rises from her rocking chair, tall and grey, her children gathering at her skirts.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
     'desc': 'The matron who would not leave her children when the plague came, and who loves them still, and who will not let anyone take them away.',
     'carry': [('mera_rosary', 100)]},
    {'id': 'corpse_flower', 'aliases': 'flower corpse bloom', 'short': 'a corpse bloom', 'role': 'elite', 'level': 69,
     'long': 'A great pale flower turns its face toward you, roots heaving out of the earth.', 'flags': 'bf', 'align': -800, 'attack': 'whip',
     'desc': 'A flower that grows from the dead and wants to grow from you.',
     'carry': [('grey_bloom', 25)]},
    {'id': 'bell_ringer', 'aliases': 'ringer bell hunched', 'short': 'the bell-ringer', 'role': 'elite', 'level': 68,
     'long': 'The hunched bell-ringer looks up from his rope, deaf and grinning.', 'flags': 'bfl', 'align': -800,
     'desc': 'He rang the bell for every death until there was no one left to hear it. He rings it now for you.',
     'carry': [('cracked_bell', 60)]},
    {'id': 'carrion_flock', 'aliases': 'flock carrion birds', 'short': 'a carrion flock', 'role': 'standard', 'level': 67,
     'long': 'A flock of carrion birds bursts out of the cracked bell, shrieking.', 'flags': 'f', 'align': -500, 'attack': 'pierce',
     'desc': 'Fat black birds, fed on a city.'},
    {'id': 'ossuary_keeper', 'aliases': 'keeper ossuary beaked masked', 'short': 'the ossuary keeper', 'role': 'elite', 'level': 69,
     'long': 'A figure in a beaked plague mask turns from its stacks of skulls.', 'flags': 'bfl', 'align': -900,
     'desc': 'The last plague doctor of Vel\'Morrow, sorting the dead forever.',
     'carry': [('plague_mask', 50)]},
    {'id': 'bloated_drowned', 'aliases': 'drowned bloated corpse', 'short': 'a bloated drowned', 'role': 'elite', 'level': 68,
     'long': 'A swollen corpse rolls over in the water and grabs at you.', 'flags': 'f', 'align': -800, 'attack': 'crush',
     'desc': 'One of the first dead of the plague, swollen with grey water.'},
    {'id': 'quarantine_patient', 'aliases': 'patient quarantine', 'short': 'a quarantined patient', 'role': 'standard', 'level': 66,
     'long': 'A patient in a grey sheet sits up in bed and swings its legs to the floor.', 'flags': 'f', 'align': -700, 'attack': 'claw',
     'desc': 'Sealed in to die. Did not.'},
]
ZONE['objs'] += [
    {'id': 'mera_rosary', 'kind': 'worn', 'slot': 'neck', 'level': 70, 'aliases': 'rosary mera',
     'short': "Saint Mera's rosary", 'long': 'A rosary of small grey beads lies here.', 'affects': [('wis', 2), ('hit', 20)]},
    {'id': 'grey_bloom', 'kind': 'worn', 'slot': 'hold', 'level': 69, 'aliases': 'bloom grey flower',
     'short': 'a grey bloom', 'long': 'A pale grey flower lies here, still breathing.', 'affects': [('mana', 25)]},
    {'id': 'cracked_bell', 'kind': 'worn', 'slot': 'hold', 'level': 68, 'aliases': 'bell cracked handbell',
     'short': 'a cracked handbell', 'long': 'A cracked iron handbell lies here.', 'affects': [('mana', 30), ('cha', -1)]},
    {'id': 'plague_mask', 'kind': 'armor', 'slot': 'head', 'level': 69, 'aliases': 'mask plague beaked',
     'short': 'a beaked plague mask', 'long': 'A beaked leather plague mask lies here.', 'affects': [('save_para', -2), ('hit', 15)]},
]
