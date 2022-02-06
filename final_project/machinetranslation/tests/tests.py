import unittest
from translator import french_to_english, english_to_french

class NullTest(unittest.TestCase):
    def test_fr_null(self):
        self.assertIsNotNone(french_to_english('Bonjour'))
    
    def test_en_null(self):
        self.assertIsNotNone(english_to_french('Hello'))

if __name__ == '__main__':
    unittest.main()