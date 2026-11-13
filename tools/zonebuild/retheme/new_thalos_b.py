"""New Thalos (zone 54), PART B: rooms 5550-5699 and every object in 54.obj.

City plan (part B's half; part A covers rooms 5400-5549, the mobs and the zone
name).  New Thalos is the crowded refugee city the survivors of Old Thalos
built, generations ago, after the first darkness took their home.  It is poor,
devout and watchful, and it supplies the front: grain, cloth, recruits, coin.

- The Palace (5550-5605): the Sultan, last of the old Thalan line, still keeps
  his palace, but its splendour is salvage carried out of the dead city and
  most of it has been sold for the tithe to the wall.  Guards, a cold dining
  hall, the women's court (the stock harem), a garden kept as a memorial, an art
  hall of paintings of the lost city, and a shrine to the Last Flame -- the
  fire the survivors carried out of Old Thalos.  Under the palace lie the beast
  pits, where things caught on the roads are caged for the war-magi to study.
- The guild halls off Guildsman's Row (bowyers, masons, tanners) work for the
  front; the library holds what was saved of Thalos; the dance hall is the
  hall of remembrance where the city keeps the Night of Leaving.
- Outside: the west road climbs into the mountains toward Midgaard (a side
  trail drops south toward the old mine country); the River of Lost Souls
  (north bank joins the penitents' road) and the Dark River run through the
  hills; the Isvar runs east through the city to the delta, the Dragon Sea and
  the supply dock where the city's goods are shipped.
"""

R = {}   # rooms
O = {}   # objs

# ================================================================= the palace
R[5550] = dict(name='The Grand Entrance', desc="""
    The entrance hall of the palace was built to dazzle, and once it did.  The
    tapestries are threadbare now, the candelabras are iron where the silver was
    sold, and the long carpet has been worn to the boards down its middle by
    petitioners.  Guard houses open north and south.  The halls of the palace
    begin to the west, and the gate lies east.""")
R[5551] = dict(name='The Library', desc="""
    The city library holds everything the survivors carried out of Old Thalos:
    rolls of charred parchment, books swollen with old water, deeds to houses
    that no longer stand.  A committee of scholars has worked for generations to
    copy what can be read.  The shelves sag, and the air smells of glue and
    mould.  Lantern Row is east.""",
    extras={'shelves books rolls parchment': 'Most of the books are burned at the edges. One shelf is kept apart and labelled in red: "From the Temple. Do not open."'})
R[5552] = dict(name='The Hall Of Remembrance', desc="""
    Once a dance hall, this long room is where the city keeps the Night of
    Leaving, when the survivors fled Old Thalos.  The feast is over; sweepers
    are clearing away cold food and the stubs of a thousand candles, one for
    every family lost.  A banner still hangs on the wall.  Lantern Row is east.""",
    extras={'banner': 'The faded banner reads: WE CAME OUT OF THE DARK. WE REMEMBER. Underneath, in smaller letters, someone has added: "And it remembers us."'})
R[5553] = dict(name='The Jail', desc="""
    A bare stone cell with straw on the floor and a bucket in the corner.  The
    walls are scratched with names, tally marks and prayers.  In New Thalos
    debtors, deserters and those who talk too loudly about the west all end up
    here sooner or later.  A barred gate leads north.""",
    extras={'walls names marks prayers scratches': 'Among the tally marks someone has scratched, over and over: "I only said what I saw on the road."'})
R[5554] = dict(name='City Hall', desc="""
    The tithe hall of New Thalos.  Clerks at long tables reckon the city's
    quotas for the front: so many sacks of grain, so many bolts of cloth, so many
    sons of fighting age.  The Sultan's word is law, but it is the mayor and his
    ledgers that decide who goes west.  West Casbah lies north.""",
    extras={'ledgers ledger tables': 'Column after column of names, each with a district and an age. A few are marked with a small black flame: those who did not come back.'})
R[5555] = dict(name="The Bowyers' And Fletchers' Guild", desc="""
    Pegs on every wall hold bows in all stages of making, and bundles of shafts
    are stacked to the ceiling, every one of them promised to the wall.  Boys sit
    in a corner fletching arrows by the thousand, their fingers sticky with glue.
    Elven craftsmen test each finished bow and send back the poor ones without a
    word.  Guildsman's Row is east.""")
R[5556] = dict(name="The Masons' Guild", desc="""
    Dwarven masons built most of New Thalos, and they are building still: walls
    first, always walls.  Hammers ring in a blur as they dress blocks for the
    city's ramparts and lintels for the shrines.  The guildmaster keeps a stone
    from Old Thalos on his bench and will not let anyone touch it.
    Guildsman's Row lies west.""",
    extras={'stone bench': 'A blackened block of carved stone, part of a face. The dwarves say it came from the gate of the old city.'})
R[5557] = dict(name='The Southern Guard House', desc="""
    The southern of the two guard houses of the palace.  It is bare and
    spartan: a bench, a brazier, a rack of spears and a duty roster nailed to
    the wall.  The guards here are older men, kept back from the front to watch
    the Sultan's door.  The grand entrance is north.""",
    extras={'roster duty': 'The roster lists the watches of the palace guard. Several names have been crossed out and "sent west" written beside them.'})
R[5558] = dict(name='The Palace Gate', desc="""
    A tall gate of gilded iron, carried piece by piece out of Old Thalos and
    set up here by the survivors.  The gilt is flaking and the bars are scarred,
    but it is still the finest thing in the city.  Beyond it rise the palace
    towers, and petitioners queue along the wall all day.  The gate opens west
    into the palace, and Sultan's Walk lies east.""",
    extras={'gate bars gilt': 'Among the scrolls of iron you can make out the old crest of Thalos: a tower and a rising sun. Someone has scratched a black flame over the sun.'})
R[5559] = dict(name='The Northwest Tower', desc="""
    You stand on the northwestern of the four towers guarding the city.  West,
    the mountains stand between New Thalos and Midgaard, and the River Isvar
    comes down out of them.  Somewhere beyond, far past the fort, lie the ruins
    of the old city and worse things.  South lie the crowded roofs of the city
    and the desert.  A stair leads down.""")
R[5560] = dict(name='The Northern Guard House', desc="""
    The northern guard house is clean and cold.  Off-duty guards sit at a table
    playing at cards for copper, their armour hung on pegs within reach.  They
    play in silence, and look up every time the door goes.  The only way out is
    south, into the grand entrance.""")
