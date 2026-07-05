from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def generate_answer(prompt):
    """
    Generate answer using Gemini
    """
    response = client.models.generate_content(
        model=os.getenv('GEMINI_MODEL'),
        contents=prompt
    )
    return response.text