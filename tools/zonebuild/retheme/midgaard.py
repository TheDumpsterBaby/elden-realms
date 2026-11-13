"""Midgaard (zones 30 and 31) re-themed as the fort on the front.

Midgaard is the last walled city before the West.  Its single western gate is
the only road into the march; everything east of it exists to keep the wall
manned.  Shops become quartermasters and armourers, cityguards become the
garrison, the Mayor becomes the Lord Commander.  The Temple stays the heart:
the dead walk back out of it.  Levels stay 1-30.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

# ====================================================================== zone 30
R[3000] = dict(name='The Reading Room', desc="""
    A narrow stone room off the temple hall, lined with benches and plain
    wooden desks.  Here the priests copy out the rolls of the fallen, name after
    name in small careful letters, and here soldiers come to read the lists
    before they go west.  It is very quiet.  East lies the temple hall.""")
R[3001] = dict(name='The Temple Of Midgaard', desc="""
    You stand at the southern end of the great temple hall.  The marble walls
    were painted long ago with gods and giants; now they are hung with the
    shields of the fallen, hundreds of them, row above row up into the dark of
    the roof.  Wounded soldiers lie on pallets along the walls, and the air
    smells of candle smoke and blood.

    This is where the dead come back.  Those who fall on the march wake here,
    before the altar to the north, cold and weak and alive.  The great doors lead
    down the steps to the temple square in the south; the reading room is west,
    and the donation alcove east.""")
R[3002] = dict(name="The Clerics' Inner Sanctum", desc="""
    A small chapel lit by a single lamp, where the clerics of the fort pray
    through the night for the men on the wall.  The floor is worn hollow before
    the shrine.  A trapdoor in the corner leads down to the cisterns; the clerics
    go down sometimes to bless the water, and come back up pale.  The bar lies
    east.""")
R[3003] = dict(name='The Bar Of Divination', desc="""
    The clerics' common room, low and smoky, its tables scratched with the names
    of priests who went west with the regiments and did not come back.  Those who
    remain drink quietly here and speak of omens: grey birds, bad water, dreams of
    a door.  The guild entrance is south, the sanctum west.""",
    extras={'sign': 'Scratched into the board above the bar: "Pray for the wall."'})
R[3004] = dict(name="The Entrance To The Clerics' Guild", desc="""
    The entrance hall of the clerics' guild, where healers are trained in haste
    and sent to the front with a satchel of bandages and a holy symbol.  A
    templar stands guard at the inner door.  The temple square is east; the bar
    lies north.""")
R[3005] = dict(name='The Temple Square', desc="""
    A broad square of cracked flagstones before the temple steps.  The fountain
    in its centre still runs, and soldiers fill their canteens here before the
    march.  Carts of the wounded come up from the west gate and unload at the
    steps.  The temple rises north; the clerics' guild is west, the Grunting Boar
    east, and the market square lies south.""")
R[3006] = dict(name='The Entrance Hall Of The Grunting Boar Inn', desc="""
    The entrance hall of the Grunting Boar, the fort's oldest inn, now half
    barracks.  Bedrolls are laid in rows on the floor and kit is hung from every
    beam.  The common room is east, the courier office north, and stairs lead up
    to the rooms.  The temple square is west.""")
R[3007] = dict(name='The Grunting Boar', desc="""
    The common room of the Grunting Boar is loud, crowded and smells of wet wool.
    Off-duty soldiers drink watered ale and play at dice, and nobody talks about
    the west.  Someone has carved the names of the regiments into the bar.  The
    entrance hall is west.""",
    extras={'sign': 'The board behind the bar reads: "One cup a man. By order of the Lord Commander."',
            'writing carving carvings symbols symbol': 'Regiment names are carved into the bar, many of them struck through with a single line: the Ashford Levy, the Riversmeet Foot, the Second of the Wall.'})
R[3008] = dict(name='The Reception', desc="""
    A small room at the top of the stairs where the innkeeper keeps the ledger of
    beds.  Every bed in the fort is spoken for, but a soldier's coin still buys a
    place.  The stairs lead down; the cold-store is north.""",
    extras={'sign': 'Beds are let by the night. Those who do not come back forfeit their kit to the quartermaster.'})
R[3009] = dict(name='The Bakery', desc="""
    The ovens here never go cold.  The baker turns out hard ration bread by the
    cartload for the regiments, and the whole room is grey with flour and heat.
    Sacks from the Granary Fields are stacked to the ceiling.  Main Street is
    south.""",
    extras={'sign': 'Ration bread, hardtack and travelling cakes. Ask the baker what is in stock.',
            'danish pastry': 'There is no time for pastry any more. The baker makes one a week, for the Lord Commander.'})
R[3010] = dict(name='The General Store', desc="""
    The fort provisioner's store: torches, lanterns, sacks and boxes, everything
    a soldier needs on the march and nothing he wants.  Every item is stamped
    with the mark of the garrison.  Main Street is south.""",
    extras={'note': 'A note pinned to the counter: "No credit to men posted west. Pay first."'})
R[3011] = dict(name='The Weapon Shop', desc="""
    The weaponsmith's shop is hung with blades from the Ironworks: plain swords,
    spears, axes and hammers, made fast and made many.  A grindstone screams in the
    back room.  Main Street is south.""",
    extras={'note': 'A note on the wall: "All arms are the property of the fort. Lose it in the west, pay for it in the east."'})
R[3012] = dict(name='Main Street', desc="""
    The western end of Main Street, where the road from the west gate enters the
    fort.  The houses here are shuttered and empty, their owners long fled east,
    and soldiers are billeted in them.  The magic shop is north, the mages' guild
    south; the inner west gate lies west and Main Street runs east.""")
R[3013] = dict(name='Main Street', desc="""
    Main Street runs between tall stone houses whose lower windows have been
    bricked up against the day the wall falls.  Supply carts grind past toward
    the west gate.  The bakery is north and the armoury south; the street runs
    east and west.""")
R[3014] = dict(name='Market Square', desc="""
    The old market square of Midgaard, where merchants once sold silks and spices.
    Now it is a muster ground, and the stalls sell boots, oil and dried meat.  A
    tall statue stands in the centre, hung with black ribbons.  The temple square
    is north and the common square south; Main Street runs east and west.""",
    extras={'statue': 'The statue shows the first Lord Commander of the wall, sword raised toward the west. Black ribbons are tied to his blade, one for each regiment lost. There are a great many ribbons.'})
R[3015] = dict(name='Main Street', desc="""
    Main Street near the market.  A crier's post stands here, plastered with
    notices: rations, curfews, names of deserters.  The general store is north
    and the kennels south; the street runs east and west.""")
R[3016] = dict(name='Main Street', desc="""
    The eastern end of Main Street.  The road widens toward the east gate, and
    wagons wait in a long line to be unloaded.  The weapon shop is north and the
    swordsmen's guild south; the inner east gate lies east.""")
