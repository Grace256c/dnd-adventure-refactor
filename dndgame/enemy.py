from dndgame.entity import Entity

DEFAULT_STATS: dict[str, int] = {
    "STR": 10,
    "DEX": 10,
    "CON": 10,
    "INT": 10,
    "WIS": 10,
    "CHA": 10,
}


class Enemy(Entity):
    """A hostile entity the player can fight, e.g. a goblin."""

    def __init__(self, name: str, base_hp: int) -> None:
        super().__init__(name, base_hp)
        self.stats = dict(DEFAULT_STATS)
        self.hp = base_hp
        self.max_hp = base_hp