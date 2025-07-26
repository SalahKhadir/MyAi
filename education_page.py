"""
Education Page for Salah Khadir's AI Assistant
Interactive timeline with expandable education details
"""

import streamlit as st

def render_education_page():
    """Render the education page with interactive timeline"""
    
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
        ">Educational Journey</h1>
        <p style="
            color: #a8a8a8;
            font-size: 1.2rem;
            margin: 0;
            font-weight: 300;
        ">From High School to Engineering Excellence</p>
        <p style="
            color: #60a5fa;
            font-size: 1rem;
            margin-top: 0.5rem;
            font-weight: 500;
        ">Currently pursuing Software Engineering at EMSI Rabat</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Education timeline data
    education_data = [
        {
            "period": "2024 - 2027",
            "institution": "École Marocaine Des Sciences De L'Ingénieur (EMSI)",
            "degree": "3ème année en Ingénierie Informatique et Réseaux",
            "location": "Rabat, Morocco",
            "status": "Currently Studying",
            "gpa": "N/A",
            "description": "Advanced engineering program focusing on software development, network infrastructure, artificial intelligence, and cloud computing technologies.",
            "key_courses": [
                "Développement & langages: C++, Python, Java, .NET, Angular, React",
                "Ingénierie logicielle: Méthodes agiles, DevOps, qualité logiciel, UML",
                "Systèmes & cloud: Unix, Windows, virtualisation, cloud computing",
                "Réseaux & cybersécurité: TCP/IP, protocoles, sécurité, forensic",
                "Intelligence artificielle: Machine learning, data science, IA appliquée",
                "Base de données: SQL, NoSQL, Oracle, MS SQL Server",
                "Gestion de projet & IT: PMP, ITIL, outils de pilotage",
                "Soft & Digital Skills: Communication, Entrepreneuriat, Employabilité"
            ],
            "projects": [
                "Développement d'un chatbot Digital",
                "EcoTrace: An environmental tracking application", 
                "SkillSync: gestion des recrutements",
                "Pharmacy Management System"
            ],
            "achievements": [
                "Successfully progressing through advanced engineering curriculum",
                "Completed multiple industry-relevant projects",
                "Developing expertise in AI and cloud technologies"
            ]
        },
        {
            "period": "2022 - 2024",
            "institution": "Institut Spécialisé de Technologie Appliquée Mohamed El Fassi",
            "degree": "Diplôme de Technicien Spécialisé en Développement Digital - Web Full Stack",
            "location": "Errachidia, Morocco",
            "status": "Graduated",
            "gpa": "Mention: Très Bien",
            "description": "Comprehensive technical program covering full-stack web development, from front-end frameworks to back-end systems and cloud deployment.",
            "key_courses": [
                "Programming & Algorithms: Algorithm design, OOP, JavaScript",
                "Web Development: HTML/CSS, React/Angular, Server-side scripting",
                "Back-End & Databases: SQL/NoSQL, RESTful APIs, Microservices",
                "Security & Infrastructure: Information security, Docker/AWS",
                "Agile Practices: Scrum methodologies, Sprint planning",
                "Languages: Technical Arabic, French, English, Spanish",
                "Entrepreneurship: Business modeling, MVP development"
            ],
            "projects": [
                "Application web gestion d'une agence de voyage",
                "Application de gestion des patrouilles de la police et de stock des infractions",
                "Full-stack development projects with modern frameworks",
                "Cloud-native application deployment"
            ],
            "achievements": [
                "Graduated with 'Très Bien' (Highest Distinction)",
                "Mastered full-stack development lifecycle",
                "Completed industry internships and client projects",
                "Developed entrepreneurial mindset for tech solutions"
            ]
        },
        {
            "period": "2018 - 2019",
            "institution": "Lycée Sijilmassa",
            "degree": "Baccalauréat en Sciences Physiques et Chimiques (Option Français)",
            "location": "Errachidia, Morocco",
            "status": "Graduated",
            "gpa": "Mention: Bien",
            "description": "Comprehensive high school diploma with advanced specialization in Physical Sciences and Chemistry, emphasizing quantitative modeling, experimental design, and analytical problem-solving across integrated scientific disciplines.",
            "key_courses": [
                "Physics - Wave Phenomena: Mechanical waves, electromagnetic propagation, amplitude modulation, interference patterns",
                "Physics - Electric Circuits: RC/RL circuits, RLC oscillations, resonance analysis, impedance calculations",
                "Physics - Mechanics & Motion: Newton's laws, projectile trajectories, rotational dynamics, harmonic oscillators",
                "Physics - Nuclear & Atomic: Mass-energy equivalence, nuclear stability, quantum behavior in atomic models",
                "Chemistry - Chemical Dynamics: Reaction kinetics, radioactive decay, acid-base equilibria, electrochemistry",
                "Chemistry - Organic Chemistry: Esterification, hydrolysis, reaction equilibrium control and optimization",
                "Mathematics - Analysis & Calculus: Limits, continuity, derivatives, function analysis, differential equations",
                "Mathematics - Probability & Statistics: Discrete probability, combinatorics, statistical reasoning, distributions",
                "Mathematics - Advanced Algebra: Complex numbers (polar/Cartesian), logarithmic/exponential functions",
                "Mathematics - Geometry & Vectors: 3D space geometry, scalar/cross products, vector applications",
                "French Language & Literature: Advanced composition, scientific French terminology",
                "Experimental Methods: Laboratory design, data interpretation, quantitative modeling"
            ],
            "projects": [
                "Wave interference experiments with quantitative analysis using differential equations",
                "RLC circuit oscillation analysis with complex number applications",
                "Chemical kinetics laboratory: Rate law derivation and decay constant calculations",
                "Projectile motion optimization using calculus-based trajectory analysis",
                "Electrochemical cell design with thermodynamic and kinetic considerations",
                "Statistical analysis of experimental data using probability distributions",
                "French scientific literature review and technical documentation"
            ],
            "achievements": [
                "Graduated with 'Bien' (Good Distinction)",
                "Mastered integrated scientific problem-solving across physics, chemistry, and mathematics",
                "Developed strong analytical skills in calculus, probability theory, and experimental design",
                "Achieved proficiency in quantitative modeling of physical and chemical phenomena",
                "Demonstrated cross-cutting competencies in experimental-analytical bridge building",
                "Trilingual scientific communication (Arabic/French/English)"
            ]
        }
    ]
    
    # Timeline container
    st.markdown("""
    <div style="max-width: 900px; margin: 0 auto;">
    """, unsafe_allow_html=True)
    
    # Render each education entry
    for i, edu in enumerate(education_data):
        render_education_entry(edu, i)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Skills summary
    render_skills_summary()

