from .vector_store import VectorStore, get_embedding
from .document_parser import parse_document, chunk_text
from . import config
import openai

openai.api_key = config.OPENAI_API_KEY

vector_store = VectorStore(config.VECTOR_DIM)

def ingest_document(filepath):
    text = parse_document(filepath)
    chunks = chunk_text(text)
    embeddings = [get_embedding(chunk) for chunk in chunks]
    vector_store.add(embeddings, chunks)

def answer_query(query):
    q_emb = get_embedding(query)
    relevant_chunks = vector_store.search(q_emb)
    prompt = (
        "Given the following context:\n"
        + "\n".join(relevant_chunks)
        + f"\nAnswer the question: {query}"
    )
    response = openai.ChatCompletion.create(
        model=config.GPT_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
