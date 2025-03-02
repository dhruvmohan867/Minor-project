import streamlit as st

def personal_info_section():
    with st.container():
        st.markdown("<div class='section'><h2>🧑💼 Personal Information</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.text_input("Full Name", key="name")
            st.text_input("Email Address", key="email")
            st.text_input("Phone Number", key="phone")
        with col2:
            st.write("Profile Photo")
            st.file_uploader("Upload photo", type=["jpg", "png"], label_visibility="collapsed", key="photo")
        st.markdown("</div>", unsafe_allow_html=True)

def education_section():
    with st.container():
        st.markdown("<div class='section'><h2>🎓 Education</h2>", unsafe_allow_html=True)
        st.text_area("Degree and University", key="education")
        st.text_input("Years Attended", key="education_years")
        st.markdown("</div>", unsafe_allow_html=True)


def work_experience_section():
     with st.container():
            st.markdown("<div class='section'><h2>💼 Work Experience</h2>", unsafe_allow_html=True)
            job_title = st.text_input("Job Title")
            company = st.text_input("Company Name")
            experience = st.text_area("Job Description")
            st.markdown("</div>", unsafe_allow_html=True)

def skills_section():
       with st.container():
            st.markdown("<div class='section'><h2>🛠 Skills</h2>", unsafe_allow_html=True)
            skills = st.text_area("List your skills (comma separated)")
            st.markdown("</div>", unsafe_allow_html=True)

def projects_section():
       with st.container():
            st.markdown("<div class='section'><h2>🏆 Projects</h2>", unsafe_allow_html=True)
            projects = st.text_area("Describe your projects")
            st.markdown("</div>", unsafe_allow_html=True)
          
# Create similar functions for work_experience_section(), skills_section(), projects_section()