R[5561] = dict(name='The Kitchen', desc="""
    The palace kitchen is the warmest room in the city.  A great copper pot
    simmers over the fire on the south wall, but it holds thin soup: the best of
    the palace stores goes to the front.  The chef chops roots at the table while
    servants hurry about.  A small door leads north into the hall, and the dining
    hall is west.""")
R[5562] = dict(name='The Northeast Tower', desc="""
    The northeastern tower looks out over the plains toward the dark line of
    the northern forest.  Caravans crawl along the roads below, bound west with
    the tithe.  South, beyond the city, the desert shimmers.  A stair leads down
    into the city.""")
R[5563] = dict(name='The Servants\' Passage', desc="""
    The eastern end of the southern hallway, plain and narrow, where servants
    pass to and from the kitchen.  The smell of soup and woodsmoke hangs here.  A
    small door leads south to the kitchen, and the hall runs west.""")
R[5564] = dict(name="The Tanners' Guild", desc="""
    The stink of the tanning pits hits you at the door.  Hides hang everywhere,
    stretched on frames and dyed in dull greens and browns, to be cut into
    jerkins, straps and scabbards for the wall.  The tanners work with their
    heads down.  Someone has scrawled a message on the wall.  Guildsman's Row is
    east.""",
    extras={'message': 'The message reads: "Forty hides a day for the front. I have not seen my own hands clean in a year."'})
R[5565] = dict(name='The East End Of The North Hall', desc="""
    The eastern end of the northern hallway.  The floor here is clean, and
    candles burn in niches along the walls.  A simple wooden door leads north,
    with a brass plaque above it, and the hall runs west.""",
    extras={'plaque': 'Engraved on the plaque: "The Shrine of the Last Flame. Carried out of Thalos. Never let it go out."'})
R[5566] = dict(name='The Shrine Of The Last Flame', desc="""
    A small, still room walled in blue and white tiles saved from the temple of
    Old Thalos.  In a bronze bowl on the altar burns the Last Flame, the fire the
    survivors carried out of the dying city, fed day and night for generations.
    The air is heavy and very quiet, as if something is listening.  The door
    leads south.""",
    extras={'flame bowl altar fire': 'A small, steady flame in a bowl of bronze. It does not flicker, even when the door opens.',
            'tiles walls': 'Some of the tiles are cracked and blackened. They were prised out of the walls of a burning temple.'})
R[5567] = dict(name='Outside The Northern Gate Of New Thalos', desc="""
    You stand before the northern gate of New Thalos.  Its iron doors are kept
    shut against the night, and a watchman on the wall above looks you over.
    The city lies south through the gate, and open country stretches north
    toward the plains.""")
R[5568] = dict(name='Outside The Eastern Gate Of New Thalos', desc="""
    The great iron gate of the eastern wall stands to the west.  Through here
    come the caravans from the sea and the dock, and the gate guards search every
    one.  The road runs east toward the coast, and a narrow strip of ground
    follows the wall south.""")
R[5569] = dict(name='Outside The West Gate Of New Thalos', desc="""
    You stand before the west gate, the busiest in the city: through it go the
    grain carts, the cloth wagons and the columns of recruits bound for Midgaard
    and the wall.  Mothers wait here for letters.  The gate is east, and the road
    climbs west toward the mountains.""")
R[5570] = dict(name='Outside The Wall', desc="""
    A small clearing in the scrub outside the east wall.  The ground is
    trodden flat, far more than a dead end should be, and there are footprints
    that lead nowhere.  Smugglers, the watch says.  The only plain way out is
    north.""",
    extras={'ground footprints prints': 'Boot prints in the dust, many of them, and all of them stop at the same patch of bare earth.'})
R[5571] = dict(name='The Grand Dining Hall', desc="""
    A long oak table runs the length of the hall, set with plate salvaged from
    the old city.  Servants lay it every night, though the Sultan seldom eats
    here any more and most of the chairs stay empty: their owners went west.  The
    kitchen is east, and double doors open north into the hall.""")
R[5572] = dict(name='A Hall By The Dining Hall', desc="""
    A crossing of the palace hallways.  Double doors to the south lead into the
    dining hall, the hall runs east toward the servants' passage and west past
    the guest rooms, and a corridor leads north.""")
R[5573] = dict(name='A Crossing Of The Halls', desc="""
    You stand at a crossing of the palace hallways, its cedar panels dark with
    age.  Corridors lead north, south and east.  To the west the hall opens into
    the palace garden, and the smell of damp earth drifts in.""")
R[5574] = dict(name='A Hall Before An Iron Door', desc="""
    The northern hallway meets a corridor here.  Halls run east and west and
    south, but the eye goes to the heavy iron door in the north wall, studded and
    banded, with scratches around the lock.  Servants walk quickly past it.""",
    extras={'door iron scratches': 'The scratches around the lock are deep, and on the inside of the door, by the sound of it, there are more.'})
R[5575] = dict(name='The Entrance To The Dungeon', desc="""
    A cold, damp room of rough stone, nothing like the palace above.  A steel
    grating in the floor leads down into darkness, and from below come the smells
    of straw, dung and something sour.  Something down there moves now and
    then.  An iron door leads south back to the hallway.""")
R[5576] = dict(name='A Guest Room', desc="""
    A small guest room for visiting nobles and envoys from the fort.  A dresser
    stands against the east wall with a mirror above it, and a bed with worn
    satin sheets lies under the window in the south wall.  The door leads north
    into the hallway.""",
    extras={'window': 'Through the window you see the palace grounds between the outer wall and the building, and guards walking the wall in pairs.',
            'mirror': 'In the mirror you see an armoured figure with a weapon in hand, looking tired. It takes a moment to know it for your own reflection.'})
R[5577] = dict(name='A Hall Of Portraits', desc="""
    The long southern hall continues east and west, with a wooden door in the
    south wall.  On the north wall hangs the portrait of a nobleman of Old Thalos,
    painted before the fall.  His eyes have been cut out of the canvas.""",
    extras={'portrait picture nobleman canvas': 'A proud man in the robes of the old city. Someone has cut out his eyes with a knife, long ago. Nobody in the palace will say who he was.'})
