from Card import *
from Enums.Suit import *
from Enums.Rank import *
from Enums.Visibility import *
from Enums.Sort_Methods import *
import HandTest
import unittest
from Error import *


class Hand(object):
    """The Hand class, collects the cards included in a hand and stores them in
    an array allowing a user to manipulate the hand

    METHODS
        >> __init__(self, visibility, sort)
            initializes a Hand with a given visibility and sort method

        >>__add__(self):
            allows for implicit adding of cards, lists of cards, and hands to hands

        >> __str__(self)
            handles proper printing of the discard pile object

        >> add_card(self, card)
            adds the designated card to the hand

        >> remove_card(self, card = None, index = None)
            removes the designated card from hand, can be designated by card or
            index

        >> play_card(self, card = None, index = None)
            in some games, places card in play, can be designated by card or index

        >> evaluate_hand(self)//Legacy, not used
            evaluates the value of a hand in games where hand comparison is key

        >> visi_override(self)
            overides the visibility hiding to print a "hidden" hand

        >> count_rank(self, rank)
            counts the number of cards in the hand of a given rank

        >> count_suit(self, suit)
            counts the number of cards in the hand of a given suit

        >> find_and_remove(self, request)
            where request is either a rank or suit, finds all cards of that rank/suit
            and removes them from the hand

        >> compare_hand(self, hand)//Legacy, not used
            compares this hand to another hand object and returns the better hand

        >> __validate_card(self, card)//Legacy, not used
            validates each card passed to the hand is a legitimate card object

        >> __sort_cards(self)
            sorts the cards in the hand by suit and by rank within suit


    SUBCLASSES
        >> Discard_Pile(Hand)
            serves as a specialized subclass used for a discard pile.
    """

    def __init__(self, visibility=None, sort=None):
        """Creates an empty Hand object"""
        self._card_count = 0
        self._cards = []
        self._visibility = None
        self._sort_type = None

        if type(sort) == Sort:
            self._sort_type = sort

        if type(visibility) == Visibility:
            self.isvisible = visibility
        elif visibility == None:
            self._visibility = Visibility.VISIBLE
        else:
            Error.log_error(TypeError("TypeError: Visibility must be in visibility enum"), "Hand.__init__")

    def __add__(self, to_add):
        """Creates adding functionality between hands and hands, hands and cards"""
        hand = Hand()
        if type(to_add) == Hand:
            temp_list = []
            temp_list.append(to_add.cards)
            temp_list.append(self._cards)
            for card in temp_list:
                hand.add_card(card)

        elif type(to_add) == Card:
            hand.add_card(to_add)

        elif type(to_add) == list:
            for item in to_add:
                if type(item) == Card:
                    hand.add_card(item)
                else:
                    Error.log_error("Value Error: items in list must be cards, got %s" % type(item), "hand.__add__")

        return hand

    def __str__(self):
        """Handles print formatting for the Hand class"""
        if self.isvisible.name == "VISIBLE":
            temp_string = "("
            for card in self._cards:
                temp_string += "%s, " % str(card)
            temp_string = temp_string.rstrip(", ")
            temp_string += ")"


        elif self.isvisible.name == "TOPVISIBLE":
            temp_string = ""
            temp_string += str(self._cards[0])


        elif self.isvisible.name == "INVISIBLE":
            temp_string = "Hand INVISBLE"

        return temp_string

    @property
    def card_count(self):
        """GETTER: gets the number of cards in the hand

        RETURNS
            @card_count (int): the number of cards in the hand
        """
        return len(self._cards)

    @property
    def sort_type(self):
        """GETTER: gets the sort type of the hand

        RETURNS
            @sort_type (Sort): the way cards will be sorted
        """
        return self._sort_type

    @property
    def cards(self):
        """GETTER: gets the array of cards in the hand

        RETURNS
            @cards (array): the array of cards in the hand
        """
        return self._cards

    @property
    def isvisible(self):
        """GETTER: Gets the enum determining hand visibility

        RETURNS
            @isvisible (enum Visibility): the visibility of the given hand

        """
        return self._visibility

    @isvisible.setter
    def isvisible(self, visibility):
        """SETTER: Sets the isvisible property

        PARAMETERS
            @visibility (VISIBILITY): Enum to set visibility
        """
        if type(visibility) == Visibility:
            self._visibility = visibility
        else:
            Error.log_error(ValueError("Value Error: visibility must be of type Visibility"), "Hand.isvisible.setter")

    def add_card(self, card):
        """adds a specified card to the hand

        PARAMETERS
            @card (card): the card to be added to the hand

        RAISES
            ValueError if card is not a card type object with a legitimate suit and
             rank
        """
        if type(card) == Card:
            self._cards.append(card)
            self.__sort_cards()
        elif type(card) == list:
            for new_card in card:
                self._cards.append(new_card)
            self.__sort_cards()
        else:
            Error.log_error(ValueError("ValueError: cannot enter both an array and a single card"), "Hand.add_card()")

    def remove_card(self, card=None, index=None):
        """discards a card from the hand

        PARAMETERS
            @card (card): specified card to be removed
            @index (card): index of card to be removed

        RAISES
            TypeError if both card and index are input

        """
        if card != None and index != None:
            Error.log_error(
                TypeError("TypeError: Either choose the index to remove OR the card to remove, both chosen"),
                "Hand.remove_card")
        elif card != None:
            print(self._cards)
            print(card)
            self._cards.remove(card)
            self.__sort_cards()
        elif index != None:
            del self._cards[index]
            self.__sort_cards()
        elif index == None and card == None:
            Error.log_error(
                TypeError("TypeError: Either choose the index to remove OR the card to remove, neither chosen"),
                "Hand.remove_card")

    def get_hand(self):
        """Overrides the visibility of a hand to allow it to print when needed

        PARAMETERS
            None

        RETURNS
            None
        """
        self.__sort_cards()
        temp_list = []
        for card in self.cards:
            temp_list.append(str(card.rank)+str(card.suit))
        return temp_list

    def visi_override(self):
        """Overrides the visibility of a hand to allow it to print when needed

        PARAMETERS
            None

        RETURNS
            None
        """
        self.__sort_cards()
        temp_string = "Your Hand = "
        for card in self.cards:
            temp_string += "%s%s " % (card.rank, card.suit)
        print(temp_string.strip(','))

    def play_card(self, card):
        """Places a card in play for applicable games

        PARAMETERS
            @card (Card): card to be placed in play

        RAISES
            ValueError if card is not in hand
        """
        if type(card) == Card:
            if card not in self._cards:
                Error.log_error(ValueError("ValueError: Card %s %s is not in this hand" % (card.rank, card.suit)),
                                "Hand.play_card")
            else:
                self.remove_card(card)
                return card
        elif type(card) == int:
            return self._cards.pop(card)

    def count_rank(self, rank):
        """Counts the number of cards of a given rank in hand

        PARAMETERS
            @rank (Rank): rank to be checked for

        RETURNS
            @count (int): the number of cards matching the input rank
        """
        count = 0
        for card in self.cards:
            if card.rank == rank:
                count += 1
        return count

    def count_suit(self, suit):
        """Counts the number of cards of a given suit in hand

        PARAMETERS
            @suit (Suit): suit to be checked for

        RETURNS
            @count (int): the number of cards matching the input rank
        """
        try:
            count = 0
            for card in self.cards:
                if card.suit == suit:
                    count += 1
            return count
        except:
            Error.log_error(sys.exc_info()[1], "Hand.count_suit()")

    def find_and_remove(self, request):
        """Counts the number of cards of a given suit or rank in hand and removes them

        PARAMETERS
            @requests (Suit or Rank): suit or rank to be checked for and remove

        """
        temp_list = []
        if type(request) == Suit:
            for card in self.cards:
                if card.suit == request:
                    self.remove_card(card)

        elif type(request) == Rank:
            for card in self.cards:
                if card.rank == request:
                    self.remove_card(card)

        else:
            Error.log_error(ValueError("card requests must be rank or suit not %s" % request), "Hand.find_and_remove()")

    def evaluate_hand(self, hands, scale):
        """Evaluates the value of a hand for applicable games

        PARAMETERS
            @hands (dictionary (list values)): the possible hands for the game
            @scale (dict): the relative values of the hands in hands(dict)

        RETURNS
            @value (int): the value of the hand as defined by the game rules
        """
        try:
            for key, value in hands:
                if self._cards == value:
                    return scale.get(key)
        except:
            Error.log_error(sys.exc_info()[1], "Hand.evaluate_hand")

    def compare_hand(self, hand):
        """Compares the value of one hand to the value of another

        PARAMETERS
            @hand (Hand): the hand for this hand to be compared to

        RETURNS
            @higher (Hand): the hand with the higher value

        RAISES
            ValueError if hand is not a legitimate Hand object
        """
        try:
            if this_hand > that_hand:
                return self._cards
            elif this_hand < that_hand:
                return hand
            else:
                return "Equal"
        except:
            Error.log_error(sys.exc_info()[1], "Hand.compare_hand")

    def __sort_cards(self):
        """The sort cards function sorts the hand exclusively by rank

        RAISES
            ValueError if any errors occur in sorting
        """
        try:
            if self.sort_type == Sort.RANKTHENSUITA:
                self._cards = sorted(self._cards, key=lambda card: (card.rank.value, card.suit.value))
            elif self.sort_type == Sort.SUITTHENRANKA:
                self._cards = sorted(self._cards, key=lambda card: (card.suit.value, card.rank.value))
            elif self.sort_type == Sort.SUITTHENRANKD:
                self._cards = sorted(self._cards, key=lambda card: (card.suit.value, card.rank.value), reverse=True)
            elif self.sort_type == Sort.RANKTHENSUITD:
                self._cards = sorted(self._cards, key=lambda card: (card.rank.value, card.suit.value), reverse=True)
            else:
                self._cards = sorted(self._cards, key=lambda card: (card.suit.value, card.rank.value), reverse=True)


        except:
            Error.log_error(sys.exc_info()[1], "Hand.__sort_cards")


