/* ************************************************************************
*  new_skills.c -- Thief and Warrior skill implementations                *
*  Elden Realms custom content for CircleMUD 3.1                          *
************************************************************************ */

#include "conf.h"
#include "sysdep.h"
#include "structs.h"
#include "utils.h"
#include "comm.h"
#include "interpreter.h"
#include "handler.h"
#include "db.h"
#include "spells.h"

extern struct room_data *world;
extern const char *dirs[];
void look_at_room(struct char_data *ch, int ignore_brief);
int mag_savingthrow(struct char_data *ch, int type, int modifier);
int House_can_enter(struct char_data *ch, room_vnum house);
int num_pc_in_room(struct room_data *room);
SPECIAL(shop_keeper);

/*
 * Hit, miss and death messages for the damaging skills live in
 * lib/misc/messages, like kick and backstab; damage() prints them.
 */

/* Shopkeepers and the caster's own pets are left out of room-wide skills. */
static int skip_room_target(struct char_data *ch, struct char_data *vict)
{
  if (vict == ch || !IS_NPC(vict))
    return (TRUE);
  if (AFF_FLAGGED(vict, AFF_CHARM) && vict->master == ch)
    return (TRUE);
  if (GET_MOB_RNUM(vict) != NOBODY && mob_index[GET_MOB_RNUM(vict)].func == shop_keeper)
    return (TRUE);
  return (FALSE);
}

/* ===================================================================
 * THIEF SKILLS
 * =================================================================== */

int peaceful_blocks(struct char_data *ch, struct char_data *victim);

ACMD(do_dodge)
{
  /* Passive skill; this command just informs the player of their rating */
  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_DODGE)) {
    send_to_char(ch, "You have no idea how to dodge attacks.\r\n");
    return;
  }
  send_to_char(ch, "Your dodge skill rating is %d%%.\r\n",
               GET_SKILL(ch, SKILL_DODGE));
}


