from loader import load_json
from area import Area
from entity import Entity

class World:
    def __init__(self):
        areas = load_json("data/areas.json")
        entities = load_json("data/entities.json")

        self.areas = {}

        for name in areas:
            area = Area(name)
            self.areas[name] = area

        for area_name, data in areas.items():
            area = self.areas[area_name]
            for connection in data["connections"]:
                area.connections.append(
                    connection
                )
            area.description = data["description"]

        for entity_name, data in entities.items():
            entity_data = data
            entity = Entity(entity_name, entity_data["type"], entity_data["hp"], entity_data["hostile"])
            area.entities.append(entity)