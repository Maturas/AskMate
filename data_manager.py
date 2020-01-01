from fileio import load
from question import Question
from answer import Answer

questions = None
answers = None


def get_questions():
    global questions

    if questions is None:
        questions = load('questions.csv', Question)

    return questions


def get_question(question_id):
    search_results = [x for x in get_questions() if x.id == question_id]

    if len(search_results) == 0:
        return None
    else:
        return search_results[0]


def get_answers(question_id):
    global answers

    if answers is None:
        answers = load('answers.csv', Answer)

    return [x for x in answers if x.question_id == question_id]