R[5578] = dict(name="The Sultan's Garden", desc="""
    The Sultan's garden is warm and close, heavy with jasmine and honeysuckle
    grown from cuttings carried out of Old Thalos.  It is kept as a memorial, and
    every plant has a small stone beside it bearing a family name.  Through the
    palms to the west stands a white gazebo, and the hallway is east.  A gilded
    sign stands by the path.""",
    extras={'sign': 'The sign reads: "These flowers grew in the gardens of Thalos. We carried them out of the fire. Take only memories. -- The Sultan"',
            'stones stone names': 'Small stones, hundreds of them, each with a family name cut into it. Some are very new.'})
R[5579] = dict(name='A Hall Before The Gallery', desc="""
    The northern hallway runs east and west, a narrow red carpet worn thin
    down its middle, with a bench here and there for petitioners kept waiting.
    A door in the north wall bears a plaque.""",
    extras={'plaque door': 'The plaque reads: "The Gallery of Thalos. Paintings of the old city, as it was." Below, a smaller note: "Touch nothing."'})
R[5580] = dict(name='The Gallery Of Thalos', desc="""
    The Sultan's gallery holds paintings of the old city as it was: markets,
    towers, summer gardens, the old army marching out in glory.  Sculptures stand
    on pedestals in the corners, and mirrors are set so a viewer can see them
    whole.  Your eye is pulled to the great painting that fills the far wall.  The
    door leads south.""",
    extras={'painting': 'The great painting on the west wall shows the temple of Old Thalos in the last light of evening. Look long enough and the shadows in its doorway seem to change.',
            'sculptures sculpture mirrors': 'Marble figures of kings and priests, their faces worn smooth by the hands of the grieving.'})
R[5581] = dict(name='A Small Guest Room', desc="""
    Another room for visiting nobles, smaller and colder than the first.  A
    dresser and a mirror stand against the east wall, and a narrow bed lies
    along the south wall.  Nobody has slept here in a long time.  The door leads
    north.""")
R[5582] = dict(name='The West End Of The South Hall', desc="""
    The western end of the southern hallway.  The hall runs back east, and
    there are doors in the south and west walls.  Behind the west door you hear
    soft voices, and once, someone crying.""")
R[5583] = dict(name='The Garden Gazebo', desc="""
    A small white gazebo stands among the flowers at the end of the garden.
    Birds nest under its roof and the scent of jasmine is thick here.  It is the
    most peaceful place in New Thalos, and the stillness feels almost wrong.  The
    garden lies east.""")
R[5584] = dict(name='The West End Of The North Hall', desc="""
    The western end of the northern hallway.  Two doors are set in the walls
    here, one to the north and a larger one to the west, guarded day and night.
    The hall runs back east.""")
R[5585] = dict(name='The Guard Room', desc="""
    A bare chamber lined with cots and footlockers, where the palace guard
    sleep.  They may not leave the palace grounds without leave, and some have
    not seen their families in years.  The only way out is south.""")
R[5586] = dict(name='The Barracks Of The Guard', desc="""
    The living quarters of the guards who watch the women's court.  Cots and
    footlockers stand in rows, and on the walls hang pictures of famous knights of
    the Sultan's Guard, most of them dead on the march.  A passage leads north.""",
    extras={'pictures picture knights': 'Faded portraits of knights in the old Thalan armour. Black ribbons are tied to every frame but one.'})
R[5587] = dict(name="The Women's Court", desc="""
    The Sultan's women live here, in a warm room of cushions and silk hangings
    that the war has not reached.  Girls lounge about the room, and at its western
    end a young woman sits atop a heap of pillows.  It is a gilded cage, and they
    know it.  Doors lead east and south, and the hangings on the north wall stir
    in a draught.""",
    extras={'hangings north wall': 'The silk hangings on the north wall move gently, though there is no window.'})
R[5588] = dict(name='A Small Room', desc="""
    A cramped secret passage that gives the Sultan private access between his
    throne room and the women's court.  It is dusty and close, and the walls are
    thin enough to hear through.  Doors lead north and south.""")
R[5589] = dict(name='The Throne Room', desc="""
    The throne room of the Sultan of New Thalos.  Guards stand at attention
    beside a gilded throne set on a marble dais; it was carried out of Old Thalos
    on the backs of four men.  The jewels have been prised out of it to pay the
    tithe.  Doors lead east and south, and the throne itself sits against the
    north wall.""",
    extras={'throne dais': 'The throne is old and heavy, empty sockets where its jewels once were. It sits a little away from the wall, as if it has been moved.'})
R[5590] = dict(name='The Treasure Room', desc="""
    The last treasury of Thalos.  It is smaller than the stories say, and much
    of it is already gone west in tithe chests.  Somewhere a gong has begun to
    sound: the guards know you are here.  Grab what you can and make for the door
    to the south.""")

# ====================================================== the beast pits below
R[5591] = dict(name="The Jailer's Room", desc="""
    An old wooden ladder leads down from the steel grating above into this
    small cave of a room.  A bench, a guttering candle and a ring of hooks for
    keys are all it holds.  The jailer keeps the beast pits, where things caught
    on the roads are caged.  A door is set into the east wall.""")
R[5592] = dict(name='The Beast Pits', desc="""
    A rough stone tunnel, its floor slick with straw and filth.  Barred cells
    open to the north and south.  The tunnel runs east, and a door in the west
    wall leads into a dark passage.""")
R[5593] = dict(name='The Beast Pits', desc="""
    The tunnel runs east and west between barred cells to the north and south.
    The bars here are bent outward a little, and fresh iron has been riveted
    across them.""")
R[5594] = dict(name='The Beast Pits', desc="""
    The tunnel continues east and west.  Cells open north and south, and
    something in one of them growls low and long as you pass.  Gnawed bones lie in
    the straw.""")
R[5595] = dict(name='The End Of The Beast Pits', desc="""
    The tunnel ends here, with cells north and south and the way back west.  A
    narrow crack runs through the stone of the east wall, and a sour animal
    smell seeps out of it.""",
    extras={'crack wall': 'The crack in the east wall is just wide enough to squeeze through. Grey hairs are caught on its edges.'})
R[5596] = dict(name='The Secret Cell', desc="""
    More a lair than a cell.  Hay is strewn over the floor, covering bones
    that are not all animal.  Blood is spattered on the walls and tufts of grey
    hair are matted in one corner.  As you turn to go, a pair of small red eyes
    watches you from the dark.  The crack leads back west.""")
R[5597] = dict(name='A Cell', desc="""
    A cold, cramped cell with one way out.  The walls are black with soot and
    the air stinks of goat and brimstone.  Something with several heads has
    paced a groove into the floor.""")
