🚀 AI-Powered Requirement Engineering & Documentation Automation Platform

📌 Overview
The AI-Powered Requirement Engineering & Documentation Automation Platform automates the software requirement engineering process using Generative AI and Multi-Agent Systems.

The platform converts raw business requirements into structured software engineering artifacts such as:

Requirement Analysis
Ambiguity Detection Reports
User Stories
Use Cases
Software Requirements Specification (SRS)
PDF & DOCX Documentation

The system leverages LangGraph, LangChain, Groq LLMs, FastAPI, Streamlit, SQLite, and FAISS to automate requirement analysis and documentation generation.

✨ Key Features
Automated Requirement Analysis
Ambiguity Detection
User Story Generation
Use Case Generation
SRS Generation
PDF Export
DOCX Export
RAG-based Question Answering
Project Storage using SQLite
Multi-Agent Workflow using LangGraph
🛠️ Technology Stack
Python
FastAPI
Streamlit
LangChain
LangGraph
Groq (Llama 3)
SQLite
FAISS
ReportLab
python-docx

🚀 How to Run
Install Dependencies;

pip install -r requirements.txt

Configure Environment Variables;

Create a .env file:

GROQ_API_KEY=your_api_key

Start Backend;

uvicorn api.main --reload

Start Frontend;

streamlit run streamlit_ui/app_ui.py

📊 Outputs Generated
Requirement Analysis
Ambiguity Report
User Stories
Use Cases
SRS Document
PDF Export
DOCX Export

🔮 Future Enhancements
Authentication & Authorization
Docker Containerization
Cloud Deployment
PostgreSQL Integration
CI/CD Pipelines
Requirement Versioning
Multi-Language Support
Collaborative Editing


🏗️ System Architecture

                 User
                   │
                   ▼
        ┌──────────────────┐
        │   Streamlit UI   │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ FastAPI Backend  │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ LangGraph Engine │
        └────────┬─────────┘
                 │
 ┌───────────────┼────────────────┐
 ▼               ▼                ▼
Requirement   User Story      Use Case
Analyzer      Generator       Generator
 Agent          Agent           Agent
 │
 ▼
Ambiguity Detector
 │
 ▼
SRS Generator
 │
 ▼
PDF / DOCX Export
 │
 ▼
SQLite Database
 │
 ▼
FAISS Vector Store
 │
 ▼
RAG Question Answering
```
