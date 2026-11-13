"""The Dwarven Kingdom (zone 65) re-themed as the hold of Orrund.

The dwarves of Orrund lost their great mine (the lost delvings, zone 40) to
the things that tunnelled in from the west.  What is left of them holds the
halls of this mountain and works its forges day and night: the hold is the
front's forge, and every hammer, plate and axe on the wall comes out of here.
They are bitter -- about the old mine, about their dead left in it, and about
the men of Midgaard who take the steel and never came to help.

Castle Strangelove becomes the Widow's Spire, the round tower of Queen Hrodna,
whose husband King Bromm died in the old mine.  The mazekeeper of the deep
galleries blames her for giving the mine up, has listened too long to what
whispers below, and has stolen the key to her treasury.  Levels unchanged.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

# ---------------------------------------------------------------- the road up
R[6500] = dict(name='The Path To Orrund', desc="""
    A stony path leaves the laneway above and drops into a cleft of grey rock,
    rutted deep by the wheels of iron-wagons.  Every cart that passes here goes
    down toward the front loaded with dwarven steel and comes back empty.  A
    cairn of black stones stands by the way, one stone for every dwarf who went
    into the old mine and did not come out.  The path runs north toward the
    mountain; the laneway lies back up the slope.""",
    extras={'cairn stones stone': 'A tall heap of black stones, each scratched with a dwarvish name. The heap is taller than a man, and new stones are still added.'},
    exits={'n': 'The wagon-path runs north toward the foot of the mountain.',
           'u': 'The slope climbs back up to the laneway and the roads of the living.'})
R[6501] = dict(name='The Foot Of The Mountain', desc="""
    The path reaches the foot of a rugged mountain, where the scrub forest grows
    thick and dark against the rock.  The trees have been cut back from the road
    for a spear's length on either side, so that nothing can wait in them.
    Porters pass here bent double under bundles of blades.  The path climbs
    north and drops away south.""",
    exits={'n': 'The path climbs north up the face of the mountain.',
           's': 'The path runs south, back toward the roads to Midgaard.'})
R[6502] = dict(name='Halfway Up The Mountain', desc="""
    Halfway up the mountain the path turns along a shelf of bare rock.  From
    here the forest lies below like a dark cloth, and far to the south the smoke
    of the lowland roads can be seen.  Iron rings are hammered into the cliff for
    the porters to rest their loads against.  The summit is close to the north;
    the path drops south.""",
    exits={'n': 'The summit of the mountain is close above you.',
           's': 'The path drops toward the foot of the mountain.'})
R[6503] = dict(name='The Summit Gate', desc="""
    The path ends on a windswept shoulder near the top of the mountain, where
    two great doorways are cut into the living rock.  The one to the west is
    the gate of the hold of Orrund, carved with hammers and anvils; the one to
    the east leads to the working mine, and its lintel is black with soot.  The
    wind never stops here, and it carries the ring of the forges up out of the
    stone.  The path leads down to the south.""",
    exits={'e': 'A soot-blackened opening leads east into the mountain and down toward the mine.',
           's': 'The path leads down the mountainside toward the lowland roads.',
           'w': 'The carved gate of the hold of Orrund stands to the west.'})
R[6505] = dict(name='The Gate Of Orrund', desc="""
    A broad porch of dressed stone lies before the gate of Orrund.  The door is
    iron-bound oak a foot thick, and above it the dwarves have carved a long
    line of runes and then, more recently, chiselled half of them away.  Through
    the door comes the din of hammers.  The summit path is east, and the gate
    opens west into the hold.""",
    extras={'runes rune lintel': 'The old runes once named the hold as one of two, this mountain and the deep mine beyond the hills. The name of the mine has been chiselled out, roughly, as if in anger.'})

# ------------------------------------------------- the narrow way to the Spire
R[6504] = dict(name='The Narrow Way', desc="""
    A narrow passage cut through the rock leads off from the soot-path.  Few use
    it except the Queen's household, and its walls are cold and sweating.  The
    lamps that once lit it are mostly dead.  The way opens out to the south and
    runs on into the dark to the north.""")
R[6506] = dict(name='A Bend In The Narrow Way', desc="""
    The narrow way bends here beneath a row of stone pillars carved to look like
    trees, their branches spreading across the ceiling in a stone canopy.  It was
    meant to remind the dwarves of the forests above.  In the half-dark the
    carved branches look like grasping fingers.  The way runs south and east.""",
    extras={'tree trees pillar pillars branches': 'Pillars carved as trees, their stone branches knotted together overhead. Someone has hung small iron charms from the lowest branches, the kind miners hang to keep the dark away.'})
R[6507] = dict(name='The Narrow Way', desc="""
    The passage pinches so tight here that a dwarf in plate must turn sideways.
    Old scrapes of armour mark the walls at shoulder height.  The way continues
    north and west.""")
R[6508] = dict(name='The Narrow Way, Under The Crag', desc="""
    The passage runs straight north and south beneath a crag of raw stone that
    was never smoothed.  Great handprints, far too large for a dwarf, are pressed
    into the dust; something big walks this way.  To the north the passage ends
    at a door, and to the south it runs back toward the soot-path.""")
R[6509] = dict(name="The Queen's Door", desc="""
    A heavy door bars the passage to the north, plated in gold leaf that has worn
    thin over the years.  Beyond lie the Queen's road and her Spire.  The narrow
    way runs back south, and an opening in the west wall leads into a guard
    house.""")
R[6510] = dict(name="The Queen's Road", desc="""
    Inside the door a smoother road begins, paved with polished slabs and lit by
    lamps in iron cages.  The Queen's road runs north toward the Spire.  The
    golden door in the south wall leads back to the narrow way.""")
R[6511] = dict(name="The Queen's Road", desc="""
    The Queen's road runs north and south through a long hall hung with banners.
    Every banner is black now; the dwarves took down the colours when the King
    died in the old mine and never put them back.""",
    extras={'banner banners': 'Mourning banners of plain black wool. Under one of them the old royal colours still show, green and gold, faded nearly to grey.'})
R[6512] = dict(name='Before The Widow\'s Spire', desc="""
    The road ends at the foot of a great round tower that rises out of the
    cavern floor and vanishes into the dark of the roof: the Widow's Spire, home
    of Queen Hrodna.  A door in its side opens to the east.  An inscription is
    cut beside the door.  The road runs back south.""",
    extras={'sign inscription': 'Cut beside the door: "THE SPIRE OF HRODNA, QUEEN OF ORRUND. HERE THE CROWN KEEPS FAITH WITH THE DEAD." Below it, smaller and scratched by another hand: "And not one step toward them."'})
R[6522] = dict(name='The Guard House', desc="""
    A cramped guard house beside the Queen's door, with a brazier, a bench and a
    rack for axes.  The walls are covered in muster rolls and a great chart of
    the old mine, nailed up and stabbed through with knives.  The only way out
    is east.""",
    extras={'poster chart map': 'A chart of the lost delvings, drawn from memory: galleries, halls, shafts going down and down. Names are written in every hall, the names of the dwarves who died there. Someone has driven a knife through the deepest level.',
            'rolls muster': 'Lists of dwarves sent to the wall at Midgaard to teach the garrison to use dwarven steel. Fewer come back than go.'})

# ------------------------------------------------------------------- the hold
R[6513] = dict(name='Inside The Gate', desc="""
    Everything inside the gate is black with soot: the walls, the floor, the
    faces of the guards.  The air is hot and smells of coal and iron.  A street
    of the hold runs north, a low door leads west into a store room, and the gate
    opens east onto the mountain.""",
    exits={'n': 'A soot-dark street of the hold runs north.',
           'e': 'The great gate leads out onto the mountain.',
           'w': 'A low doorway leads into what looks like a store room.'})
R[6514] = dict(name='The Soot Street', desc="""
    A street of the hold runs between houses carved straight into the rock.  Many
    of the doors are marked with a smear of ash, the sign of a house that lost
    someone in the old mine.  Nearly every door is marked.  The street runs north
    to the shops and south to the gate.""")
R[6515] = dict(name='A Turn In The Soot Street', desc="""
    The street turns here.  West, through an open arch, lies the Hide and Tooth,
    the armoury of the hold, and a stream of sound comes out of it, hammering and
    haggling.  Wagons of finished plate are loaded at the arch for the road to
    the front.  The street runs back south.""",
    exits={'w': 'The open arch of the Hide and Tooth armoury lies to the west.'})
R[6516] = dict(name='The Hide And Tooth', desc="""
    The armoury of Orrund, where the forges' best work is sold: hammers, axes,
    plate, helms and gauntlets, all stamped with the anvil-mark of the hold.  The
    walls are racked to the ceiling.  Half of everything here is already
    promised to the wall, and the price of the rest is high.  The street lies
    north and east.""",
    extras={'racks rack walls': 'Hammers and axes in rows, plates on stands, helms on pegs. A tag on each rack reads, in hard dwarvish letters: "Sold to Midgaard. Paid late."'})
R[6517] = dict(name='North Of The Armoury', desc="""
    The street runs north past the armoury.  To the west a warm red glow and the
    smell of bread come from the door of Granitehead's bakehouse.  The street
    continues north and back south.""")
R[6518] = dict(name='The Bend By The Forges', desc="""
    The street bends east here past the long wall of the great forges, where the
    heat comes through the very stone.  Behind that wall a hundred hammers never
    stop.  The barracks lie east; the shops are south.""")
R[6519] = dict(name='By The House Of Healing', desc="""
    The street passes the House of Healing, whose door to the north is hung with
    a white cloth.  Moans can be heard from inside.  Carts of wounded come in
    here from the mine and from the front alike.  The street runs east toward
    the barracks and west toward the forges.""")
R[6520] = dict(name='The Street Of Shields', desc="""
    Old shields line both walls of this stretch of street, each painted with the
    arms of a dwarven house.  Many are cracked across, and none have been
    repainted in years.  The street runs east to the barracks and back west.""")
R[6521] = dict(name='The Barracks Gate', desc="""
    The street ends at the barracks of the hold's wardens.  A door leads south
    into the barrack rooms, and wardens loll about the gate between watches.  The
    street runs back west.""")
R[6523] = dict(name='The First Barrack Room', desc="""
    A long barrack room of stone bunks, axes hung at the head of each.  A good
    many bunks have no axe.  The wardens here sleep in their mail.  The barracks
    continue south, and the door leads north to the street.""")
R[6524] = dict(name='The Back Of The Barracks', desc="""
    The back of the barracks is a low, foul room of bunks, boots and sour
    blankets, and it stinks of sweat and old ale.  Some of the bunks are strewn
    with the gear of wardens who went down into the old mine and never came back,
    and no one has had the heart to clear them away.  The only way out is north.""")
R[6526] = dict(name='A Store Room', desc="""
    A forgotten store room behind the gate.  Dust lies three fingers deep on the
    floor, undisturbed for months, and empty ore-barrels are stacked against the
    walls.  They were meant for ore from the old mine.  A brighter doorway leads
    east.""",
    extras={'floor dust': 'After blowing the dust off the floor, you notice a trapdoor!',
            'barrels barrel': 'Ore-barrels branded with the mark of the lost mine. They have never been filled.'},
    exits={'e': 'A lighted doorway leads east onto a well-worn floor.',
           'd': 'After blowing the dust off the floor, you notice a trapdoor.'})
R[6527] = dict(name='The Old Wine Cellar', desc="""
    A cold cellar that smells of sour wine and something worse.  The casks are
    broken and dry.  This is where the King's ale was once kept, against the day
    he came home from the old mine.  Frost forms on the stone where nothing
    should make it cold.  A trapdoor leads up.""")
R[6534] = dict(name='The House Of Healing', desc="""
    The House of Healing of Orrund is a long cavern of pallets, lamps and
    basins.  It smells of spirits and blood.  Dwarves lie here burned at the
    forges, crushed in the mine, or sent back broken from the wall, and the
    healer moves among them without rest.  The street is south.""")
R[6535] = dict(name="Granitehead's Bakehouse", desc="""
    A hot little bakehouse where Granitehead bakes black stone-bread for the
    forges and the wall.  The ovens glow red and the air is thick with flour
    and the smell of the crust.  It is the only room in the hold where anyone
    laughs.  The street is east.""")

# ----------------------------------------------------------- the Widow's Spire
R[6525] = dict(name="Inside The Widow's Spire", desc="""
    The inside of the Spire is a single round hall with no ornament at all.
    Queen Hrodna had it all stripped bare and sent the gold and silver of the
    walls to the forges.  A stair winds up around the wall, and the door leads
    out to the west.""")
R[6528] = dict(name='On The Winding Stair', desc="""
    The stair circles up the inner wall of the Spire.  Small windows show
    nothing but the dark of the cavern outside.  The stair goes on up and down.""")
R[6529] = dict(name='Higher On The Winding Stair', desc="""
    Still the stair circles, around and around, and the steps are worn hollow by
    generations of feet.  Near the top they are worn deepest: the Queen climbs
    and descends here every night, unable to sleep.  The stair continues up and
    down.""")
R[6530] = dict(name='At The Top Of The Stair', desc="""
    The stair ends at a small landing near the top of the Spire.  A passage
    leads east toward the royal rooms, and the stair winds back down.""")
R[6531] = dict(name="The Petitioners' Hall", desc="""
    The hall where petitioners wait to see the Queen.  It is always full of
    widows: wives and mothers of miners lost in the old mine, come to ask her yet
    again to send the wardens down for the bodies.  She never does.  A door to
    the north leads to the Queen's chamber, and the stair is west.""")
