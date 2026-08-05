from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from rag.retriever import get_retriever
from rag.llm import get_llm

from config.prompts import RAG_PROMPT


# Format Retrieved Documents

def format_docs(docs):

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

# Retrieve Context for Evaluation

def retrieve_context(question):

    retriever = get_retriever()
    docs = retriever.invoke(
        question
    )
    return docs


# Create RAG Chain

def get_rag_chain():
    retriever = get_retriever()
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template(
        RAG_PROMPT
    )

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    ).with_config(
        run_name="RAG_Evaluation_Chain"
    )

    return rag_chain