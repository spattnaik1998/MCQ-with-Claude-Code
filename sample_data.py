from models import Assignment, Question
from api import assignments_db

def create_sample_data():
    questions = [
        Question(
            id="q1",
            text="What is the capital of France?",
            options=["London", "Berlin", "Paris", "Madrid"],
            correct_answer=2
        ),
        Question(
            id="q2", 
            text="Which of the following is a programming language?",
            options=["HTML", "CSS", "Python", "SQL"],
            correct_answer=2
        ),
        Question(
            id="q3",
            text="What is 2 + 2?",
            options=["3", "4", "5", "6"],
            correct_answer=1
        ),
        Question(
            id="q4",
            text="What does HTML stand for?",
            options=["Home Tool Markup Language", "Hyperlinks and Text Markup Language", "HyperText Markup Language", "High-level Text Markup Language"],
            correct_answer=2
        ),
        Question(
            id="q5",
            text="Which planet is known as the Red Planet?",
            options=["Venus", "Mars", "Jupiter", "Saturn"],
            correct_answer=1
        ),
        Question(
            id="q6",
            text="What is the largest ocean on Earth?",
            options=["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            correct_answer=3
        ),
        Question(
            id="q7",
            text="In which year did World War II end?",
            options=["1944", "1945", "1946", "1947"],
            correct_answer=1
        ),
        Question(
            id="q8",
            text="What is the square root of 64?",
            options=["6", "7", "8", "9"],
            correct_answer=2
        ),
        Question(
            id="q9",
            text="Which programming language is known for its use in data science?",
            options=["JavaScript", "C++", "Python", "Java"],
            correct_answer=2
        ),
        Question(
            id="q10",
            text="What is the chemical symbol for gold?",
            options=["Go", "Gd", "Au", "Ag"],
            correct_answer=2
        )
    ]
    
    assignment = Assignment(
        id="assignment1",
        title="General Knowledge Quiz",
        description="A comprehensive quiz covering geography, programming, math, history, and science",
        questions=questions,
        time_limit_minutes=45
    )
    
    assignments_db[assignment.id] = assignment
    
    print(f"Created sample assignment: {assignment.title}")
    print(f"Assignment ID: {assignment.id}")
    print(f"Number of questions: {len(assignment.questions)}")

if __name__ == "__main__":
    create_sample_data()