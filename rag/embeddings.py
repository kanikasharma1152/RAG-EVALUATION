from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embeddings():

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding