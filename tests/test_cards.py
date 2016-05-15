import unittest

from flashcards.cards import QuestionCard

class TestQuestionCards(unittest.TestCase):

    def setUp(self):
        self.card = QuestionCard('what is PI ?', '3.14159265359')

    def test_Card_class_exists(self):
        self.assertIsNotNone(QuestionCard('meaning of life?', '42'))

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
