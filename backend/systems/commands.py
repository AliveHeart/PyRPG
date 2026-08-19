import copy
from backend.core.loader import load_json, create_json_file, save_json
from backend.systems.inventory import recall
from backend.systems.combat import act, kill, spare
from backend.systems.look import look
from types import SimpleNamespace
from backend.systems.player import Player

def execute(game, string, id):
    action = string.split()[0]
    arg = string.split()
    arg.pop(0)

    player = Player()

    data = load_json("backend/data/save_slots/" + str(id) + ".json")
    if data:
        player.load_from_dict(data)
    else:
        create_json_file(str(id), player.to_dict())
        return ["Created new account! You can now start playing!"]

    output = []

    current_location = game.world.areas[player.current_location]

    if player.in_combat == False:
        if action == "look":
            contexts = look(game, player)
            for text in contexts:
                output.append(text)
        elif action == "inventory":
            if len(player.inventory) == 0:
                output.append("Your inventory is empty.")
            else:
                for item in recall(player):
                    output.append(item)
        elif action == "go":
            if arg[0] in current_location.connections:
                player.current_location = arg[0]

                output.append("You reach the " + arg[0] + ". ")
            elif arg[0] == player.current_location:
                output.append("You are already at " + arg[0] + ". ")
            else:
                output.append("You can't find a way to " + arg[0] + ". ")
        elif action == "fight":
            if arg[0] in current_location.entities:
                output.append("You deicde to fight " + arg[0])

                enemy = game.world.entities[arg[0]]

                player.in_combat = True
                player.enemy = vars(copy.copy(enemy))
                player.enemy = SimpleNamespace(**player.enemy)

                output.append("You are in combat with a " + player.enemy.name + ". ")
                output.append("Actions : -> attack -> defend -> run")

                player.enemy = vars(player.enemy)
        elif player.enemy != {}:
            if action == "kill":
                returnState = kill(player)
                output.append(returnState[0])
                output.append(returnState[1])
            elif action == "spare":
                returnState = spare(player)
                output.append(returnState[0])
                output.append(returnState[1])

    else:
        if player.enemy != {}:
            enemy = SimpleNamespace(**player.enemy)
            condition = act(action , player, enemy)

            output.append(condition[0])
            output.append(condition[1])

            if player.health > 0 and player.enemy != {} and player.in_combat == True:
                output.append("You are in combat with a " + enemy.name + ". ")
                output.append("Your health :- " + str(player.health) + "HP. " + enemy.name + " health :- " + str(enemy.health) + "HP.")
                output.append("Actions : -> attack | -> defend | -> run | -> surrender")

    can_lvl = player.LevelUP()
    if can_lvl:
        output.append("You leveled up to " + str(player.lvl) + "!")

    save_json(str(id), player.to_dict())
    return output
                
        




