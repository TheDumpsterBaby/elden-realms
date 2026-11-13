"""New Thalos (zone 54), PART A: zone name, rooms 5400-5549, all mobs.

New Thalos is the crowded refugee city the survivors of Old Thalos built,
generations ago, when the first darkness took their old city.  It is poor,
packed, devout and watchful, and it remembers.  Today it feeds the front:
grain, cloth, recruits and coin go west on the Supply Road to Midgaard's wall.
The stock desert-city flavour (Sultan, Medina, Casbah) is kept; the desert is
gone (zone 50 is now the Supply Road through the hills south of the city).

CITY PLAN (shared with Part B, rooms 5550-5699 + objects; keep consistent)
--------------------------------------------------------------------------
Faith: the Last Flame (matches Part B), the fire the survivors carried out
of Old Thalos on the Night of Leaving; it burns in the palace Shrine of the
Last Flame (5566).  A black flame marks the dead; the old crest is a tower and
a rising sun.  The people fear the dark more than anything.  No real-world
gods: the stock Hindu statues, Allah, Akbal, Kali, Lugh, Daghdha, Cu Chulainn
are all replaced (Isvar kept for the river/drive to match Part B -- flagged).
  * Temple of the Last Flame (5503-5513, 5519, 5520): its altar fire is kindled
    from the Last Flame; the priests are Flame-wardens; high priest = the High
    Warden; clerics' guild/bar/sanctum, donation room, Temple Square.
  * Hall of the Saints (stock Museum of the Greater Gods, 5511, 5516): eight
    statues -- six saints of the Leaving and two of the darkness they fled
    (the Hollow King, the Mourning Sultana), kept so no one forgets.
  * Mob 5455 (stock Allah) is the Keeper of the Last Flame, a guardian of pale
    fire in the shrine (still aggro evil/neutral); it carries the wrath of the
    Flame (obj 5496).
Ruler: the Sultan, last of the line of Old Thalos's sultans, rules from the
  Palace (5550-5605, Part B), most of its treasure sold for the tithe to the
  wall: grand entrance, halls, dining hall, kitchen,
  Sultan's Garden + gazebo (pegasus, nightmare), art exhibit (mimic painting
  of his mother), the Women's Court (stock Harem: ladies of the court, a
  chamber guard, Nahrin the favourite who is a knife in the pillows), throne
  room (Sultan + half-orc bodyguard), treasure room, the beast pits (stock dungeon cells;
  jailer; things caught on the roads, kept for the war-magi to study).  City
  Hall (5554, the tithe hall: the Mayor's ledgers decide who goes west), Jail (5553), Library (5551, a librarian), Dance Hall
  (5552, the hall of remembrance), guard houses and wall towers, guilds on the Row (bowyers 5555,
  masons 5556, tanners 5564).
Streets (Part A):
  * Market Square (5405-5409, 5414-5417): the ration market; bakery stall,
    general store, bank, tailor, greengrocer, butcher, armourer, weaponsmith.
    Centre statue: the Sultan who led the exodus.
  * The Medina + Common Square (5403, 5404, 5410): the commons, where the
    newest refugees sleep; the Southern Bridge and South Gate (5411-5413) lead
    out to the Supply Road.
  * Sultan's Walk (5418-5421): north from the market between the Palace (west)
    and the Exile's Rest inn (east, stock Dancing Daemon, 5400-5402) to the
    North Gate (5422).  North of the city: the mountains (Part B).
  * Main Street: West Main (5423-5426) to the West Gate, Temple Square and the
    Warriors' Guild (the levy drill-yard, the Whet Stone); East Main
    (5427-5431) to the East Gate, the Mages' Tower, the apothecary (Witch's
    Brew), Braheem's magic shop and the Mercenaries' Guild.
  * Isvar Drive (5433-5442) along the River Isvar: warehouses packing goods for the front, shipwright,
    boat ramp, farrier's forge, Royal Stables, fish market, the Dump.
  * The Casbah (5444-5454): the avenue under the north wall, past the jail,
    City Hall and the Palace wall to the library end; NW/NE towers.
  * Lantern Row (stock Lantern Row, 5455-5456): library and dance hall.
  * Guildsman's Row (5460-5464): weavers, craftsmen, bowyers, masons, tanners.
  * Alleys and the Underground (5457-5502): back alleys, a dark alley where
    lamps will not burn, manholes into old tunnels, and a hand-dug passage out
    under the wall (to 5570 Outside The Wall).  Thieves and smugglers.
  * River inside the walls (5483-5487), iron gratings at each end.
"""

R = {}   # rooms
M = {}   # mobs


def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d


# ====================================================================== the inn
R[5400] = dict(name="The Entrance To The Exile's Rest", desc="""
    The narrow foyer of the Exile's Rest, the oldest inn of New Thalos.  A lamp
    burns in a niche by the door, as one burns by every door in the city, and
    the boards are worn grey by boots.  An iron stair spirals up to the
    reception.  From the south comes the noise of the common room, and the
    door west opens onto Sultan's Walk.""",
    exits={'s': 'The common room is loud and crowded.',
           'w': "Carts and porters pass along Sultan's Walk.",
           'u': 'The iron stair spirals up to the reception.'})
R[5401] = dict(name='The Reception Area', desc="""
    A quiet room above the common hall, with a heavy desk, two worn sofas and
    a rack of keys.  Every bed in the house is let twice over, to recruits on
    their way to the Supply Road and to merchants who can pay for a door that
    locks.  A slate behind the desk lists the names of guests who did not come
    back for their things.  The stair spirals down.""",
    extras={'slate names': 'Names chalked in a careful hand, each with a date. Some have been there so long the chalk has gone into the wood.'},
    exits={'d': 'The stair spirals down to the foyer.'})
R[5402] = dict(name="The Exile's Rest", desc="""
    The common room of the Exile's Rest.  A great round bar fills the east end,
    and behind it an old mage pours a row of cups at once without touching the
    jug.  On a low stage a singer gives the old songs of Thalos, the ones about
    the white towers and the night they went dark, and the whole room sings
    the refrains.  Booths along the walls are packed with tired people.  The
    only way out is north.""",
    extras={'bar': 'The bar turns, very slowly, on no wheel you can see. The old mage keeps it turning out of habit, the regulars say, so he has something to think about other than his family.'},
    exits={'n': 'The foyer of the inn lies north.'})

# ====================================================================== medina / commons / south gate
R[5403] = dict(name='The Medina', desc="""
    The Medina is the widest road in New Thalos, and still it is too narrow.
    Families who arrived with nothing camp along its edges under scraps of
    canvas, and water-carriers shove through the crowd.  A Flame-warden goes
    by with a taper, lighting the street lamps early.  The Common Square opens
    south and the Medina runs on north.""",
    exits={'n': 'The Medina runs north toward the market.',
           's': 'The Common Square opens to the south.'})
R[5404] = dict(name='The Medina', desc="""
    The northern stretch of the Medina, between the market and the commons.
    Beggars sit against every wall, some of them old soldiers with no hands to
    hold out, and children work the crowd for dropped coin.  A board nailed to
    a post lists the names of the newly arrived.  The Market Square spreads out
    north and the Medina continues south.""",
    extras={'board names post': 'Names of families come in from the villages. Beside some of them, in another hand: "looking for" and another name.'},
    exits={'n': 'The crowded Market Square lies north.',
           's': 'The Medina runs south to the commons.'})
R[5410] = dict(name='The Common Square', desc="""
    Once a grassy field, the Common Square is trodden to bare earth by the
    refugees who sleep here when the city has no other room for them.  Smoke
    from cook-fires hangs low.  The river can be heard to the south, beyond
    the bridge and the South Gate.  Isvar Drive runs east and west along the
    water, and the Medina leads north.""",
    exits={'n': 'The Medina leads north toward the market.',
           's': 'The Southern Bridge crosses the Isvar.'})
R[5411] = dict(name='Outside The Southern Gate Of New Thalos', desc="""
    The road from the south ends here at the city's southern gate, between two
    squat towers hung with the banner of Thalos: a tower and a rising sun.  Carts
    queue on the verge to be searched before they may enter, and the guards on
    the wall watch the hills, not the carts.  To the south the Supply Road winds
    away through the hills; the gate leads north into the city.""")
R[5412] = dict(name='The Southern Bridge', desc="""
    A stone bridge over the River Isvar, its parapet carved with the names
    of the families who built it.  The water below runs fast and brown.  A
    ladder goes down from the bridge to the river for those who fish or wash.
    The South Gate lies south and the Common Square north.""",
    extras={'names parapet': 'Hundreds of family names, cut small. Many are the names of streets in Old Thalos, carried here like everything else.'})
