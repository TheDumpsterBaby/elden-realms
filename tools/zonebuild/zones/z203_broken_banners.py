"""W4 The Field of Broken Banners -- the March, levels 45-50.

The plain where the last army of the living met the West and was destroyed.
Its dead do not rest: they still fight the battle they lost, and a necromancer
of the West is gathering them into a new host under their own fallen marshal.
No stronghold.
"""

ZONE = {
    'num': 203, 'name': 'The Field of Broken Banners', 'builders': 'Claude', 'lifespan': 20,
    'rooms': [
        {'id': 'approach', 'name': 'The Eastern Approach', 'sector': 'field',
         'desc': """The fens give way to a wide grey plain under a low sky.  The ground is
         littered with the leavings of an army: a broken wheel, a helmet, a boot,
         a standard pole snapped in half.  Ahead, as far as you can see, the plain
         is covered with the dead, and some of them are standing up.""",
         'exits': {'e': {'to': '@20227', 'back_desc': 'West, the ground firms and rises onto a grey battlefield.'}, 'w': 'camp_ruin'},
         'mobs': [('carrion_vulture', 2)]},
        {'id': 'camp_ruin', 'name': 'The Ruined Encampment', 'sector': 'field',
         'desc': """The army's camp stood here on the morning of the battle.  The tents are
         slashed and trampled, the cookfires cold for a year, and the camp followers'
         wagons burned where they stood.  Pots still hang over the dead fires,
         crusted with porridge nobody finished.""",
         'exits': {'w': 'field_centre', 'n': 'command_tent', 's': 'hospital_ruin'},
         'mobs': [('risen_soldier', 2), ('camp_follower_ghost', 1)]},
        {'id': 'command_tent', 'name': 'The Command Tent', 'sector': 'inside', 'flags': 'd',
         'desc': """The great tent of the army's commanders still stands, its canvas torn and its
         poles leaning.  A map table holds a plan of the battle, the pieces knocked
         over.  A ghostly officer bends over it, moving the pieces, again and again,
         trying to find the order that would have won.""",
         'extras': {'map table pieces': 'The plan of battle. Three companies on the left, five in the centre, the cavalry on the right. One piece, a black one, stands alone in the west.'},
         'mobs': [('ghost_officer', 1)]},
        {'id': 'hospital_ruin', 'name': 'The Field Hospital', 'sector': 'field',
         'desc': """Rows of cots stand under a collapsed awning, and on each cot lies a soldier
         who died waiting for a surgeon.  They are sitting up now, holding their
         wounds closed, waiting still.  A surgeon's ghost moves among them with a
         saw, unable to save any of them, unable to stop trying.""",
         'exits': {'w': 'left_flank'},
         'mobs': [('waiting_dead', 3), ('surgeon_ghost', 1)]},
        {'id': 'field_centre', 'name': 'The Centre of the Field', 'sector': 'field',
         'desc': """The heart of the battle, where the five companies of the centre broke.  The
         ground is churned and black, and the dead lie three deep.  Many of them are
         moving, re-forming their ranks, lifting broken spears.  They advance toward
         you in silence, as they once advanced toward the West.""",
         'exits': {'w': 'banner_hill', 'n': 'right_flank', 's': 'left_flank'},
         'mobs': [('risen_soldier', 3), ('risen_sergeant', 1)]},
        {'id': 'left_flank', 'name': 'The Left Flank', 'sector': 'field',
         'desc': """Three companies held the left until the end.  Their dead lie in a line,
         shields still overlapping, facing west.  Arrows stand in the earth like grey
         grass.  As you approach, the line rises as one and locks its shields.""",
         'exits': {'w': 'mass_grave', 's': 'river_ford'},
         'mobs': [('shield_wall_dead', 3)]},
        {'id': 'right_flank', 'name': 'The Right Flank, the Cavalry\'s End', 'sector': 'field',
         'desc': """The cavalry charged here, and here the cavalry died: horses and riders in
         heaps, lances snapped, banners trampled into the mud.  Some of the horses
         are getting up, skeletal and grey, and their riders are climbing back into
         the saddle.""",
         'exits': {'w': 'trebuchets', 'n': 'vulture_rocks'},
         'mobs': [('death_rider', 2)]},
        {'id': 'vulture_rocks', 'name': 'The Vulture Rocks', 'sector': 'hills',
         'desc': """A jumble of grey rocks rises from the plain, white with droppings.  Vultures
         as big as men crowd the ledges, too fat to fly, picking at the scraps they
         carried up from the field.  They do not like to be disturbed at their
         meal.""",
         'mobs': [('carrion_vulture', 2), ('vulture_matriarch', 1)]},
        {'id': 'trebuchets', 'name': 'The Wrecked Siege Line', 'sector': 'field',
         'desc': """A line of great trebuchets the army dragged here to break the West's lines.
         They were never fired.  Something tore them apart, splintering beams as
         thick as trees.  The crews lie beneath the wreckage, and one of the engines
         has been rebuilt by dead hands, out of timber and bone.""",
         'exits': {'w': 'bone_engine'},
         'mobs': [('risen_engineer', 2)]},
        {'id': 'bone_engine', 'name': 'The Bone Engine', 'sector': 'field',
         'desc': """A siege engine built from timber and the bones of men and horses squats on
         the plain, its arm drawn back, a load of skulls in its sling.  Dead crewmen
         tend it.  It is aimed east, toward the fens, toward Stilthold, toward
         Midgaard far beyond.""",
         'mobs': [('bone_engineer', 1), ('risen_engineer', 1)]},
        {'id': 'mass_grave', 'name': 'The Mass Grave', 'sector': 'field',
         'desc': """After the battle, the few survivors dug a great pit and laid their friends in
         it.  They did not dig it deep enough.  The earth has been pushed aside from
         beneath, and the pit is half empty.  The ones still in it are struggling to
         climb out.""",
         'exits': {'w': 'pyre', 'd': 'grave_pit'},
         'mobs': [('grave_risen', 2)]},
        {'id': 'grave_pit', 'name': 'Down in the Pit', 'sector': 'field', 'flags': 'a',
         'desc': """You climb down among the dead.  Limbs reach from the soil.  Faces turn toward
         you.  Somewhere at the bottom of the pit a voice is calling the names of a
         company roll, one after another, and each time a name is called, something
         answers and begins to dig.""",
         'mobs': [('grave_risen', 3), ('roll_caller', 1)]},
        {'id': 'river_ford', 'name': 'The Ford of the Rout', 'sector': 'swim',
         'desc': """When the army broke, its survivors fled for the river, and here, at the ford,
         the West caught them.  The water is choked with bodies in rusting armour.
         The current pushes them against each other, and they push back.""",
         'exits': {'w': 'reed_bank'},
         'mobs': [('drowned_soldier', 3)]},
        {'id': 'reed_bank', 'name': 'The Far Bank', 'sector': 'field',
         'desc': """A muddy bank on the far side of the ford, where a handful of survivors made a
         last stand behind an overturned wagon.  Their bones lie around it still,
         weapons in hand.  Scratched into the wagon's planks are the names of all
         of them, and a message.""",
         'exits': {'n': 'pyre'},
         'extras': {'wagon names message planks': 'Twelve names, and below them: WE HELD THE FORD UNTIL DUSK. TELL MIDGAARD IT IS COMING. TELL THEM IT CANNOT BE BEATEN IN THE FIELD.'},
         'mobs': [('ford_guardian', 1)]},
        {'id': 'pyre', 'name': 'The Bone Pyre', 'sector': 'field',
         'desc': """At the western edge of the battlefield the servants of Nu\'Groth have built a
         pyre of bones as tall as a tower.  It burns with a cold grey flame that
         gives no heat.  Dead men file past it in a slow column, and as each passes,
         the grey fire leaps into its empty eyes.""",
         'exits': {'w': 'necro_circle', 'n': 'banner_hill'},
         'mobs': [('risen_soldier', 2), ('pyre_tender', 1)]},
        {'id': 'necro_circle', 'name': 'The Circle of Raising', 'sector': 'field',
         'desc': """A circle of black iron stakes driven into the earth, each topped with a skull.
         Inside it, the ground is bare and grey.  A figure in robes of human skin
         chants over a heap of corpses, and they twitch and rise and shamble into
         the ranks of the dead host.""",
         'exits': {'w': 'west_road'},
         'mobs': [('grey_necromancer', 1), ('risen_soldier', 2)]},
        {'id': 'banner_hill', 'name': 'The Hill of Banners', 'sector': 'hills',
         'desc': """A low hill rises from the centre of the field, where the army planted its
         banners at dawn.  The banners are torn and blackened, and the hill is
         covered with the bodies of the honour guard who died defending them.  At the
         top, a ring of dead knights stands guard around a single figure.""",
         'exits': {'u': 'hilltop'},
         'mobs': [('dead_knight', 2)]},
        {'id': 'hilltop', 'name': 'The Last Stand', 'sector': 'hills',
         'desc': """The crown of the hill, where the army's marshal made his last stand around
         the royal standard.  The standard still flies, tattered and grey.  The
         Marshal stands beneath it, risen, his sword in his hand and his army re-forming
         below him.  He commands them now for Nu\'Groth.""",
         'mobs': [('fallen_marshal', 1), ('dead_knight', 2)]},
        {'id': 'west_road', 'name': 'The Road West from the Field', 'sector': 'hills',
         'desc': """Beyond the battlefield the land rises into rolling hills covered in coarse
         grey grass.  Old burial mounds hump up on every side, many of them broken
         open.  On a far hilltop, a walled building stands with a single light in
         its window.""",
         'mobs': [('carrion_vulture', 1), ('risen_soldier', 1)]},
    ],
    'mobs': [
        {'id': 'carrion_vulture', 'aliases': 'vulture carrion', 'short': 'a carrion vulture', 'role': 'standard', 'level': 45,
         'long': 'A carrion vulture as tall as a man hops toward you, wings spread.', 'flags': 'f', 'align': -400, 'attack': 'bite',
         'desc': 'Bald-headed and enormous, gorged on the field. It has learned that the living taste better.'},
        {'id': 'risen_soldier', 'aliases': 'soldier risen dead', 'short': 'a risen soldier', 'role': 'standard', 'level': 47,
         'long': 'A risen soldier in rusted mail lifts a broken spear.', 'flags': 'f', 'align': -900,
         'desc': 'He died on this field a year ago, facing west. The West took his body and turned it around.',
         'equip': [('rusted_longsword', 'wield', 60), ('rusted_mail', 'body', 20)]},
        {'id': 'camp_follower_ghost', 'aliases': 'ghost follower woman', 'short': 'the ghost of a camp follower', 'role': 'elite', 'level': 47,
         'long': 'A ghostly woman stirs a pot over a dead fire, weeping.', 'flags': 'b', 'align': -300, 'sex': 2,
         'desc': 'She followed her husband to war, cooked for his company, and died when the camp was overrun. She is still waiting for him to come back for supper.'},
        {'id': 'ghost_officer', 'aliases': 'officer ghost', 'short': 'a ghostly officer', 'role': 'elite', 'level': 49,
         'long': 'A ghostly officer moves the pieces on the battle map, over and over.', 'flags': 'b', 'align': -200, 'sex': 1,
         'desc': 'He planned the battle. He has been trying for a year to find the plan that would have won. There was none.',
         'carry': [('battle_plan', 100)]},
        {'id': 'waiting_dead', 'aliases': 'dead waiting wounded', 'short': 'a dead soldier on a cot', 'role': 'standard', 'level': 46,
         'long': 'A dead soldier sits up on his cot, holding his wound closed.', 'flags': 'f', 'align': -800,
         'desc': 'He waited for the surgeon until he died. He is still waiting, and he is angry now.'},
        {'id': 'surgeon_ghost', 'aliases': 'surgeon ghost', 'short': 'the surgeon\'s ghost', 'role': 'elite', 'level': 48,
         'long': 'The surgeon\'s ghost moves between the cots with a bloody saw.', 'flags': 'bf', 'align': -500, 'sex': 1,
         'desc': 'He could not save them then. Now he tries to save the living, and his cure is the saw.',
         'equip': [('ghost_saw', 'wield', 100)]},
        {'id': 'risen_sergeant', 'aliases': 'sergeant risen', 'short': 'a risen sergeant', 'role': 'elite', 'level': 49,
         'long': 'A risen sergeant bellows silent orders, dressing the ranks of the dead.', 'flags': 'f', 'align': -900, 'sex': 1,
         'desc': 'Even dead, he keeps his line straight.',
         'equip': [('sergeant_halberd', 'wield', 100)]},
        {'id': 'shield_wall_dead', 'aliases': 'dead shield wall', 'short': 'a dead shieldman', 'role': 'standard', 'level': 48,
         'long': 'A dead shieldman locks his shield with those beside him.', 'flags': 'f', 'align': -900,
         'desc': 'The left flank held until the end. It holds still.',
         'equip': [('dented_tower_shield', 'shield', 30)]},
        {'id': 'death_rider', 'aliases': 'rider death cavalry', 'short': 'a death rider', 'role': 'elite', 'level': 49,
         'long': 'A dead rider on a skeletal grey horse levels a broken lance.', 'flags': 'f', 'align': -900,
         'desc': 'The cavalry died charging. It charges still, through the living and the dead alike.',
         'equip': [('cavalry_lance', 'wield', 70)]},
        {'id': 'vulture_matriarch', 'aliases': 'vulture matriarch', 'short': 'the vulture matriarch', 'role': 'champion', 'level': 49,
         'long': 'A vulture as big as a horse rises on the highest ledge, hissing.', 'flags': 'bfl', 'align': -500, 'attack': 'bite',
         'desc': 'The oldest and fattest of them, her beak like a cleaver.',
         'carry': [('vulture_cloak', 100)]},
        {'id': 'risen_engineer', 'aliases': 'engineer risen', 'short': 'a risen engineer', 'role': 'standard', 'level': 47,
         'long': 'A risen engineer hauls on a rope, rebuilding the engine.', 'flags': 'f', 'align': -900,
         'desc': 'A siege crewman who died beneath his own trebuchet, still working.',
         'equip': [('engineer_maul', 'wield', 60)]},
        {'id': 'bone_engineer', 'aliases': 'engineer bone master', 'short': 'the bone engineer', 'role': 'champion', 'level': 49,
         'long': 'A dead master engineer directs the bone engine, a measuring rod in hand.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'In life he built the army\'s engines. In death he builds the West\'s, from the bodies of his friends.',
         'equip': [('engineer_maul', 'wield', 100)], 'carry': [('engineer_lens', 100)]},
        {'id': 'grave_risen', 'aliases': 'risen grave dead', 'short': 'a grave-risen corpse', 'role': 'standard', 'level': 47,
         'long': 'A corpse claws its way out of the mass grave.', 'flags': 'f', 'align': -900, 'attack': 'claw',
         'desc': 'Its friends buried it with honour. It has come back without any.'},
        {'id': 'roll_caller', 'aliases': 'caller roll', 'short': 'the roll caller', 'role': 'champion', 'level': 49,
         'long': 'A dead quartermaster reads names from a rotting roll.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'He calls the company roll, and each name he calls rises. Stop him before he reaches the end.',
         'carry': [('company_roll', 100)]},
        {'id': 'drowned_soldier', 'aliases': 'soldier drowned', 'short': 'a drowned soldier', 'role': 'standard', 'level': 48,
         'long': 'A drowned soldier in rusting armour rises from the ford.', 'flags': 'f', 'align': -900,
         'desc': 'He fled for the river and drowned under the weight of his mail.',
         'equip': [('rusted_longsword', 'wield', 40)]},
        {'id': 'ford_guardian', 'aliases': 'guardian ford ghost', 'short': 'the guardian of the ford', 'role': 'elite', 'level': 50,
         'long': 'A pale ghost in battered armour stands guard behind the wagon.', 'flags': 'b', 'align': 600, 'sex': 2,
         'desc': 'She held the ford until dusk with eleven others. She is not risen; she is simply refusing to leave. She will not fight the living unless they come at her.',
         'equip': [('ford_sword', 'wield', 100)]},
        {'id': 'pyre_tender', 'aliases': 'tender pyre', 'short': 'the pyre tender', 'role': 'elite', 'level': 50,
         'long': 'A tall gaunt figure feeds bones into the grey flame.', 'flags': 'bf', 'align': -1000,
         'desc': 'A servant of Nu\'Groth, flesh grey as ash, eyes burning with the same cold fire as the pyre.',
         'equip': [('pyre_hook', 'wield', 100)]},
        {'id': 'grey_necromancer', 'aliases': 'necromancer grey', 'short': 'the grey necromancer', 'role': 'champion', 'level': 50,
         'long': 'A necromancer in robes of human skin chants over a heap of corpses.', 'flags': 'bfl', 'align': -1000, 'sex': 2,
         'desc': 'One of Nu\'Groth\'s high servants, sent east to raise the fallen army as a weapon against the living. She has raised a thousand already.',
         'equip': [('skin_robe', 'about', 100), ('raising_wand', 'hold', 100)]},
        {'id': 'dead_knight', 'aliases': 'knight dead honour guard', 'short': 'a dead knight of the honour guard', 'role': 'elite', 'level': 50,
         'long': 'A dead knight of the honour guard raises a notched sword.', 'flags': 'f', 'align': -900, 'sex': 1,
         'desc': 'Sworn to defend the royal standard to the death. They did, and they are defending it still, for a different master.',
         'equip': [('honour_blade', 'wield', 60), ('rusted_mail', 'body', 30)]},
        {'id': 'fallen_marshal', 'aliases': 'marshal fallen', 'short': 'the Fallen Marshal', 'role': 'boss', 'level': 50,
         'long': 'The Fallen Marshal stands beneath the grey standard, sword raised to his dead army.', 'flags': 'bfl', 'align': -1000, 'sex': 1,
         'desc': 'Marshal of the realm, hero of a dozen campaigns, he led the last army west to break the darkness and died with it on this hill. Nu\'Groth raised him first of all, and gave him back his army, and pointed him east.',
         'equip': [('marshals_sword', 'wield', 100), ('marshals_plate', 'body', 100)], 'carry': [('royal_standard', 100)]},
    ],
    'objs': [
        {'id': 'battle_plan', 'kind': 'note', 'aliases': 'plan battle map', 'short': 'a bloodstained battle plan',
         'long': 'A bloodstained battle plan lies here.', 'weight': 1,
         'extras': {'plan battle map': 'Every unit marked, every manoeuvre timed. In the margin, in a shaking hand: IT DOES NOT TIRE. IT DOES NOT BREAK. IT DOES NOT DIE.'}},
        {'id': 'rusted_longsword', 'kind': 'weapon', 'level': 47, 'attack': 'slash', 'aliases': 'longsword sword rusted',
         'short': 'a rusted longsword', 'long': 'A rusted longsword lies here.'},
        {'id': 'rusted_mail', 'kind': 'armor', 'slot': 'body', 'level': 47, 'aliases': 'mail rusted', 'short': 'a coat of rusted mail',
         'long': 'A coat of rusted mail lies here.'},
        {'id': 'ghost_saw', 'kind': 'weapon', 'level': 48, 'attack': 'slash', 'aliases': 'saw ghost bone',
         'short': 'a cold bone saw', 'long': 'A bone saw, cold as ice, lies here.', 'affects': [('hitroll', 2)]},
        {'id': 'sergeant_halberd', 'kind': 'weapon', 'level': 49, 'attack': 'slash', 'aliases': 'halberd', 'two_handed': True,
         'short': 'a sergeant\'s halberd', 'long': 'A long halberd lies here.', 'affects': [('damroll', 2)]},
        {'id': 'dented_tower_shield', 'kind': 'armor', 'slot': 'shield', 'level': 48, 'aliases': 'shield tower dented',
         'short': 'a dented tower shield', 'long': 'A tall, dented shield lies here.'},
        {'id': 'cavalry_lance', 'kind': 'weapon', 'level': 49, 'attack': 'pierce', 'aliases': 'lance cavalry',
         'short': 'a broken cavalry lance', 'long': 'A broken cavalry lance lies here.'},
        {'id': 'vulture_cloak', 'kind': 'armor', 'slot': 'about', 'level': 49, 'aliases': 'cloak vulture feather',
         'short': 'a cloak of vulture feathers', 'long': 'A cloak of dark feathers lies here.', 'affects': [('move', 30), ('dex', 1)]},
        {'id': 'engineer_maul', 'kind': 'weapon', 'level': 48, 'attack': 'pound', 'aliases': 'maul engineer',
         'short': 'an engineer\'s maul', 'long': 'A heavy wooden maul lies here.'},
        {'id': 'engineer_lens', 'kind': 'worn', 'slot': 'hold', 'level': 49, 'aliases': 'lens engineer glass',
         'short': 'an engineer\'s sighting lens', 'long': 'A brass sighting lens lies here.', 'affects': [('hitroll', 3), ('int', 1)]},
        {'id': 'company_roll', 'kind': 'note', 'aliases': 'roll company', 'short': 'a rotting company roll',
         'long': 'A rotting company roll lies here.', 'weight': 1,
         'extras': {'roll company names': 'Two hundred names, every one marked DEAD. Some have been marked a second time: RISEN.'}},
        {'id': 'ford_sword', 'kind': 'weapon', 'level': 50, 'attack': 'slash', 'aliases': 'sword ford',
         'short': 'the sword of the ford', 'long': 'A notched sword with a hilt wrapped in blue cloth lies here.', 'affects': [('hitroll', 2), ('damroll', 2)]},
        {'id': 'pyre_hook', 'kind': 'weapon', 'level': 50, 'attack': 'pierce', 'aliases': 'hook pyre',
         'short': 'a pyre hook', 'long': 'A long iron hook black with soot lies here.'},
        {'id': 'skin_robe', 'kind': 'armor', 'slot': 'about', 'level': 51, 'aliases': 'robe skin',
         'short': 'a robe of stitched skin', 'long': 'A robe of stitched human skin lies here.', 'affects': [('mana', 50), ('save_spell', -3)]},
        {'id': 'raising_wand', 'kind': 'worn', 'slot': 'hold', 'level': 51, 'aliases': 'wand raising bone',
         'short': 'a wand of finger bones', 'long': 'A wand made of finger bones lies here.', 'affects': [('int', 2), ('mana', 30)]},
        {'id': 'honour_blade', 'kind': 'weapon', 'level': 50, 'attack': 'slash', 'aliases': 'blade honour',
         'short': 'an honour guard\'s blade', 'long': 'A fine notched blade lies here.', 'affects': [('hitroll', 1)]},
        {'id': 'marshals_sword', 'kind': 'weapon', 'level': 52, 'attack': 'slash', 'aliases': 'sword marshal',
         'short': 'the Marshal\'s sword', 'long': 'A long sword with a gold-wired hilt lies here.', 'affects': [('hitroll', 3), ('damroll', 4)]},
        {'id': 'marshals_plate', 'kind': 'armor', 'slot': 'body', 'level': 52, 'aliases': 'plate marshal',
         'short': 'the Marshal\'s plate', 'long': 'A suit of fine plate, dented and grey, lies here.', 'affects': [('hit', 40), ('con', 1)]},
        {'id': 'royal_standard', 'kind': 'treasure', 'level': 50, 'aliases': 'standard royal banner', 'short': 'the royal standard',
         'long': 'A tattered royal standard lies here.', 'weight': 6, 'cost': 2000,
         'extras': {'standard banner': 'The royal arms, torn and grey. The quartermasters at Midgaard would weep to see it brought home.'}},
    ],
}
