def inject_custom_css():
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    * {{
        font-family: 'Poppins', sans-serif;
        color: #2d3436;
    }}
    
    /* Main container styling */
    .stApp {{
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }}
    
    /* Header styling */
    .header {{
        animation: slideIn 1s ease-out;
        text-align: center;
        background: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin: 2rem auto;
        max-width: 800px;
    }}
    
    .header h1 {{
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }}
    
    /* Form elements styling */
    .stTextInput>div>div>input, 
    .stTextArea>div>textarea,
    .stSelectbox>div>div>div {{
        border-radius: 12px!important;
        border: 1px solid #dee2e6!important;
        background: #ffffff!important;
        padding: 0.8rem!important;
        font-size: 1rem!important;
    }}
    
    .stTextInput>div>div>input:focus, 
    .stTextArea>div>textarea:focus {{
        box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.25)!important;
        border-color: #4299e1!important;
    }}
    
    /* Section styling */
    .section {{
        background: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem auto;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid #f1f3f5;
    }}
    
    .section h2 {{
        color: #2c3e50;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #4299e1;
        padding-bottom: 0.5rem;
    }}
    
    /* Button styling */
    .stButton>button {{
        border-radius: 12px!important;
        padding: 0.8rem 2.5rem!important;
        background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%)!important;
        font-size: 1.1rem!important;
        letter-spacing: 0.5px;
    }}
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {{
        .section {{
            padding: 1.5rem;
            margin: 1rem 0;
        }}
        
        .header {{
            padding: 1.5rem;
            margin: 1rem 0;
        }}
        
        .stTextInput>div>div>input, 
        .stTextArea>div>textarea {{
            font-size: 0.95rem!important;
        }}
    }}
    
    /* Animations */
    @keyframes slideIn {{
        from {{ transform: translateY(-20px); opacity: 0; }}
        to {{ transform: translateY(0); opacity: 1; }}
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateX(-15px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    </style>
    """