R[3017] = dict(name="The Entrance To The Mages' Guild", desc="""
    The entrance to the mages' guild, its doors scorched black from an accident
    nobody will explain.  The mages of the fort study the West's sorcery so they
    can turn it back, and some of them study it too closely.  Main Street is
    north; the guild bar lies south.""")
R[3018] = dict(name="The Mages' Bar", desc="""
    A dim room where the guild's mages drink and argue in low voices over charts
    of the march.  One wall is covered in drawings of a grey radiance, made by an
    apprentice who has since been locked away.  The entrance is north and the
    laboratory east.""")
R[3019] = dict(name="The Mages' Laboratory", desc="""
    The laboratory stinks of sulphur and old blood.  Jars on the shelves hold
    things brought back from the west: a hand of ash, a grey eye, a moth that will
    not die.  A grate in the floor leads down into the cisterns.  The bar is
    west.""")
R[3020] = dict(name='The Armory', desc="""
    The armourer's shop, hot and loud.  Breastplates, mail shirts and shields
    hang in rows, and the dented ones that came back from the west are piled in a
    corner for mending.  Some of them still have holes in them.  Main Street is
    north.""",
    extras={'note': 'A note by the door: "Armour returned from the dead is sold at half price. It brought nobody luck the first time."'})
R[3021] = dict(name='The Entrance Hall To The Guild Of Swordsmen', desc="""
    The entrance hall of the swordsmen's guild, its walls hung with the arms of
    warriors who held the wall.  A knight stands at the inner door.  Main Street
    is north; the guild bar lies east.""")
R[3022] = dict(name='The Bar Of Swordsmen', desc="""
    The swordsmen's bar is a rough hall of benches and long tables where veterans
    drink, and young warriors listen to them.  The talk is all of the march: of
    Ashford burning, of the Fens, of what waits in the hills.  The yard is south,
    the hall west.""")
R[3023] = dict(name='The Tournament And Practice Yard', desc="""
    A walled yard of packed earth where the swordsmen drill from dawn to dark.
    Straw men stand in rows, hacked to pieces and stuffed again, and a grate in
    the corner leads down to the cisterns.  The bar is north.""")
R[3024] = dict(name='The Eastern End Of Poor Alley', desc="""
    Poor Alley ends here in a huddle of lean-tos built from broken carts.  The
    poorest of the fort live here: widows, cripples, men too broken for the wall.
    The common square is east, the Grubby Inn south, and the alley runs west.""")
R[3025] = dict(name='The Common Square', desc="""
    A small square where the common folk of the fort gather, few as they are now.
    A memorial post stands here, its sides covered with scratched names and tied
    tokens: a child's shoe, a ribbon, a wooden horse.  Women come to stand by it
    and say nothing.  The market is north, the dump south, Poor Alley west and the
    dark alley east.""")
R[3026] = dict(name='The Dark Alley', desc="""
    A narrow alley in permanent shadow between the backs of tall houses.  The
    gutters here run grey, and people who sleep here wake up tired.  The thieves'
    guild is south; the common square west and the levee alley east.""",
    extras={'guild': 'The sign over the door to the south shows a black glove. Nobody in the fort admits to knowing what it means.'})
R[3027] = dict(name='The Entrance Hall To The Guild Of Thieves', desc="""
    A bare room with a single door.  The fort pretends the thieves' guild does not
    exist, and the guild pretends to be a warehouse; both find the other useful
    when there is smuggling to be done, or a deserter to be found.  The alley is
    north and the bar east.""")
R[3028] = dict(name="The Thieves' Bar", desc="""
    A low cellar bar.  Smugglers, cut-purses and quiet men from the Supply Road
    drink here and trade in what the quartermaster does not sell.  The secret yard
    is south and the entrance hall west.""",
    extras={'furniture': 'The tables and chairs are all from the fort stores, still stamped with the garrison mark.'})
R[3029] = dict(name='The Secret Yard', desc="""
    A walled yard hidden behind the guild, stacked with crates that did not come
    through the east gate.  A hatch in the ground leads down into the sewers,
    the smugglers' road under the city.  The bar is north.""")
R[3030] = dict(name='The Dump', desc="""
    The fort's midden, a reeking pit where broken kit, spoiled meal and worse is
    tipped.  Carrion birds pick over it, and the mud at its bottom moves slowly
    when nothing is touching it.  A drain leads down into the sewers.  The common
    square is north.""")
R[3031] = dict(name='The Pet Shop', desc="""
    The kennels of the fort, where hounds are bred and sold for the march:
    trackers, ratters and great war-mastiffs that can bring down a ghoul.  The
    noise is deafening.  Main Street is north.""",
    extras={'sign': 'Hounds for the march. Trained, fed and wormed. They will not run.'})
R[3032] = dict(name='Pet Shop Store', desc="""
    The back kennels, a row of cages where the dogs wait to be sold.  They are
    lean and quiet and watch the door.""")
R[3033] = dict(name='The Magic Shop', desc="""
    A narrow shop crammed with scrolls, potions and wands, sold to soldiers by a
    war-magus who has been west and come back.  Wards are chalked on the floor in
    a circle around his counter.  Main Street is south.""")
R[3040] = dict(name='Inside The West Gate Of Midgaard', desc="""
    You stand inside the great west gate, the only gate in the only wall between
    the West and everything else.  The doors are oak bound in iron, scarred with
    old burns, and they are kept shut and barred except to let the regiments out
    and the wounded in.  Crossbowmen watch from the towers.  Through the gate lies
    the march; Main Street runs east, and the wall road follows the wall south.""",
    extras={'gate': 'Oak doors as thick as a man is tall, bound in iron and scored with burns and claw marks. Someone has painted on the inside, in letters a foot high: NOTHING COMES BACK THROUGH THIS GATE THAT DID NOT LEAVE BY IT.',
            'bridge footbridge': 'A covered footbridge joins the two gate towers above the doors. Crossbowmen pace it day and night.',
            'tower towers': 'Two squat towers of grey stone flank the gate, their arrow slits facing west.',
            'wall': 'The west wall is forty feet of grey stone, blackened along its face by fire. The march begins at its foot.'})
