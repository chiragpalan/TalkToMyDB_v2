import streamlit as st
from groq import Groq

MODEL_NAME = "llama3-8b-8192"

# Initialize Groq client using Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def nl_to_sql(question: str) -> str:
    """Convert a natural language question to SQL using Groq."""
    system_msg = (
        "You are an expert SQLite SQL generator for the Sakila database. "
        "Always return ONLY a syntactically correct SQL query for SQLite. "
        "Do not include explanations, comments, markdown, or extra text."
    )
    user_msg = f"Question: {question}"
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content.strip()
