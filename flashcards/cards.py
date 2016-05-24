def create_card_from_dict(data):
    """
    Construct a StudyCard Object from a dictionary object.

    :param data: the dictionary object

    :raises KeyError: when dictionary is missing a needed field to create obj.

    :returns: StudyCard object
    """
    if 'question' not in data:
        raise KeyError("Invalid data string. 'question' key is missing")
    if 'answer' not in data:
        raise KeyError("Invalid data string. 'answer' key is missing")

    question = data['question']
    answer = data['answer']

    return StudyCard(question, answer)


class StudyCard(object):
    """
    Class representing a question card.

    A question card is simple card containing a Question and an Answer.
    """

    def __init__(self, question, answer):
        """
        Creates a Question card containing a question and an answer to the
        question.

        :param question: The question of the card.
        :param answer: The answer to the question.
        """
        self._question = question
        self._answer = answer

    @property
    def question(self):
        """
        Get the question of the card.

        :returns: The question of the card.
        """
        return self._question

    @question.setter
    def question(self, value):
        """
        Set a new value for the question of this card

        :param new_question: The new question

        :raises TypeError: If the question is not of type str
        """
        if isinstance(value, basestring):
            self._question = value
        else:
            raise TypeError('Question should be of type str')

    @property
    def answer(self):
        """
        Get the answer for the question

        :returns: The answer to the question.
        """
        return self._answer

    @answer.setter
    def answer(self, value):
        """
        Set a new value for the question of this card

        :param new_question: The new question

        :raises TypeError: If the question is not of type str
        """
        if isinstance(value, basestring):
            self._answer = value
        else:
            raise TypeError('Answer should be of type str')

    def to_dict(self):
        """
        Convert this StudyCard to a dictionary.

        :returns: a dictionary object representation of this StudyCard
        """
        return {'question': self.question, 'answer': self.answer}
