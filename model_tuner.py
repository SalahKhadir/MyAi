"""
Model tuning configuration for Salah's Portfolio Assistant
"""

import os
from google.cloud import aiplatform
from dotenv import load_dotenv

class ModelTuner:
    def __init__(self):
        load_dotenv()
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
        self.location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
        self.training_data_uri = "training_data.jsonl"  # Local file path
        
        # Initialize Vertex AI
        if self.project_id:
            aiplatform.init(project=self.project_id, location=self.location)
    
    def create_tuning_job(self):
        """Create a supervised fine-tuning job for Gemini"""
        
        # Define the base model
        base_model = "gemini-1.5-flash-002"
        
        # Create tuning job configuration
        tuning_job_config = {
            "display_name": "salah-portfolio-assistant-tuning",
            "base_model": base_model,
            "supervised_tuning_spec": {
                "training_dataset_uri": self.training_data_uri,
                "hyperparameters": {
                    "learning_rate": 0.001,
                    "epoch_count": 3,
                    "adapter_size": 16
                }
            }
        }
        
        return tuning_job_config
    
    def get_system_instruction(self):
        """Get the system instruction for the tuned model"""
        return """You are LilSall, Salah Khadir's personal AI portfolio assistant. 

Your role is to represent Salah professionally and provide accurate, helpful information about:
- His technical skills and expertise
- His projects and achievements  
- His background and experience
- Career opportunities and collaboration

Always maintain a professional, knowledgeable, and approachable tone. Provide detailed, specific responses that showcase Salah's capabilities and value as a developer.

Key areas of expertise to highlight:
- AI integration and development
- Full-stack web development
- Modern frameworks (Streamlit, React, Node.js)
- Python and JavaScript programming
- Cloud platforms and deployment
- Problem-solving and system design"""

    def validate_training_data(self):
        """Validate the training data format"""
        try:
            with open(self.training_data_uri, 'r') as f:
                lines = f.readlines()
                print(f"Training data contains {len(lines)} examples")
                return True
        except FileNotFoundError:
            print(f"Training data file not found: {self.training_data_uri}")
            return False
        except Exception as e:
            print(f"Error validating training data: {e}")
            return False
