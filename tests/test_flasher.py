import unittest
import mock

from flashcards.cards import StudyCard
from flashcards.study import StudySession


class Test_CardFlasher(unittest.TestCase):

    def setUp(self):

        # Add some cards to the study set
        self.cards = [
            StudyCard('q1', 'a1'),
            StudyCard('q2', 'a2')
        ]

    def test_StudySetEnumerator(self):

        # Create the enumerator to enumerate this set
        flasher = StudySession(self.cards)
        self.assertIsNotNone(flasher)

    def test_get_current_card(self):

        flasher = StudySession(self.cards)

        # By default, the flasher starts at card index 0
        card = flasher.current_card
        self.assertEqual(card, self.cards[0])

    def test_next(self):

        flasher = StudySession(self.cards)

        # Set the index of the current card to the next card
        flasher.next()

        card = flasher.current_card
        self.assertEqual(card, self.cards[1])

    def test_next_out_of_bound(self):

        flasher = StudySession(self.cards)

        # In this case, the StudySet now only contains 2 card. Calling next
        # three times should not trigger an error and should return the last
        # card in the set.
        flasher.next()
        flasher.next()
        flasher.next()

        card = flasher.current_card
        self.assertEqual(card, self.cards[1])

    def test_previous(self):

        flasher = StudySession(self.cards)

        # Set the index of the current card to the next card --> 1
        flasher.next()
        # Set the index of the current card to the previous card sooo --> 0
        flasher.previous()

        card = flasher.current_card
        self.assertEqual(card, self.cards[0])

    def test_previous_out_of_bound(self):

        flasher = StudySession(self.cards)

        # Flasher starts at index 0. Calling previous should stay at index 0
        flasher.previous()

        card = flasher.current_card
        self.assertEqual(card, self.cards[0])

    def test_randomize(self):

        flasher = StudySession(self.cards)
        flasher.shuffle()

        self.assertIn(self.cards[0], flasher._cards)
        self.assertIn(self.cards[1], flasher._cards)

    @mock.patch('flashcards.flasher.random.shuffle')
    def test_randomize_shuffle_called(self, mock_shuffle):

        flasher = StudySession(self.cards)
        flasher.shuffle()

        mock_shuffle.assert_called_once_with(flasher._cards)