R[5413] = dict(name='Inside The South Gate Of New Thalos', desc="""
    Two stone towers frame the South Gate, an iron gate hung on heavy hinges
    and stamped with the tower and rising sun of Thalos.  The builders of the new city
    spent on its walls what they did not have to spend on anything else, and
    it shows.  A guard keeps a tally of every wagon that goes out toward the
    front.  The bridge is north and the gate opens south.""")

# ====================================================================== market square
R[5405] = dict(name='Southern Market Square', desc="""
    The southern edge of the great Market Square, and the press of people here
    is a weight on the chest.  Stalls sell rope, lamp oil, salt, second-hand
    boots taken off the dead.  Hawkers cry prices that rise every week.  The
    square continues north, east and west, and the Medina leads off south.""")
R[5406] = dict(name='The Center Of Market Square', desc="""
    The heart of the Market Square, where the city's news is cried and its
    levies are read out.  A tall statue of a man with a lamp stands in the
    middle on a worn plinth, and people touch its foot as they pass.  The square
    spreads out in every direction.""",
    extras={'statue': 'The statue shows the Sultan who led the people out of Old Thalos, a sword in one hand and a lamp in the other, looking back over his shoulder. The foot of the statue is polished bright by a hundred years of hands.',
            'plinth': 'Cut into the plinth: "WE CAME OUT OF THE DARK. WE DO NOT GO BACK."'})
R[5407] = dict(name='Southeastern Market Square', desc="""
    This corner of the market belongs to soldiers and those who want to be
    soldiers.  Recruits from the levy compare blades they cannot afford, and
    hard-faced veterans home from the wall stand about not talking.  The
    armourer's shop is east and the weaponsmith's south; the square continues
    north and west.""")
R[5408] = dict(name='Southwestern Market Square', desc="""
    A quieter corner of the market, where the shopkeepers call softly to
    passers-by and nobody has much to spend.  The smell of hard bread drifts
    from the bread stand to the south, and the general store opens to the west.
    The square spreads out north and east.""",
    exits={'s': 'A small bread stand lies south.',
           'w': 'The general store is west.'})
R[5409] = dict(name='Western Market Square', desc="""
    The western side of the square is the townsfolk's end, where the old
    families of New Thalos buy what little the war leaves them.  A crier calls
    the names of the men chosen for this season's levy, and women stand very
    still listening.  West Main Street heads west toward the gate; the square
    fills the other directions.""")
R[5414] = dict(name='Northwestern Market Square', desc="""
    This corner of the market is cleaner than the rest, swept by the bank's
    own porters.  North is the shop of Ahkeem the tailor, whose cloth the city
    is known for, and west the doors of the Bank of New Thalos, where the war
    tithe is counted.  The square continues east and south.""")
R[5415] = dict(name='Northern Market Square', desc="""
    One of the busiest stretches of the city.  Palace servants push through to
    the stalls, and tithe-wagons bound for the warehouses rumble across the
    stones.  To the north Sultan's Walk runs toward the Palace and the inn; the
    market spreads east, west and south.""")
R[5416] = dict(name='Northeastern Market Square', desc="""
    Noise and blood.  The butchery to the east slaughters what the hill farms
    send in, and the gutters here run red into the drains.  Flies are
    everywhere.  Beside it, Vera's vegetable stall to the north is quiet by
    comparison.  The market continues south and west.""")
R[5417] = dict(name='Eastern Market Square', desc="""
    The eastern side of the market, where the square meets East Main Street.
    Every bargain made in New Thalos is made somewhere within a shout of here,
    and the tithe-collector's clerks take their share of each one.  East Main
    leads east toward the gate; the market spreads north, south and west.""")

# ====================================================================== sultan's walk / north gate
R[5418] = dict(name="Sultan's Walk", desc="""
    A cobbled road leading north from the market.  It is kept clear by the
    Sultan's guards, who move beggars on with the butts of their spears.
    North lies the way past the Palace and the Exile's Rest; south is the
    Market Square.""")
R[5419] = dict(name="Sultan's Walk", desc="""
    The road runs between the high wall of the Palace and the side of the
    Exile's Rest.  Through a small window in the inn's wall comes singing,
    always the same few songs of the old city.  The Walk continues north and
    south.""",
    extras={'window': 'A small thick-glassed window. Inside, a crowded room sings with its eyes closed.'})
R[5420] = dict(name="Sultan's Walk", desc="""
    The cobbles here are worn smooth by carts and boots.  West, the Palace
    gate stands open under guard, and now and then a horn sounds within to
    announce some lord or petitioner.  East is the door of the Exile's Rest,
    with its lamp burning in the niche.  The Walk runs north and south.""")
R[5421] = dict(name="Sultan's Walk", desc="""
    The northern end of Sultan's Walk, hemmed in by the Palace wall and the back
    of the inn.  Ahead the towers of the North Gate rise, and their guard is
    heavy: the mountains lie that way, and things have come down out of them
    before.  The Walk runs south toward the market.""")
R[5422] = dict(name='Inside The Northern Gate Of New Thalos', desc="""
    Two stone towers flank the North Gate, its iron leaves stamped with the
    tower and rising sun of Thalos and barred more often than not.  Guards on the wall
    look north toward the mountains and do not look down.  Sultan's Walk runs
    south, the Casbah follows the wall east and west, and the gate opens north
    into the wild.""")

# ====================================================================== west main
R[5423] = dict(name='Inside The West Gate Of New Thalos', desc="""
    Two towers set in the wall loom over the West Gate.  This is the gate the
    levies march out of, toward the Supply Road and Midgaard, and the stones
    in front of it are scratched with the names and marks of men who left.
    The Warriors' Guild lies south, Main Street heads east, and the gate opens
    west.""",
    extras={'names marks stones': 'Names, initials, a crude lamp, a crude tower. Some were scratched with a knife-point in a hurry. Few were ever scratched out again.'})
R[5424] = dict(name='West Main Street', desc="""
    West Main Street, the road of the levies.  To the north the broad steps of
    Temple Square climb toward the Temple of the Last Flame, and south the
    hammering of the repair shop never quite stops.  Main Street runs east and
    west.""")
R[5425] = dict(name='West Main Street', desc="""
    A foreman bawls at two labourers who are mending a hole in the road with
    rubble from a fallen house.  Narrow alleys run north and south behind the
    shops of the market.  Main Street continues east and west.""")
R[5426] = dict(name='West Main Street', desc="""
    The street runs between the back walls of the bank and the general store.
    To the west a work crew curses over the road; to the east the market roars.
    A poster is pasted to the wall of the store, half torn away and pasted over
    again.""",
    extras={'poster': 'The poster shows a heavy man in red robes holding up a lamp. Beneath it: "THE WALL IS FED BY YOUR TITHE. THE SULTAN THANKS YOU."'})

# ====================================================================== east main
R[5427] = dict(name='East Main Street', desc="""
    East Main, where the smell of the butchery meets the clang of the armourer's
    hammers.  Tithe-wagons wait here in a line for the road east.  The Market
    Square lies to the west and a junction to the east.""")
R[5428] = dict(name='East Main Street', desc="""
    A junction on East Main.  To the north Guildsman's Row begins, to the south
    a dark alley opens between the shops, and the street continues east and
    west.  A sign hangs across the junction on a wire.""",
    extras={'sign': 'The sign reads: "NO LOITERING. NO BEGGING. NO LIGHTS TO BE PUT OUT AFTER DARK. (By order of the Sultan of New Thalos.)"'})
R[5429] = dict(name='East Main Street', desc="""
    The Mercenaries' Guild stands on the south side of the street, and the men
    who lounge outside it watch everyone go by with an eye for what they are
    worth.  Opposite, to the north, the apothecary's door stands open, breathing
    out smoke and incense.  Main Street continues east and west.""")
R[5430] = dict(name='East Main Street', desc="""
    The eastern end of Main Street.  Braheem's magic shop leans over the road
    to the north, its windows crowded with scrolls.  The East Gate lies a short
    way east, and Main Street runs back west toward the market.""")
R[5431] = dict(name='Inside the Eastern Gate of New Thalos', desc="""
    The East Gate is the quietest of the four, hung between two towers built
    into the wall, and stamped with the tower and rising sun of Thalos like the rest.
    North of it stands the entrance to the Mages' Tower.  Main Street heads west
    toward the market and the gate opens east.""")

# ====================================================================== wharf road (stock Isvar Drive)
R[5432] = dict(name="Cassandra's Catch Of The Day", desc="""
    The fish market.  The smell is a wall.  Eels writhe in barrels, river carp
    lie in rows on wet slate, and a heap of salt fish waits to be packed in
    casks for the soldiers on the wall.  The fishwife watches you with a
    sailor's patience.  The door leads south to Isvar Drive.""")
