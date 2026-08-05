from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings


def build_vectorstore(chunks):

    embeddings = get_embeddings()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    vectordb.persist()

    return vectordb