"""The Newbie Zone (186) re-themed as the Recruit Yards, levels 1-5.

The drill grounds east of the muster field where new characters are trained
and sent to the wall.  Three parts: the barracks halls, the drill hall and
watchtower, and the Proving Pits below, where creatures caught on the march
are kept in chains for recruits to blood themselves on.
"""

R, M, O = {}, {}, {}


def fam(vnums, name, desc):
    for v in vnums:
        R[v] = dict(name=name, desc=desc)


# ---------------------------------------------------------------- barracks
R[18600] = dict(name='The Gate Of The Recruit Yards', desc="""
    A gate in the palisade opens off the muster field into the Recruit Yards, where
    the fort turns farmhands, refugees and orphans into soldiers in a month, because
    it does not have two.  A board by the gate is chalked with the day's drill.
    The muster field lies west; the barracks run north.""",
    extras={'board drill chalk': 'TODAY: blade, shield, march, the pits. Sergeant says: if you cannot kill a chained dead man here, you will not kill a free one out there.'})
R[18601] = dict(name='The Barracks Passage', desc="""
    A long timber passage through the recruits' barracks.  Bunks are stacked three
    high behind the doors on either side, and the floor is gritty with mud from the
    yard.  The passage runs east; the gate is south.""")
R[18602] = dict(name='The Barracks Hall', desc="""
    A hall where recruits clean their kit by lamplight.  Notches cut into the
    doorpost mark each intake, and there are a great many notches.  A door leads
    south to the stores, and the hall runs east and west.""")
R[18603] = dict(name='The Crossing Of The Yards', desc="""
    The crossing where the barracks passages meet.  Doors lead north and east to
    the drill hall, brighter and cleaner than the barracks.  The barracks run west
    and south.""")
R[18604] = dict(name="The Apothecary's Passage", desc="""
    A narrow passage that smells of herbs and vinegar, between the drill hall and
    the apothecary's room.  A door is set in the south wall.""")
R[18605] = dict(name='The Punishment Pit', desc="""
    A dark, damp pit beneath the stores where recruits who run are put for a night
    to think about it.  Something else lives down here too, and it has not been
    fed.""")
R[18606] = dict(name='The Stores', desc="""
    A small storeroom of bedrolls, buckets and spare boots, kept by the yard
    sergeant.  A trapdoor in the floor leads down into the punishment pit.""")
R[18607] = dict(name='The Barracks Hall', desc="""
    More of the barracks.  The recruits here are asleep in their boots, too tired
    from drill to undress.""")
R[18608] = dict(name='The Drill Yard', desc="""
    An open yard of trampled mud where recruits drill with spear and shield.  The
    air is cold and smells of the muster field to the north.  The yard runs east
    into the barracks.""")
R[18609] = dict(name='The End Of The Barracks', desc="""
    The end of the barracks passage, where it opens onto the drill yard to the
    west.  The passage runs east.""")
R[18610] = dict(name='The Lamp-Lit Passage', desc="""
    A passage lit by lamps where the sergeants have their rooms.  It runs east and
    west.""")
R[18611] = dict(name='A Corner Of The Barracks', desc="""
    A corner of the barracks where the recruits stack their practice weapons.  A
    door leads east to the apothecary.""")
R[18612] = dict(name="The Apothecary's Room", desc="""
    Bottles, bandages and drying herbs crowd this room.  The yard apothecary
    patches up recruits after the pits.  A ladder in the corner leads down to the
    Proving Pits.""")

# ---------------------------------------------------------------- the Proving Pits
fam((18620, 18622, 18623, 18624, 18633, 18637), 'A Turn In The Proving Pits', """
    The pits are a warren of cold stone passages under the yards, coated with green
    fungus and lit by the odd sputtering torch.  Chains hang from rings in the wall,
    and not all of them are empty.  The sergeants let the chained things loose for
    recruits to fight, one at a time; some of them got loose on their own.""")
