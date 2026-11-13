# Eastern zones re-theme guide (2026-11-13)

The world (Elden Realms) is being re-themed to **dark fantasy**. Read this whole
file, then `tools/zonebuild/retheme.py` (the tool's docstring documents the spec
format) and `tools/zonebuild/retheme/midgaard.py` (a finished spec in the right
voice; copy its structure and its `mob()`/`obj()` helpers if useful).

## The world
- All evil flows from **Nu'Groth**, a dark entity far in the west. Fifteen march
  zones lie between it and Midgaard; the further west, the worse it gets.
  Write it as `Nu\'Groth` inside single-quoted Python strings.
- **Midgaard is the fort on the front**: a walled city whose western gate is the
  only road into the march. Its Lord Commander holds the wall. The dead come back
  in its temple. The zones east of Midgaard are the stronghold of the living and
  exist to keep the wall manned (supply, troops, faith, crafting, coin).
- The east is not untouched. Refugees, levies, tithes, shortages, grief, rumours,
  cults and things that crept in under the march are everywhere. Tone is **pretty
  dark**: grim, tired, frightened people; quiet horror rather than gore.
- Darkness is expressed only through lore and difficulty. Do NOT invent
  game-mechanic effects (no "gloom", no incursion system).

## Zone lore (fixed -- user decisions)
- **King Welmar's Castle (150)**: a frightened crown. An old king whose taxes and
  levies keep Midgaard manned; his court is decadent, scared and full of
  intrigue, and a quiet Nu'Groth cult is growing inside it.
- **Mines of Moria (40)**: an abandoned dwarven mine that things from the west
  have tunnelled into, under the march. The incursion from below.
- **Drow City (51)**: drow exiles who made a pact with Nu'Groth and act as its
  spies and fifth column in the east.
- **Old Thalos (52)**: the first city lost to an earlier darkness, generations
  ago; now a haunted ruin.
- **New Thalos (54)**: the crowded refugee city the survivors of Thalos built; it
  supplies the front (grain, cloth, recruits, coin). Crowded, poor, devout,
  watchful; it remembers what happened to the old city.
- **The Straight Path (15)**: a penitents' pilgrim road of allegorical trials,
  levels 24-30, the hardest foes in the east. The stock zone uses REAL religious
  figures (Allah, archangels, caliphs, Judas, Iblis, Pharaoh...). Replace every
  one with invented figures: e.g. the Pilgrim-Saints, the Watchers of the Road,
  the Weigher, the Tempter, the Pale Pharaoh -> an invented drowned king, etc.
  No real-world religion, scripture or prophet may remain.

## Zone lore (Claude's calls -- keep consistent)
- **High Tower of Magic (25)**: the war-college of battle mages. It trains
  war-magi for the wall and holds dangerous things taken from the west. Some
  floors are sealed because experiments went wrong.
- **Dwarven Kingdom (65)**: the dwarves who lost Moria; they hold their mountain
  halls and are the front's forge (arms, armour, picks). Bitter about Moria.
- **Miden'Nir (35)**: frontier forest and the Woodsman Inn on the roads east of
  Midgaard; goblin bands raid the supply wagons. A crossroads zone.
- **The Three of Swords (33)**: hill farms and a mountain ridge; a mercenary
  company (the Three Swords) sells blades to the front, and bandits/slavers in
  the caves prey on refugees.
- **Rand's Tower (64)**: the tower of a dead mage, Rand, who tried to bargain
  with what is in the west; his summoning went wrong and things still walk there.
- **Redferne's Residence (79)**: the house of Redferne, a retired paladin-captain
  of the wall, off Midgaard's Lower Ward.
You may name minor NPCs, but don't invent big new history or factions beyond
these; keep the stock place's shape (a shop stays a shop, a guard stays a guard).

## What to change, what NOT to change
- Rewrite: zone name (only if it needs it), every room name + desc, room extra
  descs, exit descs that exist, every mob's aliases/short/long/desc, every
  object's aliases/short/long/extras. Change alignment (`align`) only where the
  new lore clearly flips it.
- Never change exits, flags, stats, shops, resets or vnums. Don't add or remove
  rooms. `new_mobs`/`new_objs`/`resets` only if really needed (normally not).
- **Room descs must match the room's real exits.** Read each room's D-blocks
  in lib/world/wld/NNN.wld and only mention directions that exist (and doors
  where there are doors). Don't name the destination unless you checked it.
- If you give a room `extras`, ALL its old extras are dropped -- so give the
  full new set. If a desc mentions something lookable, add an extra for it.
  Keep the keywords of extras that the stock text/puzzles depend on (e.g. a
  hidden-exit hint, a `sign`, a `plaque`) or rewrite their text to keep the hint.
- **Mob aliases**: keep one stock alias where players or scripts are likely to
  use it (e.g. `guard`, `king`, `welmar`, `shopkeeper`) and add new ones.
  First alias word should be the main noun. Shopkeepers stay shopkeepers.
- **Object aliases**: keep the item type word (sword, helm, potion, key, ...),
  so `wield sword` still works. Keys stay keys. Keep item *kind* the same: a
  sword stays a blade, a potion stays a potion, a ring stays a ring.
- Room descs 3-8 lines (~40-110 words), 3 lines is fine for plain corridors but
  every room must be distinct -- no copy-paste between rooms. Mob descs 1-3
  sentences. Mob `long` is one line ending in a period.
- English spelling as in midgaard.py (armour, grey). No real-world religions,
  brands, or modern words. Avoid "you feel" overuse.
- Mobs with special procedures keep their role; names may change.

## Process
1. Write your spec(s) at the path(s) given in your task.
2. Validate: `python3 tools/zonebuild/retheme.py <spec> --check` must print only
   `check ...` lines, no `error:`.
3. Do NOT run it without `--check`, do NOT restart the MUD, do NOT edit
   lib/world files or src/ directly. The lead applies the specs.
4. Report back briefly: spec path(s), counts of rooms/mobs/objs covered vs the
   zone's totals (aim for 100%), any vnum you skipped and why, any hardcoded
   text you noticed in src/ (spec procs speaking stock lines) that the lead
   should change, and any minor lore you invented.
