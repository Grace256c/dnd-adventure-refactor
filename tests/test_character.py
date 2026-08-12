from dndgame.character import Character


def test_roll_stats_sets_hp():
    character = Character("Test", "Human", 10)
    character.roll_stats()
    assert character.max_hp == character.base_hp + character.get_modifier("CON")
    assert character.hp == character.max_hp
    assert set(character.stats.keys()) == {"STR", "DEX", "CON", "INT", "WIS", "CHA"}


def test_apply_racial_bonuses_human():
    character = Character("Test", "Human", 10)
    character.stats = {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}
    character.apply_racial_bonuses()
    assert all(value == 11 for value in character.stats.values())


def test_apply_racial_bonuses_elf():
    character = Character("Test", "Elf", 10)
    character.stats = {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}
    character.apply_racial_bonuses()
    assert character.stats["DEX"] == 12
    assert character.stats["STR"] == 10


def test_apply_racial_bonuses_orc():
    character = Character("Test", "Orc", 10)
    character.stats = {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}
    character.apply_racial_bonuses()
    assert character.stats["STR"] == 12


def test_is_alive():
    character = Character("Test", "Human", 10)
    character.hp = 5
    assert character.is_alive() is True
    character.hp = 0
    assert character.is_alive() is False