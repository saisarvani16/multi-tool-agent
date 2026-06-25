# Multi Tool Agent

A **Python + Streamlit based Multi-Tool AI Agent** that processes user queries through an intelligent backend and delivers dynamic responses through a simple web interface.

---

## Description

This project is a **Multi-Tool AI Agent** built using **Python** and **Streamlit**. It provides a user-friendly web interface where users can enter a query, and the agent processes it using backend logic to generate intelligent responses.

The project is structured in a modular way:
- **`app.py`** handles the Streamlit frontend/UI
- **`backend.py`** handles the backend logic and response generation

This separation makes the project easier to maintain, extend, and integrate with more tools, APIs, or automation workflows in the future.

---

## Features

- Interactive **Streamlit web interface**
- Backend-based **AI agent processing**
- Modular code structure for frontend and backend
- Supports **multi-tool agent workflow**
- Easy to extend with new tools and APIs
- Simple and clean UI for user interaction

---

## Project Structure

```bash
LLM/
├── app.py                # Streamlit frontend
├── backend.py            # Backend logic / agent workflow
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── .gitignore            # Files to ignore in Git
├── gcp-credentials.json  # Local credentials file (should not be pushed)
├── sai.ipynb             # Notebook file
└── venv/                 # Virtual environment (should not be pushed)
