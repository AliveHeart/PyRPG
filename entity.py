
class Entity :
    def __init__(self, name, hp, hostile):

        self.name = name
        self.health = hp
        self.max_health = hp
        self.hostile = hostile
        self.current_location = "Town"
        self.str = 1
        self.spd = 1
        self.endur = 1
        self.money = 100