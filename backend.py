import os
import uuid
import io
import tempfile
import sqlite3
from datetime import datetime
from fpdf import FPDF
from PyPDF2 import PdfReader
import streamlit as st
# Initialize database connection
def init_db():
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS resumes
                 (id TEXT PRIMARY KEY,
                  name TEXT,
                  email TEXT,
                  phone TEXT,
                  created_at TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_to_database(resume_data):
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    resume_id = str(uuid.uuid4())
    c.execute("INSERT INTO resumes VALUES (?,?,?,?,?)",
              (resume_id,
               resume_data['personal_info']['name'],
               resume_data['personal_info']['email'],
               resume_data['personal_info']['phone'],
               datetime.now()))
    conn.commit()
    conn.close()
    return resume_id

RESUME_STORAGE = tempfile.gettempdir()

class ResumeGenerator:
    def __init__(self, form_data):
        self.data = form_data
        self.pdf = FPDF()
        self.filename = f"resume_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        self._setup_fonts()

    def _setup_fonts(self):
        self.pdf.add_font('Arial', '', 'arial.ttf', uni=True)
        self.pdf.add_font('Arial', 'B', 'arialbd.ttf', uni=True)

    def _create_header(self):
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(200, 10, txt=self.data['personal_info']['name'], ln=1, align='C')
        self.pdf.set_font("Arial", '', 12)
        self.pdf.cell(200, 10, txt=f"{self.data['personal_info']['email']} | {self.data['personal_info']['phone']}", ln=1, align='C')

    def _create_section(self, title, content):
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(200, 10, txt=title, ln=1)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, txt=content)
        self.pdf.ln(5)

    def generate_pdf(self):
        try:
            self.pdf.add_page()
            self._create_header()
            
            sections = [
                ("Education", f"{self.data['education']['degree']}\n{self.data['education']['years']}"),
                ("Work Experience", f"{self.data['experience']['job_title']} at {self.data['experience']['company']}\n{self.data['experience']['description']}"),
                ("Skills", ", ".join(self.data['skills']) if isinstance(self.data['skills'], list) else self.data['skills']),
                ("Projects", self.data['projects'])
            ]
            
            for title, content in sections:
                if content.strip():
                    self._create_section(title, content)
            
            filepath = os.path.join(RESUME_STORAGE, self.filename)
            self.pdf.output(filepath)
            return filepath
        except Exception as e:
            raise RuntimeError(f"PDF generation failed: {str(e)}")

def parse_pdf(file):
    """Extract text from PDF files"""
    try:
        pdf = PdfReader(io.BytesIO(file.read()))
        return "\n".join(page.extract_text() for page in pdf.pages)
    except Exception as e:
        raise ValueError(f"PDF parsing error: {str(e)}")

def extract_info_from_pdf(text):
    """Extract structured data from PDF text"""
    info = {
        'name': '',
        'email': '',
        'phone': '',
        'education': [],
        'experience': []
    }
    
    # Simple extraction patterns (can be enhanced with regex/NLP)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    for i, line in enumerate(lines):
        if '@' in line and '.' in line:
            info['email'] = line
        elif any(c.isdigit() for c in line) and len(line) >= 10:
            info['phone'] = line
        elif 'education' in line.lower():
            info['education'].extend(lines[i+1:i+4])
        elif 'experience' in line.lower():
            info['experience'].extend(lines[i+1:i+6])
    
    info['name'] = lines[0] if lines else ''
    return info

def process_resume_data(form_data):
    try:
        # Validate required fields
        required = {'name', 'email', 'phone'}
        missing = required - form_data['personal_info'].keys()
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        # Handle PDF input if present
        if 'document' in st.session_state and st.session_state.document:
            if st.session_state.document.type == "application/pdf":
                pdf_text = parse_pdf(st.session_state.document)
                pdf_info = extract_info_from_pdf(pdf_text)
                
                # Merge PDF data with form data
                form_data['personal_info'] = {**pdf_info, **form_data['personal_info']}
                form_data['education'] = {**form_data['education'], 'degree': '\n'.join(pdf_info['education'])}
                form_data['experience'] = {**form_data['experience'], 'description': '\n'.join(pdf_info['experience'])}

        # Generate PDF
        generator = ResumeGenerator(form_data)
        pdf_path = generator.generate_pdf()
        
        # Save to database
        save_to_database(form_data)
        
        return {
            "success": True,
            "pdf_path": pdf_path,
            "filename": generator.filename
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Initialize database on first run
init_db()