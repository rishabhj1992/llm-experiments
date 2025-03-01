import streamlit as st

# Static credentials (replace with a real auth system if needed)
USERNAME = "rishabh"
PASSWORD = "rishabh1992"

def show_login():
    """Login form that returns True if login is successful"""
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()  # Refresh app after login
        else:
            st.error("Invalid username or password!")