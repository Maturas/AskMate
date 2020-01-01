from flask import Flask, render_template, redirect, url_for
from data_manager import get_questions, get_question, get_answers
from question import Question
from fileio import save

app = Flask(__name__)


@app.route('/')
def index():
    question = Question(0, 'TEST', 'Uhahahamodafoka', '')
    save('questions.csv', Question.get_fieldnames(), [question])

    return redirect(url_for('list_questions'))


@app.route('/list')
def list_questions():
    questions = sorted(get_questions(), key=lambda x: x.submission_time)
    return render_template('list.html', questions=questions)


@app.route('/question/<question_id>')
def display_question(question_id):
    question = get_question(int(question_id))

    if question is None:
        return f'Error. Question with id: {question_id} not found.'

    answers = get_answers(question.id)

    question.view_number += 1

    return render_template('question.html', question=question, answers=answers)


if __name__ == '__main__':
    app.run()
