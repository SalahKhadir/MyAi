"""
Internships Page - Detailed showcase of Salah's professional internship experiences
"""
import streamlit as st

def render_internships_page():
    """Render the comprehensive internships page"""
    
    # Page header
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="color: white; margin-bottom: 0.5rem;">Professional Internships</h1>
        <p style="color: #888; font-size: 1.1rem;">Real-world experience in AI development and full-stack applications</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create two columns for the internships
    col1, col2 = st.columns(2)
    
    with col1:
        render_cgi_internship()
    
    with col2:
        render_abhgzr_internship()
    
    # Skills gained section
    st.markdown("<br><br>", unsafe_allow_html=True)
    render_skills_gained()
    
    # Professional growth section
    render_professional_growth()

def render_cgi_internship():
    """Render CGI internship details"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a202c, #2d3748); padding: 2rem; border-radius: 12px; margin-bottom: 2rem; border: 1px solid #4a5568;">
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <h2 style="color: #60a5fa; margin-bottom: 0.5rem;">🏢 CGI Internship</h2>
            <h3 style="color: white; margin-bottom: 0.5rem;">AI Intern</h3>
            <p style="color: #9ca3af; font-style: italic;">Multinational IT Consulting Company</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Role details
    st.markdown("### 🎯 **Role Overview**")
    st.markdown("""
    **Position:** AI Intern  
    **Company:** CGI - Major multinational IT consulting company  
    **Focus:** AI Solutions Development & Enterprise Applications
    """)
    
    # Technologies used
    st.markdown("### 💻 **Technologies & Tools**")
    tech_cols = st.columns(2)
    with tech_cols[0]:
        st.markdown("""
        **Programming Languages:**
        - 🐍 Python
        - 📜 JavaScript
        """)
    with tech_cols[1]:
        st.markdown("""
        **Frameworks & Tools:**
        - ⚛️ React
        - 🚀 FastAPI
        - 🗄️ MySQL
        """)
    
    # Key achievements
    st.markdown("### 🏆 **Key Achievements**")
    st.markdown("""
    - ✅ Developed AI solutions and applications for enterprise clients
    - ✅ Gained experience in enterprise-level AI development workflows
    - ✅ Worked with modern web technologies in professional environment
    - ✅ Collaborated with multinational development teams
    - ✅ Applied AI/ML concepts to real-world business problems
    """)
    
    # Skills developed
    st.markdown("### 📈 **Skills Developed**")
    st.markdown("""
    - **AI Development:** Enterprise-level AI application development
    - **Full-stack Development:** React frontend with FastAPI backend
    - **Database Management:** MySQL integration and optimization
    - **Professional Collaboration:** Working in enterprise development teams
    - **Problem Solving:** Real-world AI solution implementation
    """)

def render_abhgzr_internship():
    """Render ABHGZR internship details"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a202c, #2d3748); padding: 2rem; border-radius: 12px; margin-bottom: 2rem; border: 1px solid #4a5568;">
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <h2 style="color: #10b981; margin-bottom: 0.5rem;">🚔 ABHGZR Internship</h2>
            <h3 style="color: white; margin-bottom: 0.5rem;">Full-Stack Developer</h3>
            <p style="color: #9ca3af; font-style: italic;">Government Sector Development</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project details
    st.markdown("### 🎯 **Project Overview**")
    st.markdown("""
    **Project:** Application de gestion des patrouilles de la police et de stock des infractions  
    **Translation:** Police Patrol Management System with Traffic Violation Tracking  
    **Sector:** Government/Law Enforcement  
    **Scope:** Complete management system for police operations
    """)
    
    # Technologies used
    st.markdown("### 💻 **Technologies & Architecture**")
    tech_cols = st.columns(2)
    with tech_cols[0]:
        st.markdown("""
        **Frontend:**
        - ⚛️ React.js
        - 🎨 Modern UI/UX Design
        - 📱 Responsive Design
        """)
    with tech_cols[1]:
        st.markdown("""
        **Backend:**
        - 🐘 PHP Laravel
        - 🗄️ Database Management
        - 🔐 Security Implementation
        """)
    
    # System features
    st.markdown("### 🔧 **System Features**")
    st.markdown("""
    - 👮 **Patrol Management:** Track and manage police patrol schedules and routes
    - 📋 **Violation Tracking:** Comprehensive system for recording traffic infractions
    - 📊 **Reporting System:** Generate detailed reports for law enforcement analysis
    - 👥 **User Management:** Role-based access for different levels of personnel
    - 🗃️ **Data Management:** Efficient storage and retrieval of enforcement data
    """)
    
    # Impact and learning
    st.markdown("### 🏆 **Impact & Learning**")
    st.markdown("""
    - ✅ Developed a complete government sector application
    - ✅ Learned to work with sensitive law enforcement data
    - ✅ Implemented security best practices for government systems
    - ✅ Gained experience in React.js and Laravel full-stack development
    - ✅ Understanding of real-world system requirements and constraints
    """)

