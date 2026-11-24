# 🤖 Autonomous AI Agent

An Autonomous AI Agent built with FastAPI that can plan tasks, generate content using LLMs, and automatically create a Microsoft Word (.docx) document.

---

## 🚀 Features

- Autonomous Task Planning
- AI Content Generation
- Gemini API Integration
- Automatic Groq Fallback
- DOCX Generation
- FastAPI REST API
- Professional Logging
- Execution Time Tracking
- Error Handling

---

## 📂 Project Structure

```
autonomous_ai_agent/
│
├── api/
├── agents/
├── llm/
├── models/
├── tools/
├── utils/
├── output/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_KEY
GROQ_API_KEY=YOUR_KEY
```

---

## Run Project

```bash
uvicorn app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## API

### POST /agent

Request

```json
{
    "request":"Create a project proposal for an AI Healthcare Chatbot."
}
```

Response

```json
{
    "status":"success",
    "document":"output/generated_document.docx",
    "llm_used":"Gemini"
}
```

---

## Architecture

```
User

↓

FastAPI

↓

Planner

↓

Executor

↓

LLM Manager

↓

Gemini

↓

Groq (Fallback)

↓

DOCX Generator

↓

Word Document
```

---

## Engineering Improvement

Implemented automatic LLM fallback.

```
Gemini

↓

Fail

↓

Groq

↓

Continue
```

This improves reliability and prevents failures due to API limits or temporary service issues.

---

## Technologies Used

- Python
- FastAPI
- Gemini API
- Groq API
- python-docx
- Loguru
- Pydantic

---

## Future Improvements

- Memory
- RAG
- Multi-Agent Workflow
- Context Management
- Vector Database
- Streaming Responses

---

## Author

Purvi Jain