import streamlit as st
from rag.chain import get_rag_chain, retrieve_context

st.set_page_config(
    page_title="Ask Questions",
    page_icon="💬",
    layout="wide"
)
st.title("💬 Ask Questions")
st.write(
    "Ask questions about your uploaded documents."
)
st.divider()
question = st.text_area(
    "Enter your question",
    placeholder="Example: What is the return policy?"
)
if st.button("🚀 Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Generating answer..."):

        try:
            chain = get_rag_chain()
            answer = chain.invoke(question)
            context = retrieve_context(question)
            st.success("Answer Generated")
            st.subheader("🤖 Answer")
            st.write(answer)
            with st.expander("📄 Retrieved Context"):
                for i, doc in enumerate(context, start=1):
                    st.markdown(f"### Chunk {i}")
                    st.write(doc.page_content)
        except Exception as e:
            st.error(str(e))