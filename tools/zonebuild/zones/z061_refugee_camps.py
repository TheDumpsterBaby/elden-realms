"""The Refugee Camps -- support ring, levels 5-12.

Everyone who fled the West ends up here, outside the fort that will not let
them in: crowding, sickness, hunger, crime, and a cult that preaches that the
darkness cannot be fought, only welcomed. Links the Granary Fields (west) to
the Hospice of the Last Rites (north).
"""

ZONE = {
    'num': 61, 'name': 'The Refugee Camps', 'builders': 'Claude', 'lifespan': 15,
    'rooms': [
        {'id': 'gap', 'name': 'The Gap in the Hedge', 'sector': 'field',
         'desc': """You squeeze through the hacked gap in the hawthorn and the smell of the
         camps rolls over you: smoke, sewage, sickness and too many people.  Behind
         you lie the Granary Fields.  Ahead, a sea of tents and lean-tos stretches
         to the horizon under a pall of grey smoke.""",
         'exits': {'w': {'to': '@6024', 'back_desc': 'Through the gap in the hedge lie the Refugee Camps.'}, 'e': 'mud_road'},
         'mobs': [('refugee', 2)]},
        {'id': 'mud_road', 'name': 'The Mud Road', 'sector': 'field',
         'desc': """A road of trampled mud winds into the camps, lined on both sides with
         shelters made of anything at hand: wagon covers, doors, blankets on sticks.
         Hollow-eyed faces watch from every opening.  A woman holds out an empty
         bowl to you without a word.""",
         'exits': {'e': 'bonfire', 'n': 'tents_north', 's': 'tents_south'},
         'mobs': [('refugee', 3), ('cutpurse', 1)]},
        {'id': 'tents_north', 'name': 'The Northern Tent Rows', 'sector': 'field',
         'desc': """Tents stand in rows so tight that the guy-ropes cross and tangle.  Washing
         hangs grey between them.  Families from a dozen burned villages huddle
         together, speaking dialects from the far west that you have never heard,
         all of them describing the same darkness.""",
         'exits': {'n': 'north_edge', 'e': 'soup_line'},
         'mobs': [('refugee', 3), ('sick_refugee', 1)]},
        {'id': 'north_edge', 'name': 'The Northern Edge of the Camps', 'sector': 'field',
         'desc': """The tents thin out at the foot of a low rise.  At its top stands the grey
         stone bulk of the Hospice of the Last Rites, its bell tower dark against
         the sky.  A line of stretcher-bearers trudges up the slope, and another
         line, carrying shrouded shapes, comes down it.""",
         'mobs': [('stretcher_bearer', 2)]},
        {'id': 'soup_line', 'name': 'The Soup Line', 'sector': 'field',
         'desc': """A queue hundreds long shuffles toward a row of iron cauldrons, where
         soldiers ladle out thin grey broth.  When the cauldrons run dry, the
         soldiers simply walk away, and the people at the back of the line sit down
         in the mud and wait for tomorrow.""",
         'exits': {'e': 'pens'},
         'objs': [('cauldron', 1)],
         'mobs': [('ration_soldier', 2), ('refugee', 2)]},
        {'id': 'tents_south', 'name': 'The Southern Tent Rows', 'sector': 'field',
         'desc': """The tents here are older, patched many times, and the people in them have
         given up waiting to be let into the fort.  Children with distended bellies
         play a game with stones and chalk.  An old man sits outside his tent
         sharpening a kitchen knife, over and over.""",
         'exits': {'s': 'scrap_market', 'e': 'well'},
         'mobs': [('refugee', 2), ('refugee_child', 2)]},
        {'id': 'scrap_market', 'name': 'The Scrap Market', 'sector': 'field',
         'desc': """A muddy clearing where refugees trade what little they have left: a
         wedding ring for a loaf, a sword for a blanket, a daughter's hair for a pot
         of lard.  Bargaining is quiet and bitter.  Thugs move through the crowd
         taking a share of every trade.""",
         'exits': {'e': 'alley'},
         'mobs': [('camp_thug', 2), ('scrap_trader', 1), ('cutpurse', 1)]},
        {'id': 'alley', 'name': 'Thieves\' Alley', 'sector': 'field',
         'desc': """A narrow lane between leaning shacks where the camp's predators gather.
         Nobody walks here alone if they can help it.  A body lies face down in a
         puddle, stripped of its boots.  Nobody has moved it, and nobody will.""",
         'exits': {'e': 'thug_den'},
         'mobs': [('camp_thug', 2), ('cutpurse', 2)]},
        {'id': 'thug_den', 'name': "The Gang Boss's Shack", 'sector': 'inside', 'flags': 'd',
         'desc': """A shack built from the timbers of a wrecked barn, warmer and drier than
         anything else in the camps.  Stolen food is stacked against the walls.
         The man who runs the camps' black market sits here, feet up, counting
         other people's rings.""",
         'mobs': [('gang_boss', 1), ('camp_thug', 1)]},
        {'id': 'well', 'name': 'The Camp Well', 'sector': 'field',
         'desc': """A single well serves the whole camp, and the queue for it never ends.  The
         mud around it is churned into a stinking slurry.  A soldier keeps order
         with a cudgel, and the rope has been cut and retied so many times it is
         more knot than rope.""",
         'exits': {'n': 'bonfire', 'e': 'burial_pits'},
         'objs': [('camp_well', 1)],
         'mobs': [('camp_warden', 1), ('refugee', 2)]},
        {'id': 'bonfire', 'name': 'The Bonfire Square', 'sector': 'field',
         'desc': """At the heart of the camps a great bonfire burns night and day, fed with
         broken furniture and worse.  People crowd around it for warmth.  On an
         upturned cart beside it a gaunt preacher in grey shouts that the fort is
         doomed and that only surrender to the West will save them.""",
         'exits': {'e': 'chapel_tent', 'n': 'pens'},
         'mobs': [('grey_preacher', 1), ('refugee', 3), ('cult_acolyte', 1)]},
        {'id': 'pens', 'name': 'The Livestock Pens', 'sector': 'field',
         'desc': """Pens of hurdles hold the last few beasts the refugees drove east with them:
         a lame horse, goats, a handful of sheep.  Men with clubs guard them day and
         night.  The bones of the ones that were stolen lie in a heap beside the
         fence.""",
         'exits': {'e': 'sick_tents'},
         'mobs': [('pen_guard', 2), ('feral_dog', 2)]},
        {'id': 'sick_tents', 'name': 'The Sick Tents', 'sector': 'field',
         'desc': """Long canvas tents hold rows of pallets, and on every pallet someone is
         coughing, sweating or simply lying very still.  Grey blotches spread over
         their skin.  A single healer moves among them with a bucket and a cloth,
         and her face is grey with exhaustion.""",
         'exits': {'e': {'to': 'quarantine', 'door': 'flap tent', 'state': 'closed',
                         'desc': 'A tent flap tied shut, painted with a grey cross.'}},
         'mobs': [('sick_refugee', 3), ('camp_healer', 1)]},
        {'id': 'quarantine', 'name': 'The Quarantine Tent', 'sector': 'inside', 'flags': 'd',
         'desc': """The sick who were moved here do not come out.  The air is close and sweet.
         Some of the shapes on the pallets are moving in ways that sick people do
         not move, and the grey has spread over them completely.  Their eyes are
         open.""",
         'mobs': [('greyblight_victim', 3)]},
        {'id': 'burial_pits', 'name': 'The Burial Pits', 'sector': 'field',
         'desc': """Long trenches have been dug at the camp's edge, and they are filling faster
         than they can be dug.  Bodies wrapped in sacking lie in rows waiting their
         turn.  Lime is shovelled over each layer.  Gravediggers work with rags tied
         over their faces and will not meet your eye.""",
         'exits': {'n': 'chapel_ruin'},
         'mobs': [('gravedigger', 2), ('pit_ghoul', 1)]},
        {'id': 'chapel_ruin', 'name': 'The Ruined Wayside Chapel', 'sector': 'inside', 'flags': 'd',
         'desc': """A tiny stone chapel stood here before the camps came, and its walls still
         stand though its roof is gone.  The altar has been smashed.  Someone has
         painted a grey spiral over the old saints on the walls, the same spiral
         flattened into the wheat of the Granary Fields.""",
         'extras': {'spiral grey paint': 'A spiral of grey paint, drawn with great care, winding inward to a single black dot.'},
         'mobs': [('cult_acolyte', 2)]},
        {'id': 'chapel_tent', 'name': 'The Tent of the Grey Choir', 'sector': 'inside', 'flags': 'd',
         'desc': """A large tent of grey canvas where the preacher's followers gather to sing.
         Their hymn has no words, only a long falling note that makes your teeth
         ache.  Benches face a lectern carved with a spiral.  A rug at the back of
         the tent does not quite lie flat.""",
         'exits': {'d': {'to': 'cellar_stair', 'door': 'rug trapdoor', 'state': 'closed',
                         'desc': 'Under the rug, a wooden trapdoor.'}},
         'extras': {'rug': 'Beneath the edge of the rug you can feel the outline of a trapdoor.'},
         'mobs': [('cult_acolyte', 2), ('choir_singer', 2)]},
        {'id': 'cellar_stair', 'name': 'A Stair Beneath the Camps', 'sector': 'inside', 'flags': 'ad',
         'desc': """Earthen steps lead down beneath the camp into an old root cellar from the
         farm that once stood here.  The walls have been dug out further, and the
         falling hymn rises from below, louder and clearer, carried by many
         voices.""",
         'exits': {'d': 'cult_hall'},
         'mobs': [('cult_guard', 1)]},
        {'id': 'cult_hall', 'name': 'The Hall of Surrender', 'sector': 'inside', 'flags': 'ad',
         'desc': """A low chamber lit by grey candles, packed with kneeling cultists in sacking
         robes.  They face west.  Every one of them has a grey blotch somewhere on
         their skin, and they wear it proudly, like a brand.  An arch at the far end
         opens onto a smaller, darker room.""",
         'exits': {'w': 'prophet_shrine'},
         'mobs': [('cult_acolyte', 3), ('cult_guard', 1)]},
        {'id': 'prophet_shrine', 'name': 'The Shrine of the Grey Prophet', 'sector': 'inside', 'flags': 'ad',
         'desc': """A round chamber whose walls are painted entirely grey.  In its centre a pit
         is filled with soft grey grain, the same rot that is eating the fort's
         stores, and it whispers.  Over it stands the Grey Prophet, arms raised,
         listening to the voice from the West that only he can hear.""",
         'mobs': [('grey_prophet', 1)]},
    ],
    'mobs': [
        {'id': 'refugee', 'aliases': 'refugee', 'short': 'a refugee', 'role': 'harmless', 'level': 5,
         'long': 'A refugee in mud-caked rags stares at nothing.', 'flags': 'g', 'align': 300,
         'desc': 'Everything this person owned is gone: home, family, name. All that is left is the memory of the darkness coming over the hills.'},
        {'id': 'refugee_child', 'aliases': 'child refugee', 'short': 'a refugee child', 'role': 'harmless', 'level': 3,
         'long': 'A refugee child plays a silent game with stones.', 'flags': 'g', 'align': 600,
         'desc': 'Too thin, too quiet. She does not ask you for food; she has learned that people do not give it.'},
        {'id': 'sick_refugee', 'aliases': 'refugee sick', 'short': 'a sick refugee', 'role': 'harmless', 'level': 4,
         'long': 'A sick refugee coughs, grey blotches spreading over his skin.', 'flags': 'b', 'align': 200,
         'desc': 'The greyblight starts as a cough, then a blotch, then fever. The healers have no name for what comes after.'},
        {'id': 'cutpurse', 'aliases': 'cutpurse thief', 'short': 'a cutpurse', 'role': 'standard', 'level': 7,
         'long': 'A cutpurse slips through the crowd, eyeing your belt.', 'flags': 'fl', 'align': -300, 'sex': 1,
         'desc': 'Quick hands, quick feet, and the conscience of someone who has watched their family starve.',
         'equip': [('camp_knife', 'wield', 100)]},
        {'id': 'stretcher_bearer', 'aliases': 'bearer stretcher', 'short': 'a stretcher-bearer', 'role': 'harmless', 'level': 6,
         'long': 'A stretcher-bearer trudges toward the Hospice.', 'flags': 'g', 'align': 400,
         'desc': 'Up the hill with the sick, down the hill with the dead, all day, every day.'},
        {'id': 'ration_soldier', 'aliases': 'soldier ration', 'short': 'a ration soldier', 'role': 'standard', 'level': 9,
         'long': 'A soldier ladles grey broth from a cauldron.', 'flags': 'bm', 'align': 100, 'sex': 1,
         'desc': 'He hands out the broth without looking at the faces. Looking at the faces is how you stop being able to do the job.',
         'equip': [('soldier_cudgel', 'wield', 100)]},
        {'id': 'camp_thug', 'aliases': 'thug camp', 'short': 'a camp thug', 'role': 'standard', 'level': 9,
         'long': 'A camp thug cracks his knuckles and blocks your way.', 'flags': 'fg', 'align': -400, 'sex': 1,
         'desc': 'Big, well fed, and paid in other people\'s food. In a starving camp, that makes him a lord.',
         'equip': [('soldier_cudgel', 'wield', 60)]},
        {'id': 'scrap_trader', 'aliases': 'trader scrap', 'short': 'a scrap trader', 'role': 'harmless', 'level': 6,
         'long': 'A scrap trader lays out broken treasures on a blanket.', 'flags': 'b', 'align': 0,
         'desc': 'She will trade anything for anything. Her prices are robbery, and everyone pays them.'},
        {'id': 'gang_boss', 'aliases': 'boss gang', 'short': 'the gang boss', 'role': 'champion', 'level': 11,
         'long': 'The gang boss counts a pile of rings and does not look up.', 'flags': 'bl', 'align': -600, 'sex': 1,
         'desc': 'A former quartermaster who stole from the fort until he was thrown out. Now he steals from the people the fort threw out, and he is far richer.',
         'equip': [('boss_falchion', 'wield', 100), ('padded_jerkin', 'body', 100)], 'carry': [('ring_pouch', 100)]},
        {'id': 'camp_warden', 'aliases': 'warden camp soldier', 'short': 'a camp warden', 'role': 'standard', 'level': 10,
         'long': 'A camp warden keeps order at the well with a heavy cudgel.', 'flags': 'bm', 'align': 200, 'sex': 2,
         'desc': 'She has broken up a dozen fights today. Tomorrow there will be more.',
         'equip': [('soldier_cudgel', 'wield', 100)]},
        {'id': 'grey_preacher', 'aliases': 'preacher grey', 'short': 'the grey preacher', 'role': 'elite', 'level': 11,
         'long': 'A gaunt preacher in grey howls of surrender from an upturned cart.', 'flags': 'b', 'align': -700, 'sex': 1,
         'desc': '"The wall will fall! The fort will fall! Open your hearts to the West and it will spare you!" Spittle flies from his lips. People listen.',
         'carry': [('grey_tract', 100)]},
        {'id': 'cult_acolyte', 'aliases': 'acolyte cultist', 'short': 'a grey-robed acolyte', 'role': 'standard', 'level': 10,
         'long': 'A grey-robed acolyte hums a falling note under her breath.', 'flags': 'g', 'align': -600,
         'desc': 'A grey blotch spreads across her cheek. She touches it lovingly, like a kiss.',
         'equip': [('ritual_knife', 'wield', 50)]},
        {'id': 'pen_guard', 'aliases': 'guard pen', 'short': 'a pen guard', 'role': 'standard', 'level': 8,
         'long': 'A pen guard leans on his club, watching the livestock.', 'flags': 'b', 'align': 100, 'sex': 1,
         'desc': 'Those goats are all that stands between his village and starvation.',
         'equip': [('soldier_cudgel', 'wield', 100)]},
        {'id': 'feral_dog', 'aliases': 'dog feral', 'short': 'a feral dog', 'role': 'standard', 'level': 6,
         'long': 'A feral dog slinks between the pens, ribs showing.', 'flags': 'f', 'align': -100, 'attack': 'bite',
         'desc': 'Somebody\'s pet once. Now it eats what it can catch, and the burial pits have taught it what that can be.'},
        {'id': 'camp_healer', 'aliases': 'healer camp', 'short': 'the camp healer', 'role': 'elite', 'level': 10,
         'long': 'An exhausted healer moves between the pallets with a bucket and cloth.', 'flags': 'b', 'align': 900, 'sex': 2,
         'desc': 'She was a midwife in a village that no longer exists. She has not slept in two days.',
         'carry': [('healer_herbs', 100)]},
        {'id': 'greyblight_victim', 'aliases': 'victim greyblight grey', 'short': 'a grey-skinned victim', 'role': 'elite', 'level': 11,
         'long': 'A figure grey from head to foot rises from its pallet with open, empty eyes.', 'flags': 'bf', 'align': -800, 'attack': 'claw',
         'desc': 'The greyblight\'s last stage. The person is gone; the body moves, and it is hungry, and it faces west whenever it is still.'},
        {'id': 'gravedigger', 'aliases': 'gravedigger digger', 'short': 'a gravedigger', 'role': 'harmless', 'level': 7,
         'long': 'A gravedigger shovels lime into a trench.', 'flags': 'b', 'align': 200,
         'desc': 'A rag over his face and dead eyes above it.'},
        {'id': 'pit_ghoul', 'aliases': 'ghoul pit', 'short': 'a pit ghoul', 'role': 'elite', 'level': 11,
         'long': 'Something pale crouches in the burial trench, eating.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'It was buried in the first trench. It did not stay buried.'},
        {'id': 'choir_singer', 'aliases': 'singer choir', 'short': 'a choir singer', 'role': 'standard', 'level': 9,
         'long': 'A choir singer sways, holding the long falling note.', 'flags': 'b', 'align': -500,
         'desc': 'His mouth is open in the endless hymn. His eyes have rolled up white.'},
        {'id': 'cult_guard', 'aliases': 'guard cult brute', 'short': 'a cult brute', 'role': 'elite', 'level': 12,
         'long': 'A huge cultist in grey sackcloth bars the way, a hooked blade in hand.', 'flags': 'bfl', 'align': -700, 'sex': 1,
         'desc': 'The grey has spread over half his face, and he no longer seems to feel pain.',
         'equip': [('hooked_blade', 'wield', 100)]},
        {'id': 'grey_prophet', 'aliases': 'prophet grey', 'short': 'the Grey Prophet', 'role': 'champion', 'level': 12,
         'long': 'The Grey Prophet stands over the whispering pit, arms raised to the West.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'A tall, emaciated man, grey from head to foot except for his eyes, which are entirely black. He hears Nu\'Groth\'s voice in the rotting grain, and he has promised it the camps, and then the fort.',
         'equip': [('prophet_staff', 'wield', 100), ('grey_robe', 'about', 100)], 'carry': [('grey_grain_vial', 100)]},
    ],
    'objs': [
        {'id': 'cauldron', 'kind': 'container', 'fixed': True, 'capacity': 0, 'aliases': 'cauldron cauldrons iron',
         'short': 'an iron cauldron', 'long': 'A row of iron cauldrons, scraped empty, stands here.'},
        {'id': 'camp_well', 'kind': 'fountain', 'aliases': 'well', 'short': 'the camp well',
         'long': 'The camp well stands here, surrounded by churned mud.', 'liquid': 0},
        {'id': 'camp_knife', 'kind': 'weapon', 'level': 7, 'attack': 'pierce', 'aliases': 'knife camp',
         'short': 'a sharpened kitchen knife', 'long': 'A sharpened kitchen knife lies here.'},
        {'id': 'soldier_cudgel', 'kind': 'weapon', 'level': 9, 'attack': 'bludgeon', 'aliases': 'cudgel club',
         'short': 'a heavy cudgel', 'long': 'A heavy wooden cudgel lies here.'},
        {'id': 'boss_falchion', 'kind': 'weapon', 'level': 12, 'attack': 'slash', 'aliases': 'falchion',
         'short': 'a stolen army falchion', 'long': 'An army falchion lies here.', 'affects': [('damroll', 1)]},
        {'id': 'padded_jerkin', 'kind': 'armor', 'slot': 'body', 'level': 11, 'aliases': 'jerkin padded',
         'short': 'a padded jerkin', 'long': 'A thick padded jerkin lies here.'},
        {'id': 'ring_pouch', 'kind': 'treasure', 'level': 11, 'aliases': 'pouch rings', 'short': 'a pouch of stolen rings',
         'long': 'A leather pouch of rings lies here.', 'cost': 400, 'weight': 1},
        {'id': 'grey_tract', 'kind': 'note', 'aliases': 'tract pamphlet grey', 'short': 'a grey tract',
         'long': 'A grey pamphlet lies trampled in the mud.', 'weight': 1,
         'extras': {'tract pamphlet grey': 'THE WALL IS A LIE. The West is not death but change. Those who welcome the grey will be spared when the fort falls. Seek the Choir.'}},
        {'id': 'ritual_knife', 'kind': 'weapon', 'level': 10, 'attack': 'pierce', 'aliases': 'knife ritual',
         'short': 'a grey ritual knife', 'long': 'A thin knife with a grey stone handle lies here.'},
        {'id': 'healer_herbs', 'kind': 'potion', 'level': 10, 'spells': [16, 0, 0], 'spell_level': 10,
         'aliases': 'herbs bundle healer', 'short': "a bundle of healer's herbs", 'long': 'A bundle of dried herbs lies here.', 'weight': 1},
        {'id': 'hooked_blade', 'kind': 'weapon', 'level': 12, 'attack': 'slash', 'aliases': 'blade hooked',
         'short': 'a hooked grey blade', 'long': 'A wicked hooked blade lies here.'},
        {'id': 'prophet_staff', 'kind': 'weapon', 'level': 13, 'attack': 'bludgeon', 'aliases': 'staff prophet grey',
         'short': "the Grey Prophet's staff", 'long': 'A staff of grey wood carved with spirals lies here.',
         'affects': [('mana', 25), ('int', 1), ('hitroll', 1)]},
        {'id': 'grey_robe', 'kind': 'armor', 'slot': 'about', 'level': 13, 'aliases': 'robe grey',
         'short': 'a robe of grey sackcloth', 'long': 'A grey sackcloth robe lies here.', 'affects': [('save_spell', -2), ('wis', 1)]},
        {'id': 'grey_grain_vial', 'kind': 'treasure', 'level': 12, 'aliases': 'vial grain grey', 'short': 'a vial of whispering grain',
         'long': 'A stoppered vial of grey grain lies here.', 'weight': 1, 'cost': 100,
         'extras': {'vial grain': 'The grain inside presses against the glass, always toward the west.'}},
    ],
}
