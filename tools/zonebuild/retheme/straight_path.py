"""The Straight Path (zone 15) re-themed as the penitents' pilgrim road.

A road of allegorical trials that climbs from the River of Lost Souls into the
mountain.  Penitents walk it to be weighed: deserters from the wall, those who
have done murder, those who want to be clean before they go west.  It is the
hardest ground in the east (levels 24-30).  All the stock real-world religious
figures and texts are replaced with invented ones:

  the Weigher             -- the judge at the end of the road (was Allah)
  the Watchers of the Road -- Vessamar of the Scales, Corrith the Herald,
                             Ildane the Shield, Morvaine of the Dark Gate
                             (were the four archangels)
  Sefhra the Unweighed   -- the fairest Watcher, who would not be weighed (Iblis)
  the Tempter             -- the voice that offers the crooked way (Iblis/devil)
  Oswen the First Pilgrim -- who first walked the road (the Prophet)
  the Four Stewards       -- Hadric, Talmor, Brannoc and Edrin, who kept the
                             road after Oswen (the Rashidun caliphs)
  the Pilgrim's Vow       -- the vow at the parting of the ways (Shahadah)
  Cassel the Betrayer     -- who sold Oswen for silver (Judas)
  Ozmandar the Drowned King, Prince Oduran the Ascetic, Marshal Grevaunt
                          -- examples of pride, hypocrisy and hate
                             (Pharaoh, al-Hakim, the old dictator)
  the mocking wisps       -- (the jinn);  the gate-child (the cherub)
The trial structure (light and dark halves, temptation, the fall, the last
day, repentance, the Final Facing, judgment) is kept.  Exits/stats unchanged.
"""

R = {}   # rooms
M = {}   # mobs
O = {}   # objs

# ====================================================================== rooms
R[1500] = dict(name='A Road Leading From The Bank', desc="""
    A small stony road leads up from the bank of the River of Lost Souls, whose
    dark water can be heard just to the south.  Sheer cliffs close in on either
    hand.  Penitents have tied scraps of cloth to the thorn bushes here, one for
    each sin they mean to lay down, and the bushes are heavy with them.  To the
    north a path runs straight as a drawn line into the mountain.""",
    extras={'cloth scraps bushes thorn': 'Hundreds of strips of cloth, faded to grey. Some carry names, some a single word: theft, cowardice, desertion, murder.'},
    exits={'n': 'A strange path leads north, perfectly straight, into the mountain.',
           's': 'The River of Lost Souls flows just to the south.'})
R[1501] = dict(name='A Long Road', desc="""
    You stand at the start of a long road in a great hollow silence.  Your
    first step has been taken freely, which is all the road asks at the start;
    the truth of your heart is not yet told.  A small white child stands
    guard here.  If you are not ready, turn back south and do not come again
    until you are.  The road runs north.""")
R[1502] = dict(name='A Long Road', desc="""
    You stop, and find you are shouting in frustration.  Of everything you
    regret, surely that one sin could have been avoided.  The blows and the
    hurt you gave flash before your eyes, and for a moment the pain is yours.
    Then it passes, and the straight road shows itself again, running north.
    Behind you it runs south to the river.""")
R[1503] = dict(name='A Long Road', desc="""
    The road clears, and the fog and ache of the first steps fall behind you.
    Yet your mind is still haunted by one picture: an old woman kneeling at a
    shrine, her eyes closing, smiling and weeping at once, saying a name you
    know.  The road runs north, and back south.""")
R[1504] = dict(name='A Long Road', desc="""
    Ahead the road comes to an end against the mountainside.  Something in the
    cold of the wind tells you the end of the road is only the beginning of the
    journey.  Small stones have been piled at the roadside by those who came
    before, one cairn for every pilgrim who turned back south from here.  The
    road goes on north.""",
    extras={'stones cairn cairns': 'There are a great many cairns. Some of the stones have been scratched with the badge of a Midgaard regiment.'})
