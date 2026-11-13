"""King Welmar's Castle (zone 150) re-themed: a frightened crown.

King Welmar is old.  His taxes and levies keep Midgaard's wall manned, and
the court that lives off what is left is decadent, frightened and full of
intrigue.  Behind the feasts a quiet cult of Nu'Groth is growing: grey moth
marks, whispered prayers, a comfortable cell for a mass murderer, and a ring
of black stones in the woods south of the road where something answers.

castle.c matches mobs by short description: King Welmar ("King Welmar"),
Brian, Mick, Michael, Tim, Tom.  Those shorts keep their names at the front,
and the King keeps the aliases 'king welmar' (the twins 'follow King Welmar').
Every spec-proc mob keeps its role.  Exits, doors and resets are unchanged.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

HALL_ROOF = ('The painted roof once showed the heroes of the crown riding west. Painters on '
             'scaffolds are slowly covering the western half in black, by order of someone at '
             'court; nobody will say whose order.')

# ====================================================================== the road
R[15000] = dict(name="The King's Road", desc="""
    The King's Road begins here, broad and dead straight, its fitted stones
    laid by masons whose skill nobody can match now.  The levy carts have worn
    two deep ruts down the middle of it.  A tired carter trudges past toward
    the west, his wagon full of tithe-grain, and does not look up.  The road
    runs east toward the castle and west to the lanes of Miden'Nir; a small
    overgrown trail slips away south through the undergrowth.""",
    extras={'traveller carter wagon': 'A thin carter with a tithe-collector\'s token on his hat. He nods when you greet him but keeps walking. "Grain for the wall," he mutters. "Always grain for the wall."'},
    exits={'e': "The King's Road runs straight east toward a pale castle.",
           's': 'A small trail, almost grown over, leads south through the undergrowth.',
           'w': "The King's Road narrows into a lane to the west."})
R[15001] = dict(name="The King's Road", desc="""
    The middle of the King's Road.  The road runs east and west as straight as
    a drawn line.  Every half mile a post has been set up by the verge, and on
    every post is nailed the same notice: a new levy, a new tax, in the King's
    name and sealed with his stag.""",
    extras={'notice post': 'By order of King Welmar: one son in four to the wall at Midgaard; one sheaf in three to the King\'s barns. Those who hide either will hang.'},
    exits={'w': "The King's Road runs west toward the lanes and, far beyond, Midgaard."})
R[15002] = dict(name="The King's Road", desc="""
    The road runs on east and west, perfectly level.  A gibbet stands on the
    verge here, empty now, its chain creaking.  Ahead in the east the towers
    of the castle rise pale above the trees, with banners on every one.""",
    extras={'gibbet chain': 'A tall gibbet of black wood. A board nailed to it reads "LEVY-DODGER". The cage is empty; the crows have finished with him.'},
    exits={'e': 'In the east rise the pale towers of a castle.'})
R[15003] = dict(name="On The King's Road Outside A Castle", desc="""
    The road ends before King Welmar's castle.  It was built for beauty, not
    for war: white stone, slim towers, carved windows.  Lately someone has
    tried to make up for that.  The windows have been narrowed to arrow slits
    with raw new masonry, and the moat has been dug deeper.  A drawbridge
    crosses the moat to the north; the road leads back west.""",
    exits={'n': 'The drawbridge crosses the moat to the castle gate.'})
R[15004] = dict(name='On The Drawbridge', desc="""
    You stand on the drawbridge before the castle gate, a huge double door
    carved with stags and vines.  Crossbowmen watch you from the slits above.
    The moat below is black and still, except for slow whirls that rise and
    fade on its surface.  The road lies south.""",
    extras={'whirls whirl moat': 'Something large turns slowly under the black water. The guards say it is only the old pike. They do not say it as if they believe it.',
            'gate stags carvings': 'The carvings show stags running through vines. Someone has scratched a tiny moth into the corner of one panel, and someone else has tried to scrape it off.'},
    exits={'n': 'The gate is a great double door of carved oak on huge hinges. It was made to be admired; now it is barred every night.',
           's': "The King's Road leads away south."})

# ====================================================================== ground floor
R[15005] = dict(name='The Kitchen', desc="""
    The castle kitchen roars with heat.  Spits turn, pots boil and a swarm of
    cooks run at the Chef's shouts.  Here, while Midgaard eats ration bread,
    the court still feasts: lobster, roe, sugared fruit, swans glazed in
    honey.  Shelves of copper pans line every wall.  Narrow passages lead
    north and east.""",
    extras={'shelves pans copper': 'Rows of polished copper pans, worth more than a village pays in tithe.'})
R[15006] = dict(name='A Small Passage', desc="""
    A narrow, dim passage for servants, so that the court need never see the
    food being carried.  The floor is greasy and the walls are stained with
    smoke.  The kitchen lies west, and a small door leads east.""",
    exits={'w': 'You hear pots clanging and smell roasting meat.'})
R[15007] = dict(name='The Entrance Hall', desc="""
    The entrance hall of the castle, tall and white, hung with portraits of
    Welmar's ancestors.  Every one of them has been turned a little to face the
    door, as if keeping watch.  Courtiers wait here in silk and whisper behind
    their hands.  The Great Hall opens north, a guard room lies east, the gate
    is south and a small door leads west.""",
    extras={'portraits portrait ancestors': 'Kings and queens of the stag. The oldest have calm faces. The newest, Welmar\'s own, was painted with his hand on his sword and his eyes on the west.'})
R[15008] = dict(name='The Guard Room', desc="""
    A small, stuffy room where guards off duty wait for their next watch.  A
    table is ringed with dice-cups and empty cups, and someone has chalked a
    tally of wagers on the wall.  The only way out is west, to the entrance
    hall.""",
    extras={'tally wall chalk': 'Names and sums. Beside one name someone has drawn a little grey moth instead of a number.'})
R[15009] = dict(name='Under The Tower', desc="""
    You are beneath the south-east tower, in a part of the castle that nobody
    uses.  Dust lies thick, but there are fresh footprints in it, going up the
    stairs and coming down again, always at night.  Stairs lead up into the
    tower and a passage runs north.""",
    extras={'stairs': 'Old stairs in good repair. The dust on the treads is scuffed by many feet.',
            'footprints prints dust': 'Soft shoes, not guards\' boots. Courtiers\' slippers, a great many of them.'},
    exits={'u': 'The old stairs lead up into the tower.'})
R[15010] = dict(name='The Small Passage', desc="""
    A cramped passage behind the walls, used by the servants to come and go
    unseen.  Spy-holes have been bored through the panelling here and there,
    by whom nobody knows.  It runs north and south; the kitchen noise comes
    from the south.""",
    extras={'spy holes spyholes panelling': 'Small holes, each at eye height, looking into the Great Hall. Some have been stopped with wax. Others have been opened again.'},
    exits={'s': 'You hear pots clanging and smell roasting meat.'})
R[15011] = dict(name='The Great Hall', desc="""
    The south-west corner of the Great Hall, a hall so vast that its roof seems
    as far away as the sky.  Long tables stand ready for tonight's feast, laid
    with silver for three hundred.  Musicians tune in a corner and a lady
    laughs too loudly at nothing.  The hall continues north and east.""",
    extras={'roof paintings paint': HALL_ROOF,
            'tables silver': 'Silver plates, silver cups. Every week a few pieces go missing, and every week they are quietly replaced.'})
R[15012] = dict(name='The Great Hall', desc="""
    The southern end of the Great Hall.  Courtiers drift across the polished
    floor in twos and threes, never more, and fall silent whenever a guard
    walks past.  North, at the far end of the hall, stands King Welmar's ivory
    throne.  The hall spreads east and west, and the entrance hall lies
    south.""",
    extras={'roof paintings paint': HALL_ROOF,
            'courtiers': 'Silk, perfume, rouge, and frightened eyes. They talk of feasts and marriages, and never of the west.'})
R[15013] = dict(name='The Great Hall', desc="""
    The south-east corner of the Great Hall.  A painted screen stands here,
    and behind it two lords are arguing in hushed voices over who will pay for
    the next levy and whose sons will be sent.  The hall continues north and
    west.""",
    extras={'roof paintings paint': HALL_ROOF,
            'screen': 'A screen painted with hunting scenes. It hides a great deal of whispering.'})
R[15014] = dict(name='A Passage', desc="""
    A bare passage of white stone, chilly and little used.  Southward it leads
    to the foot of the south-east tower; north it joins the small passage by
    the Great Hall.  Someone has hung a sprig of grey herbs above the
    southern arch.""",
    extras={'sprig herbs grey': 'Dried ashleaf, tied with grey thread. The servants say it is to keep moths away. There are no moths here.'})
R[15015] = dict(name='The Passage', desc="""
    A passage running north and south along the western side of the Great
    Hall.  Pages hurry along it with trays and messages.  An archway east opens
    into the Great Hall.""",
    exits={'e': 'The Great Hall, bright with candles.'})
R[15016] = dict(name='The Great Hall', desc="""
    The north-west end of the Great Hall.  A long table here is reserved for
    the King's council, its chairs carved with the stag; three of them are
    draped in black for councillors who died this year, all quite suddenly.
    East stands the throne; a passage lies west and the hall runs south.""",
    extras={'roof paintings paint': HALL_ROOF,
            'chairs black council table': 'Three chairs draped in black. A fever, a fall, a bad oyster, the court says. It says so very quickly.'})
R[15017] = dict(name='By The Throne In The Great Hall', desc="""
    You stand before King Welmar's throne, carved from a single block of
    ivory so large that the beast it came from does not bear thinking about.
    Two guardsmen never leave its side.  The steps below it are worn by
    petitioners, and the floor before it is scrubbed every morning, because
    every morning someone has drawn something on it in chalk.  The hall
    continues east, west and south.""",
    extras={'roof paintings paint': HALL_ROOF,
            'throne ivory': 'Carved with stags, griffins and old beasts. The King has had iron bands fixed to the back of it, and a sword-rack within reach of his hand.',
            'floor chalk': 'Scrubbed clean. Faintly, in the grain of the stone, the ghost of a circle can still be seen.'})
R[15018] = dict(name='The Great Hall', desc="""
    The north-east end of the Great Hall.  Tall windows here look east, away
    from the war, and the court likes to gather beneath them.  A small passage
    leads east; the throne is west and the hall runs south.""",
    extras={'roof paintings paint': HALL_ROOF,
            'windows': 'The eastern windows show green hills and quiet woods. Nobody ever stands at the western ones.'},
    exits={'e': 'A small passage.'})
R[15019] = dict(name='The Small Passage', desc="""
    A small passage leading north and south behind the Great Hall.  A guard is
    posted here day and night, though nobody can quite say what against.  The
    Great Hall lies west.""",
    exits={'w': 'The Great Hall lies west.'})
R[15020] = dict(name='The Passage', desc="""
    A passage that leads north to the foot of the great staircase and south
    toward the Great Hall.  A small, plain door opens east into the servants'
    wing.""",
    exits={'n': 'The passage leads to a great staircase.',
           'e': 'A small, plain door. Servants come and go through it without looking up.'})
R[15021] = dict(name="The Servants' Corridor", desc="""
    The servants' corridor is narrow, bare and cold, a world away from the
    silk and gilt of the court.  It runs east.  Doors lead north to the
    servants' quarters and west to the passage.""",
    exits={'n': 'A plain wooden door to the servants\' quarters.',
           'e': 'The corridor ends a little further east.',
           'w': 'A wooden door to the west.'})
