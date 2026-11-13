"""Miden'Nir (zone 35) re-themed: frontier forest and crossroads east of Midgaard.

Miden'Nir (goblin for 'Green Blood') is the wooded country on the roads east of
Midgaard.  Its northern edge is a crossroads: the Supply Road from Midgaard
(50) comes in at the shrine turning (3503); from the laneway (3502) the King's
Road runs east to King Welmar's castle (150) and a steep path drops to the
dwarves (65); from the moor (3500) tracks climb north to the hills over Moria
(40) and east to the Three of Swords (33).  South of the outer wall's gate
(3504, the gatehouse described in zone 50) lies the forest proper, the
Woodsman Inn, and the goblin bands that raid the wagons going to the wall.
The dark horsemen become deserters from the wall who ride with the goblins.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

# ====================================================================== crossroads
R[3500] = dict(name='The Moor Crossing', desc="""
    You stand on open moor, a wide, bare place where the wind howls with
    nothing to stop it.  Tracks cross the heather here.  One wanders north
    toward the hills, where few go now, for there are tales of things moving
    in the old dwarf-mines beneath them.  A narrow trail scars its way east up
    toward a stony hillside and the farms of the ridge.  A lane runs south
    between the trees.""")
R[3501] = dict(name='The Lane', desc="""
    A shady lane between tall trees.  Many of them have been felled, their
    stumps raw and white, and the trunks carted west to make stakes for the
    wall.  A crow watches you from one of the stumps.  The lane runs north to
    the moor and south to the laneway.""")
R[3502] = dict(name='The Laneway', desc="""
    The laneway, where the roads of the east meet.  East, the broad King's Road
    sets off straight as a spear toward King Welmar's castle; west, the lane
    runs on toward the shrine where the Supply Road turns for Midgaard.  A
    steep path drops away down to the northeast toward the dwarven village,
    and a lane goes north between the trees.  Wheel-ruts from the levy carts
    are cut deep into every road.""",
    extras={'ruts': 'Deep ruts from heavy carts, all of them heading west.'},
    exits={'e': "The King's Road runs east toward the pale towers of a castle in the distance.",
           'd': 'A well-trodden path leads steeply down to the northeast, toward the smoke of a dwarven village.'})
R[3503] = dict(name='The Shrine Turning', desc="""
    The lane meets the Supply Road here, at the western edge of Miden'Nir.  West
    you can see the lamp of the crossroads shrine, where the wagons for
    Midgaard turn onto the road to the fort.  Every carter who passes touches
    his hat toward it.  East the lane leads to the laneway and the roads of the
    east.""",
    exits={'w': 'West, the Supply Road and its shrine lamp, on the road back toward Midgaard.'})
R[3504] = dict(name='The South Gate', desc="""
    You are inside the squat stone gatehouse of Miden'Nir's south gate, a
    breach in the long wall of stone and timber that keeps the forest away
    from the Supply Road.  Bowmen watch from the slits overhead, and a list of
    wagons raided this month is nailed to the gate post.  West, a track runs
    down to the road; south, the gate opens on the forest.""",
    extras={'list post': 'A list of wagons lost this month: grain, arrows, salt, boots, all bound for the wall. Beside each: "goblins". Beside two: "goblins, and riders".',
            'slits bowmen': 'Narrow arrow slits. Behind them, tired faces watch the trees.'},
    exits={'s': 'South, through the gate, lies the forest of Miden\'Nir.'})

# ====================================================================== the forest
R[3505] = dict(name="The Trail To Miden'Nir", desc="""
    You are in light forest just south of the gate.  The trees here have been
    cut back from the path so that nothing can creep close to it, and the
    stumps are scarred with old arrowheads.  The path goes on south into
    darker woods, and the trees thin enough to pass east.  West, smoke rises
    above the treetops.  The gatehouse is north.""",
    exits={'n': 'To the north stands the gatehouse in the outer wall.',
           'e': 'More light forest.',
           's': "The path cuts into the darkness of Miden'Nir.",
           'w': 'A short way west, smoke rises from the chimney of the Woodsman Inn.'})
R[3506] = dict(name="The Miden'Nir", desc="""
    You are in a dark stretch of forest.  To the east the trees give out at the
    foot of the mountains.  The lighter woods lie west, and the forest runs
    on south.  A wagon wheel, splintered, lies half-hidden in the bracken.""",
    extras={'wheel wagon': 'A wagon wheel, smashed. Goblin arrows are still stuck in the spokes.'})
R[3507] = dict(name="The Miden'Nir", desc="""
    The forest is deep here, and the wind moves restlessly through the high
    branches.  North the woods grow lighter toward the gate.  South and west,
    paths lead deeper in.  Someone has hung a dead goblin from a branch as a
    warning; the crows have been at it.""",
    extras={'goblin branch': 'A small green body hung by the neck. It has not frightened anyone off.'})
R[3508] = dict(name='On A Small Path', desc="""
    A small path winds east and south through the dark woods.  To the west the
    mountains rise like a wall.  The path is marked with little cairns of
    stones, goblin-sign, telling their bands where the wagons pass.""",
    extras={'cairns cairn stones sign': 'Little piles of three stones, the top one marked with a smear of green. Goblin trail-sign.'})
R[3509] = dict(name="The Miden'Nir", desc="""
    The trees of Miden'Nir are lush and green here, and very quiet.  Too quiet:
    no birds at all.  The woods are too thick to pass west, but you can go
    north, south, or east toward the grey mountains.""")
R[3510] = dict(name='A Crossroads', desc="""
    Three worn foot-paths meet in a small clearing, going north, east and
    south.  The trees press close above, so that only scraps of sky show
    through the branches.  A broken crate lies in the clearing, stamped with
    the mark of the Midgaard quartermaster, empty.""",
    extras={'crate': 'A smashed supply crate with Midgaard\'s mark on it. Whatever was in it, the goblins have it now.'})
R[3511] = dict(name='The Trail', desc="""
    A north-south trail through the woods.  To the west, the mountains glare
    down, and thick undergrowth blocks any way in that direction.  Small,
    bare footprints cross the mud of the trail.""",
    extras={'footprints prints': 'Small, clawed, bare feet. Goblins, a band of a dozen at least.'})
R[3512] = dict(name="The Miden'Nir", desc="""
    The forest climbs toward the mountains here.  You can go north to the foot
    of the slopes, or west and south through the trees; the steep rock blocks
    the way east.  Something has stripped the bark off the trees here, high
    up, in long ragged strips.""",
    extras={'bark trees strips': 'Long tears in the bark, higher than a man could reach. Wyvern claws.'})
R[3513] = dict(name="The Miden'Nir", desc="""
    The forest is dim, and grows darker still to the west.  There is something
    bad hidden in these woods; you can smell it on the wind, faint and sweet.
    The trees thin to the north.""")
R[3514] = dict(name='The Deep Forest', desc="""
    It is dark here, and the forest closes round you, heavier and stiller with
    every step.  The trees are hung with grey moss.  It might be time to turn
    back toward somewhere safe.  Paths lead in all four directions.""")
R[3515] = dict(name='The Light Forest', desc="""
    The forest is light here, and the trail is easy to follow north and south.
    To the east the trees grow thick and dark.  The ground is strewn with grain
    from a split sack, already sprouting.""",
    extras={'grain sack': 'A split sack of Midgaard-bound grain. The goblins dropped it running.'})
R[3516] = dict(name='Some Muddy Ground', desc="""
    The ground here is a bog of mud and puddles, churned up by many small feet
    and the deep tracks of a wagon dragged off the road.  Your boots squelch at
    every step.  Paths lead north, east, south and west.""",
    extras={'tracks wagon': 'A wagon was hauled through here, its wheels sunk to the axles. Goblins pulled it, a great many of them.'})
R[3517] = dict(name='Near The Mountains', desc="""
    The mountains rise sheer to the east, grey and wet.  The rock blocks every
    way but north and west, where the ground slopes down into the trees.""")
R[3518] = dict(name='The Fading Trail', desc="""
    The trail all but vanishes here among the trunks.  North the forest is
    lighter and the trail clearer.  To the south a path goes on into darker
    woods.  East the trees stand trunk to trunk.""",
    exits={'e': 'The trees stand trunk to trunk that way.',
           's': 'Dark forest.'})
R[3519] = dict(name='The Dark Path', desc="""
    You are hemmed in by trees on both sides.  The path runs north and south,
    and east into the woods.  The trees are far too thick to go west.  A sweet,
    sickening stench drifts up from the south.""",
    exits={'s': 'A strong stench comes from this direction.',
           'w': 'The trees stand trunk to trunk that way.'})
R[3520] = dict(name='The Dark Forest', desc="""
    You push through the underbrush.  The forest is very thick here, the
    branches so dense overhead that no sunlight gets through.  It is too thick
    to go east or north, but the woods open a little to the south and west.""")
R[3521] = dict(name='The Carnage', desc="""
    A gruesome sight.  Blood is everywhere, on the trees and soaked into the
    ground, and a supply wagon lies on its side, its load torn open.  Two
    bodies lie in front of it, staring up.  The woods are impassable south,
    but you can go north, east or west.""",
    extras={'carcass body corpse carcasses bodies corpses': 'Two carters, pierced by something huge and jagged, like a spear. Their lips are pale blue: poison. The wyverns got them before the goblins could.',
            'wagon load': 'An overturned supply wagon bound for the wall. Arrows, salt, boots, scattered in the mud.'},
    exits={'n': 'Darkness.',
           'e': 'Your light does not reach that far.'})
R[3522] = dict(name="Deep In The Forest Of Miden'Nir", desc="""
    There is a sickening stench here of blood and rot.  North, through the
    branches, you catch glimpses of daylight and a trail.  East, you can see
    nothing at all.  The trees are close and stifling.""",
    exits={'e': 'The stench comes from this direction.'})
R[3523] = dict(name='The Dark Forest', desc="""
    The branches block out the sun, and the air is still and stale.  The forest
    runs on north, and east toward the mountains.  A stench comes from the
    west, and something about this place makes the hair rise on your neck.""",
    exits={'n': 'It seems to get much darker that way.',
           'e': 'The forest grows darker still toward the mountains.',
           'w': 'The trees thin a little that way, and the stench grows.'})
R[3550] = dict(name='At The Foot Of The Mountains', desc="""
    You are at the foot of the mountains, where it is too steep to climb north
    or east.  A goblin lookout post of piled stones stands on a ledge, empty
    for now.  The green forest of Miden'Nir spreads out south and west.""",
    extras={'post lookout ledge stones': 'A small hide of stacked stones. From it, a goblin could watch the whole road from the gate.'})
