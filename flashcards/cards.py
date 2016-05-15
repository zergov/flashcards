class BaseCard(object):
    """
    Basic class representing a question card.
    """

    def __init__(self, question, answer):

        self._question = question
        self._answer = answer
