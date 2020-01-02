from datetime import datetime


class Answer:

    def __init__(self, answer_id, question_id, message, image):
        self.id = answer_id
        self.question_id = question_id
        self.message = message
        self.image = image

        self.submission_time = datetime.now().timestamp()

        self.vote_number = 0

    def to_dict(self):
        data = {
            'id': self.id,
            'question_id': self.question_id,
            'message': self.message,
            'image': self.image,
            'submission_time': self.submission_time,
            'vote_number': self.vote_number
        }

        return data

    def get_date(self):
        return datetime.fromtimestamp(self.submission_time).strftime('%X %x')

    @classmethod
    def from_dict(cls, data):
        answer_id = int(data['id'])
        question_id = int(data['question_id'])
        message = data['message']
        image = data['image']

        answer = cls(answer_id, question_id, message, image)

        answer.vote_number = int(data['vote_number'])
        answer.submission_time = float(data['submission_time'])

        return answer

    @staticmethod
    def get_fieldnames():
        return ['id', 'question_id', 'message', 'image', 'submission_time', 'vote_number']