R[3041] = dict(name='Inside The East Gate Of Midgaard', desc="""
    The inner side of the east gate, where everything the fort needs comes in:
    grain, iron, men, and the dead to be buried.  Clerks with ledgers count every
    cart.  Through the gate lie the Supply Road and the support camps; Main Street
    runs west, and the water shop is south.""",
    extras={'gate': 'Heavy doors bound with iron. The east gate is opened at dawn and shut at dusk, and never otherwise.',
            'bridge footbridge': 'A footbridge joins the gate towers high above.',
            'tower towers': 'The east towers are lit all night, beacons for the supply wagons on the road.',
            'wall': 'Grey stone, tall and well kept. The east wall has never been tested, and everybody in the fort prays that it never will be.'})
R[3042] = dict(name='Wall Road', desc="""
    The wall road runs along the inside of the west wall, a narrow lane between
    the stone and the backs of the barracks.  Stairs climb to the wall walk every
    hundred paces, and sentries call to one another overhead.  The gate is north;
    the road continues south.""",
    extras={'wall': 'The inner face of the west wall is covered in scratched tallies: days on the wall, men lost, things killed.'})
R[3043] = dict(name='Wall Road', desc="""
    A bend in the wall road where Poor Alley runs off east.  Someone has painted
    words on the wall in big uneven letters.  The road runs north toward the gate
    and south toward the river.""",
    extras={'wall writing letters': 'Painted in red: "IT IS NOT A WAR. IT IS A TIDE." Someone has tried to scrub it off.',
            'wall': 'The wall is grey stone, high and very old.'})
R[3044] = dict(name='Poor Alley', desc="""
    A muddy alley of shacks where the families of soldiers live in two rooms
    to a household.  Laundry hangs between the eaves, and children play at
    soldiers in the mud, and lose.  The alley runs east; the wall road is west.""")
R[3045] = dict(name='The Dark Alley At The Levee', desc="""
    The dark alley ends at the river levee.  The air is damp and cold, and the
    smell of the river is rank: the water comes down from the west now.  The
    levee lies south, and the alley runs east and west.""")
R[3046] = dict(name='The Eastern End Of The Alley', desc="""
    A dead end of the alley, walled in by the back of an old warehouse.  Rats
    move along the gutters in a slow grey line.  The warehouse is south; the alley
    runs back west.""")
R[3047] = dict(name='Wall Road', desc="""
    The southern stretch of the wall road, where the wall comes down to meet the
    river.  A watch-fire burns in an iron basket, and the sentries here watch the
    water as much as the west.  The road continues north, and a bridge crosses
    the river to the south.""",
    extras={'wall': 'Where the wall meets the river, iron grates are sunk into the water to stop anything coming down it.'})
R[3048] = dict(name='Grubby Inn', desc="""
    The Grubby Inn is the worst drinking hole in the fort, and the cheapest.  The
    floor is sticky, the ale is brewed from the sweepings of the granary, and the
    landlord asks no questions of deserters.  Poor Alley is north.""")
R[3049] = dict(name='The Levee', desc="""
    A stone levee above the river where the fort's boats are moored.  The water
    is dark and slow and smells of rot, and things float down it from the west
    that the ferrymen pull out with hooks and do not talk about.  The alley is
    north; the river lies south.""")
R[3050] = dict(name='The Deserted Warehouse', desc="""
    An empty warehouse at the end of the alley, its roof half fallen in.  Old
    nets and broken oars lie in heaps, and a boatman sleeps among them.  The
    alley is north.""")
R[3051] = dict(name='On The Bridge', desc="""
    A stone bridge crosses the river where the wall meets the water.  To the
    north lies the upper fort with its gates and guilds; to the south, the lower
    ward with the garrison headquarters, the parade and the graves.  The water
    runs dark beneath you.""",
    extras={'bridge': 'An old stone bridge, its parapet chipped by arrows from some siege before anyone now living was born.',
            'opening': 'Under the bridge the river runs into an iron grate set in the wall.',
            'wall': 'The west wall comes right down into the river here.'})
R[3052] = dict(
    extras={'gate': 'The west gate is shut and barred from the inside. Its outer face is gouged with claw marks and blackened with fire.',
            'bridge footbridge': 'Crossbowmen on the footbridge between the towers watch you, and the road behind you.',
            'tower towers': 'Two squat towers of grey stone, their faces scorched, their arrow slits facing west.',
            'wall': 'Forty feet of grey stone, blackened by fire. Bodies hang from the battlements as a warning to the West, which has never cared.'})
R[3053] = dict(
    extras={'gate': 'The east gate stands open by day. Clerks at a table beside it count every wagon.',
            'bridge footbridge': 'A footbridge joins the gate towers high above.',
            'tower towers': 'The east towers burn beacons all night for the supply wagons.',
            'wall': 'Grey stone, tall and well kept.'})
R[3054] = dict(name='By The Temple Altar', desc="""
    You stand before the great altar at the north end of the temple hall.  This is
    where the fallen wake: one moment dead in the west, the next lying on the cold
    stone here, gasping, while the priests of the last breath kneel over them.
    Behind the altar a statue of the old god holds out empty hands.  The hall is
    south; a passage east leads out to the Hospice of the Last Rites, and the way
    behind the altar is north.""",
    extras={'altar': 'A great slab of white marble, worn smooth by the bodies of the returned. The stone is always cold.',
            'statue odin king god': 'An old god in a crown, holding out empty hands. The priests say he gives back what the West takes, at a price. Every soldier in the fort has touched his feet before going west.'})
R[3055] = dict(name="Odin's Store", desc="""
    A sealed storeroom behind the temple where the priests keep what the dead
    leave behind.""")
R[3058] = dict(name='Ye Olde Water Shoppe', desc="""
    The fort's water-seller works from a cool stone room by the east gate, selling
    clean water from the deep wells to soldiers bound west.  The water of the
    river and the cisterns is not to be trusted any more.  The gate is north.""")
R[3059] = dict(name='Behind The Temple Altar', desc="""
    A narrow passage behind the altar where the priests keep their lamps and
    oils.  A door at the north end opens onto the muster field behind the temple.
    The altar is south.""")
