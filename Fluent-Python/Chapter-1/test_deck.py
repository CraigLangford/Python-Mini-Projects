import unittest
from deck import Card, FrenchDeck, spades_high
from random import choice

class TestDeck(unittest.TestCase):
   
    def test_card(self):
        card = Card(rank='7', suit='Diamonds')
        self.assertEqual(card.rank, '7')
        self.assertEqual(card.suit, 'Diamonds')

    def test_length(self):
        deck = FrenchDeck()
        self.assertEqual(len(deck), 52)

    def test_get_card_in_deck(self):
        deck = FrenchDeck()
        self.assertEqual(deck[0], Card(rank='2',suit='Spades'))
        self.assertEqual(deck[-1], Card(rank='A',suit='Hearts'))

    def test_get_choice(self):
        deck = FrenchDeck()
        self.assertEqual(type(choice(deck)), Card)

    def test_if_in_works(self):
        deck = FrenchDeck()
        self.assertTrue(Card(rank='3', suit='Diamonds') in deck)
        self.assertFalse(Card(rank='3', suit='Clunks') in deck)

    def test_ranking_works(self):
        deck = FrenchDeck()
        deck = sorted(deck, key=spades_high)
        self.assertEqual(deck[0], Card(rank='2', suit='Clubs'))
        self.assertEqual(deck[51], Card(rank='A', suit='Spades'))

if __name__ == "__main__":
    unittest.main()
