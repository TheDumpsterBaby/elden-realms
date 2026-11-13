"""W6 The Last Light -- the March, levels 55-60.

A great river and a broken bridge, the last line the living still hold. On the
near bank stands the westernmost garrison (working name Fort Lastlight), the
stronghold. On the far bank the West's siege host is dug in around the ruins
of a river town, led by the Bridgebreaker. Beyond it begins the Blight.
"""

ZONE = {
    'num': 205, 'name': 'The Last Light', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'ridge_path', 'name': 'The Path Down the Ridge', 'sector': 'hills',
         'desc': """A switchback path drops down the western face of the ridge toward the river
         valley.  Below you the fortress sits on the near bank, its walls scarred and
         patched, its tower flying a faded banner.  Across the river, the far bank is
         one great camp of grey tents and grey shapes.""",
         'exits': {'e': {'to': '@20426', 'back_desc': 'A switchback path leads down toward the river and the fortress.'}, 'd': 'fort_approach'}},
        {'id': 'fort_approach', 'name': 'Before the Fortress', 'sector': 'field',
         'desc': """A killing ground of churned earth lies before the fortress gate, studded with
         stakes and ditches.  The bones of past assaults are trodden into the mud.
         Archers watch from the walls.  The gate opens only when the watch on the
         tower has looked you over through a spyglass.""",
         'exits': {'w': 'fort_gate', 's': 'riverbank_e'},
         'mobs': [('grey_skirmisher', 2)]},
        {'id': 'fort_gate', 'name': 'The Gate of Fort Lastlight', 'sector': 'city', 'flags': 'c',
         'desc': """A gatehouse of black stone, its doors sheathed in iron and dented by rams.
         Burning oil has scorched the walls above it.  A sergeant stands in the
         gateway with a ledger, writing down the name of every living soul who comes
         in, because so few of them do.""",
         'exits': {'w': 'fort_yard'},
         'mobs': [('lastlight_soldier', 2), ('gate_sergeant', 1)]},
        {'id': 'fort_yard', 'name': 'The Fortress Yard', 'sector': 'city', 'flags': 'c',
         'desc': """A crowded yard inside the walls.  Soldiers drill, smiths hammer at a field
         forge, and wounded men lie in rows under an awning.  Everyone is thin and
         grey-faced and moves like someone who has not slept in a month.  A great
         lantern burns on a pole in the centre, never allowed to go out.""",
         'exits': {'n': 'keep', 's': 'chapel', 'w': 'river_wall', 'u': 'wall_walk'},
         'objs': [('fort_cistern', 1)],
         'mobs': [('lastlight_soldier', 2), ('fort_smith', 1)]},
        {'id': 'wall_walk', 'name': 'The Fortress Wall', 'sector': 'city', 'flags': 'c',
         'desc': """The top of the wall, where archers stand shoulder to shoulder behind the
         merlons.  Across the river the enemy's campfires burn in their thousands.
         Now and then a stone from a siege engine whistles over and bursts against
         the wall, and the archers duck and come up and shoot again.""",
         'mobs': [('lastlight_archer', 3)]},
        {'id': 'keep', 'name': 'The Keep', 'sector': 'inside', 'flags': 'cd',
         'desc': """The squat central keep of the fortress, its hall filled with maps and
         messengers.  Officers argue in low voices around a table.  A board on the
         wall lists the garrison's strength each day, and the number at the bottom
         has been rubbed out and rewritten many times, always smaller.""",
         'exits': {'u': 'commander_room', 'd': 'cellars'},
         'mobs': [('lastlight_officer', 2)]},
        {'id': 'commander_room', 'name': 'The Commander\'s Chamber', 'sector': 'inside', 'flags': 'cde',
         'desc': """A cold room at the top of the keep with a single window over the broken
         bridge.  The commander of the Last Light sleeps here in his boots, a sword
         across his knees.  On the wall hangs a list of every fortress further west
         that has fallen, each name struck through.  This one is the last.""",
         'extras': {'list fortresses names': 'Twelve fortresses, all struck through. At the bottom, not yet struck: LASTLIGHT.'},
         'mobs': [('lastlight_commander', 1)]},
        {'id': 'cellars', 'name': 'The Keep Cellars', 'sector': 'inside', 'flags': 'cd',
         'desc': """Storerooms under the keep, mostly empty.  A few sacks of meal, a barrel of
         salt fish, crates of arrows.  The quartermaster counts them every morning
         and every evening, and every evening there are fewer, though no one has
         eaten.  Rats have come.  Grey ones.""",
         'mobs': [('fort_quartermaster', 1), ('grey_rat', 2)]},
        {'id': 'chapel', 'name': 'The Garrison Chapel', 'sector': 'inside', 'flags': 'cde',
         'desc': """A small chapel built into the fortress wall, its benches always full.
         Soldiers kneel here before every watch on the wall.  A priest hears their
         confessions and gives them the last rites in advance, because there may not
         be time afterwards.""",
         'mobs': [('garrison_priest', 1)]},
        {'id': 'river_wall', 'name': 'The River Wall', 'sector': 'city', 'flags': 'c',
         'desc': """The fortress's western wall runs along the river bank, and from it a stone
         ramp leads down to the bridgehead.  The bridge was the realm's pride, nine
         great arches across the river.  Three of them are gone now, blown up by the
         garrison to stop the West from crossing.""",
         'exits': {'w': 'bridgehead'},
         'mobs': [('lastlight_soldier', 1)]},
        {'id': 'bridgehead', 'name': 'The Bridgehead', 'sector': 'city',
         'desc': """A fortified gatehouse guards the eastern end of the bridge.  The span runs out
         over the grey river and stops in ragged stone where the arches were blown.
         The enemy has thrown a bridge of bones and timber across the gap, and every
         night they try to cross it.""",
         'exits': {'w': 'bridge_mid'},
         'mobs': [('bridge_warden', 1)]},
        {'id': 'bridge_mid', 'name': 'On the Broken Bridge', 'sector': 'field',
         'desc': """You walk out along the old bridge over the churning grey river.  Ahead the
         span ends, and a bridge of lashed timber and human bones has been laid across
         the gap to the far arches.  It creaks under every step.  The water below is
         full of bodies.""",
         'exits': {'w': 'bone_bridge'},
         'mobs': [('grey_skirmisher', 2)]},
        {'id': 'bone_bridge', 'name': 'The Bone Bridge', 'sector': 'field',
         'desc': """Lashed timbers and the long bones of men and horses form a swaying span over
         the gap.  Skulls are tied along its edges as handholds.  Grey soldiers cross
         it each night to assault the bridgehead, and few of them return.  The far
         bank is close now, and loud with drums.""",
         'exits': {'w': 'far_bank'},
         'mobs': [('bone_bridge_troll', 1)]},
        {'id': 'riverbank_e', 'name': 'The Eastern Riverbank', 'sector': 'field',
         'desc': """A muddy bank south of the fortress, where the garrison once drew water.  The
         river here is wide and slow and grey.  Bloated bodies drift past in the
         current, soldiers of both sides, and some of them are swimming.""",
         'exits': {'s': 'ferry_landing'},
         'mobs': [('river_drowned', 2)]},
        {'id': 'ferry_landing', 'name': 'The Old Ferry Landing', 'sector': 'field',
         'desc': """A rotting jetty where a ferry once crossed below the bridge.  The ferry boat
         lies half sunk at the end of the jetty, its ropes trailing in the water.  A
         figure sits in the stern, hooded, holding a pole, waiting for a passenger.""",
         'exits': {'w': 'ferry'},
         'mobs': [('river_drowned', 1)]},
        {'id': 'ferry', 'name': 'Aboard the Sunken Ferry', 'sector': 'water',
         'desc': """The ferry lists heavily, grey water sloshing over its deck.  The hooded
         ferryman turns to you, and under the hood is a skull with grey fire in its
         eyes.  He holds out a bony hand for his fare, and the coin he wants is not
         silver.""",
         'mobs': [('grey_ferryman', 1)]},
        {'id': 'far_bank', 'name': 'The Far Bank', 'sector': 'field',
         'desc': """You stand on the western bank of the river, in the enemy's country.  The
         ground is grey and dead.  The West's siege camp spreads out before you:
         tents of grey hide, bone totems, cages, cookfires where things roast that you
         do not look at closely.  Drums beat without stopping.""",
         'exits': {'w': 'siege_camp', 'n': 'ruined_town', 's': 'engine_park'},
         'mobs': [('grey_soldier', 2), ('dread_hound', 1)]},
        {'id': 'ruined_town', 'name': 'The Ruins of Riversmeet', 'sector': 'city',
         'desc': """The town of Riversmeet stood on the far bank for five hundred years.  Now it is
         rubble and ash, its people hollowed and marched west or roasted on the
         enemy's fires.  The enemy uses its houses as barracks.  Grey banners hang from
         the old guildhall.""",
         'exits': {'n': 'guildhall', 'w': 'cages'},
         'mobs': [('grey_soldier', 3)]},
        {'id': 'guildhall', 'name': 'The Captured Guildhall', 'sector': 'inside', 'flags': 'd',
         'desc': """The guildhall of Riversmeet has become the headquarters of the siege.  Its
         hall is hung with grey banners and the flayed skins of soldiers.  Maps of the
         fortress cover the tables, and grey officers bend over them, planning the
         next assault with the patience of the dead.""",
         'mobs': [('grey_captain', 2)]},
        {'id': 'cages', 'name': 'The Prisoner Cages', 'sector': 'field',
         'desc': """Rows of cages of bone and iron hold captured soldiers and townsfolk.  Some
         are being hollowed by grey-robed priests, one by one; the others watch and
         wait their turn.  A few still have the strength to beg you to open the cages.
         Most do not.""",
         'mobs': [('grey_priest', 1), ('caged_prisoner', 2)]},
        {'id': 'engine_park', 'name': 'The Engine Park', 'sector': 'field',
         'desc': """Great siege engines stand in a row along the bank: catapults, rams, a siege
         tower of bone and black wood taller than the fortress wall.  Hollowed slaves
         haul on their ropes under the whips of grey overseers.  The tower is nearly
         finished.""",
         'exits': {'u': 'siege_tower'},
         'mobs': [('grey_overseer', 1), ('hollowed_slave', 2)]},
        {'id': 'siege_tower', 'name': 'Atop the Siege Tower', 'sector': 'inside',
         'desc': """You climb the swaying siege tower to its top platform.  From here you can see
         over the fortress wall into the yard, and down into the camp where the army
         is massing.  When the tower rolls forward, the Last Light will fall within a
         night.  It must not roll.""",
         'mobs': [('tower_crew', 2)]},
        {'id': 'siege_camp', 'name': 'The Heart of the Siege Camp', 'sector': 'field',
         'desc': """The centre of the enemy camp, where the grey host's champions gather around a
         great fire of bones.  Drummers pound skin drums.  Dread hounds the size of
         horses lie chained to stakes.  At the head of the fire, on a throne of
         shields taken from the dead, sits the commander of the siege.""",
         'exits': {'w': 'command_mound'},
         'mobs': [('dread_hound', 2), ('grey_champion', 1)]},
        {'id': 'command_mound', 'name': 'The Bridgebreaker\'s Mound', 'sector': 'hills',
         'desc': """A mound of earth and rubble raised by slaves, from which the siege's commander
         can watch the fortress.  A giant figure stands upon it, armoured in iron
         plates bolted to its flesh, a hammer the size of a door across its shoulders.
         It broke the bridge's arches with that hammer, and it will break the walls.""",
         'exits': {'w': 'blight_edge'},
         'mobs': [('bridgebreaker', 1)]},
        {'id': 'blight_edge', 'name': 'The Edge of the Blight', 'sector': 'field',
         'desc': """West of the siege camp, the grey ground runs on into a waste where nothing
         grows at all.  The sky darkens.  The wind carries fine ash that stings the
         eyes.  This is where the Blight begins, and beyond this point, no fortress of
         the living has ever stood.""",
         'mobs': [('grey_skirmisher', 1)]},
    ],
    'mobs': [
        {'id': 'grey_skirmisher', 'aliases': 'skirmisher grey', 'short': 'a grey skirmisher', 'role': 'standard', 'level': 56,
         'long': 'A grey skirmisher crouches in a ditch, javelin ready.', 'flags': 'f', 'align': -900,
         'desc': 'A hollowed soldier of the West\'s host, grey-skinned and silent, sent to probe the fortress\'s defences.',
         'equip': [('grey_javelin', 'wield', 70)]},
        {'id': 'lastlight_soldier', 'aliases': 'soldier lastlight', 'short': 'a Lastlight soldier', 'role': 'elite', 'level': 58,
         'long': 'A Lastlight soldier leans on his spear, red-eyed with exhaustion.', 'flags': 'bm', 'align': 700, 'sex': 1,
         'desc': 'The last garrison of the living. He has fought every night for a month and he will fight tonight.',
         'equip': [('lastlight_spear', 'wield', 100), ('lastlight_shield', 'shield', 40)]},
        {'id': 'gate_sergeant', 'aliases': 'sergeant gate', 'short': 'the gate sergeant', 'role': 'elite', 'level': 58,
         'long': 'The gate sergeant writes your name in his ledger.', 'flags': 'b', 'align': 600, 'sex': 1,
         'desc': 'He writes down every name. "So someone will know you were here," he says, "after."'},
        {'id': 'fort_smith', 'aliases': 'smith', 'short': 'the fortress smith', 'role': 'elite', 'level': 57,
         'long': 'The fortress smith hammers a dented helm straight.', 'flags': 'b', 'align': 500, 'sex': 2,
         'desc': 'She mends what can be mended and melts what cannot, and there is never enough of either.',
         'equip': [('fort_hammer', 'wield', 100)]},
        {'id': 'lastlight_archer', 'aliases': 'archer lastlight', 'short': 'a Lastlight archer', 'role': 'elite', 'level': 58,
         'long': 'A Lastlight archer draws and looses across the river.', 'flags': 'b', 'align': 700,
         'desc': 'Fingers raw from the string. She has stopped counting her kills.',
         'equip': [('longbow', 'wield', 100)]},
        {'id': 'lastlight_officer', 'aliases': 'officer lastlight', 'short': 'a Lastlight officer', 'role': 'elite', 'level': 59,
         'long': 'A Lastlight officer studies the maps, jaw clenched.', 'flags': 'b', 'align': 600, 'sex': 1,
         'desc': 'Young for his rank. Everyone senior to him is dead.'},
        {'id': 'lastlight_commander', 'aliases': 'commander lastlight', 'short': 'the Commander of the Last Light', 'role': 'champion', 'level': 60,
         'long': 'The Commander of the Last Light watches the bridge, sword across his knees.', 'flags': 'b', 'align': 900, 'sex': 1,
         'desc': 'An old knight with a ruined face, the last of the realm\'s great captains. He knows the fortress will fall. He means to make the West pay for every stone.',
         'equip': [('lastlight_blade', 'wield', 100)]},
        {'id': 'fort_quartermaster', 'aliases': 'quartermaster', 'short': 'the fortress quartermaster', 'role': 'harmless', 'level': 56,
         'long': 'The quartermaster counts sacks with a frown.', 'flags': 'b', 'align': 400, 'sex': 1,
         'desc': 'There is less every night. He does not know why. He suspects everyone.',
         'carry': [('salt_fish', 100), ('field_kit', 100)]},
        {'id': 'grey_rat', 'aliases': 'rat grey', 'short': 'a grey rat', 'role': 'standard', 'level': 55,
         'long': 'A grey rat as big as a dog gnaws at a sack.', 'flags': 'f', 'align': -500, 'attack': 'bite',
         'desc': 'The rot that began in Midgaard\'s granary is here too. It is everywhere.'},
        {'id': 'garrison_priest', 'aliases': 'priest garrison', 'short': 'the garrison priest', 'role': 'harmless', 'level': 58,
         'long': 'The garrison priest murmurs the last rites over a kneeling soldier.', 'flags': 'b', 'align': 1000, 'sex': 1,
         'desc': 'He gives every soldier the last rites before every watch. He has given them to some soldiers forty times.',
         'carry': [('rite_vial', 100)]},
        {'id': 'bridge_warden', 'aliases': 'warden bridge', 'short': 'the bridge warden', 'role': 'champion', 'level': 59,
         'long': 'The bridge warden stands in the gatehouse arch, a great axe ready.', 'flags': 'b', 'align': 700, 'sex': 2,
         'desc': 'Every night the grey soldiers cross the bone bridge, and every night she meets them here. She has never let one past.',
         'equip': [('warden_axe', 'wield', 100)]},
        {'id': 'bone_bridge_troll', 'aliases': 'troll bridge bone', 'short': 'a bone-bridge troll', 'role': 'champion', 'level': 60,
         'long': 'A grey troll hung with skulls squats on the bone bridge, blocking the way.', 'flags': 'bfl', 'align': -900, 'attack': 'crush',
         'desc': 'The West bred it to hold the bridge for the assaults. It eats whatever falls in the gap.',
         'carry': [('troll_hide_belt', 100)]},
        {'id': 'river_drowned', 'aliases': 'drowned river soldier', 'short': 'a river-drowned soldier', 'role': 'standard', 'level': 57,
         'long': 'A drowned soldier wades up out of the grey river.', 'flags': 'f', 'align': -900,
         'desc': 'Whichever side he fought on, he fights for the West now.',
         'equip': [('grey_javelin', 'wield', 40)]},
        {'id': 'grey_ferryman', 'aliases': 'ferryman grey skull', 'short': 'the grey ferryman', 'role': 'champion', 'level': 59,
         'long': 'A hooded ferryman with a skull for a face holds out his hand for his fare.', 'flags': 'bfl', 'align': -1000,
         'desc': 'He ferried the dead of Riversmeet across the river for the West. He would like to ferry you.',
         'equip': [('ferry_pole', 'wield', 100)], 'carry': [('grave_coin', 100)]},
        {'id': 'grey_soldier', 'aliases': 'soldier grey host', 'short': 'a soldier of the grey host', 'role': 'standard', 'level': 58,
         'long': 'A soldier of the grey host stands in rank, black-eyed and silent.', 'flags': 'f', 'align': -1000,
         'desc': 'Hollowed, armoured in grey iron, utterly obedient. The West has thousands of them.',
         'equip': [('grey_iron_sword', 'wield', 60), ('grey_iron_mail', 'body', 25)]},
        {'id': 'dread_hound', 'aliases': 'hound dread', 'short': 'a dread hound', 'role': 'elite', 'level': 59,
         'long': 'A dread hound the size of a horse strains at its chain, jaws dripping.', 'flags': 'f', 'align': -900, 'attack': 'bite',
         'desc': 'Bred in the far west from wolves and something worse. Its eyes burn grey and its breath stinks of graves.'},
        {'id': 'grey_captain', 'aliases': 'captain grey', 'short': 'a grey captain', 'role': 'elite', 'level': 60,
         'long': 'A grey captain looks up from the siege maps with black eyes.', 'flags': 'f', 'align': -1000, 'sex': 1,
         'desc': 'Once a captain of the living, taken alive and hollowed. He remembers the fortress\'s weaknesses because he helped build it.',
         'equip': [('grey_iron_sword', 'wield', 100)]},
        {'id': 'grey_priest', 'aliases': 'priest grey', 'short': 'a grey priest', 'role': 'elite', 'level': 59,
         'long': 'A grey priest breathes dust into the mouth of a caged prisoner.', 'flags': 'f', 'align': -1000,
         'desc': 'Nu\'Groth\'s priests hollow the living with its words. This one is very good at it.',
         'equip': [('grey_censer', 'hold', 100)]},
        {'id': 'caged_prisoner', 'aliases': 'prisoner caged', 'short': 'a caged prisoner', 'role': 'harmless', 'level': 55,
         'long': 'A prisoner clutches the bars of a bone cage.', 'flags': 'b', 'align': 500,
         'desc': 'A soldier of the Last Light, taken in a sally. "Kill me," he whispers. "Before they make me fight my friends."'},
        {'id': 'grey_overseer', 'aliases': 'overseer grey', 'short': 'a grey overseer', 'role': 'elite', 'level': 59,
         'long': 'A grey overseer cracks a whip over the slaves at the engines.', 'flags': 'f', 'align': -1000,
         'desc': 'It drives the slaves until they drop, and then it drives the corpses.',
         'equip': [('grey_whip', 'wield', 100)]},
        {'id': 'hollowed_slave', 'aliases': 'slave hollowed', 'short': 'a hollowed slave', 'role': 'standard', 'level': 55,
         'long': 'A hollowed slave hauls on a rope, empty-eyed.', 'flags': 'f', 'align': -600,
         'desc': 'There is nothing left inside. It hauls until it is told to stop.'},
        {'id': 'tower_crew', 'aliases': 'crew tower', 'short': 'a siege tower crewman', 'role': 'standard', 'level': 58,
         'long': 'A grey crewman lashes timbers on the siege tower.', 'flags': 'f', 'align': -900,
         'desc': 'Building the tower that will bring down the last wall of the living.',
         'equip': [('grey_javelin', 'wield', 50)]},
        {'id': 'grey_champion', 'aliases': 'champion grey', 'short': 'a champion of the grey host', 'role': 'champion', 'level': 60,
         'long': 'A champion of the grey host rises from the fire, armour bolted to its flesh.', 'flags': 'bfl', 'align': -1000,
         'desc': 'The West\'s chosen warriors, remade with iron and grey fire. It has killed a hundred soldiers of the living in single combat.',
         'equip': [('champion_glaive', 'wield', 100)]},
        {'id': 'bridgebreaker', 'aliases': 'bridgebreaker giant', 'short': 'the Bridgebreaker', 'role': 'boss', 'level': 60,
         'long': 'The Bridgebreaker hefts a hammer the size of a door and roars.', 'flags': 'bfl', 'align': -1000, 'attack': 'pound',
         'desc': 'A giant from the far west, its flesh bolted with iron plates, its eyes grey fire. It smashed three arches of the great bridge with its hammer, and it has been promised the honour of breaking the Last Light\'s gate.',
         'equip': [('bridgebreaker_hammer', 'wield', 100), ('bolted_plates', 'body', 100)], 'carry': [('siege_plans', 100)]},
    ],
    'objs': [
        {'id': 'fort_cistern', 'kind': 'fountain', 'aliases': 'cistern', 'short': 'the fortress cistern',
         'long': 'A stone cistern of rainwater stands in the yard.', 'liquid': 0},
        {'id': 'grey_javelin', 'kind': 'weapon', 'level': 56, 'attack': 'pierce', 'aliases': 'javelin grey',
         'short': 'a grey iron javelin', 'long': 'A grey iron javelin lies here.'},
        {'id': 'lastlight_spear', 'kind': 'weapon', 'level': 58, 'attack': 'pierce', 'aliases': 'spear lastlight',
         'short': 'a Lastlight spear', 'long': 'A well-worn spear lies here.'},
        {'id': 'lastlight_shield', 'kind': 'armor', 'slot': 'shield', 'level': 58, 'aliases': 'shield lastlight lantern',
         'short': 'a shield painted with a lantern', 'long': 'A shield painted with a lantern lies here.'},
        {'id': 'fort_hammer', 'kind': 'weapon', 'level': 57, 'attack': 'pound', 'aliases': 'hammer smith',
         'short': 'a smith\'s hammer', 'long': 'A heavy hammer lies here.'},
        {'id': 'longbow', 'kind': 'weapon', 'level': 58, 'attack': 'pierce', 'aliases': 'longbow bow',
         'short': 'a yew longbow', 'long': 'A yew longbow lies here.', 'affects': [('dex', 1)]},
        {'id': 'lastlight_blade', 'kind': 'weapon', 'level': 61, 'attack': 'slash', 'aliases': 'blade lastlight',
         'short': 'the blade of the Last Light', 'long': 'A long sword whose blade glows faintly lies here.', 'extra': 'a',
         'affects': [('hitroll', 4), ('damroll', 4)]},
        {'id': 'salt_fish', 'kind': 'food', 'hours': 14, 'aliases': 'fish salt', 'short': 'a salted fish', 'long': 'A salted fish lies here.', 'weight': 1, 'cost': 12},
        {'id': 'field_kit', 'kind': 'potion', 'level': 58, 'spells': [28], 'spell_level': 55,
         'aliases': 'kit field', 'short': 'a field healing kit', 'long': 'A field healing kit lies here.', 'weight': 1},
        {'id': 'rite_vial', 'kind': 'potion', 'level': 58, 'spells': [36, 43], 'spell_level': 55,
         'aliases': 'vial rite', 'short': 'a vial of blessed water', 'long': 'A vial of blessed water lies here.', 'weight': 1},
        {'id': 'warden_axe', 'kind': 'weapon', 'level': 60, 'attack': 'slash', 'aliases': 'axe warden', 'two_handed': True,
         'short': 'the warden\'s great axe', 'long': 'A great axe notched by a hundred fights lies here.', 'affects': [('damroll', 4)]},
        {'id': 'troll_hide_belt', 'kind': 'armor', 'slot': 'waist', 'level': 60, 'aliases': 'belt troll hide',
         'short': 'a belt of troll hide', 'long': 'A belt of grey troll hide lies here.', 'affects': [('hit', 40), ('con', 1)]},
        {'id': 'ferry_pole', 'kind': 'weapon', 'level': 59, 'attack': 'bludgeon', 'aliases': 'pole ferry', 'two_handed': True,
         'short': 'a ferryman\'s pole', 'long': 'A long black pole lies here.'},
        {'id': 'grave_coin', 'kind': 'worn', 'slot': 'neck', 'level': 59, 'aliases': 'coin grave',
         'short': 'a grave coin on a chain', 'long': 'A coin black with age, on a chain, lies here.', 'affects': [('save_spell', -3), ('mana', 40)]},
        {'id': 'grey_iron_sword', 'kind': 'weapon', 'level': 58, 'attack': 'slash', 'aliases': 'sword grey iron',
         'short': 'a grey iron sword', 'long': 'A sword of dull grey iron lies here.'},
        {'id': 'grey_iron_mail', 'kind': 'armor', 'slot': 'body', 'level': 58, 'aliases': 'mail grey iron',
         'short': 'grey iron mail', 'long': 'A coat of grey iron mail lies here.'},
        {'id': 'grey_censer', 'kind': 'worn', 'slot': 'hold', 'level': 59, 'aliases': 'censer grey',
         'short': 'a grey censer', 'long': 'A censer leaking grey smoke lies here.', 'affects': [('int', 1), ('mana', 30)]},
        {'id': 'grey_whip', 'kind': 'weapon', 'level': 59, 'attack': 'whip', 'aliases': 'whip grey',
         'short': 'a whip of grey hide', 'long': 'A whip of grey hide lies coiled here.'},
        {'id': 'champion_glaive', 'kind': 'weapon', 'level': 60, 'attack': 'slash', 'aliases': 'glaive champion', 'two_handed': True,
         'short': 'a champion\'s glaive', 'long': 'A long glaive of black iron lies here.', 'affects': [('hitroll', 2), ('damroll', 3)]},
        {'id': 'bridgebreaker_hammer', 'kind': 'weapon', 'level': 62, 'attack': 'pound', 'aliases': 'hammer bridgebreaker', 'two_handed': True,
         'short': 'the Bridgebreaker\'s hammer', 'long': 'A hammer the size of a door lies here. You could barely lift it.', 'weight': 40,
         'affects': [('damroll', 6), ('str', 2)]},
        {'id': 'bolted_plates', 'kind': 'armor', 'slot': 'body', 'level': 61, 'aliases': 'plates bolted iron',
         'short': 'bolted iron plates', 'long': 'A set of iron plates with bloody bolt holes lies here.', 'affects': [('hit', 50)]},
        {'id': 'siege_plans', 'kind': 'note', 'aliases': 'plans siege', 'short': 'the siege plans',
         'long': 'A roll of siege plans lies here.', 'weight': 1,
         'extras': {'plans siege': 'The assault on Lastlight, in detail. The tower, the rams, the night. At the bottom, in a different hand: AND THEN MIDGAARD.'}},
    ],
}