R[3060] = dict(name='The Muster Field', desc="""
    A wide field behind the temple, trampled to mud by drilling feet.  Regiments
    form up here before they march to the west gate, and the field is ringed with
    stakes hung with banners.  The temple lies south; the field runs north.""")
R[3061] = dict(name='The Muster Field', desc="""
    The middle of the muster field.  A recruiting sergeant's table stands here
    under an awning, and a line of ragged young men and women waits in front of
    it.  East, a gate in the palisade opens onto the Recruit Yards; west, a dirt
    path leads to the gallows.  The field runs north and south.""")
R[3062] = dict(name='The Post Office', desc="""
    The courier office, where letters from the front are sorted and carried east.
    Many letters come back unopened, and they are kept in a box by the door that
    nobody likes to look at.  The entrance hall is south.""",
    extras={'sign': 'Letters east carried weekly. Letters west carried when the road is open.',
            'letters envelopes assorted': 'Bundles of letters wait to be carried. A great many are addressed to Ashford, which no longer exists.',
            'cobwebs': 'Grey cobwebs in the corners. They are thicker than they should be.',
            'crates opened large': 'Crates of letters that could not be delivered, because there was nobody left to deliver them to.',
            'WANTED posters poster wall': 'WANTED: deserters from the Second of the Wall. Reward on return, alive or not.'})
R[3063] = dict(name='The Midgaard Donation Room', desc="""
    A small alcove off the temple where those who have more than they need leave
    it for those going west.  Soldiers coming back leave the kit of friends who
    did not.  The temple hall is west.""")
R[3064] = dict(name='The Cryogenic Center', desc="""
    A cold room beneath the inn where those who must leave the fort for a long
    time may sleep in ice until they are needed.  The cryogenicist keeps the
    sleepers' names in a long ledger.  The stairs lead south.""")
R[3065] = dict(name='The Muster Field', desc="""
    The northern end of the muster field, where the ground rises to a palisade of
    sharpened stakes.  Beyond it the old north road is gone: the bridge over the
    gorge was pulled down when the war began, so that the only road west is the
    one through the gate.  The field runs south.""",
    exits={'n': 'The palisade, and beyond it the gorge where the north bridge used to be.',
           's': 'The muster field runs south toward the temple.'},
    extras={'palisade stakes gorge bridge': 'The broken stumps of the north bridge stand on either side of a deep gorge. It was torn down on the Lord Commander\'s orders, to give the West only one door.'})
R[3066] = dict(name='The Gallows Path', desc="""
    A dirt path at the edge of the muster field ends at a gallows of black timber.
    Deserters hang here, and the occasional spy from the West: they are not hard to
    tell, because the spies do not rot.  The field is east.""")

# ====================================================================== zone 31
def street(name, text, **kw):
    return dict(name=name, desc=text, **kw)

R[3100] = street('The Northwest End Of The Parade', """
    The lower ward begins here at the foot of the bridge.  The old concourse has
    been made a parade ground, its paving stones scored by iron heels.  The bridge
    is north; the parade runs east and south.""")
for v, extra in ((3101, 'Barracks line the north side, their doors marked with regiment numbers.'),
                 (3102, 'The garden gate is south, hung with a wreath of dry leaves.'),
                 (3103, 'Officers\' billets face the parade, their windows shuttered.')):
    R[v] = street('The Parade', """
    The parade runs along the top of the lower ward, wide enough for a regiment
    to march twelve abreast.  Every morning a drum sounds here and the garrison
    forms up in its ranks.  %s""" % extra)
R[3104] = street('The Northeast End Of The Parade', """
    The parade ends at the east wall of the lower ward.  Sentries walk the wall
    above, watching the lanes to the east, which have never yet needed watching.
    The parade runs west and south.""",
    extras={'wall': 'The east wall of the lower ward. It is low and old, and nobody has bothered to strengthen it.'})
R[3105] = street('The Garden Gate', """
    The gate of what was once the city park, now the Memorial Garden.  Its lawns
    were dug up for vegetables when the siege rations began, and the paths are
    lined with wooden markers for those who died with no body to bury.  The parade
    is north, a cookhouse east, and the garden paths south.""")
R[3106] = street('The Garden Cookhouse', """
    The old park cafe now cooks for the lower ward.  A great pot of thin stew
    bubbles all day, and a tired woman ladles it out to anyone with a garrison
    token.  The garden gate is west.""")
for v, d in ((3107, 'The path turns here between rows of cabbages and wooden markers.'),
             (3108, 'A narrow path among the memorial markers, each carved with a name and a place: Ashford, the Fens, the Barrow Hills.'),
             (3109, 'Crows sit on the markers here and do not fly when you pass.')):
    R[v] = street('A Path In The Memorial Garden', """
    %s  The garden is very quiet; people come here to remember, not to talk.""" % d)
R[3110] = street('Garrison Headquarters', """
    The headquarters of the garrison: a hall of maps, muster rolls and tired
    officers.  The great map on the wall shows the march in fifteen bands of
    deepening grey, and pins mark where the regiments are.  There are not many
    pins.  The door is east.""")
R[3111] = street('Park Road', """
    Park Road runs north and south past the garrison headquarters, whose door is
    west.  Soldiers come and go at a run with orders.  The memorial garden's west
    gate is east.""",
    extras={'building door sign': 'The sign above the door reads: GARRISON HEADQUARTERS. ALL ORDERS FROM THE LORD COMMANDER.'})
R[3112] = street('The Western Garden Gate', """
    A small gate on the west side of the memorial garden.  Park Road is west; the
    garden path runs east.""")
R[3113] = street('A Path In The Memorial Garden', """
    A path through the garden where the oldest markers stand, from the first years
    of the war, their names weathered nearly away.  The path runs north, east and
    west.""")
R[3114] = street('The Pond', """
    A dark pond in the middle of the garden.  Its water came from the river and
    has gone grey and still, and nothing grows on its banks.  A black swan glides
    on it in silence.  Paths lead east and west.""")
R[3115] = street('A Path In The Memorial Garden', """
    The path passes a long stone set with the names of a whole regiment, the
    Riversmeet Foot, every one of them lost on the same night.  The path runs
    north, east and west.""")
R[3116] = street('The Eastern Garden Gate', """
    The eastern gate of the memorial garden.  Emerald Avenue is east; the garden
    path runs west.""")
