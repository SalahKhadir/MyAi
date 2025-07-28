"""
Chat functionality and message management
"""
import streamlit as st
import time

class ChatManager:
    def __init__(self):
        self._initialize_session_state()
    
    def _initialize_session_state(self):
        """Initialize chat history in session state"""
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "is_generating" not in st.session_state:
            st.session_state.is_generating = False
        if "pending_response" not in st.session_state:
            st.session_state.pending_response = False
    
    def add_message(self, role, content):
        """Add a message to chat history"""
        st.session_state.messages.append({
            "role": role,
            "content": content
        })
    
    def get_messages(self):
        """Get all messages from chat history"""
        return st.session_state.messages
    
    def clear_history(self):
        """Clear all chat history"""
        st.session_state.messages = []
    
    def display_messages(self):
        """Display all chat messages using native Streamlit chat"""
        # Show welcome screen if no messages
        if not st.session_state.messages:
            return self._display_welcome_screen()
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        # Show typing indicator if AI is generating response
        if st.session_state.get("is_generating", False):
            with st.chat_message("assistant"):
                st.write("*Thinking...*")
        
        return None
    
    def _display_welcome_screen(self):
        """Display welcome screen with title and suggestions"""
        st.markdown("""
        <div style="text-align: center; padding: 3rem 0 2rem 0;">
            <h1 style="color: white; font-size: 2.5rem; margin-bottom: 1rem;">
                Salah's AI Assistant
            </h1>
            <p style="color: #888; font-size: 1.1rem; margin-bottom: 2rem;">
                Ask me anything about Salah Khadir's experience, skills, and projects
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h3 style="color: white; margin-bottom: 1rem;">Recommended questions:</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Create suggestion buttons in columns
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Tell me about Salah's projects", key="suggestion_1", use_container_width=True):
                return "Tell me about Salah's projects"
            if st.button("What skills does Salah have?", key="suggestion_2", use_container_width=True):
                return "What skills does Salah have?"
        
        with col2:
            if st.button("Describe Salah's academic background", key="suggestion_3", use_container_width=True):
                return "Describe Salah's academic background"
            if st.button("What are Salah's main interests?", key="suggestion_4", use_container_width=True):
                return "What are Salah's main interests?"
        
        return None
    
    def _display_user_message(self, content):
        """Display user message with styling"""
        st.markdown(f"""
        <div class="user-message message-appear">
            <strong>You:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
    
    def _display_assistant_message(self, content):
        """Display assistant message with styling"""
        st.markdown(f"""
        <div class="assistant-message message-appear">
            <strong>LilSall:</strong><br>
            <div id="assistant-response">{content}</div>
        </div>
        """, unsafe_allow_html=True)

    def set_generating_state(self, is_generating):
        """Set the generating state for typing indicator"""
        st.session_state.is_generating = is_generating
    
    def is_generating(self):
        """Check if AI is currently generating a response"""
        return st.session_state.get("is_generating", False)
