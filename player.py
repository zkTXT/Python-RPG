from item import Potion, BoostATT, BoostDEF, CapeInvisibilite

# Classe pour le joueur
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
        self.invisibility_turns = 0
        self.inventory = {
            "Potion": Potion(1),
            "Boost ATT": BoostATT(1),
            "Boost DEF": BoostDEF(1),
            "Cape d'invisibilité": CapeInvisibilite(1)
        }

    # Fonction pour les stats apres une montée de niveau
    def level_up(self):
        if self.xp >= 100:
            self.level += 1
            self.max_hp += 20
            self.base_attack += 5
            self.base_defense += 2
            self.attack = self.base_attack
            self.defense = self.base_defense
            self.xp = 0
            print(f"\033[34m{self.name}\033[0m levels up to {self.level}!")

    def take_damage(self, damage):
        # Only take damage if invisibility is not active
        if self.invisibility_turns == 0:
            self.hp -= max(0, damage - self.defense)
            print(f"\033[34m{self.name}\033[0m takes \033[31m{max(0, damage - self.defense)}\033[0m damage. HP left: \033[32m{self.hp}\033[0m")
        else:
            print(f"\033[34m{self.name}\033[0m is invisible and evades the attack!")

    def use_item(self, item_name):
        item = self.inventory.get(item_name)
        if item:
            item.use(self)
            if item_name == "Cape d'invisibilité":
                self.invisibility_turns = 3
        else:
            print(f"No {item_name} available!")

    # Fonction pour que les item de buff annulent leur effet apres un combat
    def reset_buffs(self):
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.invisibility_turns = 0