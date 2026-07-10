import random

def attack(game):
    enemy = game.world.entities[game.player.enemy]

    plr_damage = game.player.str * game.player.weapon_dmg
    plr_speed = game.player.spd * game.player.weapon_spd

    enemy_spd = enemy.spd

    ratio = enemy_spd / plr_speed
    dodge_chance = min(1.0, 0.1 + 0.9 * (ratio / (1 + ratio))) * 100
    roll = random.uniform(0, 100)

    if roll < dodge_chance:
        return ("The " + enemy.name + " dodges your attack!")
    else:
        enemy.health -= plr_damage
        return ("You hit " + enemy.name + " and deal " + str(plr_damage) + " damage!")


    