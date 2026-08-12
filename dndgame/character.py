from dndgame.dice import roll
from dndgame.entity import Entity

RACIAL_BONUSES: dict[str, dict[str, int]] = {
    "Human": {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1},
    "Elf": {"DEX": 2},
    "Dwarf": {"CON": 2},
    "Orc": {"STR": 2},
}


class Character(Entity):
    """A player-controlled character.

    Attributes:
        race: The character's race, e.g. "Human", "Elf", "Dwarf", "Orc".
        level: The character's current level.
    """

    def __init__(self, name: str, race: str, base_hp: int, level: int = 1) -> None:
        super().__init__(name, base_hp)
        self.race: str = race
        self.level: int = level

    def roll_stats(self) -> None:
        """Roll 3d6 for each ability score, then set max_hp and hp."""
        print("Rolling stats...\n")
        stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        self.stats = {stat: self._roll_one_stat(stat) for stat in stat_names}

        self.max_hp = self.base_hp + self.get_modifier("CON")
        self.hp = self.max_hp

    def _roll_one_stat(self, stat: str) -> int:
        """Roll 3d6 for a single stat, printing progress as it goes."""
        print(f"Rolling {stat}...")
        return roll(6, 3)

    def apply_racial_bonuses(self) -> None:
        """Apply this character's racial stat bonuses, based on RACIAL_BONUSES.

        Example:
            >>> c = Character("Aria", "Elf", 10)
            >>> c.stats = {"DEX": 10}
            >>> c.apply_racial_bonuses()
            >>> c.stats["DEX"]
            12
        """
        bonuses = RACIAL_BONUSES.get(self.race, {})
        for stat, bonus in bonuses.items():
            self.stats[stat] += bonus