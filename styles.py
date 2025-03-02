def inject_custom_css():
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    * {{
        font-family: 'Poppins', sans-serif;
    }}
    
    /* Main container styling */
    .stApp {{
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }}
    
    /* Header animation */
    @keyframes slideIn {{
        from {{ transform: translateY(-50px); opacity: 0; }}
        to {{ transform: translateY(0); opacity: 1; }}
    }}
    
    .header {{
        animation: slideIn 1s ease-out;
        text-align: center;
        color: #2c3e50;
        padding: 2rem;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }}
    
    /* Form elements styling */
    .stTextInput>div>div>input, 
    .stTextArea>div>textarea,
    .stSelectbox>div>div>div {{
        border-radius: 10px!important;
        transition: all 0.3s ease!important;
    }}
    
    .stTextInput>div>div>input:focus, 
    .stTextArea>div>textarea:focus {{
        box-shadow: 0 0 8px rgba(63, 81, 181, 0.3)!important;
    }}
    
    /* Section animations */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateX(-20px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    
    .section {{
        animation: fadeIn 0.8s ease-out;
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }}
    
    /* Button styling */
    .stButton>button {{
        border-radius: 25px!important;
        padding: 0.5rem 2rem!important;
        background: linear-gradient(45deg, #4b6cb7 0%, #182848 100%)!important;
        color: white!important;
        transition: all 0.3s ease!important;
        border: none!important;
    }}
    
    .stButton>button:hover {{
        transform: scale(1.05);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2)!important;
    }}
    
    @media (max-width: 768px) {{
        .section {{
            padding: 1rem;
        }}
        .header h1 {{
            font-size: 1.8rem!important;
        }}
    }}
    </style>
    """