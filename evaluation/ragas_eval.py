import os
from dotenv import load_dotenv
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper


load_dotenv()
def run_ragas(dataset):

    # Check GROQ API Key

    groq_key = os.getenv(
        "GROQ_API_KEY"
    )

    if not groq_key:
        raise ValueError(
            "❌ GROQ_API_KEY not found in .env file"
        )
    
    # Evaluation LLM

    groq_llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=groq_key,
        temperature=0,
        timeout=120,
        max_retries=5,
        name="RAGAS_Judge_LLM"
    )

    evaluator_llm = LangchainLLMWrapper(
        groq_llm
    )

    # Evaluation Embeddings

    embeddings = HuggingFaceEmbeddings(
        model_name=
        "sentence-transformers/all-MiniLM-L6-v2"

    )

    evaluator_embeddings = LangchainEmbeddingsWrapper(
        embeddings
    )

    # Run RAGAS

    result = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall
        ],
        llm=evaluator_llm,
        embeddings=evaluator_embeddings,
        raise_exceptions=False
    )
    return result