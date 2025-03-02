import os
import uuid
from fpdf import FPDF
import tempfile
from datetime import datetime
import sqlite3
# Temporary storage for resumes (Replace with database in production)
def init_db():
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS resumes
                 (id TEXT PRIMARY KEY,
                  name TEXT,
                  email TEXT,
                  created_at TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_to_database(resume_data):
    conn = sqlite3.connect('resumes.db')
    c = conn.cursor()
    resume_id = str(uuid.uuid4())
    c.execute("INSERT INTO resumes VALUES (?,?,?,?)",
              (resume_id,
               resume_data['personal_info']['name'],
               resume_data['personal_info']['email'],
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
        self.pdf.add_page()
        self._create_header()
        
        self._create_section("Education", 
                           f"{self.data['education']['degree']}\n"
                           f"{self.data['education']['years']}")
        
        self._create_section("Work Experience", 
                           f"{self.data['experience']['job_title']} at {self.data['experience']['company']}\n"
                           f"{self.data['experience']['description']}")
        
        self._create_section("Skills", ", ".join(self.data['skills']))
        self._create_section("Projects", self.data['projects'])
        
        filepath = os.path.join(RESUME_STORAGE, self.filename)
        self.pdf.output(filepath)
        return filepath

def process_resume_data(form_data):
    try:
        # Data validation
        required_fields = ['name', 'email', 'phone']
        for field in required_fields:
            if not form_data['personal_info'].get(field):
                raise ValueError(f"Missing required field: {field}")

        # Create PDF
        generator = ResumeGenerator(form_data)
        pdf_path = generator.generate_pdf()
        
        # Return generated file info
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