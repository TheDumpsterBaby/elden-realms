"""Drow City (zone 51) re-themed as the city of the drow exiles.

Four drow houses, cast out of the deep cities long ago, built this small city
in a cavern under the Supply Road.  Hungry and hated, the Matron Mother of the
First House made a pact with Nu'Groth: the exiles became its eyes and knives in
the east.  They scry on the wall, read stolen dispatches, raid the supply
wagons for slaves, and send disguised agents into Midgaard and New Thalos.
Their old goddess, the Spider Queen, still has her temple, but a grey envoy of
the west now stands behind her altar, and the treasury is full of eastern coin.
Exits, flags, stats and resets unchanged.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

# ====================================================================== rooms
R[5100] = dict(name='The City Entrance', desc="""
    A rope ladder drops from a crack in the cavern roof, where a little grey
    daylight leaks down from the Supply Road above.  Below it the cave widens
    into a forecourt before a great gate of dark adamantite set into the rock to
    the west.  The ground is scuffed by many feet, and wagon wheels lie stacked
    against the wall, taken from the road.""",
    extras={'gate': 'A great gate of black adamantite, worked with spider emblems. Newer, cruder marks have been scratched over them: a grey shape like a door standing ajar.',
            'wheels wagon': 'Wagon wheels, axles and broken tailboards, some still painted with the mark of the Midgaard quartermaster. Wagons that never reached the wall.'},
    exits={'w': 'A huge adamantite gate opens to the west into the city.',
           'u': 'A rope ladder climbs to daylight and the Supply Road.'})
R[5101] = dict(name='A City Street', desc="""
    A street of smooth black stone, carved with endless spider webs, runs north
    and south just inside the city gate, which lies east.  Faint violet lamps
    burn in niches along the walls.  To the west a low building gives off a
    smell of straw and fear.""")
R[5102] = dict(name='A City Street', desc="""
    The street bends here, running north toward the gate and west into the
    city.  A drow sits at a little table in a niche, copying a letter by
    violet light; the broken seal beside it is a Midgaard seal.""",
    extras={'letter seal table': 'A dispatch from the Lord Commander to the castle of King Welmar, asking for more levies. The drow is copying it word for word before it goes back into the courier\'s bag.'})
R[5103] = dict(name='A City Street', desc="""
    An ornate street running east and west between carved housefronts.  To the
    south stands the house of the Third House, its doorway hung with spider
    silk.  Somewhere above, through the rock, you can hear the faint rumble of
    a wagon passing on the road.""")
R[5104] = dict(name='The 3rd House', desc="""
    The courtyard of the Third House, decorated well enough by drow standards
    with statues and murals.  The newest mural shows a column of drow walking
    east out of the dark toward a walled city, cloaked as human merchants.  The
    street lies north, and a door leads south.""",
    extras={'mural murals': 'Drow in the cloaks and hats of eastern merchants pass through a city gate. Behind them, painted very small, a grey shadow follows.'})
R[5105] = dict(name='The Throne Room', desc="""
    The throne room of the Third House, plain but for a blood-covered altar in
    the middle of the floor.  Around it lie the things the house has taken
    from the east: a cavalry pennant, a merchant's ledger, a child's doll.  The
    door is north.""",
    extras={'altar pennant ledger doll': 'Trophies. The pennant is from a Midgaard horse troop; the ledger belonged to a grain factor of New Thalos. The doll belonged to somebody.'})
R[5106] = dict(name='A City Street', desc="""
    An ornate street running east and west.  North stands a squat building that
    rings with the clash of practice blades.  Lamps of violet glass hang from
    chains overhead, and a drow patrol has marked each one with a tally of
    raids.""")
R[5107] = dict(name='A City Street', desc="""
    The street turns north toward the great gate of the First House and runs
    east back into the city.  South lies the very large house of the Second
    House, its doorposts carved as two rearing spiders.""")
R[5108] = dict(name='The 2nd House', desc="""
    The courtyard of the Second House, crowded with statues of spiders and
    hung with murals.  A long table is covered in maps of the eastern roads,
    with every wagon station and well marked in a neat drow hand.  The street
    is north, and a door leads west.""",
    extras={'maps table': 'Maps of the Supply Road and the roads around Midgaard, with the times of the wagon convoys written beside each station.'})
R[5109] = dict(name='The Throne Room', desc="""
    The throne room of the Second House, a little more richly done than its
    courtyard, with an altar in the middle of the room.  The altar is draped
    with a grey cloth that seems to drink the lamplight.  The door is east.""",
    extras={'altar cloth': 'Under the grey cloth the spider carving of the altar has been chiselled away.'})
R[5110] = dict(name='The Main Gate', desc="""
    You stand before the gate of the First House, almost as tall and fine as
    the city gate itself.  Two great spiders in adamantite rear above it, and
    between them hangs a new banner of plain grey.  The gate is to the west;
    the street runs north and south.""",
    extras={'banner grey spiders': 'The grey banner has no device at all. The drow salute it as they pass.'},
    exits={'w': 'A large gate of adamantite lies to the west.'})
R[5111] = dict(name='The 1st House', desc="""
    The great courtyard of the First House, the largest and finest in the city.
    Murals cover the walls, showing old battles in the deep places and the
    Spider Queen enthroned.  The last panel shows the Matron Mother kneeling
    before a door of grey light.  The gate is east, and the throne room
    west.""",
    extras={'mural murals paintings': 'The old murals are of drow wars under the earth, of exile and a long march upward. The newest panel, still bright, shows the Matron Mother on her knees before a grey door, and a voice coming out of it as a long line of silver words.'})
R[5112] = dict(name='The Throne Room', desc="""
    The throne room of the First House is, in one word, awful.  It is so
    horrifying that it is almost beautiful: webs of spun silver, thrones of
    bone, and a floor of polished black glass in which the room seems to go
    down forever.  A door leads north, and the courtyard is east.""")
R[5113] = dict(name='The Main Chamber', desc="""
    The council chamber of the Matron Mother herself.  A huge table stands in
    the middle, surrounded by high chairs.  Spread across it is a map of the
    west wall of Midgaard, stone by stone, with the guard changes marked in
    red.  This is where the pact is kept.  The door is south.""",
    extras={'map table': 'A map of the west wall of Midgaard, so exact that it must have been drawn by someone who walked along it. Every postern and drain is marked. In the margin, in a different and very old hand: "When I call."'})
R[5114] = dict(name='A City Street', desc="""
    A broad street of black stone running north and south, with a branch going
    east toward the temple.  A drow crier stands on a block reading out the
    names of eastern officers in a flat voice; the listeners take notes.  The
    First House lies south.""")
R[5115] = dict(name='A City Street', desc="""
    The street ends here against the cavern wall.  West stands the clerics'
    academy, its doors carved with spiders and something newer and greyer.  The
    street runs back south.""")
R[5116] = dict(name="The Clerics' Academy", desc="""
    The most lavish of the academies, for it trains the priestesses.  Silk
    hangings cover the walls, and the reading desks hold scrolls of prayer to
    the Spider Queen, and newer ones written in a script that hurts the eyes.
    The way out is east.""",
    extras={'scrolls desks script': 'The new scrolls are prayers, but not to the Spider Queen. The letters crawl when you look away from them.'})
R[5117] = dict(name='A City Street', desc="""
    The street runs east and west beneath the bulk of the temple, which fills
    the cavern to the north.  Its gates are tall, ornate and shut.  Pilgrims of
    the city leave offerings at their foot: small bones, and coins of eastern
    mint.""",
    extras={'offerings bones coins': 'Bird bones and silver crowns of Midgaard, laid out together in neat rows.'},
    exits={'n': 'Great ornamental gates bar the entrance to the temple of the Spider Queen.'})
R[5118] = dict(name="The Warriors' Academy", desc="""
    More a barracks than a school.  Practice dummies stand in rows, and each
    one wears a real Midgaard tabard, stitched where the blades went in.  The
    drow here learn to fight the way the wall fights.  The street is south.""",
    extras={'dummies tabards dummy': 'Grey tabards of the Midgaard garrison, taken from the dead. Every one is slashed in the same places.'})
R[5119] = dict(name='The Entrance To The Temple Of The Spider Queen', desc="""
    The temple is the largest building in the city, and even its doors are
    beyond belief.  Inside the entrance the walls are sheathed in gold and
    adamantite, and a wide stair goes down into the dark below.  The gates to
    the street are south.""")
R[5120] = dict(name="The Mages' Academy", desc="""
    The mages' academy is richly furnished; the drow prize magic far above
    strength.  In the middle of the room stands a basin of black water used for
    scrying, and the students take turns watching the west wall of Midgaard in
    it.  The street is south.""",
    extras={'basin water': 'In the still black water a stretch of wall appears, seen from above: sentries walking, a brazier, a gate. One of the sentries looks up, as if he felt it.'})
R[5121] = dict(name='A City Street', desc="""
    An ornate street running east and west.  North stands the mages' academy,
    where violet light flickers behind the windows.  A drow sits on a step here
    teaching a slave to speak like a Midgaard carter.""")
R[5122] = dict(name='The Slave Chamber', desc="""
    The room is in shambles.  Straw is strewn everywhere as bedding for the
    unhappy creatures the drow have taken: goblins mostly, and now and then a
    carter or a refugee taken off the Supply Road.  Names are scratched in the
    wall above the straw.  The street is east.""",
    extras={'names wall': 'Names in a dozen hands and two languages, some with a village after them. Ashford, Riversmeet, Thalos.'})
R[5123] = dict(name='A City Street', desc="""
    An ornate street leading west into the city and south toward the gate.  To
    the north is the small house of the Fourth House, its gate kept shut.
    Of all the houses it has the least, and its warriors go east most often.""")
R[5124] = dict(name='The 4th House', desc="""
    The courtyard of the Fourth House, small and dull by drow standards.  Its
    walls are bare, but piled in one corner are cloaks, hats and boots of
    eastern make, ready for the house's agents to put on.  The gate is south and
    the throne room east.""",
    extras={'cloaks hats boots corner': 'Merchants\' cloaks, carters\' hats, pilgrims\' boots. Disguises for the road east. Some are stained.'})
R[5125] = dict(name='The Throne Room', desc="""
    The throne room of the Fourth House is hardly grander than its courtyard.
    A small throne stands behind the altar, and that is all, save a stack of
    sealed letters waiting to go east.  The courtyard is west.""",
    extras={'letters stack': 'Letters sealed with plain grey wax, addressed to a chandler in New Thalos and a clerk in King Welmar\'s castle.'})
R[5126] = dict(name='The Entrance Hall', desc="""
    The stair from the temple doors comes down into this entrance hall, which
    opens north into a long hallway running east and west.  Small statues of
    spiders line the walls, each with its eyes picked out in grey stone.""")
R[5127] = dict(name='A Hallway', desc="""
    A long hallway lined with adamantite, carved with pictures of drow and
    spiders.  It runs east and west, and one or two figures can be seen moving
    away down it.  North an obsidian stairway climbs, and south lies the
    entrance hall.""")
R[5128] = dict(name='A Long Hallway', desc="""
    The hallway runs east and west.  The carvings here tell of the exile: drow
    driven upward out of the deep cities by their own kin, carrying their
    young.  A figure slips out of sight ahead of you.""")
R[5129] = dict(name='A Long Hallway', desc="""
    The hallway runs east and west past a door to the north, finer than the
    others, carved with crossed blades.  The sound of a blade cutting air comes
    from behind it, steady as breathing.""")
R[5130] = dict(name='A Long Hallway', desc="""
    The hallway turns here, running east and west.  The carvings show the
    exiles' hungry years on the surface, burned by the sun and hunted by
    everyone.  Somebody has scratched over the faces of the hunters.""")
R[5131] = dict(name='A Long Hallway', desc="""
    The hallway runs east and west.  The carvings here are newer and rougher:
    a grey door in the far west, and drow kneeling before it, and a road
    running east from their hands.""",
    extras={'carvings door': 'The grey door is carved very deep. The drow before it are offering their eyes.'})
R[5132] = dict(name='A Long Hallway', desc="""
    The hallway runs east and west, with a plain door to the south.  The
    adamantite on the walls is scratched at knee height, where the warriors
    lean their spears on the way to bed.""")
R[5133] = dict(name="The Warriors' Barracks", desc="""
    The room is a complete mess.  None of the cots are made, and clothes and
    gear lie all over the floor, among them a good deal of loot from the road:
    a cooking pot, a carter's whip, a bundle of letters.  A door leads north.""")
