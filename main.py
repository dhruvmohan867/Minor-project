import streamlit as st
import time
from styles import inject_custom_css
from header import show_header
from form_sections import *

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
        
        # Submit button
        if st.form_submit_button("✨ Generate AI Resume"):
            with st.spinner("Generating your resume..."):
                time.sleep(2)
                st.error("⚠️ Backend integration in progress! Our AI is working hard to finish this feature.")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; color: #666;">
        <p>🚀 Powered by AI Resume Builder | Backend Integration in Progress</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()