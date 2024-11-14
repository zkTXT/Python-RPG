# Monster class
class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level * 30
        self.attack = level * 5
        self.defense = level * 2
    
    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense)
        print(f"{self.name} loses {max(0, damage - self.defense)} HP. Remaining HP: {self.hp}")
        
    def is_alive(self):
        return self.hp > 0

# Goblin subclass
class Goblin(Monster):
    def __init__(self, level):
        super().__init__("Goblin", level)
        self.hp += 10
        self.attack += 1

# Troll subclass
class Troll(Monster):
    def __init__(self, level):
        super().__init__("Troll", level)
        self.hp += 15
        self.defense += 2

# Special boss class
class Gio(Monster):
    def __init__(self, level):
        super().__init__("Gio", level)
        self.hp += 20
        self.defense += 3
