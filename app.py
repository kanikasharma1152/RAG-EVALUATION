import os
import pandas as pd
import streamlit as st

#Page Config

st.set_page_config(
    page_title="TechPage - RAG Evaluation",
    page_icon="🛒",
    layout="wide"
)

# Load CSS

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# Counts

documents = 0
questions = 0
results = 0

if os.path.exists("data/uploads"):
    documents = len(
        [
            f for f in os.listdir("data/uploads")
            if f.endswith(".pdf")
        ]
    )

if os.path.exists("data/goldens.csv"):
    questions = len(
        pd.read_csv("data/goldens.csv")
    )

if os.path.exists("data/results.csv"):
    results = len(
        pd.read_csv("data/results.csv")
    )

# Sidebar

with st.sidebar:

    st.title("⚙️ Configuration")

    st.subheader("🔑 API Keys")

    groq = st.text_input(
        "GROQ API Key",
        type="password",
        placeholder="gsk-..."
    )

    judge = st.text_input(
        "Judge GROQ Key (Optional)",
        type="password",
        placeholder="gsk-..."
    )

    st.divider()
    st.subheader("📦 Session Status")
    st.success("✅ Checkpoint Found")
    st.info("📚 Phase 1 Completed")
    st.divider()

    st.caption("RAGAS 0.4.3")
    st.caption("LangChain")
    st.caption("ChromaDB")
    st.caption("Groq LLM")


# Main Header

st.markdown(
    """
# 🛒 TechPage — RAG Evaluation Pipeline

Build a Retrieval-Augmented Generation (RAG) system over your document collection and evaluate it using **RAGAS**.
"""
)

st.divider()

# Metrics

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📄 Documents",
        documents
    )

with col2:
    st.metric(
        "📝 Goldens",
        questions
    )

with col3:
    st.metric(
        "📊 Results",
        results
    )

st.divider()

# Welcome Section

st.subheader("🚀 Welcome")

st.markdown("""
Use the sidebar to navigate through the complete RAG Evaluation workflow.

### Workflow

1. 📂 Upload Documents
2. 💬 Ask Questions
3. 📝 Create Goldens Dataset
4. ▶️ Run RAGAS Evaluation
5. 📊 View Evaluation Results
""")

st.info("👈 Select a page from the left sidebar to begin.")