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
        if "typing_animation" not in st.session_state:
            st.session_state.typing_animation = False
    
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
        """Display all chat messages"""
        for message in st.session_state.messages:
            if message["role"] == "user":
                self._display_user_message(message["content"])
            else:
                self._display_assistant_message(message["content"])
    
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

    def display_typing_animation(self):
        """Display typing animation for AI response"""
        typing_placeholder = st.empty()
        
        # Show thinking animation
        typing_placeholder.markdown(f"""
        <div class="assistant-message typing-indicator">
            <strong>LilSall:</strong><br>
            <span style="color: #888;">💭 Thinking...</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Short delay for effect
        time.sleep(0.8)
        typing_placeholder.empty()

    def add_message_with_animation(self, role, content):
        """Add message with typing animation for assistant"""
        if role == "assistant":
            self.display_typing_animation()
        
        self.add_message(role, content)
