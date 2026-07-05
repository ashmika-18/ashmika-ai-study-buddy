import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="Ashmika AI Study Buddy",
    page_icon="🎓"
)

st.title("🎓 Ashmika AI Study Buddy")
st.write("Developed by **Maddikunta Ashmika**")
