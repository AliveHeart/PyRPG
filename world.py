import area, entity

class World:
    def __init__(self):
        town = area("Town")
        forest = area("Forest")

        self.areas = {
            "Town": town,
            "Forest": forest
        }

        mom = entity("Mom")
        merchant = entity("Merchant")

        self.town.entities.append(mom)
        self.town.entities.append(merchant)

        self.town.connections["forest"] = self.forest
        self.forest.connections["town"] = self.town