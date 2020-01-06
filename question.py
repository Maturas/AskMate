class Question:

    def __init__(self, question_id, title, message, image, submission_time, view_number, vote_number):
        self.id = question_id
        self.title = title
        self.message = message
        self.image = image
        self.submission_time = submission_time
        self.view_number = view_number
        self.vote_number = vote_number

    @classmethod
    def from_tuple(cls, data):
        question_id = data[0]
        submission_time = data[1]
        view_number = data[2]
        vote_number = data[3]
        title = data[4]
        message = data[5]
        image = data[6]

        question = cls(question_id, title, message, image, submission_time, view_number, vote_number)

        return question
