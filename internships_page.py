"""
Internships Page - Professional showcase of internship experiences with slide navigation
"""
import streamlit as st

def render_internships_page():
    """Render the professional internships page with slide navigation"""
    
    # Ensure we stay on the internships page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'internships'
    st.session_state.current_page = 'internships'
    
    # Page header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <h1 style="
            color: #60a5fa;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, #60a5fa, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        ">Professional Internships</h1>
        <p style="
            color: #94a3b8;
            font-size: 1.2rem;
            margin: 0;
            font-weight: 300;
        ">Real-world experience in enterprise development and AI solutions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Internship data (chronological order: ABHGZR first, then CGI)
    internships = [
        {
            "id": "abhgzr",
            "company": "Agence du Bassin Hydraulique du Guir-Ziz-Rhéris (ABHGZR)",
            "role": "Full Stack Intern",
            "period": "April 2024",
            "duration": "1 month",
            "sector": "Water Resource Management",
            "location": "Errachidia, Morocco",
            "description": "Developed a comprehensive web application for water resource management and tracking at Morocco's hydraulic basin agency. The project focused on digitalizing water management operations, creating tracking systems for water resources, and building management tools for the Guir-Ziz-Rhéris hydraulic basin administration.",
            "technologies": ["Laravel", "PHP", "MySQL", "HTML5", "CSS3", "Bootstrap"],
            "responsibilities": [
                "Developed web application for water resource management and tracking",
                "Created comprehensive tracking systems for water basin resources",
                "Built management interfaces for hydraulic basin administration",
                "Implemented data management solutions for water resource operations",
                "Designed user-friendly interfaces for government agency staff",
                "Collaborated with water resource management professionals"
            ],
            "achievements": [
                "Successfully delivered complete water resource management system",
                "Digitized water basin tracking and monitoring operations",
                "Created efficient data management solutions for government agency",
                "Built modern web interfaces replacing manual tracking processes",
                "Enhanced understanding of government sector development needs"
            ],
            "skills_developed": [
                "Laravel Framework Development",
                "PHP Backend Programming",
                "MySQL Database Design",
                "HTML5 & CSS3 Frontend",
                "Bootstrap Framework",
                "Government Sector Web Development",
                "Water Resource Management Systems",
                "Public Administration Technology"
            ]
        },
        {
            "id": "cgi",
            "company": "CGI Promoteur Immobilier",
            "role": "AI Intern",
            "period": "July - August 2025",
            "duration": "1 month",
            "sector": "Real Estate Development",
            "location": "Rabat, Morocco",
            "description": "Successfully developed an advanced digital chatbot for CGI Promoteur Immobilier, Morocco's leading real estate company since 1960. Built a full-stack AI application with Google Gemini 2.0 Flash integration, featuring PDF document analysis, ChatGPT-style interface with persistent chat history, and dual access modes for public and authenticated users. The project enhanced customer service and property consultation processes for luxury real estate.",
            "technologies": ["FastAPI", "React 19", "Vite", "Google Gemini 2.0", "MySQL", "JWT Authentication"],
            "responsibilities": [
                "Developed full-stack AI chatbot using Google Gemini 2.0 Flash integration",
                "Built React 19 frontend with ChatGPT-style interface and sidebar navigation",
                "Implemented FastAPI backend for AI model communication and user management",
                "Created PDF document analysis system with intelligent content extraction",
                "Designed persistent chat history system with session management",
                "Developed dual access modes for public and authenticated users",
                "Collaborated with team of 2 on enterprise AI solution development"
            ],
            "achievements": [
                "Successfully delivered production-ready AI chatbot for enterprise client",
                "Implemented advanced features: PDF analysis, chat history, user authentication",
                "Built modern full-stack architecture with React 19 and FastAPI",
                "Created specialized AI responses for real estate domain expertise",
                "Contributed to digital transformation of Morocco's leading real estate company",
                "Gained expertise in cutting-edge AI technologies and enterprise development"
            ],
            "skills_developed": [
                "Google Gemini 2.0 Flash AI Integration",
                "FastAPI Framework Development",
                "React 19 with Modern Hooks",
                "Vite Build Tool and Development",
                "JWT Authentication and User Management",
                "PDF Document Processing and Analysis",
                "Enterprise AI Application Architecture",
                "Real Estate Domain AI Specialization"
            ]
        }
    ]
    
    # Initialize session state for slide navigation
    if 'current_internship' not in st.session_state:
        st.session_state.current_internship = 0
    
    # Navigation controls
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← Previous", key="prev_internship", disabled=st.session_state.current_internship == 0):
            st.session_state.current_internship -= 1
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem;">
            <span style="color: #60a5fa; font-weight: 600; font-size: 1.1rem;">
                {st.session_state.current_internship + 1} of {len(internships)}
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("Next →", key="next_internship", disabled=st.session_state.current_internship == len(internships) - 1):
            st.session_state.current_internship += 1
            st.rerun()
    
    # Display current internship
    current_internship = internships[st.session_state.current_internship]
    render_internship_slide(current_internship)
    
    # Navigation dots
    render_navigation_dots(len(internships), st.session_state.current_internship)

