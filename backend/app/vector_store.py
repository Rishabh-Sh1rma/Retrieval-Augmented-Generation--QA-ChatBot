import faiss
import numpy as np
from openai import OpenAI
from . import config

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.chunks = []

    def add(self, embeddings, chunks):
        self.index.add(np.array(embeddings).astype(np.float32))
        self.chunks.extend(chunks)

    def search(self, embedding, top_k=3):
        D, I = self.index.search(np.array([embedding]).astype(np.float32), top_k)
        return [self.chunks[i] for i in I[0]]


def get_embedding(text):
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    response = client.embeddings.create(input=[text], model=config.EMBEDDING_MODEL)
    return response['data'][0]['embedding']