class Discard_Pile(Hand):
    """The Discard_Pile subclass, a specialized hand type object used specifically for discard piles and field of play

    METHODS
        >> __init__(self, visibility)
            initializes a Discard Pile

        >> __str__(self)
            handles proper printing of the discard pile object

    """

    def __init__(self, visibility=None):
        """Creates an empty Discard_Pile object"""
        try:
            self._card_count = 0
            self._cards = []
            self._visibility = None

            if type(visibility) == Visibility:
                self.isvisible = visibility
            elif visibility == None:
                self._visibility = Visibility.TOPVISIBLE
            else:
                Error.log_error(TypeError("TypeError: Visibility must be in visibility enum"), "Discard_Pile.__init__")
        except:
            Error.log_error(sys.exc_info()[1], "Discard_Pile.__init__")

    def __str__(self):
        """Handles printing for the discard pile"""
        try:
            if self.isvisible.name == "VISIBLE":
                temp_string = "("
                for card in self._cards:
                    temp_string += "%s, " % str(card)
                temp_string += ")"

            elif self.isvisible.name == "TOPVISIBLE":
                temp_string = ""
                temp_string += str(self._cards[0])


            elif self.isvisible.name == "INVISIBLE":
                temp_string = "Not allowed, invisible hand"

            return temp_string
        except:
            Error.log_error(sys.exc_info()[1], "Discard_Pile.__str__")

