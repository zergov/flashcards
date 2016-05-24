from flashcards.cards import StudyCard


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
        self._cards = []

    def __iter__(self):
        """Iter through the cards of this set."""
        for card in self._cards:
            yield card

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

    def get(self, index):
        """
        Get a card from the set by its index.

        :param index: The index of the card

        :returns: The BaseCard object.
        """
        return self._cards[index]

    def add(self, card):
        """
        Add a card to the end of this set.

        :param card: A subclass of flashcards.cards.BaseCard object.
        """
        if isinstance(card, StudyCard):
            self._cards.append(card)
        else:
            raise TypeError("A Set can only contain subclasses of "
                            "flashcards.cards.BaseCard")

    def remove(self, index):
        """
        Remove a card by its index

        :param index: The index of the card
        """
        del self._cards[index]
