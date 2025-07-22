# 🤖 AI-Powered Document Question Answering Bot

Welcome to the **Document QA Bot** — your intelligent assistant to **ask questions directly from your documents**! Whether it's PDFs, images, or scanned files, just upload your documents and get instant, accurate answers in natural language.

---

## 🚀 What This Bot Does

No more endless searching through documents or manual reading! This bot:

- **Ingests PDFs & images**, extracts text using OCR 📝
- **Creates semantic embeddings** for efficient search 🔍
- Uses AI-powered models to **answer your natural language queries** based on your uploaded documents 💬
- Enables a **chat-style interactive interface** for seamless user experience 💡

---

## 🎯 Problem It Solves

📚 **Extracting information from large document corpora is tedious and slow.**

- Traditional search is keyword-based and misses context.
- Reading through numerous pages is time-consuming.
- Getting precise answers quickly helps make better decisions.

This bot offers a **Rapid Retrieval-Augmented Generation (RAG)** system that combines semantic search and AI generation to make your document intelligence effortless.

---

## 🛠️ How It Was Made

This project is built with a modern tech stack combining tried-and-true and cutting-edge tools:

| Component           | Technology                      |
|---------------------|---------------------------------|
| Backend API         | Python, FastAPI                  |
| Document Parsing    | OCR.space API (free and easy)   |
| Embeddings & Search | sentence-transformers, FAISS    |
| Answer Generation   | Local LLM with llama-cpp / fallback |
| Frontend UI         | React, Vite, Axios              |

The system works by extracting text via OCR.space, converting document chunks into embeddings using sentence-transformers, storing and searching embeddings with FAISS, and answering questions by generating text through a local language model or returning the most relevant snippet.

---

## 🔧 Challenges Faced

- **Document processing diversity:** PDFs, images, scans — needed robust OCR integration.
- **Replacing costly APIs:** Transitioned from OpenAI to fully free & local ML models to avoid quota limits.
- **Large file handling:** Managed environment files and dependencies carefully to optimize deployment.
- **UI/UX design:** Created a clean, intuitive interface for both mobile and desktop users.
  
---

## 📝 Stepwise Workflow

### Step 1: Upload document  
![Upload Interface](https://github.com/user-attachments/assets/10b91146-f22c-443c-85d4-a869452d8465)  
Select PDFs or images to upload securely.

### Step 2: Extract text via OCR  
![OCR Process](https://github.com/user-attachments/assets/e9739534-d090-40dd-a240-dfc5ae2d7143)  
The backend sends files to OCR.space and extracts readable text from them.

### Step 3: Text chunking and embedding  
![Chunking and Vector Store](https://github.com/user-attachments/assets/19a379d7-8209-42d9-8a9c-ab78c57d29f4)  
Extracted text is split into manageable chunks and encoded into vector embeddings with sentence-transformers.

### Step 4: Semantic search for relevant chunks  
![Semantic relevance](https://github.com/user-attachments/assets/5cc770ba-9efc-49d1-b595-db0840f4cbba)  
When you ask a question, the bot searches the vector store to find contextually relevant chunks.

### Step 5: AI-powered answer generation  
![AI Answer Generation](https://github.com/user-attachments/assets/a26f5a23-7805-4f95-80a5-d7832ba9a20d)  
The relevant chunks are used by a local language model to craft a concise, human-readable answer.

### Step 6: Interactive Chat UI  
![Chat Interaction](https://github.com/user-attachments/assets/90f704d9-3cb6-4557-87af-fb01aeb13ae2)  
Enjoy asking follow-up questions and exploring your documents conversationally on any device.

---

## 📱 Mobile and Desktop Friendly

Featuring responsive design, this bot works smoothly on:

- **Mobile devices:**  
  ![Mobile UI](https://github.com/user-attachments/assets/16a3c20a-ffe0-475d-9900-9458975cd9cf)

- **Desktop/Laptop browsers:**  
  ![Desktop UI](https://github.com/user-attachments/assets/870c3994-bcc3-44a1-bee7-5a90f56f7cee)  

---

## ✅ Features Summary

- Easy upload of documents (PDF & images)
- OCR text extraction using a free API
- Local semantic embeddings for robust search
- AI-powered answer generation with open-source LLMs
- Clean and interactive React frontend
- Fully free/Open Source compatible workflow

---

## 🙌 Try it Yourself!

Clone the repo
git clone https://github.com/yourusername/document-qa-bot.git

Backend setup
cd backend
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend setup
cd ../frontend
npm install
npm run dev


Visit `http://localhost:5173` for frontend and start uploading documents & querying!

---

## 🤝 Contributing

Feel free to open issues or PR to improve:

- Support more file formats and OCR providers
- Integrate more powerful local or cloud LLMs
- Enhance UI responsiveness and features

---

## 📅 Last updated: July 22, 2025

---

Thank you for checking out this project! Together, let's make document understanding effortless. 🚀✨

---

# Credits

- Built by **Rishabh Sharma**  
- Powered by Open Source ML: SentenceTransformers, FAISS, llama-cpp  
- OCR by OCR.space (free API)  
- Frontend with React and Vite

---

*Images courtesy of project screenshots showing actual app in action.*  
![Screenshot 1](https://github.com/user-attachments/assets/870c3994-bcc3-44a1-bee7-5a90f56f7cee)  
![Screenshot 2](https://github.com/user-attachments/assets/16a3c20a-ffe0-475d-9900-9458975cd9cf)  
![Screenshot 3](https://github.com/user-attachments/assets/10b91146-f22c-443c-85d4-a869452d8465)  
![Screenshot 4](https://github.com/user-attachments/assets/e9739534-d090-40dd-a240-dfc5ae2d7143)  
![Screenshot 5](https://github.com/user-attachments/assets/19a379d7-8209-42d9-8a9c-ab78c57d29f4)  
![Screenshot 6](https://github.com/user-attachments/assets/5cc770ba-9efc-49d1-b595-db0840f4cbba)  
![Screenshot 7](https://github.com/user-attachments/assets/a26f5a23-7805-4f95-80a5-d7832ba9a20d)  
![Screenshot 8](https://github.com/user-attachments/assets/90f704d9-3cb6-4557-87af-fb01aeb13ae2)  
