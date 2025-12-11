"""
st.session_state is the primary tool Streamlit provides for managing the state of the application across user interactions and reruns.

It functions like a Python dictionary that allows you to store and persist 
variables and data between different user interactions (like button clicks, typing
in text boxes, or selecting options) without the data being lost when the script reruns.

Streamlit reruns the entire script from top to bottom every time a widget is interacted 
with. st.session_state prevents the loss of variable values during these reruns, 
allowing the app to "remember" things.
"""

import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title = "Gemini Q&A Chatbot", layout = "wide")
st.title("🤖 Gemini-Powered Q&A Assistant")
st.write("Ask any question—I'll use Google's free 'gemini-1.5-flash' model to answer!")

# Session state for chat history (client-side)
if "messages" not in st.session_state:  # check for a list named messages inside st.session_state
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = "user_chat_1"


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input(:= warlus operator checks for input and assigns value)
if prompt := st.chat_input("What is your question"):
    # Add user message to UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):  # visual container for message bubble
        st.markdown(prompt)
    
    # Send to backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking with Gemini..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json = {"question": prompt, "session_id": st.session_state.session_id}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    if "error" in result:
                        st.error(result["error"])
                    else:
                        answer = result["answer"]
                        st.markdown(answer)
                        # Add to local history
                        st.session_state.messages.append({"role": "assistant", "content": answer})

                else:
                    st.error(f"Backend issue: {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("Can't reach backend-check if FastAPI is running on port 8000.")
            except Exception as e:
                st.error(f"Oops: {e}")


# Sidebar for new chat
with st.sidebar:
    st.header("Chat Controls")
    if st.button("New Chat"):
        st.session_state.messages = []
        st.session_state.session_id = f"user_chat_{len(st.session_state.messages) + 1}"
        st.rerun()
    
    st.write("**Backend:**", BACKEND_URL)
    if st.button("Test Connection"):
        try:
            r = requests.get(BACKEND_URL)
            st.success("✅ Backend alive!")
        except:
            st.error("❌ Backend down")