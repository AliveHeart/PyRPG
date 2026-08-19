
class Entity :
    def __init__(self, name, entitydata):

        self.name = name
        self.health = entitydata["hp"]
        self.max_health = entitydata["hp"]
        self.hostile = entitydata["hostile"]

        self.str = entitydata["str"]
        self.spd = entitydata["spd"]
        self.exp = entitydata["exp"]

        self.honor = entitydata["honor"]

        self.arrogance = entitydata["arrogance"]
        self.defensive = entitydata["defensive"]
        self.cowardness = entitydata["coward"]

        self.surrendered = False
        self.type = entitydata["type"]

        self.endur = self.str * self.spd
        self.money = entitydata["money"]