R[3551] = dict(name="Deep In The Forest Of Miden'Nir", desc="""
    The branches block out all sunlight, and the forest is very dark.  The
    woods go on west.  Mountains close off every other way but south, where a
    low tunnel has been dug into the mountainside.  The ground before it is
    trampled bare.""",
    exits={'w': 'The forest continues, and grows a little lighter.'})
R[3552] = dict(name='A Tunnel In The Mountains', desc="""
    A tunnel carved into the mountain by the goblins of Miden'Nir, long ago.
    The floor is worn smooth by small feet and by things dragged over it.  It
    runs south into the mountain and north out into the forest.""")
R[3553] = dict(name='A Tunnel In The Mountains', desc="""
    The tunnel is lighter to the north, toward the way out; south, the passage
    grows ever smaller.  A small alcove has been hacked into the east wall.
    Sacks marked with the Midgaard quartermaster's stamp are piled along the
    walls.""",
    extras={'sacks stamp': 'Stolen supply sacks: oats, salt, arrowheads. Enough to feed a company on the wall for a week.'})
R[3554] = dict(name='A Small Alcove', desc="""
    A small alcove hacked from the rock.  A pile of twigs, leaves and a stolen
    army blanket serves as a bed.  The main passage lies west.""",
    extras={'twigs leaves bead bed blanket': 'Twigs and leaves heaped into a bed for something small, with a grey wool blanket of the garrison on top.'})