R[6532] = dict(name="The Queen's Chamber", desc="""
    The Queen's own chamber is cold and bare.  The bed has not been slept in.
    A suit of the dead King's armour stands in the corner, dented and empty.  A
    ladder leads down through a hatch to the outside of the Spire, a door leads
    south, and a small wooden door is set into the west wall.  A note is pinned
    above the bed.""",
    extras={'sign note': 'In a firm, tired hand: "Whoever finds a key here: it opens the deep maze below the mine. The mazekeeper has turned against the crown and stolen the key of my treasury. Go down, and bring it back. He lairs deep in the mines. -- Hrodna"',
            'armour armor suit king': 'King Bromm\'s armour, brought back up out of the old mine by the last party to come out alive. They could not bring the King.'})
R[6533] = dict(name="Beneath The Spire, Outside", desc="""
    The ladder comes out on a ledge on the north side of the mountain, under the
    open sky.  The Spire's top pierces the rock above.  To the south and west
    lie mountains, and somewhere beyond them, under the hills, lies the old mine.
    The only way is back up the ladder.""")
R[6554] = dict(name="The Queen's Treasury", desc="""
    The treasury of Orrund, once the richest in the east.  Now most of its
    shelves are bare: the gold has gone to pay for coal, food and bodies, and
    the rest is being saved, the Queen says, for the day Orrund takes back the
    old mine.  The only exit is east.""")

