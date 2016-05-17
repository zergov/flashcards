import unittest

from flashcards.cards import QuestionCard
from flashcards.games.flasher import CardFlasher


class TestGameEnumerate(unittest.TestCase):

    def setUp(self):

        # Add some cards to the study set
        self.cards = [
            QuestionCard('q1', 'a1'),
            QuestionCard('q2', 'a2')
        ]

    def test_StudySetEnumerator(self):

        # Create the enumerator to enumerate this set
        flasher = CardFlasher(self.cards)
        self.assertIsNotNone(flasher)

    def test_get_current_card(self):

        flasher = CardFlasher(self.cards)

        # By default, the flasher starts at card index 0
        card = flasher.get_current_card()
        self.assertEqual(card, self.cards[0])

    def test_next(self):

        flasher = CardFlasher(self.cards)

        # Set the index of the current card to the next card
        flasher.next()

        card = flasher.get_current_card()
        self.assertEqual(card, self.cards[1])

    def test_next_out_of_bound(self):

        flasher = CardFlasher(self.cards)

        # In this case, the StudySet now only contains 2 card. Calling next
        # three times should not trigger an error and should return the last
        # card in the set.
        flasher.next()
        flasher.next()
        flasher.next()

        card = flasher.get_current_card()
        self.assertEqual(card, self.cards[1])

    def test_previous(self):

        flasher = CardFlasher(self.cards)

        # Set the index of the current card to the next card --> 1
        flasher.next()
        # Set the index of the current card to the previous card sooo --> 0
        flasher.previous()

        card = flasher.get_current_card()
        self.assertEqual(card, self.cards[0])

    def test_previous_out_of_bound(self):

        flasher = CardFlasher(self.cards)

        # Flasher starts at index 0. Calling previous should stay at index 0
        flasher.previous()

        card = flasher.get_current_card()
        self.assertEqual(card, self.cards[0])

    def test_randomize(self):

        flasher = CardFlasher(self.cards)
        flasher.randomize()

        #TODO: Mock that shuffle has been called with the list of cards
        self.assertIn(self.cards[0], flasher._cards)
        self.assertIn(self.cards[1], flasher._cards)
