import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Select the Gemini Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title("💡 Gemini Flash AI App")
st.write("Enter a prompt and get a response from Google's Gemini AI!")

# User input
user_input = st.text_area("Enter your prompt:", "")

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Generating response..."):
            response = model.generate_content(user_input)
            st.subheader("AI Response:")
            st.write(response.text)
    else:
        st.warning("Please enter a prompt!")