R[3555] = dict(name='A Tunnel In The Mountains', desc="""
    Deeper in, the tunnel shrinks until you must hunch over to go on.  A low
    archway south opens into a larger chamber, and the tunnel runs back
    north.""")
R[3556] = dict(name='The Goblin HeadQuarters', desc="""
    The tunnel widens into a cavern that is large, for goblins: the den of the
    Miden'Nir bands.  Bones of animals and worse are strewn about from recent
    meals.  Loot from the supply wagons is heaped against the walls, and on a
    flat stone sits a little pile of fine silver coins, too fine for goblins
    to have earned.  The tunnel leads north.""",
    extras={'loot heap': 'Boots, arrows, salt, broken barrels, a carter\'s hat. All bound for the wall.',
            'coins silver stone': 'Good silver, new-minted, unmarked. Someone is paying the goblins to strike the wagons.',
            'bones': 'Deer and boar, mostly. Not all.'})

# ====================================================================== the inn
R[3570] = dict(name='The Front Of The Inn', desc="""
    A well-worn path opens into a clearing before an old wooden building with
    smoke pouring from its chimney.  Its windows are shuttered with planks and
    the porch is ringed with sharpened stakes.  A painted sign hangs on the
    porch to the west.  Paths lead north and south around the building, and
    east back into the forest.""",
    extras={'sign': 'The sign reads: The Woodsman. Someone has painted underneath: "Beds. Ale. Walls."',
            'stakes porch': 'Sharpened stakes, hammered in a ring around the porch. Some have dried green blood on them.'},
    exits={'e': "Back through the trees to the forest of Miden'Nir.",
           'w': 'The front door of the Inn, heavy and iron-studded.'})
