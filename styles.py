"""
CSS styles for Salah Khadir's AI Assistant
"""

def get_custom_css():
    return """
    <style>
        /* Global Styles */
        .stApp {
            background-color: #0e1117;
        }
        
        .main {
            background-color: #0e1117;
            color: white;
        }
        
        /* Chat Container */
        .chat-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 1rem;
        }
        
        /* Message Styles */
        .user-message {
            background-color: #2d3748;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            margin-left: 2rem;
            border-left: 3px solid #3182ce;
        }
        
        .assistant-message {
            background-color: #1a202c;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            margin-right: 2rem;
            border-left: 3px solid #38a169;
        }
        
        /* Input Area */
        .input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #1a202c;
            padding: 1rem;
            border-top: 1px solid #2d3748;
            z-index: 1000;
        }
        
        .input-wrapper {
            max-width: 600px;
            margin: 0 auto;
            display: flex;
            gap: 0.5rem;
            align-items: flex-end;
        }
        
        /* Textarea Styling */
        .stTextArea > div > div > textarea {
            background-color: #2d3748 !important;
            color: white !important;
            border: 1px solid #4a5568 !important;
            border-radius: 8px !important;
            min-height: 40px !important;
            max-height: 40px !important;
            resize: none !important;
            font-size: 14px !important;
        }
        
        /* Button Styling */
        .stButton > button {
            background-color: #3182ce !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
            font-weight: 600 !important;
            height: 40px !important;
            width: 100% !important;
            font-size: 14px !important;
        }
        
        .stButton > button:hover {
            background-color: #2c5aa0 !important;
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Sidebar */
        .stSidebar {
            background-color: #1a202c;
        }
        
        /* Hide sidebar scrollbar */
        .stSidebar > div {
            scrollbar-width: none; /* Firefox */
            -ms-overflow-style: none; /* Internet Explorer 10+ */
        }
        
        .stSidebar > div::-webkit-scrollbar {
            display: none; /* WebKit */
        }
        
        .stSidebar .css-1d391kg {
            scrollbar-width: none;
            -ms-overflow-style: none;
        }
        
        .stSidebar .css-1d391kg::-webkit-scrollbar {
            display: none;
        }
        
        /* Sidebar Navigation Buttons */
        .stSidebar .stButton > button {
            background-color: transparent !important;
            color: #e2e8f0 !important;
            border: 2px solid #4a5568 !important;
            border-radius: 8px !important;
            padding: 0.75rem 1rem !important;
            font-weight: 500 !important;
            margin-bottom: 0.5rem !important;
            transition: all 0.3s ease !important;
            text-align: left !important;
            width: 100% !important;
        }
        
        .stSidebar .stButton > button:hover {
            background-color: #2d3748 !important;
            border-color: #718096 !important;
            color: white !important;
        }
        
        /* GitHub button styling */
        .stSidebar .stButton > button[key="github_link"] {
            border-color: #f6ad55 !important;
            color: #f6ad55 !important;
        }
        
        .stSidebar .stButton > button[key="github_link"]:hover {
            background-color: #f6ad55 !important;
            color: #1a202c !important;
        }
        
        /* LinkedIn button styling */
        .stSidebar .stButton > button[key="linkedin_link"] {
            border-color: #4299e1 !important;
            color: #4299e1 !important;
        }
        
        .stSidebar .stButton > button[key="linkedin_link"]:hover {
            background-color: #4299e1 !important;
            color: #1a202c !important;
        }
        
        /* Clear chat button */
        .stSidebar .stButton > button[key="clear_chat"] {
            border-color: #e53e3e !important;
            color: #e53e3e !important;
        }
        
        .stSidebar .stButton > button[key="clear_chat"]:hover {
            background-color: #e53e3e !important;
            color: white !important;
        }
        
        /* Text and Headers */
        h1, h2, h3, h4, h5, h6 {
            color: white !important;
        }
        
        .stMarkdown {
            color: white;
        }
        
        /* Social Links Hover Effects */
        a[href*="github.com"]:hover {
            background: linear-gradient(135deg, #333, #555) !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        
        a[href*="linkedin.com"]:hover {
            background: linear-gradient(135deg, #005885, #0077b5) !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        
        /* Typing Animation Effects */
        .typing-indicator {
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }
        
        .message-appear {
            animation: slideInUp 0.3s ease-out;
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Padding for fixed input */
        .main .block-container {
            padding-bottom: 80px;
        }
    </style>
    """