R[15022] = dict(name="The End Of The Servants' Corridor", desc="""
    The corridor ends here.  A door to the north leads to the butler's rooms;
    the corridor runs back west.  The floor outside the butler's door is
    scrubbed whiter than anywhere else in the wing.""",
    exits={'n': "The door to the butler's rooms."})
R[15023] = dict(name='The Training Room', desc="""
    The training room of the Royal Guard, a long hall smelling of sweat and
    oil, with racks of weapons along every wall.  Most are blunted for
    practice, but a few are kept sharp, and lately the sharp ones are the ones
    in use.  The guard drills here twice a day now.  A heavy door leads north
    to the barracks; a passage lies east.""",
    extras={'racks weapons rack': 'Blunt practice blades, and beside them a few good swords, freshly honed.'},
    exits={'n': 'A large, heavy door to the barracks.'})
R[15024] = dict(name='The Small Passage', desc="""
    A small passage running north and south.  From the west come grunts,
    shouted counts and the clash of practice steel.  To the north the passage
    reaches a staircase going down.""",
    exits={'n': 'The passage leads north to some stairs.',
           'w': 'The training room, loud with drill.'})
R[15025] = dict(name='The Stair Room', desc="""
    The foot of the great marble staircase that climbs to the second floor.
    Its pillars are carved as trees, with squirrels and birds running up the
    trunks.  On one pillar a carver has added, very small, a moth with a grey
    stone set for its eye.  A passage leads south.""",
    extras={'stairs stair': 'Marble stairs, made for beauty, worn soft in the middle by generations of court shoes.',
            'pillar pillars tree trees': 'Squirrels, finches, owls. And low on one trunk a small moth, newer than the rest, its eye a chip of grey stone.',
            'moth': 'A carved moth, wings spread. Its grey eye is cold to the touch.'},
    exits={'u': 'The marble stairs lead up to the second floor.'})
