from dndgame.entity import Entity


class Enemy(Entity):
    def __init__(self, name, base_hp):
        super().__init__(name, base_hp)

        self.stats = {
            "STR": 10,
            "DEX": 10,
            "CON": 10,
            "INT": 10,
            "WIS": 10,
            "CHA": 10,
        }

        self.hp = base_hp
        self.max_hp = base_hp