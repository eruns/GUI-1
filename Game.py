# use __repr__ for debugging of __str__ and __add__
"""Authors: Joanna Kus and Tristan Blus
    cool game file lets you do cool things like play card games
"""
from Enums.Rank import *
from Hand import *
from Deck import *
from Rules import *
from Enums.Sort_Methods import *
from Error import *
import GameTest
import unittest


class Game(object):
    """CLASS: Stores information about the whole game and controls it.

    METHODS:
        >> sort_method(self)
            Gets the sort type of the hand.

        >> empty_hands(self)
            Counts the number of empty hands.

        >> active_hand(self)
            Gets the currently playing hand.

        >> init_hand_size(self)
            Gets number of cards in a hand at the start of the game.

        >> init_hand_size(self, handsize)
            Sets number of cards in a hand at the start of the game.

        >> hand_count(self)
            Gets number of hands in the game.

        >> hand_count(self, handcount)
            Sets number of hands in the game.

        >> max_hand_size(self)
            Gets maximum number of allowed cards in a hand.

        >> max_hand_size(self, handsize)
            Sets maximum number of allowed cards in a hand.

        >> hands(self)
            Gets dictionary of hands in the game.

        >> ace_rank(self)
            Gets the game's ace rank.

        >> ace_rank(self, acerank)
            Sets the game's ace rank.

        >> discard_type(self)
            Gets the discard pile's visibility.

        >> discard_type(self, discardtype)
            Sets the discard pile's visibility.

        >> deck(self)
            Gets the active deck object.

        >> __init__(self, hand_size = 0, hand_count = 0, max_hand_size = 0, ace_rank = None, discard_type = None, sort = None)
            Initializes the game object.

        >> control_players(self)
            Executes main control flow for player turns.

        >> get_player_ask(self, active)
            Gets the hand the player wants to request a card from.
    """

    @property
    def sort_method(self):
        """GETTER: gets the sort type of the hand

        RETURNS
            @sort_type (Sort): the way cards will be sorted
        """
        return self._sort

    @property
    def log_file_name(self):
        """GETTER: gets the file name for the current log file

        RETURNS
            @_log_file: the name of the file to be logged in
        """
        return self._log_file

    @property
    def empty_hands(self):
        """GETTER: Counts the number of hands that are empty

        RETURNS
            @count (int): the number of empty hands in the set of self._hands
        """
        for hand in self._hands:
            if self.hands[hand][0].card_count == 0:
                self._empty_hands += 1
        return self._empty_hands

    @property
    def active_hand(self):
        """GETTER: Returns the hand which is currently playing

        RETURNS
            @active (Hand): The hand currently playing
        """
        return self._active

    @property
    def init_hand_size(self):
        """GETTER: Returns the number of cards in the hand to start the game

        RETURNS
            @init_hand_size (int): the number of cards in the hand to start the game
        """
        return self._init_hand_size

    @init_hand_size.setter
    def init_hand_size(self, handsize):
        """SETTER: Sets the number of cards in the hand to start the game

        PARAMETERS
            @handsize (int): integer count of cards per hand to start a game

        RAISES
            TypeError if init hand size is not an integer
        """
        try:
            handsize = int(handsize)
            self._init_hand_size = handsize

        except:
            Error.log_error(sys.exc_info()[1], "Game.init_hand_size")

    @property
    def hand_count(self):
        """GETTER: Returns the number of hands in the game

        RETURNS
            @count (int): the number of hands to be generated for self._hands
        """
        return self._hand_count

    @hand_count.setter
    def hand_count(self, handcount):
        """SETTER: Sets the number of cards in the hand to start the game

        PARAMETERS
            @handcount (int): integer count of hands in self._hands to start a game

        RAISES
            TypeError if handcount is not an integer
        """
        try:
            handcount = int(handcount)
            self._hand_count = handcount
        except:
            Error.log_error(sys.exc_info()[1], "Game.hand_count")

    @property
    def max_hand_size(self):
        """GETTER: Returns the maximum number of cards allowed per hand

        RETURNS
            @max_hand_size (int): the maximum number of cards in a hand
        """
        return self._max_hand_size

    @max_hand_size.setter
    def max_hand_size(self, handsize):
        """SETTER: Sets the maximum number of cards allowed per hand

        PARAMETERS
            @handsize (int): integer maximum number of cards in a hand

        RAISES
            TypeError if hand size is not an integer
        """
        try:
            handsize = int(handsize)
            self._max_hand_size = handsize
        except:
            Error.log_error(sys.exc_info()[1], "Game.max_hand_size")

    @property
    def hands(self):
        """GETTER: Returns the dictionary of hands in the game

        RETURNS
            @hands (Dictionary): hand name as the key, and a list of the hand
                    and the player's score as the value
        """
        return self._hands

    @property
    def ace_rank(self):
        """GETTER: Gets the ace rank to be used for the game

        RETURNS
            @ace_rank (Rank): determines whether ace will be ACELOW or ACEHIGH
        """
        return self._acerank

    @ace_rank.setter
    def ace_rank(self, acerank):
        """SETTER: Sets the ace rank to be used for the game

        PARAMETERS
            @acerank (Rank): rank value of Rank.ACEHIGH or Rank.ACELOW

        RAISES
            TypeError if acerank is not of type Rank

            >>
        """
        try:
            assert type(AceRank) == Rank
            self._acerank = acerank
        except:
            Error.log_error(sys.exc_info()[1], "Game.init_hand_size")

    @property
    def discard_type(self):
        """GETTER: gets the type of visibility for the discard pile for the game

        RETURNS
            discard_type (Visibility): the visibility of the discard pile
        """
        return self._discard_type

    @discard_type.setter
    def discard_type(self, discardtype):
        """SETTER: Sets the type of visibility for the discard pile

        PARAMETERS
            discardtype (Visibility): the visibility for the discard pile

        RAISES
            TypeError if discardtype is not Visibility
        """
        try:
            assert type(discardtype) == Visibility
            self._discard_type = discardtype

        except:
            Error.log_error(sys.exc_info()[1], "Game.discard_type")

    @property
    def deck(self):
        """GETTER: Returns the active deck object for the game instantiation

        RETURNS
            @deck (Deck): The deck object which the game will use
        """
        return self._deck

    def __init__(self, hand_size=0, hand_count=0, max_hand_size=0, ace_rank=None, discard_type=None, sort=None):
        """Initializes the game object"""
        self._init_hand_size = 0
        self._hand_count = 0
        self._max_hand_size = 52
        self._acerank = Rank.ACELOW
        self._discard_type = Visibility.INVISIBLE
        self._hands = []
        self._deck = []
        self._empty_hands = 0
        self._active = None
        self._sort = Sort.SUITTHENRANKD
        self._log_file = Error.log_error("Game initalized", "Game.__init__")

        """Instantiating properties"""
        if hand_size != 0 and type(hand_size) == int:
            self._init_hand_size = hand_size

        if hand_count != 0 and type(hand_count) == int:
            self._hand_count = hand_count

        if max_hand_size != 0 and type(max_hand_size) == int:
            self._max_hand_size = max_hand_size

        if ace_rank != None and type(ace_rank) == Rank:
            self._acerank = ace_rank

        if discard_type != None and type(discard_type) == Visibility:
            self._discard_type = discard_type

        if sort != None and type(sort) == Sort:
            self._sort = sort

        """Building the deck"""
        deck = Deck(ace_rank=self.ace_rank)
        self._deck = deck
        deck.shuffle()
        temp_hands = {}

        """Dealing the hands"""
        if self._hand_count != 0 and self._hands == []:
            for i in range(self.hand_count):
                hand = Hand(visibility=self.discard_type, sort=self.sort_method)
                for j in range(self.init_hand_size):
                    card = deck.deal()
                    hand.add_card(card)
                name = "hands%s" % i
                score = 0
                temp_hands[name] = [hand, score]
            self._hands = temp_hands

    def control_players(self):
        """Executes main control flow for player turns

        RAISES
            Exception if one occurs
        """
        try:
            rules = Rules(self.deck, 0)
            same_player = True
            wincondition = False

            while wincondition == False:
                for hand in self.hands:
                    same_player = True
                    self._active = self.hands[hand][0]
                    while same_player == True:
                        print("you: %s" % hand)
                        choice = self.choose_hand(hand)
                        self.hands[hand][0].visi_override()
                        if rules.play_game(self.hands[hand][0], self.hands[choice][0]) == False:
                            same_player = False
                            self.hands[hand][1] += rules.points
                        else:
                            self.hands[hand][1] += rules.points
                            same_player = True
                    if self.empty_hands == self.hand_count:
                        wincondition = True
        except:
            Error.log_error(sys.exc_info()[1], "Game.control_players()")

    def choose_hand(self, active):
        """Gets the hand the player would like to request a card from

        RETURNS
            name (string): the name of the hand to be asked

        RAISES
            ValueError if name is not in self._hands
            ValueError if name is equal to the active hand
        """
        try:
            ask = True
            while ask == True:
                for hand in self.hands:
                    print(str(hand) + " = " + str(self.hands[hand][0]) + " --- points = " + str(self.hands[hand][1]))
                choice = int(input("Enter the index of the hand you would like to ask"))
                hand = "hands%s" % choice
                if hand in active:
                    print("Cannot ask yourself for a card")

                elif self._hands[hand]:
                    ask = False
                    return hand

                else:
                    print("Cannot ask for a hand which does not exist")
        except:
            Error.log_error(sys.exc_info()[1], "Game.choose_hand()")


def main():
    print("Unit test: \n")
    suite = unittest.TestLoader().loadTestsFromModule(GameTest)
    unittest.TextTestRunner().run(suite)
    game = Game(hand_size=5,
                hand_count=4,
                max_hand_size=52,
                discard_type=Visibility.INVISIBLE,
                ace_rank=Rank.ACELOW,
                sort=Sort.RANKTHENSUITA)
    game.control_players()


if __name__ == '__main__':
    main()
