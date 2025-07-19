# AI Portfolio Assistant - LilSall

A professional AI portfolio assistant built with Streamlit and Google Gemini API. LilSall represents Salah Khadir's skills, experience, and projects in an interactive chat interface.

## 🚀 Features

- **AI-Powered Chat**: Interactive portfolio assistant using Google Gemini
- **Professional UI**: Dark theme with ChatGPT-style interface
- **Real Portfolio Data**: Trained on actual CV and project information
- **Responsive Design**: Modern, professional appearance
- **Social Integration**: Direct links to GitHub and LinkedIn

## 🛠️ Technologies

- **Frontend**: Streamlit, HTML/CSS
- **AI**: Google Gemini API
- **Backend**: Python
- **Deployment**: Streamlit Cloud

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
├── main.py              # Main application entry point
├── ai_client.py         # AI client and model management
├── chat_manager.py      # Chat functionality and message handling
├── ui_components.py     # UI components and navigation
├── styles.py           # CSS styling and themes
├── model_tuner.py      # AI model tuning configuration
├── training_data.jsonl # Training data for AI responses
├── requirements.txt    # Python dependencies
└── .env               # Environment variables (not in repo)
```

## 🤖 About LilSall

LilSall is an AI assistant trained on Salah Khadir's actual portfolio data, including:

- **Education**: Computer Science studies
- **Experience**: Internships at CGI and ABHGZR
- **Projects**: EcoTrace, SkillSync, Pharmacy Management System
- **Skills**: Python, JavaScript, AI/ML, Full-stack development
- **Certifications**: Multiple technical certifications

## 📞 Contact

- **Email**: salaho.khadir@gmail.com
- **LinkedIn**: [Salah Khadir](https://www.linkedin.com/in/salah-khadir)
- **GitHub**: [SalahKhadir](https://github.com/SalahKhadir)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ by Salah Khadir*
