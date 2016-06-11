import unittest
import mock

from flashcards import storage
from flashcards.utils import storage as storageUtils
from flashcards.storage import StudySetStorage
from flashcards.sets import StudySet
from flashcards.cards import StudyCard


class TestStorageModule(unittest.TestCase):

    @mock.patch('flashcards.storage.os.path.expanduser')
    def test_get_storage_path(self, mock_expand_usr):

        mock_expand_usr.return_value = '/home/admin'
        self.assertEqual('/home/admin/.flashcards', storage.storage_path())

    def test_generate_filename_from_str_spaces(self):
        result = storageUtils.generate_filename_from_str('file name')
        expected = 'file_name'
        self.assertEqual(expected, result)

    def test_generate_filename_from_str_dashes(self):
        result = storageUtils.generate_filename_from_str('file-name')
        expected = 'file_name'
        self.assertEqual(expected, result)

    def test_generate_filename_from_str_alphanum(self):
        result = storageUtils.generate_filename_from_str('!f@i#l$e%-^n&a*m(e)0')
        expected = 'file_name0'
        self.assertEqual(expected, result)


class TestStoredStudySet(unittest.TestCase):

    @mock.patch('flashcards.storage.os.path.isfile')
    def test_load_study_set_error_filenoexist(self, mock_filecheck):

        stored_set = StudySetStorage('/home/usr/.flashcards/set01.json')

        # Should raise an error because the file does not exist
        mock_filecheck.return_value = False
        self.assertRaises(IOError, stored_set.load)

    @mock.patch('flashcards.storage.os.rename')
    def test_rename_filename(self, mock_rename):

        stored_set = StudySetStorage('/home/usr/.flashcards/set01.json')

        study_set = StudySet('maths145', 'Maths questions')
        study_set.add(StudyCard('2+2=?', '4'))

        newname = storageUtils.generate_filename_from_str(study_set.title)
        stored_set._rename_filename(newname)

        expected = '/home/usr/.flashcards/maths145.json'
        self.assertEqual(expected, stored_set._filepath)
