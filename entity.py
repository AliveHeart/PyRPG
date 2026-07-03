
class Entity :
    def __init__(self, name, type, hp, hostile, str, spd, exp):

        self.name = name
        self.health = hp
        self.max_health = hp
        self.hostile = hostile

        self.str = str
        self.spd = spd
        self.exp = exp

        self.type = type

        self.str = 1
        self.spd = 1
        self.endur = 1
        self.money = 100