/* ************************************************************************
*   File: class.c                                       Part of CircleMUD *
*  Usage: Source file for class-specific code                             *
*                                                                         *
*  All rights reserved.  See license.doc for complete information.        *
*                                                                         *
*  Copyright (C) 1993, 94 by the Trustees of the Johns Hopkins University *
*  CircleMUD is based on DikuMUD, Copyright (C) 1990, 1991.               *
************************************************************************ */

/*
 * This file attempts to concentrate most of the code which must be changed
 * in order for new classes to be added.  If you're adding a new class,
 * you should go through this entire file from beginning to end and add
 * the appropriate new special cases for your new class.
 */



#include "conf.h"
#include "sysdep.h"

#include "structs.h"
#include "db.h"
#include "utils.h"
#include "spells.h"
#include "interpreter.h"
#include "constants.h"

/* local functions */
void snoop_check(struct char_data *ch);
int parse_class(char arg);
bitvector_t find_class_bitvector(const char *arg);
byte saving_throws(int class_num, int type, int level);
int thaco(int class_num, int level);
void roll_real_abils(struct char_data *ch);
void do_start(struct char_data *ch);
int backstab_mult(int level);
int invalid_class(struct char_data *ch, struct obj_data *obj);
int level_exp(int chclass, int level);
const char *title_male(int chclass, int level);
const char *title_female(int chclass, int level);

/* Names first */

const char *class_abbrevs[] = {
  "Mu",
  "Cl",
  "Th",
  "Wa",
  "\n"
};


const char *pc_class_types[] = {
  "Magic User",
  "Cleric",
  "Thief",
  "Warrior",
  "\n"
};


/* The menu for choosing a class in interpreter.c: */
const char *class_menu =
"\r\n"
"Select a class:\r\n"
"  [C]leric\r\n"
"  [T]hief\r\n"
"  [W]arrior\r\n"
"  [M]agic-user\r\n";



/*
 * The code to interpret a class letter -- used in interpreter.c when a
 * new character is selecting a class and by 'set class' in act.wizard.c.
 */

int parse_class(char arg)
{
  arg = LOWER(arg);

  switch (arg) {
  case 'm': return CLASS_MAGIC_USER;
  case 'c': return CLASS_CLERIC;
  case 'w': return CLASS_WARRIOR;
  case 't': return CLASS_THIEF;
  default:  return CLASS_UNDEFINED;
  }
}

/*
 * bitvectors (i.e., powers of two) for each class, mainly for use in
 * do_who and do_users.  Add new classes at the end so that all classes
 * use sequential powers of two (1 << 0, 1 << 1, 1 << 2, 1 << 3, 1 << 4,
 * 1 << 5, etc.) up to the limit of your bitvector_t, typically 0-31.
 */
bitvector_t find_class_bitvector(const char *arg)
{
  size_t rpos, ret = 0;

  for (rpos = 0; rpos < strlen(arg); rpos++)
    ret |= (1 << parse_class(arg[rpos]));

  return (ret);
}


/*
 * These are definitions which control the guildmasters for each class.
 *
 * The first field (top line) controls the highest percentage skill level
 * a character of the class is allowed to attain in any skill.  (After
 * this level, attempts to practice will say "You are already learned in
 * this area."
 * 
 * The second line controls the maximum percent gain in learnedness a
 * character is allowed per practice -- in other words, if the random
 * die throw comes out higher than this number, the gain will only be
 * this number instead.
 *
 * The third line controls the minimu percent gain in learnedness a
 * character is allowed per practice -- in other words, if the random
 * die throw comes out below this number, the gain will be set up to
 * this number.
 * 
 * The fourth line simply sets whether the character knows 'spells'
 * or 'skills'.  This does not affect anything except the message given
 * to the character when trying to practice (i.e. "You know of the
 * following spells" vs. "You know of the following skills"
 */

#define SPELL	0
#define SKILL	1

/* #define LEARNED_LEVEL	0  % known which is considered "learned" */
/* #define MAX_PER_PRAC		1  max percent gain in skill per practice */
/* #define MIN_PER_PRAC		2  min percent gain in skill per practice */
/* #define PRAC_TYPE		3  should it say 'spell' or 'skill'?	*/

int prac_params[4][NUM_CLASSES] = {
  /* MAG	CLE	THE	WAR */
  { 95,		95,	85,	80	},	/* learned level */
  { 100,	100,	12,	12	},	/* max per practice */
  { 25,		25,	0,	0	},	/* min per practice */
  { SPELL,	SPELL,	SKILL,	SKILL	},	/* prac name */
};


/*
 * ...And the appropriate rooms for each guildmaster/guildguard; controls
 * which types of people the various guildguards let through.  i.e., the
 * first line shows that from room 3017, only MAGIC_USERS are allowed
 * to go south.
 *
 * Don't forget to visit spec_assign.c if you create any new mobiles that
 * should be a guild master or guard so they can act appropriately. If you
 * "recycle" the existing mobs that are used in other guilds for your new
 * guild, then you don't have to change that file, only here.
 */
struct guild_info_type guild_info[] = {

/* Midgaard */
  { CLASS_MAGIC_USER,	3017,	SCMD_SOUTH	},
  { CLASS_CLERIC,	3004,	SCMD_NORTH	},
  { CLASS_THIEF,	3027,	SCMD_EAST	},
  { CLASS_WARRIOR,	3021,	SCMD_EAST	},

/* Brass Dragon */
  { -999 /* all */ ,	5065,	SCMD_WEST	},

/* this must go last -- add new guards above! */
  { -1, NOWHERE, -1}
};



/*
 * Saving throws for:
 * MCTW
 *   PARA, ROD, PETRI, BREATH, SPELL
 *     Levels 0-100 (LVL_IMMORT - 1)
 *
 * Levels 0-30 are the original CircleMUD 3.1 values.  Levels 31-100
 * continue each column in a straight line down to one third of its
 * level-30 value (minimum 1) at level 100.  Treat the 31+ values as a
 * starting point to be tuned.  Immortals (LVL_IMMORT and up) always
 * return 0.
 *
 * Do not forget to change extern declaration in magic.c if you add to this.
 */