# ------------------------------------------------------------ the working mine
R[6540] = dict(name='The Soot-Path', desc="""
    A well-worn path runs through the mountain, grey with coal dust.  To the
    east an iron door shuts off the working mine; the narrow way leads north,
    and the summit gate lies west.""")
R[6541] = dict(name='The Mine Mouth', desc="""
    Beyond the iron door the floor drops into a square shaft.  A chain of
    buckets creaks up and down it, carrying coal for the forges.  The shaft leads
    down, and the door is west.""")
R[6542] = dict(name='At The Bottom Of The Shaft', desc="""
    The bottom of the shaft, where the air is so thick with soot that every
    breath tastes of it.  The mineworkers here have black rags tied over their
    faces.  The gallery runs east, and the shaft leads up.""")
R[6543] = dict(name='The Coal Gallery', desc="""
    A long gallery cut through a seam of coal.  It is poor coal and a poor
    seam, nothing like the riches of the old mine, but it is all Orrund has
    left.  Overseers drive the workers hard.  The gallery runs east and back west
    to the shaft.""")
R[6544] = dict(name='The Mine Crossing', desc="""
    Four ways meet here under a ceiling shored with timber.  A heavy door to the
    north seals the deep maze, the old defensive galleries; nobody goes there
    now.  The coal store is east, the equipment room south, and the gallery runs
    west.""")