R[15026] = dict(name="The Servants' Quarters", desc="""
    A long, low room packed with narrow beds for the castle servants.  Their
    few belongings are kept in a large chest.  Over several of the beds hangs a
    knot of grey thread, and the servants who sleep there do not talk to the
    others.  The only door is south.""",
    extras={'bed beds': 'Narrow, hard beds. Above some of them hangs a little knot of grey thread.',
            'thread knot': 'Grey thread tied in a knot shaped like a moth. The servants who wear it are said to sleep very well.'},
    exits={'s': 'A wooden door leads back to the corridor.'})
R[15027] = dict(name="The Butler's Quarters", desc="""
    The butler's rooms lie in the servants' wing and yet are almost as fine as
    a lord's: a broad bed, a carpet, a writing desk, a locked drawer.  The
    butler hears everything that happens in the castle, and some of what he
    hears is worth gold.  The only way out is the door to the south.""",
    extras={'bed': 'A wide, soft bed with a fine coverlet, far too fine for a servant.',
            'drawer desk': 'A locked drawer in a writing desk. The edges of letters stick out of it, sealed in many different colours of wax.'},
    exits={'s': 'The door leads back to the corridor.'})
R[15028] = dict(name="The Guards' Barracks", desc="""
    A long room of bunks where the off-duty guard sleep, drink and gamble.
    The talk here is of the levies, and of the men who were taken from the
    Royal Guard last spring and sent west to Midgaard.  None of them have
    written back.  The heavy door is south.""",
    extras={'bunk bunks': 'Hard bunks. Several are empty, the names scratched off the frames.'},
    exits={'s': 'A large, heavy door to the training room.'})
R[15029] = dict(name='The Stairs', desc="""
    Here the white marble gives way to rough granite, and a staircase drops
    into the dark beneath the castle.  The air coming up it is damp and smells
    of old straw.  This is where the beauty of the castle stops.  The passage
    lies south.""",
    extras={'stairs stair staircase': 'Granite stairs, plain and functional, leading down to the dungeons.'},
    exits={'d': 'The stairs lead down into darkness.'})

# ====================================================================== second floor
R[15030] = dict(name='At A Bend In The Corridor', desc="""
    The long upper corridor bends here from east to north.  A tall mirror hangs
    at the corner, and it has been covered with a black cloth.  The corridor
    runs north and east.""",
    extras={'mirror cloth': 'Under the cloth the mirror is cracked across, as if something struck it from the inside.'})
R[15031] = dict(name='The Corridor', desc="""
    A long corridor hung with tapestries of the crown's old victories.  They
    show armies marching west in bright colours, and they are fading badly.  The
    corridor runs east and west.""",
    extras={'tapestries tapestry': 'Knights of the stag riding west under a gold sun. The colours have faded to grey.'})
R[15032] = dict(name='The Corridor', desc="""
    The corridor runs east and west past more tapestries.  One has been taken
    down, and only its iron hooks and a paler square of wall remain.  A guard
    is posted here.""",
    extras={'tapestries tapestry hooks square': 'A pale square where a tapestry hung. The servants say it showed the first King Welmar crowned at Midgaard. Someone sold it.'})
R[15033] = dict(name='The Corridor', desc="""
    The corridor comes to a corner here.  It runs back west, and to the north it
    opens into the guest wing, where the scent of perfume and the sound of soft
    music drift out.""",
    exits={'n': 'The guest wing, warm and perfumed.'})
R[15034] = dict(name='In The South-East Tower', desc="""
    A cold, bare room inside the south-east tower.  Old crates are stacked
    against the walls, but a path has been cleared between them to the next
    stairs.  Stairs lead on up into the dark, and down to the ground floor.""",
    exits={'u': 'The room at the top of the tower is dim, lit only by a candle.',
           'd': 'The stairs go down to the foot of the tower.'})
R[15035] = dict(name='The Corridor', desc="""
    The corridor runs north and south here, lit by candles in silver holders.
    An exit east leads to a small antechamber where guards stand watch over
    the treasury door.""",
    exits={'e': 'A small antechamber.'})
R[15036] = dict(name='By The Treasure Room', desc="""
    A small antechamber before a great door of steel, solid and new, set into
    the old white wall.  A sign is posted beside it.  The treasury holds the
    tithes of half the realm before they go west; the guards here are the
    biggest men the castle has.  The corridor lies west.""",
    extras={'sign': 'TREASURY OF THE CROWN. Tithes of the realm, held for the wall. None shall enter save by the King\'s own word. Trespass is death.'},
    exits={'e': 'A large door of new steel.'})
