from typing import Literal

from dndgame.dice import roll
from dndgame.entity import Entity

CombatResult = Literal["victory", "fled", "defeated"]


class Combat:
    """Manages a single combat encounter between a player and an enemy."""

    def __init__(self, player: Entity, enemy: Entity) -> None:
        self.player: Entity = player
        self.enemy: Entity = enemy
        self.round: int = 0
        self.initiative_order: list[Entity] = []

    def roll_initiative(self) -> list[Entity]:
        """Roll initiative for both combatants and set the turn order.

        Returns:
            The turn order as a list of two entities, first to act first.
        """
        player_init = roll(20, 1) + self.player.get_modifier("DEX")
        enemy_init = roll(20, 1) + self.enemy.get_modifier("DEX")

        if player_init >= enemy_init:
            self.initiative_order = [self.player, self.enemy]
        else:
            self.initiative_order = [self.enemy, self.player]

        return self.initiative_order

    def attack(self, attacker: Entity, defender: Entity) -> int:
        """Resolve a single attack from attacker against defender.

        Args:
            attacker: The entity making the attack.
            defender: The entity being attacked.

        Returns:
            The damage dealt, or 0 if the attack missed.
        """
        attack_roll = roll(20, 1) + attacker.get_modifier("STR")
        weapon_max_damage = 6
        if attack_roll >= defender.armor_class:
            damage = roll(weapon_max_damage, 1)
            defender.hp -= damage
            return damage
        return 0

    def run(self) -> CombatResult:
        """Run the full combat loop until someone dies or the player flees.

        Returns:
            "victory" if the enemy is defeated, "fled" if the player runs,
            or "defeated" if the player is reduced to 0 HP.
        """
        print(f"\nA {self.enemy.name} appears!")
        self.roll_initiative()
        turn = 0

        while self.player.is_alive() and self.enemy.is_alive():
            current = self.initiative_order[turn]

            if current is self.player:
                print(f"\n{self.enemy.name} HP: {self.enemy.hp}")
                print("\nYour turn!")
                print("1. Attack")
                print("2. Run away")

                choice = input("What do you do? ")
                while choice not in ("1", "2"):
                    print("Invalid choice. Please enter 1 or 2.")
                    choice = input("What do you do? ")

                if choice == "2":
                    return "fled"

                damage = self.attack(self.player, self.enemy)
                if damage > 0:
                    print(f"You hit for {damage} damage!")
                else:
                    print("You missed!")
            else:
                damage = self.attack(self.enemy, self.player)
                if damage > 0:
                    print(f"The {self.enemy.name} hits you for {damage} damage!")
                else:
                    print(f"The {self.enemy.name} missed!")

            turn = 1 - turn

        if self.player.is_alive():
            return "victory"
        else:
            return "defeated"