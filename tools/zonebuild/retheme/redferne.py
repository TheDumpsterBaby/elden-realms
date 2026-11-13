"""Redferne's Residence (zone 79) re-themed.

Redferne was a paladin-captain of the wall at Midgaard for thirty years.  Too
old and too broken to march now, he lives in a tall house built on top of an
old bastion tower in the Lower Ward.  The only way up is the iron ladder and
its hand-chain from the Road Crossing (3120), as Midgaard's spec already says.
The stock "cloud mansion of the god Naris" becomes that house on the tower:
smoke and fog of the ward instead of clouds.  His son died in the march; the
thing in his pen, caught on his last patrol, sometimes speaks in the son's
voice, and he cannot bring himself to kill it.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

R[7900] = dict(name="Outside Redferne's Residence", desc="""
    You stand on the flat stone top of an old bastion tower, high above the
    roofs of the Lower Ward.  A low parapet runs round the edge, and the fog
    and chimney smoke of the ward drift past below.  Before you to the north
    stands Redferne's house, grey and narrow and plain, with a great arched
    gate of iron.  The ladder and its chain go down over the parapet.""",
    extras={'parapet': 'A waist-high parapet of old stone, its merlons chipped by arrows from some siege long before the war.',
            'house': 'A tall, narrow house of grey stone with small deep windows, built where the tower\'s war-engines used to stand.'},
    exits={'n': 'An enormous arched iron gate leads into the house.',
           'd': 'The iron ladder and its heavy hand-chain drop away over the parapet toward the street.'})
R[7901] = dict(name='The Southern End Of The Hall', desc="""
    You stand in a long, dim hall.  The light seems to come from the walls
    themselves, a soft old warmth that the paladin's prayers put there long ago.
    A large portrait hangs here.  A wooden staircase climbs up into the house.
    East, a short passage ends at a tall oak door; west is a yellow-painted
    door.  The hall runs on north, and south is the great iron gate, the only
    way out.""",
    extras={'portrait': 'A young knight in silvered plate with a red rose on his shield: Redferne\'s son, Aldric, painted the spring he went west with the Second of the Wall. A black ribbon is tied across the frame.',
            'runes': 'Warding runes are chiselled into the oak door. Under them, in plain letters, is written: "Stay out, if you treasure your life."',
            'letters': 'They read: LIBRARY'},
    exits={'n': 'The hall continues north. More doorways open under the staircase that way.',
           'e': 'A tall oak door, tightly shut. Little runes are chiselled into the wood.',
           's': 'Not a door so much as a gate: huge, iron, and barred. A plaque on it reads: NO RETREAT.',
           'w': 'An ash-wood door painted a peculiar yellow. Small black letters are written on it.',
           'u': 'The staircase climbs up toward a bedroom at the top of the house.'})
R[7902] = dict(name="Redferne's Library", desc="""
    Books and scrolls fill every shelf of this room: drill manuals, campaign
    rolls, lives of the old captains, prayers.  A large globe stands in the
    dim north-west corner.  Two worn leather armchairs and a great oak desk
    fill the middle of the room, under a crystal chandelier.  A tall window is
    set in the west wall.  The yellow door is east.""",
    extras={'globe world map': 'A big painted globe of the realm. Midgaard is marked in red. Everything to the west of it has been painted over in grey, and pins with little black flags crowd the edge of the grey.',
            'midgaard town city': 'On the globe Midgaard sits at the edge of the grey. East of it a thin road runs out to a castle, and a river winds down through the city.',
            'chairs leather armchairs chair armchair': 'Two matching armchairs of cracked old leather. One is worn soft from use. The other has not been sat in for years.',
            'window glass': 'A tall window, reaching almost from floor to ceiling. If you look out, you might see over the roofs.',
            'out outside beyond': 'Through the window you see the roofs of the Lower Ward under their smoke, and beyond them the long grey line of the west wall, with the haze of the march behind it.',
            'river': 'On the globe a winding river runs out of a great lake in the east, through the middle of Midgaard, and on west into the grey.',
            'desk': 'An oak desk covered with letters to the families of the men who died under Redferne\'s command. He still writes one a week.'},
    exits={'e': 'An old ash-wood door, painted yellow.'})
R[7903] = dict(name='The Reliquary', desc="""
    A cold, dark room that faint light seeps into from nowhere.  Here Redferne
    keeps what he carried back from the west and would not let anyone else
    keep: a broken standard, a grey stone that hums, a pair of small shoes.
    There is no furniture at all.  The only way out is west, back through the
    low steel door of the safe.""",
    extras={'standard stone shoes': 'A torn regimental standard, a stone the size of a fist that hums faintly when you come near, and a child\'s shoes, very small, from a village that no longer exists.'},
    exits={'w': "You see only the back of the safe's steel door."})
R[7904] = dict(name='The Northern End Of The Hall', desc="""
    The northern end of the hall, beneath the wooden staircase, where the
    light is dimmer.  The kitchen lies north.  To the east is a huge metal door
    barred from this side, and a foul stench seeps under it.  To the west is a
    carved aspen-wood door.  The hall runs back south.""",
    exits={'e': 'A huge metal door, barred on this side. A foul stench seeps under it, and from behind it, very quietly, someone is saying "Father?"',
           's': 'The rest of the hall lies that way, and so does the way out.',
           'w': 'The door has SITTING ROOM carved on it. It is aspen wood, beautifully carved with stags and roses.'})
R[7905] = dict(name='The Sitting Room', desc="""
    A small, warm sitting room.  Its walls are hung with portraits of the old
    captains of the wall, stern men and women in plate, every one of them
    dead.  Pride of place goes to a portrait of a young knight in shining
    armour.  An old armchair stands by the wall.  The only exit is the
    aspen-wood door to the east.""",
    extras={'chair armchair': 'An old armchair with a big cushion, turned to face the young knight\'s portrait.',
            'portraits paintings captains knight': 'The captains of the wall, one for every generation. The young knight is Aldric, Redferne\'s son. Someone has hung his sword beneath the frame.'},
    exits={'e': 'A very heavy door, carved from a single trunk of aspen.'})
R[7906] = dict(name='The Kitchen', desc="""
    A plain soldier's kitchen with a scrubbed table and a cold hearth.  From
    behind the larder cupboard to the north comes the busy noise of rats
    feasting.  East is the heavy door of the cold-room, which the old
    household always called the fridge.  The hall lies south.""",
    exits={'n': 'The larder cupboard is dark inside, but the sounds of the rats are unmistakable.',
           'e': 'The cold-room door. Cold air breathes out around its edges.',
           's': 'The northern end of the hall.'})
R[7907] = dict(name='The Larder', desc="""
    Sacks and shelves of food: hard bread, salt meat, march rations stocked as
    if for a siege.  Huge rats have chewed into most of it, and scuttle about
    in the heaps.  The cupboard door is south.""")
R[7908] = dict(name='The Cold-Room', desc="""
    A small room kept cold with ice packed into the walls.  It is stocked with
    water barrels, small beer, and a cask of strong spirits that the old man
    no longer touches.  The door is west.""")
R[7909] = dict(name='On The Stairs', desc="""
    The wooden staircase climbs and climbs through the narrow house.  It seems
    to go on for ever in both directions.  Up is Redferne's bedroom; down
    leads to the southern end of the hall.""")
R[7910] = dict(name='The Treasure Room', desc="""
    A small, gloomy room.  A huge iron safe is cemented into the east wall,
    and its steel door is the way on east.  The way back is west, through the
    tall oak door.""",
    extras={'safe': 'A huge iron safe, set deep into the wall. The paladin-captain\'s pay of thirty years is in there, and other things.'},
    exits={'w': 'A tall oak door leads back to the hall.'})
R[7911] = dict(name="Redferne's Bedroom", desc="""
    A long, plain bedroom.  A fire crackles in the big fireplace in the east
    wall, and a wide old bed takes up half the room, built for a big man and
    his wife, though he has slept in it alone for years.  His armour stand
    stands empty beside it.  Stairs lead down to the hall, and a pair of doors
    opens south onto a balcony.""",
    extras={'fireplace fire': 'A big fire of good logs. The old man keeps it burning all night.',
            'bed': 'A wide bed with a soldier\'s grey blanket folded square on it.',
            'stand armour': 'An empty armour stand. He wears the armour.'},
    exits={'s': 'Through the doors, the balcony and the grey sky over the ward.'})
R[7912] = dict(name="Redferne's Balcony", desc="""
    A narrow balcony on the south face of the house, very high up.  The whole
    of Midgaard lies spread below: the Lower Ward, the temple, the river, and
    in the west the long grey wall with its fires.  Far below you is the yard
    on the tower top.  The doors to the bedroom are north.""",
    exits={'n': 'The plain bedroom of the old captain.',
           'd': 'A very long way down: the tower top, and the roofs and lanes of the Lower Ward far beneath it.'})
R[7913] = dict(name='The Monster Pen', desc="""
    A cage of iron bars and stone, built for something big and very dangerous.
    The walls are gouged deep with claw marks and the straw is black with old
    blood.  The thing kept here was brought back from the march, alive.  The
    only way out is the metal door to the west.""",
    extras={'walls marks claw': 'Deep gouges in the stone. Among them, scratched small and careful, a single word: ALDRIC.'},
    exits={'w': 'The metal door of the pen, the only way out.'})
R[7914] = dict(name='On The Iron Ladder', desc="""
    You cling to the iron ladder bolted to the face of the old bastion tower,
    a heavy hand-chain running beside it.  Below you lies the Road Crossing of
    the Lower Ward, with its signpost and carts.  The only ways to go are up
    and down, unless you mean to let go.""",
    exits={'u': 'The ladder and chain climb up the tower face into the smoke.',
           'd': 'Below, the ladder is bolted to the street at the Road Crossing of the Lower Ward.'})
R[7915] = dict(name='Where The Wind Catches The Ladder', desc="""
    Here the tower sticks up above the roofs and the wind from the west hits it
    full on.  The ladder judders and the chain whips about.  The rungs below
    you have rusted loose and swing free.  There is no going down from here,
    only up.  Do not try to go down.""",
    exits={'u': 'The only way off this stretch is up.',
           'd': 'DOWN IS DEATH. The loose rungs below are swinging free in the wind, and the chain thrashes like a snake. There is nothing to hold.'})
R[7916] = dict(name='Halfway Up The Bastion', desc="""
    You are halfway up the old tower, the ladder cold and wet under your hands.
    One slip and you will fall.  The ladder goes on up.  Below you the loose
    stretch swings in the wind; you would not want to climb back down it.""",
    exits={'u': 'There is only one way from here, and that is up.',
           'd': 'The ladder below is swinging back and forth in the wind. Going down would be very risky.'})
R[7917] = dict(name='The Chain Down The Back Of The Tower', desc="""
    On this side of the tower, out of the wind, a second chain has been hung for
    the way down, with iron footholds hammered into the stone.  It is a long
    way, but it is safe.  Scratched into the stone beside one foothold is a
    message: "Go carefully. Come back if you are needed. R."  The chain goes on
    down toward the street.""",
    exits={'u': 'Above, the old footholds are rusted away to nothing.',
           'd': 'Down the safe side, toward the ladder above the street.'})
R[7918] = dict(name='Beneath The Parapet', desc="""
    The ladder ends just beneath the parapet of the tower top, and from here you
    can see over the whole ward: the smoke, the roofs, the temple, and in the
    west the wall.  Hand-holds lead up over the parapet.  A second chain runs
    down the sheltered side of the tower.""",
    exits={'u': 'Over the parapet lies the tower top, and Redferne\'s grey house beyond it.',
           'd': 'The sheltered chain goes down the back of the tower, into the smoke.'})
R[7920] = dict(name='The Fall', desc="""
    You fall.  The tower face rushes past, then the roofs, then the street of
    the Road Crossing comes up to meet you, and there is a short, ugly noise,
    and then nothing at all.""")

# ====================================================================== mobs
M[7900] = dict(aliases='redferne paladin knight captain grand', short='Redferne, the old paladin-captain',
               long='Redferne, the old paladin-captain of the wall, stands here in silvered armour.',
               desc='A huge old man in silvered plate with a red rose on his shield, white-haired and badly scarred, who held the wall at Midgaard for thirty years. He cannot march any more, but he keeps his armour on, and he still stands ready to help anyone who needs it.')
M[7901] = dict(aliases='rat large', short='the large rat', long='A large rat is here, gnawing through the stores.',
               desc='A rat two feet long with claws like fingers, come up from the cisterns of the Lower Ward. Its eyes are a little too pale.')
M[7902] = dict(aliases='cleaver thing creature', short='the Cleaver',
               long='The Cleaver crouches here, watching you hungrily.',
               desc='A huge spidery thing from the march, with four long arms that end in cleaver-like talons. Redferne caught it on his last patrol. Sometimes, at night, it speaks in his dead son\'s voice, and so he cannot bring himself to kill it.')

# ====================================================================== objs
O[7900] = dict(aliases='key steel', short='a large steel key', long='A large steel key has been left here.',
               extras={'steel key': 'A big key of solid steel, worn bright by an old man\'s thumb.'})
O[7901] = dict(aliases='key copper', short='a copper key', long='A copper key has been left on the floor.',
               extras={'copper key': 'A small copper key on a loop of red cord.'})
O[7902] = dict(aliases='key brass', short='a small brass key', long='A small brass key lies here.',
               extras={'key brass': 'A small, plain brass key with no marks of any kind.'})
O[7903] = dict(aliases='treasure coins pay', short="a captain's savings", long="A heap of a captain's saved pay is here.",
               extras={'treasure': 'Thirty years of a captain\'s pay, in coins of the fort. Less than you would expect. Most of it went to the widows.'})
O[7904] = dict(aliases='chest wooden', short='a wooden chest', long='A sturdy wooden chest stands in the corner.',
               extras={'chest wooden': 'A soldier\'s chest of short heavy planks, pegged together and fitted with a simple brass lock.'})
O[7905] = dict(aliases='chest iron', short='an iron chest', long='A heavy iron chest sits in one corner of the room.')
O[7906] = dict(aliases='dagger plain black', short='a plain black dagger', long='A long, plain black dagger rests here.')
O[7907] = dict(aliases='bracelet spiked', short='a large spiked bracelet', long='A large spiked bracelet has been left here.')
O[7908] = dict(aliases='waybread bread march', short='a cake of march bread', long='Some hard march bread has been put here.',
               extras={'waybread bread march': 'Hard, dense bread baked for the regiments, made to keep for a month in a pack. It is said one cake will carry a soldier through a day\'s march.'})
O[7909] = dict(aliases='ring gold goldring', short='a golden ring', long='A plain gold ring has been abandoned here.')
O[7910] = dict(aliases='sword bastard', short='a huge bastard sword', long='A huge bastard sword with a white hilt lies here.',
               extras={'bastard sword': 'A heavy hand-and-a-half sword with a hilt of white bone. It has been to the west and back many times.'})
O[7911] = dict(aliases='helmet large', short='a large helmet', long='A large iron helmet lies on the floor.',
               extras={'large helmet': 'Heavy protection for the head, dented from more than one blow.'})
O[7912] = dict(aliases='helmet chaos spiked western', short='a spiked western helm', long='A grim, spiked black helm lies on the floor.',
               extras={'chaos helmet': 'A black helm with a crest of iron spikes, taken off a champion of the west that Redferne killed. It still feels warm inside.'})
O[7913] = dict(aliases='sword two-handed', short='a two-handed sword', long='An enormous two-handed sword rests on the floor.',
               extras={'two-handed sword': 'A great blade with runes and a pattern like flames running along its edge.',
                       'runes': 'On the blade is written: "Burn bright, and they will see you coming."'})
O[7914] = dict(aliases='plate breast silvery silver', short='a silvered breast plate', long='A silvered breast plate lies on the floor.',
               extras={'plate breast silvery silver': 'A silvered breastplate with a large rose in relief: Redferne\'s own device. It is scored with many old cuts.'})
O[7915] = dict(aliases='plates leg silvery', short='some silvered leg plates', long='Some silvered leg plates lie on the floor.',
               extras={'leg plates silvery silver': 'Silvered leg plates marked with the outline of a rose.'})
O[7916] = dict(aliases='gloves silvery silver', short='a pair of silvered gloves', long='A pair of silvered mail gloves lies on the floor.',
               extras={'gloves silvery silver': 'Gloves of fine silvered mail, worn shiny at the grip.'})
O[7917] = dict(aliases='helmet silvery silver', short='a silvered helmet', long='A silvered helmet lies here.',
               extras={'helmet silvery silver': 'A silvered helmet with a white horsehair crest, gone yellow with age.'})
O[7918] = dict(aliases='shield rose', short='the shield of the rose', long='The shield of the rose rests on the floor.',
               extras={'shield rose': 'A dark red rose painted on a white field, chipped and repainted many times. There is an inscription.',
                       'inscription': 'The inscription reads:\n\nHold, and be held.'})
O[7919] = dict(aliases='boots heavy plated', short='a pair of heavy plated boots', long='A pair of heavy plated boots stands on the floor.',
               extras={'boots heavy plated': 'Heavy boots plated with silvered steel, made for standing a long time on a wall.'})
O[7920] = dict(aliases='plates arm silvery silver', short='some silvered arm plates', long='Some silvered arm plates lie on the floor.',
               extras={'plates arm silvery silver': 'Silvered arm plates marked with the outline of a rose.'})
O[7921] = dict(aliases='barrel water', short='a water barrel', long='A barrel of clean water stands here.')

RETHEME = {
    'zones': {79: "Redferne's Residence"},
    'rooms': R, 'mobs': M, 'objs': O,
}
