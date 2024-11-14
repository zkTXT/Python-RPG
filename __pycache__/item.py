# Base Item class
class Item:
    def __init__(self, name, effect, amount=1):
        self.name = name
        self.effect = effect
        self.amount = amount

    def use(self, player):
        """Apply item effect to player. To be implemented in subclasses."""
        pass

class Potion(Item):
    def __init__(self, amount=1):
        super().__init__("Potion", "heal", amount)

    def use(self, player):
        if self.amount > 0:
            player.hp = min(player.max_hp, player.hp + 50)
            self.amount -= 1
            print(f"{player.name} uses a Potion and recovers health. Current HP: {player.hp}/{player.max_hp}")
        else:
            print("No potions left!")

class BoostATT(Item):
    def __init__(self, amount=1):
        super().__init__("Boost ATT", "increase attack", amount)

    def use(self, player):
        if self.amount > 0:
            player.attack += 5
            self.amount -= 1
            print(f"{player.name} uses an Attack Boost! Current attack: {player.attack}")
        else:
            print("No attack boosts left!")

class BoostDEF(Item):
    def __init__(self, amount=1):
        super().__init__("Boost DEF", "increase defense", amount)

    def use(self, player):
        if self.amount > 0:
            player.defense += 5
            self.amount -= 1
            print(f"{player.name} uses a Defense Boost! Current defense: {player.defense}")
        else:
            print("No defense boosts left!")
