import streamlit as st

def login_screen():
    st.header("Please log in.")
    st.button("Log in with Microsoft", on_click=st.login)

if not st.experimental_user.is_logged_in:
    login_screen()
else:
    st.header(f"Welcome, {st.experimental_user.name}!")
    st.button("Log out", on_click=st.logout)


# Add role assigning functionality with database for storing roles assigning(only by admin): admin or user
# User listing (Password reset by admin)
# Each user will have access to view specific dashboard. So the dashboard/analysis on left menu will only be visible if user has access to view specific analysis.    