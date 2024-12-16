import streamlit as st
from streamlit_theme_provider import streamlit_theme_provider

st.title("Streamlit Theme Provider")

theme = streamlit_theme_provider()

st.write(f"Theme:")

st.write(theme)