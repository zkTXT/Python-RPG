# Classe monstre
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

# Sous-classe Gobelin
class Goblin(Monster):
    def __init__(self, level):
        super().__init__("Goblin", level)
        self.hp += 10
        self.attack += 1

# Sous-classe Troll
class Troll(Monster):
    def __init__(self, level):
        super().__init__("Troll", level)
        self.hp += 15
        self.defense += 2

# Sous-classe Boss
class Zarek(Monster):
    def __init__(self, level):
        super().__init__("Zarek", level)
        self.hp += 20
        self.defense += 3
