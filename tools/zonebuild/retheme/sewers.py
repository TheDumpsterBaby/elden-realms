"""The sewers under Midgaard (zones 70-73) re-themed as the fort's underbelly.

Four layers, each deeper and worse:
  70 The Cisterns        drains and cisterns of the fort, smugglers' road
  71 The Undercroft      the great ledge around the Abyss, the Grey Choir
  72 The Deep Drains     mind-eaters, wererats, and the West's own tunnel
  73 The Old Tunnels     caves older than the fort, and what nests in them
The first signs of the West seep in from below: grey water, the Grey Choir
hiding under the city, and a tunnel the West is digging toward the wall.
"""

R, M, O = {}, {}, {}


def fam(vnums, name, desc, **kw):
    for v in vnums:
        R[v] = dict(name=name, desc=desc, **kw)


# ====================================================================== 70 The Cisterns
R[7000] = dict(name='The Fissure Under The Ledge', desc="""
    A narrow crack in the bedrock beneath the cistern ledge.  Cold air breathes up
    out of it from somewhere far below, and it smells of wet stone and something
    sweeter, like old flowers.  A ledge lies above and darker water below.""")
fam((7001, 7005, 7006), 'The Silted Drain', """
    A brick drain choked with silt to the knees.  The fort's waste comes down here
    from the streets above, and the mud sucks at your boots with every step.  Rats
    have left trails along the upper curve of the walls.""")
R[7002] = dict(name='The Silted Junction', desc="""
    Two silted drains meet here under a grating that lets in a little grey light
    from Main Street.  You can hear carts rumbling overhead and the tramp of
    soldiers' feet.""")
R[7003] = dict(name='The Mudhole', desc="""
    The drain floor gives way to a sinkhole of black mud up to your thighs.  The
    mud is warm, and something below it has dug a passage downward.""")
R[7004] = dict(name='The Dark Pit', desc="""
    The drain ends at the lip of a dark pit.  Bats hang in clusters from the brick
    vault above it, and their droppings have made the floor slick.  An old rope
    ladder, half rotten, hangs down into the dark.""")
fam((7007, 7012), 'A Bend In The Silted Drain', """
    The drain bends sharply here, and the silt has piled up against the outer wall
    in a stinking bank.  Someone has scratched an arrow and the word HESK into the
    brickwork.""")
fam((7008, 7013), 'A Muddy Intersection', """
    Drains cross here in a low vaulted chamber.  The mud is churned by many feet,
    more than sewer-workers would make; this is a road, and it is used.""")
R[7009] = dict(name='The Great Junction', desc="""
    A wide brick chamber where five drains meet, built in the days when Midgaard
    was a city and not a fort.  The ceiling is high enough to stand, and soot from
    smugglers' torches blackens the vault.""")
R[7010] = dict(name='A Bend In The Drain', desc="""
    A cold draught blows around this bend from the deeper drains, carrying a
    faint sound like distant singing.""")
R[7011] = dict(name='The Silted Pipe', desc="""
    A wide clay pipe where three drains join.  Old bones are trodden into the silt,
    some of them human.""")
R[7014] = dict(name='The Silted Drain', desc="""
    A bend in the drain where the silt is crusted grey on the walls, as if the
    water that runs here carried ash.""")
R[7015] = dict(name='The Old Well', desc="""
    An ancient well-head stands here in a vaulted room, older than the drains
    around it.  The fort once drew its water from it.  Nobody drinks from it now:
    the water at the bottom has gone grey and still, and the rope has been cut.""")
fam((7016,), 'A Bend In The Drain', """
    An ordinary bend in an ordinary drain, except that the brick here is wet with a
    grey slime that glistens in your light.""")
fam((7017, 7018), 'A Drain Junction', """
    A junction of brick drains.  A smuggler's chalk mark on the wall points the way
    toward the river outfall.""")
R[7021] = dict(name='A Quiet Junction', desc="""
    A dry, quiet junction where the smugglers rest.  A ring of stones holds old
    ashes, and empty bottles are stacked neatly against the wall.""")
R[7022] = dict(name='The Odd Room With Smooth Walls', desc="""
    A small chamber whose walls are not brick but smooth grey stone, too smooth,
    as if something had melted them.  There is a click from the floor as you enter.
    This room was not built by the fort.""")
fam((7024, 7025, 7026, 7028), 'A Cistern Passage', """
    A brick passage along the side of one of the great cisterns, where the fort's
    rainwater was once stored.  The cistern beside you is dark and still, and its
    water has a faint grey sheen.""")
R[7029] = dict(name='The Triple Junction', desc="""
    Three cistern passages meet beneath a heavy grate.  The smell of the midden
    above drips down through it.""")