R[5433] = dict(name='West Isvar Drive', desc="""
    The warehouse quarter at the western end of Isvar Drive.  Porters carry
    sacks of grain and bolts of cloth from the river boats into the warehouses,
    to be packed and sent to the front.  A clerk counts every sack.  A warehouse
    door opens north and the road leads east.""")
R[5434] = dict(name='West Isvar Drive', desc="""
    Dockworkers shoulder past with crates, in too much of a hurry to say sorry.
    The doors of the export warehouse stand open to the north, and the River
    Isvar slides by to the south.  Isvar Drive continues east and west.""")
R[5435] = dict(name='West Isvar Drive', desc="""
    The cobbles are wet and slick, running down toward the boat ramp to the
    south, and someone has bolted an iron rail along the wall for those who
    slip.  The shipwright's yard is north.  Isvar Drive continues east and
    west.""")
R[5436] = dict(name='West Isvar Drive', desc="""
    A cold wind comes off the river here and carries the shouting of the
    warehouse foremen from the west.  On the far bank there is nothing but
    reeds.  The Common Square opens to the east and Isvar Drive runs west.""")
R[5437] = dict(name='East Isvar Drive', desc="""
    Hammering and the hiss of hot iron come from the forge to the north, where
    the farrier shoes the horses that pull the tithe-wagons.  A thin boy watches
    you from a doorway and runs off.  The Common Square lies west and Isvar Drive
    continues east.""")
R[5438] = dict(name='East Isvar Drive', desc="""
    A plain stretch of Isvar Drive between the hay loft of the stables to the
    north and the river to the south.  Straw blows along the gutters.  The road
    runs east and west.""")
R[5439] = dict(name='East Isvar Drive', desc="""
    Wisps of hay on the cobbles mark the Royal Stables, north.  The Sultan's
    horses are kept there, and the couriers' mounts that carry word to and from
    Midgaard.  Isvar Drive continues east and west.""")
R[5440] = dict(name='East Isvar Drive', desc="""
    A back alley opens north between the buildings, and even at noon it is
    black as a well.  Drunken voices come out of it, and sometimes a cat
    screaming, and once in a while nothing at all, which is worse.  Isvar Drive
    runs east and west.""",
    exits={'n': 'The alley is black, and no light seems to go into it.'})
R[5441] = dict(name='East Isvar Drive', desc="""
    The smell announces the fish market, to the north, long before its door.
    Fishwives call the day's catch over the noise of the gulls.  The river runs
    alongside to the south, and Isvar Drive continues east and west.""")
R[5442] = dict(name='East Isvar Drive', desc="""
    The eastern end of Isvar Drive.  Gulls and crows squabble over heaps of
    refuse, and a stink rolls down from the dump to the north.  The river is
    clean enough here; the smell is all the city's.  A sign hangs over the dump
    gate.  The road leads back west.""",
    extras={'sign': 'Painted over an older sign: "THE DUMP OF NEW THALOS. Enter at your own risk. Burn nothing. Bury nothing. -- the Flame-wardens"'})
R[5443] = dict(name='The Boat Ramp', desc="""
    A sloping slab of stone leads down into the River Isvar.  Barges are
    moored along it, low in the water with grain from upriver, and their
    masters are off drinking in the wharf taverns.  The water laps at the foot
    of the ramp to the south, and Isvar Drive is north.""")

# ====================================================================== the casbah
R[5444] = dict(name='West Casbah', desc="""
    The western end of the Casbah, where the avenue under the wall stops.  The
    gate of the city jail stands to the south, and the narrow windows above it
    are barred.  A stair spirals up into the northwest tower.  The Casbah leads
    back east.""")
R[5445] = dict(name='West Casbah', desc="""
    Guards are thick on this end of the Casbah.  North, the city wall rises
    sheer; south, white steps climb between pillars to City Hall, where the
    ration rolls and levy lists are kept and where queues form before dawn.
    The Casbah runs east and west.""")
R[5446] = dict(name='The Casbah', desc="""
    Here the Palace wall bends away to the south, and a dark alley runs down
    beside it.  West are the steps of City Hall.  The Casbah runs on east under
    the city wall.""")
R[5447] = dict(name='The Casbah', desc="""
    Sentries walk the top of the wall overhead, their lanterns swinging.  To the
    south the Palace wall stands blank and high, with no windows on this side.
    The Casbah runs east and west.""")
R[5448] = dict(name='The Casbah', desc="""
    Cobbles run along the foot of the north wall.  Someone has chalked a lamp
    on the stones at head height, and under it a row of tally marks, one for
    each night the wall has held.  The North Gate is east and the Casbah runs
    west.""",
    extras={'lamp tally marks chalk': 'A chalked lamp and hundreds of tally marks in rows. The newest are fresh. Nobody admits to making them.'})
R[5449] = dict(name='The Casbah', desc="""
    The Casbah is busy here: messenger boys run between City Hall and the gate,
    and old scholars shuffle toward the library at the far end.  The towers of
    the North Gate stand just west, and the avenue continues east.""")
R[5450] = dict(name='The Casbah', desc="""
    The city wall towers over the road, and the sound of a whetstone on steel
    comes down from a big sentry who sits on the parapet staring north.  East is
    the crossing with Guildsman's Row; the North Gate is a short walk west.""")
R[5451] = dict(name='The Casbah', desc="""
    The crossing of the Casbah and Guildsman's Row, and the noise of the guilds
    rolls up from the south: hammers, saws, the stink of the tanners' vats, smoke
    from the bowyers' fires.  The Casbah continues east and west and the Row
    leads south.""")
R[5452] = dict(name='The Casbah', desc="""
    The avenue runs between the city wall and the back of the Masons' Guild.
    Nurses walk children here, where the wall is close and thick and the guards
    are near.  It is the safest street in the city, people say.  The Casbah runs
    east and west.""")
R[5453] = dict(name='The Casbah', desc="""
    Toward the northeast corner of the city the crowds thin.  Old men on sticks
    and young clerks with ink on their fingers are nearly the only ones who come
    this way, toward the library.  The Casbah runs east and west.""")
R[5454] = dict(name='The Casbah', desc="""
    The Casbah ends at the northeast corner of the wall and turns south into
    Lantern Row.  A spiral stair climbs into the northeast tower, where a lamp
    has burned every night since the wall was raised.  The avenue leads back
    west.""")

# ====================================================================== lantern row (stock Lantern Row)
R[5455] = dict(name='Lantern Row', desc="""
    A short street, newer than the rest, where every house hangs a lantern over
    its door.  The library is entered through a door to the west, and an old man
    plays chess on a bench outside it.  The Casbah lies north and the Row goes
    on south to the dance hall.""")
R[5456] = dict(name='Lantern Row', desc="""
    Lantern Row ends at the doors of the dance hall, west, where the city
    dances on feast nights as though it had nothing to remember.  On other
    nights the hall is used for the funerals of soldiers sent home.  The Row
    runs back north.""")

# ====================================================================== alleys
R[5458] = dict(name='Alley', desc="""
    A dark alley squeezed between the Palace wall and the side of City Hall.
    Rats and spiders, rubbish, a smell of damp.  Nobody comes here who has
    anywhere else to be.  The Casbah is north and the alley runs south.""")
R[5459] = dict(name='Alley', desc="""
    The alley ends against a blank wall.  Set into the cobbles is an iron
    manhole cover, scratched bright around its rim as if it is often lifted.
    The only other way is back north.""",
    exits={'d': 'An iron manhole covers an opening in the road.'})
R[5465] = dict(name='Alley', desc="""
    The alley off East Main is utterly dark.  Lamps carried into it go dim and
    blue and show nothing, and the city's people walk around it rather than
    through.  East Main Street is north; the alley goes on south.""")
R[5466] = dict(name='Alley', desc="""
    Darkness presses in, thick enough that the walls can only be found by
    touch.  Somewhere close a leather-worker's door stands to the west, and the
    alley goes on north and east.""")
R[5467] = dict(name='Alley', desc="""
    In the black of the alley a door leaks a little dirty light and the noise of
    drinking: the Smuggler's Inn, east.  The alley turns west and south.""")
R[5468] = dict(name='Alley', desc="""
    The darkness thins a little toward the south, where the alley comes out on
    Isvar Drive.  Something small skitters away underfoot.  The alley leads
    north into the black.""")
