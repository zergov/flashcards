import os
import json

from flashcards import sets

STORAGE_DIR_NAME = '.flashcards'
STUDY_SET_EXTENSION = '.json'


def create_study_set_file(study_set):
    """
    Create a file and store the supplied study_set in it.

    :param study_set: the study set to store.
    """
    filename = _generate_filename_from_str(study_set.title)
    filepath = os.path.join(_get_storage_path(), filename)

    if os.path.isfile(filepath) or os.path.exists(filepath):
        raise IOError('A file already exist, cannot create study set.')

    # Create the file
    open(filepath, 'a').close()


def store_study_set(study_set):
    """
    Store the supplied study set in the storage folder.

    :param study_set: the study set to store.
    """
    filename = _generate_filename_from_str(study_set.title)
    filepath = os.path.join(_get_storage_path(), filename)

    storage_item = StudySetStorage(filepath)
    storage_item.save(study_set)


class FileStorage(object):
    """
    Utility object that manage the reading / saving of a file while assuring
    that the file is closed once we're done using it.
    """
    def __init__(self, filepath):
        self._filepath = filepath

    def load(self):
        """
        Load and return the data stored in this file.

        :returns: dictionary object.
        """
        return self._load_raw_content()

    def _load_raw_content(self):
        """Read and return the raw data in this file."""
        self._assert_valid_file()

        content = None
        with open(self._filepath, 'r') as file:
            content = file.read()

        return content

    def save(self, content):
        """
        Save new content in this file.

        :param content: new content to store in this file.
        """
        self._save_raw_content(content)

    def _save_raw_content(self, content):
        """
        Open and write the provided data in this file.
        Overwriting the data already stored in this file.

        :param content: the content to store in this file.
        """
        self._assert_valid_file()

        with open(self._filepath, 'w') as file:
            file.write(content)

    def _assert_valid_file(self):
        """
        Raise an exception if the file at the given path is not a file or
        does not exists.
        """
        if not os.path.isfile(self._filepath):
            raise IOError("path: %s is not a file" % self._filepath)
        if not os.path.exists(self._filepath):
            raise IOError("path: %s does not exists" % self._filepath)

    def _rename_filename(self, filename):
        """
        Without changing the path and the extension, rename the
        base name of the file.

        :param filename: the new name for this file.
        """
        directory = os.path.dirname(self._filepath)  # keep the same path
        extension = os.path.splitext(self._filepath)[1]  # keep the extension

        # Concatenate the new path for the file, rename the file and update the
        # _filepath variable.
        new_path = os.path.join(directory, filename + extension)
        os.rename(self._filepath, new_path)
        self._filepath = new_path


class JSONFileStorage(FileStorage):
    """
    Utility object to save and load serialized JSON objects stored in a file.
    """
    def load(self):
        """
        Load and serialize the data in this file.

        :returns: a dictionary object
        """
        content = self._load_raw_content()
        return self._deserialize(content)

    def save(self, content):
        """
        Serialize and save the content in this file.

        :param content: the content to save
        """
        content = self._serialize(content)
        self._save_raw_content(content)

    def _serialize(self, data):
        """
        Serializing function used by this module.

        :param data: the dictionary to serialize

        :returns: a string of representation of the serialized object
        """
        return json.dumps(data, sort_keys=False, indent=4,
                          separators=(',', ': '))

    def _deserialize(self, string):
        """
        Deserializing function used by this module.

        :param string: the string to deserialize

        :returns: the dictionary representation of the deserialized string
        """
        return json.loads(string)


class StudySetStorage(JSONFileStorage):
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
        filename = _generate_filename_from_str(study_set.title)
        self._rename_filename(filename)


def _generate_filename_from_str(string):
    """
    Generate a valid filename from a given string.

    - replace all spaces and dashes with underscore.
    - only keeps alphanumerical chars

    :param string: the string to create the filename from

    :returns: the generated string, a valid filename
    """
    keepchars = [' ', '-', '_']  # characters to keep in the filename
    swapchars = {' ': '_', '-': '_'}  # keys are swapped by their values

    for key, value in swapchars.items():
        string = string.replace(key, value)

    _ = [c for c in string if c.isalnum() or c is ' ' or c in keepchars]
    return ''.join(_).rstrip()


def _get_storage_path():
    """ Get the absolute storage path on the machine """
    return os.path.join(os.path.expanduser('~'), STORAGE_DIR_NAME)
