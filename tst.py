from tkinter import *
import tkinter as tk
from tkinter import messagebox

from Game_orig import *
from Rules_orig import *
from Enums.Sort_Methods import *

class Root(tk.Tk):
    """Creates root window."""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("GoFIsh")
        self.geometry("900x600")

class MainMenu(tk.Menu):
    """Creates Main Menu."""

    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)

        file_menu = FileMenu(self, tearoff= 0)
        self.add_cascade(label="File", menu=file_menu)

        root.config(menu=self)

class FileMenu(tk.Menu):
    """Creates File menu."""

    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)

        self.add_command(label="Exit", command=root.quit)


class GoFish(Root, tk.Frame):
    """Class: Gui version of Go fish game

    METHODS:
        >>player_select_window(self)
            Creates the window to select number of players.

        >>init_window(self)
            creates window for interaction.

        >>set_player_count(self)
            function to gather onclick values.

        >>submit request(self)
            returns button results.

        >>reveal_button(self)
            reveals current players's hand.

        >>player_turn(self)
            Shows which player is playing.

        >>player_score(self)
        player score title label.

        >>player_score(self)
            shows all players scores.

        >> play_game(self)
            game logic.(borrowed from Game class.)

        >>choose_rank(self)
            buttons to choose which player to take a card from.

        >>rank_button_state(self)
            setting to prevent user from clicking rank before choosing player

        >>submit_rank(self)
            returns button click.

        >>submit_player(self)
            returns button click.

        >>choose_hand(self)
            temporary game logic function.

        >reveal(self)
            shows current players hands.

        >>quit(self)
            button used to quit Gui.

    """

    def __init__(self, root , *args, **kwargs):
        """initializing gui object."""
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.player_select_window()


    def set_player_count(self, player_count):
        """sets button click as player count."""
        self.player_count = player_count
        self.submit_request()


    def player_select_window(self):
        """window to select number of players"""
        self.master.title("Go fish")
        self.pack(fill=tk.BOTH, expand=1)
        self.button_list = []
        quitbutton = tk.Button(self, text="quit", command=quit)
        quitbutton.place(x=0, y=0)
        var1 = tk.IntVar()
        tk.Checkbutton(self, text='blah1', variable=var1)
        var2 = tk.IntVar()
        tk.Checkbutton(self, text='blah2', variable=var2)
        players = ( 2, 3, 4, 5)
        xx = 200
        for player in players:
            b = tk.Button(self.master, text= str(player) + ' Players',
                          command=lambda player=player: self.set_player_count(player))
            self.button_list.append(b)
            xx = xx + 65
            b.place(x=xx, y=255)

    def init_window(self):
        """Main window to interact game."""
        self.pack(fill="both", expand=1)
        self.players = self.player_select_window
        self.reveal_button()

        self.game = Game(hand_size=5,
                         hand_count=self.player_count,
                         max_hand_size=52,
                         discard_type=Visibility.INVISIBLE,
                         ace_rank=Rank.ACELOW)
        self.choose_rank()
        self.player_score()
        self.player_turn()
        # self.choose_hand(hand)
        self.choose_player()
        # self.player_hand()



    def submit_request(self):
        """submits players request."""
        tk.Frame.pack_forget(self)
        # print(self.player_count)
        for button in self.button_list:
            button.destroy()
        self.init_window()


    def reveal_button(self):
        """reaveals players hand"""
        revealbutton = tk.Button(self, text="reveal", command=self.reveal)
        revealbutton.place(x=350, y=570)

    def player_turn(self):
        """Indicates which players turn is playing"""
        # def player_score(
        # self):
        #     title = tk.Label(self, text=self.player_count, font=("Helvetica", 16))
        #     title.place(x=300, y=50)
        #     xx = 100
        #     count = 1
        #     for hand in self.game.hands:
        #         xx = xx + 150
        #
        #         player_points = self.game.hands[hand][1]
        #         player_label = tk.Label(self, text="player: " + str(count) + ": " + str(player_points),
        #                                 relief=tk.RAISED)
        #
        #         player_label.place(x=xx, y=100)
        #         count = count + 1
        # self.play_game()
        for hand in self.game.hands:

            turn = tk.Label(self, text=player, relief=tk.SUNKEN)
            turn.place(x=300, y=475)
            if hand == "hands0":
                turn = tk.Label(self, text="player 1", relief=tk.SUNKEN)
                turn.place(x=300, y=575)
            elif hand == "hands1":
                turn = tk.Label(self, text="player 2", relief=tk.SUNKEN)
                turn.place(x=300, y=575)
            elif hand == "hands2":
                turn = tk.Label(self, text="player 3", relief=tk.SUNKEN)
                turn.place(x=300, y=575)
            elif hand == "hands3":
                turn = tk.Label(self, text="player 4", relief=tk.SUNKEN)
                turn.place(x=300, y=575)
            else:
                pass

    def player_hand(self):
        """Displays current players hand."""

        for hand in Game.hands:
            player = Game.hands[hand][0]
        print(player)
        player = "p2"
        if player == "p1":
            hand = [1, 2, 3, 4, 5]
            hnd = tk.Label(self, text=hand, relief=tk.RAISED)
            hnd.place(x=300, y=600)
        elif player == "p2":
            hand = [2, 2, 2, 2, 2]
            hnd = tk.Label(self, text=hand, relief=tk.RAISED)
            hnd.place(x=300, y=600)
        elif player == "p3":
            hand = [8, 8, 9, 6, 7]
            hnd = tk.Label(self, text=hand, relief=tk.RAISED)
            hnd.place(x=300, y=600)
        elif player == "p4":
            hand = [7, 7, 7, 7, 7]
            hnd = tk.Label(self, text=hand, relief=tk.RAISED)
            hnd.place(x=300, y=600)
        else:
            pass

    # def selected_suit(self, value):
    #     print(value)

    def player_score_title(self):
        """Alerts players to where the scores are"""
        title = tk.Label(self, text="Player's Scores:", font=("Helvetica", 16))
        title.place(x=300, y=50)

    def player_score(self):
        """Shows current players score"""
        title = tk.Label(self, text=self.player_count, font=("Helvetica", 16))
        title.place(x=300, y=50)
        xx = 100
        count = 1
        for hand in self.game.hands:
            xx = xx + 85

            player_points = self.game.hands[hand][1]
            player_label = tk.Label(self, text="player: "+ str(count) + ": " + str(player_points), relief=tk.RAISED)

            player_label.place(x=xx, y=100)
            count = count + 1

    def play_game(self):
        """copied function to allow accesibility."""
        # hand = self.game.hands
        rules = Rules(self.game.deck, 0)
        same_player = True
        wincondition = False

        while wincondition == False:
            for hand in self.game.hands:
                same_player = True
                self.game.active_hand = self.game.hands[hand][0]
                while same_player == True:
                    print("you: %s" % hand)
                    choice = self.choose_hand(hand)
                    # choice = 'hand2'
                    print(self.game.active_hand)
                    self.game.hands[hand][0].visi_override()
                    if rules.play_game(self.game.hands[hand][0], self.game.hands[choice][0]) == False:
                        same_player = False
                        self.game.hands[hand][1] += rules.points
                    else:
                        self.game.hands[hand][1] += rules.points
                        same_player = True
                if self.game.empty_hands == self.game.hand_count:
                    wincondition = True

        for hand in self.game.hands:
            print(hand)
        print(self.game.active_hand)
        print(self.game.deck)
        rules = Rules(self.game.deck, 0)
        # choice = self.game.choose_hand(hand)
        # messagebox.showerror('Error!', self.game.active_hand)

    def choose_rank(self):
        """choose rank to ask for"""
        rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
        select_rank = tk.StringVar()
        select_rank.set(rank_list[0])
        self.rank_button_list = []
        nx = 275
        for rank in rank_list:
            b = tk.Button(self, text=rank, command=lambda rank=rank: self.submit_rank(rank))
            nx = nx + 35
            b.place(x=nx, y=200)
            self.rank_button_list.append(b)
        self.rank_button_state()

    def rank_button_state(self, state=DISABLED):
        """prevents  user from prematurely select rank values."""
        for button in self.rank_button_list:
            button.config(state=state)

    def submit_rank(self, r_value):
        """submit ranks values from button press."""
        self.selected_rank = r_value
        print(self.selected_rank)
        return (self.selected_rank)


    def choose_player(self):

        selected_player = tk.StringVar()
        selected_player.set("L")  # initialize
        nx = 300
        for i in range(0, self.player_count):
            player = i
            b = tk.Button(self, text="player " + str(i + 1), command=lambda player=player: self.submit_player(player))

            nx = nx + 75
            b.place(x=nx, y=150)

    def submit_player(self, p_value):
        """Submits player value."""
        self.selected_player = p_value
        print(self.selected_player)
        self.rank_button_state(state=NORMAL)
        # self.choose_hand(hand)
        return (self.selected_player)

    def show_players(self):
        print(self.game.hand)
        choice = self.choose_hand(self.game.hand)



    def choose_hand(self, active):
        """Gets the hand the player would like to request a card from
        RETURNS
            name (string): the name of the hand to be asked
        RAISES
            ValueError if name is not in self._hands
            ValueError if name is equal to the active hand
        """

        ask = True
        while ask == True:
            nx = 300
            i=0
            for hand in self.game.hands:
                def button_func(arg1):
                    pyvar.set(arg1)
                    self._choice = arg1
                    self.selected_player = arg1
                    self.rank_button_state(state=NORMAL)

                b = tk.Button(self, text="player " + str(i + 1), command=lambda player=i: button_func(player))
                nx = nx + 75
                b.place(x=nx, y=150)
                i += 1
                print(str(hand) + " = " + str(self.game.hands[hand][0]) + " --- points = " + str(self.game.hands[hand][1]))
            # choice = int(input("Enter the index of the hand you would like to ask"))
            choice = tk.Button(self, text="Choice", command=lambda arg1=3: button_func(arg1), state=NORMAL)
            # choice.place(x=120, y=120)
            pyvar = tk.IntVar(None)
            choice.wait_variable(pyvar)
            # choice = str(3)
            hand = "hands%s" % self._choice
            print('req ' + hand)

            if hand in active:
                print(ValueError("Cannot ask yourself for a card"))
                exit()

            elif self.game.hands[hand]:
                ask = False
                return hand

            else:
                print(ValueError("Cannot ask for a hand which does not exist"))

    def reveal(self):
        # self.player_hand()
        pass

    def quit(self):
        exit()


if __name__ == "__main__":
    root = Root()
    menu = MainMenu(root)
    gofish = GoFish(root)
    root.mainloop()
    gofish.game = Game(hand_size=5,
                     hand_count=gofish.player_count,
                     max_hand_size=52,
                     discard_type=Visibility.INVISIBLE,
                     ace_rank=Rank.ACELOW,
                     sort=Sort.RANKTHENSUITA)


