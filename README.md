# Gemini Q&A Chatbot

A small two-part example that demonstrates a simple chat assistant built with Google Gemini (via a LangChain wrapper) and a Streamlit frontend.

- Backend: FastAPI + Langchain Google Generative AI wrapper
- Frontend: Streamlit

This project uses an in-memory chat `session_id` to keep conversation context between messages (simple session history).

---

## Features

- Multi-turn chat using an in-memory history store on the backend
- Streamlit frontend with a chat UI and simple controls
- Easy local development using `system.bat` (Windows) that starts both backend and frontend

---

## Prerequisites

- Python 3.10 or newer (recommended)
- A Google Generative AI API key (Gemini model) with appropriate permissions
- Optional: Git (for cloning)

---

## Setup (Windows PowerShell)

1. Clone the repo and change into the project directory:

```powershell
git clone <repo-url>
cd Chatbot
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
```

3. Install dependencies:

```powershell
pip install fastapi uvicorn python-dotenv streamlit requests
# If required or if you use Langchain, add these packages (they may be optional depending on the setup):
pip install langchain langchain-google-genai
```

> Note: Package names for LangChain Google Generative wrappers may vary over time. If the imports in `backend/main.py` fail (for example, `langchain_google_genai`), check the package name on PyPI or the LangChain docs and install the correct package.

4. Create a `.env` file at the repository root with your Gemini (Generative AI) key.

```
# .env
Gemini_key=YOUR_GENERATIVE_AI_API_KEY_HERE
```

The backend reads `Gemini_key` from `.env` and sets it to `GOOGLE_API_KEY` internally.

> Important: Do not commit your `.env` file to Git. Add it to `.gitignore`.

---

## Running locally (Windows)

There are 2 primary parts to run the app:

- Backend (FastAPI): listens on port `8000`
- Frontend (Streamlit): serves on the default Streamlit port (8501)

Option A (recommended): run both at once (Windows):

```powershell
# From repository root:
.\system.bat
```

Option B: Run them individually from two terminals:

```powershell
# Terminal 1: backend
cd backend
uvicorn main:app --reload --port 8000

# Terminal 2: frontend
cd frontend
streamlit run app.py
```

Then open the Streamlit app in your browser (default):

- Frontend: http://localhost:8501/
- Backend API health (for quick check): http://127.0.0.1:8000/

Test the chat with the UI or using curl:

```powershell
curl -X POST http://127.0.0.1:8000/chat `
-H "Content-Type: application/json" `
-d '{"question":"What is photosynthesis?","session_id":"user_chat_1"}'
```

---

## Configuration

- The backend expects an environment variable named `Gemini_key`. The code will set `GOOGLE_API_KEY = Gemini_key` at runtime.
- The backend default model configuration is `gemini-2.5-flash-lite` (see `backend/main.py`). Customize the model options there if desired.

---

## Project Structure

```
Chatbot/
│  system.bat                  # quick startup script for Windows
│  README.md
├─ backend/
│  └─ main.py                  # FastAPI app, uses the Gemini Key
└─ frontend/
   └─ app.py                   # Streamlit app
```

---

## Development Notes

- This project uses an in-memory session store (`history_store` in `backend/main.py`) — it is not persistent and will reset if the backend restarts. For production, replace this with a persistent store like Redis or a DB.
- Keep your keys secret — do not commit `.env` to version control.
- There is minimal error handling, and the code uses `try/except` blocks to capture model exceptions. Add monitoring and logging for production scenarios.

Happy building! ⚡️
