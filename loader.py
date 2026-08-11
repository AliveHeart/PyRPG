import json
import os

saves_path = "data/save_slots/"

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        # Optional: handle case where file exists but is corrupted
        return False

def save_json(slot, data):
    try:
        with open(os.path.join(saves_path, f"{slot}.json"), "w") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception:
        return False