#
# def main():
#     print("Unit test: \n")
#     suite = unittest.TestLoader().loadTestsFromModule(HandTest)
#     unittest.TextTestRunner().run(suite)
#     hand = Hand(sort=Sort.RANKTHENSUITA)
#     card2 = Card(suit=Suit.DIAMONDS, rank=Rank.FIVE)
#     card3 = Card(suit=Suit.SPADES, rank=Rank.THREE)
#     card4 = Card(suit=Suit.DIAMONDS, rank=Rank.THREE)
#     card5 = Card(suit=Suit.CLUBS, rank=Rank.ACELOW)
#     card1 = Card(suit=Suit.DIAMONDS, rank=Rank.FIVE)
#     card6 = Card(suit=Suit.SPADES, rank=Rank.THREE)
#     card7 = Card(suit=Suit.DIAMONDS, rank=Rank.KING)
#     card8 = Card(suit=Suit.CLUBS, rank=Rank.ACELOW)
#     new_cards = [card2, card3, card4, card5]
#     newer = [card1, card6, card7, card8]
#     hand1 = Hand()
#     hand1.add_card(new_cards)
#     hand.add_card(newer)
#     print(hand.sort_type)
#     hand.visi_override()
#     print(hand1)
#     hand2 = hand1 + hand
#     print(hand2)
#
#
# if __name__ == '__main__':
#     main()