def render_education_entry(edu, index):
    """Render individual education timeline entry"""
    
    # Create unique key for expander
    expander_key = f"edu_expander_{index}"
    
    # Timeline entry with expander
    with st.expander(
        f"📚 {edu['institution']} ({edu['period']})",
        expanded=False
    ):
        # Main info section
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div style="margin-bottom: 1.5rem;">
                <h3 style="color: #60a5fa; margin-bottom: 0.5rem; font-size: 1.4rem;">
                    {edu['degree']}
                </h3>
                <p style="color: #a8a8a8; margin-bottom: 0.5rem; font-size: 1rem;">
                    📍 {edu['location']} | Status: <strong style="color: #4ade80;">{edu['status']}</strong>
                </p>
                <p style="color: #d1d5db; font-size: 1rem; line-height: 1.6;">
                    {edu['description']}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #1e293b, #334155);
                padding: 1.5rem;
                border-radius: 12px;
                border-left: 4px solid #60a5fa;
                margin-bottom: 1rem;
            ">
                <h4 style="color: #60a5fa; margin-bottom: 0.5rem;">Academic Performance</h4>
                <p style="color: #e2e8f0; font-size: 1.1rem; font-weight: 600;">
                    GPA: {edu['gpa']}
                </p>
                <p style="color: #94a3b8; font-size: 0.9rem;">
                    Period: {edu['period']}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Detailed sections
        tab1, tab2, tab3 = st.tabs(["📖 Key Courses", "🚀 Projects", "🏆 Achievements"])
        
        with tab1:
            st.markdown("**Core Curriculum:**")
            for course in edu['key_courses']:
                st.markdown(f"• {course}")
        
        with tab2:
            st.markdown("**Notable Projects:**")
            for project in edu['projects']:
                st.markdown(f"• {project}")
        
        with tab3:
            st.markdown("**Academic Achievements:**")
            for achievement in edu['achievements']:
                st.markdown(f"• {achievement}")

def render_skills_summary():
    """Render skills acquired through education with elegant design"""
    
    st.markdown("""
    <div style="margin-top: 4rem; margin-bottom: 2rem;">
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
        ">Technical expertise acquired through academic journey and hands-on experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills categories with improved structure
    skills_categories = {
        "Programming Languages": {
            "skills": ["C++", "Python", "Java", "JavaScript", ".NET", "SQL", "Typescript", "PHP"],
            "icon": "💻",
            "color": "#60a5fa"
        },
        "Web Technologies": {
            "skills": ["HTML/CSS", "React", "Angular", "Vue.js", "Node.js", "Express", "RESTful APIs", "Laravel", "Django", "FastAPI", "Spring Boot", "Symfony", "Bootstrap", "Tailwind CSS"],
            "icon": "🌐",
            "color": "#10b981"
        },
        "Database Systems": {
            "skills": ["SQL", "NoSQL", "Oracle", "MS SQL Server", "MongoDB"],
            "icon": "🗄️",
            "color": "#f59e0b"
        },
        "Cloud & DevOps": {
            "skills": ["Docker", "CI/CD", "Unix/Linux", "Windows", "Virtualisation"],
            "icon": "☁️",
            "color": "#8b5cf6"
        },
        "AI & Data Science": {
            "skills": ["Machine Learning", "Data Science", "IA Appliquée"],
            "icon": "🤖",
            "color": "#ef4444"
        },
        "Security & Networks": {
            "skills": ["TCP/IP", "Network Protocols"],
            "icon": "🔒",
            "color": "#06b6d4"
        },
        "Project Management": {
            "skills": ["Agile/Scrum", "DevOps", "UML"],
            "icon": "📊",
            "color": "#84cc16"
        },
        "Soft Skills": {
            "skills": ["Communication", "Entrepreneuriat", "Leadership", "Team Collaboration", "Multilingual (AR/FR/EN)"],
            "icon": "🎯",
            "color": "#f97316"
        }
    }
    
    # Create elegant grid layout
    for i in range(0, len(skills_categories), 2):
        col1, col2 = st.columns(2, gap="large")
        
        # Left column
        category_items = list(skills_categories.items())
        if i < len(category_items):
            category, data = category_items[i]
            with col1:
                render_skill_card(category, data)
        
        # Right column
        if i + 1 < len(category_items):
            category, data = category_items[i + 1]
            with col2:
                render_skill_card(category, data)

def render_skill_card(category, data):
    """Render individual skill card with elegant styling"""
    
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
    cols = st.columns(3)
    for i, skill in enumerate(skills):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="
                background: rgba({color[1:3]}, {color[3:5]}, {color[5:7]}, 0.15);
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

if __name__ == "__main__":
    render_education_page()
