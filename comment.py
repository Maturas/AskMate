class Comment:

    def __init__(self, comment_id, question_id, answer_id, message, submission_time, edited_count):
        self.id = comment_id
        self.question_id = question_id
        self.answer_id = answer_id
        self.message = message
        self.submission_time = submission_time
        self.edited_count = edited_count

    @classmethod
    def from_tuple(cls, data):
        comment_id = data[0]
        question_id = data[1]
        answer_id = data[2]
        message = data[3]
        submission_time = data[4]
        edited_count = data[5]

        comment = cls(comment_id, question_id, answer_id, message, submission_time, edited_count)

        return comment
