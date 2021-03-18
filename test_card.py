import unittest

from card import Card, Suit

class test_card_str(unittest.TestCase):
    def test_ace_diamonds(self):
        card_test = Card(1, Suit.DIAMONDS)
        self.assertEqual("A♦", str(card_test))
    
    def test_two_clubs(self):
        card_test = Card(2, Suit.CLUBS)
        self.assertEqual("2♣", str(card_test))
    
    def test_nine_hearts(self):
        card_test = Card(9, Suit.HEARTS)
        self.assertEqual("9♥", str(card_test))
    
    def test_ten_spades(self):
        card_test = Card(10, Suit.SPADES)
        self.assertEqual("T♠", str(card_test))
    
    def test_jack_spades(self):
        card_test = Card(11, Suit.SPADES)
        self.assertEqual("J♠", str(card_test))
    
    def test_queen_spades(self):
        card_test = Card(12, Suit.SPADES)
        self.assertEqual("Q♠", str(card_test))
    
    def test_king_spades(self):
        card_test = Card(13, Suit.SPADES)
        self.assertEqual("K♠", str(card_test))
    
    def test_value_error(self):
        self.assertRaises(ValueError, Card, 0, Suit.SPADES)


if __name__ == '__main__':
    unittest.main()