R[7030] = dict(name='The Junction Under The Dump', desc="""
    A filthy junction beneath the fort's midden.  Rubbish slides down from the
    drain above and piles up in a reeking heap, and the creatures of the sewer
    come here to feed.  A drain leads up to the dump.""")
R[7031] = dict(name='A Triple Junction', desc="""
    Drains meet under a low vault crusted with saltpetre.  Water drips steadily
    somewhere in the dark.""")
fam((7034, 7035), 'A Bend In The Cistern Pipe', """
    A big clay pipe turns here between two cisterns.  Your footsteps echo strangely,
    as though something else were walking a step behind you.""")
R[7036] = dict(name='The Pit', desc="""
    The pipe ends at a pit that drops away into the undercroft below.  Cold air
    rises from it, and with the air, very faintly, singing.""")
R[7037] = dict(name='The Round Room', desc="""
    A round chamber that begins to turn as you enter, grinding on some old
    mechanism; when it stops you can no longer tell which way you came in.
    Smugglers built it, or found it, to lose anyone who follows them.""")
R[7038] = dict(name='The Three Way Junction', desc="""
    A junction with a smugglers' lantern hung on a hook.  Someone has trimmed the
    wick recently.""")
R[7039] = dict(name="The Smugglers' Cache", desc="""
    A small dry storeroom lit by a single torch.  Crates stamped with the
    garrison's mark are stacked to the roof: food, oil and arrows stolen from the
    fort's stores and sold back to it at twice the price.""")
R[7041] = dict(name='The Shaft', desc="""
    A deep, square shaft drops into darkness here.  An iron ladder bolted to its
    side leads down toward the undercroft.""")
R[7043] = dict(name='The Cistern Entrance', desc="""
    A brick passage below a hatch from the thieves' secret yard.  This is the
    smugglers' front door to the drains, and the mud here is trodden flat.""")
R[7044] = dict(name='The Junction Going Three Ways', desc="""
    A passage of the drains where three ways meet.  A soldier's helmet lies in the
    mud, dented, with nobody in it.""")
R[7045] = dict(name="The Smugglers' Hall", desc="""
    A large chamber fitted out with stolen chairs and a long table, where the
    smugglers of the fort meet to divide their takings.  Maps of the drains are
    pinned to the walls, and some of the routes run out past the wall to the
    west.""")
R[7046] = dict(name="Hesk's Room", desc="""
    A room whose walls glitter with flakes of mica, where the smuggler captain
    keeps his bed and his strongbox.  A chart on the table shows the drains, the
    fort above, and a line in fresh ink running west under the wall.""")
R[7047] = dict(name='The Pool In The Cistern', desc="""
    You wade waist-deep in a cistern pool.  The water is so cold it burns, and
    things brush your legs.  A door is set in the wall to the east.""")
R[7048] = dict(name='A Dead End', desc="""
    The drain ends at a bricked-up arch beneath a grate that opens into the
    swordsmen's practice yard.  Fresh mortar seals a gap in the arch where
    somebody recently closed it, from this side.""")
R[7049] = dict(name='The Junction', desc="""
    A junction leading north, east and west.  From the dead end to the north
    comes the clash of drill in the swordsmen's yard far above.""")
R[7050] = dict(name='The Small Room', desc="""
    A small dry chamber off the drains.  An old chest sits in the corner, its lid
    pried open long ago.""")
fam((7051,), 'The Sewer Pipe', """
    A narrow, foul pipe.  The stink is enough to make your eyes stream.""")
R[7052] = dict(name='The Grand Sewer', desc="""
    The grand sewer of old Midgaard, a vaulted tunnel twenty feet high that once
    carried the waste of a hundred thousand people.  The fort is much smaller now,
    and the great channel runs half dry.""")
R[7053] = dict(name='The South End Of The Grand Sewer', desc="""
    You stand knee-deep where the grand sewer ends against a rusted grate.  A
    doorway leads west.""")
R[7055] = dict(name='The Edge Of The Water Sewer', desc="""
    Half the floor of this chamber is a channel of black water flowing south,
    toward the river and the wall.""")
R[7056] = dict(name='The Dark Hallway', desc="""
    A passage so dark that your light seems to shrink.  Footprints in the silt
    lead in, and none lead out.""")
fam((7057, 7058, 7059, 7060), 'The Dark Passageway', """
    A long dark passage.  You can see the floor where you step and nothing else.
    The darkness here feels thick, almost wet, and it presses against your light.""")
fam((7061, 7068), 'The Watery Sewer Bend', """
    Black water up to your chest, and a bend in the tunnel.  The current pulls
    gently, always west.""")
fam((7062, 7063, 7065, 7067), 'The Watery Sewer', """
    You wade through chest-deep black water in a flooded tunnel.  The water flows
    west, against the slope of the land, which is not possible, and it does.""")
