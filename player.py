from item import Potion, BoostATT, BoostDEF

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.base_attack = 10
        self.base_defense = 5
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.level = 1
        self.xp = 0
        self.inventory = {
            "Potion": Potion(1),
            "Boost ATT": BoostATT(1),
            "Boost DEF": BoostDEF(1)
        }
    
    def level_up(self):
        if self.xp >= 100:
            self.level += 1
            self.max_hp += 20
            self.base_attack += 5
            self.base_defense += 2
            self.attack = self.base_attack
            self.defense = self.base_defense
            self.xp = 0
            print(f"{self.name} levels up to {self.level}!")

    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense)
        print(f"{self.name} takes {max(0, damage - self.defense)} damage. HP left: {self.hp}")

    def use_item(self, item_name):
        item = self.inventory.get(item_name)
        if item:
            item.use(self)
        else:
            print(f"No {item_name} available!")

    def reset_buffs(self):
        self.attack = self.base_attack
        self.defense = self.base_defense
