from datetime import date


class Question:

    def __init__(self, question_id, title, message, image):
        self.id = question_id
        self.title = title
        self.message = message
        self.image = image

        self.submission_time = date.today()

        self.view_number = 0
        self.vote_number = 0

    @classmethod
    def from_tuple(cls, data):
        question_id = data[0]
        submission_time = data[1]
        view_number = data[2]
        vote_number = data[3]
        title = data[4]
        message = data[5]
        image = data[6]

        question = cls(question_id, title, message, image)

        question.submission_time = submission_time
        question.view_number = view_number
        question.vote_number = vote_number

        return question

    @staticmethod
    def get_fieldnames():
        return ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