fam((7064, 7066), 'The Watery Sewer Junction', """
    Two flooded tunnels meet.  Grey scum turns slowly on the surface of the
    water.""")
fam((7069, 7070), 'A Ledge By A Dark Pool', """
    A narrow ledge above a pool you cannot see the far side of.  The echo of
    dripping water goes on and on, and once, far out on the water, something
    surfaces and sinks again.""")

# ====================================================================== 71 The Undercroft
R[7100] = dict(name='The Edge Of The Water', desc="""
    The edge of an underground lake, lit dimly by your light.  The water is utterly
    still and stretches out beyond sight.  A crack leads up to the cisterns.""")
R[7101] = dict(name='Under The Mudhole', desc="""
    A small cave under the mudhole, its floor a slope of slumped black mud.  The
    mud is full of tracks: claws, and bare human feet.""")
R[7102] = dict(name='Under The Dark Pit', desc="""
    The bottom of the dark pit, ankle-deep in bat dung and bones.  A passage goes
    east, and a rough hole in the floor leads down into the old tunnels.""")
R[7103] = dict(name='A Muddy Bend In The Undercroft', desc="""
    A muddy bend in a tunnel dug, not built: the walls bear the marks of picks.""")
R[7104] = dict(name='A Junction In The Undercroft', desc="""
    Three dug tunnels meet.  Someone has hung a grey ribbon from a nail in the
    roof, and it stirs in a draught you cannot feel.""")
R[7105] = dict(name='Down The Old Well', desc="""
    You cling to the slimy sides of the old well, far below the cut rope.  Grey
    water waits below; above, a faint circle of light.""")
R[7106] = dict(name='The Northwestern Corner Of The Ledge', desc="""
    You stand at the corner of a ledge that runs around a vast shaft, the Abyss,
    which goes down further than any light can reach.  Steps cut into the rock
    lead down the wall of the shaft.""")
fam((7107, 7108, 7109, 7110), 'The Narrow Ledge', """
    A narrow ledge along the western wall of the Abyss, no wider than your boots.
    The drop beside you is endless, and from far down in it comes the sound of
    many voices singing the same note.""")
R[7111] = dict(name='The Southwestern Corner Of The Ledge', desc="""
    The ledge broadens at its south-western corner, where steps lead down the wall
    of the Abyss.  Grey candles have been set in niches in the rock and left
    burning.""")
R[7112] = dict(name='An Odd Intersection', desc="""
    An intersection of old pipes and newer tunnels.  Hymns have been scratched into
    the walls in a script that is almost letters.""")
R[7113] = dict(name='The Northern Ledge', desc="""
    The ledge runs east and west along the northern wall of the Abyss.  Below, very
    far down, there is a faint grey light.""")
fam((7114, 7190), 'Mid-Air', """
    You have stepped off the ledge into nothing.  For a long moment you hang above
    the Abyss, the grey light below you and the singing all around you.""")
R[7115] = dict(name='The Broad Ledge', desc="""
    A broad ledge on the southern side of the Abyss where the Grey Choir gathers.
    Grey ash has been scattered in circles on the stone, and in the middle of each
    circle is a single human tooth.""")
R[7116] = dict(name='The Northeastern Corner Of The Ledge', desc="""
    The north-eastern corner of the ledge.  A narrow way leads down from here,
    hidden behind a curtain of hanging roots.""")
fam((7117, 7118, 7119, 7120), 'The Narrow Eastern Ledge', """
    A narrow ledge along the eastern wall of the Abyss.  Grey-furred rats run past
    your feet along it, all of them heading the same way, down.""")
R[7121] = dict(name='The Southeastern Corner Of The Ledge', desc="""
    The ledge broadens at the south-eastern corner of the Abyss, where steps lead
    down.  A grey robe lies folded on the stone, as if its owner had gone down
    without it.""")
R[7122] = dict(name='Under The Pit', desc="""
    A completely dark cavern under the pit from the cisterns.  Grey candles burn in
    a ring here, and the Grey Choir holds its services where no soldier will ever
    come.""")
R[7123] = dict(name='Under The Shaft', desc="""
    The foot of the iron ladder from the cisterns.  A sapper's camp has been
    abandoned here: a bedroll, a pick, a lamp burned out.  On the wall someone has
    written, over and over: THEY ARE DIGGING BACK.""")
R[7129] = dict(name='The Sewer Line', desc="""
    A narrow drain cut through the rock below the ledge.  It slopes down toward the
    deep drains.""")

# ====================================================================== 72 The Deep Drains
R[7200] = dict(name='The Treasury', desc="""
    A small vault where the mind-eaters keep what their thralls bring them: coin,
    jewels, and the rings of soldiers who went down into the drains and never came
    up.""")
