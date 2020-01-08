import psycopg2
from question import Question
from answer import Answer
import datetime

cursor = None


def init():
    global cursor
    try:
        user_name = "user"
        password = "123"
        host = "localhost"
        database_name = "AskMate"

        connect_str = f"postgresql://{user_name}:{password}@{host}/{database_name}"

        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        cursor = connection.cursor()
    except psycopg2.DatabaseError as exception:
        print(exception)


def get_questions():
    global cursor
    cursor.execute("SELECT * FROM question;")
    data = cursor.fetchall()

    questions = []

    # convert tuples to Question objects
    for x in data:
        questions.append(Question.from_tuple(x))

    return questions


def get_question(question_id):
    global cursor
    cursor.execute("SELECT * FROM question WHERE question.id = %s LIMIT 1", [question_id])
    data = cursor.fetchall()

    if len(data) == 0:
        return None

    return Question.from_tuple(data[0])


def get_answers(question_id):
    global cursor
    cursor.execute("SELECT * FROM answer WHERE answer.question_id = %s", [question_id])
    data = cursor.fetchall()

    answers = []

    # convert tuples to Answer objects
    for x in data:
        answers.append(Answer.from_tuple(x))

    return answers


def get_answer(answer_id):
    global cursor
    cursor.execute("SELECT * FROM answer WHERE answer.id = %s LIMIT 1", [answer_id])
    data = cursor.fetchall()

    if len(data) == 0:
        return None

    return Answer.from_tuple(data[0])


def add_question(title, message):
    global cursor

    # get the latest id
    cursor.execute("SELECT id FROM question ORDER BY DESC id LIMIT 1")
    question_id = cursor.fetchall()[0][0] + 1

    date = datetime.datetime.now()

    cursor.execute("INSERT INTO question (id, submission_time, view_number, vote_number, title, message)"
                   "VALUES (%s, %s, %s, %s, %s, %s)", [question_id, date, 0, 0, title, message])

    # return the id for redirecting to the display page
    return question_id


def add_answer(question_id, message):
    global cursor

    # get the latest id
    cursor.execute("SELECT id FROM answer ORDER BY id DESC LIMIT 1")
    answer_id = cursor.fetchall()[0][0] + 1

    date = datetime.datetime.now()

    cursor.execute("INSERT INTO answer (id, submission_time, vote_number, question_id, message)"
                   "VALUES (%s, %s, %s, %s, %s)", [answer_id, date, 0, question_id, message])

    # return the id for redirecting to the display page
    return answer_id


def delete_question(question_id):
    global cursor

    cursor.execute("DELETE FROM question WHERE question.id = %s", [question_id])


def delete_answer(answer_id):
    global cursor

    cursor.execute("DELETE FROM answer WHERE answer.id = %s", [answer_id])


def edit_question(question_id, title, message):
    global cursor

    cursor.execute("UPDATE question SET title = %s, message = %s WHERE question.id = %s", [title, message, question_id])


def edit_answer(answer_id, message):
    global cursor

    cursor.execute("UPDATE answer SET message = %s WHERE answer.id = %s", [message, answer_id])


def vote_item(item_id, vote_delta, table_name):
    global cursor

    cursor.execute(f"UPDATE {table_name} SET vote_number = vote_number + %s WHERE {table_name}.id = %s",
                   [vote_delta, item_id])


def update_question_views(question_id):
    global cursor

    cursor.execute("UPDATE question SET view_number = view_number + 1 WHERE question.id = %s", [question_id])


def add_comment(question_id, answer_id, message):
    global cursor

    # get the latest id
    cursor.execute("SELECT id FROM comment ORDER BY id DESC LIMIT 1")
    comment_id = cursor.fetchall()[0][0] + 1

    date = datetime.datetime.now()

    cursor.execute("INSERT INTO comment (comment_id, question_id, answer_id, submission_time, message, edited_count) "
                   "VALUES (%s, %s, %s, %s)", [comment_id, question_id, answer_id, date, message, 0])


def edit_comment(comment_id, message):
    date = datetime.datetime.now()

    cursor.execute("UPDATE comment SET message = %s, edited_count = edited_count + 1, submission_time = %s "
                   "WHERE comment.id = %s", [message, date, comment_id])


def delete_comment(comment_id):
    global cursor

    cursor.execute("DELETE FROM comment WHERE comment.id = %s", [comment_id])
