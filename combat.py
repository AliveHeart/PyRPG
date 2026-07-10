

def attack(game):
    enemy = game.world.entities[game.player.enemy]

    plr_damage = game.player.str * game.player.weapon_dmg
    plr_speed = game.player.spd * game.player.weapon_spd

    enemy_spd = enemy.spd