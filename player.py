
class Player :
    def __init__(self):
        self.userID = 0
        
        self.health = 100
        self.max_health = 100
        self.luck = 0

        self.xp = 0
        self.lvl = 1

        self.current_location = "Town"

        self.str = 3
        self.spd = 3
        self.endur = 3
        self.money = 100

        self.weapon = "fist"
        self.weapon_dmg = 1
        self.weapon_spd = 1

        self.inventory = []

        self.honor = 0
        self.in_combat = False
        self.enemy = {}

        self.helmet = 0
        self.chestplate = 0
        self.leggings = 0
    
    def LevelUP(self):
        if self.xp >= (self.lvl**2) * 10:
            self.xp = 0
            self.lvl += 1

            return True
        return False

    def to_dict(self):
        excluded = {"userID", "in_combat", "enemy"}
        return {k: v for k, v in vars(self).items() if k not in excluded}
    
    def load_from_dict(self, data: dict):
        excluded = {"userID", "in_combat", "enemy"}
        for key, value in data.items():
            if key in excluded:
                continue
            if isinstance(value, (int, float)) and value == 0:
                continue
            setattr(self, key, value)

