from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import uuid

@dataclass
class Question:
    id: str
    text: str
    options: List[str]
    correct_answer: int
    
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())

@dataclass
class Assignment:
    id: str
    title: str
    description: str
    questions: List[Question]
    time_limit_minutes: Optional[int] = None
    created_at: datetime = None
    
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = datetime.now()

@dataclass
class Answer:
    question_id: str
    selected_option: int

@dataclass
class Submission:
    id: str
    assignment_id: str
    student_id: str
    answers: List[Answer]
    submitted_at: datetime = None
    score: Optional[float] = None
    
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.submitted_at:
            self.submitted_at = datetime.now()