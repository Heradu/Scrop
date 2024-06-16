import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Summarize the following text to fit within 280 characters, including tags based on the most important words (focus on K-pop, Korean culture, etc.):\n\n{text}",
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()
