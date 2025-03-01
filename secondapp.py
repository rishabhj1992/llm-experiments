import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google AI (Replace with your actual API key)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit UI
st.title("✨ AI Story Generator ✨")
st.write("Enter your details and let AI create a fun short story for you!")

# User inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
fav_character = st.text_input("Enter your favorite movie character:")

# Generate story on button click
if st.button("Generate Story"):
    if name and age and fav_character:
        # Prompt for LLM
        prompt = (
            f"Write a short, fun, and adventurous story featuring {name}, a {age}-year-old, "
            f"who meets their favorite movie character, {fav_character}. "
            "Make it engaging, creative, and full of surprises!"
        )
        
        # Call Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        # Display the story
        st.subheader("Here’s your story:")
        st.write(response.text)
    else:
        st.warning("Please fill in all the fields to generate a story!")