avenue = 'Emerald Avenue was the road of the rich, before they fled east.  Its tall houses are now billets, storehouses and field hospitals.'
R[3117] = street('Emerald Avenue', """
    %s  The commander's waiting room is east; the garden gate is west, and the
    avenue runs north and south.""" % avenue)
R[3118] = street('Park Road', """
    Park Road runs north and south between barracks and stables.  The road is
    churned to mud by horses and carts.""")
R[3119] = street('Emerald Avenue', """
    %s  The avenue runs north and west.""" % avenue)
R[3120] = street('The Road Crossing', """
    The crossroads of the lower ward, where Park Road meets Emerald Avenue.  A
    signpost points the way, and an iron ladder climbs a tower here to a house
    built high above the roofs.  Roads lead in all four directions.""",
    extras={'sign': 'North: Emerald Avenue. South: the lower lanes. East and west: Park Road. Up: Redferne. All civilians to keep off the roads at curfew.',
            'chain': 'A heavy chain hangs from the ladder, to drag it up in a siege.'})
R[3121] = street('Emerald Avenue', """
    %s  The avenue runs east and south.""" % avenue)
R[3122] = street('Park Road', """
    Park Road, lined with the empty shops of tradesmen who have gone to the
    Ironworks.  Elm Street runs east; the road runs north and south.""")
R[3123] = street('Elm Street', """
    A short street of officers' houses with black wreaths on many of the doors.
    It runs east and west.""")
R[3124] = street('The End Of Elm Street', """
    Elm Street ends at a great elm tree, the last tree in the lower ward.  Widows
    tie ribbons to its branches.  The street runs west.""")
R[3125] = street('Emerald Avenue', """
    %s  The avenue runs north and south.""" % avenue)
R[3126] = street('Park Road', """
    The southern stretch of Park Road, quiet but for the creak of carts carrying
    the dead to the graves.  The road runs north and south.""")
R[3127] = street('On The Parade', """
    The western end of the lower parade, at the foot of the wall.  The parade runs
    east, and the upper parade is north.""")
R[3128] = street('On The Parade', """
    The lower parade, where the dead are carried in procession on their way to
    the graves.  The parade runs east and west, and the avenue north.""")
R[3129] = street('On The Parade', """
    The lower parade before the graveyard gate.  A bell hangs here that is rung
    for every burial; it rings most days.  The gate south opens onto the Field of
    the Fallen, and the parade runs east and west, with Park Road north.""")
R[3130] = street('On The Parade', """
    The eastern end of the lower parade.  It runs west, and north toward the
    upper parade.""")
R[3131] = street('Park Road', """
    The top of Park Road, where it meets the parade.  The road runs north and
    south.""")
R[3132] = street('Emerald Avenue', """
    %s  Penny Lane runs east; the avenue runs north and south.""" % avenue)
R[3133] = street('Emerald Avenue', """
    %s  The avenue runs east and south.""" % avenue)
R[3134] = street('Emerald Avenue', """
    %s  The avenue runs north and west.""" % avenue)
R[3135] = street('Park Road', """
    Park Road runs north and east between storehouses guarded by bored soldiers.""")
R[3136] = street('Park Road', """
    Park Road, running south and west past a stable of war-horses.  The horses
    stamp and shy at nothing.""")
R[3137] = street('The Waiting Room', """
    The anteroom of the Lord Commander's office.  Hard chairs stand against the
    walls, and messengers from the front wait in them, mud-stained and grey with
    exhaustion, holding their dispatches.  The office is east; the avenue west.""",
    extras={'chair chairs': 'Plain wooden chairs, worn smooth by waiting.',
            'desk': 'The adjutant\'s desk, piled with dispatches and casualty lists.',
            'typewriter': 'A brass contraption for copying orders. It has jammed.'})
R[3138] = street("The Lord Commander's Office", """
    The Lord Commander's office is a plain room with a great table covered in maps
    of the march.  Every map ends at the same place, far in the west, where the
    mapmakers have drawn nothing at all and written only: HERE IT IS.  The
    waiting room is west.""",
    extras={'desk': 'The commander\'s table, covered in maps, reports and a cold cup of tea.',
            'chair armchair': 'A worn leather chair. The commander rarely sits in it.'})
R[3139] = street('Penny Lane', """
    A narrow lane of small houses where the garrison's craftsmen live: smiths,
    fletchers, cobblers.  It runs east and west.""")
R[3140] = street('Penny Lane', """
    Penny Lane turns north here past a fletcher's shed full of drying arrows.  The
    lane runs north and west.""")
R[3141] = street('The End Of Penny Lane', """
    Penny Lane ends at a small locked house.  The lane runs south.""")
R[3150] = street('The Field of the Fallen', """
    A gravel road runs south through the Field of the Fallen.  Graves crowd both
    sides, fresh earth on old, and the gravediggers cannot keep up.  The parade is
    north.""")
R[3151] = street('The Field of the Fallen', """
    The gravel road passes between mass graves marked only with regiment
    numbers.  Lime has been scattered over them, and still the earth moves
    sometimes at night.  The road runs north and south.""")
R[3152] = street('The Field of the Fallen', """
    A pyre stands here, where those who died in the west are burned before they
    can be buried, as the priests now insist.  The ashes blow over everything.
    The road runs north and south.""")
R[3153] = street('The Field of the Fallen', """
    The far end of the graves, where the oldest stones lean in the mud.  Some of
    the graves here are open, and the earth around them is scratched from the
    inside.  The road runs north and south.""")
R[3154] = street('In Front Of The Chapel', """
    A small stone chapel at the end of the graveyard, where the dead lie for a
    night before burial with a priest to watch them.  The road runs north, and
    the chapel door is south.""")
R[3155] = street('Inside The Chapel', """
    A cold chapel of bare stone.  Coffins lie on trestles before the altar, each
    with an iron nail through its lid, for the dead of the West do not always
    stay dead.  The door is north.""",
    extras={'glass windows': 'Narrow windows of grey glass. The light through them is the colour of ash.',
            'altar': 'A plain altar with a single candle that is never let go out.',
            'benches rows': 'A few rough benches for the mourners. Fewer come every year; there are fewer left to mourn.'})
R[3200] = street('Under The Bridge', """
    The river runs dark under the stone bridge.  Iron grates are sunk into the
    water at the wall, and things caught on them stir in the current.  The river
    runs east.""",
    extras={'wall': 'Iron grates bar the river where it passes under the wall. They are thick with weed and worse.'})
