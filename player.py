KEY_MAP = {
    "hp": "health",
    "mhp": "max_health",
    "luck": "luck",
    "xp": "xp",
    "lvl": "lvl",
    "loc": "current_location",
    "str": "str",
    "spd": "spd",
    "endur": "endur",
    "money": "money",
    "inComb": "in_combat",
    "enemy": "enemy",
    "wp": "weapon",
    "wp_dmg": "weapon_dmg",
    "wp_spd": "weapon_spd",
    "inv": "inventory",
    "honor": "honor",
    "helm": "helmet",
    "chest": "chestplate",
    "leg": "leggings"
}
REVERSE_MAP = {v: k for k, v in KEY_MAP.items()}

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

        self.weapon = 1
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
        excluded = {"userID"}
        result = {}
        for k, v in vars(self).items():
            if k in excluded:
                continue
            json_key = REVERSE_MAP.get(k, k)
            result[json_key] = v
        return result
    
    def load_from_dict(self, data: dict):
        excluded = {"userID"}
        
        for key, value in data.items():
            if key in excluded:
                continue
            attr = KEY_MAP.get(key, key)
            setattr(self, attr, value)

