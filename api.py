from flask import Flask, request, jsonify, render_template
from typing import Dict, List
from models import Assignment, Question, Submission, Answer
from datetime import datetime
import json

app = Flask(__name__)

assignments_db: Dict[str, Assignment] = {}
submissions_db: Dict[str, Submission] = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assignments', methods=['GET'])
def get_assignments():
    assignments_list = []
    for assignment in assignments_db.values():
        assignment_dict = {
            'id': assignment.id,
            'title': assignment.title,
            'description': assignment.description,
            'time_limit_minutes': assignment.time_limit_minutes,
            'created_at': assignment.created_at.isoformat(),
            'question_count': len(assignment.questions)
        }
        assignments_list.append(assignment_dict)
    
    return jsonify({'assignments': assignments_list})

@app.route('/assignments/<assignment_id>', methods=['GET'])
def get_assignment(assignment_id):
    if assignment_id not in assignments_db:
        return jsonify({'error': 'Assignment not found'}), 404
    
    assignment = assignments_db[assignment_id]
    questions_list = []
    
    for question in assignment.questions:
        question_dict = {
            'id': question.id,
            'text': question.text,
            'options': question.options
        }
        questions_list.append(question_dict)
    
    assignment_dict = {
        'id': assignment.id,
        'title': assignment.title,
        'description': assignment.description,
        'questions': questions_list,
        'time_limit_minutes': assignment.time_limit_minutes,
        'created_at': assignment.created_at.isoformat()
    }
    
    return jsonify(assignment_dict)

@app.route('/assignments/<assignment_id>/submit', methods=['POST'])
def submit_assignment(assignment_id):
    if assignment_id not in assignments_db:
        return jsonify({'error': 'Assignment not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    student_id = data.get('student_id')
    answers_data = data.get('answers', [])
    
    if not student_id:
        return jsonify({'error': 'Student ID is required'}), 400
    
    if not answers_data:
        return jsonify({'error': 'No answers provided'}), 400
    
    answers = []
    for answer_data in answers_data:
        answer = Answer(
            question_id=answer_data.get('question_id'),
            selected_option=answer_data.get('selected_option')
        )
        answers.append(answer)
    
    submission = Submission(
        id='',
        assignment_id=assignment_id,
        student_id=student_id,
        answers=answers
    )
    
    score = calculate_score(assignment_id, answers)
    submission.score = score
    
    submissions_db[submission.id] = submission
    
    return jsonify({
        'submission_id': submission.id,
        'score': score,
        'submitted_at': submission.submitted_at.isoformat()
    })

@app.route('/submissions/<submission_id>', methods=['GET'])
def get_submission(submission_id):
    if submission_id not in submissions_db:
        return jsonify({'error': 'Submission not found'}), 404
    
    submission = submissions_db[submission_id]
    answers_list = []
    
    for answer in submission.answers:
        answer_dict = {
            'question_id': answer.question_id,
            'selected_option': answer.selected_option
        }
        answers_list.append(answer_dict)
    
    submission_dict = {
        'id': submission.id,
        'assignment_id': submission.assignment_id,
        'student_id': submission.student_id,
        'answers': answers_list,
        'score': submission.score,
        'submitted_at': submission.submitted_at.isoformat()
    }
    
    return jsonify(submission_dict)

def calculate_score(assignment_id: str, answers: List[Answer]) -> float:
    if assignment_id not in assignments_db:
        return 0.0
    
    assignment = assignments_db[assignment_id]
    correct_answers = 0
    total_questions = len(assignment.questions)
    
    question_map = {q.id: q for q in assignment.questions}
    
    for answer in answers:
        if answer.question_id in question_map:
            question = question_map[answer.question_id]
            if answer.selected_option == question.correct_answer:
                correct_answers += 1
    
    return (correct_answers / total_questions) * 100 if total_questions > 0 else 0.0

if __name__ == '__main__':
    app.run(debug=True)