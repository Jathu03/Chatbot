import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

# Load .env
load_dotenv()

# Setup Gemini
api_key = os.getenv("Gemini_key")
if not api_key:
    raise ValueError("Gemini_key not found in .env file.")
os.environ["GOOGLE_API_KEY"] = api_key

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    temperature=0.7,
    max_output_tokens=1024,
    timeout = 30,
    convert_system_message_to_human = True
)

app = FastAPI(title = "Gemini Q&A Chatbot API")

# Allow Streamlit to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:8501"],
    allow_methods = ["*"],
    allow_headers = ['*'],
)

class ChatInput(BaseModel):
    question: str
    session_id: str = "default_chat"   # For multi-turn history

# Simple in-memory history store
history_store: Dict[str, List[Any]] = {}

@app.get("/")
def home():
    return {"message": "Gemini Q&A backend is running! Ask away."}

@app.post("/chat")
def chat_with_gemini(input: ChatInput) -> Dict[str, Any]:
    session_id = input.session_id
    question = input.question.strip()

    if not question:
        return {"error": "Question cannot be empty!"}
    
    # Get or init history
    if session_id not in history_store:
        history_store[session_id] = []

    # Add user message to history
    history_store[session_id].append(HumanMessage(content = question))

    # Prepare messages for model (last 10 for context limit)
    messages = history_store[session_id][-10:]

    try:
        # Invoke Gemini
        response = model.invoke(messages)
        ai_reply = response.content

        # Add AI response to history
        history_store[session_id].append(AIMessage(content = ai_reply))

        return {
            "question": question,
            "answer": ai_reply,
            "session_id": session_id,
        }

    except Exception as e:
        return {"error": f"Gemini error: {str(e)}. Check API key or rate limits."}