import streamlit as st
from app.db import get_connection
from app.users import set_user,get_user
from app.users import hash_password
from app.users import is_valid_hash
conn = get_connection()
st.title("Welcome to the home page")
st.write("This is the home page of the Cyber Incidents Dashboard application.")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ""


tab_log_in, tab_registration = st.tabs(["Log In", "Registration"]) 
with tab_log_in:
    st.header("Log In")

    login_username = st.text_input("Username",key="login_username")
    login_password = st.text_input("Password", type="password",key="login_password")
    
    if st.button("Log in"):
        user = get_user(conn, login_username)
        if user is None:
            st.error("Username not found. Please register first.")
        else:
            id, name, user_hash = user
            if login_username == name and is_valid_hash(login_password, user_hash):
                st.session_state['logged_in'] = True
                st.success("You are now logged in!")
                st.session_state['username'] = login_username
                st.switch_page('pages/Dashboard.py')
            else:
                st.error("Invalid password.")


with tab_registration:
    st.header("User Registration")
    register_user = st.text_input("Choose a Username",key="register_username")
    register_password = st.text_input("Choose a Password", type="password",key="register_password")
    
    if st.button("Register"):
        try:
            hashed_pwd = hash_password(register_password)
            set_user(conn, register_user, hashed_pwd)
            st.success("Registration successful! You can now log in.")
        except Exception as e:
            st.error(f"Registration failed: {str(e)}")

