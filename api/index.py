"""
Vercel serverless function entry point for Django application.
"""
import os
import sys

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

# Import the Django WSGI application
from config.wsgi import application

# Vercel will use this as the handler
app = application
