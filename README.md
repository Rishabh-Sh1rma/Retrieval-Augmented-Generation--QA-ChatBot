🤖 AI-Powered Document QA Bot
Instantly ask questions and find answers from your images or PDF documents—all in a beautiful chat UI!

🚀 What Is This Bot?
A powerful Retrieval Augmented Generation (RAG) bot that:

Takes images or PDFs as input

Extracts text using OCR

Allows you to ask questions about your documents

Returns smart, contextual answers in a chat interface

🎨 Visual Walkthrough
<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;"> <div style="flex: 1 1 320px; max-width: 350px; margin-bottom: 20px;"> <img src="https://github.com/user-attachments/assets/10b91146-f22c-443c-85d4-a869452d8465" alt="Document Upload" style="width:100%; border-radius:8px;"> <p align="center"><b>1. Upload your PDF or image</b></p> </div> <div style="flex: 1 1 320px; max-width: 350px; margin-bottom: 20px;"> <img src="https://github.com/user-attachments/assets/e9739534-d090-40dd-a240-dfc5ae2d7143" alt="OCR Extract" style="width:100%; border-radius:8px;"> <p align="center"><b>2. Extracts and processes text via OCR</b></p> </div> <div style="flex: 1 1 320px; max-width: 350px; margin-bottom: 20px;"> <img src="https://github.com/user-attachments/assets/19a379d7-8209-42d9-8a9c-ab78c57d29f4" alt="Chunking and Embedding" style="width:100%; border-radius:8px;"> <p align="center"><b>3. Smart semantic chunking and embeddings</b></p> </div> <div style="flex: 1 1 320px; max-width: 350px; margin-bottom: 20px;"> <img src="https://github.com/user-attachments/assets/5cc770ba-9efc-49d1-b595-db0840f4cbba" alt="Semantic Search" style="width:100%; border-radius:8px;"> <p align="center"><b>4. Finds the most relevant passage</b></p> </div> <div style="flex: 1 1 320px; max-width: 350px; margin-bottom: 20px;"> <img src="https://github.com/user-attachments/assets/a26f5a23-7805-4f95-80a5-d7832ba9a20d" alt="QA Result" style="width:100%; border-radius:8px;"> <p align="center"><b>5. AI-powered answer</b></p> </div> <div style="flex: 1 1 320px; max-width: 350px; margin-bottom: 20px;"> <img src="https://github.com/user-attachments/assets/90f704d9-3cb6-4557-87af-fb01aeb13ae2" alt="Chat and Followups" style="width:100%; border-radius:8px;"> <p align="center"><b>6. Chat and ask anything further!</b></p> </div> </div>
📱 Multi-Device Experience
<div style="display: flex; flex-wrap: wrap; gap: 40px; justify-content: center;"> <div style="flex: 1 1 320px; max-width: 350px; margin-bottom: 20px;"> <img src="https://github.com/user-attachments/assets/16a3c20a-ffe0-475d-9900-9458975cd9cf" alt="Mobile View" style="width:100%; border-radius:8px;"> <p align="center"><b>Mobile interface for anywhere access</b></p> </div> <div style="flex: 1 1 320px; max-width: 350px; margin-bottom: 20px;"> <img src="https://github.com/user-attachments/assets/870c3994-bcc3-44a1-bee7-5a90f56f7cee" alt="Desktop View" style="width:100%; border-radius:8px;"> <p align="center"><b>Desktop interface for productivity</b></p> </div> </div>
🛠️ How It Works: Stepwise Flow
Upload any PDF/image: Via drag-and-drop or file picker in the frontend.

OCR: Extracts text from PDFs & images using OCR.space API.

Chunk, Embed, Store: Splits text, generates semantic embeddings (sentence-transformers), and stores in a FAISS vector database.

Ask Your Question: Enter a natural-language question about your document.

Find Most Relevant Chunks: The backend performs vector search for semantic similarity.

AI Answer (or Top Chunk): Uses a free/open-source LLM or simply returns the top matching snippet as an answer.

Conversational UI: Get instant answers and ask follow-up questions, all in an interactive chat.

🌍 Why This Bot?
Save hours hunting through manuals, notes, or research PDFs

Students, professionals, and researchers can instantly query their own documents

Works 100% free: all models run locally or use open free APIs—no OpenAI, no costs, no card!

Ready for both mobile and desktop

💡 Tech Stack
Backend: Python, FastAPI, FAISS, sentence-transformers, requests

Frontend: React, Vite, Axios

OCR: OCR.space API (free)

Optional: Local LLMs (Llama-2, Phi-2, Mistral, etc.), or Hugging Face Inference API as fallback

🧩 Key Features
✔️ Upload PDFs/images (with scans or text)

✔️ Extract and process text automatically

✔️ Powerful semantic search and chunking

✔️ Chat-based Q&A over your documents (mobile & desktop)

✔️ 100% free and open source friendly

🤔 Challenges & Learnings
Transitioned from expensive APIs (OpenAI) to free/local tools

Overcame large file and dependency issues during deployment

Refined UI to balance simplicity and power for all devices

🚦 Quickstart
```
# 1. Clone the repo
git clone https://github.com/yourusername/document-qa-bot.git

# 2. Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# 3. Frontend setup
cd ../frontend
npm install
npm run dev
```
Open http://localhost:5173 in your browser to use!

🙏 Contribute & Extend
File issues, suggest features, or create Pull Requests

Try integrating more LLMs or alternative free OCR APIs

Improve responsiveness and accessibility

Add more visual cues and onboarding for new users
