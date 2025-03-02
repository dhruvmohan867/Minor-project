import streamlit as st
import time
from styles import inject_custom_css
from header import show_header
from form_sections import *
from backend import process_resume_data
import base64

def main():
    st.set_page_config(page_title="AI Resume Builder", page_icon="🤖", layout="wide")
    st.markdown(inject_custom_css(), unsafe_allow_html=True)
    
    show_header()
    
    with st.form(key='resume_form'):
        personal_info_section()
        education_section()
        work_experience_section()
        skills_section()
        projects_section()
        
        # Submit button INSIDE the form
        submitted = st.form_submit_button("✨ Generate AI Resume")
    
    # Handle submission OUTSIDE the form
    if submitted:
        with st.spinner("Generating your resume..."):
            # Collect form data
            form_data = {
                "personal_info": {
                    "name": st.session_state.name,
                    "email": st.session_state.email,
                    "phone": st.session_state.phone
                },
                "education": {
                    "degree": st.session_state.education,
                    "years": st.session_state.education_years
                },
                "experience": {
                    "job_title": st.session_state.job_title,
                    "company": st.session_state.company,
                    "description": st.session_state.experience
                },
                "skills": [skill.strip() for skill in st.session_state.skills.split(',')],
                "projects": st.session_state.projects
            }

            # Process data through backend
            result = process_resume_data(form_data)
            
            if result['success']:
                st.success("✅ Resume generated successfully!")
                
                # Show download button
                with open(result['pdf_path'], "rb") as f:
                    pdf_bytes = f.read()
                
                st.download_button(
                    label="Download Resume",
                    data=pdf_bytes,
                    file_name=result['filename'],
                    mime="application/pdf"
                )
            else:
                st.error(f"⚠️ Error: {result['error']}")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; color: #666;">
        <p>🚀 Powered by AI Resume Builder | Backend Integration in Progress</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()