R[5469] = dict(name='Alley', desc="""
    A tight corner of the alley behind the temple, its walls rising north and
    west.  The dirt is churned with footprints, far more than such a place
    should see, and most of them lead east.  The alley runs east and
    south.""",
    extras={'footprint footprints prints': 'Many feet, bare and booted, all going east toward the dead end and none coming back the way they went.'})
R[5470] = dict(name='Alley', desc="""
    The alley dead-ends here.  The ground is worn smooth, and set in it is a
    small iron manhole.  The alley leads back west.""",
    exits={'d': 'A small iron manhole is set in the ground.'})
R[5471] = dict(name='Alley', desc="""
    A narrow alley between the temple and the bank.  The road crew's shouting
    comes from the south.  The ground is broken, and a pothole in the middle of
    it holds black water.  The alley runs north and south.""",
    extras={'pothole': 'Black water and rubble. A copper or two might have been lost in it once. They are gone now.'})
R[5472] = dict(name='Alley', desc="""
    A cramped alley between the repair shop and the general store, full of dust
    and rat droppings.  West Main Street is north and the alley leads
    south.""")
R[5473] = dict(name='Alley', desc="""
    A corner of the alley behind the warehouses and the Warriors' Guild.  There
    are scrapes on the cobbles leading west, as if something heavy is often
    dragged that way.  The alley runs north and east.""",
    extras={'scrapes scrapings': 'Long scrapes on the stones that run up to the guild wall to the west and stop dead.'})
R[5474] = dict(name='Alley', desc="""
    The alley ends here, and so do the footprints in the dust.  A round iron
    plate is set into the ground.  The alley leads back west.""",
    exits={'d': 'A round iron manhole is set into the ground.'})

# ====================================================================== the underground
R[5457] = dict(name='Underground', desc="""
    A cramped tunnel of old brick beneath the city, older than New Thalos
    itself, its builders unknown.  Water drips.  It runs north and south.""")
R[5475] = dict(name='Underground', desc="""
    A small passage beneath the city, low enough to stoop in.  A thin grey
    glint of daylight shows around the manhole overhead.  The passage runs
    south.""")
R[5476] = dict(name='Underground', desc="""
    The tunnel walls sweat in the dark and the floor is slick with grey mud.
    Faint scratches on the brick might be words.  The passage runs north and
    south.""")
R[5477] = dict(name='Underground', desc="""
    The tunnel branches here into three: north, east and west.  Someone has
    marked each way with a smear of soot shaped like a little flame.""")
R[5478] = dict(name='Underground', desc="""
    The tunnel bends here, south and west.  A small glint of light shows
    around the manhole above, and a heap of old rags in the corner looks
    as though someone has been sleeping on it.""")
R[5479] = dict(name='Underground', desc="""
    The passage stops at a wall of dressed stone, finer than the brick of the
    tunnel.  From beyond it, very faintly, comes chanting.  The dust on the
    floor before the wall has been swept clean, though no door can be seen.
    The way back is east.""")
R[5480] = dict(name='Underground', desc="""
    The tunnel narrows until it brushes both shoulders.  Somewhere water runs
    in a pipe, and the brick is furred with pale mould.  The passage runs
    north and south.""")
R[5481] = dict(name='Underground', desc="""
    The passage turns here, north and east.  Through the manhole overhead come
    muffled sounds of the city: wheels, voices, a dog, a bell.  Down here they
    sound very far away.""")
R[5482] = dict(name='Underground', desc="""
    A long brick tunnel running east and west, its roof sagging in places and
    shored with timber.  It would be easy to lose the way down here.""")
R[5492] = dict(name='Underground', desc="""
    The tunnel runs on east and west.  The bricks here are blackened, as though
    a fire once burned along the whole passage.""")
R[5493] = dict(name='Underground', desc="""
    East and west the tunnel goes on.  A rotted lantern hangs on a nail, empty,
    and below it someone has scratched a lamp into the brick.""")
R[5500] = dict(name='Underground', desc="""
    The brick gives way to raw earth held up with planks.  This part was dug
    later, and in a hurry.  The passage runs east and west.""")
R[5501] = dict(name='Underground', desc="""
    A tunnel of packed earth and old planking.  Roots hang from the roof, so
    this must run beneath the wall itself.  It goes east and west.""")
R[5502] = dict(name='Underground', desc="""
    The earthen tunnel runs east and west, and the air smells of the open
    country.  Tool marks show in the walls, shovels and picks, by many
    hands.""")
R[5488] = dict(name='A Dark Passage', desc="""
    A small hand-dug passage that ends in a wall of earth to the west.  The
    wall looks wrong somehow, too smooth, but nothing can be found in it.  The
    only way on is east.""")
R[5489] = dict(name='A Dark Passage', desc="""
    The passage runs east and west.  The north wall has the same wrong
    smoothness, though searching it finds nothing, and through it, faintly,
    come voices.""")
R[5490] = dict(name='A Dark Passage', desc="""
    A great boulder half blocks the passage, and the tunnel squeezes past it to
    the east and west.  Something round has been bored into its face.""",
    extras={'boulder': 'A huge boulder, older than the tunnel. In its centre someone has carved a perfectly round hole.'})
R[5491] = dict(name='A Dark Passage', desc="""
    The passage ends.  In a niche a small fire burns that gives heat but does
    not move or flicker.  A short ladder lies half buried in the dirt, and
    above it a square of boards is set into the roof.  The way back is
    west.""",
    extras={'fire': 'The flames are frozen in place. They still give off heat, but they do not burn. Beside the niche is a small hole about the size of a piece of charcoal.',
            'ladder boards roof': 'A short ladder that reaches the boards in the roof. They look as though they could be pushed up.'})

# ====================================================================== the river within the walls
R[5483] = dict(name='River Isvar', desc="""
    The river runs up against an iron grating set in the eastern wall.  High
    above, guards look down to see whether you mean to leave the city by water;
    only they can raise it.  The reek of the dump drifts down from the north
    bank.  The river flows west back into the city.""")
R[5484] = dict(name='River Isvar', desc="""
    The slow current carries everything east.  Up on Isvar Drive people walk
    along the bank and do not look at the water.  West is the southern bridge;
    east is the iron grating that shuts the river off from the country.""")
R[5485] = dict(name='River Isvar', desc="""
    The river passes under the southern bridge, and every splash echoes off the
    stone.  A ladder bolted to the pier climbs up to the bridge.  The water
    runs on east and west.""")
R[5486] = dict(name='River Isvar', desc="""
    The busiest stretch of the river, crowded with moored barges from the boat
    ramp to the north.  Ropes cross the water at head height.  East, the
    southern bridge spans the river; it runs on west.""")
R[5487] = dict(name='River Isvar', desc="""
    The river comes into the city here, through a huge iron grating in the
    western wall.  Guards watch from the wall above and open it only on an
    order.  Weed and worse hang from its bars.  The river flows east.""")

# ====================================================================== guildsman's row
R[5460] = dict(name="Guildsman's Row", desc="""
    Guildsman's Row is nearly as loud as the market.  Every guild of the city's
    working folk has its hall along it, and whatever the front needs is made
    here.  On this stretch the bowyers and fletchers are west and the masons
    east.  The Row runs south and the Casbah lies north.""")
R[5461] = dict(name="Guildsman's Row", desc="""
    Bolts of grey cloth are carried out of the Weavers' Guild, west, faster than
    they can be woven; the Craftsmen's Guild opposite, east, rattles with
    saws.  The Row continues north and south.""")
R[5462] = dict(name="Guildsman's Row", desc="""
    The Tanners' Guild opens to the west, its vats making the air sting.  To the
    east a carved marble door leads into the Hall of the Saints, and people
    take off their caps as they pass it.  The Row runs north and south.""")
R[5463] = dict(name="Guildsman's Row", desc="""
    When the guilds were built there was a little ground left over, and on it
    the city raised the Hall of the Saints to those who brought it out of Old
    Thalos.  Its door is east.  The Row runs north and south.""")
R[5464] = dict(name="Guildsman's Row", desc="""
    The southern end of the Row is cramped and worn down by apprentices running
    goods from the guilds to the market shops.  The guildhalls lie north and
    East Main Street south.""")

# ====================================================================== temple of the last lamp
R[5503] = dict(name="Clerics' Sanctum", desc="""
    A silent room at the foot of the stair below the clerics' bar, lit by a
    single lamp lit from the Last Flame itself.  The master of the clerics waits
    here to teach those who are ready.  No one speaks above a whisper.  The
    stair leads back up.""",
    exits={'e': 'The floor at the foot of the eastern wall has faint scratches in it.'})
R[5504] = dict(name='The Chamber Of The High Priest', desc="""
    The plain cell of the High Warden of the Flame, the holiest man in the city
    and the Sultan's counsellor in all matters of faith.  A cot, a prayer stool,
    a lamp.  He is known for his temper, and he does not like to be interrupted
    at prayer.  The only exit is south.""")
