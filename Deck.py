from Enums.Suit import *
from Enums.Rank import *
from Card import *
from random import *
from Hand import *
from Enums.Visibility import *


class Deck(object):
    """ Deck class, Creates a deck from rank
    and suit stores it in an array.

    METHODS
        >>build(self)
            creates deck from rank and suit object

        >>shuffle(self)
            shuffles deck

        >>deal(self)
            removes deck and returns it for use


    """

    def __init__(self, ace_rank=None):
        """Creates a deck object and shuffles it."""
        self._count = 0
        self._acerank = None

        if type(ace_rank) == Rank:
            if ace_rank == Rank.ACELOW:
                self._acerank = 1
            elif ace_rank == Rank.ACEHIGH:
                self._acerank = 14

        elif ace_rank == None:
            self._acerank = 1

        self.build()

    @property
    def count(self):
        """Getter: Gets the number of cards in the deck.

        Returns
            @count(int): the number of cards in a deck.
        """
        return len(self._deck)

    @property
    def ace_rank(self):
        """Getter: gets the ace rank of the deck

        Returns
            @acerank (int): the integer value of enum acerank
        """
        return self._acerank

    @property
    def deck(self):
        """Getter: gets the array of a deck.

        Returns
            @deck (array): the array in the deck.
        """
        return self._deck

    def build(self):
        """builds deck from rank and suit.

        Paramaters
            @Card(rank, suit): used to generate the deck.
        """

        deck = []
        for suit in Suit:
            if self.ace_rank == 1:
                for i in range(1, 14):
                    card = Card(Rank(i), suit)
                    deck.append(card)
            else:
                for i in range(2, 15):
                    card = Card(Rank(i), suit)
                    deck.append(card)
        self._deck = deck

    def shuffle(self):
        """Shuffles deck

        Paramaters
            @deck: shuffles deck
        """

        shuffle(self._deck)

    # deal
    def deal(self):
        """deals card from deck

        paramater
        @deck: card removed from array
        @count: number of cards in deck
        """

        return self._deck.pop()

    # utility
    def __str__(self):
        """Converts memory location to str."""
        printed_deck = ""
        for card in self._deck:
            printed_deck += " {} {}".format(card.rank, card.suit)
        return printed_deck

    def __add__(self, other):
        """ Creates functionality to add objects."""
        if type(other) is not Card:
            raise ValueError("Card should be passed as ['rank', 'suit']")
        if self.find_in_deck(other) == True:
            raise ValueError("Card is already in deck")
        else:
            add = []
            card = Card(other.rank, other.suit)
            add.append(card)
            self._deck.extend(add)

    def find_in_deck(self, card):
        """Loops through a deck to prevent duplicates.

        paramaters
        @deck: cards to loop through.
        @card: card to compare.
        """

        for c in self._deck:
            if c.is_same_as(card) == True:
                return c.is_same_as(card)


def main():
    deck = Deck()
    deck.shuffle()
    print("hand 1:")
    for i in range(15):
        (deck.deal())
    print(deck.count)
    print(deck)
    deck + Card(Rank.FOUR, Suit.CLUBS)
    print(deck)


if __name__ == "__main__":
    main()

    # def starting_deal

    # Utility Functions
    # def print_deck(self, deck):

    #     for card in deck:
    #         print(card.rank, card.suit)

    # def print_card(self, card):

    #     print(card.rank, card.suit )