static const byte save_table[NUM_CLASSES][5][LVL_IMMORT] = {
  { /* CLASS_MAGIC_USER */
    { /* SAVING_PARA */
       90,  70,  69,  68,  67,  66,  65,  63,  61,  60,
       59,  57,  55,  54,  53,  53,  52,  51,  50,  48,
       46,  45,  44,  42,  40,  38,  36,  34,  32,  30,
       28,  28,  27,  27,  27,  27,  26,  26,  26,  26,
       25,  25,  25,  24,  24,  24,  24,  23,  23,  23,
       23,  22,  22,  22,  21,  21,  21,  21,  20,  20,
       20,  20,  19,  19,  19,  18,  18,  18,  18,  17,
       17,  17,  17,  16,  16,  16,  16,  15,  15,  15,
       14,  14,  14,  14,  13,  13,  13,  13,  12,  12,
       12,  11,  11,  11,  11,  10,  10,  10,  10,   9,
        9
    },
    { /* SAVING_ROD */
       90,  55,  53,  51,  49,  47,  45,  43,  41,  40,
       39,  37,  35,  33,  31,  30,  29,  27,  25,  23,
       21,  20,  19,  17,  15,  14,  13,  12,  11,  10,
        9,   9,   9,   9,   9,   9,   8,   8,   8,   8,
        8,   8,   8,   8,   8,   8,   8,   8,   7,   7,
        7,   7,   7,   7,   7,   7,   7,   7,   7,   7,
        6,   6,   6,   6,   6,   6,   6,   6,   6,   6,
        6,   5,   5,   5,   5,   5,   5,   5,   5,   5,
        5,   5,   5,   4,   4,   4,   4,   4,   4,   4,
        4,   4,   4,   4,   4,   3,   3,   3,   3,   3,
        3
    },
    { /* SAVING_PETRI */
       90,  65,  63,  61,  59,  57,  55,  53,  51,  50,
       49,  47,  45,  43,  41,  40,  39,  37,  35,  33,
       31,  30,  29,  27,  25,  23,  21,  19,  17,  15,
       13,  13,  13,  13,  12,  12,  12,  12,  12,  12,
       12,  12,  11,  11,  11,  11,  11,  11,  11,  11,
       10,  10,  10,  10,  10,  10,  10,  10,   9,   9,
        9,   9,   9,   9,   9,   8,   8,   8,   8,   8,
        8,   8,   8,   7,   7,   7,   7,   7,   7,   7,
        7,   6,   6,   6,   6,   6,   6,   6,   6,   5,
        5,   5,   5,   5,   5,   5,   5,   4,   4,   4,
        4
    },
    { /* SAVING_BREATH */
       90,  75,  73,  71,  69,  67,  65,  63,  61,  60,
       59,  57,  55,  53,  51,  50,  49,  47,  45,  43,
       41,  40,  39,  37,  35,  33,  31,  29,  27,  25,
       23,  23,  23,  22,  22,  22,  22,  22,  21,  21,
       21,  21,  20,  20,  20,  20,  20,  19,  19,  19,
       19,  18,  18,  18,  18,  18,  17,  17,  17,  17,
       17,  16,  16,  16,  16,  16,  15,  15,  15,  15,
       14,  14,  14,  14,  14,  13,  13,  13,  13,  12,
       12,  12,  12,  12,  11,  11,  11,  11,  11,  10,
       10,  10,  10,  10,   9,   9,   9,   9,   8,   8,
        8
    },
    { /* SAVING_SPELL */
       90,  60,  58,  56,  54,  52,  50,  48,  46,  45,
       44,  42,  40,  38,  36,  35,  34,  32,  30,  28,
       26,  25,  24,  22,  20,  18,  16,  14,  12,  10,
        8,   8,   8,   8,   8,   8,   8,   8,   7,   7,
        7,   7,   7,   7,   7,   7,   7,   7,   7,   7,
        7,   6,   6,   6,   6,   6,   6,   6,   6,   6,
        6,   6,   6,   6,   6,   6,   5,   5,   5,   5,
        5,   5,   5,   5,   5,   5,   5,   5,   5,   4,
        4,   4,   4,   4,   4,   4,   4,   4,   4,   4,
        4,   4,   4,   4,   3,   3,   3,   3,   3,   3,
        3
    },
  },
  { /* CLASS_CLERIC */
    { /* SAVING_PARA */
       90,  60,  59,  48,  46,  45,  43,  40,  37,  35,
       34,  33,  31,  30,  29,  27,  26,  25,  24,  23,
       22,  21,  20,  18,  15,  14,  12,  10,   9,   8,
        7,   7,   7,   7,   7,   7,   7,   6,   6,   6,
        6,   6,   6,   6,   6,   6,   6,   6,   6,   6,
        6,   6,   5,   5,   5,   5,   5,   5,   5,   5,
        5,   5,   5,   5,   5,   4,   4,   4,   4,   4,
        4,   4,   4,   4,   4,   4,   4,   4,   4,   4,
        3,   3,   3,   3,   3,   3,   3,   3,   3,   3,
        3,   3,   3,   2,   2,   2,   2,   2,   2,   2,
        2
    },
    { /* SAVING_ROD */
       90,  70,  69,  68,  66,  65,  63,  60,  57,  55,
       54,  53,  51,  50,  49,  47,  46,  45,  44,  43,
       42,  41,  40,  38,  35,  34,  32,  30,  29,  28,
       27,  27,  26,  26,  26,  26,  25,  25,  25,  25,
       24,  24,  24,  24,  23,  23,  23,  23,  22,  22,
       22,  22,  21,  21,  21,  21,  20,  20,  20,  20,
       19,  19,  19,  19,  18,  18,  18,  17,  17,  17,
       17,  16,  16,  16,  16,  15,  15,  15,  15,  14,
       14,  14,  14,  13,  13,  13,  13,  12,  12,  12,
       12,  11,  11,  11,  11,  10,  10,  10,  10,   9,
        9
    },
    { /* SAVING_PETRI */
       90,  65,  64,  63,  61,  60,  58,  55,  53,  50,
       49,  48,  46,  45,  44,  43,  41,  40,  39,  38,
       37,  36,  35,  33,  31,  29,  27,  25,  24,  23,
       22,  22,  22,  21,  21,  21,  21,  20,  20,  20,
       20,  20,  19,  19,  19,  19,  19,  18,  18,  18,
       18,  18,  17,  17,  17,  17,  16,  16,  16,  16,
       16,  15,  15,  15,  15,  14,  14,  14,  14,  14,
       13,  13,  13,  13,  13,  12,  12,  12,  12,  12,
       11,  11,  11,  11,  10,  10,  10,  10,  10,   9,
        9,   9,   9,   8,   8,   8,   8,   8,   7,   7,
        7
    },
    { /* SAVING_BREATH */
       90,  80,  79,  78,  76,  75,  73,  70,  67,  65,
       64,  63,  61,  60,  59,  57,  56,  55,  54,  53,
       52,  51,  50,  48,  45,  44,  42,  40,  39,  38,
       37,  37,  36,  36,  36,  35,  35,  34,  34,  34,
       33,  33,  33,  32,  32,  32,  31,  31,  31,  30,
       30,  30,  29,  29,  28,  28,  28,  27,  27,  27,
       26,  26,  26,  25,  25,  24,  24,  24,  23,  23,
       23,  22,  22,  22,  21,  21,  21,  20,  20,  20,
       19,  19,  18,  18,  18,  17,  17,  17,  16,  16,
       16,  15,  15,  14,  14,  14,  13,  13,  13,  12,
       12
    },
    { /* SAVING_SPELL */
       90,  75,  74,  73,  71,  70,  68,  65,  63,  60,
       59,  58,  56,  55,  54,  53,  51,  50,  49,  48,
       47,  46,  45,  43,  41,  39,  37,  35,  34,  33,
       32,  32,  31,  31,  31,  30,  30,  30,  30,  29,
       29,  29,  28,  28,  28,  28,  27,  27,  27,  26,
       26,  26,  25,  25,  25,  24,  24,  24,  24,  23,
       23,  23,  22,  22,  22,  22,  21,  21,  21,  20,
       20,  20,  19,  19,  19,  18,  18,  18,  18,  17,
       17,  17,  16,  16,  16,  16,  15,  15,  15,  14,
       14,  14,  13,  13,  13,  12,  12,  12,  12,  11,
       11
    },
  },
  { /* CLASS_THIEF */
    { /* SAVING_PARA */
       90,  65,  64,  63,  62,  61,  60,  59,  58,  57,
       56,  55,  54,  53,  52,  51,  50,  49,  48,  47,
       46,  45,  44,  43,  42,  41,  40,  39,  38,  37,
       36,  36,  35,  35,  35,  34,  34,  34,  33,  33,
       33,  32,  32,  32,  31,  31,  31,  30,  30,  29,
       29,  29,  28,  28,  28,  27,  27,  27,  26,  26,
       26,  25,  25,  25,  24,  24,  24,  23,  23,  23,
       22,  22,  22,  21,  21,  21,  20,  20,  20,  19,
       19,  19,  18,  18,  17,  17,  17,  16,  16,  16,
       15,  15,  15,  14,  14,  14,  13,  13,  13,  12,
       12
    },
    { /* SAVING_ROD */
       90,  70,  68,  66,  64,  62,  60,  58,  56,  54,
       52,  50,  48,  46,  44,  42,  40,  38,  36,  34,
       32,  30,  28,  26,  24,  22,  20,  18,  16,  14,
       13,  13,  13,  13,  12,  12,  12,  12,  12,  12,
       12,  12,  11,  11,  11,  11,  11,  11,  11,  11,
       10,  10,  10,  10,  10,  10,  10,  10,   9,   9,
        9,   9,   9,   9,   9,   8,   8,   8,   8,   8,
        8,   8,   8,   7,   7,   7,   7,   7,   7,   7,
        7,   6,   6,   6,   6,   6,   6,   6,   6,   5,
        5,   5,   5,   5,   5,   5,   5,   4,   4,   4,
        4
    },
    { /* SAVING_PETRI */
       90,  60,  59,  58,  58,  56,  55,  54,  53,  52,
       51,  50,  49,  48,  47,  46,  45,  44,  43,  42,
       41,  40,  39,  38,  37,  36,  35,  34,  33,  32,
       31,  31,  30,  30,  30,  30,  29,  29,  29,  28,
       28,  28,  27,  27,  27,  26,  26,  26,  26,  25,
       25,  25,  24,  24,  24,  24,  23,  23,  23,  22,
       22,  22,  21,  21,  21,  20,  20,  20,  20,  19,
       19,  19,  18,  18,  18,  18,  17,  17,  17,  16,
       16,  16,  15,  15,  15,  14,  14,  14,  14,  13,
       13,  13,  12,  12,  12,  12,  11,  11,  11,  10,
       10
    },
    { /* SAVING_BREATH */
       90,  80,  79,  78,  77,  76,  75,  74,  73,  72,
       71,  70,  69,  68,  67,  66,  65,  64,  63,  62,
       61,  60,  59,  58,  57,  56,  55,  54,  53,  52,
       51,  51,  50,  50,  49,  49,  48,  48,  47,  47,
       46,  46,  45,  45,  44,  44,  43,  43,  42,  42,
       41,  41,  40,  40,  39,  39,  38,  38,  37,  37,
       36,  36,  35,  35,  34,  34,  34,  33,  33,  32,
       32,  31,  31,  30,  30,  29,  29,  28,  28,  27,
       27,  26,  26,  25,  25,  24,  24,  23,  23,  22,
       22,  21,  21,  20,  20,  19,  19,  18,  18,  17,
       17
    },
    { /* SAVING_SPELL */
       90,  75,  73,  71,  69,  67,  65,  63,  61,  59,
       57,  55,  53,  51,  49,  47,  45,  43,  41,  39,
       37,  35,  33,  31,  29,  27,  25,  23,  21,  19,
       17,  17,  17,  17,  16,  16,  16,  16,  16,  16,
       15,  15,  15,  15,  15,  15,  14,  14,  14,  14,
       14,  14,  14,  13,  13,  13,  13,  13,  13,  12,
       12,  12,  12,  12,  12,  12,  11,  11,  11,  11,
       11,  11,  10,  10,  10,  10,  10,  10,   9,   9,
        9,   9,   9,   9,   9,   8,   8,   8,   8,   8,
        8,   7,   7,   7,   7,   7,   7,   6,   6,   6,
        6
    },
  },
  { /* CLASS_WARRIOR */
    { /* SAVING_PARA */
       90,  70,  68,  67,  65,  62,  58,  55,  53,  52,
       50,  47,  43,  40,  38,  37,  35,  32,  28,  25,
       24,  23,  22,  20,  19,  17,  16,  15,  14,  13,
       12,  12,  12,  12,  12,  11,  11,  11,  11,  11,
       11,  11,  11,  11,  10,  10,  10,  10,  10,  10,
       10,  10,   9,   9,   9,   9,   9,   9,   9,   9,
        9,   8,   8,   8,   8,   8,   8,   8,   8,   8,
        7,   7,   7,   7,   7,   7,   7,   7,   7,   6,
        6,   6,   6,   6,   6,   6,   6,   5,   5,   5,
        5,   5,   5,   5,   5,   5,   4,   4,   4,   4,
        4
    },
    { /* SAVING_ROD */
       90,  80,  78,  77,  75,  72,  68,  65,  63,  62,
       60,  57,  53,  50,  48,  47,  45,  42,  38,  35,
       34,  33,  32,  30,  29,  27,  26,  25,  24,  23,
       22,  22,  22,  21,  21,  21,  21,  20,  20,  20,
       20,  20,  19,  19,  19,  19,  19,  18,  18,  18,
       18,  18,  17,  17,  17,  17,  16,  16,  16,  16,
       16,  15,  15,  15,  15,  14,  14,  14,  14,  14,
       13,  13,  13,  13,  13,  12,  12,  12,  12,  12,
       11,  11,  11,  11,  10,  10,  10,  10,  10,   9,
        9,   9,   9,   8,   8,   8,   8,   8,   7,   7,
        7
    },
    { /* SAVING_PETRI */
       90,  75,  73,  72,  70,  67,  63,  60,  58,  57,
       55,  52,  48,  45,  43,  42,  40,  37,  33,  30,
       29,  28,  26,  25,  24,  23,  21,  20,  19,  18,
       17,  17,  17,  17,  16,  16,  16,  16,  16,  16,
       15,  15,  15,  15,  15,  15,  14,  14,  14,  14,
       14,  14,  14,  13,  13,  13,  13,  13,  13,  12,
       12,  12,  12,  12,  12,  12,  11,  11,  11,  11,
       11,  11,  10,  10,  10,  10,  10,  10,   9,   9,
        9,   9,   9,   9,   9,   8,   8,   8,   8,   8,
        8,   7,   7,   7,   7,   7,   7,   6,   6,   6,
        6
    },
    { /* SAVING_BREATH */
       90,  85,  83,  82,  80,  75,  70,  65,  63,  62,
       60,  55,  50,  45,  43,  42,  40,  37,  33,  30,
       29,  28,  26,  25,  24,  23,  21,  20,  19,  18,
       17,  17,  17,  17,  16,  16,  16,  16,  16,  16,
       15,  15,  15,  15,  15,  15,  14,  14,  14,  14,
       14,  14,  14,  13,  13,  13,  13,  13,  13,  12,
       12,  12,  12,  12,  12,  12,  11,  11,  11,  11,
       11,  11,  10,  10,  10,  10,  10,  10,   9,   9,
        9,   9,   9,   9,   9,   8,   8,   8,   8,   8,
        8,   7,   7,   7,   7,   7,   7,   6,   6,   6,
        6
    },
    { /* SAVING_SPELL */
       90,  85,  83,  82,  80,  77,  73,  70,  68,  67,
       65,  62,  58,  55,  53,  52,  50,  47,  43,  40,
       39,  38,  36,  35,  34,  33,  31,  30,  29,  28,
       27,  27,  26,  26,  26,  26,  25,  25,  25,  25,
       24,  24,  24,  24,  23,  23,  23,  23,  22,  22,
       22,  22,  21,  21,  21,  21,  20,  20,  20,  20,
       19,  19,  19,  19,  18,  18,  18,  17,  17,  17,
       17,  16,  16,  16,  16,  15,  15,  15,  15,  14,
       14,  14,  14,  13,  13,  13,  13,  12,  12,  12,
       12,  11,  11,  11,  11,  10,  10,  10,  10,   9,
        9
    },
  },
};

