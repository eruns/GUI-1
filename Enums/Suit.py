"""Defines suit class for Hearts, Spades, Diamonds, and Clubs."""

from enum import Enum

class Suit(Enum):
    HEARTS = 4
    SPADES = 3
    DIAMONDS = 2
    CLUBS = 1

    def __str__(self):
        """ Returns suit.

        Returns: (string) suit.
        """

        if self.name == "HEARTS":
            return u"\u2665"
        if self.name == "SPADES":
            return u"\u2660"
        if self.name == "DIAMONDS":
            return u"\u2666"
        if self.name == "CLUBS":
            return u"\u2663"
        else:
            raise ValueError("Unexpected suit:" + self.name)

if __name__ == "__main__":
    for suit in Suit:
        print(suit)
