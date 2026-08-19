from backend.systems.items import get

def recall(player):
    inventory = []
    for item in player.inventory:
        item = str(item)
        the_item = get(item)
        if the_item and item[0] == "1":
            inventory.append(the_item[0]["name"] + " x" + the_item[1])
        elif the_item:
            inventory.append(the_item[0]["name"] + " " + the_item[1]["name"] + " " + the_item[2]["name"] + " x" + the_item[3])

    return inventory