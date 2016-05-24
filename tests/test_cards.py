import unittest

from flashcards import cards
from flashcards.cards import StudyCard


class TestModulefunctions(unittest.TestCase):

    def test_create_card_from_dict(self):
        data = {'question': '2+2=?', 'answer': '4'}
        card = cards.create_card_from_dict(data)

        self.assertEqual('2+2=?', card.question)
        self.assertEqual('4', card.answer)


class TestQuestionCards(unittest.TestCase):

    def setUp(self):
        self.card = StudyCard('what is PI ?', '3.14159265359')

    def test_Card_class_exists(self):
        self.assertIsNotNone(StudyCard('meaning of life?', '42'))

    def test_card_get_question(self):
        self.assertEqual('what is PI ?', self.card.question)

    def test_card_get_answer(self):
        self.assertEqual('3.14159265359', self.card.answer)

    def test_card_set_question(self):
        new_question = 'What is e ?'
        self.card.question = new_question
        self.assertEqual(new_question, self.card.question)

    def test_card_set_question_error(self):
        bad_question = 4123451
        self.assertRaises(TypeError, setattr, self.card.question, bad_question)

    def test_card_set_answer(self):
        new_answer = '2.71828'
        self.card.answer = new_answer
        self.assertEqual(new_answer, self.card.answer)

    def test_card_set_answer_error(self):
        bad_answer = 2.71828
        self.assertRaises(TypeError, setattr, self.card.answer, bad_answer)

    def test_to_dict(self):
        data = self.card.to_dict()
        expected = {'question': 'what is PI ?', 'answer': '3.14159265359'}
        self.assertEqual(expected, data)
