# styles.py (updated)
def inject_custom_css():
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    * {{
        font-family: 'Poppins', sans-serif;
        color: #2d3436;
    }}
    
    .stApp {{
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }}
    
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
    }}
    
    .section {{
        background: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem auto;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid #f1f3f5;
    }}
    
    .section h2 {{
        color: #2563eb;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #2563eb;
        padding-bottom: 0.5rem;
    }}
    
    .stButton>button {{
        background: #2563eb!important;
        color: white!important;
        border-radius: 8px!important;
        padding: 0.8rem 2rem!important;
    }}
    
    .quality-report {{
        padding: 1.5rem;
        background: #f0f9ff;
        border-radius: 8px;
        margin: 1rem 0;
        border: 2px solid #2563eb;
    }}
    
    .ai-suggestion {{
        padding: 1rem;
        background: #f5f3ff;
        border-radius: 8px;
        margin: 1rem 0;
    }}
    
    .footer {{
        text-align: center;
        margin-top: 2rem;
        color: #4b5563;
        padding: 1rem;
    }}
    
    @media (max-width: 768px) {{
        .section {{
            padding: 1.5rem;
            margin: 1rem 0;
        }}
    }}
    
    @keyframes slideIn {{
        from {{ transform: translateY(-20px); opacity: 0; }}
        to {{ transform: translateY(0); opacity: 1; }}
    }}
    </style>
    """