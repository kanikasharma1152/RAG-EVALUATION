from langchain_community.vectorstores import Chroma
from config.settings import CHROMA_PATH
from rag.embeddings import get_embeddings


def get_retriever():

    print("Retriever Step 1")

    embeddings = get_embeddings()

    print("Retriever Step 2")

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    print("Retriever Step 3")

    retriever = db.as_retriever(
        search_kwargs={"k": 3}
    )

    print("Retriever Step 4")

    return retriever