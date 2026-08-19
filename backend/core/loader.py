import json
import os

saves_path = "backend/data/save_slots/"

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False

def save_json(slot, data):
    try:
        with open(os.path.join(saves_path, f"{slot}.json"), "w") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception:
        return False

def create_json_file(file_name, data):
    if not os.path.exists(saves_path):
        raise FileNotFoundError(f"The folder '{saves_path}' does not exist.")

    file_path = os.path.join(saves_path, f"{file_name}.json")

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    return file_path

