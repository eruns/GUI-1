"""Defines rank class for ranks."""

from enum import Enum


class Rank(Enum):
    ACELOW = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACEHIGH = 14

    def __str__(self):
        """ returns rank.

        Returns: (string) rank.
        """

        if self.name == "ACELOW":
            return "A"
        if self.name == "TWO":
            return "2"
        if self.name == "THREE":
            return "3"
        if self.name == "FOUR":
            return "4"
        if self.name == "FIVE":
            return "5"
        if self.name == "SIX":
            return "6"
        if self.name == "SEVEN":
            return "7"
        if self.name == "EIGHT":
            return "8"
        if self.name == "NINE":
            return "9"
        if self.name == "TEN":
            return "10"
        if self.name == "JACK":
            return "J"
        if self.name == "QUEEN":
            return "Q"
        if self.name == "KING":
            return "K"
        if self.name == "ACEHIGH":
            return "A"

        else:
            raise ValueError("Unexpected rank:" + self.name)


if __name__ == "__main__":
    for rank in Rank:
        print(rank)

