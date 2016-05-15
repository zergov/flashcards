class StudySet(object):
    """
    A StudySet is a container of flash cards.
    """

    def __init__(self, title, description=None):
        """
        Creates a Study set.

        :param title: The title of the study set.
        :param description: The description for this study set.
        """
        self._title = title
        self._description = description

    @property
    def title(self):
        """
        Get the title of this set.

        :returns: The title of this Study set.
        """
        return self._title

    @title.setter
    def title(self, value):
        """
        Set the title of this set.

        :param value: The new title for this set
        """
        if isinstance(value, basestring):
            self._title = value
        else:
            raise TypeError("StudySet title should be of type str")

    @property
    def description(self):
        """
        Get the description of this set.
        """
        return self._description

    @description.setter
    def description(self, value):
        """
        Set the description of this set.

        :param value: The new description for this set
        """
        if isinstance(value, basestring):
            self._description = value
        else:
            raise TypeError("StudySet description should be of type str")
