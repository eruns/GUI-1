"""Author: Joanna Kus
 This class deals with information about a card for use with card games.
 Used with Hands superclass (Hand.py).
"""
import Enums.Rank
from Enums.Suit import *
from Enums.Visibility import *

class Card(object):
    """CLASS: Stores information about a given card. Stores a suit and rank value
    and a visual representation of the card. Read-only object.

    METHODS:
        >> __init__(self, suit=None, rank=None, visibility=Visibility.VISIBLE)
            Initializes the card object.

        >> __str__(self)
            Outputs rank and suit for the card.

        >> suit(self)
            Gets card suit.

        >> rank(self)
            Gets card rank.

        >> isvisible(self)
            Gets card visibility.

        >> isvisible(self, visibility)
            Sets card visibility.

        >> top_img(self)
            Gets top card image file URL.

        >> side_img(self)
            Gets side card image file URL.

        >> full_img(self)
            Gets full card image file URL.

        >> compare_cards_by_rank(self, other_card)
            Compares two cards by rank. Useful for sorting.

        >> compare_cards_by_suit(self, other_card)
            Compares two cards by suit (sorted in alphabetical order). Useful for sorting.

        >> compare_cards(self, other_card)
            Compares two cards by suit and then by rank. Useful for sorting.

        >> is_same_as(self, other_card)
            Compares two cards. Checks to see if the two cards are the same.
    """

    def __init__(self, rank=None, suit=None, isvisible=Visibility.VISIBLE, top_img=None, side_img=None, full_img=None):
        """Creates a Card object.

        PARAMETERS:
            suit (string):                Suit of the given card (e.g. Spades, Hearts, etc.).
            rank (string):                Rank of the given card (e.g. A, J, 2, 9, etc.).
            visibility (Visibility enum): Visibility of the card.
            top_img(string):              Top image file URL.
            side_img(string):             Side image file URL.
            full_img(string):             Full image file URL.
        """

        self._suit = suit
        self._rank = rank
        self._isvisible = isvisible
        self._top_img = top_img
        self._side_img = side_img
        self._full_img = full_img

        if suit != None:
            self._suit = suit
        if rank != None:
            self._rank = rank
        if isvisible == None:
            self._isvisible = Visibility.VISIBLE

        if type(isvisible) != Visibility:
            raise TypeError("Incorrect data type for visibility parameter; must be Visibility enum.")

        if top_img != None:
            self._top_img = top_img
        if side_img != None:
            self._side_img = side_img
        if full_img != None:
            self._full_img = full_img

    def __str__(self):
        """METHOD: Outputs rank and suit for the card.

            >> __str__(self)

            RETURNS:
                string: Card rank and suit.
        """
        new_string = str(self._rank) + str(self._suit)
        return new_string

    @property
    def suit(self):
        """METHOD: Gets card suit.

            >> suit(self)

            RETURNS:
                Suit enum: Card suit information.
        """
        return self._suit

    @property
    def rank(self):
        """METHOD: Gets card rank.

            >> rank(self)

            RETURNS:
                Rank enum: Card rank information.
        """
        return self._rank

    @property
    def isvisible(self):
        """METHOD: Gets card visibility.

            >> isvisible(self)

            RETURNS:
                Visibility enum: Card visibility.
        """
        return self._isvisible

    @isvisible.setter
    def isvisible(self, isvisible):
        """METHOD: Sets card visibility.

            >> isvisible(self, isvisible)

            PARAMETERS:
                isvisible (Visibility enum): Card visibility.
        """
        if type(isvisible) == Visibility:
            self._isvisible = isvisible

    @property
    def top_img(self):
        """METHOD: Gets top card image file URL.

            >> top_img(self)

            RETURNS:
                string: Image URL.
        """
        return self._top_img

    @property
    def side_img(self):
        """METHOD: Gets side card image file URL.

            >> side_img(self)

            RETURNS:
                string: Image URL.
        """
        return self._side_img

    @property
    def full_img(self):
       	"""METHOD: Gets full card image file URL.

            >> full_img(self)

            RETURNS:
                string: Image URL.
        """
        return self._full_img

    def compare_cards_by_rank(self, other_card):
        """METHOD: Compares two cards by rank. Useful for sorting.

            >> compare_cards_by_rank(self, other_card)

            PARAMETERS:
                other_card (Card object): Other card to compare to.

            RETURNS:
                int: Negative integer if this card is less than the other card.
                     Zero if this card is equal to the other card.
                     Positive integer if this card is greater than the other card.
        """
        comparison = -1
        rankself = 0
        rankother = 0

        rankself = int(self._rank.value)
        rankother = int(other_card._rank.value)

        if rankself == rankother:
            comparison = 0
        elif rankself > rankother:
            comparison = 1
        elif rankself < rankother:
            comparison = -1

        return comparison

    def compare_cards_by_suit(self, other_card):
        """METHOD: Compares two cards by suit (sorted in alphabetical order). Useful for sorting.

            >> compare_cards_by_suit(self, other_card)

            PARAMETERS:
                other_card (Card object): Other card to compare to.

            RETURNS:
                int: Negative integer if this card is less than the other card.
                     Zero if this card is equal to the other card.
                     Positive integer if this card is greater than the other card.
        """
        comparison = -1
        suitself = 0
        suitother = 0

        suitself = self._suit.value
        suitother = other_card._suit.value

        if suitself == suitother:
            comparison = 0
        elif suitself > suitother:
            comparison = 1

        return comparison

    def compare_cards(self, other_card):
        """METHOD: Compares two cards. Useful for sorting. Cards are sorted by suit
        and then by rank.

            >> compare_cards(self, other_card)

            PARAMETERS:
                other_card (Card object): Other card to compare to.

            RETURNS:
                int: Negative integer if this card is less than the other card.
                     Zero if this card is equal to the other card.
                     Positive integer if this card is greater than the other card.
        """
        comparison = -1

        if self.compare_cards_by_suit(other_card) == -1:
            comparison = -1
        elif self.compare_cards_by_suit(other_card) == 0:
            comparison = self.compare_cards_by_rank(other_card)
        else:
            comparison = 1

        return comparison

    def is_same_as(self, other_card):
        """METHOD: Compares two cards. Checks to see if the two cards are the same.

            >> is_same_as(self, other_card)

            PARAMETERS:
                other_card (Card object): Other card to compare to.

            RETURNS:
                bool: True if the two cards are of the same value.
                      False otherwise.
        """
        if self.compare_cards(other_card) == 0:
            return True
        else:
            return False

def main():
    card = Card(rank=Rank.THREE, suit=Suit.CLUBS)
    print(card)

if __name__ == '__main__':
    main()
