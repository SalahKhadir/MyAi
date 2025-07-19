"""
AI Client configuration and management
"""
import os
from google import genai
from google.genai.types import HttpOptions
from dotenv import load_dotenv

class AIClient:
    def __init__(self):
        self.client = None
        self.api_key = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the AI client with API key"""
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if self.api_key:
            os.environ["GOOGLE_GENAI_API_KEY"] = self.api_key
            self.client = genai.Client(http_options=HttpOptions(api_version="v1"))
            return True
        return False
    
    def is_configured(self):
        """Check if client is properly configured"""
        return self.client is not None and self.api_key is not None
    
    def generate_response(self, user_input):
        """Generate response from AI model"""
        if not self.is_configured():
            raise Exception("AI client is not properly configured")
        
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
        )
        
        return response.text
