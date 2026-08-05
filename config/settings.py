import os
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    "chroma_db"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL"
)