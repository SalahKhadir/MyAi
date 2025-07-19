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
            ("Chat with Mimir", "chat"),
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
        
        # GitHub button
        if st.button("GitHub", key="github_link", use_container_width=True):
            st.markdown("""
            <script>
                window.open('https://github.com/SalahKhadir', '_blank');
            </script>
            """, unsafe_allow_html=True)
        
        # LinkedIn button  
        if st.button("LinkedIn", key="linkedin_link", use_container_width=True):
            st.markdown("""
            <script>
                window.open('https://linkedin.com/in/your-profile', '_blank');
            </script>
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
