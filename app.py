
import streamlit as st
import google.generativeai as genai

# -----------------------------
# Configure Gemini API
# -----------------------------
genai.configure(api_key="AQ.Ab8RN6LSgAll-SVJ9FJU7Lmlib4HZ-6wyI3QOf7vjE15Z25SYA")

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Ashmika AI Study Buddy",
    page_icon="🎓"
)

# -----------------------------
# Title
# -----------------------------
st.title("🎓 Ashmika AI Study Buddy")
st.write("Developed by **Maddikunta Ashmika**")

# -----------------------------
# User Input
# -----------------------------
topic = st.text_input("📖 Enter a Topic")

# -----------------------------
# Activity Selection
# -----------------------------
option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("🚀 Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":

            prompt = f"""
You are Ashmika AI Learning Buddy.

Explain the concept of {topic} in simple language as if teaching a 15-year-old student.

Use easy words.
Use one simple analogy.
Keep the explanation short, clear, and engaging.
"""

        elif option == "Real-Life Example":

            prompt = f"""
You are Ashmika AI Learning Buddy.

Give one clear real-life example of {topic}.

Explain how it works in simple language and why it is important.
"""

        elif option == "Generate Quiz":

            prompt = f"""
You are Ashmika AI Learning Buddy.

Create 5 multiple-choice questions on {topic}.

Each question should have four options (A, B, C, D).

After every question provide:
• Correct Answer
• Short Explanation
"""

        else:

            prompt = f"""
You are Ashmika AI Learning Buddy.

Answer the following question clearly and accurately.

Question:
{topic}

Use simple language.
Give examples whenever helpful.
"""

        with st.spinner("Generating response..."):
            response = model.generate_content(prompt)

        st.success("✅ Response Generated Successfully!")

        st.write(response.text) 