for v in (3201, 3202, 3203, 3204, 3205):
    R[v] = street('On The River', """
    The river runs slow and dark through the fort.  It comes from the west now,
    and its water is grey and cold and smells of rot.  Bodies sometimes come down
    it, and the ferrymen hook them out before they reach the grates.""")

# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d

M[3000] = mob('the war-magus', 'magus war wizard', 'A war-magus stands behind the counter, muttering wards under his breath.',
              'An old mage who went west with the first regiments and came back alone. His eyes are clouded grey, and he can see things nobody else can. He sells what the fort needs to fight sorcery with sorcery.')
M[3001] = mob('the ration baker', 'baker ration', 'The ration baker wipes flour from her face and looks at you wearily.',
              'A broad-armed woman grey with flour, who has not slept a full night since the war began. Her bread is hard and plain and keeps for a month on the march.', sex=2)
M[3002] = mob('the provisioner', 'provisioner grocer', 'The fort provisioner stands at the counter, ticking items off a ledger.',
              'A thin, precise man who knows the price of every torch and sack in the fort, and the cost of running out.')
M[3003] = mob('the weaponsmith', 'weaponsmith smith', 'The weaponsmith is grinding an edge onto a sword from the Ironworks.',
              'A burly smith with burn scars up both arms. He sells blades to boys who will die with them in their hands, and he does not like to think about it.')
M[3004] = mob('the armourer', 'armourer armorer', 'The armourer is hammering a dent out of a breastplate.',
              'A stocky armourer who mends what comes back from the west. He has stopped looking at the holes.')
M[3005] = mob('the innkeeper', 'innkeeper receptionist', 'The innkeeper is checking the ledger of beds.',
              'A tired woman with a pen behind her ear, who keeps track of who sleeps in the fort, and who does not come back to their bed.', sex=2)
M[3006] = mob('the ferryman', 'ferryman captain stolar', 'The ferryman leans on a boathook, watching the river.',
              'A grizzled boatman who works the river with a hook, pulling out what comes down from the west. He will sell you a boat, if you are fool enough to need one.')
M[3007] = mob('the boatman', 'boatman sailor', 'A boatman sleeps among the nets, snoring.',
              'A boatman too drunk to work the river and too tired to care.')
M[3009] = mob('the water-seller', 'water seller wally watermaster', 'The water-seller stands behind a row of clean water jars.',
              'A careful man who draws his water from the deep wells under the fort and seals every jar with wax. Nobody drinks from the river any more.')
M[3010] = mob('the courier-master', 'courier master postmaster', 'The courier-master is sorting letters into bundles.',
              'A precise old man who sorts the letters of the living and keeps the letters of the dead.')
M[3020] = mob("the master of the mages' guild", 'master guildmaster mage', 'The master of the mages\' guild is studying a chart of the march.',
              'A gaunt mage who teaches the young to fight the West with fire and will. She does not let them read the books in the locked case.', sex=2)
M[3021] = mob("the master of the clerics' guild", 'master guildmaster priest cleric', 'The master of the clerics\' guild kneels in prayer.',
              'An old priest whose hands shake except when he heals. He has buried more soldiers than live in the fort.')
M[3022] = mob('the guildmaster of the black glove', 'master guildmaster thief', 'A soft-spoken man counts coins in the shadows.',
              'The master of a guild that does not exist. He trains those who will scout the march unseen, and he takes his cut of everything smuggled through the fort.')
M[3023] = mob("the master of the swordsmen's guild", 'master guildmaster warrior swordsman', 'The master of the swordsmen\'s guild watches the drill with folded arms.',
              'A one-eyed veteran of the first siege. He trains warriors to hold a line, because a line is all that stands between the West and everything else.')
M[3024] = mob('a warded sentry', 'sentry warded sorcerer', 'A sentry in a robe stitched with wards stands at the inner door.',
              'A mage of the guild set to guard the door. The wards on her robe glow faintly when you come near.', sex=2)
M[3025] = mob('a templar', 'templar knight', 'A templar in a grey surcoat guards the inner door.',
              'A knight of the temple sworn to guard the clerics, and to burn any of them who come back from the west wrong.')
M[3026] = mob('a cut-throat', 'cutthroat assassin', 'A cut-throat leans in the doorway, cleaning his nails with a knife.',
              'The guild\'s doorman. He looks at you as if measuring you for a shroud.')
M[3027] = mob('a knight of the wall', 'knight wall', 'A knight of the wall stands guard at the inner door.',
              'A knight in battered plate, sworn to the defence of the west wall. He has been west and it shows in his eyes.')
M[3040] = mob('the landlord of the Boar', 'landlord bartender', 'The landlord of the Grunting Boar is drawing watered ale.',
              'A heavy man who runs the oldest inn in the fort, and pours one cup a man by order of the Lord Commander.')
for v in (3041, 3042, 3043, 3044, 3045):
    M[v] = mob('the potboy', 'potboy waiter', 'A potboy is carrying a tray of cups.',
               'A thin boy too young for the wall, who works the bars and listens to the soldiers talk.')
M[3046] = mob('Filthy', 'filthy landlord', 'Filthy is standing behind the bar, grinning with brown teeth.',
              'The landlord of the Grubby Inn, who asks no questions and serves drink that would strip paint.')
M[3059] = mob('the provost marshal', 'provost marshal peacekeeper', 'The provost marshal stands here, watching for deserters.',
              'A hard-faced officer whose job is to keep order in the fort and to hang those who run. He is very good at his job.')
M[3060] = mob('a soldier of the garrison', 'soldier garrison guard cityguard', 'A soldier of the garrison stands here in a grey-trimmed tabard.',
              'A soldier of the fort, tired and thin, his tabard patched and his sword well kept. He would die on the wall for you, and probably will.')
M[3061] = mob('the corpse-carter', 'carter corpse janitor', 'A corpse-carter pushes a handcart along, picking things up.',
              'An old man who carts away whatever is left in the streets: rubbish, kit, and sometimes bodies.')
M[3062] = mob('a starving cur', 'cur dog starving fido', 'A starving cur is sniffing at the gutter.',
              'A thin, ugly dog, all ribs and teeth, that eats whatever it can find, including the dead.')
M[3063] = mob('a sellsword', 'sellsword mercenary', 'A sellsword lounges here, looking for work or trouble.',
              'A hired blade from the eastern kingdoms who came for the garrison\'s pay and has not yet worked out that nobody comes back to spend it.')