byte saving_throws(int class_num, int type, int level)
{
  if (class_num < 0 || class_num >= NUM_CLASSES || type < 0 || type > SAVING_SPELL) {
    log("SYSERR: Invalid class %d or saving throw type %d in saving_throws().", class_num, type);
    return 100;
  }

  if (level < 0)
    level = 0;
  if (level >= LVL_IMMORT)
    return 0;	/* immortals */

  return save_table[class_num][type][level];
}

/*
 * THAC0 for classes and levels.  (To Hit Armor Class 0)
 *
 * Levels 0-30 are the original CircleMUD 3.1 values.  Levels 31-100 continue
 * in a straight line to a per-class value at level 100 (Mu 5, Cl 1, Th 1, Wa 1).
 * Tune as desired.  Immortals (LVL_IMMORT and up) get 1.
 */

static const byte thaco_table[NUM_CLASSES][LVL_IMMORT] = {
  { /* CLASS_MAGIC_USER */
      100,  20,  20,  20,  19,  19,  19,  18,  18,  18,
       17,  17,  17,  16,  16,  16,  15,  15,  15,  14,
       14,  14,  13,  13,  13,  12,  12,  12,  11,  11,
       11,  11,  11,  11,  11,  11,  10,  10,  10,  10,
       10,  10,  10,  10,  10,  10,  10,  10,   9,   9,
        9,   9,   9,   9,   9,   9,   9,   9,   9,   9,
        8,   8,   8,   8,   8,   8,   8,   8,   8,   8,
        8,   7,   7,   7,   7,   7,   7,   7,   7,   7,
        7,   7,   7,   6,   6,   6,   6,   6,   6,   6,
        6,   6,   6,   6,   6,   5,   5,   5,   5,   5,
        5
  },
  { /* CLASS_CLERIC */
      100,  20,  20,  20,  18,  18,  18,  16,  16,  16,
       14,  14,  14,  12,  12,  12,  10,  10,  10,   8,
        8,   8,   6,   6,   6,   4,   4,   4,   2,   2,
        2,   2,   2,   2,   2,   2,   2,   2,   2,   2,
        2,   2,   2,   2,   2,   2,   2,   2,   2,   2,
        2,   2,   2,   2,   2,   2,   2,   2,   2,   2,
        2,   2,   2,   2,   2,   2,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1
  },
  { /* CLASS_THIEF */
      100,  20,  20,  19,  19,  18,  18,  17,  17,  16,
       16,  15,  15,  14,  14,  13,  13,  12,  12,  11,
       11,  10,  10,   9,   9,   8,   8,   7,   7,   6,
        6,   6,   6,   6,   6,   6,   6,   6,   5,   5,
        5,   5,   5,   5,   5,   5,   5,   5,   5,   5,
        5,   4,   4,   4,   4,   4,   4,   4,   4,   4,
        4,   4,   4,   4,   4,   4,   3,   3,   3,   3,
        3,   3,   3,   3,   3,   3,   3,   3,   3,   2,
        2,   2,   2,   2,   2,   2,   2,   2,   2,   2,
        2,   2,   2,   2,   1,   1,   1,   1,   1,   1,
        1
  },
  { /* CLASS_WARRIOR */
      100,  20,  19,  18,  17,  16,  15,  14,  14,  13,
       12,  11,  10,   9,   8,   7,   6,   5,   4,   3,
        2,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
        1
  },
};

int thaco(int class_num, int level)
{
  if (class_num < 0 || class_num >= NUM_CLASSES) {
    log("SYSERR: Unknown class in thac0 chart.");
    return 100;
  }

  if (level < 0)
    level = 0;
  if (level >= LVL_IMMORT)
    return 1;	/* immortals */

  return thaco_table[class_num][level];
}


/*
 * Roll the 6 stats for a character... each stat is made of the sum of
 * the best 3 out of 4 rolls of a 6-sided die.  Each class then decides
 * which priority will be given for the best to worst stats.
 */
void roll_real_abils(struct char_data *ch)
{
  int i, j, k, temp;
  ubyte table[6];
  ubyte rolls[4];

  for (i = 0; i < 6; i++)
    table[i] = 0;

  for (i = 0; i < 6; i++) {

    for (j = 0; j < 4; j++)
      rolls[j] = rand_number(1, 6);

    temp = rolls[0] + rolls[1] + rolls[2] + rolls[3] -
      MIN(rolls[0], MIN(rolls[1], MIN(rolls[2], rolls[3])));

    for (k = 0; k < 6; k++)
      if (table[k] < temp) {
	temp ^= table[k];
	table[k] ^= temp;
	temp ^= table[k];
      }
  }

  ch->real_abils.str_add = 0;

  switch (GET_CLASS(ch)) {
  case CLASS_MAGIC_USER:
    ch->real_abils.intel = table[0];
    ch->real_abils.wis = table[1];
    ch->real_abils.dex = table[2];
    ch->real_abils.str = table[3];
    ch->real_abils.con = table[4];
    ch->real_abils.cha = table[5];
    break;
  case CLASS_CLERIC:
    ch->real_abils.wis = table[0];
    ch->real_abils.intel = table[1];
    ch->real_abils.str = table[2];
    ch->real_abils.dex = table[3];
    ch->real_abils.con = table[4];
    ch->real_abils.cha = table[5];
    break;
  case CLASS_THIEF:
    ch->real_abils.dex = table[0];
    ch->real_abils.str = table[1];
    ch->real_abils.con = table[2];
    ch->real_abils.intel = table[3];
    ch->real_abils.wis = table[4];
    ch->real_abils.cha = table[5];
    break;
  case CLASS_WARRIOR:
    ch->real_abils.str = table[0];
    ch->real_abils.dex = table[1];
    ch->real_abils.con = table[2];
    ch->real_abils.wis = table[3];
    ch->real_abils.intel = table[4];
    ch->real_abils.cha = table[5];
    if (ch->real_abils.str == 18)
      ch->real_abils.str_add = rand_number(0, 100);
    break;
  }
  ch->aff_abils = ch->real_abils;
}


/* Some initializations for characters, including initial skills */
#include <sys/types.h>
#include <sys/stat.h>

extern struct spell_info_type spell_info[];

/*
 * REMORT SKILL MEMORY
 *
 * Before a remort wipes a character's skills, the best percent reached in every
 * skill of the class being left is remembered (legacy_record).  When the
 * character later plays that class again, each remembered skill is handed back
 * as soon as the character reaches the level that class learns it at
 * (legacy_restore, called whenever a level is gained) -- never earlier.
 *
 * The memory lives in one small text file per character, plrlegacy/<name>,
 * with lines of "<class> <skill> <percent>".
 */
static void legacy_path_name(const char *charname, char *buf, size_t len)
{
  char name[MAX_INPUT_LENGTH];
  int i;

  strlcpy(name, charname, sizeof(name));
  for (i = 0; name[i]; i++)
    name[i] = LOWER(name[i]);
  snprintf(buf, len, "plrlegacy/%s", name);
}

static void legacy_path(struct char_data *ch, char *buf, size_t len)
{
  legacy_path_name(GET_NAME(ch), buf, len);
}

/* Remove a character's skill memory file (character deleted). */
void legacy_delete(const char *charname)
{
  char path[MAX_INPUT_LENGTH];

  legacy_path_name(charname, path, sizeof(path));
  if (remove(path) < 0 && errno != ENOENT)
    log("SYSERR: deleting remort skill memory %s: %s", path, strerror(errno));
}

/*
 * A brand-new character never has skill memory.  Wipe any left over from a
 * deleted character of the same name so it cannot be inherited.
 */
void legacy_reset(struct char_data *ch)
{
  if (IS_NPC(ch))
    return;
  legacy_delete(GET_NAME(ch));
  memset(ch->player_specials->legacy, 0, sizeof(ch->player_specials->legacy));
  ch->player_specials->legacy_loaded = TRUE;
}

static void legacy_load(struct char_data *ch)
{
  char path[MAX_INPUT_LENGTH];
  FILE *fl;
  int cls, skill, pct;

  if (IS_NPC(ch) || ch->player_specials->legacy_loaded)
    return;
  ch->player_specials->legacy_loaded = TRUE;

  legacy_path(ch, path, sizeof(path));
  if (!(fl = fopen(path, "r")))
    return;
  while (fscanf(fl, "%d %d %d", &cls, &skill, &pct) == 3) {
    if (cls >= 0 && cls < NUM_CLASSES && skill > 0 && skill <= MAX_SKILLS && pct > 0 && pct <= 255)
      ch->player_specials->legacy[cls][skill] = pct;
  }
  fclose(fl);
}

/* Remember the best percent of every skill the character's current class can learn. */
void legacy_record(struct char_data *ch)
{
  int skill, cls = GET_CLASS(ch);

  if (IS_NPC(ch) || cls < 0 || cls >= NUM_CLASSES)
    return;
  legacy_load(ch);
  for (skill = 1; skill <= MAX_SKILLS; skill++)
    if (spell_info[skill].min_level[cls] < LVL_IMMORT &&
	GET_SKILL(ch, skill) > ch->player_specials->legacy[cls][skill])
      ch->player_specials->legacy[cls][skill] = GET_SKILL(ch, skill);
}

void legacy_save(struct char_data *ch)
{
  char path[MAX_INPUT_LENGTH];
  FILE *fl;
  int cls, skill;

  if (IS_NPC(ch))
    return;
  legacy_load(ch);
  mkdir("plrlegacy", 0755);		/* fine if it already exists */
  legacy_path(ch, path, sizeof(path));
  if (!(fl = fopen(path, "w"))) {
    log("SYSERR: Unable to write remort skill memory %s.", path);
    return;
  }
  for (cls = 0; cls < NUM_CLASSES; cls++)
    for (skill = 1; skill <= MAX_SKILLS; skill++)
      if (ch->player_specials->legacy[cls][skill])
	fprintf(fl, "%d %d %d\n", cls, skill, ch->player_specials->legacy[cls][skill]);
  fclose(fl);
}

/* Give back remembered skills the character's class has reached the level for. */
void legacy_restore(struct char_data *ch)
{
  int skill, cls = GET_CLASS(ch);

  if (IS_NPC(ch) || cls < 0 || cls >= NUM_CLASSES)
    return;
  legacy_load(ch);
  for (skill = 1; skill <= MAX_SKILLS; skill++)
    if (spell_info[skill].min_level[cls] <= GET_LEVEL(ch) &&
	ch->player_specials->legacy[cls][skill] > GET_SKILL(ch, skill))
      SET_SKILL(ch, skill, ch->player_specials->legacy[cls][skill]);
}

/* Skills a brand-new character of this class starts with (also used by remort). */
void init_class_skills(struct char_data *ch)
{
  switch (GET_CLASS(ch)) {

  case CLASS_MAGIC_USER:
    break;

  case CLASS_CLERIC:
    break;

  case CLASS_THIEF:
    SET_SKILL(ch, SKILL_SNEAK, 10);
    SET_SKILL(ch, SKILL_HIDE, 5);
    SET_SKILL(ch, SKILL_STEAL, 15);
    SET_SKILL(ch, SKILL_BACKSTAB, 10);
    SET_SKILL(ch, SKILL_PICK_LOCK, 10);
    SET_SKILL(ch, SKILL_TRACK, 10);
    break;

  case CLASS_WARRIOR:
    break;
  }
}

