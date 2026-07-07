import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

# -----------------------------
# Get API Key
# -----------------------------

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    api_key = st.secrets["OPENROUTER_API_KEY"]

# -----------------------------
# Get Model
# -----------------------------

model_name = os.getenv("OPENROUTER_MODEL")

if not model_name:
    model_name = st.secrets["OPENROUTER_MODEL"]

# -----------------------------
# Create Client
# -----------------------------

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)
# -----------------------------
# Generate Answer
# -----------------------------

def generate_answer(prompt):

    response = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
    )

    return response.choices[0].message.content
