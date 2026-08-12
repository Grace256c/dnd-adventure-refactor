from unittest.mock import patch

from dndgame.character import Character
from dndgame.enemy import Enemy
from dndgame.combat import Combat


def make_player():
    player = Character("Hero", "Human", 10)
    player.stats = {"STR": 14, "DEX": 14, "CON": 14, "INT": 10, "WIS": 10, "CHA": 10}
    player.hp = 10
    player.max_hp = 10
    return player


def test_roll_initiative_player_wins_ties():
    player = make_player()
    enemy = Enemy("Goblin", 5)
    combat = Combat(player, enemy)

    with patch("random.randint", return_value=10):
        order = combat.roll_initiative()

    assert order == [player, enemy]


def test_attack_hits_and_deals_damage():
    player = make_player()
    enemy = Enemy("Goblin", 5)
    combat = Combat(player, enemy)

    with patch("random.randint", return_value=20):
        damage = combat.attack(player, enemy)

    assert damage > 0
    assert enemy.hp == 5 - damage


def test_attack_misses_deals_no_damage():
    player = make_player()
    enemy = Enemy("Goblin", 5)
    combat = Combat(player, enemy)

    with patch("random.randint", return_value=1):
        damage = combat.attack(player, enemy)

    assert damage == 0
    assert enemy.hp == 5


def test_run_player_flees():
    player = make_player()
    enemy = Enemy("Goblin", 5)
    combat = Combat(player, enemy)

    with patch("random.randint", return_value=1), patch("builtins.input", return_value="2"):
        result = combat.run()

    assert result == "fled"


def test_run_player_wins():
    player = make_player()
    enemy = Enemy("Goblin", 1)
    combat = Combat(player, enemy)

    with patch("random.randint", return_value=20), patch("builtins.input", return_value="1"):
        result = combat.run()

    assert result == "victory"