R[5598] = dict(name='A Cell', desc="""
    A cramped stone cell with a single barred door.  Scorch marks branch
    across the walls like lightning, and the straw is burnt in patches.""")
R[5599] = dict(name='A Cell', desc="""
    A cold cell, its only exit the barred door.  Gnawed bones are heaped in
    the corners, and the walls are scored low down by many claws, as if a pack
    were kept here together.""")
R[5600] = dict(name='A Cell', desc="""
    A cramped cell with a single door.  Frost furs the walls and the straw is
    frozen stiff, though there is no draught; the cold comes from whatever lives
    here.""")
R[5601] = dict(name='A Cell', desc="""
    A small cell with one way out.  Grey paper hangs in sheets from the ceiling,
    the remains of a great nest, and a dry buzzing echoes off the stone.""")
R[5602] = dict(name='A Cell', desc="""
    A cold cell with a single barred door.  Bright feathers lie scattered in
    the straw, strangely clean in so foul a place, and the air smells faintly of
    rain.""")
R[5603] = dict(name='A Cell', desc="""
    A cramped cell, its one door barred.  Tawny hair is caught in the cracks of
    the stone, and deep claw marks run down the back wall.""")
R[5604] = dict(name='A Cell', desc="""
    A low, wet cell with one door.  Shed scales lie in the muck, and the bars
    of the door are dented from the inside by something heavy with horns.""")
R[5605] = dict(name='The Cedar Hall', desc="""
    A long hall panelled in cedar, the one wood that came out of Old Thalos
    unburned.  A narrow purple rug runs down its length.  The hall leads west
    into the palace and east to the grand entrance.""")

# ================================================= the mountains to the west
R[5606] = dict(name='A Path Through The Mountains', desc="""
    The narrow path turns here between grey shoulders of rock, heading south
    and west.  A cairn of stones marks the bend; travellers add one each, for the
    ones who did not come back.""",
    extras={'cairn stones': 'A cairn of small stones, some with names scratched on them.'})
R[5607] = dict(name='A Path Through The Mountains', desc="""
    Travel is hard and slow here; you must clamber around great boulders
    strewn across the path.  Wagon wheels have left deep ruts where they could
    pass.  The path runs north and east.""")
R[5608] = dict(name='The Edge Of The Ravine', desc="""
    The ground drops away below you to a rushing river.  A rope bridge sways in
    the wind across the gap, its planks patched with wood of many colours.  The
    bridge leads east, and the path runs back west.""")
R[5609] = dict(name='On A Rope Bridge', desc="""
    The rope bridge shudders under your weight high above the valley.  Far
    below, the river is a white thread among the rocks.  The bridge runs east and
    west.""")
R[5610] = dict(name='The Ledge Around The Valley', desc="""
    A narrow ledge winds around a deep valley in the mountains.  It once turned
    north with the shape of the valley, but a rockfall has torn that way off the
    mountainside.  A steep trail leads east.""",
    exits={'n': 'The ledge to the north has fallen away into the valley. There is nothing there but air.'})
R[5611] = dict(name='A Path Through The Mountains', desc="""
    A rock-strewn path deep in the mountains between Midgaard and New Thalos.
    Loose stones turn underfoot at every step.  The path leads east and west.""")
R[5612] = dict(name='On The Eastern Edge Of The Mountains', desc="""
    You stand on the eastern edge of the mountains.  The high peaks lie behind
    you to the west, toward Midgaard and the wall, and the hills fall away to the
    south toward the plains and the city.""")
R[5613] = dict(name='In The Foothills', desc="""
    The path winds down the face of the mountain in tight turns, worn deep by
    the boots of recruits going one way and carts of wounded coming back the
    other.  It leads north and east.""")
R[5614] = dict(name='In The Foothills', desc="""
    The path bends down the slope through stunted pines.  A broken cart wheel
    lies abandoned among the stones.  The way leads south and west.""")
R[5615] = dict(name='A Rocky Trail', desc="""
    The sound of running water reaches you from the south, and through the
    trees you glimpse the river and a landing.  The trail continues north up into
    the foothills and east toward the road.""")
R[5616] = dict(name='On A Road', desc="""
    A long road of packed earth, rutted by supply wagons.  Milestones mark the
    distance to Midgaard.  The road continues east and south.""")
R[5617] = dict(name='On A Road', desc="""
    The road runs east and west between fields of thin grain, every sack of it
    already promised to the fort.  A gibbet stands empty by the verge.""")
R[5618] = dict(name='On A Road', desc="""
    A well kept road leads east to New Thalos and west into the mountains.
    Wide plains stretch away to the north and a dark green forest begins to the
    south.  Pilgrims and recruits walk it side by side.""")
R[5619] = dict(name='The Headwaters Of The River Of Lost Souls', desc="""
    You are at the headwaters of the darkest river in the land.  Black water
    pools in this rocky valley, still and swampy, and nothing grows on its banks.
    The rock walls close in on every side except the bank to the north, where a
    path leaves the water, and to the south, where the river flows away.""",
    exits={'n': 'A small path leaves the bank to the north. Penitents use it, walking barefoot.',
           's': 'The swampy water flows slowly south.'})

# =========================================================== River Isvar west
R[5620] = dict(name='River Isvar', desc="""
    The river calms after its fight through the heart of the mountain.  The
    rock still rises on both sides, but there are faint traces of green to the
    east.  The water flows east, and back west to a split in the river.""")
R[5621] = dict(name='River Isvar', desc="""
    The river runs east and west through the hills, cold and fast.  A dead
    tree has lodged against a rock midstream, hung with weed.""")
R[5622] = dict(name='River Isvar', desc="""
    The river begins its descent out of the mountains here, quickening toward
    the east.  It flows back west into the hills.""")
R[5623] = dict(name='River Isvar', desc="""
    The river flows east under the wall of the city through an iron grating
    furred with weed.  Westward it stretches back toward the mountains.""")
R[5624] = dict(name='River Isvar', desc="""
    The river flows out of the city down a long winding gully toward the
    Dragon Sea.  The desert lies south and grassland north, and a road runs
    beside the river, though the banks are too steep to see far.  The water runs
    east, and west back into the city.""")
R[5625] = dict(name='River Isvar', desc="""
    The river runs gently through the lowlands, wide and brown.  It is hard to
    believe this is the same water that came crashing down the mountains.  It
    flows east and west.""")