R[3571] = dict(name='North Of The Inn', desc="""
    You stand on the north side of the Inn, where firewood is stacked high under
    the eaves.  The air smells of smoke and cooking.  The only way is back
    south to the front porch.""")
R[3572] = dict(name='South Of The Inn', desc="""
    The south side of the Inn.  You can go north to the front door or west
    round to the back.  A faint trail leads south into the trees, and from it
    comes a muffled sound of crying.""",
    exits={'s': 'The trail heads south, toward the crying.'})
R[3573] = dict(name='Behind The Inn', desc="""
    The back of the Inn, where the keeper throws his rubbish.  It does not smell
    good.  Piles of garbage lie to the west.  You can go back east round the
    side of the building.""")
R[3574] = dict(name='The Woodsman Inn', desc="""
    The common room of the Woodsman Inn, low-beamed and smoky.  It is mostly
    empty.  Since the goblins grew bold, few carters stop here, and those who do
    sleep with their boots on.  An axe hangs by the door within easy reach.  The
    bar is north, a quiet table south, and in a dark corner west sits a heavy
    drinker.  The door is east.""",
    extras={'axe': 'A woodsman\'s axe, well used and not for wood.'},
    exits={'n': 'The bar, manned by the Innkeeper.',
           'e': 'The door out to the clearing.',
           's': 'An empty table, a rare thing on a busier night.',
           'w': 'A table in a dark corner, occupied by a heavy drinker.'})
R[3575] = dict(name='The Ambush Point', desc="""
    An overgrown foot-trail south of the Inn, where a supply wagon was
    ambushed not long ago.  Bushes are trampled flat and branches are broken
    down; a smashed lantern and a carter's whip lie in the leaves.  Hoof-marks
    lead away west.  The Inn is north.""",
    extras={'lantern whip': 'A smashed carter\'s lantern and a whip. The rest of the wagon\'s crew is not here.'},
    exits={'w': 'A trail through the woods, cut by hoof-marks.'})
R[3576] = dict(name='The Bar', desc="""
    Folk once came here for the food and the welcome.  Now the Innkeeper serves
    only the few carters and fighters who make it through the forest, and keeps
    a loaded crossbow under the bar.  The common room is south.""",
    extras={'crossbow bar': 'A heavy crossbow, wound and loaded, under the bar.'})
R[3577] = dict(name="The Bard's Table", desc="""
    A dark corner of the Inn with a big round table and a few wooden chairs.
    There is a large sticky stain on the table where a drink was spilled and
    nobody wiped it up.  The common room is east.""")
R[3578] = dict(name='The Garbage Dump', desc="""
    You stand knee-deep in garbage: bones, peelings, broken pots, rags.  It
    smells terrible, and something is moving underneath it.  Cleaner ground
    lies east.""")
R[3579] = dict(name='A Quieter Section Of The Inn', desc="""
    A quiet end of the Woodsman, empty but for a bench and a table.  It is a
    safe enough place to rest and bind your wounds.  The common room is
    north.""")
R[3581] = dict(name='On The Trail Of The Horsemen', desc="""
    The path runs east and west.  Fresh hoof-prints in the soft ground show
    where the riders fled west, shod horses, army-shod, not goblin
    ponies.""",
    exits={'e': 'Back to the ambush point.'})
R[3582] = dict(name='On The Trail Of The Horsemen', desc="""
    The path turns here, east and south.  The hoof-prints swing south.  A torn
    strip of grey cloth hangs from a thorn: part of a garrison tabard.""",
    extras={'cloth tabard strip': 'Grey wool with a trim of the Midgaard garrison. One of the riders was a soldier of the wall, once.'})
R[3583] = dict(name='On The Trail Of The Horsemen', desc="""
    The trail of the horsemen runs north and west through the forest.  The
    tracks are very fresh.  They must be close.""",
    exits={'w': 'The tracks lead west.'})
R[3584] = dict(name='A Dead End Trail', desc="""
    The path ends abruptly where the trees close in.  Fresh tracks churn the
    ground and stop right here, by a ring of cold ashes and a heap of stolen
    sacks.  The riders' hiding place.  The only way back is east.""",
    extras={'ashes sacks': 'A cold campfire and supply sacks with the Midgaard stamp. Deserters\' loot.'},
    exits={'e': 'Back along the trail.'})

