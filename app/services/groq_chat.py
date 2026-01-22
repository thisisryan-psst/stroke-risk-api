from groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def ask_groq(messages):
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content