fam((18621, 18627, 18630, 18634, 18636), 'A Crossing In The Proving Pits', """
    Passages cross in the cold of the pits.  Scratches and old blood on the walls
    show where recruits have fought and won, and where they have fought and been
    carried out.""")
fam((18625, 18638, 18639), 'A Fighting Pit', """
    A wide round pit with a sanded floor, ringed by a low wall where sergeants
    stand to watch.  The sand is raked smooth each morning and is never clean by
    night.""")
fam((18626, 18631, 18635), 'A Pit Passage', """
    A long passage under the yards, slick with fungus and stinking of the creatures
    kept in the cages.  Something rattles its chain in the dark.""")
R[18628] = dict(name='A Corner Of The Pits', desc="""
    A cramped corner where two passages meet.  A sergeant's stool stands here, and a
    bucket of water for the wounded.""")
R[18629] = dict(name="The Minotaur's Pen", desc="""
    The torchlight is red here, from a brazier beside a great iron pen.  A minotaur
    taken alive on the march is kept in it, and it is let out for the best recruits
    of every intake.  A ramp leads up to the muster field.""")
R[18632] = dict(name='The Foot Of The Ladder', desc="""
    The foot of the ladder down from the apothecary's room, the entrance to the
    Proving Pits.  It is cold and dank, and from the passages ahead come growls,
    rattling chains and the shouts of recruits.""")

# ---------------------------------------------------------------- drill hall and watchtower
R[18640] = dict(name="The Hall Of The Founder", desc="""
    A small hall holding a statue of the soldier who founded the Recruit Yards.
    Recruits touch its boots for luck before the pits.""",
    extras={'statue': 'A stone sergeant with a spear, his boots rubbed bright by ten thousand hands. A plaque is fixed to the plinth.',
            'plaque nameplate name': 'It says: SERGEANT ALDO VENN, WHO TAUGHT THEM TO STAND. HE STOOD AT ASHFORD. HE IS STANDING THERE STILL.'})
R[18641] = dict(name='The Drill Hall Passage', desc="""
    A clean, bright passage hung with banners of the regiments that recruits may
    be sent to.  Many of the banners are edged in black.""")
fam((18642, 18647), 'The Drill Hall', """
    A wide hall with a high domed roof where recruits drill in bad weather.  Wooden
    stairs climb to a balcony around the dome.""")
fam((18643, 18645), 'The Watch Balcony', """
    A balcony high above the drill hall, open to the sky on the west side.  From
    here you can see over the wall: the grey country of the march, the smoke of
    burning things, and very far off, a darkness on the horizon that is not cloud.
    The sergeants bring every recruit up here once, so they know.""")
fam((18644, 18646), 'A Bright Hallway', """
    A clean hallway of whitewashed stone, a change from the mud of the barracks.
    The drill hall lies beyond.""")

# ---------------------------------------------------------------- mobs
def mob(short, aliases, long, desc, **kw):
    d = dict(short=short, aliases=aliases, long=long, desc=desc); d.update(kw); return d

M[18601] = mob('the pit beast', 'beast pit', 'A pit beast snarls in the dark, chain rattling.',
               'A mangy, many-toothed thing from the march, kept in the punishment pit to make sure nobody sleeps there.')
M[18602] = mob('a sparring recruit', 'recruit sparring', 'A sparring recruit swings a practice blade at the air.',
               'A young recruit looking for someone to spar with, and not too particular about the rules.')
M[18603] = mob('a drake whelp', 'drake whelp dragon', 'A drake whelp, the yards\' mascot, snaps at your fingers.',
               'A small grey drake found as an egg on the march and raised by the sergeants. It bites.')
M[18604] = mob('the yard sergeant', 'sergeant yard guard', 'The yard sergeant watches you with folded arms.',
               'A scarred, loud sergeant who has trained a thousand recruits and buried most of them. He looks at you as if counting.')
