"""
UI Components for the AI Assistant
"""
import streamlit as st

def render_sidebar():
    """Render the navigation sidebar"""
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 0.25rem 0 1rem 0;">
            <h2 style="color: white; margin-bottom: 1.5rem; margin-top: 0; padding-top: 0;">Navigation</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation buttons
        nav_buttons = [
            ("Chat with LilSall", "chat"),
            ("Internships", "internships"),
            ("Projects", "projects"),
            ("About Me", "about"),
            ("Education", "education")
        ]
        
        selected_page = None
        
        for button_text, page_key in nav_buttons:
            if st.button(button_text, key=f"nav_{page_key}", use_container_width=True):
                selected_page = page_key
        
        # Social links section
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
            <h4 style="color: white; margin-bottom: 1rem;">Connect with Me</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # GitHub link
        st.markdown("""
        <div style="text-align: center; margin-bottom: 0.5rem;">
            <a href="https://github.com/SalahKhadir" target="_blank">
                GitHub
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # LinkedIn link
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1rem;">
            <a href="https://www.linkedin.com/in/salah-khadir" target="_blank">
                LinkedIn
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        return selected_page

def render_header():
    """Render simple chat interface - no extra sections"""
    # Just display chat messages - no header needed
    pass

def render_input_area():
    """Render the input area at the bottom"""
    st.markdown("""
    <div class="input-container">
        <div class="input-wrapper">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_area(
            "",
            placeholder="Type your message here...",
            key="user_input",
            height=50,
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("Send", key="send_button", use_container_width=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    return user_input, send_button
