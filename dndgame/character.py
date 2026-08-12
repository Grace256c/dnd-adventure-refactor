from dndgame.dice import roll
from dndgame.entity import Entity


RACIAL_BONUSES = {
    "Human": {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1},
    "Elf": {"DEX": 2},
    "Dwarf": {"CON": 2},
    "Orc": {"STR": 2},  # example new race, added with zero new code logic
}


class Character(Entity):
    def __init__(self, name, race, base_hp, level=1):
        super().__init__(name, base_hp)
        self.race = race
        self.level = level

    def roll_stats(self):
        print("Rolling stats...\n")
        stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for stat in stats:
            print(f"Rolling {stat}...")
            self.stats[stat] = roll(6, 3)

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def apply_racial_bonuses(self):
        bonuses = RACIAL_BONUSES.get(self.race, {})
        for stat, bonus in bonuses.items():
            self.stats[stat] += bonus