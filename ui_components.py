"""
UI Components for the AI Assistant
"""
import streamlit as st

def render_sidebar():
    """Render the navigation sidebar"""
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0 1rem 0;">
            <h2 style="color: white; margin-bottom: 2rem;">Navigation</h2>
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
            <a href="https://github.com/SalahKhadir" target="_blank" style="
                display: inline-block;
                width: 80%;
                padding: 0.5rem 1rem;
                background: linear-gradient(135deg, #24292e, #333);
                color: white;
                text-decoration: none;
                border-radius: 6px;
                border: 1px solid #444;
                text-align: center;
                transition: all 0.3s ease;
            ">
                🐙 GitHub
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # LinkedIn link
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1rem;">
            <a href="https://www.linkedin.com/in/salah-khadir" target="_blank" style="
                display: inline-block;
                width: 80%;
                padding: 0.5rem 1rem;
                background: linear-gradient(135deg, #0077b5, #005885);
                color: white;
                text-decoration: none;
                border-radius: 6px;
                border: 1px solid #004a6b;
                text-align: center;
                transition: all 0.3s ease;
            ">
                💼 LinkedIn
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        return selected_page

def render_header():
    """Render the main header"""
    st.title("AI Assistant Portfolio")
    st.markdown("---")

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