ACMD(do_peek)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;
  struct obj_data *obj;
  int percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_PEEK)) {
    send_to_char(ch, "You have no idea how to peek at someone's inventory.\r\n");
    return;
  }
  one_argument(argument, arg);
  if (!*arg) {
    send_to_char(ch, "Peek at whose inventory?\r\n");
    return;
  }
  if (!(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
    send_to_char(ch, "You don't see that person here.\r\n");
    return;
  }
  if (vict == ch) {
    send_to_char(ch, "You peek at your own inventory — no surprise there.\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_PEEK);

  if (percent > prob) {
    send_to_char(ch, "You fail to get a good look at %s's belongings.\r\n",
                 GET_NAME(vict));
    return;
  }

  send_to_char(ch, "You peek at %s's inventory:\r\n", GET_NAME(vict));
  for (obj = vict->carrying; obj; obj = obj->next_content)
    if (CAN_SEE_OBJ(ch, obj))
      send_to_char(ch, "  %s\r\n", obj->short_description);
}


ACMD(do_circle)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;
  int dam, percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_CIRCLE)) {
    send_to_char(ch, "You have no idea how to circle behind a foe.\r\n");
    return;
  }
  one_argument(argument, arg);

  if (FIGHTING(ch)) {
    vict = FIGHTING(ch);
  } else {
    if (!*arg) {
      send_to_char(ch, "Circle behind whom?\r\n");
      return;
    }
    if (!(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
      send_to_char(ch, "Circle behind whom?\r\n");
      return;
    }
  }
  if (vict == ch) {
    send_to_char(ch, "Circle behind yourself? Really?\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_CIRCLE);

  if (percent > prob)
    damage(ch, vict, 0, SKILL_CIRCLE);
  else {
    dam = GET_LEVEL(ch) / 2 + dice(2, 6);
    damage(ch, vict, dam, SKILL_CIRCLE);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_poison_weapon)
{
  struct obj_data *weapon;
  int percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_POISON_WEAPON)) {
    send_to_char(ch, "You have no idea how to poison a weapon.\r\n");
    return;
  }

  weapon = GET_EQ(ch, WEAR_WIELD);
  if (!weapon) {
    send_to_char(ch, "You need to be wielding a weapon to poison it.\r\n");
    return;
  }

  if (GET_OBJ_TYPE(weapon) != ITEM_WEAPON) {
    send_to_char(ch, "You can only poison a real weapon.\r\n");
    return;
  }
  /*
   * The poison is an affect on the thief, not a value on the object: weapon
   * value 3 is the attack type (slash, pierce...) and must not be touched.
   * fight.c applies the poison on hits while the affect lasts.
   */
  if (affected_by_spell(ch, SKILL_POISON_WEAPON)) {
    send_to_char(ch, "Your weapon is already coated with poison.\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_POISON_WEAPON);

  if (percent > prob) {
    send_to_char(ch, "Your hands slip and you accidentally nick yourself!\r\n");
    if (!peaceful_blocks(ch, ch))
      GET_HIT(ch) = MAX(1, GET_HIT(ch) - dice(1, 4));
    update_pos(ch);
  } else {
    struct affected_type af;

    af.type = SKILL_POISON_WEAPON;
    af.duration = 1 + GET_SKILL(ch, SKILL_POISON_WEAPON) / 25;
    af.modifier = 0;
    af.location = APPLY_NONE;
    af.bitvector = 0;
    affect_to_char(ch, &af);
    send_to_char(ch, "You carefully coat %s with deadly poison.\r\n",
                 weapon->short_description);
    act("$n carefully coats $p with a dark substance.",
        TRUE, ch, weapon, 0, TO_ROOM);
  }
}


ACMD(do_shadow_step)
{
  char arg[MAX_INPUT_LENGTH];
  int dir;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_SHADOW_STEP)) {
    send_to_char(ch, "You don't know how to shadow step.\r\n");
    return;
  }
  one_argument(argument, arg);
  if (!*arg) {
    send_to_char(ch, "Shadow step in which direction?\r\n");
    return;
  }
  if ((dir = search_block(arg, dirs, FALSE)) < 0) {
    send_to_char(ch, "That's not a direction.\r\n");
    return;
  }
  if (!EXIT(ch, dir) || EXIT(ch, dir)->to_room == NOWHERE) {
    send_to_char(ch, "There's no exit in that direction.\r\n");
    return;
  }
  if (AFF_FLAGGED(ch, AFF_PARALYZE)) {
    send_to_char(ch, "You are paralyzed and cannot move!\r\n");
    return;
  }
  /* Shadows don't pass through doors, and don't break the rules of rooms. */
  if (EXIT_FLAGGED(EXIT(ch, dir), EX_CLOSED)) {
    send_to_char(ch, "The way is closed.\r\n");
    return;
  }
  if (ROOM_FLAGGED(IN_ROOM(ch), ROOM_ATRIUM) &&
      !House_can_enter(ch, GET_ROOM_VNUM(EXIT(ch, dir)->to_room))) {
    send_to_char(ch, "That's private property -- no trespassing!\r\n");
    return;
  }
  if (ROOM_FLAGGED(EXIT(ch, dir)->to_room, ROOM_TUNNEL) &&
      num_pc_in_room(&(world[EXIT(ch, dir)->to_room])) >= CONFIG_TUNNEL_SIZE) {
    send_to_char(ch, "There isn't enough room for you to go there!\r\n");
    return;
  }
  if (ROOM_FLAGGED(EXIT(ch, dir)->to_room, ROOM_GODROOM) && GET_LEVEL(ch) < LVL_GRGOD) {
    send_to_char(ch, "You aren't godly enough to use that room!\r\n");
    return;
  }
  if (ROOM_FLAGGED(EXIT(ch, dir)->to_room, ROOM_DEATH) && GET_LEVEL(ch) < LVL_IMMORT) {
    send_to_char(ch, "The shadows there are deadly; you dare not step into them.\r\n");
    return;
  }

  if (rand_number(1, 101) > GET_SKILL(ch, SKILL_SHADOW_STEP)) {
    send_to_char(ch, "You fail to merge with the shadows and stumble.\r\n");
  } else {
    /*
     * Read the destination before leaving: after char_from_room() the
     * character is in NOWHERE and EXIT(ch, dir) would index world[-1].
     */
    room_rnum dest = EXIT(ch, dir)->to_room;

    act("$n melts into the shadows and vanishes!", TRUE, ch, 0, 0, TO_ROOM);
    char_from_room(ch);
    char_to_room(ch, dest);
    act("$n steps out of the shadows!", TRUE, ch, 0, 0, TO_ROOM);
    look_at_room(ch, 0);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE);
}


ACMD(do_detect_trap)
{
  struct obj_data *obj;
  int found = FALSE;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_DETECT_TRAP)) {
    send_to_char(ch, "You have no idea how to detect traps.\r\n");
    return;
  }

  if (rand_number(1, 101) > GET_SKILL(ch, SKILL_DETECT_TRAP)) {
    send_to_char(ch, "You carefully examine the area but find nothing suspicious.\r\n");
    return;
  }

  for (obj = world[IN_ROOM(ch)].contents; obj; obj = obj->next_content) {
    if (GET_OBJ_TYPE(obj) == ITEM_TRAP) {
      send_to_char(ch, "You spot a trap: %s!\r\n", obj->short_description);
      found = TRUE;
    }
  }
  if (!found)
    send_to_char(ch, "You carefully examine the area and find no traps.\r\n");
}


