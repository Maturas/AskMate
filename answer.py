class Answer:

    def __init__(self, answer_id, question_id, message, image, submission_time, vote_number):
        self.id = answer_id
        self.question_id = question_id
        self.message = message
        self.image = image
        self.submission_time = submission_time
        self.vote_number = vote_number

    @classmethod
    def from_tuple(cls, data):
        answer_id = data[0]
        submission_time = data[1]
        vote_number = data[2]
        question_id = data[3]
        message = data[4]
        image = data[5]

        answer = cls(answer_id, question_id, message, image, submission_time, vote_number)

        return answer
