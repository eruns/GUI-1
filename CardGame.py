# from tkinter import *
import tkinter as tk
# from game import *


class Gofish(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)

        self.master = master
        self.init_window()
        # self.show_frame(PageOne)
        frame = self.frames[PageOne]
        frame.tkraise()
        #add_player to indicate turn



    def init_window(self):
        self.master.title("Go fish")

        self.pack(fill=tk.BOTH, expand=1)

        quitbutton = tk.Button(self, text="quit", command=quit)

        quitbutton.place(x=0, y=0)

        revealbutton = tk.Button(self, text="reveal", command=self.reveal)
        revealbutton.place(x=350, y=570)

        # submitbutton = tk.Button(self, text="submit", command=self.submit_request)

        self.player_turn()
        self.player_score()
        self.choose_player()
        self.choose_rank()
        # self.choose_suit()

    def player_turn(self):
        player = "p1"
        if player == "p1":
            turn = tk.Label(self, text = "player 1", relief = tk.SUNKEN)
            turn.place(x=300, y=575)
        elif player == "p2":
            turn = tk.Label(self, text = "player 2", relief = tk.SUNKEN)
            turn.place(x=300, y=575)
        elif player == "p3":
            turn = tk.Label(self, text = "player 3", relief = tk.SUNKEN)
            turn.place(x=300, y=575)
        elif player == "p4":
            turn = tk.Label(self, text = "player 4", relief = tk.SUNKEN)
            turn.place(x=300, y=575)
        else:
            pass

    def player_hand(self):
        player = "p2"
        if player == "p1":
            hand = [1, 2, 3 ,4 ,5]
            hnd = tk.Label(self, text = hand, relief = tk.RAISED)
            hnd.place(x=300, y=600)
        elif player == "p2":
            hand = [2,2, 2, 2, 2]
            hnd = tk.Label(self, text = hand, relief = tk.RAISED)
            hnd.place(x=300, y=600)
        elif player == "p3":
            hand = [8, 8, 9, 6, 7]
            hnd = tk.Label(self, text = hand, relief = tk.RAISED)
            hnd.place(x=300, y=600)
        elif player == "p4":
            hand = [7,7, 7, 7, 7]
            hnd = tk.Label(self, text = hand, relief = tk.RAISED)
            hnd.place(x=300, y=600)
        else:
            pass

    def choose_player(self):
        player_list = ["p1", "p2", "p3", "p4"]
        select_player = tk.StringVar()
        select_player.set(player_list[0])

        player_menu = tk.OptionMenu(self.master, select_player, *player_list, command=self.selected_player)
        player_menu.place(x=300, y=225)

    def selected_player(self, value):
        print(value)


    def choose_rank(self):
        rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
        select_rank = tk.StringVar()
        select_rank.set(rank_list[0])

        rank_menu = tk.OptionMenu(self.master, select_rank, *rank_list, command=self.selected_rank)
        rank_menu.place(x=300, y=255)

    def selected_rank(self, value):
        print(value)

    # def submit_request(self):


    # def choose_suit(self):
    #     suit_list = ["C", "D", "H", "S"]
    #     select_suit = tk.StringVar()
    #     select_suit.set(suit_list[0])
    #
    #     suit_menu = tk.OptionMenu(self.master, select_suit, *suit_list, command=self.selected_suit)
    #     suit_menu.place(x=300, y=285)

    def selected_suit(self, value):
        print(value)


    def player_score(self):
        title = tk.Label(self, text = "Player's Scores:", font=("Helvetica", 16))
        title.place(x= 300, y=50)
        players = 4
        if players == 2:
            player_1_points = 1
            player_2_points = 1

            player_1 = tk.Label(self, text ="player 1: " + str(player_1_points), relief = tk.RAISED)
            player_1.place(x=300, y = 100)
            player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
            player_2.place(x=450, y=100)

        elif players == 3:
            player_1_points = 1
            player_2_points = 1
            player_3_points = 1

            player_1 = tk.Label(self, text ="player 1:" + str(player_1_points), relief = tk.RAISED)
            player_1.place(x=300, y = 100)
            player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
            player_2.place(x=450, y=100)
            player_3 = tk.Label(self, text="player 3: " + str(player_3_points), relief=tk.RAISED)
            player_3.place(x=600, y=100)

        elif players == 4:
            player_1_points = 1
            player_2_points = 1
            player_3_points = 1
            player_4_points = 1

            player_1 = tk.Label(self, text ="player 1: " + str(player_1_points), relief = tk.RAISED)
            player_1.place(x=300, y = 100)
            player_2 = tk.Label(self, text="player 2: " + str(player_2_points), relief=tk.RAISED)
            player_2.place(x=450, y=100)
            player_3 = tk.Label(self, text="player 3: " + str(player_3_points), relief=tk.RAISED)
            player_3.place(x=600, y=100)
            player_4 = tk.Label(self, text="player 4: " + str(player_4_points), relief=tk.RAISED)
            player_4.place(x=750, y=100)
        else:
            pass

    def reveal(self):
        self.player_hand()

    def quit(self):
        exit()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x900")
    app = Gofish(root)
    root.mainloop()