ACMD(do_improved_hide)
{
  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_IMPROVED_HIDE)) {
    send_to_char(ch, "You don't know how to conceal yourself that well.\r\n");
    return;
  }

  if (AFF_FLAGGED(ch, AFF_HIDE)) {
    send_to_char(ch, "You are already hidden.\r\n");
    return;
  }

  if (rand_number(1, 101) <= GET_SKILL(ch, SKILL_IMPROVED_HIDE)) {
    SET_BIT(AFF_FLAGS(ch), AFF_HIDE);
    send_to_char(ch, "You melt into the shadows.\r\n");
  } else {
    send_to_char(ch, "You fail to conceal yourself.\r\n");
  }
}


ACMD(do_garrote)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;
  int dam, percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_GARROTE)) {
    send_to_char(ch, "You have no idea how to garrote someone.\r\n");
    return;
  }
  one_argument(argument, arg);
  if (!*arg) {
    send_to_char(ch, "Garrote whom?\r\n");
    return;
  }
  if (!(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
    send_to_char(ch, "You don't see them here.\r\n");
    return;
  }
  if (vict == ch) {
    send_to_char(ch, "Garroting yourself won't end well.\r\n");
    return;
  }
  if (FIGHTING(vict)) {
    send_to_char(ch, "You can only garrote someone who isn't fighting.\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_GARROTE);

  if (percent > prob)
    damage(ch, vict, 0, SKILL_GARROTE);
  else {
    dam = GET_LEVEL(ch) + dice(3, 8);
    if (damage(ch, vict, dam, SKILL_GARROTE) > 0)
      WAIT_STATE(vict, PULSE_VIOLENCE * 2);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_shadow_walk)
{
  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_SHADOW_WALK)) {
    send_to_char(ch, "You don't know how to shadow walk.\r\n");
    return;
  }

  /* Typing it again steps out of the shadows early. */
  if (affected_by_spell(ch, SKILL_SHADOW_WALK)) {
    affect_from_char(ch, SKILL_SHADOW_WALK);
    send_to_char(ch, "You step out of the shadows.\r\n");
    return;
  }
  /*
   * Older versions set the sneak bit permanently.  Clear a stray bit that no
   * affect accounts for, so those characters stop sneaking forever.
   */
  if (AFF_FLAGGED(ch, AFF_SNEAK) && !affected_by_spell(ch, SKILL_SNEAK)) {
    REMOVE_BIT(AFF_FLAGS(ch), AFF_SNEAK);
    send_to_char(ch, "You step out of the shadows.\r\n");
    return;
  }

  if (rand_number(1, 101) <= GET_SKILL(ch, SKILL_SHADOW_WALK)) {
    struct affected_type af;

    af.type = SKILL_SHADOW_WALK;
    af.duration = GET_LEVEL(ch);		/* same as the sneak skill */
    af.modifier = 0;
    af.location = APPLY_NONE;
    af.bitvector = AFF_SNEAK;
    affect_to_char(ch, &af);
    send_to_char(ch, "You begin moving through the shadows unseen.\r\n");
  } else {
    send_to_char(ch, "You fail to blend with the shadows.\r\n");
  }
}


ACMD(do_ambush)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;
  int dam, percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_AMBUSH)) {
    send_to_char(ch, "You have no idea how to ambush someone.\r\n");
    return;
  }
  one_argument(argument, arg);
  if (!*arg) {
    send_to_char(ch, "Ambush whom?\r\n");
    return;
  }
  if (!(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
    send_to_char(ch, "You don't see them here.\r\n");
    return;
  }
  if (vict == ch) {
    send_to_char(ch, "You can't ambush yourself.\r\n");
    return;
  }
  if (!AFF_FLAGGED(ch, AFF_HIDE) && !AFF_FLAGGED(ch, AFF_SNEAK)) {
    send_to_char(ch, "You must be hidden or sneaking to ambush someone.\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_AMBUSH);

  REMOVE_BIT(AFF_FLAGS(ch), AFF_HIDE);

  if (percent > prob)
    damage(ch, vict, 0, SKILL_AMBUSH);
  else {
    dam = GET_LEVEL(ch) + dice(4, 8);
    damage(ch, vict, dam, SKILL_AMBUSH);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_death_strike)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;
  int dam, percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_DEATH_STRIKE)) {
    send_to_char(ch, "You don't know how to deliver a death strike.\r\n");
    return;
  }

  if (!(vict = FIGHTING(ch))) {
    one_argument(argument, arg);
    if (!*arg || !(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
      send_to_char(ch, "Death strike whom?\r\n");
      return;
    }
  }
  if (vict == ch) {
    send_to_char(ch, "You can't death strike yourself.\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_DEATH_STRIKE);

  if (percent > prob)
    damage(ch, vict, 0, SKILL_DEATH_STRIKE);
  else {
    dam = GET_LEVEL(ch) * 2 + dice(5, 10);
    damage(ch, vict, dam, SKILL_DEATH_STRIKE);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE * 3);
}


/* ===================================================================
 * WARRIOR SKILLS
 * =================================================================== */

ACMD(do_berserk)
{
  struct affected_type af;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_BERSERK)) {
    send_to_char(ch, "You don't know how to enter a berserker rage.\r\n");
    return;
  }

  if (affected_by_spell(ch, SKILL_BERSERK)) {
    send_to_char(ch, "You are already in a berserker rage!\r\n");
    return;
  }

  if (rand_number(1, 101) > GET_SKILL(ch, SKILL_BERSERK)) {
    send_to_char(ch, "You fail to work yourself into a rage.\r\n");
    return;
  }

  af.type = SKILL_BERSERK;
  af.duration = 2 + GET_LEVEL(ch) / 20;
  af.modifier = GET_LEVEL(ch) / 10 + 2;
  af.location = APPLY_HITROLL;
  af.bitvector = 0;
  affect_to_char(ch, &af);

  act("Your eyes go bloodshot as fury overtakes you!",
      FALSE, ch, 0, 0, TO_CHAR);
  act("$n's eyes go bloodshot — $e enters a berserker rage!",
      TRUE, ch, 0, 0, TO_ROOM);
  WAIT_STATE(ch, PULSE_VIOLENCE);
}


ACMD(do_battle_cry)
{
  struct char_data *vict;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_BATTLE_CRY)) {
    send_to_char(ch, "You don't know how to deliver a battle cry.\r\n");
    return;
  }

  if (rand_number(1, 101) > GET_SKILL(ch, SKILL_BATTLE_CRY)) {
    send_to_char(ch, "You let out a weak yell that impresses nobody.\r\n");
    return;
  }

  act("You let out a thunderous battle cry!",
      FALSE, ch, 0, 0, TO_CHAR);
  act("$n lets out a thunderous battle cry!",
      TRUE, ch, 0, 0, TO_ROOM);

  /* Demoralize current opponent */
  if ((vict = FIGHTING(ch)) != NULL) {
    act("$n's battle cry shakes your nerve!", FALSE, ch, 0, vict, TO_VICT);
    if (!mag_savingthrow(vict, SAVING_PARA, 0))
      WAIT_STATE(vict, PULSE_VIOLENCE);
  }

  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_cleave)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;
  int dam, percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_CLEAVE)) {
    send_to_char(ch, "You don't know how to cleave.\r\n");
    return;
  }

  if (!(vict = FIGHTING(ch))) {
    one_argument(argument, arg);
    if (!*arg || !(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
      send_to_char(ch, "Cleave whom?\r\n");
      return;
    }
  }
  if (vict == ch) {
    send_to_char(ch, "You can't cleave yourself.\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_CLEAVE);

  if (percent > prob)
    damage(ch, vict, 0, SKILL_CLEAVE);
  else {
    dam = GET_LEVEL(ch) + dice(3, 8);
    damage(ch, vict, dam, SKILL_CLEAVE);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_charge)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;
  int dam, percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_CHARGE)) {
    send_to_char(ch, "You don't know how to charge.\r\n");
    return;
  }
  if (FIGHTING(ch)) {
    send_to_char(ch, "You can't charge while already in combat!\r\n");
    return;
  }
  one_argument(argument, arg);
  if (!*arg || !(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
    send_to_char(ch, "Charge whom?\r\n");
    return;
  }
  if (vict == ch) {
    send_to_char(ch, "Charging yourself seems unproductive.\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_CHARGE);

  if (percent > prob)
    damage(ch, vict, 0, SKILL_CHARGE);
  else {
    dam = GET_LEVEL(ch) + dice(4, 6);
    if (damage(ch, vict, dam, SKILL_CHARGE) > 0)
      WAIT_STATE(vict, PULSE_VIOLENCE);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_whirlwind)
{
  struct char_data *vict, *next_vict;
  int dam, percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_WHIRLWIND)) {
    send_to_char(ch, "You don't know how to perform a whirlwind attack.\r\n");
    return;
  }
  if (ROOM_FLAGGED(IN_ROOM(ch), ROOM_PEACEFUL)) {
    send_to_char(ch, "This room just has such a peaceful, easy feeling...\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_WHIRLWIND);

  if (percent > prob) {
    send_to_char(ch, "Your whirlwind attack is sloppy and ineffective.\r\n");
    return;
  }

  act("You spin in a deadly whirlwind, striking all nearby foes!",
      FALSE, ch, 0, 0, TO_CHAR);
  act("$n spins in a deadly whirlwind, attacking everyone nearby!",
      TRUE, ch, 0, 0, TO_ROOM);

  dam = GET_LEVEL(ch) / 2 + dice(2, 6);
  for (vict = world[IN_ROOM(ch)].people; vict; vict = next_vict) {
    next_vict = vict->next_in_room;
    if (skip_room_target(ch, vict) || MOB_FLAGGED(vict, MOB_NOTDEADYET))
      continue;
    damage(ch, vict, dam, SKILL_WHIRLWIND);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE * 3);
}


ACMD(do_intimidate)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_INTIMIDATE)) {
    send_to_char(ch, "You don't know how to intimidate others.\r\n");
    return;
  }
  one_argument(argument, arg);
  if (!*arg) {
    send_to_char(ch, "Intimidate whom?\r\n");
    return;
  }
  if (!(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
    send_to_char(ch, "You don't see them here.\r\n");
    return;
  }
  if (vict == ch) {
    send_to_char(ch, "You can't intimidate yourself.\r\n");
    return;
  }
  if (ROOM_FLAGGED(IN_ROOM(ch), ROOM_PEACEFUL)) {
    send_to_char(ch, "This room just has such a peaceful, easy feeling...\r\n");
    return;
  }
  if (IS_NPC(vict) && GET_MOB_RNUM(vict) != NOBODY && mob_index[GET_MOB_RNUM(vict)].func == shop_keeper) {
    act("$N is not the least bit intimidated by you.", FALSE, ch, 0, vict, TO_CHAR);
    return;
  }

  if (rand_number(1, 101) > GET_SKILL(ch, SKILL_INTIMIDATE)) {
    act("You try to intimidate $N but $E just laughs at you.",
        FALSE, ch, 0, vict, TO_CHAR);
    return;
  }

  act("You fix $N with a fearsome gaze — $E flinches!",
      FALSE, ch, 0, vict, TO_CHAR);
  act("$n fixes you with a terrifying stare — your nerve wavers!",
      FALSE, ch, 0, vict, TO_VICT);

  if (!mag_savingthrow(vict, SAVING_PARA, 0))
    WAIT_STATE(vict, PULSE_VIOLENCE * 2);

  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_war_stomp)
{
  struct char_data *vict, *next_vict;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_WAR_STOMP)) {
    send_to_char(ch, "You don't know how to perform a war stomp.\r\n");
    return;
  }
  if (ROOM_FLAGGED(IN_ROOM(ch), ROOM_PEACEFUL)) {
    send_to_char(ch, "This room just has such a peaceful, easy feeling...\r\n");
    return;
  }

  if (rand_number(1, 101) > GET_SKILL(ch, SKILL_WAR_STOMP)) {
    send_to_char(ch, "You stomp the ground but create little impact.\r\n");
    return;
  }

  act("You stomp the ground with tremendous force, shaking everything nearby!",
      FALSE, ch, 0, 0, TO_CHAR);
  act("$n stomps the ground, sending shockwaves through the area!",
      TRUE, ch, 0, 0, TO_ROOM);

  for (vict = world[IN_ROOM(ch)].people; vict; vict = next_vict) {
    next_vict = vict->next_in_room;
    if (skip_room_target(ch, vict) || MOB_FLAGGED(vict, MOB_NOTDEADYET))
      continue;
    if (!mag_savingthrow(vict, SAVING_PARA, 0)) {
      act("The shockwave knocks $n off $s feet!", TRUE, vict, 0, 0, TO_ROOM);
      GET_POS(vict) = POS_SITTING;
      WAIT_STATE(vict, PULSE_VIOLENCE * 2);
    }
  }

  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_blade_storm)
{
  char arg[MAX_INPUT_LENGTH];
  struct char_data *vict;
  int dam, percent, prob;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_BLADE_STORM)) {
    send_to_char(ch, "You don't know how to perform a blade storm.\r\n");
    return;
  }

  if (!(vict = FIGHTING(ch))) {
    one_argument(argument, arg);
    if (!*arg || !(vict = get_char_vis(ch, arg, NULL, FIND_CHAR_ROOM))) {
      send_to_char(ch, "Blade storm whom?\r\n");
      return;
    }
  }
  if (vict == ch) {
    send_to_char(ch, "You can't blade storm yourself.\r\n");
    return;
  }

  percent = rand_number(1, 101);
  prob = GET_SKILL(ch, SKILL_BLADE_STORM);

  if (percent > prob)
    damage(ch, vict, 0, SKILL_BLADE_STORM);
  else {
    dam = GET_LEVEL(ch) * 2 + dice(3, 10);
    damage(ch, vict, dam, SKILL_BLADE_STORM);
  }
  WAIT_STATE(ch, PULSE_VIOLENCE * 2);
}


