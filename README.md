# Chatbot Application

![Python](https://img.shields.io/badge/Language-Python-97%25-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-green)

This repository houses a full-stack **Chatbot Application**. It features a Python-based backend for handling logic and Natural Language Processing (NLP), coupled with a frontend interface for user interaction. The project includes automation scripts to streamline deployment on Windows environments.

## 📂 Repository Structure

The codebase is organized into three distinct components to separate concerns between the user interface, logic, and system orchestration.

| File/Folder | Type | Description |
| :--- | :--- | :--- |
| **`backend/`** | Folder | Contains the core application logic, API endpoints, and data processing algorithms. This is the "brain" of the chatbot written in Python. |
| **`frontend/`** | Folder | Houses the User Interface (UI) components. This directory manages how the user interacts with the chat system visually. |
| **`system.bat`** | File | A Windows Batch utility script. Designed to automate environment setup, initialization, or startup of the application. |

## 🛠️ Tech Stack

*   **Core Logic:** Python (97.1%)
*   **Automation:** Batchfile (2.9%)

## 🚀 Getting Started

### Prerequisites
*   Python 3.x installed and added to system PATH.
*   Windows OS (for the `.bat` script execution).

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Jathu03/Chatbot.git
    cd Chatbot
    ```

2.  **Automated Start (Windows):**
    Run the system script to initialize the application:
    ```cmd
    system.bat
    ```

3.  **Manual Start (Alternative):**
    If you wish to run the backend manually:
    ```bash
    cd backend
    # Install dependencies (if requirements.txt exists)
    # pip install -r requirements.txt
    python main.py
    ```
