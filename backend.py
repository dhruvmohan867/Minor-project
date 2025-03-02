# backend.py (updated)
import os
import uuid
import io
import tempfile
import sqlite3
import openai
from datetime import datetime
from fpdf import FPDF
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize database
def init_db():
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS resumes
                 (id TEXT PRIMARY KEY,
                  name TEXT,
                  email TEXT,
                  phone TEXT,
                  score INTEGER,
                  created_at TIMESTAMP)''')
    conn.commit()
    conn.close()

def analyze_resume_quality(resume_data):
    # Calculate quality score
    score = 0
    feedback = []
    
    # Check for essential components
    essential_fields = ['name', 'email', 'phone']
    for field in essential_fields:
        if resume_data['personal_info'].get(field):
            score += 1
        else:
            feedback.append(f"Missing {field.replace('_', ' ')}")
    
    # Experience analysis
    exp_length = len(resume_data['experience']['description'])
    if exp_length > 50:
        score += 2
    elif exp_length > 20:
        score += 1
    else:
        feedback.append("Add more details to work experience")
    
    # Skills analysis
    if len(resume_data['skills']) >= 5:
        score += 2
    elif len(resume_data['skills']) >= 3:
        score += 1
    else:
        feedback.append("Add more skills")
    
    # Education validation
    if resume_data['education']['degree']:
        score += 2
    
    # Cap score at 10
    score = min(score, 10)
    
    # Generate feedback
    if not feedback:
        feedback.append("Good structure! Consider adding more details for higher score")
    
    return {'score': score, 'feedback': " | ".join(feedback)}

def generate_ai_content(form_data):
    prompt = f"""Generate professional resume suggestions based on:
    Name: {form_data.get('name', '')}
    Education: {form_data.get('education', '')}
    Experience: {form_data.get('experience', '')}
    Skills: {form_data.get('skills', '')}
    Projects: {form_data.get('projects', '')}
    
    Suggest improvements for:"""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional career coach"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    return response.choices[0].message['content']

# Keep other backend functions same as previous version with font fixes