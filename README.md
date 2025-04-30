---
title: LanggraphAgenticAI
emoji: 🐨
colorFrom: blue
colorTo: red
sdk: streamlit
sdk_version: 1.42.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Refined langgraphAgenticAI
---


# 🤖 Agentic AI Chatbot Framework (LangGraph + Groq)

An advanced modular Agentic AI system using **LangGraph**, **Groq LLMs**, and **Tavily Search** — deployable via Hugging Face Spaces.  
Supports both a basic chatbot and a tool-augmented agent using a dynamic Streamlit UI.

---

## 🌐 Live Demo

[![Open in Hugging Face](https://img.shields.io/badge/Live-Huggingface-blue?logo=huggingface)](https://huggingface.co/spaces/nishant-ds/Agentic-AI)

---

## 🧠 Key Features

- 💬 **Use Case Selector**: Switch between Basic Chatbot and Tool-augmented agent
- 🧱 **LangGraph State Management**: Modular, visual graph architecture
- ⚡ **Groq LLM Integration**: Ultra-fast inference with LLaMA3 and Mixtral models
- 🔍 **Tool Support via Tavily API**: Live web search during conversation
- 🎛️ **Streamlit UI** with model/API key inputs and chat display
- 🚀 **CI/CD to Hugging Face** using GitHub Actions

---

## 🛠️ Tech Stack

| Layer            | Tools Used                                    |
|------------------|-----------------------------------------------|
| UI               | Streamlit                                     |
| LLM Inference    | Groq LLMs via LangChain                        |
| Orchestration    | LangGraph (LangChain ecosystem)               |
| Tools            | Tavily Search Tool                            |
| State Format     | TypedDict + LangGraph Messaging               |
| DevOps           | GitHub Actions (auto-deploy to HF Spaces)     |

---
🚀 Getting Started Locally
```bash
# 1. Clone the repo
git clone https://github.com/nishantsingh-ds/langgraph-agentic-ai.git
cd langgraph-agentic-ai

# 2. Set up environment
python -m venv venv
source venv/bin/activate  # or use 'venv\Scripts\activate' on Windows

# 3. Install requirements
pip install -r requirements.txt

# 4. Run app
streamlit run main.py

```

Make sure to set the following environment variables before running:
```
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

🧪 Supported Use Cases
- Basic Chatbot: A clean Groq-powered LLM assistant using LangGraph state
- Chatbot with Tool: Adds search capabilities via Tavily API for contextual queries

You can select both use case and LLM model from the sidebar UI.

🔄 CI/CD with GitHub → Hugging Face
This repo includes a GitHub Actions workflow to:

- Clean unnecessary files from push (e.g. PDFs)
- Push main branch to Hugging Face Space
- Uses your Hugging Face token via HF_TOKEN GitHub secret

📈 Future Improvements

- PDF-based summarization (DocQA + RAG)
- Persona-based chatbot switching
- Conversational memory with context carry-over
- REST API endpoints for programmatic access

📸 Screenshot
![Agentic AI Demo](images/demo_screenshot.png)

🙌 Acknowledgements
- LangGraph
- Groq
- Tavily
- Streamlit
- Hugging Face Spaces
