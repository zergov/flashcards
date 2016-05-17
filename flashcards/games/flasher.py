class CardFlasher(object):
    """
    Contains the logic and the options behind the itteration on a StudySet.
    """

    def __init__(self, study_set):
        """
        Creates the CardFlasher object.

        :param study_set: The flashcards.sets.StudySet to enumerate through
        """
        self._study_set = study_set

        # Initialize the Flasher to start at the first card
        self._current_card = 0

    def get_current_card(self):
        """
        Get the current selected card.

        :returns: The card object that is currently selected.
        """
        index = self._current_card
        return self._study_set.get(index)