M[3064] = mob('a shell-shocked veteran', 'veteran drunk', 'A shell-shocked veteran sits here, drinking and staring at nothing.',
              'An old soldier who came back from the Barrow Hills and has not stopped shaking. He drinks so he does not dream.')
M[3065] = mob('a refugee beggar', 'beggar refugee', 'A refugee beggar holds out a thin hand.',
              'Someone who fled the West with nothing and found nothing here either.')
M[3066] = mob('a carrion hound', 'hound carrion dog', 'A carrion hound slinks along, its eyes faintly grey.',
              'A big grey-eyed dog that came in through the west gate one night and would not leave. It eats the dead and watches the living.')
M[3067] = mob('a gate warden', 'warden gate guard cityguard', 'A gate warden in heavy mail stands guard here.',
              'One of the wardens of the gates, picked men who decide who goes out to the west and who is let back in. Those who come back wrong do not get in.')
M[3068] = mob('a grey gelatinous blob', 'blob grey gelatinous', 'A grey gelatinous blob slides along the ground, cleaning as it goes.',
              'A mass of grey jelly that crawled up out of the cisterns. It eats rubbish, and nobody is quite sure what else.')
M[3089] = mob('the kennelmaster', 'kennelmaster pet shop boy', 'The kennelmaster is feeding the dogs.',
              'A scarred woman who breeds hounds for the march. She knows every one of them by name, and remembers the ones that did not come back.', sex=2)
M[3090] = mob('a ratting cat', 'cat ratting kitten', 'A lean ratting cat watches you.',
              'A scarred grey cat bred to keep the rats of the cisterns down.')
M[3091] = mob('a war-hound pup', 'pup puppy hound', 'A war-hound pup tumbles about.',
              'A big-pawed pup that will grow into a war-hound, if it lives that long.')
M[3092] = mob('a tracking hound', 'hound tracking beagle', 'A tracking hound sniffs the air.',
              'A long-eared hound with a nose that can find a man in the march, or what is left of him.')
M[3093] = mob('a war-mastiff', 'mastiff war rottweiler', 'A war-mastiff stares at you, silent.',
              'A huge dog in a spiked collar, trained to bring down ghouls.')
M[3094] = mob('a tamed wolf', 'wolf tamed', 'A tamed wolf paces its cage.',
              'A wolf caught as a cub on the march. It has never forgotten what it is.')
M[3095] = mob('the cryogenicist', 'cryogenicist', 'The cryogenicist is checking the ice in the sleepers\' cells.',
              'A pale, careful man who keeps the sleepers cold until the fort needs them.')
M[3100] = mob('the cook', 'cook maid', 'The cook is ladling out stew.',
              'A tired woman with a great ladle who feeds the lower ward on very little.', sex=2)
M[3101] = mob('the gravedigger', 'gravedigger sexton', 'The gravedigger leans on his shovel.',
              'An old man with dirt under every nail, who digs from dawn to dark and never catches up.')
M[3102] = mob('the sergeant-at-arms', 'sergeant arms chief guard', 'The sergeant-at-arms is bellowing orders.',
              'The garrison\'s sergeant-at-arms, a bull-necked veteran with a voice that can be heard on the far wall.')
M[3103] = mob('a weary soldier', 'soldier weary cityguard', 'A weary soldier is sitting with his head in his hands.',
              'A soldier just back from the march, who has not yet stopped seeing it.')
M[3104] = mob("the commander's adjutant", 'adjutant secretary', 'The commander\'s adjutant is sorting dispatches.',
              'A neat young officer with ink-stained fingers, who reads every casualty list before the commander does, so he can soften it.')
M[3105] = mob('the Lord Commander', 'lord commander mayor', 'The Lord Commander of the wall stands here, grey-haired and straight-backed.',
              'The commander of Midgaard and of the war, an old soldier who has held the west wall for twenty years and buried two sons in the march. He walks the fort every day so the soldiers can see him, and opens the gates himself.')
M[3106] = mob('the herald', 'herald crier', 'The herald is reading out names from a long scroll.',
              'The fort\'s herald, who reads the names of the dead at every crossroad, every morning. It takes longer every year.')
M[3120] = mob('a black swan', 'swan black', 'A black swan glides on the grey water.',
              'A black swan, silent and graceful, on the dead pond.')
M[3121] = mob('a starving duckling', 'duckling starving', 'A starving duckling peeps miserably.',
              'A thin duckling. There is nothing left in the pond to eat.')
M[3122] = mob('a carrion crow', 'crow carrion', 'A carrion crow sits on a marker, watching you.',
              'A crow with a knowing black eye. The crows have grown fat since the war began.')
M[3123] = mob('a grey duck', 'duck grey', 'A grey duck paddles slowly.',
              'An old duck, its feathers gone grey like the water.')

# ====================================================================== objs
O[3000] = dict(short='a barrel of watered ale', aliases='barrel ale beer')
O[3001] = dict(short='a bottle of watered ale', aliases='bottle ale beer')
O[3002] = dict(short='a bottle of dark ale', aliases='bottle dark ale')
O[3003] = dict(short='a bottle of firewater', aliases='bottle firewater firebreather')
O[3004] = dict(short='a bottle of granary beer', aliases='bottle granary beer local')
O[3009] = dict(short='a travelling cake', aliases='cake travelling waybread bread', long='A hard travelling cake lies here.')
O[3010] = dict(short='a loaf of ration bread', aliases='bread loaf ration', long='A loaf of hard ration bread lies here.')
O[3011] = dict(short="the Lord Commander's pastry", aliases='pastry danish', long='A sticky pastry lies here. Someone will miss it.')
O[3012] = dict(short='a strip of salt pork', aliases='pork salt strip taco', long='A strip of salt pork lies here.')
O[3013] = dict(short='a bowl of camp stew', aliases='stew bowl camp burrito', long='A bowl of thin camp stew sits here.')
O[3014] = dict(short='a handful of hardtack', aliases='hardtack handful nachos', long='A handful of hardtack lies here.')
O[3034] = dict(short="the paymaster's strongbox", aliases='strongbox paymaster box atm teller bank',
               long="The paymaster's iron strongbox stands against the wall, guarded by a clerk.",
               extras={'strongbox paymaster box atm teller bank': "A clerk sits by the iron box with a ledger. Soldiers' pay is kept here against the day they come back for it. To use it, type BALANCE, WITHDRAW <amount> or DEPOSIT <amount>."})