void do_start(struct char_data *ch)
{
  GET_LEVEL(ch) = 1;
  GET_EXP(ch) = 1;

  set_title(ch, NULL);
  roll_real_abils(ch);

  GET_MAX_HIT(ch)  = 10;
  GET_MAX_MANA(ch) = 100;
  GET_MAX_MOVE(ch) = 82;

  init_class_skills(ch);

  advance_level(ch);
  mudlog(BRF, MAX(LVL_IMMORT, GET_INVIS_LEV(ch)), TRUE, "%s advanced to level %d", GET_NAME(ch), GET_LEVEL(ch));

  GET_HIT(ch) = GET_MAX_HIT(ch);
  GET_MANA(ch) = GET_MAX_MANA(ch);
  GET_MOVE(ch) = GET_MAX_MOVE(ch);

  GET_COND(ch, THIRST) = 24;
  GET_COND(ch, FULL) = 24;
  GET_COND(ch, DRUNK) = 0;

  if (CONFIG_SITEOK_ALL)
    SET_BIT(PLR_FLAGS(ch), PLR_SITEOK);


  ch->player_specials->saved.olc_zone = NOWHERE;
}



/*
 * This function controls the change to maxmove, maxmana, and maxhp for
 * each class every time they gain a level.
 */
void advance_level(struct char_data *ch)
{
  int add_hp, add_mana = 0, add_move = 0, i;

  add_hp = con_app[GET_CON(ch)].hitp;

  switch (GET_CLASS(ch)) {

  case CLASS_MAGIC_USER:
    add_hp += rand_number(3, 8);
    add_mana = rand_number(GET_LEVEL(ch), (int)(1.5 * GET_LEVEL(ch)));
    add_mana = MIN(add_mana, 10);
    add_move = rand_number(0, 2);
    break;

  case CLASS_CLERIC:
    add_hp += rand_number(5, 10);
    add_mana = rand_number(GET_LEVEL(ch), (int)(1.5 * GET_LEVEL(ch)));
    add_mana = MIN(add_mana, 10);
    add_move = rand_number(0, 2);
    break;

  case CLASS_THIEF:
    add_hp += rand_number(7, 13);
    add_mana = 0;
    add_move = rand_number(1, 3);
    break;

  case CLASS_WARRIOR:
    add_hp += rand_number(10, 15);
    add_mana = 0;
    add_move = rand_number(1, 3);
    break;
  }

  ch->points.max_hit += MAX(1, add_hp);
  ch->points.max_move += MAX(1, add_move);

  if (GET_LEVEL(ch) > 1)
    ch->points.max_mana += add_mana;

  if (IS_MAGIC_USER(ch) || IS_CLERIC(ch))
    GET_PRACTICES(ch) += MAX(2, wis_app[GET_WIS(ch)].bonus);
  else
    GET_PRACTICES(ch) += MIN(2, MAX(1, wis_app[GET_WIS(ch)].bonus));

  if (GET_LEVEL(ch) >= LVL_IMMORT) {
    for (i = 0; i < 3; i++)
      GET_COND(ch, i) = (char) -1;
    SET_BIT(PRF_FLAGS(ch), PRF_HOLYLIGHT);
  }

  legacy_restore(ch);

  snoop_check(ch);
  save_char(ch);
}


/*
 * This simply calculates the backstab multiplier based on a character's
 * level.  This used to be an array, but was changed to be a function so
 * that it would be easier to add more levels to your MUD.  This doesn't
 * really create a big performance hit because it's not used very often.
 */
int backstab_mult(int level)
{
  if (level <= 0)
    return 1;	  /* level 0 */
  else if (level <= 7)
    return 2;	  /* level 1 - 7 */
  else if (level <= 13)
    return 3;	  /* level 8 - 13 */
  else if (level <= 20)
    return 4;	  /* level 14 - 20 */
  else if (level <= 28)
    return 5;	  /* level 21 - 28 */
  else if (level < LVL_IMMORT)
    return 6;	  /* all remaining mortal levels */
  else
    return 20;	  /* immortals */
}


/*
 * invalid_class is used by handler.c to determine if a piece of equipment is
 * usable by a particular class, based on the ITEM_ANTI_{class} bitvectors.
 */
int invalid_class(struct char_data *ch, struct obj_data *obj)
{
  if (OBJ_FLAGGED(obj, ITEM_ANTI_MAGIC_USER) && IS_MAGIC_USER(ch))
    return TRUE;

  if (OBJ_FLAGGED(obj, ITEM_ANTI_CLERIC) && IS_CLERIC(ch))
    return TRUE;

  if (OBJ_FLAGGED(obj, ITEM_ANTI_WARRIOR) && IS_WARRIOR(ch))
    return TRUE;

  if (OBJ_FLAGGED(obj, ITEM_ANTI_THIEF) && IS_THIEF(ch))
    return TRUE;

  return FALSE;
}


/*
 * SPELLS AND SKILLS.  This area defines which spells are assigned to
 * which classes, and the minimum level the character must be to use
 * the spell or skill.
 */
void init_spell_levels(void)
{
  /* MAGES */
  spell_level(SPELL_MAGIC_MISSILE, CLASS_MAGIC_USER, 1);
  spell_level(SPELL_DETECT_INVIS, CLASS_MAGIC_USER, 2);
  spell_level(SPELL_DETECT_MAGIC, CLASS_MAGIC_USER, 2);
  spell_level(SPELL_CHILL_TOUCH, CLASS_MAGIC_USER, 3);
  spell_level(SPELL_INFRAVISION, CLASS_MAGIC_USER, 3);
  spell_level(SPELL_INVISIBLE, CLASS_MAGIC_USER, 4);
  spell_level(SPELL_ARMOR, CLASS_MAGIC_USER, 4);
  spell_level(SPELL_BURNING_HANDS, CLASS_MAGIC_USER, 5);
  spell_level(SPELL_LOCATE_OBJECT, CLASS_MAGIC_USER, 6);
  spell_level(SPELL_STRENGTH, CLASS_MAGIC_USER, 6);
  spell_level(SPELL_SHOCKING_GRASP, CLASS_MAGIC_USER, 7);
  spell_level(SPELL_SLEEP, CLASS_MAGIC_USER, 8);
  spell_level(SPELL_LIGHTNING_BOLT, CLASS_MAGIC_USER, 9);
  spell_level(SPELL_BLINDNESS, CLASS_MAGIC_USER, 9);
  spell_level(SPELL_DETECT_POISON, CLASS_MAGIC_USER, 10);
  spell_level(SPELL_COLOR_SPRAY, CLASS_MAGIC_USER, 11);
  spell_level(SPELL_ENERGY_DRAIN, CLASS_MAGIC_USER, 13);
  spell_level(SPELL_CURSE, CLASS_MAGIC_USER, 14);
  spell_level(SPELL_POISON, CLASS_MAGIC_USER, 14);
  spell_level(SPELL_FIREBALL, CLASS_MAGIC_USER, 15);
  spell_level(SPELL_CHARM, CLASS_MAGIC_USER, 16);
  spell_level(SPELL_ENCHANT_WEAPON, CLASS_MAGIC_USER, 26);
  spell_level(SPELL_CLONE, CLASS_MAGIC_USER, 30);
  spell_level(SPELL_HASTE,          CLASS_MAGIC_USER, 90);
  spell_level(SPELL_CHAIN_LIGHTNING, CLASS_MAGIC_USER, 95);
  spell_level(SPELL_METEOR_SWARM,   CLASS_MAGIC_USER, 100);

  /* CLERICS */
  spell_level(SPELL_CURE_LIGHT, CLASS_CLERIC, 1);
  spell_level(SPELL_ARMOR, CLASS_CLERIC, 1);
  spell_level(SPELL_CREATE_FOOD, CLASS_CLERIC, 2);
  spell_level(SPELL_CREATE_WATER, CLASS_CLERIC, 2);
  spell_level(SPELL_DETECT_POISON, CLASS_CLERIC, 3);
  spell_level(SPELL_DETECT_ALIGN, CLASS_CLERIC, 4);
  spell_level(SPELL_CURE_BLIND, CLASS_CLERIC, 4);
  spell_level(SPELL_BLESS, CLASS_CLERIC, 5);
  spell_level(SPELL_DETECT_INVIS, CLASS_CLERIC, 6);
  spell_level(SPELL_BLINDNESS, CLASS_CLERIC, 6);
  spell_level(SPELL_INFRAVISION, CLASS_CLERIC, 7);
  spell_level(SPELL_PROT_FROM_EVIL, CLASS_CLERIC, 8);
  spell_level(SPELL_POISON, CLASS_CLERIC, 8);
  spell_level(SPELL_GROUP_ARMOR, CLASS_CLERIC, 9);
  spell_level(SPELL_CURE_CRITIC, CLASS_CLERIC, 9);
  spell_level(SPELL_SUMMON, CLASS_CLERIC, 10);
  spell_level(SPELL_REMOVE_POISON, CLASS_CLERIC, 10);
  spell_level(SPELL_WORD_OF_RECALL, CLASS_CLERIC, 12);
  spell_level(SPELL_EARTHQUAKE, CLASS_CLERIC, 12);
  spell_level(SPELL_DISPEL_EVIL, CLASS_CLERIC, 14);
  spell_level(SPELL_DISPEL_GOOD, CLASS_CLERIC, 14);
  spell_level(SPELL_SANCTUARY, CLASS_CLERIC, 15);
  spell_level(SPELL_CALL_LIGHTNING, CLASS_CLERIC, 15);
  spell_level(SPELL_HEAL, CLASS_CLERIC, 16);
  spell_level(SPELL_CONTROL_WEATHER, CLASS_CLERIC, 17);
  spell_level(SPELL_SENSE_LIFE, CLASS_CLERIC, 18);
  spell_level(SPELL_HARM, CLASS_CLERIC, 19);
  spell_level(SPELL_GROUP_HEAL, CLASS_CLERIC, 22);
  spell_level(SPELL_REMOVE_CURSE,    CLASS_CLERIC, 26);
  spell_level(SPELL_DIVINE_SHIELD,   CLASS_CLERIC, 90);
  spell_level(SPELL_MASS_PARALYSIS,  CLASS_CLERIC, 95);
  spell_level(SPELL_HOLY_WORD,       CLASS_CLERIC, 100);
  spell_level(SPELL_RESURRECTION,    CLASS_CLERIC, 85);

  /* THIEVES - 20 skills spread over levels 1-100 */
  spell_level(SKILL_SNEAK,         CLASS_THIEF, 1);
  spell_level(SKILL_PICK_LOCK,     CLASS_THIEF, 5);
  spell_level(SKILL_BACKSTAB,      CLASS_THIEF, 10);
  spell_level(SKILL_STEAL,         CLASS_THIEF, 15);
  spell_level(SKILL_HIDE,          CLASS_THIEF, 20);
  spell_level(SKILL_TRACK,         CLASS_THIEF, 25);
  spell_level(SKILL_DODGE,         CLASS_THIEF, 30);
  spell_level(SKILL_PEEK,          CLASS_THIEF, 35);
  spell_level(SKILL_CIRCLE,        CLASS_THIEF, 40);
  spell_level(SKILL_POISON_WEAPON, CLASS_THIEF, 45);
  spell_level(SKILL_SHADOW_STEP,   CLASS_THIEF, 50);
  spell_level(SKILL_DETECT_TRAP,   CLASS_THIEF, 55);
  spell_level(SKILL_IMPROVED_HIDE, CLASS_THIEF, 60);
  spell_level(SKILL_GARROTE,       CLASS_THIEF, 65);
  spell_level(SKILL_SHADOW_WALK,   CLASS_THIEF, 70);
  spell_level(SKILL_AMBUSH,        CLASS_THIEF, 75);
  spell_level(SKILL_DEATH_STRIKE,  CLASS_THIEF, 80);
  /* 3 open slots for future thief skills at 85, 90, 95 */

  /* WARRIORS - 20 skills spread over levels 1-100 */
  spell_level(SKILL_KICK,          CLASS_WARRIOR, 1);
  spell_level(SKILL_RESCUE,        CLASS_WARRIOR, 5);
  spell_level(SKILL_TRACK,         CLASS_WARRIOR, 10);
  spell_level(SKILL_BASH,          CLASS_WARRIOR, 15);
  spell_level(SKILL_PARRY,         CLASS_WARRIOR, 20);
  spell_level(SKILL_SHIELD_BLOCK,  CLASS_WARRIOR, 25);
  spell_level(SKILL_SECOND_ATTACK, CLASS_WARRIOR, 30);
  spell_level(SKILL_BERSERK,       CLASS_WARRIOR, 35);
  spell_level(SKILL_BATTLE_CRY,    CLASS_WARRIOR, 40);
  spell_level(SKILL_CLEAVE,        CLASS_WARRIOR, 45);
  spell_level(SKILL_CHARGE,        CLASS_WARRIOR, 50);
  spell_level(SKILL_THIRD_ATTACK,  CLASS_WARRIOR, 55);
  spell_level(SKILL_WHIRLWIND,     CLASS_WARRIOR, 60);
  spell_level(SKILL_INTIMIDATE,    CLASS_WARRIOR, 65);
  spell_level(SKILL_WAR_STOMP,     CLASS_WARRIOR, 70);
  spell_level(SKILL_FOURTH_ATTACK, CLASS_WARRIOR, 75);
  spell_level(SKILL_BLADE_STORM,   CLASS_WARRIOR, 80);
  spell_level(SKILL_EVASION,       CLASS_WARRIOR, 85);
  spell_level(SKILL_WARLORDS_MIGHT,CLASS_WARRIOR, 90);
  /* 1 open slot for future warrior skill at 95 */
}


