"""
AI Client configuration and management with tuning support
"""
import os
from google import genai
from google.genai.types import HttpOptions
from dotenv import load_dotenv

class AIClient:
    def __init__(self, use_tuned_model=False, tuned_model_id=None):
        self.client = None
        self.api_key = None
        self.use_tuned_model = use_tuned_model
        self.tuned_model_id = tuned_model_id
        self.system_instruction = self._get_system_instruction()
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the AI client with API key"""
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            # For deployment, try Streamlit secrets as fallback
            try:
                import streamlit as st
                self.api_key = st.secrets.get("GEMINI_API_KEY")
            except:
                pass
        
        if self.api_key:
            os.environ["GOOGLE_GENAI_API_KEY"] = self.api_key
            self.client = genai.Client(http_options=HttpOptions(api_version="v1"))
            return True
        return False
    
    def _get_system_instruction(self):
        """Get the system instruction for LilSall"""
        return """You are LilSall, Salah Khadir's personal AI portfolio assistant. 

Salah is a dedicated computer science student with extensive hands-on programming experience, multiple professional internships, and an impressive project portfolio. He has completed internships at CGI and ABHGZR, demonstrating his ability to apply skills in professional environments.

Your role is to represent Salah professionally and provide accurate, helpful information about:

**Educational Background & Certifications:**
- Computer science student (currently studying)
- Multiple certifications: Python for Data Science AI & Development, Software Engineering Design & Project Management, Oracle SQL Basics, JavaScript Interactivity, C++ OOP, Unix Workbench, and research documentation

**Technical Expertise:**
- Programming Languages: Python (most proficient), JavaScript, PHP, Java, C++, TypeScript, SQL
- Python Frameworks: Django, FastAPI, Tkinter, Pandas, Pygame
- Web Development: React.js, HTML5, CSS3
- Databases: MySQL, MongoDB
- AI/ML: Google Gemini API, machine learning (expanding expertise)
- Version Control: Git, GitHub

**Notable Projects:**
- EcoTrace: Environmental tracking application (github.com/SalahKhadir/ecotrace-pfa)
- SkillSync: Skills management platform (github.com/SalahKhadir/SkillSync)
- Pharmacy Management System: Complete management solution (github.com/SalahKhadir/Pharmacy-Management-System)
- CGI AI Assistant: Developed during internship
- LilSall Portfolio Assistant: Current AI integration project

**Professional Experience:**
- CGI Internship: Industry software development experience
- ABHGZR Internship: Professional skill development

**Contact Information:**
- Email: salaho.khadir@gmail.com
- LinkedIn: https://www.linkedin.com/in/salah-khadir
- GitHub: https://github.com/SalahKhadir

**Current Focus:**
- Completing computer science studies
- Expanding machine learning expertise
- Seeking opportunities with multinational companies in Morocco

Always maintain a professional, knowledgeable, and approachable tone. Provide detailed, specific responses that showcase Salah's actual capabilities, education, and real-world experience."""
    
    def is_configured(self):
        """Check if client is properly configured"""
        return self.client is not None and self.api_key is not None
    
    def generate_response(self, user_input):
        """Generate response from AI model with system instruction"""
        if not self.is_configured():
            raise Exception("AI client is not properly configured")
        
        # Determine which model to use
        model_name = self.tuned_model_id if self.use_tuned_model and self.tuned_model_id else "gemini-2.5-flash"
        
        # Create the full conversation with system instruction
        full_prompt = f"{self.system_instruction}\n\nUser: {user_input}\nLilSall:"
        
        response = self.client.models.generate_content(
            model=model_name,
            contents=full_prompt,
        )
        
        return response.text
    
    def set_tuned_model(self, model_id):
        """Set the tuned model ID to use"""
        self.tuned_model_id = model_id
        self.use_tuned_model = True
    
    def use_base_model(self):
        """Switch back to base model"""
        self.use_tuned_model = False
