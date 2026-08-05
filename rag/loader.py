from langchain_community.document_loaders import PyPDFLoader
import os


def load_documents(upload_dir="data/uploads"):
    documents = []
    for file in os.listdir(upload_dir):
        if file.endswith(".pdf"):
            path = os.path.join(upload_dir, file)
            loader = PyPDFLoader(path)
            documents.extend(loader.load())

    return documents