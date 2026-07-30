import loader

data_path = "data/"

def get(id):
    item_ids = id.split()
    u_id = " ".join(item_ids[:-1])

    if item_ids[0] == "1":
        items = loader.load_json(data_path + "items.json")
        if str(u_id) in items:
            return [items[u_id], str(int(item_ids[-1]))]
    else:
        armor = loader.load_json(data_path + "armour.json")
        material = loader.load_json(data_path + "material.json")
        adjective = loader.load_json(data_path + "adjective-armour.json")
        if item_ids[0] == "3":
            adjective = loader.load_json(data_path + "adjective-weapon.json")

        armor_index = item_ids[0] + " " + item_ids[1]
        if (armor_index) in armor and item_ids[2] in material:
            return [adjective[item_ids[3]], material[item_ids[2]], armor[armor_index], str(int(item_ids[-1]))]

    return False