R[15037] = dict(name='The Great Treasury', desc="""
    The treasury of the crown.  There is less gold than the stories say;
    most of it has gone west to pay the wall.  What remains is art: paintings,
    tapestries, carvings and statues, crowded together under dust sheets.  The
    ledgers say the crown owns more pieces than are here.  Nobody has dared
    to tell the King.  The steel door is west.""",
    extras={'painting paintings carving carvings sculptures tapestries': 'Treasures of the stag kings, sheeted against the dust. Gaps in the rows show where pieces have quietly gone.',
            'ledgers ledger': 'The ledgers list a silver stag, three tapestries and a dozen paintings that are no longer here. Each has been marked "lent" in a neat hand.'})
R[15038] = dict(name='The Guest Wing', desc="""
    The guest wing, where lords and envoys stay when they come to beg the King
    for fewer levies.  It is warm and perfumed and full of soft footsteps.  A
    large ornamented door leads east to the great suite, a smaller door north
    to a guest room, and the corridor lies south.""",
    exits={'n': 'A smaller door to a guest room.',
           'e': 'A large ornamented door to the guest suite.'})
R[15039] = dict(name='The Guest Suite', desc="""
    The living room of the great guest suite, gilt and velvet and far too
    warm.  Wine cups stand about half-finished.  Whoever stays here now never
    seems to leave it by day, but the servants say that at night the suite is
    full of visitors.  The bedroom is north and a door leads west.""",
    extras={'cups wine': 'Half-finished cups of dark wine. In the dregs of one, a drowned grey moth.'},
    exits={'w': 'Behind the door lies the guest wing.'})
R[15040] = dict(name='The Corridor', desc="""
    A stretch of the long corridor running north and south.  The candles here
    have burned down and not been replaced, and the tapestries are in deep
    shadow.""")
R[15041] = dict(name='The Ball Room', desc="""
    The south-west end of the great Ball Room, its floor polished like dark
    water.  The court still dances here every week, masked, while the levies
    march.  The stage for the musicians is east; the ball room runs north.""")
R[15042] = dict(name='By The Stage', desc="""
    The musicians' stage, wide enough for forty players.  It is empty now,
    and the boards beneath it creak hollowly.  Under the edge of the stage
    someone has drawn a grey circle in chalk and not quite rubbed it out.  The
    Ball Room continues west and north.""",
    extras={'circle chalk': 'A circle of grey chalk with seven marks around it, like seven standing stones.'})
R[15043] = dict(name='A Guest Room', desc="""
    A comfortable guest room for lesser visitors: a good bed, a wash-stand and a
    window.  A minor lord's travelling chest stands open and empty, and his
    boots are still by the bed.  Nobody has seen him for a week.  The door is
    south.""",
    extras={'chest boots': 'A lord\'s chest, open and empty, and a pair of good riding boots. He would not have left without them.'})
R[15044] = dict(name='The Bedroom', desc="""
    The bedroom of the great suite, filled by a huge four-poster bed hung with
    grey velvet.  The air is heavy with incense that does not quite hide another
    smell beneath it, like cold earth.  The living room is south.""",
    extras={'bed velvet': 'Grey velvet curtains, a bolstered bed. On the pillow lies a single grey thread.'})
R[15045] = dict(name='The Corridor', desc="""
    The long corridor runs north and south.  To the east a wide archway opens
    into the Ball Room, and the sound of a lone violin drifts out.""",
    exits={'e': 'The Ball Room.'})
R[15046] = dict(name='The Ball Room', desc="""
    The north-west end of the Ball Room.  Masks hang along the wall on silver
    pegs, ready for the next revel: stags, foxes, swans, and a new one, grey
    and plain, with no mouth.  The Ball Room continues east and south, and the
    corridor lies west.""",
    extras={'masks mask': 'Masks for the revels. The grey mouthless one is the most popular this season. Nobody admits to wearing it.'})
R[15047] = dict(name='The Ball Room', desc="""
    The north-east end of the Ball Room.  Great windows look out over the
    gardens, and a guard stands here to stop the dancers slipping away into
    them.  East, a door opens into a tower; the stage lies south and the Ball
    Room west.""",
    exits={'e': 'To the east, the foot of a tower.'})
R[15048] = dict(name='In The Tower', desc="""
    The base of the north-east tower, the tallest of the three watch-towers.
    Granite stairs wind up from here a long way toward the lookout.  The Ball
    Room is west.""",
    extras={'stairs': 'Solid granite stairs, worn by the boots of watchmen.'},
    exits={'u': 'The stairs climb a long way to the top of the tower.'})
R[15049] = dict(name='The Grand Staircase', desc="""
    The grand staircase climbs on above the second floor toward a tower top,
    and sweeps down to the floor below.  East is a large oak door, iron-bound
    and newly fitted with three locks: the King's own rooms.  A corridor runs
    south.""",
    extras={'stairs': 'Marble stairs and tree-carved pillars, with small animals running up the trunks.',
            'door oak locks': 'A heavy oak door with three new locks. The King keeps every key himself.'},
    exits={'e': 'A large oak door with three new locks.',
           'u': 'The stairs continue up to the top of a tower.',
           'd': 'The stairs lead down to the ground floor.'})
R[15050] = dict(name='The Cosy Room', desc="""
    The King's private sitting room.  A fire burns day and night in the
    fireplace, and a few deep chairs stand around a small table.  Here Welmar
    sits up through the small hours with every candle lit, reading the lists
    from Midgaard.  A door leads west, and the bedroom opens east.""",
    extras={'fire fireplace': 'A big log fire. It is never let go out. The King does not like the dark.',
            'table': 'A small mahogany table piled with dispatches from the Lord Commander of Midgaard: casualties, requests for men, requests for grain.',
            'chairs': 'Deep chairs drawn close to the fire.',
            'dispatches lists': 'Names of the dead of the wall, and at the foot of each list the same line: "We need more men."'},
    exits={'e': 'The King\'s bedroom lies east.',
           'w': 'The large oak door leads back to the staircase.'})
