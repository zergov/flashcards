import unittest

from flashcards import sets
from flashcards.sets import StudySet
from flashcards.cards import StudyCard


class TestModuleFunction(unittest.TestCase):

    def test_create_from_dict(self):
        card = StudyCard('2+2=?', '4')

        data = {'title': 'Maths', 'description': 'Math-145'}
        data['cards'] = [card.to_dict()]

        study_set = sets.create_from_dict(data)

        self.assertEqual(study_set.title, 'Maths')
        self.assertEqual(study_set.description, 'Math-145')
        self.assertEqual(len(study_set), 1)
        self.assertEqual(study_set._cards[0].question, '2+2=?')
        self.assertEqual(study_set._cards[0].answer, '4')


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
        card = StudyCard('What is my name?', 'Jonathan')
        self.set_instance.add(card)
        self.assertEqual(len(self.set_instance._cards), 1)
        self.assertIn(card, self.set_instance._cards)

    def test_set_add_wrong_type(self):
        card = "A String is not a question !"
        self.assertRaises(TypeError, self.set_instance.add, card)
        self.assertEqual(len(self.set_instance._cards), 0)
        self.assertNotIn(card, self.set_instance._cards)

    def test_iter_cards(self):
        card0 = StudyCard('What is my name?', 'Jonathan')
        card1 = StudyCard("What is bird's name ?", "Gandalf")
        card2 = StudyCard("What is the meaning of life ?", "42")
        self.set_instance.add(card0)
        self.set_instance.add(card1)
        self.set_instance.add(card2)

        index = 0
        for card in self.set_instance:
            index += 1
            self.assertIsInstance(card, StudyCard)

        self.assertEqual(index, 3)

    def test_len_studyset(self):
        # Should return the number of cards in this study set
        card0 = StudyCard('What is my name?', 'Jonathan')
        card1 = StudyCard("What is bird's name ?", "Gandalf")
        card2 = StudyCard("What is the meaning of life ?", "42")
        self.set_instance.add(card0)
        self.set_instance.add(card1)
        self.set_instance.add(card2)

        self.assertEqual(len(self.set_instance), 3)

    def test_to_dict(self):
        card = StudyCard('What is my name?', 'Jonathan')
        self.set_instance.add(card)

        data = self.set_instance.to_dict()
        expected = {'title': 'Maths', 'description': 'A study set about maths'}

        # List of serialized cards in this set
        cards = [c.to_dict() for c in self.set_instance]
        expected['cards'] = cards

        self.assertEqual(expected, data)
