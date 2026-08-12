class Entity:
    def __init__(self, name, base_hp):
        self.name = name
        self.stats = {}
        self.base_hp = base_hp
        self.hp = 0
        self.max_hp = 0
        self.armor_class = 10

    def get_modifier(self, stat):
        """Calculate ability modifier."""
        return (self.stats[stat] - 10) // 2

    def is_alive(self):
        return self.hp > 0