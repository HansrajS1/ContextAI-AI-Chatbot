# ContextAI – Retrieval-Augmented AI Chatbot
Live: [Link](https://contextai-ai-chatbot.streamlit.app)
## Overview

ContextAI is a production-ready, ChatGPT-style conversational AI application built using Streamlit.  
It combines Retrieval-Augmented Generation (RAG), live web search fallback, and configurable response modes to deliver accurate, contextual, and reliable answers.

The project is designed with modularity and scalability in mind, making it suitable for real-world AI engineering use cases, assignments, and interviews.


---

## Features

- Conversational chat interface with session-based memory
- Retrieval-Augmented Generation using FAISS
- Supports PDF, CSV, and TXT documents as knowledge sources
- Live web search fallback when local knowledge is insufficient
- Configurable response modes: Concise and Detailed
- Modular architecture for LLMs, embeddings, and utilities
- Secure API key management using environment variables
- Production-ready Streamlit UI

---

## Technology Stack

- Python 3.10+
- Streamlit
- LangChain (Community + Text Splitters)
- FAISS Vector Database
- Groq LLM (LLaMA-based, configurable)
- SERP API for live web search
- python-dotenv for environment management

---
## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/HansrajS1/ContextAI-AI-Chatbot.git
cd ContextAI-AI-Chatbot
pip install -r requirements.txt
```

### 2. Create a .env file in the project root:
- GROQ_API_KEY=your_groq_api_key
- SERP_API_KEY=your_serp_api_key

### 3. Run streamlit app
```bash
streamlit run app.py
```


Response Modes

Concise
- Provides short and summarized answers

Detailed
- Provides expanded and in-depth explanations