R[1505] = dict(name='A Test for the Faithful', desc="""
    Here the road parts and the first choice must be made.  A stair climbs up
    toward a pale light; another goes down into darkness.  Only the depths of
    your own soul can choose between them, but the Watchers of the Road say
    this much: the same truth waits at the end of both, and the Weigher waits
    behind the truth.""")
R[1506] = dict(name='Halls of the Forgotten', desc="""
    Even the darkest have a place on the road to the truth.  It is in these
    empty halls, long forgotten by the living, that the Weigher has gathered
    the worst of men to look upon them one last time.  Passages lead east and
    west into the dark, and the stair climbs back up to the parting of the
    ways.""")
R[1507] = dict(name="The Pilgrim's Vow", desc="""
    Words are cut into the rock here in a flowing hand, the vow that Oswen the
    First Pilgrim made at this spot: to walk straight though the road is hard,
    to carry the light though it burns the hand, and to answer for all he
    carried when he came to be weighed.  Every penitent says it aloud before
    going on, and after it, everything carried this far seems light.  Ways lead
    east and west, and a stair goes down.""",
    extras={'words rock vow': '"I will walk straight though the road is hard. I will carry the light though it burns. I will answer for what I carry." Beneath it, thousands of pilgrims have cut their marks.'})
R[1508] = dict(name='Earthly Evil', desc="""
    Whatever it holds, rage makes a weapon of it.  Wrath arms everyone.  When an
    angry man thirsts for blood anything at all will serve him for a spear, and
    fury turns a stick into a cudgel.  The floor is littered with such things:
    sticks, stones, a broken bottle, a cook's knife.  The way leads north, and
    east back to the halls.""",
    extras={'sticks stones bottle knife': 'Ordinary things, each with a dark stain at one end.'})
R[1509] = dict(name='Misguidance', desc="""
    Some are brought here not for what they did but for what they failed to
    do: those who were shown the plain truth and turned it away with a clear
    mind.  Of all who suffer on the road they deserve the most pity.  A king in
    a crown of weed is here, dripping water that never stops.  The way goes
    north and south.""")
R[1510] = dict(name='Temptation', desc="""
    The old tale says that the Tempter came to Oswen the First Pilgrim in the
    hills and offered him a kingdom, great riches, and a glorious death from
    which the Watchers would catch him up.  Even Oswen had to stop and think
    before he answered.  Consider how much harder it is for the rest of us.
    The way runs north and south.""")
R[1511] = dict(name='Hypocrisy', desc="""
    Prince Oduran called his people to strict purity.  He set the hours of
    prayer and punished every slip in the words of the vow, and he set the best
    example of all, shunning riches and riding through his capital in rags on
    a lame mule.  But remember this: behind closed doors, all men are
    hypocrites.  The way runs north and south.""")
R[1512] = dict(name='Hate', desc="""
    Nothing in life is easier than hate, and nothing is a quicker road to
    ruin.  You give thanks that these trials are nearly done, but your words are
    drowned by a hoarse shouting that fills your ears with anger: a single
    phrase, over and over, "They took it from us.  Burn them, and it will come
    back."  The way runs north and south.""")
R[1513] = dict(name='Spiritual Danger', desc="""
    Some evils are plain and solid, so open that they spit in your face.
    Others are clever and quiet, and those are the most dangerous.  Looking
    north down the hall, a great fear fills you, and with it a great, heavy
    longing.  The way back to the halls lies west.""")
R[1514] = dict(name='The Fall', desc="""
    In the beginning Sefhra was the first and fairest of the Watchers of the
    Road.  When the Weigher set the scales upon the road, every Watcher bowed
    and laid a hand on them to be weighed first.  Sefhra would not; nothing so
    fair, he said, could be found wanting.  Look at your own beauty, pilgrim,
    and do what he could not: put it on the scales.  The hall runs north and
    south.""")
