"""Old Thalos (zone 52) re-themed as the first city lost to the darkness.

Generations ago, before there was a wall at Midgaard, the darkness came out of
the west for the first time and Thalos fell to it in a single season.  The
survivors fled east and built New Thalos; the old city was left to the dead.
It is a haunted ruin now: the lamias nest in its houses, the ruin itself has
learned to lie (the mimics), a great Eye that came in with the darkness never
left the temple dome, and the stone wardens on the watchtowers are still
keeping watch for a city that is gone.  Exits, stats and resets unchanged.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

# ====================================================================== rooms
R[5200] = dict(name='The Grand Gate Of Thalos', desc="""
    You stand beneath the great arch of Thalos, the first city of the east and
    the first to fall.  Its two steel gates were forced inward long ago and have
    rusted where they hang, bent like paper.  The names of the founding houses
    are cut into the keystone, chipped almost smooth.  A cold wind blows past
    you into the dead city to the west; north, a track climbs back to the
    Supply Road.""",
    extras={'gates gate steel': 'The gates were not battered down. They were bent inward from the middle, as if something had leaned on them until they gave.',
            'keystone names arch': 'The names of the houses of Thalos run around the keystone. Somebody has scratched a small mark beside each one, the way the priests of Midgaard mark the rolls of the dead.'},
    exits={'w': 'Main Street runs west into the ruin, between houses with no roofs.',
           'n': 'North of the gate a rutted track climbs to the Supply Road.'})
R[5201] = dict(name='Main Street', desc="""
    The great street of Thalos runs west from the gate between the shells of
    tall houses.  Weeds grow in the cracks of its paving, and the wind has
    heaped grey dust in every doorway.  South stands a squat guard house, and
    north a dark alley slips between two fallen walls; the gate is back east.
    Somewhere deeper in the city something howls, and something else answers
    it.""",
    exits={'n': 'A narrow alley, black with shadow, runs north between fallen walls.',
           'e': 'The broken gate of the city stands to the east.',
           's': 'The guard house to the south still has its roof, though little else.',
           'w': 'Main Street runs on westward toward the domed temple.'})
R[5202] = dict(name='Main Street', desc="""
    Main Street widens here before the city hall, whose charred doorway gapes to
    the south.  To the north a house has been blown apart, its stones flung far
    across the road.  West the street gives onto the overgrown garden path that
    rings the temple, whose great dome still rises intact above the ruin.  The
    gate lies back to the east.""",
    extras={'dome temple': 'The dome of the temple of Thalos stands whole while everything around it lies broken. Nothing in the city looks less safe.'},
    exits={'n': 'Little remains to the north but a crater and scattered stone.',
           's': 'The scorched doorway of the city hall opens to the south.',
           'w': 'A withered garden path curves around the temple to the west.'})
R[5203] = dict(name='A Garden Path', desc="""
    You stand on the eastern arc of the garden path that rings the temple.
    Once these beds were the pride of Thalos; now the flowers are grey stalks and
    the trees are bare, and thorny vines climb the temple wall and catch at your
    ankles.  The path curves away north and south, the temple doors stand open to
    the west, and Main Street lies east.  A howl rises and breaks off.""",
    extras={'vines vine': 'The vines are grey and leafless, but they are still growing. They have pulled stones out of the temple wall.'},
    exits={'n': 'The garden path curves north around the temple.',
           's': 'The garden path curves south around the temple.',
           'e': 'Main Street leads back east toward the gate.',
           'w': 'The east doors of the temple stand open. Thin shafts of daylight fall inside.'})
R[5204] = dict(name='A Garden Path', desc="""
    The northern arc of the garden path.  A row of stone planters has been
    knocked over, and the soil that spilled from them is full of small bones.
    A side street leads away north into the poorer quarter, the path bends east
    and west around the temple, and the temple's north door stands open to the
    south.""",
    extras={'bones planters soil': 'Bird bones, lizard bones, and a few that are neither. Something eats here.'},
    exits={'n': 'A side street leads north into the common quarter.',
           'e': 'The garden path curves east around the temple.',
           's': 'The north door of the temple opens to the south.',
           'w': 'The garden path curves west around the temple.'})
R[5205] = dict(name='A Garden Path', desc="""
    The western arc of the garden path, where the vines are thickest.  A stone
    bench stands here, half swallowed by them, and someone has laid a ring of
    pale pebbles on its seat.  The path curves north and south, the temple's
    west door is to the east, and the old market place spreads out to the
    west.""",
    extras={'bench pebbles ring': 'The pebbles are arranged with care. Nobody living has come this way in years, but the ring is neat and free of dust.'},
    exits={'n': 'The garden path curves north around the temple.',
           'e': 'The west door of the temple stands open to the east.',
           's': 'The garden path curves south around the temple.',
           'w': 'The market place opens out to the west, full of overturned stalls.'})
R[5206] = dict(name='A Garden Path', desc="""
    The southern arc of the garden path.  A fallen statue of a woman lies face
    down across the way, its arms broken off at the elbow.  The temple's south
    door is to the north; the path curves east and west, and a side street runs
    south into what was once the quarter of guilds and counting-houses.""",
    extras={'statue woman': 'The statue lies face down. You could turn it over, if you had the strength and wished to see its face. Nobody in New Thalos would advise it.'},
    exits={'n': 'The south door of the temple stands open to the north.',
           'e': 'The garden path curves east around the temple.',
           's': 'A side street runs south toward the old business quarter.',
           'w': 'The garden path curves west around the temple.'})
R[5207] = dict(name='The Market Place', desc="""
    The great market of Thalos, where the whole east once came to trade.  Carts
    and baskets and stalls stand where their owners left them in the last days,
    some still holding goods gone to dust and rust.  A jeweller's table lies
    toppled to the north and a produce cart rots to the south.  The market runs
    on west, and the temple garden lies east.""",
    extras={'carts baskets stalls': 'Many of the stalls are still laid out, as if their keepers stepped away for a moment and meant to come back.'},
    exits={'n': 'A jeweller\'s table lies on its side to the north, its trinkets spilled across the stones.',
           'e': 'The garden path around the temple lies to the east.',
           's': 'A produce cart stands to the south under a cloud of flies.',
           'w': 'The market place continues west.'})
R[5208] = dict(name='The Market Place', desc="""
    The western end of the market square, where the dearer stalls stood.  Bolts
    of cloth have rotted on their poles and the awnings hang in strips.  A
    tapestry stall stands to the north, and to the south the reek of the meat
    stand hangs in the air.  The centre of the market lies back east.""",
    exits={'n': 'Heaps of tattered carpets and silks lie by a stall to the north.',
           'e': 'The centre of the market lies to the east.',
           's': 'The stench of the old meat stand comes from the south.'})
R[5209] = dict(name='A Side Street', desc="""
    A narrow street at the top of the common quarter, so choked with fallen
    stone that you must climb as much as walk.  Back alleys lead off east and
    west, and the street runs on south toward the temple.  The howling is
    louder here, and closer.""")
R[5210] = dict(name='A Side Street', desc="""
    The heart of the common quarter, where the poor of Thalos lived in houses
    of clay and fieldstone.  Most are heaps of rubble now.  To the east one house
    still stands with its door in its frame, and to the west a small clay
    dwelling sags on its beams.  The street runs north and south.""",
    exits={'e': 'A narrow doorway leads into a house that is somehow still standing.',
           'w': 'A small clay dwelling sits to the west, its roof fallen in.'})
R[5211] = dict(name='A Side Street', desc="""
    A side street leading north from the temple garden into the common
    quarter, lined with rubble that was once the homes of weavers and porters.
    East a tall house looms over everything near it; west a thatched stone
    cottage has folded in on itself.  The street runs north, and the garden path
    lies south.""",
    exits={'e': 'A tall dwelling stands to the east, leaning a little toward the street.',
           's': 'The garden path around the temple lies to the south.',
           'w': 'A small stone house with a fallen thatched roof sits to the west.'})
R[5212] = dict(name='A Side Street', desc="""
    The street runs south from the temple into the quarter of guilds and
    counting-houses.  These buildings were made of good dressed stone, and they
    fell all the same.  The wall of the city hall to the east has a great hole
    torn in it, and a smithy stands open to the west.  The garden path is north
    and the street continues south.""",
    exits={'n': 'The garden path around the temple lies to the north.',
           'e': 'A hole torn in the city hall wall leads east into its reception hall.',
           'w': 'Through the smithy door you can see anvils, tongs and a cold forge.'})
R[5213] = dict(name='A Side Street', desc="""
    Broken pillars line this stretch of street, the fronts of buildings that
    were grand once.  West stands the old guild house, darker than the ruins
    around it, and east the doorway of a tavern whose upper floor has fallen in.
    The street runs north and south.""",
    exits={'e': 'The doorway of a two-storey tavern opens to the east. There is sky where its roof should be.',
           'w': 'The guild house stands to the west. Its doorway is very dark.'})
R[5214] = dict(name='A Side Street', desc="""
    The street ends here at a crossing with a long back alley that runs east
    and west.  A heap of rubble to the east hides a shop doorway, if you look for
    it.  The street leads north again toward the centre of the dead city.""")
R[5215] = dict(name='Under A Ruined Watchtower', desc="""
    The south-west watchtower rises above you, a tall shaft of grey stone that
    was built to watch the western road.  Its base is scarred with old burns.
    A worn stair climbs up inside it.  An alley runs north behind the market and
    another leads east.""",
    extras={'burns scars stone': 'The stone is blackened in long streaks, as if fire had climbed the tower from the outside.'})
R[5216] = dict(name='A Back Alley', desc="""
    A filthy alley behind the market, where the butchers of Thalos threw what
    they could not sell.  The ground is soft and dark underfoot and the smell is
    very bad.  North is the back of the meat stand; south stands the watchtower.""",
    exits={'n': 'The back of the meat stand lies to the north.',
           's': 'The south-west watchtower stands a silent vigil to the south.'})
R[5217] = dict(name='The Meat Stand', desc="""
    A butcher's stall of hooks and racks.  Its meat should have rotted away
    generations ago, but there are fresh scraps on the hooks, and fresh blood
    in the gutter beneath them.  Something keeps a larder here.  The market is
    north, the produce cart east, and an alley runs off south.""",
    extras={'hooks racks scraps': 'The scraps on the hooks are fresh. Some of them are lizard. Some of them are not.'},
    exits={'n': 'The market place lies to the north.',
           'e': 'A cart of rotted fruit and vegetables stands to the east.'})
R[5218] = dict(name='A Back Alley', desc="""
    A narrow alley between blind walls.  Scratches run along both sides at
    shoulder height, as if something wide had squeezed through here many
    times.  The alley opens onto a side street to the east and reaches the
    south-west watchtower to the west.""",
    exits={'e': 'A side street crosses the end of the alley to the east.',
           'w': 'The south-west watchtower stands a silent vigil to the west.'})
R[5219] = dict(name='The Guild House', desc="""
    The guild house of Thalos, where its fighters and adventurers once
    mustered.  Tables and benches have been smashed to kindling and broken
    weapons lie everywhere, as if the last stand of the city was made in this
    room.  Draped along the back wall is a tattered black banner that does not
    belong to Thalos.  The only way out is east.""",
    extras={'banner black': 'The banner is black, and bears no device but a long grey stain shaped like a door left ajar. The old men of New Thalos say it was carried in by the things that took the city. Nobody has ever been willing to take it down.'},
    exits={'e': 'A side street runs past the guild house to the east.'})
R[5220] = dict(name='The Produce Stand', desc="""
    A great cart heaped with fruit and vegetables that turned to black mush
    long ago and have somehow never finished rotting.  Flies swarm over it in a
    droning cloud.  The market lies north and the meat stand west.""",
    exits={'n': 'The deserted market place lies to the north.',
           'w': 'A strong stench drifts from the meat stand to the west.'})
R[5221] = dict(name='The Smithy', desc="""
    The smithy of Thalos, its forge cold for generations.  The racks on the
    walls were stripped bare in the last days, when every blade in the city was
    carried to the gate, and only a few unfinished pieces remain.  Hammers still
    lie by the anvils where the smiths put them down.  The street is east.""",
    extras={'anvils hammers forge': 'The hammers lie neatly by the anvils. The smiths put them down and went to the gate, and did not come back for them.'},
    exits={'e': 'A side street runs past the smithy to the east.'})
R[5222] = dict(name='The Tapestry Stand', desc="""
    Rugs and tapestries lie heaped in great soft piles, torn and stained, and
    fine robes have been dragged off their poles into the heaps.  Looking longer,
    you see that the piles are hollowed in the middle and lined with hair.  They
    are nests.  The jewellery stand is east, the market south, and an alley
    leads north.""",
    extras={'piles nests rugs tapestries': 'Each heap has a hollow pressed into it, large enough for a body with four legs, and lined with long dark hair.'},
    exits={'e': 'A jewellery stand lies in ruin to the east.',
           's': 'The deserted market place lies to the south.'})
R[5223] = dict(name='A Back Alley', desc="""
    A narrow alley runs north from the tapestry stand toward the north-west
    watchtower.  A child's shoe lies in the middle of it, small and stiff, and
    nobody has moved it in a very long time.""",
    extras={'shoe': 'A small leather shoe, gone hard as wood. It points north, toward the tower, as if its owner had been running there.'},
    exits={'n': 'The north-west watchtower stands a silent vigil to the north.'})
R[5224] = dict(name='Under The Watchtower', desc="""
    You stand at the foot of the north-west watchtower.  Its door was barred
    from the inside once, and something tore the bar out of the wall.  A stair
    winds up inside.  Alleys lead away east and south.""",
    exits={'u': 'A narrow stair winds up into the north-west watchtower.'})
R[5225] = dict(name='The Jewellery Stand', desc="""
    A jeweller's table has been tipped over and its stock lies scattered in the
    dust: tarnished chains, cracked settings, beads gone dull.  The looters took
    nothing.  Nobody who fled Thalos stopped to carry jewels.  The market lies
    south and the tapestry stand west.""",
    extras={'chains settings beads trinkets': 'Cheap things and fine things lie together, all equally worthless now. A betrothal ring still has a name engraved inside it.'},
    exits={'s': 'The deserted market place lies to the south.',
           'w': 'A stand heaped with ruined rugs and cloth lies to the west.'})
R[5226] = dict(name='A Ruined Clay Dwelling', desc="""
    A plain one-room house of clay with a few broken chairs and a bed.  The
    fireplace is cold and full of ash so old it has set like stone.  Scratched
    into the hearthstone are tally marks, rows of them, counting days.  The
    street is east.""",
    extras={'marks tally hearthstone': 'Forty-one marks. Then nothing.'},
    exits={'e': 'The side street lies outside to the east.'})
R[5227] = dict(name='A Collapsed Stone Dwelling', desc="""
    This little stone house has fallen in upon itself.  A few rafters still
    stand with blackened thatch hanging from them, and the wind moves through
    the gaps with a sound like someone breathing.  The street is east.""",
    exits={'e': 'A small side street runs past the house to the east.'})
R[5228] = dict(name='A Back Alley', desc="""
    A crooked alley between the backs of houses.  Every doorway along it has
    been nailed shut from the outside, long ago.  The alley leads west to the
    north-west watchtower and east to a side street.""",
    extras={'doorways doors nails': 'The nails are driven in from the alley side. Whoever did it wanted to keep something in, not out.'})
R[5229] = dict(name='An Abandoned Shop', desc="""
    From the street this looks like nothing but a heap of rubble, but inside is
    a cramped shop that once sold arms, armour and travelling gear.  Its shelves
    are bare except for dust.  A small wooden sign still hangs by one nail and
    turns slowly in the draught.  The street is west.""",
    extras={'sign': 'The paint is almost gone, but you can read: "Blades, mail, rope and lamps. Bought and sold. No credit." Below it, in a different hand: "Gone to the gate."'},
    exits={'w': 'A small side street runs past the shop to the west.'})
R[5230] = dict(name='The Tavern Of The Sun', desc="""
    The Tavern of the Sun was the brightest house in Thalos.  Now its tables lie
    broken and its glasses crushed into the floor, and a little stage is buried
    under the beams.  Instruments lie in the wreckage beside the belongings of
    people who are not there.  The upper floor and roof have fallen in, and grey
    sky shows through the hole.  The street is west.""",
    extras={'stage instruments': 'The players left their instruments on the stage when the bells rang. The instruments are still there.'},
    exits={'w': 'A small side street runs past the tavern to the west.'})
R[5231] = dict(name='The South Wing Of The City Hall', desc="""
    A large chamber at the end of the hall, where the council of Thalos once
    received petitioners.  Its pillars have fallen and its treasures were
    carried off, but a few chairs survive, and a great curved desk.  A
    vine-hung archway to the east opens on a private courtyard.  The reception
    hall is north.""",
    extras={'chairs pillars': 'The chairs are arranged in a half circle, facing the desk, as though the council was still sitting when the end came.'},
    exits={'n': 'A long hallway leads back north to the reception hall.'})
R[5232] = dict(name='The City Hall', desc="""
    The reception hall of the city hall of Thalos.  Its walls are charred and
    scored with long gouges, and debris lies from wall to wall.  A great hole
    has been torn in the west wall, through which you can see the side street.
    Main Street lies north through the doorway, and a hallway runs south.""",
    extras={'gouges walls': 'Long parallel gouges run across the plaster, four at a time, as high as a man can reach.'},
    exits={'n': 'Main Street runs past the city hall to the north.',
           's': 'A hallway leads south to the south wing.'})
R[5233] = dict(name='The East Wing Of The City Hall', desc="""
    The office of the last Warden of Thalos, who gave the order to abandon the
    city and stayed behind.  Withered plants stand in their pots and the
    furniture is broken, but a tall glass cabinet stands intact against one
    wall.  A hallway leads west, and an ivy-covered archway south.""",
    extras={'cabinet glass': 'A tall cabinet of thick old glass with a small lock shaped like an ivory seal.'})
R[5234] = dict(name='The Private Gardens And Courtyard Of Thalos', desc="""
    The council's private garden was the loveliest place in the city.  Its
    trees have been smashed flat and its benches flung through the walls, but a
    great marble fountain still stands in the middle of it, cracked through and
    running red.  The stump of a watchtower rises above the wall.  An archway to
    the west leads back into the city hall.""",
    extras={'watchtower stump': 'The broken top of the north-east watchtower rises over the wall. Its ladder looks rotten even from here.'})
R[5235] = dict(name='A Small Guard House', desc="""
    The guard house of the city watch, a stout stone hut that still has its
    roof.  Its weapon racks are empty and its single cot is collapsed.  On the
    wall the watch kept a duty roster, and the last day on it was never
    finished.  Main Street is north.""",
    extras={'roster wall': 'A painted duty roster lists the watch by name. The last column is half filled in, and the brush stroke trails off down the wall.'},
    exits={'n': 'Main Street runs by the guard house to the north.'})
R[5236] = dict(name='A Collapsed Home', desc="""
    Nothing of this house remains but scattered stones and a deep blast crater,
    glassy at the bottom.  Whoever lived here was important enough to be killed
    first.  A shrieking howl carries across the rubble.  Main Street lies south.""",
    extras={'crater': 'The bottom of the crater has run like glass. Nothing natural burns that hot.'},
    exits={'s': 'Main Street runs past the ruined house to the south.'})
R[5237] = dict(name='A Tall Dwelling', desc="""
    The tallest building left in Thalos, once an inn of some kind.  Its back
    wall has been knocked out, opening onto a shack to the east through a
    second broken wall, with boulders and craters between.  An old wooden stair
    climbs to a creaking upper floor that sags visibly.  The street is west.""",
    extras={'stair stairs floor': 'The stair is old and the floor above it bows downward in the middle. Something heavy walks up there, or used to.'},
    exits={'w': 'A small side street winds past the dwelling to the west.',
           'u': 'The stair and the whole upper floor look badly rotted. You would be wise to stay off them.'})
R[5238] = dict(name='A Small Shack', desc="""
    A cramped shack that must once have been the city's apothecary.  Shelves
    and workbenches lie broken, and vials and pouches have spilled their
    powders across the floor in faded colours.  Its front door is blocked solid
    with rubble, so the only way out is back west through the broken wall.""",
    extras={'vials pouches powders shelves': 'Most of the vials are smashed or empty. The labels that remain are in the old script of Thalos, which few in New Thalos can still read.'})
R[5239] = dict(name='A Back Alley', desc="""
    A narrow alley running north from Main Street toward the north-east
    watchtower.  The walls lean together overhead, and it is darker here than
    the sky allows.  A great chorus of howls goes up somewhere ahead and stops all
    at once.""",
    exits={'s': 'Main Street runs past the mouth of the alley to the south.'})
R[5240] = dict(name='A Back Alley', desc="""
    The alley narrows between two windowless walls.  Dark hair is caught on the
    rough stone on either side, and the dust is full of prints that are not
    feet and not hooves.  It leads north to the watchtower and south toward
    Main Street.""",
    extras={'hair prints': 'Long dark hair, like a woman\'s, caught at shoulder height. The prints beneath it have four legs.'},
    exits={'n': 'The north-east watchtower stands a silent vigil to the north.'})
R[5241] = dict(name='Under A Watchtower', desc="""
    You stand beneath the north-east watchtower, the tallest of the four.  Its
    stair is gone and only a rickety ladder leads up into it.  Alleys run south
    and west.  From somewhere close comes the sound of many voices, hungry and
    almost human, whispering to one another.""",
    exits={'u': 'Wind howls high above in the tower. The ladder looks weak, and old.'})
R[5242] = dict(name='A Bath House', desc="""
    The public bath house of Thalos, built over a hot spring.  Steaming water
    still wells up through a hole in the floor and fills the old pool, and the
    air is thick and warm and smells of rot.  Something pale turns slowly in the
    water.  The west wall has collapsed into the house next door, and an alley
    lies north.""",
    extras={'water pool body': 'A body floats in the pool, turning slowly in the current from the spring. The heat has taken its skin away. It has been floating here far longer than any body should last.'},
    exits={'w': 'The wall has collapsed onto the adjoining house, opening a way west.'})
R[5243] = dict(name='A Back Alley', desc="""
    A narrow alley, damp and warm, where steam rolls out of the bath house to
    the south and beads on the walls.  The alley leads west to a side street and
    east to the north-east watchtower.""",
    exits={'e': 'The north-east watchtower stands a silent vigil to the east.',
           'w': 'A side street runs by the end of the alley to the west.'})
R[5244] = dict(name='An Upright House', desc="""
    Almost the only house in Thalos still standing whole.  The table is laid
    for four, the chairs pushed back, the windows unbroken.  Only the east wall
    is gone, smashed through into the bath house, and steam drifts in through
    the hole.  The street door is west.""",
    extras={'table chairs': 'Four places are laid. The bowls are full of dust. The chairs were pushed back in a hurry.'},
    exits={'e': 'Steam pours through a great hole in the east wall from the bath house beyond.',
           'w': 'A small side street runs past the house to the west.'})
R[5245] = dict(name='On The Second Floor', desc="""
    The moment you step onto this floor you know it was a mistake.  The rotten
    boards give way all at once and you plunge through, down onto the jagged
    timbers below.  The last thing you hear is the city howling.""")
R[5246] = dict(name='The North-West Watchtower', desc="""
    You stand atop the north-west watchtower.  From here the whole dead city
    lies spread below you, and beyond it the road runs west toward the far
    mountains, the way the darkness came the first time.  The stone warden of
    this tower still faces west.  A stair leads back down.""",
    extras={'mountains west road': 'The western road runs straight toward the mountains. The wardens of Thalos watched it for a hundred years, and saw it coming, and it made no difference.'},
    exits={'d': 'The ruined city lies below.'})
R[5247] = dict(name='The South-West Watchtower', desc="""
    You stand atop the south-west watchtower.  The western mountains are a grey
    line on the horizon, and to the south the desert stretches away under a
    white sky.  The parapet is scored with deep claw marks.  A stair leads back
    down into the city.""",
    extras={'parapet marks claw': 'Something climbed the outside of this tower to reach the top. The claw marks go all the way down.'},
    exits={'d': 'The ruined city lies below.'})
R[5248] = dict(name='The North-East Watchtower', desc="""
    You stand atop the north-east watchtower, the highest point in Thalos.  The
    desert sand runs to the horizon and the wind never stops.  The ladder you
    came up looks far worse from above: several rungs are cracked through and
    the uprights are soft with rot.""",
    extras={'ladder rungs': 'Climbing back down that ladder would be a gamble. It is a very long way to the street.'},
    exits={'d': 'The city lies below... far, far below.'})
R[5249] = dict(name='Under A Watchtower', desc="""
    As you start down the ladder, the rotten rungs snap one after another and
    you fall, a long way, onto the stones of the street below.  Thalos takes
    one more.""")
R[5250] = dict(name='The Temple Of Thalos', desc="""
    You stand beneath the great dome of the temple of Thalos, once the holiest
    place in the east.  Long benches lie toppled and the altar has been defiled.
    Stone has fallen from the roof, and thin shafts of daylight cut down through
    the dust.  Old books lie open on the floor.  Four archways lead out to the
    garden path: north, east, south and west.  Under the dome, something
    watches.""",
    extras={'books book': 'The books are prayer rolls of Thalos, written in the old script. Every page has been torn through the middle, very carefully, one at a time.',
            'altar': 'The altar has been split in two and something has been written across both halves in a dark stain. The letters are not any you know, and they are hard to look at.'},
    exits={'n': 'The north archway opens onto the garden path and the common quarter beyond.',
           'e': 'The east archway opens onto the garden path and Main Street.',
           's': 'The south archway opens onto the garden path and the old guild quarter.',
           'w': 'The west archway opens onto the garden path and the market place.'})

# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d

M[5200] = mob('the Eye in the Dome', 'beholder eye dome', 'A vast floating eye turns slowly beneath the dome to fix its gaze on you.',
              'A great round body that is mostly eye, crowned with writhing stalks that each end in a smaller one. It came into Thalos with the darkness generations ago and never left; the people of New Thalos still name it in their prayers, as a thing to be spared from.')
M[5201] = mob('the lamia', 'lamia beast', 'A lamia stands here with her head tilted, waiting for her next meal.',
              'The upper body of a woman and the lower body of a great four-legged beast. Her face is painted as for a festival of Thalos that has not been held in generations, and she murmurs to herself in its old tongue as she looks you over.')
M[5202] = mob('the mimic', 'mimic chest', 'A strong chest lies in one corner of the room.',
              'A wooden chest bound with iron straps and fastened with a heavy padlock. The wood is warm to the touch, and very faintly it rises and falls.')
M[5203] = mob('the mimic', 'mimic boulder skeleton skeletons', 'Two skeletons lie crushed under a large boulder.',
              'A great boulder of a stone found nowhere near Thalos, and two clean skeletons pinned beneath it. There is not a scrap of cloth on the bones. The boulder has been licked clean too.')
M[5204] = mob('the mimic', 'mimic floor', 'The stone floor of this house has been ripped apart.',
              'The flagstones are heaved up in a ragged ring, as if something had burst out from beneath them. Or as if something were waiting, open-mouthed, for you to step in.')
M[5205] = mob('the mimic', 'mimic pottery shards', 'Some broken shards of pottery lie strewn about the floor.',
              'Shards of a great painted jar from before the fall. If you look long enough, the pieces seem to have shifted a little since you came in.')
M[5206] = mob('the mimic', 'mimic planks wooden', 'A few wooden planks lie stacked on a low shelf.',
              'A neat stack of planks, free of dust in a room thick with it. In a city where nothing has been tidied for generations, that ought to worry you.')
M[5207] = mob('the horned lizard', 'lizard horned', 'A small horned lizard flicks his tongue and slithers away.',
              'A little grey desert lizard, one of the few living things in Thalos that nothing else seems to bother. It eats the flies off the produce cart.')
M[5208] = mob('the stone warden', 'golem stone warden', 'A stone warden stands at the parapet, faithfully keeping watch to the west.',
              'A giant of carved stone, set on the towers by the mages of Thalos to guard the western road. It did not stop the darkness, and nobody ever told it the city had fallen. It is still on watch.')
M[5209] = mob('the starving lamia', 'lamia beast starving', 'A starving lamia stands here, her ribs showing, waiting for her next meal.',
              'A lamia gone thin and wild with hunger, her long hair matted and her festival paint cracked and flaking. She no longer bothers to speak, but her lips keep moving.')

# ====================================================================== objs
O[5200] = dict(short='a ringmail vest of the Thalos watch', aliases='vest ringmail watch', long='A ringmail vest of the old city watch lies heaped on the floor.')
O[5201] = dict(short='an old iron helm', aliases='helm iron old', long='An old iron helm of the Thalos council guard has been left on the ground.')
O[5202] = dict(short='a pair of old iron gauntlets', aliases='gauntlets iron old', long='A pair of old iron gauntlets rests heavily on the ground.')
O[5203] = dict(short='a pair of old iron sleeves', aliases='sleeves iron old', long='A set of old iron sleeves lies on the ground.')
O[5204] = dict(short='a pair of old iron boots', aliases='boots iron old', long='A pair of old iron boots has been left here.')
O[5205] = dict(short='a set of old iron greaves', aliases='greaves iron old', long='A set of old iron greaves lies here, crusted with ancient dust.')
O[5206] = dict(short='an old iron girth', aliases='girth iron old belt', long='An old iron girth, the badge of the council guard, lies at your feet.')
O[5207] = dict(short='a battered iron breastplate', aliases='plate breast breastplate iron battered', long='A battered iron breastplate, holed through the middle, lies here.')
O[5208] = dict(short='a stone warden\'s iron shield', aliases='shield iron warden sturdy', long='A small but sturdy iron shield, worn smooth by a century of wind, has been left here.')
O[5210] = dict(short='a black potion', aliases='potion black', long='A stoppered jet-black potion from the old apothecary stands upright here.')
O[5211] = dict(short='an orange potion', aliases='potion orange', long='A small orange potion sealed with ancient wax lies here.')
O[5213] = dict(short='a green serpentine staff', aliases='staff serpentine green', long='A staff of green serpentine stone, carved with the old script of Thalos, has been left here.')
O[5214] = dict(short='a smooth quartz ball', aliases='ball quartz smooth', long='A smooth quartz ball lies here, glowing with a cold inner light.')
O[5215] = dict(short='a tattered scroll', aliases='scroll tattered', long='A tattered scroll in the old script of Thalos has been left here.')
O[5216] = dict(short='a bound scroll', aliases='scroll bound', long='A bound scroll from the council\'s desk lies at your feet.')
O[5217] = dict(short='a silver flute', aliases='flute silver', long='A silver flute from the Tavern of the Sun glimmers from beneath a rock.')
O[5218] = dict(short='a demon-faced talisman', aliases='talisman demon', long='A talisman carved with a snarling demon face glares up at you.',
               extras={'talisman demon': 'The face is not one carved in Thalos. It came in with the things that took the city, and it is heavier than it should be.'})
O[5219] = dict(short='a chunk of fresh meat', aliases='venison chunk meat fresh', long='A chunk of fresh meat from the lamias\' larder sits here.')
O[5220] = dict(short='a large cracked fountain', aliases='fountain blood cracked marble',
               extras={'fountain blood cracked marble': 'A great marble fountain, split through the middle. The water that wells up into its basin is dark red and warm, and it never stops.'})
O[5221] = dict(short='a two-handed sword', aliases='sword two-handed greatsword', long='A great two-handed sword of the Thalos wardens hangs on a hook in the wall.')
O[5222] = dict(short='a black silk robe', aliases='robe black silk', long='A black silk robe, the mourning dress of Thalos, lies heaped in one corner.')
O[5223] = dict(short='a dark green cloak', aliases='cloak green dark', long='A dark green cloak of the Thalos road-wardens has been dropped here.')
O[5224] = dict(short='an engraved ebony seal', aliases='seal ebony key', long='A small ebony seal, engraved with the arms of the council, lies here.')
O[5225] = dict(short='the council desk', aliases='desk curved council')
O[5226] = dict(short='an engraved ivory seal', aliases='seal ivory key', long='A small ivory seal, engraved with the Warden\'s mark, lies here.')
O[5227] = dict(short='the glass cabinet', aliases='cabinet glass')
O[5228] = dict(short='a half-rotted arm', aliases='arm rotted', long='A half-rotted arm floats lazily past your feet.')
O[5230] = dict(short='a pale blue stone', aliases='stone pale blue', long='A pale blue mosaic stone from the temple dome lies here.')
O[5231] = dict(short='a scarlet and blue stone', aliases='stone scarlet blue', long='A scarlet and blue stone, fallen from some old mosaic, lies here.')
O[5232] = dict(short='an incandescent blue stone', aliases='stone blue incandescent', long='A small incandescent blue stone glows in the dust.')
O[5233] = dict(short='a deep red stone', aliases='stone red deep', long='A deep red stone, like a drop of old blood, lies here.')
O[5234] = dict(short='a pink stone', aliases='stone pink', long='A tiny pink stone lies at your feet.')
O[5235] = dict(short='a pearly white stone', aliases='stone pearly white', long='A pearly white stone lies here, untouched by the dust around it.')
O[5236] = dict(short='a pale lavender stone', aliases='stone lavender pale', long='A pale lavender stone lies here, faintly cold.')
O[5237] = dict(short='a lavender and green stone', aliases='stone lavender green', long='A lavender and green stone rests on the ground.')
O[5238] = dict(short='a dusty rose stone', aliases='stone rose dusty', long='A dusty rose stone, the colour of old festival paint, lies here.')
O[5239] = dict(short='a dull grey stone', aliases='stone grey dull', long='You can barely make out a dull grey stone among the rubble.')
O[5240] = dict(short='a vibrant purple stone', aliases='stone purple vibrant', long='A vibrant purple stone glows sullenly among the ruins.')
O[5241] = dict(short='a pink and green stone', aliases='stone pink green', long='A bright pink and green stone has been left here.')
O[5242] = dict(short='a pale green stone', aliases='stone green pale', long='A pale green stone lies here collecting dust.')
O[5243] = dict(short='a clear stone', aliases='stone clear', long='A clear stone lies at your feet. Something seems to move inside it.')
O[5244] = dict(short='an iridescent stone', aliases='stone iridescent', long='A large iridescent stone from the heart of the temple dome lies here.')
O[5250] = dict(short='a mandolin', aliases='mandolin', long='A mandolin from the Tavern of the Sun lies against the wall, its strings slack.')
O[5251] = dict(short='a golden harp', aliases='harp golden', long='A battered golden harp lies tipped over among the broken tables.')

RETHEME = {
    'zones': {52: 'The Ruins of Old Thalos'},
    'rooms': R, 'mobs': M, 'objs': O,
}
