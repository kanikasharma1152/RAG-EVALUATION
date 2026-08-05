from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vector_store import build_vectorstore


def create_vector_database():

    documents = load_documents()

    chunks = split_documents(documents)

    vectordb = build_vectorstore(chunks)

    return vectordb