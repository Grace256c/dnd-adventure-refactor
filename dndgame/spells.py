class Spell:
    def __init__(self, name: str, level: int, school: str, spell_power: int) -> None:
        self.name = name
        self.level = level
        self.school = school
        self.spell_power = spell_power

    def cast(self, caster: object, target: object) -> None:
        pass


class SpellBook:
    def __init__(self) -> None:
        self.spells: list[Spell] = []

    def add_spell(self, spell: Spell) -> None:
        self.spells.append(spell)

    def get_available_spells(self, spell_level: int) -> list[Spell]:
        """Return all spells at or below the given level, using filter()."""
        return list(filter(lambda spell: spell.level <= spell_level, self.spells))