/*
 * This is the exp given to implementors -- it must always be greater
 * than the exp required for immortality, plus at least 20,000 or so.
 * (Exp is a 32-bit int, so keep this well under 2,147,483,647.)
 */
#define EXP_MAX  1000000000

/*
 * Exp required for each mortal class/level, indexed [class][level].
 * The last entry (index LVL_IMMORT) is the exp needed for immortality.
 *
 * Levels 0-30 are the original CircleMUD 3.1 values.  From level 31 on,
 * each class follows  exp30 + inc30*d + k*d*d  (d = level - 30, inc30 =
 * the original 29->30 step, k chosen so that level 100 costs 30 times the
 * level-30 exp), rounded to the nearest 1000.  Tune as desired.
 */
static const int exp_table[NUM_CLASSES][LVL_IMMORT + 1] = {
  { /* CLASS_MAGIC_USER */
               0,          1,       2500,       5000,      10000,      20000,
           40000,      60000,      90000,     135000,     250000,     375000,
          750000,    1125000,    1500000,    1875000,    2250000,    2625000,
         3000000,    3375000,    3750000,    4000000,    4300000,    4600000,
         4900000,    5200000,    5500000,    5950000,    6400000,    6850000,
         7400000,    7986000,    8644000,    9373000,   10175000,   11048000,
        11994000,   13011000,   14100000,   15261000,   16494000,   17799000,
        19175000,   20624000,   22144000,   23736000,   25400000,   27136000,
        28944000,   30824000,   32776000,   34799000,   36894000,   39062000,
        41301000,   43612000,   45995000,   48449000,   50976000,   53575000,
        56245000,   58987000,   61801000,   64687000,   67645000,   70675000,
        73777000,   76950000,   80196000,   83513000,   86902000,   90363000,
        93896000,   97501000,  101177000,  104926000,  108746000,  112639000,
       116603000,  120639000,  124747000,  128927000,  133178000,  137502000,
       141897000,  146365000,  150904000,  155515000,  160198000,  164953000,
       169780000,  174678000,  179649000,  184691000,  189805000,  194991000,
       200249000,  205579000,  210981000,  216455000,  222000000,  227617000
  },
  { /* CLASS_CLERIC */
               0,          1,       1500,       3000,       6000,      13000,
           27500,      55000,     110000,     225000,     450000,     675000,
          900000,    1125000,    1350000,    1575000,    1800000,    2100000,
         2400000,    2700000,    3000000,    3250000,    3500000,    3800000,
         4100000,    4400000,    4800000,    5200000,    5600000,    6000000,
         6400000,    6832000,    7329000,    7889000,    8515000,    9204000,
         9958000,   10776000,   11658000,   12605000,   13616000,   14692000,
        15832000,   17036000,   18304000,   19637000,   21034000,   22495000,
        24021000,   25611000,   27265000,   28984000,   30767000,   32614000,
        34526000,   36502000,   38542000,   40647000,   42816000,   45049000,
        47347000,   49709000,   52135000,   54626000,   57181000,   59800000,
        62484000,   65232000,   68044000,   70920000,   73861000,   76866000,
        79936000,   83070000,   86268000,   89531000,   92857000,   96249000,
        99704000,  103224000,  106808000,  110457000,  114169000,  117947000,
       121788000,  125694000,  129664000,  133698000,  137797000,  141960000,
       146188000,  150480000,  154836000,  159256000,  163741000,  168290000,
       172903000,  177581000,  182323000,  187129000,  192000000,  196935000
  },
  { /* CLASS_THIEF */
               0,          1,       1250,       2500,       5000,      10000,
           20000,      40000,      70000,     110000,     160000,     220000,
          440000,     660000,     880000,    1100000,    1500000,    2000000,
         2500000,    3000000,    3500000,    3650000,    3800000,    4100000,
         4400000,    4700000,    5100000,    5500000,    5900000,    6300000,
         6650000,    7034000,    7487000,    8009000,    8600000,    9259000,
         9987000,   10784000,   11649000,   12583000,   13586000,   14657000,
        15797000,   17006000,   18284000,   19630000,   21045000,   22529000,
        24082000,   25703000,   27393000,   29152000,   30979000,   32875000,
        34840000,   36873000,   38975000,   41146000,   43386000,   45694000,
        48071000,   50517000,   53032000,   55615000,   58267000,   60988000,
        63777000,   66635000,   69562000,   72557000,   75621000,   78754000,
        81956000,   85226000,   88565000,   91973000,   95450000,   98995000,
       102609000,  106292000,  110043000,  113863000,  117752000,  121709000,
       125735000,  129830000,  133994000,  138226000,  142527000,  146897000,
       151336000,  155843000,  160419000,  165064000,  169777000,  174559000,
       179410000,  184329000,  189317000,  194374000,  199500000,  204694000
  },
  { /* CLASS_WARRIOR */
               0,          1,       2000,       4000,       8000,      16000,
           32000,      64000,     125000,     250000,     500000,     750000,
         1000000,    1250000,    1500000,    1850000,    2200000,    2550000,
         2900000,    3250000,    3600000,    3900000,    4200000,    4500000,
         4800000,    5150000,    5500000,    5950000,    6400000,    6850000,
         7400000,    7986000,    8644000,    9373000,   10175000,   11048000,
        11994000,   13011000,   14100000,   15261000,   16494000,   17799000,
        19175000,   20624000,   22144000,   23736000,   25400000,   27136000,
        28944000,   30824000,   32776000,   34799000,   36894000,   39062000,
        41301000,   43612000,   45995000,   48449000,   50976000,   53575000,
        56245000,   58987000,   61801000,   64687000,   67645000,   70675000,
        73777000,   76950000,   80196000,   83513000,   86902000,   90363000,
        93896000,   97501000,  101177000,  104926000,  108746000,  112639000,
       116603000,  120639000,  124747000,  128927000,  133178000,  137502000,
       141897000,  146365000,  150904000,  155515000,  160198000,  164953000,
       169780000,  174678000,  179649000,  184691000,  189805000,  194991000,
       200249000,  205579000,  210981000,  216455000,  222000000,  227617000
  },
};

/* Function to return the exp required for each class/level */
int level_exp(int chclass, int level)
{
  if (level > LVL_IMPL || level < 0) {
    log("SYSERR: Requesting exp for invalid level %d!", level);
    return 0;
  }

  /*
   * Gods have exp close to EXP_MAX.  This statement should never have to
   * changed, regardless of how many mortal or immortal levels exist.
   */
  if (level > LVL_IMMORT) {
    return EXP_MAX - ((LVL_IMPL - level) * 1000);
  }

  /* Exp required for normal mortals is below */
  if (chclass < 0 || chclass >= NUM_CLASSES) {
    /*
     * This statement should never be reached if the exp tables in this function
     * are set up properly.  If you see exp of 123456 then something is wrong.
     */
    log("SYSERR: XP tables not set up correctly in class.c!");
    return 123456;
  }

  return exp_table[chclass][level];
}


/* 
 * Default titles of male characters.
 */
