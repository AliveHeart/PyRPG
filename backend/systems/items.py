from backend.core.loader import load_json

data_path = "data/"

items = load_json(data_path + "items.json")
armor = load_json(data_path + "armour.json")
material = load_json(data_path + "material.json")
adjective_armr = load_json(data_path + "adjective-armour.json")
adjective_wp = load_json(data_path + "adjective-weapon.json")

def get(id):
    item_ids = str(id)
    u_id = " ".join(item_ids[:-1])

    if item_ids[0] == "1":
        if str(u_id) in items:
            return [items[u_id], str(int(item_ids[-1]))]
    else:
        if item_ids[0] == "3":
            adjective = adjective_wp
        else:
            adjective = adjective_armr

        armor_index = item_ids[0] + " " + item_ids[1]
        if (armor_index) in armor and item_ids[2] in material:
            return [adjective[item_ids[3]], material[item_ids[2]], armor[armor_index], str(int(item_ids[-1]))]

    return False