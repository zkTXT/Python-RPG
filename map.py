from utils import clear_screen

# Fonction pour dessiner la carte centrée sur la position du joueur
def draw_map(player_pos):
    grid_size = 7
    half_grid = grid_size // 2
    
    clear_screen()
    print("Map:")
    
    for y in range(player_pos[1] + half_grid, player_pos[1] - half_grid - 1, -1):
        row = ""
        for x in range(player_pos[0] - half_grid, player_pos[0] + half_grid + 1):
            if (x, y) == tuple(player_pos):
                row += f"\033[34m P \033[0m"
            elif (x, y) in game_map:
                row += f" {symbol_map[game_map[(x, y)]]} "
            else:
                row += " . "
        print(row)
    print("\nP: Player | .: Empty space\n")

# Fonction de mouvement du joueur avec vérification des limites
def move_player(player_pos, direction):
    new_pos = player_pos.copy()
    
    if direction == "z":
        new_pos[1] += 1
    elif direction == "s":
        new_pos[1] -= 1
    elif direction == "d":
        new_pos[0] += 1
    elif direction == "q":
        new_pos[0] -= 1
    
    if tuple(new_pos) in game_map:
        return new_pos
    else:
        print("You can't go any further in that direction.")
        return player_pos

game_map = {
    (0, 0): "Starting Point",
    
    # clearing
    (1, 0): "A bright clearing", (2, 0): "A bright clearing", (3, 0): "A bright clearing",
    (-1, 0): "A bright clearing", (-2, 0): "A bright clearing", (-3, 0): "A bright clearing",
    (0, 1): "A bright clearing", (0, 2): "A bright clearing", (0, 3): "A bright clearing",
    (0, -1): "A bright clearing", (0, -2): "A bright clearing", (0, -3): "A bright clearing",
    
    # Calm lakes
    (2, 1): "A calm lake", (1, 1): "A calm lake", (3, 1): "A calm lake",
    (1, 2): "A calm lake", (2, 2): "A calm lake", (3, 2): "A calm lake",
    (1, -1): "A calm lake", (2, -1): "A calm lake", (3, -1): "A calm lake",
    
    # Mystical ruins
    (0, 4): "A mysterious ruin", (1, 4): "A mysterious ruin", (2, 4): "A mysterious ruin",
    (0, -4): "A mysterious ruin", (1, -4): "A mysterious ruin", (2, -4): "A mysterious ruin",

    # Dark caves
    (-1, 1): "A dark cave", (-2, 1): "A dark cave", (-3, 1): "A dark cave",
    (-1, 2): "A dark cave", (-2, 2): "A dark cave", (-3, 2): "A dark cave",
    
    # Boss's lair
    (4, 1): "The boss's lair", (5, 1): "The boss's lair", (6, 1): "The boss's lair",
    (4, 2): "The boss's lair", (5, 2): "The boss's lair", (6, 2): "The boss's lair",
    (4, -1): "The boss's lair", (5, -1): "The boss's lair", (6, -1): "The boss's lair",

    # Enchanted forests and towers surrounding
    (1, 3): "Enchanted forest", (2, 3): "Enchanted forest", (3, 3): "Enchanted forest",
    (-1, -1): "Enchanted forest", (-2, -2): "Ancient tower ruins", (-3, -3): "Ancient tower ruins",
    
    # Graves and villages
    (-1, -3): "Old graveyard", (-2, -3): "Old graveyard", (-3, -3): "Old graveyard",
    (-1, -2): "Abandoned village", (-2, -2): "Abandoned village", (-3, -2): "Abandoned village",

    # marshlands, mountain passes, valleys
    (-4, 0): "Haunted marshlands", (-4, 1): "Haunted marshlands", (-4, -1): "Haunted marshlands",
    (4, 0): "Mountain pass", (4, 1): "Mountain pass", (4, -1): "Mountain pass",
    (0, 5): "Foggy valley", (1, 5): "Foggy valley", (-1, 5): "Foggy valley"
}


# Symboles sur la carte
symbol_map = {
    "Starting Point": "🚩",
    "A bright clearing": "🌾",
    "A calm lake": "🌊",
    "A dark cave": "⬛",
    "A mysterious ruin": "🏛",
    "The boss's lair": "🎃",
    "Enchanted forest": "🌲",
    "Ancient tower ruins": "🏰",
    "Old graveyard": "🪦",
    "Abandoned village": "🏚",
    "Haunted marshlands": "💀",
    "Mountain pass": "⛰️",
    "Foggy valley": "🌫️"
}
