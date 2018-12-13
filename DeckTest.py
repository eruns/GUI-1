import unittest
from Deck import *
from Card import *
from Enums.Suit import *
from Enums.Rank import *


class DeckTestCase(unittest.TestCase):
    """Tests the Hand class and its subclasses"""

    def setUp(self):
        pass

    def test_constructor_count_none(self):
        deck = Deck()
        self.assertEqual(deck.count, 0, "Count not initializing to 0.")

    def test_constructor_count_build(self):
        deck = Deck()
        deck.build()
        self.assertEqual(deck.count, 52, "Count not initializing to 52")

    def test_constructor_count_post_deal_once(self):
        deck = Deck()
        deck.build()
        deck.deal()
        self.assertEqual(deck.count, 51, "Count not initializing to 51.")

    def test_function_count_three(self):
        deck = Deck()
        deck.build()
        deck.deal()
        deck.deal()
        deck.deal()
        self.assertEqual(deck.count, 49, "Count not initializing to 51.")

    def test_constructor_deck_none(self):
        deck = Deck()
        self.assertEqual(deck.deck, [], "Deck is not initializing to empty.")


if __name__ == '__main__':
    unittest.main()