"""
Salah Khadir's AI Assistant - Main Application
Clean, modular Streamlit application with ChatGPT-like interface
"""

import streamlit as st
from styles import get_custom_css
from ai_client import AIClient
from chat_manager import ChatManager
from ui_components import render_sidebar, render_header
from internships_page import render_internships_page
from education_page import render_education_page
from about_page import render_about_page
from projects_page import render_projects_page

# Page Configuration
st.set_page_config(
    page_title="Salah's AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize components
ai_client = AIClient(use_tuned_model=False)  # Set to True when tuned model is ready
chat_manager = ChatManager()

# Render sidebar and check for navigation
selected_page = render_sidebar()

# Initialize current page state if it doesn't exist
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'chat'

# Update current page only if a navigation was actually selected
if selected_page:
    st.session_state.current_page = selected_page

# Initialize show_chat flag
show_chat = True

# Handle navigation based on current page state
current_page = st.session_state.current_page

if current_page == "chat":
    # Stay on current chat page - show chat interface
    show_chat = True
elif current_page == "internships":
    render_internships_page()
    show_chat = False
elif current_page == "projects":
    render_projects_page()
    show_chat = False
elif current_page == "about":
    render_about_page()
    show_chat = False
elif current_page == "education":
    render_education_page()
    show_chat = False

# Only show chat interface if not on another page
if show_chat:
    # Main content area - Simple chat interface
    # Display chat messages and get suggestion if clicked
    suggested_question = chat_manager.display_messages()

    # Handle suggestion clicks
    if suggested_question:
        if ai_client.is_configured():
            # Add user message
            chat_manager.add_message("user", suggested_question)
            
            try:
                # Generate AI response
                response = ai_client.generate_response(suggested_question)
                chat_manager.add_message("assistant", response)
                st.rerun()
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.error("AI client not configured. Please check your API key.")

    # User input - simple chat input
    if prompt := st.chat_input("Type your message..."):
        if ai_client.is_configured():
            # Add user message
            chat_manager.add_message("user", prompt)
            
            try:
                # Generate AI response
                response = ai_client.generate_response(prompt)
                chat_manager.add_message("assistant", response)
                st.rerun()
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.error("AI client not configured. Please check your API key.")