R[5134] = dict(name='A Long Hallway', desc="""
    The far end of the hallway loop, quiet and dim, running east and west.  A
    single lamp burns low, and the carvings beneath it show the Spider Queen
    weeping.""",
    extras={'carvings queen': 'The Spider Queen is carved turning away, her face in her hands. Nobody seems to have noticed what the carver meant.'})
R[5135] = dict(name='The Grand Stairway', desc="""
    You stand at the foot of a vast stairway of obsidian and adamantite, its
    edges trimmed with gold.  It climbs up into the higher temple.  The hallway
    lies south.""")
R[5136] = dict(name='The Grand Hallway', desc="""
    The middle of a grand hallway of the purest adamantite trimmed with gold.
    Mosaics of spiders and webs cover the walls.  A door leads east, the
    hallway continues north, and the stairway goes back down.""")
R[5137] = dict(name="The Mages' Barracks", desc="""
    The mages' quarters are clean but for a few used component jars.  Cots
    line the floor, and above each one is pinned a scrap of map: every mage
    has a stretch of the east to watch.  The only door is to the west.""",
    extras={'map maps scraps': 'Scraps of map, each a different stretch of road or wall: the Woodsman Inn, the Granary Fields, the Midgaard west gate.'})
R[5138] = dict(name='The Grand Hallway', desc="""
    The grand hallway ends here in adamantite and gold.  A door leads west, the
    hallway runs back south, and a stair goes down again into the heart of the
    temple, toward a cold draught and a smell of blood.""")
