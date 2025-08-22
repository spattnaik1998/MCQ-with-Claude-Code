import requests
import json

BASE_URL = "http://localhost:8000"

def test_get_assignments():
    response = requests.get(f"{BASE_URL}/assignments")
    print("GET /assignments:")
    print(json.dumps(response.json(), indent=2))
    print()

def test_get_assignment(assignment_id):
    response = requests.get(f"{BASE_URL}/assignments/{assignment_id}")
    print(f"GET /assignments/{assignment_id}:")
    print(json.dumps(response.json(), indent=2))
    print()

def test_submit_assignment(assignment_id):
    submission_data = {
        "student_id": "student123",
        "answers": [
            {"question_id": "q1", "selected_option": 2},
            {"question_id": "q2", "selected_option": 2},
            {"question_id": "q3", "selected_option": 1}
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/assignments/{assignment_id}/submit",
        json=submission_data
    )
    print(f"POST /assignments/{assignment_id}/submit:")
    print(json.dumps(response.json(), indent=2))
    print()
    
    return response.json().get('submission_id')

def test_get_submission(submission_id):
    response = requests.get(f"{BASE_URL}/submissions/{submission_id}")
    print(f"GET /submissions/{submission_id}:")
    print(json.dumps(response.json(), indent=2))
    print()

if __name__ == "__main__":
    print("Testing Multiple Choice Assignment API")
    print("=" * 40)
    
    # Test getting all assignments
    test_get_assignments()
    
    # Test getting specific assignment
    assignment_id = "assignment1"
    test_get_assignment(assignment_id)
    
    # Test submitting assignment
    submission_id = test_submit_assignment(assignment_id)
    
    # Test getting submission
    if submission_id:
        test_get_submission(submission_id)