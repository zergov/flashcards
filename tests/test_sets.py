import unittest

from flashcards.sets import StudySet


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