# ====================================================================== mobs
M[3500] = dict(aliases='wyvern', short='the wyvern', long='A monstrous wyvern circles low over your head.',
               desc='A huge winged beast down from the mountains, its barbed tail dripping with venom. It flaps and shrieks only feet above you. Since the goblins started leaving dead carters in the woods, the wyverns have grown fat.')
M[3501] = dict(aliases='goblin mountain raider', short='the goblin', long='A goblin raider creeps about, muttering to himself.',
               desc='A small, twisted creature with knotted muscles and green skin, wearing a stolen army boot on one foot. The bands raid the wagons bound for the wall.')
M[3502] = dict(aliases='goblin lieutenant', short='the goblin lieutenant', long='A goblin lieutenant stands here, trying to beat his band into order.',
               desc='A bigger, angrier goblin with a stolen sword and a garrison helmet stuffed with rags to fit. He is looking for someone to beat, and you will do.')
M[3503] = dict(aliases='goblin leader chief', short='the goblin leader', long='The goblin leader squats among his loot, surveying the den.',
               desc='The chief of the Miden\'Nir bands, scarred and cunning, with a purse of new silver at his belt that no goblin minted. He is not happy that you have found him. He grabs for his spear.')
M[3504] = dict(aliases='boy small carter', short='the small boy', long="A carter's boy sits here, nursing his wounds and crying.",
               desc='A boy of ten or so, covered in cuts and scratches. He rode on the supply wagon with his father. He is the only one who got away from the ambush.')
M[3505] = dict(aliases='innkeeper keeper woodsman', short='the Innkeeper', long='The Innkeeper stands here, cleaning cups and listening for the door.',
               desc='A big, tired woodsman who keeps the Woodsman Inn. By day he waits for customers who seldom come; by night he sits up with his crossbow, watching for goblins. It used to be a happy house.')
M[3506] = dict(aliases='bard balladeer drunk', short='the bard', long='A sullen bard is here, drinking away his troubles.',
               desc='A bard who used to sing in the halls of the east. He went west with a regiment to sing them into battle, and came back alone. He has been drinking ever since, and you can smell it across the room.')
M[3507] = dict(aliases='horseman dark deserter rider', short='the dark horseman', long='A dark horseman sits his black horse here, a deserter\'s scowl on his face.',
               desc='A deserter from the wall, his garrison tabard dyed black. He and his kind ride with the goblin bands and take the best of every wagon. He has no qualms about cutting you to pieces.')

# ====================================================================== objs
O[3500] = dict(aliases='sword small', short='a small sword', long='A small, notched sword lies here.')
O[3501] = dict(aliases='sword long fine', short='a fine long sword', long='A fine long sword has been left here.')
O[3502] = dict(aliases='club wooden', short='a wooden club', long='A crude wooden club, studded with nails, lies here.')
O[3503] = dict(aliases='jacket studded leather', short='a studded leather jacket', long='A studded leather jacket, dyed black, lies on the ground.')
O[3504] = dict(aliases='spear small', short='a small spear', long='A small goblin spear with a jagged head lies here.')
O[3505] = dict(aliases='corpse mutilated carter', short="a carter's mutilated corpse", long="A carter's mutilated corpse lies on the ground here.",
               extras={'corpse mutilated carter': 'A carter, torn open by something huge. His lips are blue.'})
O[3506] = dict(aliases='corpse mutilated officer', short="a mutilated officer's corpse", long="An officer's mutilated corpse lies on the ground here.",
               extras={'corpse mutilated officer': 'A young officer of the escort, in a torn grey tabard. He died with his hand on his belt, as if reaching for something.'})
O[3507] = dict(aliases='dagger ornate', short='an ornate dagger', long='A beautiful dagger is stuck in the ground.',
               extras={'dagger ornate': 'The hilt is two snakes twined together, with a small red ruby at the end. An officer\'s dagger, too fine for the escort of a supply wagon.'})
O[3508] = dict(aliases='top toy gyroscope spinning', short='a painted spinning top', long='A small painted top spins about on the ground here.',
               extras={'top toy gyroscope spinning': 'A child\'s spinning top, painted with red and green rings. As it spins round and round, it is hard to look away.'})

RETHEME = {
    'zones': {35: "Miden'Nir"},
    'rooms': R, 'mobs': M, 'objs': O,
}