R[15051] = dict(name="King Welmar's Bedroom", desc="""
    The King's bedchamber, with a wide view east over the quiet hills.  The
    western window has been bricked up.  A great four-poster bed stands to one
    side, and the walls are lined with shelves of books, many of them on war,
    on the west, and on old wards against the dark.  The only way out is
    west.""",
    extras={'books book shelf shelves bookshelf bookshelves': 'Worn books, thoroughly read: "The Holding of the Wall", "Of the March and What Walks There", and "Wards and Watches", its pages heavily marked in the King\'s hand.',
            'bed': 'A royal bed with a sword hung on the post within reach of the pillow.',
            'history wall holding': '"The Holding of the Wall," a dry history of every Lord Commander of Midgaard. Welmar has underlined each one who died at his post.',
            'wards watches': '"Wards and Watches," an old book of protective signs. Someone else has written in the margins too, in grey ink, crossing out every ward.',
            'window bricked': 'The western window is bricked up with new red brick. The mortar is still pale.'})
R[15052] = dict(name='Up In The Tower', desc="""
    At the top of the south-east tower is a small, dim room lit by one
    flickering candle on a cluttered table.  Charts of the night sky cover the
    walls, and a great telescope points out through a slit in the roof.  The
    King's star-reader works here, and courtiers climb up at night to ask him
    what the stars say about the west.  The only way out is down.""",
    extras={'table': 'Star charts, compasses, a skull, and a list of courtiers\' names with the hour of their birth beside each.',
            'candle': 'A tallow candle, burning low. It is the only light he allows.',
            'charts chart walls': 'Charts of the stars. In the western sky a cluster has been inked over in grey and labelled with a single word too faint to read.'},
    exits={'d': 'The stairs go back down the tower.'})
R[15053] = dict(name='The Top Of The Tower', desc="""
    The top of a watch-tower, built for defence and nothing else.  The windows
    are slits for bowmen, narrow outside and broad within.  Fresh arrows have
    been stacked beneath them, and a brazier stands ready.  The only way is
    down the stairs.""",
    extras={'window slit windows': 'Through the slits you see the green countryside, and the King\'s Road running west toward Midgaard.',
            'arrows brazier': 'Sheaves of new arrows and a brazier of pitch. The castle expects to be attacked one day, and not from the east.'},
    exits={'d': 'The stairs go down to the second floor.'})
R[15054] = dict(name='The Top Of The Tower', desc="""
    The top of the highest tower, the castle's lookout.  The view is vast.
    North and east rise the white mountains; south roll quiet hills.  West, the
    King's Road runs dead straight to Midgaard, and beyond the fort, on the far
    horizon, lies a grey haze that never lifts.  The only way is down.""",
    exits={'n': 'To the north the White Mountains lift their peaks into the clouds. The dwarves hold halls under them still, and their forge-smoke rises from the high valleys.',
           'e': 'East lies an arm of the White Mountains, quiet and far from the war.',
           's': 'South, rolling hills stretch away, dotted with farms that have too few men left to work them.',
           'w': 'West, past the woods and lanes, Midgaard stands on its river, a grey wall with smoke above it. Beyond it the land goes on into a haze, grey, flat and unmoving, where nothing can be seen at all.',
           'd': 'The stairs go back down to the second floor.'})

# ====================================================================== dungeons
R[15055] = dict(name='The Bottom Of The Stairs', desc="""
    The stairs end in a damp stone room beneath the castle.  Water drips
    somewhere in the dark.  A single torch in a bracket lights the way east,
    into a small guard room; the stairs climb back up.""",
    exits={'e': 'A small guard room opens to the east.',
           'u': 'The stairs lead up out of the damp.'})
R[15056] = dict(name='The Guard Room', desc="""
    A cheerless guard room under the castle.  A table, a chair and a deck of
    cards are all its furniture.  Somebody must sit down here all day, and the
    only reason anyone would is the prisoner behind the south door.  A
    stairwell in the west wall leads back up.""",
    extras={'table cards deck': 'A deck of cards, stacked on the table. One card lies on the floor.',
            'card floor': 'The Ace of Spades, face up. Nobody has picked it up. The guards will not touch it.'},
    exits={'s': 'Through the peep hole in the small wooden door you see a corridor lined with cells.',
           'w': 'A small stairwell in the western wall leads upwards.'})
R[15057] = dict(name='The Prison', desc="""
    A short corridor of cells, about thirty feet long.  Torches burn in locked
    iron cages along the walls, with a flame that never flickers and gives no
    smoke; some court mage set them burning years ago.  Cells open east and
    west near the north end, and a third, double-padlocked, stands alone at the
    south end with a small plaque in the keystone of its arch.  A wooden door
    leads north.""",
    extras={'plaque keystone': 'The plaque in the keystone is engraved with four simple words: Ergan, Murderer of Townsbridge.',
            'torches torch cages': 'The flames stand perfectly still, like painted fire.'},
    exits={'s': 'The cell door to the south is double padlocked, with a plaque in the keystone above it.'})
R[15058] = dict(name='A Cell', desc="""
    A wrecked cell.  Something has broken through the western wall from the
    other side, leaving a small ragged hole, and the stones around it are
    scratched by many small claws.  The cell door is in the eastern wall.""",
    extras={'hole': 'The hole is far too small to climb through. Something in the dark beyond it rustles.'})
R[15059] = dict(name="Ergan's Cell", desc="""
    This large cell is almost a lodging: a cot with good blankets, a table cut
    from the wall, a rug, a jug of wine.  Ergan butchered a whole village, and
    yet someone at court pays to keep him warm.  On the wall above the cot he
    has scratched a ring of seven marks.  The door is north.""",
    extras={'marks ring wall': 'Seven scratches in a ring, around a smooth black smear. The same shape as the stones in the woods south of the road.',
            'rug cot blankets wine jug': 'Good wool, good wine. Gifts, sent down by somebody who does not sign their name.'})
R[15060] = dict(name='A Cell', desc="""
    A small, damp, dark cell that has stood empty a long time.  Something is
    written on the wall in a careful hand, over and over.  The door is in the
    west wall.""",
    extras={'wall writing': '"It will be kind. It will be kind. It will be kind." The rest is scratched out.'})

# ====================================================================== Townsbridge
R[15061] = dict(name='An Overgrown Trail', desc="""
    A faint trail leaves the King's Road and burrows into the woods, almost lost
    under brambles and fern.  Nobody has cut it back in years.  Behind you the
    creak of levy carts on the road is already muffled.  The trail leads north
    and south.""",
    exits={'n': "The creak of carts on the King's Road comes from the north."})
