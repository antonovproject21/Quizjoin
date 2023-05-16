# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from quizzes import quizzes

app = Flask(__name__)
CORS(app)

# Get all quizzes
@app.route('/quizzes', methods=['GET'])
def get_quizzes():
    return jsonify(quizzes)

# Get a specific quiz by ID
@app.route('/quizzes/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    quiz = [quiz for quiz in quizzes if quiz['id'] == quiz_id]
    if len(quiz) == 0:
        return jsonify({'error': 'Quiz not found'})
    return jsonify(quiz[0])

# Add a new quiz
@app.route('/quizzes', methods=['POST'])
def add_quiz():
    new_quiz = {
        'id': quizzes[-1]['id'] + 1,
        'title': request.json['title'],
        'questions': request.json['questions']
    }
    quizzes.append(new_quiz)
    return jsonify({'message': 'Quiz added successfully'})

# Update an existing quiz
@app.route('/quizzes/<int:quiz_id>', methods=['PUT'])
def update_quiz(quiz_id):
    quiz = [quiz for quiz in quizzes if quiz['id'] == quiz_id]
    if len(quiz) == 0:
        return jsonify({'error': 'Quiz not found'})
    quiz[0]['title'] = request.json['title']
    quiz[0]['questions'] = request.json['questions']
    return jsonify({'message': 'Quiz updated successfully'})

# Delete a quiz
@app.route('/quizzes/<int:quiz_id>', methods=['DELETE'])
def delete_quiz(quiz_id):
    quiz = [quiz for quiz in quizzes if quiz['id'] == quiz_id]
    if len(quiz) == 0:
        return jsonify({'error': 'Quiz not found'})
    quizzes.remove(quiz[0])
    return jsonify({'message': 'Quiz deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

# quizzes.py (Data for testing)
quizzes = [
    {
        'id': 1,
        'title': 'General Knowledge Quiz',
        'questions': [
            {'question': 'What is the capital of France?', 'answer': 'Paris'},
            {'question': 'Who painted the Mona Lisa?', 'answer': 'Leonardo da Vinci'},
            {'question': 'Which planet is known as the Red Planet?', 'answer': 'Mars'}
        ]
    },
    {
        'id': 2,
        'title': 'Science Quiz',
        'questions': [
            {'question': 'What is the atomic symbol for gold?', 'answer': 'Au'},
            {'question': 'Who developed the theory of general relativity?', 'answer': 'Albert Einstein'},
            {'question': 'What is the largest organ in the human body?', 'answer': 'Skin'}
        ]
    }
]
