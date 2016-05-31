import unittest
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
