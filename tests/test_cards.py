import unittest

from flashcards.cards import BaseCard

class TestCards(unittest.TestCase):

    def test_Card_class_exists(self):
        self.assertIsNotNone(BaseCard('meaning of life?', '42'))