R[1515] = dict(name='Temptation', desc="""
    Temptation is the IF: the wondering, the second guess, the "I will be a
    better man... if...".  And the if is usually taken alone, in the dark,
    listening to a voice at your shoulder offering such an easy road, and such
    a crooked one.  Some pilgrims say the voice sounds like the wind out of the
    west.  The hall runs north and south.""")
R[1516] = dict(name='The Last Day', desc="""
    The din of a great battle shakes these halls, and the earth groans at the
    shaking of the last day, when the Weigher's scales come down for the final
    time.  Be ready for that day, very ready, for if you are not, the Tempter
    will claim you for his own.  A violet shape coils in the smoke.  The hall
    runs north and south.""")
R[1517] = dict(name='Flame', desc="""
    Horror past describing, a blackness broken only by burning.  The fire here
    does not come from wood or molten rock but from the souls themselves, the
    brightness and pain of the tormented crowding close on every side.  Through
    it the way runs north toward the last trials, and back south.""")
R[1518] = dict(name='Earthly Light', desc="""
    Slipping into evil is easy; walking this way is the hardest thing of all.
    Even the four you will meet ahead strayed from the line at least once, and
    there are still some who curse their names.  Confront them all the same,
    and let what they did be your example.  The way runs north, and east back
    to the vow.""")
R[1519] = dict(name='The Light of the Stewards', desc="""
    Many believed Oswen the First Pilgrim could never die, but when they stood
    over his body they saw they must keep the road without him.  The four who
    came after are called the Stewards, the rightly-guided, who carried his
    lantern and his word and built the great pilgrim houses of the old east.
    The way runs north and south.""")
R[1520] = dict(name='The Light of the Stewards', desc="""
    Each Steward was chosen by a council of elders, every one of whom hoped to
    rule the road alone and so voted for the man he thought weakest.  Each
    time, they were wrong.  Each Steward was nobler and more upright than the
    one before.  A tall, plain man waits here, unwilling to fight.  The way runs
    north and south.""")
R[1521] = dict(name='The Light of the Stewards', desc="""
    Every bright and happy tale ends too soon, and so it was with the age of
    the Stewards.  They were good men and true to the road, but their followers
    began to quarrel over who should hold the lantern, and war between brothers
    gathered on the horizon.  The way runs north and south.""")
R[1522] = dict(name='The Light of the Stewards', desc="""
    The end of the Stewards was the beginning of the Schism.  The memory of
    Oswen and the example of the four were not enough for the faithful.  Edrin,
    the last Steward, was killed at the river crossing, and some say the
    stewardship died with him, a martyr whose blood still runs in the nameless
    river.  The way runs north and south.""")
R[1523] = dict(name='Spiritual Reward', desc="""
    The Weigher is generous and would not leave those who walk the way of light
    without a guide.  So the road was given its Pilgrim-Saints, and in the
    story of their growing, from cradle to grave and beyond, each pilgrim may
    find the truth of their own.  The way runs north, and west back to the
    vow.""")
R[1524] = dict(name='Creation', desc="""
    Every dawn on the road is a small making.  The pilgrims say the Weigher
    made the world in a single breath and left the road running through it like
    a thread through cloth, so that anything made could find its way home.  An
    infant sleeps here in a nest of blankets, newly made and not yet lost.  The
    way runs north and south.""")
R[1525] = dict(name='Revelation', desc="""
    The boy who would be the first of the Pilgrim-Saints was lame, and the
    other children laughed at him.  Corrith the Herald found him by the river
    and set a lantern in his hands, and told him the road would carry him as
    far as he would carry the light.  He walked from that day on.  The way runs
    north and south.""")
R[1526] = dict(name='Conversion', desc="""
    Here the man turned from the road he had walked all his life.  He gave his
    house to his brother and his sword to the river, and went on with nothing
    but the lantern.  It is not hard to turn, the saints say; it is hard to
    stay turned.  A man kneels here in a worn robe, at peace.  The way runs
    north and south.""")
