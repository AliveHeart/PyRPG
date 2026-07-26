import renderer, combat, loader

def execute(game, string):
    action = string.split()[0]
    arg = string.split()
    arg.pop(0)

    current_location = game.world.areas[game.player.current_location]

    if game.player.in_combat == False:
        if action == "look":
            path_names = ""
            path_no = len(current_location.connections)
            for index, area_name in enumerate(current_location.connections):
                if path_no > 1:
                    if (path_no - 1) == index:
                        path_names += "and " + area_name + ". "
                    elif (path_no - 2) == index:
                        path_names += "" + area_name + " "
                    else:
                        path_names += "" + area_name + ", "
                else:
                    path_names += "" + area_name + ". "

            entity_Names = ""
            entity_no = len(current_location.entities)
            for index, entity_name in enumerate(current_location.entities):
                if entity_no > 1:
                    if (entity_no - 1) == index:
                        entity_Names += "and " + entity_name + ". "
                    elif (entity_no - 2) == index:
                        entity_Names += "" + entity_name + " "
                    else:
                        entity_Names += "" + entity_name + ", "
                else:
                    entity_Names += "" + entity_name + ". "

            renderer.render("You look around. " + current_location.description + " You see " + str(path_no) + " paths to " + path_names)
            renderer.render("You spot " + entity_Names)
        elif action == "save":
            save = loader.save_json(str(arg[0]), game.player.to_dict())
            if save == True:
                renderer.render("Data saved!")
        elif action == "load":
            data = loader.load_json("data/save_slots/" + str(arg[0]) + ".json")
            game.player.load_from_dict(data)

            renderer.render("Data loaded!")
        elif action == "go":
            if arg[0] in current_location.connections:
                game.player.current_location = arg[0]

                renderer.render("You reach the " + arg[0] + ". ")
            else:
                renderer.render("You can't find a way to " + arg[0] + ". ")
        elif action == "fight":
            if arg[0] in current_location.entities:
                renderer.render("You deicde to fight " + arg[0])
                game.player.in_combat = True
                game.player.enemy = arg[0]

                renderer.render("You are in combat with a " + game.player.enemy + ". ")
                renderer.render("Actions : -> attack -> defend -> run -> surrender")
        elif game.player.enemy != "air":
            if action == "kill":
                returnState = combat.kill(game)
                renderer.render(returnState[0])
                renderer.render(returnState[1])
            elif action == "spare":
                returnState = combat.spare(game)
                renderer.render(returnState[0])
                renderer.render(returnState[1])
        elif game.player.enemy != "air":
            game.player.enemy = "air"

    else:
        if game.player.enemy != "air":
            enemy = game.world.entities[game.player.enemy]
            condition = combat.act(action ,game)

            renderer.render(condition[0])
            renderer.render(condition[1])

            if game.player.health > 0 and game.player.enemy != "air" and game.player.in_combat == True:
                renderer.render("You are in combat with a " + game.player.enemy + ". ")
                renderer.render("Your health :- " + str(game.player.health) + "HP. " + game.player.enemy + " health :- " + str(enemy.health) + "HP.")
                renderer.render("Actions : -> attack | -> defend | -> run | -> surrender")

    can_lvl = game.player.LevelUP()
    if can_lvl:
        renderer.render("You leveled up to " + str(game.player.lvl) + "!")
                
        




