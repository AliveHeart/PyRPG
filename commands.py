import renderer

def execute(game, string):
    action = string.split()[0]
    arg = string.split()
    arg.pop(0)

    current_location = game.world.areas[game.player.current_location]

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

        renderer.render("You look around. " + current_location.description + " You see " + str(path_no) + " paths to " + path_names)
    elif action == "go":
        if arg[0] in current_location.connections:
            game.player.current_location = arg[0]   