const char *title_male(int chclass, int level)
{
  if (level <= 0 || level > LVL_IMPL)
    return "the Man";
  if (level == LVL_IMPL)
    return "the Implementor";
  if (level == LVL_LIMPL)
    return "the Lesser Implementor";

  switch (chclass) {

    case CLASS_MAGIC_USER:
    switch (level) {
      case  1: return "the Apprentice of Magic";
      case  2: return "the Spell Student";
      case  3: return "the Scholar of Magic";
      case  4: return "the Delver in Spells";
      case  5: return "the Medium of Magic";
      case  6: return "the Scribe of Magic";
      case  7: return "the Seer";
      case  8: return "the Sage";
      case  9: return "the Illusionist";
      case 10: return "the Abjurer";
      case 11: return "the Invoker";
      case 12: return "the Enchanter";
      case 13: return "the Conjurer";
      case 14: return "the Magician";
      case 15: return "the Creator";
      case 16: return "the Savant";
      case 17: return "the Magus";
      case 18: return "the Wizard";
      case 19: return "the Warlock";
      case 20: return "the Sorcerer";
      case 21: return "the Necromancer";
      case 22: return "the Thaumaturge";
      case 23: return "the Student of the Occult";
      case 24: return "the Disciple of the Uncanny";
      case 25: return "the Minor Elemental";
      case 26: return "the Greater Elemental";
      case 27: return "the Crafter of Magics";
      case 28: return "the Shaman";
      case 29: return "the Keeper of Talismans";
      case 30: return "the Archmage";
      case 31: return "the Adept of Arcana";
      case 32: return "the Weaver of Spells";
      case 33: return "the Master of Arcane Arts";
      case 34: return "the Spellbinder";
      case 35: return "the Runemaster";
      case 36: return "the Lord of Sorcery";
      case 37: return "the Conjurer Supreme";
      case 38: return "the Stormcaller";
      case 39: return "the Grand Magus";
      case 40: return "the Eldritch Scholar";
      case 41: return "the Wielder of Flame";
      case 42: return "the Frostcaller";
      case 43: return "the Binder of Elementals";
      case 44: return "the Planar Walker";
      case 45: return "the Keeper of Hidden Lore";
      case 46: return "the Mind Shaper";
      case 47: return "the Warden of the Veil";
      case 48: return "the Sage of Ages";
      case 49: return "the Eldritch Sage";
      case 50: return "the Magister of the Arcane";
      case 51: return "the Dreamweaver";
      case 52: return "the Starcaller";
      case 53: return "the Lorekeeper of Ages";
      case 54: return "the Rift Walker";
      case 55: return "the Keeper of Forbidden Lore";
      case 56: return "the Sunderer of Wards";
      case 57: return "the Shaper of Reality";
      case 58: return "the Oracle of Time";
      case 59: return "the Spellwright of Legend";
      case 60: return "the Arcane Luminary";
      case 61: return "the Voice of Thunder";
      case 62: return "the Master of the Elements";
      case 63: return "the Warlock King";
      case 64: return "the Lord of the Arcane Tower";
      case 65: return "the Archon of Sorcery";
      case 66: return "the Eternal Scholar";
      case 67: return "the Wyrd Weaver";
      case 68: return "the Timeless Sage";
      case 69: return "the Mage Ascendant";
      case 70: return "the Arcane Sovereign";
      case 71: return "the Shaper of Worlds";
      case 72: return "the Voice of the Void";
      case 73: return "the Lord of the Ninth Circle";
      case 74: return "the Spell Sovereign";
      case 75: return "the Living Grimoire";
      case 76: return "the Harbinger of Magic";
      case 77: return "the Master of the Weave";
      case 78: return "the Eldritch Monarch";
      case 79: return "the Wellspring of Power";
      case 80: return "the Arcane Paragon";
      case 81: return "the Breaker of Seals";
      case 82: return "the Architect of Magic";
      case 83: return "the Sage Eternal";
      case 84: return "the Sorcerer Supreme";
      case 85: return "the Lord of All Magic";
      case 86: return "the Soul of the Arcane";
      case 87: return "the Chosen of the Weave";
      case 88: return "the Greater Archmage";
      case 89: return "the Bane of Mortal Limits";
      case 90: return "the Magus Transcendent";
      case 91: return "the Keeper of the Final Spell";
      case 92: return "the Unraveler of Fate";
      case 93: return "the Worldshaper";
      case 94: return "the Pillar of Sorcery";
      case 95: return "the Voice of Creation";
      case 96: return "the Master of Time and Space";
      case 97: return "the Ascendant Archmage";
      case 98: return "the Archmage Eternal";
      case 99: return "the Supreme Archmage";
      case 100: return "the Demigod of Magic";
      case LVL_IMMORT: return "the Immortal Warlock";
      case LVL_GOD: return "the Avatar of Magic";
      case LVL_GRGOD: return "the God of Magic";
      default: return "the Mage";
    }
    break;

    case CLASS_CLERIC:
    switch (level) {
      case  1: return "the Believer";
      case  2: return "the Attendant";
      case  3: return "the Acolyte";
      case  4: return "the Novice";
      case  5: return "the Missionary";
      case  6: return "the Adept";
      case  7: return "the Deacon";
      case  8: return "the Vicar";
      case  9: return "the Priest";
      case 10: return "the Minister";
      case 11: return "the Canon";
      case 12: return "the Levite";
      case 13: return "the Curate";
      case 14: return "the Monk";
      case 15: return "the Healer";
      case 16: return "the Chaplain";
      case 17: return "the Expositor";
      case 18: return "the Bishop";
      case 19: return "the Arch Bishop";
      case 20: return "the Patriarch";
      case 21: return "the Cantor";
      case 22: return "the Almoner";
      case 23: return "the Provost";
      case 24: return "the Dean";
      case 25: return "the Monsignor";
      case 26: return "the Abbot";
      case 27: return "the Prior";
      case 28: return "the Vicar-General";
      case 29: return "the Primate";
      case 30: return "the Holy Father";
      case 31: return "the Elder of the Faith";
      case 32: return "the Shepherd of Souls";
      case 33: return "the High Priest";
      case 34: return "the Bearer of the Holy Word";
      case 35: return "the Prelate";
      case 36: return "the Keeper of the Flame";
      case 37: return "the Healer of Nations";
      case 38: return "the Hierophant";
      case 39: return "the Lightbringer";
      case 40: return "the Grand Patriarch";
      case 41: return "the Warden of the Temple";
      case 42: return "the Anointed One";
      case 43: return "the Sentinel of Faith";
      case 44: return "the Revered Confessor";
      case 45: return "the Voice of the Divine";
      case 46: return "the Beacon of Hope";
      case 47: return "the Judge of the Faithful";
      case 48: return "the Archbishop";
      case 49: return "the Cardinal of the Light";
      case 50: return "the Hand of Mercy";
      case 51: return "the Miracle Worker";
      case 52: return "the Blessed Healer";
      case 53: return "the Defender of the Faith";
      case 54: return "the Vessel of Grace";
      case 55: return "the Chosen of the Gods";
      case 56: return "the Prophet";
      case 57: return "the Seer of Holy Visions";
      case 58: return "the Bringer of Dawn";
      case 59: return "the Sanctified";
      case 60: return "the Holy Inquisitor";
      case 61: return "the Guardian of the Sacred Flame";
      case 62: return "the Ward Against Darkness";
      case 63: return "the Heavenly Herald";
      case 64: return "the Pontiff of the Realm";
      case 65: return "the Radiant Oracle";
      case 66: return "the Divine Healer";
      case 67: return "the Exalted Priest";
      case 68: return "the Venerable Saint";
      case 69: return "the Torch of Heaven";
      case 70: return "the Saint";
      case 71: return "the Beloved of the Gods";
      case 72: return "the Wrath of Heaven";
      case 73: return "the Right Hand of Heaven";
      case 74: return "the Grace Eternal";
      case 75: return "the Pillar of the Church";
      case 76: return "the Archpriest";
      case 77: return "the Thunder of the Righteous";
      case 78: return "the Celestial Emissary";
      case 79: return "the Paragon of Faith";
      case 80: return "the Living Saint";
      case 81: return "the Exarch of Light";
      case 82: return "the Bulwark Against Evil";
      case 83: return "the Sacred Sentinel";
      case 84: return "the Messenger of the Divine";
      case 85: return "the Holy Ascendant";
      case 86: return "the Soul of Mercy";
      case 87: return "the Crown of the Faithful";
      case 88: return "the Sanctified Avatar";
      case 89: return "the Eternal Flame";
      case 90: return "the Champion of Heaven";
      case 91: return "the Voice of the Seraphim";
      case 92: return "the Redeemer";
      case 93: return "the Radiance Eternal";
      case 94: return "the Blessed Ascendant";
      case 95: return "the Consecrated";
      case 96: return "the Lord of Light";
      case 97: return "the Divine Vessel";
      case 98: return "the Beatific";
      case 99: return "the Divine Champion";
      case 100: return "the Demigod of Faith";
      case LVL_IMMORT: return "the Immortal Cardinal";
      case LVL_GOD: return "the Inquisitor";
      case LVL_GRGOD: return "the God of good and evil";
      default: return "the Cleric";
    }
    break;

    case CLASS_THIEF:
    switch (level) {
      case  1: return "the Pilferer";
      case  2: return "the Footpad";
      case  3: return "the Filcher";
      case  4: return "the Pick-Pocket";
      case  5: return "the Sneak";
      case  6: return "the Pincher";
      case  7: return "the Cut-Purse";
      case  8: return "the Snatcher";
      case  9: return "the Sharper";
      case 10: return "the Rogue";
      case 11: return "the Robber";
      case 12: return "the Magsman";
      case 13: return "the Highwayman";
      case 14: return "the Burglar";
      case 15: return "the Thief";
      case 16: return "the Knifer";
      case 17: return "the Quick-Blade";
      case 18: return "the Killer";
      case 19: return "the Brigand";
      case 20: return "the Cut-Throat";
      case 21: return "the Housebreaker";
      case 22: return "the Swindler";
      case 23: return "the Smuggler";
      case 24: return "the Bandit";
      case 25: return "the Outlaw";
      case 26: return "the Rapscallion";
      case 27: return "the Shadow";
      case 28: return "the Assassin";
      case 29: return "the Master Rogue";
      case 30: return "the Master Assassin";
      case 31: return "the Silent Blade";
      case 32: return "the Night Prowler";
      case 33: return "the Master Thief";
      case 34: return "the Vault Breaker";
      case 35: return "the Shadow Stalker";
      case 36: return "the Shadow Lord";
      case 37: return "the Lockmaster";
      case 38: return "the Cloaked Menace";
      case 39: return "the Phantom";
      case 40: return "the Prince of Pickpockets";
      case 41: return "the Silent Death";
      case 42: return "the Grave Robber";
      case 43: return "the Dagger in the Dark";
      case 44: return "the Unseen Hand";
      case 45: return "the Whisper in the Dark";
      case 46: return "the Fence of Fortunes";
      case 47: return "the Guildmaster";
      case 48: return "the Nightblade";
      case 49: return "the Ghost of the Night";
      case 50: return "the Lord of Larceny";
      case 51: return "the Vanisher";
      case 52: return "the Heist Legend";
      case 53: return "the Poisoner";
      case 54: return "the Kingpin";
      case 55: return "the Spymaster";
      case 56: return "the Doom of Locks";
      case 57: return "the Trapmaster";
      case 58: return "the Ghost of the Rooftops";
      case 59: return "the Cloak of Midnight";
      case 60: return "the Legend of the Underworld";
      case 61: return "the Shade";
      case 62: return "the Silent Assassin";
      case 63: return "the Master of Disguise";
      case 64: return "the Black Hand";
      case 65: return "the Lord of Thieves";
      case 66: return "the Thief of Legends";
      case 67: return "the Crime Lord";
      case 68: return "the Mist Walker";
      case 69: return "the Unseen Death";
      case 70: return "the Grandmaster Thief";
      case 71: return "the Merchant of Shadows";
      case 72: return "the Eclipse Blade";
      case 73: return "the Ruler of the Underworld";
      case 74: return "the Blade of Midnight";
      case 75: return "the Untouchable";
      case 76: return "the Whisper of Doom";
      case 77: return "the Shadow Sovereign";
      case 78: return "the Master of Knives";
      case 79: return "the Thief Eternal";
      case 80: return "the Dark Paragon";
      case 81: return "the Phantom Blade";
      case 82: return "the King of Thieves";
      case 83: return "the Ghost King";
      case 84: return "the Emperor of Shadows";
      case 85: return "the Vanishing Legend";
      case 86: return "the Perfect Thief";
      case 87: return "the Death Unseen";
      case 88: return "the Night's Embrace";
      case 89: return "the Stealer of Stars";
      case 90: return "the Last Shadow";
      case 91: return "the Master of the Midnight Court";
      case 92: return "the Shadow Incarnate";
      case 93: return "the Unmatched Rogue";
      case 94: return "the Dark Sovereign";
      case 95: return "the Thief Supreme";
      case 96: return "the Voice of Silence";
      case 97: return "the Lord of Shadows";
      case 98: return "the Darkness Itself";
      case 99: return "the Prince of Thieves";
      case 100: return "the Demigod of Thieves";
      case LVL_IMMORT: return "the Immortal Assasin";
      case LVL_GOD: return "the Demi God of thieves";
      case LVL_GRGOD: return "the God of thieves and tradesmen";
      default: return "the Thief";
    }
    break;

    case CLASS_WARRIOR:
    switch(level) {
      case  1: return "the Swordpupil";
      case  2: return "the Recruit";
      case  3: return "the Sentry";
      case  4: return "the Fighter";
      case  5: return "the Soldier";
      case  6: return "the Warrior";
      case  7: return "the Veteran";
      case  8: return "the Swordsman";
      case  9: return "the Fencer";
      case 10: return "the Combatant";
      case 11: return "the Hero";
      case 12: return "the Myrmidon";
      case 13: return "the Swashbuckler";
      case 14: return "the Mercenary";
      case 15: return "the Swordmaster";
      case 16: return "the Lieutenant";
      case 17: return "the Champion";
      case 18: return "the Dragoon";
      case 19: return "the Cavalier";
      case 20: return "the Knight";
      case 21: return "the Bannerman";
      case 22: return "the Man-at-Arms";
      case 23: return "the Gladiator";
      case 24: return "the Centurion";
      case 25: return "the Crusader";
      case 26: return "the Templar";
      case 27: return "the Captain of War";
      case 28: return "the Warden";
      case 29: return "the Knight Errant";
      case 30: return "the Paladin";
      case 31: return "the Veteran Champion";
      case 32: return "the Blademaster";
      case 33: return "the Warlord";
      case 34: return "the Battle Captain";
      case 35: return "the Slayer";
      case 36: return "the Battle Lord";
      case 37: return "the Knight Commander";
      case 38: return "the Shield of the Realm";
      case 39: return "the Marshal of War";
      case 40: return "the Iron Champion";
      case 41: return "the Dragon Hunter";
      case 42: return "the Giant Slayer";
      case 43: return "the Banner Bearer";
      case 44: return "the Bane of Armies";
      case 45: return "the Conqueror";
      case 46: return "the Siege Breaker";
      case 47: return "the Hero of the Realm";
      case 48: return "the War Chief";
      case 49: return "the Warmaster";
      case 50: return "the Scourge of Armies";
      case 51: return "the Unyielding";
      case 52: return "the Steel Sentinel";
      case 53: return "the Grand Marshal";
      case 54: return "the Doom Bringer";
      case 55: return "the Crusher of Legions";
      case 56: return "the Lord of Battle";
      case 57: return "the Champion of Champions";
      case 58: return "the Thunder of War";
      case 59: return "the Warden of the Realm";
      case 60: return "the Legend of War";
      case 61: return "the Immovable Wall";
      case 62: return "the Dread Commander";
      case 63: return "the Shatterer of Shields";
      case 64: return "the Crimson Knight";
      case 65: return "the General of Generals";
      case 66: return "the Victorious";
      case 67: return "the Titan Slayer";
      case 68: return "the Iron Lord";
      case 69: return "the Unconquered";
      case 70: return "the Warrior King";
      case 71: return "the Storm of Steel";
      case 72: return "the Peerless Blade";
      case 73: return "the Last Line of Defense";
      case 74: return "the Wrath of the Battlefield";
      case 75: return "the Hero Eternal";
      case 76: return "the Overlord of War";
      case 77: return "the Mountain Breaker";
      case 78: return "the Sword of Kings";
      case 79: return "the Terror of the Field";
      case 80: return "the Paragon of War";
      case 81: return "the Fist of the Realm";
      case 82: return "the Dragonbane";
      case 83: return "the Unstoppable";
      case 84: return "the Emperor of War";
      case 85: return "the Eternal Champion";
      case 86: return "the Bringer of Ruin";
      case 87: return "the Warhammer of the Gods";
      case 88: return "the Lord of Legions";
      case 89: return "the Blade Eternal";
      case 90: return "the Undefeated";
      case 91: return "the Colossus of War";
      case 92: return "the Vanquisher of Hosts";
      case 93: return "the Master of a Thousand Battles";
      case 94: return "the Warlord Eternal";
      case 95: return "the Fury Incarnate";
      case 96: return "the Sovereign of War";
      case 97: return "the Champion Ascendant";
      case 98: return "the Hero of Ages";
      case 99: return "the Unbroken";
      case 100: return "the Demigod of War";
      case LVL_IMMORT: return "the Immortal Warlord";
      case LVL_GOD: return "the Extirpator";
      case LVL_GRGOD: return "the God of war";
      default: return "the Warrior";
    }
    break;
  }

  /* Default title for classes which do not have titles defined */
  return "the Classless";
}