R[6545] = dict(name='The Coal Store', desc="""
    A cavern heaped with coal waiting to be hauled up.  The props holding up the
    roof are cracked and bowed, and grit sifts down from above with every blow of
    the hammers far overhead.  The crossing is west.""")
R[6551] = dict(name='The Equipment Room', desc="""
    A cramped room of racks for picks, lamps and ropes.  Most of the racks are
    empty: the tools wear out faster than the smiths can spare time to make new
    ones, and the forges serve the wall first.  The only way out is north.""")
R[6546] = dict(name='The Mouth Of The Maze', desc="""
    Beyond the door begin the deep maze's galleries, built long ago to confuse
    anything that dug in from below.  The dwarves remember why that was
    necessary now.  Carvings show to the east, and the door leads back south.""")
R[6547] = dict(name='At The Maze Inscription', desc="""
    You are inside the maze, but not yet far enough to be lost.  An old warding
    inscription is cut into the wall, the way the builders left it for their own
    folk: a row of numbers, 1 3 2 4, and under each a letter, N W N S.
    Passages lead north, east and west.""",
    extras={'inscription carving carvings wall': 'The inscription is cut in two rows. The upper row reads 1, 3, 2, 4. Under each number is a letter: under the 1 an N, under the 3 a W, under the 2 an N, under the 4 an S. Below, in fresher scratches: "Count them in order, as the builders did."'})
