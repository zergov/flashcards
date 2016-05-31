import unittest
import mock

from flashcards.sets import StudySet
from flashcards.cards import StudyCard
from flashcards.study import StudySession


class TestStudymodule(unittest.TestCase):

    def create_study_set(self):
        """ Create a simple study set for test purposes. """

        cards = [
            StudyCard('2 + 2 = ?', '4'),
            StudyCard('2 + 3 = ?', '5'),
            StudyCard('2 + 4 = ?', '6'),
            StudyCard('2 + 5 = ?', '7')
            ]

        study_set = StudySet('Basic Maths')
        study_set._cards = cards

        return study_set

    def create_cards_list(self):
        """ Create a simple list of cards for test purposes. """

        cards = [
            StudyCard('2 + 2 = ?', '4'),
            StudyCard('2 + 3 = ?', '5'),
            StudyCard('2 + 4 = ?', '6'),
            StudyCard('2 + 5 = ?', '7')
        ]

        return cards

    def test_studySession_start_calls_strategy_show(self):

        mock_strategy = mock.Mock()
        mock_show = mock.Mock()
        mock_strategy.attach_mock(mock_show, 'show')

        study_set = self.create_study_set()
        session = StudySession(study_set)
        session.start(mock_strategy)

        self.assertEqual(mock_show.call_count, 4)
