"""Rand's Tower (zone 64) re-themed: the drowned tower of a dead mage.

Rand was a mage who believed he could bargain with what is in the west --
open a door for it in exchange for power and his own safety.  Generations ago
he called something through in the summoning room under his tower.  The
summoning went wrong: the mountains round his valley burst, molten rock filled
the valley and buried the tower to its upper floors, and Rand died at his own
front doors trying to flee.  The thing he called is still bound in the circle
below; the things that came with it still walk the halls, and Rand's household
wards still keep the linen clean and the larders full for a master who will
never come back.  Entry is by the trapdoor in the crown of the tower, which is
all that shows above the cooled lava; the tower is explored top-down.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs


def room(name, desc, **kw):
    d = dict(name=name, desc=desc)
    d.update(kw)
    return d


# ====================================================================== the climb
R[6400] = room('A Mountain Trail', """
    A thin trail climbs steeply into the mountains, picking its way along
    ledges where one slip would mean a long fall.  Goats have worn it; few men
    have.  The trail climbs on to the east, and drops back west into the small
    hidden valley.""")
R[6401] = room('A Mountain Trail', """
    The trail is very high now and the air thin and cold.  Below, the hidden
    valley is a black thumbprint among the rocks.  The way goes on up to the
    east, and back down to the west.""")
R[6402] = room('A Mountain Trail', """
    Ragged clouds drift past at the level of the trail and the ears ache with
    the height.  Ahead to the east is the shoulder of the mountain, and beyond
    it the peaks stand in a strange broken ring around some great hollow.  The
    trail also leads down to the west.""")
R[6403] = room("Below The Mountain's Peak", """
    The peak rises a few hundred feet higher, but here the trail tips over the
    shoulder and down into the valley beyond.  It is a valley drowned in stone:
    long ago, molten rock poured into it hundreds of feet deep and set flat and
    black.  Nothing about it looks natural.  The path leads down east into the
    valley, and west back toward the living world.""")
R[6404] = room('The Trail To The Valley', """
    The trail winds down toward the black valley floor.  Thin, grey trees have
    taken root in the old lava, and judging by their height it cooled many
    lifetimes ago.  Below, the path enters a silent wood and is lost.  East
    leads into the valley; west climbs back up the mountain.""")
R[6405] = room('In The Drowned Valley', """
    A skin of thin soil lies over the rock, but the valley is too flat and too
    stony to hide what happened here.  The ring of mountains around it is
    shattered, their peaks blown open as if from within, though none of them
    ever burned.  Shepherds say it was a mage who did it.  The path leads into
    the woods to the east, and back up the mountain to the west.""")
R[6406] = room('A Clearing In The Grey Wood', """
    A small clearing among the grey trees, utterly silent; no bird sings in this
    wood.  Squared blocks of stone break the ground here in a wide circle, and
    on a second look they are battlements: the crown of a tower, buried almost
    to its top by the lava.  In the centre a rusted iron ring is set into an old
    trapdoor.  The path leads back west.""",
    exits={'d': 'An ancient trapdoor, crusted with earth and age. Someone has scratched a warding sign into it, and then, beneath it, the word NO.'},
    extras={'battlements blocks stone stones': 'The tops of crenellations, black-streaked where the molten rock lapped against them. The tower is under your feet.',
            'ring trapdoor': 'A rusted iron ring on an old trapdoor. Someone has scratched a warding sign into the wood, and beneath it, the word NO.'})

# ====================================================================== upper floors
R[6407] = room('The Head Of The Stair', """
    The top of a stairwell that winds down deep into the tower.  Thin daylight
    leaks around the edges of the trapdoor overhead.  To the south is a wooden
    door, untouched by the years; to the west runs a short hall.  The stair
    goes on down into the dark, and the air that rises from it smells of
    decay.""",
    exits={'u': 'The ancient trapdoor overhead, leaking a thin grey light around its edges.'})
R[6408] = room('A Linen Closet', """
    Shelves of linen line the walls, sheets and pillow-cases washed and folded
    as if this morning.  Rand's household wards still keep them so, generations
    after there was anyone left to sleep in them.  The neatness is worse than
    dust would be.  The door leads north.""",
    extras={'linen shelf shelves sheets': 'White sheets, crisp and clean, folded with care. One has been unfolded and laid out flat on the floor, the way a shroud is laid.'})
R[6409] = room('A Corridor', """
    A clean, bare corridor, swept by nobody.  It leads back east to the
    stairwell, and doors open off it to the north and south.  A faint smell of
    lavender hangs in the air, and under it, something else.""")
R[6410] = room('A Bathing Room', """
    A bathing room of the old mage's devising.  Pipes leading from nowhere fill
    the basins with hot and cold water that drains away to nowhere, and the
    taps still run when touched.  The mirror over the basin has been turned to
    face the wall.  The door is north.""",
    extras={'mirror': 'A tall silvered mirror, turned to the wall. On its back someone has written in a shaking hand: do not look at what stands behind you.'})
R[6411] = room("Rand's Bedchamber", """
    An opulent chamber hung with silks and gold thread.  Against one wall stands
    an ebony desk, and over it the lava has burst in through the window and
    spilled across its surface in a black, frozen wave.  A spacious closet holds
    clothes still cleaned and pressed for a man long dead.  The door is
    south.""",
    extras={'desk': 'Rand\'s ebony desk, half buried under a tongue of cooled lava. Its drawers can still be reached.',
            'closet clothes': 'Fine robes of a mage, freshly pressed. They are cut for a tall, thin man, and none of them will ever be worn again.',
            'lava window': 'Molten rock poured in at the window and froze in mid-fall, a black wave caught as it broke.'})
R[6412] = room('The Library', """
    A great mage's library fills this floor of the tower, shelf upon shelf of
    books on every art, and more on the arts that should not be practised.  Many
    volumes lie torn open on the floor, their pages stirring though there is no
    draught.  A door leads back east to the stairwell, and a big bookcase stands
    against the west wall.""",
    exits={'w': 'A big bookcase stands against the west wall. It does not sit quite flush.'},
    extras={'book books': 'Treatises on warding and binding, on the far roads, on the voices that answer from the west. Rand\'s notes crowd every margin.',
            'bookcase': 'A big bookcase that does not sit quite flush against the wall.'})
R[6413] = room('The Stairwell', """
    The stairwell winds on up and down through the tower, the stone steps worn
    in a single narrow track.  A door leads west onto this floor.""")
R[6414] = room('A Hidden Hall', """
    A small, hidden hall behind the library.  At its north end, in the east
    wall, is the back of the movable bookcase; at its south end a trapdoor is
    set in the floor.  Claw marks score the trapdoor deep.""",
    exits={'e': 'The back of a movable bookcase.',
           'd': 'A trapdoor in the floor, deeply scored with claw marks.'})
R[6415] = room('A Stairwell', """
    The stairwell continues up and down.  A door to the west opens onto this
    floor, and the walls here are scratched with tallies, as if someone
    counted days on the way down.""")
R[6416] = room("Rand's Treasury", """
    A small, low room where Rand kept his wealth: heavy chests ranged against the
    walls, the price of many years of dangerous work.  The air is thick and
    cold, and the darkness in the corners does not lift when a light is
    brought in.  The trapdoor leads back up.""",
    exits={'u': 'The trapdoor back up to the hidden hall.'})
R[6417] = room('A Hallway', """
    A hall runs through the servants' floor of the tower.  It goes on to the
    west, doors lead north and south, and a door to the east opens back onto the
    stairwell.  Small, muddy footprints cross the floor and stop at a wall.""")
R[6418] = room("A Servant's Room", """
    A sparse servant's bedroom: a narrow bed, a nightstand, a chair and a table.
    The bed is made.  On the table lies a half-finished letter home, the ink
    dried for a lifetime.  The door leads north.""",
    extras={'letter': '"...the master says it will make us all safe. He says when the West comes it will pass us by. He has been in the cellar three days now. The lamps all burn blue."'})
R[6419] = room("A Servant's Room", """
    Another small servant's room, with a bed, a nightstand, a chair and a table.
    The chair is pushed hard against the door, and the bedclothes are torn into
    strips and knotted, as if for a rope that was never used.  The door leads
    south.""")
R[6420] = room('A Hallway', """
    The hallway goes on east, and a door opens to the north.  The layout of the
    floor is not quite right; the walls seem to sit a little further apart each
    time you look back.""")
R[6421] = room("A Servant's Room", """
    The third servant's room has a bed, a nightstand, a chair and a table, like
    the others.  But here a child's wooden doll sits on the pillow, facing the
    door, and the room is much colder.  The door leads south.""",
    extras={'doll': 'A small wooden doll in a faded dress. Its painted face has been scratched away.'})
R[6422] = room('The Stairwell', """
    The stairwell leads up and down, and a long, open hall lies to the west.
    Candle grease has run down the walls in long frozen streams.""")
R[6423] = room('The Dining Hall', """
    A long dining hall with a table running its length, laid for ten.  The
    plates are clean, the candles unlit.  Paintings and tapestries hang on the
    walls, and the lava that poured in at the windows has frozen black between
    them.  A door leads north, and the stairwell is east.""",
    extras={'tapestry tapestries painting paintings': 'Scenes of high magic: a mage with a staff at the head of a great company, a door opening in the west, a light pouring through it. In the last painting the light is coloured black.',
            'table plates': 'The table is laid for ten. At the head of it, the master\'s chair has been knocked over and left.'})
R[6424] = room('The Kitchen', """
    A well-stocked kitchen, its larders still fresh and full by the old wards,
    bread warm in the oven though no fire has been lit for generations.  It is
    almost a good place to rest; almost.  The door leads south.""")

# ====================================================================== lower floors
R[6425] = room('The Stairwell', """
    The stairwell runs up and down, and a hall opens to the west.  The stone
    here is damp and the walls sweat a cold, sour moisture.""")
R[6426] = room('The Cell Hall', """
    This part of the tower is dank and oppressive.  The hall runs north and
    south between cells, and an empty cell stands open to the west.  The
    stairwell is east.""",
    extras={'cell cells': 'An open cell with iron rings in the wall. Rand kept the people he needed for his work here. The cells are empty now.'})
R[6427] = room('The North Cells', """
    The north end of the cell hall.  Cells stand open on either side, empty, the
    straw in them rotted to black.  Names are scratched into the doorposts.  The
    hall leads back south.""",
    extras={'cell cells': 'Empty cells. The straw is black with age, and the chains have been opened with a key.',
            'names doorposts': 'Names, a dozen or more, scratched in different hands. Some are only marks.'})
R[6428] = room('The South Cells', """
    The south end of the cell hall.  The cells on either side stand open and
    empty, and in one of them a chalk circle has been drawn on the floor, very
    carefully.  The hall leads back north.""",
    extras={'cell cells': 'Empty cells, their doors standing open.',
            'circle chalk': 'A practice circle in chalk, the lines checked and redrawn many times. Rand tested his bindings here first, on whoever was in the cells.'})
R[6429] = room('A Stairwell', """
    The stair goes on up and down here.  A large room opens to the west.  The
    lamps in the niches burn with a faint blue light that gives no warmth.""")
R[6430] = room("Rand's Study", """
    A small desk here is buried under papers and documents, all preserved by
    magic.  Most are accounts and letters, but a sheaf of notes lies apart from
    the rest, weighted with a stone.  The room has a stale, closed-up feeling.
    The stairwell is east.""",
    extras={'paper papers documents document notes sheaf': 'Rand\'s notes, in a cramped hand. He writes that the West cannot be fought, only bargained with; that he has spoken with what is there, and it has promised to spare him and his when it comes east, if only he opens a door for it. The last page reads: "The terms are agreed. Tonight." Below that, in another hand, someone has written: "He was wrong."',
            'desk': 'Cluttered with papers. One sheaf, weighted with a stone, looks more important than the rest.'})
R[6431] = room('The Stairwell', """
    The stairs wind up and down, and a room opens to the west.  From far below
    comes a faint, steady hum, felt in the teeth more than heard.""")
R[6432] = room('A Sitting Room', """
    A plainly furnished room with chairs set about a fireplace in an inner wall,
    its chimney turned by some old magic.  The fire is laid but unlit.  Of all
    the rooms in the tower this one feels nearly safe, as if the wards here were
    made more carefully than the rest.  The stairwell is east.""")
R[6433] = room('The Foot Of The Stair', """
    The stairwell ends here at what was once the ground floor.  A hall leads
    west.  The hum from below is stronger now.""")
R[6434] = room('The Ground-Floor Hall', """
    A short hall on what was once the ground floor, running north and south.
    The stairwell to the east climbs into the shadowy heights of the tower, and
    to the west lies the entranceway.  The north end is sealed solid by a wall
    of black lava; southward the way is clear.""")
R[6435] = room('The Entranceway', """
    A grand chamber hung with tapestries and set with statues, meant to impress
    the kings and envoys who once came to treat with the mage.  Giant double
    doors stand to the west, sealed fast.  The main floor of the tower lies
    east.""",
    exits={'w': 'Great double doors of iron-bound oak. They are locked, and nothing short of a key will open them.'},
    extras={'sculpture tapestry sculptures tapestries statues': 'Fine work, faded now: kings and mages in procession toward the west. Not worth carrying away.'})
R[6436] = room("The Doorway Of Rand's Tower", """
    This was the entrance to the tower; now the lava has sealed it completely.
    When the summoning broke, a man was running for these doors.  The molten rock
    caught him there and flung him against them, and his blackened skeleton is
    still pressed to the wood, its hand clutching a staff.  It is Rand.""",
    exits={'e': 'The double doors bear the scorched outline of a man, burned into the wood.'},
    extras={'skeleton man rand': 'A tall, thin skeleton pressed into the doors, its jaw open. Even in death its fingers are locked around its staff. Rand did not get out.'})
R[6437] = room('The Barred Hallway', """
    The southern end of the hallway.  To the west is a door barred with
    gleaming bands of light, Rand's last and strongest warding, still holding.
    The hallway runs back north.""",
    extras={'bands light': 'Bands of cold white light lie across the western door. They are wards against what lies below, and they are meant to keep it in.'})
R[6438] = room('The Cellar Stair', """
    Stairs lead down here into the tower's cellars.  A door leads east back onto
    the main floor.  The steps are coated with a fine grey ash.""")
R[6439] = room('The Cellar Stair', """
    The stair climbs here to the main floor, and the cellar opens to the east.
    The grey ash lies deeper, and it is scuffed by many feet, none of them
    shod.""")
R[6440] = room('An Alcove', """
    An alcove in the cellars.  A great room opens to the north, stairs lead
    down to the east, and the stair back up is to the west.  The hum is very
    loud here.""")
R[6441] = room('The Laboratory', """
    Rand's laboratory, crowded with beakers, flasks, burners and tongs, mortars
    and pestles, and jars: jars of salts, jars of strange things, jars of things
    that moved once and might again.  Much is broken.  A careful search might
    turn something up.  The alcove is south.""",
    extras={'beaker beakers flask flasks burner burners tong tongs': 'Fine glass and brass, much of it shattered, as though everything on the benches jumped at once.',
            'mortar mortars pestle pestles jar jars': 'Jars of powders, salts, and pale things in cloudy fluid. One jar has been opened from the inside.'})
R[6442] = room('The Deep Stair', """
    Stairs lead down here to the lowest cellar, or back west to the alcove.  The
    stone is warm underfoot, and a light that is not quite a light comes from
    below.""")
R[6443] = room('The Deep Stair', """
    The stair climbs back up to the first cellar.  To the east opens a great
    room, lit by a dull, sick glow.  Every instinct says to go back up.""")
R[6444] = room('The Summoning Room', """
    A vast vault, dimly lit by a great glowing circle of binding cut into the
    floor.  Bands of force rise from it and wrap about something trapped inside,
    something Rand called out of the west.  It has been waiting there for
    generations, and it is watching.  Stepping into the circle would be the last
    thing anyone ever did.  The stair is west.""",
    extras={'pentagram circle binding': 'The circle is cut deep into the stone and filled with silver, and it still burns. In one place the cut has cracked. That is where it went wrong.',
            'being thing': 'It cannot be seen clearly through the bands of force, but its shape is wrong, and its attention is a weight on the skin. Whatever it is, it is very, very angry, and it remembers Rand.'})
R[6445] = room('Inside The Circle', """
    The thing Rand called out of the west turns its attention fully upon you.
    There is no fight, no struggle, only a moment of seeing what it is, and then
    nothing at all.  It has been bound here for generations, and it does not
    let go of what it catches.  You are dead.""")

# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d


M[6400] = mob('the mountain goat', 'goat mountain', 'A gaunt mountain goat picks at a tuft of grass here.',
              'A rangy goat, well used to the cliffs. It will not go near the valley below, and it eyes you warily.')
M[6401] = mob('the Demon of Decay', 'demon decay', 'A cloaked, clawed demon of decay comes at you, rotting the air around it!',
              'One of the things that came through when Rand\'s summoning broke. Wood softens and metal pits where it walks, and it hates anything that is still alive.')
M[6402] = mob('the Book Haunt', 'haunt book monster guardian', 'A mound of torn books heaves up into a man\'s shape and lunges at you!',
              'Rand\'s library, possessed. Pages and bindings churn in the shape of a man, and where its face should be is a book of the mage\'s own notes, flapping open and shut like a mouth.')
M[6403] = mob('a Dread', 'dread feeling bad', 'A dread closes on your throat like a hand.',
              'It is like every dread you have ever felt, but heavier, and it has a shape. Something from the west that clings to the room where Rand slept.')
M[6404] = mob('Your Worst Nightmare', 'nightmare', 'Your worst nightmare takes shape in front of you and attacks!',
              'Your own deepest fears, given flesh by what Rand let in. It has your face, or the face of someone you lost.')
M[6405] = mob('the Warden', 'guardian warden', 'A warden of bound stone guards the barred door. It turns and attacks!',
              'A guardian that Rand bound to watch the door to his cellars. It does not know he is dead. It knows only that nobody passes.')

# ====================================================================== objs
O[6400] = dict(aliases='dagger glowing', short='a glowing dagger', long='A dagger lies here, glowing with a cold light.')
O[6401] = dict(aliases='platemail glowing plate mail', short='the glowing platemail',
               long='A suit of platemail lies in a heap here, glowing faintly.',
               extras={'platemail plate mail': 'Heavy plate worked with Rand\'s wards. It glows with a pale light that does not warm.'})
O[6402] = dict(aliases='agate gem', short='an agate', long='A small banded agate lies here.')
O[6403] = dict(aliases='jade jewel', short='a piece of jade', long='A small piece of green jade gleams here.')
O[6404] = dict(aliases='sculpture statue', short='a piece of sculpture', long='A fine piece of sculpture stands here.',
               extras={'sculpture statue': 'A woman carved in white stone, straining beneath a heavy weight, tears chiselled on her cheeks. On the base: "For Ilsa, who would not leave." It makes you sad.'})
O[6405] = dict(aliases='vial dragons blood', short="a vial of dragon's blood",
               long='A small vial of dark red fluid lies in the ash here.',
               extras={'vial blood': 'A stoppered vial of thick red blood, one of Rand\'s rarest reagents. It is still warm.'})
O[6406] = dict(aliases='amulet warding', short='a warding amulet', long='An amulet of tarnished silver has been dropped here.',
               extras={'amulet warding': 'A silver amulet cut with a warding sign. It did not save whoever wore it.'})
O[6407] = dict(aliases='rod pole surveyor', short="a surveyor's rod",
               long="A long rod marked with Rand's measuring runes has been cast aside here.",
               extras={'rod pole surveyor runes': 'A rod of iron-shod ash, marked with runes for measuring out circles of binding. There is power still in it.'})
O[6408] = dict(aliases='bag powder wealth', short='a bag of powder of wealth',
               long='A small bag filled with glittering powder lies here.')
O[6409] = dict(aliases='desk drawers ebony', short='an ebony desk', long='Rand\'s ebony desk stands here, half buried in lava.')
O[6410] = dict(aliases='book chaos', short='the Book of Chaos',
               long='A book whose title crawls across its cover rests here.')
O[6411] = dict(aliases='book elder', short='the Book of the Elder', long='A grey-bound book lies here.')
O[6412] = dict(aliases='lens occluded', short='the Occluded Lens',
               long='A smoky lens about a foot across lies scuffed in the dust here.',
               extras={'lens occluded': 'A disc of smoked glass. Through it the world looks dimmer, and other things can be seen moving in it.'})
O[6413] = dict(aliases='mevais herb leaf', short='a leaf of mevais',
               long='A small black leaf of mevais lies here, well preserved.',
               extras={'mevais herb leaf': 'A black, glossy leaf from Rand\'s stores. Chewing it might have interesting effects.'})
O[6414] = dict(aliases='bottle peska', short='a bottle of peska', long='A bottle of milky fluid stands here.',
               extras={'bottle peska': 'A milky concoction with strange motes drifting in it, brewed by Rand for his long nights.'})
O[6415] = dict(aliases='staff rand', short="Rand's staff", long='A metal-shod staff lies here.',
               extras={'staff rand': 'The staff of Rand, carved with binding-signs from end to end. It is still warm where his hand held it.'})
O[6416] = dict(aliases='chest wooden', short='a wooden chest', long='A heavy wooden chest stands here.')
O[6417] = dict(aliases='chest wooden', short='a wooden chest', long='A heavy wooden chest stands here.')
O[6418] = dict(aliases='chest wooden', short='a wooden chest', long='A heavy wooden chest stands here.')
O[6419] = dict(aliases='basin water', short='a water basin', long='A basin of crisp, clean water from nowhere stands here.')
O[6420] = dict(aliases='food bread', short='some food', long='Some food from the warded larder lies here.',
               extras={'food bread': 'Bread, cheese and cold meat, fresh as the day they were laid in. Rand\'s wards keep the larder for a master who will never eat again.'})

RETHEME = {
    'rooms': R, 'mobs': M, 'objs': O,
}
