import loader

data_path = "data/"
items_path =  data_path + "items.json"

def get_Item(id):
    item_ids = id.split()
    u_id = " ".join(item_ids[:-1])

    if item_ids[0] == "01":
        items = loader.load_json(items_path)
        if str(u_id) in items:
            return items[u_id]["name"], item_ids[-1]

    return False