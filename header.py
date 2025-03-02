import streamlit as st

def show_header():
    st.markdown("""
    <div class='header'>
        <h1>🤖 AI Resume Builder</h1>
        <p>Create your professional resume in minutes</p>
    </div>
    """, unsafe_allow_html=True)