R[1527] = dict(name='Deliverance', desc="""
    The balance has been struck, the soul made ready, and the final weighing
    taken.  For those who have come this far, surely this is the first day of
    forever.  The air is full of warmth and the smell of gardens, though no
    garden grows here.  The way runs north and south.""")
R[1528] = dict(name='Repentance', desc="""
    Sorrow freely given is weighed lightly.  But the Watchers of the Road say
    there is one sorrow that counts for nothing: the sorrow of a man who does
    evil all his life, knowing it, and weeps only when the grave opens at his
    feet.  For him the road is long and very cold.  A Watcher in black stands at
    the stair going up; the way also leads east, and south.""")
R[1529] = dict(name='Pilgrimage', desc="""
    It is asked of every soul to walk this road once in its life, if it is
    able.  For those who have lived the lesser evils, walking it with an open
    and sorrowful heart lays down all they carry.  The scraps of cloth by the
    river are all that is left of a thousand such burdens.  A stair climbs up,
    and ways lead east and west.""")
R[1530] = dict(name='Intercession', desc="""
    It is written on the road that no one may plead before the Weigher for
    another.  No prayer said for him can save a doomed man; his only hope is
    the prayer of his own mouth.  A Watcher with a great shield waits here,
    and will not move aside for any prayer but yours.  Ways lead up, south and
    west.""")
R[1531] = dict(name='The Upper Reaches', desc="""
    You have walked the way of light, and faced the examples of the Stewards
    who kept Oswen's road.  Only the last journey is left; live as they lived,
    and you will live forever.  The air is thin and very clear.  The way runs
    east, back south, and down.""")
R[1532] = dict(name='The Upper Reaches', desc="""
    Up here a great book lies open on a stone, and the wind turns its pages:
    the Weigher's record, with every deed of every pilgrim written in it.  No
    hand holds the pen, but the writing goes on.  You catch sight of your own
    name and look away.  The way runs east and west, and a stair leads
    down.""")
R[1533] = dict(name='The Upper Reaches', desc="""
    You have walked the way of light, and your journey has followed the
    growing of the most perfect soul.  Only one road is left; die as the one in
    the room before you died, and your death will mean nothing.  A Watcher
    holding scales waits here.  The way runs west, back south, and down.""")
R[1534] = dict(name='The Final Facing', desc="""
    The western end of a long bare gallery where the two halves of the road
    meet again.  The last of the darkness lies below you, and the last of the
    light above; only the straight road remains.  Go on with a clean heart.
    The gallery runs east; stairs lead both up and down.""")
R[1535] = dict(name='The Final Facing', desc="""
    The middle of the gallery of the Final Facing.  Here every pilgrim must
    turn and look at all they have been, the dark below and the bright above,
    and own both.  Only the penitent find what they seek.  The straight road
    goes on north; the gallery runs east and west, and stairs go up and
    down.""")
R[1536] = dict(name='The Final Facing', desc="""
    The eastern end of the gallery.  Pilgrims have scratched their names into
    the walls here, and some have scratched them out again.  The last of the
    darkness lies behind you, and the gallery runs back west toward the
    straight road.  Stairs climb up and go down.""",
    extras={'names walls': 'Thousands of names, some struck through by the same hand that wrote them. One reads only: "Not yet."'})
R[1537] = dict(name='A Straight Path', desc="""
    "Keeper of the Scales, be patient with us.  We are crooked, and the road is
    straight.  Hold up the lantern a little longer, and we will come."  So the
    pilgrims sing as they reach this place, and their voices still hang in the
    air.  The road runs straight ahead to the north, and the gallery lies
    south.""")
R[1538] = dict(name='Progression', desc="""
    Each step now asks a little more of you, and gives a little more back.  The
    pilgrims say the Weigher never tires of making, and will make a man again
    as often as he falls, so long as he gets up facing the right way.  The road
    runs north and south.""")
