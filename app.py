from api import app
from sample_data import create_sample_data

if __name__ == '__main__':
    create_sample_data()
    print("Starting Multiple Choice Assignment API server...")
    print("Available endpoints:")
    print("- GET /assignments - Get all assignments")
    print("- GET /assignments/<id> - Get specific assignment")
    print("- POST /assignments/<id>/submit - Submit assignment answers")
    print("- GET /submissions/<id> - Get submission details")
    print()
    app.run(debug=True, port=8000)