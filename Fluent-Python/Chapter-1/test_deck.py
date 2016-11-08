import unittest
from deck import Card, FrenchDeck

class TestDeck(unittest.TestCase):
    
    def test_length_works(self):
        fd = FrenchDeck
        self.assertEqual(len(fd), 52)
        

if __name__ == "__main__":
    unittest.main()