M[18605] = mob('the yard apothecary', 'apothecary alchemist yard', 'The yard apothecary is mixing a poultice.',
               'A brisk woman with stained fingers who patches recruits up after the pits and does not want to see them twice.', sex=2)
M[18606] = mob('a cellar crawler', 'crawler cellar', 'A cellar crawler skitters across the floor.',
               'A many-legged thing the size of a cat.')
M[18607] = mob('a chained dead man', 'dead man chained zombie', 'A chained dead man lurches at the end of its chain.',
               'A corpse from the march, still moving, kept on a chain for recruits to practise on. The sergeants say it is the kindest use for it.')
M[18608] = mob('a captured imp', 'imp captured quasit', 'A captured imp hisses and spits at you.',
               'A small grey devil caught in the Hollow Wood. It knows dirty words in four languages.')
M[18609] = mob('the pit minotaur', 'minotaur pit massive', 'The pit minotaur paws the ground, horns lowered.',
               'A huge bull-headed brute taken alive on the march, kept for the best recruits to face. Most of them lose.')
M[18610] = mob('a captive shade', 'shade captive spectre', 'A captive shade flickers in a ring of salt.',
               'A dead soldier\'s shade, bound with salt and iron. It does not know it is dead.')
M[18611] = mob('a cocky recruit', 'recruit cocky', 'A cocky recruit sneers at you.',
               'A young bully who thinks the march will be easy.')
M[18612] = mob('a clueless recruit', 'recruit clueless', 'A clueless recruit is holding his sword by the wrong end.',
               'A recruit who will need a great deal of luck.')
M[18613] = mob('a talkative recruit', 'recruit talkative', 'A talkative recruit wants to tell you all about the farm.',
               'A recruit from the Granary Fields who will not stop talking about home.')
M[18614] = mob('a lost recruit', 'recruit lost', 'A lost recruit is looking for the drill hall.',
               'A recruit who has been lost in the barracks for two days.')
M[18615] = mob('a sharp recruit', 'recruit sharp', 'A sharp-eyed recruit polishes her kit.',
               'The best of this intake, quick and careful. She will make sergeant, if she lives.', sex=2)

O[18601] = dict(short="a recruit's sword", aliases='sword recruit newbie', long="A recruit's sword lies here.")
O[18602] = dict(short="a recruit's padded vest", aliases='vest padded recruit newbie', long="A recruit's padded vest lies here.")
O[18603] = dict(short="a recruit's helm", aliases='helm recruit newbie', long="A recruit's dented helm lies here.")
O[18604] = dict(short='a dark wool cloak', aliases='cloak wool dark', long='A dark wool cloak lies here.')
O[18605] = dict(short='an oath ring', aliases='ring oath signet', long='A plain iron oath ring lies here.')
O[18606] = dict(short="a recruit's dagger", aliases='dagger recruit newbie', long="A recruit's dagger lies here.")
O[18607] = dict(short="a drake's collar", aliases='collar drake', long="A drake's collar lies here.")
O[18608] = dict(short='a small iron key', aliases='key small iron wee', long='A small iron key lies here.')
O[18609] = dict(short='a jar of glow-moss', aliases='jar glow moss', long='A jar of glowing moss lies here.')
O[18610] = dict(short='the horns of the pit minotaur', aliases='horns minotaur')
O[18611] = dict(short='the hide of the pit minotaur', aliases='hide minotaur')
O[18612] = dict(short="a recruit's leggings", aliases='leggings recruit newbie', long="A pair of recruit's leggings lies here.")
O[18613] = dict(short="a recruit's sleeves", aliases='sleeves recruit newbie', long="A pair of recruit's sleeves lies here.")
O[18614] = dict(short='a blessed training mace', aliases='mace blessed training', long='A blessed training mace lies here, glowing faintly.')

RETHEME = {'zones': {186: 'The Recruit Yards'}, 'rooms': R, 'mobs': M, 'objs': O}
