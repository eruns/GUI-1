import unittest
from Game import *
from Hand import *
from Card import *
from Enums.Suit import *
from Enums.Rank import *
from Enums.Visibility import *
from Enums.Sort_Methods import *


class GameTestCase(unittest.TestCase):
    """Tests the Game class"""

    def setUp(self):
        pass

    def test_constructor_none_hands(self):
        game = Game()
        self.assertEqual(game.hands, [], "Hands dictionary not initializing to empty")

    def test_constructor_none_deck(self):
        game = Game()
        self.assertEqual(type(game.deck), Deck, "Deck type object not found")
        self.assertEqual(game.deck.count, 52, "Deck not creating correct number of cards")

    def test_constructor_none_hand_count(self):
        game = Game()
        self.assertEqual(game.hand_count, 0, "hand count not initializing to 0")

    def test_constructor_none_hand_sizes(self):
        game = Game()
        self.assertEqual(game.init_hand_size, 0, "init hand size not defaulting to 0")
        self.assertEqual(game.max_hand_size, 52, "Max hand size not defaulting to 52")

    def test_constructor_none_acerank(self):
        game = Game()
        self.assertEqual(game.ace_rank, Rank.ACELOW, "ace rank not defaulting to ace low")

    def test_constructor_none_discard_type(self):
        game = Game()
        self.assertEqual(game.discard_type, Visibility.INVISIBLE, "Visibility of discard not defalting to Invisible")

    def test_constructor_none_empty_hands(self):
        game = Game()
        self.assertEqual(game.empty_hands, 0, "empty hands not initializing to 0")

    def test_constructor_none_active(self):
        game = Game()
        self.assertEqual(game.active_hand, None, "Active hand not empty to start game")

    def test_constructor_none_sort_type(self):
        game = Game()
        self.assertEqual(game.sort_method, Sort.SUITTHENRANKD, "sort type not initializng properly")

    def test_constructor_two_hands(self):
        game = Game(hand_count=2)
        self.assertEqual(len(game.hands), 2, "Hands dictionary not initializing to empty")

    def test_constructor_ace_rank_deck(self):
        game = Game(ace_rank=Rank.ACEHIGH)
        self.assertEqual(type(game.deck), Deck, "Deck type object not found")
        self.assertEqual(Rank(game.deck.ace_rank), Rank.ACEHIGH, "Deck not setting acerank as required")

    def test_constructor_five_hand_count(self):
        game = Game(hand_count=5, hand_size=1)
        self.assertEqual(game.hand_count, 5, "hand count not initializing to 0")

    def test_constructor_5to10_hand_sizes(self):
        game = Game(hand_count=3, hand_size=5, max_hand_size=10)
        self.assertEqual(game.init_hand_size, 5, "init hand size not defaulting to 0")
        self.assertEqual(game.max_hand_size, 10, "Max hand size not defaulting to 52")

    def test_constructor_high_acerank(self):
        game = Game(ace_rank=Rank.ACEHIGH)
        self.assertEqual(game.ace_rank, Rank.ACEHIGH, "ace rank not defaulting to ace low")

    def test_constructor_visible_discard_type(self):
        game = Game(discard_type=Visibility.VISIBLE)
        self.assertEqual(game.discard_type, Visibility.VISIBLE, "Visibility of discard not defalting to Invisible")

    def test_constructor_4hands0cards_empty_hands(self):
        game = Game(hand_count=4, hand_size=0)
        self.assertEqual(game.empty_hands, 4, "empty hands not initializing to 0")

    def test_constructor_RthenSA_sort_type(self):
        game = Game(sort=Sort.RANKTHENSUITA)
        self.assertEqual(game.sort_method, Sort.RANKTHENSUITA, "sort type not initializng properly")

    def test_constructor_pass_sort_hands(self):
        game = Game(hand_count=4, hand_size=4, sort=Sort.RANKTHENSUITA)
        self.assertEqual(game.hands["hands1"][0].sort_type, Sort.RANKTHENSUITA,
                         "Game class not properly passing sort to hand")


if __name__ == '__main__':
    unittest.main(verbosity=2)