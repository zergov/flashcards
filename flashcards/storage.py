"""
flashcards.storage
~~~~~~~~~~~~~~~~~~~

Contain the logic to load and save items in the Flashcards
storage directory on this machine.
"""


import os
import errno

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


""" Selected studyset filename """
SELECTED_STUDYSET_NAME = '.SELECTEDSTUDYSET'


def create_studyset_file(studyset):
    """
    Create a file and store the supplied studyset in it.

    :param study_set: the study set to store.
    """
    filepath = _generate_studyset_filepath(studyset)

    if os.path.isfile(filepath) or os.path.exists(filepath):
        raise IOError('A file already exist, cannot create study set.')

    # Create the file
    open(filepath, 'a').close()

    # Store the study set in the file
    store_studyset(studyset)
    return filepath


def store_studyset(studyset):
    """
    Store the supplied study set in the storage folder.

    An exception is raised if the file does not exists.

    :param study_set: the study set to store.
    """
    filepath = _generate_studyset_filepath(studyset)

    storage_item = StudySetStorage(filepath)
    storage_item.save(studyset)


def load_studyset(filepath):
    """
    Attempt to load the study set from a storage item.

    :param filepath: the filepath of the study set file

    :returns: StudySetStorage object
    """
    storageUtils.assert_valid_file(filepath)
    return StudySetStorage(filepath)


def link_selected_studyset(filepath):
    """
    Create a symbolic link to the selected studyset.

    :param filepath: the filepath of the studyset
    """
    linkpath = selected_studyset_path()

    # Force symlink
    try:
        os.symlink(filepath, linkpath)

    except OSError, e:
        if e.errno == errno.EEXIST:
            os.remove(linkpath)
            os.symlink(filepath, linkpath)


def load_selected_studyset():
    """
    Load and return the currently selected studyset.

    :returns: StudySet object.
    """
    item = StudySetStorage(selected_studyset_path())
    return item.load()


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


def storage_path():
    """ Get the absolute storage path on the machine """
    return os.path.join(os.path.expanduser('~'), STORAGE_DIR_NAME)


def studyset_storage_path():
    """ Get the absolute storage path for the study sets on the machine """
    return os.path.join(os.path.expanduser('~'),
                        STORAGE_DIR_NAME, STUDY_SET_STORAGE_DIR)


def selected_studyset_path():
    """
    Get the absolute path for the currently selected studyset
    on the machine.
    """
    return os.path.join(storage_path(), SELECTED_STUDYSET_NAME)


def _generate_studyset_filepath(study_set):
    """
    Generate the absolute filepath in which the given study set
    should be stored

    :param study_set: the study set to store.

    :returns: absolute file path to the storage file.
    """
    filename = storageUtils.generate_filename_from_str(study_set.title)
    filename = filename + STUDY_SET_EXTENSION
    return os.path.join(studyset_storage_path(), filename)


def verify_storage_dir_integrity():
    """ Check that the storage directory is intact. """

    path = storage_path()
    if not os.path.exists(path) or os.path.isfile(path):
        _create_storage_dir()

    path = studyset_storage_path()
    if not os.path.exists(path) or os.path.isfile(path):
        _create_studyset_storage_dir()


def _create_storage_dir():
    """ Create the storage directory in the home folder. """
    if os.path.exists(storage_path()) and os.path.isdir(storage_path()):
        raise IOError('Storage directory already exists.')

    os.mkdir(storage_path())


def _create_studyset_storage_dir():
    """ Create the studyset storage directory in the storage directory. """
    path = studyset_storage_path()
    if os.path.exists(path) and os.path.isdir(path):
        raise IOError('Studyset storage directory already exists.')

    os.mkdir(path)
