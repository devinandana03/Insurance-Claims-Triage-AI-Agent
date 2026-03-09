import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")

GROK_URL = "https://api.x.ai/v1/chat/completions"
MODEL = "grok-beta"