from datetime import date


class Answer:

    def __init__(self, answer_id, question_id, message, image):
        self.id = answer_id
        self.question_id = question_id
        self.message = message
        self.image = image

        self.submission_time = date.today()

        self.vote_number = 0

    @classmethod
    def from_tuple(cls, data):
        answer_id = data[0]
        submission_time = data[1]
        vote_number = data[2]
        question_id = data[3]
        message = data[4]
        image = data[5]

        question = cls(answer_id, question_id, message, image)

        question.submission_time = submission_time
        question.vote_number = vote_number

        return question

    @staticmethod
    def get_fieldnames():
        return ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']