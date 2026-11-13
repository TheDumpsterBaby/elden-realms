"""The Three of Swords (zone 33) re-themed for the dark-fantasy east.

Hill farms and a mountain ridge east of the forest roads.  Stanneg by the
Mountains is a hill village emptied by the levies; its inn is the hall of the
Three Swords, a mercenary company that buys and sells blades for the front and
hires out to whoever pays.  Gabadiel, the smith-mage of the ridge, forged for
the company until he refused to sell his last three blades; three people
wrecked his smithy, killed him and took them.  The tracks split three ways:
east to Salle, captain of the Three Swords, in Stanneg; south to Duwick, whose
bandits and slavers hold the caves and prey on refugees fleeing the west; and
west, to a burned cottage and the peak where the old dragon Aglandiir keeps
what comes up his mountain.  Levels unchanged.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

# ------------------------------------------------------- the trail and smithy
R[3300] = dict(name='A Scraggly Trail', desc="""
    A faint trail leaves the main road to the west and climbs east into rocky
    hill country.  Grey stone and grey mountain grass make it hard to follow,
    and the refugees who come this way often lose it.  A weathered signboard
    stands here, out of place in such rough country.  The trail climbs east.""",
    extras={'sign signboard': 'A painted board, its paint cracking: "GABADIEL\'S SMITHERY", with an arrow pointing east. Under it someone has nailed a smaller board: "Blades for the Three Swords only. No refugees. No credit."'})
R[3301] = dict(name='A Scraggly Trail', desc="""
    The trail tops a rise and looks down into a very small valley, where a stone
    cottage stands in a neat yard.  Smoke does not rise from its forge chimney.
    The front door hangs open.  The trail drops down into the valley, and runs
    back west toward the road.""")
R[3302] = dict(name='A Groomed Path', desc="""
    The western end of a valley hardly big enough for the one house that stands
    to the east.  A path between clipped shrubs leads up to it.  The shrubs have
    been trampled flat in places, by more than one pair of boots in a hurry.
    The path ends here, by the climb back up into the hills.""")
R[3303] = dict(name='Outside The Smithery', desc="""
    The path runs from the edge of the valley to the cottage's front door in the
    east.  The house is silent.  The anvil-sign over the door has been knocked
    down and trampled, and there is a dark stain on the step.  The path leads back
    west across the valley.""",
    extras={'stain step': 'Dried blood, quite a lot of it, smeared toward the door as if something was dragged inside.'},
    exits={'e': 'The smithery\'s front door, heavy oak bound with iron.'})
R[3304] = dict(name='The Smithery', desc="""
    Ruin greets you.  The forge has been blasted apart, along with most of the
    back wall, and hammers, tongs and anvils lie scattered across the floor.
    The smith's bed still smoulders.  This was done by more than one person, to
    judge by the tracks in the soot, and they took their time.  A hole gapes in
    the east wall, and the front door is west.""",
    extras={'bed': 'Lucky! Under the scorched pillow is a half-written letter, unaddressed. The words not burnt or smeared speak of the smith-mage Gabadiel\'s masterwork: a sword of unequalled power, and two blades that came before it, set aside as "not yet what I was working toward". The letter ends: "The company has offered again. I will not sell these to be thrown away on the wall." Looking around, you see no swords at all.',
            'tracks dust soot': 'Three sets of prints lead out through the hole where the back wall used to stand.'},
    exits={'e': 'A ragged hole torn through the back wall leads out into a garden.',
           'w': 'The smithery\'s heavy front door.'})
R[3305] = dict(name='A Burnt Garden', desc="""
    This was once a tidy herb garden.  Somebody has burned it with fire that was
    not lit by any torch; the earth is glassy in places and the ashes are still
    warm.  The remains of a trail lead east to the edge of the valley, and the
    hole into the smithery is west.""",
    extras={'tracks track': 'They lead east.'})
R[3306] = dict(name='The Mountain Ridge', desc="""
    A bare ridge east of the little valley, where the wind never stops.  Looking
    back you can see the smithery's broken roof.  Sheer drops fall away to the
    north and east.  The ridge runs south, and the garden lies west.""",
    extras={'tracks track': 'The tracks lead south.'})
R[3307] = dict(name='Along The Mountain Ridge', desc="""
    The ridge runs north and widens to the south into a small plateau.  The
    drops on either side are too steep to try.  From here the whole country
    lies open: hill farms to the south and east, a small village in a valley,
    and westward a single tall peak, dark against the sky, that the farmers do
    not name.""",
    extras={'tracks track': 'They lead south.', 'peak': 'A black peak, taller than the rest. Smoke drifts from somewhere high on its side.'})
R[3308] = dict(name='The Parting Of The Ways', desc="""
    A small plateau at the southern end of the ridge, where gentle slopes run
    down east, south and west into different parts of the hills.  The ridge
    leads north.  The dark peak looms in the west, and the wind from that way
    is cold.  Three sets of tracks cross the dust here and part.""",
    extras={'tracks track': 'The three sets of tracks split up here: one west, one east, one south. Whoever they were, they did not trust each other enough to travel together.'})
R[3309] = dict(name='A Steep Slope', desc="""
    A slope runs down and west from the plateau above, into a deep bowl in the
    hills.  For such wild country there is a great deal of traffic here: boot
    prints, the drag-marks of something heavy, a child's shoe.  The plateau is
    back up to the north.""",
    extras={'signs tracks prints shoe': 'Boot prints, many of them, and among them the smaller bare prints of people who were made to walk. A child\'s shoe lies trodden into the dust.'})
R[3310] = dict(name='A Small Plateau', desc="""
    A narrow shelf of flat ground under a sheer wall of rock to the north.  You
    can climb back up the slope to the east or follow the shelf west.  A loose,
    unsafe slope drops away to the south.""")
R[3311] = dict(name='The End Of The Shelf', desc="""
    The shelf ends here at a steep drop to the south, under the same rock wall.
    The shelf runs back east, and a steep slope of shale climbs west.  From the
    edge you can see down into the bowl, where a cave mouth shows dark against
    the rock, south and far below.""")
R[3312] = dict(name='A Shale Slope', desc="""
    The shale here slides under every step, and you are nearly thrown off your
    feet.  It looks steadier to the north, and the slope drops back east to the
    shelf.  This is no place to be without a rope.""")
R[3313] = dict(name='The Overlook', desc="""
    A point of rock with a long view north over the hill farms.  Far below, a
    foot-path climbs toward the dark central peak.  Half the farms you can see
    have no smoke at their chimneys; their sons went to the wall, and the rest
    went east.  The only safe way off the point is south.""")
R[3314] = dict(name='A Rocky Slope', desc="""
    You slide your way across steep, broken ground, trying hard to keep your
    feet.  A small plateau lies up to the north, and the floor of the bowl is
    down to the west.  Neither way looks safe.""")
R[3315] = dict(name='The Floor Of The Bowl', desc="""
    The floor of the bowl, ringed by sheer rock walls that make it a natural
    fortress.  A small spring bubbles up here, and the ground around it is
    trampled to mud by many feet.  Bits of rope and cut cord lie in the mud.  A
    path runs south, and the rocky slope climbs east.""",
    extras={'rope cord': 'Lengths of rough rope, cut, as if prisoners were untied here to drink.'})
R[3316] = dict(name='Below The Cave', desc="""
    The path runs north to the spring and east toward a great cave in the
    mountainside.  Everything is quiet, much too quiet.  There are fresh
    footprints, and nobody to make them.""")
R[3317] = dict(name='The Cave Mouth', desc="""
    A cave leads into the heart of the mountain, lit by sconces on the walls.  A
    big rock sits by a firepit, and the ground is littered with rabbit bones, a
    broken whetstone and a heap of worn-out shoes taken from captives.  Many
    pairs of boots have beaten the earth bare.  The cave leads east, and the
    path is west.""",
    extras={'shoes heap': 'Shoes of every size, from refugees taken on the roads. The bandits take them so that nobody runs.'})

# ------------------------------------------------- the lit passages, north side
R[3318] = dict(name='Inside The Cave Mouth', desc="""
    Daylight comes in from the west and makes the sconce-flames gutter.  The
    passage splits north and south.  The north way is the more trodden.""")
R[3319] = dict(name='A Sconce-Lit Bend', desc="""
    The passage turns here, south toward the entrance and east deeper into the
    mountain.  Voices echo from somewhere far ahead.""")
R[3320] = dict(name='The Echoing Passage', desc="""
    A twisting passage runs east and west.  Low voices come from the east, but
    the echoes play tricks and there is no telling how near they are.""")
R[3321] = dict(name='A Dark Corner', desc="""
    One sconce here has burned out, leaving this corner black.  Brighter light
    shows to the south.  The passage runs back west.""")
R[3322] = dict(name='The Branching Passage', desc="""
    The passage forks three ways.  North leads back toward the entrance; west
    opens into a well-lit cave; east runs into the shadowed depths.""")
R[3323] = dict(name="The Bandits' Armoury", desc="""
    Sconces light weapon racks and chests of armour, kept neat and well-oiled.
    Most of the blades are cheap curved swords, but someone takes care of them.
    A tally chalked on the wall counts blades sold to the Three Swords.  The only
    way out is east.""",
    extras={'tally wall chalk': 'Rows of chalk strokes under two headings: "BLADES TO THE COMPANY" and "HEADS". The second list is longer.'})
R[3324] = dict(name='A Rubble-Strewn Passage', desc="""
    Loose stones and rocks litter the floor, making the going slow in the dim
    sconce-light.  The voices seem fainter here.  The passage runs south and
    west.""")
R[3325] = dict(name='The Coiled Passage', desc="""
    The cave coils round on itself like a snake, leading north and east.  Iron
    rings are set into the walls at waist height, for chaining people.""",
    extras={'rings ring': 'Iron rings sunk into the rock, worn bright by chains.'})
R[3326] = dict(name='A Chill Turn', desc="""
    Cold air breathes along this turn of the passage, which runs north and west.
    The voices grow louder from the north.  Scratched low on the wall are the
    names of the people who were chained here.""",
    extras={'names wall scratches': 'Names scratched into the rock with a nail or a fingernail: Ada of Ashford, Tam, Little Wenna, and many more, with no family names.'})
R[3327] = dict(name='The Torn Silk', desc="""
    The passage runs north toward the voices and south to another bend.  A scrap
    of red silk is caught on a jag of rock here, torn from someone's good
    dress as she was dragged past.""",
    extras={'silk cloth scrap red': 'A scrap of fine red silk, too good for these caves. A refugee family\'s best, carried out of the west and lost here.'})
R[3328] = dict(name='The Guard Post', desc="""
    Two large boulders, wiped clean, sit against the wall as seats.  A greasy
    food wrapper is trodden into the floor.  This is a guard post.  The main
    passage runs south, and a smaller tunnel leads west.""")
R[3329] = dict(name="Before The Slaver's Door", desc="""
    The tunnel ends to the north at a heavy wooden door set into the stone,
    finely made, too finely for these caves.  The way back to the main passage
    is east.  An echo makes you turn, but nothing is there.""",
    exits={'n': 'A sturdy wooden door, carved by a good craftsman for a different house.'})
R[3330] = dict(name="Duwick's Cavern", desc="""
    A natural cavern made over into an office and storeroom.  A brook rushes in
    through the south wall and out through a hole in the west.  Crates are
    stacked against the walls, and a battered oak desk by the door is heaped
    with ledgers.  Big lanterns keep it bright.  The door leads south.""",
    extras={'desk ledgers ledger papers': 'Ledgers in an unsteady hand: names, ages, heights, prices. Most are sold as labour, "to the hill farms" or "to the company". A few, the youngest, are marked only with a small grey circle and a far higher price.'},
    exits={'s': 'A sturdy wooden door.'})

# ------------------------------------------------- the dark passages, south side
R[3331] = dict(name='South Of The Mouth', desc="""
    South of the cave mouth the passage is badly lit, a sconce every fifteen
    feet.  A faint, steady thumping comes from somewhere deep below.  The way
    runs north and south.""")
R[3332] = dict(name='The Southern Bend', desc="""
    The passage bends east and north.  The far-off pounding makes the rock
    seem to have a heartbeat.""")
R[3333] = dict(name='The U-Turn', desc="""
    The passage doubles back sharply, north and west.  The air is damp, and
    slime on the floor gives off a smell of rot.""")
R[3334] = dict(name='A Dismal Twist', desc="""
    The tunnel twists south and east, bare and lifeless.  The thumping sound
    seems to come from every wall at once.""")
R[3335] = dict(name='The Last Sconce', desc="""
    The sconces stop here.  West, the tunnels are lit; south is utter darkness.
    The thumping goes on, patient.""")
R[3336] = dict(name='The Black Tunnel', desc="""
    A natural tunnel runs north toward the light and south into total dark.  The
    thumping is louder.  Somewhere a chain rattles.""")
R[3337] = dict(name='A Dark Corner', desc="""
    The passage turns north and east in deep gloom.  As you round it, the
    pounding sounds as if it is right beside you.""")
R[3338] = dict(name='The Weaving Tunnel', desc="""
    Darkness nearly total.  The tunnel weaves north and west.  Ahead, metal
    rings against stone: picks, and the clink of chains between blows.""")
R[3339] = dict(name='The Spoil Heaps', desc="""
    Heaps of earth and broken rock crowd the tunnel, and you must pick your way
    through.  Light glimmers to the east.  South, the tunnel goes back into the
    dark.""")
R[3340] = dict(name='The Fissure', desc="""
    The tunnel stops at a fissure in the rock.  Gravel and broken stone are
    heaped all around, dug out by hand to widen the crack into a passage
    through the mountain: a back door for the slavers, dug by their captives.
    The work is recent, and bloody.  The only way back is west.""")

# --------------------------------------------------------- Stanneg village
R[3341] = dict(name='A Rocky Slope East', desc="""
    A long, treacherous slope drops east toward a valley where a small village
    huddles.  Smoke rises from some of its chimneys, though not from many.
    The slope climbs back west toward the plateau.""")
R[3342] = dict(name='The Foot Of The Slope', desc="""
    You slither down the last of the slope.  Below, a few people move in the
    village, slowly.  The village road begins just to the east, and the slope
    climbs west, far up the mountain.""")
R[3343] = dict(name='The Main Road, West End', desc="""
    The western end of Stanneg's main road.  The people here go about their
    chores slowly, eyes down, as people do when every family has someone at the
    wall.  Two shops of wood and stone stand north and south.  The road runs
    east, and a slope climbs west.  There is a small sign here.""",
    extras={'sign': 'A board reads: "STANNEG BY THE MOUNTAINS. Population: 27." The 27 has been crossed out and rewritten several times, each time lower. The latest figure is 19.'})
R[3344] = dict(name='The Mountain Tavern', desc="""
    A tavern with no one in it.  The tavern-keeper went west with the last levy,
    and nobody has opened the place since.  Hunting trophies still hang on the
    walls: antlered heads, longbows, a boar's tusks, all of it gathering dust.
    The road is south.""",
    extras={'trophies heads bows': 'Old hunting trophies. Under one of the bows is a scrap of paper: "Back by harvest."'})
R[3345] = dict(name='The General Store', desc="""
    A small store of rope, candles, nails and pots.  The shelves are half
    empty; anything worth having was bought by the Three Swords and sent to the
    front.  The road is north.""")
R[3346] = dict(name='The Main Road', desc="""
    Little happens on this stretch of road.  East lies the village crossroads,
    and the road runs back west.  A fenced paddock to the south holds the
    village horses, those the company has not yet bought.""")
R[3347] = dict(name='The Corral', desc="""
    A grassy corral inside a stout wooden fence.  The horses look up warily as
    you come in.  They are good mountain stock, and every buyer for the front
    wants them.  The road is north.""")
R[3348] = dict(name='The Crossroads', desc="""
    The only crossroads in Stanneg by the Mountains.  Plain buildings stand to
    the north, south, east and west, and roads run off in all four directions.
    A muster notice is nailed to a post.""",
    extras={'notice post': '"The Three Swords are hiring. Good pay, good blades, good food. Ask for Captain Salle at the inn." Someone has scrawled underneath: "Ask where my brother is."'})
R[3349] = dict(name='A Small Road', desc="""
    A small road runs north through the village.  To the west is an open-sided
    farmers' market.  The road continues north, and the crossroads is just to the
    south.""")
R[3350] = dict(name="The Farmers' Market", desc="""
    An open-roofed market of empty stalls, save one.  A farmer's wife waits by
    her baskets with what her family grew; half of it is owed in tithe to the
    wall, and she sells the rest.  The road is east.""")
R[3351] = dict(name='The North End Of The Road', desc="""
    The small road ends here, curving into the front walk of a house to the
    east.  The shutters are closed.  The road runs south toward the middle of the
    village.""",
    exits={'e': 'A plain wooden front door. A ribbon of black cloth is tied to the latch.'})
R[3352] = dict(name='A Farmhouse', desc="""
    A simple farmhouse with a ladder up to a sleeping loft.  A wood-stove keeps
    it warm.  A rocking chair stands in the corner, a shawl over its back, and
    on the table is a letter from the wall that nobody has had the heart to put
    away.  The door is west.""",
    extras={'letter table': 'A short letter from Midgaard, sealed with the garrison\'s mark, regretting to inform the family. The name has been read so often the ink is smudged.'},
    exits={'w': 'The front door is set in the western wall.'})
R[3353] = dict(name='A Small Road, South', desc="""
    The road ends at a stone house to the south.  Smoke pours from its chimney in
    a thick dark stream and the windows are fogged.  The crossroads is north.""",
    exits={'s': 'A wooden front door, warm to the touch.'})
R[3354] = dict(name="The Hunter's House", desc="""
    The house is unbearably hot.  The fire is built up like a bonfire, with a
    huge stack of wood beside it.  The furnishing is spare: a hill landscape on
    the wall, an old bow, a row of bounty-tags from the company nailed by the
    door.  The door is north.""",
    extras={'tags bounty': 'Wooden tags stamped with three crossed blades, each one paid for a bandit\'s head.'},
    exits={'n': 'A plain wooden front door.'})
R[3355] = dict(name='The Well', desc="""
    The main road ends at a great well sunk deep into the earth.  To the north
    is a large building, a sign of three crossed swords hung over its double
    doors.  The crossroads lies west.  All around is rock and mountain; there is
    nowhere else to go.""",
    extras={'well': 'A deep stone well. The rope is new; the bucket comes up with clean, cold water.',
            'sign swords': 'Three crossed swords, newly painted over an older inn sign.'},
    exits={'n': 'A large pair of wooden double doors, the company\'s sign above them.'})
R[3356] = dict(name='The Stanneg Inn', desc="""
    The front room of the Stanneg Inn, now the hall of the Three Swords.  Racks
    of blades bought for the front stand along the walls under guard.  An arch to
    the west leads to the common room, and rickety stairs climb to the rooms.
    A threadbare rug lies on the floor, thick with cat hair.  The double doors
    lead out south.""",
    extras={'racks blades rack': 'Swords of every make, bought cheap and sold dear to the quartermasters of Midgaard.'},
    exits={'s': 'A large pair of wooden double doors.'})
R[3357] = dict(name='The Common Room', desc="""
    A great fire fights the drafts from the windows on the west and north.  Long
    benches and tables fill the room, where locals drink beside the company's
    hired blades and try not to be noticed.  At the end of the room the Three
    Swords sign up new recruits.  The arch leads east.""")
R[3358] = dict(name='The Reception', desc="""
    A short landing at the top of the stairs, lined with small brown doors, all
    of them shut and taken by the company's men.  A table holds a ledger, almost
    unused; the company's blades sleep free.  A painting of the mountains hangs
    above the stairs that lead back down to the inn.""")

# ------------------------------------------------------ west to the dark peak
R[3359] = dict(name='A Gentle Slope', desc="""
    A shallow slope of loose shale, easy enough to walk.  East is the high
    plateau; west is a flat ledge where trails lead up and down into the hills.
    High above to the west the dark peak seems to give off a weight of
    hopelessness.""")
R[3360] = dict(name='A Ledge', desc="""
    A ledge above a path that runs up and down.  Below, a cottage sits on a flat
    stretch of ground with smoke rising from it.  Above, the path climbs toward
    the dark peak.  Boot-tracks lead down toward the cottage, and the slope
    runs back east.""",
    extras={'tracks': 'One set of boot-tracks, leading down. They do not come back up.'})
R[3361] = dict(name='Outside A Burned Cottage', desc="""
    Closer, you see that the smoke is not from the chimney but from the gutted
    cottage itself.  Something torched it, thoroughly.  There is no sign of life.
    A large hole in the wall to the west leads inside, and the path climbs back
    up.""")
R[3362] = dict(name='The Burned Cottage', desc="""
    The whole cottage still smoulders.  In the centre of the ruin lies the
    burned body of a man, stretched out and blackened, one hand reaching for an
    empty scabbard.  Whatever burned this place did it from above, and did it
    well.  The hole leads east.""",
    extras={'body man scabbard': 'A charred body. The scabbard at his belt is sized for a short sword, and it is empty. Huge claw marks score the ground around the cottage.'})
R[3363] = dict(name='A Mountain Trail', desc="""
    The trail climbs straight up into the hard mountains.  High above, the dark
    peak seems to radiate dread, and the trail leads toward it.  The trail climbs
    higher to the west and drops back down the mountain.""")
R[3364] = dict(name='A Cold Trail', desc="""
    The trail climbs higher to the west.  Cold mountain air washes over you, and
    your back prickles; nothing that lives up here is likely to be small.  Back
    down the trail to the east looks very inviting.""")
R[3365] = dict(name='The Last Of The Trail', desc="""
    The trail climbs the side of the tallest mountain in the range, which stands
    against the sky like a monument to futility.  Safety lies back east; the
    trail climbs on to the west.""")
R[3366] = dict(name='Near The Peak', desc="""
    This is as close to the summit as most will come.  A tiny path leads up to
    the north toward a great cave hollowed in the mountainside, its inside
    pitch black.  The trail drops east, and that looks the better way.""")
R[3367] = dict(name='A Small, Dangerous Path', desc="""
    The path climbs up the face of the mountain toward the black cave.  It also
    drops south, which is safer.  Footsteps, heavy ones, sound from the rocks
    above your head.""")
R[3368] = dict(name='The Ambush Ledge', desc="""
    Too late you see that this broad ledge before the dark cave is a perfect
    place for an ambush.  Rocks the size of a man lie scattered about, thrown
    from above.  The view of the range is breathtaking.  The cave is north, and
    the path drops down.""")
R[3369] = dict(name='The Great Cave', desc="""
    The mouth of an enormous cave.  Around it lie burnt bones and scraps of wood
    and iron, the remains of those who came to steal.  Giant claw marks score the
    floor.  Two tunnels lead off, one up and one down, and the claw marks lead
    both ways.  The ledge is south.""")
R[3370] = dict(name='A Sloping Tunnel', desc="""
    The tunnel slopes up to the north into the mountain.  A gusty wind tugs at
    your clothes from somewhere ahead.  The claw marks continue up into the
    dark, and the tunnel leads back down.""")
R[3371] = dict(name='A Windy Tunnel', desc="""
    The tunnel climbs on and the wind is stronger.  The claw marks in the stone
    stop abruptly here, where heaps of dug earth and stone lie on the floor.
    The tunnel runs north and south.  Something about this place is wrong.""",
    extras={'dirt stone earth': 'It has been dug from somewhere, but where?',
            'claw claws track tracks mark marks': 'They stop very abruptly here, right where the heaps of earth begin.',
            'floor': 'The floor up ahead looks... strange. You do not think going ahead would be a good idea.'})
R[3372] = dict(name='The Pit', desc="""
    The floor ahead was an illusion, and you fall straight through it onto the
    poisoned spikes below.  You die slowly, bleeding, your head twisted at an
    awkward angle.""")
R[3373] = dict(name='A Sloping Tunnel Down', desc="""
    This tunnel slopes deep down into the heart of the mountain.  The air is
    still and too warm, and a deep musky odour hangs in it.  The giant claw marks
    lead down, and the cave mouth is up.""")
R[3374] = dict(name='Above The Lair', desc="""
    A bright, warm light shines from the north, after the dark of the tunnel
    above.  The heat makes you sweat, and the musk is so strong it is hard to
    breathe.  Something in your gut knows what is ahead.  The tunnel leads north
    and back up.""")
R[3375] = dict(name="Aglandiir's Lair", desc="""
    An enormous hall, as it must be for a dragon's bulk.  There is no heap of
    bones and gold here; instead it is hung with tapestries and drapes, rugs and
    other comforts taken from the farms below, and there is even a bed of dragon
    size.  Aglandiir has lived a long time and likes his comforts.  Everything
    that comes up his mountain, he keeps.  The tunnel leads south.""",
    extras={'tapestries tapestry drapes rugs': 'Fine hangings, many of them from the hill farms and the old manors east of the march. Some are scorched at the edges.'})

# =================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d


M[3300] = mob('a hill farmer', 'farmer hill', 'A hill farmer trudges by, looking for work that needs doing.',
              'A tired farmer of Stanneg, grey before his time. His sons went to the wall and his fields are too big for him alone.')
M[3301] = mob('the storekeeper', 'storekeeper shopkeeper', 'The storekeeper waits behind half-empty shelves.',
              'A thin, worried man who sells what the company leaves him. He watches your weapons more than your coin.')
M[3302] = mob('the horse-warden', 'cowgirl warden horsewarden woman', 'A horse-warden stands here, ready to defend her horses.',
              'A hard-faced woman with a crook and a knife. She has seen off company buyers, requisition men and bandits from this corral, and she will see you off too.')
M[3303] = mob('a mountain horse', 'horse mountain', 'A shaggy mountain horse grazes here.',
              'A sure-footed hill horse with soft brown eyes. The front wants every one of them.')
M[3304] = mob("the farmer's wife", "farmer's wife woman", "A farmer's wife offers you some of her harvest.",
              'A careworn woman with baskets of roots and fruit. Half of what she grows goes to the wall in tithe; she sells the rest and does not smile.')
M[3305] = mob('Aglandiir', 'aglandiir dragon prince', 'The old dragon Aglandiir lies here, watching you curiously.',
              'Aglandiir is a prince of his kind and very old. He takes no side in the war of the west and wants none; he only keeps what comes up his mountain, and burns what tries to leave with it.')
M[3306] = mob('the cyclops', 'cyclops giant', 'A cyclops crouches here, hefting a rock.',
              'A one-eyed hill giant that throws rocks at anything on the ledge. With one eye it often misses, and it growls each time it does.')
M[3307] = mob('Salle', 'salle woman captain', 'A woman ignores you completely, so intent is she upon her sword.',
              'Salle, captain of the Three Swords: tawny-skinned and tawny-haired, dressed in brown leather, with cold blue eyes that weigh you as a buyer weighs a horse. She sells blades and blades-for-hire to the front, and she does not ask where either came from.')
M[3308] = mob('Duwick', 'duwick man slaver', 'A truly immense man laughs at you, and draws his knife!',
              'Duwick, master of the slavers in these caves: seven feet tall and three hundred pounds, mostly muscle. He buys and sells refugees off the roads like cattle. An ornate scabbard hangs at his side with a silvered knife in it, a tiny weapon for such a huge man.')
M[3309] = mob('the receptionist', 'receptionist clerk', 'A receptionist offers you a room.',
              'A retired farmer keeping the inn\'s ledger for the company. He would rather be keeping sheep.')
M[3310] = mob('the innkeeper', 'innkeeper keeper', 'An aged innkeeper greets you as you enter.',
              'An old, grey innkeeper in a thick woollen sweater who let his inn to the Three Swords because the alternative was losing it. His eyes take in your weapons without much surprise.')
M[3311] = mob('a hill hunter', 'hunter hill', 'A hill hunter walks the street, bow on his back.',
              'A hard, weathered man with cold dark eyes. These days he hunts bandits for the company\'s bounty more often than he hunts deer.')
M[3312] = mob('a waiter', 'waiter', 'A waiter rushes by, intent on his business.',
              'A harried young man running drinks to the company\'s blades. He does not look at you; it is safer not to.')
M[3313] = mob('a waitress', 'waitress', 'A waitress rushes by, intent on her business.',
              'A harried young woman carrying drink and stew, who keeps out of reach of the company\'s men.')
M[3314] = mob('a bartender', 'bartender barkeep', 'A bartender polishes a clean glass here.',
              'A heavy, quiet man who polishes the same clean glass over and over and hears everything said at the tables.')
M[3315] = mob('a slaver bandit', 'bandit slaver', 'A slaver bandit springs into action at the sight of you.',
              'A filthy bandit, grimed from head to foot, who preys on the refugees fleeing the west. Only his curved sword is clean.')
M[3316] = mob('a bandit guard', 'bandit guard slaver', 'A bandit guard stands at attention here.',
              'A dirty, disciplined bandit with a scimitar and a coil of rope. Someone keeps these men in line, and it is not by kindness.')
M[3317] = mob('a chained refugee', 'slave miner worker refugee', 'A chained refugee is digging out a new passage here.',
              'A thin refugee from the west, chained at the ankles, who looks up at you with pleading eyes. He walked a hundred miles to get away from the march and ended here.')
M[3318] = mob('a hill farmer', 'farmer hill', 'A hill farmer sits over a cup, looking at nothing.',
              'A farmer of Stanneg drinking away the evening. He keeps glancing at the company\'s recruiting table.')
M[3319] = mob('a hill hunter', 'hunter hill', 'A hill hunter drinks alone by the fire.',
              'A hard, weathered hunter who has just been paid a bounty. He is not celebrating.')

# =================================================================== objs
O[3300] = dict(short='a turnip', aliases='turnip orange', long='A muddy turnip lies on the ground here.',
               extras={'turnip orange': 'A hard hill turnip. Most of them go west to the wall in sacks.'})
O[3301] = dict(short='a bale of wheat', aliases='bale wheat', long='There is a bale of wheat here.',
               extras={'bale wheat': 'It does not look appetising to you, but a horse might enjoy it. It is stamped with the tithe-mark of the wall.'})
O[3302] = dict(short='a great golden zither', aliases='zither golden', long='A huge golden zither rests in the corner.',
               extras={'zither golden': 'Someone truly huge, with very big claws, might be able to play this. You cannot.'})
O[3303] = dict(short='a barrel of perfume', aliases='barrel perfume', long='You can smell a barrel of perfume from across the room.',
               extras={'barrel perfume': 'A cask of rich scent, taken from some merchant\'s wagon on the roads. It smells of roses and money.'})
O[3304] = dict(short='a golden statue of Aglandiir', aliases='statue golden', long='A statue of Aglandiir stands here, made of solid gold.',
               extras={'statue golden': 'A striking likeness of the dragon, cast from the melted gold of many hoards.'})
O[3305] = dict(short='a runed halberd', aliases='halberd runed', long='A runed halberd lies on the ground here.',
               extras={'halberd runed': 'The runes glow with a bright light. Whoever owned this came up the mountain armed, and did not go down again.'})
O[3306] = dict(short='a potion of protection', aliases='potion protection dun vial', long='A vial of dun fluid is here.',
               extras={'potion protection dun vial': 'Thick and brownish-grey. It smells of earth.'})
O[3307] = dict(short="a dragon's crown", aliases='crown dragon', long="Aglandiir's crown sits here, wrapped in a shimmering ward.",
               extras={'crown dragon': 'The ward pushes you back. You wonder how you could ever lay hands on such a great, valuable mass of gold.'})
O[3308] = dict(short='an apple', aliases='apple', long='A scrawny red apple sits here.',
               extras={'apple': 'It is not wormy... yet.'})
O[3309] = dict(short='a loaf of rye bread', aliases='bread loaf rye', long='A loaf of dark rye bread lies here.',
               extras={'bread loaf rye': 'Dark, heavy hill bread.'})
O[3310] = dict(short='a marrow', aliases='melon marrow', long='A big marrow sits here, discarded.',
               extras={'melon marrow': 'A great green marrow, the only thing in the hills that grew well this year.'})
O[3311] = dict(short="Gabadiel's knife", aliases='knife gabadiel silvered', long='An exquisitely crafted silvered knife rests here.',
               extras={'knife gabadiel silvered': 'The craftsmanship takes your breath away. This knife was forged by the smith-mage Gabadiel, the first of his last three blades. It must be worth a fortune.'})
O[3312] = dict(short="Gabadiel's long sword", aliases='sword long gabadiel', long='A superb long sword sticks in the earth.',
               extras={'sword long gabadiel': 'The sword is light and perfectly balanced. Only the smith-mage Gabadiel could have made it: the second of his last three blades, and worth a fortune.'})
O[3313] = dict(short="Gabadiel's short sword", aliases='sword short gabadiel', long='A short sword lies here, a work of art.',
               extras={'sword short gabadiel': 'It brings tears to your eyes. This was Gabadiel\'s masterwork, his last blade, the one he would not sell to be thrown away on the wall. Beyond price.'})
O[3314] = dict(short='the burnt body of the smith', aliases='corpse body smith', long='The dismembered and burnt body of the smith lies on the floor here.',
               extras={'corpse body smith': 'Gabadiel, or what is left of him. He is still smouldering a little; his killers cannot be far off.'})
O[3315] = dict(short='a scimitar', aliases='scimitar sword curved', long='A curved scimitar as long as your arm lies here.',
               extras={'scimitar sword curved': 'A cheap curved blade of the kind the bandits buy by the dozen. It is not of high quality.'})
O[3316] = dict(short='a crate', aliases='crate', long='A crate is stacked here.',
               extras={'crate': 'A plain wooden crate stencilled with three crossed swords.'})
O[3317] = dict(short='a hunting bow', aliases='bow hunting', long='A hunting bow lies here, unwanted.',
               extras={'bow hunting': 'A bow for deer and rabbits, not for battle. Lately it has been used for bandits.'})
O[3318] = dict(short='a runed leather vest', aliases='vest leather runed', long='A fine leather vest lies here.',
               extras={'vest leather runed': 'The seams are sewn with a rune-worked thread, the kind Gabadiel used.'})
O[3319] = dict(short='a glass of beer', aliases='glass beer', long='A glass of beer sits forgotten here.',
               extras={'glass beer': 'Thin home-brewed beer, with not too much floating in it.'})
O[3320] = dict(short='a glass of mead', aliases='glass mead ale', long='A big glass of mead sits here.',
               extras={'glass mead ale': 'Hill mead, sweet and strong.'})
O[3321] = dict(short='a shot of whisky', aliases='shot whisky', long='A shot of whisky is sitting here.',
               extras={'shot whisky': 'Potent stuff, distilled in a barn somewhere.'})

RETHEME = {
    'zones': {33: 'The Three of Swords'},
    'rooms': R, 'mobs': M, 'objs': O,
}