R[7201] = dict(name='The Inner Lair', desc="""
    An octagonal room with smooth purple walls that pulse faintly.  The air hums,
    and thoughts that are not yours slide across your mind like fingers.  The
    master of the lair dwells here.""")
fam((7202, 7203, 7204, 7205, 7206, 7207), 'The Lair Of The Mind-Eaters', """
    Human remains litter the floor, the skulls neatly opened.  The mind-eaters
    came up from the deep long ago, and since the West stirred they have been
    hungry, and bold.""")
R[7208] = dict(name='The Lair Entrance', desc="""
    A dry part of the drains before a heavy door.  The floor is swept clean, and the
    silence is total.""")
R[7209] = dict(name='The Crawlway', desc="""
    A narrow crawlway where you must go on hands and knees.  The walls are scored
    by the claws of the wererats.""")
R[7210] = dict(name='The Four-Way Junction', desc="""
    A junction of the deep drains, where the wererats have built a barricade of
    bones and rubbish.""")
R[7211] = dict(name='The Small Cave', desc="""
    A collapsed drain that is now a small cave, littered with gnawed bones and
    the light-sticks of dead soldiers.""")
fam((7212, 7213), 'The Deep Drain', """
    A dry drain, deep below the fort.  It bends, and bends again.""")
R[7214] = dict(name='The End Of The Drain', desc="""
    The drain ends at a wall of rubble.  The wererats sleep here in a heap of
    rags.""")
R[7215] = dict(name='The Half-Wet Drain', desc="""
    The floor of the drain is covered in a few inches of grey water.""")
R[7216] = dict(name='Under Water In The Drain', desc="""
    You are swimming in black water with your head scraping the roof of the drain.
    Something long and pale slides past you.""")
R[7217] = dict(name='The Half-Dry Drain', desc="""
    A half-dry drain where the wererats leave their kills to rot.""")
R[7218] = dict(name='The Very Small Room', desc="""
    A very small chamber, empty but for the stink of rat.""")
fam((7219, 7220, 7221, 7222, 7225), 'The Deep Drain', """
    A deep drain far below the fort, slimy with grey water.  The scrabbling of rats
    never quite stops.""")
R[7223] = dict(name='The Drain Bend', desc="""
    A bend in the deep drains, its walls clawed to the brick.""")
R[7224] = dict(name='The Drain Junction', desc="""
    Three deep drains meet.  A grey-furred rat the size of a dog watches you from
    the shadows, and does not run.""")
fam((7229, 7231), 'The Clawed Drain', """
    A drain whose walls are covered in scratches, thousands of them, as if
    something had been trying to dig its way out, or in.""")
R[7230] = dict(name='The Damp Drain', desc="""
    A drain filled with a damp, grey fungus that puffs spores when touched.""")
R[7232] = dict(name='The Clawed Drain', desc="""
    More scratches on the walls here, deeper, leading north.""")
R[7233] = dict(name='The Drain Before The Lair', desc="""
    A drain that opens into a cave to the east.  The stench of rat is so strong it
    is almost a taste.""")
R[7234] = dict(name="The Rat-Father's Lair", desc="""
    A cave heaped with bones and the rags of soldiers.  The Rat-Father, a rat the
    size of a pony with grey and hairless skin, rules the wererats from here.""")
R[7279] = dict(name='The Wall Of The Abyss', desc="""
    You cling to steps cut into the wall of the Abyss.  Below, the grey light is
    brighter, and the singing is louder.""")
R[7299] = dict(name='On The Walls Of The Abyss', desc="""
    You cling to the lowest steps on the wall of the Abyss.  Below you there is
    nothing but grey light, and you know with perfect certainty that if you let
    go you would fall into the West.""")
R[7280] = dict(name="The Sappers' Gate", desc="""
    A very dark room cut from the living rock, its walls marked with fresh pick
    scars.  This tunnel was not dug by the fort.  It comes from the west, under
    the march and under the wall, and it is still being dug.""")
R[7281] = dict(name='The Grey Gallery', desc="""
    A corridor glowing with a faint grey light that has no source.  Its walls are
    shored with timbers taken from the burned farms of the march.""")
R[7282] = dict(name='The Hall Of Lost Souls', desc="""
    A hall where the walls fall away and you seem to stand in nothing.  Around you
    drift the faces of the people the West has taken, whispering.  The tunnel goes
    on beyond them.""")
R[7283] = dict(name="The Sappers' Crossing", desc="""
    A crossing of tunnels with doors to east and west.  Picks and shovels are
    stacked here, and grey iron rails run along the floor for the spoil carts.""")
R[7284] = dict(name='The Burning Shaft', desc="""
    A shaft full of grey fire that burns without heat and consumes without smoke.
    Nothing that comes in here comes out.""")
