# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("No API key provided. Please set the API_KEY environment variable.")

# Database Configuration
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')

# Application Settings
DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']
PORT = int(os.getenv('PORT', 5000))

# Logging Configuration
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')
