"""
About Me Page - Professional overview of Salah Khadir's background, skills, and passion
"""
import streamlit as st

def render_about_page():
    """Render the professional about me page"""
    
    # Ensure we stay on the about page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'about'
    st.session_state.current_page = 'about'
    
    # Page header with professional introduction
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
        ">About Me</h1>
        <p style="
            color: #94a3b8;
            font-size: 1.2rem;
            margin: 0;
            font-weight: 300;
        ">Computer Engineering & Networks Student | Future AI & Data Science Specialist</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main profile section
    col1, col2 = st.columns([2, 3], gap="large")
    
    with col1:
        # Profile card
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.7));
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid rgba(96, 165, 250, 0.2);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
            text-align: center;
            margin-bottom: 2rem;
        ">
            <div style="
                width: 120px;
                height: 120px;
                border-radius: 50%;
                background: linear-gradient(135deg, #60a5fa, #3b82f6);
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 1.5rem auto;
                box-shadow: 0 4px 20px rgba(96, 165, 250, 0.4);
            ">
                <span style="
                    color: white;
                    font-size: 3rem;
                    font-weight: 700;
                ">SK</span>
            </div>
            <h2 style="color: #e2e8f0; font-size: 1.5rem; margin-bottom: 0.5rem;">Salah Khadir</h2>
            <p style="color: #94a3b8; font-size: 1rem; margin: 0;">Computer Engineering & Networks Student</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact information
        st.markdown("""
        <div style="
            background: rgba(96, 165, 250, 0.1);
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #60a5fa;
            margin-bottom: 2rem;
        ">
            <h4 style="color: #60a5fa; margin-bottom: 1rem; font-size: 1.2rem; font-weight: 600;">
                Contact Information
            </h4>
            <div style="color: #e2e8f0; line-height: 1.8;">
                <p style="margin: 0.5rem 0;">
                    <strong style="color: #60a5fa;">📧 Email:</strong><br>
                    salaho.khadir@gmail.com
                </p>
                <p style="margin: 0.5rem 0;">
                    <strong style="color: #60a5fa;">📍 Location:</strong><br>
                    Morocco
                </p>
                <p style="margin: 0.5rem 0;">
                    <strong style="color: #60a5fa;">💼 LinkedIn:</strong><br>
                    linkedin.com/in/salah-khadir
                </p>
                <p style="margin: 0.5rem 0;">
                    <strong style="color: #60a5fa;">🔗 GitHub:</strong><br>
                    github.com/SalahKhadir
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Personal introduction
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.7));
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid rgba(96, 165, 250, 0.2);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
            margin-bottom: 2rem;
        ">
            <h3 style="color: #60a5fa; font-size: 1.4rem; margin-bottom: 1rem; font-weight: 600;">
                Hello! I'm Salah Khadir
            </h3>
            <p style="color: #e2e8f0; font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
                I'm Salah Khadir, a 23-year-old passionate Computer Engineering & Networks student born in Errachidia, Morocco. 
                Currently in my 3rd year at EMSI, I have a deep fascination for Artificial Intelligence and full-stack development. 
                I'm preparing to specialize in AI & Data Science in my 4th year, with an expected graduation in 2027.
            </p>
            <p style="color: #e2e8f0; font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
                My portfolio includes diverse projects like EcoTrace (digital waste management system), SkillSync (modern recruitment platform), 
                and a comprehensive Pharmacy Management System. During my professional internships, I developed enterprise solutions 
                including a water resource management system and an advanced AI chatbot using Google's Gemini 2.0 Flash for real estate services.
            </p>
            <p style="color: #e2e8f0; font-size: 1.05rem; line-height: 1.7; margin: 0;">
                I believe in continuous learning and have earned multiple certifications in Python, AI development, and software engineering. 
                My goal is to leverage cutting-edge AI technologies and modern development practices to solve complex problems 
                and contribute to digital transformation across various industries in Morocco and beyond.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Skills & Competencies section (focused on favorites and best skills)
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0 2rem 0;">
        <h2 style="
            color: #60a5fa;
            text-align: center;
            font-size: 2.2rem;
            font-weight: 600;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #60a5fa, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        ">Skills & Competencies</h2>
        <p style="
            color: #94a3b8;
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 3rem;
            font-weight: 300;
        ">My favorite technologies and areas where I excel the most</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Favorite and best skills - more focused selection
    favorite_skills = {
        "AI & Machine Learning": {
            "skills": ["Google Gemini 2.0", "AI Model Integration", "FastAPI for AI", "Document Analysis", "AI Domain Specialization"],
            "icon": "AI",
            "color": "#ef4444"
        },
        "Frontend Development": {
            "skills": ["React 19", "React 18", "Vite", "Material-UI", "Tailwind CSS"],
            "icon": "WEB",
            "color": "#60a5fa"
        },
        "Backend Development": {
            "skills": ["FastAPI", "Django 4.2", "Laravel", "PHP", "Django REST Framework"],
            "icon": "API",
            "color": "#10b981"
        },
        "Database & Tools": {
            "skills": ["MySQL", "PostgreSQL", "JWT Auth", "Java Swing", "iText PDF"],
            "icon": "DB",
            "color": "#f59e0b"
        }
    }
    
    # Create elegant grid layout
    for i in range(0, len(favorite_skills), 2):
        col1, col2 = st.columns(2, gap="large")
        
        # Left column
        category_items = list(favorite_skills.items())
        if i < len(category_items):
            category, data = category_items[i]
            with col1:
                render_favorite_skill_card(category, data)
        
        # Right column
        if i + 1 < len(category_items):
            category, data = category_items[i + 1]
            with col2:
                render_favorite_skill_card(category, data)
    
    # What I'm passionate about
    st.markdown("""
    <h3 style="
        color: #60a5fa; 
        font-size: 1.8rem; 
        font-weight: 600; 
        text-align: center; 
        margin: 3rem 0 2rem 0;
    ">What Drives Me</h3>
    """, unsafe_allow_html=True)
    
    passion_items = [
        {
            "icon": "",
            "title": "Artificial Intelligence",
            "description": "Exploring the potential of AI to transform industries and solve complex real-world problems through innovative applications."
        },
        {
            "icon": "",
            "title": "Full-Stack Development",
            "description": "Building end-to-end solutions that combine beautiful user interfaces with robust backend systems and databases."
        },
        {
            "icon": "",
            "title": "Continuous Learning",
            "description": "Staying updated with emerging technologies and best practices to deliver modern, efficient, and scalable solutions."
        },
        {
            "icon": "",
            "title": "Innovation & Impact",
            "description": "Creating technology solutions that make a meaningful difference in people's lives and contribute to digital transformation."
        }
    ]
    
    for i in range(0, len(passion_items), 2):
        cols = st.columns(2, gap="large")
        for j, col in enumerate(cols):
            if i + j < len(passion_items):
                item = passion_items[i + j]
                with col:
                    render_passion_card(item["icon"], item["title"], item["description"])

def render_favorite_skill_card(category, data):
    """Render individual favorite skill card with elegant styling matching education page"""
    
    skills = data["skills"]
    icon = data["icon"]
    color = data["color"]
    
    # Create a container with proper styling
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.7));
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border: 1px solid {color}40;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    ">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <span style="font-size: 1.5rem; margin-right: 0.75rem;">{icon}</span>
            <h4 style="color: {color}; margin: 0; font-size: 1.1rem; font-weight: 600;">{category}</h4>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a clean grid for skills
    cols = st.columns(2)  # Using 2 columns instead of 3 for better spacing
    for i, skill in enumerate(skills):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="
                background: rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.15);
                padding: 0.5rem 0.8rem;
                border-radius: 8px;
                margin: 0.2rem 0;
                border-left: 3px solid {color};
                color: #e2e8f0;
                font-size: 0.85rem;
                text-align: center;
            ">
                {skill}
            </div>
            """, unsafe_allow_html=True)

def render_passion_card(icon, title, description):
    """Render a passion/interest card"""
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.7));
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(96, 165, 250, 0.2);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        margin-bottom: 1rem;
        text-align: center;
    ">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">{icon}</div>
        <h4 style="color: #60a5fa; font-size: 1.1rem; margin-bottom: 0.8rem; font-weight: 600;">
            {title}
        </h4>
        <p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.5; margin: 0;">
            {description}
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_about_page()