R[15062] = dict(name='An Overgrown Trail', desc="""
    The trail winds deeper into the woods.  Birds sing here, but fewer than
    there should be, and none at all in the trees ahead.  Fern closes over the
    path.  The trail runs north and east.""")
R[15063] = dict(name='An Overgrown Trail', desc="""
    The trail bends here.  To the south the woods thin, and an unnatural
    silence hangs over that way, as if every sound were being swallowed.  The
    trail leads west and south.""",
    exits={'s': 'The undergrowth opens up to the south onto a small, silent village.',
           'w': 'The overgrown trail winds back west.'})
R[15064] = dict(name='A Dirt Road', desc="""
    The trail comes out of the woods onto the dirt road of a small village.
    There is no sound but the wind: no dogs, no hammering, no voices.  Nothing
    moves.  A sign lies fallen by the roadside.  A house stands to the west;
    the road runs south into the village, and the trail goes back north.""",
    extras={'sign': 'A painted board: "Welcome to the hamlet of Townsbridge. Population: 276." The number has been scratched out and replaced with a 0.'},
    exits={'n': 'A trail leads into the heavy undergrowth to the north.',
           'w': 'A house stands just west of the road, its door hanging open.'})
R[15065] = dict(name='A Small Intersection', desc="""
    A small path splits off the dirt road here and runs west into the dark
    trees.  The woods lean close around the village, as if they were keeping
    something in.  A wailing sound comes from the house on the east side of the
    road.  The road runs north and south.""",
    exits={'e': 'A thin, endless wail comes from the house to the east.',
           'w': 'A small, dark trail leads into the woods to the west.'})
R[15066] = dict(name='A Dirt Road', desc="""
    This stretch of road reeks of rot.  West, a small thatched cottage stands
    untouched, as if nothing had happened.  East is the blackened shell of a
    shop, its sign hanging from a charred chain.  The road runs north, and
    south toward the source of the stench.""",
    extras={'sign': 'Charred and sooty, the sign still shows a few letters: T TO SB DGE  NER L  RE.'},
    exits={'e': 'The burned shell of a shop stands east.',
           'w': 'A quiet cottage stands west of the road, strangely untouched.'})
R[15067] = dict(name='A Large Pit', desc="""
    The road ends at the lip of a great pit, and here is the stench.  The pit is
    a mass grave, full of the bones of Townsbridge.  But many of the bodies are
    fresh, far too fresh: someone still brings the dead here, a decade after
    the village died.  The road leads back north.""",
    extras={'bodies corpses bones pit': 'Old bones below; newer bodies above, in rags of every kind, refugees, carters, a man in a courtier\'s silk. Every one has been laid face down, toward the west.'})
R[15068] = dict(name='A House', desc="""
    The house has been torn apart: the furniture is smashed and flung about as
    if a storm had burst inside it.  And yet there is no dust and no cobweb
    anywhere.  It looks as though it happened this morning, and every
    morning.  The road is east, through the doorway.""")
R[15069] = dict(name='A House', desc="""
    A dark house full of cobwebs and deep dust that rises at every step.  The
    furniture is old and of a fashion not seen for a lifetime.  A thin howl
    comes and goes from nowhere you can find.  Weak light falls through the
    doorway to the west.""")
R[15070] = dict(name='A Small Cottage', desc="""
    The cottage is just as its owners left it: table laid, bread on the board,
    the fire laid but not lit.  Nothing is dusty.  The bread is fresh.  There is
    a body on the floor.  It would be wise to leave.  The road is east through
    the open door.""")
R[15071] = dict(name='The Burned Shop', desc="""
    The village shop, burned out.  The fire must have smouldered unwatched for
    days.  The roof is gone and two walls are burned down to half their height.
    Scorched goods lie in the ash, and the stump of a counter stands by the
    north wall.  The road is west, through the gap in the wall.""",
    extras={'counter goods ash': 'Melted candles, cracked jars, a scorched ledger with the last page torn out.'})
R[15072] = dict(name='A Dark Path', desc="""
    Under the trees the light dies quickly, too quickly, as if the dark here
    were made rather than grown.  Not a leaf stirs.  Something in you wants
    very much to turn back.  The path goes on west, and daylight lies east.""",
    exits={'e': 'The path leads back to a small crossroads in the village.'})
R[15073] = dict(name='A Dark Path', desc="""
    The trees crowd in over the narrow path, so close that their branches brush
    your face.  The silence is complete.  Ahead in the west there is a green
    glow that lights nothing.  The path runs east and west.""",
    exits={'w': 'A green glow comes from the west, strong but somehow giving no light.'})
R[15074] = dict(name='The Circle Of Stones', desc="""
    Seven standing stones of black glassy rock stand in a ring here, each twice
    the height of a man, each giving off a faint green glow.  In the centre of
    the ring lies a round black pool, flat as a mirror, its surface rippling
    though there is no wind.  The trees close overhead and blot out the sky.

    Fresh flowers, grey ribbons and a courtier's silk glove lie at the foot of
    the stones.  Someone from the castle comes here.  A narrow path leads
    east.""",
    extras={'stones glow stone ring circle': 'Each stone is fifteen feet tall or more. The dark rock glows a dull green, enough to see by. Seven moths are cut into each one.',
            'pool mirror disk': 'A black disc of water, perfectly round. Your reflection in it is a moment late.',
            'flowers ribbons glove': 'Offerings. The glove is fine kidskin, embroidered with a little grey moth, the kind of thing a lady of the court would wear.'},
    exits={'e': 'A narrow path leads away into the darkness.',
           'u': 'The trees knot together over the ring, shutting out the sky.'})

# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d


M[15000] = mob('Gwydion', 'gwydion guard royal jailer', 'Gwydion the Royal Guard is here, keeping watch on the cells.',
               'A grey-bearded guard in chain mail who has kept the dungeon for ten years. He is the only man who talks to Ergan, and he does not like what Ergan says.')
