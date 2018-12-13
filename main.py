from Game import *
from Enums.Visibility import *
from Enums.Rank import *
from Gui import *


def main():
    """Runs main program logic"""
    root = Root()
    menu = MainMenu(root)
    gofish = GoFish(root)
    root.mainloop()
    game = Game(hand_size=5, hand_count=None, max_hand_size=52, discard_type=Visibility.INVISIBLE, ace_rank=Rank.ACELOW)
    game.hand_count = gofish.player_count
    print(game.hand_count)
    game.control_players()



main()