from rag.chain import get_rag_chain

# create chain
chain = get_rag_chain()

question = "What is this document about?"

response = chain.invoke(
    question
)
print("\nANSWER:")
print(response)