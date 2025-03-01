import streamlit as st
import google.generativeai as genai
import streamlit_authenticator as stauth

# Configure login credentials (Static for now)
USERNAME = "rishabh"
PASSWORD = "rishabh1992"

# Create a session state variable for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login Page
if not st.session_state.logged_in:
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid username or password!")
else:
    # Story Generator App (After Login)
    st.title("📖 AI Story Generator")
    
    # User inputs
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)
    character = st.text_input("Enter your favorite movie character:")

    # Generate story button
    if st.button("Generate Story"):
        if name and character:
            story_prompt = f"Write a short story about {name}, who is {age} years old and embarks on an adventure with {character}."
            
            # Load API Key
            gemini_key = st.secrets["api"]["gemini_key"]
            genai.configure(api_key=gemini_key)
            
            # Generate story
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(story_prompt)
            st.write(response.text)
        else:
            st.warning("Please enter both name and favorite movie character!")
    
    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()