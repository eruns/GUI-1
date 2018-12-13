import unittest
from Hand import *
from Card import *
from Enums.Suit import *
from Enums.Rank import *
from Enums.Visibility import *
import Error


class HandTestCase(unittest.TestCase):
    """Tests the Hand class and its subclasses"""

    def setUp(self):
        pass

    def test_constructor_none_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [], "Hand is not initializing to empty hand")

    def test_constructor_none_card_count(self):
        hand = Hand()
        self.assertEqual(hand.card_count, 0, "Card count not initializing to 0 cards")

    # def test_constructor_something(self):
    #     self.assertRaises(TypeError, Hand, 10)

    # def test_function_add_card_none(self):
    #     hand = Hand()
    #     self.assertRaises(ValueError, hand.add_card, None)

    def test_function_add_card_single(self):
        hand = Hand()
        card = Card(suit=Suit.SPADES, rank=Rank.TEN)
        hand.add_card(card=card)
        self.assertEqual(hand.cards[0].rank.value, 10, "Add card not adding a single card properly")

    def test_property_card_count_add_card(self):
        hand = Hand()
        card = Card(suit=Suit.SPADES, rank=Rank.TEN)
        hand.add_card(card=card)
        self.assertEqual(hand.card_count, 1, "card count not setting accurately")

    def test_function_add_card_array_addTest(self):
        hand = Hand()
        card1 = Card(suit=Suit.SPADES, rank=Rank.TEN)
        card2 = Card(suit=Suit.DIAMONDS, rank=Rank.FIVE)
        card3 = Card(suit=Suit.SPADES, rank=Rank.THREE)
        card4 = Card(suit=Suit.DIAMONDS, rank=Rank.KING)
        card5 = Card(suit=Suit.CLUBS, rank=Rank.ACEHIGH)
        new_cards = [card1, card2, card3, card4, card5]
        hand.add_card(new_cards)
        self.assertEqual(hand.card_count, 5, "Add card not properly adding array")

    def test_function_add_card_array_sortTest(self):
        hand = Hand(sort=Sort.RANKTHENSUITA)
        card1 = Card(suit=Suit.SPADES, rank=Rank.TEN)
        card2 = Card(suit=Suit.DIAMONDS, rank=Rank.FIVE)
        card3 = Card(suit=Suit.SPADES, rank=Rank.THREE)
        card4 = Card(suit=Suit.DIAMONDS, rank=Rank.KING)
        card5 = Card(suit=Suit.CLUBS, rank=Rank.ACELOW)
        new_cards = [card1, card2, card3, card4, card5]
        hand.add_card(new_cards)
        self.assertEqual(hand.cards[0].rank.value, 1, "Sort card not properly sorting hand")
        self.assertEqual(hand.cards[4].rank.value, 13, "Sort card not properly sorting hand")

    # def test_function_play_card_none(self):
    #     hand = Hand()
    #     card = Card(rank = Rank.TEN, suit = Suit.CLUBS)
    #     self.assertRaises(ValueError, hand.play_card, card)

    def test_function_play_card_newCard_return(self):
        hand = Hand()
        card = Card(rank=Rank.TEN, suit=Suit.CLUBS)
        hand.add_card(card)
        self.assertEqual(hand.play_card(card), card, "Play card not returning card properly")

    def test_function_play_card_newCard_remove(self):
        hand = Hand()
        card = Card(rank=Rank.TEN, suit=Suit.CLUBS)
        hand.add_card(card)
        hand.play_card(card)
        self.assertEqual(hand.card_count, 0, "Play card not removing card properly")

    # def test_function_remove_card_none(self):
    #     hand = Hand()
    #     self.assertRaises(ValueError, hand.remove_card, None)

    # def test_function_remove_card_both(self):
    #     hand = Hand()
    #     self.assertRaises(TypeError, hand.remove_card, index = 2, card = 2)

    def test_function_remove_card_card(self):
        hand = Hand()
        card = Card(rank=Rank.TEN, suit=Suit.CLUBS)
        hand.add_card(card)
        hand.remove_card(card=card)
        self.assertEqual(hand.card_count, 0, "Remove card not removing card properly")

    def test_function_remove_card_index(self):
        hand = Hand()
        card = Card(rank=Rank.TEN, suit=Suit.CLUBS)
        hand.add_card(card)
        hand.remove_card(index=0)
        self.assertEqual(hand.card_count, 0, "Play card not removing card properly")

    def test_constructor_set_visibility(self):
        hand = Hand(visibility=Visibility.INVISIBLE)
        self.assertEqual(hand.isvisible, Visibility.INVISIBLE, "visibility not setting correctly")

    def test_constructor_visibility_default(self):
        hand = Hand()
        self.assertEqual(hand.isvisible, Visibility.VISIBLE,
                         "Visibility not initializing to visible when no input given")

    """Discard Pile testing begins"""

    def test_constructor_Discard_Pile_none_visibility(self):
        dscrd = Discard_Pile()
        self.assertEqual(dscrd.isvisible, Visibility.TOPVISIBLE,
                         "Visibility not initializing to topvisible when no input given")

    # def test_constructor_Discard_Pile_num_visibility(self):
    #     self.assertRaises(TypeError, Discard_Pile, visibility = 10)

    def test_constructor_Discard_Pile_visible_visibility(self):
        dscrd = Discard_Pile(visibility=Visibility.VISIBLE)
        self.assertEqual(dscrd.isvisible, Visibility.VISIBLE, "Visibility setter not setting properly")

    def main(self):
        unittest.main()


if __name__ == '__main__':
    unittest.main()
