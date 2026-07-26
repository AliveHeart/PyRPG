import json

saves_path = "data/save_slots/"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)
    
def save_json(slot, data):
    with open(saves_path + str(slot) + ".json", "w") as f:
        json.dump(data, f, indent=4)
        return True