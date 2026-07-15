from loader import load_json
from area import Area
from entity import Entity

class World:
    def __init__(self):
        areas = load_json("data/areas.json")
        entities = load_json("data/entities.json")

        self.areas = {}
        self.entities = {}

        for name in areas:
            area = Area(name)
            self.areas[name] = area

        for area_name, data in areas.items():
            area = self.areas[area_name]
            for connection in data["connections"]:
                area.connections.append(
                    connection
                )
            for entitie in data["entities"]:
                area.entities.append(
                    entitie
                )
            area.description = data["description"]

        for entity_name, data in entities.items():
            entity_data = data
            entity = Entity(entity_name, entity_data["type"], entity_data["hp"], entity_data["hostile"], entity_data["str"], entity_data["spd"], entity_data["exp"], entity_data["honor"])
            self.entities[entity_name] = entity