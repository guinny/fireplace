from ..utils import *


##
# Minions

# Darnassus Aspirant
class AT_038:
	play = GainEmptyMana(CONTROLLER, 1)
	deathrattle = GainMana(CONTROLLER, -1)


# Savage Combatant
class AT_039:
	inspire = Buff(FRIENDLY_HERO, "AT_039e")

AT_039e = buff(atk=2)


# Wildwalker
class AT_040:
	play = Buff(TARGET, "AT_040e")

AT_040e = buff(health=3)


# Knight of the Wild
class AT_041:
	events = Summon(CONTROLLER, BEAST).on(Buff(SELF, "AT_041e"))

AT_041e = buff(cost=-1)


# Druid of the Saber
class AT_042:
	choose = ("AT_042a", "AT_042b")

class AT_042a:
	play = Morph(SELF, "AT_042t")

class AT_042b:
	play = Morph(SELF, "AT_042t2")


# Aviana
class AT_045:
	update = Refresh(CONTROLLER_HAND + MINION, {GameTag.COST: SET(1)})


##
# Spells

# Living Roots
class AT_037:
	choose = ("AT_037a", "AT_037b")

class AT_037a:
	play = Hit(TARGET, 2)

class AT_037b:
	play = Summon(CONTROLLER, "AT_037t") * 2


# Astral Communion
class AT_043:
	play = GainMana(CONTROLLER, 10), Discard(CONTROLLER_HAND)


# Mulch
class AT_044:
	play = Destroy(TARGET), Give(OPPONENT, RandomMinion())
