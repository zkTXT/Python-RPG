import os

# Fonction pour effacer l'écran
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')