R[5626] = dict(name='River Isvar', desc="""
    Herd animals can be heard in the distance, though none come down to the
    water; the banks are too steep, or they will not drink here.  The river runs
    east and west.""")

# ==================================================== mountains, east of ravine
R[5627] = dict(name='The Edge Of The Ravine', desc="""
    You stand at the edge of a long drop.  A rope bridge leads west across the
    gap, swaying in the wind, and a path leads off east through the mountains.
    Someone has cut warning notches in the bridge post.""",
    extras={'post notches': 'Three notches: the old sign for "one at a time".'})
R[5628] = dict(name='A Path Through The Mountains', desc="""
    The narrow path winds east and west.  A buzzard circles overhead, waiting.
    A rough trail drops away south toward the foothills and the old mine country;
    the drovers say nobody goes that way now.""")
R[5629] = dict(name='A Path Through The Mountains', desc="""
    A boulder has rolled down onto the path here, recently, crushing the scrub.
    You squeeze past it.  The path runs east and west.""")
R[5630] = dict(name='On A Road', desc="""
    The road runs east and west through thin woodland.  The trees close in
    overhead, and the carters keep their torches lit even by day.""")
R[5631] = dict(name='On A Road', desc="""
    The road runs east and west.  A shrine of piled stones stands at the
    roadside, with a small flame burning in a lamp.""",
    extras={'shrine lamp flame': 'A roadside shrine to the Last Flame. Travellers leave a drop of oil for the lamp.'})
R[5632] = dict(name='On A Road', desc="""
    The road runs east and west.  The ditches on either side are full of
    nettles and old, broken barrel-staves.""")
R[5633] = dict(name='On A Road', desc="""
    The road bends here toward the river, where a little dock gives on to the
    water to the south.  The road continues north and west.""")

# ===================================================== River Of Lost Souls
R[5634] = dict(name='The River Of Lost Souls', desc="""
    The black river flows south through a valley in the mountains.  To the
    west, beyond the rocks, you can see the roofs of a small village with no smoke
    rising from it.  The water runs north and south.""")
R[5635] = dict(name='The River Of Lost Souls', desc="""
    The river flows through the southern end of a wide valley.  The walls close
    in to the south.  The water is so dark you cannot see your own hands in it.""")
R[5636] = dict(name='The River Of Lost Souls', desc="""
    The river speeds up as it pours down a mountain crevice.  High above, a
    rope bridge sways across the gap.  The water runs north and south.""")
R[5637] = dict(name='The River Of Lost Souls', desc="""
    The river rushes through a crack in the side of the mountain toward the
    south.  Listen for rapids; there is no room here to turn back.  It flows north
    and south.""")
R[5638] = dict(name='The River Of Lost Souls', desc="""
    The river calms as the crevasse widens and loosens its grip on the water.
    It flows back north through the crack and on to the south.""")
R[5639] = dict(name='A Split In The River', desc="""
    The waters crash onto a great rock and divide: the River of Lost Souls runs
    on north and south, and the Isvar breaks off east.  To the west the rocks are
    split and crumbled as if torn apart by some huge force, and there is no way
    through.""")
R[5640] = dict(name='The River Of Lost Souls', desc="""
    The river runs north and south through a valley eroded by water.  The rock
    banks are smooth and grey, and nothing grows on them.""")
R[5641] = dict(name='The River Of Lost Souls', desc="""
    The river runs north and south.  Things drift by in the dark water now and
    then, too sodden to tell what they were.""")
R[5642] = dict(name='The River Of Lost Souls', desc="""
    The river runs north and south through the worn valley.  The current pulls
    hard here, and the cold of it aches in the bones.""")
R[5643] = dict(name='The River Of Lost Souls', desc="""
    The river bends sharply, plunging south into the mountain where you cannot
    follow.  On a ledge above you to the west, something moves and is still.
    The only way is back north.""")

# =========================================================== River Isvar east
R[5644] = dict(name='River Isvar', desc="""
    The river widens here, free of the rock at last, and flows east toward the
    plains.  Behind you to the west it runs back into the hills.""")
R[5645] = dict(name='River Isvar', desc="""
    The river runs east and west.  There is a landing to the north where boats
    put in, and a trail leads up from it.""")
R[5646] = dict(name='River Isvar', desc="""
    The river meanders through the foothills.  The air is drier on this side of
    the mountains, and a little warmer.  The water runs east and west.""")
R[5647] = dict(name='River Isvar', desc="""
    The river runs east across the plains.  Westward rise the snow-capped
    peaks, and to the east you can make out the walls and smoke of New Thalos.""")
R[5648] = dict(name='River Isvar', desc="""
    The river runs east and west, slow and brown.  Grain barges drift past,
    bound for the city and then for the front.""")
R[5649] = dict(name='River Isvar', desc="""
    The river slows as it widens through the lowlands.  A small dock gives
    access to the north shore.  The water runs east toward the city and west.""")

# ============================================== the mountain tangle (a maze)
R[5651] = dict(name='In The Mountains', desc="""
    You pick your way over rocks and stones in the mountains between the Isvar
    and the Dark River.  Paths of a sort lead every way, and every rock looks like
    every other.""")
R[5652] = dict(name='In The Mountains', desc="""
    Grey rock, grey scree, grey sky.  You are fairly sure you have passed this
    split boulder before.  Or one just like it.""")
R[5653] = dict(name='In The Mountains', desc="""
    The rocks here crowd close.  To the east a great boulder sits wedged in a
    gap, and you can hear running water beyond it.  Other ways lead north, south
    and west, all much alike.""",
    exits={'e': 'A great boulder blocks the gap. There is a crack around its edge, and the sound of water beyond.'})
R[5654] = dict(name='In The Mountains', desc="""
    Loose stones slide underfoot.  The mountains between the rivers fold in on
    themselves, and the path you came by is already hard to find.""")
R[5655] = dict(name='In The Mountains', desc="""
    A cold wind whistles through the rocks.  A pile of stones has been stacked
    here by someone else who was lost, and it did not help them.""")
R[5656] = dict(name='In The Mountains', desc="""
    A shallow hollow among the rocks, sheltered from the wind.  Old ashes mark
    a cookfire.  Ways lead off in all four directions, all of them the same.""")
R[5657] = dict(name='In The Mountains', desc="""
    You clamber over a ridge of broken stone.  Every way out looks like the way
    you came in, and the mountains seem to shift when you are not looking.""")
