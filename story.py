import time
from utils import clear_screen

# ASCII Art du jeu
def display_ascii_art():
    ascii_art = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@: .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%. :@@@@@@@@
@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:@@            @@@@@@@@
@@@@@@@@@@    @@    @@          @@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-   @@@        *@   @    @@@ @@@@@@@@
@@@@@@@@@@*   @@@    @@@    @=    @@@           @@@@@@@@@     @@@@@      @@=                *@   @@@@  @*  @@   *@@@@@@@@@@@@
@@@@@@@@@@@   :@@    @@@@   @@@    @   @@@@@@   @@@@@@.   %@-    @@#   @@@@@@  @@@   @@@@@- @@   +@@@  @@@@@:   @@@@@@@@@@@@@
@@@@@@@@@@@        :@@@@@   *@:   @   %@@@@@@@ @@@@@@    @@@@@.   @#   @@@@@@  @@@   @@@.  @@@       @@@@@@@    @@@@@@@@@@@@@
@@@@@@@@@@@        :@@@@@        @@   %@@@@      @@@%   @@@@@@@   @#   @@@@@@  @@@         @@@@@@      @@@@@   -@@@@@@@@@@@@@
@@@@@@@@@@@    @*    @@@@   *@@@@@@    @@@@@@   @@@@#   @@@@@@@   @+   @@@@@@  @@@   @@@@ %@@  @@@@*   @@@@@   @@@@@@@@@@@@@@
@@@@@@@@@@@    @@@    *@@   =@@@@@@@    @@@@@   @@@@@    @@@@@+  =@@   @@@@@=  @@@   @@@@@  @  -@@@@   @@@@@   @@@@@@@@@@@@@@
@@@@@@@@@@       @@           %@@@@@@=     -    @@@@@@@    +=   @@@@#         @@@          .@         @@@@:      @@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  *@@@@@@@@@@@@:    .@@@@@@@@=  .#@@@@@%@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
    print("\033[31m" + ascii_art + "\033[0m")

# Classe Speech pour les dialogues
class Speech:
    def __init__(self, speaker, color, text_lines):
        self.speaker = speaker
        self.color = color
        self.text_lines = text_lines

    def speak(self):
        for line in self.text_lines:
            clear_screen()
            print(f"\033[{self.color}m{self.speaker}: {line}\033[0m")
            time.sleep(3)

# Discours du Vieil Homme
def old_man_speech():
    
    speech_lines = [
        "Ah, jeune héros, entends-tu le vent ? Il porte avec lui les échos d'un royaume perdu...",
        "Il y a bien des années, ce royaume prospérait sous le règne d'un roi sage et juste.",
        "Mais un jour, un mal ancien s'est éveillé. Un sorcier, assoiffé de pouvoir, a pris le contrôle de la région.",
        "Son nom... c'est Zarek, un être sans pitié, dont la seule ambition est de détruire tout ce qui est bon.",
        "Mais il y a une légende... une légende qui parle d'un héros ressuscité, destiné à le vaincre.",
        "Et ce héros, mon jeune ami, c'est toi. Toi qui es appelé à restaurer l'équilibre et sauver notre monde.",
        "Le chemin sera long, rempli de monstres et de dangers. Mais je sais que tu es prêt.",
        "Va, jeune héros, et porte l'espoir du royaume sur tes épaules. Le destin t'appelle..."
    ]
    old_man = Speech("Vieil homme", "35", speech_lines)
    old_man.speak()

# Discours du Narrateur
def narrator_intro():
    narrator_lines = [
        "Vous vous réveillez dans un endroit inconnu, les souvenirs flous de votre passé vous échappent..."
    ]
    narrator = Speech("Narrateur", "33", narrator_lines)
    narrator.speak()
