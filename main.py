from map import game_map, symbol_map, draw_map, move_player
from utils import clear_screen
from player import Player
from item import Item, Potion, BoostATT, BoostDEF
from monster import Monster, Goblin, Troll, Zarek
from story import display_ascii_art, old_man_speech, narrator_intro
from combat import combat, game_over_screen
import random
import time
import os

# Fonction de game over
def game_over_screen():
    print("\n===== Game Over =====")
    print("Thanks for playing!")
    return False

# Fonction principale du jeu
def play_game():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    player_pos = [0, 0]
    
    # Introduction du narrateur
    narrator_intro()
    
    # Discours du vieil homme
    old_man_speech()

    while True:
        draw_map(player_pos)
        print(f"\nYou are at: {game_map.get(tuple(player_pos), 'An unknown place')}")

        if tuple(player_pos) == (5, 2):
            print("You enter the boss's lair!")
            boss = Zarek(2)
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

# Boucle principale du jeu
while True:
    clear_screen()
    display_ascii_art()
    choice = input("1. New Game\n2. Quit\nYour choice: ")
    if choice == "1":
        if not play_game():
            break
    elif choice == "2":
        print("Thanks for playing!")
        break