R[5139] = dict(name="The Clerics' Barracks", desc="""
    A bedchamber bright with spider statues and murals, its large beds soft
    with silk.  The priestesses sleep well.  On a stand by the door lie grey
    veils they have lately begun to wear.  The door is east.""",
    extras={'veils stand': 'Veils of fine grey gauze. They are cold to the touch, and through them the room looks further away.'})
R[5140] = dict(name='The Grand Stairway', desc="""
    You are on a stair of obsidian between walls of adamantite.  It climbs up
    toward the grand hallway, and at its foot to the north stand a pair of tall
    golden doors.""")
R[5141] = dict(name='The Main Chamber', desc="""
    The southern side of a great hall where the priestesses hold their rites.
    In its centre gapes a wide sacrificial pit, and beyond it rises the altar.
    The golden doors are south, and the hall opens east and west around the
    pit.""")
R[5142] = dict(name='The Eastern Side Of The Main Chamber', desc="""
    You are on the eastern side of the great hall, looking down into the pit.
    The rim is worn smooth by the feet of those who were pushed.  A door leads
    east, the altar stands to the north, and the hall runs south.""")
R[5143] = dict(name='The Sacrificial Pit', desc="""
    As you climb down into the pit, thousands of spiders pour over you and tear
    your body to shreds.  High above, the priestesses sing, and their hymn is
    for the Spider Queen and for the grey thing in the west together.""")
