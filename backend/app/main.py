from fastapi import FastAPI, UploadFile, File, Form
import os
from .rag_pipeline import ingest_document, answer_query

app = FastAPI()

# Create "uploads" directory inside backend/app if it doesn't exist
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        f.write(await file.read())
    ingest_document(filepath)
    return {"message": "Document ingested"}

@app.post("/query/")
async def query(question: str = Form(...)):
    answer = answer_query(question)
    return {"answer": answer}