R[7285] = dict(name='The Question Room', desc="""
    A square chamber with iron rings set in the walls, where the sappers take the
    soldiers they catch and ask them about the wall: where it is weak, how many
    hold it.  Nobody has answered yet.  Everybody has tried not to.""")
R[7286] = dict(name="The Sappers' Yard", desc="""
    A wide cavern ankle-deep in spoil and mud, where the tunnel's diggers live.
    Spoil carts stand in rows, and from beyond the far wall comes the steady sound
    of picks, closer every day.""")

# ====================================================================== 73 The Old Tunnels
R[7300] = dict(name='Cave Entrance', desc="""
    The mouth of a cave system older than the fort, below the deepest of its
    drains.  It is very cold.  A rough hole leads back up.""")
R[7301] = dict(name='Cave Tunnel', desc="""
    A tunnel of natural rock, worn smooth by water that stopped flowing long
    ago.""")
R[7302] = dict(name='Cave Room', desc="""
    A cool cave room.  Ancient paintings on the walls show men hunting, and above
    them, very faint, a grey shape watching from the west.""")
R[7303] = dict(name='The Cave T-Cross', desc="""
    A crossing of tunnels floored with a slick mud-like substance.""")
R[7304] = dict(name='The Cave Turning-Point', desc="""
    The mud grows deeper here.  A door has been set into the rock to the south.""")
R[7305] = dict(name='The Secret Room', desc="""
    A forgotten room thick with dust.  Nobody has been here since before
    Midgaard had a wall.""")
R[7306] = dict(name='The Mudhole', desc="""
    A pit of warm grey mud, bubbling slowly.  Pale shapes move in it.""")
R[7307] = dict(name='A Tunnel', desc="""
    A tunnel with mud to your knees.""")
R[7308] = dict(name='The Long Tunnel', desc="""
    A long, dry tunnel, its walls glittering with frost.""")
R[7309] = dict(name='The Hot Room', desc="""
    After the cold, this room is hot, and the rock is warm to the touch.  Something
    very large breathes somewhere nearby.""")
R[7310] = dict(name='The Small Room', desc="""
    A small room with a little statue of a kneeling figure carved from the rock,
    facing west.""")
R[7311] = dict(name='The Stalagmite Cave', desc="""
    A cave of stalagmites where water drips with a sound like slow footsteps.""")
R[7312] = dict(name='The Stalagmite Tunnel', desc="""
    A quiet tunnel between the stalagmites.""")
R[7313] = dict(name='The Spongy Room', desc="""
    The floor here is soft and gives underfoot, and it is warm.  You do not want to
    know what it is.""")
R[7314] = dict(name='The Stalagmite T-Cross', desc="""
    A crossing among the stalagmites.""")
R[7315] = dict(name='The Blind End Room', desc="""
    A dead-end chamber with a door in its north wall.""")
R[7316] = dict(name='The Treasure Room', desc="""
    A richly carved room from some kingdom that stood here before the fort, its
    walls set with mosaics of gold and lapis.""")
fam((7317, 7318, 7319), 'The Square Lair', """
    A square cave strewn with gnawed bones, the den of the ettins.  Two-headed
    giants have lived under Midgaard since before it had a name.""")
R[7320] = dict(name='The Lair End', desc="""
    The end of the ettins' lair.  A great stone table stands here, set with
    plates as big as shields.""")
R[7321] = dict(name='The East Tunnel', desc="""
    A dark tunnel with a door at its western end.""")
R[7322] = dict(name='The North Tunnel', desc="""
    A dark tunnel leading upward.""")
R[7323] = dict(name='The L-Shaped Room', desc="""
    A deeply dark room that turns a corner.""")
R[7324] = dict(name='The Circular Hall', desc="""
    A round hall with doors in every wall, most of them false.""")
R[7325] = dict(name='A Dusty Tunnel', desc="""
    A tunnel deep in dust, undisturbed for centuries.""")
R[7326] = dict(name='The Crossing', desc="""
    A crossing of carved hallways.  Smoke drifts from the south.""")
R[7327] = dict(name='The L-Shaped Room', desc="""
    An L-shaped room.  You can hear slow, enormous breathing to the east.""")
R[7328] = dict(name="The Wyrm's Lair", desc="""
    A vast burned cavern, its floor-stones fused to glass.  The old red wyrm has
    slept beneath Midgaard for a thousand years, and the West's tunnelling has
    woken it, and it is angry.""")
R[7329] = dict(name='The Burnt Room', desc="""
    A room scorched black, its contents long burned to ash.""")
R[7330] = dict(name='The Windy Tunnel', desc="""
    A tunnel where a hot wind blows from the wyrm's lair.""")
