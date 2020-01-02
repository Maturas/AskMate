from fileio import load, save
from question import Question
from answer import Answer

questions = None
answers = None


def load_questions():
    global questions
    questions = load('questions.csv', Question)


def load_answers():
    global answers
    answers = load('answer.csv', Answer)


def get_questions():
    global questions

    if questions is None:
        load_questions()

    return questions


def get_answers(question_id):
    global answers

    if answers is None:
        load_answers()

    # search for matching question ids
    return [x for x in answers if x.question_id == question_id]


def get_question(question_id):
    # search for the matching question id
    search_results = [x for x in get_questions() if x.id == question_id]

    if len(search_results) == 0:
        return None
    else:
        return search_results[0]


def add_question(title, message):
    global questions

    # make sure that questions are loaded
    load_questions()

    question_id = 0

    # search for the latest id
    if len(questions) > 0:
        question_id = sorted([x.id for x in questions])[-1] + 1

    questions.append(Question(question_id, title, message, ''))
    save('questions.csv', Question.get_fieldnames(), questions)

    # return the id for redirecting to the display page
    return question_id


def add_answer(question_id, message):
    global answers

    # make sure that answers are loaded
    load_answers(question_id)

    answer_id = 0

    # search for the latest id
    if len(answers) > 0:
        answer_id = sorted([x.id for x in answers])[-1] + 1

    answers.append(Answer(answer_id, question_id, message, ''))
    save('answers.csv', Answer.get_fieldnames(), answers)