R[1539] = dict(name='Judgment', desc="""
    Without doubt the shortest road is the straightest one.  Only one step is
    left before the final choice is made and a home given you for all time.
    A mocking wisp flits here to make you doubt it.  The road goes north, and
    back south.""")
R[1540] = dict(name='The Utmost Throne', desc="""
    You have come at last to the seat of the Weigher.  A clarity like crystal
    has been given to your sight; seven guardians stand about the edge of the
    throne, and everything is bathed in a warm, clean light.  Here the last
    choice is made, and nothing you do in defiance can change what is weighed.
    The road lies back south.""")

# ====================================================================== mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc)
    d.update(kw)
    return d

M[1500] = mob('the Weigher', 'weigher judge god', 'You resist the urge to avert your eyes from the Weigher at the end of the road.',
              'The sight is different for every soul, a mirror held up to what each pilgrim truly is. At first a proud and bitter old judge; just as easily a gentle open hand, a smile, and gardens... gardens.')
M[1501] = mob('Vessamar of the Scales', 'vessamar watcher scales', 'Vessamar, the Watcher of the Scales, turns and begins to look you over.',
              'At first you see only a bright and comforting glow; then the shape sharpens, and you see a face, eyes, hands holding a pair of scales, and then that too fades and you see nothing.')
M[1502] = mob('Corrith the Herald', 'corrith watcher herald', 'Corrith the Herald, Watcher of the Road, smiles and begins to tell you something.',
              'Called the Herald, it was this Watcher who brought the word of the road to the Pilgrim-Saints, and who carried Oswen the First Pilgrim across the mountains in a single night.')
M[1503] = mob('Ildane the Shield', 'ildane watcher shield', 'Ildane the Shield, Watcher of the Road, looks up and frowns at you in disapproval.',
              'It is impossible to fix your eyes on this Watcher. He is nothing human, and with a whisper he scatters every picture of him you try to make in your mind.')
M[1504] = mob('Morvaine of the Dark Gate', 'morvaine watcher gate dark', 'Morvaine, the Watcher of the Dark Gate, stands here guarding the way forward.',
              'When Sefhra fell, the Weigher had need of a fourth Watcher, and Morvaine rose from the dark ways of the road to take the place. Morvaine knows every sin that passes up the stair.')
M[1505] = mob('the gate-child', 'child warden gatechild', 'The gate-child of the blazing sword looks at you and begins to chuckle.',
              'It seems to be nothing more than a small child wrapped in glowing white cloth, but as you try to walk past it grins and cackles, drawing a sword far too large for it, and bars the road.')
M[1506] = mob('the jester', 'jester fool', 'A mad, drunken jester is sitting here, lost in his deepening stupor.',
              'He is dimly aware of your gaze. Chuckling softly, he mutters something about dragons, a temple, the falling of great kingdoms and a city in the west that will swallow them all. He laughs at you and takes another drink.')
M[1507] = mob('the mocking wisp', 'wisp sprite mocking', 'A mocking wisp dances in and out of the air before your eyes, taunting you.',
              'The pilgrims say the wisps are the souls of liars, bound to the road to lie to those who walk it. They promise shortcuts, wishes, easy ways. To you it looks like nothing more than an annoying little sprite of light.')
M[1508] = mob('the slumped old warlord', 'warlord old man grevaunt marshal', 'A slumped, shaking old warlord stands up and begins to shout at the world.',
              'Marshal Grevaunt wears a faded uniform hung with honours he awarded himself. He once taught a whole people to hate their neighbours and marched them into the fire for it, and his hand has not stopped shaking since.')
M[1509] = mob('Prince Oduran', 'oduran prince ascetic', 'Prince Oduran the Ascetic sits here in rags, washing blood from his hands in a silver bowl.',
              'Thin as a rake, in a coarse wool tunic, he has not bathed in months nor eaten in days. His people thought him a saint. The water in his bowl never runs clear, and his smile is still so charming.')
