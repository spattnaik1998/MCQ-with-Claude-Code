const API_BASE = '';

let currentAssignment = null;

async function loadAssignments() {
    try {
        const response = await fetch('/assignments');
        const data = await response.json();
        
        const container = document.getElementById('assignments-container');
        container.innerHTML = '';
        
        if (data.assignments && data.assignments.length > 0) {
            data.assignments.forEach(assignment => {
                const assignmentCard = document.createElement('div');
                assignmentCard.className = 'assignment-card';
                assignmentCard.innerHTML = `
                    <h3>${assignment.title}</h3>
                    <p>${assignment.description}</p>
                    <p><strong>Questions:</strong> ${assignment.question_count}</p>
                    <p><strong>Time Limit:</strong> ${assignment.time_limit_minutes || 'No limit'} minutes</p>
                    <button onclick="loadAssignment('${assignment.id}')" class="start-btn">Start Assignment</button>
                `;
                container.appendChild(assignmentCard);
            });
        } else {
            container.innerHTML = '<p>No assignments available.</p>';
        }
    } catch (error) {
        console.error('Error loading assignments:', error);
        document.getElementById('assignments-container').innerHTML = '<p>Error loading assignments.</p>';
    }
}

async function loadAssignment(assignmentId) {
    try {
        const response = await fetch(`/assignments/${assignmentId}`);
        const assignment = await response.json();
        
        currentAssignment = assignment;
        
        document.getElementById('assignment-title').textContent = assignment.title;
        document.getElementById('assignment-description').textContent = assignment.description;
        document.getElementById('time-limit').textContent = 
            assignment.time_limit_minutes ? `Time Limit: ${assignment.time_limit_minutes} minutes` : 'No time limit';
        
        const questionsContainer = document.getElementById('questions-container');
        questionsContainer.innerHTML = '';
        
        assignment.questions.forEach((question, index) => {
            const questionDiv = document.createElement('div');
            questionDiv.className = 'question';
            questionDiv.innerHTML = `
                <h4>Question ${index + 1}</h4>
                <p>${question.text}</p>
                <div class="options">
                    ${question.options.map((option, optionIndex) => `
                        <label class="option">
                            <input type="radio" name="question-${question.id}" value="${optionIndex}" required>
                            <span>${option}</span>
                        </label>
                    `).join('')}
                </div>
            `;
            questionsContainer.appendChild(questionDiv);
        });
        
        showSection('assignment-detail');
    } catch (error) {
        console.error('Error loading assignment:', error);
        alert('Error loading assignment');
    }
}

async function submitAssignment(event) {
    event.preventDefault();
    
    const studentId = document.getElementById('student-id').value;
    if (!studentId) {
        alert('Please enter your Student ID');
        return;
    }
    
    const answers = [];
    currentAssignment.questions.forEach(question => {
        const selectedOption = document.querySelector(`input[name="question-${question.id}"]:checked`);
        if (selectedOption) {
            answers.push({
                question_id: question.id,
                selected_option: parseInt(selectedOption.value)
            });
        }
    });
    
    if (answers.length !== currentAssignment.questions.length) {
        alert('Please answer all questions');
        return;
    }
    
    try {
        const response = await fetch(`/assignments/${currentAssignment.id}/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                student_id: studentId,
                answers: answers
            })
        });
        
        const result = await response.json();
        
        if (response.ok) {
            showResults(result);
        } else {
            alert('Error submitting assignment: ' + result.error);
        }
    } catch (error) {
        console.error('Error submitting assignment:', error);
        alert('Error submitting assignment');
    }
}

function showResults(result) {
    const resultContent = document.getElementById('result-content');
    resultContent.innerHTML = `
        <div class="result-card">
            <h3>Assignment Submitted Successfully!</h3>
            <p><strong>Score:</strong> ${result.score.toFixed(1)}%</p>
            <p><strong>Submission ID:</strong> ${result.submission_id}</p>
            <p><strong>Submitted at:</strong> ${new Date(result.submitted_at).toLocaleString()}</p>
        </div>
    `;
    showSection('result-section');
}

function showSection(sectionId) {
    const sections = ['assignments-list', 'assignment-detail', 'result-section'];
    sections.forEach(section => {
        document.getElementById(section).style.display = section === sectionId ? 'block' : 'none';
    });
}

function showAssignmentsList() {
    showSection('assignments-list');
    document.getElementById('assignment-form').reset();
}

document.getElementById('assignment-form').addEventListener('submit', submitAssignment);

window.addEventListener('load', loadAssignments);