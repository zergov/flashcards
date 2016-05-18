import random

class CardFlasher(object):
    """
    Contains the logic and the options behind the itteration on a list of cards.
    """

    def __init__(self, cards):
        """
        Creates the CardFlasher object.

        :param cards: A list of BaseCard object
        """
        self._cards = cards

        # Initialize the Flasher to start at the first card
        self._current_card_index = 0

    @property
    def current_card(self):
        """
        Get the current selected card.

        :returns: The card object that is currently selected.
        """
        index = self._current_card_index
        return self._cards[index]

    def next(self):
        """
        Set the selection to the next card in the set.
        """
        if self._current_card_index + 1 < len(self._cards):
            self._current_card_index += 1

    def previous(self):
        """
        Set the selection to the previous card in the set.
        """
        if not self._current_card_index - 1 < 0:
            self._current_card_index -= 1

    def shuffle(self):
        """
        Randomize the order of the cards.
        """
        random.shuffle(self._cards)