R[5658] = dict(name='In The Mountains', desc="""
    A narrow cleft between two slabs of rock.  Someone has scratched an arrow
    on the stone, but there are arrows scratched pointing every way.""")
R[5659] = dict(name='In The Mountains', desc="""
    A bleak saddle of rock between two peaks.  Bones of a mule lie bleached
    among the stones.  You are lost, and the rocks do not care.""")

# ============================================================= the Dark River
R[5660] = dict(name='The Headwaters Of The Dark River', desc="""
    A spring wells up black from the heart of the mountain and flows west.
    An earthquake has torn this place not long ago: the path east is choked with
    fallen rock, and you must scramble to pass it.""")
R[5661] = dict(name='On The Dark River', desc="""
    The river flows west down a large crevasse and back east up into the
    mountains toward its spring.  The water has no reflection.""")
R[5662] = dict(name='On The Dark River', desc="""
    The walls of the canyon tower overhead, black with wet.  The river runs
    east and west between them.""")
R[5663] = dict(name='On The Dark River', desc="""
    The rock walls sink slowly to the level of the ground as the river leaves
    the mountains for a stretch of open land.  It runs east and west.""")
R[5664] = dict(name='On The Dark River', desc="""
    The river bends out of the foothills to the east and turns south toward
    the mountains again.  Dead reeds rattle on the banks.""")
R[5665] = dict(name='On The Dark River', desc="""
    The river follows a low fold in the foothills, bending and twisting.  Tall
    mountains rise to the south and east.  The water runs north and south.""")
R[5666] = dict(name='On The Dark River', desc="""
    The river makes a wide, sweeping turn here, from the north into the face of
    the mountain to the west.""")
R[5667] = dict(name='On The Dark River', desc="""
    The river flows west into a black mouth in the heart of the mountain, and
    east back toward the foothills.  The light behind you is very small.""")
R[5668] = dict(name='On The Dark River', desc="""
    You can barely see ahead as the river slides quietly through the
    underground passage.  The water turns from the east to the south.""")
R[5669] = dict(name='On The Dark River', desc="""
    The river flows slowly west, deeper into the mountain.  There are small
    cracks in the passage wall to the north where you might climb out of the
    water.  The way back is east.""")
R[5670] = dict(name='On The Dark River', desc="""
    The river runs east and west beneath a dark ledge high above the water.
    Your breath sounds very loud in the stone passage.""")
R[5671] = dict(name='On The Dark River', desc="""
    The passage narrows as the river flows south, deeper into the mountain.
    The way back is east.""",
    exits={'s': 'Downstream, the river passes under the arch of an old stone bridge.'})
R[5672] = dict(name='On A Small Ledge', desc="""
    You haul yourself out of the water onto a narrow ledge, hoping it leads
    somewhere.  It does not; it is wide enough only to rest on.  Old scratch marks
    on the wall count days.  The only way is south, back into the river.""")

# =============================================== the plains north of the city
R[5681] = dict(name='On The Plains', desc="""
    You stand on open grassland that stretches away in every direction.  The
    north gate of New Thalos stands to the south, and far off to the north a line
    of trees darkens the horizon.  East and west the grass runs on.""")
R[5682] = dict(name='On The Plains', desc="""
    An open field of tall grass.  The forest to the north is closer now, but
    still a long way off.  A trodden dirt path leads south toward the city.""")
R[5683] = dict(name='The Edge Of The Forest', desc="""
    You stand at the edge of a great forest.  The trees run east and west as far
    as the eye can see, and no birds sing in them.  Grass spreads out to the
    south.""")

# ================================================== the delta and the sea
R[5684] = dict(name='River Isvar', desc="""
    The river broadens and its water grows murky.  The smell of salt reaches
    you from the east: the Dragon Sea is near.  Grassland stretches away to the
    north.  The river flows east and west.""")
R[5685] = dict(name='The River Delta', desc="""
    Here the river empties into the Dragon Sea, staining the blue water brown
    with sand and silt.  East is open sea all the way to the horizon, and the
    river stretches west back toward New Thalos.""")
R[5686] = dict(name='The Dragon Sea', desc="""
    Clear blue sea rolls in every direction.  The current pulls you round in
    circles; the river mouth is west, and you think you can see a dock off to the
    north.""")
R[5687] = dict(name='The Dragon Sea', desc="""
    The Dragon Sea rolls in along the shore here, breaking on the beach.  To
    the north a wooden dock juts out into the surf.  Open water lies east and
    south.""")
R[5688] = dict(name='The Dragon Sea', desc="""
    The sea is grey-green and choppy, with the dock close by to the south.
    Gulls wheel overhead, crying.  The water runs on north and east.""")
R[5689] = dict(name='The Dragon Sea', desc="""
    Deep water just east of the dock, which lies to the west.  The water here
    is dark, and below you can see the shadow of the pilings going down.""")
R[5690] = dict(name='On A Road', desc="""
    New Thalos keeps its roads well, because they carry the city's tithe to the
    front.  Road gangs work here in all weathers, and the taxes that pay them are
    the heaviest in the realm.  The road runs east to the coast and west to the
    eastern gate.""")
R[5691] = dict(name='On A Road', desc="""
    A well used road through open country.  To the north a wall of tall pines
    runs for miles beyond the plains; to the south, past the river, lies the
    desert.  The road runs east and west.""")
R[5692] = dict(name='On A Road', desc="""
    The Dragon Sea can be seen to the east now.  From the south come the calls
    of bargemen on the Isvar, bringing goods down to the coast.  The road runs
    east and west.""")
R[5693] = dict(name='On A Road', desc="""
    This is the main land route to the coast.  Merchants bring their goods here
    to be shipped, and the tithe goes west the other way, through New Thalos, over
    the mountains and down to Midgaard.  The road runs east and west.""")
R[5694] = dict(name='Near The Shore', desc="""
    The road ends here, turning into a sandy path down the beach to a dock.
    The coastline runs away north and south.  West of here the lowlands roll up
    toward the distant snow-capped mountains.""")
R[5695] = dict(name='On A Dock', desc="""
    A plain wooden dock reaches out from the end of the road into the sea.  It
    is old but sturdy, its planks stained with tar and fish scales.  Crates of
    goods wait under oiled cloth.  The sea lies north, east and south, and the
    shore is west.""")
R[5696] = dict(name='The Dragon Sea', desc="""
    Open sea, the swell long and slow.  Far to the west a low line of coast
    shows, and the water carries you on east.  A dock lies somewhere to the west,
    beyond the breakers.""")
