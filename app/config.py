import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

BEST_THRESHOLD = 0.048
GROQ_MODEL = "llama-3.1-8b-instant"
print("GROQ KEY:", GROQ_API_KEY[:6] if GROQ_API_KEY else None)
