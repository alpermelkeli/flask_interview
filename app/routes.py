from flask import render_template, request, redirect, url_for, flash, session
from app.models import Question
from app import app, db

@app.route('/quizPage')
def quiz_page():
    questions = Question.query.all()
    max_score = session.get('max_score', 0)
    return render_template('quiz_template.html', 
                         questions=questions, 
                         max_score=max_score,
                         total_questions=len(questions))

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    questions = Question.query.all()
    score = 0
    total_questions = len(questions)
    submitted_answers = {}
    
    for question in questions:
        submitted_answer = request.form.get(f'answer{question.id}')
        submitted_answers[question.id] = submitted_answer
        if submitted_answer == question.correct_answer:
            score += 1
    
    current_max_score = session.get('max_score', 0)
    if score > current_max_score:
        session['max_score'] = score
    
    percentage = (score / total_questions) * 100
    flash(f'Puanınız: {score}/{total_questions} (%{percentage:.1f})')
    
    return render_template('quiz_template.html',
                         questions=questions,
                         submitted_answers=submitted_answers,
                         score=score,
                         max_score=session.get('max_score', 0),
                         total_questions=total_questions)