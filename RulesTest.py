import unittest
from Rules import *
from Hand import *
from Card import *
from Enums.Suit import *
from Enums.Rank import *
from Enums.Visibility import *


class RulesTestCase(unittest.TestCase):
    "Tests the Rules class for Go Fish"

    def seUp(self):
        pass

    def test_constructor_none_points(self):
        rules = Rules()
        self.assertEqual(rules.points, 0, "self.points not defaulting to 0")

    def test_constructor_none_books(self):
        rules = Rules()
        self.assertEqual(rules.books, 0, "books not defaulting to a count of 0")

        """Card Request not being tested as it is input function"""

    def test_function_player_answer_yes(self):
        rules = Rules()
        hand = Hand()
        card = Card(rank=Rank.ACEHIGH, suit=Suit.DIAMONDS)
        hand += card
        self.assertEqual(rules.player_answer(Rank.ACEHIGH, hand), "YES",
                         "player answer Not returning YES when it should")

    def test_function_player_answer_gofish(self):
        rules = Rules()
        hand = Hand()
        self.assertEqual(rules.player_answer(Rank.ACEHIGH, hand), "GOFISH",
                         "player answer not returning GO FIsh properly")

    def test_function_book_check_fullbook(self):
        rules = Rules()
        hand = Hand()
        for s in Suit:
            hand.add_card(Card(rank=Rank.THREE, suit=s))
        self.assertEqual(rules.book_check(Rank.THREE, hand), 4, "book check not finding book")

    def test_function_book_check_emptybook(self):
        rules = Rules()
        hand = Hand()
        self.assertEqual(rules.book_check(Rank.THREE, hand), 0, "book check not returning 0 when 0 cards in hand")

    def test_function_count_request_none(self):
        rules = Rules()
        hand = Hand()
        self.assertEqual(rules.count_request(hand, Rank.THREE), 0, "Count request not returning 0 for empty hand")

    def test_function_count_request_2(self):
        rules = Rules()
        hand = Hand()
        hand += [Card(rank=Rank.THREE, suit=Suit.DIAMONDS), Card(rank=Rank.THREE, suit=Suit.SPADES)]
        self.assertEqual(rules.count_request(hand, Rank.THREE), 2,
                         "count request not returning 2 for hand with two rank matches")

    def test_function_check_deck_none(self):
        rules = Rules(Deck(ace_rank=Rank.ACELOW))
        self.assertEqual(rules.check_deck(), 52, "Deck not producing 52 cards")

    def test_function_check_deck_10pop(self):
        deck = Deck(ace_rank=Rank.ACELOW)
        rules = Rules(deck=deck)
        hand = Hand()
        for i in range(10):
            hand += deck.deal()
        self.assertEqual(rules.check_deck(), 42, "Deck not showing 42 cards after dealing 10")

    def test_function_play_game(self):
        """I am not sure how to test this function: it has far too much user interaction at this point to accurately test"""


if __name__ == "__main__":
    unittest.main()