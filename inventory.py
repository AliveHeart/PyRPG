import items, items

def recall(player):
    inventory = []
    for item in player.inventory:
        the_item = items.get(item)
        if the_item:
            inventory.append(the_item)

    return inventory