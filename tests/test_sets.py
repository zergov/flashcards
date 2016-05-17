import unittest

from flashcards.sets import StudySet
from flashcards.cards import QuestionCard


class TestStudySets(unittest.TestCase):

    def setUp(self):
        self.set_instance = StudySet('Maths', 'A study set about maths')

    def test_StudySet_exists(self):
        self.assertIsNotNone(StudySet('Math 145'))

    def test_set_get_title(self):
        self.assertEqual('Maths', self.set_instance.title)

    def test_set_set_title(self):
        self.set_instance.title = 'French'
        self.assertEqual('French', self.set_instance.title)

    def test_set_set_title_error(self):
        self.assertRaises(TypeError, setattr, self.set_instance, 'title', 1337)

    def test_set_get_description(self):
        desc = 'A study set about maths'
        self.assertEqual(desc, self.set_instance.description)

    def test_set_set_description(self):
        desc = 'Study set about space maths'
        self.set_instance.description = desc
        self.assertEqual(desc, self.set_instance.description)

    def test_set_set_description_error(self):
        self.assertRaises(TypeError, setattr,
                          self.set_instance, 'description', 1337)

    def test_set_add(self):
        card = QuestionCard('What is my name?', 'Jonathan')
        self.set_instance.add(card)
        self.assertEqual(len(self.set_instance._cards), 1)
        self.assertIn(card, self.set_instance._cards)

    def test_set_add_wrong_type(self):
        card = "A String is not a question !"
        self.assertRaises(TypeError, self.set_instance.add, card)
        self.assertEqual(len(self.set_instance._cards), 0)
        self.assertNotIn(card, self.set_instance._cards)

    def test_set_get_card(self):
        card = QuestionCard('What is my name?', 'Jonathan')
        self.set_instance.add(card)
        c = self.set_instance.get(0)
        self.assertEqual(c, card)

    def test_set_remove_card(self):
        card0 = QuestionCard('What is my name?', 'Jonathan')
        card1 = QuestionCard("What is bird's name ?", "Gandalf")
        self.set_instance.add(card0)
        self.set_instance.add(card1)

        self.set_instance.remove(1) # Remove the Gandalf card
        self.assertEqual(len(self.set_instance._cards), 1)
        self.assertNotIn(card1, self.set_instance._cards)
        self.assertIn(card0, self.set_instance._cards)
