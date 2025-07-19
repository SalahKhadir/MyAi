"""
AI Assistant Portfolio - Main Application
Clean, modular Streamlit application with ChatGPT-like interface
"""

import streamlit as st
from styles import get_custom_css
from ai_client import AIClient
from chat_manager import ChatManager
from ui_components import render_sidebar, render_header

# Page Configuration
st.set_page_config(
    page_title="AI Assistant Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize components
ai_client = AIClient()
chat_manager = ChatManager()

# Render sidebar and check for navigation
selected_page = render_sidebar()

# Handle navigation
if selected_page:
    if selected_page == "chat":
        # Stay on current chat page
        pass
    elif selected_page == "internships":
        st.info("Internships page - Coming soon!")
    elif selected_page == "projects":
        st.info("Projects page - Coming soon!")
    elif selected_page == "about":
        st.info("About Me page - Coming soon!")
    elif selected_page == "education":
        st.info("Education page - Coming soon!")

# Main content area
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Render header
render_header()

# Display chat messages
chat_manager.display_messages()

st.markdown('</div>', unsafe_allow_html=True)

# Input area (fixed at bottom)
col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_area(
        "",
        placeholder="Type your message here...",
        key="user_input",
        height=40,
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send", key="send_button")

# Process user input
if send_button and user_input.strip():
    if ai_client.is_configured():
        # Add user message
        chat_manager.add_message("user", user_input)
        
        try:
            # Generate AI response
            with st.spinner("Generating response..."):
                response = ai_client.generate_response(user_input)
                chat_manager.add_message("assistant", response)
            
            # Clear input and refresh
            st.rerun()
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.error("AI client not configured. Please check your API key.")

elif send_button and not user_input.strip():
    st.warning("Please enter a message.")
