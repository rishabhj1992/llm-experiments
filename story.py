import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def generate_story(name, age, character):
    """Generates a story using Gemini AI"""

    if not name or not character:
        st.warning("Please enter both name and favorite movie character!")
        return None

    # 🔑 Load API key from Streamlit secrets
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # 📝 Story Prompt
    story_prompt = "Write a short story about {name}, who is {age} years old and embarks on an adventure with {character}."

    # 🤖 Generate story using Gemini AI

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(story_prompt)

    return response.text if response else "⚠️ Error generating story!"
