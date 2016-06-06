import unittest
import mock

from flashcards.sets import StudySet
from flashcards.cards import StudyCard
from flashcards.study import BaseStudySession


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


class TestBasicStudyStrategy(unittest.TestCase):

    def test_studySession_start(self):

        mock_show_question = mock.Mock()
        mock_show_answer = mock.Mock()

        study_set = create_study_set()

        session = BaseStudySession()
        session.show_question = mock_show_question
        session.show_answer = mock_show_answer

        session.start(study_set)
        self.assertEqual(4, mock_show_question.call_count)
        self.assertEqual(4, mock_show_answer.call_count)
