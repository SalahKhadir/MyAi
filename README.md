# Professional Portfolio - Salah Khadir

A comprehensive professional portfolio application built with Streamlit, featuring an AI-powered assistant and multi-page showcase. This modern portfolio presents Salah Khadir's professional journey, projects, education, and experience through an interactive web interface with integrated AI chat capabilities.

## ✨ Features

- **Multi-Page Portfolio**: Complete professional showcase with dedicated pages
- **AI-Powered Assistant (LilSall)**: Interactive portfolio assistant using Google Gemini 2.0
- **Project Gallery**: Visual showcase with real project images and detailed descriptions
- **Professional Design**: Modern dark theme with blue gradient color palette
- **Responsive Layout**: Mobile-friendly design with professional styling
- **Real Portfolio Data**: Accurate information from actual CV and project details
- **GitHub Integration**: Direct links to repositories and profile

## 🛠️ Technologies

- **Frontend**: Streamlit, HTML5/CSS3, Custom Styling
- **AI**: Google Gemini 2.0 Flash API
- **Backend**: Python 3.8+
- **Data**: JSON training data for AI tuning
- **Deployment**: Streamlit Cloud
- **Version Control**: Git/GitHub

## 📱 Portfolio Pages

### 🏠 Home (About)
- Personal introduction and bio (age 23, born in Errachidia, Morocco)
- Skill categorization with modern UI components
- Professional summary and career objectives
- Contact information and social links

### 💼 Projects
- **EcoTrace**: React 18 + Django 4.2 waste management system
- **SkillSync**: React + Python recruitment platform  
- **Pharmacy Management**: Java Swing desktop application
- **CGI AI Chatbot**: FastAPI + React 19 + Gemini 2.0 enterprise solution
- Real project images and detailed technical specifications
- Direct GitHub repository links

### 🎓 Education
- Computer Engineering & Networks at EMSI
- Academic progression and specialization details
- Certification showcase and achievements

### 💻 Internships
- **CGI Promoteur Immobilier** (July-August 2025): AI Development Intern
- **ABHGZR** (April 2024): Web Development Intern
- Detailed project descriptions and technologies used
- Professional achievements and outcomes

### 🤖 AI Chat (LilSall)
- Interactive portfolio assistant powered by Google Gemini 2.0
- Trained on accurate personal and professional data
- ChatGPT-style interface with persistent chat history
- Real-time responses about skills, projects, and experience

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API key

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SalahKhadir/MyAi.git
   cd MyAi
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

## 🌐 Deployment on Streamlit Cloud

1. **Push to GitHub** (API key will be set in Streamlit Cloud secrets)
2. **Connect to Streamlit Cloud**
3. **Add secrets in Streamlit Cloud dashboard**:
   - Go to your app settings
   - Add secret: `GEMINI_API_KEY = "your_api_key_here"`

## 📁 Project Structure

```
MyAi/
├── main.py                 # Main application with navigation
├── about_page.py          # Home/About page with personal info
├── projects_page.py       # Projects showcase with images
├── education_page.py      # Academic background and certifications
├── internships_page.py    # Professional experience timeline
├── ai_client.py           # Google Gemini AI integration
├── chat_manager.py        # Chat functionality and history
├── ui_components.py       # Reusable UI components
├── styles.py             # Professional CSS styling
├── model_tuner.py        # AI model configuration
├── training_data.jsonl   # Accurate training data for AI
├── assets/               # Project images and resources
│   └── images/
│       ├── projects/     # Project screenshots
│       └── internships/  # Internship-related images
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (not in repo)
└── README.md           # This file
```

## 🤖 About LilSall AI Assistant

LilSall is an AI assistant trained on Salah Khadir's actual portfolio data, including:

- **Education**: Computer Engineering & Networks at EMSI (3rd → 4th year AI & Data Science)
- **Current Projects**: EcoTrace (React 18/Django), SkillSync (React/Python), CGI AI Chatbot (FastAPI/React 19/Gemini 2.0)
- **Professional Experience**: 
  - CGI Promoteur Immobilier (2025) - AI Development Intern
  - ABHGZR (2024) - Web Development Intern
- **Technical Skills**: Python, JavaScript, React, Django, FastAPI, AI/ML, Full-stack development
- **Specializations**: AI integration, modern web development, enterprise solutions
- **Personal Details**: Age 23, born in Errachidia, Morocco

## 🎨 Design Features

- **Professional Color Palette**: Blue gradient theme (#60a5fa, #3b82f6) with accent colors
- **Modern UI Components**: Card-based layouts, gradient backgrounds, professional styling
- **Responsive Design**: Mobile-friendly interface with consistent branding
- **Image Integration**: Real project screenshots with fallback placeholders
- **Professional Navigation**: Multi-page structure with smooth transitions
- **GitHub Integration**: Direct repository links and profile access

## 🚀 Live Demo

Visit the live portfolio: [Streamlit Cloud Deployment URL]

## 🔗 Additional Resources

- **All Projects**: [GitHub Repositories](https://github.com/SalahKhadir?tab=repositories)
- **Professional Profile**: [GitHub Profile](https://github.com/SalahKhadir)

## 📞 Contact

- **Email**: salaho.khadir@gmail.com
- **LinkedIn**: [Salah Khadir](https://www.linkedin.com/in/salah-khadir)
- **GitHub**: [SalahKhadir](https://github.com/SalahKhadir)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🏆 Key Achievements

- **Production-Ready AI Chatbot**: Successfully delivered enterprise solution for CGI
- **Full-Stack Portfolio**: Complete professional showcase with modern tech stack
- **Accurate AI Training**: Real portfolio data with corrected timelines and achievements
- **Professional Design**: Corporate-ready appearance with consistent branding
- **Image Integration**: Visual project showcase with real screenshots
- **Multi-Page Architecture**: Comprehensive portfolio structure

---

*Built with precision and professionalism by Salah Khadir*
*Powered by Google Gemini 2.0 Flash • Streamlit • Modern Web Technologies*
