"""The High Tower of Magic (zone 25) re-themed as the war-college of battle mages.

The tower stands in a warded mistwood on the plains below the hills of Kar-Dumhal,
reached by a faint trail from the copse in zone 40.  It trains war-magi for
the wall at Midgaard, and it keeps, behind obsidian and wards, the dangerous
things brought back from the west.  Some floors are sealed because experiments
went wrong.  An old escape-way at the very top drops through a blue light into
the temple of Midgaard (3001).

Floors, bottom to top:
  the Mistwood (2500-2511)     -- an illusion-maze the tower keeps round itself
  the ground floor (2512-2520) -- gate, muster hall, refectory, tavern, stores
  the undercroft (2521-2529)   -- cells for things that came back wrong
  the officers' wing (2515, 2530-2539) -- quarters for magi back from the wall
  the novice floor (2540-2547) -- apprentice barracks
  the lecture halls (2548-2568) -- drill rooms, amphitheatre, masters' rooms
  the floor of making (2569-2598) -- scriptorium, forge, alchemy, summoning, pens
  the binding floor (2599-2628) -- spellbinder, golems, illusion, the sealed wing
  the warding galleries (2629-2649) -- obsidian vaults of things taken from the west
  the crown (2650-2683)        -- the three orders and the Archmagus
Levels unchanged (18-30).
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs




# ============================================================ the Mistwood
R[2500] = dict(name='The Edge Of The Mistwood', desc="""
    The trail from the copse ends here against a wall of grey mist that does not
    move with the wind.  Old trees stand half-seen inside it, their bark pale as
    bone.  A post of black iron is driven into the ground at the edge, hung with
    a board.  The air is cold and smells faintly of struck flint.  A narrow path
    goes north into the mist; the copse lies back to the south.""",
    extras={'post board iron': 'The board is painted in plain letters: "WAR-COLLEGE OF THE HIGH TOWER. The wood is warded. Keep to the path. Those who leave it are not looked for."'},
    exits={'n': 'Grey mist, and the pale shapes of trees inside it.',
           's': 'The copse of trees and the open plains lie back to the south.'})
R[2501] = dict(name='The Mistwood', desc="""
    The mist is thick enough to taste.  Grey trunks crowd in on every side, and
    a ring of white stones has been laid on the ground here, as if to mark a
    place where something was buried, or where something should stay.  Faint
    growling comes from nowhere in particular.  Paths, or what may be paths,
    lead north, east, south and west.""",
    extras={'ring stones white': 'Smooth white river stones, each one scratched with a small ward-sign. Two of them have been kicked out of the ring.'},
    exits={d: 'The mist swallows the path a few steps on.' for d in 'nesw'})
R[2502] = dict(name='The Mistwood', desc="""
    A tall tree here has been split by fire from crown to root, and the two
    halves lean apart like an open door.  Something has scratched marks into
    the burnt wood at the height of a man's face.  The mist is a little thinner
    to the north, where there may be a clearing.  Other ways run east, south
    and west into grey.""",
    extras={'tree marks burnt': 'Tally marks, dozens of them, scratched with a knife or a nail. Someone was counting days here.'},
    exits={'n': 'The mist thins a little; there may be a clearing that way.',
           'e': 'Grey mist and grey trees.', 's': 'Grey mist and grey trees.', 'w': 'Grey mist and grey trees.'})
R[2503] = dict(name='The Mistwood', desc="""
    The ground dips into a hollow full of dead leaves, and the mist pools in it
    like water.  A rusted helmet lies at the bottom, upside down, holding a
    little rainwater.  There is no sign of whoever wore it.  The moaning in the
    trees is louder here.  Ways lead off north, east, south and west, and every
    one of them looks the same.""",
    extras={'helmet helm rusted': 'An old levy helmet of the kind the Recruit Yards hand out. The strap has been cut, not broken.'},
    exits={d: 'The mist hides whatever lies that way.' for d in 'nesw'})
R[2504] = dict(name='The Mistwood', desc="""
    A bell of green bronze hangs from a low branch on a rotten cord, without a
    clapper.  The tower's mages hang them through the wood to mark the safe
    paths, but the mist moves the paths and not the bells.  Wet roots knot
    across the ground.  Shapes in the grey suggest ways north, east, south and
    west.""",
    extras={'bell bronze cord': 'The bell has no clapper. When the mist stirs it moves, but it makes no sound at all.'},
    exits={d: 'Trees loom and fade in the mist.' for d in 'nesw'})
R[2505] = dict(name='The Mistwood', desc="""
    The trees here grow in a near-perfect circle, as if planted, and the mist
    inside the circle is darker than the mist outside it.  A cold that has
    nothing to do with the weather settles on the skin.  Shadows move between
    the trunks a little after the trees do.  Paths lead north, east, south and
    west between the trunks.""",
    exits={d: 'Something dark moves in the grey that way, then is gone.' for d in 'nesw'})
R[2506] = dict(name='The Mistwood', desc="""
    A stake of black ash wood stands here, charred at the tip and carved with
    a ward-sign that has been scored through with a deep scratch.  The grass
    round it is dead in a perfect circle.  To the west the mist seems to open
    onto a clearing; north, east and south it is as thick as ever.""",
    extras={'stake ash ward sign': 'One of the tower\'s ward-stakes. Something has drawn a line through the ward with a claw, and the wood beneath the cut has gone grey.'},
    exits={'w': 'The mist parts a little onto a clearing.',
           'n': 'Grey mist and grey trees.', 'e': 'Grey mist and grey trees.', 's': 'Grey mist and grey trees.'})
R[2507] = dict(name='The Mistwood', desc="""
    The bones of a slender man lie under a tree here, wrapped in a dark cloak
    that the damp has not rotted.  A curved knife is still in his hand.  The
    mages left him where he fell as a warning to others of his kind.  The mist
    goes on to the north, east, south and west.""",
    extras={'bones cloak man': 'The skull is long and narrow and the cloak is of drow weave, black on black. A spy for the west, come to look at the tower. He did not get far.'},
    exits={d: 'Pale trunks and grey mist.' for d in 'nesw'})
R[2508] = dict(name='The Mistwood', desc="""
    Close to the edge of the wood the mist is thinner, and the trees have been
    marked with daubs of white paint at head height, some of them very old.  A
    trodden track seems to bend away south toward the wood's edge.  Other ways
    lead north, east and west into thicker grey.""",
    extras={'paint daubs marks': 'White daubs, each one a ward-sign. The newest are fresh; the oldest have weathered almost away.'},
    exits={'s': 'The mist is thinner that way, toward the edge of the wood.',
           'n': 'Grey mist and grey trees.', 'e': 'Grey mist and grey trees.', 'w': 'Grey mist and grey trees.'})
R[2509] = dict(name='The Mistwood', desc="""
    A fallen tree lies across the ground here, and someone has built a lean-to
    of branches against it and then abandoned it.  A cold fire-pit holds the
    burnt ends of what looks like a map.  The growling seems very close.  Ways
    lead north, east, south and west through the trees.""",
    extras={'lean-to fire pit map': 'Scraps of a hand-drawn map of the wood, every path crossed out in turn. The last scrap only says, in a shaking hand, "they move".'},
    exits={d: 'The grey closes in that way.' for d in 'nesw'})
R[2510] = dict(name='The Mistwood', desc="""
    The trees stand further apart here, and their roots have been scorched
    black.  To the east the shadows draw back and something like a clearing
    can be seen.  Elsewhere the mist hangs in heavy folds, hiding the ways
    north, south and west.""",
    exits={'e': 'The shadows draw back to show a small clearing.',
           'n': 'Grey mist and grey trees.', 's': 'Grey mist and grey trees.', 'w': 'Grey mist and grey trees.'})
R[2511] = dict(name='A Burnt Clearing', desc="""
    A clearing of charred grass where nothing has grown back.  The war-magi
    burn this ground every spring so that nothing can hide close to the tower.
    The mist stands in a wall around the edges, east, south and west, and
    goes no further in.  A paved path leads north toward a dark shape rising
    out of the grey.""",
    exits={'n': 'A paved path runs north toward the foot of a great tower.',
           'e': 'The mist stands like a wall.', 's': 'The mist stands like a wall.', 'w': 'The mist stands like a wall.'})

# ============================================================ the ground floor
R[2512] = dict(name='Before The Diamond Gate', desc="""
    The High Tower rises out of the mist above you, black stone without a
    window for the first hundred feet, until it vanishes into low cloud.  Scorch
    marks streak the lower courses where something once tried to burn its way
    in.  A gate of cut diamond, clear as ice and set with ward-runes, closes the
    doorway to the north.  The path behind has already gone back into the
    mist.""",
    extras={'scorch marks courses': 'Long black streaks in the stone, as if from fire that ran upward. The masons have never been able to scrub them out.'},
    exits={'n': 'The diamond gate is clear as ice, and very strong.'})
R[2513] = dict(name='The Gate Hall', desc="""
    Inside, the tower is far larger than its walls allow; the war-magi fold
    space as easily as cloth.  The gate hall is a long vault hung with the
    banners of regiments the college has sent mages to.  Apprentices in grey
    hurry past with books and satchels.  The muster hall is north, a corridor
    runs east, the refectory lies west, and the diamond gate is south.""",
    extras={'banners banner regiments': 'Faded regimental banners: the Second of the Wall, the Ashford Levy, the Riversmeet Foot. A black thread is tied round the staff of every one.'})
R[2514] = dict(name='The Muster Hall', desc="""
    The great common room of the college, where apprentice war-magi rest
    between drills.  They sit at long tables comparing notes, playing at dice,
    or staring at nothing.  A board on the wall lists who is posted west next.
    A small stone fountain splashes in one corner.  A dim passage leads north,
    the tavern is east, the quartermaster's shop west and the gate hall
    south.""",
    extras={'board list': 'A list of names in chalk under the heading POSTED TO THE WALL. Some have been wiped off and written again. Some have been wiped off.',
            'fountain': 'Clean water, drawn from a deep well. Someone has carved "drink while you can" into the rim.'})
R[2515] = dict(name='The Corridor Of Names', desc="""
    A plain corridor whose walls are covered from floor to ceiling in small
    painted names, one for every war-magus the college has lost on the march.
    The newest are at the eastern end, where the painters are still at work.
    The corridor runs east toward the officers' wing and west to the gate
    hall.""",
    extras={'names wall walls': 'Thousands of names, small and neat. Beside some of them a second mark has been painted: a grey eye. Nobody will say what it means.'})
R[2516] = dict(name='The Refectory', desc="""
    A long hall of trestle tables that could seat several hundred.  At meal
    times it is full and loud; now it is empty, the benches pushed in, and the
    only sound is something bubbling beyond the kitchen door.  Every table has
    a ration-mark burnt into its end.  The kitchen door is west; the gate hall
    lies east.""")
R[2517] = dict(name='A Disused Passage', desc="""
    A narrow passage that nobody seems to use.  Dust lies thick on the floor,
    and in the dust are a few footprints that go one way only.  The outline of
    a trapdoor can be made out underfoot, its iron ring polished by use.  The
    muster hall lies back to the south.""",
    extras={'trapdoor ring': 'A heavy trapdoor with a polished iron ring. Somebody uses it, even if the dust says otherwise.',
            'footprints prints dust': 'Booted prints, going toward the trapdoor. None come back.'})
R[2518] = dict(name='The Drowned Lamp Tavern', desc="""
    The college's tavern, smoky and low, where the masters let the students
    drink because they will be at the wall soon enough.  Cups float from the
    bar to the tables on their own.  Nobody looks up as you come in; they have
    their own thoughts to drown.  The only way out is west.""",
    extras={'sign': 'A board behind the bar: "Herbal brew for the head. Bread for the road. Nothing for the dreams."'})
R[2519] = dict(name="The Quartermaster Of Reagents", desc="""
    The college's store, crammed with herbs, chalk, parchment, candles and
    sealed jars, everything a war-magus needs in the field.  Each item carries
    the tower's mark and the date it was issued.  A ledger of debts lies open
    on the counter.  The only exit leads back east.""",
    extras={'ledger debts': 'A ledger of what each student owes the store. Beside many names the debt has been struck through and the word "wall" written in.'})
R[2520] = dict(name='The Kitchen', desc="""
    A hot, crowded kitchen.  A black oven twelve feet high squats against one
    wall, and opposite it stands an iron meat locker large enough to hold a
    man, and perhaps it has.  A spice rack hangs in mid-air in the middle of
    the room, turning slowly.  The cooks here are mages too, and they do not
    like visitors.  The wooden door east leads back to the refectory.""")

# ============================================================ the undercroft
R[2521] = dict(name='Below The Trapdoor', desc="""
    A cramped shaft beneath the floor, dark and smelling of damp stone.  A
    little grey light leaks down through the trapdoor above.  Water drips
    somewhere far below, slow and steady, and a rope ladder hangs down into
    the dark.""")
R[2522] = dict(name='The Undercroft Crossing', desc="""
    A low vaulted crossing in the cellars of the tower, where the college keeps
    what it does not want upstairs.  The walls sweat.  Running water can be
    heard to the south, and a faint light glows down the passage east.  Other
    passages lead north and west, and the ladder climbs back up.""",
    exits={'e': 'A faint light shows at the far end of the passage.'})
R[2523] = dict(name='Before The Cell Door', desc="""
    The passage ends at a stout oak door to the north, bound with iron and painted with a
    ward-sign in red.  Under the sign someone has chalked the words DO NOT
    ANSWER HIM.  There is a slot at the bottom for food.  The only other way is
    back south.""",
    extras={'sign ward words chalk': 'DO NOT ANSWER HIM, in a careful hand. Below, in another hand: "Whatever he says."'})
R[2524] = dict(name='The Jailor\'s Passage', desc="""
    A dark passage ending in a door to the east that stands half open, soft
    lamplight showing round its edges.  Loud snoring comes from beyond it.  A
    row of iron hooks along the wall holds manacles of several sizes, some of
    them not made for human wrists.  The crossing lies back west.""",
    extras={'hooks manacles': 'Manacles of many sizes. One pair is long and thin, with too many joints in the cuff.'})
R[2525] = dict(name='The Midden Pool', desc="""
    A black pool fills the end of this cellar, and the stench of it is
    enough to make the eyes water.  The kitchens and the laboratories both
    empty their waste down here.  Things float in it that are better not looked
    at, and something gurgles beneath the surface.  The crossing lies north;
    the only other way is down, into the water.""",
    exits={'d': 'No light reaches below the surface of the pool.'})
R[2526] = dict(name='The Fallen Passage', desc="""
    The passage ends in a great fall of broken stone and earth that fills it
    from floor to roof.  The masons say it was not an accident: something dug
    up toward the tower from the deep tunnels under Kar-Dumhal, and the masters
    brought the roof down on it.  Scratching can still be heard in the stone on
    some nights.  The only way out is back east.""",
    extras={'stone fall rubble earth': 'Broken stone, packed tight. In one gap a grey claw, long dead, is pinned between two blocks.'})
R[2527] = dict(name='The Muzzled Man\'s Cell', desc="""
    A black cell floored with filthy straw.  A man is chained to the far wall
    by wrists, ankles and neck, and an iron muzzle is locked over his mouth.
    The walls around him have been scratched with marks that hurt the eyes to
    follow.  The only exit is the oak door back south.""",
    extras={'walls marks scratches': 'Lines that bend the wrong way. They look a little like the ward-signs upstairs, turned inside out.'})
R[2528] = dict(name='The Jailor\'s Office', desc="""
    A cluttered office with a cot, a lamp and a table covered in bread crusts
    and unsigned release papers.  The jailor sleeps a great deal; very few of
    the things kept down here need feeding for long.  A ring of hooks by the
    door is empty except for one.  The only exit is the door west.""",
    extras={'papers release': 'Release orders, all of them blank. Nobody has ever been released from the undercroft.'})
R[2529] = dict(name='Beneath The Midden Pool', desc="""
    The filthy water closes overhead and a current takes hold at once, pulling
    down and sideways into a drain no mage ever meant anyone to swim.  There is
    no light and no air.  The pull goes on, and on, and the cold reaches into
    the chest and stays there.""")

# ============================================================ the officers' wing
R[2530] = dict(name='The Officers\' Wing', desc="""
    The corridor widens where the officers' wing begins.  Here war-magi home
    from the wall are given beds, and the walls glow with a dim, steady ward-
    light so that nobody need sleep in the dark.  There are wooden doors north
    and south; the corridor goes on east and back west.""")
R[2531] = dict(name='A Turn In The Officers\' Wing', desc="""
    The corridor turns here around a pillar carved with the college's sign, a
    hand holding a flame.  Three wooden doors open off it: north, east and
    south.  The way back runs west.  A ward-light burns in a niche, and
    someone has left a cup of cold tea beside it.""",
    extras={'pillar sign hand flame': 'A hand holding a flame, carved in black stone. The motto under it is worn almost smooth: "We burn so the wall may stand."'})
R[2532] = dict(name='A Linen Store', desc="""
    A narrow store room of shelves stacked with folded blankets, spare robes and
    boxes of candle ends.  Some of the robes are scorched or stained and have
    been folded anyway, as if their owners might come back for them.  The only
    way out is the door south.""",
    extras={'robes robe': 'Grey robes with names stitched inside the collars. Several are stiff with old blood.'})
R[2533] = dict(name='A Broom Closet', desc="""
    A dark closet full of brooms, mops and buckets.  The brooms were enchanted
    long ago to sweep the officers' wing by themselves, and the enchantment has
    gone sour; they are now kept shut in here.  Several of them are leaning
    toward the door.  The only exit is north.""")
R[2534] = dict(name='The Officers\' Corridor', desc="""
    A quiet corridor lit by the warm glow of the walls.  The doors here are
    hung with small slates bearing the names of whoever sleeps behind them, and
    most of the slates are blank.  A wooden door leads east, another south, and
    the corridor runs on north.""",
    extras={'walls wall': 'The walls shed a warm, even light, a small mercy for men who have come back from the dark.',
            'slates slate': 'Most are wiped clean. One still reads "Corvan, 3rd Battle-Circle, back by midwinter."'})
R[2535] = dict(name='The Wardens\' Chamber', desc="""
    A bare chamber with no furniture, because its keepers have no need of any.
    Disembodied hands and eyes drift here between their rounds, bound into the
    tower's service by the masters long ago.  The air prickles.  The only way
    out is the door to the north.""")
R[2536] = dict(name='A Guest Bedroom', desc="""
    A small bare room with a cot in one corner and a dusty mirror on the wall.
    Nobody has slept here in a long while.  The bedding is folded at the foot
    of the cot and has not been touched.  The only door leads back west.""",
    extras={'mirror': 'Someone seems to be looking back at you from the other side, a thin grey figure standing a little behind where your reflection should be. When you turn round there is no one there.'})
R[2537] = dict(name='A Guest Bedroom', desc="""
    A comfortable room with a small globe of ward-light floating under the
    ceiling, a washstand and a cot with real blankets.  Someone is sleeping in
    the cot, still half in his travelling clothes, his boots muddy from the
    road.  The only door leads back west.""")
R[2538] = dict(name='The Foot Of The Novice Stair', desc="""
    The officers' corridor ends here at the foot of a broad stair that climbs
    to the novices' floor.  A charred door is set in the east wall, and a smell
    of old smoke still comes from under it.  The corridor runs back south.""")
R[2539] = dict(name='The Burnt Room', desc="""
    This was a guest room once.  The walls are black with soot and the bed is a
    heap of ash, and the floor is scorched in the shape of a man lying on his
    side.  A war-magus came back from the west here and slept, and in the
    night the fire in him came out.  The only exit is the charred door west.""",
    extras={'floor shape scorch': 'A pale outline on the black floor where something lay while everything around it burned.'})

# ============================================================ the novice floor
R[2540] = dict(name='The Novice Landing', desc="""
    The stair comes up onto the novices' floor.  The corridor smells of ink and
    sweat and cheap candles.  An oak door north opens on the barracks, faint
    moonlight shows in a small alcove to the east, and the corridor runs on
    west.  The stair leads back down.""",
    exits={'e': 'Faint moonlight falls into a small alcove that way.'})
R[2541] = dict(name='The Window Alcove', desc="""
    A small alcove ending in a tall window to the east, its glass long gone,
    letting in a cold breeze and the moonlight.  The novices come here to look
    out at a world they have not yet been sent into.  Initials are carved deep
    into the sill.  The only way out is back west.""",
    extras={'window': 'Below, the grey mistwood spreads in every direction like a sea. Beyond it lie dark hills, and far off the small lights of the eastern farms that feed the wall.',
            'sill initials': 'Hundreds of initials, carved over many years. Some of them match names in the Corridor of Names below.'},
    exits={'e': 'Below, the grey mistwood spreads out like a sea, and far beyond it lie the small lights of the eastern farms.'})
R[2542] = dict(name='The Novice Barracks', desc="""
    Rows of narrow cots line the walls.  Apprentices sit cross-legged on them,
    muttering cantrips or bent over books by the light of a single conjured
    spark each.  Their kit is stacked at the foot of every bed, ready to go.
    The room runs on west, and an oak door leads back south.""")
R[2543] = dict(name='The Novice Corridor', desc="""
    A corridor scuffed by hundreds of young feet.  Lesson rotas are pinned
    along the walls, and someone has drawn a rude sketch of a master on one of
    them.  An oak door leads north, and the corridor runs east and west.""",
    extras={'rotas rota sketch': 'The rotas list drills by hour: wards at dawn, fire at noon, blade at dusk. The sketch shows a master with a very large nose.'})
R[2544] = dict(name='The Novice Barracks', desc="""
    The far end of the barracks, where the youngest apprentices sleep.  Some of
    them are no more than children, sent by families in the refugee camps who
    could not feed them.  A few have hung charms over their beds.  The room
    runs back east, and an oak door leads south.""",
    extras={'charms charm': 'Little twists of straw and ribbon, the kind mothers make in the east to keep the dark away from a sleeping child.'})
R[2545] = dict(name='Outside The Workshop', desc="""
    The corridor runs east and west past an oak door to the north.  Flashes of
    blue light show under it, followed by small cries and giggling.  A bucket
    of sand stands by the door, and a sign above it says FIRE.""",
    extras={'sign bucket sand': 'A bucket of sand under a sign: FIRE. It has clearly been used more than once.'},
    exits={'n': 'A flash of blue light shows round the edges of the door.'})
R[2546] = dict(name='The Novices\' Workshop', desc="""
    A small workshop of scarred tables strewn with chalk, parchment and
    snapped wands.  In the far corner a knot of young apprentices has a small
    kitten cornered, and they are trying spells on it.  The room reeks of singed
    fur.  The only door leads back south.""")
R[2547] = dict(name='A Turn In The Novice Corridor', desc="""
    The corridor turns south toward the lecture halls.  A notice nailed to the
    corner reads SILENCE BEYOND THIS POINT, and below it, smaller, LECTURES IN
    PROGRESS.  The way back runs east.""",
    extras={'notice': 'SILENCE BEYOND THIS POINT. LECTURES IN PROGRESS. A third line has been scratched out.'})

# ============================================================ the lecture halls
R[2548] = dict(name='The Hall Of Lectures', desc="""
    A tall corridor of black stone lined with closed doors.  The voices of
    masters drone behind them, reciting the words of the burning bolt and the
    lesser ward over and over.  A metal door to the west is marked FIRST DRILL.
    The hall runs north and south.""")
R[2549] = dict(name='The First Drill Room', desc="""
    A classroom of benches facing a scorched target wall.  Bored students
    slump at their desks while the instructor drills them in the bolt of force,
    a spell every war-magus must cast a hundred times without thinking before
    he is sent west.  The instructor does not like to be interrupted.  The only
    exit is the metal door east.""",
    extras={'target wall': 'A wall of stone pocked with thousands of small craters, one for every bolt cast here.'})
R[2550] = dict(name='The Hall Of Lectures', desc="""
    The hall goes on north and south.  Beside a metal door to the west, a
    student has been made to stand facing the wall, and has been forgotten;
    only the scuff marks of his feet remain.  Chalk dust drifts in the air.""")
R[2551] = dict(name='The Hall Of Lectures', desc="""
    Here the hall is hung with charts showing the march: fifteen bands of
    country between the wall and the west, each one coloured darker than the
    last.  A metal door leads west.  The hall runs north and south.""",
    extras={'charts chart march': 'Fifteen bands from Midgaard to the west, the last almost black. Across the bottom a master has written: "Every band you hold is a band they do not."'})
R[2552] = dict(name='The Empty Drill Room', desc="""
    An empty classroom.  A blackboard hangs in the air at the front, covered in
    sigils that nobody has wiped away, and the desks have been pushed back
    against the walls as though something was drawn on the floor and then
    scrubbed out.  The only exit is the metal door east.""",
    extras={'blackboard sigils board': 'The sigils of a binding, half finished. The last one has been written over and over until the chalk broke.',
            'floor': 'Faint lines of a scrubbed-out circle still show between the boards.'})
R[2553] = dict(name='A Turn In The Hall Of Lectures', desc="""
    The hall turns here from north to east.  A brass bell hangs from a bracket
    to mark the hours of the drills, its rope worn thin.  The walls glow with a
    steady ward-light.""",
    extras={'bell brass rope': 'The hour bell. The college rings it eight times for the end of a drill and once, slowly, when news comes back from the wall.'})
R[2554] = dict(name='The Veiling Room', desc="""
    At first glance the classroom is empty: rows of desks, a lectern, a cold
    lamp.  Then there is the rustle of robes, a chair that moves by itself, and
    the sense of being watched.  The students of the veil are practising, and
    so is their teacher.  The only exit is the metal door east.""")
R[2555] = dict(name='The Hall Of Lectures', desc="""
    The hall runs east and west here.  A sturdy iron door to the south leads to
    the amphitheatre, and a slate beside it gives the day's lecture: THE
    NATURE OF THE GREY.  The ward-light is brighter here, as if the walls were
    listening too.""",
    extras={'slate lecture': 'THE NATURE OF THE GREY: what it takes from the living, and how to keep it out. Attendance compulsory.'})
R[2556] = dict(name='The Hall Of Lectures', desc="""
    The hall runs east and west.  The thud of blows and the stamp of feet come
    through a large oaken door to the south, and the floor here is scuffed with
    the boots of students limping out of it.""")
R[2557] = dict(name='The Amphitheatre', desc="""
    A small amphitheatre of stone tiers rising round a podium.  The acoustics
    are so fine that every footstep rings, and an old wizard at the podium is
    speaking of the west in a voice barely above a whisper.  Nobody in the
    tiers is moving.  The only exit is the iron door north.""")
R[2558] = dict(name='The Hall Of Lectures', desc="""
    The hall runs east and west.  The walls here are scorched in streaks, and
    a small door to the south has been reinforced with iron bands.  Beside it a
    rack holds wet cloths for burns.""",
    extras={'rack cloths': 'Wet cloths, and a jar of grease. The duellists come out of the south door and reach for them without looking.'})
R[2559] = dict(name='The Blade Yard', desc="""
    A long hall of packed sand set out with battle-scarred dummies.  A war-magus
    who runs out of spells on the march has only his knife, and here the young
    mages learn to use it.  The battle mistress walks among them, correcting
    grips.  The only exit is the door north.""",
    extras={'dummies dummy': 'Straw dummies dressed in rags of grey, each with a crude face painted on. The faces have no eyes.'})
R[2560] = dict(name='A Turn In The Hall Of Lectures', desc="""
    The hall turns from west to north.  The noise of the drill rooms fades
    behind, and the floor is carpeted from here on, a sign of the masters'
    quarters.  A row of hooks holds wet cloaks.""")
R[2561] = dict(name='The Duelling Room', desc="""
    A bare room for duels of spell against spell.  The walls, floor and ceiling
    are scarred black by fire and crazed by frost, but they were built to hold
    and they hold.  A war-magus learns here what it is to be struck by a spell,
    so that it will not surprise him in the west.  The only exit is the small
    door north.""")
R[2562] = dict(name='The Masters\' Corridor', desc="""
    A carpeted corridor where the teaching masters live.  It is quieter here,
    and warmer.  A door to the east leads to the masters' lounge, and the
    corridor runs north and south.""")
R[2563] = dict(name='The Masters\' Corridor', desc="""
    Portraits of former masters line the corridor, each with a small brass
    plate giving the years of teaching and, for most of them, the place on the
    march where they fell.  A wooden door leads east, and the corridor runs
    north and south.""",
    extras={'portraits portrait plates plate': 'Stern faces in oils. "Master Iselde, the Fens." "Master Orrin, the Barrow Hills." "Master Hal, Ashford." The newest frame is empty.'})
R[2564] = dict(name='The Masters\' Lounge', desc="""
    A large comfortable lounge of deep chairs and low tables, where teachers
    rest between drills.  A great copper urn of bitter black tea simmers
    against the far wall, and the masters drink it to stay awake through the
    night watches.  The only exit is the wooden door west.""",
    extras={'urn copper tea': 'A copper urn of black tea, kept hot by a small rune on its base. It tastes of tar.'})
R[2565] = dict(name='The Senior Master\'s Bedchamber', desc="""
    A large, plush bedroom belonging to a master of standing.  An ice mirror
    hangs on one wall, and a scrying globe sits on a stand, clouded grey.  The
    bed floats a yard above the floor, because the master no longer trusts
    what might be under it.  The only exit is the wooden door west.""",
    extras={'mirror ice': 'A mirror of ice that never melts. It shows the room, but not the bed.',
            'globe scrying': 'The globe is clouded grey, and the cloud moves as if something on the other side were pressed up against it.'})
R[2566] = dict(name='The Masters\' Corridor', desc="""
    The corridor runs north and south.  A glass door to the east shows a
    lamplit study beyond.  A small shrine in the wall here holds a cold candle
    for each master posted west this year.""",
    extras={'shrine candle candles': 'Seven candles, cold. The masters light one only when its owner comes home.'})
R[2567] = dict(name='The Map Study', desc="""
    A small study lined with old books.  A great table fills the middle of
    the room, spread with maps of the march weighted down with stones, and
    pins mark where the war-magi are posted.  The only light is a plain oil
    lamp; the masters say spell-light draws the eye of the west.  The only exit
    is the glass door west.""",
    extras={'maps map pins table': 'Maps of the fifteen bands west of Midgaard, drawn and redrawn. Black pins mark posts that have gone silent. There are a great many black pins.'})
R[2568] = dict(name='Below The Upper Stair', desc="""
    The corridor ends at the foot of a narrow stair climbing to the upper
    floors, where only masters and their chosen go.  A pair of disembodied
    hands keeps silent watch on it, and a wooden golem stands beside the first
    step.  The corridor runs back south.""")

# ============================================================ the floor of making
R[2569] = dict(name='The Head Of The Upper Stair', desc="""
    The stair comes up into the floor of making, where the college's scrolls,
    blades, potions and bindings are made for the wall.  The halls here are
    little used and smell of hot metal, ink and sulphur.  The walls give off a
    faint blue light.  A corridor leads west, and the stair goes back down.""")
R[2570] = dict(name='The Scriptorium Corridor', desc="""
    A long corridor running east and west, its floor spotted with old ink.
    A thick wooden door to the north is marked with a quill.  The faint scratch
    of many pens comes from behind it, steady as rain.""")
R[2571] = dict(name='The Scriptorium', desc="""
    A calligrapher's office crowded with desks, quills, inkpots and drying
    parchment.  Scribes copy out ward-scrolls by the hundred for the wall, and
    translate the few written things brought back from the west, which they do
    slowly and with their eyes half shut.  A curtain to the west glows with
    candlelight; the wooden door is south.""",
    extras={'parchment parchments': 'Ward-scrolls, all the same. One sheet on the end desk is not a ward: it is a copy of grey writing that crawls when you look away.'})
R[2572] = dict(name='The Scriptorium Corridor', desc="""
    The corridor runs east and west.  Racks along the walls hold rolled scrolls
    waiting to be sent down to the quartermaster, each one tagged with the name
    of a regiment.""",
    extras={'racks scrolls tags': 'Tags for the Second of the Wall, the Riversmeet Foot, the Fenwatch. Some tags have been crossed out and the scrolls left to gather dust.'})
R[2573] = dict(name='The Master Scribe\'s Workshop', desc="""
    The master scribe's workshop, where the greatest scrolls are written.
    Half-finished sheets cover a writing table, held down by lumps of lead.  A
    giant candle burns with a soft blue flame that gives light but no heat,
    so that nothing here can catch.  The only way out is back through the
    curtain east.""",
    extras={'candle blue': 'A candle as thick as a man\'s waist, its blue flame perfectly still.'})
R[2574] = dict(name='The Corridor Of Stores', desc="""
    A long corridor running east and west.  A half-closed wooden door to the
    north leads into darkness, and the air coming through it is cold and stale.
    Something heavy has been dragged along the floor here, leaving two long
    grooves.""",
    exits={'n': 'A dark room shows through the half-open door.'})
R[2575] = dict(name='A Dark Store Room', desc="""
    A small, cold store room with shelves of common stock: candles, chalk,
    twine, sealing wax.  None of it looks worth the pair of disembodied eyes
    that hangs in the dark, watching the door.  Perhaps the eyes are not here
    for the shelves.  The only exit is the door south.""")
R[2576] = dict(name='A Turn In The Corridor Of Stores', desc="""
    The corridor bends from east to south.  The ring of hammers comes faintly
    from further south, and the stone underfoot is warm.  Someone has painted
    an arrow on the wall and the word FORGE.""")
R[2577] = dict(name='Outside The Metal Store', desc="""
    The corridor runs north and south.  An iron-bound door to the west is
    locked and warded, and a brass plate on it reads METALS: BY ORDER OF THE
    ENCHANTER.  The heat is stronger here.""",
    extras={'plate brass': 'METALS. BY ORDER OF THE ENCHANTER. A smaller line beneath: "Silver is counted."'})
R[2578] = dict(name='Outside The Forge', desc="""
    The corridor runs north and south.  Behind an iron door to the west comes
    the sharp ring of metal on metal, and a red light flickers under the door.
    The stone of the wall is hot to the touch.""")
R[2579] = dict(name='The Metal Store', desc="""
    A large store room of bins full of ores, salt and rare earths, beside
    neat stacks of ingots.  A heavy cabinet carved with warding sigils is
    bolted to one wall.  The college needs silver above all things, for blades
    that bite the dead.  The iron door is east; the ring of the forge comes
    through another door to the south.""",
    extras={'bins ores': 'Ores from the Ironworks and the dwarven halls, each bin chalked with its weight and the day it came.'})
R[2580] = dict(name='The Corridor Of Stores', desc="""
    The corridor runs north and south.  Soot streaks the ceiling here, and a
    long crack runs along the floor, as if the forge's heat had once split the
    stone.""")
R[2581] = dict(name='The Enchanter\'s Forge', desc="""
    A furnace-hot room.  A great forge burns against one wall with a blue
    flame, and its smoke pours up into a vent in the ceiling.  A mithril anvil
    encrusted with runes stands in the middle, worn bright with use.  Tools
    hang from a rack that floats ten feet up.  Doors lead north to the metal
    store, east to the corridor, and south.""",
    extras={'anvil mithril runes': 'A mithril anvil, its runes worn by a hundred years of hammering silver into blades for the wall.',
            'vent ceiling': 'A grated vent above the forge. The grate can be swung open.'})
R[2582] = dict(name='The Master Enchanter\'s Chamber', desc="""
    The walls of the Enchanter's chamber are hung with racks of fine blades,
    each one with a ward-word etched near the hilt.  A huge chest with a glowing
    lock stands to one side, and unfinished swords lie on a small work table.
    Not all of them are lying quite still.  The only exit is the door north.""")
R[2583] = dict(name='A Turn In The Corridor Of Stores', desc="""
    The corridor bends from north to east.  A heap of cracked crucibles has
    been swept into the corner, and the smell changes here from hot iron to
    something sweet and rotten.""")
R[2584] = dict(name='The Alchemists\' Corridor', desc="""
    A corridor running east and west, stained yellow and green by years of
    spills.  A steel door to the south has been dented outward from within.
    A sign beside it reads LABORATORY: KNOCK AND WAIT.""",
    extras={'sign': 'LABORATORY: KNOCK AND WAIT. Underneath, in another hand: "Do not wait long."',
            'dent dents': 'The door is dented outward, as if something on the other side had struck it very hard.'})
R[2585] = dict(name='The Alchemists\' Corridor', desc="""
    The corridor runs east and west.  The air is thick and sweet and makes
    the head swim.  Small glass shards crunch underfoot, and someone has drawn
    a chalk line across the floor and written STAY EAST OF THIS on one side
    and nothing on the other.""")
R[2586] = dict(name='The Laboratory', desc="""
    A small laboratory with a workbench buried under instruments, vials and
    scrawled notes.  It looks abandoned, or kept by a madman: half the notes
    are formulae for draughts to be issued to the wall, and half are the same
    sentence written over and over.  A steel door leads north, and an opening
    leads east.""",
    extras={'notes': 'Recipes for healing draughts, carefully set out. And then, in a crabbed hand, hundreds of times: "it tastes grey it tastes grey it tastes grey".'})
R[2587] = dict(name='The Alchemists\' Corridor', desc="""
    The corridor runs east and west.  A steel door to the south is painted
    with a five-pointed star and the words SUMMONING IN PROGRESS.  The air
    hums and the hair on the arms stands up.""")
R[2588] = dict(name='The Mad Alchemist\'s Workroom', desc="""
    Bubbling braziers, coils of glass and scores of odd vials crowd every
    surface.  Broken glass carpets the floor.  The alchemist who works here
    once made the best healing draughts in the east; then he began to test
    potions brewed from things taken from the west, and he tested them on
    himself.  The only way out is back west.""")
R[2589] = dict(name='A Turn In The Alchemists\' Corridor', desc="""
    The corridor turns from west to north.  The humming from the summoning
    room fades, and a smell of straw and animals comes from further north.
    Someone has scratched a tally of days into the wall at knee height.""")
R[2590] = dict(name='The Pentagram Chamber', desc="""
    A five-pointed star is cut into the floor and filled with silver.  The
    Summoner stands within it, holding a gate open so the college can study
    what comes through, and kill it.  To the south a crackling field of energy
    fills the far end of the room.  The steel door is north.""",
    extras={'star pentagram floor silver': 'A star of inlaid silver, its points scorched. The silver is worn thin where something has scraped at it from inside.'},
    exits={'s': 'The energy field crackles and glows. Nothing can be seen beyond it.'})
R[2591] = dict(name='The Corridor Of Pens', desc="""
    The corridor runs north and south.  A bronze door to the east stands in a
    wall freshly painted white, and the smell of animals is stronger here.
    Feathers and tufts of fur drift along the floor.""")
R[2592] = dict(name='Inside The Energy Field', desc="""
    The world turns over and the stomach with it.  There is no floor, no wall,
    no door, only a crackling light that holds you like a fly in amber.  The
    Summoner made this to keep what he calls up; it does not care what it
    keeps.  There is no way out but magic.""")
R[2593] = dict(name='The Corridor Of Pens', desc="""
    The corridor runs north and south.  A bronze door to the east has a
    grille in it at head height, and through the grille comes a soft, coaxing
    voice speaking to something that growls back.""")
R[2594] = dict(name='The Quiet Room', desc="""
    A small empty room, warm and still, with a woven mat on the floor.  The
    masters of the floor of making set it aside so that anyone who has seen
    too much in the workrooms may sit here until their hands stop shaking.
    The only exit is the bronze door west.""",
    extras={'mat': 'A plain woven mat, worn through in the middle by many knees.'})
R[2595] = dict(name='The Charm Master\'s Chamber', desc="""
    Straw and dirt litter the floor of the chamber of the Master of Charm, who
    bends the wills of beasts and men to the college's use.  Leashes and
    collars hang from pegs.  Through a cage of bars to the north come growls
    and scratching; the bronze door is west.""",
    extras={'leashes collars pegs': 'Leashes and collars of many sizes. One is sized for a man.'})
R[2596] = dict(name='The Corridor Of Pens', desc="""
    The corridor runs north and south.  Claw marks score the stone along one
    wall, as though something was dragged this way and did not want to go.""")
R[2597] = dict(name='The Animal Pens', desc="""
    A row of stinking cages along both walls.  Wolves, birds, a bear and other
    beasts are kept here, some caught on the march with something grey behind
    their eyes, to be charmed, studied or cut up.  They watch you go by.  The
    only way out is the cage of bars to the south.""")
R[2598] = dict(name='The Foot Of The Binding Stair', desc="""
    The corridor ends at a stair climbing to the binding floor above.  Two
    wooden golems stand guard at the foot of it.  Someone has nailed a board to
    the bottom step: MASTERS ONLY.  The corridor runs back south.""",
    extras={'board': 'MASTERS ONLY. Below it, freshly painted: THE BLACK DOOR IS SEALED.'})

# ============================================================ the binding floor
R[2599] = dict(name='The Head Of The Binding Stair', desc="""
    The stair comes up onto the binding floor, where the masters bind power
    into staves and wands, and clay and stone into servants.  It is very quiet.
    A corridor leads west, and the stair goes back down.  Fresh chalk wards
    have been drawn across the top step, and stepping over them makes the
    teeth ache.""",
    extras={'wards chalk step': 'A line of chalk wards, redrawn often. They are there to keep something on this floor from going down.'})
R[2600] = dict(name='The Silver Corridor', desc="""
    A corridor running east and west, its walls inlaid with thin lines of
    silver that catch the light.  A silver door to the north leads to a store
    room.  A pair of disembodied eyes drifts slowly up and down the length of
    the corridor.""")
R[2601] = dict(name='The Stave Store', desc="""
    A large store room where raw materials are bundled and stacked: freshly cut
    staves of ash and yew, rods of iron and copper, wands not yet bound.  Each
    bundle is tagged with the master it was cut for.  A silver door leads west,
    and another south.""",
    extras={'staves bundles tags': 'Staves cut from trees in the Mistwood. The tags give names, and some of the names are struck through.'})
R[2602] = dict(name='The Master Spellbinder\'s Chamber', desc="""
    The chamber of the Master Spellbinder, who binds spells into wood and
    metal for the war-magi to carry west.  Unlike the workshops below, it holds
    no tools at all; he needs only his hands and his will.  A black scorch on
    the floor marks where a wand once broke.  Silver doors lead east and
    west.""",
    extras={'scorch floor': 'A starburst of black on the floor. The stone inside it has gone soft, like old cheese.'})
R[2603] = dict(name='The Spellbinder\'s Cache', desc="""
    The Spellbinder's cache, where finished work waits to be issued.  Three
    tall cabinets chased with silver stand against the walls; otherwise the
    room is bare, and very cold.  Silver doors lead east and south.""")
R[2604] = dict(name='The Silver Corridor', desc="""
    The corridor runs east and west.  The silver lines in the walls are
    tarnished black here, as though something had passed close to them and
    soured them.  A master has scrawled DO NOT POLISH beside the worst of it.""")
R[2605] = dict(name='The Silver Corridor', desc="""
    The corridor runs east and west.  A silver door to the north is locked and
    sealed with wax stamped with the Spellbinder's mark.  The floor in front
    of it is worn smooth by people who stood here waiting to be let in.""",
    extras={'wax seal mark': 'A seal of black wax stamped with a wand crossed by a key.'})
R[2606] = dict(name='A Turn In The Silver Corridor', desc="""
    The corridor bends from east to south.  A small window of thick glass is
    set in the outer wall, too high to see out of, and grey light comes
    through it.""")
R[2607] = dict(name='The Clay Corridor', desc="""
    The corridor runs north and south.  The floor here is gritty with dried
    clay, and big footprints, far too big for any man, are pressed into it
    going both ways.""")
R[2608] = dict(name='The Clay Corridor', desc="""
    The corridor runs north and south.  A rusty old door to the west hangs a
    little crooked on its hinges, and a thud of heavy movement comes from
    behind it.  Clay dust lies thick round the threshold.""")
R[2609] = dict(name='The Golem Maker\'s Workshop', desc="""
    A workshop of half-finished forms: torsos of clay, limbs of stone, a head
    of bronze with no face yet.  Some of them move and some do not.  The golems
    made here stand on the wall where there are not enough men.  A store room
    lies north and the golem chamber south; a rusty door leads east, and a
    trapdoor is set in the floor.""",
    extras={'trapdoor': 'A wooden trapdoor in the floor, warm to the touch. Heat rises through its cracks.'})
R[2610] = dict(name='The Clay Store', desc="""
    A small store room heaped with clay, stone, timber and less pleasant
    materials in sealed barrels.  Everything is grey with dust.  The only way
    out is south.""",
    extras={'barrels barrel': 'The barrels are sealed with pitch and marked FLESH. The college does not ask where the Golem Maker gets it.'})
R[2611] = dict(name='The Golem Chamber', desc="""
    A long chamber where finished golems stand in rows, from some no taller
    than a hand to some that stoop under the ceiling.  They seem to sleep.  A
    few have a name chalked on the chest, the regiment they are meant for.  The
    only way out is north.""")
R[2612] = dict(name='In The Flue', desc="""
    It is very dark here, and hot.  This is a crawlspace between floors where
    the forge's smoke is drawn up before it is led away.  Soot covers
    everything.  A trapdoor is set in the roof above, and a vent opens in the
    floor below, glowing faintly red.""")
R[2613] = dict(name='The Clay Corridor', desc="""
    The corridor runs north and south.  A golem's hand lies on the floor here,
    broken off at the wrist, and its fingers are still slowly opening and
    closing.""")
R[2614] = dict(name='A Turn In The Clay Corridor', desc="""
    The corridor turns from north to east.  The walls change from plain stone
    to stone painted with shifting colours that will not stay still when you
    look at them directly.""")
R[2615] = dict(name='The Corridor Of Veils', desc="""
    The corridor runs east and west.  The colours on the walls shift and run
    like oil on water, and now and then a doorway appears in them that is not
    really there.""")
R[2616] = dict(name='The Corridor Of Veils', desc="""
    The corridor runs east and west.  An emerald door to the south glitters
    so brightly it is hard to look at, and it may be the only real thing in
    the wall.  The floor seems to tilt, though a dropped coin would not roll.""")
R[2617] = dict(name='The Illusion Master\'s Chamber', desc="""
    The walls of the Master of Illusions' chamber change colour and texture as
    you watch, reforming from moment to moment.  Heaps of treasure glitter on
    every side, or seem to.  The master teaches war-magi to hide a company in a
    fold of hillside, and to make the dead see the living where there are none.
    An emerald door leads north and an opening west.""")
R[2618] = dict(name='The Endless Bedchamber', desc="""
    The bedroom of the Master of Illusions.  Strange things float in the air,
    and the walls never quite stay where they were.  The room seems far larger
    than it can be, stretching off to the north, south and west, and every way
    leads back to the same bed.  The chamber lies east.""",
    exits={'n': 'The room stretches off to the north.', 's': 'The room stretches off to the south.',
           'w': 'The room stretches off to the west.'})
R[2619] = dict(name='The Corridor Of Veils', desc="""
    The corridor runs east and west.  The colours on the walls are gentler
    here, and a glass door to the south shows a still, dim room beyond.  A
    small sign beside it asks for silence.""",
    extras={'sign': 'SILENCE. In smaller letters: "Here you may rest from what you have seen."'})
R[2620] = dict(name='The Meditation Chamber', desc="""
    A meditation chamber so quiet that not even footsteps make a sound.  The
    masters come here to clear their minds before a binding, and war-magi come
    to forget.  It is very peaceful, and very empty.  The only exit is the
    glass door north.""")
R[2621] = dict(name='A Turn In The Corridor Of Veils', desc="""
    The corridor turns from west to north.  The colours drain out of the walls
    here and leave them grey, and a cold draught comes from the north, smelling
    faintly of rot.""")
R[2622] = dict(name='Before The Sealed Wing', desc="""
    The corridor runs north and south past a blackened door to the east.  The
    door is chained, and the chains have been broken from the inside.  Across
    it is painted in red: SEALED BY ORDER OF THE ARCHMAGUS.  A smell of rot
    seeps from under it.""",
    extras={'chains chain': 'Heavy chains, snapped. The broken links are bent outward.',
            'door sealed paint': 'SEALED BY ORDER OF THE ARCHMAGUS. Below it, in a different hand: "He went too far in to come back."'})
R[2623] = dict(name='The Sealed Wing', desc="""
    A large dark room behind the sealed door.  The air is stale and cold, and a
    dread settles on the chest that has no cause anyone could name.  The master
    of this wing studied the dead of the west to learn how to unmake them, and
    the college sealed it when he began to make them instead.  The stench of
    rot comes from the north; the black door is west.""")
R[2624] = dict(name='The Cutting Room', desc="""
    The stench makes the stomach heave.  Body parts and half-rotted corpses lie
    everywhere, and on the operating tables are still forms that resemble
    nothing that ever lived.  Some of them wear the grey of the college.
    Screams come from the north.  The way back is south.""",
    exits={'n': 'Looking north fills you with a deep dread.'})
R[2625] = dict(name='The Necromancer\'s Lair', desc="""
    The lair of the Necromancer, once a master of the war-college.  Undead of
    every kind stand in rows awaiting his word, among them the bodies of
    students who came looking for him.  Glowing sigils are cut into the walls
    and floor to keep his own creations off him.  The only way out is
    south.""",
    extras={'sigils': 'Wards of the college, but redrawn with a grey hand. They no longer keep the dead out; they keep them in line.'})
R[2626] = dict(name='The Grey Corridor', desc="""
    The corridor runs north and south.  The ward-light in the walls is weak and
    flickering here, and the stones are cold.  Students hurry through this
    stretch without looking at the black door behind them.""")
R[2627] = dict(name='The Grey Corridor', desc="""
    The corridor runs north and south.  A row of fresh ward-signs has been
    painted across the floor, the paint still tacky, and the light grows
    steadier beyond them.""")
R[2628] = dict(name='The Foot Of The Gallery Stair', desc="""
    The corridor ends at the foot of a stair of black stone climbing to the
    warding galleries.  Two wooden golems guard it, and the walls glow brightly
    here, as if to make up for the dark behind.  The corridor runs back
    south.""")

# ============================================================ the warding galleries
R[2629] = dict(name='The Warding Galleries', desc="""
    The stair comes up at the east end of a long gallery of black obsidian,
    cut with runes of warding that whisper faintly in no tongue anyone living
    speaks.  Here the college keeps what it has taken from the west, each
    thing sealed in its own niche.  The first niche holds a grey banner.  The
    gallery runs west, and the stair goes back down.""",
    extras={'banner niche grey': 'A banner of grey cloth taken from the Field of Broken Banners. It bears no sign at all, and yet it is hard to stop looking at it.',
            'runes walls': 'Ward-runes cut deep into the obsidian and filled with silver. They whisper all the time; the masters say that is how you know they are working.'})
R[2630] = dict(name='The Warding Galleries', desc="""
    The gallery runs east and west.  A niche in the obsidian holds a sealed
    jar of grey ash, and the glass is warm though nothing near it is.  The
    runes around this niche have been recut three times.""",
    extras={'jar ash niche': 'A jar of ash from the Ashen Waste, labelled in a neat hand: "Do not open. Do not let it be opened. It remembers being alive."'})
R[2631] = dict(name='A Turn In The Warding Galleries', desc="""
    The gallery turns from east to south.  In the niche at the corner rests a
    crown of black iron, still wet, though it was brought up out of the
    Drowned Kingdom many years ago and has never been near water since.""",
    extras={'crown niche iron': 'A crown of black iron, dripping slowly. The drops vanish before they reach the floor of the niche.'})
R[2632] = dict(name='The Warding Galleries', desc="""
    The gallery runs north and south.  A niche here holds a single small shoe,
    a child's, laced with grey thread.  It was found walking on its own on the
    road from Vel'Morrow.  It does not walk now.  The masters check every
    morning.""",
    extras={'shoe niche': 'A child\'s leather shoe, laced with grey thread. Its toe points a little toward the west, whichever way it is set down.'})
R[2633] = dict(name='The Crossing Of The Galleries', desc="""
    Four obsidian galleries meet here around a pillar of white stone, the ward
    that holds all the others.  The runes on every wall pulse in time with it,
    slowly, like a heartbeat.  Galleries lead north, east, south and west.""",
    extras={'pillar stone ward': 'A pillar of white stone carved all over with the college\'s strongest wards. A hairline crack runs up one side, and someone has filled it with silver.'})
R[2634] = dict(name='The End Of The East Gallery', desc="""
    The gallery ends at a dark door to the east.  Tendrils of mist cling to the
    floor here, seeping from under the door, and they are cold enough to
    numb the ankles.  The gallery runs back west.""")
R[2635] = dict(name='The Scrying Chamber', desc="""
    The scrying chamber of the college, where the faceless seers look out over
    the march and tell the wall what is coming.  A huge black cauldron bubbles
    in the centre, pouring smoky fog into the air, and in the fog move pictures
    of grey country and grey things walking.  The only exit is the black door
    west.""",
    extras={'fog pictures smoke': 'Grey country, burnt fields, a line of figures walking east without hurrying. One of them stops and turns its head, and the fog clouds over.'})
R[2636] = dict(name='The End Of The West Gallery', desc="""
    The gallery ends at a wooden door to the west, oddly homely between the
    obsidian walls.  Soft snoring comes through it.  The niche beside the door
    is empty, its runes cut away, and a note says ON LOAN TO THE LIBRARY.  The
    gallery runs back east.""",
    extras={'note niche': 'ON LOAN TO THE LIBRARY. The date on the note is forty years old.'})
R[2637] = dict(name='The Library Of The War-College', desc="""
    The entrance to the great library.  A giant desk stands here under a
    landslide of books, parchments and scrolls.  Shelves loaded with books run
    away north, south and west as far as the eye can see; the books of the
    west are somewhere in there, chained.  The door back to the gallery is
    east.""",
    extras={'desk books': 'Books on wards, on fire, on the anatomy of the dead. A ledger of loans lies open; most are years overdue, and against many the librarian has written "fell".'})
R[2638] = dict(name='Among The Shelves Of Wards', desc="""
    Shelves of books on warding rise out of reach, floating a little off the
    floor.  The books seem to wink in and out of sight when not looked at
    straight.  A strong musty smell hangs over everything.  Aisles lead north,
    east, south and west.""")
R[2639] = dict(name='Among The Shelves Of Fire', desc="""
    Here the shelves hold the books of fire, bound in iron so that they cannot
    burn.  The air is warm and dry and smells of hot metal.  Aisles lead off
    north, east, south and west between the stacks, and they all look much the
    same.""")
R[2640] = dict(name='Among The Shelves Of The Dead', desc="""
    These shelves hold the college's studies of the dead: their anatomy,
    their habits, how they are put down and how they get up again.  Several
    books are bound in a pale leather that nobody asks about.  Aisles lead
    north, east, south and west.""")
R[2641] = dict(name='Among The Shelves Of Histories', desc="""
    Histories fill these shelves: of the wall, of Old Thalos and its fall, of
    the first darkness and the second.  Many of the newest volumes are only a
    few pages long, and end mid-sentence.  Aisles lead north, east, south and
    west.""")
R[2642] = dict(name='Among The Chained Shelves', desc="""
    The books on these shelves are chained, and the chains are warded.  They
    were taken from the west, and some of them move against their chains when
    no one is near.  A faint whispering rises from the stacks.  Aisles lead
    north, east, south and west.""",
    extras={'chains books chained': 'Black books on silver chains. The nearest has no title, only a grey thumbprint pressed into the cover.'})
R[2643] = dict(name='Among The Forgotten Shelves', desc="""
    A corner of the library that the librarian seldom reaches.  Dust lies
    thick, and the books here have been shelved in no order at all.  To the
    west there is a small gap between two shelves; the aisle runs back
    east.""",
    exits={'w': 'There is a small gap between the shelves, just wide enough to squeeze through.'})
R[2644] = dict(name='Between The Shelves', desc="""
    The shelves press so close here that it is hard to turn round.  Books
    hover just out of reach, and the musty smell is strong.  A faint flicker
    of light shows to the north; the way back is east.""")
R[2645] = dict(name='The Hidden Reading Room', desc="""
    A small bare room with nothing in it but an enormous tome lying open on the
    floor.  Its jewelled bindings are worn like old bark, and spidery writing
    crawls across its pages too fast to follow.  Something has been wedged
    between the pages.  The only way out is south, between the shelves.""",
    extras={'tome book writing pages': 'The writing moves. Now and then a word holds still long enough to be read: wall, ward, west, wake.'})
R[2646] = dict(name='The South Gallery', desc="""
    The gallery runs north and south.  A tall shape in a niche is covered with
    a black cloth, and a small sign reads DO NOT UNCOVER.  The runes around it
    are thicker than anywhere else in the galleries.""",
    extras={'cloth shape niche sign': 'A mirror, by its shape, under a black cloth. DO NOT UNCOVER. The cloth stirs a little, as though something behind it were breathing.'})
R[2647] = dict(name='The End Of The South Gallery', desc="""
    The obsidian ends at a golden archway to the south that hums with power
    strong enough to numb the skin.  This is the last ward before the crown of
    the tower.  The gallery runs back north.""",
    extras={'archway arch': 'A golden arch carved with the hand and flame of the college. The gold is warm, and the hum comes up through the soles of the feet.'})
R[2648] = dict(name='Beneath The Golden Arch', desc="""
    Passing through the arch brings a tingle, as if the living ward had looked
    into you, found you wanting and let you by anyway.  The light from the arch
    is almost blinding.  Through the glare a stairway can be made out climbing
    up.  The gallery lies back north.""")
R[2649] = dict(name='The Silent Landing', desc="""
    A landing halfway up a long stair.  No sound or smell reaches here at
    all, and there is nothing to see in any direction but stair.  It is meant
    to empty the mind before the crown.  The stair goes on up, and back
    down.""")

# ============================================================ the crown
R[2650] = dict(name='The Crossing Of The Orders', desc="""
    The stair ends in a crossing where the halls of the three orders of the
    college meet, and their powers push and pull against one another in the
    air.  A grey-tiled hall leads south to the Grey Order, a black-tiled hall
    east to the Black, and a white-tiled hall west to the White.  To the north
    a wide hall swirls with colours, the way to the Archmagus.  The stair
    leads back down.""")
R[2651] = dict(name='The Grey Hall', desc="""
    A hall of grey tiles running north and south.  Dim globes of light drift
    here, showing the way.  The Grey Order keeps the college's wards and holds
    the balance between the other two, and its hall is calm and plain.""")
R[2652] = dict(name='The Grey Hall', desc="""
    The grey hall runs north to the crossing.  To the south stand large double
    doors of grey metal, engraved with a pair of scales.  The globes of light
    gather here, waiting.""",
    extras={'scales doors': 'A pair of scales, perfectly level, engraved on the grey doors. Under it: "Neither fire nor shadow. The wall."'})
R[2653] = dict(name='The Grey Antechamber', desc="""
    The antechamber of the Master of the Grey Order.  Power hangs in the air
    thickly enough to taste, like the air before a storm.  Once the eyes adjust
    to the half-light, a larger chamber can be made out to the south.  The grey
    doors lead back north.""")
R[2654] = dict(name='The Grey Chamber', desc="""
    The audience chamber of the Grey Order, plain and orderly.  Ward-stones
    from the march stand on stands about the walls, each one cracked, brought
    back so that the order can learn how it failed.  A study lies west, a
    closet east and a bedchamber south; the antechamber is north.""",
    extras={'ward-stones stones stands': 'Ward-stones from posts on the march, each split clean through. Labels give the post and the date. The dates are getting closer together.'})
R[2655] = dict(name='The Grey Study', desc="""
    A large study whose walls are shelved with books of warding.  A broad oak
    desk is covered in reports from the wall.  A small pair of scales floats
    at eye level in perfect balance, the sign of the order.  The only exit is
    east.""",
    extras={'scales': 'Tiny scales of grey metal, hanging in the air. They do not move, even when you breathe on them.',
            'reports desk': 'Reports from every post on the march, in many hands. The Master has written in the margins of each one: "hold".'})
R[2656] = dict(name='The Grey Closet', desc="""
    A small closet hung with grey cloaks and robes, all of them plain, all of
    them mended many times.  A row of empty pegs at the end is labelled with
    the names of masters who did not come back to claim them.  The only exit
    is west.""")
R[2657] = dict(name='The Grey Bedchamber', desc="""
    The bedchamber of the Master of the Grey Order.  A large plain bed takes up
    most of the room, and curtained windows are set in the far wall.  The bed
    has not been slept in; the Master sleeps sitting up, at his desk.  The only
    exit is north.""",
    extras={'windows curtains': 'Behind the curtains the glass looks out on nothing but grey cloud.'})
R[2658] = dict(name='The Black Hall', desc="""
    A hall of black tiles running east and west, filled with an unnatural
    darkness that swallows light.  The Black Order studies the sorcery of the
    west in order to turn it back on itself.  The college needs what they
    learn, and is afraid of them.  The dread grows the further east you go.""")
R[2659] = dict(name='The Black Hall', desc="""
    The black hall runs east and west.  The darkness is thicker here, and
    voices seem to whisper in it, too low to make out.  Small bones have been
    set into the black tiles in a pattern.""",
    extras={'bones pattern tiles': 'Finger bones set into the tiles in the shape of a ward. Or of something that looks like a ward from the wrong side.'})
R[2660] = dict(name='Before The Obsidian Doors', desc="""
    The black hall ends at a pair of obsidian doors to the east.  The darkness
    here is so thick it can almost be held, and a deep fear and loathing rises
    in the throat.  The hall runs back west.""")
R[2661] = dict(name='The Chamber Of Darkness', desc="""
    A vast chamber whose walls are lost in the dark.  Patches of pure black
    swirl here and there, drinking whatever light comes near them.  This is
    where the Black Order brings what it has learned in the west, to practise.
    Ways lead north, east and south into deeper dark; the obsidian doors are
    west.""")
R[2662] = dict(name='A Lightless Room', desc="""
    It is very dark here...  So dark that it presses on the eyes.  Something
    in the room breathes, slowly and patiently.  The only way out is south.""")
R[2663] = dict(name='The Question Room', desc="""
    A dimly lit chamber.  Instruments hang from a rack on the wall, and they
    quiver as if eager.  An iron table stands in the middle, bare and clean.
    The Black Order says it questions only things from the west here.  The
    straps on the table are sized for a man.  The only way out is north.""",
    extras={'instruments rack': 'Hooks, blades and pins, all of fine silver, all of them stirring slightly on their pegs.',
            'table straps': 'An iron table with leather straps at wrist, ankle and throat.'})
R[2664] = dict(name='The Inner Sanctum Of The Black Order', desc="""
    A small dark chamber.  Glowing sigils cover the walls in a language that
    is no longer spoken anywhere in the east.  An altar of obsidian stands
    here, and it glows without giving light; it seems to drink the light in.
    The only way out is west.""",
    extras={'altar obsidian': 'An altar of black glass. Looking into it, there is a long way down, and something far off in the west looks back up.',
            'sigils walls': 'Writing taken from the west. The Black Order says it has tamed it. It does not look tame.'})
R[2665] = dict(name='The White Hall', desc="""
    A long, brilliantly lit hall running east and west.  The walls and floor
    are milky white and glow with a cold radiance.  The White Order would burn
    every tainted thing in the east, and every tainted mage, and they keep
    their hall so bright that no shadow can stand in it.""")
R[2666] = dict(name='The White Hall', desc="""
    The white hall runs east and west.  The light is so bright it hurts.  To
    the west stand great double doors of finely worked ivory, carved with a
    flame.  A row of iron stakes stands along the wall, ready.""",
    extras={'stakes iron': 'Burning-stakes. The White Order keeps them clean and oiled.'})
R[2667] = dict(name='The White Antechamber', desc="""
    A small antechamber lit by a glow with no source, as if the room itself
    were burning cold.  A larger chamber lies west, and the sense of being
    weighed and found wanting is strong.  The ivory doors lead back east.""")
R[2669] = dict(name='The Chamber Of The White Flame', desc="""
    A vast chamber of some unknown metal, white to the point of blindness.  A
    flame burns in the centre, feeding on shadow, and it leans toward each
    visitor as if testing them for taint.  A meditation room lies north, a
    study south and a closet west; the antechamber is east.""",
    extras={'flame': 'A white flame without fuel. It leans toward you and tastes the air, and then, reluctantly, leans away.'})
R[2670] = dict(name='The White Meditation Room', desc="""
    A small room heaped with white silk cushions.  It is warm and very quiet,
    and the urge to lie down and sleep is almost too strong to resist.  The
    only way out is south.""")
R[2671] = dict(name='The White Study', desc="""
    A spacious study, tidy to the point of being bare.  Lists of names lie in
    perfect stacks on the desk: mages of the college the White Order suspects
    of taint.  The only way out is north.""",
    extras={'lists names desk': 'Lists of names, neatly written. Many are students. One of them is the Master of the Grey Order.'})
R[2672] = dict(name='The White Closet', desc="""
    A small closet with white cloaks and vests hung on hooks, and a few old
    boots set in a row.  Everything is spotless.  The only way out is east.""")
R[2673] = dict(name='The Hall Of Three Doors', desc="""
    A wide hall where several people could walk abreast.  The floor swirls
    with colours in constant motion.  A huge door of grey metal bars the way
    north; it opens only with the Grey Order's key.  The crossing lies
    south.""")
R[2674] = dict(name='The Hall Of Three Doors', desc="""
    The wide hall goes on between two great doors: grey metal back to the
    south, and black obsidian to the north, which opens only with the Black
    Order's key.  The swirl of colours on the floor darkens here, as if
    shadowed.""")
R[2675] = dict(name='The Hall Of Three Doors', desc="""
    The last stretch of the wide hall.  The black door is south, and a door of
    white ivory bars the way north, opening only with the White Order's key.
    No one comes to the Archmagus unless all three orders agree, or unless
    they rob all three.""")
R[2676] = dict(name='The Entranceway Of The Archmagus', desc="""
    The entrance to the audience chamber of the Archmagus of the war-college.
    Tapestries on the walls show the masters who held the tower before her,
    each standing on the wall with fire in hand.  A multicoloured carpet
    rustles under the boots.  The audience chamber lies north; the ivory door
    is south.""",
    extras={'tapestries tapestry': 'Archmagi of old, each shown on the wall of Midgaard holding back a grey tide with fire. In the last tapestry the tide is closer.'})
R[2677] = dict(name='The Audience Chamber', desc="""
    Bolts of energy leap crackling from wall to wall, and colours bloom in the
    air and fade.  It all draws the eye to a throne cut from a single huge
    emerald in the centre of the room, where the Archmagus hears the reports of
    the wall.  An altar room lies north, a dressing room east, a library west,
    and the entranceway south.""",
    extras={'throne emerald': 'A throne of flawless emerald, taken, they say, from a drowned king\'s hall in the west long ago, and cleansed by fire for a year and a day before anyone sat on it.'})
R[2678] = dict(name='The Dressing Room', desc="""
    A plush dressing room.  Robes of state and battle hang from a rack that
    floats at eye level, some of them scorched at the hems.  A large silver
    mirror stands on a gold stand.  The only way out is west.""",
    extras={'mirror silver': 'A silver mirror. It shows the room as it is, and nothing else, which in this tower is a comfort.'})
R[2679] = dict(name='The Archmagus\' Library', desc="""
    A small, cosy library, the shelves filled with well-used books.  A big oak
    writing table holds letters from the Lord Commander of Midgaard, asking
    for more war-magi, and drafts of replies.  The light comes from a plain
    oil lamp.  The only way out is east.""",
    extras={'letters table drafts': 'Letters from the Lord Commander: "Send more. Send any." The drafts of the replies have all been torn up but the last: "I am sending the novices."'})
R[2680] = dict(name='The Chapel Of The Lamp', desc="""
    A small chapel built round a golden altar.  Icons of lesser powers line the
    walls, but the altar bears the sign of the Lamp, the old patron of mages,
    whose flame they say was lit before the west ever went dark.  The audience
    chamber lies south.  Narrow doors, hidden in the panelling, lead east and
    west.""",
    extras={'altar icons lamp sign': 'A golden altar marked with a small lamp. The flame carved on it has been worn smooth by hands.'})
R[2681] = dict(name='The Treasury', desc="""
    A small chamber of stale air that has not been opened in many years.  The
    college's treasury, against the day the wall falls and the masters must
    buy passage east.  The only way out is the hidden door west.""")
R[2682] = dict(name='The Escape-Way', desc="""
    A small dark passage that ends in a blinding blue light to the west.
    Travelling cloaks and a leather backpack hang ready on hooks.  This is the
    Archmagus' way out: if the tower falls, the light will carry her to the
    temple of Midgaard.  The hidden door leads back east.""",
    extras={'hooks cloaks': 'Hooks for a dozen cloaks. Only a few cloaks remain. Someone has already used the way out more than once.'})
R[2683] = dict(name='In The Blue Light', desc="""
    You float in a blue field of force with no source anywhere.  It pushes from
    every side at once and holds you weightless.  High overhead there is a flaw
    in the blue, like a doorway seen through water, and beyond it the faint
    sound of temple bells.""")


# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d


M[2500] = mob('the ward-shade', 'shade shadow guardian ward', 'A ward-shade rises out of the mist with a shriek and attacks.',
              'A shadow bound by the masters to walk the Mistwood and kill whatever strays from the path. It is made of nothing but darkness and an old, bitter order.')
M[2501] = mob('the lost courier', 'courier adventurer lost', 'An emaciated courier stumbles here, looking lost and hopeless.',
              'A courier of the wall sent to the tower with letters weeks ago. The mist has had him ever since; his satchel is empty and his eyes do not quite focus.')
M[2502] = mob('Edgar', 'edgar recruit levy', 'Edgar, a levy recruit, stands here looking very lost.',
              'A gangling farm boy in an oversized levy helmet, sent from the Recruit Yards with a message he has forgotten. Edgar says \'Pardon me, is this the way to the wall? They said follow the road west.\'')
M[2503] = mob('the diamond golem', 'golem diamond warden', 'A huge golem of cut diamond stands guard before the gate.',
              'A gate-warden made of clear diamond, so hard that the fire of the west only polished it. It carries the key of the gate inside its chest.')
M[2504] = mob('the young war-magus', 'magus mage young war', 'A young war-magus wanders by, lost in thought.',
              'A novice in a grey robe a size too large, muttering the words of a ward. He has been told he will be posted west in the spring, and he is trying not to think about it.')
M[2505] = mob('Strick the barkeep', 'strick bartender barkeep', 'Strick is here levitating cups to his customers.',
              'A broad, quiet man who failed his last drill twenty years ago and stayed on to pour drinks. He looks harmless, but then so does a sleeping dragon.')
M[2506] = mob('Tatorious the quartermaster', 'tatorious quartermaster wizard shopkeeper', 'Tatorious the quartermaster is here counting the day\'s takings.',
              'A plump, cheerful war-magus who lost a leg on the march and now issues reagents and scrolls to those who still have both. He winks, and charges what he likes.')
M[2507] = mob('Ezmerelda', 'ezmerelda cook', 'Ezmerelda the cook is here stirring a large pot of something.',
              'A gaunt cook with ink-black nails and a mage\'s eyes. She feeds the college on what the supply road brings and what the laboratories do not want, and nobody asks which is in the pot.', sex=2)
M[2508] = mob('the cook\'s assistant', 'assistant cook mage', 'The cook\'s assistant is here, adding things to the pot.',
              'A pale young man with burnt fingers who drops strange things into the pot without looking at them.')
M[2509] = mob('the muzzled prisoner', 'prisoner muzzled man', 'A muzzled prisoner hangs in his chains against the wall.',
              'A man in the rags of a master\'s robe, with an iron muzzle locked over his mouth. He was a war-magus once, and went too far west; he came back speaking in a voice that was not his. The muzzle is so that nobody hears it.')
M[2510] = mob('the jailor', 'jailor mage gaoler', 'The jailor is here, enjoying a comfortable nap.',
              'A dirty, heavy-lidded mage who keeps the undercroft. He sleeps a great deal, because the things in his cells do not last long.')
M[2511] = mob('the broom', 'broom straw', 'A straw broom leans against the wall, twitching.',
              'One of the enchanted brooms of the officers\' wing, its spell gone sour with the years. The broom screams \'Take that, you lout!\' and goes for your purse.')
M[2512] = mob('the warding hands', 'hands lesser guardian warding', 'A pair of disembodied hands floats in the air here.',
              'A pair of grey hands bound into the tower\'s service to guard its doors. They twitch, eager to close round a throat.')
M[2513] = mob('the warding eyes', 'eyes greater guardian warding', 'A pair of disembodied eyes floats here, glaring at you.',
              'A pair of eyes without a face, bound to watch the tower\'s halls. They smoulder with an old and patient hatred for anything that does not belong.')
M[2514] = mob('the visiting war-magus', 'magus mage visitor officer', 'A war-magus home from the wall is snoring here.',
              'A war-magus on leave from the wall, too tired even to take off his boots. He mutters wards in his sleep.')
M[2515] = mob('the young apprentice', 'apprentice young novice', 'A young apprentice is here, bent over her studies.',
              'A thin girl from the refugee camps with ink on her fingers. She studies as if her life depended on it, which it does.', sex=2)
M[2516] = mob('the young apprentice', 'apprentice young novice', 'A young apprentice is here mumbling the words of a ward.',
              'A boy repeating the same ward over and over, his lips moving, his eyes shut tight.')
M[2517] = mob('the young apprentice', 'apprentice young novice', 'A young apprentice is sleeping here.',
              'A novice asleep in his robe with a book on his chest. He twitches as he dreams.')
M[2518] = mob('the cruel apprentice', 'apprentice young cruel novice', 'A young apprentice is here, tormenting a cornered kitten.',
              'A sharp-faced boy who has learned that the college will forgive a great deal in a student who is good with fire.')
M[2519] = mob('the small kitten', 'kitten cat small', 'A small kitten is here, mewing in terror.',
              'A little ball of mottled fur, singed and burnt in patches. It shakes.', sex=2)
M[2520] = mob('the student', 'student novice', 'A student of the bolt is here, looking bored.',
              'A student slumped at a desk, casting the same bolt of force for the hundredth time today. The student yawns.')
M[2521] = mob('the drill instructor', 'instructor teacher mage drill', 'The drill instructor screams at the interruption and attacks you.',
              'A hard-faced master with a burnt hand who has drilled a thousand novices in the bolt of force. He is furious at being interrupted.')
M[2522] = mob('the student of the veil', 'student veil novice', 'A student of the veil flickers in and out of sight here.',
              'A student trying to master the veil of unseeing, blinking in and out of existence. The war-magi need it to cross the march unseen.')
M[2523] = mob('the master of the veil', 'teacher mage master veil', 'The master of the veil appears out of nowhere and attacks.',
              'A thin, fierce master who teaches the veil, and who is rarely seen until it is too late.')
M[2524] = mob('the student of the veil', 'student veil novice', 'A student of the veil has fallen asleep at her desk here.',
              'A student who has collapsed over her desk, worn out. Her hand is still half invisible.', sex=2)
M[2525] = mob('the old lecturer', 'wizard speaker mage lecturer', 'An old wizard is here, lecturing on the west.',
              'A shrunken old man who looks as if he could be the oldest man alive. The magic of the west takes years from those who touch it, and he may in truth be no older than you.')
M[2526] = mob('the young war-magus', 'mage magus young', 'A young war-magus is here learning to fight with a knife.',
              'A confident young mage with a silvered dagger, sure he will never run out of spells. The battle mistress is trying to cure him of that.')
M[2527] = mob('the battle mistress', 'mistress battle', 'The battle mistress is here, teaching the use of the dagger.',
              'A scarred, rugged woman who looks more like a sergeant of the wall than a mage. She has been west three times and come back three times, and she teaches the young to do the same.', sex=2)
M[2528] = mob('the weary master', 'mage teacher master weary', 'A weary master is here, resting with a cup of black tea.',
              'A teacher worn thin by long drills, bad news and inattentive novices.')
M[2529] = mob('the aged master', 'wizard master aged', 'An aged master is sleeping here.',
              'A very old master of the college, sleeping uneasily. Dreams of fire and of the march pass behind his eyelids. Better not to wake him.')
M[2530] = mob('the map-scribe', 'scribe mage map', 'A scribe is here, copying out a map of the march.',
              'A careful scribe redrawing the march from the latest reports, moving the line a little further east each time.')
M[2531] = mob('the scribe', 'scribe mage translator', 'A scribe is here, working slowly on a translation.',
              'A young scribe translating writing taken from the west. She works with her eyes half shut and stops often to rub them.', sex=2)
M[2532] = mob('the Master Scribe', 'master scribe', 'The Master Scribe is here, looking very put out.',
              'A scribe so old his skin has folded into one great wrinkle. The Master Scribe screams \'How dare you interrupt my work? The wall is waiting for these!\'')
M[2533] = mob('the scribe\'s assistant', 'assistant scribe', 'The scribe\'s assistant is here, folding parchments.',
              'A clerk not yet trusted with the sealed scrolls, folding and stacking the plain ones for the regiments.')
M[2534] = mob('the Enchanter', 'enchanter master mage', 'The Enchanter is here, laying a ward-word on a fine sword.',
              'The master of the college\'s forge, concentrating hard on a working that will either ruin the blade or make it bite the dead.')
M[2535] = mob('the dancing sword', 'sword dancing', 'A finely made sword lies on the work table here.',
              'A blade the Enchanter woke and could not put back to sleep. It looks very sharp.')
M[2536] = mob('the Mad Alchemist', 'alchemist mad', 'The Mad Alchemist babbles something and attacks.',
              'Once the best maker of healing draughts in the east, he began testing brews made from things taken from the west, and tested them on himself. His eyes dart about, he drools, and he throws back his head and cackles.')
M[2537] = mob('the Master Summoner', 'master summoner', 'The Master Summoner is here, holding a gate open to elsewhere.',
              'The Summoner calls things through so the college can learn how to kill them. He is concentrating hard on keeping the gate in hand, before what is on the other side takes him instead.')
M[2538] = mob('the Master of Charm', 'master charmer charm', 'The Master of Charm utters the words, \'uuuzzldctz\'.',
              'A smiling master who bends the wills of beasts and men for the college. He sizes you up, always looking for a new pet.')
M[2539] = mob('the wooden golem', 'golem wooden sentry', 'A wooden golem stands a silent vigil here, guarding the stair.',
              'A tall golem of seasoned oak, set to guard the stairs. It looks very flammable.')
M[2540] = mob('the Master Spellbinder', 'master spellbinder binder', 'The Master Spellbinder is here, recharging a blackened wand.',
              'A cold, hard master who binds spells into wood and metal for the war-magi. He does not like to be disturbed. He snarls and attacks.')
M[2541] = mob('the Golem Maker', 'maker golem master', 'The Golem Maker is here, chiselling stone.',
              'A fussy, meticulous master who makes golems to stand on the wall where there are no longer enough men.')
M[2542] = mob('the granite golem', 'golem granite', 'A granite golem stands here, waiting for orders.',
              'It looks like a statue, until it shambles toward you.')
M[2543] = mob('the bronze golem', 'golem bronze', 'A bronze golem stands here, shining dully.',
              'A golem of polished bronze with a blank face. It looks very slow-witted.')
M[2544] = mob('the flesh golem', 'golem flesh', 'A flesh golem stands guard here.',
              'A golem stitched together from many bodies, some of them not human. The Golem Maker does not say where he gets the parts.')
M[2545] = mob('the cloth golem', 'golem cloth', 'A cloth golem shuffles around here.',
              'A heap of old rags stitched into the shape of a man. It is a wonder it can walk, and it is made from the robes of dead students.')
M[2546] = mob('the adamantite golem', 'golem adamantite', 'An adamantite golem stands here, looking very dangerous.',
              'A golem forged of dark adamantite from the dwarven halls. It is strong and very hard to hurt, and not at all clever.')
M[2547] = mob('the clay golem', 'golem clay', 'A clay golem stands guard here.',
              'A big golem of grey clay that looks almost like a heap of earth.')
M[2548] = mob('the Master of Illusions', 'master illusionist mage dragon', 'An enormous many-coloured three-headed dragon growls at you.',
              'The dragon flickers, and where it was stands a small, harmless-looking old man. He teaches the war-magi to hide a company in a fold of hillside.')
M[2549] = mob('the Necromancer', 'necromancer master', 'The Necromancer is here, raising the dead.',
              'Once a master of the war-college, who studied the dead of the west to learn to unmake them, and learned instead to make them. He is tall and gaunt, all in black, his eyes two embers in the shadow of his cowl. He shrieks and orders his dead to attack.')
M[2550] = mob('the animated skeleton', 'skeleton undead', 'An animated skeleton screams silently and attacks.',
              'The bones of a student who came looking for the Necromancer. It feels no pain, and hacks at you without mercy.')
M[2551] = mob('the undead giant', 'giant undead', 'An undead giant lumbers toward you.',
              'The rotting corpse of a hill giant brought back from the march for study, and raised. It is enormous, and it does not stop.')
M[2552] = mob('the faceless seer', 'seer witch faceless hag', 'A faceless seer is here, scrying out the march.',
              'A woman with no face at all, only blank skin; the seers give their eyes to the cauldron so they may watch the west. From where her mouth should be comes a soft, disgusting giggle.', sex=2)
M[2553] = mob('the Librarian', 'librarian mage', 'The Librarian has fallen asleep at his desk here.',
              'A peaceful old man who has kept the library for fifty years, and kept the chained books from getting loose.')
M[2554] = mob('the grey apprentice', 'apprentice grey', 'The grey apprentice leaps to bar your way.',
              'A powerful mage in his own right, who gave up his rank to serve the Master of the Grey Order and learn what cannot be learned alone.')
M[2555] = mob('the grey cat', 'cat grey familiar', 'A grey cat is lounging lazily here.',
              'The familiar of the Grey Order\'s master. It cocks an ear toward you and purrs. It looks harmless, until you notice the size of its claws.', sex=2)
M[2556] = mob('the Master of the Grey Order', 'master guildmaster grey', 'The Master of the Grey Order is here, weighing reports from the wall.',
              'A calm, tired man who keeps the wards of the college and the balance between the Black and the White. He looks peaceful, and very far away.')
M[2557] = mob('the black-robed apprentice', 'apprentice black', 'A black-robed apprentice leaps from the shadows and attacks.',
              'A woman with a wicked scar down one side of her face, a gift from the first west-spell she tried. She must once have been beautiful; now her scowl is permanent.', sex=2)
M[2558] = mob('the black cat', 'cat black familiar', 'A black cat with its fur on end hisses at you.',
              'The familiar of the Black Order\'s master. Its eyes are faintly grey. Petting it is out of the question.')
M[2559] = mob('the Master of the Black Order', 'master guildmaster black', 'The Master of the Black Order is here, plotting.',
              'The master of the order that studies the sorcery of the west. The college needs what he knows. Whether he still works for the college is another question. He glares at you.')
M[2560] = mob('the white-robed apprentice', 'apprentice white', 'A white-robed apprentice screams at your intrusion.',
              'A fanatic in spotless white. The white-robed apprentice screams \'Thou art tainted! Thou art unworthy!\'')
M[2561] = mob('the white cat', 'cat white familiar', 'A white cat is here, preening its fur.',
              'The familiar of the White Order\'s master: a large ball of white fluff with claws.')
M[2562] = mob('the Master of the White Order', 'master guildmaster white', 'The Master of the White Order is here, frowning at your intrusion.',
              'A cold, self-righteous zealot who would burn every tainted thing in the east, and every tainted mage with it. He keeps a list.')
M[2563] = mob('the calico cat', 'cat calico familiar', 'A great calico cat is lounging here.',
              'The Archmagus\' familiar, a giant of its kind, wearing a jewelled collar. It watches everything and forgets nothing.')
M[2564] = mob('the Archmagus', 'archmagus guildmaster grand mistress', 'The Archmagus of the war-college sits here on her emerald throne.',
              'The Grand Mistress of the High Tower, who commands the war-college for the wall. She looks young, kept so by strong magic, but her eyes are very old. She strokes her familiar and smiles at you.', sex=2)


# ====================================================================== objs
def obj(short, aliases, long, **kw):
    d = dict(short=short, aliases=aliases, long=long)
    d.update(kw)
    return d


O[2500] = obj('a diamond key', 'key diamond gate', 'A key of clear diamond glints on the ground here.')
O[2501] = obj('a black oven', 'oven black', ' ')
O[2502] = obj('an iron meat locker', 'locker meat iron', ' ',
              extras={'locker meat iron': 'A great iron locker, cold inside. You have the horrid thought that a body might be in there, and then that it might not be the first.'})
O[2503] = obj('a floating spice rack', 'rack spice', ' ')
O[2504] = obj('a slice of road bread', 'slice bread traveller road', 'A slice of hard road bread lies here.')
O[2505] = obj('a large chunk of meat', 'chunk meat', 'A large chunk of meat of no particular animal lies here.')
O[2506] = obj('a finger sandwich', 'sandwich finger', 'A finger sandwich lies here.',
              extras={'sandwich finger': 'It would look quite tasty if someone had first taken the fingernails out.'})
O[2507] = obj('a straw broom', 'broom straw', 'A straw broom leans against the wall here.',
              extras={'broom straw': 'An ordinary broom. Probably. It has not moved yet.'})
O[2508] = obj('a warded arms cabinet', 'cabinet arms warded', 'A heavy arms cabinet carved with ward-sigils is bolted to the wall.')
O[2509] = obj('an ingot of silver', 'bar ingot silver', 'An ingot of silver, stamped with the college\'s mark, lies here.')
O[2510] = obj('an ingot of gold', 'bar ingot gold', 'An ingot of gold, stamped with the college\'s mark, lies here.')
O[2511] = obj('an ingot of mithril', 'bar ingot mithril', 'An ingot of mithril from the dwarven halls lies here.')
O[2512] = obj('an ingot of adamantite', 'bar ingot adamantite', 'A dark ingot of adamantite lies here.')
O[2513] = obj('a mithril forge-hammer', 'hammer mithril forge', 'A mithril forge-hammer, its face scored with runes, lies here.')
O[2514] = obj('a chest with a glowing lock', 'chest glowing', 'A huge chest with a glowing lock stands here.')
O[2515] = obj('a small iron key', 'key small iron', 'A small iron key has been left here.')
O[2516] = obj('a warded long sword', 'sword long warded', 'A long sword with a ward-word etched near the hilt lies here.')
O[2517] = obj('a silvered dagger', 'dagger silver silvered', 'A finely made dagger of silver lies on the ground here.')
O[2518] = obj('a curved scimitar', 'scimitar curved', 'A curved scimitar in a jewelled sheath, a trophy from the west, lies here.')
O[2519] = obj('a stave of mistwood', 'staff stave wooden mistwood', 'A pale stave of mistwood leans against the wall here.')
O[2520] = obj('a silver chased cabinet', 'cabinet silver', 'A tall cabinet chased with silver stands here.')
O[2521] = obj('a silver chased cabinet', 'cabinet silver', 'A tall cabinet chased with silver stands here.')
O[2522] = obj('an old cell key', 'key old cell', 'An old cell key, heavy and rusty, lies here.')
O[2523] = obj('a silvery key', 'key silvery', 'A silvery key has been left here.')
O[2524] = obj('a silvery key', 'key silvery', 'A silvery key has been left here.')
O[2525] = obj('a red and white staff', 'staff red white', 'A staff banded in red and white leans against the wall here.')
O[2526] = obj('a burnt staff', 'staff burnt', 'A staff charred black along its length leans against the wall here.')
O[2527] = obj('a black rod', 'rod black wand', 'A short rod of black iron has been left here.')
O[2528] = obj('a wooden stick', 'wand wooden stick', 'A plain wooden stick lies here, humming faintly.')
O[2529] = obj('a metal wand', 'wand metal', 'A wand of grey metal lies here.')
O[2530] = obj('a black cauldron', 'cauldron black', 'A huge black cauldron bubbles here, pouring out fog.')
O[2531] = obj('a small pair of bat wings', 'wings bat', 'A small pair of dried bat wings lies here.')
O[2532] = obj('a grey eyeball', 'eyeball eye grey', 'A grey eyeball lies here. It was not taken from anything human.')
O[2533] = obj('the great tome', 'book tome great', 'An enormous tome lies open here, its writing crawling.')
O[2534] = obj('a pair of spectacles', 'spectacles glasses', 'A pair of wire-rimmed spectacles has been left here.')
O[2535] = obj('a golden altar', 'altar golden', ' ')
O[2536] = obj('a heart-shaped medallion', 'medallion heart', 'A heart-shaped medallion of old gold lies here.')
O[2537] = obj('a large iron chest', 'chest large iron', 'A large iron chest stands here, thick with dust.')
O[2538] = obj('an intricately carved key', 'key intricate carved', 'An intricately carved key has been left here.')
O[2539] = obj('a pile of coins', 'coins pile gold', 'A pile of coins lies here.')
O[2540] = obj('a brown travelling cloak', 'cloak brown travelling', 'A travel-worn brown cloak has been left here.')
O[2541] = obj('a chameleon poncho', 'poncho chameleon cloth', 'Some cloth of shifting colours lies on the ground here.')
O[2542] = obj('a pair of old boots', 'boots old worn', 'A pair of old boots stands here; they look very comfortable.')
O[2543] = obj('a seashell ring', 'ring seashell shell', 'A small ring of seashell has been left here.')
O[2544] = obj('a leather backpack', 'backpack pack leather', 'A leather backpack lies here, packed for a hasty journey.')
O[2545] = obj('a herbal brew', 'cup brew herbal tea', 'A cup of herbal brew is here, steaming.')
O[2546] = obj('a loaf of waybread', 'waybread bread loaf', 'A loaf of waybread wrapped in a leaf lies here.')
O[2547] = obj('a meat cleaver', 'cleaver meat', 'A meat cleaver is stuck in the wall here.')
O[2548] = obj('some warded shackles', 'shackles chain warded', 'Some warded chain shackles have been thrown down here.')
O[2549] = obj('a silvered drill dagger', 'dagger silvery silvered drill', 'A long dagger of silvered steel lies here.')
O[2550] = obj('a ward-scroll', 'scroll ward', 'A ward-scroll lies here.')
O[2551] = obj('a bound scroll', 'scroll bound', 'A bound scroll lies here, stirring in a draught.')
O[2552] = obj('a scroll case', 'tube case scroll cylinder', 'A long leather scroll case is rolling about here.')
O[2553] = obj('an old scroll', 'scroll old', 'An old scroll has been left here.')
O[2554] = obj('a scroll on blue paper', 'scroll blue', 'A scroll of blue paper has been left here.')
O[2555] = obj('a stained leather pouch', 'pouch leather stained', 'A leather pouch, stained every colour, lies here.')
O[2556] = obj('a silver stirring spoon', 'spoon silver stirring', 'A silver stirring spoon, bent and blackened, lies here.')
O[2557] = obj('a blue potion', 'potion blue', 'A blue potion is here.')
O[2558] = obj('a bright red potion', 'potion red bright', 'A bright red potion is here.')
O[2559] = obj('a green potion', 'potion green', 'A green potion is here.')
O[2560] = obj('an effervescent potion', 'potion effervescent', 'An effervescent potion fizzes away here.',
              extras={'potion effervescent': 'A fizzing draught in a stoppered vial. The label, in the Mad Alchemist\'s crabbed hand, says only "BETTER".'})
O[2561] = obj('a milky white potion', 'potion white milky', 'A milky white potion is here.')
O[2562] = obj('a black staff', 'staff black', 'A staff of black wood leans against the wall here.')
O[2563] = obj('a golden flute', 'flute golden', 'A golden flute has been left here.')
O[2564] = obj('a small figurine', 'figurine humanoid small', 'A small figurine in the shape of a man stands here.')
O[2565] = obj('a holstered belt', 'belt holster', 'A belt with a wand holster lies here.')
O[2566] = obj('a blackened wand', 'wand blackened', 'A blackened wand lies here.')
O[2567] = obj('a runed chisel', 'chisel runed', 'A runed chisel lies here.')
O[2568] = obj('a beltpouch', 'pouch belt beltpouch', 'A small beltpouch lies here.')
O[2569] = obj('some sparkling dust', 'dust sparkling', 'A pile of sparkling dust glitters here.')
O[2570] = obj('a dark cowl', 'cowl dark', 'A dark cowl lies here, its folds full of shadow.')
O[2571] = obj('an ashen wand', 'wand ashen', 'A wand the colour of ash lies here.')
O[2572] = obj('a huge spiked club', 'club spiked huge', 'A huge spiked club, made for a giant\'s hand, lies here.')
O[2573] = obj('a grey robe', 'robe grey', 'A pile of plain grey cloth has been left here.')
O[2574] = obj('a glinting silver bracelet', 'bracelet silver', 'A glinting hoop of silver lies here.')
O[2575] = obj('a long grey cloak', 'cloak grey long', 'A pile of grey cloth, much mended, has been left here.')
O[2576] = obj('an iron-shod staff', 'staff iron shod', 'A grey staff shod in iron has been left here.')
O[2577] = obj('a ward minor', 'ward minor cube clear', 'A small clear cube sits here, faintly humming.')
O[2578] = obj('a black robe', 'robe black', 'A pile of black cloth lies on the ground here.')
O[2579] = obj('an onyx bracelet', 'bracelet onyx', 'A hoop of black onyx lies here.')
O[2580] = obj('a dark black cloak', 'cloak black dark', 'A pile of black cloth lies on the ground here, darker than it should be.')
O[2581] = obj('a sharp shard of obsidian', 'shard black obsidian', 'A sharp shard of black glass lies here.')
O[2582] = obj('a white robe', 'robe white', 'A pile of spotless white cloth lies on the ground here.')
O[2583] = obj('a white gold bracelet', 'bracelet white gold', 'A hoop of white gold lies here.')
O[2584] = obj('a white cloak', 'cloak white', 'A pile of white cloth lies on the ground here.')
O[2585] = obj('an ivory hilted dagger', 'dagger ivory', 'An ivory hilted dagger has been left here.')
O[2586] = obj('a jewelled collar', 'collar spiked jewelled', 'A small jewelled collar with silver spikes lies here.')
O[2587] = obj('a shimmering cloak of many colours', 'cloak shimmering', 'A shimmering pile of many-coloured cloth lies here.')
O[2588] = obj('a small emerald ring', 'ring emerald', 'A small ring set with a green stone lies here.')
O[2589] = obj('an emerald bracelet', 'bracelet emerald', 'A beautifully cut hoop of emerald lies here.')
O[2590] = obj('a ward major', 'ward major clear crystal cube', 'A large clear crystal cube sits here, humming.')
O[2591] = obj('the ebony kris', 'kris ebony dagger', 'A wavy-bladed knife of ebony lies here.')
O[2592] = obj('a tight green dragon scale shirt', 'shirt green scale dragon', 'A shirt of green dragon scales sewn together lies here.',
              extras={'shirt green scale dragon': 'A shirt of green scales from a dragon killed on the march by the first Archmagus. The scales are still warm.'})
O[2593] = obj('a grey key', 'key grey metal', 'A key of strange grey metal has been left here.')
O[2594] = obj('a black key', 'key black obsidian', 'A key of black obsidian has been left here.')
O[2595] = obj('a white key', 'key white ivory', 'A key of white ivory has been left here.')

RETHEME = {
    'zones': {25: 'The High Tower of Magic'},
    'rooms': R, 'mobs': M, 'objs': O,
}
