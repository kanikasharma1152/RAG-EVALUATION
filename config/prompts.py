RAG_PROMPT = """
You are a helpful AI assistant.

Use ONLY the provided context to answer.

If the answer is not present in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{question}

Answer:
"""