R[6548] = dict(name='In The Maze', desc="""
    The galleries here twist back on themselves.  The walls are rough and all
    the same, and the dust shows your own footprints going every way.  Openings
    lead north, south and west.""")
R[6549] = dict(name='Deeper In The Maze', desc="""
    A cold draught moves through this part of the maze, from somewhere below.
    A shed snake-skin, longer than a dwarf, lies coiled against one wall.
    Openings lead north, south and west.""",
    extras={'skin snake': 'A pale, papery skin shed by a serpent as thick as a dwarf\'s waist. It came up from far below.'})
R[6550] = dict(name='A Crossing In The Maze', desc="""
    Four galleries meet in the maze, each as dark and blank as the others.
    Someone has scratched marks at the mouth of each one and then scratched them
    out again.  Openings lead in every direction.""")
R[6552] = dict(name='The End Of The Maze', desc="""
    The maze ends in a bleak, cold gallery.  The way back into the maze is
    north.  To the south is a low doorway, and above it someone has cut a line of
    rough letters.""",
    extras={'sign letters doorway': 'Cut above the south doorway: "THOSE WHO ENTER, PLAN ON A TIMELY DEATH. ESPECIALLY IF YOU ARE LOYAL TO THE QUEEN."'})
R[6553] = dict(name="The Mazekeeper's Room", desc="""
    The mazekeeper's den.  The walls are covered in charcoal drawings of the
    Queen, with knives stuck through them, and scrawled words: THE QUEEN SOLD
    THE DEEP.  THE DEAD ARE CALLING.  WE WILL GO HOME.  The floor has been dug at
    with bare hands, as if he were trying to reach something below.  The only
    way out is north.""",
    extras={'drawings words walls wall': 'Again and again: "The Queen sold the deep." Lower down, in a smaller and shakier hand: "They are not dead down there. They are waiting."'})

# =================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d


M[6500] = mob('a warden of Orrund', 'warden guard dwarf dwarven', 'A warden of Orrund stands here, axe on his shoulder.',
              'A broad, scarred dwarf in soot-black mail, with his beard braided short so nothing can grab it. He looks at outsiders as if they owe him something.')
M[6501] = mob('a dwarven porter', 'porter worker dwarf dwarven', 'A dwarven porter trudges by under a load of blades.',
              'A dwarf bent under a great bundle of new-forged blades bound for the front. He has carried a load like this down the mountain every day for years.')
M[6502] = mob('the wraith', 'wraith shade ghost', 'A wraith hangs in the cold air here, waiting.',
              'A black, almost transparent shape with the outline of a dwarf in mail. Something came back up from the old mine that was not quite the warden who went down.')
M[6503] = mob('the armourer of the Hide and Tooth', 'storekeeper armourer shopkeeper', 'The armourer of the Hide and Tooth stands here, arms folded.',
              'A thick, rotund dwarf with forge-burns on both forearms. He sells the hold\'s steel to anyone who can pay, and to Midgaard, who often cannot.')
M[6504] = mob('Granitehead the baker', 'baker granite head granitehead', 'Granitehead the baker waits behind his counter, covered in flour.',
              'A cheerful old dwarf white with flour to the elbows. He lost three sons in the old mine and bakes as if bread could fill the hole.')
M[6505] = mob('a tunnel lizard', 'lizard giant tunnel', 'A tunnel lizard forages along the stone floor here.',
              'A long, pale lizard as big as a pony, bred by the dwarves to haul ore carts. Since the old mine fell there is not enough ore to haul, and it wanders the hold, hungry.')
M[6506] = mob('the hill giant', 'giant hill', 'A hill giant prowls the narrow way here.',
              'A giant, nearly eighteen feet tall, wearing a dwarf\'s plate as a breastplate. It has come down from the high peaks because the west is driving everything east.')
M[6507] = mob('a dwarven mineworker', 'mineworker dwarven dwarf miner worker', 'A dwarven mineworker swings his pick at the coal here.',
              'A worn-out dwarf black with coal dust, muscles knotted from too many shifts. He curses the poor seam and the old mine both.')
