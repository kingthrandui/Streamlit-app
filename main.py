import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

st.set_page_config(
    page_title="Gemini AI Chat",
    page_icon="🤖",
    layout="centered"
)
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def map_role(role):
    return "Assistant" if role == "assistant" else "User"

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Hello Navjeet!")

for message in st.session_state.chat_session.history:
   with st.chat_message(map_role(message.role)):
    st.markdown(message.parts[0].text)

user_input = st.chat_input("Ask me Sir!")
if user_input:
    st.chat_message("user").markdown(user_input)
    response = st.session_state.chat_session.send_message(user_input)

    with st.chat_message("assistant"):
        st.markdown(response.text)