def render_skills_gained():
    """Render comprehensive skills gained section"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #7c3aed, #a855f7); padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
        <h2 style="color: white; text-align: center; margin-bottom: 2rem;">🚀 Professional Skills Developed</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Create skill categories
    skill_cols = st.columns(3)
    
    with skill_cols[0]:
        st.markdown("""
        ### 🤖 **AI & Development**
        - Enterprise AI solution development
        - FastAPI for AI model deployment
        - Python for AI/ML applications
        - Integration of AI in business workflows
        """)
    
    with skill_cols[1]:
        st.markdown("""
        ### 🌐 **Full-Stack Expertise**
        - React.js frontend development
        - Laravel backend development
        - MySQL database design and management
        - RESTful API development
        """)
    
    with skill_cols[2]:
        st.markdown("""
        ### 💼 **Professional Skills**
        - Working in multinational environments
        - Government sector development
        - Security-focused development
        - Team collaboration and communication
        """)

def render_professional_growth():
    """Render professional growth and impact section"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a, #1e293b); padding: 2rem; border-radius: 12px; border: 1px solid #334155;">
        <h2 style="color: white; text-align: center; margin-bottom: 2rem;">📈 Professional Growth & Impact</h2>
    </div>
    """, unsafe_allow_html=True)
    
    growth_cols = st.columns(2)
    
    with growth_cols[0]:
        st.markdown("""
        ### 🎯 **Career Development**
        
        These internships provided invaluable experience in:
        
        - **Enterprise Development:** Working with large-scale, production-ready applications
        - **Industry Standards:** Learning professional development practices and code standards
        - **Real-world Problem Solving:** Addressing actual business and government needs
        - **Technology Integration:** Combining multiple technologies to create comprehensive solutions
        - **Professional Communication:** Working with stakeholders and team members
        """)
    
    with growth_cols[1]:
        st.markdown("""
        ### 💡 **Technical Evolution**
        
        **From CGI Internship:**
        - Advanced AI development skills
        - Enterprise-level application architecture
        - Modern JavaScript and Python frameworks
        
        **From ABHGZR Internship:**
        - Government sector development experience
        - Full-stack application development
        - Security-conscious development practices
        
        **Combined Impact:**
        - Versatile technology stack expertise
        - Adaptability to different industry requirements
        - Strong foundation for AI/Data Science career goals
        """)
    
    # Call to action
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #059669, #10b981); padding: 1.5rem; border-radius: 8px; text-align: center;">
        <h3 style="color: white; margin-bottom: 1rem;">💼 Ready for New Opportunities</h3>
        <p style="color: white; margin-bottom: 0;">
            With proven experience in AI development and full-stack applications, 
            Salah is ready to take on new challenges in multinational companies 
            and continue growing in the AI/Data Science field.
        </p>
    </div>
    """, unsafe_allow_html=True)