def render_internship_slide(internship):
    """Render individual internship slide with professional layout"""
    
    # Main internship card
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.7));
        padding: 2.5rem;
        border-radius: 16px;
        margin: 2rem 0;
        border: 1px solid rgba(96, 165, 250, 0.2);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    ">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #60a5fa; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">
                {internship['company']}
            </h2>
            <h3 style="color: #e2e8f0; font-size: 1.3rem; margin-bottom: 0.5rem;">
                {internship['role']}
            </h3>
            <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
                <span style="color: #94a3b8; font-size: 0.95rem;">
                    <strong>Period:</strong> {internship['period']}
                </span>
                <span style="color: #94a3b8; font-size: 0.95rem;">
                    <strong>Duration:</strong> {internship['duration']}
                </span>
                <span style="color: #94a3b8; font-size: 0.95rem;">
                    <strong>Sector:</strong> {internship['sector']}
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Description
    st.markdown(f"""
    <div style="
        background: rgba(96, 165, 250, 0.1);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border-left: 4px solid #60a5fa;
    ">
        <p style="color: #e2e8f0; font-size: 1.05rem; line-height: 1.6; margin: 0;">
            {internship['description']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Content sections
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Technologies section
        st.markdown("""
        <h4 style="color: #60a5fa; margin-bottom: 1rem; font-size: 1.2rem; font-weight: 600;">
            Technologies & Tools
        </h4>
        """, unsafe_allow_html=True)
        
        for tech in internship['technologies']:
            st.markdown(f"""
            <div style="
                background: rgba(16, 185, 129, 0.1);
                padding: 0.4rem 0.8rem;
                border-radius: 6px;
                margin: 0.3rem 0;
                border-left: 3px solid #10b981;
                color: #e2e8f0;
                font-size: 0.9rem;
            ">
                {tech}
            </div>
            """, unsafe_allow_html=True)
        
        # Skills developed section
        st.markdown("""
        <h4 style="color: #60a5fa; margin: 2rem 0 1rem 0; font-size: 1.2rem; font-weight: 600;">
            Skills Developed
        </h4>
        """, unsafe_allow_html=True)
        
        for skill in internship['skills_developed']:
            st.markdown(f"""
            <div style="
                background: rgba(139, 92, 246, 0.1);
                padding: 0.4rem 0.8rem;
                border-radius: 6px;
                margin: 0.3rem 0;
                border-left: 3px solid #8b5cf6;
                color: #e2e8f0;
                font-size: 0.9rem;
            ">
                {skill}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Responsibilities section
        st.markdown("""
        <h4 style="color: #60a5fa; margin-bottom: 1rem; font-size: 1.2rem; font-weight: 600;">
            Key Responsibilities
        </h4>
        """, unsafe_allow_html=True)
        
        for responsibility in internship['responsibilities']:
            st.markdown(f"""
            <div style="
                background: rgba(59, 130, 246, 0.1);
                padding: 0.6rem 1rem;
                border-radius: 8px;
                margin: 0.5rem 0;
                border-left: 3px solid #3b82f6;
                color: #e2e8f0;
                font-size: 0.9rem;
                line-height: 1.4;
            ">
                {responsibility}
            </div>
            """, unsafe_allow_html=True)
        
        # Achievements section
        st.markdown("""
        <h4 style="color: #60a5fa; margin: 2rem 0 1rem 0; font-size: 1.2rem; font-weight: 600;">
            Key Achievements
        </h4>
        """, unsafe_allow_html=True)
        
        for achievement in internship['achievements']:
            st.markdown(f"""
            <div style="
                background: rgba(245, 158, 11, 0.1);
                padding: 0.6rem 1rem;
                border-radius: 8px;
                margin: 0.5rem 0;
                border-left: 3px solid #f59e0b;
                color: #e2e8f0;
                font-size: 0.9rem;
                line-height: 1.4;
            ">
                {achievement}
            </div>
            """, unsafe_allow_html=True)

def render_navigation_dots(total_slides, current_slide):
    """Render navigation dots for slide navigation"""
    
    # Create a centered column layout for the dots
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        dots_container = ""
        for i in range(total_slides):
            if i == current_slide:
                dots_container += "🔵 "  # Active dot
            else:
                dots_container += "⚫ "  # Inactive dot
        
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0; font-size: 1.2rem;">
            {dots_container}
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_internships_page()