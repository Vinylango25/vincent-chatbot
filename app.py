# app.py
import streamlit as st
import requests

st.set_page_config(page_title="Vincent Chatbot", layout="centered")

st.title("🤖 Vincent Chatbot")
st.markdown("Ask Vincent anything about his skills, experience, or background.")

query = st.text_area("Your question:", height=100)

if st.button("Send"):
    if query.strip():
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",  # Change this to your deployed FastAPI URL later
                json={"query": query}
            )
            if response.ok:
                st.success(response.json().get("response", "No response received."))
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter a question.")
