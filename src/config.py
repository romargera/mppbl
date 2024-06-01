# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

lat, lon, zoom = 48.858653170975046, 2.294514165895997, 16  # sample data  (Paris)
# lat, lon, zoom = 25.19745, 55.27417, 16 # sample data (Dubai)
scale = 1.5
projection = "web_mercator"
l = "map"

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