R[5144] = dict(name='The Western Side Of The Main Chamber', desc="""
    You are on the western side of the great hall, above the sacrificial pit.
    The rustling from below never stops.  The altar stands to the north, and the
    hall runs back south.""")
R[5145] = dict(name='The Altar', desc="""
    You stand before an altar, thickly and freshly stained with blood.  On its
    top is carved a great spider with a human head, and over the carving
    someone has set a slab of grey stone that is cold as winter.  Below the
    altar the sacrificial pit seethes with spiders.  A dais rises north, and the
    hall runs east and west.""",
    extras={'slab stone grey': 'A slab of grey stone that did not come from this cavern. It is so cold your breath frosts over it, and there is a faint sense of something listening on the other side.'},
    exits={'d': 'Thousands of spiders eye you with undisguised hunger.'})
R[5146] = dict(name='The Slave Cells', desc="""
    The guardroom of the cells where slaves are kept for the pit.  There are no
    guards; the drow do not think anyone would come for a slave.  A cell door is
    north, and a door leads west.""")
R[5147] = dict(name='The Slave Pen', desc="""
    Rotten meat and bread lie on the floor and shackles hang empty from the
    walls.  The room reeks of death.  Scratched on the wall at child height is a
    small picture of a house with a road running from it.  Whoever was kept
    here is gone.  The cell door is south.""")
