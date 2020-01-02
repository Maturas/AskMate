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
    question_id = int(question_id)
    question = data_manager.get_question(question_id)

    if question is None:
        return f'Error. Question with id: {question_id} not found.'

    answers = data_manager.get_answers(question.id)

    question.view_number += 1

    return render_template('display-question.html', question=question, answers=answers)


@app.route('/add-question', methods=['GET'])
def add_question_get():
    return render_template('add-question.html')


@app.route('/add-question', methods=['POST'])
def add_question_post():
    title = request.form['title']
    message = request.form['message']

    question_id = data_manager.add_question(title, message)

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<question_id>/new-answer', methods=['GET'])
def add_answer_get(question_id):
    question_id = int(question_id)
    question = data_manager.get_question(question_id)

    if question is None:
        return f'Error. Question with id: {question_id} not found.'

    return render_template('add-answer.html', question_id=question_id)


@app.route('/question/<question_id>/new-answer', methods=['POST'])
def add_answer_post(question_id):
    question_id = int(question_id)
    message = request.form['message']

    data_manager.add_answer(question_id, message)

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<question_id>/edit', methods=['GET'])
def edit_question_get(question_id):
    question_id = int(question_id)
    question = data_manager.get_question(question_id)

    if question is None:
        return f'Error. Question with id: {question_id} not found.'

    return render_template('edit-question.html', question=question)


@app.route('/question/<question_id>/edit', methods=['POST'])
def edit_question_post(question_id):
    question_id = int(question_id)
    question = data_manager.get_question(question_id)

    if question is None:
        return f'Error. Question with id: {question_id} not found.'

    question.title = request.form['title']
    question.message = request.form['message']

    data_manager.save_questions()

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/answer/<answer_id>/edit', methods=['GET'])
def edit_answer_get(answer_id):
    answer_id = int(answer_id)
    answer = data_manager.get_answer(answer_id)

    if answer is None:
        return f'Error. Answer with id: {answer_id} not found.'

    return render_template('edit-answer.html', answer=answer)


@app.route('/answer/<answer_id>/edit', methods=['POST'])
def edit_answer_post(answer_id):
    answer_id = int(answer_id)
    answer = data_manager.get_answer(answer_id)

    if answer is None:
        return f'Error. Answer with id: {answer_id} not found.'

    answer.message = request.form['message']
    data_manager.save_answers()

    return redirect(url_for('display_question', question_id=answer.question_id))


if __name__ == '__main__':
    app.run()