/* 
 * Default titles of female characters.
 */
const char *title_female(int chclass, int level)
{
  if (level <= 0 || level > LVL_IMPL)
    return "the Woman";
  if (level == LVL_IMPL)
    return "the Implementress";
  if (level == LVL_LIMPL)
    return "the Lesser Implementress";

  switch (chclass) {

    case CLASS_MAGIC_USER:
    switch (level) {
      case  1: return "the Apprentice of Magic";
      case  2: return "the Spell Student";
      case  3: return "the Scholar of Magic";
      case  4: return "the Delveress in Spells";
      case  5: return "the Medium of Magic";
      case  6: return "the Scribess of Magic";
      case  7: return "the Seeress";
      case  8: return "the Sage";
      case  9: return "the Illusionist";
      case 10: return "the Abjuress";
      case 11: return "the Invoker";
      case 12: return "the Enchantress";
      case 13: return "the Conjuress";
      case 14: return "the Witch";
      case 15: return "the Creator";
      case 16: return "the Savant";
      case 17: return "the Craftess";
      case 18: return "the Wizard";
      case 19: return "the War Witch";
      case 20: return "the Sorceress";
      case 21: return "the Necromancress";
      case 22: return "the Thaumaturgess";
      case 23: return "the Student of the Occult";
      case 24: return "the Disciple of the Uncanny";
      case 25: return "the Minor Elementress";
      case 26: return "the Greater Elementress";
      case 27: return "the Crafter of Magics";
      case 28: return "Shaman";
      case 29: return "the Keeper of Talismans";
      case 30: return "Archwitch";
      case 31: return "the Adept of Arcana";
      case 32: return "the Weaver of Spells";
      case 33: return "the Mistress of Arcane Arts";
      case 34: return "the Spellbinder";
      case 35: return "the Runemistress";
      case 36: return "the Lady of Sorcery";
      case 37: return "the Conjurer Supreme";
      case 38: return "the Stormcaller";
      case 39: return "the Grand Enchantress";
      case 40: return "the Eldritch Scholar";
      case 41: return "the Wielder of Flame";
      case 42: return "the Frostcaller";
      case 43: return "the Binder of Elementals";
      case 44: return "the Planar Walker";
      case 45: return "the Keeper of Hidden Lore";
      case 46: return "the Mind Shaper";
      case 47: return "the Warden of the Veil";
      case 48: return "the Sage of Ages";
      case 49: return "the Eldritch Sage";
      case 50: return "the Magistra of the Arcane";
      case 51: return "the Dreamweaver";
      case 52: return "the Starcaller";
      case 53: return "the Lorekeeper of Ages";
      case 54: return "the Rift Walker";
      case 55: return "the Keeper of Forbidden Lore";
      case 56: return "the Sunderer of Wards";
      case 57: return "the Shaper of Reality";
      case 58: return "the Oracle of Time";
      case 59: return "the Spellwright of Legend";
      case 60: return "the Arcane Luminary";
      case 61: return "the Voice of Thunder";
      case 62: return "the Mistress of the Elements";
      case 63: return "the Warlock Queen";
      case 64: return "the Lady of the Arcane Tower";
      case 65: return "the Archon of Sorcery";
      case 66: return "the Eternal Scholar";
      case 67: return "the Wyrd Weaver";
      case 68: return "the Timeless Sage";
      case 69: return "the Mage Ascendant";
      case 70: return "the Arcane Sovereign";
      case 71: return "the Shaper of Worlds";
      case 72: return "the Voice of the Void";
      case 73: return "the Lady of the Ninth Circle";
      case 74: return "the Spell Sovereign";
      case 75: return "the Living Grimoire";
      case 76: return "the Harbinger of Magic";
      case 77: return "the Mistress of the Weave";
      case 78: return "the Eldritch Monarch";
      case 79: return "the Wellspring of Power";
      case 80: return "the Arcane Paragon";
      case 81: return "the Breaker of Seals";
      case 82: return "the Architect of Magic";
      case 83: return "the Sage Eternal";
      case 84: return "the Sorceress Supreme";
      case 85: return "the Lady of All Magic";
      case 86: return "the Soul of the Arcane";
      case 87: return "the Chosen of the Weave";
      case 88: return "the Greater Archmage";
      case 89: return "the Bane of Mortal Limits";
      case 90: return "the Magus Transcendent";
      case 91: return "the Keeper of the Final Spell";
      case 92: return "the Unraveler of Fate";
      case 93: return "the Worldshaper";
      case 94: return "the Pillar of Sorcery";
      case 95: return "the Voice of Creation";
      case 96: return "the Mistress of Time and Space";
      case 97: return "the Ascendant Archmage";
      case 98: return "the Archmage Eternal";
      case 99: return "the Supreme Archmage";
      case 100: return "the Demigoddess of Magic";
      case LVL_IMMORT: return "the Immortal Enchantress";
      case LVL_GOD: return "the Empress of Magic";
      case LVL_GRGOD: return "the Goddess of Magic";
      default: return "the Witch";
    }
    break;

    case CLASS_CLERIC:
    switch (level) {
      case  1: return "the Believer";
      case  2: return "the Attendant";
      case  3: return "the Acolyte";
      case  4: return "the Novice";
      case  5: return "the Missionary";
      case  6: return "the Adept";
      case  7: return "the Deaconess";
      case  8: return "the Vicaress";
      case  9: return "the Priestess";
      case 10: return "the Lady Minister";
      case 11: return "the Canon";
      case 12: return "the Levitess";
      case 13: return "the Curess";
      case 14: return "the Nunne";
      case 15: return "the Healess";
      case 16: return "the Chaplain";
      case 17: return "the Expositress";
      case 18: return "the Bishop";
      case 19: return "the Arch Lady of the Church";
      case 20: return "the Matriarch";
      case 21: return "the Cantor";
      case 22: return "the Almoner";
      case 23: return "the Provost";
      case 24: return "the Dean";
      case 25: return "the Monsignor";
      case 26: return "the Abbess";
      case 27: return "the Prioress";
      case 28: return "the Vicar-General";
      case 29: return "the Primate";
      case 30: return "the Holy Mother";
      case 31: return "the Elder of the Faith";
      case 32: return "the Shepherd of Souls";
      case 33: return "the High Priestess";
      case 34: return "the Bearer of the Holy Word";
      case 35: return "the Prelate";
      case 36: return "the Keeper of the Flame";
      case 37: return "the Healer of Nations";
      case 38: return "the Hierophant";
      case 39: return "the Lightbringer";
      case 40: return "the Grand Matriarch";
      case 41: return "the Warden of the Temple";
      case 42: return "the Anointed One";
      case 43: return "the Sentinel of Faith";
      case 44: return "the Revered Confessor";
      case 45: return "the Voice of the Divine";
      case 46: return "the Beacon of Hope";
      case 47: return "the Judge of the Faithful";
      case 48: return "the Archbishop";
      case 49: return "the Cardinal of the Light";
      case 50: return "the Hand of Mercy";
      case 51: return "the Miracle Worker";
      case 52: return "the Blessed Healer";
      case 53: return "the Defender of the Faith";
      case 54: return "the Vessel of Grace";
      case 55: return "the Chosen of the Gods";
      case 56: return "the Prophetess";
      case 57: return "the Seer of Holy Visions";
      case 58: return "the Bringer of Dawn";
      case 59: return "the Sanctified";
      case 60: return "the Holy Inquisitor";
      case 61: return "the Guardian of the Sacred Flame";
      case 62: return "the Ward Against Darkness";
      case 63: return "the Heavenly Herald";
      case 64: return "the Pontiff of the Realm";
      case 65: return "the Radiant Oracle";
      case 66: return "the Divine Healer";
      case 67: return "the Exalted Priestess";
      case 68: return "the Venerable Saint";
      case 69: return "the Torch of Heaven";
      case 70: return "the Saint";
      case 71: return "the Beloved of the Gods";
      case 72: return "the Wrath of Heaven";
      case 73: return "the Right Hand of Heaven";
      case 74: return "the Grace Eternal";
      case 75: return "the Pillar of the Church";
      case 76: return "the Archpriestess";
      case 77: return "the Thunder of the Righteous";
      case 78: return "the Celestial Emissary";
      case 79: return "the Paragon of Faith";
      case 80: return "the Living Saint";
      case 81: return "the Exarch of Light";
      case 82: return "the Bulwark Against Evil";
      case 83: return "the Sacred Sentinel";
      case 84: return "the Messenger of the Divine";
      case 85: return "the Holy Ascendant";
      case 86: return "the Soul of Mercy";
      case 87: return "the Crown of the Faithful";
      case 88: return "the Sanctified Avatar";
      case 89: return "the Eternal Flame";
      case 90: return "the Champion of Heaven";
      case 91: return "the Voice of the Seraphim";
      case 92: return "the Redeemer";
      case 93: return "the Radiance Eternal";
      case 94: return "the Blessed Ascendant";
      case 95: return "the Consecrated";
      case 96: return "the Lady of Light";
      case 97: return "the Divine Vessel";
      case 98: return "the Beatific";
      case 99: return "the Divine Champion";
      case 100: return "the Demigoddess of Faith";
      case LVL_IMMORT: return "the Immortal Priestess";
      case LVL_GOD: return "the Inquisitress";
      case LVL_GRGOD: return "the Goddess of good and evil";
      default: return "the Cleric";
    }
    break;

    case CLASS_THIEF:
    switch (level) {
      case  1: return "the Pilferess";
      case  2: return "the Footpad";
      case  3: return "the Filcheress";
      case  4: return "the Pick-Pocket";
      case  5: return "the Sneak";
      case  6: return "the Pincheress";
      case  7: return "the Cut-Purse";
      case  8: return "the Snatcheress";
      case  9: return "the Sharpress";
      case 10: return "the Rogue";
      case 11: return "the Robber";
      case 12: return "the Magswoman";
      case 13: return "the Highwaywoman";
      case 14: return "the Burglaress";
      case 15: return "the Thief";
      case 16: return "the Knifer";
      case 17: return "the Quick-Blade";
      case 18: return "the Murderess";
      case 19: return "the Brigand";
      case 20: return "the Cut-Throat";
      case 21: return "the Housebreaker";
      case 22: return "the Swindler";
      case 23: return "the Smuggler";
      case 24: return "the Bandit";
      case 25: return "the Outlaw";
      case 26: return "the Rapscallion";
      case 27: return "the Shadow";
      case 28: return "the Assassin";
      case 29: return "the Mistress Rogue";
      case 30: return "the Mistress Assassin";
      case 31: return "the Silent Blade";
      case 32: return "the Night Prowler";
      case 33: return "the Master Thief";
      case 34: return "the Vault Breaker";
      case 35: return "the Shadow Stalker";
      case 36: return "the Shadow Lady";
      case 37: return "the Lockmaster";
      case 38: return "the Cloaked Menace";
      case 39: return "the Phantom";
      case 40: return "the Princess of Pickpockets";
      case 41: return "the Silent Death";
      case 42: return "the Grave Robber";
      case 43: return "the Dagger in the Dark";
      case 44: return "the Unseen Hand";
      case 45: return "the Whisper in the Dark";
      case 46: return "the Fence of Fortunes";
      case 47: return "the Guildmaster";
      case 48: return "the Nightblade";
      case 49: return "the Ghost of the Night";
      case 50: return "the Lady of Larceny";
      case 51: return "the Vanisher";
      case 52: return "the Heist Legend";
      case 53: return "the Poisoner";
      case 54: return "the Queenpin";
      case 55: return "the Spymaster";
      case 56: return "the Doom of Locks";
      case 57: return "the Trapmaster";
      case 58: return "the Ghost of the Rooftops";
      case 59: return "the Cloak of Midnight";
      case 60: return "the Legend of the Underworld";
      case 61: return "the Shade";
      case 62: return "the Silent Assassin";
      case 63: return "the Mistress of Disguise";
      case 64: return "the Black Hand";
      case 65: return "the Lady of Thieves";
      case 66: return "the Thief of Legends";
      case 67: return "the Crime Lady";
      case 68: return "the Mist Walker";
      case 69: return "the Unseen Death";
      case 70: return "the Grandmaster Thief";
      case 71: return "the Merchant of Shadows";
      case 72: return "the Eclipse Blade";
      case 73: return "the Ruler of the Underworld";
      case 74: return "the Blade of Midnight";
      case 75: return "the Untouchable";
      case 76: return "the Whisper of Doom";
      case 77: return "the Shadow Sovereign";
      case 78: return "the Mistress of Knives";
      case 79: return "the Thief Eternal";
      case 80: return "the Dark Paragon";
      case 81: return "the Phantom Blade";
      case 82: return "the Queen of Thieves";
      case 83: return "the Ghost Queen";
      case 84: return "the Empress of Shadows";
      case 85: return "the Vanishing Legend";
      case 86: return "the Perfect Thief";
      case 87: return "the Death Unseen";
      case 88: return "the Night's Embrace";
      case 89: return "the Stealer of Stars";
      case 90: return "the Last Shadow";
      case 91: return "the Mistress of the Midnight Court";
      case 92: return "the Shadow Incarnate";
      case 93: return "the Unmatched Rogue";
      case 94: return "the Dark Sovereign";
      case 95: return "the Thief Supreme";
      case 96: return "the Voice of Silence";
      case 97: return "the Lady of Shadows";
      case 98: return "the Darkness Itself";
      case 99: return "the Princess of Thieves";
      case 100: return "the Demigoddess of Thieves";
      case LVL_IMMORT: return "the Immortal Assasin";
      case LVL_GOD: return "the Demi Goddess of thieves";
      case LVL_GRGOD: return "the Goddess of thieves and tradesmen";
      default: return "the Thief";
    }
    break;

    case CLASS_WARRIOR:
    switch(level) {
      case  1: return "the Swordpupil";
      case  2: return "the Recruit";
      case  3: return "the Sentress";
      case  4: return "the Fighter";
      case  5: return "the Soldier";
      case  6: return "the Warrior";
      case  7: return "the Veteran";
      case  8: return "the Swordswoman";
      case  9: return "the Fenceress";
      case 10: return "the Combatess";
      case 11: return "the Heroine";
      case 12: return "the Myrmidon";
      case 13: return "the Swashbuckleress";
      case 14: return "the Mercenaress";
      case 15: return "the Swordmistress";
      case 16: return "the Lieutenant";
      case 17: return "the Lady Champion";
      case 18: return "the Lady Dragoon";
      case 19: return "the Cavalier";
      case 20: return "the Lady Knight";
      case 21: return "the Bannerman";
      case 22: return "the Woman-at-Arms";
      case 23: return "the Gladiator";
      case 24: return "the Centurion";
      case 25: return "the Crusader";
      case 26: return "the Templar";
      case 27: return "the Captain of War";
      case 28: return "the Warden";
      case 29: return "the Lady Errant";
      case 30: return "the Paladin";
      case 31: return "the Veteran Champion";
      case 32: return "the Blademaster";
      case 33: return "the Warlord";
      case 34: return "the Battle Captain";
      case 35: return "the Slayer";
      case 36: return "the Battle Lady";
      case 37: return "the Knight Commander";
      case 38: return "the Shield of the Realm";
      case 39: return "the Marshal of War";
      case 40: return "the Iron Champion";
      case 41: return "the Dragon Hunter";
      case 42: return "the Giant Slayer";
      case 43: return "the Banner Bearer";
      case 44: return "the Bane of Armies";
      case 45: return "the Conqueror";
      case 46: return "the Siege Breaker";
      case 47: return "the Hero of the Realm";
      case 48: return "the War Chief";
      case 49: return "the Warmaster";
      case 50: return "the Scourge of Armies";
      case 51: return "the Unyielding";
      case 52: return "the Steel Sentinel";
      case 53: return "the Grand Marshal";
      case 54: return "the Doom Bringer";
      case 55: return "the Crusher of Legions";
      case 56: return "the Lady of Battle";
      case 57: return "the Champion of Champions";
      case 58: return "the Thunder of War";
      case 59: return "the Warden of the Realm";
      case 60: return "the Legend of War";
      case 61: return "the Immovable Wall";
      case 62: return "the Dread Commander";
      case 63: return "the Shatterer of Shields";
      case 64: return "the Crimson Knight";
      case 65: return "the General of Generals";
      case 66: return "the Victorious";
      case 67: return "the Titan Slayer";
      case 68: return "the Iron Lady";
      case 69: return "the Unconquered";
      case 70: return "the Warrior Queen";
      case 71: return "the Storm of Steel";
      case 72: return "the Peerless Blade";
      case 73: return "the Last Line of Defense";
      case 74: return "the Wrath of the Battlefield";
      case 75: return "the Hero Eternal";
      case 76: return "the Overlord of War";
      case 77: return "the Mountain Breaker";
      case 78: return "the Sword of Kings";
      case 79: return "the Terror of the Field";
      case 80: return "the Paragon of War";
      case 81: return "the Fist of the Realm";
      case 82: return "the Dragonbane";
      case 83: return "the Unstoppable";
      case 84: return "the Empress of War";
      case 85: return "the Eternal Champion";
      case 86: return "the Bringer of Ruin";
      case 87: return "the Warhammer of the Gods";
      case 88: return "the Lady of Legions";
      case 89: return "the Blade Eternal";
      case 90: return "the Undefeated";
      case 91: return "the Colossus of War";
      case 92: return "the Vanquisher of Hosts";
      case 93: return "the Mistress of a Thousand Battles";
      case 94: return "the Warlord Eternal";
      case 95: return "the Fury Incarnate";
      case 96: return "the Sovereign of War";
      case 97: return "the Champion Ascendant";
      case 98: return "the Hero of Ages";
      case 99: return "the Unbroken";
      case 100: return "the Demigoddess of War";
      case LVL_IMMORT: return "the Immortal Lady of War";
      case LVL_GOD: return "the Queen of Destruction";
      case LVL_GRGOD: return "the Goddess of war";
      default: return "the Warrior";
    }
    break;
  }

  /* Default title for classes which do not have titles defined */
  return "the Classless";
}

