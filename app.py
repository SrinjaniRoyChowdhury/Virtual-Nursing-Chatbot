import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the system prompt as the first message manually
nursebot_prompt = """
You are NurseBot, a professional virtual nursing assistant.
Your job is to understand all user inputs as health, medical, or nursing-related.
Provide medically accurate, supportive, and compassionate answers.
If a user says something like "I have pile", assume it's about hemorrhoids.
Avoid hallucination.
"""

# Streamlit UI
st.set_page_config(page_title="NurseBot 🩺", page_icon="🩺")
st.title("🩺 NurseBot - Your Virtual Nursing Assistant")

# Start a chat session
if "chat_session" not in st.session_state:
    chat = model.start_chat(history=[])
    chat.send_message(nursebot_prompt)  # Inject the system instruction as first message
    st.session_state.chat_session = chat

# Display chat history (excluding system prompt)
for msg in st.session_state.chat_session.history[1:]:  # skip system prompt
    with st.chat_message(msg.role, avatar="🧑" if msg.role == "user" else "🤖"):
        st.markdown(msg.parts[0].text)

# Input box
user_input = st.chat_input("Ask your health or nursing-related question here...")

if user_input:
    # Display user's message
    st.chat_message("user", avatar="🧑").markdown(user_input)

    try:
        # Get assistant response
        response = st.session_state.chat_session.send_message(user_input)
        st.chat_message("assistant", avatar="🤖").markdown(response.text)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