M[15001] = mob('King Welmar', 'king welmar', 'King Welmar is here, old and grey, his eyes always on the doors.',
               'Welmar is old now, his beard white, his big frame gone gaunt. He was once a wise and well-loved king. Now he barely sleeps, eats only what his taster has eaten, and sends every son and sheaf his realm can spare to the wall, because he knows what will come east if Midgaard falls. He trusts no one at his court, and he is right not to.')
M[15002] = mob('the horrible ghost', 'ghost horrible villager wailing', 'A horrible ghost drifts toward you, wailing without end.',
               'The ghost of a woman of Townsbridge, torn and translucent, her mouth open in a scream that has not stopped for ten years.')
M[15003] = mob('Jim', 'jim guard royal', 'Jim the Royal Guard stands here on duty, hand on his sword.',
               'A young guard in the chain mail of the Royal Guard. He came to the castle to escape the levy, and has started to wonder whether he chose well.')
M[15004] = mob('Brian', 'brian guard royal', 'Brian the Royal Guard is here, sparring with the Master.',
               'A broad, sweating guard in chain mail, working through the drills again and again. They train for real now.')
M[15005] = mob('Mick', 'mick guard royal', 'Mick the Royal Guard is here, sparring with the Master.',
               'A wiry guard in chain mail, quick on his feet. His brother was taken by the levy and sent to Midgaard.')
M[15006] = mob('Matt', 'matt guard royal', 'Matt the Royal Guard stands here on duty.',
               'A steady guard in chain mail, his eyes moving over every courtier who passes.')
M[15007] = mob('Jochem', 'jochem guard royal', 'Jochem the Royal Guard sits here, off duty, sharpening a knife.',
               'A scarred veteran in chain mail who has fought in the west and come back. He does not talk about it. He longs, oddly, to go back.')
M[15008] = mob('Anne', 'anne guard royal', 'Anne the Royal Guard is here on duty.',
               'A tall guardswoman in chain mail, well trained and watchful. She keeps a list of which courtiers go out at night.', sex=2)
M[15009] = mob('Andrew', 'andrew guard royal', 'Andrew the Royal Guard is here on duty.',
               'A seasoned guard in chain mail, who moves like a man who has seen real battle and has not slept well since.')
M[15010] = mob('Bertram', 'bertram bert guard royal', 'Bertram the Royal Guard stands here on duty.',
               'A big, scarred guard in chain mail. There is a small grey moth tattooed on the inside of his wrist, and he keeps his sleeve pulled over it.')
M[15011] = mob('Jeanette', 'jeanette guard royal', 'Jeanette the Royal Guard stands here on duty.',
               'A hard-faced guardswoman in chain mail, carrying her scars with pride. She could be very dangerous if she wished.', sex=2)
M[15012] = mob('Peter, the Captain of the Royal Guard', 'peter captain guard royal', 'Peter, the Captain of the Royal Guard, walks the castle, inspecting his men.',
               'The Captain of the Royal Guard is huge and moves with a cat\'s grace. He is utterly loyal to the King, and he knows there is rot in the castle. He inspects his guards twice a day now, and he is not looking at their boots.')
M[15013] = mob('the Training Master', 'master trainingmaster training', 'The Training Master is here, supervising the drill.',
               'An old swordsman who has mastered nearly every weapon there is. He used to train guards for show. Now he trains them to kill.')
M[15014] = mob('the Royal Herald', 'herald royal', 'The Royal Herald stands here with a sheaf of proclamations.',
               'A young, broad-chested man with a great voice, whose work these days is reading out new levies and new taxes. He is hated in every village he visits.')
M[15015] = mob('Ergan the Murderer', 'ergan murderer', 'Slumped in a corner is Ergan, the Murderer of Townsbridge, smiling.',
               'Ten years ago Ergan killed every soul in Townsbridge, two hundred and seventy-six of them, in one night, and laid them face down toward the west. He says he was asked to. He says it was a gift. He was a great warrior once, and he is still dangerous, and someone at court keeps him fed and warm.')
M[15016] = mob('James the Butler', 'butler james', 'James the Butler stands here, looking pompous.',
               'The perfect butler: stout, balding, impeccable. He knows every secret in the castle and sells the best of them.')
M[15017] = mob('the Cleaning Woman', 'woman cleaning', 'A Cleaning Woman is here, scrubbing and trying not to be noticed.',
               'A thin, nervous woman with raw red hands. She scrubs chalk circles off the floors every morning and has learned never to ask who draws them.', sex=2)
M[15018] = mob('the cockroach', 'cockroach roach', 'A huge cockroach scuttles along the wall.',
               'A cockroach as long as your forearm, which crawled in through the hole in the cell wall. They say these are very hard to kill. They have been eating something down there.')
M[15019] = mob('the Astrologer', 'astrologer star reader', 'The Astrologer sits here, poring over a chart of the stars.',
               'An old white-bearded star-reader who sells his scrolls and potions to frightened courtiers along with their fortunes. Lately the stars tell him only one thing, and he will not say what.')
M[15020] = mob("Tim, the King's Lifeguard", 'tim guard lifeguard', "Tim, the King's Lifeguard, stands here, watching every hand.",
               'Tim looks exactly like his twin, Tom. The twins taste the King\'s food, sleep across his door, and would die for him without a thought. They are the only two men in the castle the King still trusts.')
M[15021] = mob("Tom, the King's Lifeguard", 'tom guard lifeguard', "Tom, the King's Lifeguard, stands here, watching every hand.",
               'Tom looks exactly like his twin, Tim. The twins taste the King\'s food, sleep across his door, and would die for him without a thought. They are the only two men in the castle the King still trusts.')
M[15022] = mob('the Chef', 'chef cook', 'The Chef is here, bellowing orders at the cooks.',
               'A great fat foreign chef who has tasted too much of his own cooking. He feeds the court on lobster and roe while the realm eats bran, and he has never once asked why.')
M[15023] = mob('the cook', 'cook', 'A cook is here, busy with a pot.',
               'A junior cook, eager and sweaty, terrified of the Chef.')
M[15024] = mob('David', 'david man guard', 'David, a huge, mean-looking man, stands here guarding the treasury door.',
               'He is very big and very loyal to the King\'s silver. He would not take kindly to anyone trying to get past.')
