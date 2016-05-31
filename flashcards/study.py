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
        study_strategy.start(self._cards)


class SimpleStudyStrategy(object):
    """
    Simple linear study strategy. The cards are beeing showed one at
    a time, in order.
    """

    def start(self, cards):
        """
        Start iterating over a StudyCard iterator.

        Show the question of the card to the user. Wait for user input
        before showing the answer. Wait again for user input to show next
        card.

        :param cards: StudyCard iterator.
        """
        for card in cards:
            pass