O[3035] = dict(short='the temple fountain', long='The temple fountain still runs clear here.')
O[3036] = dict(short="a paymaster's token", aliases='token paymaster cashcard card atm', long="A paymaster's iron token lies here.")
O[3096] = dict(short='the soldiers\' notice board', aliases='board notice soldiers social bulletin')
O[3098] = dict(short='the temple board', aliases='board temple holy bulletin')
O[3100] = dict(short='a cup of tea', aliases='cup tea')
O[3101] = dict(short='a cup of chicory', aliases='cup chicory coffee')
O[3104] = dict(short='a garrison canteen', aliases='canteen garrison water')
O[3111] = dict(short='a memorial bench', aliases='bench memorial', long='A memorial bench carved with a regiment\'s name stands here.')
O[3112] = dict(short='the Key of the Wall', aliases='key wall city', long='A heavy iron key, the Key of the Wall, lies here.')
O[3113] = dict(short='a memorial fountain', aliases='fountain memorial water', long='A small memorial fountain trickles here.')
O[3117] = dict(short='the last elm', aliases='tree elm last', long='The last elm tree of the lower ward stands here, hung with widows\' ribbons.')

# ====================================================================== new mobs
NEW = [
    dict(vnum=3011, zone=30, id='sentry', aliases='sentry wall', short='a wall sentry', role='standard', level=14,
         long='A wall sentry stands here, watching the west.', flags='bm', align=600,
         desc='A soldier on wall duty, wrapped in a grey cloak, a horn at his belt to sound if anything comes out of the march.'),
    dict(vnum=3012, zone=30, id='xbow', aliases='crossbowman bowman soldier', short='a crossbowman', role='standard', level=16,
         long='A crossbowman stands at the gate, his weapon loaded.', flags='bm', align=600,
         desc='A grim soldier with a heavy crossbow and a quiver of bolts tipped with blessed iron.'),
    dict(vnum=3013, zone=30, id='wounded', aliases='soldier wounded', short='a wounded soldier', role='harmless', level=4,
         long='A wounded soldier lies on a pallet, bandaged and pale.', flags='b', align=500,
         desc='A young soldier carried back from the march with a wound that will not close. The edges of it are grey.'),
    dict(vnum=3014, zone=30, id='lastbreath', aliases='priest last breath', short='a priest of the last breath', role='standard', level=22,
         long='A priest of the last breath kneels by the altar, waiting for the dead.', flags='b', align=1000,
         desc='One of the priests who watch over the altar where the fallen return. She has seen thousands of soldiers wake on the cold stone, and she greets every one of them the same way: you are home, you are alive, you are needed.', sex=2),
    dict(vnum=3015, zone=30, id='recruiter', aliases='sergeant recruiting recruiter', short='a recruiting sergeant', role='standard', level=18,
         long='A recruiting sergeant sits at a table, taking down names.', flags='b', align=500,
         desc='A big, cheerful sergeant with a ledger and a missing hand. He signs up anyone who can hold a spear and sends them east to the Recruit Yards to learn how.'),
    dict(vnum=3016, zone=30, id='widow', aliases='widow mourner woman', short='a war widow', role='harmless', level=2,
         long='A war widow stands by the memorial post in silence.', flags='b', align=800,
         desc='A woman in black who comes here every day to touch a name on the post.', sex=2),
    dict(vnum=3017, zone=30, id='messenger', aliases='messenger runner', short='a fort messenger', role='standard', level=8,
         long='A fort messenger hurries past with a dispatch case.', flags='', align=400,
         desc='A quick, thin youth carrying orders between the gates and headquarters.'),
    dict(vnum=3018, zone=30, id='stranger', aliases='stranger hollow eyed', short='a hollow-eyed stranger', role='standard', level=10,
         long='A hollow-eyed stranger stands in the shadows, his skin faintly grey.', flags='bl', align=-500,
         desc='He came in with the refugees, and something came in with him. His eyes are pale, his skin is grey at the fingertips, and he hums a tune that has no end. The first sign of the West, inside the walls.'),
    dict(vnum=3107, zone=31, id='drillmaster', aliases='drillmaster drill master', short='the drillmaster', role='standard', level=20,
         long='The drillmaster stands here with a cane under his arm.', flags='bm', align=600,
         desc='The garrison drillmaster, who has turned farm boys into soldiers for twenty years. He lost his own boys in the Fens.'),
    dict(vnum=3108, zone=31, id='burner', aliases='burner corpse', short='a corpse-burner', role='standard', level=12,
         long='A corpse-burner tends the pyre, his face wrapped in wet cloth.', flags='b', align=300,
         desc='A soot-black man who burns the dead of the west before they can be buried, because buried, they get up.'),
    dict(vnum=3109, zone=31, id='mourner', aliases='mourner', short='a mourner', role='harmless', level=2,
         long='A mourner sits by a coffin, praying.', flags='b', align=800,
         desc='Someone keeping the last watch over a body with a nail through its coffin lid.'),
    dict(vnum=3110, zone=31, id='restless', aliases='dead restless corpse', short='a restless dead', role='standard', level=12,
         long='A dead soldier claws its way out of an open grave.', flags='f', align=-800, attack='claw',
         desc='A soldier who died in the west and was buried without burning. The West is not finished with him.'),
]

RETHEME = {
    'zones': {30: 'The Fort of Midgaard', 31: 'The Lower Ward of Midgaard'},
    'rooms': R, 'mobs': M, 'objs': O,
    'new_mobs': NEW,
    'resets': {
        30: ['M 0 3011 3 3042', 'E 1 3022 100 16', 'M 0 3011 3 3043', 'E 1 3022 100 16', 'M 0 3011 3 3047', 'E 1 3022 100 16',
             'M 0 3012 2 3040', 'E 1 3021 100 16', 'M 0 3012 2 3040', 'E 1 3021 100 16',
             'M 0 3013 3 3001', 'M 0 3013 3 3001', 'M 0 3013 3 3001',
             'M 0 3014 1 3054',
             'M 0 3015 1 3061',
             'M 0 3016 1 3025',
             'M 0 3017 2 3014', 'M 0 3017 2 3041',
             'M 0 3018 2 3026', 'M 0 3018 2 3045'],
        31: ['M 0 3107 1 3110', 'E 1 3022 100 16',
             'M 0 3108 1 3152',
             'M 0 3109 1 3155',
             'M 0 3110 2 3153', 'M 0 3110 2 3153'],
    },
}
