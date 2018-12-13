from Hand import *
from Deck import *
from Enums.Rank import *


class Rules(object):
    """Defines the rules of go fish game."""

    def __init__(self, deck=None, points=None, books=None):
        """Creates deck object.

        Args:
            deck (deck): all cards.
        """

        self.deck = None
        self._points = 0
        self._books = None

        self.deck = deck

    @property
    def points(self):
        """ Getter: Tracks the p1_points points.

        Returns (int): p1_points
        """

        return self._points

    @property
    def books(self):
        """ Getter: Tracks the number of books.

        Returns (int): books
        """

        return self._books

    def card_request(self):

        """Gets the requested card rank from
        the player.

        Returns:
            request (string): requested card rank.
        """

        request = int(input("Enter a card rank you like to collect (1-13)."))

        return Rank(request)

    def player_answer(self, request, p2):

        """Gets the answer from the other player.

           Args:
               request (string): requested card rank.

            Returns:
                answer (string): answer from the other player.
        """
        if p2.count_rank(request):
            answer = "YES"
        elif not p2.count_rank(request):
            answer = "GOFISH"

        return answer

    def book_check(self, request, p1):

        """Checks if the player have a book.

        Args:
           request (string): requested card rank.
           p1      (array) : p1 cards.

        Returns:
            book (arry): Four suit of one rank.
        """

        book = p1.count_rank(request)

        return book

    def count_request(self, p2, request):

        """Counts the number of the requested rank in p2.

        Args:
           p2 (array): array of cards for the other player.

        Returns:
            p1 (array): array of cards for the player.
            p2 (array): array of cards for the other player.
        """

        req_num = p2.count_rank(request)
        # print("p2 has" + " " + str(req_num) + " " + "of" + " " + str(request))

        return req_num

    def check_deck(self):

        """Count's the number of cards in the deck.

        Args:
           deck (array): array of cards in the deck.

        Returns:
            p1 (array): array of cards for the player.
            Deck (array): array of cards in the deck.
        """

        deck_count = self.deck.count

        return deck_count

    def play_game(self, p1, p2):

        """Plays the Go Fish game.

        Args:
            p1 (array): first player cards.
            p2 (array): the other player cards.

        Returns:
            True : player take another turn.
            False: player turn ended.
        """

        request = self.card_request()
        answer = self.player_answer(request, p2)

        """If p2 has the requested rank (answer = YES)."""
        if answer.upper() == "YES":
            for card in p2.cards:
                if card.rank == request:
                    move_card = p2.play_card(card)
                    p1.add_card(move_card)

                    """Checks if p1 has a book of requested rank."""
                    book = self.book_check(request, p1)

                    """If p1 has book(four suit of one rank)."""
                    if book == 4:
                        p1.find_and_remove(request)
                        self._points += 1
                        self._books += 1

                        """If p1 is empty from cards."""
                        if p1.card_count == 0:
                            deck_count = self.check_deck()

                            """If deck has less than 5 cards."""
                            if deck_count < 5:
                                for i in range(deck_count):
                                    p1.add_card(self.deck.deal())
                                print("Player turn ended.")
                                return False

                                """If deck has more than 5 cards."""
                            else:
                                for i in range(0, 4):
                                    p1.add_card(self.deck.deal())
                                return False

                        print("Player turn ended.")
                        return False

                    print("Player take another turn,")
                    return True

            """Answer is GOFISH (p2 does not have the requested card)."""
        else:
            for card in p2.cards:
                if card.rank == request:
                    print("Player is cheating.")
                    return True

            deck_count = self.check_deck()
            if deck_count != 0:
                card = self.deck.deal()
                p1.add_card(card)

                book = self.book_check(card, p1)

                """Player has a book or got requested card from the deck."""
                if book == 4 and request == card:
                    print("Show the card.")
                    p1.find_and_remove(request)
                    self._points += 1
                    self._books += 1
                    print("player gets" + " " + str(self.points) + " " + "points")
                    print("player take another turn.")
                    return True

                    """Player got the requested card from the deck."""
                elif book != 4 and request == card:
                    print("Show the card.")
                    print("p1 take another turn.")
                    return True

                    """Player has a book."""
                elif book == 4 and request != card:
                    p1.find_and_remove(request)
                    self._points += 1
                    self._books += 1
                    print("p1 gets" + " " + str(self.points) + " " + "points")
                    return False

                    """No book, No requested card."""
                else:
                    print("p1 turn is ended")
                    return False

                """ Deck is empty."""
            else:
                print("Deck is empty, players keep playing.")
                return False


def main():
    play_game(self, p1, p2)


if __name__ == '__main__':
    main()