M[1510] = mob('Cassel the Betrayer', 'cassel betrayer', 'The Betrayer approaches slowly, holding out his arms in an embrace.',
              'Cassel walked beside Oswen the First Pilgrim for years, and sold him for a purse of silver. You see nothing in his face but the sadness of a man who would sell the road itself.')
M[1511] = mob('Ozmandar the Drowned King', 'ozmandar king drowned', 'Ozmandar the Drowned King stands here, dripping, sent for a lifetime of pride.',
              'Robed in sodden cloth of gold and crowned with river weed, he was shown the truth and drove his host into the flood rather than bow to it. He looks at you with nothing but a smirk of contempt.')
M[1512] = mob('Hadric the Mourner', 'hadric steward first mourner', 'Hadric, first of the Stewards, mourns over the death of the First Pilgrim.',
              'A simple man in dark, plain robes, bent and silent, living again the memory of a friend he never believed would die.')
M[1513] = mob('Talmor the Upright', 'talmor steward second upright', 'You see Talmor, second of the Stewards, who kept the First Pilgrim\'s road.',
              'You are struck by the man\'s uprightness. He looks at you sadly and says: "I do not wish to fight you, but if you refuse the truth of the road, then I must."')
M[1514] = mob('Brannoc the Chosen', 'brannoc steward third chosen', 'The third of the rightly-guided Stewards, Brannoc, stands before you.',
              'He was chosen by a clique of jealous rivals who could agree on nobody else. With the memory of the First Pilgrim fading fast from the faithful, he could do little, and in the end his enemies killed him.')
M[1515] = mob('Edrin the Last Steward', 'edrin steward fourth last', 'You have come before Edrin, fourth and last of the Stewards.',
              'Some hold him the nearest to the truth of all the Stewards, most deserving of honour. Others called him a schismatic and a traitor, to be killed and forgotten. Looking at him now, you must decide for yourself.')
M[1516] = mob('Sefhra the Unweighed', 'sefhra unweighed fallen watcher', 'You gaze in awe at the fairest of all the Watchers, Sefhra the Unweighed.',
              'He smiles calmly and tells you of the day he would not lay his hand upon the scales. Then he gestures at you, smiling, and conjures a picture of every temptation that will be yours if only you follow him.')
M[1517] = mob('the Tempter', 'tempter voice', 'You pause nervously as a voice whispers at you from over your shoulder.',
              'There is no shape to the presence that fills this place, only laughter, moaning, screaming and begging, and beneath it all a patient voice that knows your name.')
M[1518] = mob('the violet dragon', 'dragon serpent violet', 'A violet dragon turns to you in violent lust for your soul.',
              'The old serpent of the last day, ancient and violet-hued, that has watched kingdom after kingdom bow down before it. It turns to you as though you were the last.')
M[1519] = mob('the burning demon', 'demon fire burning', 'The fire around you is ruled by a massive, burning demon.',
              'You see nothing but the red, unending anger of the lord of the burning ways, the fate you have always been afraid of.')
M[1520] = mob('the innocent baby', 'baby innocent', 'Lying on the ground wrapped in blankets is the most innocent of babies.',
              'A newly made soul at the start of its road, barely aware of you, lost in a sleepy, contented yawn.')
M[1521] = mob('the teenage boy', 'boy teenage', 'You stop in surprise at the sight of a teenage boy staring off into the distance.',
              'He is young, and has not yet seen how bloody the world is. Following his gaze, you see he is staring in wonder at the full moon.')
M[1522] = mob('the man', 'man kneeling', 'A middle-aged man is here, kneeling in prayer.',
              'He is tired and lined with age, but kneeling in his worn robe he is the picture of perfect contentment.')
