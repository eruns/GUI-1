"""Defines Visibility class for visible, invisible, and topvisible."""

from enum import Enum


class Visibility(Enum):
    VISIBLE = 1
    INVISIBLE = 2
    TOPVISIBLE = 3

    def __str__(self):
        """ Returns visible, invisible, and topvisible.

        Returns: (string) visible, invisible, and topvisible.
        """

        if self.name == "VISIBLE":
            return "V"
        if self.name == "INVISIBLE":
            return "I"
        if self.name == "TOPVISIBLE":
            return "T"
        else:
            raise ValueError("Unexpected suit:" + self.name)


if __name__ == "__main__":
    for visible in Visibility:
        print(visible)
