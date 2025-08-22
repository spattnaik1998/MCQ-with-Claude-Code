# Multiple Choice Assignment System

A modern web-based multiple choice quiz application built with Python Flask and vanilla JavaScript. Features a clean, responsive UI and RESTful API for creating and managing quiz assignments.

## 🚀 Features

- **Interactive Quiz Interface**: Clean, modern UI with responsive design
- **RESTful API**: Complete backend API for quiz management
- **Real-time Scoring**: Automatic scoring and instant feedback
- **Student Tracking**: Track submissions with unique student IDs
- **Flexible Question Management**: Easy to add/modify questions
- **Docker Support**: Containerized deployment ready

## 📋 Demo Quiz Topics

The application comes with a 10-question general knowledge quiz covering:
- Geography (Capitals, Oceans)
- Programming (Languages, HTML, Data Science)
- Mathematics (Basic arithmetic, Square roots)
- History (World War II)
- Science (Planets, Chemistry)

## 🛠️ Technology Stack

- **Backend**: Python 3.9, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Containerization**: Docker & Docker Compose
- **Styling**: Modern CSS with gradients and animations

## 🚀 Quick Start

### Option 1: Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Simple_Agentic_Coding
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

### Option 2: Local Development

1. **Clone and setup**
   ```bash
   git clone <your-repo-url>
   cd Simple_Agentic_Coding
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## 📚 API Documentation

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main quiz interface |
| GET | `/assignments` | Get all assignments |
| GET | `/assignments/<id>` | Get specific assignment |
| POST | `/assignments/<id>/submit` | Submit quiz answers |
| GET | `/submissions/<id>` | Get submission details |

### API Examples

**Get all assignments:**
```bash
curl http://localhost:8000/assignments
```

**Submit answers:**
```bash
curl -X POST http://localhost:8000/assignments/assignment1/submit \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": "student123",
    "answers": [
      {"question_id": "q1", "selected_option": 2},
      {"question_id": "q2", "selected_option": 2}
    ]
  }'
```

## 🏗️ Project Structure

```
Simple_Agentic_Coding/
├── app.py              # Main application entry point
├── api.py              # Flask API routes and logic
├── models.py           # Data models (Question, Assignment, Submission)
├── sample_data.py      # Sample quiz data
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
├── templates/
│   └── index.html      # Main HTML template
└── static/
    ├── style.css       # CSS styling
    └── script.js       # JavaScript functionality
```

## 🎨 Features Showcase

- **Responsive Design**: Works seamlessly on desktop and mobile
- **Modern UI**: Clean interface with gradient backgrounds and hover effects
- **Real-time Feedback**: Instant scoring and submission confirmation
- **Easy Navigation**: Smooth transitions between assignment list and quiz views
- **Student Tracking**: Unique submission IDs for tracking purposes

## 🔧 Customization

### Adding New Questions

Edit `sample_data.py` to add more questions:

```python
Question(
    id="q11",
    text="Your question here?",
    options=["Option A", "Option B", "Option C", "Option D"],
    correct_answer=0  # Index of correct answer (0-3)
)
```

### Styling Modifications

Customize the appearance by editing `static/style.css`. The design uses CSS Grid and Flexbox for responsive layouts.

## 🚀 Deployment

### Docker Hub (Optional)

1. **Build and tag image**
   ```bash
   docker build -t your-username/quiz-app .
   ```

2. **Push to Docker Hub**
   ```bash
   docker push your-username/quiz-app
   ```

### Production Considerations

- Add environment variables for configuration
- Implement proper database storage (currently in-memory)
- Add authentication and authorization
- Set up logging and monitoring
- Configure reverse proxy (nginx)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created with ❤️ by [Your Name]

---

⭐ **Star this repository if you found it helpful!** ⭐