R[7331] = dict(name='The Glittering Room', desc="""
    A room whose walls glitter with crystals that catch your light and throw it
    back grey.""")
R[7332] = dict(name='The Secret Passageway', desc="""
    A tiny hidden passage.""")
R[7333] = dict(name='The End Of Long Tunnel', desc="""
    The end of a long tunnel, before a door in the west wall.""")
R[7334] = dict(name='The Stair-Room', desc="""
    A small room with drawings of serpents carved around its walls.""")
R[7335] = dict(name='A Dark Tunnel', desc="""
    A dark tunnel, guarded.  The nagas of the deep have watched this way since the
    old kingdom fell.""")
R[7336] = dict(name='The Entrance To The Lair', desc="""
    The stench of the basilisk's lair rolls out of the south.""")
fam((7337, 7338, 7339, 7340), "The Basilisk's Cave", """
    A smoky cave scattered with hay and the stone figures of the basilisk's
    victims: rats, a dog, a soldier with his sword half drawn.""")
R[7341] = dict(name='The Small Cave', desc="""
    A small cave sloping down to water.""")
R[7342] = dict(name='The Northern End Of The Pool', desc="""
    You stand ankle-deep at the edge of an underground pool.""")
fam((7343, 7345), 'The Pool', """
    You swim in black, freezing water in total darkness.  Something touches your
    foot.""")
R[7344] = dict(name='The South End Of The Pool', desc="""
    Water to your neck.  The cistern hag hunts in these waters.""")

# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc); d.update(kw); return d

M[7000] = mob('a sludge horror', 'horror sludge mudmonster monster', 'A sludge horror heaves itself up out of the mud.',
              'A mound of grey sludge with bones and buttons in it, all that is left of what it ate.')
M[7001] = mob('a cistern bat', 'bat cistern', 'A cistern bat flits about your head.',
              'A grey bat with a nasty bite.')
M[7002] = mob('a grey sewer rat', 'rat sewer grey', 'A grey sewer rat scurries along the wall.',
              'A big rat with grey fur and pale, intelligent eyes.')
M[7003] = mob('a drain spider', 'spider drain', 'A drain spider scuttles across its web.',
              'A hairy spider as big as your hand.')
M[7004] = mob('a giant tunnel beetle', 'beetle tunnel giant', 'A giant tunnel beetle clicks its mandibles.',
              'A beetle the size of a dog, armoured in black chitin.')
M[7005] = mob('a corpse maggot', 'maggot corpse', 'A corpse maggot, fat and white, writhes here.',
              'A maggot as long as your arm, swollen on the dead.')
M[7006] = mob('a cistern adder', 'adder snake cistern', 'A cistern adder slides through the water.',
              'A grey snake with a venomous bite.')
M[7007] = mob('a lost wanderer', 'wanderer lost', 'A lost wanderer stumbles through the dark, muttering.',
              'Someone who came down into the drains and could not find the way back up. Their mind did not come back either.')
M[7008] = mob('a homunculus', 'homunculus creature', 'A homunculus crouches here, watching with tiny eyes.',
              'A little man-shaped thing of grey flesh, left behind by a mage who came down here to experiment.')
M[7009] = mob('a shadow from below', 'shadow below morkoth', 'A shadow from below drifts over the dark water.',
              'A thing of darkness that rises from the deep pools. It hungers for warmth.')
M[7010] = mob("the chr-eff'n", "chr-eff'n chreffn", "The chr-eff'n lurks here.",
              'A twisted thing from the deep tunnels with too many joints.')
M[7040] = mob('the old red wyrm', 'wyrm red dragon old', 'The old red wyrm uncoils across its lair, smoke curling from its jaws.',
              'A great red dragon that has slept beneath Midgaard for a thousand years. The West\'s tunnelling woke it, and it blames everything that walks.')
M[7041] = mob('the cistern hag', 'hag cistern sea', 'The cistern hag rises dripping from the pool.',
              'A drowned crone with weed for hair, who drags swimmers under.', sex=2)
M[7042] = mob('a guardian naga', 'naga guardian', 'A guardian naga coils in the tunnel, watching.',
              'A great serpent with a woman\'s face, set to guard the old kingdom\'s halls long ago, and still guarding them.')
M[7043] = mob('the scaled basilisk', 'basilisk scaled', 'A scaled basilisk turns its terrible gaze on you.',
              'A heavy lizard whose eyes turn flesh to stone.')
M[7044] = mob('a lemure', 'lemure blob', 'A shapeless lemure oozes through the mud.',
              'A blob of pale flesh that was once something else.')
M[7045] = mob('Gorm the ettin', 'gorm ettin jones cruncher', 'Gorm the ettin argues with himself, both heads shouting.',
              'A two-headed giant, old and scarred. His heads have never agreed on anything except that intruders are food.')
