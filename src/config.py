import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("API key not found! Set OPENAI_API_KEY in .env file")
