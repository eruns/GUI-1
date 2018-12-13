from tkinter import *
import tkinter as tk
from Game import *


class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("GoFIsh")
        self.geometry("700x500")

class MainMenu(tk.Menu):

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


class GoFish(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.player_select_window()


    def player_select_window(self):
        self.master.title("Go fish")

        self.pack(fill=tk.BOTH, expand=1)

        self.button_list = []

        # quitbutton = tk.Button(self, text="quit", command=quit)
        # quitbutton.place(x=0, y=0)


        var1 = tk.IntVar()
        tk.Checkbutton(self, text='blah1', variable=var1)
        var2 = tk.IntVar()
        tk.Checkbutton(self, text='blah2', variable=var2)
        players = ( 2, 3, 4)
        xx = 200
        for player in players:
            b = tk.Button(self.master, text= str(player) + ' Players',
                          command=lambda player=player: self.set_player_count(player))
            self.button_list.append(b)
            xx = xx + 85
            b.place(x=xx, y=255)




    def set_player_count(self, player_count):
        self.player_count = player_count
        self.submit_player_count_request()

    def submit_player_count_request(self):
        tk.Frame.pack_forget(self)
        for button in self.button_list:
            button.destroy()
        self.init_window()

    def init_window(self):

        self.pack(fill="both", expand=1)
        self.players = self.player_select_window
        self.game = Game(hand_size=5,
                         hand_count=self.player_count,
                         max_hand_size=52,
                         discard_type=Visibility.INVISIBLE,
                         ace_rank=Rank.ACELOW)
        self.reveal_button()
        # self.player_turn()
        self.player_scores()
        # self.game = Game(hand_size=5, hand_count=self.player_count, max_hand_size=52, discard_type=Visibility.INVISIBLE,
        #             ace_rank=Rank.ACELOW)
        self.choose_player()
        self.choose_rank()
        # self.player_hand()

    def reveal_button(self):
        revealbutton = tk.Button(self, text="reveal", command=self.reveal)
        revealbutton.place(x=350, y=370)

    def player_scores(self):
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

    def submit_player(self, p_value):
        self.selected_player = p_value

        self.rank_button_state(state=NORMAL)

        if self.game.active_hand == None:
            self.game.active_player_id = 0
            self.game.active_hand = self.game.hands['hands' + str(self.game.active_player_id)][0]

        if self.game.active_hand == self.game.hands['hands' + str(p_value)][0]:
            print("Same Player")
        else:
            self.game.asked_player_id = p_value
            self.game.asked_player_hand = self.game.hands['hands' + str(self.game.asked_player_id)][0]
            self.game.active_hand.visi_override()
            self.game.asked_player_hand.visi_override()
        # print(self.game.active_hand.card_count)
        # exit(0)
        selected_player_hand = self.game.choose_hand('hands' + str(self.game.active_hand), p_value)
        if selected_player_hand == False:
            # Hand does not exist
            message = "Hand does not exist"
            pass
        elif selected_player_hand == -1:
            # Can't ask a card from yourself
            message = "Can't ask a card from yourself"
            pass
        else:
            message = ""
            pass

        if message != "":
            print(message)

        # print( 'selected_player_hand: ' + str(selected_player_hand))
        return(self.selected_player)

    def submit_rank(self, r_value):
        self.game.asked_rank = r_value
        print(self.game.asked_rank)

        answer = self.game.ask(self.game.asked_player_hand, self.game.asked_rank)

        print(answer)

        return(self.game.asked_rank)

    def choose_player(self):

        selected_player = tk.StringVar()
        selected_player.set("L")  # initialize
        nx = 300
        for i in range(0, self.player_count):
            player = i
            b = tk.Button(self, text="player " + str(i+1), command=lambda player=player: self.submit_player(player))

            nx = nx + 75
            b.place(x=nx, y=150)

    def choose_rank(self):
        rank_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        select_rank = tk.StringVar()
        select_rank.set(rank_list[0])
        self.rank_button_list = []
        nx = 275
        for rank in rank_list:
            b = tk.Button(self, text=rank,  command=lambda rank=rank: self.submit_rank(rank))
            nx = nx + 35
            b.place(x=nx, y=200)
            self.rank_button_list.append(b)
        self.rank_button_state()

    def rank_button_state(self, state=DISABLED):
        for button in self.rank_button_list:
            button.config(state=state)





    def selected_suit(self, value):
        print(value)

    def player_score_title(self):
        title = tk.Label(self, text="Player's Scores:", font=("Helvetica", 16))
        title.place(x=300, y=50)

    # def player_score(self):
    #     title = tk.Label(self, text=self.player_count, font=("Helvetica", 16))
    #     title.place(x=300, y=50)
    #
    #     players = 2
    #
    #     if players == 2:
    #         player_1_points = 1
    #         player_2_points = 1
    #
    #         player_1 = tk.Label(self, text="player 1: " + str(player_1_points), relief=tk.RAISED)
    #         player_1.place(x=300, y=100)
    #         player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
    #         player_2.place(x=450, y=100)
    #
    #     elif players == 3:
    #         player_1_points = 1
    #         player_2_points = 1
    #         player_3_points = 1
    #
    #         player_1 = tk.Label(self, text="player 1:" + str(player_1_points), relief=tk.RAISED)
    #         player_1.place(x=300, y=100)
    #         player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
    #         player_2.place(x=450, y=100)
    #         player_3 = tk.Label(self, text="player 3: " + str(player_3_points), relief=tk.RAISED)
    #         player_3.place(x=600, y=100)
    #
    #     elif players == 4:
    #         player_1_points = 1
    #         player_2_points = 1
    #         player_3_points = 1
    #         player_4_points = 1
    #
    #         player_1 = tk.Label(self, text="player 1: " + str(player_1_points), relief=tk.RAISED)
    #         player_1.place(x=300, y=100)
    #         player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
    #         player_2.place(x=450, y=100)
    #         player_3 = tk.Label(self, text="player 3: " + str(player_3_points), relief=tk.RAISED)
    #         player_3.place(x=600, y=100)
    #         player_4 = tk.Label(self, text="player 4: " + str(player_4_points), relief=tk.RAISED)
    #         player_4.place(x=750, y=100)
    #     else:
    #         pass

    # def play_game(self):
    #

    def reveal(self):
        h = self.game.hands['hands' + str(self.game.active_player_id)]
        hnd = h[0].get_hand()
        hand = tk.Label(self, text=str(hnd), relief=tk.SUNKEN)
        hand.place(x=350, y=400)
        print(hnd)

    def quit(self):
        exit()

if __name__ == "__main__":
    root = Root()
    menu = MainMenu(root)
    gofish = GoFish(root)
    root.mainloop()
