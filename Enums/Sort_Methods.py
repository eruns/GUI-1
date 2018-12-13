"""Defines Visibility class for visible, invisible, and topvisible."""

from enum import Enum


class Sort(Enum):
    RANKTHENSUITD = 1
    SUITTHENRANKD = 2
    RANKTHENSUITA = 3
    SUITTHENRANKA = 4

    def __str__(self):
        """ Returns visible, invisible, and topvisible.

        Returns: (string) visible, invisible, and topvisible.
        """

        if self.name == "RANK":
            return "Descending Rank then Suit"
        if self.name == "SUIT":
            return "Descending Suit then Rank"
        if self.name == "RANKTHENSUITA":
            return "Ascending Rank then Suit"
        if self.name == "SUITTHENRANKA":
            return "Ascending Suit then Rank"
        else:
            raise ValueError("Unexpected sort method:" + self.name)


if __name__ == "__main__":
    for sort in Sort:
        print(sort)