R[5505] = dict(name='By The Altar', desc="""
    The northern end of the temple.  On an altar of black onyx burns the altar
    fire, kindled from the Last Flame in the Sultan's shrine and never once let
    go out.  Two wardens tend it at all hours.  Behind the altar rises a tall
    statue of the first Flame-keeper, who carried the fire out on the Night of
    Leaving.  The nave lies south.""",
    extras={'statue keeper': 'The first Flame-keeper is carved as a thin, ragged woman shielding a small flame with her hands, looking back over her shoulder at something behind her.',
            'fire flame altar': 'A small, steady, very bright flame in a bowl on black onyx. The wardens never let anyone else closer than arm\'s length.'})
R[5506] = dict(name="The Weavers' Guild", desc="""
    Bales of raw wool and flax from the hill farms are stacked to the roof, and
    rows of looms clatter without rest.  Most of the cloth is grey: cloaks and
    blankets for the soldiers on the wall.  A boy comes in, takes an armful of
    it, and goes out.  The Row is east.""")
R[5507] = dict(name="The Craftsmans' Guild", desc="""
    A crowded workshop where carpenters, wheelwrights and coopers work elbow to
    elbow, building carts, barrels and spear-shafts for the front.  Everyone is
    behind and everyone is shouting.  The Row is west.""")
R[5508] = dict(name='Inside The Temple', desc="""
    A side aisle of the temple, plainer than the nave but kept spotless.  To the
    north is the High Warden's door, with a notice on it in large letters.  The
    entrance to the clerics' guild is south and the nave lies east.""",
    extras={'notice door': 'In large letters: "AT PRAYER. DO NOT DISTURB."'})
R[5509] = dict(name='Inside The Temple', desc="""
    The nave of the Temple of the Last Flame.  Marble pillars rise to a dark
    roof, and between them carvings show the flight from Old Thalos: the towers
    burning, the long road, the saints with their lamp.  Rows of benches face the
    altar.  Hundreds of small lamps burn along the walls, one for every family
    in the city, a black flame painted on those whose people are dead.  The altar is north, the donation room east, a side aisle west
    and the gates south.""",
    extras={'carvings pillars': 'The carvings are worn smooth where people have touched them. In the last panel a great darkness stands behind the city, with no face.',
            'lamps': 'Each small lamp has a family\'s name scratched on its base. A few have gone cold, and nobody has taken them down.'})
R[5510] = dict(name='The Donation Room', desc="""
    A bare side room built in the hungry years, when the city first filled with
    refugees.  Whatever is given here goes to those who arrive with nothing,
    and a warden's curse goes with anyone who takes more than they need.  The
    nave lies west.""")
R[5511] = dict(name='The Museum Of The Greater Gods', desc="""
    The northern half of the Hall of the Saints, where four tall statues stand
    in the lamplight.  The people of New Thalos raised them to the saints who
    led them out of the dark, and to the dark itself, so that none of it would
    be forgotten.  The hall continues south and the Row is west.""")
R[5516] = dict(name='The Museum Of The Greater Gods', desc="""
    The southern half of the Hall of the Saints.  Four more statues stand here,
    and the floor before them is scattered with dry flowers and small clay
    lamps left by the faithful.  The hall continues north and the Row is
    west.""")
R[5512] = dict(name='The Entrance To The Guild of Clerics', desc="""
    The guild hall of the temple's clerics, low and plain.  Shaven-headed
    novices in grey robes talk quietly in pairs before they are sent out to the
    commons or to the front.  The temple proper is north and the clerics' bar
    south.""")
R[5513] = dict(name='The Temple Gates', desc="""
    Two wrought iron gates stand open before the Temple of the Last Flame.
    They were made to be shut, and the wardens drill at shutting them: the
    city has seen what happens to a temple that is taken.  The nave is north,
    and the steps lead down south to Temple Square.""")
R[5519] = dict(name='Nectar Of The Gods', desc="""
    The clerics' bar is warmer and softer than anything else in the temple, the
    one comfort the order allows itself after nights with the dying.  Cushions,
    low tables, weak wine.  In the corner a stair goes down to the meditation
    chambers.  The guild entrance is north.""")
R[5520] = dict(name='Temple Square', desc="""
    A wide paved square before the temple steps, where preachers stand on boxes
    and the faithful gather.  Each evening the wardens bring fire from the altar
    down these steps to light the city's street lamps.  The steps climb north
    to the temple gates and West Main Street is south.""")

# ====================================================================== shops and guilds off the market / main
R[5514] = dict(name="Ahkeem's Stuff", desc="""
    A tailor's shop thick with incense smoke, its walls hung with bolts of
    patterned cloth such as the old city used to weave, before.  Ahkeem keeps
    the old patterns alive, and charges for it.  The door is south.""")
R[5515] = dict(name="Vera's Veggies", desc="""
    A busy stall of onions, beans, turnips and roots from the hill farms, never
    enough of any of them.  Customers haggle over every bunch.  Vera herself is
    the kind of woman who looks at you as if you have not been eating properly.
    The market is south.""")
R[5521] = dict(name='The Bank', desc="""
    A tall hall of black marble and faded red hangings, the one grand room
    left in the city outside the Palace.  Dwarven masons cut its trim long
    ago.  Clerks count the war tithe at long tables behind a rail, and guards
    watch the clerks.  The market is east.""")
R[5522] = dict(name='The Butchery', desc="""
    The butchery stinks of blood.  Carcasses hang on hooks over catch-pans, and
    the pans drain into a vat set in the floor.  Most of the meat is salted and
    packed in barrels for the wall.  The market is west.""",
    extras={'vat': 'A deep stone vat, dark and wet. Something down there moves the surface, now and then. Probably rats.'})
R[5523] = dict(name="The Witch's Brew", desc="""
    The apothecary is lit by hundreds of candles on crowded shelves, and a low
    mist of herb-smoke curls about the floor.  Jars of salve and bottles of
    draughts line the walls, most of them meant for wounds.  A cluttered table
    stands against the far wall.  The door is south.""")
R[5524] = dict(name="Braheem's Magic Shop", desc="""
    A cramped shop of bookshelves and heaps of scrolls.  Its owner hunches over
    his latest work, muttering.  A small sign hangs on the wall.  The street is
    south.""",
    extras={'sign': 'The sign reads: "BRAHEEM\'S. LIST - see my creations. VALUE - learn their worth. SELL - rid yourself of magic you dare not keep. BUY - rid yourself of coin. Nothing taken from the west will be bought."'})
R[5525] = dict(name="The Entrance To The Mages' Tower", desc="""
    A small, poorly lit hall whose only purpose is to hold the sorcerer who
    guards it.  The war-magi of the city train beyond, before the High Tower
    sends them west.  The courtyard lies north and the gate street south.""")
R[5526] = dict(name='The Entrance To The Guild of Warriors', desc="""
    A cramped guardroom at the door of the Warriors' Guild, where levy
    recruits give their names before they are drilled.  It keeps the unwanted
    out.  The West Gate is north and the guild's tavern south.""")
R[5527] = dict(name='The Repair Shop', desc="""
    A workshop heaped with dented helms and split shields sent back from the
    wall.  One man used to mend it all single-handed; now the work has grown
    past him.  A sign stands on the counter.  West Main Street is north.""",
    extras={'sign': 'The sign reads: "Closed. Too much to mend."'})
R[5528] = dict(name='The General Store', desc="""
    The general store sells what a soldier or a refugee needs to stay alive:
    lamp oil, candles, rope, sacks, waterskins.  Everything is dear and nothing
    is new.  The market is east.""")
R[5529] = dict(name="Abdul's Armour", desc="""
    The armoury rings with hammering.  Boys run with buckets of water and coal,
    and dwarves at the back beat out plates faster than the eye can follow.
    The walls show Abdul's best work, made for officers who can pay.  A note is
    pinned to the wall.  The market is west.""",
    extras={'note': 'The note reads: "LIST: what is for sale. VALUE: what I will give. SELL: sell to Abdul. BUY: Abdul\'s favourite word. Armour for the wall goes first."'})
R[5530] = dict(name="The Mercenaries' Guild", desc="""
    The Mercenaries' Guild is despised by the city and used by it all the same.
    Those who will not or cannot fight their own battles come here, and those
    who would rather be paid than levied wait to be hired.  For a fee, a sword
    can be bought.  East Main Street is north.""",
    exits={'e': 'There are small scratches in the floor beside the eastern wall.'})
