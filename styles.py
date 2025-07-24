"""
CSS styles for Salah Khadir's AI Assistant - Improved Dark Theme
"""

def get_custom_css():
    return """
    <style>
        /* Import Google Fonts for better readability */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Styles - Improved Dark Theme */
        .stApp {
            background-color: #1a1a1a !important;
            color: #FAFAFA !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        .main {
            background-color: #1a1a1a !important;
            color: #FAFAFA !important;
        }
        
        /* Ensure main content area has proper background */
        .main .block-container {
            background-color: #1a1a1a !important;
            padding-top: 2rem;
        }
        
        /* Hide deploy button */
        .stDeployButton {
            display: none !important;
        }
        
        /* Hide header */
        header[data-testid="stHeader"] {
            height: 0 !important;
            display: none !important;
        }
        
        /* Sidebar - Fixed height, no scrolling */
        .stSidebar {
            background-color: #262730 !important;
            height: 100vh !important;
            overflow: hidden !important;
        }
        
        .stSidebar > div {
            background-color: #262730 !important;
            height: 100vh !important;
            overflow: hidden !important;
            padding-bottom: 2rem !important;
            padding-top: 0 !important;
        }
        
        .stSidebar .block-container {
            padding-top: 0 !important;
            padding-bottom: 1rem !important;
            max-height: 100vh !important;
            overflow: hidden !important;
        }
        
        /* Remove top margin from sidebar content */
        .stSidebar [data-testid="stVerticalBlock"] {
            padding-top: 0 !important;
            margin-top: 0 !important;
            overflow: hidden !important;
        }
        
        /* Remove top spacing from first element in sidebar */
        .stSidebar > div > div > div:first-child {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        
        /* Remove any default margins from markdown elements in sidebar */
        .stSidebar .stMarkdown {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        .stSidebar .stMarkdown:first-child {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Remove default spacing from h2 elements in sidebar */
        .stSidebar h2 {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Hide scrollbars completely */
        .stSidebar::-webkit-scrollbar {
            display: none !important;
        }
        
        .stSidebar > div::-webkit-scrollbar {
            display: none !important;
        }
        
        /* All text in sidebar should be white */
        .stSidebar * {
            color: #FAFAFA !important;
        }
        
        /* Navigation buttons with better contrast - professional blue theme */
        .stButton > button {
            background-color: #60a5fa !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            margin-bottom: 0.5rem !important;
            width: 100% !important;
            padding: 0.75rem !important;
            font-weight: 500 !important;
            font-size: 14px !important;
            letter-spacing: 0.025em !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
        }
        
        .stButton > button:hover {
            background-color: #3b82f6 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 12px rgba(96, 165, 250, 0.3) !important;
        }
        
        .stButton > button:active {
            transform: translateY(0) !important;
            box-shadow: 0 2px 4px rgba(96, 165, 250, 0.2) !important;
        }
        
        /* Social links with professional styling - full width */
        .stSidebar a {
            color: #FAFAFA !important;
            text-decoration: none !important;
            display: block !important;
            padding: 0.75rem !important;
            margin: 0.25rem 0 !important;
            background: linear-gradient(135deg, #3a3a3a, #4a4a4a) !important;
            border: 1px solid #555 !important;
            border-radius: 8px !important;
            text-align: center !important;
            font-weight: 500 !important;
            font-size: 14px !important;
            letter-spacing: 0.025em !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
            width: 100% !important;
            box-sizing: border-box !important;
        }
        
        /* GitHub specific styling */
        .stSidebar a[href*="github"] {
            background: linear-gradient(135deg, #24292e, #333) !important;
            border: 1px solid #444 !important;
        }
        
        .stSidebar a[href*="github"]:hover {
            background: linear-gradient(135deg, #333, #404040) !important;
            border-color: #60a5fa !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 8px rgba(96, 165, 250, 0.2) !important;
        }
        
        /* LinkedIn specific styling */
        .stSidebar a[href*="linkedin"] {
            background: linear-gradient(135deg, #0077b5, #005885) !important;
            border: 1px solid #004a6b !important;
        }
        
        .stSidebar a[href*="linkedin"]:hover {
            background: linear-gradient(135deg, #005885, #004a6b) !important;
            border-color: #60a5fa !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 8px rgba(96, 165, 250, 0.2) !important;
        }
        
        /* General hover for other links */
        .stSidebar a:hover {
            background: linear-gradient(135deg, #4a4a4a, #5a5a5a) !important;
            border-color: #60a5fa !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 8px rgba(96, 165, 250, 0.2) !important;
        }
        
        /* Chat messages - ensure proper styling */
        .stChatMessage {
            background-color: #262730 !important;
            border: 1px solid #3a3a3a !important;
            border-radius: 12px !important;
            margin: 1rem 0 !important;
            padding: 1rem !important;
        }
        
        .stChatMessage [data-testid="chatAvatarIcon-user"] {
            background-color: #4CAF50 !important;
        }
        
        .stChatMessage [data-testid="chatAvatarIcon-assistant"] {
            background-color: #2196F3 !important;
        }
        
        /* Ensure all text is visible - but preserve custom colors */
        .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6 {
            color: #FAFAFA !important;
        }
        
        /* Allow custom inline styles to override - preserve blue colors */
        .stMarkdown h1[style*="color"],
        .stMarkdown h2[style*="color"], 
        .stMarkdown h3[style*="color"],
        .stMarkdown p[style*="color"],
        .stMarkdown div[style*="color"] {
            color: inherit !important;
        }
        
        /* Preserve custom background gradients and colors */
        .stMarkdown div[style*="background"] {
            background: inherit !important;
        }
        
        /* Simple Chat Input Styling - Clean and functional */
        .stChatInput {
            margin-top: 2rem !important;
        }
        
        /* Ensure all chat input elements are interactive */
        .stChatInput, .stChatInput *, .stChatInput *:before, .stChatInput *:after {
            pointer-events: auto !important;
        }
        
        /* Style the input text to be visible */
        .stChatInput input,
        .stChatInput textarea {
            color: #FAFAFA !important;
            background-color: transparent !important;
        }
        
        .stChatInput input::placeholder,
        .stChatInput textarea::placeholder {
            color: #888 !important;
        }
        
        /* Fix any black backgrounds */
        div[data-testid="stVerticalBlock"] {
            background-color: transparent !important;
        }
        
        /* Ensure proper contrast for all elements - blue theme */
        .stSelectbox, .stTextInput, .stTextArea {
            background-color: #262730 !important;
            color: #FAFAFA !important;
            border: 1px solid #60a5fa !important;
        }
    </style>
    """
