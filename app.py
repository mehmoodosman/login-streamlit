import streamlit as st

def login_screen():
    st.header("Private App within your Organization.")
    st.button("Log in with Microsoft", on_click=st.login)

if not st.experimental_user.is_logged_in:
    login_screen()
else:
    st.header(f"Welcome, {st.experimental_user.name}!")
    st.button("Log out", on_click=st.logout)

