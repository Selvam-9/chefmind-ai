import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

def generate_answer(prompt):
    """
    Generate answer using Gemini
    """
    response = client.models.generate_content(
        model=os.getenv('GEMINI_MODEL'),
        contents=prompt
    )
    if not response:
        response = client.models.generate_content(
        model=st.secrets.get('GEMINI_MODEL'),
        contents=prompt
    )
    
    return response.text