M[1523] = mob('the bodyless soul', 'soul bodyless', 'You are overwhelmed by the presence of a soul that has left its body behind.',
              'Tastes and scents reach you, and the wind moving through gardens. Nothing can explain or describe this perfection, this utter peace.')

# ====================================================================== objs
O[1500] = dict(short='the Scales of Vessamar', aliases='scales justice scale vessamar', long='Two beautiful plates hung like scales have been left here.',
               extras={'scales justice scale vessamar': 'The scales sway gently back and forth of their own accord, as if weighing something you cannot yet see.'})
O[1501] = dict(short="the Herald's Scroll", aliases='scroll parchment herald', long='A solid, silver-lined scroll rests on the ground.',
               extras={'scroll parchment herald': 'It seems to hold some working meant to carry its bearer across great distances, as the Herald carried the First Pilgrim, but how to use it is impossible to tell.'})
O[1502] = dict(short='a blazing sword', aliases='sword blazing', long='You are startled by the sight of a sword that blazes up as you approach it.',
               extras={'sword blazing': 'The edge of the blade is lined with writing, the words of the Pilgrim\'s Vow, in a fine silver-laced flowing script.'})
O[1503] = dict(short='the Shield of the Penitent', aliases='shield protector penitent', long='A weighty shield has been abandoned here by one unworthy to hold it.',
               extras={'shield protector penitent': 'It slides away from your attempts to look at it, turning your gaze as it will turn the weapons that try to kill you.'})
O[1504] = dict(short='a faded armband', aliases='armband band faded', long='A ragged, faded strip of cloth has been left here, forgotten.',
               extras={'armband band faded': 'It bears the badge of Marshal Grevaunt\'s army, a burning tower on a grey field. Whatever rank it marked means nothing now.'})
O[1505] = dict(short='a jewelled scimitar', aliases='scimitar jeweled jewelled', long='A stunning curved blade glistens on the ground.',
               extras={'scimitar jeweled jewelled': 'The hilt and guard are set all round with stones and bright metals, a gift to Hadric from the pilgrim houses that he never once wore in battle.'})
O[1506] = dict(short='a charred ember', aliases='ember charred')
O[1507] = dict(short='an ethereal flame', aliases='ethereal flame')
O[1508] = dict(short='the Key to the Gates', aliases='key gates', long='You have found at last the Key to the Gates at the end of the road.')
O[1509] = dict(short='a burnt history', aliases='history burnt book', long='A burnt book, some forgotten history, lies on the ground.')
O[1510] = dict(short="a leaf of the Pilgrim's Book", aliases='leaf book page pilgrim', long='A thin leaf of parchment with flowing script and rich trim glows softly here.',
               extras={'leaf book page pilgrim': 'The Third Lantern Saying: "Carry the light, and the road carries you. Set it down, and you are only walking."'})
O[1511] = dict(short='the Forge of Unity', aliases='forge unity gloves', long='It is surely the best of men who has left these gloves here to aid you.')
O[1512] = dict(short="the Drowned King's pendant", aliases='pendant drowned king loop', long='A beautiful pendant of ancient and noble workmanship lies here, wet with river water.',
               extras={'pendant drowned king loop': 'A loop of white gold above two crossed bars, the royal sign of Ozmandar\'s sunken kingdom. It is never quite dry.'})
O[1513] = dict(short='the Amulet of the Burned Sun', aliases='amulet sun burned disc', long='A gleaming golden disc stamped with a burning sun lies here.')
O[1514] = dict(short="a graven image of Nu'Groth", aliases='image graven idol', long='You frown in disgust at the hideous idol of a false god that you have found.',
               extras={'image graven idol': 'A small figure of black stone, crudely made, showing a shape that is mostly an open door and a great deal of grey. The Tempter offers it to every pilgrim who will take it. It is the god of the west.'})

RETHEME = {
    'zones': {15: 'The Straight Path'},
    'rooms': R, 'mobs': M, 'objs': O,
}