M[7046] = mob('Brag the ettin', 'brag ettin herald', 'Brag the ettin gnaws on a rat.',
              'A young ettin, both heads hungry.')
M[7200] = mob('the master mind-eater', 'master mindeater mind eater mindflayer', 'The master mind-eater floats here, its face tentacles curling.',
              'A tall, robed thing with a squid\'s head and long fingers. It came up from the deep long ago. Since the West stirred, it hears a voice in the dark, and it has begun to answer.')
M[7201] = mob('a senior mind-eater', 'senior mindeater mind eater mindflayer', 'A senior mind-eater turns its tentacled face toward you.',
              'A mind-eater, hungry for thought.')
M[7202] = mob('a junior mind-eater', 'junior mindeater mind eater mindflayer', 'A junior mind-eater hisses at you.',
              'A young mind-eater, eager to feed.')
M[7203] = mob('a wererat', 'wererat rat', 'A wererat stands here, half man and half rat, holding a stolen blade.',
              'One of the rat-men of the deep drains. They were men once, deserters and smugglers who hid down here too long.')
M[7204] = mob('the Rat-Father', 'rat father ratfather gigantic', 'The Rat-Father heaves its bulk up from a nest of bones.',
              'A rat the size of a pony, grey and hairless, with a man\'s intelligence in its eyes. Every rat in the drains is its child.')

# ====================================================================== objs
O[7200] = dict(short='the hollow rod', aliases='rod hollow devil', long='A black rod that hums faintly lies here.')
O[7204] = dict(short='a pale blue draught', aliases='draught pale blue potion neon', long='A vial of pale blue liquid lies here.')
O[7206] = dict(short='an opened skull', aliases='skull opened white strange', long='An opened human skull lies here.')
O[7208] = dict(short="a soldier's light-stick", aliases='stick light soldier small', long="A soldier's light-stick lies here.")
O[7210] = dict(short='a heap of stolen coin', aliases='heap coin stolen treasure huge', long='A heap of stolen coin and soldiers\' rings lies here.')

