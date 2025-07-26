"""
Projects Page - Professional showcase of projects with sliding card navigation
"""
import streamlit as st

def render_projects_page():
    """Render the professional projects page with all cards displayed"""
    
    # Ensure we stay on the projects page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'projects'
    st.session_state.current_page = 'projects'
    
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
        ">My Projects</h1>
        <p style="
            color: #94a3b8;
            font-size: 1.2rem;
            margin: 0;
            font-weight: 300;
        ">Innovative solutions built with passion and cutting-edge technologies</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Projects data - Add your actual projects here
    projects = [
        {
            "id": "ecotrace",
            "title": "EcoTrace",
            "subtitle": "Digital Waste Management System",
            "description": "A comprehensive digital waste management system for sustainable waste tracking and collection coordination. ECOTRACE digitalizes and streamlines waste management processes, connecting individuals, companies, logistics coordinators, transporters, and technicians in an efficient eco-friendly ecosystem with complete traceability from collection request to final processing.",
            "technologies": ["React 18", "Vite", "Tailwind CSS", "Django 4.2", "Django REST Framework", "JWT Authentication"],
            "github_link": "https://github.com/SalahKhadir/ecotrace-pfa",
            "image_path": "assets/images/projects/ecotrace.png",
            "image_placeholder": "ECO",
            "features": [
                "Multi-role system for all stakeholders",
                "Digital waste tracking with complete traceability",
                "Smart collection planning and route optimization",
                "Real-time notifications and status updates"
            ],
            "highlights": [
                "Full-stack application with modern tech stack",
                "Role-based access control for 6 user types",
                "Automated route optimization for collections",
                "Mobile-responsive design for all devices"
            ]
        },
        {
            "id": "skillsync",
            "title": "SkillSync",
            "subtitle": "Modern Recruitment Platform",
            "description": "A modern, full-stack recruitment platform that streamlines the hiring process for both recruiters and job seekers. Built with React and Python, it features an intuitive UI with modern design patterns, smooth animations, and comprehensive candidate management with #1ABC9C branding.",
            "technologies": ["React.js", "Material-UI", "Python", "MySQL", "RESTful API", "Custom CSS"],
            "github_link": "https://github.com/SalahKhadir/SkillSync",
            "image_path": "assets/images/projects/skillsync.png",
            "image_placeholder": "SYNC",
            "features": [
                "Smart job matching based on skills and experience",
                "Application tracking dashboard for job seekers",
                "Comprehensive candidate management for recruiters",
                "Interview scheduling and coordination system"
            ],
            "highlights": [
                "Modern card-based interface with animations",
                "Glassmorphism and modern design patterns",
                "Role-based access for recruiters and job seekers",
                "Real-time notifications and status updates"
            ]
        },
        {
            "id": "pharmacy-management",
            "title": "Pharmacy Management System",
            "subtitle": "Desktop Application for Pharmacy Operations",
            "description": "A comprehensive desktop application for managing pharmacy operations, built with Java Swing and MySQL. This system provides role-based access control for administrators and pharmacists with complete inventory management, sales processing, FIFO inventory rotation, and automated PDF invoice generation.",
            "technologies": ["Java Swing", "MySQL 8.0", "JDBC", "iText PDF", "JCalendar"],
            "github_link": "https://github.com/SalahKhadir/Pharmacy-Management-System",
            "image_path": "assets/images/projects/pharmacy-management.png",
            "image_placeholder": "PHARM",
            "features": [
                "Role-based access for administrators and pharmacists",
                "FIFO inventory with automatic stock rotation",
                "Complete point-of-sale system with cart functionality",
                "Automated PDF invoice generation with auto-print"
            ],
            "highlights": [
                "Desktop application with Java Swing GUI",
                "Real-time search with dynamic filtering",
                "Comprehensive input validation and error handling",
                "Secure authentication with role management"
            ]
        },
        {
            "id": "cgi-real-estate-chatbot",
            "title": "CGI Real Estate AI Chatbot",
            "subtitle": "Full-Stack AI Assistant for Morocco's Leading Real Estate Company",
            "description": "An intelligent conversational AI assistant designed specifically for CGI (Compagnie générale immobilière), Morocco's leading real estate company since 1960. This full-stack application combines Google Gemini 2.0 Flash with robust user management, document analysis capabilities, and ChatGPT-style interface for luxury properties and investment opportunities.",
            "technologies": ["FastAPI", "React 19", "Vite", "Google Gemini 2.0", "MySQL", "JWT Authentication"],
            "github_link": "https://github.com/SalahKhadir/ChatBot",
            "image_path": "assets/images/projects/ai-chatbot.png",
            "image_placeholder": "CGI",
            "features": [
                "Google Gemini 2.0 Flash integration for real estate expertise",
                "PDF document analysis with intelligent extraction",
                "Persistent chat history with ChatGPT-style sidebar",
                "Dual access modes: public and authenticated users"
            ],
            "highlights": [
                "Professional internship project for enterprise client",
                "Real estate domain-specialized AI responses",
                "Full-stack architecture with modern tech stack",
                "Production-ready with comprehensive user management"
            ]
        }
    ]
    
    # Display all projects as cards in a grid layout
    for i in range(0, len(projects), 2):
        cols = st.columns(2, gap="large")
        
        # Left column
        if i < len(projects):
            with cols[0]:
                render_project_card(projects[i])
        
        # Right column
        if i + 1 < len(projects):
            with cols[1]:
                render_project_card(projects[i + 1])
    
    # Add "See More Projects" section at the bottom
    st.markdown("""
    <div style="
        margin-top: 4rem;
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.7));
        border-radius: 20px;
        border: 1px solid rgba(96, 165, 250, 0.2);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    ">
        <h2 style="
            color: #60a5fa;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #60a5fa, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        ">Want to See More?</h2>
        <p style="
            color: #94a3b8;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            font-weight: 300;
            line-height: 1.6;
        ">Explore my complete collection of projects, experiments, and contributions on GitHub.</p>
        <div style="
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        ">
            <a href="https://github.com/SalahKhadir?tab=repositories" target="_blank" style="
                background: linear-gradient(135deg, #60a5fa, #3b82f6);
                color: white;
                text-decoration: none;
                padding: 0.8rem 2rem;
                border-radius: 12px;
                font-weight: 600;
                font-size: 1rem;
                box-shadow: 0 4px 20px rgba(96, 165, 250, 0.4);
                transition: all 0.3s ease;
                border: none;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
            ">
                View All Repositories
            </a>
            <a href="https://github.com/SalahKhadir" target="_blank" style="
                background: rgba(16, 185, 129, 0.15);
                color: #10b981;
                text-decoration: none;
                padding: 0.8rem 2rem;
                border-radius: 12px;
                font-weight: 600;
                font-size: 1rem;
                border: 1px solid rgba(16, 185, 129, 0.3);
                transition: all 0.3s ease;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
            ">
                GitHub Profile
            </a>
        </div>
        <div style="
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(96, 165, 250, 0.2);
        ">
            <div style="
                display: flex;
                justify-content: center;
                gap: 2rem;
                flex-wrap: wrap;
                color: #94a3b8;
                font-size: 0.9rem;
            ">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <div style="
                        width: 8px;
                        height: 8px;
                        border-radius: 50%;
                        background: #60a5fa;
                    "></div>
                    <span>20+ Repositories</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <div style="
                        width: 8px;
                        height: 8px;
                        border-radius: 50%;
                        background: #10b981;
                    "></div>
                    <span>Open Source Projects</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <div style="
                        width: 8px;
                        height: 8px;
                        border-radius: 50%;
                        background: #f59e0b;
                    "></div>
                    <span>Active Development</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_project_card(project):
    """Render individual project card using Streamlit components with proper styling"""
    
    # Create a container with custom styling
    with st.container():
        # Project image or placeholder
        if project.get('image_path') and project['image_path']:
            try:
                # Display actual project image
                st.image(project['image_path'], use_container_width=True, caption=f"{project['title']} - {project['subtitle']}")
            except:
                # Fallback to placeholder if image fails to load
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.7));
                    padding: 2rem;
                    border-radius: 16px;
                    margin-bottom: 1rem;
                    border: 1px solid rgba(96, 165, 250, 0.2);
                    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
                    text-align: center;
                ">
                    <div style="
                        width: 120px;
                        height: 120px;
                        border-radius: 12px;
                        background: linear-gradient(135deg, #60a5fa, #3b82f6);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin: 0 auto 1rem auto;
                        box-shadow: 0 4px 20px rgba(96, 165, 250, 0.4);
                    ">
                        <span style="
                            color: white;
                            font-size: 1.5rem;
                            font-weight: 700;
                        ">{project['image_placeholder']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Show placeholder for projects without images
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(51, 65, 85, 0.7));
                padding: 2rem;
                border-radius: 16px;
                margin-bottom: 1rem;
                border: 1px solid rgba(96, 165, 250, 0.2);
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
                text-align: center;
            ">
                <div style="
                    width: 120px;
                    height: 120px;
                    border-radius: 12px;
                    background: linear-gradient(135deg, #60a5fa, #3b82f6);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1rem auto;
                    box-shadow: 0 4px 20px rgba(96, 165, 250, 0.4);
                ">
                    <span style="
                        color: white;
                        font-size: 1.5rem;
                        font-weight: 700;
                    ">{project['image_placeholder']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Project header
        st.markdown(f"""
        <div style="
            text-align: center;
            margin-bottom: 1.5rem;
        ">
            <h3 style="color: #60a5fa; font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;">
                {project['title']}
            </h3>
            <p style="color: #94a3b8; font-size: 1rem; margin-bottom: 1.5rem; font-weight: 400;">
                {project['subtitle']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # GitHub button
        if st.button(f"🔗 View on GitHub", key=f"github_{project['id']}", use_container_width=True):
            st.markdown(f"**GitHub Repository:** [{project['github_link']}]({project['github_link']})")
        
        # Project description with proper title styling
        st.markdown("""
        <h4 style="
            color: #e2e8f0; 
            font-size: 1.3rem; 
            font-weight: 600; 
            margin: 1.5rem 0 1rem 0;
            border-bottom: 2px solid #60a5fa;
            padding-bottom: 0.5rem;
        ">Description:</h4>
        """, unsafe_allow_html=True)
        st.write(project['description'])
        
        # Technologies section with proper styling
        st.markdown("""
        <h4 style="
            color: #e2e8f0; 
            font-size: 1.3rem; 
            font-weight: 600; 
            margin: 1.5rem 0 1rem 0;
            border-bottom: 2px solid #10b981;
            padding-bottom: 0.5rem;
        ">Technologies Used:</h4>
        """, unsafe_allow_html=True)
        
        # Technology badges with green theme
        cols = st.columns(3)
        for i, tech in enumerate(project['technologies']):
            with cols[i % 3]:
                st.markdown(f"""
                <div style="
                    background: rgba(16, 185, 129, 0.15);
                    color: #10b981;
                    padding: 0.5rem 0.8rem;
                    border-radius: 8px;
                    margin: 0.3rem 0;
                    border: 1px solid rgba(16, 185, 129, 0.3);
                    text-align: center;
                    font-weight: 600;
                    font-size: 0.9rem;
                ">{tech}</div>
                """, unsafe_allow_html=True)
        
        # Key features with proper styling
        st.markdown("""
        <h4 style="
            color: #e2e8f0; 
            font-size: 1.3rem; 
            font-weight: 600; 
            margin: 1.5rem 0 1rem 0;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 0.5rem;
        ">Key Features:</h4>
        """, unsafe_allow_html=True)
        
        for feature in project['features']:
            st.markdown(f"""
            <div style="
                background: rgba(59, 130, 246, 0.1);
                color: #e2e8f0;
                padding: 0.6rem 1rem;
                border-radius: 8px;
                margin: 0.4rem 0;
                border-left: 4px solid #3b82f6;
                font-size: 0.95rem;
                line-height: 1.4;
            ">• {feature}</div>
            """, unsafe_allow_html=True)
        
        # Technical highlights with proper styling
        st.markdown("""
        <h4 style="
            color: #e2e8f0; 
            font-size: 1.3rem; 
            font-weight: 600; 
            margin: 1.5rem 0 1rem 0;
            border-bottom: 2px solid #f59e0b;
            padding-bottom: 0.5rem;
        ">Technical Highlights:</h4>
        """, unsafe_allow_html=True)
        
        for highlight in project['highlights']:
            st.markdown(f"""
            <div style="
                background: rgba(245, 158, 11, 0.1);
                color: #e2e8f0;
                padding: 0.6rem 1rem;
                border-radius: 8px;
                margin: 0.4rem 0;
                border-left: 4px solid #f59e0b;
                font-size: 0.95rem;
                line-height: 1.4;
            ">• {highlight}</div>
            """, unsafe_allow_html=True)
        
        # Project separator
        st.markdown("""
        <div style="
            height: 2px;
            background: linear-gradient(90deg, transparent, #60a5fa, transparent);
            margin: 2rem 0;
        "></div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_projects_page()
