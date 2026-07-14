import random, randomer

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
    defend_weightage = 20 + enemy.defensive
    surrender_weightage = 10 + enemy.cowardness 
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

    if player.str <= (enemy.str + enemy.endur):
        surrender_weightage -= 20
        defend_weightage -= 20
        attack_weightage += 40

    attack_weightage = max(0, attack_weightage)
    defend_weightage = max(0, defend_weightage)
    surrender_weightage = max(0, surrender_weightage)

    weightage_list = {"attack": attack_weightage, 
                      "defend": defend_weightage, 
                      "surrender": surrender_weightage}
    descision = randomer.weighted_choice(weightage_list)
    
    return descision

def attack(game, descision):
    enemy = game.world.entities[game.player.enemy]

    plr_damage = game.player.str * game.player.weapon_dmg
    plr_speed = game.player.spd * game.player.weapon_spd

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
        if (game.player.str * game.player.endur) > (enemy.str * enemy.endur):
            enemy_feedback = "You hit the " + enemy.name + " but the " + enemy.name + " blocks the attack. You deal " + str(plr_damage) + " damage!"
        else:
            enemy_feedback = "You hit the " + enemy.name + " but the " + enemy.name + " blocks the attack."
    

    if descision == "attack" :
        enemy_feedback = enemy_attack(enemy, game.player)
    elif descision == "surrender":
        enemy.surrendered = True
        enemy_feedback = "The " + enemy.name + " has surrendered."

    return [plr_feedback, enemy_feedback]
    

def act(action, game):
    enemy = game.world.entities[game.player.enemy]

    descision = enemy_descision(enemy, game.player)
    
    condition = []
    if action == "attack":
        condition = attack(game, descision)
    if action == "run":
        can_run = chance_roll(enemy.spd, game.player.spd)
        condition.append("You try to run away.")
        if can_run:
            game.player.in_combat = False
            game.player.enemy = "air"

            condition.append("You managed to escape the " + enemy.name + ". ")
        else:
            condition.append(enemy_attack(enemy, game.player))


    if enemy.health <= 0:
        game.player.in_combat = False
        game.player.enemy = "air"

        return ["The " + enemy.name + " has fallen", "+ " + str(random.randint(1, 5) * enemy.str * enemy.endur) + " xp"]

    return condition