R[5531] = dict(name='The Mercenaries Guild', desc="""
    A windowless back room where the hired swords wait until someone pays for
    them.  Bedrolls, dice, the smell of oil and old sweat.""")
R[5532] = dict(name="Entrance To The Thieves' Guild", desc="""
    A small dark room lit by one torch in a bracket.  There is a bench and a
    book lying on it.  The cut-throat who guards the door against outsiders
    stands up as you come in.  A passage leads south.""",
    extras={'book': 'A ledger of debts owed, in a cipher. Some entries are written in another hand, and marked with a small black eye.'})
R[5533] = dict(name='The Whet Stone', desc="""
    The tavern of the Warriors' Guild, full of big men with big swords and
    big cups, many of them back from the wall and not right.  The tables are
    gouged from old brawls.  It is a good place to keep quiet.  The practice
    yard is east and the guild entrance north.""")
R[5534] = dict(name='The Tournament And Practice Yard', desc="""
    A yard of trampled grass full of straw dummies and sweating recruits, drilled
    hard and sent to the Supply Road in batches.  The master, in black robes
    among the iron, watches from the edge.  The tavern is west.""",
    exits={'e': 'The grass near the base of the eastern wall is slightly torn.'})
R[5535] = dict(name='The Bread Stand', desc="""
    A small stand under a patched awning, with a few trays of dark ration bread
    and hard biscuit.  The baker has chalked up a list, and the prices on it
    have been rubbed out and raised more than once.  The market is north.""",
    extras={'list': 'Bread, biscuit, oatcake. The prices have been changed four times.'})
R[5536] = dict(name="Igor's Implements Of Destruction", desc="""
    Swords, axes and spears hang on pegs around the walls, and a dwarf with a
    hunched back works at a bench in the back of the shop.  He makes the rarer
    blades, the ones that cost a year of pay.  A note is pinned up near the
    door.  The market is north.""",
    extras={'note': 'The note simply reads: "READ THE NOTE IN THE ARMOURY. -- Igor."'})
R[5537] = dict(name='Ye Old Leather Shoppe', desc="""
    A leatherworker's shop off the black alley, lit by a single lamp.  Racks of
    belts, straps and jerkins crowd the walls, and women sit on cushions
    stitching harness for the army's horses.  The alley is east.""")
R[5538] = dict(name="Smuggler's Inn", desc="""
    A filthy drinking den that has not been cleaned in years.  Card tables line
    the walls, everyone stops talking when the door opens, and the bar is pitted
    with knife holes.  What comes in here comes in without paying the tithe.
    The bartender waits.  The alley is west.""")
R[5539] = dict(name='The Filthy Unicorn', desc="""
    A cold draught moves through the room though there is no window.  Hooded
    figures talk in low voices in the corners, and steel flashes now and then.
    It would be wise to check your purse.  A narrow stair leads down; the door
    to the north leads out.""")
R[5540] = dict(name='The Warehouse', desc="""
    The export hall of the warehouses, stacked with sealed crates and sacks
    stencilled with the tower and sun of Thalos.  Grain, cloth, salt fish, arrows:
    everything here goes to the front.  The other hall is east and Isvar Drive
    south.""")
R[5541] = dict(name='The Warehouse', desc="""
    Clerks walk among the stacks counting and writing.  This hall stores the
    raw stuff brought in from upriver and the hill farms before it goes out to
    the guilds.  The export hall is west and Isvar Drive south.""")
R[5542] = dict(name='The Shipwright', desc="""
    The floor creaks, soaked by years of river water.  An old man with a curly
    grey beard stands behind a small counter, and behind him hang model barges
    and a great dried river fish.  A drafting room opens east and Isvar Drive is
    south.""")
R[5543] = dict(name='The Drafting Room', desc="""
    Sketches of hulls cover every wall, pinned over one another: barges, flat
    river boats, one tall ship that was never built.  The shipwright draws each
    boat here before a single plank is cut.  The shop is west.""")
R[5544] = dict(name='The Forge', desc="""
    The farrier's forge, hot as an oven.  Horseshoes, bits and wagon fittings
    hang from the walls.  The tithe-wagons go west on iron from this anvil, and
    the smith never seems to stop.  Isvar Drive is south.""")
R[5545] = dict(name='The Royal Stables', desc="""
    The Sultan's stables.  A few fine horses remain from the herds that came out
    of Old Thalos; the rest of the stalls hold couriers' mounts and wagon
    horses.  A boy comes by with a shovel.  The hay loft is east and Isvar Drive
    south.""")
R[5546] = dict(name='The Secret Yard', desc="""
    A hidden yard known to few in New Thalos, walled in and roofed with
    sacking.  Here thieves are taught to pick locks, cut purses and vanish.  A
    narrow stair climbs back up to the Unicorn.""",
    exits={'s': 'There are small scratches in the wall to the south.'})
R[5547] = dict(name='The Dump', desc="""
    The city's refuse heap, steaming in the cold.  Wind off the mountains blows
    most of the smell over the wall and out across the hills.  The wardens
    forbid anything to be buried here.  Isvar Drive lies south.""")
R[5548] = dict(name="The Mage's Laboratory", desc="""
    The top of an old stone tower, crowded with potions, scrolls and wands in
    no order at all.  The master of the war-magi sits hunched over a little
    table with two flasks bubbling before him, and looks up with a broad smile.
    A stair leads down.""")
R[5549] = dict(name='The Hay Loft', desc="""
    A cramped loft over the stables, stacked with hay for the horses.  The
    stable boy sleeps up here in a nest of straw, with a lamp he is not allowed
    to light.  The stables are west.""")
R[5517] = dict(name='The Base Of The Tower', desc="""
    A cold room whose only feature is an old wooden stair spiralling up the wall.
    Up there, they say, the master of the war-magi will teach those worth
    teaching.  The courtyard is east.""",
    exits={'s': 'There are small scratches on the floor near the base of the southern wall.'})
R[5518] = dict(name="The Mages' Courtyard", desc="""
    A small tiled courtyard with a dry fountain in the middle and four iron
    benches where young magi sit and argue over the West.  A two-storey tower
    stands to the west, where the master works.  The entrance hall is
    south.""")

# ====================================================================== mobs
M[5400] = mob('the guildmaster', 'guildmaster mage master', 'The master of the war-magi stands here.',
              'An old man in a scorched robe peers at you over a heap of ancient books, as if measuring how long you would last on the wall.')
M[5401] = mob('the guildmaster', 'guildmaster cleric master warden', 'The master of the Flame-wardens stands here.',
              'An old man in grey robes kneels by a single lamp. His eyes are red from years of night vigils.')
M[5402] = mob('the guildmaster', 'guildmaster warrior master', 'The master of the drill-yard stands here.',
              'A small, hard man in black robes waits to train you. He has sent a great many recruits to the wall, and he remembers them.')
M[5403] = mob('the guildmaster', 'guildmaster thief master', 'The master of the yard stands here in the shadows.',
              "A small man dressed in black rests in the corner. As you enter he throws a knife that lands in the wall by your ear. 'We will now begin,' is all he says.")
M[5404] = mob('the receptionist', 'receptionist woman', 'A veiled woman greets you from behind the desk.',
              'A tired young woman, veiled in the Thalos fashion, keeps the ledger of beds. A small moon-shaped birthmark shows on her cheek above the veil.')
M[5405] = mob('the old withered man', 'bartender man mage old', 'An old withered man leans against the bar.',
              'An old mage who came out of Old Thalos as a child. He pours five cups at once without touching the jug and does not seem to see any of them.')
M[5406] = mob('Brother John', 'john brother singer', 'Brother John stands on the stage, singing the old songs.',
              'A thin man with a fine voice who sings the songs of Old Thalos every night, the same few songs, and weeps at the same verses every time.')
M[5407] = mob('the panhandler', 'panhandler refugee', 'A panhandler sits here with his hand out.',
              'A skinny man in a blanket, newly come from some village nobody will ever go back to.')
M[5408] = mob('the panhandler', 'panhandler refugee', 'A panhandler sits here, staring at your clothes.',
              'A thin man with an old soldier\'s brand on his arm. He is very interested in your boots.')
M[5409] = mob('the beggar', 'beggar', 'A grubby beggar sits in the filth.',
              'A filthy, hollow-cheeked soul who has been begging so long he has forgotten what he was before.')
M[5410] = mob('the baker', 'baker', 'The baker stands behind his trays, counting loaves.',
              'A big man in an apron white with flour. He bakes for the wall first and the city second, and both go hungry.')
M[5411] = mob('the shopkeeper', 'shopkeeper storekeeper', 'The shopkeeper stands behind the counter.',
              'A half-elf on a high stool behind the counter, with an eye for coin and a slate of what he has left.')
