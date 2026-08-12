class Entity:
    """Base class for anything that participates in combat.

    Attributes:
        name: Display name of the entity.
        stats: Mapping of ability score name (e.g. "STR") to its value.
        base_hp: The starting hit point value used to compute max_hp.
        hp: Current hit points.
        max_hp: Maximum hit points.
        armor_class: Defense value that attack rolls must meet or beat.
    """

    def __init__(self, name: str, base_hp: int) -> None:
        self.name: str = name
        self.stats: dict[str, int] = {}
        self.base_hp: int = base_hp
        self.hp: int = 0
        self.max_hp: int = 0
        self.armor_class: int = 10

    def get_modifier(self, stat: str) -> int:
        """Calculate the ability modifier for a given stat.

        Args:
            stat: The ability score name, e.g. "STR" or "DEX".

        Returns:
            The modifier, using the standard D&D formula (value - 10) // 2.

        Example:
            >>> e = Entity("Test", 10)
            >>> e.stats["STR"] = 14
            >>> e.get_modifier("STR")
            2
        """
        return (self.stats[stat] - 10) // 2

    def is_alive(self) -> bool:
        """Return whether this entity still has positive hit points."""
        return self.hp > 0