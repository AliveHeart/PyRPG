import loader

data_path = "data/"
items_path =  data_path + "items.json"

def get_Item(id):
    item_ids = id.split()

    if item_ids[0] == "01":
        items = loader.load_json(items_path)
        if id in items:
            return items[id]["name"]

    return False