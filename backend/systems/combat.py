import random
from backend.utils.randomer import weighted_choice
from types import SimpleNamespace

def chance_roll(enemy_atr, plr_atr):
    ratio = enemy_atr / plr_atr
    chance = min(1.0, 0.1 + 0.6 * (ratio / (1 + ratio))) * 100
    roll = random.uniform(0, 100)

    return roll < chance

def enemy_attack(enemy, player):
    plr_speed = player.spd * player.weapon_spd
    
    if chance_roll(enemy.spd, plr_speed):
        return ("You dodge the " + enemy.name + " attack!")
    else:
        player.health -= enemy.str
        return ("The " + enemy.name + " attacks you for " + str(enemy.str) + " damage!")
    
def enemy_descision(enemy, player):
    attack_weightage = 80 + enemy.arrogance
    defend_weightage = 35 + enemy.defensive
    surrender_weightage = 35 + enemy.cowardness

    if enemy.health <= (enemy.max_health * 0.4) and enemy.health > (enemy.max_health * 0.2):
        defend_weightage += 20
        attack_weightage -= 20
    elif enemy.health <= (enemy.max_health * 0.2):
        defend_weightage += 20
        attack_weightage -= 40
        surrender_weightage += 20

    if player.health < (player.max_health * 0.5):
        attack_weightage += 30
        defend_weightage -= 15
        surrender_weightage -= 15

    if player.str <= enemy.str:
        surrender_weightage -= 20
        defend_weightage -= 20
        attack_weightage += 40

    attack_weightage = max(0, attack_weightage)
    defend_weightage = max(0, defend_weightage)
    surrender_weightage = max(0, surrender_weightage)

    weightage_list = {"attack": attack_weightage, 
                      "defend": defend_weightage, 
                      "surrender": surrender_weightage}
    descision = weighted_choice(weightage_list)
    
    return descision

def attack(player, descision):
    enemy = SimpleNamespace(**player.enemy)

    plr_damage = player.str * player.weapon_dmg
    plr_speed = player.spd * player.weapon_spd

    enemy_spd = enemy.spd

    plr_feedback = " "
    enemy_feedback = " "
    if descision != "defend":
        if chance_roll(enemy_spd, plr_speed):
            plr_feedback = "The " + enemy.name + " dodges your attack!"
        else:
            enemy.health -= plr_damage
            plr_feedback = "You hit the " + enemy.name + " and deal " + str(plr_damage) + " damage!"
    else:
        plr_feedback = "The " + enemy.name + " defends!"
        if (player.str * player.endur) > (enemy.str * enemy.endur):
            enemy_feedback = "You hit the " + enemy.name + " but the " + enemy.name + " blocks the attack. You deal " + str(plr_damage) + " damage!"
        else:
            enemy_feedback = "You hit the " + enemy.name + " but the " + enemy.name + " blocks the attack."
    

    if descision == "attack" :
        enemy_feedback = enemy_attack(enemy, player)
    elif descision == "surrender":
        enemy.surrendered = True
        enemy_feedback = "The " + enemy.name + " has surrendered."

    return [plr_feedback, enemy_feedback]

def run(player, enemy):
    can_run = chance_roll(enemy.spd, player.spd)
    condition = ["You try to run away."]
    if can_run:
        player.in_combat = False
        player.enemy = {}

        condition.append("You managed to escape the " + enemy.name + ". ")
    else:
        condition.append(enemy_attack(enemy, player))
    
    return condition

def defend(player, enemy, descision):
    can_block = chance_roll(enemy.endur, player.endur)
    condition = ["You block."]
    if can_block and descision == "attack":
        condition.append("You block the hit")
    elif descision == "attack":
        condition[0] = "You try to block but fail."
        condition.append(enemy_attack(enemy, player))
    
    return condition

def act(action, player, enemy):
    descision = enemy_descision(enemy, player)
    
    condition = []
    if action == "attack":
        condition = attack(player, descision)
    elif action == "run":
       condition = run(player, enemy)
    elif action == "defend":
        condition = defend(player, enemy, descision)
        
    if descision == "surrender":
        player.in_combat = False
        condition = ["The " + enemy.name + " has surrendered. Choose what to do with the " + enemy.name, "-> kill | -> steal | -> spare"]

    if enemy.health <= 0:
        condition = kill(player)

    if player.health <= 0:
        player.in_combat = False
        player.health = player.max_health

        condition = ["You have fallen", "It's like it never happened."]


    if len(condition) < 2:
        return [".", "."]
    return condition

def kill(player):
    enemy = SimpleNamespace(**player.enemy)
    xp = (random.randint(1, 5) * enemy.str * enemy.endur / 2)

    player.enemy = {}

    player.money += enemy.money
    player.xp += xp
    player.honor += enemy.honor

    player.in_combat = False

    return ["The " + enemy.name + " has fallen", "+ " + str(xp) + " xp, " + str(enemy.honor) + "+ honor, +" + str(enemy.money) + "$"]

def steal(player):
    enemy = SimpleNamespace(**player.enemy)

def spare(player):
    enemy = SimpleNamespace(**player.enemy)
    honor = abs(enemy.honor / 2)

    player.in_combat = False

    player.enemy = {}
    player.honor += honor

    return ["You spare " + enemy.name + ".", "+ " + str(honor) + " honor"]