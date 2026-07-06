import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

# -----------------------------
# Get API Key
# -----------------------------

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    api_key = st.secrets["GROQ_API_KEY"]

# -----------------------------
# Get Model
# -----------------------------

model_name = os.getenv("GROQ_API_KEY")

if not model_name:
    model_name = st.secrets["GROQ_API_KEY"]

# -----------------------------
# Create Client
# -----------------------------

client = genai.Client(api_key=api_key)

# -----------------------------
# Generate Answer
# -----------------------------

def generate_answer(prompt):

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    return response.text