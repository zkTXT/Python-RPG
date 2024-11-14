from player import Player
from monster import Monster, Goblin, Troll, Zarek
import random
from utils import clear_screen

# Fonction de combat
def combat(player, monster):
    print(f"A \033[31m{monster.name}\033[0m of level {monster.level} appears!")
    
    is_boss_fight = isinstance(monster, Zarek)
    
    while player.hp > 0 and monster.hp > 0:
        clear_screen()
        print("\n====== Combat ======")
        print(f"\033[34m{player.name}\033[0m: {player.hp}/{player.max_hp} HP | \033[31m{monster.name}\033[0m: {monster.hp} HP")
        
        if is_boss_fight:
            action = input(" // 1- Attack // 2- Potion // 3- Boost ATT // 4- Boost DEF // ").lower()
        else:
            action = input(" // 1- Attack // 2- Potion // 3- Boost ATT // 4- Boost DEF // 5- Run // ").lower()

        if action == "1":
            damage = random.randint(player.attack - 2, player.attack + 2)
            monster.take_damage(damage)
            if not monster.is_alive():
                print(f"\033[31m{monster.name}\033[0m is defeated! You gain \033[34mXP\033[0m.")
                player.xp += monster.level * 20
                player.level_up()
                input("Press Enter to continue...")
                clear_screen()
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
        elif action == "5" and not is_boss_fight:
            print("You run away from the fight!")
            input("Press Enter to continue...")
            clear_screen()
            break
        else:
            print("Invalid choice, please select a valid action.")
            input("Press Enter to continue...")
            clear_screen()
            continue
        
        if monster.is_alive():
            damage = random.randint(monster.attack - 2, monster.attack + 2)
            player.take_damage(damage)
            if player.hp <= 0:
                print("You have died...")
                return False

        input("Press Enter to continue...")
        clear_screen()

    print(f"\033[34m{player.name}\033[0m is at level {player.level} with \033[34m{player.xp}\033[0m/100 \033[34mXP\033[0m.")
    input("Press Enter to continue...")
    player.reset_buffs()
    return True

# Fonction de game over
def game_over_screen():
    print("\n===== Game Over =====")
    print("Thanks for playing!")
    return False