M[5412] = mob('the banker', 'banker clerk', 'A banker waits to help you.',
              'A small halfling with ink-stained fingers who counts the war tithe and dreams of it in his sleep.')
M[5413] = mob('Ahkeem the tailor', 'ahkeem tailor', 'Ahkeem the tailor welcomes you to his shop.',
              'A middle-aged man in a coat of the old Thalos weave. He looks you over with disdain and suggests a new wardrobe.')
M[5414] = mob('Vera the vegetable seller', 'vera lady seller', 'Vera beams at you over her stall of roots and onions.',
              'A tall, thin woman with dirt under her nails and a broad smile. She feeds half the street on credit and pretends she does not.')
M[5415] = mob('Butch the meatcutter', 'butch meatcutter butcher', 'Butch the meatcutter stands here in his bloodied apron.',
              'A stocky dwarf with a mad glint in his eye, twirling his cleaver into the air and catching it without looking.')
M[5416] = mob('Abdul the armourer', 'abdul armourer armorer', 'Abdul stands here, waiting to help you.',
              'Abdul returns your gaze with a steady, cold eye. Half the officers on the wall wear his plate.')
M[5417] = mob('Igor the weaponsmith', 'igor weaponsmith smith', 'Igor stands here, fussing over a blade.',
              'A small dwarf with a great hump on his left shoulder and burn scars up both arms.')
M[5418] = mob('Cassandra', 'cassandra fishwife fishmonger', 'Cassandra stands proudly over her catch.',
              'A cheerful weather-worn face, lined by years on the river. Only a lifetime of fish lets her bear the smell.')
M[5419] = mob('the foreman', 'foreman man', 'The foreman stands here shouting at the workers.',
              'A worried dwarf who keeps making notes in a book and glancing at the sky, as if the dark might come early.')
M[5420] = mob('the construction worker', 'worker labourer construction', 'A labourer is mending the road.',
              'A big sweating refugee working off his family\'s ration debt. He does not look up.')
M[5421] = mob('the statue of Saint Oren', 'statue oren saint', 'The statue of Saint Oren the Warder stands here.',
              'A marble statue of Saint Oren, sword raised, striking down a hollow-faced king. Wards are cut into its base, and they hum faintly.')
M[5422] = mob('the statue of the Hollow King', 'statue hollow king', 'The statue of the Hollow King stands here.',
              'A statue of the shape the darkness wore when it came to Old Thalos: a crown on an empty face. It was made to be struck down by Saint Oren, forever.')
M[5423] = mob('the statue of Saint Ulme', 'statue ulme saint', 'The statue of Saint Ulme stands here.',
              'Saint Ulme rides a great tusked beast with children clinging to its back, carved as she led them out of the burning city.')
M[5424] = mob('the statue of the Grey Warden', 'statue grey warden', 'The statue of the Grey Warden stands here.',
              'A cowled figure with a ledger, the warden who counts the dead. Its robe is covered in strange runes that nobody can read.')
M[5425] = mob('the statue of Saint Ilsa', 'statue ilsa saint', 'The statue of Saint Ilsa of the Dawn stands here.',
              'Saint Ilsa, who held the gate until the sun came up, carved holding up her hands. The marble seems to glow faintly, as if warm.')
M[5426] = mob('the statue of the Mourning Sultana', 'statue mourning sultana queen', 'The statue of the Mourning Sultana stands here.',
              'A sultana of Old Thalos in black marble covered with silver runes, her face hidden in her hands. It was she who opened the gate, they say, on the Night of Leaving.')
M[5427] = mob('the statue of Saint Teodor', 'statue teodor saint', 'The statue of Saint Teodor the Scribe stands here.',
              'A stooped scholar in weathered marble, writing on a tablet. He wrote down the fall of Old Thalos so that none of it would be lost.')
M[5428] = mob('the statue of Saint Perrin', 'statue perrin saint', 'The statue of Saint Perrin of the Road stands here.',
              'A worn, dusty statue of a pilgrim with a staff. It was dragged all the way from Old Thalos on the exodus road, and looks it.')
M[5429] = mob('Aziz', 'aziz deserter human', 'Aziz the deserter stands here in the dark.',
              'A big, burly man in a stripped levy coat. He ran from the wall, and he grins as he draws his sword.')
M[5430] = mob('Mustafah', 'mustafah robber human', 'Mustafah the robber stands here.',
              'A lithe man with an evil smirk who robs the families who come in by the south gate.')
M[5431] = mob('Fatima', 'fatima elf invoker witch', 'Fatima the elven hedge-witch stands here.',
              'A dusky-skinned elf with black hair, expelled from the war-college for what she tried to learn.')
M[5432] = mob('Kareem', 'kareem dwarf mercenary', 'Kareem the dwarven sell-sword stands here.',
              'A short stocky fellow with a chest the girth of a barrel, who has sold his axe to every side of every quarrel.')
M[5433] = mob('the caravan trader', 'trader merchant nomad caravan', 'A caravan trader looks you over.',
              'A robust fellow with a ready smile who brings goods in from the hills without paying the tithe. Something tells you not to trust him far.')
M[5434] = mob("the Sultan's bodyguard", 'bodyguard guard', 'A bodyguard sizes you up.',
              'A big half-orc who glances you over and goes back to watching the doors. He has been the Sultan\'s shadow for twenty years.')
M[5435] = mob('the skinny kid', 'kid thief', 'A skinny kid wanders around.',
              'A small orphan of the commons who sees you looking at him and quickly looks away.')
M[5436] = mob('the dockworker', 'dockworker porter', 'A strong dockworker walks by moving crates.',
              'A hulking man who carries grain sacks from the barges as if they were full of feathers.')
M[5437] = mob('the tithe-collector', 'collector taxcollector man tithe', 'A small man walks around scribbling in a ledger.',
              'The Sultan\'s tithe-collector, who goes from shop to shop taking the wall\'s share. Nobody in the city is glad to see him.')
M[5438] = mob('Gorran', 'gorran rogue gord', 'Gorran the rogue stands here.',
              'A lean rogue in a patched cloak, who walks the streets as if he owned them and keeps one hand near his knife.')
M[5439] = mob('Ser Corvane', 'corvane knight captain ser', 'Ser Corvane, heir of the last captain of Old Thalos, stands here.',
              'A big, grey-bearded knight who carries his grandfather\'s spear, the one that held the gate on the Night of Leaving. He does not seem surprised by your approach and looks at you curiously.')
M[5440] = mob('Master Orsin', 'orsin magus master', 'Master Orsin the war-magus stands here.',
              'A war-magus of the High Tower in long brown robes, here to choose students for the wall. His gaze goes right through you.')
M[5441] = mob('Fenn Greenleaf', 'fenn greenleaf halfling', 'Fenn Greenleaf stands here.',
              'A halfling scout with a sling and a bag of stones, back from the hills and in no hurry to go out again.')
M[5442] = mob('the doomsayer', 'doomsayer man prophet', 'A small grey-haired man walks around shouting about the West.',
              'A ragged old preacher who stands on corners crying that the dark that ate Old Thalos is coming back. Some people listen more than they admit.')
M[5443] = mob('the alley cat', 'cat alley', 'A small, starved cat searches for food.',
              'A thin grey cat, all ribs and eyes.')
M[5444] = mob('the vulture', 'vulture bird', 'A vulture circles above you.',
              'A great bald-headed bird that follows the burial carts. The only thing it wants is a corpse.')
M[5445] = mob('the old man', 'man old', 'An old man sits here playing chess.',
              'An old man who remembers his grandfather\'s stories of the old city. He is very intent on winning.')
M[5446] = mob('Lorcan the Librarian', 'librarian lorcan', 'Lorcan the Librarian sits behind a desk.',
              'A huge, hulking man who keeps the last books of Old Thalos, and rises slowly whenever someone asks him a question.')
M[5447] = mob('the dirt devil', 'devil dirt dust', 'The wind kicks up some dust.',
              'A small whirl of grit and wind, a young air spirit loose on the hills.')
M[5448] = mob('the lamia', 'lamia beast', 'A lamia waits here for her next meal.',
              'A creature with the upper body of a beautiful woman and the lower body of a four-legged beast. She preys on refugees on the road, and licks her lips as she looks at you.')
M[5449] = mob('the hollow-eyed wanderer', 'wanderer madman', 'A ragged, hollow-eyed wanderer stands here.',
              'A refugee who went back to look for someone in the west and came back wrong. He does not sleep, and he does not like the living.')
