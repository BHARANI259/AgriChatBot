# 🌾 AgriChat – Agricultural Advisory Chatbot using RAG + LLaMA

An AI-powered agricultural assistant designed to provide intelligent farming guidance using **Retrieval-Augmented Generation (RAG)** and **LLaMA 3 via Ollama**.

The system helps users receive agricultural recommendations for:

- 🌱 Crop cultivation
- 💧 Irrigation methods
- 🌾 Soil preparation
- 🧪 Fertilizer selection
- 🐛 Pest and disease control
- 📅 Seasonal farming practices

This project combines **FastAPI + React + ChromaDB + LangChain + LLaMA** to deliver accurate and context-aware agricultural responses.

---

# 📌 Project Overview

AgriChat uses a **Retrieval-Augmented Generation (RAG)** pipeline.

Instead of relying only on an LLM, it retrieves relevant agricultural information from a custom knowledge base and generates responses grounded in retrieved content.

### Workflow

```text
User Query
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
RAG Pipeline
   ↓
Retrieve Relevant Knowledge (ChromaDB)
   ↓
Generate Response (LLaMA via Ollama)
   ↓
Return Answer
```

---

# ✨ Features

### 🤖 AI Agricultural Assistant
Provides farming recommendations using LLaMA.

### 🔍 Retrieval-Augmented Generation (RAG)
Improves response quality by retrieving domain-specific agricultural knowledge.

### 📚 Knowledge Base Support
Supports:
- Agricultural datasets
- PDF documents
- Text-based farming notes

### 🌍 Multi-language Capability
Can respond in simple Tamil when user input is in Tamil.

### ⚡ Real-Time Chat Interface
Interactive frontend built using React.

### 🖥️ Fully Local Deployment
Runs locally using Ollama without requiring cloud inference.

---

# 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | React.js |
| Backend | FastAPI |
| LLM | LLaMA 3 (Ollama) |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Framework | LangChain |
| API | REST |

---

# 📂 Project Structure

```text
Agri-chatbot/
│
├── backend/
│   ├── main.py                 # FastAPI server
│   ├── rag_pipeline.py         # RAG implementation
│   ├── model_loader.py         # Ollama integration
│   ├── generate_dataset.py     # Dataset creation
│   ├── ingest_data.py          # Vector DB ingestion
│   ├── utils.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── Chatbot.js
│   │   ├── App.js
│   │   ├── api.js
│   │   └── styles.css
│   ├── package.json
│   └── public/
│
├── data/
│   ├── agriculture_dataset.csv
│   ├── agriculture_notes.txt
│   └── agriculture_data.pdf
│
├── vector_db/
│   └── chroma.sqlite3
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/agri-chatbot.git

cd agri-chatbot
```

---

## 2. Install Ollama

Download and install:

```text
https://ollama.com/download
```

Verify installation:

```bash
ollama --version
```

Pull LLaMA model:

```bash
ollama pull llama3
```

---

## 3. Setup Backend

Move to backend:

```bash
cd backend
```

Create virtual environment:

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 4. Generate Dataset

```bash
python generate_dataset.py
```

---

## 5. Create Vector Database

```bash
python ingest_data.py
```

This step:

- Loads agricultural documents
- Generates embeddings
- Stores vectors in ChromaDB

---

## 6. Setup Frontend

Open another terminal:

```bash
cd frontend

npm install
```

---

# ▶️ Running the Application

## Start Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Start Frontend

```bash
cd frontend

npm start
```

Frontend:

```text
http://localhost:3000
```

---

# 🔌 API Endpoints

## Health Check

```http
GET /
```

Response:

```json
{
  "message": "Agricultural Advisory Chatbot API is running"
}
```

---

## Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "message": "Which fertilizer is suitable for rice?"
}
```

Response:

```json
{
  "response": "For rice cultivation..."
}
```

---

# 🧪 Example Queries

### Crop Guidance

```text
Which crop is suitable for red soil?
```

### Fertilizers

```text
Best fertilizer for rice?
```

### Irrigation

```text
How often should I irrigate maize?
```

### Pest Control

```text
How to control pests in tomato?
```

### Tamil Query

```text
நெல் பயிருக்கு எந்த உரம் பயன்படுத்தலாம்?
```

---

# 🧠 RAG Architecture

```text
Input Query
     ↓
Embedding Generation
     ↓
Similarity Search
     ↓
Retrieve Context
     ↓
Prompt Construction
     ↓
LLaMA Response Generation
```

---

# 📦 Dependencies

```text
fastapi
uvicorn
langchain
langchain-community
langchain-text-splitters
chromadb
sentence-transformers
pypdf
pandas
python-dotenv
requests
```

Install:

```bash
pip install -r requirements.txt
```

---

# 🚀 Future Enhancements

- Voice-enabled interaction
- Multilingual support
- Weather integration
- Crop disease image detection
- Mobile application
- Cloud deployment

---

# 👨‍💻 Authors

Developed as an AI + Agriculture project using:

- FastAPI
- React
- LangChain
- ChromaDB
- Ollama
- LLaMA

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star.
