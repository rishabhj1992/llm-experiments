import streamlit as st
from auth import show_login
from story import generate_story

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Show login if not authenticated
if not st.session_state.logged_in:
    show_login()
else:
    # Story Generator UI
    st.title("📖 AI Story Generator")

    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)
    character = st.text_input("Enter your favorite movie character:")

    if st.button("Generate Story"):
        story = generate_story(name, age, character)
        if story:
            st.write(story)

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()