R[5148] = dict(name='The Dias', desc="""
    You stand on a dais behind the altar.  Above you hangs a vast illusion of a
    drow woman turning into a giant spider and back again; but at each change,
    for a moment, she is neither, only a grey shape like an open door.  A
    heavy door leads west, and the altar lies south.""",
    extras={'illusion': 'Woman, spider, woman, spider... and for a heartbeat between them, nothing but a grey door, ajar. Each time, it stays a little longer.'})
R[5149] = dict(name='The Treasury', desc="""
    The temple treasury is nearly bare: what comes in goes out again quickly,
    as bribes for clerks and sentries in the east.  What remains is in eastern
    coin.  The heavy door is east.""")
R[5150] = dict(name="The Weaponsmaster's Chamber", desc="""
    An elegant bedchamber for one.  Its owner is held in high regard: the
    weaponsmaster who trains the city's knives before they go east.  A rack on
    the wall holds a row of plain human daggers, the kind that leave no drow
    mark.  The door is south.""",
    extras={'rack daggers': 'Plain iron daggers of eastern make. A knife from the Midgaard armoury leaves no question about who killed a sentry.'})

# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d

M[5100] = mob('the goblin slave', 'goblin slave', 'A goblin slave lies here asleep on the straw.',
              'A thin goblin taken in a raid on the Supply Road, with a drow brand on its shoulder. It begs for mercy the moment it sees you.')
M[5101] = mob('the drow commoner', 'drow commoner', 'A drow commoner walks here on guard duty, watching everything.',
              'A lean drow in a dark cloak, one of the exiles\' common folk. He is not the type to give directions, but he will remember your face and describe it later to someone who matters.')
M[5102] = mob('the drow warrior', 'drow warrior noble', 'A drow warrior stands here guarding his house.',
              'A noble warrior of one of the four houses, his mail blackened so it will not catch the light. He has been east many times, and every time came back with a trophy.')
M[5103] = mob('the drow mage', 'drow mage noble', 'A drow mage is here protecting his house.',
              'A drow mage with ink on his fingers and violet light in his eyes, who spends his nights watching the wall of Midgaard in a scrying basin. He prepares to cast a spell... at you.')
M[5104] = mob('the drow priestess', 'drow priestess', 'A drow priestess is here shouting orders.',
              'A priestess of the Spider Queen in a grey veil, who prays now to two masters and does not seem troubled by it. You would not want to get on her bad side.')
M[5105] = mob('the drow master', 'drow master spymaster', 'A drow master stares at you angrily.',
              'A master of the city\'s agents, who decides who goes east in disguise and who never comes back. He is always ready for a fight, and never fights fair.')
M[5106] = mob('the weaponsmaster', 'drow weaponsmaster master', 'A drow weaponsmaster is here, shadow boxing.',
              'The weaponsmaster of the city, who teaches the knives that go east how to kill a sentry without a sound. He clearly knows his way around a fight.')
M[5107] = mob('the Matron Mother', 'drow matron mother', 'The Matron Mother of the house is standing here.',
              'The ruler of one of the lesser houses, who signed the pact because the First House did, and who hopes to be repaid when the wall falls. She looks truly annoyed that you have found your way here.')