R[5697] = dict(name='The Dragon Sea', desc="""
    The ocean rolls gently in every direction.  On the horizon you can make out
    an island, and to the west the mainland.""")
R[5698] = dict(name='Under The Dock', desc="""
    You swim beneath the dock among four great wooden pilings, furred with weed.
    The water is murky, but to the west you think you can make out an iron
    grating.  The surface is above.""")
R[5699] = dict(name='The Lair Of The Ixitxachitl', desc="""
    Blood clouds the water as the ixitxachitl finishes its meal.  It is a great
    ray, black and barbed, that came in from the deep sea and grew fat on
    drowned dockworkers.  It wheels round as you intrude, and attacks!  The
    grating lies east.""")


# ===================================================================== objects
def obj(short, aliases, long, **kw):
    d = dict(short=short, aliases=aliases, long=long)
    d.update(kw)
    return d

# keys and fixtures
O[5400] = obj('the palace key of New Thalos', 'key palace', 'A heavy key bearing the old crest of Thalos lies here.')
O[5401] = obj('the key to the city of New Thalos', 'key city', 'The heavy key to the city lies here in the dust.')
O[5402] = obj('the great central fountain', 'fountain water', 'The great fountain of the central square runs here, its basin crowded with water jars.')
O[5493] = obj('the jail key', 'key jail', 'The key to the city jail lies here.')
O[5494] = obj('the beast-pit key', 'key dungeon pit beast', 'A rusted key to the beast pits lies here.')

# weapons (the weaponsmith's racks, made for the front)
O[5403] = obj('a morningstar', 'morningstar morning star', 'A spiked iron ball on a chain and haft lies here.')
O[5404] = obj('an awl-pike', 'awl-pike pike awl', 'A long awl-pike, made for holding a line, lies here.')
O[5405] = obj('a bardiche', 'bardiche axe', 'A heavy bardiche with a crescent blade lies here.')
O[5406] = obj('a bec de corbin', 'corbin bec hammer', 'A bec de corbin, its beak meant for punching through armour, lies here.')
O[5407] = obj('a bill-guisarme', 'guisarme bill polearm', 'A hooked bill-guisarme lies here.')
O[5408] = obj('a fauchard', 'fauchard polearm', 'A fauchard, a blade on a long pole, lies here.')
O[5409] = obj('a glaive', 'glaive polearm', 'A long-bladed glaive lies here.')
O[5410] = obj('a guisarme', 'guisarme polearm', 'A guisarme with a wicked hook lies here.')
O[5411] = obj('a sickle', 'sickle', 'A harvest sickle, ground to a war edge, lies here.')
O[5412] = obj('a two-handed bastard sword', 'sword bastard two-handed', 'A long two-handed sword stamped with the mark of New Thalos lies here.')
O[5413] = obj('a scimitar', 'scimitar sword', 'A curved scimitar of the palace guard lies here.')
O[5414] = obj('a rapier', 'rapier sword', 'A thin rapier lies here.')

# armour (the armourer's stock and the palace guard's kit)
O[5415] = obj('a suit of banded mail', 'suit mail banded', 'A suit of banded mail, mended many times, lies here.')
O[5416] = obj('a suit of brigandine', 'suit brigandine', 'A suit of brigandine, its plates riveted inside canvas, lies here.')
O[5417] = obj('a suit of field plate', 'suit plate field', 'A suit of field plate in the old Thalan style lies here.')
O[5418] = obj('a suit of ringmail', 'suit ringmail ring mail', 'A suit of ringmail lies here.')
O[5419] = obj('a suit of splintmail', 'suit splintmail splint mail', 'A suit of splintmail armour lies here.')
O[5420] = obj('a wooden shield', 'shield wooden', 'A plain wooden shield lies here.')
O[5421] = obj('a splinted shield', 'shield splinted', 'A splinted shield painted with a tower and a rising sun lies here.')
O[5422] = obj('a buckler', 'buckler shield', 'A small leather-faced buckler lies here.')
O[5423] = obj('a leather jerkin', 'jacket leather jerkin', 'A leather jerkin lies here.')
O[5424] = obj('a pair of leather sleeves', 'sleeves leather', 'A pair of leather sleeves lies here.')
O[5425] = obj('a leather cap', 'cap leather', 'A leather cap lies here.')
O[5426] = obj('a pair of leather breeches', 'pants leather breeches', 'A pair of leather breeches lies here.')
O[5427] = obj('a pair of leather gloves', 'gloves leather', 'A pair of leather gloves lies here.')
O[5428] = obj('a pair of padded leather boots', 'boots padded leather', 'A pair of padded leather boots lies here.')
O[5429] = obj('a studded leather jerkin', 'jacket studded leather jerkin', 'A studded leather jerkin lies here.')
O[5430] = obj('a pair of studded leather sleeves', 'sleeves studded leather', 'A pair of studded leather sleeves lies here.')
O[5431] = obj('a pair of studded leather breeches', 'pants studded leather breeches', 'A pair of studded leather breeches lies here.')
O[5432] = obj('a pair of studded leather gloves', 'gloves studded leather', 'A pair of studded leather gloves lies here.')
O[5433] = obj('a leather shield', 'shield leather', 'A shield of boiled leather lies here.')

# general store
O[5434] = obj('a sack', 'sack', 'A coarse grain sack lies here.')
O[5435] = obj('an oil lamp', 'lamp oil oillamp', 'A clay oil lamp lies here.')
O[5436] = obj('a backpack', 'backpack back pack', 'A sturdy canvas backpack lies here.')
O[5437] = obj('a basket', 'basket', 'A woven reed basket lies here.')
O[5438] = obj('a belt pouch', 'pouch belt', 'A leather belt pouch lies here.')
O[5439] = obj('a tallow candle', 'candle tallow', 'A tallow candle lies here.')

# the baker's shelf
O[5440] = obj('a hunk of goat cheese', 'cheese goat hunk', 'A hunk of hard goat cheese lies here.')
O[5441] = obj('some barley bread', 'bread barley', 'A heel of grey barley bread lies here.')
O[5442] = obj('some dry rations', 'rations dry', 'A bundle of dry rations lies here.')
O[5443] = obj('some iron rations', 'rations iron', 'A tin of iron rations, stamped for the front, lies here.')
O[5445] = obj('some nuts', 'nuts', 'Some nuts lie scattered on the ground.')
O[5491] = obj('a sesame seed', 'seed sesame', 'A single sesame seed lies here.')

