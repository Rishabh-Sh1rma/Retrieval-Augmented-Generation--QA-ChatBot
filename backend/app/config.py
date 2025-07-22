import os
from dotenv import load_dotenv

# Automatically load .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
GPT_MODEL = os.getenv("GPT_MODEL", "gpt-4")
VECTOR_DIM = int(os.getenv("VECTOR_DIM", "1536"))