M[5108] = mob('the Matron Mother', 'drow matron mother first', 'The Matron Mother of the First House is waiting for you.',
              'The eldest of the exiles, who led her people up out of the deep places and then, starving and hated, knelt before the grey door in the west and made the pact. Her eyes have gone grey at the edges. She looks ready to rip your head off.')
M[5109] = mob('the drider', 'drider', 'The drider looks at you viciously while it draws its sword.',
              'Half drow and half spider, a punishment of the old faith for drow who failed it. Now the exiles use them as sentries and send them up at night to take wagons off the road.')
M[5110] = mob('the drider', 'drider gate', 'The drider looks at you viciously while it draws its sword.',
              'A huge drider set to guard the gate of the First House, its spider body scarred from the deep wars. It stands absolutely still until it moves.')
M[5111] = mob('the grey envoy', 'yochlol envoy grey', 'A grey envoy forms out of a swirling mist...',
              'A thing of grey mist and too many limbs, sent out of the west to seal the pact and stay behind to watch it kept. It has the shape of a handmaiden of the Spider Queen, worn like a borrowed coat. It is not in a good mood.')

# ====================================================================== objs
O[5100] = dict(short="a commoner's longsword", aliases='longsword sword commoner', long="A drow commoner's longsword of black adamantite has been left here.")
O[5101] = dict(short="a noble's longsword", aliases='longsword sword noble', long="A drow noble's longsword, made of adamantite, lies here.")
O[5102] = dict(short='a two-headed snake whip', aliases='whip snake twoheaded', long='A whip ending in two living snake heads lies here.')
O[5103] = dict(short='a three-headed snake whip', aliases='whip snake threeheaded', long='A whip ending in three living snake heads has been left here.')
O[5104] = dict(short='a four-headed snake whip', aliases='whip snake fourheaded', long='A whip ending in four living snake heads has been carelessly left here.')
O[5105] = dict(short='a black longsword', aliases='longsword sword black', long='A black longsword that drinks the light has been carelessly left here.')
O[5106] = dict(short='a five-headed snake whip', aliases='whip snake fiveheaded', long='A whip ending in five snake heads, their eyes gone grey, has been dropped here.')
O[5107] = dict(short='a six-headed snake whip', aliases='whip snake sixheaded', long='A whip ending in six grey-eyed snake heads has been dropped here very carelessly.')
O[5108] = dict(short='a pair of iron bracers', aliases='bracers iron', long='A pair of black iron bracers has been dropped here.')
O[5109] = dict(short='a pair of gauntlets', aliases='gauntlets', long='A pair of supple black gauntlets is lying on the ground.')
O[5110] = dict(short='a silvery blue wand', aliases='wand blue silver', long='A silvery blue wand has been dropped in the dirt.')
O[5111] = dict(short='a small helmet', aliases='helmet small', long='A small, close-fitting drow helmet lies against a rock.')
O[5112] = dict(short='a small ruby ring', aliases='ring ruby', long='A small ruby ring, the seal of the First House, lies in the dirt.')
O[5113] = dict(short='a spider-shaped dagger', aliases='dagger sacrificial spider', long='A dagger with blades shaped like spider legs lies on the ground.',
               extras={'dagger sacrificial spider': 'The sacrificial dagger of the temple. The legs of the spider are blades, and the body is a lump of cold grey stone.'})
O[5114] = dict(short='a small bright green hat', aliases='hat green', long="A small bright green merchant's hat lies in the dirt.",
               extras={'hat green': 'A merchant\'s hat of the kind worn on the Supply Road, with a Midgaard trade token pinned in the band. A drow agent wore it east, and the merchant it belonged to did not need it any more.'})
O[5115] = dict(short='an adamantite key', aliases='key adamantite', long='A key made of a strange black metal is lying here.')
O[5116] = dict(short='a pile of eastern coins', aliases='gold treasure coins pile', long='A large pile of gold and silver coins of eastern mint is lying here.')

RETHEME = {
    'zones': {51: 'The Drow City of the Exiles'},
    'rooms': R, 'mobs': M, 'objs': O,
}
