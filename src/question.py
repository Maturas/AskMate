from datetime import datetime


class Question:

    def __init__(self, question_id, title, message, image):
        self.id = question_id
        self.title = title
        self.message = message
        self.image = image

        self.submission_time = datetime.now().strftime('%d%m%y')

        self.view_number = 0
        self.vote_number = 0

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'image': self.image,
            'submission_time': self.submission_time,
            'view_number': self.view_number,
            'vote_number': self.vote_number
        }

        return data

    @classmethod
    def from_dict(cls, data):
        question_id = int(data['id'])
        title = data['title']
        message = data['message']
        image = data['image']

        question = cls(question_id, title, message, image)

        question.view_number = int(data['view_number'])
        question.vote_number = int(data['vote_number'])
        question.submission_time = data['submission_time']

        return question

    @staticmethod
    def get_fieldnames():
        return ['id', 'title', 'message', 'image', 'submission_time', 'view_number', 'vote_number']
