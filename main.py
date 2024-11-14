from player import Player
from item import Item, Potion, BoostATT, BoostDEF
from monster import Monster, Goblin, Troll, Gio
import random
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game map
game_map = {
    (0, 0): "Starting Point",
    (1, 0): "A bright clearing",
    (0, 1): "A calm lake",
    (-1, 0): "A dark cave",
    (0, -1): "A mysterious ruin",
    (2, 0): "The boss's lair"
}

# Player movement
def move_player(player_pos, direction):
    if direction == "z":  # Up
        player_pos[1] += 1
    elif direction == "s":  # Down
        player_pos[1] -= 1
    elif direction == "d":  # Right
        player_pos[0] += 1
    elif direction == "q":  # Left
        player_pos[0] -= 1
    return player_pos

# Combat function
def combat(player, monster):
    print(f"A {monster.name} of level {monster.level} appears!")
    
    while player.hp > 0 and monster.hp > 0:
        print("\n====== Combat ======")
        print(f"{player.name}: {player.hp}/{player.max_hp} HP | {monster.name}: {monster.hp} HP")
        
        action = input(" // 1- Attack // 2- Potion // 3- Boost ATT // 4- Boost DEF // 5- Run // ").lower()
        
        if action == "1":
            damage = random.randint(player.attack - 2, player.attack + 2)
            monster.take_damage(damage)
            if not monster.is_alive():
                print(f"{monster.name} is defeated! You gain XP.")
                player.xp += monster.level * 20
                player.level_up()
                input("Press Enter to continue...")
                break
        elif action == "2":
            player.use_item("Potion")
            input("Press Enter to continue...")
        elif action == "3":
            player.use_item("Boost ATT")
            input("Press Enter to continue...")
        elif action == "4":
            player.use_item("Boost DEF")
            input("Press Enter to continue...")
        elif action == "5":
            print("You run away from the fight!")
            input("Press Enter to continue...")
            break
        
        if monster.is_alive():
            damage = random.randint(monster.attack - 2, monster.attack + 2)
            player.take_damage(damage)
            if player.hp <= 0:
                print("You have died...")
                return False

        input("Press Enter to continue...")
        clear_screen()

    print(f"End of combat! {player.name} is at level {player.level} with {player.xp}/100 XP.")
    input("Press Enter to continue...")
    player.reset_buffs()
    return True

# Game over screen
def game_over_screen():
    print("\n===== Game Over =====")
    print("Thanks for playing!")
    return False

# Main game function
def play_game():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    player_pos = [0, 0]
    
    while True:
        clear_screen()
        print(f"\nYou are at: {game_map.get(tuple(player_pos), 'An unknown place')}")

        if tuple(player_pos) == (2, 0):
            print("You enter the boss's lair!")
            boss = Gio(2)
            if not combat(player, boss):
                game_over_screen()
                return False
            else:
                print("You have defeated the boss and won the game!")
                return False
        
        direction = input("Move with Z (up), S (down), Q (left), D (right): ").lower()
        player_pos = move_player(player_pos, direction)
        
        if tuple(player_pos) == (0, 0):
            continue
        
        event = random.choice(["monster", "item", "nothing"])
        if event == "monster":
            monster_type = random.choice([Goblin, Troll])
            monster = monster_type(random.randint(1, player.level))
            if not combat(player, monster):
                game_over_screen()
                return False
        elif event == "item":
            item = random.choice(["Potion", "Boost ATT", "Boost DEF"])
            print(f"You find an item: {item}")
            player.inventory[item].amount += 1
            input("Press Enter to continue..."); clear_screen()
        else:
            print("Nothing happens here...")
            input("Press Enter to continue..."); clear_screen()

# Main game loop
while True:
    choice = input("1. New Game\n2. Quit\nYour choice: ")
    if choice == "1":
        if not play_game():
            break
    elif choice == "2":
        print("Thanks for playing!")
        break
