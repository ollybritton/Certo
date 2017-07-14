# ---
# types.py
# File that stores all classes that involve things like items and roles.
# ---

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Spell:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Battle:
    def __init__(self, name, code):
        self.name = name
        self.execute = code


class Character:
    def __init__(self, name, inventory, health, exp):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.exp = exp


class Player(Character):
    def __init__(self, name, health, exp):
        super().__init__(
            name = name,
            inventory = [],
            health = health,
            exp = exp
        )


class Hostile(Character):
    def __init__(self, name, inventory, health, exp):
        super().__init__(
            name = name,
            inventory = inventory,
            health = health,
            exp = exp
        )
