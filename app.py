import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["AQ.Ab8RN6IvXTjyAIQcZsilLqVX-OgQ8d55gU6ZVWRieg111L6_aw"])
PI_KE
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="Ashmika AI Study Buddy",
    page_icon="🎓"
)

st.title("🎓 Ashmika AI Study Buddy")
st.write("Developed by **Maddikunta Ashmika**")
