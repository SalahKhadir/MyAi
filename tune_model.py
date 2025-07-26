"""
Script to execute model tuning for Salah's Portfolio Assistant
"""

import json
import os
from model_tuner import ModelTuner
from ai_client import AIClient

def main():
    """Main function to execute model tuning"""
    
    print("🤖 Salah's Portfolio Assistant - Model Tuning")
    print("=" * 50)
    
    # Initialize tuner
    tuner = ModelTuner()
    
    # Validate training data
    print("📊 Validating training data...")
    if not tuner.validate_training_data():
        print("❌ Training data validation failed")
        return False
    
    print("✅ Training data validated successfully")
    
    # Get tuning configuration
    config = tuner.create_tuning_job()
    print("\n🔧 Tuning Configuration:")
    print(f"Base Model: {config['base_model']}")
    print(f"Display Name: {config['display_name']}")
    print(f"Training Data: {config['supervised_tuning_spec']['training_dataset_uri']}")
    
    # Test current system instruction
    print("\n🧪 Testing System Instruction...")
    ai_client = AIClient()
    
    if ai_client.is_configured():
        test_queries = [
            "Describe Salah's academic background",
            "Tell me about his projects",
            "What makes him a great developer?",
            "What is EcoTrace?",
            "Tell me about the CGI AI Chatbot project"
        ]
        
        for query in test_queries:
            print(f"\n❓ Query: {query}")
            try:
                response = ai_client.generate_response(query)
                print(f"💬 Response: {response[:200]}...")
            except Exception as e:
                print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("📋 Next Steps:")
    print("1. Upload training_data.jsonl to Google Cloud Storage")
    print("2. Run Vertex AI tuning job with the configuration")
    print("3. Test the tuned model when ready")
    print("4. Update ai_client.py with the tuned model ID")
    
    return True

def create_env_template():
    """Create a template .env file"""
    env_template = """# Google Cloud Configuration for Model Tuning
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_CLOUD_PROJECT_ID=your_project_id_here
GOOGLE_CLOUD_LOCATION=us-central1

# Instructions:
# 1. Replace the values above with your actual credentials
# 2. Ensure your Google Cloud project has Vertex AI enabled
# 3. Set up authentication for Vertex AI
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(env_template)
        print("📝 Created .env template file - please fill in your credentials")

def test_portfolio_responses():
    """Test the portfolio assistant responses"""
    print("\n🎯 Testing Portfolio Assistant Responses")
    print("-" * 40)
    
    ai_client = AIClient()
    
    portfolio_questions = [
        "Where is Salah from and how old is he?",
        "What programming languages does Salah know?",
        "Tell me about EcoTrace project",
        "What is SkillSync?",
        "Tell me about the Pharmacy Management System",
        "What makes Salah stand out as a developer?",
        "How can I hire Salah?",
        "What's Salah's experience with AI?",
        "Tell me about his internship at CGI",
        "What technologies does Salah use for AI projects?",
        "What are Salah's career goals?",
        "Why should I hire Salah?",
        "What makes his projects special?",
        "Tell me about his GitHub portfolio",
        # Personal life questions to test enhanced training data
        "What does Salah enjoy doing in his free time?",
        "What motivated Salah to choose Computer Engineering?",
        "What sports does Salah play and what are his hobbies?",
        "Tell me about Salah's personality and what makes him unique",
        "What languages does Salah speak and where is he from exactly?",
        "When was Salah born and where did he grow up?",
        "What's Salah's favorite anime and what music does he like?",
        "How did Salah start programming and what was his first language?",
        "What does Salah find most satisfying about programming?"
    ]
    
    for question in portfolio_questions:
        print(f"\n❓ {question}")
        try:
            response = ai_client.generate_response(question)
            print(f"🤖 LilSall: {response}")
        except Exception as e:
            print(f"❌ Error: {e}")
        print("-" * 40)

if __name__ == "__main__":
    # Create environment template if needed
    create_env_template()
    
    # Run main tuning process
    success = main()
    
    if success:
        # Test portfolio responses
        test_portfolio_responses()
