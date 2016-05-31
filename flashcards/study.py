import random


class StudySession(object):
    """
    Object that encapsulate a Study session. This object cycle through
    an iterator of StudyCard.
    """

    def __init__(self, cards):
        """
        Creates the CardFlasher object.

        :param cards: An iterator of StudyCard.
        """
        self._cards = cards