M[15025] = mob('Dick', 'dick man guard', 'Dick, a huge, mean-looking man, stands here guarding the treasury door.',
               'David\'s brother, just as big. He sleeps against the treasury door at night.')
M[15026] = mob('Jerry', 'jerry guard royal', 'Jerry the Royal Guard is here off duty, throwing dice.',
               'A guard in chain mail who gambles away his pay every week. Lately he has been winning, and paying his debts in coins with a moth on them.')
M[15027] = mob('Michael', 'michael guard royal', 'Michael the Royal Guard is here off duty, throwing dice.',
               'A guard in chain mail, dicing to forget the levy lists. He has lost three cousins to the wall.')
M[15028] = mob('Hans', 'hans guard royal', 'Hans the Royal Guard stands here on duty.',
               'A guard in chain mail who has seen more than one battle, and keeps the dancers out of the gardens at night.')
M[15029] = mob('Boris', 'boris guard royal', 'Boris the Royal Guard stands here on duty.',
               'A big, scarred guard in chain mail, posted at the foot of the old tower to see who goes up at night. He has stopped writing down the names.')
M[15030] = mob('the zombie', 'zombie villager', 'A zombie shambles silently among the corpses here.',
               'A dead villager of Townsbridge, grey and bloated, still in the rags of a farmer\'s smock. It does not rest because something will not let it.')
M[15031] = mob('the skeleton', 'skeleton villager', 'A skeleton clatters about here, climbing over the corpses.',
               'The bones of a Townsbridge villager, held together by nothing at all, turning its skull always toward the west.')
M[15032] = mob('the fiend of the black pool', 'fiend demon pit pool', 'A great burning shape rises out of the black pool.',
               'It is what answers when the cult calls into the pool: a towering thing of ash and flame with blood-red eyes and long talons. It came a long way from the west to be here, and it is glad to see you.', align=-1000)

# ====================================================================== objs
O[15000] = dict(aliases='nothingness universal blade sword', short='a blade of grey nothing',
                long='There seems to be a blade of grey nothing here, though it is hard to be sure.',
                extras={'nothingness universal blade sword': 'It is less a sword than a sword-shaped absence, grey and cold, that hurts the eye. Something is written along it.',
                        'text writing inscription': 'It just says: "NOTHING". Not very enlightening.'})
O[15001] = dict(aliases='gold coins crowns', short='the crown\'s gold', long='A heap of the crown\'s gold is here.')
O[15002] = dict(aliases='sceptre royal golden', short='a golden sceptre', long='A golden royal sceptre, topped with a stag, lies here.')
O[15003] = dict(aliases='crown golden', short='a golden crown', long='A heavy jewelled golden crown has been left here.')
O[15004] = dict(aliases='apple golden', short='a golden apple', long='A golden apple, the King\'s token of plenty, lies here.')
O[15005] = dict(aliases='telescope scope', short='a large telescope', long='A large brass telescope stands here, pointing at the western sky.',
                extras={'telescope scope': 'A fine brass telescope. Its lens is trained on one patch of the western sky, and there is a scratch on the brass beside it: a small moth.'})
O[15006] = dict(aliases='sword training', short='a training sword', long='A blunt training sword leans against the wall.')
O[15007] = dict(aliases='key huge treasury', short='a huge key', long='A huge, heavy iron key lies here.')
O[15008] = dict(aliases='wormbane sword verminator', short='Wormbane', long='A black sword wreathed in a faint green glow lies here.',
                extras={'wormbane sword verminator': 'A sword of black metal with a sickly green glow around the blade. It was made somewhere far in the west. It is very good at killing.'})
O[15009] = dict(aliases='key butlers butler', short="the Butler's key", long="The Butler's key is here.")
O[15010] = dict(aliases='key small', short='a small key', long='A small key lies here.')
O[15011] = dict(aliases='chest wooden', short='a large wooden chest', long='A large wooden chest stands in a corner.',
                extras={'chest': 'The servants\' common chest, with a small lock any thief could pick.'})
O[15012] = dict(aliases='vial large potion brown', short='a large vial', long='A large vial of brown liquid has been left here.',
                extras={'vial large brown potion': 'It is filled with a thick brown liquid that smells of bitter herbs. The Astrologer swears it wards off the dark.'})
O[15013] = dict(aliases='banner royal standard', short='a royal banner', long='The royal banner of the stag is planted firmly here.',
                extras={'banner royal standard': 'A great heavy banner on an iron pole. King Welmar\'s flag hangs from it, faded and wind-torn.',
                        'flag': 'The flag of King Welmar\'s house: a white stag on green. The stag\'s eye has been stitched over, recently, in grey thread.'})
O[15014] = dict(aliases='key', short='a key', long='A key lies on the floor.',
                extras={'key': 'A fine key with a letter W carved on it: the King\'s own key.'})
O[15015] = dict(aliases='hauberk mail chain', short="a guard's chain mail hauberk", long="A Royal Guard's chain mail hauberk lies on the floor.")
O[15016] = dict(aliases='broadsword sword large', short='a large broadsword', long='A large broadsword lies here.')
O[15017] = dict(aliases='key cell', short='the cell key', long='An iron key lies on the floor.',
                extras={'key cell': 'The key to the cells under the castle.'})
O[15018] = dict(aliases='corpse body', short='a corpse', long='A corpse lies face down in the middle of the floor, toward the west.')
O[15019] = dict(aliases='lobster', short='a glazed lobster', long='A glazed lobster lies here, absurdly rich.')
O[15020] = dict(aliases='caviar roe', short='some sturgeon roe', long='A little silver dish of black sturgeon roe sits here.')
O[15021] = dict(aliases='glow', short='the glow from the west', long='A strange green glow comes from the west.',
                extras={'glow': 'The glow from the west is strong, but it lights nothing around you, and you cannot see where it comes from.'})
O[15022] = dict(aliases='wail sound', short='the wailing from the east', long='An eerie wailing comes from the house to the east.')

RETHEME = {
    'zones': {150: "King Welmar's Castle"},
    'rooms': R, 'mobs': M, 'objs': O,
}
