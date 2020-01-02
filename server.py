from flask import Flask, render_template, redirect, url_for, request
import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    # TODO Main page
    return redirect(url_for('list_questions'))


@app.route('/list')
def list_questions():
    questions = sorted(data_manager.get_questions(), key=lambda x: x.submission_time, reverse=True)
    return render_template('list.html', questions=questions)


@app.route('/question/<question_id>')
def display_question(question_id):
    question = data_manager.get_question(int(question_id))

    if question is None:
        return f'Error. Question with id: {question_id} not found.'

    answers = data_manager.get_answers(question.id)

    question.view_number += 1

    return render_template('display-question.html', question=question, answers=answers)


@app.route('/add-question')
def add_question():
    return render_template('add-question.html')


@app.route('/add-question-handler', methods=['POST'])
def add_question_handler():
    title = request.form['title']
    message = request.form['message']

    question_id = data_manager.add_question(title, message)

    return redirect(url_for('display_question', question_id=question_id))


if __name__ == '__main__':
    app.run()