M[5450] = mob('the Sultan', 'sultan', 'The Sultan sits here on his throne.',
              'A heavy, frightened man in faded red robes, last of the old Thalan line. He has sold most of his palace treasure to pay the tithe to the wall, and he smiles at you the way he smiles at everyone who might be useful.')
M[5451] = mob('a lady of the court', 'lady girl court', 'A veiled lady of the Women\'s Court stands here.',
              'A dark-eyed woman of the Sultan\'s household in faded silks and a pale blue veil, sewing shrouds for the wall. Her loyalty to the Sultan is unwavering.')
M[5452] = mob('the jailer', 'jailer', 'The jailer sleeps here, snoring loudly.',
              'A pathetic soul, probably some nobleman who fell out of favour and was given the keys to the dungeon as punishment.')
M[5453] = mob('a chamber guard', 'guard chamber eunich eunuch', 'A chamber guard stands watch over the court.',
              'A huge silent man whose only duty is to guard the Women\'s Court of the Palace.')
M[5454] = mob('Nahrin, the Sultan\'s favourite', 'nahrin favourite favorite girl nichole', 'Nahrin, the Sultan\'s favourite, rests on a mound of pillows.',
              'The loveliest woman in the Palace, and the one with a knife hidden in her pillows. She is about to use it.')
M[5455] = mob('the Keeper of the Last Flame', 'keeper flame guardian', 'The Keeper of the Last Flame stands here, wreathed in pale fire.',
              'A tall figure of pale, steady fire in the shape of a cowled woman. It has guarded the flame since the Night of Leaving, and it will not suffer the dark near it.')
M[5456] = mob('the guildguard', 'guildguard mage guard', 'The guard of the Mages\' Tower stands here.',
              'A war-magus in mail with wards stitched into his sleeves. You would not want to test either.')
M[5457] = mob('the guildguard', 'guildguard cleric guard', 'The guard of the Flame-wardens stands here.',
              'A broad warden with a mace and a lamp. He looks like he has buried a lot of people.')
M[5458] = mob('the guildguard', 'guildguard warrior guard', 'The guard of the Warriors\' Guild stands here.',
              'A scarred veteran of the wall, built like a gatepost. You would not want to mess with him.')
M[5459] = mob('the guildguard', 'guildguard thief guard', 'The guard of the thieves stands here.',
              'A thief dressed in black, who stands as you enter and steps to bar your way, hands on two knife-hilts.')
M[5460] = mob('the servant boy', 'boy servant', 'A servant boy is here running errands.',
              'A small boy who runs through the halls of the Palace and knows all of its secrets.')
M[5461] = mob("the Sultan's guard", 'guard sultans', 'A guard stands here, watching the street.',
              'A trained fighter in the tower-and-sun of Thalos, who watches every face for the ones that do not belong.')
M[5462] = mob("the Sultan's guard", 'guard sultans', 'A guard stands here, watching the gate.',
              'A trained fighter in a tabard of the tower and rising sun, sworn to hold the gate as Saint Ilsa held it.')
M[5463] = mob('the Chief Guard', 'guard chief sultans', "The Chief of the Sultan's Guard stands here.",
              'A big, quiet man who has hunted things in the hills that most of his guards would not believe in.')
M[5464] = mob('the mercenary', 'mercenary sellsword', 'A mercenary stands here waiting for a job.',
              'A down-at-heel cut-throat who would rather be hired than levied.')
M[5465] = mob('the shipwright', 'shipwright captain', 'An old captain rests here, carving on a stick.',
              'The shipwright of New Thalos, who builds the barges that carry the grain. He beams at you through his beard.')
M[5466] = mob('the blacksmith', 'blacksmith smith farrier', 'The blacksmith stands here pumping the bellows.',
              'A big man dripping with sweat, who shoes the horses of the tithe-wagons. He stops to bid you welcome.')
M[5467] = mob('the horse', 'horse', 'A horse stands here.',
              'One of the fine horses whose sires came out of Old Thalos.')
M[5468] = mob('the bewildered refugee', 'refugee tourist', 'A refugee stands here looking lost.',
              'A small, round man with everything he owns tied around his neck, squinting at a hand-drawn map he is holding upside down.')
M[5469] = mob('the ixitxachitl', 'ixitxachitl ray', 'A very large ray with a wicked looking tail swims here.',
              'A great ray with sharp fangs and a barbed tail, that the fishermen say takes swimmers.')
M[5470] = mob('the cryohydra', 'cryohydra hydra', 'The cryohydra stands here.',
              'A grey-brown many-headed reptile with amber eyes, its breath freezing on the bars. It was taken in the high passes.')
M[5471] = mob('the minotaur lizard', 'lizard minotaur', 'The minotaur lizard stands here.',
              'A huge lizard with horns like a bull\'s, kept in the Sultan\'s cells for the war-magi.')
M[5472] = mob('the death dog', 'dog death', 'The death dog stands here.',
              'A big two-headed hound that crept east out of the march. It barks at you viciously from both mouths.')
M[5473] = mob('the spotted lion', 'lion spotted', 'The spotted lion stands here.',
              'A fierce, dapple-skinned hill lion that glares at you through its matted mane.')
M[5474] = mob('the behir', 'behir', 'A behir slithers on the ground.',
              'A great snake-like reptile with more than a dozen legs, and lightning in its throat.')
M[5475] = mob('the chimera', 'chimera creature lion goat dragon', 'A creature with three heads, lion, goat and dragon, stands here.',
              'The chimera has the hindquarters of a goat, the forepaws of a lion and the body of a red dragon. Nobody knows where the Sultan\'s hunters found it.')
M[5476] = mob('the feathered serpent', 'serpent feathered', 'A feathered serpent hovers here.',
              'A beautiful creature with the body of a serpent and rainbow-coloured feathered wings, wasting in a cell far from the sky.')
M[5477] = mob('the giant hornet', 'hornet giant', 'The giant hornet hovers here.',
              'A hornet the size of a dog. There is nothing more to be said.')
M[5478] = mob('the pegasus', 'pegasus horse', 'The pegasus stands here, flexing its wings.',
              'A magnificent winged steed, like the best horses of Old Thalos, but with wings. It is the pride of the Sultan\'s garden.')
M[5479] = mob('Elriva', 'elriva apothecary', 'Elriva stands here mixing a draught.',
              'A strong woman dressed in black, with long black hair. She mixes draughts for wounds, for sleep, and for forgetting.')
M[5480] = mob('Braheem', 'braheem mage', 'Braheem stands here talking to the walls.',
              'A powerful mage, expelled from the war-college and slightly mad. The walls sometimes answer him.')
M[5481] = mob('the high priest', 'priest high warden', 'The High Warden kneels here, or was kneeling until you came in.',
              'The High Warden of the Flame, a gaunt old man with a terrible temper. He does NOT look happy that you have disturbed him.')
M[5482] = mob('the Royal Guard', 'guard royal elite', 'An elite Royal Guard stands here, watching the crowd.',
              'One of the Royal Guard of New Thalos, who has served a term on the wall and come back harder.')
M[5483] = mob('Patch the bartender', 'patch bartender', 'A large half-orc with a patch over one eye pours drink behind the counter.',
              'A really big man who lost an eye somewhere, and does not tell anyone where.')
M[5484] = mob('Stitch the leatherworker', 'stitch leatherworker', 'Stitch the leatherworker reclines in his chair.',
              'A small halfling with his feet up on his desk, waiting for some fool, that is, customer, to come in.')
M[5485] = mob('the gardener', 'gardener elf', 'A small elf stands here tending the garden.',
              'A young elf in dirt-stained clothes, weeding the Sultan\'s garden, the only green place in the city.')
M[5486] = mob('the nightmare', 'nightmare horse', 'A huge horse, black as night, stands here.',
              'The largest horse you have ever seen, ten feet at the shoulder, breathing flame from its nostrils. It leaps to attack.')
M[5487] = mob('the wolverine', 'wolverine wolf', 'A large wolf-like creature leaps out of the darkness.',
              'A half wolf, half man thing in a glove with long thin blades on it, kept locked away in the deepest cell.')
M[5488] = mob('the mimic', 'mimic painting', "You see an incredibly life-like painting of the Sultan's mother.",
              'Boy, is she ugly.')
M[5489] = mob('the mayor', 'mayor', 'The Mayor of New Thalos stands here.',
              'A plump, nervous man in his best coat, who keeps the tithe ledgers. His ledgers decide who goes west, and he sleeps very badly.')
M[5490] = mob('the chef', 'chef cook', 'The chef stands here making dinner.',
              'A very large man who cooks for the Palace and tastes everything twice, in case it is poisoned.')

RETHEME = {
    'zones': {54: 'New Thalos'},
    'rooms': R,
    'mobs': M,
}
