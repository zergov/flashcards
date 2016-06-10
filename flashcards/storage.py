import os

from flashcards.utils import storage as storageUtils
from flashcards import sets

"""
The directory name where all of the Flashcards data is stored on the machine.
"""
STORAGE_DIR_NAME = '.flashcards'


"""
The directory name where all of the Flashcards's study set data
is stored on the machine.
"""
STUDY_SET_STORAGE_DIR = 'studysets'


""" Default extension of a study set file on the machine """
STUDY_SET_EXTENSION = '.json'


def create_study_set_file(study_set):
    """
    Create a file and store the supplied study_set in it.

    :param study_set: the study set to store.
    """
    filepath = _generate_study_set_filepath(study_set)

    if os.path.isfile(filepath) or os.path.exists(filepath):
        raise IOError('A file already exist, cannot create study set.')

    # Create the file
    open(filepath, 'a').close()

    # Store the study set in the file
    store_study_set(study_set)


def store_study_set(study_set):
    """
    Store the supplied study set in the storage folder.

    An exception is raised if the file does not exists.

    :param study_set: the study set to store.
    """
    filepath = _generate_study_set_filepath(study_set)

    storage_item = StudySetStorage(filepath)
    storage_item.save(study_set)


def load_study_set(filepath):
    """
    Attempt to load the study set from a storage item.

    :param filepath: the filepath of the study set file

    :returns: StudySetStorage object
    """
    storageUtils.assert_valid_file(filepath)
    return StudySetStorage(filepath)


class StudySetStorage(storageUtils.JSONFileStorage):
    """
    Utility object to load and save a StudySet object from a
    file on the machine.
    """
    def load(self):
        """
        Load and return the StudySet contain in this file.

        :returns: a StudySet object
        """
        content = super(StudySetStorage, self).load()
        return sets.create_from_dict(content)

    def save(self, study_set):
        """ Save the provided StudySet object in the current file. """
        data = study_set.to_dict()
        super(StudySetStorage, self).save(data)

        # rename the name of this file by the title of this study set.
        filename = storageUtils.generate_filename_from_str(study_set.title)
        self._rename_filename(filename)


def _get_storage_path():
    """ Get the absolute storage path on the machine """
    return os.path.join(os.path.expanduser('~'), STORAGE_DIR_NAME)


def _get_study_set_storage_path():
    """ Get the absolute storage path for the study sets on the machine """
    return os.path.join(os.path.expanduser('~'),
                        STORAGE_DIR_NAME, STUDY_SET_STORAGE_DIR)


def _generate_study_set_filepath(study_set):
    """
    Generate the absolute filepath in which the given study set
    should be stored

    :param study_set: the study set to store.

    :returns: absolute file path to the storage file.
    """
    filename = storageUtils.generate_filename_from_str(study_set.title)
    filename = filename + STUDY_SET_EXTENSION
    return os.path.join(_get_study_set_storage_path(), filename)
