import streamlit as st
from utils.db_utils import create_sandTable

if create_sandTable():
    username = st.text_input("Username")