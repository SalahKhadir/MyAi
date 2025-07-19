import streamlit as st
from dotenv import load_dotenv
import os
import google.genai as genai
import json

# Load API key
load_dotenv()
genai_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=genai_api_key)

# Check if this is an API request
query_params = st.query_params
is_api_request = query_params.get("api") == "true"

if is_api_request:
    # API mode - handle POST requests from frontend
    st.set_page_config(page_title="API", layout="centered")
    
    # Add CORS headers
    st.markdown("""
    <script>
    // Allow CORS for API requests
    window.addEventListener('message', function(event) {
        if (event.data.type === 'STREAMLIT_QUERY') {
            event.source.postMessage({
                type: 'STREAMLIT_RESPONSE',
                data: 'CORS_ENABLED'
            }, '*');
        }
    });
    </script>
    """, unsafe_allow_html=True)
    
    # Get the question from query params
    question = query_params.get("question", "")
    
    if question:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp", 
                contents=question
            )
            result = {
                "success": True,
                "response": response.text,
                "error": None
            }
        except Exception as e:
            result = {
                "success": False,
                "response": None,
                "error": str(e)
            }
        
        # Display result as JSON for API consumption
        st.json(result)
    else:
        st.json({"success": False, "error": "No question provided"})

else:
    # Regular Streamlit UI mode
    st.set_page_config(page_title="Gemini Chatbot 🤖", layout="centered")
    st.title("💬 Ask Anything - Powered by Gemini")
    
    # Add API endpoint info
    st.info("🔗 API Endpoint: Add `?api=true&question=YOUR_QUESTION` to the URL")

    user_input = st.text_input("Type your question here:")

    if st.button("Ask") and user_input:
        with st.spinner("Thinking... 🤔"):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp", 
                    contents=user_input
                )
                st.success("✅ Gemini says:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
