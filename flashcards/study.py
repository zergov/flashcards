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

    def start(self, study_strategy):
        """
        Start a StudySession with the given study strategy.

        :param study_strategy: an instance of StudyStrategy.
        """
        for card in self._cards:
            study_strategy.show(card)
