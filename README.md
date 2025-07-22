# 🤖 AI-Powered Document QA Bot

Instantly ask questions and find answers from your images or PDF documents — all in a beautiful chat UI!
<img width="1588" height="505" alt="image" src="https://github.com/user-attachments/assets/ce90238f-835b-4060-9810-75136fbf9710" />


---

## 🚀 What Is This Bot?

A powerful Retrieval Augmented Generation (RAG) bot that:

- Takes images or PDFs as input
- Extracts text using OCR
- Allows you to ask questions about your documents
- Returns smart, contextual answers in a chat interface

---

## 🎨 Visual Walkthrough

<p align="center">
  <img src="https://github.com/user-attachments/assets/10b91146-f22c-443c-85d4-a869452d8465" alt="Upload" width="150" />
  <img src="https://github.com/user-attachments/assets/e9739534-d090-40dd-a240-dfc5ae2d7143" alt="OCR" width="150" />
  <img src="https://github.com/user-attachments/assets/19a379d7-8209-42d9-8a9c-ab78c57d29f4" alt="Chunking" width="150" />
  <img src="https://github.com/user-attachments/assets/5cc770ba-9efc-49d1-b595-db0840f4cbba" alt="Search" width="150" />
  <img src="https://github.com/user-attachments/assets/a26f5a23-7805-4f95-80a5-d7832ba9a20d" alt="Answer" width="150" />
<!--   <img src="https://github.com/user-attachments/assets/90f704d9-3cb6-4557-87af-fb01aeb13ae2" alt="Chat" width="150" /> -->
</p>
---

## 🛠️ How It Works

1. **Upload a PDF or Image**  
   Drag and drop or use the file picker

2. **OCR**  
   Uses the free OCR.space API to extract text

3. **Chunk + Embed + Store**  
   Splits text into chunks, generates semantic embeddings with Sentence-Transformers, and stores them in a FAISS vector DB

4. **Ask a Question**  
   Input a question in natural language

5. **Semantic Search**  
   Backend finds the most relevant chunks

6. **Answering**  
   Uses a free or local LLM to answer (or just returns top chunks)

7. **Chat UI**  
   Fully conversational — ask follow-ups in a clean UI

---

## 🌍 Why This Bot?

- Save hours hunting through documents, manuals, research papers
- Students, professionals, researchers — anyone can use it
- Runs fully locally or with free APIs — no cost, no OpenAI needed
- Responsive: works well on mobile & desktop

---

## 💡 Tech Stack

- **Backend**: Python, FastAPI, FAISS, SentenceTransformers, OCR.space API
- **Frontend**: React, Vite, Axios
- **Optional**: Local LLMs (Llama-2, Phi-2, Mistral) or HuggingFace Inference APIs

---

## 🧩 Key Features

- ✔️ Upload PDFs or images
- ✔️ Auto OCR + Text Extraction
- ✔️ Semantic chunking + vector DB
- ✔️ Natural-language Q&A
- ✔️ 100% free and open-source friendly

---

## 🤔 Challenges & Learnings

- Migrated from expensive APIs to open-source + free APIs
- Overcame large dependency and deployment issues
- Refined mobile UI for real-world usage

---

## 🚦 Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/Rishabh-Sh1rma/Retrieval-Augmented-Generation--QA-ChatBot.git

# 2. Backend setup
cd backend
python -m venv venv
venv\Scripts\activate   # (on Windows)
pip install -r requirements.txt
uvicorn app.main:app --reload

# 3. Frontend setup
cd ../frontend
npm install
npm run dev
