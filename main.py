from dndgame.character import Character
from dndgame.enemy import Enemy
from dndgame.combat import Combat


def create_character():
    print("Welcome to D&D Adventure!")
    name = input("Enter your character's name: ")

    print("\nChoose your race:")
    print("1. Human (+1 to all stats)")
    print("2. Elf (+2 DEX)")
    print("3. Dwarf (+2 CON)")
    print("4. Orc (+2 STR)")
    race_choice = input("Enter choice (1-4): ")
    print("\n")
    race = ["Human", "Elf", "Dwarf", "Orc"][int(race_choice) - 1]

    character = Character(name, race, 10)
    character.roll_stats()
    character.apply_racial_bonuses()
    return character


def display_character(character):
    print(f"\n{character.name} the {character.race}")
    print("\nStats:")
    for stat, value in character.stats.items():
        modifier = character.get_modifier(stat)
        print(f"{stat}: {value} ({'+' if modifier >= 0 else ''}{modifier})")
    print(f"\nHP: {character.hp}")


def main():
    player = create_character()

    while player.is_alive():
        print("\nWhat would you like to do?")
        print("1. Fight a goblin")
        print("2. View character")
        print("3. Quit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            goblin = Enemy("Goblin", 5)
            combat = Combat(player, goblin)
            result = combat.run()
            if result == "victory":
                print("You defeated the goblin!")
            elif result == "fled":
                print("You ran away!")
            elif result == "defeated":
                print("You have been defeated...")
        elif choice == "2":
            display_character(player)
        elif choice == "3":
            break

    if not player.is_alive():
        print(f"\nGame over — {player.name} has fallen.")


if __name__ == "__main__":
    main()