M[6508] = mob('the overseer', 'mineleader overseer dwarven dwarf mine leader', 'A dwarven overseer is here, driving the work.',
              'A huge, hard dwarf who keeps the coal coming for the forges. He was a gallery-master in the old mine, and he was among the last out.')
M[6509] = mob('the dwarven healer', 'doctor healer dwarven', 'The dwarven healer moves among the sick and wounded here.',
              'A grey-bearded healer who has not slept a whole night in years. He prays to the old stone-gods with every bandage, and they have not answered lately.')
M[6510] = mob('a wounded dwarf', 'peon wounded dwarven dwarf', 'A wounded dwarf lies here, waiting for the healer.',
              'A dwarf bandaged from shoulder to hip, sent back from the wall with a wound that will not close.')
M[6511] = mob('an off-duty warden', 'dwarf warden', 'An off-duty warden sits on a bunk, oiling his axe.',
              'A young warden who has only ever known Orrund at war. He talks of the old mine as if it were a story.')
M[6514] = mob('a barrack guard', 'guard barrack warden', 'A barrack guard lounges here between watches.',
              'A sour veteran warden who would rather be asleep, and makes sure you know it.')
M[6516] = mob('the mazekeeper', 'mazekeeper keeper', 'The mazekeeper crouches here, muttering at the floor.',
              'A gaunt dwarf with wild eyes and bleeding fingers, who was set to keep the deep maze and has listened too long to what moves beneath it. He blames the Queen for the old mine, and he means to go home.')
M[6517] = mob('a pale cave serpent', 'snake giant serpent', 'A pale cave serpent coils in the dark here.',
              'A huge colourless snake that came up out of the depths, from the direction of the old mine. Its eyes are milky and blind, and it does not need them.')

# =================================================================== objs
O[6500] = dict(short='the key of the Queen\'s treasury', aliases='key treasury', long='The key of the Queen\'s treasury is lying here.')
O[6501] = dict(short='the hoard of Orrund', aliases='gold treasure coins hoard',
               long='A great heap of dwarven gold lies here: the last hoard of Orrund.')
O[6502] = dict(short='an iron mine key', aliases='key mine iron', long='An iron key to the mine door is lying here.')
O[6503] = dict(short='a bright golden key', aliases='key bright gold golden', long='A bright golden key, stamped with the Queen\'s mark, is lying here.')
O[6504] = dict(short='a dwarven hammer', aliases='hammer dwarven war', long='A heavy dwarven war-hammer, stamped with the anvil-mark, lies here.')
O[6505] = dict(short='a suit of dwarven plate mail', aliases='plate dwarven mail', long='A suit of dwarven plate mail lies here, black with forge-scale.')
O[6506] = dict(short="a long black healer's staff", aliases='staff stick black long healer',
               long="A long black healer's staff lies here.",
               extras={'staff stick black long healer': 'A staff of black stone-wood carved with runes of mending. The runes are worn nearly smooth.'})
O[6507] = dict(short='a black glowstone rod', aliases='stick black long glowstone rod', long='A long black rod tipped with a glowstone is propped here.')
O[6508] = dict(short='a dwarven club', aliases='club dwarven cudgel', long='An iron-banded dwarven club lies here.')
O[6509] = dict(short='a two-handed dwarven axe', aliases='axe two-handed dwarven', long='A great two-handed dwarven axe is here.')
O[6510] = dict(short='a dwarven helmet', aliases='helmet helm dwarven', long='A dented dwarven helmet is here.')
O[6511] = dict(short='a golden dwarven ring', aliases='ring gold golden dwarven', long='A golden dwarven ring, engraved with a house-mark, is lying here.')
O[6512] = dict(short='a pair of dwarven gauntlets', aliases='gloves gauntlets dwarven', long='A pair of thick dwarven gauntlets lie here.')
O[6513] = dict(short='a chunk of coal', aliases='coal chunk', long='A chunk of poor, crumbling coal lies here.')
O[6514] = dict(short='a mining pick', aliases='pick mining', long='A worn mining pick is here.',
               extras={'pick mining': 'The haft is carved with old miners\' warding runes, the kind they cut in the old mine. They look almost blessed.'})
O[6515] = dict(short='a deep green key', aliases='key deep green', long='A deep green key to the gate of Orrund is lying here.')
O[6516] = dict(short='an old key', aliases='key old maze', long='Someone seems to have dropped an old key.')

RETHEME = {
    'zones': {65: 'The Dwarven Kingdom of Orrund'},
    'rooms': R, 'mobs': M, 'objs': O,
}