# ====================================================================== new mobs (in 70.mob) and objects (in 72.obj)
NEW_MOBS = [
    dict(vnum=7011, zone=70, aliases='smuggler', short='a smuggler', role='standard', level=8,
         long='A smuggler with a sack over his shoulder eyes you warily.', flags='l', align=-200,
         desc='One of Hesk\'s crew, who move the fort\'s stolen stores through the drains and sell them back at the east gate.'),
    dict(vnum=7012, zone=70, aliases='hesk smuggler captain', short='Hesk the smuggler', role='elite', level=14,
         long='Hesk the smuggler captain lounges here, a cutlass across his knees.', flags='bl', align=-400,
         desc='A lean, scarred man who has run the drains for ten years. Lately he has been taking cargo west, under the wall, and he does not ask who pays him.'),
    dict(vnum=7013, zone=70, aliases='keeper cistern old', short='the cistern keeper', role='standard', level=6,
         long='An old cistern keeper sits by the well, staring into it.', flags='b', align=500,
         desc='The last of the men who kept the fort\'s water clean. He cut the well rope himself, the day the water turned grey. He says he heard it singing.'),
    dict(vnum=7014, zone=70, aliases='deserter hiding', short='a deserter in hiding', role='standard', level=7,
         long='A deserter in a filthy tabard cowers in the dark.', flags='', align=0,
         desc='A soldier who ran from the wall and hid down here. If the provost finds him, he hangs. He would rather fight you.'),
    dict(vnum=7015, zone=70, aliases='swarm rats grey', short='a grey rat swarm', role='standard', level=10,
         long='A swarm of grey-furred rats pours along the ledge toward you.', flags='f', align=-500, attack='bite',
         desc='Hundreds of grey rats moving as one, all with the same pale eyes.'),
    dict(vnum=7016, zone=70, aliases='sapper lost', short='a lost sapper', role='standard', level=12,
         long='A lost sapper sits by a dead lamp, listening to the walls.', flags='b', align=400,
         desc='A garrison sapper sent down to find the sound of digging. He found it. He has not slept since.'),
    dict(vnum=7017, zone=70, aliases='cultist grey choir', short='a cultist of the Grey Choir', role='standard', level=14,
         long='A cultist of the Grey Choir sways here in a grey robe, humming one long note.', flags='fl', align=-800,
         desc='One of the Grey Choir, the cult that came in with the refugees. They meet here in the dark under the fort and sing to the West, and the West, they say, sings back.'),
    dict(vnum=7018, zone=70, aliases='cantor grey choir', short='a cantor of the Grey Choir', role='elite', level=17,
         long='A cantor of the Grey Choir lifts her hands, and the singing in the Abyss rises with her.', flags='bfl', align=-900, sex=2,
         desc='A leader of the Grey Choir under the fort, her eyes gone entirely grey.'),
    dict(vnum=7019, zone=70, aliases='sapper hollow', short='a hollow sapper', role='standard', level=18,
         long='A hollow sapper turns from the rock face, pick in hand, grey eyes empty.', flags='f', align=-1000,
         desc='One of the West\'s diggers: a dead man in grey, digging toward the wall without rest.'),
    dict(vnum=7020, zone=70, aliases='tunnel mother', short='the Tunnel-Mother', role='champion', level=22,
         long='The Tunnel-Mother rises from the spoil, a bloated grey thing with a hundred digging arms.', flags='bfl', align=-1000, attack='claw', sex=2,
         desc='The West sent her to dig, and she births the hollow sappers in the mud of the yard. Kill her and the tunnel will stop, for a while.'),
    dict(vnum=7021, zone=70, aliases='horror tunnel born', short='a tunnel-born horror', role='elite', level=20,
         long='A pale, eyeless thing crawls out of the dark on too many legs.', flags='f', align=-1000, attack='bite',
         desc='Something that came up the West\'s tunnel ahead of the diggers.'),
]
NEW_OBJS = [
    dict(vnum=7212, zone=72, kind='treasure', level=8, aliases='bundle contraband', short='a bundle of contraband',
         long='A bundle of stolen garrison stores lies here.', cost=120),
    dict(vnum=7213, zone=72, kind='weapon', level=14, attack='slash', aliases='cutlass hesk', short="Hesk's cutlass",
         long='A well-kept cutlass lies here.', affects=[('hitroll', 1), ('damroll', 1)]),
    dict(vnum=7214, zone=72, kind='worn', slot='hold', level=14, aliases='hymnal grey', short='a grey hymnal',
         long='A book bound in grey cloth lies here, humming faintly.', affects=[('mana', 15), ('wis', -1)],
         extras={'hymnal': 'Every page is the same single note, written out over and over in a script that is almost letters.'}),
    dict(vnum=7215, zone=72, kind='weapon', level=18, attack='pierce', aliases='pick sapper', short="a sapper's pick",
         long="A sapper's pick of grey iron lies here.", affects=[('damroll', 2)]),
    dict(vnum=7216, zone=72, kind='light', level=12, hours=200, aliases='lantern sapper', short="a sapper's lantern",
         long="A sapper's shuttered lantern lies here."),
    dict(vnum=7217, zone=72, kind='worn', slot='neck', level=22, aliases='eye tunnel mother', short="the Tunnel-Mother's eye",
         long='A great grey eye, hard as stone, lies here.', affects=[('int', 1), ('hit', 15), ('save_spell', -1)]),
    dict(vnum=7218, zone=72, kind='armor', slot='about', level=14, aliases='coat smuggler oilskin', short="a smuggler's oilskin coat",
         long='An oilskin coat lies here in a puddle.', affects=[('dex', 1)]),
]

RETHEME = {
    'zones': {70: 'The Cisterns Under Midgaard', 71: 'The Undercroft', 72: 'The Deep Drains', 73: 'The Old Tunnels'},
    'rooms': R, 'mobs': M, 'objs': O,
    'new_mobs': NEW_MOBS, 'new_objs': NEW_OBJS,
    'resets': {
        70: ['M 0 7011 4 7039', 'G 1 7212 50', 'M 0 7011 4 7045', 'M 0 7011 4 7045', 'G 1 7212 50', 'M 0 7011 4 7009',
             'M 0 7012 1 7046', 'E 1 7213 100 16', 'E 1 7218 100 12',
             'M 0 7013 1 7015',
             'M 0 7014 2 7021', 'M 0 7014 2 7056',
             'M 0 7007 1 7057', 'M 0 7008 1 7022', 'M 0 7009 1 7069',
             'M 0 7002 6 7030', 'M 0 7000 4 7030'],
        71: ['M 0 7015 3 7108', 'M 0 7015 3 7118', 'M 0 7015 3 7113',
             'M 0 7016 1 7123', 'G 1 7216 100',
             'M 0 7017 5 7122', 'G 1 7214 25', 'M 0 7017 5 7122', 'M 0 7017 5 7115', 'G 1 7214 25', 'M 0 7017 5 7115', 'M 0 7017 5 7111',
             'M 0 7018 1 7115', 'G 1 7214 100'],
        72: ['M 0 7019 6 7283', 'E 1 7215 50 16', 'M 0 7019 6 7286', 'E 1 7215 50 16', 'M 0 7019 6 7286', 'E 1 7215 50 16',
             'M 0 7019 6 7285', 'M 0 7020 1 7286', 'G 1 7217 100',
             'M 0 7021 2 7282', 'M 0 7021 2 7281'],
    },
}
