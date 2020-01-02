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
    answers = load('answers.csv', Answer)


def save_questions():
    save('questions.csv', Question.get_fieldnames(), questions)


def save_answers():
    save('answers.csv', Answer.get_fieldnames(), answers)


def get_questions():
    global questions

    if questions is None:
        load_questions()

    return questions


def get_question(question_id):
    # search for the matching question id
    search_results = [x for x in get_questions() if x.id == question_id]

    if len(search_results) == 0:
        return None
    else:
        return search_results[0]


def get_answers(question_id=None):
    global answers

    if answers is None:
        load_answers()

    if question_id is None:
        return answers
    else:
        # search for matching question ids
        results = [x for x in answers if x.question_id == question_id]
        return results


def get_answer(answer_id):
    # search for the matching answer id
    search_results = [x for x in get_answers() if x.id == answer_id]

    if len(search_results) == 0:
        return None
    else:
        return search_results[0]


def add_question(title, message):
    global questions

    # make sure that questions are loaded
    get_questions()

    question_id = 0

    # search for the latest id
    if len(questions) > 0:
        question_id = sorted([x.id for x in questions])[-1] + 1

    questions.append(Question(question_id, title, message, ''))
    save_questions()

    # return the id for redirecting to the display page
    return question_id


def add_answer(question_id, message):
    global answers

    # make sure that a question of given id exists
    if get_question(question_id) is None:
        return

    # make sure that answers are loaded
    get_answers()

    answer_id = 0

    # search for the latest id
    if len(answers) > 0:
        answer_id = sorted([x.id for x in answers])[-1] + 1

    answers.append(Answer(answer_id, question_id, message, ''))
    save_answers()


def delete_question(question_id):
    global questions

    question = get_question(question_id)

    if questions is not None:
        questions.remove(question)
        save_questions()


def delete_answer(answer_id):
    global answers

    answer = get_answer(answer_id)

    if answer is not None:
        answers.remove(answer)
        save_answers()
