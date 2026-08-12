
def look(game, player):
    path_names = ""
    path_no = len(current_location.connections)

    current_location = game.world.areas[player.current_location]
    
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

        return [("You look around. " + current_location.description + " You see " + str(path_no) + " paths to " + path_names), ("You spot " + entity_Names)]