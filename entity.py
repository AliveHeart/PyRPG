
class Entity :
    def __init__(self, name, type, hp, hostile, str, spd, exp, honor):

        self.name = name
        self.health = hp
        self.max_health = hp
        self.hostile = hostile

        self.str = str
        self.spd = spd
        self.exp = exp

        self.honor = honor

        self.arrogance = 0
        self.defensive = 0
        self.cowardness = 0

        self.surrendered = False
        self.type = type

        self.endur = str * spd
        self.money = 100