"""Mines of Moria (zone 40) re-themed as the Lost Delvings of Kar-Dumhal.

Kar-Dumhal was a dwarven mine under a lone mountain north of Miden'Nir.  The
dwarves of the Kingdom (zone 65) lost it when their deep tunnels broke into
passages that had been dug from the other side -- from the west, under the
march.  What came up through them still holds the delvings: kobold diggers,
orcs, hobgoblins, renegade men who have gone over to Nu'Groth, and older things
in the deep.  The north side of the mountain is wild foothill country, with
trails to New Thalos, to Rand's valley, and a shadow that opens into the High
Tower's Shadow Grove.  The Tolkien names (Moria, Mount Moria) are gone.

Level 1 (4010-4030) is the upper workings; level 2 (4050-4074) the fire caves
and the old maze of exploratory drifts; level 3 (4100-4126) the deep: the
golden cave, the invaders' torch-lit camp, and the dwarves' sealed vault.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs


def room(name, desc, **kw):
    d = dict(name=name, desc=desc)
    d.update(kw)
    return d


# ====================================================================== approach
R[4000] = room('The Hill Road', """
    A rutted cart road climbs north out of the plains into low, bare hills.  The
    dwarves once hauled ore down this road to the markets of the east; now the
    ruts are full of weeds and nobody comes this way who can help it.  Far off to
    the northeast the first peaks of a long mountain chain rise grey against the
    sky.  The road runs north into the hills and south back to the plains.""")
R[4001] = room('The Hill Road', """
    The road winds between dark, scrubby hills that close in on either side.  A
    milestone lies toppled in the ditch, its dwarven runes chipped away by
    someone with a hammer and a grudge.  Ahead to the north a single mountain
    stands alone, black and enormous, apart from all the others.  The road
    continues north and falls away south.""",
    extras={'milestone stone runes': 'A squat dwarven milestone, knocked flat. Most of the runes have been hacked out; what remains reads "KAR-DUM..." and a distance no one will walk again.'})
R[4002] = room('The End Of The Road', """
    The cart road ends at a turning-place of packed stone where the ore wagons
    were once loaded.  The lone mountain looms directly north, and a narrow trail
    climbs through the rocks to the dark mouth of the old mine.  Someone has
    scratched a warning on a boulder beside the trail.  To the northeast the
    southern end of the great range can be seen.  The road leads back south.""",
    extras={'boulder warning scratch scratches': 'Scratched deep into the boulder in dwarvish and then, more crudely, in the common tongue: "SEALED. DO NOT DIG. THEY ARE BELOW."'})

# ====================================================================== level 1
R[4010] = room('The Mine Mouth', """
    The adit of the mine opens into a low chamber some forty feet long, its
    walls marked by dwarven picks.  The great timber gate that once closed it
    lies in splinters on the floor, broken outward, from inside.  Fresh air comes
    in from the south, where the trail leads back down; to the north a tunnel
    runs on into the mountain.""",
    extras={'gate timber splinters': 'Heavy oak beams bound with iron, smashed outward. The iron bands are bent the wrong way, as if something pushed from within.'})
R[4011] = room('The Entry Drift', """
    A narrow drift squeezes north between walls slick with seeping water.  The
    smell of wet stone and old mould thickens with every step away from the
    light, and the dwarves' tally marks on the wall stop abruptly partway along.
    The last breath of fresh air comes from the south.""")
R[4012] = room('A Bend In The Drift', """
    The drift turns sharply here.  To the north it opens into a wider cave; to
    the east it runs on through the mountain.  An abandoned ore barrow lies on
    its side across the bend, one wheel missing.""",
    extras={'barrow ore': 'A dwarven ore barrow, its bed still half full of grey stone. Whoever was pushing it left in a hurry.'})
R[4013] = room('A Dusty Drift', """
    Dust lies thick on the floor of this east-west drift, and the only marks in
    it are the small, clawed prints of kobolds.  No dwarf has walked here in a
    long time.  The way runs east and west.""")
R[4014] = room('The Breach', """
    The old drift curves away to the south and west here, but in the north wall
    a new hole has been torn through the rock, rough and unshored, much younger
    than the dwarven work around it.  The spoil from the digging lies heaped
    against the wall, and it was dug from the other side.""",
    extras={'hole breach spoil': 'The rubble lies on this side of the wall, pushed out. Whatever dug this tunnel came from the north and broke through into the dwarves\' mine.'})
R[4015] = room('A Jagged Drift', """
    The drift jags from west to north here.  The walls sweat with condensation
    and the roof hangs low enough to brush the head; the weight of the mountain
    above is easy to imagine.  Cracked props of black timber hold up the
    ceiling, and none of them look sound.""")
R[4016] = room('The Great Stope', """
    A wide stope where the dwarves once quarried out a whole seam, leaving a
    cavern so broad that its eastern and western ends are lost in darkness.
    Pillars of unworked rock hold up the roof.  A drift leads south out of the
    stope, and the cavern stretches away east and west.""")
R[4017] = room('The East End Of The Stope', """
    The stope ends against a wall worn smooth and rippled by water long before
    the dwarves came.  A cold draught rises from cracks along its foot, and
    there is no way on.  The rest of the cavern lies west.""")
R[4018] = room('The Bone Cave', """
    A cave narrows here into a tunnel that runs south, while the cave itself
    goes on north into the dark.  In one corner lies a great heap of bones,
    gnawed clean and sorted, the small ones on one side and the large on the
    other.""",
    extras={'pile bones heap': 'Kobold bones, goat bones, and -- unmistakably -- the broad, heavy skulls of dwarves. Someone has arranged them with care.'})
R[4019] = room('The Water-Cut Passage', """
    A wide passage runs north and south, its walls smooth and curved where an
    underground river carved them long ago.  The dwarves widened it into a haul
    road; the iron rails are gone, prised up and carried off by the newcomers.""")
R[4020] = room('The Shaft Alcove', """
    A small alcove opens off the main drift.  In its floor a winding shaft
    drops away into the lower workings, the windlass that served it smashed and
    the rope cut.  The only other way out is north.""",
    extras={'windlass rope shaft': 'The windlass has been beaten to pieces and the rope cut clean. Somebody did not want anything coming up. It came up anyway.'})
R[4021] = room('The Sweating Shaft', """
    The drift ends here at a broad shaft sunk in the northwestern corner of the
    floor.  The air rising from it is warm and wet and clings to the skin, and
    it carries a faint, sweetish smell.  The drift leads back east.""")
R[4022] = room('The Damp Drift', """
    Moisture hangs so thick in this drift that it beads on cloth and metal
    alike.  Water runs in a thin sheet down the walls.  The drift goes north and
    west, and a large cavern opens to the east.""")
R[4023] = room('The West End Of The Stope', """
    The western reach of the great stope, where the dwarves stopped cutting.
    The air near the drift mouth to the west is heavy and wet, like standing in
    fog.  The walls and the far end of the cavern are lost in shadow; the stope
    stretches on to the east.""")
R[4024] = room('The Dripping Drift', """
    The walls here run with a constant trickle of water and the floor is a chain
    of stagnant pools, scummed and still.  Something has been wading through
    them, more than once.  The drift leads south, and to the west the air grows
    damper still.""")
R[4025] = room('The Lamp Cave', """
    The north end of a fair-sized cave where the dwarves kept their lamp store.
    Empty niches line the walls, every lamp taken.  An opening in the east wall
    leads to a junction of several tunnels, and the cave runs back south.""",
    extras={'niches niche lamps': 'Rows of little stone niches, each blackened by old flame. Not one lamp is left.'})
R[4026] = room('The Crossdrifts', """
    Four drifts meet here at a dwarven crossing, each once marked with a carved
    rune now hacked away.  A musty stench comes from the north; the western way
    opens at once into a cave, and the drifts to the south and east are black
    as pitch.""")
R[4027] = room('An Elbow In The Drift', """
    The drift bends here to run west and north.  A small alcove hides in the
    shadows just to the south, and a faint breath of moving air comes from
    somewhere to the north.""")
R[4028] = room('The Reeking Drift', """
    A narrow north-south drift.  A pale glimmer of daylight shows to the north,
    and with it comes a sweet, heavy smell of rot that catches in the throat.
    The drift leads back south.""")
R[4029] = room('The Air Cave', """
    A cave where fresh, cold air pours in from the north, and the dust is swept
    into ripples on the floor by the wind.  The dwarves cut their ventilation
    shafts here; now the wind only brings in the smell of the hills.  A tunnel
    leads south into the mountain.""")
R[4030] = room('The Light Shaft', """
    A shaft high overhead lets in a grey circle of sky, and in the dim light lies
    the source of the stench: the bodies of several creatures, torn open and
    left to rot.  Something large dens here and does not eat all it kills.  The
    only way out is the drift to the south.""",
    extras={'corpse corpses bodies': 'Kobolds and a goblin or two, ripped apart by something with a long body and a crushing bite. They have been here some time.'})

# ====================================================================== north side
R[4031] = room('The Valley Below The Mountain', """
    A small, cold valley on the north side of the mountain, ringed by bare
    hills.  An air-cave opens in the mountainside to the south.  To the north
    the valley climbs into the hills, and a steep trail climbs a hill to the
    east.""",
    exits={'e': 'A narrow trail climbs the steep hill to the east.'})
R[4032] = room('The Foothills', """
    A winding path through the foothills on the north flank of Mount Dumhal.
    Cairns of stacked stones mark the way, set up by dwarves long ago.  The path
    runs north and south.""",
    extras={'cairn cairns stones': 'Dwarven waymarks. Some have been kicked over; one has been rebuilt, crudely, with a small skull on top.'})
R[4033] = room('A Fork In The Foothills', """
    The path forks here.  It runs on north and south, while a rough trail
    breaks away east toward the mountains.  A wooden signpost once stood here;
    only its stump remains.""")
R[4034] = room('The Long Grass', """
    The grass grows rank and tall here, crushed flat in great swathes where
    something very heavy has lain or walked.  Boulders the size of carts lie
    scattered about, not where they fell but where they were thrown.  The way
    leads north to the edge of the hills, west deeper into them, and south to
    the fork.""")
R[4035] = room("The Foothills' End", """
    The foothills give out here onto open plains to the north.  The wind comes
    hard and cold across the flat grass.  The hills lie back to the south.""")
R[4036] = room('The Plains', """
    Open grassland under a wide grey sky.  The path leads south into the
    foothills.  A faint, almost hidden trail leads west toward a copse of dark
    trees that seems nearer than it should be.""")
R[4037] = room('The Path Through The Foothills', """
    The path runs east and west through the foothills.  To the west it returns
    to the fork; to the east it ends where a spur of the mountain chain thrusts
    up out of the ground and blots out half the sky.""")
R[4038] = room('The Foot Of The Spur', """
    The base of a great mountain, first of the chain that marches north from
    Mount Dumhal toward the top of the world.  A path leads back west through
    the foothills, and to the east a narrow, well-worn trail starts up the
    mountainside.  The trail is worn by paws, not boots.""")
R[4039] = room('A Trail Up The Mountain', """
    A narrow trail clings to the mountainside, worn deep by the passage of some
    animal.  It climbs on up toward the summit and drops west back to the foot
    of the mountain.  Tufts of tawny fur are caught on the thorns.""")
R[4040] = room('The Summit', """
    The top of the mountain is a flat, wind-scoured plateau some thirty yards
    across, smaller than it looked from below.  From here the march can be seen
    to the west, a brown haze under a darker sky.  A gouge in the north side of
    the plateau leads to a cave; a rough trail heads east down toward a hidden
    valley, and the way back is down.""")
R[4041] = room("The Lion's Den", """
    The gouge leads down into a cramped den that stinks of cat and old blood.
    Bones are scattered over a bed of flattened grass, some of them very large.
    A great mountain lion makes its lair here.  The only way out is south.""")
R[4042] = room('The Level Foothills', """
    The foothills flatten out here.  Off to the west a great cave mouth gapes in
    the side of a hill that rises too steeply and too suddenly from the land
    around it.  A path begins here, out of nothing, and leads east.""")
R[4043] = room('The Cave Mouth', """
    The tunnel inside the hill is far larger than it looked from outside: the
    roof is twenty feet up and the floor fifteen feet across, the walls rubbed
    smooth by something passing through.  Fresh air comes in from the east, and
    to the west the tunnel runs into darkness.""")
R[4044] = room("The Hill Giant's Hall", """
    A vast cavern, its roof twenty-five feet up or more and its walls lost in
    shadow.  In the middle of the sandy floor stands an enormous table of rough
    timber, tall enough to walk beneath without stooping, and around it lie the
    gnawed remains of many meals.  A great tunnel leads out of the east wall.""",
    extras={'table': 'A table built from whole tree trunks, lashed together. On it lie a cracked cauldron, a cartwheel used as a plate, and a dwarven helm used as a cup.'})
R[4045] = room('The Steep Trail', """
    The trail climbs a steep hill and levels out where it starts to pass
    between the mountains.  Loose scree slides away underfoot.  It goes on east
    through the hills and drops west to the valley.""",
    exits={'e': 'The rocky trail continues east between the mountains.',
           'w': 'The trail drops steeply west to the valley floor.'})
R[4046] = room('Between The Mountains', """
    The trail between the mountains seems to have no end.  Grey walls of rock
    rise on either side and the wind moans between them.  It runs east and
    west.""",
    exits={'e': 'The trail winds on eastward between the peaks.',
           'w': 'The trail winds on westward between the peaks.'})
R[4047] = room('The Eastern Foothills', """
    After the long trek between the mountains the trail comes out into
    foothills again.  A short way east the path turns toward a narrow trail
    that bends away to the northwest.  The mountain pass lies back west.""",
    exits={'e': 'The path continues east toward the narrow trail.',
           'w': 'The trail back through the mountains seems to go on forever.'})
R[4048] = room('A Turn In The Eastern Foothills', """
    A short way into the foothills the trail faces the long pass between the
    mountains to the west, which looks a hard and tiring road.  Eastward the
    path leads toward a narrow trail that bends away northwest.""",
    exits={'e': 'The path continues east toward the narrow trail.',
           'w': 'The trail through the mountains seems to go on forever.'})
R[4049] = room('The Bend Toward Thalos', """
    The trail turns here from its westward run into a track meandering away to
    the north, toward the mountain road to New Thalos.  Refugees have come this
    way; a dropped shoe and a broken cart axle lie in the ditch.""",
    exits={'n': 'A narrow trail winds away north into the mountains.',
           'w': 'The trail heads west toward the mountains.'})

# ====================================================================== level 2
R[4050] = room('The Mossy Bend', """
    The tunnel bends from east to south.  The walls are cold and wet, and a
    greenish moss grows thick near the roof on the northern side, glowing very
    faintly in the dark.""",
    extras={'moss': 'A pale green moss that gives off a faint, sickly light. The dwarves never wrote of it. It came with the newcomers.'})
R[4051] = room('The Broken Steps', """
    The tunnel narrows sharply here, and eastward the floor drops nearly five
    feet in a run of jagged, broken steps.  The dwarves cut them square; claws
    have since chewed their edges.  Westward the floor is smooth.""")
R[4052] = room('The Spring', """
    The floor levels out again.  A small spring bubbles up beside the southern
    wall into a stone basin the dwarves carved for it, though the water now
    tastes of iron and something worse.  The tunnel runs east and west.""",
    extras={'spring basin water': 'Clear water in a carved basin, with a faint oily sheen. Nobody has drunk here in a long time and lived to complain.'})
R[4053] = room('The Right-Angle Drift', """
    The drift turns at a right angle, leading north and east.  To the north it
    runs on through the gloom of the deep; to the east, unexpectedly, the drift
    opens into a large cave lit by the red flicker of fire.""")
R[4054] = room('The Fire Cave', """
    The north end of a great cave lit by a flickering red glare from a huge fire
    that burns a short way to the south.  The light throws long, leaping shadows
    on the walls, and they do not always move with the flames.  Tunnels lead
    away east and west, half hidden in the shadows.""")
R[4055] = room('The Old Drifts', """
    A cramped exploratory drift, low and damp, one of many the dwarves cut while
    searching for the seam.  It twists away into darkness and this branch ends
    here; the only way back is west.""")
R[4056] = room('The Forge-Fire', """
    In the middle of the cave burns an enormous fire, built in the stone hearth
    of the dwarves' old forge and fed with their own timbers.  It gives light
    enough to see both ends of the cave, north and south.  Iron scraps lie
    around the hearth, beaten crudely into blades.""",
    extras={'fire hearth forge': 'The fire has burned here a long time. The roof is black with soot and the floor grey with ash. The great dwarven hearth now serves those who drove the dwarves out.',
            'scraps iron blades': 'Dwarven rail-iron and pick-heads, hammered into ugly, serviceable blades by someone with no skill and no patience.'})
R[4057] = room('The Old Drifts', """
    Another low, wet drift in the warren of exploratory tunnels.  Pick marks
    show where the dwarves gave up on this one and started a new one beside it.
    The way leads north and south.""")
R[4058] = room('The Old Drifts', """
    The drift turns here, the roof dripping steadily onto a fallen prop.  A
    chalk mark on the wall, a dwarven arrow, points south.  The ways lead south
    and west.""")
R[4059] = room('The Rivulet Drift', """
    A drift deep in the heart of Mount Dumhal.  A thin rivulet runs along the
    north wall and down the slope to the east, where the drift plunges deeper
    into the earth.  Westward it climbs a little toward damper air.""")
R[4060] = room('The Still Pool', """
    The drift runs nearly level here.  The rivulet along the north wall feeds a
    small black pool, yet the pool never rises, as if something below drinks it.
    The drift climbs west, and to the east a red flicker shows where it opens
    into a cave.""",
    extras={'pool water': 'Black, still water. It never ripples, even when the rivulet runs into it.'})
R[4061] = room('The South Fire Cave', """
    The southern end of the great fire cave, lit by the glare of the fire a
    short way north.  Crude bedding of stolen dwarven cloth lies heaped along
    the walls, where the warband sleeps.  Tunnels lead away west and south.""")
R[4062] = room('The Old Drifts', """
    A small, damp drift whose low roof is furred with pale growth.  Water seeps
    from every crack and gathers in shallow puddles that nothing has disturbed
    for years.  The drift runs east and west.""")
R[4063] = room('The Old Drifts', """
    The drift bends north and east here.  Someone has lined the floor with
    sharpened stakes, and then, it seems, forgotten them; one still holds a
    scrap of hide.""")
R[4064] = room('The Shaft Foot', """
    A small round chamber at the bottom of a shaft.  The roof is smooth and in
    its centre a well-rounded hole leads up to the workings above.  The walls
    are damp to the touch, and the chamber narrows west into a drift.""")
R[4065] = room('The Old Drifts', """
    A low drift that twists away into darkness.  To the north a red glow marks
    the mouth of the great fire cave; the drift also leads east.""")
R[4066] = room('The Old Drifts', """
    Three drifts meet here in the warren: north, east and south.  Southward the
    way opens out into a great echoing cavern; the air from it is cold.""")
R[4067] = room('The Old Drifts', """
    A dead-end bay of the old workings, where the dwarves found nothing.  The
    drift leads north and west, and the scratches on the walls here were not
    made by picks.""")
R[4068] = room('The Echoing Cavern', """
    The northwest corner of a natural cavern so vast that every breath comes back
    as an echo.  Stalactites hang from the dark above like teeth, and stalagmites
    rise to meet them.  The cavern stretches east and south.""")
R[4069] = room('The Echoing Cavern', """
    The northeast reach of the great cavern.  Something drips steadily in the
    dark, and the echo makes it sound like footsteps.  A narrow drift leads off
    north; the cavern spreads away west and south.""")
R[4070] = room('The Echoing Cavern', """
    The southwest reach of the great cavern, where a forest of stalagmites rises
    from the floor.  Several have been snapped off and dragged away.  The cavern
    continues north and east.""")
R[4071] = room('The Echoing Cavern', """
    The southeast end of the great cavern, where the stone teeth hang lowest.
    Clawed tracks cross the floor toward a narrow tunnel in the east wall.  The
    cavern opens north and west.""")
R[4072] = room('The New Tunnel', """
    A narrow tunnel bores through the mountain, turning from east to south.  It
    is not dwarven work: the walls are gouged, not cut.  Its west side breaks
    through a natural crack into a great cavern.""")
R[4073] = room('The Unfinished Tunnel', """
    The gouged tunnel stops dead against a face of raw rock, its last few feet
    scraped at as if by hands.  The diggers stopped here and did not say why.
    The only way out is back west.""")
R[4074] = room('The Narrow Hole', """
    A small hole opens in the floor of the tunnel, far too narrow for anything
    larger than a kobold to pass, and warm air breathes up out of it.  The only
    way out is north.""",
    exits={'d': 'The hole is far too small to fit through. Warm air rises from it, smelling of smoke.'},
    extras={'hole floor': 'A narrow, worn hole. Something small has passed through it many times. Warm air breathes up from below, smelling of smoke.'})

# ====================================================================== shadow and Rand's valley
R[4075] = room('The Copse Of Dark Trees', """
    A copse of black-barked trees stands alone on the plain, silent, with no
    birds in it.  The plains lie to the east.  Just to the north a shadow hangs
    between the trunks, shifting shape all the time, and seems to beckon.""",
    exits={'n': 'A shadow hangs between the trees, deeper than it should be. Beyond it is somewhere else.'})
R[4076] = room('On A Mountain Trail', """
    A rough trail twists down the mountainside toward a small hidden valley in
    the shadow of another mountain to the east.  From here the valley proves
    tiny, scarcely thirty feet long, and its floor is strangely dark.  The
    summit is back west, and the trail drops down.""")
R[4077] = room('In The Hidden Valley', """
    A cramped, cold valley at the foot of the eastern mountain, its floor black
    with old cinders.  Nothing grows here.  A carefully hidden trail climbs the
    eastern mountain, and the way back is up.""")
R[4078] = room('In The Hidden Valley', """
    The far end of the hidden valley, in the shadow of the great mountain to the
    east.  A trail leads east up the mountain, vanishing and reappearing among
    the rocks as if it does not want to be followed.  The trail back climbs up
    the western slope.""")

# ====================================================================== level 3
R[4100] = room('The Deep Incline', """
    The drift falls steeply here toward the deep, and a rivulet of water rushes
    down one side of it.  The dwarves cut steps into the floor; most are worn
    smooth.  The drift runs straight east for a long way and climbs back west.""")
R[4101] = room('The Long Drift', """
    A broad haul drift, wide enough for four to walk abreast, sloping gently
    east.  A rivulet runs along the north wall.  Iron rings for lamps are set in
    the roof at even intervals, all empty.""")
R[4102] = room('The Long Drift', """
    The long drift goes on, and its walls begin to close in quickly to the east
    like the neck of a funnel.  Broken lamp glass crunches underfoot, as though
    a whole crew dropped their lights here at once.  The way runs east and west.""")
R[4103] = room('The Funnel', """
    The drift narrows here to room for two side by side.  Westward it widens;
    eastward it dives deeper.  At waist height in the southern wall is a round
    hole some two feet across, edged with a faint gold light.""")
R[4104] = room('The Bulb', """
    The drift ends in a round, bulb-shaped chamber thirty feet across.  The walls
    are dry and strangely blurred to the eye, and nothing grows on them.  The
    only way out is the drift climbing sharply from the west wall.""")
R[4105] = room('The Golden Cave', """
    The northeast corner of a vast cavern lit by a soft, unwholesome golden light
    that seeps out of the walls themselves.  The dwarves broke into this cave and
    thought they had found their fortune.  It stretches west and south.""",
    extras={'light gold golden walls': 'Gold-coloured veins pulse faintly in the rock. It is not gold. It is warm to the touch, and it is worthless.'})
R[4106] = room('The Golden Cave', """
    The northwest corner of the golden cavern.  Old dwarven pick marks score the
    glowing veins where they tried, and failed, to mine them.  A round hole two
    feet across opens in the north wall onto darkness.  The cave stretches east
    and south.""",
    extras={'light gold golden veins': 'The light is gold, but nothing else is. The dwarves\' picks cut into it and left only glowing dust.'})
R[4107] = room('The Hewn Passage', """
    A small passage makes a sharp turn here, south and west.  The walls are
    roughly hewn.  Southward the passage goes on in the dark; westward there is
    a soft golden glow.""")
R[4108] = room('The Golden Cave', """
    The southeast corner of the golden cavern.  The light pulses very slowly
    here, like breathing.  A crack in the east wall leads into a passage, and
    the cave stretches north and west.""",
    extras={'light gold golden': 'The glow brightens and fades in a slow rhythm. It is like standing inside something that sleeps.'})
R[4109] = room('The Golden Cave', """
    The middle of the golden cavern's western side.  A dwarf's pick lies here
    with its haft burned black and its head half melted.  The cave opens north,
    east and south.""",
    extras={'light gold golden': 'The veins are brightest here, and the air tastes of hot metal.',
            'pick haft': 'A dwarven pick, its iron head slumped as if it had been in a furnace. Whoever held it struck the wrong vein.'})
R[4110] = room('The Pit', """
    The tunnel ends abruptly in an alcove, at the very lip of a great hole in
    the floor.  One more step would have been the last.  A cold, rotten smell
    rises out of it, and far down there is a sound like digging.  The tunnel
    leads back west.""",
    exits={'d': 'A dropped stone falls and falls and never strikes bottom. This is the way they came up, from the west and below. Nobody sane goes down.'},
    extras={'hole floor pit': 'A dropped stone falls and falls and never strikes bottom. This is the way they came up, from the west and below. Nobody sane goes down.'})
R[4111] = room('The Orange Moss Tunnel', """
    The walls of this small tunnel are furred with a strange orange moss that
    flakes away at a touch.  The air is still and stale, with a rotten smell
    coming from the east.  The tunnel runs east and west, and low in the
    southern wall there is a small, easily missed hole.""",
    exits={'s': 'The hole is very small. You would have to crawl through it.'},
    extras={'moss walls wall': 'A dry, scratchy orange moss that crumbles under the fingers and leaves an orange stain that will not rub off.',
            'hole': 'A small hole low in the southern wall, just big enough to crawl into.'})
R[4112] = room('The Oily Tunnel', """
    This tunnel is unusually wide for the deep workings, yet the air is close and
    damp.  A thin film of moisture coats the walls and feels slick and oily
    under the hand.  The tunnel runs east and west.""",
    extras={'wall walls moisture coat coating': 'Colours swirl slowly through the film on the walls, like oil on water, though there is no oil here and no reason for it to move.'})
R[4113] = room('The Hewn Passage', """
    A natural passage running north and south, its walls roughly smoothed by
    dwarven chisels to ease the way.  It wanders deeper into the mountain.  A
    shadow in the eastern wall hides the mouth of a side tunnel.""")
R[4114] = room('The Golden Cave', """
    The southwest corner of the golden cavern, where the glow fades to a dull
    amber.  The cave stretches north, and a strange fold of shadow in the west
    wall hides a passage.""",
    extras={'light gold golden': 'The glow is dimmest here, a dull and dirty amber.',
            'shadow fold': 'The shadow hides the opening of a dark passage leading west.'})
R[4115] = room('The Dark Passage', """
    A short, dark passage ends here and its wall curves up toward the ceiling.
    Overhead is a hole just large enough to climb through, and handholds have
    been cut into the curve of the wall, too far apart for a dwarf's reach.  The
    passage leads east.""",
    extras={'handholds handhold wall': 'Deep holds gouged into the rock, spaced for long arms and long claws.'})
R[4116] = room('The Square Passage', """
    A dwarf-cut passage, square and true, wide enough for two to walk side by
    side.  It runs north and south, and far off to the south a pinpoint of
    yellow light flickers.""",
    extras={'light': 'A flickering yellow point, too steady for fire alone. Torches, perhaps, and someone to tend them.'})
R[4117] = room('The Secret Way', """
    A narrow passage that few have ever walked.  To the north there is a glimmer
    of golden light; to the south it leads toward a chamber.  Dwarven runes of
    warding are cut into the lintel, and all of them have been scratched out.""",
    extras={'runes lintel': 'Warding runes, deliberately defaced. Whatever the dwarves sealed in here, someone wanted it let out.'})
R[4118] = room('The Torch Cave', """
    A large cave lit by some twenty torches burning in iron sconces high on the
    walls, dwarven sconces filled with the invaders' pitch.  The dancing flames
    hold the eye too long.  The cave continues west and south, and in the north
    wall a narrow vertical crack may lead somewhere.""",
    exits={'n': 'The crack looks like a very tight fit.'})
R[4119] = room('The Torch Cave', """
    The northwest part of the torch-lit cave.  Stolen dwarven gear is piled here
    in heaps for sorting: helms, picks, cups and coin.  The cave continues east
    and south, and the rock wall to the west has an odd, too-smooth look.""",
    exits={'w': 'The rock wall to the west looks wrong somehow, as though it were set there.'},
    extras={'wall rock': 'The western wall is too smooth and too square. There is a hairline seam around it.',
            'gear heaps pile': 'Dwarven loot, sorted into heaps by a mind that values everything by weight.'})
R[4120] = room('The Rising Passage', """
    A passage just too narrow for two.  The floor climbs here so that the roof
    seems to dip.  To the south the passage narrows again; northward it widens.
    A flickering light shows from the south.""",
    extras={'light': 'It is nearly enough to light the passage. Torchlight, somewhere to the south.'})
R[4121] = room('The Dwarven Hall', """
    An unnaturally regular hall, ten feet broad and twelve high, its walls
    dressed and polished by dwarven masons.  Westward it narrows to a doorway
    five feet across.  At the east end the hall stops at a smooth rock wall.""",
    exits={'e': 'The smooth rock wall to the east looks as though it could be moved.'},
    extras={'wall rock': 'The smooth rock wall to the east looks as though it could be moved. It is a dwarven secret door, cleverly hung.'})
R[4122] = room('The Sealed Vault', """
    A small, perfectly round chamber that no stream ever carved.  Its walls are
    polished like glass and its two doorways, north and east, are exactly five
    feet broad and eleven tall.  The dwarves sealed something in here when they
    fled.  Whatever guards it now is not a dwarf.""",
    extras={'walls wall': 'Polished dwarven stonework, carved with a frieze of dwarves walking away from something, their heads bowed.'})
R[4123] = room('The Torch Cave', """
    The southeast part of the torch-lit cave.  Gnawed bones and broken jars
    litter the floor, and the smoke of the torches hangs under the roof in a
    brown pall.  The cave continues north and west.""")
R[4124] = room('The Torch Cave', """
    The southwest part of the torch-lit cave, where the invaders' rough
    pallets lie beneath the sconces.  The cave continues north and east, and a
    passage leads out of the western wall and turns north.""")
R[4125] = room('The Passage End', """
    The end of a narrow passage that leads away north.  The bare southern wall
    seems to dance with the shadows thrown by the torchlight from the cave to
    the east.""")
R[4126] = room('The Crawlway', """
    A crawlway barely two feet high, with jagged rock snagging at every move.
    There is no room to turn and none to fight.  It would be a very bad place to
    meet whatever made it.  It runs north and south.""",
    exits={'n': 'A small hole marks the northern end of the crawlway.',
           's': 'Torchlight shows at the southern end of the crawlway.'})


# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d


M[4000] = mob('the cave adder', 'adder snake large cave', 'A great cave adder lies coiled here, hissing at you.',
              'A long, pale adder, blind from the dark and fat on what it kills. Its fangs drip.')
M[4001] = mob('the green adder', 'adder snake green', 'A small green adder is here, and it does not look friendly.',
              'A thin green snake that hunts kobold pups in the drifts. Small, but its bite burns.')
M[4002] = mob('the centipede', 'centipede', 'A small centipede is making its way across the floor.',
              'A finger-long centipede, quite harmless, one of the few things down here that is.')
M[4003] = mob('the kobold digger', 'kobold digger', 'A kobold digger is here, scratching at the rock for something to eat.',
              'A scrawny, scaly kobold with claws worn down from digging. They came first, tunnelling under the march at the bidding of things further west.')
M[4004] = mob('the orc', 'orc', 'An orc prowls the drift, looking for something to kill.',
              'A squat, grey-skinned orc in scraps of dwarven mail. There is a mean, hungry look in its eyes.')
M[4005] = mob('the orc chieftain', 'orc chieftain large', 'A large orc chieftain is here, looking very mean.',
              'A huge, scarred orc who leads the warband in the upper workings. He wears a dwarf\'s ring on a thong around his thick neck, as a trophy.')
M[4050] = mob('the scarred renegade', 'warrior renegade scarred', 'A tall renegade is here, his body covered in more scars than you have ever seen.',
              'A man who deserted the wall and went over to the west. He is strong and brainless, and he fights like he has nothing left to lose.')
M[4051] = mob('the renegade', 'warrior renegade', 'A tall renegade warrior is here.',
              'A deserter from the march who now serves those who dig below. He knows his way with weapons and keeps his eyes from yours.')
M[4052] = mob('the hobgoblin', 'hobgoblin', 'A small hobgoblin stands here.',
              'A young hobgoblin, far from its band and quite lost in the dark drifts.')
M[4053] = mob('the brown adder', 'adder snake brown', 'A brown adder watches you from the rocks.',
              'A thick-bodied brown snake with a mean, flat head.')
M[4054] = mob('the white centipede', 'centipede white', 'A white centipede crawls here.',
              'A pale centipede that has never seen daylight. It does not seem to notice you.')
M[4055] = mob('the hobgoblin brute', 'hobgoblin brute large', 'A large hobgoblin brute is here.',
              'A broad, hulking hobgoblin wearing a necklace of dwarven teeth. It looks very dangerous.')
M[4056] = mob('the cave orc', 'orc cave', 'An orc is here, looking for something (or someone) to eat.',
              'A lean cave orc with pale, hungry eyes. It is not friendly.')
M[4057] = mob('the mountain lion', 'lion mountain', 'A mountain lion is here, growling at you viciously.',
              'A lean, tawny lion of the high country, with huge claws and long teeth. Game is scarce in the hills now, and it is hungry.')
M[4058] = mob('the hill giant', 'giant hill', 'A hill giant is here, tossing rocks around.',
              'A shaggy hill giant some nine feet tall. He is not clever, but he has learned that dwarves no longer come to drive him off.')
M[4100] = mob('the hedge-sorcerer', 'mage sorcerer hedge', 'A small, sharp-eyed sorcerer is standing here.',
              'A thin man in a grey robe stitched with signs from the west. He came down from the march to study what the dwarves found below, and the magic he has learned is cruel.')
M[4101] = mob('the cave troll', 'troll cave', 'A huge, mean-looking cave troll is here.',
              'A great grey troll set to guard the dwarves\' sealed vault, and what was found in it. It looks very dangerous.')
M[4102] = mob('the guardian serpent', 'snake serpent guardian green', 'A large green serpent is here, coiled like a guardian for some evil power.',
              'A thick green serpent with eyes that are far too knowing. Something from the west has put a mind behind them.')
M[4103] = mob('the scavenger', 'thief scavenger', 'A scavenger is here, all dressed in black.',
              'A thin man in black who picks the dwarves\' bones for coin. He is counting a handful of it now. Maybe you ought to count yours.')
M[4104] = mob('the ugly orc', 'orc ugly', 'An ugly orc is standing here.',
              'A misshapen orc, disgusting to look at even by the standards of its kind.')
M[4105] = mob('the centipede', 'centipede small', 'A small, harmless centipede is here.',
              'A tiny centipede that pays no attention to you whatsoever.')
M[4106] = mob('the renegade sellsword', 'warrior sellsword renegade human', 'A human sellsword is here, with an evil grin on his face.',
              'A sellsword who sold his blade to the west instead of to the wall. He does not look friendly at all.')
M[4107] = mob('the green kobold', 'kobold green', 'A green kobold is here.',
              'A slimy green kobold from the deepest tunnels, smelling of the pit.')

# ====================================================================== objs
O[4000] = dict(aliases='ring yellow green dwarven', short='a dwarven ring of yellow and green',
               long='A ring of yellow and green stonework lies here. It looks very old.',
               extras={'ring yellow green dwarven': 'A heavy dwarven ring of gold set with green stone. Inside the band is a name in runes, worn too faint to read.'})
O[4001] = dict(aliases='corpse goblin', short="a goblin's corpse",
               long='The half-rotten corpse of a goblin lies here, giving off a foul odour.')
O[4002] = dict(aliases='coins dwarven', short='some old dwarven coins',
               long='A small pile of old dwarven coins lies on the ground.')
O[4050] = dict(aliases='potion purple', short='a purple potion', long='A purple potion stands here.',
               extras={'potion purple': 'A thick purple draught in a stoppered vial, brewed by the invaders from something that grows in the deep.'})
O[4051] = dict(aliases='helmet metal dwarven helm', short="a dwarven miner's helmet",
               long="A dwarven miner's helmet lies here.",
               extras={'helmet metal dwarven helm': 'A close-fitting iron helmet with runes of warding around the brim. It still has a faint magic in it.'})
O[4052] = dict(aliases='mushroom pale', short='a pale mushroom', long='A small, pale mushroom grows here.',
               extras={'mushroom pale': 'A pale cave mushroom with a grey stem. It would be very unwise to eat it.'})
O[4053] = dict(aliases='dirk', short="a thieves' dirk", long='A beautifully crafted dirk is lying here.',
               extras={'dirk': 'A slender dirk of some greyish dwarven alloy, double-edged and very thin. A good weapon for a thief.'})
O[4100] = dict(aliases='blade black demon', short='a black demon blade', long='A black demon blade lies here.',
               extras={'blade black demon': 'A blade of black metal that drinks the light. It was sealed in the dwarves\' vault for a reason. Whoever wields it will feel the will of the west in their hand.'})
O[4101] = dict(aliases='gloves swordsmans swordmans', short="a pair of swordsman's gloves",
               long='A pair of finely crafted gloves lies on the ground here.',
               extras={'gloves swordsmans': 'Stiff leather gloves with steel across the knuckles, dwarf-made and the right kind of thing to wear in a fight.'})
O[4102] = dict(aliases='scroll identify dwarven', short='a dwarven scroll of identification',
               long='A fragile old scroll covered in dwarven runes lies here.',
               extras={'scroll identify dwarven': 'A brittle scroll of runes, the kind dwarven assayers used to name the properties of strange finds.'})
O[4103] = dict(aliases='slime mould green', short='a green slime mould',
               long='A green slime mould is here. It stinks beyond belief.',
               extras={'slime mould': 'It was never meant to be food -- at least, not for anything that walks in daylight.'})
O[4104] = dict(aliases='slime mould green', short='a green slime mould',
               long='A green slime mould is here. It stinks beyond belief.',
               extras={'slime mould': 'It was never meant to be food -- at least, not for anything that walks in daylight.'})

RETHEME = {
    'zones': {40: 'The Lost Delvings of Kar-Dumhal'},
    'rooms': R, 'mobs': M, 'objs': O,
}