ACMD(do_warlords_might)
{
  struct affected_type af;

  if (IS_NPC(ch) || !GET_SKILL(ch, SKILL_WARLORDS_MIGHT)) {
    send_to_char(ch, "You don't know how to channel warlord's might.\r\n");
    return;
  }

  if (affected_by_spell(ch, SKILL_WARLORDS_MIGHT)) {
    send_to_char(ch, "You are already channeling your full might!\r\n");
    return;
  }

  if (rand_number(1, 101) > GET_SKILL(ch, SKILL_WARLORDS_MIGHT)) {
    send_to_char(ch, "You strain but cannot channel the power within you.\r\n");
    return;
  }

  af.type = SKILL_WARLORDS_MIGHT;
  af.duration = GET_LEVEL(ch) / 10 + 2;
  af.modifier = GET_LEVEL(ch) / 10 + 3;
  af.location = APPLY_DAMROLL;
  af.bitvector = 0;
  affect_to_char(ch, &af);

  act("You channel the fury of a thousand battles into your strikes!",
      FALSE, ch, 0, 0, TO_CHAR);
  act("$n roars and channels tremendous power into $s weapon arm!",
      TRUE, ch, 0, 0, TO_ROOM);
  WAIT_STATE(ch, PULSE_VIOLENCE);
}