# the tailor's stock
O[5446] = obj('a belt', 'belt', 'A plain, well made belt lies here.')
O[5447] = obj('a pair of walking boots', 'boots hiking walking', 'A pair of sturdy walking boots lies here.')
O[5448] = obj('a fur cloak', 'cloak fur', 'A fur cloak, the kind recruits buy for the cold of the wall, lies here.')
O[5449] = obj('a girdle', 'girdle', 'A cloth girdle lies here.')
O[5450] = obj('a pair of hose', 'hose', 'A pair of woollen hose lies here.')
O[5451] = obj('a common robe', 'robe common', 'A robe of plain undyed cloth lies here.')
O[5452] = obj('an embroidered robe', 'robe embroidered', 'A robe embroidered with small black flames lies here.')
O[5453] = obj('a pair of sandals', 'sandals', 'A pair of rope-soled sandals lies here.')
O[5454] = obj('a sash', 'sash', 'A mourning sash of grey cloth lies here.')
O[5455] = obj('a silk jacket', 'jacket silk', 'A silk jacket, the last of some family\'s finery, lies here.')
O[5483] = obj("a pair of tailor's shears", 'shears sewing tailor', "A pair of heavy tailor's shears lies here.")

# the vegetable seller
O[5456] = obj('an egg', 'egg', 'A small brown egg lies here.')
O[5457] = obj('a carrot', 'carrot', 'A thin, crooked carrot lies here.')
O[5458] = obj('a tomato', 'tomato', 'A bruised tomato lies here.')
O[5459] = obj('a fig', 'fig', 'A dried fig lies here.')
O[5460] = obj('some dates', 'dates', 'A bunch of dates lies here.')

# the meatcutter and the fishmonger
O[5461] = obj('a leg of mutton', 'lamb leg mutton', 'A stringy leg of mutton lies here.')
O[5462] = obj('a side of beef', 'beef side', 'A side of salted beef lies here.')
O[5463] = obj('a plucked chicken', 'chicken whole plucked', 'A scrawny plucked chicken lies here.')
O[5484] = obj("a butcher's cleaver", 'cleaver meat butcher', "A heavy butcher's cleaver lies here.")
O[5464] = obj('a salted herring', 'herring salted', 'A salted herring lies here.')
O[5465] = obj('a mussel', 'mussel muscle', 'A black mussel lies here.')

# drink
O[5467] = obj('a glass of blue oasis', 'glass liquor blue oasis whisky', 'A glass of strong blue spirit rests here.')
O[5468] = obj('a glass of sour wine', 'glass wine', 'A glass of sour wine rests here.')
O[5469] = obj('a bottle of grog', 'bottle grog ale', 'A bottle of cheap grog lies here.')
O[5475] = obj('a flaming scorpion', 'bottle scorpion flaming beer', 'A bottle of strong, peppery beer lies here.')
O[5476] = obj('a barrel of beer', 'barrel beer', 'A barrel of thin beer lies here.')
O[5477] = obj('a shot of whisky', 'shot whisky', 'A shot of rough spirit lies here.')

# the potion seller
O[5470] = obj('a glowing blue vial', 'vial glowing blue', 'A glowing blue vial lies here.',
              extras={'vial glowing blue': "The bluish liquid inside glows with a soft, steady light. A small label reads 'Protection', and someone has added in pencil: 'for the road'."})
O[5471] = obj('a deep-green potion', 'potion green', 'A deep-green potion lies here.',
              extras={'potion green': "The potion is a murky green. A small label reads 'Curative'."})
O[5472] = obj('a crystal clear potion', 'potion crystal clear', 'A crystal clear potion lies here.',
              extras={'potion crystal clear': "The bottle holds a liquid clear as spring water. Its label reads 'Preparation'."})
O[5473] = obj('an off-white potion', 'potion white', 'An off-white potion lies here.',
              extras={'potion white': "A thick, whitish liquid. A small label reads 'Redemption', and under it, 'take before the march'."})
O[5474] = obj('a dark blue potion', 'potion dark blue', 'A dark blue potion lies here.',
              extras={'potion dark blue': "This dark blue potion bears a small label reading 'Restoration'."})

# the wand seller
O[5478] = obj('a scroll of recall', 'scroll recall', 'A scroll of recall, sealed with a black flame, lies here.')
O[5479] = obj('a grey-silver wand', 'wand grey silver', 'A grey-silver wand lies here.',
              extras={'wand grey silver': 'A small storm cloud is engraved at the base of the wand.'})
O[5480] = obj('a wand of glinting yellow', 'wand yellow', 'A wand of glinting yellow lies here.',
              extras={'wand yellow': 'At the base of the wand a shape seems to fade slowly in and out of sight.'})
O[5481] = obj('an oak wand', 'wand oak', 'A wand of dark oak lies here.')
O[5482] = obj('a pink wand', 'wand pink', 'A pale pink wand lies here.')

# workmen's tools and the smith's stock
O[5485] = obj("the foreman's steel pen", 'pen steel fountain', 'A sharp steel-nibbed pen lies here.')
O[5486] = obj('a sledge hammer', 'hammer sledge', 'A mason\'s sledge hammer lies here.')
O[5487] = obj('a horse shoe', 'shoe horse horseshoe', 'An iron horse shoe lies here.')
O[5488] = obj('a saddle', 'saddle', 'A worn cavalry saddle lies here.')
O[5489] = obj('a riding crop', 'crop riding', 'A riding crop lies here.')
O[5490] = obj('a marble chessboard', 'chessboard board marble', 'A heavy marble chessboard lies here.')

# special arms
O[5492] = obj('the Grief of Thalos', 'spear grief thalos', 'A long, beautiful spear lies on the ground here.',
              extras={'spear grief thalos': 'The spear is nearly eight feet long, its silver blade tapering to the finest point you have ever seen. It was carried out of the old city by its last captain, and the haft is notched once for every year since.'})
O[5495] = obj('the wolverine claw', 'claw wolverine', 'A long, hooked claw lies here.')
O[5496] = obj('the wrath of the Flame', 'wrath mace flame', 'A large ornate mace floats above the ground here.',
              extras={'wrath mace flame': 'A huge mace of bronze, its head wrought like a burning flame. It is warm to the touch, and it looks as though it could break anything that came out of the dark.'})

RETHEME = {'rooms': R, 'objs': O}
