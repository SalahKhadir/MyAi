"""
CSS styles for Salah Khadir's AI Assistant - Simple Dark Theme
"""

def get_custom_css():
    return """
    <style>
        /* Global Styles - Simple Dark Theme */
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        
        .main {
            background-color: #0e1117;
            color: white;
        }
        
        /* Hide deploy button */
        .stDeployButton {
            display: none;
        }
        
        /* Hide header */
        header[data-testid="stHeader"] {
            height: 0;
        }
        
        /* Sidebar - Dark theme */
        .css-1d391kg {
            background-color: #1a202c;
        }
        
        .stSidebar > div {
            background-color: #1a202c;
        }
        
        /* Navigation buttons */
        .stButton > button[kind="secondary"] {
            background-color: #3182ce;
            color: white;
            border: none;
            border-radius: 6px;
            margin-bottom: 0.5rem;
            width: 100%;
            padding: 0.75rem;
        }
        
        .stButton > button[kind="secondary"]:hover {
            background-color: #2c5aa0;
        }
        
        /* Social links */
        a {
            color: white;
            text-decoration: none;
            display: block;
            padding: 0.5rem;
            margin: 0.25rem 0;
            background: #2d3748;
            border-radius: 4px;
            text-align: center;
        }
        
        a:hover {
            background-color: #4a5568;
        }
        
        /* Chat messages - let Streamlit handle styling */
        .stChatMessage {
            margin: 1rem 0;
        }
        
        /* Sidebar text colors */
        .stSidebar h1 {
            color: white;
        }
        
        .stSidebar h2 {
            color: white;
        }
        
        .stSidebar h3 {
            color: white;
        }
        
        .stSidebar h4 {
            color: white;
        }
        
        .stSidebar p {
            color: white;
        }
    </style>
    """
