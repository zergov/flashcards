import unittest
import mock

from flashcards.sets import StudySet
from flashcards.cards import StudyCard
from flashcards.study import StudySession
from flashcards.study import SimpleStudyStrategy


def create_study_set():
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


def create_cards_list():
    """ Create a simple list of cards for test purposes. """

    cards = [
        StudyCard('2 + 2 = ?', '4'),
        StudyCard('2 + 3 = ?', '5'),
        StudyCard('2 + 4 = ?', '6'),
        StudyCard('2 + 5 = ?', '7')
    ]

    return cards


class TestStudymodule(unittest.TestCase):

    def test_studySession_start_calls_strategy_show(self):

        mock_strategy = mock.Mock()
        mock_start = mock.Mock()
        mock_strategy.attach_mock(mock_start, 'start')

        study_set = create_study_set()
        session = StudySession(study_set)
        session.start(mock_strategy)

        self.assertEqual(mock_start.call_count, 1)


class TestSimpleStudyStrategy(unittest.TestCase):

    def test_start_show_card_called(self):
        # Test that the show_question function is called for every card in the
        # the card iterator.

        study_set = create_study_set()
        strategy = SimpleStudyStrategy()

        mock_show_question = mock.Mock()
        strategy.show_question = mock_show_question

        strategy.start(study_set)
        self.assertEqual(mock_show_question.call_count, 4)
